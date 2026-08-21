# Professional PETSc coding workflow

Use this workflow to turn documentation into code without silently changing the API contract.

## 1. Establish the execution contract

Record the PETSc release, C or Fortran interface, communicator, anticipated process count, scalar and precision assumptions, index width, and device/backend requirements. These details can change types, format specifiers, available matrix/vector implementations, and runtime options.

## 2. Select the abstraction before the implementation

Choose the PETSc object that owns the problem-level responsibility:

- `Vec`, `IS`, and layouts for distributed values and indices.
- `Mat` for assembled, shell, nested, sparse, dense, or backend-specific operators.
- `KSP` plus `PC` for linear systems.
- `SNES` for nonlinear equations and nonlinear least-squares workflows.
- `TS` for time integration, events, adjoints, and sensitivities.
- `TAO` for optimization.
- `DM` and its implementations for topology, decomposition, fields, local/global data, and discretization.

Prefer runtime selection through the options database unless a fixed type is an explicit application requirement.

## 3. Verify every API contract

For every less-than-obvious call, locate its manual-page entry and check:

- exact C synopsis and header;
- collective, logically collective, or noncollective classification;
- input, output, and in/out parameter ownership;
- required object state and ordering constraints;
- paired calls such as assembly or scatter begin/end;
- options-database equivalents;
- Fortran-specific notes and unsupported callback patterns;
- return/error behavior and related routines.

Do not infer a signature from a similarly named routine.

## 4. Build the lifecycle explicitly

A typical application has the following phases, adjusted to the selected objects:

1. Initialize PETSc and parse application options.
2. Create distributed objects on the intended communicator.
3. Establish sizes/layouts and allow runtime type selection.
4. Preallocate before inserting sparse matrix entries.
5. Populate local contributions using ownership-aware indexing.
6. Complete every required assembly or communication pair.
7. Attach operators and callbacks, then apply `*SetFromOptions()`.
8. Solve or advance.
9. inspect convergence/status and report failures meaningfully.
10. Destroy objects in a valid order and finalize PETSc.

## 5. Preserve parallel correctness

Collective calls must be reached by all ranks in the communicator with compatible arguments. Only write locally owned entries unless the documented insertion path supports off-process values. Keep `INSERT_VALUES` and `ADD_VALUES` phases separate when required. Complete ghost exchanges and local-to-global/global-to-local operations before consuming updated data.

## 6. Make configuration observable

Call the relevant `*SetFromOptions()` routines and document useful runtime flags rather than burying all solver choices in code. Add viewers or monitors only when requested, and ensure their output works under MPI. Query convergence reasons for KSP, SNES, TS, and TAO as applicable.

## 7. Adapt tutorials safely

Choose the nearest official example by mathematical problem, physics, object family, dimensionality, discretization, and parallel layout. Preserve its setup/assembly/callback ordering while adapting data and equations. Then re-check every used routine against the matching manual page because examples can omit generality or rely on test-harness options.

## 8. Verify claims

If a PETSc toolchain is available, compile with the project’s supported build mechanism and run at least one serial and one relevant MPI case. Exercise representative runtime options. Otherwise, label the result as documentation-checked but uncompiled.

