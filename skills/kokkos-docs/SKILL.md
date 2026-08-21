---
name: kokkos-docs
description: Write, migrate, debug, and review performance-portable Kokkos Core C++ using source-level Programming Guide, API reference, and official use-case documentation. Use for Kokkos Views, execution and memory spaces, parallel_for/reduce/scan, policies, hierarchical and multidimensional parallelism, atomics, reducers, algorithms, containers, SIMD, MPI/Fortran interoperability, synchronization, and portability questions.
---

# Kokkos Docs

Use this skill as a source-grounded coding assistant for Kokkos. The bundled corpus is self-contained.

## Start here

1. Classify the request: concept/design, exact API contract, implementation, migration, debugging, or review.
2. Read `references/reference-index.md` and route to the smallest relevant source files.
3. Search the bundled references for the exact symbol before writing code. Prefer `rg -n "parallel_for|MDRangePolicy" references` or an equivalent recursive text search.
4. For code generation, normally consult both the exact API file and its Programming Guide chapter. Add a use case when integration behavior matters.
5. State assumptions that affect correctness: Kokkos version, enabled backends, C++ standard, memory accessibility, MPI GPU awareness, and whether execution may be asynchronous.

## When to use this skill

Use it to implement or review Kokkos Core code, choose portable data and execution abstractions, verify an exact overload or requirement, migrate backend-specific loops, diagnose memory-space or synchronization bugs, and integrate Kokkos with MPI, Fortran, Cabana, or host/device overlap. Do not use it as authority for Kokkos Kernels, Kokkos Tools, build-system configuration, or APIs absent from the bundled scope.

## Source precedence

- Use the exact file under `API/` for signatures, headers, overloads, requirements, semantics, version notes, and deprecations.
- Use `ProgrammingGuide/` for the mental model, design choices, portability guidance, and broader examples.
- Use `usecases/` for end-to-end patterns, but re-check every copied API against the API reference because use cases may document legacy or deprecated techniques.
- Treat external-library calls in use cases as illustrative, not normative. Validate MPI, Fortran, Cabana, and backend runtime behavior against their own contracts.
- Treat `.. versionadded::`, `.. deprecated::`, warnings, requirements, and notes as normative constraints. Do not silently generalize across versions.
- Read `references/known-source-caveats.md` before adapting MPI halo exchange, MDRange reductions, or tasking examples.
- If the bundled references do not establish a claim, say that the included documentation does not resolve it instead of inventing an API.

## Coding workflow

When writing or reviewing Kokkos C++:

1. Include the documented header and use the documented overload, not a guessed convenience form.
2. Establish lifecycle ownership (`Kokkos::initialize`/`finalize` or `ScopeGuard`) and ensure all Kokkos objects are destroyed before finalization.
3. Choose execution space, memory space, layout, and policy deliberately. Verify accessibility before dereferencing a `View` or passing its pointer to another library.
4. Match the functor/lambda signature to the policy, work tag, reducer, and rank. Keep device-callable code and captures portable.
5. Account for asynchronous dispatch. Add a fence only where host access, reuse, external libraries, timing, or ordering actually requires completion; prefer an execution-space instance fence when appropriate.
6. Use `create_mirror[_view]`, `deep_copy`, `subview`, reducers, and atomics according to their exact contracts. Never replace a deep copy with handle assignment.
7. Check edge cases: zero-length ranges, static versus dynamic extents, const propagation, layout conversion, unmanaged memory lifetime, reducer identity/join semantics, and integer/index width.
8. Keep backend-specific assumptions out of kernels unless the request explicitly targets one backend.
9. For MPI buffers, require contiguity, memory-space support, and an explicit Kokkos/MPI completion-order argument. Do not copy the bundled MPI halo examples verbatim.

## Minimal portable shape

Use this only as a structural starting point, then verify the exact APIs required by the task:

```cpp
#include <Kokkos_Core.hpp>

int main(int argc, char* argv[]) {
  Kokkos::ScopeGuard guard(argc, argv);
  {
    Kokkos::View<double*> values("values", 1024);
    Kokkos::parallel_for(
        "initialize values", values.extent(0),
        KOKKOS_LAMBDA(const int i) { values(i) = static_cast<double>(i); });
    Kokkos::fence("wait before leaving the example scope");
  }
}
```

The inner scope ensures managed Kokkos objects are destroyed before `ScopeGuard` finalizes Kokkos. A real program should fence at its actual dependency boundary and use the exact execution-space overload where ordering matters.

## Review checklist

- Initialization/finalization order is valid.
- `View` element type, rank, extents, layout, memory space, and ownership match actual use.
- Host code never directly accesses device-only memory; data movement and mirrors are explicit.
- Kernel captures do not retain host-only pointers or references and do not perform forbidden allocation or I/O.
- Policy and callable signatures match, including tags and team/member types.
- Reduction/scan value type, identity, initialization, join, and final-pass behavior are correct.
- Required synchronization is present, but unnecessary global fences are avoided.
- MPI or other library calls respect memory accessibility and completion/stream ordering.
- Deprecated APIs and version-specific features are identified.
- The answer includes a compact build/run or verification strategy when practical.

## Navigation

- `references/reference-index.md`: task routes and a complete grouped document index.
- `references/symbol-index.md`: API directive and `Kokkos::` symbol lookup.
- `references/coding-checklist.md`: focused correctness and portability reminders.
- `references/known-source-caveats.md`: verified ambiguities and unsafe examples in the bundled documentation.
- `references/source--*`: the unabridged RST, Markdown, and C++ references. Filenames encode document paths with `--` separators.

Because source files are flattened to prevent basename collisions, follow `reference-index.md` or `symbol-index.md` rather than relative Sphinx links embedded in the original documents. Read only the references needed for the task, but do not answer exact-signature questions from a conceptual chapter alone.
