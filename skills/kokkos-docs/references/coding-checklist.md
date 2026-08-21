# Kokkos code-generation checklist

Use this as a final pass after consulting the exact source documents. It is a routing aid, not a substitute for API contracts.

## Program lifetime

- Prefer `Kokkos::ScopeGuard` where the documented constructor is suitable; otherwise pair initialization and finalization on every path.
- Destroy Kokkos-managed objects before finalization.
- Do not call Kokkos operations before initialization or after finalization.

## Views and memory

- Distinguish `View` handle assignment (aliasing/reference-count behavior) from `deep_copy` (data transfer).
- Confirm rank, dynamic/static extent order, layout, memory space, and constness.
- Use mirrors or accessible memory spaces for host access; do not assume a default-space allocation is host accessible.
- Keep unmanaged allocations alive for the full lifetime of every unmanaged view.
- Check `span_is_contiguous()` or the documented contiguity condition before passing `data()` plus `size()` as one contiguous buffer.

## Dispatch and synchronization

- Match `RangePolicy`, `MDRangePolicy`, `TeamPolicy`, nested range, work tag, and functor/lambda signatures exactly.
- `parallel_for`, `parallel_reduce`, `parallel_scan`, and copies may have different completion behavior by overload; verify the cited API.
- Fence at observable dependency boundaries, not reflexively after every kernel.
- Give kernels meaningful labels for profiling and debugging.

## Device portability

- Use the documented `KOKKOS_LAMBDA`, `KOKKOS_FUNCTION`, or `KOKKOS_INLINE_FUNCTION` form.
- Capture trivially copyable/device-valid state by value; avoid host references, host-only virtual dispatch, and unsupported standard-library calls.
- Avoid allocation, blocking synchronization, and host I/O inside kernels unless the relevant backend/API explicitly permits it.

## Reductions, scans, and atomics

- Verify the reduction value type, reducer, identity, `init`, `join`, and result location.
- For scans, distinguish accumulation from the final pass and avoid returning a value from a `void` scan lambda.
- Use atomics only for the shared update that needs them; choose fetch-versus-operation-return semantics deliberately.

## Interoperability

- For MPI, verify whether the MPI library accepts the view's memory space and whether the producing Kokkos work has completed.
- Before using `View::data()` with `View::size()` as an MPI buffer, prove contiguity with the exact View/layout/subview contract; pack otherwise.
- Complete nonblocking MPI requests before reusing or destroying buffers, and complete receive operations plus required runtime synchronization before launching consumers.
- For Fortran, verify layout, indexing, ownership, and lifetime at the language boundary.
- For CUDA/HIP/SYCL-specific integration, do not infer stream or queue ordering; consult the execution-space and fence APIs.

## Answer quality

- Cite bundled source filenames next to non-obvious constraints.
- Mention version-added/deprecated/removed status.
- Provide complete includes and lifecycle code for standalone examples.
- Separate portable code from backend-specific optional tuning.
