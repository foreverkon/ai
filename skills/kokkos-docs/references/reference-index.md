# Kokkos reference index

The files below are unabridged Kokkos references. Use exact API documents for contracts and Programming Guide chapters for concepts.

## Fast task routing

| Task | Start with | Then verify |
|---|---|---|
| Initialize/finalize a program | `API/core/Initialize-and-Finalize.rst`, `API/core/initialize_finalize/*` | `ProgrammingGuide/Initialization.rst` |
| Define/access/copy a `View` | `API/core/view/*`, `API/core/View.rst` | `ProgrammingGuide/View.rst`, `ProgrammingGuide/Subviews.md` |
| Choose execution or memory spaces | `API/core/Spaces.rst`, `execution_spaces.rst`, `memory_spaces.rst`, `SpaceAccessibility.rst` | machine/programming model chapters |
| Write `parallel_for/reduce/scan` | `API/core/parallel-dispatch/*` | `ProgrammingGuide/ParallelDispatch.md` and custom-reduction chapters |
| Use `RangePolicy`, `MDRangePolicy`, or teams | `API/core/policies/*` | hierarchical and multidimensional guide chapters |
| Use atomics | `API/core/atomics*` | `ProgrammingGuide/Atomic-Operations.md` |
| Use reducers | `API/core/builtin_reducers.rst`, `API/core/builtinreducers/*` | custom-reduction chapters |
| Use Kokkos algorithms | `API/algorithms/*` | exact algorithm file for iterator and overload constraints |
| Use containers | `API/containers/*` | exact container file |
| Use SIMD | `API/simd/*` | `ProgrammingGuide/SIMD.md` |
| Integrate MPI/Fortran/Cabana or overlap work | `usecases/*` | re-check every used symbol in `API/` |
| Check graphs or tasking | graph guide/API/example; tasking use case | heed all deprecation/version notes |

## Same-name disambiguation

- `API/core/View.rst` is a View API landing page; `API/core/view/view.rst` is the detailed class contract; `ProgrammingGuide/View.rst` is the conceptual chapter.
- `API/core/c_style_memory_management/realloc.rst` covers raw allocation reallocation; `API/core/view/realloc.rst` covers View reallocation.
- `API/algorithms/std-algorithms/Iterators.rst` covers algorithm iterators; `API/core/view/iterators.rst` covers View iterators.

## Complete grouped index

### Entry points

- [API References](source--api-references.rst) — `api-references.rst`
- [Programming Guide](source--programmingguide.rst) — `programmingguide.rst`
- [Use Cases and Examples](source--tutorials-and-examples--use-cases-and-examples.rst) — `tutorials-and-examples/use-cases-and-examples.rst`

### Programming Guide

- [Atomic Operations](source--ProgrammingGuide--Atomic-Operations.md) — `ProgrammingGuide/Atomic-Operations.md`
- [Backwards & Future Compatibility](source--ProgrammingGuide--Compatibility.md) — `ProgrammingGuide/Compatibility.md`
- [Built-In Reducers with Custom Scalar Types](source--ProgrammingGuide--Custom-Reductions-Built-In-Reducers-with-Custom-Scalar-Types.md) — `ProgrammingGuide/Custom-Reductions-Built-In-Reducers-with-Custom-Scalar-Types.md`
- [Built-In-Reducers](source--ProgrammingGuide--Custom-Reductions-Built-In-Reducers.md) — `ProgrammingGuide/Custom-Reductions-Built-In-Reducers.md`
- [Custom Reducers](source--ProgrammingGuide--Custom-Reductions-Custom-Reducers.md) — `ProgrammingGuide/Custom-Reductions-Custom-Reducers.md`
- [Custom Reductions](source--ProgrammingGuide--Custom-Reductions.rst) — `ProgrammingGuide/Custom-Reductions.rst`
- [include "cublas_v2.h"](source--ProgrammingGuide--examples--graph_capture.cpp) — `ProgrammingGuide/examples/graph_capture.cpp`
- [Graphs](source--ProgrammingGuide--Graph.rst) — `ProgrammingGuide/Graph.rst`
- [Hierarchical Parallelism](source--ProgrammingGuide--HierarchicalParallelism.md) — `ProgrammingGuide/HierarchicalParallelism.md`
- [Initialization](source--ProgrammingGuide--Initialization.rst) — `ProgrammingGuide/Initialization.rst`
- [Interoperability and Legacy Codes](source--ProgrammingGuide--Interoperability.md) — `ProgrammingGuide/Interoperability.md`
- [Introduction](source--ProgrammingGuide--Introduction.md) — `ProgrammingGuide/Introduction.md`
- [Kokkos and Virtual Functions](source--ProgrammingGuide--Kokkos-and-Virtual-Functions.md) — `ProgrammingGuide/Kokkos-and-Virtual-Functions.md`
- [Machine Model](source--ProgrammingGuide--Machine-Model.rst) — `ProgrammingGuide/Machine-Model.rst`
- [Multi-Dimensional Parallelism](source--ProgrammingGuide--Multi-Dimensional-Parallelism.rst) — `ProgrammingGuide/Multi-Dimensional-Parallelism.rst`
- [Parallel dispatch](source--ProgrammingGuide--ParallelDispatch.md) — `ProgrammingGuide/ParallelDispatch.md`
- [Programming Model](source--ProgrammingGuide--ProgrammingModel.md) — `ProgrammingGuide/ProgrammingModel.md`
- [SIMD Types](source--ProgrammingGuide--SIMD.md) — `ProgrammingGuide/SIMD.md`
- [Subviews](source--ProgrammingGuide--Subviews.md) — `ProgrammingGuide/Subviews.md`
- [View: Multidimensional array](source--ProgrammingGuide--View.rst) — `ProgrammingGuide/View.rst`

