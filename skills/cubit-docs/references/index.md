# Coreform Cubit reference index

The references contain 515 pages from the official v2026.6 manual, grouped by Skill Seekers into
10 category files. Each source page begins with a level-two heading and its official URL.

## Task routing

| Task | Read first | Useful searches |
|---|---|---|
| Installation, licensing, support, system requirements | `introduction.md` | `Licensing and Activation`, `System Requirements`, `Support` |
| GUI, command syntax, journals, sessions, graphics, selection | `environment.md` | `Command Syntax`, `Journal`, `Entity Selection`, `Saving and Restoring` |
| Create, import, transform, decompose, heal, imprint, merge, or export geometry | `geometry.md` | `Primitive`, `Boolean`, `Importing`, `Web Cutting`, `Healing`, `Imprint`, `Merge` |
| Assign sizes/intervals and generate, smooth, modify, validate, or assess a mesh | `meshing.md` | `Interval`, `Scheme`, `Sweep`, `TetMesh`, `Pave`, `Quality`, `Smoothing` |
| Boundary layers, Sculpt, parallel meshing, adaptivity | `meshing.md` | `Boundary Layer Meshing`, `Sculpt`, `Parallel`, `Adaptivity` |
| Define blocks, nodesets, sidesets, materials, BCs, and export an FE model | `fe_model.md` | `Element Block`, `Nodeset`, `Sideset`, `Boundary Condition`, `Exodus` |
| Automate Cubit with Python | `python_api.md` | `Method-Based API`, `Object-Based API`, `cubit.init`, `cubit.cmd` |
| Use the ITEM wizard and geometry power tools | `item.md` | `ITEM`, `Merge Tolerance`, `Forced Sweepability`, `Small Feature` |
| Follow GUI, command-line, ITEM, or power-tools walkthroughs | `tutorials.md` | `Basic Tutorial`, `Power Tools`, `Step 1` |
| Use APREPRO, Alpha, quick reference, FASTQ, or appendix material | `reference.md` | `APREPRO`, `Alpha Commands`, `Quick Reference`, `FASTQ` |
| View credits | `other.md` | `Credits` |

## Retrieval pattern

Search for both the user term and likely manual terminology. For example:

```bash
rg -n -i "sweep|source surface|target surface" references/meshing.md
rg -n -i "nodeset|sideset|block|exodus" references/fe_model.md
rg -n -i "cubit\.init|cubit\.cmd|object-based" references/python_api.md
rg -n -i "imprint|merge|tolerance" references/geometry.md references/item.md
```

After finding a line, read from its nearest preceding `##` heading through the next page separator
or `##` heading. Do not treat similarly named commands from another category as interchangeable.

## Workflow cross-checks

- Geometry-to-mesh work commonly needs `geometry.md`, then `meshing.md`.
- Solver-export work commonly needs `meshing.md`, then `fe_model.md`.
- Journal automation commonly needs `environment.md` plus the domain category.
- Python automation commonly needs `python_api.md` plus the domain category.
- ITEM recommendations may require `item.md`, `geometry.md`, and `meshing.md`.
- Reproduce tutorial commands only after checking their assumptions and the current model state.
