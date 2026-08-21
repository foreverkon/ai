# Known source caveats

Apply these verified documentation caveats before generating code.

## MPI halo exchange use case

Do not copy `source--usecases--MPI-Halo-Exchange.md` verbatim.

- Its single-message snippet assigns both `source_rank` and `destination_rank` to `1`; the blocking send has no matching receive on another rank. The receive call also passes `destination_rank` as its source argument. Choose distinct ranks and pass the actual source rank (or a deliberate wildcard).
- Its `find_subset` reduction lambda returns a value instead of accumulating into `local_sum`. A Kokkos reduction callable must update its reduction reference according to the exact `parallel_reduce` contract.
- The statement that CUDA-aware MPI should “just work” is not a portable guarantee. Check the MPI build/runtime, actual Kokkos memory space, supported backend, and stream/queue semantics.
- `View::data()` plus `View::size()` is a valid flat MPI buffer only when the represented storage is contiguous and the MPI implementation can access that memory. Consult `source--API--core--view--view.rst` for `span`, `size`, and `span_is_contiguous`; pack a noncontiguous subview or layout.
- Complete the producing Kokkos work before MPI reads a buffer. Complete MPI requests and any implementation-required device synchronization before Kokkos consumes received data or before a buffer is reused/destroyed.

## MDRange reduction wording

`source--API--core--parallel-dispatch--parallel_reduce.rst` describes indices as `i0, ..., iN` in a way that can look like rank-plus-one indices. Interpret the callable using `source--API--core--policies--MDRangePolicy.rst` and `source--ProgrammingGuide--Multi-Dimensional-Parallelism.rst`: a rank-R MDRange callable has R index parameters, followed by the reduction update reference for `parallel_reduce`.

## Tasking

`source--usecases--Tasking.md` marks its tasking facility deprecated since Kokkos 4.5 and removed in Kokkos 5.0. Do not recommend it without an explicit version constraint and migration discussion.