### Use cases and examples

- [ScatterView averaging elements to nodes](source--usecases--Average-To-Nodes.md) — `usecases/Average-To-Nodes.md`
- [Fortran Interop Use Case](source--usecases--Kokkos-Fortran-Interoperability.md) — `usecases/Kokkos-Fortran-Interoperability.md`
- [Moving code from requiring ``Kokkos_ENABLE_CUDA_UVM`` to using ``SharedSpace](source--usecases--Moving_from_EnableUVM_to_SharedSpace.rst) — `usecases/Moving_from_EnableUVM_to_SharedSpace.rst`
- [MPI Halo Exchange](source--usecases--MPI-Halo-Exchange.md) — `usecases/MPI-Halo-Exchange.md`
- [Overlapping Host and Device work](source--usecases--OverlappingHostAndDeviceWork.md) — `usecases/OverlappingHostAndDeviceWork.md`
- [Array of Structures and Structure of Arrays with Cabana](source--usecases--SoA-and-AoSoA-with-Cabana.md) — `usecases/SoA-and-AoSoA-with-Cabana.md`
- [Tagged Operators](source--usecases--TaggedOperators.md) — `usecases/TaggedOperators.md`
- [Kokkos Tasking Use Case](source--usecases--Tasking.md) — `usecases/Tasking.md`

### API / Core / Detection-Idiom.rst

- [Detection Idiom](source--API--core--Detection-Idiom.rst) — `API/core/Detection-Idiom.rst`

### API / Core / Execution-Policies.rst

- [Execution Policies](source--API--core--Execution-Policies.rst) — `API/core/Execution-Policies.rst`

### API / Core / Initialize-and-Finalize.rst

- [Initialize and Finalize](source--API--core--Initialize-and-Finalize.rst) — `API/core/Initialize-and-Finalize.rst`

### API / Core / KokkosConcepts.rst

- [Kokkos Concepts](source--API--core--KokkosConcepts.rst) — `API/core/KokkosConcepts.rst`

### API / Core / Macros.rst

- [Macros](source--API--core--Macros.rst) — `API/core/Macros.rst`

### API / Core / MultiGPUSupport.rst

- [Multi-GPU Support](source--API--core--MultiGPUSupport.rst) — `API/core/MultiGPUSupport.rst`

### API / Core / Numerics.rst

- [Numerics](source--API--core--Numerics.rst) — `API/core/Numerics.rst`

### API / Core / ParallelDispatch.rst

- [Parallel Execution/Dispatch](source--API--core--ParallelDispatch.rst) — `API/core/ParallelDispatch.rst`

### API / Core / Profiling.rst

- [Profiling](source--API--core--Profiling.rst) — `API/core/Profiling.rst`

### API / Core / STL-Compatibility.rst

- [STL Compatibility Issues](source--API--core--STL-Compatibility.rst) — `API/core/STL-Compatibility.rst`

### API / Core / SpaceAccessibility.rst

- [Space Accessibility](source--API--core--SpaceAccessibility.rst) — `API/core/SpaceAccessibility.rst`

### API / Core / Spaces.rst

- [Spaces](source--API--core--Spaces.rst) — `API/core/Spaces.rst`

### API / Core / Task-Parallelism.rst

- [Task-Parallelism](source--API--core--Task-Parallelism.rst) — `API/core/Task-Parallelism.rst`

### API / Core / Traits.rst

- [Traits](source--API--core--Traits.rst) — `API/core/Traits.rst`

### API / Core / Utilities.rst

