---
name: petsc-docs
description: Use the official PETSc 3.25.4 release documentation to design, write, review, explain, and troubleshoot accurate PETSc C or Fortran code. Apply for Vec, Mat, KSP/PC, SNES, TS, TAO, DM, DMPlex, discretization, MPI ownership and assembly, runtime options, debugging, profiling, GPU backends, API signatures, collective semantics, and adapting official tutorials. Prefer exact local manual-page evidence over memory.
---

# PETSc Docs Skill

Use this skill as a task-oriented interface to the official PETSc release documentation. Do not guess PETSc symbols, signatures, option names, collectivity, or ownership rules when the local references can answer them.

## When to Use This Skill

Use it whenever a task requires PETSc C or Fortran implementation, API verification, code review, debugging, solver configuration, parallel-data reasoning, tutorial adaptation, or performance guidance grounded in the current release documentation.

## Start every task this way

1. Identify the requested PETSc version, language (C or Fortran), MPI execution model, scalar type, index width, precision, and CPU/GPU backend. If unspecified, state the assumptions that affect the code.
2. Open `references/index.md` and choose the smallest relevant task area.
3. Search that reference for the exact routine, type, option, or concept. For an API routine, read its synopsis, parameters, notes, Fortran notes, options, and see-also links; verify its short parallel classification in `references/api_collectivity.md`.
4. Find the closest official tutorial or user-guide pattern. Treat examples as patterns to adapt, not as substitutes for the exact API page.
5. Implement using `references/professional-coding-workflow.md`.
6. Audit the result with `references/code-review-checklist.md` before answering.

## Retrieve evidence efficiently

Search references instead of loading large files wholesale:

- Linear solvers: `rg -n -i "KSPSetOperators|KSPSetFromOptions|KSPSolve|KSPGetConvergedReason" references/linear_solvers.md`
- Matrix assembly: `rg -n -i "MatSetValues|MatAssemblyBegin|MatAssemblyEnd|ownership range" references/matrices.md`
- API semantics: `rg -n -i "Fortran Notes|Collective|Logically Collective" references/*.md`

Verify `Collective`, `Logically Collective`, `Not Collective`, and qualified variants in `references/api_collectivity.md`, then read the full subsystem reference for the rest of the contract.

When a symbol occurs in both the user guide and a manual page, use the user guide for workflow and the manual page for the exact contract. Preserve the manual-page URL in explanations when the user asks for sources.

## Code-generation contract

- Produce a complete, internally consistent lifecycle: initialize, create, configure, assemble/setup, solve/apply, inspect status, destroy, finalize.
- Use the documented communicator and honor collective or logically collective calls on the participating ranks.
- Respect ownership ranges, local/global layouts, ghost updates, insertion modes, and paired `Begin`/`End` assembly or communication calls.
- In C, propagate PETSc errors using the documented PETSc error-handling macros and callback conventions. In Fortran, use the documented module/include form and error argument conventions for the target version.
- Expose normal solver and object choices through the options database and call the corresponding `*SetFromOptions()` routine at the correct point.
- Check convergence reason after solvers; an iteration count alone does not prove convergence.
- Keep residual, Jacobian, monitor, event, and other callbacks signature-correct and give context data a valid lifetime.
- Do not hard-code a GPU, external solver, matrix type, or optional package unless the requested PETSc build supports it. Prefer runtime-selectable types where appropriate.
- Never invent an option or claim code was compiled, run, parallel-tested, or performance-validated unless that verification actually occurred.

## Resolve ambiguity

- Distinguish API availability in PETSc 3.25.4 from older or development versions.
- Distinguish C API, Fortran interface notes, and petsc4py; this skill is centered on C and Fortran.
- If a routine contract is absent or contradictory in the bundled references, say so and consult the live official release manual page rather than improvising.
- For performance advice, separate correctness requirements from workload- and machine-dependent tuning.

## Reference map

Use `references/index.md` for task routing. The principal groups are orientation and tutorials; program structure; vectors and indices; matrices; linear, nonlinear, time-integration, and optimization solvers; DM and meshes; discretization; parallel layouts; I/O and visualization; runtime options, debugging, and performance.
