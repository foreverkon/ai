# PETSc code review checklist

## API accuracy

- Every symbol exists in the PETSc 3.25.4 references.
- Headers/modules, signatures, callback types, enum constants, and format specifiers match the documented interface.
- C error propagation or Fortran error handling follows current PETSc guidance.
- No petsc4py convention has leaked into C or Fortran code.

## Parallel and data-layout correctness

- Communicators and collective call paths agree across ranks.
- Global and local sizes are compatible; ownership ranges are respected.
- Sparse matrices are preallocated for the expected nonzero structure.
- Insertion modes and all assembly/scatter/ghost `Begin`/`End` pairs are correct.
- Local arrays obtained from PETSc objects are restored on every path.

## Solver correctness

- Operators, residuals, Jacobians, objective functions, and contexts remain valid for the solve.
- Runtime options are applied after programmatic defaults in the intended precedence order.
- Tolerances and convergence tests match the problem scale and stated goal.
- The convergence reason—not just iteration count—is inspected.
- Reuse/reset behavior is valid when matrices, sizes, or nonlinear/time-step state changes.

## Resource and error safety

- All created PETSc objects are destroyed exactly once.
- Temporary vectors/matrices and borrowed resources follow their documented ownership rules.
- Cleanup and finalization are reachable under the chosen error-handling pattern.
- Output is MPI-safe and does not accidentally duplicate or race.

## Portability and performance

- Optional packages, device types, scalar assumptions, precision, and index width are explicit.
- Correctness does not depend on one process count or a single backend.
- Performance advice is supported by profiling or clearly marked as a hypothesis.
- Expensive setup can be reused only where the documentation permits it.

## Answer quality

- State meaningful assumptions and required runtime options.
- Explain the PETSc object lifecycle and parallel semantics that are easy to misuse.
- Point to exact local reference sections or official URLs for non-obvious API claims.
- Do not claim compilation, execution, convergence, or scaling results that were not observed.