- [Utilities](source--API--core--Utilities.rst) — `API/core/Utilities.rst`

### API / Core / View.rst

- [View and related](source--API--core--View.rst) — `API/core/View.rst`

### API / Core / atomics

- [atomic_assign](source--API--core--atomics--atomic_assign.rst) — `API/core/atomics/atomic_assign.rst`
- [atomic_compare_exchange](source--API--core--atomics--atomic_compare_exchange.rst) — `API/core/atomics/atomic_compare_exchange.rst`
- [atomic_compare_exchange_strong](source--API--core--atomics--atomic_compare_exchange_strong.rst) — `API/core/atomics/atomic_compare_exchange_strong.rst`
- [atomic_exchange](source--API--core--atomics--atomic_exchange.rst) — `API/core/atomics/atomic_exchange.rst`
- [atomic_fetch_[op]](source--API--core--atomics--atomic_fetch_op.rst) — `API/core/atomics/atomic_fetch_op.rst`
- [atomic_load](source--API--core--atomics--atomic_load.rst) — `API/core/atomics/atomic_load.rst`
- [atomic_[op]](source--API--core--atomics--atomic_op.rst) — `API/core/atomics/atomic_op.rst`
- [atomic_[op]_fetch](source--API--core--atomics--atomic_op_fetch.rst) — `API/core/atomics/atomic_op_fetch.rst`
- [atomic_store](source--API--core--atomics--atomic_store.rst) — `API/core/atomics/atomic_store.rst`

### API / Core / atomics.rst

- [Atomics](source--API--core--atomics.rst) — `API/core/atomics.rst`

### API / Core / builtin_reducers.rst

- [Built-in Reducers](source--API--core--builtin_reducers.rst) — `API/core/builtin_reducers.rst`

### API / Core / builtinreducers

- [BAnd](source--API--core--builtinreducers--BAnd.rst) — `API/core/builtinreducers/BAnd.rst`
- [BOr](source--API--core--builtinreducers--BOr.rst) — `API/core/builtinreducers/BOr.rst`
- [FirstLoc](source--API--core--builtinreducers--FirstLoc.rst) — `API/core/builtinreducers/FirstLoc.rst`
- [FirstLocScalar](source--API--core--builtinreducers--FirstLocScalar.rst) — `API/core/builtinreducers/FirstLocScalar.rst`
- [LAnd](source--API--core--builtinreducers--LAnd.rst) — `API/core/builtinreducers/LAnd.rst`
- [LastLoc](source--API--core--builtinreducers--LastLoc.rst) — `API/core/builtinreducers/LastLoc.rst`
- [LastLocScalar](source--API--core--builtinreducers--LastLocScalar.rst) — `API/core/builtinreducers/LastLocScalar.rst`
- [LOr](source--API--core--builtinreducers--LOr.rst) — `API/core/builtinreducers/LOr.rst`
- [Max](source--API--core--builtinreducers--Max.rst) — `API/core/builtinreducers/Max.rst`
- [MaxFirstLoc](source--API--core--builtinreducers--MaxFirstLoc.rst) — `API/core/builtinreducers/MaxFirstLoc.rst`
- [MaxLoc](source--API--core--builtinreducers--MaxLoc.rst) — `API/core/builtinreducers/MaxLoc.rst`
- [Min](source--API--core--builtinreducers--Min.rst) — `API/core/builtinreducers/Min.rst`
- [MinFirstLoc](source--API--core--builtinreducers--MinFirstLoc.rst) — `API/core/builtinreducers/MinFirstLoc.rst`
- [MinLoc](source--API--core--builtinreducers--MinLoc.rst) — `API/core/builtinreducers/MinLoc.rst`
- [MinMax](source--API--core--builtinreducers--MinMax.rst) — `API/core/builtinreducers/MinMax.rst`
- [MinMaxFirstLastLoc](source--API--core--builtinreducers--MinMaxFirstLastLoc.rst) — `API/core/builtinreducers/MinMaxFirstLastLoc.rst`
- [MinMaxLoc](source--API--core--builtinreducers--MinMaxLoc.rst) — `API/core/builtinreducers/MinMaxLoc.rst`
- [MinMaxLocScalar](source--API--core--builtinreducers--MinMaxLocScalar.rst) — `API/core/builtinreducers/MinMaxLocScalar.rst`
- [MinMaxScalar](source--API--core--builtinreducers--MinMaxScalar.rst) — `API/core/builtinreducers/MinMaxScalar.rst`
- [Prod](source--API--core--builtinreducers--Prod.rst) — `API/core/builtinreducers/Prod.rst`
- [ReducerConcept](source--API--core--builtinreducers--ReducerConcept.rst) — `API/core/builtinreducers/ReducerConcept.rst`
- [reduction_identity](source--API--core--builtinreducers--reduction_identity.rst) — `API/core/builtinreducers/reduction_identity.rst`
- [Reduction Scalar Types](source--API--core--builtinreducers--ReductionScalarTypes.rst) — `API/core/builtinreducers/ReductionScalarTypes.rst`
- [Sum](source--API--core--builtinreducers--Sum.rst) — `API/core/builtinreducers/Sum.rst`
- [ValLocScalar](source--API--core--builtinreducers--ValLocScalar.rst) — `API/core/builtinreducers/ValLocScalar.rst`

