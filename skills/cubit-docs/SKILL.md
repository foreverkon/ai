---
name: cubit-docs
description: Use the official Coreform Cubit 2026.6 user manual to create, explain, review, and troubleshoot Cubit commands, journal files, Python API scripts, GUI workflows, geometry creation and cleanup, mesh sizing and generation, mesh quality and modification, finite-element blocks/nodesets/sidesets, boundary conditions, boundary-layer meshes, ITEM workflows, Sculpt/APREPRO features, imports/exports, and tutorials. Trigger for Coreform Cubit or CUBIT command syntax, meshing workflows, automation, API usage, and documentation-grounded answers; distinguish Coreform Cubit from unrelated products and older Sandia CUBIT behavior when version matters.
---

# Work with Coreform Cubit

Ground answers, commands, journals, and scripts in the bundled Coreform Cubit 2026.6 user manual.
Preserve the manual's command syntax and page URLs, and account for version differences.

## Start with targeted retrieval

1. Classify the task using `references/index.md`.
2. Search only the relevant category files for the exact command, option, API method, or error.
3. Locate the matching `##` page heading and read that page section before drafting an answer.
4. Cross-check multi-stage workflows against related geometry, meshing, FE model, or tutorial pages.
5. Cite or provide the source URL stored under the relevant page heading when traceability helps.

Use fast text search because several category references are large:

```bash
rg -n -i "exact command|option|error fragment" references
rg -n "^## " references/meshing.md
```

Do not load all reference files into context. Read only the matching page section and adjacent
prerequisites.

## Build commands and journal workflows

- Determine the target entity type and ID range before composing a command.
- Preserve optional-argument ordering and braces/brackets semantics shown by the manual.
- State assumptions about model state, coordinate system, entity IDs, sizing, and units.
- For a journal, order operations explicitly: reset/import or create geometry, heal/modify,
  imprint and merge when appropriate, assign sizes/intervals and schemes, mesh, assess quality,
  define FE entities, then export.
- Prefer the smallest command sequence that satisfies the request. Do not add cleanup, imprint,
  merge, deletion, or remeshing steps without explaining their effects.

## Write Python automation

- Read `references/python_api.md` and distinguish the method-based API, object-based API, embedded
  Python, and stand-alone Python initialization.
- Use documented Python methods when available. Use `cubit.cmd(...)` for command-language calls
  only when that interface is appropriate.
- Check return types and entity-ID conventions instead of guessing from method names.
- Separate Cubit initialization/licensing/path setup from the reusable modeling function.

## Design geometry and meshing workflows

- Inspect geometry prerequisites before selecting a meshing scheme.
- Make sizing, interval constraints, scheme assignment, sweep source/target, and mesh order explicit.
- For failed meshing, diagnose geometry validity, topology, interval compatibility, scheme
  prerequisites, and quality separately.
- Treat boundary-layer, Sculpt, parallel, and ITEM workflows as specialized paths; read their
  dedicated sections before adapting commands.
- Never claim that a mesh is valid or analysis-ready unless the relevant checks were actually run.

## Define and export an FE model

- Read `references/fe_model.md` for blocks, nodesets, sidesets, materials, boundary conditions, and
  Exodus-related settings.
- Keep geometry selection, mesh entity selection, IDs, names, and export format distinct.
- Verify solver-specific requirements with that solver's documentation; the Cubit manual governs
  model construction and export, not downstream solver semantics.

## Modify user artifacts safely

- Inspect the existing `.jou`, Python script, model assumptions, and reported log before editing.
- Preserve working commands and make minimal, reviewable changes.
- Warn before commands that delete entities, reset the model, alter topology, merge geometry,
  overwrite files, or replace an existing mesh. Recommend saving a Cubit session or journal first.
- If execution is unavailable, label the result as documentation-derived and untested.

## Handle version and documentation gaps

- The bundled manual is v2026.6. For another installed release, verify changed syntax against its
  matching help pages or release notes.
- Do not silently substitute legacy Sandia CUBIT syntax or behavior.
- If the references do not support a claim, state the gap and consult current official Coreform
  documentation when external access is available.

## Navigate references

Read `references/index.md` for the topic-to-file map, important search terms, and retrieval guidance.
