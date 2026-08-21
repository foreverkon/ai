# nekRS reference index

This index routes tasks to the smallest useful set of upstream files. Paths are relative to the
skill root. The documentation is preserved as reStructuredText so commands, tables, directives,
and code blocks remain close to the source.

## Core workflows

| Task | Read first | Then read when needed |
|---|---|---|
| Install, build, environment, first run | `references/documentation/other/quickstart.rst` | `references/documentation/other/running.rst` |
| Understand case files, `.par`, `.udf`, `.oudf`, `.usr` | `references/documentation/other/case.rst` | Boundary, property, or model reference below |
| Select or implement boundary conditions | `references/documentation/other/boundary_conditions.rst` | `case.rst`, closest example |
| Set initial conditions | `references/documentation/other/initial_conditions.rst` | `case.rst`, closest example |
| Generate, convert, refine, or restart a mesh | `references/documentation/other/meshing.rst` | Relevant tutorial and example |
| Configure material or transport properties | `references/documentation/other/properties.rst` | `theory.rst`, `case.rst` |
| Configure LES, RANS, filtering, or other models | `references/documentation/other/models.rst` | `theory.rst`, RANS example |
| Run locally, with MPI, or on an HPC scheduler | `references/documentation/other/running.rst` | `quickstart.rst`, `debugging.rst` |
| Debug build, JIT, runtime, or convergence problems | `references/documentation/other/debugging.rst` | `running.rst`, topic-specific file |
| Write fields, visualize, or extract results | `references/documentation/other/postprocessing.rst` | Relevant tutorial |
| Understand equations and numerical approach | `references/documentation/other/theory.rst` | `models.rst`, `properties.rst` |
| Use low-level mesh, memory, linear algebra, or SEM APIs | `references/documentation/other/other_resources.rst` | `case.rst` |
| Decode terminology | `references/documentation/other/glossary.rst` | Topic-specific file |

## Tutorials

| Scenario | Tutorial | Exact input examples |
|---|---|---|
| Fully developed laminar flow | `references/documentation/guides/fdlf.rst` | `references/examples/fdlf/` |
| Conjugate heat transfer | `references/documentation/guides/conjugate_heat_transfer.rst` | `references/examples/cht/` |
| RANS channel / k-tau workflow | `references/documentation/guides/rans_channel.rst` | `references/examples/ktauTutorial/` |
| Periodic hill case | Use model, case, and meshing references | `references/examples/periodic_hill/` |

## Project and contributor material

- Documentation overview and local Sphinx build:
  `references/documentation/overview/README.md`
- Documentation entry point: `references/documentation/other/index.rst`
- Developer guide: `references/documentation/guides/_developer_guide.rst`
- Contribution notes: `references/documentation/guides/contributing.rst`
- Doxygen notes: `references/documentation/guides/doxygen.rst`
- Bibliography: `references/documentation/other/references.rst`

## Search hints

Search exact option names, callback names, file extensions, or an error fragment across both docs
and examples. Useful terms include `UDF_Setup`, `UDF_ExecuteStep`, `udfDirichlet`, `nrsmpi`,
`nrsbmpi`, `boundaryTypeMap`, `pressure`, `velocity`, `scalar`, `restart`, `checkpoint`, `AMG`,
`RANS`, `LES`, `lowMach`, `CUDA`, and `HIP`.

The `_problem_setup.rst`, `_tutorials.rst`, and `_developer_guide.rst` files are navigation stubs;
prefer the concrete topic files above.