### API / Core / c_style_memory_management

- [kokkos_free](source--API--core--c_style_memory_management--free.rst) — `API/core/c_style_memory_management/free.rst`
- [kokkos_malloc](source--API--core--c_style_memory_management--malloc.rst) — `API/core/c_style_memory_management/malloc.rst`
- [kokkos_realloc](source--API--core--c_style_memory_management--realloc.rst) — `API/core/c_style_memory_management/realloc.rst`

### API / Core / c_style_memory_management.rst

- [C-style memory management](source--API--core--c_style_memory_management.rst) — `API/core/c_style_memory_management.rst`

### API / Core / execution_spaces.rst

- [Execution Spaces](source--API--core--execution_spaces.rst) — `API/core/execution_spaces.rst`

### API / Core / initialize_finalize

- [finalize](source--API--core--initialize_finalize--finalize.rst) — `API/core/initialize_finalize/finalize.rst`
- [InitializationSettings](source--API--core--initialize_finalize--InitializationSettings.rst) — `API/core/initialize_finalize/InitializationSettings.rst`
- [initialize](source--API--core--initialize_finalize--initialize.rst) — `API/core/initialize_finalize/initialize.rst`
- [is_initialized`` and ``is_finalized](source--API--core--initialize_finalize--is_initialized_or_finalized.rst) — `API/core/initialize_finalize/is_initialized_or_finalized.rst`
- [push_finalize_hook](source--API--core--initialize_finalize--push_finalize_hook.rst) — `API/core/initialize_finalize/push_finalize_hook.rst`
- [ScopeGuard](source--API--core--initialize_finalize--ScopeGuard.rst) — `API/core/initialize_finalize/ScopeGuard.rst`

### API / Core / macros-special

- [Function Annotation Macros](source--API--core--macros-special--host_device_macros.rst) — `API/core/macros-special/host_device_macros.rst`
- [KOKKOS_IF_ON_HOST`` and ``KOKKOS_IF_ON_DEVICE](source--API--core--macros-special--if_on_host_or_device.rst) — `API/core/macros-special/if_on_host_or_device.rst`

### API / Core / memory_spaces.rst

- [Memory Spaces](source--API--core--memory_spaces.rst) — `API/core/memory_spaces.rst`

### API / Core / numerics

- [Bit manipulation](source--API--core--numerics--bit-manipulation.rst) — `API/core/numerics/bit-manipulation.rst`
- [complex](source--API--core--numerics--complex.rst) — `API/core/numerics/complex.rst`
- [Half precision types](source--API--core--numerics--half-precision-types.rst) — `API/core/numerics/half-precision-types.rst`
- [Mathematical constants](source--API--core--numerics--mathematical-constants.rst) — `API/core/numerics/mathematical-constants.rst`
- [Common math functions](source--API--core--numerics--mathematical-functions.rst) — `API/core/numerics/mathematical-functions.rst`
- [Numeric traits](source--API--core--numerics--numeric-traits.rst) — `API/core/numerics/numeric-traits.rst`

### API / Core / parallel-dispatch

- [fence](source--API--core--parallel-dispatch--fence.rst) — `API/core/parallel-dispatch/fence.rst`
- [parallel_for](source--API--core--parallel-dispatch--parallel_for.rst) — `API/core/parallel-dispatch/parallel_for.rst`
- [parallel_reduce](source--API--core--parallel-dispatch--parallel_reduce.rst) — `API/core/parallel-dispatch/parallel_reduce.rst`
- [parallel_scan](source--API--core--parallel-dispatch--parallel_scan.rst) — `API/core/parallel-dispatch/parallel_scan.rst`
- [ParallelForTag](source--API--core--parallel-dispatch--ParallelForTag.rst) — `API/core/parallel-dispatch/ParallelForTag.rst`
- [ParallelReduceTag](source--API--core--parallel-dispatch--ParallelReduceTag.rst) — `API/core/parallel-dispatch/ParallelReduceTag.rst`
- [ParallelScanTag](source--API--core--parallel-dispatch--ParallelScanTag.rst) — `API/core/parallel-dispatch/ParallelScanTag.rst`

