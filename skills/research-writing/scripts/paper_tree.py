"""Paper Intent Markdown v3: readable intent trees, separate drafts, review and evaluation.

Python standard library only. A linter is not a scientific reviewer or an identity verifier.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from datetime import datetime, timezone
from urllib.parse import unquote, urlsplit, urlunsplit

LEVELS = {'architecture': {'paper', 'section', 'subsection'},
          'paragraphs': {'paper', 'section', 'subsection', 'paragraph'},
          'sentences': {'paper', 'section', 'subsection', 'paragraph', 'sentence'}}
KINDS = set(LEVELS['sentences'])
RELATIONS = {'introduce', 'elaborate', 'support', 'contrast', 'consequence', 'qualify',
             'example', 'transition', 'synthesize'}
CLAIMS = {'observation', 'method', 'inference', 'hypothesis', 'definition', 'background', 'transition'}
STATES = {'unassessed', 'located', 'missing', 'conflicting'}
MODES = {'compose', 'reverse-analysis'}
NONPLAN = {'prose', 'blocks', 'evidence', 'evidence_state', 'claim_type', 'tasks', 'numeric_facts',
           'execution', 'status', 'notes'}
HEADER = re.compile(r'^(#{1,6}) \[([A-Za-z][A-Za-z0-9_-]*)\] (.+)$')

def digest(data):
    return hashlib.sha256(data).hexdigest()

def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))

def read_json(path, default=None):
    path = Path(path)
    if not path.exists() and default is not None:
        return default
    return json.loads(path.read_text(encoding='utf-8-sig'))

def write_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

SENTENCE = re.compile(r'^- \[([A-Za-z][A-Za-z0-9_-]*)\] (.+)$')
SOURCE = re.compile(r'^(?:\[原文\]\((https?://[^ ]+)\)|(?:DOI|来源|Source)[：:]\s*(\S+))$')
NODE_DATA = {'depends_on', 'uses', 'introduces', 'relation', 'claim_type',
             'evidence_state', 'evidence', 'tasks', 'numeric_facts', 'execution',
             'status', 'notes'}
PROJECT_DATA = {'mode', 'language', 'maturity', 'basis', 'known_terms', 'node_data'}

BLOCK_START = re.compile(r'^<!-- block ([A-Za-z][A-Za-z0-9_-]*) type=(equation|figure|table) after=([A-Za-z][A-Za-z0-9_-]*) -->$')
IMAGE = re.compile(r'!\[[^\]\n]*\]\((<[^>\n]+>|[^\s)]+)(\s+[^)]+)?\)')

def local_images(content, parent):
    for match in IMAGE.finditer(content):
        target = match[1].strip('<>')
        parts = urlsplit(target)
        if not parts.scheme and not parts.netloc and parts.path:
            yield Path(parent) / unquote(parts.path)

def read_draft(path, known_ids):
    """Read sentence prose and ordered, sentence-anchored Markdown blocks."""
    path = Path(path)
    if not path.exists():
        return {}, []
    sentences, blocks, block_ids, current, active = {}, [], set(), None, None
    for line_no, line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(), 1):
        if active is not None:
            if line == '<!-- /block -->':
                content = '\n'.join(active.pop('_lines')).strip('\n')
                if not content.strip():
                    raise ValueError('Empty draft block ' + active['id'])
                active['content'] = content
                blocks.append(active)
                active, current = None, None
            elif BLOCK_START.fullmatch(line):
                raise ValueError(f'Nested draft block at line {line_no}')
            else:
                active['_lines'].append(line)
            continue
        block = BLOCK_START.fullmatch(line)
        if block:
            bid, kind, anchor = block.groups()
            if bid in block_ids or bid in known_ids:
                raise ValueError('Duplicate/conflicting draft block ID: ' + bid)
            if anchor not in sentences:
                raise ValueError('Draft block must follow a filled sentence: ' + anchor)
            block_ids.add(bid)
            active = {'id': bid, 'type': kind, 'after': anchor, '_lines': []}
            current = None
            continue
        match = SENTENCE.fullmatch(line)
        if match:
            nid, prose = match.groups()
            if nid not in known_ids:
                raise ValueError(f'Unknown draft sentence ID {nid} at line {line_no}')
            if nid in sentences:
                raise ValueError(f'Duplicate draft sentence ID {nid} at line {line_no}')
            if not prose.strip():
                raise ValueError(f'Empty draft sentence {nid} at line {line_no}')
            sentences[nid], current = prose.strip(), nid
        elif not line.strip() or re.match(r'^#{1,6} ', line):
            current = None
        elif line[:1].isspace() and current:
            sentences[current] += ' ' + line.strip()
        else:
            raise ValueError(f'Draft must use - [S-ID] prose entries at line {line_no}')
    if active is not None:
        raise ValueError('Unclosed draft block: ' + active['id'])
    return sentences, blocks

def draft_data(path, known_ids):
    """Compatibility API: return sentence prose only."""
    return read_draft(path, known_ids)[0]

def parse(path, project=None, draft=None):
    path = Path(path)
    raw = path.read_bytes()
    nodes, current, stack, source_url = [], None, [], None
    for line_no, line in enumerate(raw.decode('utf-8-sig').splitlines(), 1):
        match = HEADER.fullmatch(line)
        if match:
            depth, nid, title = len(match[1]), match[2], match[3].strip()
            if not title:
                raise ValueError(f'Empty heading title at line {line_no}')
            if nid.startswith('S-'):
                raise ValueError(f'Sentence intentions use list entries at line {line_no}')
            kind = 'paper' if depth == 1 else ('paragraph' if nid.startswith('PAR-') else
                                               ('section' if depth == 2 else 'subsection'))
            while stack and stack[-1]['_depth'] >= depth:
                stack.pop()
            if depth != len(stack) + 1:
                raise ValueError(f'Heading skips a level at line {line_no}')
            current = {'id': nid, 'title': title, 'kind': kind,
                       'parent': stack[-1]['id'] if stack else None,
                       'intent': title if kind == 'paragraph' else '',
                       '_depth': depth, '_line': line_no}
            nodes.append(current)
            stack.append(current)
        elif SENTENCE.fullmatch(line):
            match = SENTENCE.fullmatch(line)
            nid, intent = match.groups()
            if not intent.strip():
                raise ValueError(f'Empty sentence intention at line {line_no}')
            intent = intent.strip()
            if not current or current['kind'] != 'paragraph':
                raise ValueError(f'Sentence entry needs a paragraph heading at line {line_no}')
            if not nid.startswith('S-'):
                raise ValueError(f'Sentence ID must begin S- at line {line_no}')
            nodes.append({'id': nid, 'title': intent, 'intent': intent, 'kind': 'sentence',
                          'parent': current['id'], '_depth': min(current['_depth'] + 1, 6),
                          '_line': line_no})
        elif line.startswith(('概述：', '论证顺序：')):
            if current is None or current['kind'] == 'paragraph':
                raise ValueError(f'Paragraph intention belongs in its heading at line {line_no}')
            field = 'intent' if line.startswith('概述：') else 'logic'
            if field == 'intent' and current.get('intent') or field == 'logic' and field in current:
                raise ValueError(f'Duplicate {field} at line {line_no}')
            current[field] = line.split('：', 1)[1].strip()
            if not current[field]:
                raise ValueError(f'Empty {field} at line {line_no}')
        elif SOURCE.fullmatch(line):
            if len(nodes) != 1 or nodes[0]['kind'] != 'paper' or source_url:
                raise ValueError(f'One source line belongs below the root at line {line_no}')
            match = SOURCE.fullmatch(line)
            source_url = match[1] or match[2]
        elif not line.strip():
            continue
        else:
            raise ValueError(f'Unexpected tree text at line {line_no}; keep prose and metadata in sidecars')
    project_path = Path(project) if project else path.with_name('project.json')
    state = read_json(project_path, {})
    if not isinstance(state, dict) or set(state) - PROJECT_DATA:
        raise ValueError('project.json must contain only mode, language, maturity, basis, known_terms and node_data')
    meta = {'format': 'paper-intent/3', 'mode': 'reverse-analysis' if source_url else 'compose',
            'language': 'en', 'maturity': 'developing', 'basis': [], 'known_terms': []}
    meta.update({k: v for k, v in state.items() if k != 'node_data'})
    if source_url:
        meta['source_url'] = source_url
    lookup = {n['id']: n for n in nodes}
    node_data = state.get('node_data', {})
    if not isinstance(node_data, dict):
        raise ValueError('node_data must be an ID-to-object map')
    for nid, fields in node_data.items():
        if nid not in lookup:
            raise ValueError('Unknown node_data ID: ' + nid)
        if not isinstance(fields, dict) or set(fields) - NODE_DATA:
            raise ValueError('Invalid node_data fields for ' + nid + '; tree identity and intentions stay in Markdown')
        lookup[nid].update(fields)
    draft_path = Path(draft) if draft else path.with_name('draft.md')
    prose, blocks = read_draft(draft_path, {n['id'] for n in nodes if n['kind'] == 'sentence'})
    if any(block['id'] in lookup for block in blocks):
        raise ValueError('Draft block IDs must differ from tree IDs')
    for nid, text in prose.items():
        lookup[nid]['prose'] = text
    for block in blocks:
        lookup[block['after']].setdefault('blocks', []).append(block)
    return {'path': path, 'raw': raw, 'meta': meta, 'nodes': nodes,
            'project_path': project_path, 'draft_path': draft_path}

def index(doc):
    return {n['id']: n for n in doc['nodes']}

def mode(doc):
    return doc['meta'].get('mode', 'compose')

def ancestor_nodes(doc, scope):
    lookup, result, seen = index(doc), [], set()
    parent = lookup[scope].get('parent')
    while parent is not None:
        if parent not in lookup or parent in seen:
            raise ValueError('Invalid ancestor path for scope: ' + scope)
        seen.add(parent)
        result.insert(0, lookup[parent])
        parent = lookup[parent].get('parent')
    return result

def descendants(doc, scope):
    ids, result = {scope}, []
    for n in doc['nodes']:
        if n['id'] == scope or n.get('parent') in ids:
            result.append(n)
            ids.add(n['id'])
    if not result:
        raise ValueError('Unknown scope: ' + scope)
    return result

def issue(code, node, message, severity='blocker'):
    return {'code': code, 'node': node, 'severity': severity, 'message': message}

def validate(doc, level='sentences', scope=None):
    errors, seen, stack, edges = [], {}, [], {}
    nodes = doc['nodes']
    roots = [n for n in nodes if n.get('kind') == 'paper' and n.get('parent') is None]
    if len(roots) != 1 or not nodes or nodes[0] not in roots:
        errors.append(issue('root', None, 'Exactly one leading paper root required'))
    if sum(n.get('kind') == 'paper' for n in nodes) != 1:
        errors.append(issue('paper_count', None, 'Exactly one paper node permitted; nested papers are invalid'))
    if mode(doc) not in MODES:
        errors.append(issue('mode', None, 'mode must be compose or reverse-analysis'))
    if not isinstance(doc['meta'].get('language'), str) or not doc['meta']['language'].strip():
        errors.append(issue('language', None, 'language is required'))
    if not isinstance(doc['meta'].get('known_terms', []), list):
        errors.append(issue('known_terms', None, 'known_terms must be an array'))
    if not isinstance(doc['meta'].get('basis', []), list) or not all(isinstance(x, str) and x.strip() for x in doc['meta'].get('basis', [])):
        errors.append(issue('basis', None, 'Declared basis must be an array of nonempty strings'))
    if not isinstance(doc['meta'].get('maturity'), str):
        errors.append(issue('maturity', None, 'maturity is required'))
    allowed_children = {'paper': {'section'}, 'section': {'subsection', 'paragraph'},
                        'subsection': {'subsection', 'paragraph'}, 'paragraph': {'sentence'}, 'sentence': set()}
    selected_ids = {n['id'] for n in descendants(doc, scope)} if scope else {n['id'] for n in nodes}
    for n in nodes:
        nid, kind, parent = n['id'], n.get('kind'), n.get('parent')
        if nid in seen:
            errors.append(issue('duplicate_id', nid, 'IDs must be unique'))
        if kind not in KINDS:
            errors.append(issue('kind', nid, 'Unknown node kind'))
        if not isinstance(n.get('intent'), str) or not n['intent'].strip():
            errors.append(issue('intent', nid, 'Nonempty intention required'))
        for field in ('depends_on', 'uses', 'introduces', 'evidence', 'tasks'):
            value = n.get(field, [])
            if not isinstance(value, list) or not all(isinstance(x, str) for x in value) or len(value) != len(set(value)):
                errors.append(issue('array', nid, field + ' must contain unique string IDs'))
        if kind == 'paper':
            if parent is not None or n is not nodes[0]:
                errors.append(issue('paper_root', nid, 'The paper must be the leading root with parent null'))
            stack = [nid]
        else:
            if parent not in seen or parent not in stack:
                errors.append(issue('parent_order', nid, 'Parent must precede child in a contiguous preorder subtree'))
            else:
                stack = stack[:stack.index(parent) + 1] + [nid]
                if kind not in allowed_children.get(seen[parent].get('kind'), set()):
                    errors.append(issue('hierarchy', nid, 'Invalid child kind for parent'))
                edges.setdefault(parent, []).append(nid)
        if n['_depth'] != min(len(stack), 6):
            errors.append(issue('heading_depth', nid, 'Heading depth must project the parent depth, capped at six'))
        if kind == 'sentence' and 'relation' in n and n['relation'] not in RELATIONS:
            errors.append(issue('relation', nid, 'Unknown declared sentence relation'))
        if kind != 'sentence' and n.get('prose'):
            errors.append(issue('branch_prose', nid, 'Prose belongs only to sentence leaves'))
        seen[nid] = n
    if not any(n.get('kind') == 'section' for n in nodes):
        errors.append(issue('sections', None, 'At least one section required'))
    for n in nodes:
        if n['id'] not in edges and n['id'] in selected_ids:
            permitted = {'architecture': {'section', 'subsection', 'paragraph', 'sentence'},
                         'paragraphs': {'paragraph', 'sentence'}, 'sentences': {'sentence'}}[level]
            if n.get('kind') not in permitted:
                errors.append(issue('unexpanded', n['id'], 'Terminal kind is incomplete at ' + level))
        if isinstance(n.get('depends_on', []), list):
            for dep in n.get('depends_on', []):
                if dep not in seen:
                    errors.append(issue('dependency_ref', n['id'], 'Unknown prerequisite: ' + str(dep)))
    active, done = set(), set()
    def visit(nid):
        if nid in active:
            return True
        if nid in done:
            return False
        active.add(nid)
        for dep in seen[nid].get('depends_on', []):
            if isinstance(dep, str) and dep in seen and visit(dep):
                return True
        active.remove(nid)
        done.add(nid)
        return False
    if not any(e['code'] == 'array' for e in errors) and any(visit(nid) for nid in seen):
        errors.append(issue('dependency_cycle', None, 'Logical prerequisites must be acyclic'))
    return errors

def projected_nodes(doc, scope, level, stage='outline'):
    """Relevant scope plus ancestors and transitive prerequisites, in file order.

    An explicit prerequisite to a branch includes its relevant descendants. This
    retains evidence/prose changes to a depended-on argument without binding
    every unrelated source or lower-level prose during outline review.
    """
    selected = [n for n in descendants(doc, scope) if n.get('kind') in LEVELS[level]]
    selected_ids = {n['id'] for n in selected}
    contextual = {n['id'] for n in ancestor_nodes(doc, scope)}
    lookup = index(doc)
    queue = selected + [lookup[nid] for nid in contextual]
    visited = set()
    while queue:
        n = queue.pop()
        if n['id'] in visited:
            continue
        visited.add(n['id'])
        for dep in n.get('depends_on', []):
            if dep not in lookup:
                raise ValueError('Unknown prerequisite: ' + str(dep))
            relevant = [x for x in descendants(doc, dep) if x.get('kind') in LEVELS[level]]
            relevant += ancestor_nodes(doc, dep)
            for x in relevant:
                if x['id'] not in selected_ids:
                    contextual.add(x['id'])
                queue.append(x)
    def project(n):
        return {k: v for k, v in n.items() if not k.startswith('_') and
                (k not in NONPLAN or (stage == 'draft' and k in
                 {'prose', 'blocks', 'evidence', 'evidence_state', 'claim_type', 'numeric_facts'}))}
    return {'nodes': [project(n) for n in selected],
            'context': [project(n) for n in doc['nodes'] if n['id'] in contextual and n['id'] not in selected_ids]}

def context_meta(doc, projection):
    terms = {term for n in projection['nodes'] + projection['context']
             for field in ('uses', 'introduces') for term in n.get(field, [])}
    return {**{k: doc['meta'][k] for k in ('mode', 'language', 'basis', 'source_url') if k in doc['meta']},
            'known_terms': [term for term in doc['meta'].get('known_terms', []) if term in terms]}

def plan_hash(doc, scope, level):
    projection = projected_nodes(doc, scope, level)
    meta = context_meta(doc, projection)
    payload = {'meta': meta, 'nodes': projection['nodes']}
    # Preserve existing whole-paper review hashes if the review has no external
    # context. Legacy scoped records intentionally become stale rather than
    # silently imply approval of previously unhashed ancestor/dependency changes.
    if projection['context']:
        payload['context'] = projection['context']
    return digest(canonical(payload).encode('utf-8'))

def gate(doc, reviews, scope=None):
    if mode(doc) == 'reverse-analysis':
        return {'ok': False, 'errors': [issue('reverse_readonly', scope,
                'Reverse analysis cannot approve or gate manuscript composition')],
                'required': [], 'valid': [], 'stale': [], 'missing': []}
    scope = scope or (doc['nodes'][0]['id'] if doc['nodes'] else '')
    errors = validate(doc, 'sentences', scope)
    if errors:
        return {'ok': False, 'errors': errors, 'required': [], 'valid': [], 'stale': []}
    roots = [n for n in doc['nodes'] if n['kind'] == 'paper']
    root = roots[0]['id']
    selected = descendants(doc, scope)
    if selected[0]['kind'] == 'sentence':
        return {'ok': False, 'errors': [issue('review_scope', scope,
                'Use its paragraph as composition scope to retain sentence order')],
                'required': [], 'valid': [], 'stale': [], 'missing': []}
    sections = [n['id'] for n in selected if n['kind'] == 'section']
    ancestors = ancestor_nodes(doc, scope)
    if scope != root and not sections:
        sections = [n['id'] for n in ancestors if n['kind'] == 'section']
    architecture_scope = root if scope == root else sections[0]
    records = read_json(reviews, {'items': []}).get('items', [])
    valid, stale = [], []
    latest = {}
    for position, row in enumerate(records):
        latest[(row.get('scope'), row.get('level'))] = (position, row)
    for position, row in latest.values():
        receipt_scope, level = row.get('scope'), row.get('level')
        if row.get('decision') != 'approved':
            continue
        if level not in LEVELS or receipt_scope not in index(doc) or row.get('by') != 'human' or not all(row.get(k) for k in ('source', 'reference', 'recorded_at')):
            stale.append({'scope': receipt_scope, 'level': level, 'reason': 'invalid/missing approval provenance'})
        elif row.get('plan_hash') == plan_hash(doc, receipt_scope, level):
            valid.append(dict(row, _position=position))
        else:
            stale.append({'scope': receipt_scope, 'level': level, 'reason': 'intent projection changed'})
    required = [{'scope': architecture_scope, 'level': 'architecture'}]
    paragraph_scopes = sections if scope == root or selected[0]['kind'] == 'section' else [scope]
    required += [{'scope': s, 'level': 'paragraphs'} for s in paragraph_scopes]
    # A sentence plan is reviewed in paragraph batches. An approved broader
    # scope can cover several batches; smaller receipts need no invented union.
    required += [{'scope': n['id'], 'level': 'sentences'} for n in selected if n['kind'] == 'paragraph']
    missing = []
    for req in required:
        candidates = [r for r in valid if r['level'] == req['level'] and req['scope'] in {n['id'] for n in descendants(doc, r['scope'])}]
        required_ids = {n['id'] for n in descendants(doc, req['scope'])}
        denials = [(pos, r) for pos, r in latest.values() if r.get('decision') == 'changes-required' and r.get('level') == req['level'] and r.get('scope') in index(doc) and required_ids.intersection(n['id'] for n in descendants(doc, r['scope']))]
        newest_approval = max((r['_position'] for r in candidates), default=-1)
        if not candidates or any(pos > newest_approval for pos, _ in denials):
            missing.append(req)
    return {'ok': not errors and not missing, 'scope': scope, 'errors': errors, 'required': required,
            'valid': [{'scope': r['scope'], 'level': r['level']} for r in valid], 'stale': stale, 'missing': missing}

def evidence_data(doc, path=None):
    path = Path(path) if path else doc['path'].with_name('evidence.json')
    data = read_json(path, {'items': []})
    items = data.get('items', [])
    if not isinstance(items, list) or any(not isinstance(x, dict) for x in items):
        raise ValueError('evidence items must be objects')
    if len({x.get('id') for x in items}) != len(items):
        raise ValueError('Duplicate evidence IDs')
    return path, {x['id']: x for x in items}

def adjacent_nodes(doc, scope):
    """Immediate sibling roots at the chosen scope, not unrelated branches."""
    lookup = index(doc)
    siblings = [n for n in doc['nodes'] if n.get('parent') == lookup[scope].get('parent')]
    position = next(i for i, n in enumerate(siblings) if n['id'] == scope)
    return siblings[max(0, position - 1):position] + siblings[position + 1:position + 2]

def audit_projection(doc, scope, level, stage):
    # Human planning receipts intentionally retain projected_nodes semantics.
    # Evaluation additionally binds the neighboring argument being assessed.
    content_level = 'sentences' if stage == 'draft' else level
    projection = projected_nodes(doc, scope, content_level, stage)
    present = {n['id'] for n in projection['nodes'] + projection['context']}
    for neighbor in adjacent_nodes(doc, scope):
        extra = projected_nodes(doc, neighbor['id'], content_level, stage)
        for n in extra['nodes'] + extra['context']:
            if n['id'] not in present:
                projection['context'].append(n)
                present.add(n['id'])
    order = {n['id']: i for i, n in enumerate(doc['nodes'])}
    projection['context'].sort(key=lambda n: order[n['id']])
    return projection

def protect_output(doc, out, evidence=None, reviews=None, audit=None, review_write=False):
    """Reject aliases of authoritative inputs before creating or writing output."""
    target = Path(out)
    protected = [doc['path'], doc['project_path'], doc['draft_path']]
    registry, records = evidence_data(doc, evidence)
    protected.append(registry)
    protected.extend(registry.parent / row['path'] for row in records.values() if row.get('path'))
    protected.extend(doc['path'].parent / value for value in doc['meta'].get('basis', [])
                     if Path(value).is_absolute() or not urlsplit(value).scheme)
    for n in doc['nodes']:
        for block in n.get('blocks', []):
            protected.extend(local_images(block['content'], doc['draft_path'].parent))
    if not review_write:
        protected.extend([doc['path'].with_name('reviews.json'),
                          doc['path'].parent / 'review' / 'reviews.json',
                          doc['path'].parent.parent / 'review' / 'reviews.json'])
        if reviews:
            protected.append(Path(reviews))
    if audit:
        protected.append(Path(audit))
    for source in protected:
        if target.resolve() == source.resolve() or (target.exists() and source.exists() and target.samefile(source)):
            raise ValueError('Output would overwrite an input: ' + str(source))

def binding(doc, stage, level, scope, evidence=None):
    if stage == 'draft':
        path, records = evidence_data(doc, evidence)
    else:
        path, records = doc['path'].with_name('evidence.json'), {}
    projection = audit_projection(doc, scope, level, stage)
    referenced = {eid for n in projection['nodes'] + projection['context'] for eid in n.get('evidence', [])}
    records = {eid: item for eid, item in records.items() if eid in referenced}
    local = {}
    if stage == 'draft':
        for eid, item in records.items():
            if item.get('path'):
                source = path.parent / item['path']
                local[eid] = digest(source.read_bytes()) if source.is_file() else None
        for n in projection['nodes'] + projection['context']:
            for block in n.get('blocks', []):
                for source in local_images(block['content'], doc['draft_path'].parent):
                    local['block:' + block['id'] + ':' + str(source.resolve())] = digest(source.read_bytes()) if source.is_file() else None
    meta = context_meta(doc, projection)
    return {'binding_version': 3,
            'scope_sha256': digest(canonical({'meta': meta, **projection}).encode('utf-8')),
            'stage': stage, 'level': level, 'scope': scope,
            'evidence_registry_sha256': digest(canonical(records).encode('utf-8')) if stage == 'draft' else None,
            'local_evidence_sha256': local}

def evidence_checks(doc, scope, evidence=None):
    path, records = evidence_data(doc, evidence)
    errors, eligible, traceable = [], 0, 0
    for n in descendants(doc, scope):
        if n.get('kind') != 'sentence' or not n.get('prose') or (n.get('claim_type') == 'transition' and not n.get('blocks')):
            continue
        eligible += 1
        refs = n.get('evidence', [])
        before = len(errors)
        if n.get('claim_type') not in CLAIMS:
            errors.append(issue('claim_type', n['id'], 'Written sentence needs claim_type in project node_data'))
        if n.get('evidence_state') not in STATES:
            errors.append(issue('evidence_state', n['id'], 'Written sentence needs evidence_state in project node_data'))
        if not refs or n.get('evidence_state') != 'located':
            errors.append(issue('unresolved_assertion', n['id'], 'Written assertion must have located grounding; unresolved prose stays empty'))
        for eid in refs:
            item = records.get(eid)
            if not item:
                errors.append(issue('evidence_ref', n['id'], 'Unknown evidence: ' + eid))
                continue
            if not all(item.get(k) for k in ('id', 'kind', 'locator', 'checked_by', 'checked_at')) or not (item.get('path') or item.get('url')):
                errors.append(issue('evidence_metadata', n['id'], 'Incomplete provenance fields for ' + eid, 'major'))
            if item.get('path'):
                source = path.parent / item['path']
                if not source.is_file():
                    errors.append(issue('missing_artifact', n['id'], 'Missing local source: ' + eid))
                elif not item.get('sha256'):
                    errors.append(issue('missing_hash', n['id'], 'Local source needs checked version hash: ' + eid, 'major'))
                elif digest(source.read_bytes()) != item['sha256']:
                    errors.append(issue('stale_artifact', n['id'], 'Local source changed since registration: ' + eid))
        for fact in n.get('numeric_facts', []):
            content = n['prose'] + '\n' + '\n'.join(b['content'] for b in n.get('blocks', []))
            if not isinstance(fact, dict) or not isinstance(fact.get('literal'), str) or fact['literal'] not in content or fact.get('evidence') not in refs or not fact.get('locator'):
                errors.append(issue('numeric_mapping', n['id'], 'Invalid declared numeric-fact mapping', 'major'))
        for block in n.get('blocks', []):
            for source in local_images(block['content'], doc['draft_path'].parent):
                if not source.is_file():
                    errors.append(issue('missing_block_asset', n['id'], 'Missing local image in ' + block['id'] + ': ' + str(source)))
        if len(errors) == before:
            traceable += 1
    return errors, {'numerator': traceable, 'denominator': eligible, 'rate': traceable / eligible if eligible else None,
                    'meaning': 'Declared traceability only; semantic support requires actual source review'}

def audit_units(doc, stage, level, scope):
    selected = [n for n in descendants(doc, scope) if n.get('kind') in LEVELS[level]]
    units, children = [], {}
    def add(dim, key, ids, block=None):
        unit = {'key': dim + ':' + key, 'dimension': dim, 'nodes': ids,
                      'score': None, 'quote': '', 'reason': '',
                      'consequence': '', 'repair': '', 'close_criterion': ''}
        if block:
            unit['block'] = block
        units.append(unit)
    for n in selected:
        children.setdefault(n.get('parent'), []).append(n)
    if stage == 'outline':
        for n in selected:
            add('specificity', n['id'], [n['id']])
            if n.get('parent') is not None:
                add('parent_fit', n['id'], [n['parent'], n['id']])
            if n['kind'] == 'paragraph' or (n['kind'] in ('section', 'subsection') and n['id'] not in children):
                add('focus', n['id'], [n['id']])
            for dep in n.get('depends_on', []):
                add('dependency', n['id'] + '<-' + dep, [dep, n['id']])
        for siblings in children.values():
            for a, b in zip(siblings, siblings[1:]):
                add('sequence', a['id'] + '->' + b['id'], [a['id'], b['id']])
    else:
        for n in selected:
            if n['kind'] == 'sentence' and n.get('prose'):
                add('realization', n['id'], [n['id']])
                add('terminology', n['id'], [n['id']])
                if n.get('claim_type') != 'transition':
                    add('evidence_fit', n['id'], [n['id']])
                    add('strength', n['id'], [n['id']])
            if n['kind'] == 'paragraph' and written_content(doc, n['id']):
                add('economy', n['id'], [n['id']])
        # Blocks remain reviewable at coarse paragraph/architecture levels;
        # their current body and inherited evidence cannot disappear from scope.
        for n in descendants(doc, scope):
            for block in n.get('blocks', []):
                for dimension in ('realization', 'terminology', 'evidence_fit', 'strength'):
                    add(dimension, block['id'], [n['id']], block['id'])
        for siblings in children.values():
            for a, b in zip(siblings, siblings[1:]):
                if a['kind'] == 'sentence' and b['kind'] == 'sentence' and a.get('prose') and b.get('prose'):
                    add('reader_flow', a['id'] + '->' + b['id'], [a['id'], b['id']])
                elif a['kind'] == b['kind'] and a['kind'] in ('paragraph', 'section', 'subsection') and written_content(doc, a['id']) and written_content(doc, b['id']):
                    add('reader_flow', a['id'] + '->' + b['id'], [a['id'], b['id']])
    neighbors = adjacent_nodes(doc, scope)
    order = {n['id']: i for i, n in enumerate(doc['nodes'])}
    for neighbor in neighbors:
        ids = sorted([scope, neighbor['id']], key=lambda nid: order[nid])
        if stage == 'outline':
            add('sequence', '->'.join(ids), ids)
        elif all(written_content(doc, nid) for nid in ids):
            add('reader_flow', '->'.join(ids), ids)
    return units

def written_content(doc, nid):
    """Current prose/block anchors, including the descendants of branch targets."""
    return [text for n in descendants(doc, nid)
            for text in ([n.get('prose', '')] + [b['content'] for b in n.get('blocks', [])]) if text]

def audit_anchors(doc, stage, unit):
    lookup = index(doc)
    if unit.get('block'):
        return [b['content'] for nid in unit['nodes'] for b in lookup[nid].get('blocks', [])
                if b['id'] == unit['block']]
    if stage == 'draft':
        return [text for nid in unit['nodes'] for text in written_content(doc, nid)]
    return [str(lookup[nid].get(field, '')) for nid in unit['nodes'] for field in ('intent', 'logic')]

def evaluate(doc, stage, level, scope, audit=None, evidence=None):
    errors = validate(doc, level, scope)
    structure_ok = not errors
    selected = descendants(doc, scope)
    leaves = [n for n in selected if not any(x.get('parent') == n['id'] for x in selected)]
    sentences = [n for n in selected if n.get('kind') == 'sentence']
    written = [n for n in sentences if n.get('prose')]
    hard = {'intent_presence': {'numerator': sum(bool(n.get('intent', '').strip()) for n in selected), 'denominator': len(selected)},
            'sentence_expansion': {'numerator': sum(n.get('kind') == 'sentence' for n in leaves), 'denominator': len(leaves)},
            'filling': {'numerator': len(written), 'denominator': len(sentences), 'rate': len(written) / len(sentences) if sentences else None}}
    if stage == 'draft' and not errors and mode(doc) != 'reverse-analysis':
        extra, hard['declared_traceability'] = evidence_checks(doc, scope, evidence)
        errors.extend(extra)
    expected = audit_units(doc, stage, level, scope) if structure_ok else []
    assessments = {}
    stale = False
    if audit:
        data = read_json(audit)
        if not data.get('reviewer') or data.get('reviewer_type') not in ('agent', 'human', 'independent'):
            errors.append(issue('audit_reviewer', None, 'Reviewer and reviewer_type required'))
        if data.get('binding') != binding(doc, stage, level, scope, evidence):
            stale = True
            errors.append(issue('stale_audit', None, 'Audit does not bind current stage/scope/artifacts'))
        else:
            rows = data.get('units', [])
            expected_map = {u['key']: u for u in expected}
            if not isinstance(rows, list) or any(not isinstance(r, dict) for r in rows):
                raise ValueError('Audit units must be objects')
            seen = set()
            for row in rows:
                key = row.get('key')
                if key in seen or key not in expected_map:
                    errors.append(issue('audit_unit', key, 'Duplicate or unexpected assessment'))
                    continue
                seen.add(key)
                unit = expected_map[key]
                if row.get('dimension') != unit['dimension'] or row.get('nodes') != unit['nodes'] or row.get('block') != unit.get('block'):
                    errors.append(issue('audit_target', key, 'Assessment must retain exact unit target'))
                    continue
                score = row.get('score')
                if score is None:
                    continue
                if mode(doc) == 'reverse-analysis' and unit['dimension'] in ('evidence_fit', 'strength'):
                    errors.append(issue('reverse_science_unverified', key,
                        'PDF-only reverse analysis leaves scientific evidence_fit and strength unassessed', 'major'))
                    continue
                quote = row.get('quote', '')
                anchors = audit_anchors(doc, stage, unit)
                if type(score) is not int or score not in range(4) or not isinstance(row.get('reason'), str) or not row['reason'].strip() or not isinstance(quote, str) or not quote.strip() or not any(quote in anchor for anchor in anchors):
                    errors.append(issue('audit_anchor', key, 'Score 0..3, specific reason and exact intention/prose quote required'))
                    continue
                if score < 3 and not all(isinstance(row.get(k), str) and row[k].strip() for k in ('consequence', 'repair', 'close_criterion')):
                    errors.append(issue('audit_closure', key, 'Every defect needs consequence, repair and a testable closure criterion'))
                    continue
                assessments[key] = row
    dimensions = {}
    dim_names = ('specificity', 'parent_fit', 'sequence', 'focus', 'dependency') if stage == 'outline' else ('realization', 'evidence_fit', 'strength', 'reader_flow', 'economy', 'terminology')
    for dim in dim_names:
        units = [u for u in expected if u['dimension'] == dim]
        rated = [assessments[u['key']] for u in units if u['key'] in assessments]
        dimensions[dim] = {'expected': len(units), 'assessed': len(rated), 'coverage': len(rated) / len(units) if units else None,
                           'index': 100 * sum(r['score'] for r in rated) / (3 * len(rated)) if rated else None}
    scores = [d['index'] for d in dimensions.values() if d['index'] is not None]
    severities = [e['severity'] for e in errors] + [{0: 'blocker', 1: 'major', 2: 'minor', 3: 'none'}[r['score']] for r in assessments.values()]
    low = min(scores) if scores else None
    if 'blocker' in severities:
        proposed = 'D'
    elif 'major' in severities:
        proposed = 'C'
    elif 'minor' in severities:
        proposed = 'B'
    else:
        proposed = 'A' if scores else 'U'
    complete = bool(expected) and len(assessments) == len(expected) and not stale
    grade = proposed if complete else 'U'
    semantic_issues = [dict(r, severity={0: 'blocker', 1: 'major', 2: 'minor'}[r['score']]) for r in assessments.values() if r['score'] < 3]
    return {'rubric': 'research-writing/3', 'mode': mode(doc), 'stage': stage, 'level': level, 'scope': scope,
            'scientific_verification_status': 'unverified' if mode(doc) == 'reverse-analysis' else 'not-established-by-tool',
            'research_maturity': doc['meta'].get('maturity'), 'hard': hard, 'hard_issues': errors,
            'dimensions': dimensions, 'semantic_coverage': {'assessed': len(assessments), 'expected': len(expected)},
            'grade': grade, 'provisional_grade': proposed if grade == 'U' else None,
            'weakest_dimension_index': low,
            'issue_counts': {severity: severities.count(severity) for severity in ('blocker', 'major', 'minor')},
            'whole_manuscript_grade': grade if scope == doc['nodes'][0]['id'] and (stage == 'outline' or len(written) == len(sentences)) else 'U',
            'semantic_issues': semantic_issues, 'unassessed': [u['key'] for u in expected if u['key'] not in assessments],
            'limitations': 'Deterministic checks establish bookkeeping, not scientific support. Semantic ratings are reviewer judgments. Grade thresholds require calibration.'}

def export(doc, out, reviews, audit=None, evidence=None, incomplete=False, scope=None):
    protect_output(doc, out, evidence, reviews, audit)
    if mode(doc) == 'reverse-analysis':
        raise ValueError('Reverse analysis is read-only: manuscript export is unavailable')
    scope = scope or (doc['nodes'][0]['id'] if doc['nodes'] else '')
    review_gate = gate(doc, reviews, scope)
    if not review_gate['ok']:
        raise ValueError('Export blocked: incomplete/stale intent review gate')
    selected = descendants(doc, scope)
    report = evaluate(doc, 'draft', 'sentences', scope, audit, evidence)
    if report['hard_issues']:
        raise ValueError('Export blocked: assertion/provenance errors')
    filling = report['hard']['filling']
    if not incomplete and (report['grade'] not in ('A', 'B') or filling['rate'] != 1 or not audit):
        raise ValueError('Full scoped export requires complete prose and a current complete A/B draft audit; use --allow-incomplete for a marked review draft')
    result, paragraph = [], []
    def flush():
        if paragraph:
            result.extend([' '.join(paragraph), ''])
            paragraph.clear()
    if incomplete:
        result.extend(['> Incomplete review draft; open nodes and unreviewed semantics are not final findings.', ''])
    if scope != doc['nodes'][0]['id']:
        result.extend(['> Scoped manuscript excerpt: ' + scope + '; no whole-paper approval or grade implied.', ''])
    for n in selected:
        if n['kind'] in ('paper', 'section', 'subsection'):
            flush()
            result.extend(['#' * n['_depth'] + ' ' + n['title'], ''])
        elif n['kind'] == 'paragraph':
            flush()
        elif n['kind'] == 'sentence':
            if n.get('prose'):
                paragraph.append(n['prose'])
            elif incomplete:
                paragraph.append('[OPEN INTENT ' + n['id'] + ']')
            for block in n.get('blocks', []):
                flush()
                def rebase_image(match):
                    target = match[1].strip('<>')
                    parts = urlsplit(target)
                    if parts.scheme or parts.netloc or not parts.path:
                        return match[0]
                    source = (doc['draft_path'].parent / unquote(parts.path)).resolve()
                    relative = Path(os.path.relpath(source, Path(out).resolve().parent)).as_posix()
                    rebased = urlunsplit(('', '', relative, parts.query, parts.fragment))
                    start, end = match.start(1) - match.start(), match.end(1) - match.start()
                    return match[0][:start] + '<' + rebased + '>' + match[0][end:]
                result.extend([IMAGE.sub(rebase_image, block['content']), ''])
    flush()
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text('\n'.join(result).rstrip() + '\n', encoding='utf-8')
    return {'ok': True, 'out': str(out), 'scope': scope, 'incomplete_review_draft': incomplete}

def display_nodes(nodes):
    lines = []
    for n in nodes:
        if n['kind'] == 'sentence':
            lines.append('- [' + n['id'] + '] ' + n['intent'])
            continue
        lines.extend(['', '#' * n['_depth'] + ' [' + n['id'] + '] ' + n['title'], ''])
        if n['kind'] != 'paragraph':
            lines.extend(['概述：' + n['intent'], ''])
            if n.get('logic'):
                lines.extend(['论证顺序：' + n['logic'], ''])
    return '\n'.join(lines).strip()

def display_projection(nodes):
    return [{k: v for k, v in n.items() if k in
             {'id', 'kind', 'parent', 'title', 'intent', 'logic', 'depends_on', 'uses', 'introduces'}}
            for n in nodes]

def main():
    # CLI output has one encoding on every platform; importing this module leaves
    # the caller's streams unchanged. StringIO and other custom streams may not
    # expose reconfigure.
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, 'reconfigure', None)
        if callable(reconfigure):
            reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ('validate', 'show', 'review', 'gate', 'audit-template', 'evaluate', 'export'):
        p = sub.add_parser(name)
        p.add_argument('tree')
        p.add_argument('--project', help='Optional project state; default: project.json beside tree')
        p.add_argument('--draft', help='Optional prose file; default: draft.md beside tree')
        if name in ('validate', 'review', 'audit-template', 'evaluate'):
            p.add_argument('--level', choices=LEVELS, default='sentences')
        if name in ('validate', 'review', 'gate', 'audit-template', 'evaluate', 'export'):
            p.add_argument('--scope')
        if name in ('audit-template', 'evaluate'):
            p.add_argument('--stage', choices=('outline', 'draft'), required=True)
        if name in ('audit-template', 'evaluate', 'export'):
            p.add_argument('--evidence')
        if name in ('review', 'gate', 'export'):
            p.add_argument('--reviews', required=True)
        if name in ('evaluate', 'export'):
            p.add_argument('--audit')
        if name in ('audit-template', 'evaluate', 'export'):
            p.add_argument('--out', required=True)
        if name == 'show':
            p.add_argument('node')
            p.add_argument('--context', action=argparse.BooleanOptionalAction, default=True)
            p.add_argument('--json', action='store_true', help='Structured machine output')
        if name == 'review':
            p.add_argument('--decision', choices=('approved', 'changes-required'), required=True)
            p.add_argument('--source', required=True, help='Exact actual human feedback quote')
            p.add_argument('--reference', required=True, help='Chat/meeting reference; not fabricated')
        if name == 'export':
            p.add_argument('--allow-incomplete', action='store_true')
    args = parser.parse_args()
    try:
        doc = parse(args.tree, args.project, args.draft)
        scope = getattr(args, 'scope', None) or (doc['nodes'][0]['id'] if doc['nodes'] else '')
        if args.command == 'validate':
            errors = validate(doc, args.level, scope)
            result = {'ok': not errors, 'scope': scope, 'nodes': len(descendants(doc, scope)), 'errors': errors}
        elif args.command == 'show':
            subtree = descendants(doc, args.node)
            context = []
            if args.context:
                lookup, parent = index(doc), subtree[0].get('parent')
                while parent:
                    context.insert(0, lookup[parent])
                    parent = lookup[parent].get('parent')
                context += [n for n in doc['nodes'] if n.get('parent') == subtree[0].get('parent') and n['id'] != args.node]
                contextual_ids = {n['id'] for n in context}
                subtree_ids = {n['id'] for n in subtree}
                for n in projected_nodes(doc, args.node, 'sentences')['context']:
                    if n['id'] not in contextual_ids and n['id'] not in subtree_ids:
                        context.append(lookup[n['id']])
                        contextual_ids.add(n['id'])
            result = {'context': display_projection(context), 'subtree': display_projection(subtree)}
            if not args.json:
                if context:
                    print('上下文\n\n' + display_nodes(context) + '\n\n子树\n')
                print(display_nodes(subtree))
                return 0
        elif args.command == 'gate':
            result = gate(doc, args.reviews, scope)
        elif args.command == 'review':
            protect_output(doc, args.reviews, reviews=args.reviews, review_write=True)
            if mode(doc) == 'reverse-analysis':
                raise ValueError('Reverse analysis is read-only: human composition approval cannot be recorded')
            errors = validate(doc, args.level, scope)
            if errors:
                raise ValueError('Cannot review malformed/incomplete level: ' + canonical(errors))
            if not args.source.strip() or not args.reference.strip():
                raise ValueError('Actual human feedback and reference required')
            data = read_json(args.reviews, {'items': []})
            row = {'scope': scope, 'level': args.level, 'decision': args.decision, 'by': 'human',
                   'source': args.source, 'reference': args.reference,
                   'recorded_at': datetime.now(timezone.utc).isoformat(), 'plan_hash': plan_hash(doc, scope, args.level)}
            data['items'].append(row)
            write_json(args.reviews, data)
            result = {'recorded': row, 'notice': 'Recording is not identity authentication; do not fabricate feedback.'}
        elif args.command == 'audit-template':
            protect_output(doc, args.out, args.evidence)
            errors = validate(doc, args.level, scope)
            if errors:
                raise ValueError('Cannot assess malformed level: ' + canonical(errors))
            result = {'rubric': 'research-writing/3', 'reviewer': '', 'reviewer_type': 'agent',
                      'binding': binding(doc, args.stage, args.level, scope, args.evidence),
                      'units': audit_units(doc, args.stage, args.level, scope)}
            write_json(args.out, result)
            result = {'out': args.out, 'units': len(result['units']), 'notice': 'Fill by actual semantic inspection; null is unassessed.'}
        elif args.command == 'evaluate':
            protect_output(doc, args.out, args.evidence, audit=args.audit)
            result = evaluate(doc, args.stage, args.level, scope, args.audit, args.evidence)
            write_json(args.out, result)
        else:
            result = export(doc, args.out, args.reviews, args.audit, args.evidence, args.allow_incomplete, scope)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1 if result.get('ok') is False else 0
    except (ValueError, KeyError, TypeError, OSError, RecursionError) as exc:
        print(json.dumps({'ok': False, 'error': str(exc)}, ensure_ascii=False))
        return 2

if __name__ == '__main__':
    sys.exit(main())
