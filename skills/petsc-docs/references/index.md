# Task-oriented reference index

Open the smallest relevant file, then search for the exact routine, option, object type, or heading. The generated documentation files can be large because they preserve full manual-page contracts.

| Task | Primary reference | Typical searches |
|---|---|---|
| Understand PETSc scope, architecture, supported systems, and release orientation | `overview_orientation.md` | `PETSc in a nutshell`, supported systems, GPU roadmap |
| Choose and adapt an official example | `tutorials_examples.md`, `tutorial_source_patterns.md` | mathematical problem, physics, `ex*.c`, test options |
| Initialize/finalize, structure an application, use options, or write Fortran | `getting_started_core.md` | `PetscInitialize`, `PetscFinalize`, options database, Fortran users |
| Work with distributed vectors and index sets | `vectors_indices.md` | `VecCreate`, ownership range, `VecSetValues`, ghost, `ISCreate` |
| Assemble, preallocate, or apply matrices | `matrices.md` | `MatCreate`, preallocation, `MatSetValues`, assembly, shell matrix |
| Solve linear systems and configure preconditioners | `linear_solvers.md` | `KSPCreate`, `KSPSetOperators`, `PCSetType`, convergence reason |
| Solve nonlinear equations or nonlinear least squares | `nonlinear_solvers.md` | `SNESSetFunction`, `SNESSetJacobian`, line search, FAS |
| Integrate time-dependent systems, events, adjoints, or sensitivities | `time_stepping_sensitivity.md` | `TSSetRHSFunction`, `TSSetIFunction`, event, adjoint |
| Formulate optimization or learning problems | `optimization_learning.md` | `TaoSetObjective`, gradient, Hessian, constraints, regressor |
| Manage distributed layouts, fields, and application data | `dm_core_layout.md` | `DMCreateGlobalVector`, local/global, `PetscSection` |
| Use structured grids and composite layouts | `structured_meshes.md` | `DMDA`, `DMStag`, `DMComposite`, stencil |
| Use unstructured meshes, networks, labels, forests, or swarms | `unstructured_meshes.md` | `DMPlex`, `DMLabel`, distribute, refine, interpolate |
| Define finite-element/finite-volume spaces and quadrature | `discretization.md` | `PetscFE`, `PetscFV`, `PetscSpace`, quadrature |
| Build lower-level parallel mappings | `parallel_layout.md` | `PetscSF`, `PetscLayout`, `AO`, broadcast, reduce |
| View, load, save, draw, or connect to visualization tools | `io_visualization.md` | `PetscViewer`, binary, HDF5, VTK, draw |
| Configure, diagnose, log, profile, test, or tune | `runtime_debug_performance.md` | error handling, `-log_view`, options, device, BLAS/LAPACK |

## Cross-cutting guidance

- `api_collectivity.md`: explicit parallel classification for 6,131 routines, including qualified variants.
- `professional-coding-workflow.md`: evidence-driven implementation sequence.
- `code-review-checklist.md`: correctness and portability audit.
- `source.md`: version, provenance, coverage, and extraction limits.

## Search patterns

Exact API name:

```bash
rg -n -F "MatAssemblyBegin" references/matrices.md
```

Concept plus contract metadata:

```bash
rg -n -i "ownership range|collective|fortran notes" references/vectors_indices.md
```

Runtime option or type:

```bash
rg -n -i -- "-ksp_type|KSPType|KSPGMRES" references/linear_solvers.md
```

If a term spans several subsystems, search all references first and then open only the matching sections:

```bash
rg -l -i "adjoint sensitivity" references/*.md
```