### API / Core / policies

- [ExecutionPolicy](source--API--core--policies--ExecutionPolicyConcept.rst) — `API/core/policies/ExecutionPolicyConcept.rst`
- [MDRangePolicy](source--API--core--policies--MDRangePolicy.rst) — `API/core/policies/MDRangePolicy.rst`
- [NestedPolicies](source--API--core--policies--NestedPolicies.rst) — `API/core/policies/NestedPolicies.rst`
- [RangePolicy](source--API--core--policies--RangePolicy.rst) — `API/core/policies/RangePolicy.rst`
- [TeamHandleConcept](source--API--core--policies--TeamHandleConcept.rst) — `API/core/policies/TeamHandleConcept.rst`
- [TeamPolicy](source--API--core--policies--TeamPolicy.rst) — `API/core/policies/TeamPolicy.rst`
- [TeamThreadMDRange](source--API--core--policies--TeamThreadMDRange.rst) — `API/core/policies/TeamThreadMDRange.rst`
- [TeamThreadRange](source--API--core--policies--TeamThreadRange.rst) — `API/core/policies/TeamThreadRange.rst`
- [TeamVectorMDRange](source--API--core--policies--TeamVectorMDRange.rst) — `API/core/policies/TeamVectorMDRange.rst`
- [TeamVectorRange](source--API--core--policies--TeamVectorRange.rst) — `API/core/policies/TeamVectorRange.rst`
- [ThreadVectorMDRange](source--API--core--policies--ThreadVectorMDRange.rst) — `API/core/policies/ThreadVectorMDRange.rst`
- [ThreadVectorRange](source--API--core--policies--ThreadVectorRange.rst) — `API/core/policies/ThreadVectorRange.rst`

### API / Core / profiling

- [Profiling::ProfilingSection](source--API--core--profiling--profiling_section.rst) — `API/core/profiling/profiling_section.rst`
- [Profiling::ScopedRegion](source--API--core--profiling--scoped_region.rst) — `API/core/profiling/scoped_region.rst`

### API / Core / spaces

- [partition_space](source--API--core--spaces--partition_space.rst) — `API/core/spaces/partition_space.rst`

### API / Core / stl-compat

- [Array](source--API--core--stl-compat--Array.rst) — `API/core/stl-compat/Array.rst`
- [pair](source--API--core--stl-compat--pair.md) — `API/core/stl-compat/pair.md`

### API / Core / utilities

- [abort](source--API--core--utilities--abort.rst) — `API/core/utilities/abort.rst`
- [KOKKOS_ASSERT](source--API--core--utilities--assert.rst) — `API/core/utilities/assert.rst`
- [device_id](source--API--core--utilities--device_id.rst) — `API/core/utilities/device_id.rst`
- [Minimum/maximum operations](source--API--core--utilities--min_max_clamp.rst) — `API/core/utilities/min_max_clamp.rst`
- [num_devices](source--API--core--utilities--num_devices.rst) — `API/core/utilities/num_devices.rst`
- [num_threads](source--API--core--utilities--num_threads.rst) — `API/core/utilities/num_threads.rst`
- [printf](source--API--core--utilities--printf.rst) — `API/core/utilities/printf.rst`
- [kokkos_swap](source--API--core--utilities--swap.rst) — `API/core/utilities/swap.rst`
- [Timer](source--API--core--utilities--timer.rst) — `API/core/utilities/timer.rst`

### API / Core / view

- [ALL``, ``ALL_t](source--API--core--view--ALL.rst) — `API/core/view/ALL.rst`
- [create_mirror[_view]](source--API--core--view--create_mirror.rst) — `API/core/view/create_mirror.rst`
- [deep_copy](source--API--core--view--deep_copy.rst) — `API/core/view/deep_copy.rst`
- [Iterators](source--API--core--view--iterators.rst) — `API/core/view/iterators.rst`
- [LayoutLeft](source--API--core--view--layoutLeft.rst) — `API/core/view/layoutLeft.rst`
- [LayoutRight](source--API--core--view--layoutRight.rst) — `API/core/view/layoutRight.rst`
- [LayoutStride](source--API--core--view--layoutStride.rst) — `API/core/view/layoutStride.rst`
- [MemoryTraits](source--API--core--view--memoryTraits.rst) — `API/core/view/memoryTraits.rst`
- [realloc](source--API--core--view--realloc.rst) — `API/core/view/realloc.rst`
- [resize](source--API--core--view--resize.rst) — `API/core/view/resize.rst`
- [subview](source--API--core--view--subview.rst) — `API/core/view/subview.rst`
- [Subview](source--API--core--view--Subview_type.rst) — `API/core/view/Subview_type.rst`
- [View](source--API--core--view--view.rst) — `API/core/view/view.rst`
- [view_alloc](source--API--core--view--view_alloc.rst) — `API/core/view/view_alloc.rst`
- [View-like Types](source--API--core--view--view_like.rst) — `API/core/view/view_like.rst`

