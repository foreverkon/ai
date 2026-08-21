# Source and scope

- Source site: <https://petsc.org/release/>
- Focus areas: Overview, Tutorials, User Guide, and C/Fortran manual pages.
- Captured documentation version: PETSc 3.25.4.
- Release-site build observed: `v3.25.4-18-g20dc33036117`.
- Release-site last-updated value observed: 2026-08-19.
- Extraction date: 2026-08-20.
- Extraction tool: Skill Seekers 3.9.1, followed by task-oriented curation.
- Extracted documentation entries: 8,428 across 17 generated task categories (8,426 unique URLs).
- API coverage: 8,378 unique routine/type/component URLs under the C/Fortran manual-pages area were inspected, excluding the root index.
- Collectivity supplement: 8,378 manual-page URLs inspected; 6,131 explicit labels retained; 2,247 type/constant/index pages had no synopsis label; zero fetch failures.
- User-guide coverage: 30 unique URLs.
- Overview coverage: 12 unique URLs.
- Narrative tutorial coverage: 7 unique URLs.
- Curated tutorial-source supplement: 11 official C listings directly linked by the problem- and physics-oriented tutorial guides.

The snapshot intentionally excludes static assets, search/generated indexes, previous-release documentation, and petsc4py pages. It centers on C and Fortran application development. Skill Seekers' paragraph-length filter omits short synopsis labels such as `Collective`; `api_collectivity.md` deterministically restores them from the same official manual pages. PETSc's source-code listings use bare c2html `<pre>` pages, which Skill Seekers 3.9.1 visits but classifies as empty because they contain no prose paragraphs. The 11 examples directly selected by the official tutorial guides were therefore normalized deterministically from those official pages into `tutorial_source_patterns.md`; no generated code was added. Use them as patterns, then verify every API call against the captured manual pages.

The live release documentation can change after extraction. For version-sensitive work, compare the target PETSc installation with this snapshot before using newly introduced APIs or options.