### API / algorithms

- [Random-Number](source--API--algorithms--Random-Number.rst) — `API/algorithms/Random-Number.rst`
- [Sort](source--API--algorithms--Sort.rst) — `API/algorithms/Sort.rst`
- [Std Algorithms](source--API--algorithms--std-algorithms-index.rst) — `API/algorithms/std-algorithms-index.rst`
- [adjacent_difference](source--API--algorithms--std-algorithms--all--StdAdjacentDifference.md) — `API/algorithms/std-algorithms/all/StdAdjacentDifference.md`
- [adjacent_find](source--API--algorithms--std-algorithms--all--StdAdjacentFind.rst) — `API/algorithms/std-algorithms/all/StdAdjacentFind.rst`
- [all_of](source--API--algorithms--std-algorithms--all--StdAllOf.rst) — `API/algorithms/std-algorithms/all/StdAllOf.rst`
- [any_of](source--API--algorithms--std-algorithms--all--StdAnyOf.rst) — `API/algorithms/std-algorithms/all/StdAnyOf.rst`
- [copy](source--API--algorithms--std-algorithms--all--StdCopy.rst) — `API/algorithms/std-algorithms/all/StdCopy.rst`
- [copy_n](source--API--algorithms--std-algorithms--all--StdCopy_n.rst) — `API/algorithms/std-algorithms/all/StdCopy_n.rst`
- [copy_backward](source--API--algorithms--std-algorithms--all--StdCopyBackward.rst) — `API/algorithms/std-algorithms/all/StdCopyBackward.rst`
- [copy_if](source--API--algorithms--std-algorithms--all--StdCopyIf.rst) — `API/algorithms/std-algorithms/all/StdCopyIf.rst`
- [count](source--API--algorithms--std-algorithms--all--StdCount.rst) — `API/algorithms/std-algorithms/all/StdCount.rst`
- [count_if](source--API--algorithms--std-algorithms--all--StdCountIf.rst) — `API/algorithms/std-algorithms/all/StdCountIf.rst`
- [equal](source--API--algorithms--std-algorithms--all--StdEqual.rst) — `API/algorithms/std-algorithms/all/StdEqual.rst`
- [exclusive_scan](source--API--algorithms--std-algorithms--all--StdExclusiveScan.md) — `API/algorithms/std-algorithms/all/StdExclusiveScan.md`
- [fill](source--API--algorithms--std-algorithms--all--StdFill.md) — `API/algorithms/std-algorithms/all/StdFill.md`
- [fill_n](source--API--algorithms--std-algorithms--all--StdFill_n.md) — `API/algorithms/std-algorithms/all/StdFill_n.md`
- [find](source--API--algorithms--std-algorithms--all--StdFind.rst) — `API/algorithms/std-algorithms/all/StdFind.rst`
- [find_end](source--API--algorithms--std-algorithms--all--StdFindEnd.rst) — `API/algorithms/std-algorithms/all/StdFindEnd.rst`
- [find_first_of](source--API--algorithms--std-algorithms--all--StdFindFirstOf.rst) — `API/algorithms/std-algorithms/all/StdFindFirstOf.rst`
- [find_if](source--API--algorithms--std-algorithms--all--StdFindIf.rst) — `API/algorithms/std-algorithms/all/StdFindIf.rst`
- [find_if_not](source--API--algorithms--std-algorithms--all--StdFindIfNot.rst) — `API/algorithms/std-algorithms/all/StdFindIfNot.rst`
- [for_each](source--API--algorithms--std-algorithms--all--StdForEach.md) — `API/algorithms/std-algorithms/all/StdForEach.md`
- [for_each_n](source--API--algorithms--std-algorithms--all--StdForEachN.md) — `API/algorithms/std-algorithms/all/StdForEachN.md`
- [generate](source--API--algorithms--std-algorithms--all--StdGenerate.rst) — `API/algorithms/std-algorithms/all/StdGenerate.rst`
- [generate_n](source--API--algorithms--std-algorithms--all--StdGenerate_n.rst) — `API/algorithms/std-algorithms/all/StdGenerate_n.rst`
- [inclusive_scan](source--API--algorithms--std-algorithms--all--StdInclusiveScan.md) — `API/algorithms/std-algorithms/all/StdInclusiveScan.md`
- [is_partitioned](source--API--algorithms--std-algorithms--all--StdIsPartitioned.rst) — `API/algorithms/std-algorithms/all/StdIsPartitioned.rst`
- [is_sorted](source--API--algorithms--std-algorithms--all--StdIsSorted.rst) — `API/algorithms/std-algorithms/all/StdIsSorted.rst`
- [is_sorted_until](source--API--algorithms--std-algorithms--all--StdIsSortedUntil.rst) — `API/algorithms/std-algorithms/all/StdIsSortedUntil.rst`
- [lexicographical_compare](source--API--algorithms--std-algorithms--all--StdLexicographicalCompare.md) — `API/algorithms/std-algorithms/all/StdLexicographicalCompare.md`
- [max_element](source--API--algorithms--std-algorithms--all--StdMaxElement.rst) — `API/algorithms/std-algorithms/all/StdMaxElement.rst`
- [min_element](source--API--algorithms--std-algorithms--all--StdMinElement.rst) — `API/algorithms/std-algorithms/all/StdMinElement.rst`
- [minmax_element](source--API--algorithms--std-algorithms--all--StdMinMaxElement.rst) — `API/algorithms/std-algorithms/all/StdMinMaxElement.rst`
- [mismatch](source--API--algorithms--std-algorithms--all--StdMismatch.md) — `API/algorithms/std-algorithms/all/StdMismatch.md`
- [move](source--API--algorithms--std-algorithms--all--StdMove.rst) — `API/algorithms/std-algorithms/all/StdMove.rst`
- [move_backward](source--API--algorithms--std-algorithms--all--StdMoveBackward.rst) — `API/algorithms/std-algorithms/all/StdMoveBackward.rst`
- [none_of](source--API--algorithms--std-algorithms--all--StdNoneOf.rst) — `API/algorithms/std-algorithms/all/StdNoneOf.rst`
- [partition_copy](source--API--algorithms--std-algorithms--all--StdPartitionCopy.rst) — `API/algorithms/std-algorithms/all/StdPartitionCopy.rst`
- [partition_point](source--API--algorithms--std-algorithms--all--StdPartitionPoint.md) — `API/algorithms/std-algorithms/all/StdPartitionPoint.md`
- [reduce](source--API--algorithms--std-algorithms--all--StdReduce.md) — `API/algorithms/std-algorithms/all/StdReduce.md`
- [remove](source--API--algorithms--std-algorithms--all--StdRemove.rst) — `API/algorithms/std-algorithms/all/StdRemove.rst`
- [remove_copy](source--API--algorithms--std-algorithms--all--StdRemoveCopy.rst) — `API/algorithms/std-algorithms/all/StdRemoveCopy.rst`
- [remove_copy_if](source--API--algorithms--std-algorithms--all--StdRemoveCopyIf.rst) — `API/algorithms/std-algorithms/all/StdRemoveCopyIf.rst`
- [remove_if](source--API--algorithms--std-algorithms--all--StdRemoveIf.rst) — `API/algorithms/std-algorithms/all/StdRemoveIf.rst`
- [replace](source--API--algorithms--std-algorithms--all--StdReplace.md) — `API/algorithms/std-algorithms/all/StdReplace.md`
- [replace_copy](source--API--algorithms--std-algorithms--all--StdReplaceCopy.md) — `API/algorithms/std-algorithms/all/StdReplaceCopy.md`
- [replace_copy_if](source--API--algorithms--std-algorithms--all--StdReplaceCopyIf.md) — `API/algorithms/std-algorithms/all/StdReplaceCopyIf.md`
- [replace_if](source--API--algorithms--std-algorithms--all--StdReplaceIf.md) — `API/algorithms/std-algorithms/all/StdReplaceIf.md`
- [reverse](source--API--algorithms--std-algorithms--all--StdReverse.rst) — `API/algorithms/std-algorithms/all/StdReverse.rst`
- [reverse_copy](source--API--algorithms--std-algorithms--all--StdReverseCopy.rst) — `API/algorithms/std-algorithms/all/StdReverseCopy.rst`
- [rotate](source--API--algorithms--std-algorithms--all--StdRotate.rst) — `API/algorithms/std-algorithms/all/StdRotate.rst`
- [rotate_copy](source--API--algorithms--std-algorithms--all--StdRotateCopy.rst) — `API/algorithms/std-algorithms/all/StdRotateCopy.rst`
- [search](source--API--algorithms--std-algorithms--all--StdSearch.md) — `API/algorithms/std-algorithms/all/StdSearch.md`
- [search_n](source--API--algorithms--std-algorithms--all--StdSearchN.md) — `API/algorithms/std-algorithms/all/StdSearchN.md`
- [shift_left](source--API--algorithms--std-algorithms--all--StdShiftLeft.rst) — `API/algorithms/std-algorithms/all/StdShiftLeft.rst`
- [shift_right](source--API--algorithms--std-algorithms--all--StdShiftRight.rst) — `API/algorithms/std-algorithms/all/StdShiftRight.rst`
- [swap_ranges](source--API--algorithms--std-algorithms--all--StdSwapRanges.rst) — `API/algorithms/std-algorithms/all/StdSwapRanges.rst`
- [transform](source--API--algorithms--std-algorithms--all--StdTransform.rst) — `API/algorithms/std-algorithms/all/StdTransform.rst`
- [transform_exclusive_scan](source--API--algorithms--std-algorithms--all--StdTransformExclusiveScan.md) — `API/algorithms/std-algorithms/all/StdTransformExclusiveScan.md`
- [transform_inclusive_scan](source--API--algorithms--std-algorithms--all--StdTransformInclusiveScan.md) — `API/algorithms/std-algorithms/all/StdTransformInclusiveScan.md`
- [transform_reduce](source--API--algorithms--std-algorithms--all--StdTransformReduce.md) — `API/algorithms/std-algorithms/all/StdTransformReduce.md`
- [unique](source--API--algorithms--std-algorithms--all--StdUnique.rst) — `API/algorithms/std-algorithms/all/StdUnique.rst`
- [unique_copy](source--API--algorithms--std-algorithms--all--StdUniqueCopy.rst) — `API/algorithms/std-algorithms/all/StdUniqueCopy.rst`
- [Iterators](source--API--algorithms--std-algorithms--Iterators.rst) — `API/algorithms/std-algorithms/Iterators.rst`
- [Minimum/maximum](source--API--algorithms--std-algorithms--StdMinMaxElement.rst) — `API/algorithms/std-algorithms/StdMinMaxElement.rst`
- [Modifying Sequence](source--API--algorithms--std-algorithms--StdModSeq.rst) — `API/algorithms/std-algorithms/StdModSeq.rst`
- [Non-modifying Sequence](source--API--algorithms--std-algorithms--StdNonModSeq.rst) — `API/algorithms/std-algorithms/StdNonModSeq.rst`
- [Numeric](source--API--algorithms--std-algorithms--StdNumeric.rst) — `API/algorithms/std-algorithms/StdNumeric.rst`
- [Partitioning](source--API--algorithms--std-algorithms--StdPartitioningOps.rst) — `API/algorithms/std-algorithms/StdPartitioningOps.rst`
- [Sorting](source--API--algorithms--std-algorithms--StdSorting.rst) — `API/algorithms/std-algorithms/StdSorting.rst`

### API / algorithms-index.rst

- [Algorithms API](source--API--algorithms-index.rst) — `API/algorithms-index.rst`

### API / containers

- [Bitset](source--API--containers--Bitset.rst) — `API/containers/Bitset.rst`
- [DualView](source--API--containers--DualView.rst) — `API/containers/DualView.rst`
- [DynamicView](source--API--containers--DynamicView.rst) — `API/containers/DynamicView.rst`
- [DynRankView](source--API--containers--DynRankView.rst) — `API/containers/DynRankView.rst`
- [ErrorReporter](source--API--containers--ErrorReporter.rst) — `API/containers/ErrorReporter.rst`
- [OffsetView](source--API--containers--Offset-View.rst) — `API/containers/Offset-View.rst`
- [ScatterView](source--API--containers--ScatterView.rst) — `API/containers/ScatterView.rst`
- [StaticCrsGraph`` [DEPRECATED]](source--API--containers--StaticCrsGraph.rst) — `API/containers/StaticCrsGraph.rst`
- [UnorderedMap](source--API--containers--Unordered-Map.rst) — `API/containers/Unordered-Map.rst`
- [vector`` [DEPRECATED]](source--API--containers--vector.rst) — `API/containers/vector.rst`

### API / containers-index.rst

- [Containers API](source--API--containers-index.rst) — `API/containers-index.rst`

### API / core-index.rst

- [Core API](source--API--core-index.rst) — `API/core-index.rst`

### API / simd

- [Experimental::simd](source--API--simd--simd.md) — `API/simd/simd.md`
- [Experimental::simd_mask](source--API--simd--simd_mask.md) — `API/simd/simd_mask.md`
- [Experimental::where_expression](source--API--simd--where_expression.md) — `API/simd/where_expression.md`

### API / simd-index.rst

- [SIMD API](source--API--simd-index.rst) — `API/simd-index.rst`
