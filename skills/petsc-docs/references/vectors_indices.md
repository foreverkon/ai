# Petsc-Docs-Full-Raw - Vectors Indices

**Pages:** 559

---

## Index sets (IS)#

**URL:** https://petsc.org/release/manualpages/IS/

**Contents:**
- Index sets (IS)#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Single list of manual pages#

IS objects are used to index into vectors and matrices and to setup vector scatters. Users guide section: Low-level Vector Communication

ISGeneralSetIndicesFromMask

ISGlobalToLocalMappingMode

ISLOCALTOGLOBALMAPPINGBASIC

ISLOCALTOGLOBALMAPPINGHASH

ISLocalToGlobalMappingType

ISBlockRestoreIndices

ISColoringViewFromOptions

ISCompressIndicesGeneral

ISExpandIndicesGeneral

ISLocalToGlobalMapping

ISLocalToGlobalMappingGetType

ISLocalToGlobalMappingLoad

ISLocalToGlobalMappingSetType

ISLocalToGlobalMappingView

ISLocalToGlobalMappingViewFromOptions

ISRestoreNonlocalIndices

ISRestoreTotalIndices

ISGlobalToLocalMappingApply

ISGlobalToLocalMappingApplyBlock

ISGlobalToLocalMappingApplyIS

ISLocalToGlobalMappingApply

ISLocalToGlobalMappingApplyBlock

ISLocalToGlobalMappingApplyIS

ISLocalToGlobalMappingConcatenate

ISLocalToGlobalMappingCreate

ISLocalToGlobalMappingCreateIS

ISLocalToGlobalMappingCreateSF

ISLocalToGlobalMappingDestroy

ISLocalToGlobalMappingDuplicate

ISLocalToGlobalMappingGetBlockIndices

ISLocalToGlobalMappingGetBlockInfo

ISLocalToGlobalMappingGetBlockMultiLeavesSF

ISLocalToGlobalMappingGetBlockNodeInfo

ISLocalToGlobalMappingGetBlockSize

ISLocalToGlobalMappingGetIndices

ISLocalToGlobalMappingGetInfo

ISLocalToGlobalMappingGetNodeInfo

ISLocalToGlobalMappingGetSize

ISLocalToGlobalMappingRegister

ISLocalToGlobalMappingRegisterAll

ISLocalToGlobalMappingRestoreBlockIndices

ISLocalToGlobalMappingRestoreBlockInfo

ISLocalToGlobalMappingRestoreBlockNodeInfo

ISLocalToGlobalMappingRestoreIndices

ISLocalToGlobalMappingRestoreInfo

ISLocalToGlobalMappingRestoreNodeInfo

ISLocalToGlobalMappingSetBlockSize

ISLocalToGlobalMappingSetFromOptions

ISPartitioningToNumbering

PetscKDTreeQueryPointsNearestNeighbor

PetscLayoutCreateFromSizes

PetscLayoutCreateFromRanges

PetscLayoutFindOwnerIndex

PetscLayoutGetBlockSize

PetscLayoutGetLocalSize

PetscLayoutSetBlockSize

PetscLayoutSetISLocalToGlobalMapping

PetscLayoutSetLocalSize

ISBlockRestoreIndices

ISColoringViewFromOptions

ISCompressIndicesGeneral

ISExpandIndicesGeneral

ISGeneralSetIndicesFromMask

ISGlobalToLocalMappingApply

ISGlobalToLocalMappingApplyBlock

ISGlobalToLocalMappingApplyIS

ISGlobalToLocalMappingMode

ISLOCALTOGLOBALMAPPINGBASIC

ISLOCALTOGLOBALMAPPINGHASH

ISLocalToGlobalMapping

ISLocalToGlobalMappingApply

ISLocalToGlobalMappingApplyBlock

ISLocalToGlobalMappingApplyIS

ISLocalToGlobalMappingConcatenate

ISLocalToGlobalMappingCreate

ISLocalToGlobalMappingCreateIS

ISLocalToGlobalMappingCreateSF

ISLocalToGlobalMappingDestroy

ISLocalToGlobalMappingDuplicate

ISLocalToGlobalMappingGetBlockIndices

ISLocalToGlobalMappingGetBlockInfo

ISLocalToGlobalMappingGetBlockMultiLeavesSF

ISLocalToGlobalMappingGetBlockNodeInfo

ISLocalToGlobalMappingGetBlockSize

ISLocalToGlobalMappingGetIndices

ISLocalToGlobalMappingGetInfo

ISLocalToGlobalMappingGetNodeInfo

ISLocalToGlobalMappingGetSize

ISLocalToGlobalMappingGetType

ISLocalToGlobalMappingLoad

ISLocalToGlobalMappingRegister

ISLocalToGlobalMappingRegisterAll

ISLocalToGlobalMappingRestoreBlockIndices

ISLocalToGlobalMappingRestoreBlockInfo

ISLocalToGlobalMappingRestoreBlockNodeInfo

ISLocalToGlobalMappingRestoreIndices

ISLocalToGlobalMappingRestoreInfo

ISLocalToGlobalMappingRestoreNodeInfo

ISLocalToGlobalMappingSetBlockSize

ISLocalToGlobalMappingSetFromOptions

ISLocalToGlobalMappingSetType

ISLocalToGlobalMappingType

ISLocalToGlobalMappingView

ISLocalToGlobalMappingViewFromOptions

ISPartitioningToNumbering

ISRestoreNonlocalIndices

ISRestoreTotalIndices

PetscKDTreeQueryPointsNearestNeighbor

PetscLayoutCreateFromRanges

PetscLayoutCreateFromSizes

PetscLayoutFindOwnerIndex

PetscLayoutGetBlockSize

PetscLayoutGetLocalSize

PetscLayoutSetBlockSize

PetscLayoutSetISLocalToGlobalMapping

PetscLayoutSetLocalSize

Vector Operations (Vec)

Matrices and Matrix Operations

---

## ISAllGatherColors#

**URL:** https://petsc.org/release/manualpages/IS/ISAllGatherColors/

**Contents:**
- ISAllGatherColors#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Given a set of colors on each processor, generates a large set (same on each processor) by concatenating together each processors colors

comm - communicator to share the indices

n - local size of set

lindices - local colors

outN - total number of indices

outindices - all of the colors

ISAllGatherColors() is clearly not scalable for large index sets.

ISColoringValue, ISColoring(), ISCreateGeneral(), ISCreateStride(), ISCreateBlock(), ISAllGather()

src/vec/is/is/utils/iscoloring.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISAllGatherColors(MPI_Comm comm, PetscInt n, ISColoringValue lindices[], PetscInt *outN, ISColoringValue *outindices[])
```

Example 2 (unknown):
```unknown
ISAllGatherColors()
```

Example 3 (unknown):
```unknown
ISColoringValue
```

Example 4 (unknown):
```unknown
ISColoring()
```

---

## ISAllGather#

**URL:** https://petsc.org/release/manualpages/IS/ISAllGather/

**Contents:**
- ISAllGather#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Given an index set IS on each processor, generates a large index set (same on each processor) by concatenating together each processors index set.

is - the distributed index set

isout - the concatenated index set (same on all processors)

ISAllGather() is clearly not scalable for large index sets.

The IS created on each processor must be created with a common communicator (e.g., PETSC_COMM_WORLD). If the index sets were created with PETSC_COMM_SELF, this routine will not work as expected, since each process will generate its own new IS that consists only of itself.

The communicator for this new IS is PETSC_COMM_SELF

Low-level Vector Communication, IS, ISCreateGeneral(), ISCreateStride(), ISCreateBlock()

src/vec/is/is/utils/iscoloring.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISAllGather(IS is, IS *isout)
```

Example 2 (unknown):
```unknown
ISAllGather()
```

Example 3 (unknown):
```unknown
PETSC_COMM_WORLD
```

Example 4 (unknown):
```unknown
PETSC_COMM_SELF
```

---

## ISBlockGetIndices#

**URL:** https://petsc.org/release/manualpages/IS/ISBlockGetIndices/

**Contents:**
- ISBlockGetIndices#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Gets the indices associated with each block in an ISBLOCK

idx - the integer indices, one for each block and count of block not indices

Call ISBlockRestoreIndices() when you no longer need access to the indices

Low-level Vector Communication, IS, ISBLOCK, ISGetIndices(), ISBlockRestoreIndices(), ISBlockSetIndices(), ISCreateBlock()

src/vec/is/is/impls/block/block.c

src/vec/is/is/tutorials/ex3.c src/vec/is/is/tutorials/ex3f90.F90

ISBlockGetIndices_Block() in src/vec/is/is/impls/block/block.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"     
PetscErrorCode ISBlockGetIndices(IS is, const PetscInt *idx[])
```

Example 2 (unknown):
```unknown
ISBlockRestoreIndices()
```

Example 3 (julia):
```julia
PetscInt, pointer :: idx(:)
```

Example 4 (unknown):
```unknown
ISGetIndices()
```

---

## ISBlockGetLocalSize#

**URL:** https://petsc.org/release/manualpages/IS/ISBlockGetLocalSize/

**Contents:**
- ISBlockGetLocalSize#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Returns the local number of blocks in the index set of ISType ISBLOCK

size - the local number of blocks

Low-level Vector Communication, IS, ISGetBlockSize(), ISBlockGetSize(), ISGetSize(), ISCreateBlock(), ISBLOCK

src/vec/is/is/impls/block/block.c

src/vec/is/is/tutorials/ex3.c src/vec/is/is/tutorials/ex3f90.F90

ISBlockGetLocalSize_Block() in src/vec/is/is/impls/block/block.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"     
PetscErrorCode ISBlockGetLocalSize(IS is, PetscInt *size)
```

Example 2 (unknown):
```unknown
ISGetBlockSize()
```

Example 3 (unknown):
```unknown
ISBlockGetSize()
```

Example 4 (unknown):
```unknown
ISGetSize()
```

---

## ISBlockGetSize#

**URL:** https://petsc.org/release/manualpages/IS/ISBlockGetSize/

**Contents:**
- ISBlockGetSize#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Returns the global number of blocks in parallel in the index set of ISType ISBLOCK

size - the global number of blocks

Low-level Vector Communication, IS, ISGetBlockSize(), ISBlockGetLocalSize(), ISGetSize(), ISCreateBlock(), ISBLOCK

src/vec/is/is/impls/block/block.c

ISBlockGetSize_Block() in src/vec/is/is/impls/block/block.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"     
PetscErrorCode ISBlockGetSize(IS is, PetscInt *size)
```

Example 2 (unknown):
```unknown
ISGetBlockSize()
```

Example 3 (unknown):
```unknown
ISBlockGetLocalSize()
```

Example 4 (unknown):
```unknown
ISGetSize()
```

---

## ISBlockRestoreIndices#

**URL:** https://petsc.org/release/manualpages/IS/ISBlockRestoreIndices/

**Contents:**
- ISBlockRestoreIndices#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Restores the indices associated with each block in an ISBLOCK obtained with ISBlockGetIndices()

idx - the integer indices

Low-level Vector Communication, IS, ISBLOCK, ISRestoreIndices(), ISBlockGetIndices()

src/vec/is/is/impls/block/block.c

src/vec/is/is/tutorials/ex3.c src/vec/is/is/tutorials/ex3f90.F90

ISBlockRestoreIndices_Block() in src/vec/is/is/impls/block/block.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISBlockGetIndices()
```

Example 2 (unknown):
```unknown
#include "petscis.h"     
PetscErrorCode ISBlockRestoreIndices(IS is, const PetscInt *idx[])
```

Example 3 (julia):
```julia
PetscInt, pointer :: idx(:)
```

Example 4 (unknown):
```unknown
ISRestoreIndices()
```

---

## ISBlockSetIndices#

**URL:** https://petsc.org/release/manualpages/IS/ISBlockSetIndices/

**Contents:**
- ISBlockSetIndices#
- Synopsis#
- Input Parameters#
- Notes#
- Example#
- See Also#
- Level#
- Location#
- Implementations#

Set integers representing blocks of indices in an index set of ISType ISBLOCK

bs - number of elements in each block

n - the length of the index set (the number of blocks)

idx - the list of integers, one for each block, the integers contain the index of the first index of each block divided by the block size

mode - see PetscCopyMode, only PETSC_COPY_VALUES and PETSC_OWN_POINTER are supported

When the communicator is not MPI_COMM_SELF, the operations on the index sets, IS, are NOT conceptually the same as MPI_Group operations. The index sets are then distributed sets of indices and thus certain operations on them are collective.

The convenience routine ISCreateBlock() allows one to create the IS and provide the blocks in a single function call.

If you wish to index the values {0,1,4,5}, then use a block size of 2 and idx of {0,2}.

Low-level Vector Communication, IS, ISCreateStride(), ISCreateGeneral(), ISAllGather(), ISCreateBlock(), ISBLOCK, ISGeneralSetIndices()

src/vec/is/is/impls/block/block.c

ISBlockSetIndices_Block() in src/vec/is/is/impls/block/block.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"     
PetscErrorCode ISBlockSetIndices(IS is, PetscInt bs, PetscInt n, const PetscInt idx[], PetscCopyMode mode)
```

Example 2 (unknown):
```unknown
PetscCopyMode
```

Example 3 (unknown):
```unknown
PETSC_COPY_VALUES
```

Example 4 (unknown):
```unknown
PETSC_OWN_POINTER
```

---

## ISBuildTwoSided#

**URL:** https://petsc.org/release/manualpages/IS/ISBuildTwoSided/

**Contents:**
- ISBuildTwoSided#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Takes an IS that describes where each element will be mapped globally over all ranks. Generates an IS that contains new numbers from remote or local on the IS.

ito - an IS describes to which rank each entry will be mapped. Negative target rank will be ignored

toindx - an IS describes what indices should send. NULL means sending natural numbering

rows - contains new numbers from remote or local

This manual page is incomprehensible and still needs to be fixed

Low-level Vector Communication, IS, MatPartitioningCreate(), ISPartitioningToNumbering(), ISPartitioningCount()

src/vec/is/is/utils/iscoloring.c

src/ksp/ksp/tutorials/ex64.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISBuildTwoSided(IS ito, IS toindx, IS *rows)
```

Example 2 (unknown):
```unknown
MatPartitioningCreate()
```

Example 3 (unknown):
```unknown
ISPartitioningToNumbering()
```

Example 4 (unknown):
```unknown
ISPartitioningCount()
```

---

## ISClearInfoCache#

**URL:** https://petsc.org/release/manualpages/IS/ISClearInfoCache/

**Contents:**
- ISClearInfoCache#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

clear the cache of computed index set properties

clear_permanent_local - whether to remove the permanent status of local properties

Because all processes must agree on the global permanent status of a property, the permanent status can only be changed with ISSetInfo(), because this routine is not collective

IS, ISInfo, ISInfoType, ISSetInfo()

src/vec/is/is/interface/index.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISClearInfoCache(IS is, PetscBool clear_permanent_local)
```

Example 2 (unknown):
```unknown
ISSetInfo()
```

Example 3 (unknown):
```unknown
ISSetInfo()
```

---

## ISColoringCreate#

**URL:** https://petsc.org/release/manualpages/IS/ISColoringCreate/

**Contents:**
- ISColoringCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Generates an ISColoring context from lists (provided by each MPI process) of colors for each node.

comm - communicator for the processors creating the coloring

ncolors - max color value

n - number of nodes on this processor

colors - array containing the colors for this MPI rank, color numbers begin at 0, for each local node

mode - see PetscCopyMode for meaning of this flag.

iscoloring - the resulting coloring data structure

-is_coloring_view - Activates ISColoringView()

By default sets coloring type to IS_COLORING_GLOBAL

ISColoring, ISColoringValue, MatColoringCreate(), ISColoringView(), ISColoringDestroy(), ISColoringSetType()

src/vec/is/is/utils/iscoloring.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISColoringCreate(MPI_Comm comm, PetscInt ncolors, PetscInt n, const ISColoringValue colors[], PetscCopyMode mode, ISColoring *iscoloring)
```

Example 2 (unknown):
```unknown
PetscCopyMode
```

Example 3 (unknown):
```unknown
ISColoringView()
```

Example 4 (unknown):
```unknown
IS_COLORING_GLOBAL
```

---

## ISColoringDestroy#

**URL:** https://petsc.org/release/manualpages/IS/ISColoringDestroy/

**Contents:**
- ISColoringDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#

Destroys an ISColoring coloring context.

iscoloring - the coloring context

ISColoring, ISColoringView(), MatColoring

src/vec/is/is/utils/iscoloring.c

src/mat/tutorials/ex16.c src/snes/tutorials/ex14.c src/tao/unconstrained/tutorials/minsurf2.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISColoringDestroy(ISColoring *iscoloring)
```

Example 2 (unknown):
```unknown
ISColoringView()
```

Example 3 (unknown):
```unknown
MatColoring
```

---

## ISColoringGetColors#

**URL:** https://petsc.org/release/manualpages/IS/ISColoringGetColors/

**Contents:**
- ISColoringGetColors#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Returns an array with the color for each local node

iscoloring - the coloring context

nc - number of colors

colors - color for each node

Do not free the colors array.

The colors array will only be valid for the lifetime of the ISColoring

ISColoring, ISColoringValue, ISColoringRestoreIS(), ISColoringView(), ISColoringGetIS()

src/vec/is/is/utils/iscoloring.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISColoringGetColors(ISColoring iscoloring, PetscInt *n, PetscInt *nc, const ISColoringValue **colors)
```

Example 2 (unknown):
```unknown
ISColoringValue
```

Example 3 (unknown):
```unknown
ISColoringRestoreIS()
```

Example 4 (unknown):
```unknown
ISColoringView()
```

---

## ISColoringGetIS#

**URL:** https://petsc.org/release/manualpages/IS/ISColoringGetIS/

**Contents:**
- ISColoringGetIS#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Extracts index sets from the coloring context. Each is contains the nodes of one color

iscoloring - the coloring context

mode - if this value is PETSC_OWN_POINTER then the caller owns the pointer and must free the array of IS and each IS in the array

nn - number of index sets in the coloring context

isis - array of index sets

If mode is PETSC_USE_POINTER then ISColoringRestoreIS() must be called when the IS are no longer needed

ISColoring, IS, ISColoringRestoreIS(), ISColoringView(), ISColoringGetColoring(), ISColoringGetColors()

src/vec/is/is/utils/iscoloring.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISColoringGetIS(ISColoring iscoloring, PetscCopyMode mode, PetscInt *nn, IS *isis[])
```

Example 2 (unknown):
```unknown
PETSC_OWN_POINTER
```

Example 3 (unknown):
```unknown
PETSC_USE_POINTER
```

Example 4 (unknown):
```unknown
ISColoringRestoreIS()
```

---

## ISColoringGetType#

**URL:** https://petsc.org/release/manualpages/IS/ISColoringGetType/

**Contents:**
- ISColoringGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

gets if the coloring is for the local representation (including ghost points) or the global representation

coloring - the coloring object

type - either IS_COLORING_LOCAL or IS_COLORING_GLOBAL

MatFDColoringCreate(), ISColoring, ISColoringType, ISColoringCreate(), IS_COLORING_LOCAL, IS_COLORING_GLOBAL, ISColoringSetType()

src/vec/is/is/utils/iscoloring.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISColoringGetType(ISColoring coloring, ISColoringType *type)
```

Example 2 (unknown):
```unknown
IS_COLORING_LOCAL
```

Example 3 (unknown):
```unknown
IS_COLORING_GLOBAL
```

Example 4 (unknown):
```unknown
MatFDColoringCreate()
```

---

## ISColoringReference#

**URL:** https://petsc.org/release/manualpages/IS/ISColoringReference/

**Contents:**
- ISColoringReference#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#

Increases the reference count of an ISColoring object by one

coloring - the ISColoring object

The reference count is decreased by a matching call to ISColoringDestroy().

ISColoring, ISColoringCreate(), ISColoringDestroy()

src/vec/is/is/utils/iscoloring.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISColoringReference(ISColoring coloring)
```

Example 2 (unknown):
```unknown
ISColoringDestroy()
```

Example 3 (unknown):
```unknown
ISColoringCreate()
```

Example 4 (unknown):
```unknown
ISColoringDestroy()
```

---

## ISColoringRestoreIS#

**URL:** https://petsc.org/release/manualpages/IS/ISColoringRestoreIS/

**Contents:**
- ISColoringRestoreIS#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Restores the index sets extracted from the coloring context with ISColoringGetIS() using PETSC_USE_POINTER

iscoloring - the coloring context

mode - who retains ownership of the is

is - array of index sets

ISColoring(), IS, ISColoringGetIS(), ISColoringView(), PetscCopyMode

src/vec/is/is/utils/iscoloring.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISColoringGetIS()
```

Example 2 (unknown):
```unknown
PETSC_USE_POINTER
```

Example 3 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISColoringRestoreIS(ISColoring iscoloring, PetscCopyMode mode, IS *is[])
```

Example 4 (unknown):
```unknown
ISColoring()
```

---

## ISColoringSetType#

**URL:** https://petsc.org/release/manualpages/IS/ISColoringSetType/

**Contents:**
- ISColoringSetType#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

indicates if the coloring is for the local representation (including ghost points) or the global representation of a Mat

coloring - the coloring object

type - either IS_COLORING_LOCAL or IS_COLORING_GLOBAL

IS_COLORING_LOCAL can lead to faster computations since parallel ghost point updates are not needed for each color

With IS_COLORING_LOCAL the coloring is in the numbering of the local vector, for IS_COLORING_GLOBAL it is in the numbering of the global vector

MatFDColoringCreate(), ISColoring, ISColoringType, ISColoringCreate(), IS_COLORING_LOCAL, IS_COLORING_GLOBAL, ISColoringGetType()

src/vec/is/is/utils/iscoloring.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISColoringSetType(ISColoring coloring, ISColoringType type)
```

Example 2 (unknown):
```unknown
IS_COLORING_LOCAL
```

Example 3 (unknown):
```unknown
IS_COLORING_GLOBAL
```

Example 4 (unknown):
```unknown
IS_COLORING_LOCAL
```

---

## ISColoringType#

**URL:** https://petsc.org/release/manualpages/IS/ISColoringType/

**Contents:**
- ISColoringType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#
- Examples#
- Examples#

determines if the coloring is for the entire parallel grid/graph/matrix or for just the local ghosted portion

IS_COLORING_GLOBAL - does not include the colors for ghost points, this is used when the function is called synchronously in parallel. This requires generating a “parallel coloring”.

IS_COLORING_LOCAL - includes colors for ghost points, this is used when the function can be called separately on individual processes with the ghost points already filled in. Does not require a “parallel coloring”, rather each process colors its local + ghost part. Using this can result in much less parallel communication. Currently only works with DMDA and if you call MatFDColoringSetFunction() with the local function.

ISColoring, ISColoringSetType(), ISColoringGetType(), DMCreateColoring()

src/tao/unconstrained/tutorials/minsurf2.c src/snes/tutorials/ex14.c

src/snes/tutorials/ex14.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
typedef enum {
  IS_COLORING_GLOBAL,
  IS_COLORING_LOCAL
} ISColoringType;
```

Example 2 (unknown):
```unknown
IS_COLORING_GLOBAL
```

Example 3 (unknown):
```unknown
IS_COLORING_LOCAL
```

Example 4 (unknown):
```unknown
MatFDColoringSetFunction()
```

---

## ISColoringValueCast#

**URL:** https://petsc.org/release/manualpages/IS/ISColoringValueCast/

**Contents:**
- ISColoringValueCast#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

casts an integer a ISColoringValue (which may be 1-bits in size), generates an error if the value is too large

Not Collective; No Fortran Support

a - the PetscCount value

b - the resulting ISColoringValue value, optional, pass NULL if not needed

Errors if the integer is negative

ISColoringValue, ISColoringCreate(), PetscBLASInt, PetscMPIInt, PetscInt, PetscMPIIntCast(), PetscIntCast()

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISColoringValue
```

Example 2 (unknown):
```unknown
#include "petscis.h" 
static inline PetscErrorCode ISColoringValueCast(PetscCount a, ISColoringValue *b)
```

Example 3 (unknown):
```unknown
ISColoringValue
```

Example 4 (unknown):
```unknown
ISColoringValue
```

---

## ISColoringViewFromOptions#

**URL:** https://petsc.org/release/manualpages/IS/ISColoringViewFromOptions/

**Contents:**
- ISColoringViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Developer Note#
- See Also#
- Level#
- Location#

Processes command line options to determine if/how an ISColoring object is to be viewed.

obj - the ISColoring object

bobj - prefix to use for viewing, or NULL to use prefix of mat

name - option to activate viewing

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

This cannot use PetscObjectViewFromOptions() because ISColoring is not a PetscObject

ISColoring, ISColoringView(), PetscObjectViewFromOptions()

src/vec/is/is/utils/iscoloring.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISColoringViewFromOptions(ISColoring obj, PetscObject bobj, const char name[])
```

Example 2 (unknown):
```unknown
PetscObjectViewFromOptions()
```

Example 3 (unknown):
```unknown
PetscObjectViewFromOptions()
```

Example 4 (unknown):
```unknown
PetscObject
```

---

## ISColoringView#

**URL:** https://petsc.org/release/manualpages/IS/ISColoringView/

**Contents:**
- ISColoringView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Views an ISColoring coloring context.

iscoloring - the coloring context

ISColoring(), ISColoringViewFromOptions(), ISColoringDestroy(), ISColoringGetIS(), MatColoring

src/vec/is/is/utils/iscoloring.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISColoringView(ISColoring iscoloring, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
ISColoring()
```

Example 3 (unknown):
```unknown
ISColoringViewFromOptions()
```

Example 4 (unknown):
```unknown
ISColoringDestroy()
```

---

## ISColoring#

**URL:** https://petsc.org/release/manualpages/IS/ISColoring/

**Contents:**
- ISColoring#
- Synopsis#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

sets of ISs that define a coloring of something, such as a graph defined by a sparse matrix

One should not access the *is records below directly because they may not yet have been created. One should use ISColoringGetIS() to make sure they are created when needed.

When the coloring type is IS_COLORING_LOCAL the coloring is in the local ordering of the unknowns. That is the matching the local (ghosted) vector; a local to global mapping must be applied to map them to the global ordering.

This is not a PetscObject

IS, MatColoringCreate(), MatColoring, ISColoringCreate(), ISColoringGetIS(), ISColoringView()

include/petscistypes.h

src/mat/tutorials/ex16.c src/snes/tutorials/ex14.c src/tao/unconstrained/tutorials/minsurf2.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _n_ISColoring *ISColoring;
```

Example 2 (unknown):
```unknown
ISColoringGetIS()
```

Example 3 (unknown):
```unknown
IS_COLORING_LOCAL
```

Example 4 (unknown):
```unknown
PetscObject
```

---

## ISComplementVec#

**URL:** https://petsc.org/release/manualpages/Vec/ISComplementVec/

**Contents:**
- ISComplementVec#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Creates the complement of the index set relative to a layout defined by a Vec

V - the reference vector space

T - the complement of S

IS, Vec, ISCreateGeneral()

src/vec/vec/utils/projection.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"  
PetscErrorCode ISComplementVec(IS S, Vec V, IS *T)
```

Example 2 (unknown):
```unknown
ISCreateGeneral()
```

---

## ISComplement#

**URL:** https://petsc.org/release/manualpages/IS/ISComplement/

**Contents:**
- ISComplement#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Given an index set IS generates the complement index set. That is all indices that are NOT in the given set.

nmin - the first index desired in the local part of the complement

nmax - the largest index desired in the local part of the complement (note that all indices in is must be greater or equal to nmin and less than nmax)

isout - the complement

The communicator for isout is the same as for the input is

For a parallel is, this will generate the local part of the complement on each process

To generate the entire complement (on each process) of a parallel is, first call ISAllGather() and then call this routine.

Low-level Vector Communication, IS, ISCreateGeneral(), ISCreateStride(), ISCreateBlock(), ISAllGather()

src/vec/is/is/utils/iscoloring.c

src/ksp/pc/tutorials/ex4.c src/vec/vec/utils/tagger/tutorials/ex1.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISComplement(IS is, PetscInt nmin, PetscInt nmax, IS *isout)
```

Example 2 (unknown):
```unknown
ISAllGather()
```

Example 3 (unknown):
```unknown
ISCreateGeneral()
```

Example 4 (unknown):
```unknown
ISCreateStride()
```

---

## ISCompressIndicesGeneral#

**URL:** https://petsc.org/release/manualpages/IS/ISCompressIndicesGeneral/

**Contents:**
- ISCompressIndicesGeneral#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

convert the indices of an array of IS into an array of ISGENERAL of block indices

n - maximum possible length of the index set

nkeys - expected number of keys when using PETSC_USE_CTABLE

bs - the size of block

imax - the number of index sets

is_in - the non-blocked array of index sets

is_out - the blocked new index set, as ISGENERAL, not as ISBLOCK

Low-level Vector Communication, IS, ISGENERAL, ISExpandIndicesGeneral()

src/vec/is/is/utils/isblock.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISCompressIndicesGeneral(PetscInt n, PetscInt nkeys, PetscInt bs, PetscInt imax, const IS is_in[], IS is_out[])
```

Example 2 (unknown):
```unknown
PETSC_USE_CTABLE
```

Example 3 (unknown):
```unknown
ISExpandIndicesGeneral()
```

---

## ISConcatenate#

**URL:** https://petsc.org/release/manualpages/IS/ISConcatenate/

**Contents:**
- ISConcatenate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Forms a new IS by locally concatenating the indices from an IS list without reordering.

comm - communicator of the concatenated IS.

len - size of islist array (nonnegative)

islist - array of index sets

isout - The concatenated index set; empty, if len == 0.

The semantics of calling this on comm imply that the comms of the members of islist also contain this rank.

Low-level Vector Communication, IS, ISDifference(), ISSum(), ISExpand(), ISIntersect()

src/vec/is/is/utils/isdiff.c

src/ksp/ksp/tutorials/ex43.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISConcatenate(MPI_Comm comm, PetscInt len, const IS islist[], IS *isout)
```

Example 2 (unknown):
```unknown
ISDifference()
```

Example 3 (unknown):
```unknown
ISIntersect()
```

---

## ISContiguousLocal#

**URL:** https://petsc.org/release/manualpages/IS/ISContiguousLocal/

**Contents:**
- ISContiguousLocal#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Locates an index set with contiguous range within a global range, if possible

gstart - global start

start - start of contiguous block, as an offset from gstart

contig - PETSC_TRUE if the index set refers to contiguous entries on this process, else PETSC_FALSE

IS, ISGetLocalSize(), VecGetOwnershipRange()

src/vec/is/is/interface/index.c

ISContiguousLocal_General() in src/vec/is/is/impls/general/general.c ISContiguousLocal_Stride() in src/vec/is/is/impls/stride/stride.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISContiguousLocal(IS is, PetscInt gstart, PetscInt gend, PetscInt *start, PetscBool *contig)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
ISGetLocalSize()
```

Example 4 (unknown):
```unknown
VecGetOwnershipRange()
```

---

## ISCopy#

**URL:** https://petsc.org/release/manualpages/IS/ISCopy/

**Contents:**
- ISCopy#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

isy - the copy of the index set

IS, ISDuplicate(), ISShift()

src/vec/is/is/interface/index.c

ISCopy_Block() in src/vec/is/is/impls/block/block.c ISCopy_General() in src/vec/is/is/impls/general/general.c ISCopy_Stride() in src/vec/is/is/impls/stride/stride.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISCopy(IS is, IS isy)
```

Example 2 (unknown):
```unknown
ISDuplicate()
```

---

## ISCreateBlock#

**URL:** https://petsc.org/release/manualpages/IS/ISCreateBlock/

**Contents:**
- ISCreateBlock#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- Example#
- See Also#
- Level#
- Location#
- Examples#

Creates a data structure for an index set containing a list of integers. Each integer represents a fixed block size set of indices.

comm - the MPI communicator

bs - number of elements in each block

n - the length of the index set (the number of blocks)

idx - the list of integers, one for each block, the integers contain the index of the first entry of each block divided by the block size

mode - see PetscCopyMode, only PETSC_COPY_VALUES and PETSC_OWN_POINTER are supported in this routine

is - the new index set

When the communicator is not MPI_COMM_SELF, the operations on the index sets, IS, are NOT conceptually the same as MPI_Group operations. The index sets are then distributed sets of indices and thus certain operations on them are collective.

The routine ISBlockSetIndices() can be used to provide the indices to a preexisting block IS

If you wish to index the values {0,1,6,7}, then use a block size of 2 and idx of {0,3}.

Low-level Vector Communication, IS, ISCreateStride(), ISCreateGeneral(), ISAllGather(), ISBlockSetIndices(), ISBLOCK, ISGENERAL

src/vec/is/is/impls/block/block.c

src/vec/is/is/tutorials/ex3.c src/vec/is/is/tutorials/ex3f90.F90 src/vec/vec/utils/tagger/tutorials/ex1.c src/ksp/ksp/tutorials/ex71.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"     
PetscErrorCode ISCreateBlock(MPI_Comm comm, PetscInt bs, PetscInt n, const PetscInt idx[], PetscCopyMode mode, IS *is)
```

Example 2 (unknown):
```unknown
PetscCopyMode
```

Example 3 (unknown):
```unknown
PETSC_COPY_VALUES
```

Example 4 (unknown):
```unknown
PETSC_OWN_POINTER
```

---

## ISCreateGeneral#

**URL:** https://petsc.org/release/manualpages/IS/ISCreateGeneral/

**Contents:**
- ISCreateGeneral#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates a data structure for an index set containing a list of integers.

comm - the MPI communicator

n - the length of the index set

idx - the list of integers

mode - PETSC_COPY_VALUES, PETSC_OWN_POINTER, or PETSC_USE_POINTER; see PetscCopyMode for meaning of this flag.

is - the new index set

When the communicator is not MPI_COMM_SELF, the operations on IS are NOT conceptually the same as MPI_Group operations. The IS are then distributed sets of indices and thus certain operations on them are collective.

Use ISGeneralSetIndices() to provide indices to an already existing IS of ISType ISGENERAL

Low-level Vector Communication, IS, ISGENERAL, ISCreateStride(), ISCreateBlock(), ISAllGather(), PETSC_COPY_VALUES, PETSC_OWN_POINTER, PETSC_USE_POINTER, PetscCopyMode, ISGeneralSetIndicesFromMask()

src/vec/is/is/impls/general/general.c

src/ksp/pc/tutorials/ex4.c src/ksp/ksp/tutorials/ex85.c src/ksp/ksp/tutorials/ex59.c src/vec/is/is/tutorials/ex1.c src/ksp/ksp/tutorials/ex71.c src/ksp/ksp/tutorials/ex76f.F90 src/ksp/ksp/tutorials/ex49.c src/vec/is/is/tutorials/ex1f90.F90 src/ksp/ksp/tutorials/ex84.c src/ksp/ksp/tutorials/ex76.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISCreateGeneral(MPI_Comm comm, PetscInt n, const PetscInt idx[], PetscCopyMode mode, IS *is)
```

Example 2 (unknown):
```unknown
PETSC_COPY_VALUES
```

Example 3 (unknown):
```unknown
PETSC_OWN_POINTER
```

Example 4 (unknown):
```unknown
PETSC_USE_POINTER
```

---

## ISCreateStride#

**URL:** https://petsc.org/release/manualpages/IS/ISCreateStride/

**Contents:**
- ISCreateStride#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates a data structure for an index set containing a list of evenly spaced integers.

comm - the MPI communicator

n - the length of the locally owned portion of the index set

first - the first element of the locally owned portion of the index set

step - the change to the next index

is - the new index set

ISStrideSetStride() may be used to set the stride of an ISSTRIDE that already exists

When the communicator is not MPI_COMM_SELF, the operations on IS are NOT conceptually the same as MPI_Group operations. The IS are the distributed sets of indices and thus certain operations on them are collective.

Low-level Vector Communication, IS, ISStrideSetStride(), ISCreateGeneral(), ISCreateBlock(), ISAllGather(), ISSTRIDE

src/vec/is/is/impls/stride/stride.c

src/ksp/ksp/tutorials/ex59.c src/vec/is/is/tutorials/ex2f.F90 src/ksp/ksp/tutorials/ex79.c src/vec/is/is/tutorials/ex2.c src/ksp/ksp/tutorials/ex73.c src/ksp/ksp/tutorials/ex71.c src/ksp/ksp/tutorials/ex19.c src/ksp/ksp/tutorials/ex84.c src/tao/pde_constrained/tutorials/hyperbolic.c src/ksp/ksp/tutorials/ex82.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"   
PetscErrorCode ISCreateStride(MPI_Comm comm, PetscInt n, PetscInt first, PetscInt step, IS *is)
```

Example 2 (unknown):
```unknown
ISStrideSetStride()
```

Example 3 (unknown):
```unknown
MPI_COMM_SELF
```

Example 4 (unknown):
```unknown
ISStrideSetStride()
```

---

## ISCreateSubIS#

**URL:** https://petsc.org/release/manualpages/IS/ISCreateSubIS/

**Contents:**
- ISCreateSubIS#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Example usage#
- See Also#
- Level#
- Location#

Create a sub index set from a global index set selecting some components.

comps - which components we will extract from is

subis - the new sub index set

We have an index set is living on 3 processes with the following values: | 4 9 0 | 2 6 7 | 10 11 1| and another index set comps used to indicate which components of is we want to take, | 7 5 | 1 2 | 0 4| The output index set subis should look like: | 11 7 | 9 0 | 4 6|

IS, VecGetSubVector(), MatCreateSubMatrix()

src/vec/is/is/interface/index.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISCreateSubIS(IS is, IS comps, IS *subis)
```

Example 2 (unknown):
```unknown
VecGetSubVector()
```

Example 3 (unknown):
```unknown
MatCreateSubMatrix()
```

---

## ISCreate#

**URL:** https://petsc.org/release/manualpages/IS/ISCreate/

**Contents:**
- ISCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Create an index set object. IS, index sets, are PETSc objects used to do efficient indexing into other data structures such as Vec and Mat

comm - the MPI communicator

is - the new index set

When the communicator is not MPI_COMM_SELF, the operations on is are NOT conceptually the same as MPI_Group operations. The IS are then distributed sets of indices and thus certain operations on them are collective.

Low-level Vector Communication, IS, ISType(), ISSetType(), ISCreateGeneral(), ISCreateStride(), ISCreateBlock(), ISAllGather()

src/vec/is/is/interface/isreg.c

src/ksp/ksp/tutorials/ex87.c src/ksp/ksp/tutorials/ex27.c src/ksp/ksp/tutorials/ex76.c src/ksp/ksp/tutorials/ex76f.F90

ISCreate_Block() in src/vec/is/is/impls/block/block.c ISCreate_General() in src/vec/is/is/impls/general/general.c ISCreate_Stride() in src/vec/is/is/impls/stride/stride.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISCreate(MPI_Comm comm, IS *is)
```

Example 2 (unknown):
```unknown
MPI_COMM_SELF
```

Example 3 (unknown):
```unknown
ISSetType()
```

Example 4 (unknown):
```unknown
ISCreateGeneral()
```

---

## ISDestroy#

**URL:** https://petsc.org/release/manualpages/IS/ISDestroy/

**Contents:**
- ISDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Destroys an index set.

IS, ISCreateGeneral(), ISCreateStride(), ISCreateBlock()

src/vec/is/is/interface/index.c

src/snes/tutorials/ex28.c src/mat/tutorials/ex11.c src/mat/tutorials/ex1.c src/snes/tutorials/ex73f90t.F90 src/mat/tutorials/ex11f.F90 src/mat/tutorials/ex17f.F90 src/snes/tutorials/ex13.c src/mat/tutorials/ex15.c src/mat/tutorials/ex15f.F90 src/mat/tutorials/ex17.c

ISDestroy_Block() in src/vec/is/is/impls/block/block.c ISDestroy_General() in src/vec/is/is/impls/general/general.c ISDestroy_Stride() in src/vec/is/is/impls/stride/stride.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISDestroy(IS *is)
```

Example 2 (unknown):
```unknown
ISCreateGeneral()
```

Example 3 (unknown):
```unknown
ISCreateStride()
```

Example 4 (unknown):
```unknown
ISCreateBlock()
```

---

## ISDifference#

**URL:** https://petsc.org/release/manualpages/IS/ISDifference/

**Contents:**
- ISDifference#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Computes the difference between two index sets.

is1 - first index, to have items removed from it

is2 - index values to be removed

Negative values are removed from the lists. is2 may have values that are not in is1.

This computation requires O(imax-imin) memory and O(imax-imin) work, where imin and imax are the bounds on the indices in is1.

If is2 is NULL, the result is the same as for an empty IS, i.e., a duplicate of is1.

The difference is computed separately on each MPI rank

Low-level Vector Communication, IS, ISDestroy(), ISView(), ISSum(), ISExpand()

src/vec/is/is/utils/isdiff.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISDifference(IS is1, IS is2, IS *isout)
```

Example 2 (unknown):
```unknown
ISDestroy()
```

---

## ISDuplicate#

**URL:** https://petsc.org/release/manualpages/IS/ISDuplicate/

**Contents:**
- ISDuplicate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Creates a duplicate copy of an index set.

newIS - the copy of the index set

IS, ISCreateGeneral(), ISCopy()

src/vec/is/is/interface/index.c

src/ksp/ksp/tutorials/ex81.c src/dm/impls/plex/tutorials/ex10.c src/dm/tutorials/ex22.c

ISDuplicate_Block() in src/vec/is/is/impls/block/block.c ISDuplicate_General() in src/vec/is/is/impls/general/general.c ISDuplicate_Stride() in src/vec/is/is/impls/stride/stride.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISDuplicate(IS is, IS *newIS)
```

Example 2 (unknown):
```unknown
ISCreateGeneral()
```

---

## ISEmbed#

**URL:** https://petsc.org/release/manualpages/IS/ISEmbed/

**Contents:**
- ISEmbed#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Embed IS a into IS b by finding the locations in b that have the same indices as in a. If c is the IS of these locations, we have a = b*c, regarded as a composition of the corresponding ISLocalToGlobalMapping.

drop - flag indicating whether to drop indices of a that are not in b.

c - local embedding indices

If some of the global indices of a are not among the indices of b, the embedding is impossible. The local indices of a corresponding to these global indices are either mapped to -1 (if !drop) or are omitted (if drop). In the former case the size of c is the same as that of a, in the latter case the size of c may be smaller.

The resulting IS is sequential, since the index substitution it encodes is purely local.

IS, ISLocalToGlobalMapping

src/vec/is/is/utils/isdiff.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 2 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISEmbed(IS a, IS b, PetscBool drop, IS *c)
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMapping
```

---

## ISEqualUnsorted#

**URL:** https://petsc.org/release/manualpages/IS/ISEqualUnsorted/

**Contents:**
- ISEqualUnsorted#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Compares if two index sets have the same indices.

is1 - first index set to compare

is2 - second index set to compare

flg - output flag, either PETSC_TRUE (if both index sets have the same indices), or PETSC_FALSE if the index sets differ by size or by the set of indices)

Unlike ISEqual(), this routine does NOT sort the contents of the index sets before the comparison is made, i.e., the order of indices is important.

Each MPI rank must have the same indices.

Low-level Vector Communication, IS, ISEqual()

src/vec/is/is/utils/iscomp.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISEqualUnsorted(IS is1, IS is2, PetscBool *flg)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

---

## ISEqual#

**URL:** https://petsc.org/release/manualpages/IS/ISEqual/

**Contents:**
- ISEqual#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Compares if two index sets have the same set of indices.

is1 - first index set to compare

is2 - second index set to compare

flg - output flag, either PETSC_TRUE (if both index sets have the same indices), or PETSC_FALSE if the index sets differ by size or by the set of indices)

Unlike ISEqualUnsorted(), this routine sorts the contents of the index sets (only within each MPI rank) before the comparison is made, so the order of the indices on a processor is immaterial.

Each processor has to have the same indices in the two sets, for example,

Low-level Vector Communication, IS, ISEqualUnsorted()

src/vec/is/is/utils/iscomp.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISEqual(IS is1, IS is2, PetscBool *flg)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
ISEqualUnsorted()
```

Example 4 (unknown):
```unknown
Processor
             0      1
    is1 = {0, 1} {2, 3}
    is2 = {2, 3} {0, 1}
```

---

## ISExpandIndicesGeneral#

**URL:** https://petsc.org/release/manualpages/IS/ISExpandIndicesGeneral/

**Contents:**
- ISExpandIndicesGeneral#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

convert the indices of an array IS into non-block indices in an array of ISGENERAL

n - the length of the index set (not being used)

nkeys - expected number of keys when PETSC_USE_CTABLE is used

bs - the size of block

imax - the number of index sets

is_in - the blocked array of index sets, must be as large as imax

is_out - the non-blocked new index set, as ISGENERAL, must be as large as imax

Low-level Vector Communication, IS, ISGENERAL, ISCompressIndicesGeneral()

src/vec/is/is/utils/isblock.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISExpandIndicesGeneral(PetscInt n, PetscInt nkeys, PetscInt bs, PetscInt imax, const IS is_in[], IS is_out[])
```

Example 2 (unknown):
```unknown
PETSC_USE_CTABLE
```

Example 3 (unknown):
```unknown
ISCompressIndicesGeneral()
```

---

## ISExpand#

**URL:** https://petsc.org/release/manualpages/IS/ISExpand/

**Contents:**
- ISExpand#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Computes the union of two index sets, by concatenating 2 lists and removing duplicates.

is1 - first index set

is2 - index values to be added

isout - is1 + is2 The index set is2 is appended to is1 removing duplicates

Negative values are removed from the lists. This requires O(imax-imin) memory and O(imax-imin) work, where imin and imax are the bounds on the indices in is1 and is2.

is1 and is2 do not need to be sorted.

The operations are performed separately on each MPI rank

Low-level Vector Communication, IS, ISDestroy(), ISView(), ISDifference(), ISSum(), ISIntersect()

src/vec/is/is/utils/isdiff.c

src/ksp/ksp/tutorials/ex81.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISExpand(IS is1, IS is2, IS *isout)
```

Example 2 (unknown):
```unknown
ISDestroy()
```

Example 3 (unknown):
```unknown
ISDifference()
```

Example 4 (unknown):
```unknown
ISIntersect()
```

---

## ISFinalizePackage#

**URL:** https://petsc.org/release/manualpages/Vec/ISFinalizePackage/

**Contents:**
- ISFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys everything in the IS package. It is called from PetscFinalize().

src/vec/vec/interface/dlregisvec.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
#include "petscvec.h" */
PetscErrorCode ISFinalizePackage(void)
```

Example 3 (unknown):
```unknown
PetscFinalize()
```

---

## ISGeneralFilter#

**URL:** https://petsc.org/release/manualpages/IS/ISGeneralFilter/

**Contents:**
- ISGeneralFilter#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Remove all indices outside of [start, end) from an ISGENERAL

start - the lowest index kept

end - one more than the highest index kept, start \(\le\) end

Low-level Vector Communication, IS, ISGENERAL, ISCreateGeneral(), ISGeneralSetIndices()

src/vec/is/is/impls/general/general.c

ISGeneralFilter_General() in src/vec/is/is/impls/general/general.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
#include "petscis.h"  
PetscErrorCode ISGeneralFilter(IS is, PetscInt start, PetscInt end)
```

Example 2 (unknown):
```unknown
ISCreateGeneral()
```

Example 3 (unknown):
```unknown
ISGeneralSetIndices()
```

---

## ISGeneralSetIndicesFromMask#

**URL:** https://petsc.org/release/manualpages/IS/ISGeneralSetIndicesFromMask/

**Contents:**
- ISGeneralSetIndicesFromMask#
- Synopsis#
- Input Parameters#
- Note#
- Example#
- See Also#
- Level#
- Location#
- Implementations#

Sets the indices for an ISGENERAL index set using a boolean mask

rstart - the range start index (inclusive)

rend - the range end index (exclusive)

mask - the boolean mask array of length rend-rstart, indices will be set for each PETSC_TRUE value in the array

The mask array may be freed by the user after this call.

will feed the IS with indices

Low-level Vector Communication, IS, ISCreateGeneral(), ISGeneralSetIndices(), ISGENERAL

src/vec/is/is/impls/general/general.c

ISGeneralSetIndicesFromMask_General() in src/vec/is/is/impls/general/general.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISGeneralSetIndicesFromMask(IS is, PetscInt rstart, PetscInt rend, const PetscBool mask[])
```

Example 2 (unknown):
```unknown
PetscBool mask[] = {PETSC_FALSE, PETSC_TRUE, PETSC_FALSE, PETSC_FALSE, PETSC_TRUE};
   ISGeneralSetIndicesFromMask(is,10,15,mask);
```

Example 3 (unknown):
```unknown
ISCreateGeneral()
```

Example 4 (unknown):
```unknown
ISGeneralSetIndices()
```

---

## ISGeneralSetIndices#

**URL:** https://petsc.org/release/manualpages/IS/ISGeneralSetIndices/

**Contents:**
- ISGeneralSetIndices#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets the indices for an ISGENERAL index set

n - the length of the index set

idx - the list of integers

mode - see PetscCopyMode for meaning of this flag.

Use ISCreateGeneral() to create the IS and set its indices in a single function call

Low-level Vector Communication, IS, ISBLOCK, ISCreateGeneral(), ISGeneralSetIndicesFromMask(), ISBlockSetIndices(), ISGENERAL, PetscCopyMode

src/vec/is/is/impls/general/general.c

src/ksp/ksp/tutorials/ex87.c

ISGeneralSetIndices_General() in src/vec/is/is/impls/general/general.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISGeneralSetIndices(IS is, PetscInt n, const PetscInt idx[], PetscCopyMode mode)
```

Example 2 (unknown):
```unknown
PetscCopyMode
```

Example 3 (unknown):
```unknown
ISCreateGeneral()
```

Example 4 (unknown):
```unknown
ISCreateGeneral()
```

---

## ISGetBlockSize#

**URL:** https://petsc.org/release/manualpages/IS/ISGetBlockSize/

**Contents:**
- ISGetBlockSize#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Returns the number of elements in a block.

size - the number of elements in a block

IS, ISBlockGetSize(), ISGetSize(), ISCreateBlock(), ISSetBlockSize()

src/vec/is/is/interface/index.c

src/vec/is/is/tutorials/ex3.c src/vec/is/is/tutorials/ex3f90.F90

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISGetBlockSize(IS is, PetscInt *size)
```

Example 2 (unknown):
```unknown
ISSetBlockSize()
```

Example 3 (unknown):
```unknown
ISBlockGetSize()
```

Example 4 (unknown):
```unknown
ISGetSize()
```

---

## ISGetCompressOutput#

**URL:** https://petsc.org/release/manualpages/IS/ISGetCompressOutput/

**Contents:**
- ISGetCompressOutput#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the flag for output compression

compress - the flag to compress output

IS, ISSetCompressOutput(), ISView()

src/vec/is/is/interface/index.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISGetCompressOutput(IS is, PetscBool *compress)
```

Example 2 (unknown):
```unknown
ISSetCompressOutput()
```

---

## ISGetIndices#

**URL:** https://petsc.org/release/manualpages/IS/ISGetIndices/

**Contents:**
- ISGetIndices#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Returns a pointer to the indices. The user should call ISRestoreIndices() after having looked at the indices. The user should NOT change the indices.

ptr - the location to put the pointer to the indices

IS, ISRestoreIndices()

src/vec/is/is/interface/index.c

src/ksp/ksp/tutorials/ex87.c src/snes/tutorials/ex62.c src/vec/is/is/tutorials/ex1.c src/snes/tutorials/ex13.c src/ksp/ksp/tutorials/ex76f.F90 src/ksp/ksp/tutorials/ex71.c src/snes/tutorials/ex56.c src/vec/vec/utils/tagger/tutorials/ex1.c src/snes/tutorials/ex77.c src/ksp/ksp/tutorials/ex76.c

ISGetIndices_Block() in src/vec/is/is/impls/block/block.c ISGetIndices_General() in src/vec/is/is/impls/general/general.c ISGetIndices_Stride() in src/vec/is/is/impls/stride/stride.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISRestoreIndices()
```

Example 2 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISGetIndices(IS is, const PetscInt *ptr[])
```

Example 3 (julia):
```julia
PetscInt, pointer :: ptr(:)
```

Example 4 (unknown):
```unknown
ISRestoreIndices()
```

---

## ISGetInfo#

**URL:** https://petsc.org/release/manualpages/IS/ISGetInfo/

**Contents:**
- ISGetInfo#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Determine whether an index set satisfies a given property

Collective or Logically Collective if the type is IS_GLOBAL (logically collective if the value of the property has been permanently set with ISSetInfo())

info - describing a property of the index set, one of those listed in the documentation of ISSetInfo()

compute - if PETSC_FALSE, the property will not be computed if it is not already known and the property will be assumed to be false

type - whether the property is local (IS_LOCAL) or global (IS_GLOBAL)

flg - whether the property is true (PETSC_TRUE) or false (PETSC_FALSE)

ISGetInfo() uses cached values when possible, which will be incorrect if ISSetInfo() has been called with incorrect information.

To clear cached values, use ISClearInfoCache().

IS, ISInfo, ISInfoType, ISSetInfo(), ISClearInfoCache()

src/vec/is/is/interface/index.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISGetInfo(IS is, ISInfo info, ISInfoType type, PetscBool compute, PetscBool *flg)
```

Example 2 (unknown):
```unknown
ISSetInfo()
```

Example 3 (unknown):
```unknown
ISSetInfo()
```

Example 4 (unknown):
```unknown
PETSC_FALSE
```

---

## ISGetLayout#

**URL:** https://petsc.org/release/manualpages/IS/ISGetLayout/

**Contents:**
- ISGetLayout#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

get PetscLayout describing index set layout

IS, PetscLayout, ISSetLayout(), ISGetSize(), ISGetLocalSize()

src/vec/is/is/interface/index.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLayout
```

Example 2 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISGetLayout(IS is, PetscLayout *map)
```

Example 3 (unknown):
```unknown
PetscLayout
```

Example 4 (unknown):
```unknown
ISSetLayout()
```

---

## ISGetLocalSize#

**URL:** https://petsc.org/release/manualpages/IS/ISGetLocalSize/

**Contents:**
- ISGetLocalSize#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Returns the local (processor) length of an index set.

size - the local size

src/vec/is/is/interface/index.c

src/ksp/ksp/tutorials/ex87.c src/ksp/ksp/tutorials/ex59.c src/snes/tutorials/ex13.c src/ksp/ksp/tutorials/ex76f.F90 src/ksp/ksp/tutorials/ex71.c src/snes/tutorials/ex56.c src/vec/vec/utils/tagger/tutorials/ex1.c src/snes/tutorials/ex77.c src/ksp/ksp/tutorials/ex76.c src/ksp/ksp/tutorials/ex82.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISGetLocalSize(IS is, PetscInt *size)
```

Example 2 (unknown):
```unknown
ISGetSize()
```

---

## ISGetMinMax#

**URL:** https://petsc.org/release/manualpages/IS/ISGetMinMax/

**Contents:**
- ISGetMinMax#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Gets the minimum and maximum values in an IS

min - the minimum value, you may pass NULL

max - the maximum value, you may pass NULL

Empty index sets return min=PETSC_INT_MAX and max=PETSC_INT_MIN.

In parallel, it returns the min and max of the local portion of is

IS, ISGetIndices(), ISRestoreIndices()

src/vec/is/is/interface/index.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISGetMinMax(IS is, PetscInt *min, PetscInt *max)
```

Example 2 (unknown):
```unknown
PETSC_INT_MAX
```

Example 3 (unknown):
```unknown
PETSC_INT_MIN
```

Example 4 (unknown):
```unknown
ISGetIndices()
```

---

## ISGetNonlocalIndices#

**URL:** https://petsc.org/release/manualpages/IS/ISGetNonlocalIndices/

**Contents:**
- ISGetNonlocalIndices#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Retrieve an array of indices from remote processors in this communicator.

indices - indices with rank 0 indices first, and so on, omitting the current rank. Total number of indices is the difference total and local, obtained with ISGetSize() and ISGetLocalSize(), respectively.

Restore the indices using ISRestoreNonlocalIndices().

The same scalability considerations as those for ISGetTotalIndices() apply here.

IS, ISGetTotalIndices(), ISRestoreNonlocalIndices(), ISGetSize(), ISGetLocalSize().

src/vec/is/is/interface/index.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISGetNonlocalIndices(IS is, const PetscInt *indices[])
```

Example 2 (unknown):
```unknown
ISGetSize()
```

Example 3 (unknown):
```unknown
ISGetLocalSize()
```

Example 4 (unknown):
```unknown
ISRestoreNonlocalIndices()
```

---

## ISGetNonlocalIS#

**URL:** https://petsc.org/release/manualpages/IS/ISGetNonlocalIS/

**Contents:**
- ISGetNonlocalIS#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Gather all nonlocal indices for this IS and present them as another sequential index set.

complement - sequential IS with indices identical to the result of ISGetNonlocalIndices()

Complement represents the result of ISGetNonlocalIndices() as an IS. Therefore scalability issues similar to ISGetNonlocalIndices() apply.

The resulting IS must be restored using ISRestoreNonlocalIS().

IS, ISGetNonlocalIndices(), ISRestoreNonlocalIndices(), ISAllGather(), ISGetSize()

src/vec/is/is/interface/index.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISGetNonlocalIS(IS is, IS *complement)
```

Example 2 (unknown):
```unknown
ISGetNonlocalIndices()
```

Example 3 (unknown):
```unknown
ISGetNonlocalIndices()
```

Example 4 (unknown):
```unknown
ISGetNonlocalIndices()
```

---

## ISGetPointRange#

**URL:** https://petsc.org/release/manualpages/IS/ISGetPointRange/

**Contents:**
- ISGetPointRange#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Returns a description of the points in an IS suitable for traversal

pointIS - The IS object

pStart - The first index, see notes

pEnd - One past the last index, see notes

points - The indices, see notes

If the IS contains contiguous indices in an ISSTRIDE, then the indices are contained in [pStart, pEnd) and points = NULL. Otherwise, pStart = 0, pEnd = numIndices, and points is an array of the indices. This supports the following pattern

Hence the same code can be written for pointIS being a ISSTRIDE or ISGENERAL

Low-level Vector Communication, IS, ISRestorePointRange(), ISGetPointSubrange(), ISGetIndices(), ISCreateStride()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISGetPointRange(IS pointIS, PetscInt *pStart, PetscInt *pEnd, const PetscInt *points[])
```

Example 2 (unknown):
```unknown
pEnd = numIndices
```

Example 3 (sass):
```sass
ISGetPointRange(is, &pStart, &pEnd, &points);
  for (p = pStart; p < pEnd; ++p) {
    const PetscInt point = points ? points[p] : p;
    // use point
  }
  ISRestorePointRange(is, &pstart, &pEnd, &points);
```

Example 4 (unknown):
```unknown
ISRestorePointRange()
```

---

## ISGetPointSubrange#

**URL:** https://petsc.org/release/manualpages/IS/ISGetPointSubrange/

**Contents:**
- ISGetPointSubrange#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Configures the input IS to be a subrange for the traversal information given

subpointIS - The IS object to be configured

pStart - The first index of the subrange

pEnd - One past the last index for the subrange

points - The indices for the entire range, from ISGetPointRange()

subpointIS - The IS object now configured to be a subrange

The input IS will now respond properly to calls to ISGetPointRange() and return the subrange.

Low-level Vector Communication, IS, ISGetPointRange(), ISRestorePointRange(), ISGetIndices(), ISCreateStride()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISGetPointSubrange(IS subpointIS, PetscInt pStart, PetscInt pEnd, const PetscInt points[])
```

Example 2 (unknown):
```unknown
ISGetPointRange()
```

Example 3 (unknown):
```unknown
ISGetPointRange()
```

Example 4 (unknown):
```unknown
ISGetPointRange()
```

---

## ISGetSize#

**URL:** https://petsc.org/release/manualpages/IS/ISGetSize/

**Contents:**
- ISGetSize#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Returns the global length of an index set.

size - the global size

src/vec/is/is/interface/index.c

src/ts/tutorials/ex11.c src/dm/impls/plex/tutorials/ex8.c src/ksp/ksp/tutorials/ex19.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISGetSize(IS is, PetscInt *size)
```

---

## ISGetTotalIndices#

**URL:** https://petsc.org/release/manualpages/IS/ISGetTotalIndices/

**Contents:**
- ISGetTotalIndices#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Retrieve an array containing all indices across the communicator.

indices - total indices with rank 0 indices first, and so on; total array size is the same as returned with ISGetSize().

this is potentially nonscalable, but depends on the size of the total index set and the size of the communicator. This may be feasible for index sets defined on subcommunicators, such that the set size does not grow with PETSC_WORLD_COMM. Note also that there is no way to tell where the local part of the indices starts (use ISGetIndices() and ISGetNonlocalIndices() to retrieve just the local and just the nonlocal part (complement), respectively).

IS, ISRestoreTotalIndices(), ISGetNonlocalIndices(), ISGetSize()

src/vec/is/is/interface/index.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISGetTotalIndices(IS is, const PetscInt *indices[])
```

Example 2 (unknown):
```unknown
ISGetSize()
```

Example 3 (unknown):
```unknown
PETSC_WORLD_COMM
```

Example 4 (unknown):
```unknown
ISGetIndices()
```

---

## ISGetType#

**URL:** https://petsc.org/release/manualpages/IS/ISGetType/

**Contents:**
- ISGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the index set type name, ISType, (as a string) from the IS.

type - The index set type name

type should not be retained for later use as it will be an invalid pointer if the ISType of is is changed.

Low-level Vector Communication, IS, ISType, ISSetType(), ISCreate(), PetscObjectTypeCompare(), PetscObjectTypeCompareAny()

src/vec/is/is/interface/isreg.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISGetType(IS is, ISType *type)
```

Example 2 (unknown):
```unknown
ISSetType()
```

Example 3 (unknown):
```unknown
PetscObjectTypeCompare()
```

Example 4 (unknown):
```unknown
PetscObjectTypeCompareAny()
```

---

## ISGlobalToLocalMappingApplyBlock#

**URL:** https://petsc.org/release/manualpages/IS/ISGlobalToLocalMappingApplyBlock/

**Contents:**
- ISGlobalToLocalMappingApplyBlock#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#

Provides the local block numbering for a list of integers specified with a block global numbering.

mapping - mapping between local and global numbering

type - IS_GTOLM_MASK - maps global indices with no local value to -1 in the output list (i.e., mask them) IS_GTOLM_DROP - drops the indices with no local value from the output list

n - number of global indices to map

idx - global indices to map

nout - number of indices in output array (if type == IS_GTOLM_MASK then nout = n)

idxout - local index of each global index, one must pass in an array long enough to hold all the indices. You can call ISGlobalToLocalMappingApplyBlock() with idxout == NULL to determine the required length (returned in nout) and then allocate the required space and call ISGlobalToLocalMappingApplyBlock() a second time to set the values.

Either nout or idxout may be NULL. idx and idxout may be identical.

For “small” problems when using ISGlobalToLocalMappingApply() and ISGlobalToLocalMappingApplyBlock(), the ISLocalToGlobalMappingType of ISLOCALTOGLOBALMAPPINGBASIC will be used; this uses more memory but is faster; this approach is not scalable for extremely large mappings. For large problems ISLOCALTOGLOBALMAPPINGHASH is used, this is scalable. Use ISLocalToGlobalMappingSetType() or call ISLocalToGlobalMappingSetFromOptions() with the option -islocaltoglobalmapping_type <basic,hash> to control which is used.

The manual page states that idx and idxout may be identical but the calling sequence declares idx as const so it cannot be the same as idxout.

Low-level Vector Communication, ISLocalToGlobalMapping, ISLocalToGlobalMappingApply(), ISGlobalToLocalMappingApply(), ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingDestroy()

src/vec/is/utils/isltog.c

src/vec/is/is/tutorials/ex5.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISGlobalToLocalMappingApplyBlock(ISLocalToGlobalMapping mapping, ISGlobalToLocalMappingMode type, PetscInt n, const PetscInt idx[], PetscInt *nout, PetscInt idxout[])
```

Example 2 (unknown):
```unknown
IS_GTOLM_MASK
```

Example 3 (unknown):
```unknown
IS_GTOLM_DROP
```

Example 4 (unknown):
```unknown
IS_GTOLM_MASK
```

---

## ISGlobalToLocalMappingApplyIS#

**URL:** https://petsc.org/release/manualpages/IS/ISGlobalToLocalMappingApplyIS/

**Contents:**
- ISGlobalToLocalMappingApplyIS#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates from an IS in the global numbering a new index set using the local numbering defined in an ISLocalToGlobalMapping context.

mapping - mapping between local and global numbering

type - IS_GTOLM_MASK - maps global indices with no local value to -1 in the output list (i.e., mask them) IS_GTOLM_DROP - drops the indices with no local value from the output list

is - index set in global numbering

newis - index set in local numbering

The output IS will be sequential, as it encodes a purely local operation

If type is IS_GTOLM_MASK, newis will have the same block size as is

Low-level Vector Communication, ISGlobalToLocalMapping, ISGlobalToLocalMappingApply(), ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingDestroy()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 2 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISGlobalToLocalMappingApplyIS(ISLocalToGlobalMapping mapping, ISGlobalToLocalMappingMode type, IS is, IS *newis)
```

Example 3 (unknown):
```unknown
IS_GTOLM_MASK
```

Example 4 (unknown):
```unknown
IS_GTOLM_DROP
```

---

## ISGlobalToLocalMappingApply#

**URL:** https://petsc.org/release/manualpages/IS/ISGlobalToLocalMappingApply/

**Contents:**
- ISGlobalToLocalMappingApply#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#

Provides the local numbering for a list of integers specified with a global numbering.

mapping - mapping between local and global numbering

type - IS_GTOLM_MASK - maps global indices with no local value to -1 in the output list (i.e., mask them) IS_GTOLM_DROP - drops the indices with no local value from the output list

n - number of global indices to map

idx - global indices to map

nout - number of indices in output array (if type == IS_GTOLM_MASK then nout = n)

idxout - local index of each global index, one must pass in an array long enough to hold all the indices. You can call ISGlobalToLocalMappingApply() with idxout == NULL to determine the required length (returned in nout) and then allocate the required space and call ISGlobalToLocalMappingApply() a second time to set the values.

Either nout or idxout may be NULL. idx and idxout may be identical.

For “small” problems when using ISGlobalToLocalMappingApply() and ISGlobalToLocalMappingApplyBlock(), the ISLocalToGlobalMappingType of ISLOCALTOGLOBALMAPPINGBASIC will be used; this uses more memory but is faster; this approach is not scalable for extremely large mappings. For large problems ISLOCALTOGLOBALMAPPINGHASH is used, this is scalable. Use ISLocalToGlobalMappingSetType() or call ISLocalToGlobalMappingSetFromOptions() with the option -islocaltoglobalmapping_type <basic,hash> to control which is used.

The manual page states that idx and idxout may be identical but the calling sequence declares idx as const so it cannot be the same as idxout.

Low-level Vector Communication, ISLocalToGlobalMapping, ISLocalToGlobalMappingApply(), ISGlobalToLocalMappingApplyBlock(), ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingDestroy()

src/vec/is/utils/isltog.c

src/vec/is/is/tutorials/ex4.c src/vec/is/is/tutorials/ex5.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISGlobalToLocalMappingApply(ISLocalToGlobalMapping mapping, ISGlobalToLocalMappingMode type, PetscInt n, const PetscInt idx[], PetscInt *nout, PetscInt idxout[])
```

Example 2 (unknown):
```unknown
IS_GTOLM_MASK
```

Example 3 (unknown):
```unknown
IS_GTOLM_DROP
```

Example 4 (unknown):
```unknown
IS_GTOLM_MASK
```

---

## ISGlobalToLocalMappingMode#

**URL:** https://petsc.org/release/manualpages/IS/ISGlobalToLocalMappingMode/

**Contents:**
- ISGlobalToLocalMappingMode#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#
- Examples#
- Examples#

Indicates mapping behavior if global indices are missing

IS_GTOLM_MASK - missing global indices are masked by mapping them to a local index of -1

IS_GTOLM_DROP - missing global indices are dropped

ISGlobalToLocalMappingApplyBlock(), ISGlobalToLocalMappingApply()

src/vec/is/is/tutorials/ex4.c src/vec/is/is/tutorials/ex5.c

src/vec/is/is/tutorials/ex4.c src/vec/is/is/tutorials/ex5.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
typedef enum {
  IS_GTOLM_MASK,
  IS_GTOLM_DROP
} ISGlobalToLocalMappingMode;
```

Example 2 (unknown):
```unknown
IS_GTOLM_MASK
```

Example 3 (unknown):
```unknown
IS_GTOLM_DROP
```

Example 4 (unknown):
```unknown
ISGlobalToLocalMappingApplyBlock()
```

---

## ISIdentity#

**URL:** https://petsc.org/release/manualpages/IS/ISIdentity/

**Contents:**
- ISIdentity#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Determines whether index set is the identity mapping.

ident - PETSC_TRUE if an identity, else PETSC_FALSE

If ISSetIdentity() (or ISSetInfo() for a permanent property) has been called, ISIdentity() will return its answer without communication between processes, but otherwise the output ident will be computed from ISGetInfo(), which may require synchronization on the communicator of is. To avoid this computation, call ISGetInfo() directly with the compute flag set to PETSC_FALSE, and ident will be assumed false.

IS, ISSetIdentity(), ISGetInfo()

src/vec/is/is/interface/index.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISIdentity(IS is, PetscBool *ident)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
ISSetIdentity()
```

Example 4 (unknown):
```unknown
ISSetInfo()
```

---

## ISInfoType#

**URL:** https://petsc.org/release/manualpages/IS/ISInfoType/

**Contents:**
- ISInfoType#
- Synopsis#
- Values#
- Note#
- See Also#
- Level#
- Location#

Selects whether an ISInfo property of an IS is recorded with respect to the local indices on this MPI process or to the full global index set

IS_LOCAL - the property holds for the local portion of the IS

IS_GLOBAL - the property holds for the entire (parallel) index set

Some properties (for example IS_SORTED) may be true locally but not globally; ISInfoType lets the caller specify which interpretation is wanted in ISSetInfo()/ISGetInfo().

IS, ISInfo, ISSetInfo(), ISGetInfo(), ISClearInfoCache()

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
typedef enum {
  IS_LOCAL,
  IS_GLOBAL
} ISInfoType;
```

Example 2 (unknown):
```unknown
ISSetInfo()
```

Example 3 (unknown):
```unknown
ISGetInfo()
```

Example 4 (unknown):
```unknown
ISSetInfo()
```

---

## ISInfo#

**URL:** https://petsc.org/release/manualpages/IS/ISInfo/

**Contents:**
- ISInfo#
- Synopsis#
- Developer Note#
- See Also#
- Level#
- Location#

Info that may either be computed or set as known for an index set

Entries that are negative need not be called collectively by all processes.

IS, ISType, ISSetInfo()

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
typedef enum {
  IS_INFO_MIN    = -1,
  IS_SORTED      = 0,
  IS_UNIQUE      = 1,
  IS_PERMUTATION = 2,
  IS_INTERVAL    = 3,
  IS_IDENTITY    = 4,
  IS_INFO_MAX    = 5
} ISInfo;
```

Example 2 (unknown):
```unknown
ISSetInfo()
```

---

## ISInitializePackage#

**URL:** https://petsc.org/release/manualpages/Vec/ISInitializePackage/

**Contents:**
- ISInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function initializes everything in the IS package. It is called from PetscDLLibraryRegister_petscvec() when using dynamic libraries, and on the first call to ISCreateXXXX() when using shared or static libraries.

src/vec/vec/interface/dlregisvec.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" */
PetscErrorCode ISInitializePackage(void)
```

Example 2 (unknown):
```unknown
PetscInitialize()
```

---

## ISIntersect#

**URL:** https://petsc.org/release/manualpages/IS/ISIntersect/

**Contents:**
- ISIntersect#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Computes the intersection of two index sets, by sorting and comparing.

is1 - first index set

is2 - second index set

isout - the sorted intersection of is1 and is2

Negative values are removed from the lists. This requires O(min(is1,is2)) memory and O(max(is1,is2)log(max(is1,is2))) work

is1 and is2 do not need to be sorted.

The operations are performed separately on each MPI rank

Low-level Vector Communication, IS, ISDestroy(), ISView(), ISDifference(), ISSum(), ISExpand(), ISConcatenate()

src/vec/is/is/utils/isdiff.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISIntersect(IS is1, IS is2, IS *isout)
```

Example 2 (unknown):
```unknown
ISDestroy()
```

Example 3 (unknown):
```unknown
ISDifference()
```

Example 4 (unknown):
```unknown
ISConcatenate()
```

---

## ISInvertPermutation#

**URL:** https://petsc.org/release/manualpages/IS/ISInvertPermutation/

**Contents:**
- ISInvertPermutation#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Creates a new permutation that is the inverse of a given permutation.

nlocal - number of indices on this processor in result (ignored for 1 processor) or use PETSC_DECIDE

isout - the inverse permutation

For parallel index sets this does the complete parallel permutation, but the code is not efficient for huge index sets (10,000,000 indices).

IS, ISGetInfo(), ISSetPermutation(), ISGetPermutation()

src/vec/is/is/interface/index.c

ISInvertPermutation_Block() in src/vec/is/is/impls/block/block.c ISInvertPermutation_General() in src/vec/is/is/impls/general/general.c ISInvertPermutation_Stride() in src/vec/is/is/impls/stride/stride.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISInvertPermutation(IS is, PetscInt nlocal, IS *isout)
```

Example 2 (unknown):
```unknown
PETSC_DECIDE
```

Example 3 (unknown):
```unknown
ISGetInfo()
```

Example 4 (unknown):
```unknown
ISSetPermutation()
```

---

## ISListToPair#

**URL:** https://petsc.org/release/manualpages/IS/ISListToPair/

**Contents:**
- ISListToPair#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Convert an IS list to a pair of IS of equal length defining an equivalent integer multimap. Each IS in islist is assigned an integer j so that all of the indices of that IS are mapped to j.

listlen - IS list length

The global integers assigned to the IS of islist might not correspond to the local numbers of the IS on that list, but the two orderings are the same: the global integers assigned to the IS on the local list form a strictly increasing sequence.

The IS in islist can belong to subcommunicators of comm, and the subcommunicators on the input IS list are assumed to be in a “deadlock-free” order.

Local lists of PetscObjects (or their subcomms) on a comm are “deadlock-free” if subcomm1 precedes subcomm2 on any local list, then it precedes subcomm2 on all ranks. Equivalently, the local numbers of the subcomms on each local list are drawn from some global numbering. This is ensured, for example, by ISPairToList().

src/vec/is/is/utils/isdiff.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISListToPair(MPI_Comm comm, PetscInt listlen, IS islist[], IS *xis, IS *yis)
```

Example 2 (unknown):
```unknown
PetscObject
```

Example 3 (unknown):
```unknown
ISPairToList()
```

Example 4 (unknown):
```unknown
ISPairToList()
```

---

## ISLoad#

**URL:** https://petsc.org/release/manualpages/IS/ISLoad/

**Contents:**
- ISLoad#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Loads an index set that has been stored in binary or HDF5 format with ISView().

is - the newly loaded index set, this needs to have been created with ISCreate() or some related function before a call to ISLoad().

viewer - binary file viewer, obtained from PetscViewerBinaryOpen() or HDF5 file viewer, obtained from PetscViewerHDF5Open()

IF using HDF5, you must assign the IS the same name as was used in is that was stored in the file using PetscObjectSetName(). Otherwise you will get the error message: “Cannot H5DOpen2() with Vec name NAMEOFOBJECT”

IS, PetscViewerBinaryOpen(), ISView(), MatLoad(), VecLoad()

src/vec/is/is/interface/index.c

src/ksp/ksp/tutorials/ex87.c src/ksp/ksp/tutorials/ex76.c src/ksp/ksp/tutorials/ex76f.F90

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISLoad(IS is, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscViewerBinaryOpen()
```

Example 3 (unknown):
```unknown
PetscViewerHDF5Open()
```

Example 4 (unknown):
```unknown
PetscObjectSetName()
```

---

## ISLocalToGlobalMappingApplyBlock#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingApplyBlock/

**Contents:**
- ISLocalToGlobalMappingApplyBlock#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Example#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Takes a list of integers in a local block numbering and converts them to the global block numbering

mapping - the local to global mapping context

N - number of integers

in - input indices in local block numbering

out - indices in global block numbering

If the index values are {0,1,6,7} set with a call to ISLocalToGlobalMappingCreate(PETSC_COMM_SELF,2,2,{0,3}) then the mapping applied to 0 (the first block) would produce 0 and the mapping applied to 1 (the second block) would produce 3.

The in and out array parameters may be identical.

Low-level Vector Communication, ISLocalToGlobalMappingApply(), ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingDestroy(), ISLocalToGlobalMappingApplyIS(), AOCreateBasic(), AOApplicationToPetsc(), AOPetscToApplication(), ISGlobalToLocalMappingApply()

src/vec/is/utils/isltog.c

src/ksp/ksp/tutorials/ex71.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingApplyBlock(ISLocalToGlobalMapping mapping, PetscInt N, const PetscInt in[], PetscInt out[])
```

Example 2 (unknown):
```unknown
ISLocalToGlobalMappingCreate
```

Example 3 (unknown):
```unknown
PETSC_COMM_SELF
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingApply()
```

---

## ISLocalToGlobalMappingApplyIS#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingApplyIS/

**Contents:**
- ISLocalToGlobalMappingApplyIS#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Creates from an IS in the local numbering a new index set using the global numbering defined in an ISLocalToGlobalMapping context.

mapping - mapping between local and global numbering

is - index set in local numbering

newis - index set in global numbering

The output IS will have the same communicator as the input IS as well as the same block size.

Low-level Vector Communication, ISLocalToGlobalMappingApply(), ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingDestroy(), ISGlobalToLocalMappingApply()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 2 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingApplyIS(ISLocalToGlobalMapping mapping, IS is, IS *newis)
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingApply()
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingCreate()
```

---

## ISLocalToGlobalMappingApply#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingApply/

**Contents:**
- ISLocalToGlobalMappingApply#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Takes a list of integers in a local numbering and converts them to the global numbering.

mapping - the local to global mapping context

N - number of integers

in - input indices in local numbering

out - indices in global numbering

The in and out array parameters may be identical.

Low-level Vector Communication, ISLocalToGlobalMapping, ISLocalToGlobalMappingApplyBlock(), ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingDestroy(), ISLocalToGlobalMappingApplyIS(), AOCreateBasic(), AOApplicationToPetsc(), AOPetscToApplication(), ISGlobalToLocalMappingApply()

src/vec/is/utils/isltog.c

src/vec/is/is/tutorials/ex4.c src/vec/is/is/tutorials/ex5.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingApply(ISLocalToGlobalMapping mapping, PetscInt N, const PetscInt in[], PetscInt out[])
```

Example 2 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingApplyBlock()
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingCreate()
```

---

## ISLOCALTOGLOBALMAPPINGBASIC#

**URL:** https://petsc.org/release/manualpages/IS/ISLOCALTOGLOBALMAPPINGBASIC/

**Contents:**
- ISLOCALTOGLOBALMAPPINGBASIC#
- Options Database Key#
- Developer Note#
- See Also#
- Level#
- Location#

basic implementation of the ISLocalToGlobalMapping object. When ISGlobalToLocalMappingApply() is used this is good for only small and moderate size problems.

-islocaltoglobalmapping_type basic - select this method

This stores all the mapping information on each MPI rank.

Low-level Vector Communication, ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingSetType(), ISLOCALTOGLOBALMAPPINGHASH

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 2 (unknown):
```unknown
ISGlobalToLocalMappingApply()
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingCreate()
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingSetType()
```

---

## ISLocalToGlobalMappingConcatenate#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingConcatenate/

**Contents:**
- ISLocalToGlobalMappingConcatenate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#

Create a new mapping that concatenates a list of mappings

comm - communicator for the new mapping, must contain the communicator of every mapping to concatenate

n - number of mappings to concatenate

ltogs - local to global mappings

ltogcat - new mapping

This currently always returns a mapping with block size of 1

If all the input mapping have the same block size we could easily handle that as a special case

Low-level Vector Communication, ISLocalToGlobalMapping, ISLocalToGlobalMappingCreate()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingConcatenate(MPI_Comm comm, PetscInt n, const ISLocalToGlobalMapping ltogs[], ISLocalToGlobalMapping *ltogcat)
```

Example 2 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingCreate()
```

---

## ISLocalToGlobalMappingCreateIS#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingCreateIS/

**Contents:**
- ISLocalToGlobalMappingCreateIS#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Creates a mapping between a local (0 to n) ordering and a global parallel ordering.

is - index set containing the global numbers for each local number

mapping - new mapping data structure

the block size of the IS determines the block size of the mapping

Low-level Vector Communication, ISLocalToGlobalMapping, ISLocalToGlobalMappingDestroy(), ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingSetFromOptions()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingCreateIS(IS is, ISLocalToGlobalMapping *mapping)
```

Example 2 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingDestroy()
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingCreate()
```

---

## ISLocalToGlobalMappingCreateSF#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingCreateSF/

**Contents:**
- ISLocalToGlobalMappingCreateSF#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Creates a mapping between a local (0 to n) ordering and a global parallel ordering induced by a star forest.

sf - star forest mapping contiguous local indices to (rank, offset)

start - first global index on this process, or PETSC_DECIDE to compute contiguous global numbering automatically

mapping - new mapping data structure

If a process calls this function with start = PETSC_DECIDE then all processes must, otherwise the program will hang.

Low-level Vector Communication, PetscSF, ISLocalToGlobalMappingDestroy(), ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingCreateIS(), ISLocalToGlobalMappingSetFromOptions()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingCreateSF(PetscSF sf, PetscInt start, ISLocalToGlobalMapping *mapping)
```

Example 2 (unknown):
```unknown
PETSC_DECIDE
```

Example 3 (unknown):
```unknown
PETSC_DECIDE
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingDestroy()
```

---

## ISLocalToGlobalMappingCreate#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingCreate/

**Contents:**
- ISLocalToGlobalMappingCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates a mapping between a local (0 to n) ordering and a global parallel ordering.

Not Collective, but communicator may have more than one process

comm - MPI communicator

n - the number of local elements divided by the block size, or equivalently the number of block indices

indices - the global index for each local element, these do not need to be in increasing order (sorted), these values should not be scaled (i.e. multiplied) by the blocksize bs

mode - see PetscCopyMode

mapping - new mapping data structure

There is one integer value in indices per block and it represents the actual indices bs*idx + j, where j=0,..,bs-1

For “small” problems when using ISGlobalToLocalMappingApply() and ISGlobalToLocalMappingApplyBlock(), the ISLocalToGlobalMappingType of ISLOCALTOGLOBALMAPPINGBASIC will be used; this uses more memory but is faster; this approach is not scalable for extremely large mappings.

For large problems ISLOCALTOGLOBALMAPPINGHASH is used, this is scalable. Use ISLocalToGlobalMappingSetType() or call ISLocalToGlobalMappingSetFromOptions() with the option -islocaltoglobalmapping_type <basic,hash> to control which is used.

Low-level Vector Communication, ISLocalToGlobalMapping, ISLocalToGlobalMappingDestroy(), ISLocalToGlobalMappingCreateIS(), ISLocalToGlobalMappingSetFromOptions(), ISLOCALTOGLOBALMAPPINGBASIC, ISLOCALTOGLOBALMAPPINGHASH, ISLocalToGlobalMappingSetType(), ISLocalToGlobalMappingType

src/vec/is/utils/isltog.c

src/ksp/ksp/tutorials/ex85.c src/mat/tutorials/ex3.c src/vec/vec/tutorials/ex8f.F90 src/ksp/ksp/tutorials/ex59.c src/ksp/ksp/tutorials/ex71.c src/vec/is/is/tutorials/ex4.c src/vec/is/is/tutorials/ex5.c src/vec/vec/tutorials/ex8.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingCreate(MPI_Comm comm, PetscInt bs, PetscInt n, const PetscInt indices[], PetscCopyMode mode, ISLocalToGlobalMapping *mapping)
```

Example 2 (unknown):
```unknown
ISGlobalToLocalMappingApply()
```

Example 3 (unknown):
```unknown
ISGlobalToLocalMappingApplyBlock()
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingType
```

---

## ISLocalToGlobalMappingDestroy#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingDestroy/

**Contents:**
- ISLocalToGlobalMappingDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#

Destroys a mapping between a local (0 to n) ordering and a global parallel ordering.

mapping - mapping data structure

Low-level Vector Communication, ISLocalToGlobalMapping, ISLocalToGlobalMappingCreate()

src/vec/is/utils/isltog.c

src/ksp/ksp/tutorials/ex85.c src/mat/tutorials/ex3.c src/vec/vec/tutorials/ex8f.F90 src/ksp/ksp/tutorials/ex59.c src/ksp/ksp/tutorials/ex71.c src/vec/is/is/tutorials/ex4.c src/vec/is/is/tutorials/ex5.c src/vec/vec/tutorials/ex8.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingDestroy(ISLocalToGlobalMapping *mapping)
```

Example 2 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingCreate()
```

---

## ISLocalToGlobalMappingDuplicate#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingDuplicate/

**Contents:**
- ISLocalToGlobalMappingDuplicate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Duplicates the local to global mapping object

ltog - local to global mapping

nltog - the duplicated local to global mapping

Low-level Vector Communication, ISLocalToGlobalMapping, ISLocalToGlobalMappingDestroy(), ISLocalToGlobalMappingCreate()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingDuplicate(ISLocalToGlobalMapping ltog, ISLocalToGlobalMapping *nltog)
```

Example 2 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingDestroy()
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingCreate()
```

---

## ISLocalToGlobalMappingGetBlockIndices#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingGetBlockIndices/

**Contents:**
- ISLocalToGlobalMappingGetBlockIndices#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get global indices for every local block in a ISLocalToGlobalMapping

ltog - local to global mapping

array - array of indices

Low-level Vector Communication, ISLocalToGlobalMapping, ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingApply(), ISLocalToGlobalMappingRestoreBlockIndices()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 2 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingGetBlockIndices(ISLocalToGlobalMapping ltog, const PetscInt *array[])
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingCreate()
```

---

## ISLocalToGlobalMappingGetBlockInfo#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingGetBlockInfo/

**Contents:**
- ISLocalToGlobalMappingGetBlockInfo#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Gets the neighbor information

Collective the first time it is called

mapping - the mapping from local to global indexing

nproc - number of processes that are connected to the calling process

procs - neighboring processes

numprocs - number of block indices for each process

indices - block indices (in local numbering) shared with neighbors (sorted by global numbering)

Low-level Vector Communication, ISLocalToGlobalMappingDestroy(), ISLocalToGlobalMappingCreateIS(), ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingRestoreBlockInfo(), ISLocalToGlobalMappingGetBlockMultiLeavesSF()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingGetBlockInfo(ISLocalToGlobalMapping mapping, PetscInt *nproc, PetscInt *procs[], PetscInt *numprocs[], PetscInt **indices[])
```

Example 2 (unknown):
```unknown
ISLocalToGlobalMappingDestroy()
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingCreateIS()
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingCreate()
```

---

## ISLocalToGlobalMappingGetBlockMultiLeavesSF#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingGetBlockMultiLeavesSF/

**Contents:**
- ISLocalToGlobalMappingGetBlockMultiLeavesSF#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Get the star-forest to communicate multi-leaf block data

Collective the first time it is called

mapping - the mapping from local to global indexing

The returned star forest is suitable to exchange local information with other processes sharing the same global block index. For example, suppose a mapping with two processes has been created with

and we want to share the local information

then, the broadcasting action of mlsf will allow to collect

Use ISLocalToGlobalMappingGetBlockNodeInfo() to index into the multi-leaf data.

Low-level Vector Communication, ISLocalToGlobalMappingGetBlockNodeInfo(), PetscSF

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingGetBlockMultiLeavesSF(ISLocalToGlobalMapping mapping, PetscSF *mlsf)
```

Example 2 (json):
```json
rank 0 global block indices: [0, 1, 2]
    rank 1 global block indices: [2, 3, 4]
```

Example 3 (json):
```json
rank 0 data: [-1, -2, -3]
    rank 1 data: [1, 2, 3]
```

Example 4 (json):
```json
rank 0 mlleafdata: [-1, -2, -3, 3]
    rank 1 mlleafdata: [-3, 3, 1, 2]
```

---

## ISLocalToGlobalMappingGetBlockNodeInfo#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingGetBlockNodeInfo/

**Contents:**
- ISLocalToGlobalMappingGetBlockNodeInfo#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Gets the neighbor information for each local block index

Collective the first time it is called

mapping - the mapping from local to global indexing

n - number of local block nodes

n_procs - an array storing the number of processes for each local block node (including self)

procs - the processes’ rank for each local block node (sorted, self is first)

The user needs to call ISLocalToGlobalMappingRestoreBlockNodeInfo() when the data is no longer needed. The information returned by this function complements that of ISLocalToGlobalMappingGetBlockInfo(). The latter only provides local information, and the neighboring information cannot be inferred in the general case, unless the mapping is locally one-to-one on each process.

ISLocalToGlobalMappingDestroy(), ISLocalToGlobalMappingCreateIS(), ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingGetBlockInfo(), ISLocalToGlobalMappingRestoreBlockNodeInfo(), ISLocalToGlobalMappingGetNodeInfo()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingGetBlockNodeInfo(ISLocalToGlobalMapping mapping, PetscInt *n, PetscInt *n_procs[], PetscInt **procs[])
```

Example 2 (unknown):
```unknown
ISLocalToGlobalMappingRestoreBlockNodeInfo()
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingGetBlockInfo()
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingDestroy()
```

---

## ISLocalToGlobalMappingGetBlockSize#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingGetBlockSize/

**Contents:**
- ISLocalToGlobalMappingGetBlockSize#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the blocksize of the mapping ordering and a global parallel ordering.

mapping - mapping data structure

Low-level Vector Communication, ISLocalToGlobalMapping, ISLocalToGlobalMappingDestroy(), ISLocalToGlobalMappingCreateIS()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingGetBlockSize(ISLocalToGlobalMapping mapping, PetscInt *bs)
```

Example 2 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingDestroy()
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingCreateIS()
```

---

## ISLocalToGlobalMappingGetIndices#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingGetIndices/

**Contents:**
- ISLocalToGlobalMappingGetIndices#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Get global indices for every local point that is mapped

ltog - local to global mapping

array - array of indices, the length of this array may be obtained with ISLocalToGlobalMappingGetSize()

ISLocalToGlobalMappingGetSize() returns the length the this array

Low-level Vector Communication, ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingApply(), ISLocalToGlobalMappingRestoreIndices(), ISLocalToGlobalMappingGetBlockIndices(), ISLocalToGlobalMappingRestoreBlockIndices()

src/vec/is/utils/isltog.c

src/ksp/ksp/tutorials/ex43.c src/ksp/ksp/tutorials/ex70.c src/ksp/ksp/tutorials/ex49.c src/ksp/ksp/tutorials/ex14f.F90

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingGetIndices(ISLocalToGlobalMapping ltog, const PetscInt *array[])
```

Example 2 (unknown):
```unknown
ISLocalToGlobalMappingGetSize()
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingGetSize()
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingCreate()
```

---

## ISLocalToGlobalMappingGetInfo#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingGetInfo/

**Contents:**
- ISLocalToGlobalMappingGetInfo#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- Fortran Notes#
- See Also#
- Level#
- Location#

Gets the neighbor information for each process

Collective the first time it is called

mapping - the mapping from local to global indexing

nproc - number of processes that are connected to the calling process

procs - neighboring processes

numprocs - number of indices for each process

indices - indices (in local numbering) shared with neighbors (sorted by global numbering)

The user needs to call ISLocalToGlobalMappingRestoreInfo() when the data is no longer needed.

There is no ISLocalToGlobalMappingRestoreInfo() in Fortran. You must make sure that procs[], numprocs[] and indices[][] are large enough arrays, either by allocating them dynamically or defining static ones large enough.

Low-level Vector Communication, ISLocalToGlobalMappingDestroy(), ISLocalToGlobalMappingCreateIS(), ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingRestoreInfo(), ISLocalToGlobalMappingGetNodeInfo()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingGetInfo(ISLocalToGlobalMapping mapping, PetscInt *nproc, PetscInt *procs[], PetscInt *numprocs[], PetscInt **indices[])
```

Example 2 (unknown):
```unknown
ISLocalToGlobalMappingRestoreInfo()
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingRestoreInfo()
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingDestroy()
```

---

## ISLocalToGlobalMappingGetNodeInfo#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingGetNodeInfo/

**Contents:**
- ISLocalToGlobalMappingGetNodeInfo#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Gets the neighbor information of local nodes

Collective the first time it is called

mapping - the mapping from local to global indexing

n - number of local nodes

n_procs - an array storing the number of processes for each local node (including self)

procs - the processes’ rank for each local node (sorted, self is first)

The user needs to call ISLocalToGlobalMappingRestoreNodeInfo() when the data is no longer needed.

Low-level Vector Communication, ISLocalToGlobalMappingDestroy(), ISLocalToGlobalMappingCreateIS(), ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingGetInfo(), ISLocalToGlobalMappingRestoreNodeInfo(), ISLocalToGlobalMappingGetBlockNodeInfo()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingGetNodeInfo(ISLocalToGlobalMapping mapping, PetscInt *n, PetscInt *n_procs[], PetscInt **procs[])
```

Example 2 (unknown):
```unknown
ISLocalToGlobalMappingRestoreNodeInfo()
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingDestroy()
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingCreateIS()
```

---

## ISLocalToGlobalMappingGetSize#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingGetSize/

**Contents:**
- ISLocalToGlobalMappingGetSize#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the local size of a local to global mapping

mapping - local to global mapping

n - the number of entries in the local mapping, ISLocalToGlobalMappingGetIndices() returns an array of this length

Low-level Vector Communication, ISLocalToGlobalMapping, ISLocalToGlobalMappingDestroy(), ISLocalToGlobalMappingCreate()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingGetSize(ISLocalToGlobalMapping mapping, PetscInt *n)
```

Example 2 (unknown):
```unknown
ISLocalToGlobalMappingGetIndices()
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingDestroy()
```

---

## ISLocalToGlobalMappingGetType#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingGetType/

**Contents:**
- ISLocalToGlobalMappingGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Get the type of the ISLocalToGlobalMapping

ltog - the ISLocalToGlobalMapping object

type should not be retained for later use as it will be an invalid pointer if the ISLocalToGlobalMappingType of ltog is changed.

Low-level Vector Communication, ISLocalToGlobalMappingType, ISLocalToGlobalMappingRegister(), ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingSetType(), PetscObjectTypeCompare(), PetscObjectTypeCompareAny()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 2 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingGetType(ISLocalToGlobalMapping ltog, ISLocalToGlobalMappingType *type)
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingType
```

---

## ISLOCALTOGLOBALMAPPINGHASH#

**URL:** https://petsc.org/release/manualpages/IS/ISLOCALTOGLOBALMAPPINGHASH/

**Contents:**
- ISLOCALTOGLOBALMAPPINGHASH#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

hash implementation of the ISLocalToGlobalMapping object. When ISGlobalToLocalMappingApply() is used this is good for large memory problems.

-islocaltoglobalmapping_type hash - select this method

This is selected automatically for large problems if the user does not set the type.

Low-level Vector Communication, ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingSetType(), ISLOCALTOGLOBALMAPPINGBASIC

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 2 (unknown):
```unknown
ISGlobalToLocalMappingApply()
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingCreate()
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingSetType()
```

---

## ISLocalToGlobalMappingLoad#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingLoad/

**Contents:**
- ISLocalToGlobalMappingLoad#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Loads a local-to-global mapping that has been stored in binary format.

mapping - the newly loaded map, this needs to have been created with ISLocalToGlobalMappingCreate() or some related function before a call to ISLocalToGlobalMappingLoad()

viewer - binary file viewer, obtained from PetscViewerBinaryOpen()

Low-level Vector Communication, PetscViewer, ISLocalToGlobalMapping, ISLocalToGlobalMappingView(), ISLocalToGlobalMappingCreate()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingLoad(ISLocalToGlobalMapping mapping, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
ISLocalToGlobalMappingCreate()
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingLoad()
```

Example 4 (unknown):
```unknown
PetscViewerBinaryOpen()
```

---

## ISLocalToGlobalMappingRegisterAll#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingRegisterAll/

**Contents:**
- ISLocalToGlobalMappingRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the local to global mapping components in the IS package.

Low-level Vector Communication, ISRegister(), ISLocalToGlobalRegister()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingRegisterAll(void)
```

Example 2 (unknown):
```unknown
ISRegister()
```

Example 3 (unknown):
```unknown
ISLocalToGlobalRegister()
```

---

## ISLocalToGlobalMappingRegister#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingRegister/

**Contents:**
- ISLocalToGlobalMappingRegister#
- Synopsis#
- Input Parameters#
- Example Usage#
- Note#
- See Also#
- Level#
- Location#

Registers a method for applying a global to local mapping with an ISLocalToGlobalMapping

Not Collective, No Fortran Support

sname - name of a new method

function - routine to create method context

Then, your mapping can be chosen with the procedural interface via

or at runtime via the option

ISLocalToGlobalMappingRegister() may be called multiple times to add several user-defined mappings.

Low-level Vector Communication, ISLocalToGlobalMappingRegisterAll(), ISLocalToGlobalMappingRegisterDestroy(), ISLOCALTOGLOBALMAPPINGBASIC, ISLOCALTOGLOBALMAPPINGHASH, ISLocalToGlobalMapping, ISLocalToGlobalMappingApply()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 2 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingRegister(const char sname[], PetscErrorCode (*function)(ISLocalToGlobalMapping))
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingRegister("my_mapper", MyCreate);
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingSetType(ltog, "my_mapper")
```

---

## ISLocalToGlobalMappingRestoreBlockIndices#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingRestoreBlockIndices/

**Contents:**
- ISLocalToGlobalMappingRestoreBlockIndices#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Restore indices obtained with ISLocalToGlobalMappingGetBlockIndices()

ltog - local to global mapping

array - array of indices

Low-level Vector Communication, ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingApply(), ISLocalToGlobalMappingGetIndices()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISLocalToGlobalMappingGetBlockIndices()
```

Example 2 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingRestoreBlockIndices(ISLocalToGlobalMapping ltog, const PetscInt *array[])
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingCreate()
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingApply()
```

---

## ISLocalToGlobalMappingRestoreBlockInfo#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingRestoreBlockInfo/

**Contents:**
- ISLocalToGlobalMappingRestoreBlockInfo#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Frees the memory allocated by ISLocalToGlobalMappingGetBlockInfo()

mapping - the mapping from local to global indexing

nproc - number of processes that are connected to the calling process

procs - neighboring processes

numprocs - number of block indices for each process

indices - block indices (in local numbering) shared with neighbors (sorted by global numbering)

Low-level Vector Communication, ISLocalToGlobalMappingDestroy(), ISLocalToGlobalMappingCreateIS(), ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingGetInfo()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISLocalToGlobalMappingGetBlockInfo()
```

Example 2 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingRestoreBlockInfo(ISLocalToGlobalMapping mapping, PetscInt *nproc, PetscInt *procs[], PetscInt *numprocs[], PetscInt **indices[])
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingDestroy()
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingCreateIS()
```

---

## ISLocalToGlobalMappingRestoreBlockNodeInfo#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingRestoreBlockNodeInfo/

**Contents:**
- ISLocalToGlobalMappingRestoreBlockNodeInfo#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Frees the memory allocated by ISLocalToGlobalMappingGetBlockNodeInfo()

mapping - the mapping from local to global indexing

n - number of local block nodes

n_procs - an array storing the number of processes for each local block nodes (including self)

procs - the processes’ rank for each local block node (sorted, self is first)

ISLocalToGlobalMappingDestroy(), ISLocalToGlobalMappingCreateIS(), ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingGetBlockNodeInfo()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISLocalToGlobalMappingGetBlockNodeInfo()
```

Example 2 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingRestoreBlockNodeInfo(ISLocalToGlobalMapping mapping, PetscInt *n, PetscInt *n_procs[], PetscInt **procs[])
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingDestroy()
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingCreateIS()
```

---

## ISLocalToGlobalMappingRestoreIndices#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingRestoreIndices/

**Contents:**
- ISLocalToGlobalMappingRestoreIndices#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Restore indices obtained with ISLocalToGlobalMappingGetIndices()

ltog - local to global mapping

array - array of indices

Low-level Vector Communication, ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingApply(), ISLocalToGlobalMappingGetIndices()

src/vec/is/utils/isltog.c

src/ksp/ksp/tutorials/ex43.c src/ksp/ksp/tutorials/ex70.c src/ksp/ksp/tutorials/ex49.c src/ksp/ksp/tutorials/ex14f.F90

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISLocalToGlobalMappingGetIndices()
```

Example 2 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingRestoreIndices(ISLocalToGlobalMapping ltog, const PetscInt *array[])
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingCreate()
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingApply()
```

---

## ISLocalToGlobalMappingRestoreInfo#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingRestoreInfo/

**Contents:**
- ISLocalToGlobalMappingRestoreInfo#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Frees the memory allocated by ISLocalToGlobalMappingGetInfo()

mapping - the mapping from local to global indexing

nproc - number of processes that are connected to the calling process

procs - neighboring processes

numprocs - number of indices for each process

indices - indices (in local numbering) shared with neighbors (sorted by global numbering)

Low-level Vector Communication, ISLocalToGlobalMappingDestroy(), ISLocalToGlobalMappingCreateIS(), ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingGetInfo()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISLocalToGlobalMappingGetInfo()
```

Example 2 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingRestoreInfo(ISLocalToGlobalMapping mapping, PetscInt *nproc, PetscInt *procs[], PetscInt *numprocs[], PetscInt **indices[])
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingDestroy()
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingCreateIS()
```

---

## ISLocalToGlobalMappingRestoreNodeInfo#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingRestoreNodeInfo/

**Contents:**
- ISLocalToGlobalMappingRestoreNodeInfo#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Frees the memory allocated by ISLocalToGlobalMappingGetNodeInfo()

mapping - the mapping from local to global indexing

n - number of local nodes

n_procs - an array storing the number of processes for each local node (including self)

procs - the processes’ rank for each local node (sorted, self is first)

Low-level Vector Communication, ISLocalToGlobalMappingDestroy(), ISLocalToGlobalMappingCreateIS(), ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingGetInfo()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISLocalToGlobalMappingGetNodeInfo()
```

Example 2 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingRestoreNodeInfo(ISLocalToGlobalMapping mapping, PetscInt *n, PetscInt *n_procs[], PetscInt **procs[])
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingDestroy()
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingCreateIS()
```

---

## ISLocalToGlobalMappingSetBlockSize#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingSetBlockSize/

**Contents:**
- ISLocalToGlobalMappingSetBlockSize#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the blocksize of the mapping

mapping - mapping data structure

Low-level Vector Communication, ISLocalToGlobalMapping, ISLocalToGlobalMappingDestroy(), ISLocalToGlobalMappingCreateIS()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingSetBlockSize(ISLocalToGlobalMapping mapping, PetscInt bs)
```

Example 2 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingDestroy()
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingCreateIS()
```

---

## ISLocalToGlobalMappingSetFromOptions#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingSetFromOptions/

**Contents:**
- ISLocalToGlobalMappingSetFromOptions#
- Synopsis#
- Input Parameter#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

Set mapping options from the options database.

mapping - mapping data structure

-islocaltoglobalmapping_type (basic|hash) - nonscalable and scalable versions

Low-level Vector Communication, ISLocalToGlobalMapping, ISLocalToGlobalMappingDestroy(), ISLocalToGlobalMappingCreateIS(), ISLOCALTOGLOBALMAPPINGBASIC, ISLOCALTOGLOBALMAPPINGHASH, ISLocalToGlobalMappingSetType(), ISLocalToGlobalMappingType

src/vec/is/utils/isltog.c

src/vec/is/is/tutorials/ex4.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingSetFromOptions(ISLocalToGlobalMapping mapping)
```

Example 2 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingDestroy()
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingCreateIS()
```

---

## ISLocalToGlobalMappingSetType#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingSetType/

**Contents:**
- ISLocalToGlobalMappingSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#

Sets the implementation type ISLocalToGlobalMapping will use

ltog - the ISLocalToGlobalMapping object

type - a known method

-islocaltoglobalmapping_type (basic|hash) - Sets the method used for applying the mapping, see ISLocalToGlobalMappingType

See ISLocalToGlobalMappingType for available methods

Normally, it is best to use the ISLocalToGlobalMappingSetFromOptions() command and then set the ISLocalToGlobalMappingType from the options database rather than by using this routine.

ISLocalToGlobalMappingRegister() is used to add new types to ISLocalToGlobalMappingList from which they are accessed by ISLocalToGlobalMappingSetType().

Low-level Vector Communication, ISLocalToGlobalMappingType, ISLocalToGlobalMappingRegister(), ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingGetType()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 2 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingSetType(ISLocalToGlobalMapping ltog, ISLocalToGlobalMappingType type)
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingType
```

---

## ISLocalToGlobalMappingType#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingType/

**Contents:**
- ISLocalToGlobalMappingType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

String with the name of a mapping method

ISLOCALTOGLOBALMAPPINGBASIC - a non-memory scalable way of storing ISLocalToGlobalMapping that allows applying ISGlobalToLocalMappingApply() efficiently

ISLOCALTOGLOBALMAPPINGHASH - a memory scalable way of storing ISLocalToGlobalMapping that allows applying ISGlobalToLocalMappingApply() reasonably efficiently

ISLocalToGlobalMapping, ISLocalToGlobalMappingSetType(), ISLocalToGlobalSetFromOptions(), ISGlobalToLocalMappingMode

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
typedef const char *ISLocalToGlobalMappingType;
#define ISLOCALTOGLOBALMAPPINGBASIC "basic"
#define ISLOCALTOGLOBALMAPPINGHASH  "hash"
```

Example 2 (unknown):
```unknown
ISLOCALTOGLOBALMAPPINGBASIC
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 4 (unknown):
```unknown
ISGlobalToLocalMappingApply()
```

---

## ISLocalToGlobalMappingViewFromOptions#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingViewFromOptions/

**Contents:**
- ISLocalToGlobalMappingViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

View an ISLocalToGlobalMapping based on values in the options database

A - the local to global mapping object

obj - Optional object that provides the options prefix used for the options database query

name - command line option

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

Low-level Vector Communication, PetscViewer, ISLocalToGlobalMapping, ISLocalToGlobalMappingView, PetscObjectViewFromOptions(), ISLocalToGlobalMappingCreate()

src/vec/is/utils/isltog.c

src/ksp/ksp/tutorials/ex71.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 2 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingViewFromOptions(ISLocalToGlobalMapping A, PetscObject obj, const char name[])
```

Example 3 (unknown):
```unknown
PetscObjectViewFromOptions()
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## ISLocalToGlobalMappingView#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMappingView/

**Contents:**
- ISLocalToGlobalMappingView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

View a local to global mapping

mapping - local to global mapping

Low-level Vector Communication, PetscViewer, ISLocalToGlobalMapping, ISLocalToGlobalMappingDestroy(), ISLocalToGlobalMappingCreate()

src/vec/is/utils/isltog.c

src/vec/is/is/tutorials/ex4.c src/vec/vec/tutorials/ex9.c

ISLocalToGlobalMappingView_Multi() in src/mat/impls/is/matis.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISLocalToGlobalMappingView(ISLocalToGlobalMapping mapping, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingDestroy()
```

---

## ISLocalToGlobalMapping#

**URL:** https://petsc.org/release/manualpages/IS/ISLocalToGlobalMapping/

**Contents:**
- ISLocalToGlobalMapping#
- Synopsis#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

mappings from a local ordering (on individual MPI processes) of 0 to n-1 to a global PETSc ordering (across collections of MPI processes) used by a vector or matrix.

Mapping from local to global is scalable; but global to local may not be if the range of global values represented locally is very large. ISLocalToGlobalMappingType provides alternative ways of efficiently applying `ISGlobalToLocalMappingApply()

ISLocalToGlobalMapping is actually a private object; it is included here for the inline function ISLocalToGlobalMappingApply() to allow it to be inlined since it is used so often.

ISLocalToGlobalMappingCreate(), ISLocalToGlobalMappingApply(), ISLocalToGlobalMappingDestroy(), ISGlobalToLocalMappingApply()

include/petscistypes.h

src/mat/tutorials/ex3.c src/ksp/ksp/tutorials/ex85.c src/vec/vec/tutorials/ex8f.F90 src/ksp/ksp/tutorials/ex59.c src/ksp/ksp/tutorials/ex70.c src/ksp/ksp/tutorials/ex14f.F90 src/ksp/ksp/tutorials/ex71.c src/ksp/ksp/tutorials/ex49.c src/snes/tutorials/ex48.c src/ksp/ksp/tutorials/ex43.c

_p_ISLocalToGlobalMapping in include/petsc/private/isimpl.h ISLocalToGlobalMapping_Basic in src/vec/is/utils/isltog.c ISLocalToGlobalMapping_Hash in src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_ISLocalToGlobalMapping *ISLocalToGlobalMapping;
```

Example 2 (unknown):
```unknown
ISLocalToGlobalMappingType
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingApply()
```

---

## ISLocate#

**URL:** https://petsc.org/release/manualpages/IS/ISLocate/

**Contents:**
- ISLocate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

determine the location of an index within the local component of an index set

location - if >= 0, a location within the index set that is equal to the key, otherwise the key is not in the index set

src/vec/is/is/interface/index.c

src/ksp/ksp/tutorials/ex76.c

ISLocate_Block() in src/vec/is/is/impls/block/block.c ISLocate_General() in src/vec/is/is/impls/general/general.c ISLocate_Stride() in src/vec/is/is/impls/stride/stride.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISLocate(IS is, PetscInt key, PetscInt *location)
```

---

## ISOnComm#

**URL:** https://petsc.org/release/manualpages/IS/ISOnComm/

**Contents:**
- ISOnComm#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Split a parallel IS on subcomms (usually self) or concatenate index sets on subcomms into a parallel index set

comm - communicator for new index set

mode - copy semantics, PETSC_USE_POINTER for no-copy if possible, otherwise PETSC_COPY_VALUES

newis - new IS on comm

It is usually desirable to create a parallel IS and look at the local part when necessary.

This function is useful if serial ISs must be created independently, or to view many logically independent serial ISs.

The input IS must have the same type on every MPI process.

src/vec/is/is/interface/index.c

src/dm/label/tutorials/ex1.c

ISOnComm_Block() in src/vec/is/is/impls/block/block.c ISOnComm_General() in src/vec/is/is/impls/general/general.c ISOnComm_Stride() in src/vec/is/is/impls/stride/stride.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISOnComm(IS is, MPI_Comm comm, PetscCopyMode mode, IS *newis)
```

Example 2 (unknown):
```unknown
PETSC_USE_POINTER
```

Example 3 (unknown):
```unknown
PETSC_COPY_VALUES
```

---

## ISPairToList#

**URL:** https://petsc.org/release/manualpages/IS/ISPairToList/

**Contents:**
- ISPairToList#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Convert an IS pair encoding an integer map to a list of IS.

yis - range IS, the maximum value must be less than PETSC_MPI_INT_MAX

listlen - length of islist

islist - list of ISs breaking up indices by color

Each IS in islist contains the preimage for each index on yis. The IS in islist are constructed on the subcommunicators of the input IS pair. Each subcommunicator corresponds to the preimage of some index j – this subcomm contains exactly the MPI processes that assign some indices i to j. This is essentially the inverse of ISListToPair().

xis and yis must be of the same length and have congruent communicators.

The resulting IS have subcommunicators in a “deadlock-free” order (see ISListToPair()).

src/vec/is/is/utils/isdiff.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISPairToList(IS xis, IS yis, PetscInt *listlen, IS **islist)
```

Example 2 (unknown):
```unknown
PETSC_MPI_INT_MAX
```

Example 3 (unknown):
```unknown
ISListToPair()
```

Example 4 (unknown):
```unknown
ISListToPair()
```

---

## ISPartitioningCount#

**URL:** https://petsc.org/release/manualpages/IS/ISPartitioningCount/

**Contents:**
- ISPartitioningCount#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Takes a IS that represents a partitioning (the MPI rank that each local entry belongs to) and determines the number of resulting elements on each (partition) rank

part - a partitioning as generated by MatPartitioningApply() or MatPartitioningApplyND()

len - length of the array count, this is the total number of partitions

count - array of length size, to contain the number of elements assigned to each partition, where size is the number of partitions generated (see notes below).

By default the number of partitions generated (and thus the length of count) is the size of the communicator associated with IS, but it can be set by MatPartitioningSetNParts().

The resulting array of lengths can for instance serve as input of PCBJacobiSetTotalBlocks().

If the partitioning has been obtained by MatPartitioningApplyND(), the returned count does not include the separators.

Low-level Vector Communication, IS, MatPartitioningCreate(), AOCreateBasic(), ISPartitioningToNumbering(), MatPartitioningSetNParts(), MatPartitioningApply(), MatPartitioningApplyND()

src/vec/is/is/utils/iscoloring.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISPartitioningCount(IS part, PetscInt len, PetscInt count[])
```

Example 2 (unknown):
```unknown
MatPartitioningApply()
```

Example 3 (unknown):
```unknown
MatPartitioningApplyND()
```

Example 4 (unknown):
```unknown
MatPartitioningSetNParts()
```

---

## ISPartitioningToNumbering#

**URL:** https://petsc.org/release/manualpages/IS/ISPartitioningToNumbering/

**Contents:**
- ISPartitioningToNumbering#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Takes an IS' that represents a partitioning (the MPI rank that each local entry belongs to) and on each MPI process generates an IS` that contains a new global node number in the new ordering for each entry

part - a partitioning as generated by MatPartitioningApply() or MatPartitioningApplyND()

is - on each processor the index set that defines the global numbers (in the new numbering) for all the nodes currently (before the partitioning) on that processor

The resulting IS tells where each local entry is mapped to in a new global ordering

Low-level Vector Communication, IS, MatPartitioningCreate(), AOCreateBasic(), ISPartitioningCount()

src/vec/is/is/utils/iscoloring.c

src/ksp/ksp/tutorials/ex64.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
IS' that represents a partitioning (the MPI rank that each local entry belongs to) and on each MPI process generates an
```

Example 2 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISPartitioningToNumbering(IS part, IS *is)
```

Example 3 (unknown):
```unknown
MatPartitioningApply()
```

Example 4 (unknown):
```unknown
MatPartitioningApplyND()
```

---

## ISPermutation#

**URL:** https://petsc.org/release/manualpages/IS/ISPermutation/

**Contents:**
- ISPermutation#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#

PETSC_TRUE or PETSC_FALSE depending on whether the index set has been declared to be a permutation.

perm - PETSC_TRUE if a permutation, else PETSC_FALSE

If it is not already known that is is a permutation (if ISSetPermutation() or ISSetInfo() has not been called), this routine will not attempt to compute whether the index set is a permutation and will assume perm is PETSC_FALSE. To compute the value when it is not already known, use ISGetInfo() with the compute flag set to PETSC_TRUE.

Perhaps some of these routines should use the PetscBool3 enum to return appropriate values

IS, ISSetPermutation(), ISGetInfo()

src/vec/is/is/interface/index.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_FALSE
```

Example 2 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISPermutation(IS is, PetscBool *perm)
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (unknown):
```unknown
ISSetPermutation()
```

---

## ISRegisterAll#

**URL:** https://petsc.org/release/manualpages/IS/ISRegisterAll/

**Contents:**
- ISRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the index set components in the IS package.

Low-level Vector Communication, IS, ISType, ISRegister()

src/vec/is/is/interface/isregall.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISRegisterAll(void)
```

Example 2 (unknown):
```unknown
ISRegister()
```

---

## ISRegister#

**URL:** https://petsc.org/release/manualpages/IS/ISRegister/

**Contents:**
- ISRegister#
- Synopsis#
- Input Parameters#
- Example Usage#
- Notes#
- See Also#
- Level#
- Location#

Adds a new index set implementation

Not Collective, No Fortran Support

sname - The name of a new user-defined creation routine

function - The creation routine itself

Then, your vector type can be chosen with the procedural interface via

or at runtime via the option

ISRegister() may be called multiple times to add several user-defined vectors

This is no ISSetFromOptions() and the current implementations do not have a way to dynamically determine type, so dynamic registration of custom IS types will be of limited use to users.

Low-level Vector Communication, IS, ISType, ISSetType(), ISRegisterAll(), ISRegisterDestroy()

src/vec/is/is/interface/isreg.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISRegister(const char sname[], PetscErrorCode (*function)(IS))
```

Example 2 (unknown):
```unknown
ISRegister("my_is_name",  MyISCreate);
```

Example 3 (unknown):
```unknown
ISCreate(MPI_Comm, IS *);
    ISSetType(IS,"my_is_name");
```

Example 4 (unknown):
```unknown
-is_type my_is_name
```

---

## ISRenumber#

**URL:** https://petsc.org/release/manualpages/IS/ISRenumber/

**Contents:**
- ISRenumber#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Renumbers the non-negative entries of an index set in a contiguous way, starting from 0.

subset - the index set

subset_mult - the multiplicity of each entry in subset (optional, can be NULL)

N - one past the largest entry of the new IS

subset_n - the new IS

All negative entries are mapped to -1. Indices with non positive multiplicities are skipped.

src/vec/is/is/interface/index.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISRenumber(IS subset, IS subset_mult, PetscInt *N, IS *subset_n)
```

---

## ISRestoreIndices#

**URL:** https://petsc.org/release/manualpages/IS/ISRestoreIndices/

**Contents:**
- ISRestoreIndices#
- Synopsis#
- Input Parameters#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Restores an index set to a usable state after a call to ISGetIndices().

ptr - the pointer obtained by ISGetIndices()

src/vec/is/is/interface/index.c

src/ksp/ksp/tutorials/ex87.c src/snes/tutorials/ex62.c src/vec/is/is/tutorials/ex1.c src/snes/tutorials/ex13.c src/ksp/ksp/tutorials/ex76f.F90 src/ksp/ksp/tutorials/ex71.c src/snes/tutorials/ex56.c src/vec/vec/utils/tagger/tutorials/ex1.c src/snes/tutorials/ex77.c src/ksp/ksp/tutorials/ex76.c

ISRestoreIndices_Block() in src/vec/is/is/impls/block/block.c ISRestoreIndices_General() in src/vec/is/is/impls/general/general.c ISRestoreIndices_Stride() in src/vec/is/is/impls/stride/stride.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISGetIndices()
```

Example 2 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISRestoreIndices(IS is, const PetscInt *ptr[])
```

Example 3 (unknown):
```unknown
ISGetIndices()
```

Example 4 (julia):
```julia
PetscInt, pointer :: ptr(:)
```

---

## ISRestoreNonlocalIndices#

**URL:** https://petsc.org/release/manualpages/IS/ISRestoreNonlocalIndices/

**Contents:**
- ISRestoreNonlocalIndices#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Restore the index array obtained with ISGetNonlocalIndices().

indices - index array; must be the array obtained with ISGetNonlocalIndices()

IS, ISGetTotalIndices(), ISGetNonlocalIndices(), ISRestoreTotalIndices()

src/vec/is/is/interface/index.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISGetNonlocalIndices()
```

Example 2 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISRestoreNonlocalIndices(IS is, const PetscInt *indices[])
```

Example 3 (unknown):
```unknown
ISGetNonlocalIndices()
```

Example 4 (unknown):
```unknown
ISGetTotalIndices()
```

---

## ISRestoreNonlocalIS#

**URL:** https://petsc.org/release/manualpages/IS/ISRestoreNonlocalIS/

**Contents:**
- ISRestoreNonlocalIS#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Restore the IS obtained with ISGetNonlocalIS().

complement - index set of is’s nonlocal indices

IS, ISGetNonlocalIS(), ISGetNonlocalIndices(), ISRestoreNonlocalIndices()

src/vec/is/is/interface/index.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISGetNonlocalIS()
```

Example 2 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISRestoreNonlocalIS(IS is, IS *complement)
```

Example 3 (unknown):
```unknown
ISGetNonlocalIS()
```

Example 4 (unknown):
```unknown
ISGetNonlocalIndices()
```

---

## ISRestorePointRange#

**URL:** https://petsc.org/release/manualpages/IS/ISRestorePointRange/

**Contents:**
- ISRestorePointRange#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Destroys the traversal description created with ISGetPointRange()

pointIS - The IS object

pStart - The first index, from ISGetPointRange()

pEnd - One past the last index, from ISGetPointRange()

points - The indices, from ISGetPointRange()

Low-level Vector Communication, IS, ISGetPointRange(), ISGetPointSubrange(), ISGetIndices(), ISCreateStride()

src/vec/is/utils/isltog.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISGetPointRange()
```

Example 2 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISRestorePointRange(IS pointIS, PetscInt *pStart, PetscInt *pEnd, const PetscInt *points[])
```

Example 3 (unknown):
```unknown
ISGetPointRange()
```

Example 4 (unknown):
```unknown
ISGetPointRange()
```

---

## ISRestoreTotalIndices#

**URL:** https://petsc.org/release/manualpages/IS/ISRestoreTotalIndices/

**Contents:**
- ISRestoreTotalIndices#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Restore the index array obtained with ISGetTotalIndices().

indices - index array; must be the array obtained with ISGetTotalIndices()

IS, ISGetNonlocalIndices()

src/vec/is/is/interface/index.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISGetTotalIndices()
```

Example 2 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISRestoreTotalIndices(IS is, const PetscInt *indices[])
```

Example 3 (unknown):
```unknown
ISGetTotalIndices()
```

Example 4 (unknown):
```unknown
ISGetNonlocalIndices()
```

---

## ISSetBlockSize#

**URL:** https://petsc.org/release/manualpages/IS/ISSetBlockSize/

**Contents:**
- ISSetBlockSize#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

informs an index set that it has a given block size

This is much like the block size for Vecs. It indicates that one can think of the indices as being in a collection of equal size blocks. For ISBLOCK these collections of blocks are all contiguous within a block but this is not the case for other IS. For example, an IS with entries {0, 2, 3, 4, 6, 7} could have a block size of three set.

ISBlockGetIndices() only works for ISBLOCK, not others.

IS, ISGetBlockSize(), ISCreateBlock(), ISBlockGetIndices()

src/vec/is/is/interface/index.c

src/ksp/ksp/tutorials/ex73.c src/ksp/ksp/tutorials/ex49.c src/ksp/ksp/tutorials/ex76.c src/ksp/ksp/tutorials/ex87.c

ISSetBlockSize_Block() in src/vec/is/is/impls/block/block.c ISSetBlockSize_General() in src/vec/is/is/impls/general/general.c ISSetBlockSize_Stride() in src/vec/is/is/impls/stride/stride.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISSetBlockSize(IS is, PetscInt bs)
```

Example 2 (unknown):
```unknown
ISBlockGetIndices()
```

Example 3 (unknown):
```unknown
ISGetBlockSize()
```

Example 4 (unknown):
```unknown
ISCreateBlock()
```

---

## ISSetCompressOutput#

**URL:** https://petsc.org/release/manualpages/IS/ISSetCompressOutput/

**Contents:**
- ISSetCompressOutput#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

set the flag for output compression

compress - flag for output compression

IS, ISGetCompressOutput(), ISView()

src/vec/is/is/interface/index.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISSetCompressOutput(IS is, PetscBool compress)
```

Example 2 (unknown):
```unknown
ISGetCompressOutput()
```

---

## ISSetIdentity#

**URL:** https://petsc.org/release/manualpages/IS/ISSetIdentity/

**Contents:**
- ISSetIdentity#
- Synopsis#
- Input Parameter#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#

Informs the index set that it is an identity.

is will be considered the identity permanently, even if indices have been changes (for example, with ISGeneralSetIndices()). It’s a good idea to only set this property if is will not change in the future.

To clear this property, use ISClearInfoCache().

Some of these info routines have statements about values changing in the IS, this seems to contradict the fact that IS cannot be changed?

IS, ISIdentity(), ISSetInfo(), ISClearInfoCache()

src/vec/is/is/interface/index.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISSetIdentity(IS is)
```

Example 2 (unknown):
```unknown
ISGeneralSetIndices()
```

Example 3 (unknown):
```unknown
ISClearInfoCache()
```

Example 4 (unknown):
```unknown
ISIdentity()
```

---

## ISSetInfo#

**URL:** https://petsc.org/release/manualpages/IS/ISSetInfo/

**Contents:**
- ISSetInfo#
- Synopsis#
- Input Parameters#
- Values of info Describing IS Structure#
- Notes#
- See Also#
- Level#
- Location#

Set known information about an index set.

Logically Collective if ISInfoType is IS_GLOBAL

info - describing a property of the index set, one of those listed below,

type - IS_LOCAL if the information describes the local portion of the index set, IS_GLOBAL if it describes the whole index set

permanent - PETSC_TRUE if it is known that the property will persist through changes to the index set, PETSC_FALSE otherwise If the user sets a property as permanently known, it will bypass computation of that property

flg - set the described property as true (PETSC_TRUE) or false (PETSC_FALSE)

IS_SORTED - the [local part of the] index set is sorted in ascending order

IS_UNIQUE - each entry in the [local part of the] index set is unique

IS_PERMUTATION - the [local part of the] index set is a permutation of the integers {0, 1, …, N-1}, where N is the size of the [local part of the] index set

IS_INTERVAL - the [local part of the] index set is equal to a contiguous range of integers {f, f + 1, …, f + N-1}

IS_IDENTITY - the [local part of the] index set is equal to the integers {0, 1, …, N-1}

If type is IS_GLOBAL, all processes that share the index set must pass the same value in flg

It is possible to set a property with ISSetInfo() that contradicts what would be previously computed with ISGetInfo()

ISInfo, ISInfoType, IS

src/vec/is/is/interface/index.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISSetInfo(IS is, ISInfo info, ISInfoType type, PetscBool permanent, PetscBool flg)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (unknown):
```unknown
IS_PERMUTATION
```

---

## ISSetLayout#

**URL:** https://petsc.org/release/manualpages/IS/ISSetLayout/

**Contents:**
- ISSetLayout#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

set PetscLayout describing index set layout

Users should typically use higher level functions such as ISCreateGeneral().

This function can be useful in some special cases of constructing a new IS, e.g. after ISCreate() and before ISLoad(). Otherwise, it is only valid to replace the layout with a layout known to be equivalent.

IS, PetscLayout, ISCreate(), ISGetLayout(), ISGetSize(), ISGetLocalSize()

src/vec/is/is/interface/index.c

src/ksp/ksp/tutorials/ex87.c src/ksp/ksp/tutorials/ex76.c src/ksp/ksp/tutorials/ex76f.F90

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLayout
```

Example 2 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISSetLayout(IS is, PetscLayout map)
```

Example 3 (unknown):
```unknown
ISCreateGeneral()
```

Example 4 (unknown):
```unknown
PetscLayout
```

---

## ISSetPermutation#

**URL:** https://petsc.org/release/manualpages/IS/ISSetPermutation/

**Contents:**
- ISSetPermutation#
- Synopsis#
- Input Parameter#
- Notes#
- See Also#
- Level#
- Location#

Informs the index set that it is a permutation.

is will be considered a permutation permanently, even if indices have been changes (for example, with ISGeneralSetIndices()). It’s a good idea to only set this property if is will not change in the future.

To clear this property, use ISClearInfoCache().

The debug version of the libraries (./configure –with-debugging=1) checks if the index set is actually a permutation. The optimized version just believes you.

IS, ISPermutation(), ISSetInfo(), ISClearInfoCache().

src/vec/is/is/interface/index.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISSetPermutation(IS is)
```

Example 2 (unknown):
```unknown
ISGeneralSetIndices()
```

Example 3 (unknown):
```unknown
ISClearInfoCache()
```

Example 4 (unknown):
```unknown
ISPermutation()
```

---

## ISSetType#

**URL:** https://petsc.org/release/manualpages/IS/ISSetType/

**Contents:**
- ISSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Builds a index set, for a particular ISType

is - The index set object

method - The name of the index set type

-is_type type - Sets the index set type; see ISType

See ISType for available types (for instance, ISGENERAL, ISSTRIDE, or ISBLOCK).

Often convenience constructors such as ISCreateGeneral(), ISCreateStride() or ISCreateBlock() can be used to construct the desired IS in one step

Use ISDuplicate() to make a duplicate

Low-level Vector Communication, IS, ISGENERAL, ISBLOCK, ISGetType(), ISCreate(), ISCreateGeneral(), ISCreateStride(), ISCreateBlock()

src/vec/is/is/interface/isreg.c

src/ksp/ksp/tutorials/ex87.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISSetType(IS is, ISType method)
```

Example 2 (unknown):
```unknown
ISCreateGeneral()
```

Example 3 (unknown):
```unknown
ISCreateStride()
```

Example 4 (unknown):
```unknown
ISCreateBlock()
```

---

## ISShift#

**URL:** https://petsc.org/release/manualpages/IS/ISShift/

**Contents:**
- ISShift#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Shift all indices by given offset

isy - the shifted copy of the input index set

The offset can be different across processes.

is and isy can be the same.

ISDuplicate(), ISCopy()

src/vec/is/is/interface/index.c

ISShift_Block() in src/vec/is/is/impls/block/block.c ISShift_General() in src/vec/is/is/impls/general/general.c ISShift_Stride() in src/vec/is/is/impls/stride/stride.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISShift(IS is, PetscInt offset, IS isy)
```

Example 2 (unknown):
```unknown
ISDuplicate()
```

---

## ISSorted#

**URL:** https://petsc.org/release/manualpages/IS/ISSorted/

**Contents:**
- ISSorted#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Checks the indices to determine whether they have been sorted.

flg - output flag, either PETSC_TRUE if the index set is sorted, or PETSC_FALSE otherwise.

For parallel IS objects this only indicates if the local part of is is sorted. So some processors may return PETSC_TRUE while others may return PETSC_FALSE.

ISSort(), ISSortRemoveDups()

src/vec/is/is/interface/index.c

ISSorted_Block() in src/vec/is/is/impls/block/block.c ISSorted_General() in src/vec/is/is/impls/general/general.c ISSorted_Stride() in src/vec/is/is/impls/stride/stride.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISSorted(IS is, PetscBool *flg)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (unknown):
```unknown
ISSortRemoveDups()
```

---

## ISSortPermutation#

**URL:** https://petsc.org/release/manualpages/IS/ISSortPermutation/

**Contents:**
- ISSortPermutation#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

calculate the permutation of the indices into a nondecreasing order.

always - build the permutation even when f’s indices are nondecreasing.

h - permutation or NULL, if f is nondecreasing and always == PETSC_FALSE.

Indices in f are unchanged. f[h[i]] is the i-th smallest f index.

If always == PETSC_FALSE, an extra check is performed to see whether the f indices are nondecreasing. h is built on PETSC_COMM_SELF, since the permutation has a local meaning only.

IS, ISLocalToGlobalMapping, ISSort()

src/vec/is/is/utils/isdiff.c

src/ksp/ksp/tutorials/ex76.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISSortPermutation(IS f, PetscBool always, IS *h)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (unknown):
```unknown
PETSC_COMM_SELF
```

---

## ISSortRemoveDups#

**URL:** https://petsc.org/release/manualpages/IS/ISSortRemoveDups/

**Contents:**
- ISSortRemoveDups#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Sorts the indices of an index set, removing duplicates.

IS, ISSort(), ISSorted()

src/vec/is/is/interface/index.c

ISSortRemoveDups_Block() in src/vec/is/is/impls/block/block.c ISSortRemoveDups_General() in src/vec/is/is/impls/general/general.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISSortRemoveDups(IS is)
```

---

## ISSort#

**URL:** https://petsc.org/release/manualpages/IS/ISSort/

**Contents:**
- ISSort#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sorts the indices of an index set.

IS, ISSortRemoveDups(), ISSorted()

src/vec/is/is/interface/index.c

src/dm/impls/plex/tutorials/ex10.c src/ksp/ksp/tutorials/ex76.c

ISSort_Block() in src/vec/is/is/impls/block/block.c ISSort_General() in src/vec/is/is/impls/general/general.c ISSort_Stride() in src/vec/is/is/impls/stride/stride.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISSort(IS is)
```

Example 2 (unknown):
```unknown
ISSortRemoveDups()
```

---

## ISStrideGetInfo#

**URL:** https://petsc.org/release/manualpages/IS/ISStrideGetInfo/

**Contents:**
- ISStrideGetInfo#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#

Returns the first index in a stride index set and the stride width from an IS of ISType ISSTRIDE

first - the first index

step - the stride width

Low-level Vector Communication, IS, ISCreateStride(), ISGetSize(), ISSTRIDE

src/vec/is/is/impls/stride/stride.c

src/vec/is/is/tutorials/ex2f.F90 src/vec/is/is/tutorials/ex2.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"   
PetscErrorCode ISStrideGetInfo(IS is, PetscInt *first, PetscInt *step)
```

Example 2 (unknown):
```unknown
ISCreateStride()
```

Example 3 (unknown):
```unknown
ISGetSize()
```

---

## ISStrideSetStride#

**URL:** https://petsc.org/release/manualpages/IS/ISStrideSetStride/

**Contents:**
- ISStrideSetStride#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Sets the stride information for a stride index set.

n - the length of the locally owned portion of the index set

first - the first element of the locally owned portion of the index set

step - the change to the next index

ISCreateStride() can be used to create an ISSTRIDE and set its stride in one function call

Low-level Vector Communication, IS, ISCreateGeneral(), ISCreateBlock(), ISAllGather(), ISSTRIDE, ISCreateStride(), ISStrideGetInfo()

src/vec/is/is/impls/stride/stride.c

ISStrideSetStride_Stride() in src/vec/is/is/impls/stride/stride.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"   
PetscErrorCode ISStrideSetStride(IS is, PetscInt n, PetscInt first, PetscInt step)
```

Example 2 (unknown):
```unknown
ISCreateStride()
```

Example 3 (unknown):
```unknown
ISCreateGeneral()
```

Example 4 (unknown):
```unknown
ISCreateBlock()
```

---

## ISSum#

**URL:** https://petsc.org/release/manualpages/IS/ISSum/

**Contents:**
- ISSum#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Computes the sum (union) of two index sets.

Only sequential version (at the moment)

is1 - index set to be extended

is2 - index values to be added

is3 - the sum; this can not be is1 or is2

If n1 and n2 are the sizes of the sets, this takes O(n1+n2) time;

Both index sets need to be sorted on input.

The sum is computed separately on each MPI rank

Low-level Vector Communication, IS, ISDestroy(), ISView(), ISDifference(), ISExpand()

src/vec/is/is/utils/isdiff.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h"  
PetscErrorCode ISSum(IS is1, IS is2, IS *is3)
```

Example 2 (unknown):
```unknown
ISDestroy()
```

Example 3 (unknown):
```unknown
ISDifference()
```

---

## ISToGeneral#

**URL:** https://petsc.org/release/manualpages/IS/ISToGeneral/

**Contents:**
- ISToGeneral#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Converts an IS object of any type to ISGENERAL type

src/vec/is/is/interface/index.c

ISToGeneral_Block() in src/vec/is/is/impls/block/block.c ISToGeneral_General() in src/vec/is/is/impls/general/general.c ISToGeneral_Stride() in src/vec/is/is/impls/stride/stride.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISToGeneral(IS is)
```

---

## ISType#

**URL:** https://petsc.org/release/manualpages/IS/ISType/

**Contents:**
- ISType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

String with the name of a PETSc index set type

ISGENERAL - the values are stored with an array of indices and generally have no structure

ISSTRIDE - the values have a simple structure of an initial offset and then a step size between values

ISBLOCK - values are an array of indices, each representing a block (of the same common length) of values

ISSetType(), IS, ISCreateGeneral(), ISCreateStride(), ISCreateBlock(), ISCreate(), ISRegister(), VecScatterCreate(), MatGetSubMatrices()

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
typedef const char *ISType;
#define ISGENERAL "general"
#define ISSTRIDE  "stride"
#define ISBLOCK   "block"
```

Example 2 (unknown):
```unknown
ISSetType()
```

Example 3 (unknown):
```unknown
ISCreateGeneral()
```

Example 4 (unknown):
```unknown
ISCreateStride()
```

---

## ISViewFromOptions#

**URL:** https://petsc.org/release/manualpages/IS/ISViewFromOptions/

**Contents:**
- ISViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

View an IS based on options in the options database

obj - Optional object that provides the prefix for the options database

name - command line option

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

IS, ISView(), PetscObjectViewFromOptions(), ISCreate()

src/vec/is/is/interface/index.c

src/snes/tutorials/ex27.c src/vec/vec/utils/tagger/tutorials/ex1.c src/snes/tutorials/ex13.c src/ts/tutorials/ex30.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISViewFromOptions(IS A, PetscObject obj, const char name[])
```

Example 2 (unknown):
```unknown
PetscObjectViewFromOptions()
```

Example 3 (unknown):
```unknown
PetscObjectViewFromOptions()
```

---

## ISView#

**URL:** https://petsc.org/release/manualpages/IS/ISView/

**Contents:**
- ISView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Displays an index set.

viewer - viewer used to display the set, for example PETSC_VIEWER_STDOUT_SELF.

IS, PetscViewer, PetscViewerASCIIOpen(), ISViewFromOptions()

src/vec/is/is/interface/index.c

src/mat/tutorials/ex11.c src/mat/tutorials/ex1.c src/mat/tutorials/ex11f.F90 src/mat/tutorials/ex17f.F90 src/mat/tutorials/ex15.c src/ksp/ksp/tutorials/ex8.c src/ksp/ksp/tutorials/ex62.c src/mat/tutorials/ex15f.F90 src/ksp/ksp/tutorials/ex84.c src/mat/tutorials/ex17.c

ISView_Block() in src/vec/is/is/impls/block/block.c ISView_General() in src/vec/is/is/impls/general/general.c ISView_Stride() in src/vec/is/is/impls/stride/stride.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode ISView(IS is, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PETSC_VIEWER_STDOUT_SELF
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewerASCIIOpen()
```

---

## IS#

**URL:** https://petsc.org/release/manualpages/IS/IS/

**Contents:**
- IS#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Abstract PETSc object used for efficient indexing into vector and matrices

ISType, ISCreateGeneral(), ISCreateBlock(), ISCreateStride(), ISGetIndices(), ISDestroy()

include/petscistypes.h

src/snes/tutorials/ex28.c src/mat/tutorials/ex3.c src/mat/tutorials/ex11.c src/mat/tutorials/ex1.c src/mat/tutorials/ex11f.F90 src/mat/tutorials/ex17f.F90 src/snes/tutorials/ex70.c src/mat/tutorials/ex15.c src/mat/tutorials/ex15f.F90 src/mat/tutorials/ex17.c

_p_IS in include/petsc/private/isimpl.h IS_Block in src/vec/is/is/impls/block/block.c IS_General in src/vec/is/is/impls/general/general.h IS_Stride in src/vec/is/is/impls/stride/stride.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_IS *IS;
```

Example 2 (unknown):
```unknown
ISCreateGeneral()
```

Example 3 (unknown):
```unknown
ISCreateBlock()
```

Example 4 (unknown):
```unknown
ISCreateStride()
```

---

## NormType#

**URL:** https://petsc.org/release/manualpages/Vec/NormType/

**Contents:**
- NormType#
- Synopsis#
- Values#
- Note#
- See Also#
- Level#
- Location#
- Examples#

determines what type of norm to compute with VecNorm(), VecNormBegin()/VecNormEnd() and MatNorm().

NORM_1 - the one norm, \(||v|| = \sum_i | v_i |\). \(||A|| = \max_j || A_{*j} ||\), maximum column sum

NORM_2 - the two norm, \(||v|| = sqrt(\sum_i |v_i|^2)\) (vectors only)

NORM_FROBENIUS - \(||A|| = sqrt(\sum_{ij} |A_{ij}|^2)\), same as NORM_2 for vectors

NORM_INFINITY - \(||v|| = \max_i |v_i|\). \(||A|| = \max_i || A_{i*} ||_1\), maximum row sum

NORM_1_AND_2 - computes both the 1 and 2 norm of a vector. The values are stored in two adjacent PetscReal memory locations

The v above represents a Vec while the A represents a Mat

Vectors and Parallel Data, Vec, Mat, VecNorm(), VecNormBegin(), VecNormEnd(), MatNorm(), NORM_1, NORM_2, NORM_FROBENIUS, NORM_INFINITY, NORM_1_AND_2, ReductionType

src/tao/tutorials/ex4.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecNormBegin()
```

Example 2 (unknown):
```unknown
VecNormEnd()
```

Example 3 (unknown):
```unknown
typedef enum {
  NORM_1         = 0,
  NORM_2         = 1,
  NORM_FROBENIUS = 2,
  NORM_INFINITY  = 3,
  NORM_1_AND_2   = 4
} NormType;
```

Example 4 (unknown):
```unknown
NORM_FROBENIUS
```

---

## NORM_1#

**URL:** https://petsc.org/release/manualpages/Vec/NORM_1/

**Contents:**
- NORM_1#
- See Also#
- Level#
- Location#
- Examples#

the one norm, \(||v|| = \sum_i | v_i |\). \(||A|| = \max_j || A_{*,j} ||\), maximum column sum

Vectors and Parallel Data, NormType, MatNorm(), VecNorm(), VecNormBegin(), VecNormEnd(), NORM_2, NORM_FROBENIUS, NORM_INFINITY, NORM_1_AND_2

src/mat/tutorials/ex3.c src/tao/tutorials/ex4.c src/snes/tutorials/ex9.c src/tao/constrained/tutorials/tomographyADMM.c src/ksp/ksp/tutorials/ex34.c src/vec/vec/tutorials/performance.c src/vec/vec/tutorials/ex11f90.F90 src/ksp/ksp/tutorials/ex43.c src/vec/vec/tutorials/ex11.c src/vec/vec/tutorials/ex11f.F90

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecNormBegin()
```

Example 2 (unknown):
```unknown
VecNormEnd()
```

Example 3 (unknown):
```unknown
NORM_FROBENIUS
```

Example 4 (unknown):
```unknown
NORM_INFINITY
```

---

## NORM_1_AND_2#

**URL:** https://petsc.org/release/manualpages/Vec/NORM_1_AND_2/

**Contents:**
- NORM_1_AND_2#
- See Also#
- Level#
- Location#

computes both the 1 and 2 norm of a vector. The values are stored in two adjacent PetscReal memory locations

Vectors and Parallel Data, NormType, MatNorm(), VecNorm(), VecNormBegin(), VecNormEnd(), NORM_1, NORM_2, NORM_FROBENIUS, NORM_INFINITY

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecNormBegin()
```

Example 2 (unknown):
```unknown
VecNormEnd()
```

Example 3 (unknown):
```unknown
NORM_FROBENIUS
```

Example 4 (unknown):
```unknown
NORM_INFINITY
```

---

## NORM_2#

**URL:** https://petsc.org/release/manualpages/Vec/NORM_2/

**Contents:**
- NORM_2#
- See Also#
- Level#
- Location#
- Examples#

the two norm, \(||v|| = \sqrt{\sum_i |v_i|^2}\) (vectors only)

Vectors and Parallel Data, NormType, MatNorm(), VecNorm(), VecNormBegin(), VecNormEnd(), NORM_1, NORM_FROBENIUS, NORM_INFINITY, NORM_1_AND_2

src/mat/tutorials/ex3.c src/snes/tutorials/ex73f90t.F90 src/mat/tutorials/ex9.c src/snes/tutorials/ex14.c src/snes/tutorials/ex12.c src/mat/tutorials/ex10.c src/snes/tutorials/ex70.c src/mat/tutorials/ex2.c src/snes/tutorials/ex15.c src/snes/tutorials/ex22.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecNormBegin()
```

Example 2 (unknown):
```unknown
VecNormEnd()
```

Example 3 (unknown):
```unknown
NORM_FROBENIUS
```

Example 4 (unknown):
```unknown
NORM_INFINITY
```

---

## NORM_FROBENIUS#

**URL:** https://petsc.org/release/manualpages/Vec/NORM_FROBENIUS/

**Contents:**
- NORM_FROBENIUS#
- See Also#
- Level#
- Location#
- Examples#

\(||A|| = \sqrt{\sum_{i,j} |A_{i,j}|^2}\), same as NORM_2 for vectors

Vectors and Parallel Data, NormType, MatNorm(), VecNorm(), VecNormBegin(), VecNormEnd(), NORM_1, NORM_2, NORM_INFINITY, NORM_1_AND_2

src/ts/tutorials/ex14.c src/ksp/ksp/tutorials/ex29.c src/ksp/ksp/tutorials/ex21.c src/ksp/ksp/tutorials/ex34.c src/snes/tutorials/ex48.c src/ml/da/tutorials/ex2.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecNormBegin()
```

Example 2 (unknown):
```unknown
VecNormEnd()
```

Example 3 (unknown):
```unknown
NORM_INFINITY
```

Example 4 (unknown):
```unknown
NORM_1_AND_2
```

---

## NORM_INFINITY#

**URL:** https://petsc.org/release/manualpages/Vec/NORM_INFINITY/

**Contents:**
- NORM_INFINITY#
- See Also#
- Level#
- Location#
- Examples#

\(||v|| = \max_i |v_i|\). \(||A|| = \max_i || A_{i,*} ||_1\), maximum row sum

Vectors and Parallel Data, NormType, MatNorm(), VecNorm(), VecNormBegin(), VecNormEnd(), NORM_1, NORM_2, NORM_FROBENIUS, NORM_1_AND_2

src/snes/tutorials/ex55.c src/snes/tutorials/ex5f.F90 src/snes/tutorials/ex9.c src/snes/tutorials/ex5.c src/snes/tutorials/ex13.c src/snes/tutorials/ex56.c src/ksp/ksp/tutorials/ex77f.F90 src/ksp/ksp/tutorials/ex8.c src/ksp/ksp/tutorials/ex43.c src/snes/tutorials/ex7.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecNormBegin()
```

Example 2 (unknown):
```unknown
VecNormEnd()
```

Example 3 (unknown):
```unknown
NORM_FROBENIUS
```

Example 4 (unknown):
```unknown
NORM_1_AND_2
```

---

## NORM_MAX#

**URL:** https://petsc.org/release/manualpages/Vec/NORM_MAX/

**Contents:**
- NORM_MAX#
- Level#
- Location#
- Examples#

src/ts/tutorials/ex5.c src/ts/tutorials/ex4.c src/ksp/ksp/tutorials/ex25.c src/ts/tutorials/ex21.c src/ts/tutorials/ex3.c src/ts/tutorials/ex6.c src/ts/tutorials/ex2.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
NORM_INFINITY
```

---

## PetscCommSplitReductionBegin#

**URL:** https://petsc.org/release/manualpages/Vec/PetscCommSplitReductionBegin/

**Contents:**
- PetscCommSplitReductionBegin#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#

Begin an asynchronous split-mode reduction

Collective but not synchronizing

comm - communicator on which split reduction has been queued

Calling this function is optional when using split-mode reduction. On supporting hardware, calling this after all VecXxxBegin() allows the reduction to make asynchronous progress before the result is needed (in VecXxxEnd()).

VecNormBegin(), VecNormEnd(), VecDotBegin(), VecDotEnd(), VecTDotBegin(), VecTDotEnd(), VecMDotBegin(), VecMDotEnd(), VecMTDotBegin(), VecMTDotEnd()

src/vec/vec/utils/comb.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"    
PetscErrorCode PetscCommSplitReductionBegin(MPI_Comm comm)
```

Example 2 (unknown):
```unknown
VecNormBegin()
```

Example 3 (unknown):
```unknown
VecNormEnd()
```

Example 4 (unknown):
```unknown
VecDotBegin()
```

---

## PetscKDTreeCreate#

**URL:** https://petsc.org/release/manualpages/IS/PetscKDTreeCreate/

**Contents:**
- PetscKDTreeCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

Not Collective, No Fortran Support

num_coords - number of coordinate points to build the PetscKDTree

dim - the dimension of the coordinates

coords - array of the coordinates, in point-major order

copy_mode - behavior handling coords, PETSC_COPY_VALUES generally more performant

max_bucket_size - maximum number of points stored at each leaf

new_tree - the resulting PetscKDTree

When copy_mode == PETSC_COPY_VALUES, the coordinates are copied and organized to optimize vectorization and cache-coherency. It is recommended to run this way if the extra memory use is not a concern and it has very little impact on the PetscKDTree creation time.

Building algorithm detailed in ‘Building a Balanced k-d Tree in O(kn log n) Time’ Brown, 2015

PetscKDTree, PetscKDTreeDestroy(), PetscKDTreeQueryPointsNearestNeighbor()

src/vec/is/utils/kdtree.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscKDTree
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscKDTreeCreate(PetscCount num_coords, PetscInt dim, const PetscReal coords[], PetscCopyMode copy_mode, PetscInt max_bucket_size, PetscKDTree *new_tree)
```

Example 3 (unknown):
```unknown
PetscKDTree
```

Example 4 (unknown):
```unknown
PETSC_COPY_VALUES
```

---

## PetscKDTreeDestroy#

**URL:** https://petsc.org/release/manualpages/IS/PetscKDTreeDestroy/

**Contents:**
- PetscKDTreeDestroy#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

destroy a PetscKDTree

Not Collective, No Fortran Support

tree - tree to destroy

PetscKDTree, PetscKDTreeCreate()

src/vec/is/utils/kdtree.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscKDTree
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscKDTreeDestroy(PetscKDTree *tree)
```

Example 3 (unknown):
```unknown
PetscKDTree
```

Example 4 (unknown):
```unknown
PetscKDTreeCreate()
```

---

## PetscKDTreeQueryPointsNearestNeighbor#

**URL:** https://petsc.org/release/manualpages/IS/PetscKDTreeQueryPointsNearestNeighbor/

**Contents:**
- PetscKDTreeQueryPointsNearestNeighbor#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

find the nearest neighbor in a PetscKDTree

Not Collective, No Fortran Support

num_points - number of points to query

points - array of the coordinates, in point-major order

tolerance - tolerance for nearest neighbor

indices - indices of the nearest neighbor to the query point

distances - distance between the queried point and the nearest neighbor

When traversing the tree, if a point has been found to be closer than the tolerance, the function short circuits and doesn’t check for any closer points.

The indices and distances arrays should be at least of size num_points.

PetscKDTree, PetscKDTreeCreate()

src/vec/is/utils/kdtree.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscKDTree
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscKDTreeQueryPointsNearestNeighbor(PetscKDTree tree, PetscCount num_points, const PetscReal points[], PetscReal tolerance, PetscCount indices[], PetscReal distances[])
```

Example 3 (unknown):
```unknown
PetscKDTree
```

Example 4 (unknown):
```unknown
PetscKDTreeCreate()
```

---

## PetscKDTreeView#

**URL:** https://petsc.org/release/manualpages/IS/PetscKDTreeView/

**Contents:**
- PetscKDTreeView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Not Collective, No Fortran Support

viewer - visualization context

PetscKDTree, PetscKDTreeCreate(), PetscViewer

src/vec/is/utils/kdtree.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscKDTree
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscKDTreeView(PetscKDTree tree, PetscViewer viewer)
```

Example 3 (unknown):
```unknown
PetscKDTree
```

Example 4 (unknown):
```unknown
PetscKDTreeCreate()
```

---

## PetscKDTree#

**URL:** https://petsc.org/release/manualpages/IS/PetscKDTree/

**Contents:**
- PetscKDTree#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#

Implementation of KDTree for efficiently querying spatial points

See https://en.wikipedia.org/wiki/K-d_tree for a description of K-d trees

PetscKDTreeCreate(), PetscKDTreeDestroy(), PetscKDTreeView(), PetscKDTreeQueryPointsNearestNeighbor()

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
#include "petscis.h" 
typedef struct _n_PetscKDTree *PetscKDTree;
```

Example 2 (unknown):
```unknown
PetscKDTreeCreate()
```

Example 3 (unknown):
```unknown
PetscKDTreeDestroy()
```

Example 4 (unknown):
```unknown
PetscKDTreeView()
```

---

## PetscLayoutCompare#

**URL:** https://petsc.org/release/manualpages/IS/PetscLayoutCompare/

**Contents:**
- PetscLayoutCompare#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

mapa - pointer to the first map

mapb - pointer to the second map

congruent - PETSC_TRUE if the two layouts are congruent, PETSC_FALSE otherwise

PetscLayout, PetscLayoutCreate(), PetscLayoutSetLocalSize(), PetscLayoutGetLocalSize(), PetscLayoutGetBlockSize(), PetscLayoutGetRange(), PetscLayoutGetRanges(), PetscLayoutSetSize(), PetscLayoutGetSize(), PetscLayoutSetUp()

src/vec/is/utils/pmap.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode PetscLayoutCompare(PetscLayout mapa, PetscLayout mapb, PetscBool *congruent)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
PetscLayoutCreate()
```

Example 4 (unknown):
```unknown
PetscLayoutSetLocalSize()
```

---

## PetscLayoutCreateFromRanges#

**URL:** https://petsc.org/release/manualpages/IS/PetscLayoutCreateFromRanges/

**Contents:**
- PetscLayoutCreateFromRanges#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Creates a new PetscLayout with the given ownership ranges and sets it up.

comm - the MPI communicator

range - the array of ownership ranges for each rank with length commsize+1

mode - the copy mode for range

bs - the block size (or PETSC_DECIDE)

newmap - the new PetscLayout

PetscLayout, PetscLayoutCreate(), PetscLayoutSetLocalSize(), PetscLayoutSetSize(), PetscLayoutGetSize(), PetscLayoutGetLocalSize(), PetscLayout, PetscLayoutDestroy(), PetscLayoutGetRange(), PetscLayoutGetRanges(), PetscLayoutSetBlockSize(), PetscLayoutGetBlockSize(), PetscLayoutSetUp(), PetscLayoutCreateFromSizes()

src/vec/is/utils/pmap.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLayout
```

Example 2 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode PetscLayoutCreateFromRanges(MPI_Comm comm, const PetscInt range[], PetscCopyMode mode, PetscInt bs, PetscLayout *newmap)
```

Example 3 (unknown):
```unknown
PETSC_DECIDE
```

Example 4 (unknown):
```unknown
PetscLayout
```

---

## PetscLayoutCreateFromSizes#

**URL:** https://petsc.org/release/manualpages/IS/PetscLayoutCreateFromSizes/

**Contents:**
- PetscLayoutCreateFromSizes#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Allocates PetscLayout object and sets the layout sizes, and sets the layout up.

comm - the MPI communicator

n - the local size (or PETSC_DECIDE)

N - the global size (or PETSC_DECIDE)

bs - the block size (or PETSC_DECIDE)

map - the new PetscLayout

PetscLayout, PetscLayoutCreate(), PetscLayoutSetLocalSize(), PetscLayoutSetSize(), PetscLayoutGetSize(), PetscLayoutGetLocalSize(), PetscLayout, PetscLayoutDestroy(), PetscLayoutGetRange(), PetscLayoutGetRanges(), PetscLayoutSetBlockSize(), PetscLayoutGetBlockSize(), PetscLayoutSetUp(), PetscLayoutCreateFromRanges()

src/vec/is/utils/pmap.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLayout
```

Example 2 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode PetscLayoutCreateFromSizes(MPI_Comm comm, PetscInt n, PetscInt N, PetscInt bs, PetscLayout *map)
```

Example 3 (unknown):
```unknown
PETSC_DECIDE
```

Example 4 (unknown):
```unknown
PETSC_DECIDE
```

---

## PetscLayoutCreate#

**URL:** https://petsc.org/release/manualpages/IS/PetscLayoutCreate/

**Contents:**
- PetscLayoutCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Allocates PetscLayout object

comm - the MPI communicator

map - the new PetscLayout

Typical calling sequence

Optionally use any of the following

The PetscLayout object and methods are intended to be used in the PETSc Vec and Mat implementations; it is often not needed in user codes unless you really gain something in their use.

PetscLayout, PetscLayoutSetLocalSize(), PetscLayoutSetSize(), PetscLayoutGetSize(), PetscLayoutGetLocalSize(), PetscLayout, PetscLayoutDestroy(), PetscLayoutGetRange(), PetscLayoutGetRanges(), PetscLayoutSetBlockSize(), PetscLayoutGetBlockSize(), PetscLayoutSetUp(), PetscLayoutCreateFromSizes()

src/vec/is/utils/pmap.c

src/ts/tutorials/ex30.c src/ksp/ksp/tutorials/ex85.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLayout
```

Example 2 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode PetscLayoutCreate(MPI_Comm comm, PetscLayout *map)
```

Example 3 (unknown):
```unknown
PetscLayout
```

Example 4 (unknown):
```unknown
PetscLayoutCreate(MPI_Comm,PetscLayout *);
       PetscLayoutSetBlockSize(PetscLayout,bs);
       PetscLayoutSetSize(PetscLayout,N); // or PetscLayoutSetLocalSize(PetscLayout,n);
       PetscLayoutSetUp(PetscLayout);
```

---

## PetscLayoutDestroy#

**URL:** https://petsc.org/release/manualpages/IS/PetscLayoutDestroy/

**Contents:**
- PetscLayoutDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#

Frees a PetscLayout object and frees its range if that exists.

map - the PetscLayout

PetscLayout, PetscLayoutSetLocalSize(), PetscLayoutSetSize(), PetscLayoutGetSize(), PetscLayoutGetLocalSize(), PetscLayout, PetscLayoutCreate(), PetscLayoutGetRange(), PetscLayoutGetRanges(), PetscLayoutSetBlockSize(), PetscLayoutGetBlockSize(), PetscLayoutSetUp()

src/vec/is/utils/pmap.c

src/ts/tutorials/ex30.c src/ksp/ksp/tutorials/ex85.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLayout
```

Example 2 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode PetscLayoutDestroy(PetscLayout *map)
```

Example 3 (unknown):
```unknown
PetscLayout
```

Example 4 (unknown):
```unknown
PetscLayoutSetLocalSize()
```

---

## PetscLayoutDuplicate#

**URL:** https://petsc.org/release/manualpages/IS/PetscLayoutDuplicate/

**Contents:**
- PetscLayoutDuplicate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

creates a new PetscLayout with the same information as a given one. If the PetscLayout already exists it is destroyed first.

in - input PetscLayout to be duplicated

PetscLayoutSetUp() does not need to be called on the resulting PetscLayout

PetscLayout, PetscLayoutCreate(), PetscLayoutDestroy(), PetscLayoutSetUp(), PetscLayoutReference()

src/vec/is/utils/pmap.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLayout
```

Example 2 (unknown):
```unknown
PetscLayout
```

Example 3 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode PetscLayoutDuplicate(PetscLayout in, PetscLayout *out)
```

Example 4 (unknown):
```unknown
PetscLayout
```

---

## PetscLayoutFindOwnerIndex#

**URL:** https://petsc.org/release/manualpages/IS/PetscLayoutFindOwnerIndex/

**Contents:**
- PetscLayoutFindOwnerIndex#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Find the owning MPI process and the local index on that process for a global index

Not Collective; No Fortran Support

idx - global index to find the owner of

owner - the owning rank

lidx - local index used by the owner for idx

PetscLayout, PetscLayoutFindOwner()

src/vec/is/utils/pmap.c

PetscLayoutFindOwnerIndex_Internal() in src/dm/impls/plex/cgns/plexcgns2.c PetscLayoutFindOwnerIndex_CGNSSectionLayouts() in src/dm/impls/plex/cgns/plexcgns2.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode PetscLayoutFindOwnerIndex(PetscLayout map, PetscInt idx, PetscMPIInt *owner, PetscInt *lidx)
```

Example 2 (unknown):
```unknown
PetscLayout
```

Example 3 (unknown):
```unknown
PetscLayoutFindOwner()
```

---

## PetscLayoutFindOwner#

**URL:** https://petsc.org/release/manualpages/IS/PetscLayoutFindOwner/

**Contents:**
- PetscLayoutFindOwner#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Find the owning MPI process for a global index

Not Collective; No Fortran Support

idx - global index to find the owner of

owner - the owning rank

PetscLayout, PetscLayoutFindOwnerIndex()

src/vec/is/utils/pmap.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode PetscLayoutFindOwner(PetscLayout map, PetscInt idx, PetscMPIInt *owner)
```

Example 2 (unknown):
```unknown
PetscLayout
```

Example 3 (unknown):
```unknown
PetscLayoutFindOwnerIndex()
```

---

## PetscLayoutGetBlockSize#

**URL:** https://petsc.org/release/manualpages/IS/PetscLayoutGetBlockSize/

**Contents:**
- PetscLayoutGetBlockSize#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Gets the block size for a PetscLayout object.

map - pointer to the map

Call this after the call to PetscLayoutSetUp()

PetscLayout, PetscLayoutCreate(), PetscLayoutSetLocalSize(), PetscLayoutGetLocalSize(), PetscLayoutSetSize(), PetscLayoutSetUp(), PetscLayoutGetRange(), PetscLayoutGetRanges(), PetscLayoutSetBlockSize(), PetscLayoutGetSize()

src/vec/is/utils/pmap.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLayout
```

Example 2 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode PetscLayoutGetBlockSize(PetscLayout map, PetscInt *bs)
```

Example 3 (unknown):
```unknown
PetscLayoutSetUp()
```

Example 4 (unknown):
```unknown
PetscLayoutCreate()
```

---

## PetscLayoutGetLocalSize#

**URL:** https://petsc.org/release/manualpages/IS/PetscLayoutGetLocalSize/

**Contents:**
- PetscLayoutGetLocalSize#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the local size for a PetscLayout object.

map - pointer to the map

Call this after the call to PetscLayoutSetUp()

PetscLayout, PetscLayoutCreate(), PetscLayoutSetSize(), PetscLayoutGetSize(), PetscLayoutSetUp(), PetscLayoutGetRange(), PetscLayoutGetRanges(), PetscLayoutSetBlockSize(), PetscLayoutGetBlockSize()

src/vec/is/utils/pmap.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLayout
```

Example 2 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode PetscLayoutGetLocalSize(PetscLayout map, PetscInt *n)
```

Example 3 (unknown):
```unknown
PetscLayoutSetUp()
```

Example 4 (unknown):
```unknown
PetscLayoutCreate()
```

---

## PetscLayoutGetRanges#

**URL:** https://petsc.org/release/manualpages/IS/PetscLayoutGetRanges/

**Contents:**
- PetscLayoutGetRanges#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- Fortran Notes#
- See Also#
- Level#
- Location#

gets the ranges of values owned by all processes

map - pointer to the map

range - start of each processors range of indices (the final entry is one more than the last index on the last process). The length of the array is one more than the number of processes in the MPI communicator owned by map

Call this after the call to PetscLayoutSetUp()

Call PetscLayoutRestoreRanges() when no longer needed.

PetscLayout, PetscLayoutCreate(), PetscLayoutSetLocalSize(), PetscLayoutGetLocalSize(), PetscLayoutSetSize(), PetscLayoutGetSize(), PetscLayoutGetRange(), PetscLayoutSetBlockSize(), PetscLayoutSetUp()

src/vec/is/utils/pmap.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode PetscLayoutGetRanges(PetscLayout map, const PetscInt *range[])
```

Example 2 (unknown):
```unknown
PetscLayoutSetUp()
```

Example 3 (julia):
```julia
PetscInt, pointer :: range(:)
```

Example 4 (unknown):
```unknown
PetscLayoutRestoreRanges()
```

---

## PetscLayoutGetRange#

**URL:** https://petsc.org/release/manualpages/IS/PetscLayoutGetRange/

**Contents:**
- PetscLayoutGetRange#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

gets the range of values owned by this process

map - pointer to the map

rstart - first index owned by this process

rend - one more than the last index owned by this process

Call this after the call to PetscLayoutSetUp()

PetscLayout, PetscLayoutCreate(), PetscLayoutSetLocalSize(), PetscLayoutGetLocalSize(), PetscLayoutSetSize(), PetscLayoutGetSize(), PetscLayoutGetRanges(), PetscLayoutSetBlockSize(), PetscLayoutSetUp()

src/vec/is/utils/pmap.c

src/ksp/ksp/tutorials/ex85.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode PetscLayoutGetRange(PetscLayout map, PetscInt *rstart, PetscInt *rend)
```

Example 2 (unknown):
```unknown
PetscLayoutSetUp()
```

Example 3 (unknown):
```unknown
PetscLayoutCreate()
```

Example 4 (unknown):
```unknown
PetscLayoutSetLocalSize()
```

---

## PetscLayoutGetSize#

**URL:** https://petsc.org/release/manualpages/IS/PetscLayoutGetSize/

**Contents:**
- PetscLayoutGetSize#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the global size for a PetscLayout object.

map - pointer to the map

Call this after the call to PetscLayoutSetUp()

PetscLayout, PetscLayoutCreate(), PetscLayoutSetLocalSize(), PetscLayoutGetLocalSize(), PetscLayoutSetSize(), PetscLayoutSetUp(), PetscLayoutGetRange(), PetscLayoutGetRanges(), PetscLayoutSetBlockSize(), PetscLayoutGetBlockSize()

src/vec/is/utils/pmap.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLayout
```

Example 2 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode PetscLayoutGetSize(PetscLayout map, PetscInt *n)
```

Example 3 (unknown):
```unknown
PetscLayoutSetUp()
```

Example 4 (unknown):
```unknown
PetscLayoutCreate()
```

---

## PetscLayoutReference#

**URL:** https://petsc.org/release/manualpages/IS/PetscLayoutReference/

**Contents:**
- PetscLayoutReference#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Causes a PETSc Vec or Mat to share a PetscLayout with one that already exists.

in - input PetscLayout to be copied

out - the reference location

PetscLayoutSetUp() does not need to be called on the resulting PetscLayout

If the out location already contains a PetscLayout it is destroyed

PetscLayout, PetscLayoutCreate(), PetscLayoutDestroy(), PetscLayoutSetUp(), PetscLayoutDuplicate()

src/vec/is/utils/pmap.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLayout
```

Example 2 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode PetscLayoutReference(PetscLayout in, PetscLayout *out)
```

Example 3 (unknown):
```unknown
PetscLayout
```

Example 4 (unknown):
```unknown
PetscLayoutSetUp()
```

---

## PetscLayoutSetBlockSize#

**URL:** https://petsc.org/release/manualpages/IS/PetscLayoutSetBlockSize/

**Contents:**
- PetscLayoutSetBlockSize#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the block size for a PetscLayout object.

map - pointer to the map

PetscLayout, PetscLayoutCreate(), PetscLayoutSetLocalSize(), PetscLayoutGetLocalSize(), PetscLayoutGetBlockSize(), PetscLayoutGetRange(), PetscLayoutGetRanges(), PetscLayoutSetSize(), PetscLayoutGetSize(), PetscLayoutSetUp()

src/vec/is/utils/pmap.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLayout
```

Example 2 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode PetscLayoutSetBlockSize(PetscLayout map, PetscInt bs)
```

Example 3 (unknown):
```unknown
PetscLayoutCreate()
```

Example 4 (unknown):
```unknown
PetscLayoutSetLocalSize()
```

---

## PetscLayoutSetISLocalToGlobalMapping#

**URL:** https://petsc.org/release/manualpages/IS/PetscLayoutSetISLocalToGlobalMapping/

**Contents:**
- PetscLayoutSetISLocalToGlobalMapping#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

sets a ISLocalGlobalMapping into a PetscLayout

in - input PetscLayout

ltog - the local to global mapping

PetscLayoutSetUp() does not need to be called on the resulting PetscLayout

If the PetscLayout already contains a ISLocalGlobalMapping it is destroyed

PetscLayout, PetscLayoutCreate(), PetscLayoutDestroy(), PetscLayoutSetUp(), PetscLayoutDuplicate()

src/vec/is/utils/pmap.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISLocalGlobalMapping
```

Example 2 (unknown):
```unknown
PetscLayout
```

Example 3 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode PetscLayoutSetISLocalToGlobalMapping(PetscLayout in, ISLocalToGlobalMapping ltog)
```

Example 4 (unknown):
```unknown
PetscLayout
```

---

## PetscLayoutSetLocalSize#

**URL:** https://petsc.org/release/manualpages/IS/PetscLayoutSetLocalSize/

**Contents:**
- PetscLayoutSetLocalSize#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the local size for a PetscLayout object.

map - pointer to the map

n - the local size, pass PETSC_DECIDE (the default) to have this value determined by the global size set with PetscLayoutSetSize()

PetscLayout, PetscLayoutCreate(), PetscLayoutSetSize(), PetscLayoutGetSize(), PetscLayoutGetLocalSize(), PetscLayoutSetUp(), PetscLayoutGetRange(), PetscLayoutGetRanges(), PetscLayoutSetBlockSize(), PetscLayoutGetBlockSize()

src/vec/is/utils/pmap.c

src/ts/tutorials/ex30.c src/ksp/ksp/tutorials/ex85.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLayout
```

Example 2 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode PetscLayoutSetLocalSize(PetscLayout map, PetscInt n)
```

Example 3 (unknown):
```unknown
PETSC_DECIDE
```

Example 4 (unknown):
```unknown
PetscLayoutSetSize()
```

---

## PetscLayoutSetSize#

**URL:** https://petsc.org/release/manualpages/IS/PetscLayoutSetSize/

**Contents:**
- PetscLayoutSetSize#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the global size for a PetscLayout object.

map - pointer to the map

n - the global size, use PETSC_DETERMINE (the default) to have this value computed as the sum of the local sizes set with PetscLayoutSetLocalSize()

PetscLayout, PetscLayoutCreate(), PetscLayoutSetLocalSize(), PetscLayoutGetLocalSize(), PetscLayoutGetSize(), PetscLayoutSetUp(), PetscLayoutGetRange(), PetscLayoutGetRanges(), PetscLayoutSetBlockSize(), PetscLayoutGetBlockSize()

src/vec/is/utils/pmap.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLayout
```

Example 2 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode PetscLayoutSetSize(PetscLayout map, PetscInt n)
```

Example 3 (unknown):
```unknown
PETSC_DETERMINE
```

Example 4 (unknown):
```unknown
PetscLayoutSetLocalSize()
```

---

## PetscLayoutSetUp#

**URL:** https://petsc.org/release/manualpages/IS/PetscLayoutSetUp/

**Contents:**
- PetscLayoutSetUp#
- Synopsis#
- Input Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

given a map where you have set either the global or local size sets up the map so that it may be used.

map - pointer to the map

Typical calling sequence

If range exists, and local size is not set, everything gets computed from the range.

If the local size, global size are already set and range exists then this does nothing.

PetscLayout, PetscLayoutSetLocalSize(), PetscLayoutSetSize(), PetscLayoutGetSize(), PetscLayoutGetLocalSize(), PetscLayout, PetscLayoutDestroy(), PetscLayoutGetRange(), PetscLayoutGetRanges(), PetscLayoutSetBlockSize(), PetscLayoutGetBlockSize(), PetscLayoutCreate(), PetscSplitOwnership()

src/vec/is/utils/pmap.c

src/ksp/ksp/tutorials/ex85.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode PetscLayoutSetUp(PetscLayout map)
```

Example 2 (unknown):
```unknown
PetscLayoutCreate(MPI_Comm,PetscLayout *);
  PetscLayoutSetBlockSize(PetscLayout,1);
  PetscLayoutSetSize(PetscLayout,n) or PetscLayoutSetLocalSize(PetscLayout,N); or both
  PetscLayoutSetUp(PetscLayout);
  PetscLayoutGetSize(PetscLayout,PetscInt *);
```

Example 3 (unknown):
```unknown
PetscLayoutSetLocalSize()
```

Example 4 (unknown):
```unknown
PetscLayoutSetSize()
```

---

## PetscLayout#

**URL:** https://petsc.org/release/manualpages/IS/PetscLayout/

**Contents:**
- PetscLayout#
- Synopsis#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

defines layout of vectors and matrices (that is the “global” numbering of vector and matrix entries) across MPI processes (which rows are owned by which processes)

PETSc vectors (Vec) have a global number associated with each vector entry. The first MPI process that shares the vector owns the first n0 entries of the vector, the second MPI process the next n1 entries, etc. A PetscLayout is a way of managing this information, for example the number of locally owned entries is provided by PetscLayoutGetLocalSize() and the range of indices for a given MPI process is provided by PetscLayoutGetRange().

Before calling PetscLayoutSetUp(), one must call either (or both) PetscLayoutSetSize() or PetscLayoutSetLocalSize(),

Each PETSc Vec contains a PetscLayout object which can be obtained with VecGetLayout(). For convenience Vec provides an API to access the layout information directly, for example with VecGetLocalSize() and VecGetOwnershipRange().

Similarly PETSc matrices have layouts, these are discussed in Matrices.

PetscLayoutCreate(), PetscLayoutDestroy(), PetscLayoutGetRange(), PetscLayoutGetLocalSize(), PetscLayoutGetSize(), PetscLayoutGetBlockSize(), PetscLayoutGetRanges(), PetscLayoutFindOwner(), PetscLayoutFindOwnerIndex(), VecGetLayout(), VecGetLocalSize(), VecGetOwnershipRange(), PetscLayoutSetUp(), PetscLayoutSetSize(), PetscLayoutSetLocalSize()

include/petscistypes.h

src/ksp/ksp/tutorials/ex87.c src/ksp/ksp/tutorials/ex85.c src/ts/tutorials/ex30.c src/ksp/ksp/tutorials/ex76f.F90 src/vec/vec/utils/tagger/tutorials/ex1.c src/ksp/ksp/tutorials/ex76.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _n_PetscLayout *PetscLayout;
```

Example 2 (unknown):
```unknown
PetscLayout
```

Example 3 (unknown):
```unknown
PetscLayoutGetLocalSize()
```

Example 4 (unknown):
```unknown
PetscLayoutGetRange()
```

---

## PetscOptionsGetVec#

**URL:** https://petsc.org/release/manualpages/Vec/PetscOptionsGetVec/

**Contents:**
- PetscOptionsGetVec#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Gets a Vec from the options database as an array of real values

options - the options database, or NULL for the default global one

prefix - an option prefix, or NULL

key - the option name (must include the leading -)

v - the vector to fill in on option match; unchanged if the option is not found

set - PETSC_TRUE if the option was found (may be NULL)

The option value is read as an array of PetscReal of length equal to the global size of v; each MPI process copies the entries corresponding to its local ownership range into v.

Vec, PetscOptionsGetRealArray(), PetscOptionsGetInt(), PetscOptionsGetReal(), VecView()

src/vec/vec/interface/vector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode PetscOptionsGetVec(PetscOptions options, const char prefix[], const char key[], Vec v, PetscBool *set)
```

Example 2 (unknown):
```unknown
PetscOptionsGetRealArray()
```

Example 3 (unknown):
```unknown
PetscOptionsGetInt()
```

Example 4 (unknown):
```unknown
PetscOptionsGetReal()
```

---

## PetscParallelSortInt#

**URL:** https://petsc.org/release/manualpages/IS/PetscParallelSortInt/

**Contents:**
- PetscParallelSortInt#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Globally sort a distributed array of integers

mapin - PetscLayout describing the distribution of the input keys

mapout - PetscLayout describing the desired distribution of the output keys

keysin - the pre-sorted array of integers

keysout - the array in which the sorted integers will be stored. If mapin == mapout, then keysin may be equal to keysout.

This implements a distributed samplesort, which, with local array sizes n_in and n_out, global size N, and global number of MPI processes P, does:

If keysin != keysout, then keysin will not be changed during PetscParallelSortInt().

PetscSortInt(), PetscParallelSortedInt()

src/vec/is/utils/psort.c

Index of all IS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscis.h" 
PetscErrorCode PetscParallelSortInt(PetscLayout mapin, PetscLayout mapout, PetscInt keysin[], PetscInt keysout[])
```

Example 2 (unknown):
```unknown
PetscLayout
```

Example 3 (unknown):
```unknown
PetscLayout
```

Example 4 (julia):
```julia
- sorts locally
  - chooses pivots by sorting (in parallel) (P-1) pivot suggestions from each process using bitonic sort and allgathering a subset of (P-1) of those
  - using to the pivots to repartition the keys by all-to-all exchange
  - sorting the repartitioned keys locally (the array is now globally sorted, but does not match the mapout layout)
  - redistributing to match the mapout layout
```

---

## PetscSectionVecNorm#

**URL:** https://petsc.org/release/manualpages/Vec/PetscSectionVecNorm/

**Contents:**
- PetscSectionVecNorm#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Computes the vector norm of each field

s - the local Section

gs - the global section

type - one of NORM_1, NORM_2, NORM_INFINITY.

val - the array of norms

VecNorm(), PetscSectionCreate()

src/vec/vec/utils/vsection.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
#include "petscvec.h"   
PetscErrorCode PetscSectionVecNorm(PetscSection s, PetscSection gs, Vec x, NormType type, PetscReal val[])
```

Example 2 (unknown):
```unknown
NORM_INFINITY
```

Example 3 (unknown):
```unknown
PetscSectionCreate()
```

---

## PetscSectionVecView#

**URL:** https://petsc.org/release/manualpages/Vec/PetscSectionVecView/

**Contents:**
- PetscSectionVecView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

View a vector, using the section to structure the values

s - the organizing PetscSection

viewer - the PetscViewer

PetscSection, PetscViewer, PetscSectionCreate(), VecSetValuesSection(), PetscSectionArrayView()

src/vec/vec/utils/vsection.c

src/dm/impls/plex/tutorials/ex14.c src/dm/impls/plex/tutorials/ex14f90.F90

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
#include "petscvec.h"   
PetscErrorCode PetscSectionVecView(PetscSection s, Vec v, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscSection
```

---

## PetscViennaCLIndices#

**URL:** https://petsc.org/release/manualpages/Vec/PetscViennaCLIndices/

**Contents:**
- PetscViennaCLIndices#
- Synopsis#
- See Also#
- Level#
- Location#

Opaque handle to an index buffer used by PETSc’s ViennaCL VECVIENNACL vector backend to perform partial scatters between CPU and GPU memory

Vec, VECVIENNACL, VecCreateSeqViennaCL(), VecCreateMPIViennaCL(), VecViennaCLCopyToGPUSome_Public(), VecViennaCLCopyFromGPUSome_Public()

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VECVIENNACL
```

Example 2 (julia):
```julia
typedef struct _p_PetscViennaCLIndices *PetscViennaCLIndices;
```

Example 3 (unknown):
```unknown
VECVIENNACL
```

Example 4 (unknown):
```unknown
VecCreateSeqViennaCL()
```

---

## ReductionType#

**URL:** https://petsc.org/release/manualpages/Vec/ReductionType/

**Contents:**
- ReductionType#
- Synopsis#
- Values#
- Developer Note#
- See Also#
- Level#
- Location#

determines what type of column reduction (one that is not a type of norm defined in NormType) to obtain with MatGetColumnReductions()

REDUCTION_SUM_REALPART - sum of real part of each matrix column

REDUCTION_SUM_IMAGINARYPART - sum of imaginary part of each matrix column

REDUCTION_MEAN_REALPART - arithmetic mean of real part of each matrix column

REDUCTION_MEAN_IMAGINARYPART - arithmetic mean of imaginary part of each matrix column

The constants defined in ReductionType MUST BE DISTINCT from those defined in NormType. This is because MatGetColumnReductions() is used to compute both norms and other types of reductions, and the constants defined in both NormType and ReductionType are used to designate the desired operation.

Vectors and Parallel Data, MatGetColumnReductions(), MatGetColumnNorms(), NormType, REDUCTION_SUM_REALPART, REDUCTION_SUM_IMAGINARYPART, REDUCTION_MEAN_REALPART, REDUCTION_MEAN_IMAGINARYPART

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
MatGetColumnReductions()
```

Example 2 (unknown):
```unknown
typedef enum {
  REDUCTION_SUM_REALPART       = 10,
  REDUCTION_MEAN_REALPART      = 11,
  REDUCTION_SUM_IMAGINARYPART  = 12,
  REDUCTION_MEAN_IMAGINARYPART = 13
} ReductionType;
```

Example 3 (unknown):
```unknown
REDUCTION_SUM_REALPART
```

Example 4 (unknown):
```unknown
REDUCTION_SUM_IMAGINARYPART
```

---

## REDUCTION_MEAN_IMAGINARYPART#

**URL:** https://petsc.org/release/manualpages/Vec/REDUCTION_MEAN_IMAGINARYPART/

**Contents:**
- REDUCTION_MEAN_IMAGINARYPART#
- See Also#
- Level#
- Location#

arithmetic mean of imaginary part of matrix column to obtain with MatGetColumnReductions()

Vectors and Parallel Data, ReductionType, MatGetColumnReductions(), REDUCTION_MEAN_REALPART, REDUCTION_SUM_IMAGINARYPART

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
MatGetColumnReductions()
```

Example 2 (unknown):
```unknown
ReductionType
```

Example 3 (unknown):
```unknown
MatGetColumnReductions()
```

Example 4 (unknown):
```unknown
REDUCTION_MEAN_REALPART
```

---

## REDUCTION_MEAN_REALPART#

**URL:** https://petsc.org/release/manualpages/Vec/REDUCTION_MEAN_REALPART/

**Contents:**
- REDUCTION_MEAN_REALPART#
- See Also#
- Level#
- Location#

arithmetic mean of real part of matrix column to obtain with MatGetColumnReductions()

Vectors and Parallel Data, ReductionType, MatGetColumnReductions(), REDUCTION_MEAN_IMAGINARYPART, REDUCTION_SUM_REALPART

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
MatGetColumnReductions()
```

Example 2 (unknown):
```unknown
ReductionType
```

Example 3 (unknown):
```unknown
MatGetColumnReductions()
```

Example 4 (unknown):
```unknown
REDUCTION_MEAN_IMAGINARYPART
```

---

## REDUCTION_SUM_IMAGINARYPART#

**URL:** https://petsc.org/release/manualpages/Vec/REDUCTION_SUM_IMAGINARYPART/

**Contents:**
- REDUCTION_SUM_IMAGINARYPART#
- See Also#
- Level#
- Location#

sum of imaginary part of matrix column to obtain with MatGetColumnReductions()

Vectors and Parallel Data, ReductionType, MatGetColumnReductions(), REDUCTION_SUM_REALPART, REDUCTION_MEAN_IMAGINARYPART

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
MatGetColumnReductions()
```

Example 2 (unknown):
```unknown
ReductionType
```

Example 3 (unknown):
```unknown
MatGetColumnReductions()
```

Example 4 (unknown):
```unknown
REDUCTION_SUM_REALPART
```

---

## REDUCTION_SUM_REALPART#

**URL:** https://petsc.org/release/manualpages/Vec/REDUCTION_SUM_REALPART/

**Contents:**
- REDUCTION_SUM_REALPART#
- See Also#
- Level#
- Location#

sum of real part of a matrix column to obtain with MatGetColumnReductions()

Vectors and Parallel Data, ReductionType, MatGetColumnReductions(), REDUCTION_SUM_IMAGINARYPART, REDUCTION_MEAN_REALPART

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
MatGetColumnReductions()
```

Example 2 (unknown):
```unknown
ReductionType
```

Example 3 (unknown):
```unknown
MatGetColumnReductions()
```

Example 4 (unknown):
```unknown
REDUCTION_SUM_IMAGINARYPART
```

---

## ScatterMode#

**URL:** https://petsc.org/release/manualpages/Vec/ScatterMode/

**Contents:**
- ScatterMode#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#
- Examples#

Determines the direction of a scatter in VecScatterBegin() and VecScatterEnd()

SCATTER_FORWARD - Scatters the values as dictated by the VecScatterCreate() call

SCATTER_REVERSE - Moves the values in the opposite direction than the directions indicated in the VecScatterCreate() call

SCATTER_FORWARD_LOCAL - Scatters the values as dictated by the VecScatterCreate() call except NO MPI communication is done

SCATTER_REVERSE_LOCAL - Moves the values in the opposite direction than the directions indicated in the VecScatterCreate() call except NO MPI communication is done

Vectors and Parallel Data, VecScatter, VecScatterBegin(), VecScatterEnd(), SCATTER_FORWARD, SCATTER_REVERSE, SCATTER_FORWARD_LOCAL, SCATTER_REVERSE_LOCAL

src/ksp/ksp/tutorials/ex73.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecScatterBegin()
```

Example 2 (unknown):
```unknown
VecScatterEnd()
```

Example 3 (unknown):
```unknown
typedef enum {
  SCATTER_FORWARD       = 0,
  SCATTER_REVERSE       = 1,
  SCATTER_FORWARD_LOCAL = 2,
  SCATTER_REVERSE_LOCAL = 3
} ScatterMode;
```

Example 4 (unknown):
```unknown
SCATTER_FORWARD
```

---

## SCATTER_FORWARD#

**URL:** https://petsc.org/release/manualpages/Vec/SCATTER_FORWARD/

**Contents:**
- SCATTER_FORWARD#
- See Also#
- Level#
- Location#
- Examples#

Scatters the values as dictated by the VecScatterCreate() call during VecScatterBegin() and VecScatterEnd()

Vectors and Parallel Data, VecScatter, ScatterMode, VecScatterCreate(), VecScatterBegin(), VecScatterEnd(), SCATTER_REVERSE, SCATTER_FORWARD_LOCAL, SCATTER_REVERSE_LOCAL

src/vec/vec/tutorials/ex14f.F90 src/ksp/ksp/tutorials/ex70.c src/ksp/ksp/tutorials/ex73.c src/snes/tutorials/ex13.c src/snes/tutorials/ex42.c src/vec/vec/tutorials/ex9.c src/ksp/ksp/tutorials/ex49.c src/vec/vec/utils/tagger/tutorials/ex1.c src/ksp/ksp/tutorials/ex43.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecScatterCreate()
```

Example 2 (unknown):
```unknown
VecScatterBegin()
```

Example 3 (unknown):
```unknown
VecScatterEnd()
```

Example 4 (unknown):
```unknown
ScatterMode
```

---

## SCATTER_FORWARD_LOCAL#

**URL:** https://petsc.org/release/manualpages/Vec/SCATTER_FORWARD_LOCAL/

**Contents:**
- SCATTER_FORWARD_LOCAL#
- See Also#
- Level#
- Location#

Scatters the values as dictated by the VecScatterCreate() during VecScatterBegin() and VecScatterEnd() call except NO parallel communication is done. Any variables that have be moved between processes are ignored

Vectors and Parallel Data, VecScatter, ScatterMode, VecScatterCreate(), VecScatterBegin(), VecScatterEnd(), SCATTER_REVERSE, SCATTER_FORWARD, SCATTER_REVERSE_LOCAL

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecScatterCreate()
```

Example 2 (unknown):
```unknown
VecScatterBegin()
```

Example 3 (unknown):
```unknown
VecScatterEnd()
```

Example 4 (unknown):
```unknown
ScatterMode
```

---

## SCATTER_REVERSE#

**URL:** https://petsc.org/release/manualpages/Vec/SCATTER_REVERSE/

**Contents:**
- SCATTER_REVERSE#
- See Also#
- Level#
- Location#
- Examples#

Moves the values in the opposite direction than the directions indicated in the VecScatterCreate() during VecScatterBegin() and VecScatterEnd()

Vectors and Parallel Data, VecScatter, ScatterMode, VecScatterCreate(), VecScatterBegin(), VecScatterEnd(), SCATTER_FORWARD, SCATTER_FORWARD_LOCAL, SCATTER_REVERSE_LOCAL

src/dm/tutorials/ex14.c src/ts/tutorials/ex30.c src/ksp/ksp/tutorials/ex73.c src/vec/vec/tutorials/ex9.c src/snes/tutorials/ex42.c src/tao/pde_constrained/tutorials/elliptic.c src/tao/pde_constrained/tutorials/parabolic.c src/tao/pde_constrained/tutorials/hyperbolic.c src/dm/impls/swarm/tutorials/ex1.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecScatterCreate()
```

Example 2 (unknown):
```unknown
VecScatterBegin()
```

Example 3 (unknown):
```unknown
VecScatterEnd()
```

Example 4 (unknown):
```unknown
ScatterMode
```

---

## SCATTER_REVERSE_LOCAL#

**URL:** https://petsc.org/release/manualpages/Vec/SCATTER_REVERSE_LOCAL/

**Contents:**
- SCATTER_REVERSE_LOCAL#
- See Also#
- Level#
- Location#

Moves the values in the opposite direction than the directions indicated in the VecScatterCreate() during VecScatterBegin() and VecScatterEnd() except NO parallel communication is done. Any variables that have be moved between processes are ignored

Vectors and Parallel Data, VecScatter, ScatterMode, VecScatterCreate(), VecScatterBegin(), VecScatterEnd(), SCATTER_FORWARD, SCATTER_FORWARD_LOCAL, SCATTER_REVERSE

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecScatterCreate()
```

Example 2 (unknown):
```unknown
VecScatterBegin()
```

Example 3 (unknown):
```unknown
VecScatterEnd()
```

Example 4 (unknown):
```unknown
ScatterMode
```

---

## VecAbs#

**URL:** https://petsc.org/release/manualpages/Vec/VecAbs/

**Contents:**
- VecAbs#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Replaces every element in a vector with its absolute value.

Vec, VecExp(), VecSqrtAbs(), VecReciprocal(), VecLog(), VecPointwiseSign()

src/vec/vec/utils/vinv.c

src/tao/tutorials/ex4.c src/tao/unconstrained/tutorials/elastic_net_regularization.c

VecAbs_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecAbs(Vec v)
```

Example 2 (unknown):
```unknown
VecSqrtAbs()
```

Example 3 (unknown):
```unknown
VecReciprocal()
```

Example 4 (unknown):
```unknown
VecPointwiseSign()
```

---

## VecAppendOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/Vec/VecAppendOptionsPrefix/

**Contents:**
- VecAppendOptionsPrefix#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Appends to the prefix used for searching for all Vec options in the database.

prefix - the prefix to prepend to all option names

A hyphen (-) must NOT be given at the beginning of the prefix name. The first character of all runtime options is AUTOMATICALLY the hyphen.

Vectors and Parallel Data, Vec, VecGetOptionsPrefix()

src/vec/vec/interface/vector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecAppendOptionsPrefix(Vec v, const char prefix[])
```

Example 2 (unknown):
```unknown
VecGetOptionsPrefix()
```

---

## VecAssemblyBegin#

**URL:** https://petsc.org/release/manualpages/Vec/VecAssemblyBegin/

**Contents:**
- VecAssemblyBegin#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Begins assembling the vector; that is ensuring all the vector’s entries are stored on the correct MPI process. This routine should be called after completing all calls to VecSetValues().

Vectors and Parallel Data, Vec, VecAssemblyEnd(), VecSetValues()

src/vec/vec/interface/vector.c

src/snes/tutorials/ex28.c src/mat/tutorials/ex3.c src/snes/tutorials/ex73f90t.F90 src/ksp/ksp/tutorials/ex72.c src/snes/tutorials/ex70.c src/mat/tutorials/ex2.c src/snes/tutorials/ex30.c src/snes/tutorials/ex56.c src/ksp/pc/tutorials/ex2.c src/ksp/pc/tutorials/ex1.c

VecAssemblyBegin_MPI() in src/vec/vec/impls/mpi/pdvec.c VecAssemblyBegin_Nest() in src/vec/vec/impls/nest/vecnest.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecSetValues()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecAssemblyBegin(Vec vec)
```

Example 3 (unknown):
```unknown
VecAssemblyEnd()
```

Example 4 (unknown):
```unknown
VecSetValues()
```

---

## VecAssemblyEnd#

**URL:** https://petsc.org/release/manualpages/Vec/VecAssemblyEnd/

**Contents:**
- VecAssemblyEnd#
- Synopsis#
- Input Parameter#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Completes assembling the vector. This routine should be called after VecAssemblyBegin().

-vec_view [viewertype][:…] - Display the vector. See VecViewFromOptions()/PetscObjectViewFromOptions() for the possible arguments

-vecstash_view [viewertype][:…] - Display the vector stash. See VecStashViewFromOptions()/PetscObjectViewFromOptions() for the possible arguments

Vectors and Parallel Data, Vec, VecAssemblyBegin(), VecSetValues(), VecViewFromOptions(), VecStashViewFromOptions(), PetscObjectViewFromOptions()

src/vec/vec/interface/vector.c

src/snes/tutorials/ex28.c src/mat/tutorials/ex3.c src/snes/tutorials/ex73f90t.F90 src/ksp/ksp/tutorials/ex72.c src/snes/tutorials/ex70.c src/mat/tutorials/ex2.c src/snes/tutorials/ex30.c src/snes/tutorials/ex56.c src/ksp/pc/tutorials/ex2.c src/ksp/pc/tutorials/ex1.c

VecAssemblyEnd_MPI() in src/vec/vec/impls/mpi/pdvec.c VecAssemblyEnd_Nest() in src/vec/vec/impls/nest/vecnest.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecAssemblyBegin()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecAssemblyEnd(Vec vec)
```

Example 3 (unknown):
```unknown
VecViewFromOptions()
```

Example 4 (unknown):
```unknown
PetscObjectViewFromOptions()
```

---

## VecAXPBYPCZ#

**URL:** https://petsc.org/release/manualpages/Vec/VecAXPBYPCZ/

**Contents:**
- VecAXPBYPCZ#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#

Computes z = alpha x + beta y + gamma z

x, y and z must be different vectors

The implementation is optimized for alpha of 1.0 and gamma of 1.0 or 0.0

Vectors and Parallel Data, Vec, VecAYPX(), VecMAXPY(), VecWAXPY(), VecAXPY(), VecAXPBY()

src/vec/vec/interface/rvector.c

src/tao/tutorials/ex4.c

VecAXPBYPCZ_Nest() in src/vec/vec/impls/nest/vecnest.c VecAXPBYPCZ_Seq() in src/vec/vec/impls/seq/bvec1.c VecAXPBYPCZ_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecAXPBYPCZ_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
z = alpha x + beta y + gamma z
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecAXPBYPCZ(Vec z, PetscScalar alpha, PetscScalar beta, PetscScalar gamma, Vec x, Vec y)
```

---

## VecAXPBY#

**URL:** https://petsc.org/release/manualpages/Vec/VecAXPBY/

**Contents:**
- VecAXPBY#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Computes y = alpha x + beta y.

x - the first scaled vector

y - the second scaled vector

The implementation is optimized for alpha and/or beta values of 0.0 and 1.0

Vectors and Parallel Data, Vec, VecAYPX(), VecMAXPY(), VecWAXPY(), VecAXPY(), VecAXPBYPCZ()

src/vec/vec/interface/rvector.c

src/ts/tutorials/ex30.c

VecAXPBY_Nest() in src/vec/vec/impls/nest/vecnest.c VecAXPBY_Seq() in src/vec/vec/impls/seq/bvec1.c VecAXPBY_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecAXPBY_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
y = alpha x + beta y
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecAXPBY(Vec y, PetscScalar alpha, PetscScalar beta, Vec x)
```

Example 3 (unknown):
```unknown
VecAXPBYPCZ()
```

---

## VecAXPY#

**URL:** https://petsc.org/release/manualpages/Vec/VecAXPY/

**Contents:**
- VecAXPY#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Computes y = alpha x + y.

x - vector scale by alpha

y - vector accumulated into

This routine is optimized for alpha of 0.0, otherwise it calls the BLAS routine

Vectors and Parallel Data, Vec, VecAYPX(), VecMAXPY(), VecWAXPY(), VecAXPBYPCZ(), VecAXPBY()

src/vec/vec/interface/rvector.c

src/mat/tutorials/ex9.c src/snes/tutorials/ex9.c src/snes/tutorials/ex12.c src/snes/tutorials/ex70.c src/mat/tutorials/ex2.c src/snes/tutorials/ex15.c src/snes/tutorials/ex69.c src/snes/tutorials/ex7.c src/snes/tutorials/ex22.c src/snes/tutorials/ex77.c

VecAXPY_Nest() in src/vec/vec/impls/nest/vecnest.c VecAXPY_Seq() in src/vec/vec/impls/seq/bvec1.c VecAXPY_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecAXPY_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
y = alpha x + y
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecAXPY(Vec y, PetscScalar alpha, Vec x)
```

Example 3 (unknown):
```unknown
VecAXPY(y,alpha,x)                   y = alpha x           +      y
    VecAYPX(y,beta,x)                    y =       x           + beta y
    VecAXPBY(y,alpha,beta,x)             y = alpha x           + beta y
    VecWAXPY(w,alpha,x,y)                w = alpha x           +      y
    VecAXPBYPCZ(z,alpha,beta,gamma,x,y)  z = alpha x           + beta y + gamma z
    VecMAXPY(y,nv,alpha[],x[])           y = sum alpha[i] x[i] +      y
```

Example 4 (unknown):
```unknown
VecAXPBYPCZ()
```

---

## VecAYPX#

**URL:** https://petsc.org/release/manualpages/Vec/VecAYPX/

**Contents:**
- VecAYPX#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Computes y = x + beta y.

x - the unscaled vector

y - the vector to be scaled

The implementation is optimized for beta of -1.0, 0.0, and 1.0

Vectors and Parallel Data, Vec, VecMAXPY(), VecWAXPY(), VecAXPY(), VecAXPBYPCZ(), VecAXPBY()

src/vec/vec/interface/rvector.c

src/ksp/ksp/tutorials/ex100f.F90 src/vec/vec/tutorials/ex1.c src/ksp/ksp/tutorials/ex14f.F90 src/ksp/ksp/tutorials/ex100.c src/tao/pde_constrained/tutorials/elliptic.c src/tao/pde_constrained/tutorials/parabolic.c src/ksp/ksp/tutorials/ex74.c src/vec/vec/tutorials/ex1f90.F90 src/tao/pde_constrained/tutorials/hyperbolic.c src/vec/vec/tutorials/ex20f90.F90

VecAYPX_Nest() in src/vec/vec/impls/nest/vecnest.c VecAYPX_Seq() in src/vec/vec/impls/seq/dvec2.c VecAYPX_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecAYPX_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
y = x + beta y
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecAYPX(Vec y, PetscScalar beta, Vec x)
```

Example 3 (unknown):
```unknown
VecAXPBYPCZ()
```

---

## VecBindToCPU#

**URL:** https://petsc.org/release/manualpages/Vec/VecBindToCPU/

**Contents:**
- VecBindToCPU#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

marks a vector to temporarily stay on the CPU and perform computations on the CPU

flg - bind to the CPU if value of PETSC_TRUE

Vectors and Parallel Data, Vec, VecBoundToCPU()

src/vec/vec/interface/vector.c

VecBindToCPU_MPIViennaCL() in src/vec/vec/impls/mpi/mpiviennacl/mpiviennacl.cxx VecBindToCPU_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecBindToCPU_SeqAIJViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecBindToCPU(Vec v, PetscBool flg)
```

Example 2 (unknown):
```unknown
VecBoundToCPU()
```

---

## VecBoundGradientProjection#

**URL:** https://petsc.org/release/manualpages/Vec/VecBoundGradientProjection/

**Contents:**
- VecBoundGradientProjection#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Projects vector according to this definition. If XL[i] < X[i] < XU[i], then GP[i] = G[i]; If X[i] <= XL[i], then GP[i] = min(G[i],0); If X[i] >= XU[i], then GP[i] = max(G[i],0);

G - current gradient vector

X - current solution vector with XL[i] <= X[i] <= XU[i]

GP - gradient projection vector

GP may be the same vector as G

For complex numbers only the real part is used in the bounds.

src/vec/vec/utils/projection.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"  
PetscErrorCode VecBoundGradientProjection(Vec G, Vec X, Vec XL, Vec XU, Vec GP)
```

---

## VecBoundToCPU#

**URL:** https://petsc.org/release/manualpages/Vec/VecBoundToCPU/

**Contents:**
- VecBoundToCPU#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

query if a vector is bound to the CPU

flg - the logical flag

Vectors and Parallel Data, Vec, VecBindToCPU()

src/vec/vec/interface/vector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecBoundToCPU(Vec v, PetscBool *flg)
```

Example 2 (unknown):
```unknown
VecBindToCPU()
```

---

## VecCheckAssembled#

**URL:** https://petsc.org/release/manualpages/Vec/VecCheckAssembled/

**Contents:**
- VecCheckAssembled#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#

checks if values have been changed in the vector, by VecSetValues() or related routines, but it has not been assembled

v - the vector to check

After calls to VecSetValues() and related routines one must call VecAssemblyBegin() and VecAssemblyEnd() before using the vector

Vectors and Parallel Data, Vec, VecSetValues(), VecAssemblyBegin(), VecAssemblyEnd(), MatAssemblyBegin(), MatAssemblyEnd()

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecSetValues()
```

Example 2 (cpp):
```cpp
#include <petscvec.h>
VecCheckAssembled(Vec v);
```

Example 3 (unknown):
```unknown
VecSetValues()
```

Example 4 (unknown):
```unknown
VecAssemblyBegin()
```

---

## VecConcatenate#

**URL:** https://petsc.org/release/manualpages/Vec/VecConcatenate/

**Contents:**
- VecConcatenate#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Creates a new vector that is a vertical concatenation of all the given array of vectors in the order they appear in the array. The concatenated vector resides on the same communicator and is the same type as the source vectors.

nx - number of vectors to be concatenated

X - array containing the vectors to be concatenated in the order of concatenation

Y - concatenated vector

x_is - array of index sets corresponding to the concatenated components of Y (pass NULL if not needed)

Concatenation is similar to the functionality of a VECNEST object; they both represent combination of different vector spaces. However, concatenated vectors do not store any information about their sub-vectors and own their own data. Consequently, this function provides index sets to enable the manipulation of data in the concatenated vector that corresponds to the original components at creation.

This is a useful tool for outer loop algorithms, particularly constrained optimizers, where the solver has to operate on combined vector spaces and cannot utilize VECNEST objects due to incompatibility with bound projections.

Vectors and Parallel Data, Vec, VECNEST, VECSCATTER, VecScatterCreate()

src/vec/vec/interface/rvector.c

src/vec/vec/tutorials/ex44.c

VecConcatenate_Nest() in src/vec/vec/impls/nest/vecnest.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecConcatenate(PetscInt nx, const Vec X[], Vec *Y, IS *x_is[])
```

Example 2 (unknown):
```unknown
VecScatterCreate()
```

---

## VecConjugate#

**URL:** https://petsc.org/release/manualpages/Vec/VecConjugate/

**Contents:**
- VecConjugate#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Conjugates a vector. That is, replace every entry in a vector with its complex conjugate

Vectors and Parallel Data, Vec, VecSet()

src/vec/vec/utils/vinv.c

VecConjugate_Nest() in src/vec/vec/impls/nest/vecnest.c VecConjugate_Seq() in src/vec/vec/impls/seq/bvec2.c VecConjugate_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecConjugate(Vec x)
```

---

## VecCopy#

**URL:** https://petsc.org/release/manualpages/Vec/VecCopy/

**Contents:**
- VecCopy#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#

Copies a vector y = x

For default parallel PETSc vectors, both x and y must be distributed in the same manner; local copies are done.

PetscCheckSameTypeAndComm(x,1,y,2) is not used on these vectors because we allow one of the vectors to be sequential and one to be parallel so long as both have the same local sizes. This is used in some internal functions in PETSc.

Vectors and Parallel Data, Vec, VecDuplicate()

src/vec/vec/interface/vector.c

src/mat/tutorials/ex9.c src/snes/tutorials/ex15.c src/ksp/ksp/tutorials/ex9.c src/vec/vec/tutorials/ex1.c src/ksp/ksp/tutorials/ex14f.F90 src/snes/tutorials/ex30.c src/ksp/ksp/tutorials/ex27.c src/snes/tutorials/ex33.c src/snes/tutorials/ex3.c src/ksp/ksp/tutorials/ex28.c

VecCopy_Nest() in src/vec/vec/impls/nest/vecnest.c VecCopy_Seq() in src/vec/vec/impls/seq/bvec2.c VecCopy_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecCopy_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecCopy(Vec x, Vec y)
```

Example 2 (unknown):
```unknown
PetscCheckSameTypeAndComm
```

Example 3 (unknown):
```unknown
VecDuplicate()
```

---

## VecCreateFromOptions#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateFromOptions/

**Contents:**
- VecCreateFromOptions#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#

Creates a vector whose type is set from the options database

comm - The communicator for the vector object

prefix - [optional] prefix for the options database

bs - the block size (commonly 1)

m - the local size (or PETSC_DECIDE)

n - the global size (or PETSC_DETERMINE)

vec - The vector object

-vec_type - see VecType, for example seq, mpi, cuda, defaults to mpi

Vectors and Parallel Data, Vec, VecSetType(), VecSetSizes(), VecCreateMPIWithArray(), VecCreateMPI(), VecDuplicate(), VecDuplicateVecs(), VecCreateGhost(), VecCreateSeq(), VecPlaceArray(), VecCreate(), VecType

src/vec/vec/interface/veccreate.c

src/ts/tutorials/ex11.c src/ksp/ksp/tutorials/ex77.c src/ksp/ksp/tutorials/ex2f.F90 src/ksp/ksp/tutorials/ex52f.F90 src/vec/vec/tutorials/ex2f.F90 src/vec/vec/tutorials/ex42a.c src/ksp/ksp/tutorials/ex57f.F90 src/dm/field/tutorials/ex1.c src/ksp/ksp/tutorials/ex15f.F90

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecCreateFromOptions(MPI_Comm comm, const char *prefix, PetscInt bs, PetscInt m, PetscInt n, Vec *vec)
```

Example 2 (unknown):
```unknown
PETSC_DECIDE
```

Example 3 (unknown):
```unknown
PETSC_DETERMINE
```

Example 4 (unknown):
```unknown
VecSetType()
```

---

## VecCreateGhostBlockWithArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateGhostBlockWithArray/

**Contents:**
- VecCreateGhostBlockWithArray#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates a parallel vector with ghost padding on each processor; the caller allocates the array space. Indices in the ghost region are based on blocks.

comm - the MPI communicator to use

n - local vector length

N - global vector length (or PETSC_DETERMINE to have calculated if n is given)

nghost - number of local ghost blocks

ghosts - global indices of ghost blocks (or NULL if not needed), counts are by block not by index, these do not need to be in increasing order (sorted)

array - the space to store the vector values (as long as \(n + nghost*bs\))

vv - the global vector representation (without ghost points as part of vector)

Use VecGhostGetLocalForm() to access the local, ghosted representation of the vector.

n is the local vector size (total local size not the number of blocks) while nghost is the number of blocks in the ghost portion, i.e. the number of elements in the ghost portion is bs*nghost

Vectors and Parallel Data, Vec, VecType, VecCreate(), VecGhostGetLocalForm(), VecGhostRestoreLocalForm(), VecCreateGhost(), VecCreateSeqWithArray(), VecCreateMPIWithArray(), VecCreateGhostWithArray(), VecCreateGhostBlock(), VecGhostUpdateBegin(), VecGhostUpdateEnd()

src/vec/vec/impls/mpi/pbvec.c

src/vec/vec/tutorials/ex14f.F90

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecCreateGhostBlockWithArray(MPI_Comm comm, PetscInt bs, PetscInt n, PetscInt N, PetscInt nghost, const PetscInt ghosts[], const PetscScalar array[], Vec *vv)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
VecGhostGetLocalForm()
```

Example 4 (unknown):
```unknown
VecCreate()
```

---

## VecCreateGhostBlock#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateGhostBlock/

**Contents:**
- VecCreateGhostBlock#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates a parallel vector with ghost padding on each processor. The indicing of the ghost points is done with blocks.

comm - the MPI communicator to use

n - local vector length

N - global vector length (or PETSC_DETERMINE to have calculated if n is given)

nghost - number of local ghost blocks

ghosts - global indices of ghost blocks, counts are by block, not by individual index, these do not need to be in increasing order (sorted)

vv - the global vector representation (without ghost points as part of vector)

Use VecGhostGetLocalForm() to access the local, ghosted representation of the vector.

n is the local vector size (total local size not the number of blocks) while nghost is the number of blocks in the ghost portion, i.e. the number of elements in the ghost portion is bs*nghost

Vectors and Parallel Data, Vec, VecType, VecCreateSeq(), VecCreate(), VecDuplicate(), VecDuplicateVecs(), VecCreateMPI(), VecGhostGetLocalForm(), VecGhostRestoreLocalForm(), VecGhostUpdateBegin(), VecGhostUpdateEnd(), VecCreateGhostWithArray(), VecCreateMPIWithArray(), VecCreateGhostBlockWithArray()

src/vec/vec/impls/mpi/pbvec.c

src/vec/vec/tutorials/ex14f.F90

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecCreateGhostBlock(MPI_Comm comm, PetscInt bs, PetscInt n, PetscInt N, PetscInt nghost, const PetscInt ghosts[], Vec *vv)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
VecGhostGetLocalForm()
```

Example 4 (unknown):
```unknown
VecCreateSeq()
```

---

## VecCreateGhostWithArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateGhostWithArray/

**Contents:**
- VecCreateGhostWithArray#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates a parallel vector with ghost padding on each processor; the caller allocates the array space.

comm - the MPI communicator to use

n - local vector length

N - global vector length (or PETSC_DETERMINE to have calculated if n is given)

nghost - number of local ghost points

ghosts - global indices of ghost points (or NULL if not needed), these do not need to be in increasing order (sorted)

array - the space to store the vector values (as long as n + nghost)

vv - the global vector representation (without ghost points as part of vector)

Use VecGhostGetLocalForm() to access the local, ghosted representation of the vector.

This also automatically sets the ISLocalToGlobalMapping() for this vector.

Vectors and Parallel Data, Vec, VecType, VecCreate(), VecGhostGetLocalForm(), VecGhostRestoreLocalForm(), VecCreateGhost(), VecCreateSeqWithArray(), VecCreateMPIWithArray(), VecCreateGhostBlock(), VecCreateGhostBlockWithArray(), VecMPISetGhost(), VecGhostUpdateBegin(), VecGhostUpdateEnd()

src/vec/vec/impls/mpi/pbvec.c

src/vec/vec/tutorials/ex9f.F90 src/vec/vec/tutorials/ex9.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecCreateGhostWithArray(MPI_Comm comm, PetscInt n, PetscInt N, PetscInt nghost, const PetscInt ghosts[], const PetscScalar array[], Vec *vv)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
VecGhostGetLocalForm()
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMapping()
```

---

## VecCreateGhost#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateGhost/

**Contents:**
- VecCreateGhost#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates a parallel vector with ghost padding on each processor.

comm - the MPI communicator to use

n - local vector length

N - global vector length (or PETSC_DETERMINE to have calculated if n is given)

nghost - number of local ghost points

ghosts - global indices of ghost points, these do not need to be in increasing order (sorted)

vv - the global vector representation (without ghost points as part of vector)

Use VecGhostGetLocalForm() to access the local, ghosted representation of the vector.

This also automatically sets the ISLocalToGlobalMapping() for this vector.

Vectors and Parallel Data, Vec, VecType, VecCreateSeq(), VecCreate(), VecDuplicate(), VecDuplicateVecs(), VecCreateMPI(), VecGhostGetLocalForm(), VecGhostRestoreLocalForm(), VecGhostUpdateBegin(), VecCreateGhostWithArray(), VecCreateMPIWithArray(), VecGhostUpdateEnd(), VecCreateGhostBlock(), VecCreateGhostBlockWithArray(), VecMPISetGhost()

src/vec/vec/impls/mpi/pbvec.c

src/vec/vec/tutorials/ex9f.F90 src/vec/vec/tutorials/ex9.c src/snes/tutorials/ex42.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecCreateGhost(MPI_Comm comm, PetscInt n, PetscInt N, PetscInt nghost, const PetscInt ghosts[], Vec *vv)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
VecGhostGetLocalForm()
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMapping()
```

---

## VecCreateLocalVector#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateLocalVector/

**Contents:**
- VecCreateLocalVector#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Creates a vector object suitable for use with VecGetLocalVector() and friends. You must call VecDestroy() when the vector is no longer needed.

v - The vector for which the local vector is desired.

w - Upon exit this contains the local vector.

Vectors and Parallel Data, Vec, VecGetLocalVectorRead(), VecRestoreLocalVectorRead(), VecGetLocalVector(), VecRestoreLocalVector()

src/vec/vec/interface/rvector.c

VecCreateLocalVector_Nest() in src/vec/vec/impls/nest/vecnest.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetLocalVector()
```

Example 2 (unknown):
```unknown
VecDestroy()
```

Example 3 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecCreateLocalVector(Vec v, Vec *w)
```

Example 4 (unknown):
```unknown
VecGetLocalVectorRead()
```

---

## VecCreateMPICUDAWithArrays#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateMPICUDAWithArrays/

**Contents:**
- VecCreateMPICUDAWithArrays#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a parallel, array-style vector using CUDA, where the user provides the complete array space to store the vector values.

Collective, Possibly Synchronous

comm - the MPI communicator to use

bs - block size, same meaning as VecSetBlockSize()

n - local vector length, cannot be PETSC_DECIDE

N - global vector length (or PETSC_DECIDE to have calculated)

cpuarray - CPU memory where the vector elements are to be stored (or NULL)

gpuarray - GPU memory where the vector elements are to be stored (or NULL)

See VecCreateSeqCUDAWithArrays() for further discussion, this routine shares identical semantics.

VecCreateMPICUDA(), VecCreateSeqCUDAWithArrays(), VecCreateMPIWithArray(), VecCreateSeqWithArray(), VecCreate(), VecDuplicate(), VecDuplicateVecs(), VecCreateGhost(), VecCreateMPI(), VecCreateGhostWithArray(), VecPlaceArray()

src/vec/vec/impls/mpi/cupm/cuda/vecmpicupm.cu

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecCreateMPICUDAWithArrays(MPI_Comm comm, PetscInt bs, PetscInt n, PetscInt N, const PetscScalar cpuarray[], const PetscScalar gpuarray[], Vec *v)
```

Example 2 (unknown):
```unknown
VecSetBlockSize()
```

Example 3 (unknown):
```unknown
PETSC_DECIDE
```

Example 4 (unknown):
```unknown
PETSC_DECIDE
```

---

## VecCreateMPICUDAWithArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateMPICUDAWithArray/

**Contents:**
- VecCreateMPICUDAWithArray#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a parallel, array-style vector using CUDA, where the user provides the device array space to store the vector values.

comm - the MPI communicator to use

bs - block size, same meaning as VecSetBlockSize()

n - local vector length, cannot be PETSC_DECIDE

N - global vector length (or PETSC_DECIDE to have calculated)

gpuarray - the user provided GPU array to store the vector values

See VecCreateSeqCUDAWithArray() for further discussion, this routine shares identical semantics.

VecCreateMPICUDA(), VecCreateSeqCUDAWithArray(), VecCreateMPIWithArray(), VecCreateSeqWithArray(), VecCreate(), VecDuplicate(), VecDuplicateVecs(), VecCreateGhost(), VecCreateMPI(), VecCreateGhostWithArray(), VecPlaceArray()

src/vec/vec/impls/mpi/cupm/cuda/vecmpicupm.cu

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecCreateMPICUDAWithArray(MPI_Comm comm, PetscInt bs, PetscInt n, PetscInt N, const PetscScalar gpuarray[], Vec *v)
```

Example 2 (unknown):
```unknown
VecSetBlockSize()
```

Example 3 (unknown):
```unknown
PETSC_DECIDE
```

Example 4 (unknown):
```unknown
PETSC_DECIDE
```

---

## VecCreateMPICUDA#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateMPICUDA/

**Contents:**
- VecCreateMPICUDA#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a standard, parallel, array-style vector for CUDA devices.

Collective, Possibly Synchronous

comm - the MPI communicator to use

n - local vector length (or PETSC_DECIDE to have calculated if N is given)

N - global vector length (or PETSC_DETERMINE to have calculated if n is given)

Use VecDuplicate() or VecDuplicateVecs() to form additional vectors of the same type as an existing vector.

This function may initialize PetscDevice, which may incur a device synchronization.

VecCreateMPICUDAWithArray(), VecCreateMPICUDAWithArrays(), VecCreateSeqCUDA(), VecCreateSeq(), VecCreateMPI(), VecCreate(), VecDuplicate(), VecDuplicateVecs(), VecCreateGhost(), VecCreateMPIWithArray(), VecCreateGhostWithArray(), VecMPISetGhost()

src/vec/vec/impls/mpi/cupm/cuda/vecmpicupm.cu

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecCreateMPICUDA(MPI_Comm comm, PetscInt n, PetscInt N, Vec *v)
```

Example 2 (unknown):
```unknown
PETSC_DECIDE
```

Example 3 (unknown):
```unknown
PETSC_DETERMINE
```

Example 4 (unknown):
```unknown
VecDuplicate()
```

---

## VecCreateMPIHIPWithArrays#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateMPIHIPWithArrays/

**Contents:**
- VecCreateMPIHIPWithArrays#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a parallel, array-style vector using HIP, where the user provides the complete array space to store the vector values.

Collective, Possibly Synchronous

comm - the MPI communicator to use

bs - block size, same meaning as VecSetBlockSize()

n - local vector length, cannot be PETSC_DECIDE

N - global vector length (or PETSC_DECIDE to have calculated)

cpuarray - CPU memory where the vector elements are to be stored (or NULL)

gpuarray - GPU memory where the vector elements are to be stored (or NULL)

See VecCreateSeqHIPWithArrays() for further discussion, this routine shares identical semantics.

VecCreateMPIHIP(), VecCreateSeqHIPWithArrays(), VecCreateMPIWithArray(), VecCreateSeqWithArray(), VecCreate(), VecDuplicate(), VecDuplicateVecs(), VecCreateGhost(), VecCreateMPI(), VecCreateGhostWithArray(), VecPlaceArray()

src/vec/vec/impls/mpi/cupm/hip/vecmpicupm.hip.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecCreateMPIHIPWithArrays(MPI_Comm comm, PetscInt bs, PetscInt n, PetscInt N, const PetscScalar cpuarray[], const PetscScalar gpuarray[], Vec *v)
```

Example 2 (unknown):
```unknown
VecSetBlockSize()
```

Example 3 (unknown):
```unknown
PETSC_DECIDE
```

Example 4 (unknown):
```unknown
PETSC_DECIDE
```

---

## VecCreateMPIHIPWithArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateMPIHIPWithArray/

**Contents:**
- VecCreateMPIHIPWithArray#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a parallel, array-style vector using HIP, where the user provides the device array space to store the vector values.

comm - the MPI communicator to use

bs - block size, same meaning as VecSetBlockSize()

n - local vector length, cannot be PETSC_DECIDE

N - global vector length (or PETSC_DECIDE to have calculated)

gpuarray - the user provided GPU array to store the vector values

See VecCreateSeqHIPWithArray() for further discussion, this routine shares identical semantics.

VecCreateMPIHIP(), VecCreateSeqHIPWithArray(), VecCreateMPIWithArray(), VecCreateSeqWithArray(), VecCreate(), VecDuplicate(), VecDuplicateVecs(), VecCreateGhost(), VecCreateMPI(), VecCreateGhostWithArray(), VecPlaceArray()

src/vec/vec/impls/mpi/cupm/hip/vecmpicupm.hip.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecCreateMPIHIPWithArray(MPI_Comm comm, PetscInt bs, PetscInt n, PetscInt N, const PetscScalar gpuarray[], Vec *v)
```

Example 2 (unknown):
```unknown
VecSetBlockSize()
```

Example 3 (unknown):
```unknown
PETSC_DECIDE
```

Example 4 (unknown):
```unknown
PETSC_DECIDE
```

---

## VecCreateMPIHIP#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateMPIHIP/

**Contents:**
- VecCreateMPIHIP#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a standard, parallel, array-style vector for HIP devices.

Collective, Possibly Synchronous

comm - the MPI communicator to use

n - local vector length (or PETSC_DECIDE to have calculated if N is given)

N - global vector length (or PETSC_DETERMINE to have calculated if n is given)

Use VecDuplicate() or VecDuplicateVecs() to form additional vectors of the same type as an existing vector.

This function may initialize PetscDevice, which may incur a device synchronization.

VecCreateMPIHIPWithArray(), VecCreateMPIHIPWithArrays(), VecCreateSeqHIP(), VecCreateSeq(), VecCreateMPI(), VecCreate(), VecDuplicate(), VecDuplicateVecs(), VecCreateGhost(), VecCreateMPIWithArray(), VecCreateGhostWithArray(), VecMPISetGhost()

src/vec/vec/impls/mpi/cupm/hip/vecmpicupm.hip.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecCreateMPIHIP(MPI_Comm comm, PetscInt n, PetscInt N, Vec *v)
```

Example 2 (unknown):
```unknown
PETSC_DECIDE
```

Example 3 (unknown):
```unknown
PETSC_DETERMINE
```

Example 4 (unknown):
```unknown
VecDuplicate()
```

---

## VecCreateMPIKokkosWithArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateMPIKokkosWithArray/

**Contents:**
- VecCreateMPIKokkosWithArray#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a parallel, array-style vector, where the user provides the GPU array space to store the vector values.

comm - the MPI communicator to use

bs - block size, same meaning as VecSetBlockSize()

n - local vector length, cannot be PETSC_DECIDE

N - global vector length (or PETSC_DECIDE to have calculated)

darray - the user provided GPU array to store the vector values

Use VecDuplicate() or VecDuplicateVecs() to form additional vectors of the same type as an existing vector.

If the user-provided array is NULL, then VecKokkosPlaceArray() can be used at a later stage to SET the array for storing the vector values.

PETSc does NOT free the array when the vector is destroyed via VecDestroy(). The user should not free the array until the vector is destroyed.

VecCreateSeqKokkosWithArray(), VecCreateMPIWithArray(), VecCreateSeqWithArray(), VecCreate(), VecDuplicate(), VecDuplicateVecs(), VecCreateGhost(), VecCreateMPI(), VecCreateGhostWithArray(), VecPlaceArray()

src/vec/vec/impls/mpi/kokkos/mpikok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode VecCreateMPIKokkosWithArray(MPI_Comm comm, PetscInt bs, PetscInt n, PetscInt N, const PetscScalar darray[], Vec *v)
```

Example 2 (unknown):
```unknown
VecCreateSeqKokkosWithArray()
```

Example 3 (unknown):
```unknown
VecCreateMPIWithArray()
```

Example 4 (unknown):
```unknown
VecCreateSeqWithArray()
```

---

## VecCreateMPIViennaCLWithArrays#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateMPIViennaCLWithArrays/

**Contents:**
- VecCreateMPIViennaCLWithArrays#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a parallel, array-style vector, where the user provides the ViennaCL vector to store the vector values.

comm - the MPI communicator to use

bs - block size, same meaning as VecSetBlockSize()

n - local vector length, cannot be PETSC_DECIDE

N - global vector length (or PETSC_DECIDE to have calculated)

cpuarray - the user provided CPU array to store the vector values

viennaclvec - ViennaCL vector where the Vec entries are to be stored on the device.

If both cpuarray and viennaclvec are provided, the caller must ensure that the provided arrays have identical values.

Use VecDuplicate() or VecDuplicateVecs() to form additional vectors of the same type as an existing vector.

PETSc does NOT free the provided arrays when the vector is destroyed via VecDestroy(). The user should not free the array until the vector is destroyed.

VecCreateSeqViennaCLWithArrays(), VecCreateMPIWithArray(), VecCreate(), VecDuplicate(), VecDuplicateVecs(), VecCreateGhost(), VecCreateMPI(), VecCreateGhostWithArray(), VecViennaCLPlaceArray(), VecPlaceArray(), VecCreateMPICUDAWithArrays(), VecViennaCLAllocateCheckHost()

src/vec/vec/impls/mpi/mpiviennacl/mpiviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecCreateMPIViennaCLWithArrays(MPI_Comm comm, PetscInt bs, PetscInt n, PetscInt N, const PetscScalar cpuarray[], const ViennaCLVector *viennaclvec, Vec *vv) PeNS
```

Example 2 (unknown):
```unknown
VecCreateSeqViennaCLWithArrays()
```

Example 3 (unknown):
```unknown
VecCreateMPIWithArray()
```

Example 4 (unknown):
```unknown
VecCreate()
```

---

## VecCreateMPIViennaCLWithArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateMPIViennaCLWithArray/

**Contents:**
- VecCreateMPIViennaCLWithArray#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a parallel, array-style vector, where the user provides the viennacl vector to store the vector values.

comm - the MPI communicator to use

bs - block size, same meaning as in VecSetBlockSize()

n - local vector length, cannot be PETSC_DECIDE

N - global vector length (or PETSC_DECIDE to have calculated)

array - the user provided GPU array to store the vector values

Use VecDuplicate() or VecDuplicateVecs() to form additional vectors of the same type as an existing vector.

If the user-provided array is NULL, then VecViennaCLPlaceArray() can be used at a later stage to SET the array for storing the vector values.

PETSc does NOT free the array when the vector is destroyed via VecDestroy(). The user should not free the array until the vector is destroyed.

VecCreateSeqViennaCLWithArray(), VecCreateMPIWithArray(), VecCreateSeqWithArray(), VecCreate(), VecCreateMPI(), VecCreateGhostWithArray(), VecViennaCLPlaceArray()

src/vec/vec/impls/mpi/mpiviennacl/mpiviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecCreateMPIViennaCLWithArray(MPI_Comm comm, PetscInt bs, PetscInt n, PetscInt N, const ViennaCLVector *array, Vec *vv) PeNS
```

Example 2 (unknown):
```unknown
VecSetBlockSize()
```

Example 3 (unknown):
```unknown
PETSC_DECIDE
```

Example 4 (unknown):
```unknown
PETSC_DECIDE
```

---

## VecCreateMPIWithArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateMPIWithArray/

**Contents:**
- VecCreateMPIWithArray#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates a parallel, array-style vector, where the user provides the array space to store the vector values.

comm - the MPI communicator to use

bs - block size, same meaning as VecSetBlockSize()

n - local vector length, cannot be PETSC_DECIDE

N - global vector length (or PETSC_DETERMINE to have calculated)

array - the user provided array to store the vector values

Use VecDuplicate() or VecDuplicateVecs() to form additional vectors of the same type as an existing vector.

If the user-provided array is NULL, then VecPlaceArray() can be used at a later stage to SET the array for storing the vector values.

PETSc does NOT free array when the vector is destroyed via VecDestroy().

The user should not free array until the vector is destroyed.

Vectors and Parallel Data, Vec, VecType, VecCreateSeqWithArray(), VecCreate(), VecDuplicate(), VecDuplicateVecs(), VecCreateGhost(), VecCreateMPI(), VecCreateGhostWithArray(), VecPlaceArray()

src/vec/vec/impls/mpi/pbvec.c

src/dm/tutorials/ex22.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecCreateMPIWithArray(MPI_Comm comm, PetscInt bs, PetscInt n, PetscInt N, const PetscScalar array[], Vec *vv)
```

Example 2 (unknown):
```unknown
VecSetBlockSize()
```

Example 3 (unknown):
```unknown
PETSC_DECIDE
```

Example 4 (unknown):
```unknown
PETSC_DETERMINE
```

---

## VecCreateMPI#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateMPI/

**Contents:**
- VecCreateMPI#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates a parallel vector.

comm - the MPI communicator to use

n - local vector length (or PETSC_DECIDE to have calculated if N is given)

N - global vector length (or PETSC_DETERMINE to have calculated if n is given)

It is recommended to use VecCreateFromOptions() instead of this routine

Use VecDuplicate() or VecDuplicateVecs() to form additional vectors of the same type as an existing vector.

If n is not PETSC_DECIDE, then the value determines the PetscLayout of the vector and the ranges returned by VecGetOwnershipRange() and VecGetOwnershipRanges()

Vectors and Parallel Data, Vec, VecType, VecCreateSeq(), VecCreate(), VecDuplicate(), VecDuplicateVecs(), VecCreateGhost(), VecCreateMPIWithArray(), VecCreateGhostWithArray(), VecMPISetGhost(), PetscLayout, VecGetOwnershipRange(), VecGetOwnershipRanges()

src/vec/vec/impls/mpi/vmpicr.c

src/tao/bound/tutorials/plate2f.F90 src/tao/bound/tutorials/plate2.c src/ts/tutorials/ex30.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecCreateMPI(MPI_Comm comm, PetscInt n, PetscInt N, Vec *v)
```

Example 2 (unknown):
```unknown
PETSC_DECIDE
```

Example 3 (unknown):
```unknown
PETSC_DETERMINE
```

Example 4 (unknown):
```unknown
VecCreateFromOptions()
```

---

## VecCreateNest#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateNest/

**Contents:**
- VecCreateNest#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Creates a new vector containing several nested subvectors, each stored separately

comm - Communicator for the new Vec

nb - number of nested blocks

is - array of nb index sets describing each nested block, or NULL to pack subvectors contiguously

x - array of nb sub-vectors

VECNEST, Vectors and Parallel Data, Vec, VecType, VecCreate(), MatCreateNest(), DMSetVecType()

src/vec/vec/impls/nest/vecnest.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecCreateNest(MPI_Comm comm, PetscInt nb, IS is[], Vec x[], Vec *Y)
```

Example 2 (unknown):
```unknown
VecCreate()
```

Example 3 (unknown):
```unknown
MatCreateNest()
```

Example 4 (unknown):
```unknown
DMSetVecType()
```

---

## VecCreateSeqCUDAWithArrays#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateSeqCUDAWithArrays/

**Contents:**
- VecCreateSeqCUDAWithArrays#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a sequential, array-style vector using CUDA, where the user provides the complete array space to store the vector values.

Collective, Possibly Synchronous

comm - the communicator, must be PETSC_COMM_SELF

n - the local vector length

cpuarray - CPU memory where the vector elements are to be stored (or NULL)

gpuarray - GPU memory where the vector elements are to be stored (or NULL)

If the user-provided array is NULL, then VecCUDAPlaceArray() can be used at a later stage to SET the array for storing the vector values. Otherwise, the array must be allocated on the device.

If both cpuarray and gpuarray are provided, the provided arrays must have identical values.

The arrays are NOT freed when the vector is destroyed via VecDestroy(). The user must free them themselves, but not until the vector is destroyed.

This function may initialize PetscDevice, which may incur a device synchronization.

Vectors and Parallel Data, PetscDeviceInitialize(), VecCreate(), VecCreateSeqWithArray(), VecCreateSeqCUDA(), VecCreateSeqCUDAWithArray(), VecCreateMPICUDA(), VecCreateMPICUDAWithArray(), VecCreateMPICUDAWithArrays(), VecCUDAPlaceArray()

src/vec/vec/impls/seq/cupm/cuda/vecseqcupm.cu

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecCreateSeqCUDAWithArrays(MPI_Comm comm, PetscInt bs, PetscInt n, const PetscScalar cpuarray[], const PetscScalar gpuarray[], Vec *v)
```

Example 2 (unknown):
```unknown
PETSC_COMM_SELF
```

Example 3 (unknown):
```unknown
VecCUDAPlaceArray()
```

Example 4 (unknown):
```unknown
VecDestroy()
```

---

## VecCreateSeqCUDAWithArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateSeqCUDAWithArray/

**Contents:**
- VecCreateSeqCUDAWithArray#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a sequential, array-style vector using CUDA, where the user provides the device array space to store the vector values.

Collective, Possibly Synchronous

comm - the communicator, must be PETSC_COMM_SELF

n - the vector length

gpuarray - GPU memory where the vector elements are to be stored (or NULL)

If the user-provided array is NULL, then VecCUDAPlaceArray() can be used at a later stage to SET the array for storing the vector values. Otherwise, the array must be allocated on the device.

The array is NOT freed when the vector is destroyed via VecDestroy(). The user must free the array themselves, but not until the vector is destroyed.

Use VecDuplicate() or VecDuplicateVecs() to form additional vectors of the same type as an existing vector.

This function may initialize PetscDevice, which may incur a device synchronization.

Vectors and Parallel Data, PetscDeviceInitialize(), VecCreate(), VecCreateSeq(), VecCreateSeqWithArray(), VecCreateMPIWithArray(), VecCreateSeqCUDA(), VecCreateMPICUDAWithArray(), VecCUDAPlaceArray(), VecDuplicate(), VecDuplicateVecs(), VecCreateGhost()

src/vec/vec/impls/seq/cupm/cuda/vecseqcupm.cu

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecCreateSeqCUDAWithArray(MPI_Comm comm, PetscInt bs, PetscInt n, const PetscScalar gpuarray[], Vec *v)
```

Example 2 (unknown):
```unknown
PETSC_COMM_SELF
```

Example 3 (unknown):
```unknown
VecCUDAPlaceArray()
```

Example 4 (unknown):
```unknown
VecDestroy()
```

---

## VecCreateSeqCUDA#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateSeqCUDA/

**Contents:**
- VecCreateSeqCUDA#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a standard, sequential, array-style vector.

Collective, Possibly Synchronous

comm - the communicator, must be PETSC_COMM_SELF

n - the vector length

Use VecDuplicate() or VecDuplicateVecs() to form additional vectors of the same type as an existing vector.

This function may initialize PetscDevice, which may incur a device synchronization.

Vectors and Parallel Data, Vec, VECSEQCUDA, PetscDeviceInitialize(), VecCreate(), VecCreateSeq(), VecCreateSeqCUDAWithArray(), VecCreateMPI(), VecCreateMPICUDA(), VecDuplicate(), VecDuplicateVecs(), VecCreateGhost()

src/vec/vec/impls/seq/cupm/cuda/vecseqcupm.cu

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecCreateSeqCUDA(MPI_Comm comm, PetscInt n, Vec *v)
```

Example 2 (unknown):
```unknown
PETSC_COMM_SELF
```

Example 3 (unknown):
```unknown
VecDuplicate()
```

Example 4 (unknown):
```unknown
VecDuplicateVecs()
```

---

## VecCreateSeqHIPWithArrays#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateSeqHIPWithArrays/

**Contents:**
- VecCreateSeqHIPWithArrays#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a sequential, array-style vector using HIP, where the user provides the complete array space to store the vector values.

Collective, Possibly Synchronous

comm - the communicator, must be PETSC_COMM_SELF

n - the local vector length

cpuarray - CPU memory where the vector elements are to be stored (or NULL)

gpuarray - GPU memory where the vector elements are to be stored (or NULL)

If the user-provided array is NULL, then VecHIPPlaceArray() can be used at a later stage to SET the array for storing the vector values. Otherwise, the array must be allocated on the device.

If both cpuarray and gpuarray are provided, the provided arrays must have identical values.

The arrays are NOT freed when the vector is destroyed via VecDestroy(). The user must free them themselves, but not until the vector is destroyed.

This function may initialize PetscDevice, which may incur a device synchronization.

Vectors and Parallel Data, PetscDeviceInitialize(), VecCreate(), VecCreateSeqWithArray(), VecCreateSeqHIP(), VecCreateSeqHIPWithArray(), VecCreateMPIHIP(), VecCreateMPIHIPWithArray(), VecCreateMPIHIPWithArrays(), VecHIPPlaceArray()

src/vec/vec/impls/seq/cupm/hip/vecseqcupm.hip.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecCreateSeqHIPWithArrays(MPI_Comm comm, PetscInt bs, PetscInt n, const PetscScalar cpuarray[], const PetscScalar gpuarray[], Vec *v)
```

Example 2 (unknown):
```unknown
PETSC_COMM_SELF
```

Example 3 (unknown):
```unknown
VecHIPPlaceArray()
```

Example 4 (unknown):
```unknown
VecDestroy()
```

---

## VecCreateSeqHIPWithArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateSeqHIPWithArray/

**Contents:**
- VecCreateSeqHIPWithArray#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a sequential, array-style vector using HIP, where the user provides the device array space to store the vector values.

Collective, Possibly Synchronous

comm - the communicator, must be PETSC_COMM_SELF

n - the vector length

gpuarray - GPU memory where the vector elements are to be stored (or NULL)

If the user-provided array is NULL, then VecHIPPlaceArray() can be used at a later stage to SET the array for storing the vector values. Otherwise, the array must be allocated on the device.

The array is NOT freed when the vector is destroyed via VecDestroy(). The user must free the array themselves, but not until the vector is destroyed.

Use VecDuplicate() or VecDuplicateVecs() to form additional vectors of the same type as an existing vector.

This function may initialize PetscDevice, which may incur a device synchronization.

Vectors and Parallel Data, PetscDeviceInitialize(), VecCreate(), VecCreateSeq(), VecCreateSeqWithArray(), VecCreateMPIWithArray(), VecCreateSeqHIP(), VecCreateMPIHIPWithArray(), VecHIPPlaceArray(), VecDuplicate(), VecDuplicateVecs(), VecCreateGhost()

src/vec/vec/impls/seq/cupm/hip/vecseqcupm.hip.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecCreateSeqHIPWithArray(MPI_Comm comm, PetscInt bs, PetscInt n, const PetscScalar gpuarray[], Vec *v)
```

Example 2 (unknown):
```unknown
PETSC_COMM_SELF
```

Example 3 (unknown):
```unknown
VecHIPPlaceArray()
```

Example 4 (unknown):
```unknown
VecDestroy()
```

---

## VecCreateSeqHIP#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateSeqHIP/

**Contents:**
- VecCreateSeqHIP#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a standard, sequential, array-style vector.

Collective, Possibly Synchronous

comm - the communicator, must be PETSC_COMM_SELF

n - the vector length

Use VecDuplicate() or VecDuplicateVecs() to form additional vectors of the same type as an existing vector.

This function may initialize PetscDevice, which may incur a device synchronization.

Vectors and Parallel Data, PetscDeviceInitialize(), VecCreate(), VecCreateSeq(), VecCreateSeqHIPWithArray(), VecCreateMPI(), VecCreateMPIHIP(), VecDuplicate(), VecDuplicateVecs(), VecCreateGhost()

src/vec/vec/impls/seq/cupm/hip/vecseqcupm.hip.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecCreateSeqHIP(MPI_Comm comm, PetscInt n, Vec *v)
```

Example 2 (unknown):
```unknown
PETSC_COMM_SELF
```

Example 3 (unknown):
```unknown
VecDuplicate()
```

Example 4 (unknown):
```unknown
VecDuplicateVecs()
```

---

## VecCreateSeqKokkosWithArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateSeqKokkosWithArray/

**Contents:**
- VecCreateSeqKokkosWithArray#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a Kokkos sequential array-style vector, where the user provides the array space to store the vector values. The array provided must be a device array.

comm - the communicator, should be PETSC_COMM_SELF

n - the vector length

darray - device memory where the vector elements are to be stored.

Use VecDuplicate() or VecDuplicateVecs() to form additional vectors of the same type as an existing vector.

PETSc does NOT free the array when the vector is destroyed via VecDestroy(). The user should not free the array until the vector is destroyed.

VecCreateMPICUDAWithArray(), VecCreate(), VecDuplicate(), VecDuplicateVecs(), VecCreateGhost(), VecCreateSeq(), VecCreateSeqWithArray(), VecCreateMPIWithArray()

src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode VecCreateSeqKokkosWithArray(MPI_Comm comm, PetscInt bs, PetscInt n, const PetscScalar darray[], Vec *v)
```

Example 2 (unknown):
```unknown
VecCreateMPICUDAWithArray()
```

Example 3 (unknown):
```unknown
VecCreate()
```

Example 4 (unknown):
```unknown
VecDuplicate()
```

---

## VecCreateSeqKokkos#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateSeqKokkos/

**Contents:**
- VecCreateSeqKokkos#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a standard, sequential array-style vector.

comm - the communicator, should be PETSC_COMM_SELF

n - the vector length

Use VecDuplicate() or VecDuplicateVecs() to form additional vectors of the same type as an existing vector.

VecCreateMPI(), VecCreate(), VecDuplicate(), VecDuplicateVecs(), VecCreateGhost()

src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode VecCreateSeqKokkos(MPI_Comm comm, PetscInt n, Vec *v)
```

Example 2 (unknown):
```unknown
PETSC_COMM_SELF
```

Example 3 (unknown):
```unknown
VecCreateMPI()
```

Example 4 (unknown):
```unknown
VecCreate()
```

---

## VecCreateSeqViennaCLWithArrays#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateSeqViennaCLWithArrays/

**Contents:**
- VecCreateSeqViennaCLWithArrays#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a ViennaCL sequential vector, where the user provides the array space to store the vector values.

comm - the communicator, should be PETSC_COMM_SELF

n - the vector length

cpuarray - CPU memory where the vector elements are to be stored.

viennaclvec - ViennaCL vector where the Vec entries are to be stored on the device.

If both cpuarray and viennaclvec are provided, the caller must ensure that the provided arrays have identical values.

PETSc does NOT free the provided arrays when the vector is destroyed via VecDestroy(). The user should not free the array until the vector is destroyed.

VecCreateMPIViennaCLWithArrays(), VecCreate(), VecCreateSeqWithArray(), VecViennaCLPlaceArray(), VecPlaceArray(), VecCreateSeqCUDAWithArrays(), VecViennaCLAllocateCheckHost()

src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecCreateSeqViennaCLWithArrays(MPI_Comm comm, PetscInt bs, PetscInt n, const PetscScalar cpuarray[], const ViennaCLVector *viennaclvec, Vec *V) PeNS
```

Example 2 (unknown):
```unknown
VecCreateMPIViennaCLWithArrays()
```

Example 3 (unknown):
```unknown
VecCreate()
```

Example 4 (unknown):
```unknown
VecCreateSeqWithArray()
```

---

## VecCreateSeqViennaCLWithArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateSeqViennaCLWithArray/

**Contents:**
- VecCreateSeqViennaCLWithArray#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a viennacl sequential array-style vector, where the user provides the array space to store the vector values.

comm - the communicator, should be PETSC_COMM_SELF

n - the vector length

array - viennacl array where the vector elements are to be stored.

Use VecDuplicate() or VecDuplicateVecs() to form additional vectors of the same type as an existing vector.

If the user-provided array is NULL, then VecViennaCLPlaceArray() can be used at a later stage to SET the array for storing the vector values.

PETSc does NOT free the array when the vector is destroyed via VecDestroy(). The user should not free the array until the vector is destroyed.

VecCreateMPIViennaCLWithArray(), VecCreate(), VecDuplicate(), VecDuplicateVecs(), VecCreateGhost(), VecCreateSeq(), VecCUDAPlaceArray(), VecCreateSeqWithArray(), VecCreateMPIWithArray()

src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PETSC_EXTERN PetscErrorCode VecCreateSeqViennaCLWithArray(MPI_Comm comm, PetscInt bs, PetscInt n, const ViennaCLVector *array, Vec *V) PeNS
```

Example 2 (unknown):
```unknown
VecCreateMPIViennaCLWithArray()
```

Example 3 (unknown):
```unknown
VecCreate()
```

Example 4 (unknown):
```unknown
VecDuplicate()
```

---

## VecCreateSeqViennaCL#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateSeqViennaCL/

**Contents:**
- VecCreateSeqViennaCL#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a standard, sequential array-style vector.

comm - the communicator, should be PETSC_COMM_SELF

n - the vector length

Use VecDuplicate() or VecDuplicateVecs() to form additional vectors of the same type as an existing vector.

VecCreateMPI(), VecCreate(), VecDuplicate(), VecDuplicateVecs(), VecCreateGhost()

src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecCreateSeqViennaCL(MPI_Comm comm, PetscInt n, Vec *v)
```

Example 2 (unknown):
```unknown
VecCreateMPI()
```

Example 3 (unknown):
```unknown
VecCreate()
```

Example 4 (unknown):
```unknown
VecDuplicate()
```

---

## VecCreateSeqWithArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateSeqWithArray/

**Contents:**
- VecCreateSeqWithArray#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates a standard,sequential array-style vector, where the user provides the array space to store the vector values.

comm - the communicator, should be PETSC_COMM_SELF

n - the vector length

array - memory where the vector elements are to be stored.

Use VecDuplicate() or VecDuplicateVecs() to form additional vectors of the same type as an existing vector.

If the user-provided array is NULL, then VecPlaceArray() can be used at a later stage to SET the array for storing the vector values.

PETSc does NOT free the array when the vector is destroyed via VecDestroy(). The user should not free the array until the vector is destroyed.

VecCreateMPIWithArray(), VecCreate(), VecDuplicate(), VecDuplicateVecs(), VecCreateGhost(), VecCreateSeq(), VecPlaceArray()

src/vec/vec/impls/seq/bvec2.c

src/ksp/ksp/tutorials/ex83f.F90 src/ksp/ksp/tutorials/ex13f90.F90 src/mat/tutorials/ex2.c src/ksp/ksp/tutorials/ex61f.F90 src/ksp/ksp/tutorials/ex13.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecCreateSeqWithArray(MPI_Comm comm, PetscInt bs, PetscInt n, const PetscScalar array[], Vec *V)
```

Example 2 (unknown):
```unknown
PETSC_COMM_SELF
```

Example 3 (unknown):
```unknown
VecDuplicate()
```

Example 4 (unknown):
```unknown
VecDuplicateVecs(
```

---

## VecCreateSeq#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateSeq/

**Contents:**
- VecCreateSeq#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates a standard, sequential array-style vector.

comm - the communicator, should be PETSC_COMM_SELF

n - the vector length

It is recommended to use VecCreateFromOptions() instead of this routine

Use VecDuplicate() or VecDuplicateVecs() to form additional vectors of the same type as an existing vector.

Vectors and Parallel Data, Vec, VecType, VecCreateMPI(), VecCreate(), VecDuplicate(), VecDuplicateVecs(), VecCreateGhost()

src/vec/vec/impls/seq/vseqcr.c

src/tao/leastsquares/tutorials/chwirut1f.F90 src/snes/tutorials/ex1f.F90 src/ksp/ksp/tutorials/ex89f.F90 src/ksp/pc/tutorials/ex2.c src/vec/vec/tutorials/ex4f.F90 src/ksp/ksp/tutorials/ex43.c src/ksp/ksp/tutorials/ex88f.F90 src/vec/vec/tutorials/ex4f90.F90 src/ksp/pc/tutorials/ex1.c src/tao/leastsquares/tutorials/chwirut1.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecCreateSeq(MPI_Comm comm, PetscInt n, Vec *v)
```

Example 2 (unknown):
```unknown
PETSC_COMM_SELF
```

Example 3 (unknown):
```unknown
VecCreateFromOptions()
```

Example 4 (unknown):
```unknown
VecDuplicate()
```

---

## VecCreateShared#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreateShared/

**Contents:**
- VecCreateShared#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a parallel vector that uses shared memory.

comm - the MPI communicator to use

n - local vector length (or PETSC_DECIDE to have calculated if N is given)

N - global vector length (or PETSC_DECIDE to have calculated if n is given)

Currently VecCreateShared() is available only on the SGI; otherwise, this routine is the same as VecCreateMPI().

Use VecDuplicate() or VecDuplicateVecs() to form additional vectors of the same type as an existing vector.

Vectors and Parallel Data, Vec, VecType, VecCreateSeq(), VecCreate(), VecCreateMPI(), VecDuplicate(), VecDuplicateVecs(), VecCreateGhost(), VecCreateMPIWithArray(), VecCreateGhostWithArray()

src/vec/vec/impls/shared/shvec.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecCreateShared(MPI_Comm comm, PetscInt n, PetscInt N, Vec *v)
```

Example 2 (unknown):
```unknown
PETSC_DECIDE
```

Example 3 (unknown):
```unknown
PETSC_DECIDE
```

Example 4 (unknown):
```unknown
VecCreateShared()
```

---

## VecCreate#

**URL:** https://petsc.org/release/manualpages/Vec/VecCreate/

**Contents:**
- VecCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Creates an empty vector object. The type can then be set with VecSetType(), or VecSetFromOptions().

comm - The communicator for the vector object

vec - The vector object

If you never call VecSetType() or VecSetFromOptions() it will generate an error when you try to use the vector.

PETSc Vec always have all zero entries until routines such as VecSet() or VecSetValues() are used to change the values. There is no reason to call VecZeroEntries() after creation.

Vectors and Parallel Data, Vec, VecSetType(), VecSetSizes(), VecCreateMPIWithArray(), VecCreateMPI(), VecDuplicate(), VecDuplicateVecs(), VecCreateGhost(), VecCreateSeq(), VecPlaceArray()

src/vec/vec/interface/veccreate.c

src/snes/tutorials/ex99.c src/snes/tutorials/ex59.c src/snes/tutorials/ex1.c src/snes/tutorials/ex6.c src/snes/tutorials/ex73f90t.F90 src/mat/tutorials/ex19.c src/snes/tutorials/ex70.c src/mat/tutorials/ex12.c src/mat/tutorials/ex7.c src/snes/tutorials/ex7.c

VecCreate_CUDA() in src/vec/vec/impls/mpi/cupm/cuda/vecmpicupm.cu VecCreate_MPICUDA() in src/vec/vec/impls/mpi/cupm/cuda/vecmpicupm.cu VecCreate_HIP() in src/vec/vec/impls/mpi/cupm/hip/vecmpicupm.hip.cxx VecCreate_MPIHIP() in src/vec/vec/impls/mpi/cupm/hip/vecmpicupm.hip.cxx VecCreate_MPIKokkos() in src/vec/vec/impls/mpi/kokkos/mpikok.kokkos.cxx VecCreate_Kokkos() in src/vec/vec/impls/mpi/kokkos/mpikok.kokkos.cxx VecCreate_MPIViennaCL() in src/vec/vec/impls/mpi/mpiviennacl/mpiviennacl.cxx VecCreate_ViennaCL() in src/vec/vec/impls/mpi/mpiviennacl/mpiviennacl.cxx VecCreate_MPI() in src/vec/vec/impls/mpi/pbvec.c VecCreate_Standard() in src/vec/vec/impls/mpi/pbvec.c VecCreate_Seq() in src/vec/vec/impls/seq/bvec3.c VecCreate_SeqCUDA() in src/vec/vec/impls/seq/cupm/cuda/vecseqcupm.cu VecCreate_SeqHIP() in src/vec/vec/impls/seq/cupm/hip/vecseqcupm.hip.cxx VecCreate_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecCreate_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx VecCreate_Shared() in src/vec/vec/impls/shared/shvec.c VecCreate_Shared() in src/vec/vec/impls/shared/shvec.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecSetType()
```

Example 2 (unknown):
```unknown
VecSetFromOptions().
```

Example 3 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecCreate(MPI_Comm comm, Vec *vec)
```

Example 4 (unknown):
```unknown
VecSetType()
```

---

## VecCUDAGetArrayRead#

**URL:** https://petsc.org/release/manualpages/Vec/VecCUDAGetArrayRead/

**Contents:**
- VecCUDAGetArrayRead#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Provides read access to the CUDA buffer inside a vector.

Not Collective; Asynchronous; No Fortran Support

a - the CUDA pointer.

See VecCUDAGetArray() for data movement semantics of this function.

This function assumes that the user will not modify the vector data. This is analgogous to intent(in) in Fortran.

The device pointer must be restored by calling VecCUDARestoreArrayRead(). If the data on the host side was previously up to date it will remain so, i.e. data on both the device and the host is up to date. Accessing data on the host side does not incur a device to host data transfer.

Vectors and Parallel Data, VecCUDARestoreArrayRead(), VecCUDAGetArray(), VecCUDAGetArrayWrite(), VecGetArray(), VecGetArrayRead()

src/vec/vec/impls/seq/cupm/cuda/vecseqcupm.cu

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecCUDAGetArrayRead(Vec v, const PetscScalar **a)
```

Example 2 (unknown):
```unknown
VecCUDAGetArray()
```

Example 3 (unknown):
```unknown
VecCUDARestoreArrayRead()
```

Example 4 (unknown):
```unknown
VecCUDARestoreArrayRead()
```

---

## VecCUDAGetArrayWrite#

**URL:** https://petsc.org/release/manualpages/Vec/VecCUDAGetArrayWrite/

**Contents:**
- VecCUDAGetArrayWrite#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Provides write access to the CUDA buffer inside a vector.

Logically Collective; Asynchronous; No Fortran Support

The data pointed to by the device pointer is uninitialized. The user may not read from this data. Furthermore, the entire array needs to be filled by the user to obtain well-defined behaviour. The device memory will be allocated by this function if it hasn’t been allocated previously. This is analogous to intent(out) in Fortran.

The device pointer needs to be released with VecCUDARestoreArrayWrite(). When the pointer is released the host data of the vector is marked as out of data. Subsequent access of the host data with e.g. VecGetArray() incurs a device to host data transfer.

Vectors and Parallel Data, VecCUDARestoreArrayWrite(), VecCUDAGetArray(), VecCUDAGetArrayRead(), VecCUDAGetArrayWrite(), VecGetArray(), VecGetArrayRead()

src/vec/vec/impls/seq/cupm/cuda/vecseqcupm.cu

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecCUDAGetArrayWrite(Vec v, PetscScalar **a)
```

Example 2 (unknown):
```unknown
VecCUDARestoreArrayWrite()
```

Example 3 (unknown):
```unknown
VecCUDARestoreArrayWrite()
```

Example 4 (unknown):
```unknown
VecCUDAGetArray()
```

---

## VecCUDAGetArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecCUDAGetArray/

**Contents:**
- VecCUDAGetArray#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#

Provides access to the device buffer inside a vector

Logically Collective; Asynchronous; No Fortran Support

a - the device buffer

This routine has semantics similar to VecGetArray(); the returned buffer points to a consistent view of the vector data. This may involve copying data from the host to the device if the data on the device is out of date. It is also assumed that the returned buffer is immediately modified, marking the host data out of date. This is similar to intent(inout) in Fortran.

If the user does require strong memory guarantees, they are encouraged to use VecCUDAGetArrayRead() and/or VecCUDAGetArrayWrite() instead.

The user must call VecCUDARestoreArray() when they are finished using the array.

If the device memory hasn’t been allocated previously it will be allocated as part of this routine.

Vectors and Parallel Data, VecCUDARestoreArray(), VecCUDAGetArrayRead(), VecCUDAGetArrayWrite(), VecGetArray(), VecGetArrayRead(), VecGetArrayWrite()

src/vec/vec/impls/seq/cupm/cuda/vecseqcupm.cu

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecCUDAGetArray(Vec v, PetscScalar **a)
```

Example 2 (unknown):
```unknown
VecGetArray()
```

Example 3 (unknown):
```unknown
VecCUDAGetArrayRead()
```

Example 4 (unknown):
```unknown
VecCUDAGetArrayWrite()
```

---

## VecCUDAPlaceArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecCUDAPlaceArray/

**Contents:**
- VecCUDAPlaceArray#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Allows one to replace the GPU array in a vector with a GPU array provided by the user.

Logically Collective; Asynchronous; No Fortran Support

array - the GPU array

Adding const to array was an oversight, see notes in VecPlaceArray().

This routine is useful to avoid copying an array into a vector, though you can return to the original GPU array with a call to VecCUDAResetArray().

It is not possible to use VecCUDAPlaceArray() and VecPlaceArray() at the same time on the same vector.

vec does not take ownership of array in any way. The user must free array themselves but be careful not to do so before the vector has either been destroyed, had its original array restored with VecCUDAResetArray() or permanently replaced with VecCUDAReplaceArray().

Vectors and Parallel Data, VecPlaceArray(), VecGetArray(), VecRestoreArray(), VecReplaceArray(), VecResetArray(), VecCUDAResetArray(), VecCUDAReplaceArray()

src/vec/vec/impls/seq/cupm/cuda/vecseqcupm.cu

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecCUDAPlaceArray(Vec vin, const PetscScalar array[])
```

Example 2 (unknown):
```unknown
VecPlaceArray()
```

Example 3 (unknown):
```unknown
VecCUDAResetArray()
```

Example 4 (unknown):
```unknown
VecCUDAPlaceArray()
```

---

## VecCUDAReplaceArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecCUDAReplaceArray/

**Contents:**
- VecCUDAReplaceArray#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Permanently replace the GPU array in a vector with a GPU array provided by the user.

Logically Collective; No Fortran Support

array - the GPU array

Adding const to array was an oversight, see notes in VecPlaceArray().

This is useful to avoid copying a GPU array into a vector.

This frees the memory associated with the old GPU array. The vector takes ownership of the passed array so it CANNOT be freed by the user. It will be freed when the vector is destroyed.

Vectors and Parallel Data, VecGetArray(), VecRestoreArray(), VecPlaceArray(), VecResetArray(), VecCUDAResetArray(), VecCUDAPlaceArray(), VecReplaceArray()

src/vec/vec/impls/seq/cupm/cuda/vecseqcupm.cu

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecCUDAReplaceArray(Vec vin, const PetscScalar array[])
```

Example 2 (unknown):
```unknown
VecPlaceArray()
```

Example 3 (unknown):
```unknown
VecGetArray()
```

Example 4 (unknown):
```unknown
VecRestoreArray()
```

---

## VecCUDAResetArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecCUDAResetArray/

**Contents:**
- VecCUDAResetArray#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Resets a vector to use its default memory.

Logically Collective; No Fortran Support

Call this after the use of VecCUDAPlaceArray().

Vectors and Parallel Data, VecGetArray(), VecRestoreArray(), VecReplaceArray(), VecPlaceArray(), VecResetArray(), VecCUDAPlaceArray(), VecCUDAReplaceArray()

src/vec/vec/impls/seq/cupm/cuda/vecseqcupm.cu

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecCUDAResetArray(Vec vin)
```

Example 2 (unknown):
```unknown
VecCUDAPlaceArray()
```

Example 3 (unknown):
```unknown
VecGetArray()
```

Example 4 (unknown):
```unknown
VecRestoreArray()
```

---

## VecCUDARestoreArrayRead#

**URL:** https://petsc.org/release/manualpages/Vec/VecCUDARestoreArrayRead/

**Contents:**
- VecCUDARestoreArrayRead#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Restore a CUDA device pointer previously acquired with VecCUDAGetArrayRead().

Not Collective; Asynchronous; No Fortran Support

a - the CUDA device pointer

This routine does not modify the corresponding array on the host in any way. The pointer is invalid after this function returns.

Vectors and Parallel Data, VecCUDAGetArrayRead(), VecCUDAGetArrayWrite(), VecCUDAGetArray(), VecGetArray(), VecRestoreArray(), VecGetArrayRead()

src/vec/vec/impls/seq/cupm/cuda/vecseqcupm.cu

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecCUDAGetArrayRead()
```

Example 2 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecCUDARestoreArrayRead(Vec v, const PetscScalar **a)
```

Example 3 (unknown):
```unknown
VecCUDAGetArrayRead()
```

Example 4 (unknown):
```unknown
VecCUDAGetArrayWrite()
```

---

## VecCUDARestoreArrayWrite#

**URL:** https://petsc.org/release/manualpages/Vec/VecCUDARestoreArrayWrite/

**Contents:**
- VecCUDARestoreArrayWrite#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Restore a CUDA device pointer previously acquired with VecCUDAGetArrayWrite().

Logically Collective; Asynchronous; No Fortran Support

a - the CUDA device pointer. This pointer is invalid after VecCUDARestoreArrayWrite() returns.

Data on the host will be marked as out of date. Subsequent access of the data on the host side e.g. with VecGetArray() will incur a device to host data transfer.

Vectors and Parallel Data, VecCUDAGetArrayWrite(), VecCUDAGetArray(), VecCUDAGetArrayRead(), VecCUDAGetArrayWrite(), VecGetArray(), VecRestoreArray(), VecGetArrayRead()

src/vec/vec/impls/seq/cupm/cuda/vecseqcupm.cu

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecCUDAGetArrayWrite()
```

Example 2 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecCUDARestoreArrayWrite(Vec v, PetscScalar **a)
```

Example 3 (unknown):
```unknown
VecCUDARestoreArrayWrite()
```

Example 4 (unknown):
```unknown
VecGetArray()
```

---

## VecCUDARestoreArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecCUDARestoreArray/

**Contents:**
- VecCUDARestoreArray#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Restore a device buffer previously acquired with VecCUDAGetArray().

NotCollective; Asynchronous; No Fortran Support

a - the device buffer

The restored pointer is invalid after this function returns. This function also marks the host data as out of date. Subsequent access to the vector data on the host side via VecGetArray() will incur a (synchronous) data transfer.

Vectors and Parallel Data, VecCUDAGetArray(), VecCUDAGetArrayRead(), VecCUDAGetArrayWrite(), VecGetArray(), VecRestoreArray(), VecGetArrayRead()

src/vec/vec/impls/seq/cupm/cuda/vecseqcupm.cu

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecCUDAGetArray()
```

Example 2 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecCUDARestoreArray(Vec v, PetscScalar **a)
```

Example 3 (unknown):
```unknown
VecGetArray()
```

Example 4 (unknown):
```unknown
VecCUDAGetArray()
```

---

## VECCUDA#

**URL:** https://petsc.org/release/manualpages/Vec/VECCUDA/

**Contents:**
- VECCUDA#
- Options Database Keys#
- See Also#
- Level#
- Location#

VECCUDA = “cuda” - A VECSEQCUDA on a single-process MPI communicator, and VECMPICUDA otherwise.

-vec_type cuda - sets the vector type to VECCUDA during a call to VecSetFromOptions()

VecCreate(), VecSetType(), VecSetFromOptions(), VecCreateMPIWithArray(), VECSEQCUDA, VECMPICUDA, VECSTANDARD, VecType, VecCreateMPI(), VecSetPinnedMemoryMin(), VECHIP

src/vec/vec/impls/mpi/cupm/cuda/vecmpicupm.cu

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecSetFromOptions()
```

Example 2 (unknown):
```unknown
VecCreate()
```

Example 3 (unknown):
```unknown
VecSetType()
```

Example 4 (unknown):
```unknown
VecSetFromOptions()
```

---

## VecDestroyVecs#

**URL:** https://petsc.org/release/manualpages/Vec/VecDestroyVecs/

**Contents:**
- VecDestroyVecs#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Frees a block of vectors obtained with VecDuplicateVecs().

m - the number of vectors previously obtained, if zero no vectors are destroyed

vv - pointer to pointer to array of vector pointers, if NULL no vectors are destroyed

Vectors and Parallel Data, Vec, PETSc for Fortran Users, VecDuplicateVecs(), VecDestroyVecsf90()

src/vec/vec/interface/vector.c

src/tao/pde_constrained/tutorials/hyperbolic.c src/vec/vec/tutorials/ex1.c src/tao/pde_constrained/tutorials/parabolic.c src/ksp/ksp/tutorials/ex49.c src/vec/vec/tutorials/ex1f90.F90 src/vec/vec/tutorials/ex19.c src/vec/vec/tutorials/ex20f90.F90

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecDuplicateVecs()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecDestroyVecs(PetscInt m, Vec *vv[])
```

Example 3 (unknown):
```unknown
VecDuplicateVecs()
```

Example 4 (unknown):
```unknown
VecDestroyVecsf90()
```

---

## VecDestroy#

**URL:** https://petsc.org/release/manualpages/Vec/VecDestroy/

**Contents:**
- VecDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Vectors and Parallel Data, Vec, VecCreate(), VecDuplicate(), VecDestroyVecs()

src/vec/vec/interface/vector.c

src/mat/tutorials/ex3.c src/snes/tutorials/ex99.c src/snes/tutorials/ex1.c src/mat/tutorials/ex9.c src/mat/tutorials/ex19.c src/snes/tutorials/ex40f90.F90 src/snes/tutorials/ex35.c src/mat/tutorials/ex2.c src/mat/tutorials/ex12.c src/mat/tutorials/ex7.c

VecDestroy_MPIFFTW() in src/mat/impls/fft/fftw/fftw.c VecDestroy_MPIKokkos() in src/vec/vec/impls/mpi/kokkos/mpikok.kokkos.cxx VecDestroy_MPIViennaCL() in src/vec/vec/impls/mpi/mpiviennacl/mpiviennacl.cxx VecDestroy_MPI() in src/vec/vec/impls/mpi/pdvec.c VecDestroy_Nest() in src/vec/vec/impls/nest/vecnest.c VecDestroy_Seq() in src/vec/vec/impls/seq/bvec2.c VecDestroy_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecDestroy_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecDestroy(Vec *v)
```

Example 2 (unknown):
```unknown
VecCreate()
```

Example 3 (unknown):
```unknown
VecDuplicate()
```

Example 4 (unknown):
```unknown
VecDestroyVecs()
```

---

## VecDotBegin#

**URL:** https://petsc.org/release/manualpages/Vec/VecDotBegin/

**Contents:**
- VecDotBegin#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Starts a split phase dot product computation.

y - the second vector

result - where the result will go (can be NULL)

Each call to VecDotBegin() should be paired with a call to VecDotEnd().

VecDotEnd(), VecNormBegin(), VecNormEnd(), VecNorm(), VecDot(), VecMDot(), VecTDotBegin(), VecTDotEnd(), PetscCommSplitReductionBegin()

src/vec/vec/utils/comb.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"    
PetscErrorCode VecDotBegin(Vec x, Vec y, PetscScalar *result)
```

Example 2 (unknown):
```unknown
VecDotBegin()
```

Example 3 (unknown):
```unknown
VecDotEnd()
```

Example 4 (unknown):
```unknown
VecDotEnd()
```

---

## VecDotEnd#

**URL:** https://petsc.org/release/manualpages/Vec/VecDotEnd/

**Contents:**
- VecDotEnd#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Ends a split phase dot product computation.

x - the first vector (can be NULL)

y - the second vector (can be NULL)

result - where the result will go

Each call to VecDotBegin() should be paired with a call to VecDotEnd().

VecDotBegin(), VecNormBegin(), VecNormEnd(), VecNorm(), VecDot(), VecMDot(), VecTDotBegin(), VecTDotEnd(), PetscCommSplitReductionBegin()

src/vec/vec/utils/comb.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"    
PetscErrorCode VecDotEnd(Vec x, Vec y, PetscScalar *result)
```

Example 2 (unknown):
```unknown
VecDotBegin()
```

Example 3 (unknown):
```unknown
VecDotEnd()
```

Example 4 (unknown):
```unknown
VecDotBegin()
```

---

## VecDotNorm2#

**URL:** https://petsc.org/release/manualpages/Vec/VecDotNorm2/

**Contents:**
- VecDotNorm2#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

computes the inner product of two vectors and the 2-norm squared of the second vector

conj(x) is the complex conjugate of x when x is complex

Vec, VecDot(), VecNorm(), VecDotBegin(), VecNormBegin(), VecDotEnd(), VecNormEnd()

src/vec/vec/utils/vinv.c

VecDotNorm2_MPIKokkos() in src/vec/vec/impls/mpi/kokkos/mpikok.kokkos.cxx VecDotNorm2_MPIViennaCL() in src/vec/vec/impls/mpi/mpiviennacl/mpiviennacl.cxx VecDotNorm2_Nest() in src/vec/vec/impls/nest/vecnest.c VecDotNorm2_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecDotNorm2_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecDotNorm2(Vec s, Vec t, PetscScalar *dp, PetscReal *nm)
```

Example 2 (unknown):
```unknown
VecDotBegin()
```

Example 3 (unknown):
```unknown
VecNormBegin()
```

Example 4 (unknown):
```unknown
VecDotEnd()
```

---

## VecDotRealPart#

**URL:** https://petsc.org/release/manualpages/Vec/VecDotRealPart/

**Contents:**
- VecDotRealPart#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes for Users of Complex Numbers#
- Developer Notes#
- See Also#
- Level#
- Location#

Computes the real part of the vector dot product.

val - the real part of the dot product;

See VecDot() for more details on the definition of the dot product for complex numbers

For real numbers this returns the same value as VecDot()

For complex numbers in C^n (that is a vector of n components with a complex number for each component) this is equal to the usual real dot product on the the space R^{2n} (that is a vector of 2n components with the real or imaginary part of the complex numbers for components)

This is not currently optimized to compute only the real part of the dot product.

Vectors and Parallel Data, Vec, VecMDot(), VecTDot(), VecNorm(), VecDotBegin(), VecDotEnd(), VecDot(), VecDotNorm2()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecDotRealPart(Vec x, Vec y, PetscReal *val)
```

Example 2 (unknown):
```unknown
VecDotBegin()
```

Example 3 (unknown):
```unknown
VecDotEnd()
```

Example 4 (unknown):
```unknown
VecDotNorm2()
```

---

## VecDot#

**URL:** https://petsc.org/release/manualpages/Vec/VecDot/

**Contents:**
- VecDot#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Computes the vector dot product.

val - the dot product

For complex vectors, VecDot() computes

where \(y^H\) denotes the conjugate transpose of y. Note that this corresponds to the usual “mathematicians” complex inner product where the SECOND argument gets the complex conjugate. Since the BLASdot() complex conjugates the first first argument we call the BLASdot() with the arguments reversed.

Use VecTDot() for the indefinite form

where \(y^T\) denotes the transpose of y.

Vectors and Parallel Data, Vec, VecMDot(), VecTDot(), VecNorm(), VecDotBegin(), VecDotEnd(), VecDotRealPart()

src/vec/vec/interface/rvector.c

src/vec/vec/tutorials/ex18f.F90 src/vec/vec/tutorials/ex1.c src/ksp/ksp/tutorials/ex49.c src/vec/vec/tutorials/performance.c src/vec/vec/tutorials/ex1f90.F90 src/snes/tutorials/ex15.c src/snes/tutorials/ex69.c src/tao/constrained/tutorials/maros.c src/vec/vec/tutorials/ex18.c src/vec/vec/tutorials/ex20f90.F90

VecDot_MPIKokkos() in src/vec/vec/impls/mpi/kokkos/mpikok.kokkos.cxx VecDot_MPIViennaCL() in src/vec/vec/impls/mpi/mpiviennacl/mpiviennacl.cxx VecDot_MPI() in src/vec/vec/impls/mpi/pvec2.c VecDot_Nest() in src/vec/vec/impls/nest/vecnest.c VecDot_Seq() in src/vec/vec/impls/seq/bvec1.c VecDot_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecDot_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecDot(Vec x, Vec y, PetscScalar *val)
```

Example 2 (unknown):
```unknown
val = (x,y) = y^H x,
```

Example 3 (unknown):
```unknown
val = (x,y) = y^T x,
```

Example 4 (unknown):
```unknown
VecDotBegin()
```

---

## VecDuplicateVecs#

**URL:** https://petsc.org/release/manualpages/Vec/VecDuplicateVecs/

**Contents:**
- VecDuplicateVecs#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Creates several vectors of the same type as an existing vector.

m - the number of vectors to obtain

v - a vector to mimic

V - location to put pointer to array of vectors

Use VecDestroyVecs() to free the space. Use VecDuplicate() to form a single vector.

PETSc Vec always have all zero entries when created with VecDuplicateVecs() until routines such as VecSet() or VecSetValues() are used to change the values. There is no reason to call VecZeroEntries() after creation.

Some implementations ensure that the arrays accessed by each vector are contiguous in memory. Certain VecMDot() and VecMAXPY() implementations utilize this property to use BLAS 2 operations for higher efficiency. This is especially useful in KSPGMRES, see KSPGMRESSetPreAllocateVectors().

Vectors and Parallel Data, Vec, PETSc for Fortran Users, VecDestroyVecs(), VecDuplicate(), VecCreate(), VecMDot(), VecMAXPY(), KSPGMRES, KSPGMRESSetPreAllocateVectors()

src/vec/vec/interface/vector.c

src/tao/pde_constrained/tutorials/hyperbolic.c src/vec/vec/tutorials/ex1.c src/tao/pde_constrained/tutorials/parabolic.c src/ksp/ksp/tutorials/ex49.c src/vec/vec/tutorials/ex1f90.F90 src/vec/vec/tutorials/ex19.c src/vec/vec/tutorials/ex20f90.F90

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecDuplicateVecs(Vec v, PetscInt m, Vec *V[])
```

Example 2 (unknown):
```unknown
VecDestroyVecs()
```

Example 3 (unknown):
```unknown
VecDuplicate()
```

Example 4 (unknown):
```unknown
VecDuplicateVecs()
```

---

## VecDuplicate#

**URL:** https://petsc.org/release/manualpages/Vec/VecDuplicate/

**Contents:**
- VecDuplicate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Creates a new vector of the same type as an existing vector.

v - a vector to mimic

newv - location to put new vector

VecDuplicate() DOES NOT COPY the vector entries, but rather allocates storage for the new vector. Use VecCopy() to copy a vector.

PETSc Vec always have all zero entries when created with VecDuplicate() until routines such as VecSet() or VecSetValues() are used to change the values. There is no reason to call VecZeroEntries() after creation.

Use VecDestroy() to free the space. Use VecDuplicateVecs() to get several vectors.

Vectors and Parallel Data, Vec, VecDestroy(), VecDuplicateVecs(), VecCreate(), VecCopy()

src/vec/vec/interface/vector.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex99.c src/snes/tutorials/ex1.c src/mat/tutorials/ex9.c src/snes/tutorials/ex14.c src/snes/tutorials/ex9.c src/snes/tutorials/ex12.c src/snes/tutorials/ex70.c src/snes/tutorials/ex15.c src/snes/tutorials/ex21.c

VecDuplicate_MPIKokkos() in src/vec/vec/impls/mpi/kokkos/mpikok.kokkos.cxx VecDuplicate_MPIViennaCL() in src/vec/vec/impls/mpi/mpiviennacl/mpiviennacl.cxx VecDuplicate_MPI() in src/vec/vec/impls/mpi/pbvec.c VecDuplicate_Nest() in src/vec/vec/impls/nest/vecnest.c VecDuplicate_Seq() in src/vec/vec/impls/seq/bvec2.c VecDuplicate_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecDuplicate_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx VecDuplicate_Shared() in src/vec/vec/impls/shared/shvec.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecDuplicate(Vec v, Vec *newv)
```

Example 2 (unknown):
```unknown
VecDuplicate()
```

Example 3 (unknown):
```unknown
VecDuplicate()
```

Example 4 (unknown):
```unknown
VecSetValues()
```

---

## VecEqual#

**URL:** https://petsc.org/release/manualpages/Vec/VecEqual/

**Contents:**
- VecEqual#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Compares two vectors. Returns true if the two vectors are either pointing to the same memory buffer, or if the two vectors have the same local and global layout as well as bitwise equality of all entries. Does NOT take round-off errors into account.

vec1 - the first vector

vec2 - the second vector

flg - PETSC_TRUE if the vectors are equal; PETSC_FALSE otherwise.

src/vec/vec/utils/vinv.c

src/dm/tutorials/ex9.c src/vec/vec/tutorials/ex19.c src/vec/vec/tutorials/ex44.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecEqual(Vec vec1, Vec vec2, PetscBool *flg)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

---

## VecErrorWeightedNorms#

**URL:** https://petsc.org/release/manualpages/Vec/VecErrorWeightedNorms/

**Contents:**
- VecErrorWeightedNorms#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

compute a weighted norm of the difference between two vectors

U - first vector to be compared

Y - second vector to be compared

E - optional third vector representing the error (if not provided, the error is ||U-Y||)

wnormtype - norm type

atol - scalar for absolute tolerance

vatol - vector representing per-entry absolute tolerances (can be NULL)

rtol - scalar for relative tolerance

vrtol - vector representing per-entry relative tolerances (can be NULL)

ignore_max - ignore values smaller than this value in absolute terms.

norm_loc - number of vector locations used for the weighted norm

norma - weighted norm based on the absolute tolerance

norma_loc - number of vector locations used for the absolute weighted norm

normr - weighted norm based on the relative tolerance

normr_loc - number of vector locations used for the relative weighted norm

This is primarily used for computing weighted local truncation errors in TS.

Vectors and Parallel Data, Vec, NormType, TSErrorWeightedNorm(), TSErrorWeightedENorm()

src/vec/vec/interface/vector.c

VecErrorWeightedNorms_MPIKokkos() in src/vec/vec/impls/mpi/kokkos/mpikok.kokkos.cxx VecErrorWeightedNorms_Nest() in src/vec/vec/impls/nest/vecnest.c VecErrorWeightedNorms_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecErrorWeightedNorms(Vec U, Vec Y, Vec E, NormType wnormtype, PetscReal atol, Vec vatol, PetscReal rtol, Vec vrtol, PetscReal ignore_max, PetscReal *norm, PetscInt *norm_loc, PetscReal *norma, PetscInt *norma_loc, PetscReal *normr, PetscInt *normr_loc)
```

Example 2 (unknown):
```unknown
TSErrorWeightedNorm()
```

Example 3 (unknown):
```unknown
TSErrorWeightedENorm()
```

---

## VecExp#

**URL:** https://petsc.org/release/manualpages/Vec/VecExp/

**Contents:**
- VecExp#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Replaces each component of a vector by e^x_i

v - The vector of exponents

Vec, VecLog(), VecAbs(), VecSqrtAbs(), VecReciprocal()

src/vec/vec/utils/vinv.c

src/tao/pde_constrained/tutorials/elliptic.c src/tao/pde_constrained/tutorials/hyperbolic.c src/tao/pde_constrained/tutorials/parabolic.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecExp(Vec v)
```

Example 2 (unknown):
```unknown
VecSqrtAbs()
```

Example 3 (unknown):
```unknown
VecReciprocal()
```

---

## VecFilter#

**URL:** https://petsc.org/release/manualpages/Vec/VecFilter/

**Contents:**
- VecFilter#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Set all values in the vector with an absolute value less than or equal to the tolerance to zero

tol - The zero tolerance

v - The filtered vector

VecCreate(), VecSet(), MatFilter()

src/vec/vec/utils/vecio.c

src/snes/tutorials/ex77.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"  
PetscErrorCode VecFilter(Vec v, PetscReal tol)
```

Example 2 (unknown):
```unknown
VecCreate()
```

Example 3 (unknown):
```unknown
MatFilter()
```

---

## VecFinalizePackage#

**URL:** https://petsc.org/release/manualpages/Vec/VecFinalizePackage/

**Contents:**
- VecFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function finalizes everything in the Vec package. It is called from PetscFinalize().

src/vec/vec/interface/dlregisvec.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" */
PetscErrorCode VecFinalizePackage(void)
```

Example 2 (unknown):
```unknown
PetscInitialize()
```

---

## VecFlag#

**URL:** https://petsc.org/release/manualpages/Vec/VecFlag/

**Contents:**
- VecFlag#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

set infinity into the local part of the vector on any subset of MPI processes

xin - the vector, can be NULL but only if on all processes

flg - indicates if this processes portion of the vector should be set to infinity

This removes the values from the vector norm cache for all processes by calling PetscObjectIncrease().

This is used for any subset of MPI processes to indicate an failure in a solver, after the next use of VecNorm() if KSPCheckNorm() detects an infinity and at least one of the MPI processes has a not converged reason then the KSP object collectively is labeled as not converged.

Vectors and Parallel Data, Vec, PetscLayout, VecGetLayout(), VecGetSize(), VecGetOwnershipRange(), VecGetOwnershipRanges()

src/vec/vec/interface/vector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecFlag(Vec xin, PetscInt flg)
```

Example 2 (unknown):
```unknown
PetscObjectIncrease()
```

Example 3 (unknown):
```unknown
KSPCheckNorm()
```

Example 4 (unknown):
```unknown
PetscLayout
```

---

## VecGetArray1dRead#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetArray1dRead/

**Contents:**
- VecGetArray1dRead#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Returns a pointer to a 1d contiguous array that contains this processor’s portion of the vector data. You MUST call VecRestoreArray1dRead() when you no longer need access to the array.

m - first dimension of two dimensional array

mstart - first index you will use in first coordinate direction (often 0)

a - location to put pointer to the array

For a vector obtained from DMCreateLocalVector() mstart is likely obtained from the corner indices obtained from DMDAGetGhostCorners() while for DMCreateGlobalVector() they are the corner indices from DMDAGetCorners().

For standard PETSc vectors this is an inexpensive call; it does not copy the vector values.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecGetArrays(), VecPlaceArray(), VecRestoreArray2d(), DMDAVecGetArray(), DMDAVecRestoreArray(), VecGetArray3d(), VecRestoreArray3d(), VecGetArray2d(), VecRestoreArray1d(), VecGetArray4d(), VecRestoreArray4d()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecRestoreArray1dRead()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetArray1dRead(Vec x, PetscInt m, PetscInt mstart, PetscScalar *a[])
```

Example 3 (unknown):
```unknown
DMCreateLocalVector()
```

Example 4 (unknown):
```unknown
DMDAGetGhostCorners()
```

---

## VecGetArray1dWrite#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetArray1dWrite/

**Contents:**
- VecGetArray1dWrite#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Returns a pointer to a 1d contiguous array that will contain this processor’s portion of the vector data. You MUST call VecRestoreArray1dWrite() when you no longer need access to the array.

m - first dimension of two dimensional array

mstart - first index you will use in first coordinate direction (often 0)

a - location to put pointer to the array

For a vector obtained from DMCreateLocalVector() mstart is likely obtained from the corner indices obtained from DMDAGetGhostCorners() while for DMCreateGlobalVector() they are the corner indices from DMDAGetCorners().

For standard PETSc vectors this is an inexpensive call; it does not copy the vector values.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecGetArrays(), VecPlaceArray(), VecRestoreArray2d(), DMDAVecGetArray(), DMDAVecRestoreArray(), VecGetArray3d(), VecRestoreArray3d(), VecGetArray2d(), VecRestoreArray1d(), VecGetArray4d(), VecRestoreArray4d()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecRestoreArray1dWrite()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetArray1dWrite(Vec x, PetscInt m, PetscInt mstart, PetscScalar *a[])
```

Example 3 (unknown):
```unknown
DMCreateLocalVector()
```

Example 4 (unknown):
```unknown
DMDAGetGhostCorners()
```

---

## VecGetArray1d#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetArray1d/

**Contents:**
- VecGetArray1d#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Returns a pointer to a 1d contiguous array that contains this processor’s portion of the vector data. You MUST call VecRestoreArray1d() when you no longer need access to the array.

m - first dimension of two dimensional array

mstart - first index you will use in first coordinate direction (often 0)

a - location to put pointer to the array

For a vector obtained from DMCreateLocalVector() mstart is likely obtained from the corner indices obtained from DMDAGetGhostCorners() while for DMCreateGlobalVector() they are the corner indices from DMDAGetCorners().

For standard PETSc vectors this is an inexpensive call; it does not copy the vector values.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecGetArrays(), VecPlaceArray(), VecRestoreArray2d(), DMDAVecGetArray(), DMDAVecRestoreArray(), VecGetArray3d(), VecRestoreArray3d(), VecGetArray2d(), VecRestoreArray1d(), VecGetArray4d(), VecRestoreArray4d()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecRestoreArray1d()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetArray1d(Vec x, PetscInt m, PetscInt mstart, PetscScalar *a[])
```

Example 3 (unknown):
```unknown
DMCreateLocalVector()
```

Example 4 (unknown):
```unknown
DMDAGetGhostCorners()
```

---

## VecGetArray2dRead#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetArray2dRead/

**Contents:**
- VecGetArray2dRead#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Returns a pointer to a 2d contiguous array that contains this processor’s portion of the vector data. You MUST call VecRestoreArray2dRead() when you no longer need access to the array.

m - first dimension of two dimensional array

n - second dimension of two dimensional array

mstart - first index you will use in first coordinate direction (often 0)

nstart - first index in the second coordinate direction (often 0)

a - location to put pointer to the array

For a vector obtained from DMCreateLocalVector() mstart and nstart are likely obtained from the corner indices obtained from DMDAGetGhostCorners() while for DMCreateGlobalVector() they are the corner indices from DMDAGetCorners(). In both cases the arguments from DMDAGet[Ghost]Corners() are reversed in the call to VecGetArray2d().

For standard PETSc vectors this is an inexpensive call; it does not copy the vector values.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecGetArrays(), VecPlaceArray(), VecRestoreArray2d(), DMDAVecGetArray(), DMDAVecRestoreArray(), VecGetArray3d(), VecRestoreArray3d(), VecGetArray1d(), VecRestoreArray1d(), VecGetArray4d(), VecRestoreArray4d()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecRestoreArray2dRead()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetArray2dRead(Vec x, PetscInt m, PetscInt n, PetscInt mstart, PetscInt nstart, PetscScalar **a[])
```

Example 3 (unknown):
```unknown
DMCreateLocalVector()
```

Example 4 (unknown):
```unknown
DMDAGetGhostCorners()
```

---

## VecGetArray2dWrite#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetArray2dWrite/

**Contents:**
- VecGetArray2dWrite#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Returns a pointer to a 2d contiguous array that will contain this processor’s portion of the vector data. You MUST call VecRestoreArray2dWrite() when you no longer need access to the array.

m - first dimension of two dimensional array

n - second dimension of two dimensional array

mstart - first index you will use in first coordinate direction (often 0)

nstart - first index in the second coordinate direction (often 0)

a - location to put pointer to the array

For a vector obtained from DMCreateLocalVector() mstart and nstart are likely obtained from the corner indices obtained from DMDAGetGhostCorners() while for DMCreateGlobalVector() they are the corner indices from DMDAGetCorners(). In both cases the arguments from DMDAGet[Ghost]Corners() are reversed in the call to VecGetArray2d().

For standard PETSc vectors this is an inexpensive call; it does not copy the vector values.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecGetArrays(), VecPlaceArray(), VecRestoreArray2d(), DMDAVecGetArray(), DMDAVecRestoreArray(), VecGetArray3d(), VecRestoreArray3d(), VecGetArray1d(), VecRestoreArray1d(), VecGetArray4d(), VecRestoreArray4d()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecRestoreArray2dWrite()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetArray2dWrite(Vec x, PetscInt m, PetscInt n, PetscInt mstart, PetscInt nstart, PetscScalar **a[])
```

Example 3 (unknown):
```unknown
DMCreateLocalVector()
```

Example 4 (unknown):
```unknown
DMDAGetGhostCorners()
```

---

## VecGetArray2d#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetArray2d/

**Contents:**
- VecGetArray2d#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Returns a pointer to a 2d contiguous array that contains this processor’s portion of the vector data. You MUST call VecRestoreArray2d() when you no longer need access to the array.

m - first dimension of two dimensional array

n - second dimension of two dimensional array

mstart - first index you will use in first coordinate direction (often 0)

nstart - first index in the second coordinate direction (often 0)

a - location to put pointer to the array

For a vector obtained from DMCreateLocalVector() mstart and nstart are likely obtained from the corner indices obtained from DMDAGetGhostCorners() while for DMCreateGlobalVector() they are the corner indices from DMDAGetCorners(). In both cases the arguments from DMDAGet[Ghost]Corners() are reversed in the call to VecGetArray2d().

For standard PETSc vectors this is an inexpensive call; it does not copy the vector values.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecGetArrays(), VecPlaceArray(), VecRestoreArray2d(), DMDAVecGetArray(), DMDAVecRestoreArray(), VecGetArray3d(), VecRestoreArray3d(), VecGetArray1d(), VecRestoreArray1d(), VecGetArray4d(), VecRestoreArray4d()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecRestoreArray2d()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetArray2d(Vec x, PetscInt m, PetscInt n, PetscInt mstart, PetscInt nstart, PetscScalar **a[])
```

Example 3 (unknown):
```unknown
DMCreateLocalVector()
```

Example 4 (unknown):
```unknown
DMDAGetGhostCorners()
```

---

## VecGetArray3dRead#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetArray3dRead/

**Contents:**
- VecGetArray3dRead#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Returns a pointer to a 3d contiguous array that contains this processor’s portion of the vector data. You MUST call VecRestoreArray3dRead() when you no longer need access to the array.

m - first dimension of three dimensional array

n - second dimension of three dimensional array

p - third dimension of three dimensional array

mstart - first index you will use in first coordinate direction (often 0)

nstart - first index in the second coordinate direction (often 0)

pstart - first index in the third coordinate direction (often 0)

a - location to put pointer to the array

For a vector obtained from DMCreateLocalVector() mstart, nstart, and pstart are likely obtained from the corner indices obtained from DMDAGetGhostCorners() while for DMCreateGlobalVector() they are the corner indices from DMDAGetCorners(). In both cases the arguments from DMDAGet[Ghost]Corners() are reversed in the call to VecGetArray3dRead().

For standard PETSc vectors this is an inexpensive call; it does not copy the vector values.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecGetArrays(), VecPlaceArray(), VecRestoreArray2d(), DMDAVecGetarray(), DMDAVecRestoreArray(), VecGetArray3d(), VecRestoreArray3d(), VecGetArray1d(), VecRestoreArray1d(), VecGetArray4d(), VecRestoreArray4d()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecRestoreArray3dRead()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetArray3dRead(Vec x, PetscInt m, PetscInt n, PetscInt p, PetscInt mstart, PetscInt nstart, PetscInt pstart, PetscScalar ***a[])
```

Example 3 (unknown):
```unknown
DMCreateLocalVector()
```

Example 4 (unknown):
```unknown
DMDAGetGhostCorners()
```

---

## VecGetArray3dWrite#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetArray3dWrite/

**Contents:**
- VecGetArray3dWrite#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Returns a pointer to a 3d contiguous array that will contain this processor’s portion of the vector data. You MUST call VecRestoreArray3dWrite() when you no longer need access to the array.

m - first dimension of three dimensional array

n - second dimension of three dimensional array

p - third dimension of three dimensional array

mstart - first index you will use in first coordinate direction (often 0)

nstart - first index in the second coordinate direction (often 0)

pstart - first index in the third coordinate direction (often 0)

a - location to put pointer to the array

For a vector obtained from DMCreateLocalVector() mstart, nstart, and pstart are likely obtained from the corner indices obtained from DMDAGetGhostCorners() while for DMCreateGlobalVector() they are the corner indices from DMDAGetCorners(). In both cases the arguments from DMDAGet[Ghost]Corners() are reversed in the call to VecGetArray3d().

For standard PETSc vectors this is an inexpensive call; it does not copy the vector values.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecGetArrays(), VecPlaceArray(), VecRestoreArray2d(), DMDAVecGetarray(), DMDAVecRestoreArray(), VecGetArray3d(), VecRestoreArray3d(), VecGetArray1d(), VecRestoreArray1d(), VecGetArray4d(), VecRestoreArray4d()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecRestoreArray3dWrite()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetArray3dWrite(Vec x, PetscInt m, PetscInt n, PetscInt p, PetscInt mstart, PetscInt nstart, PetscInt pstart, PetscScalar ***a[])
```

Example 3 (unknown):
```unknown
DMCreateLocalVector()
```

Example 4 (unknown):
```unknown
DMDAGetGhostCorners()
```

---

## VecGetArray3d#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetArray3d/

**Contents:**
- VecGetArray3d#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Returns a pointer to a 3d contiguous array that contains this processor’s portion of the vector data. You MUST call VecRestoreArray3d() when you no longer need access to the array.

m - first dimension of three dimensional array

n - second dimension of three dimensional array

p - third dimension of three dimensional array

mstart - first index you will use in first coordinate direction (often 0)

nstart - first index in the second coordinate direction (often 0)

pstart - first index in the third coordinate direction (often 0)

a - location to put pointer to the array

For a vector obtained from DMCreateLocalVector() mstart, nstart, and pstart are likely obtained from the corner indices obtained from DMDAGetGhostCorners() while for DMCreateGlobalVector() they are the corner indices from DMDAGetCorners(). In both cases the arguments from DMDAGet[Ghost]Corners() are reversed in the call to VecGetArray3d().

For standard PETSc vectors this is an inexpensive call; it does not copy the vector values.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecGetArrays(), VecPlaceArray(), VecRestoreArray2d(), DMDAVecGetarray(), DMDAVecRestoreArray(), VecRestoreArray3d(), VecGetArray1d(), VecRestoreArray1d(), VecGetArray4d(), VecRestoreArray4d()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecRestoreArray3d()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetArray3d(Vec x, PetscInt m, PetscInt n, PetscInt p, PetscInt mstart, PetscInt nstart, PetscInt pstart, PetscScalar ***a[])
```

Example 3 (unknown):
```unknown
DMCreateLocalVector()
```

Example 4 (unknown):
```unknown
DMDAGetGhostCorners()
```

---

## VecGetArray4dRead#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetArray4dRead/

**Contents:**
- VecGetArray4dRead#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Returns a pointer to a 4d contiguous array that contains this processor’s portion of the vector data. You MUST call VecRestoreArray4dRead() when you no longer need access to the array.

m - first dimension of four dimensional array

n - second dimension of four dimensional array

p - third dimension of four dimensional array

q - fourth dimension of four dimensional array

mstart - first index you will use in first coordinate direction (often 0)

nstart - first index in the second coordinate direction (often 0)

pstart - first index in the third coordinate direction (often 0)

qstart - first index in the fourth coordinate direction (often 0)

a - location to put pointer to the array

For a vector obtained from DMCreateLocalVector() mstart, nstart, and pstart are likely obtained from the corner indices obtained from DMDAGetGhostCorners() while for DMCreateGlobalVector() they are the corner indices from DMDAGetCorners(). In both cases the arguments from DMDAGet[Ghost]Corners() are reversed in the call to VecGetArray3d().

For standard PETSc vectors this is an inexpensive call; it does not copy the vector values.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecGetArrays(), VecPlaceArray(), VecRestoreArray2d(), DMDAVecGetarray(), DMDAVecRestoreArray(), VecGetArray3d(), VecRestoreArray3d(), VecGetArray1d(), VecRestoreArray1d(), VecGetArray4d(), VecRestoreArray4d()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecRestoreArray4dRead()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetArray4dRead(Vec x, PetscInt m, PetscInt n, PetscInt p, PetscInt q, PetscInt mstart, PetscInt nstart, PetscInt pstart, PetscInt qstart, PetscScalar ****a[])
```

Example 3 (unknown):
```unknown
DMCreateLocalVector()
```

Example 4 (unknown):
```unknown
DMDAGetGhostCorners()
```

---

## VecGetArray4dWrite#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetArray4dWrite/

**Contents:**
- VecGetArray4dWrite#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Returns a pointer to a 4d contiguous array that will contain this processor’s portion of the vector data. You MUST call VecRestoreArray4dWrite() when you no longer need access to the array.

m - first dimension of four dimensional array

n - second dimension of four dimensional array

p - third dimension of four dimensional array

q - fourth dimension of four dimensional array

mstart - first index you will use in first coordinate direction (often 0)

nstart - first index in the second coordinate direction (often 0)

pstart - first index in the third coordinate direction (often 0)

qstart - first index in the fourth coordinate direction (often 0)

a - location to put pointer to the array

For a vector obtained from DMCreateLocalVector() mstart, nstart, and pstart are likely obtained from the corner indices obtained from DMDAGetGhostCorners() while for DMCreateGlobalVector() they are the corner indices from DMDAGetCorners(). In both cases the arguments from DMDAGet[Ghost]Corners() are reversed in the call to VecGetArray3d().

For standard PETSc vectors this is an inexpensive call; it does not copy the vector values.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecGetArrays(), VecPlaceArray(), VecRestoreArray2d(), DMDAVecGetarray(), DMDAVecRestoreArray(), VecGetArray3d(), VecRestoreArray3d(), VecGetArray1d(), VecRestoreArray1d(), VecGetArray4d(), VecRestoreArray4d()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecRestoreArray4dWrite()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetArray4dWrite(Vec x, PetscInt m, PetscInt n, PetscInt p, PetscInt q, PetscInt mstart, PetscInt nstart, PetscInt pstart, PetscInt qstart, PetscScalar ****a[])
```

Example 3 (unknown):
```unknown
DMCreateLocalVector()
```

Example 4 (unknown):
```unknown
DMDAGetGhostCorners()
```

---

## VecGetArray4d#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetArray4d/

**Contents:**
- VecGetArray4d#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Returns a pointer to a 4d contiguous array that contains this processor’s portion of the vector data. You MUST call VecRestoreArray4d() when you no longer need access to the array.

m - first dimension of four dimensional array

n - second dimension of four dimensional array

p - third dimension of four dimensional array

q - fourth dimension of four dimensional array

mstart - first index you will use in first coordinate direction (often 0)

nstart - first index in the second coordinate direction (often 0)

pstart - first index in the third coordinate direction (often 0)

qstart - first index in the fourth coordinate direction (often 0)

a - location to put pointer to the array

For a vector obtained from DMCreateLocalVector() mstart, nstart, and pstart are likely obtained from the corner indices obtained from DMDAGetGhostCorners() while for DMCreateGlobalVector() they are the corner indices from DMDAGetCorners(). In both cases the arguments from DMDAGet[Ghost]Corners() are reversed in the call to VecGetArray3d().

For standard PETSc vectors this is an inexpensive call; it does not copy the vector values.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecGetArrays(), VecPlaceArray(), VecRestoreArray2d(), DMDAVecGetarray(), DMDAVecRestoreArray(), VecGetArray3d(), VecRestoreArray3d(), VecGetArray1d(), VecRestoreArray1d(), VecRestoreArray4d()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecRestoreArray4d()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetArray4d(Vec x, PetscInt m, PetscInt n, PetscInt p, PetscInt q, PetscInt mstart, PetscInt nstart, PetscInt pstart, PetscInt qstart, PetscScalar ****a[])
```

Example 3 (unknown):
```unknown
DMCreateLocalVector()
```

Example 4 (unknown):
```unknown
DMDAGetGhostCorners()
```

---

## VecGetArrayAndMemType#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetArrayAndMemType/

**Contents:**
- VecGetArrayAndMemType#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Like VecGetArray(), but if this is a standard device vector (e.g., VECCUDA), the returned pointer will be a device pointer to the device memory that contains this MPI processes’s portion of the vector data.

Logically Collective; No Fortran Support

a - location to put pointer to the array

mtype - memory type of the array

Device data is guaranteed to have the latest value. Otherwise, when this is a host vector (e.g., VECMPI), this routine functions the same as VecGetArray() and returns a host pointer.

For VECKOKKOS, if Kokkos is configured without device (e.g., use serial or openmp), per this function, the vector works like VECSEQ/VECMPI; otherwise, it works like VECCUDA or VECHIP etc.

Use VecRestoreArrayAndMemType() when the array access is no longer needed.

Vectors and Parallel Data, Vec, VecRestoreArrayAndMemType(), VecGetArrayReadAndMemType(), VecGetArrayWriteAndMemType(), VecRestoreArray(), VecGetArrayRead(), VecGetArrays(), VecPlaceArray(), VecGetArray2d(), VecGetArrayPair(), VecRestoreArrayPair(), VecGetArrayWrite(), VecRestoreArrayWrite()

src/vec/vec/interface/rvector.c

VecGetArrayAndMemType_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetArray()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetArrayAndMemType(Vec x, PetscScalar *a[], PetscMemType *mtype)
```

Example 3 (unknown):
```unknown
VecGetArray()
```

Example 4 (unknown):
```unknown
VecRestoreArrayAndMemType()
```

---

## VecGetArrayPair#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetArrayPair/

**Contents:**
- VecGetArrayPair#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Accesses a pair of pointers for two vectors that may be common. When the vectors are not the same the first pointer is read only

Logically Collective; No Fortran Support

y - the second vector

xv - location to put pointer to the first array

yv - location to put pointer to the second array

Vectors and Parallel Data, VecGetArray(), VecGetArrayRead(), VecRestoreArrayPair()

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
static inline PetscErrorCode VecGetArrayPair(Vec x, Vec y, PetscScalar *xv[], PetscScalar *yv[])
```

Example 2 (unknown):
```unknown
VecGetArray()
```

Example 3 (unknown):
```unknown
VecGetArrayRead()
```

Example 4 (unknown):
```unknown
VecRestoreArrayPair()
```

---

## VecGetArrayReadAndMemType#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetArrayReadAndMemType/

**Contents:**
- VecGetArrayReadAndMemType#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Like VecGetArrayRead(), but if the input vector is a device vector, it will return a read-only device pointer. The returned pointer is guaranteed to point to up-to-date data. For host vectors, it functions as VecGetArrayRead().

Not Collective; No Fortran Support

mtype - memory type of the array

The array must be returned using a matching call to VecRestoreArrayReadAndMemType().

Vectors and Parallel Data, Vec, VecRestoreArrayReadAndMemType(), VecGetArrayAndMemType(), VecGetArrayWriteAndMemType(), VecGetArray(), VecRestoreArray(), VecGetArrayPair(), VecRestoreArrayPair()

src/vec/vec/interface/rvector.c

src/mat/tutorials/ex19.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetArrayRead()
```

Example 2 (unknown):
```unknown
VecGetArrayRead()
```

Example 3 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetArrayReadAndMemType(Vec x, const PetscScalar *a[], PetscMemType *mtype)
```

Example 4 (unknown):
```unknown
VecRestoreArrayReadAndMemType()
```

---

## VecGetArrayRead#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetArrayRead/

**Contents:**
- VecGetArrayRead#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Get read-only pointer to contiguous array containing this processor’s portion of the vector data.

The array must be returned using a matching call to VecRestoreArrayRead().

Unlike VecGetArray(), preserves cached information like vector norms.

Standard PETSc vectors use contiguous storage so that this routine does not perform a copy. Other vector implementations may require a copy, but such implementations should cache the contiguous representation so that only one copy is performed when this routine is called multiple times in sequence.

For vectors that may also have the array data in GPU memory, for example, VECCUDA, this call ensures the CPU array has the most recent array values by copying the data from the GPU memory if needed.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecGetArrayPair(), VecRestoreArrayPair(), VecGetArrayAndMemType()

src/vec/vec/interface/rvector.c

src/snes/tutorials/ex99.c src/snes/tutorials/ex59.c src/snes/tutorials/ex1.c src/snes/tutorials/ex6.c src/snes/tutorials/ex73f90t.F90 src/snes/tutorials/ex13.c src/snes/tutorials/ex70.c src/mat/tutorials/ex12.c src/snes/tutorials/ex48.c src/snes/tutorials/ex7.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetArrayRead(Vec x, const PetscScalar *a[])
```

Example 2 (unknown):
```unknown
VecRestoreArrayRead()
```

Example 3 (unknown):
```unknown
VecGetArray()
```

Example 4 (unknown):
```unknown
VecGetArray()
```

---

## VecGetArrays#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetArrays/

**Contents:**
- VecGetArrays#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Returns a pointer to the arrays in a set of vectors that were created by a call to VecDuplicateVecs().

Logically Collective; No Fortran Support

n - the number of vectors

a - location to put pointer to the array

You MUST call VecRestoreArrays() when you no longer need access to the arrays.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArrays()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecDuplicateVecs()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetArrays(const Vec x[], PetscInt n, PetscScalar **a[])
```

Example 3 (unknown):
```unknown
VecRestoreArrays()
```

Example 4 (unknown):
```unknown
VecGetArray()
```

---

## VecGetArrayWriteAndMemType#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetArrayWriteAndMemType/

**Contents:**
- VecGetArrayWriteAndMemType#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Like VecGetArrayWrite(), but if this is a device vector it will always return a device pointer to the device memory that contains this processor’s portion of the vector data.

Logically Collective; No Fortran Support

mtype - memory type of the array

The array must be returned using a matching call to VecRestoreArrayWriteAndMemType(), where it will label the device memory as most recent.

Vectors and Parallel Data, Vec, VecRestoreArrayWriteAndMemType(), VecGetArrayReadAndMemType(), VecGetArrayAndMemType(), VecGetArray(), VecRestoreArray(), VecGetArrayPair(), VecRestoreArrayPair()

src/vec/vec/interface/rvector.c

VecGetArrayWriteAndMemType_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetArrayWrite()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetArrayWriteAndMemType(Vec x, PetscScalar *a[], PetscMemType *mtype)
```

Example 3 (unknown):
```unknown
VecRestoreArrayWriteAndMemType()
```

Example 4 (unknown):
```unknown
VecRestoreArrayWriteAndMemType()
```

---

## VecGetArrayWrite#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetArrayWrite/

**Contents:**
- VecGetArrayWrite#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Returns a pointer to a contiguous array that WILL contain this MPI processes’s portion of the vector data.

a - location to put pointer to the array

The values in this array are NOT valid, the caller of this routine is responsible for putting values into the array; any values it does not set will be invalid.

The array must be returned using a matching call to VecRestoreArrayWrite().

For vectors associated with GPUs, the host and device vectors are not synchronized before giving access. If you need correct values in the array use VecGetArray()

Vectors and Parallel Data, Vec, VecRestoreArray(), VecGetArrayRead(), VecGetArrays(), VecPlaceArray(), VecGetArray2d(), VecGetArrayPair(), VecRestoreArrayPair(), VecGetArray(), VecRestoreArrayWrite(), VecGetArrayAndMemType()

src/vec/vec/interface/rvector.c

src/ts/tutorials/ex45.c src/ts/tutorials/ex36.c src/dm/impls/plex/tutorials/ex14.c src/ts/tutorials/ex77.c src/ts/tutorials/ex3.c src/snes/tutorials/ex17.c src/ts/tutorials/ex43.c src/ts/tutorials/ex23fwdadj.c src/tao/unconstrained/tutorials/rosenbrock3.c src/ksp/ksp/tutorials/ex27.c

VecGetArrayWrite_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecGetArrayWrite_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetArrayWrite(Vec x, PetscScalar *a[])
```

Example 2 (unknown):
```unknown
VecRestoreArrayWrite()
```

Example 3 (unknown):
```unknown
VecGetArray()
```

Example 4 (unknown):
```unknown
VecRestoreArray()
```

---

## VecGetArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetArray/

**Contents:**
- VecGetArray#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Returns a pointer to a contiguous array that contains this MPI processes’s portion of the vector data

a - location to put pointer to the array

For the standard PETSc vectors, VecGetArray() returns a pointer to the local data array and does not use any copies. If the underlying vector data is not stored in a contiguous array this routine will copy the data to a contiguous array and return a pointer to that. You MUST call VecRestoreArray() when you no longer need access to the array.

For vectors that may also have the array data in GPU memory, for example, VECCUDA, this call ensures the CPU array has the most recent array values by copying the data from the GPU memory if needed.

Vectors and Parallel Data, Vec, VecRestoreArray(), VecGetArrayRead(), VecGetArrays(), VecPlaceArray(), VecGetArray2d(), VecGetArrayPair(), VecRestoreArrayPair(), VecGetArrayWrite(), VecRestoreArrayWrite(), VecGetArrayAndMemType()

src/vec/vec/interface/rvector.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex5f90.F90 src/snes/tutorials/ex99.c src/snes/tutorials/ex59.c src/snes/tutorials/ex1.c src/snes/tutorials/ex6.c src/snes/tutorials/ex13.c src/snes/tutorials/ex22.c src/snes/tutorials/ex7.c src/snes/tutorials/ex21.c

VecGetArray_Nest() in src/vec/vec/impls/nest/vecnest.c VecGetArray_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecGetArray_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetArray(Vec x, PetscScalar *a[])
```

Example 2 (unknown):
```unknown
VecGetArray()
```

Example 3 (unknown):
```unknown
VecRestoreArray()
```

Example 4 (julia):
```julia
PetscScalar, pointer :: a(:)
```

---

## VecGetBindingPropagates#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetBindingPropagates/

**Contents:**
- VecGetBindingPropagates#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets whether the state of being bound to the CPU for a GPU vector type propagates to child and some other associated objects

flg - flag indicating whether the boundtocpu flag will be propagated

Vectors and Parallel Data, Vec, VecSetBindingPropagates()

src/vec/vec/interface/vector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetBindingPropagates(Vec v, PetscBool *flg)
```

Example 2 (unknown):
```unknown
VecSetBindingPropagates()
```

---

## VecGetBlockSize#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetBlockSize/

**Contents:**
- VecGetBlockSize#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets the blocksize for the vector, i.e. what is used for VecSetValuesBlocked() and VecSetValuesBlockedLocal().

All vectors obtained by VecDuplicate() inherit the same blocksize.

Vectors and Parallel Data, Vec, VecSetValuesBlocked(), VecSetLocalToGlobalMapping(), VecSetBlockSize()

src/vec/vec/interface/vector.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex76.c src/ksp/ksp/tutorials/ex73.c src/dm/tutorials/swarm_ex3.c src/ksp/ksp/tutorials/ex71.c src/dm/field/tutorials/ex1.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecSetValuesBlocked()
```

Example 2 (unknown):
```unknown
VecSetValuesBlockedLocal()
```

Example 3 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetBlockSize(Vec v, PetscInt *bs)
```

Example 4 (unknown):
```unknown
VecDuplicate()
```

---

## VecGetKokkosViewWrite#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetKokkosViewWrite/

**Contents:**
- VecGetKokkosViewWrite#
- Synopsis#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Returns a Kokkos View that contains the array of a vector in the specified memory space.

Logically Collective, No Fortran Support

v - the vector in type of VECKOKKOS

kv - the Kokkos View with a user-specified template parameter MemorySpace

If the vector is not of type VECKOKKOS, an error will be raised.

The functions is similar to VecGetArrayWrite(). The returned view might contain garbage data or stale data and one is not expected to read data from the View. Instead, one is expected to overwrite all data in the View. One must return the View by a matching VecRestoreKokkosViewWrite() after finishing using the View.

Currently, only two memory spaces are supported: HostMirrorMemorySpace and Kokkos::DefaultExecutionSpace::memory_space.

VecRestoreKokkosViewWrite(), VecRestoreKokkosView(), VecGetKokkosView(), VecRestoreArray(), VecGetArrayRead(), VecGetArrays(), VecPlaceArray(), VecGetArray2d(), VecGetArrayPair(), VecRestoreArrayPair(), VecGetArrayWrite(), VecRestoreArrayWrite()

include/petscvec_kokkos.hpp

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (jsx):
```jsx
template <class MemorySpace>
PetscErrorCode VecGetKokkosViewWrite(Vec, Kokkos::View<PetscScalar *, MemorySpace> *)
```

Example 2 (cpp):
```cpp
#include <petscvec_kokkos.hpp>
PetscErrorCode VecGetKokkosViewWrite  (Vec v,Kokkos::View<PetscScalar*,MemorySpace>* kv);
```

Example 3 (unknown):
```unknown
VecGetArrayWrite()
```

Example 4 (unknown):
```unknown
VecRestoreKokkosViewWrite()
```

---

## VecGetKokkosView#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetKokkosView/

**Contents:**
- VecGetKokkosView#
- Synopsis#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Returns a constant Kokkos View that contains up-to-date data of a vector in the specified memory space.

Logically Collective, No Fortran Support

v - the vector in type of VECKOKKOS

kv - the Kokkos View with a user-specified template parameter MemorySpace

If the vector is not of type VECKOKKOS, an error will be raised.

The functions are similar to VecGetArrayRead() and VecGetArray() respectively. One can read-only or read/write the returned Kokkos View.

Passing in a const View enables read-only access.

One must return the View by a matching VecRestoreKokkosView() after finishing using the View. Currently, only two memory spaces are supported: HostMirrorMemorySpace and Kokkos::DefaultExecutionSpace::memory_space. If needed, a memory copy will be internally called to copy the latest vector data to the specified memory space.

VecRestoreKokkosView(), VecRestoreArray(), VecGetKokkosViewWrite(), VecGetArrayRead(), VecGetArrays(), VecPlaceArray(), VecGetArray2d(), VecGetArrayPair(), VecRestoreArrayPair(), VecGetArrayWrite(), VecRestoreArrayWrite()

include/petscvec_kokkos.hpp

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (jsx):
```jsx
template <class MemorySpace>
PetscErrorCode VecGetKokkosView(Vec, Kokkos::View<const PetscScalar *, MemorySpace> *)
```

Example 2 (jsx):
```jsx
#include <petscvec_kokkos.hpp>
PetscErrorCode VecGetKokkosView  (Vec v,Kokkos::View<const PetscScalar*,MemorySpace>* kv);
PetscErrorCode VecGetKokkosView  (Vec v,Kokkos::View<PetscScalar*,MemorySpace>* kv);
```

Example 3 (unknown):
```unknown
VecGetArrayRead()
```

Example 4 (unknown):
```unknown
VecGetArray()
```

---

## VecGetLayout#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetLayout/

**Contents:**
- VecGetLayout#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

get PetscLayout describing a vector layout

The layout determines what vector elements are contained on each MPI process

Vectors and Parallel Data, PetscLayout, Vec, VecGetSize(), VecGetOwnershipRange(), VecGetOwnershipRanges()

src/vec/vec/interface/vector.c

src/vec/vec/utils/tagger/tutorials/ex1.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLayout
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetLayout(Vec x, PetscLayout *map)
```

Example 3 (unknown):
```unknown
PetscLayout
```

Example 4 (unknown):
```unknown
VecGetSize()
```

---

## VecGetLocalSize#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetLocalSize/

**Contents:**
- VecGetLocalSize#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Returns the number of elements of the vector stored in local memory (that is on this MPI process)

size - the length of the local piece of the vector

Vectors and Parallel Data, Vec, VecGetSize()

src/vec/vec/interface/vector.c

src/snes/tutorials/ex71.c src/ksp/pc/tutorials/ex4.c src/snes/tutorials/ex76.c src/ksp/ksp/tutorials/ex72.c src/ksp/ksp/tutorials/ex23.c src/ksp/ksp/tutorials/ex76f.F90 src/snes/tutorials/ex36.c src/snes/tutorials/ex48.c src/snes/tutorials/ex7.c src/snes/tutorials/ex22.c

VecGetLocalSize_Nest() in src/vec/vec/impls/nest/vecnest.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetLocalSize(Vec x, PetscInt *size)
```

Example 2 (unknown):
```unknown
VecGetSize()
```

---

## VecGetLocalToGlobalMapping#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetLocalToGlobalMapping/

**Contents:**
- VecGetLocalToGlobalMapping#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Gets the local-to-global numbering set by VecSetLocalToGlobalMapping()

mapping - the mapping

Vectors and Parallel Data, Vec, VecSetValuesLocal(), VecSetLocalToGlobalMapping()

src/vec/vec/interface/vector.c

src/vec/vec/tutorials/ex9.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecSetLocalToGlobalMapping()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetLocalToGlobalMapping(Vec X, ISLocalToGlobalMapping *mapping)
```

Example 3 (unknown):
```unknown
VecSetValuesLocal()
```

Example 4 (unknown):
```unknown
VecSetLocalToGlobalMapping()
```

---

## VecGetLocalVectorRead#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetLocalVectorRead/

**Contents:**
- VecGetLocalVectorRead#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Maps the local portion of a vector into a vector.

v - The vector for which the local vector is desired.

w - Upon exit this contains the local vector.

You must call VecRestoreLocalVectorRead() when the local vector is no longer needed.

This function is similar to VecGetArrayRead() which maps the local portion into a raw pointer. VecGetLocalVectorRead() is usually almost as efficient as VecGetArrayRead() but in certain circumstances VecGetLocalVectorRead() can be much more efficient than VecGetArrayRead(). This is because the construction of a contiguous array representing the vector data required by VecGetArrayRead() can be an expensive operation for certain vector types. For example, for GPU vectors VecGetArrayRead() requires that the data between device and host is synchronized.

Unlike VecGetLocalVector(), this routine is not collective and preserves cached information.

Vectors and Parallel Data, Vec, VecCreateLocalVector(), VecRestoreLocalVectorRead(), VecGetLocalVector(), VecGetArrayRead(), VecGetArray()

src/vec/vec/interface/rvector.c

VecGetLocalVectorRead_Nest() in src/vec/vec/impls/nest/vecnest.c VecGetLocalVectorRead_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetLocalVectorRead(Vec v, Vec w)
```

Example 2 (unknown):
```unknown
VecRestoreLocalVectorRead()
```

Example 3 (unknown):
```unknown
VecGetArrayRead()
```

Example 4 (unknown):
```unknown
VecGetLocalVectorRead()
```

---

## VecGetLocalVector#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetLocalVector/

**Contents:**
- VecGetLocalVector#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Maps the local portion of a vector into a vector.

v - The vector for which the local vector is desired.

w - Upon exit this contains the local vector.

You must call VecRestoreLocalVector() when the local vector is no longer needed.

This function is similar to VecGetArray() which maps the local portion into a raw pointer. VecGetLocalVector() is usually about as efficient as VecGetArray() but in certain circumstances VecGetLocalVector() can be much more efficient than VecGetArray(). This is because the construction of a contiguous array representing the vector data required by VecGetArray() can be an expensive operation for certain vector types. For example, for GPU vectors VecGetArray() requires that the data between device and host is synchronized.

Vectors and Parallel Data, Vec, VecCreateLocalVector(), VecRestoreLocalVector(), VecGetLocalVectorRead(), VecGetArrayRead(), VecGetArray()

src/vec/vec/interface/rvector.c

VecGetLocalVector_Nest() in src/vec/vec/impls/nest/vecnest.c VecGetLocalVector_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetLocalVector(Vec v, Vec w)
```

Example 2 (unknown):
```unknown
VecRestoreLocalVector()
```

Example 3 (unknown):
```unknown
VecGetArray()
```

Example 4 (unknown):
```unknown
VecGetLocalVector()
```

---

## VecGetOffloadMask#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetOffloadMask/

**Contents:**
- VecGetOffloadMask#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the offload mask of a Vec

mask - corresponding PetscOffloadMask enum value.

Vectors and Parallel Data, Vec, VecCreateSeqCUDA(), VecCreateSeqViennaCL(), VecGetArray(), VecGetType()

src/vec/vec/interface/vector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetOffloadMask(Vec v, PetscOffloadMask *mask)
```

Example 2 (unknown):
```unknown
PetscOffloadMask
```

Example 3 (unknown):
```unknown
VecCreateSeqCUDA()
```

Example 4 (unknown):
```unknown
VecCreateSeqViennaCL()
```

---

## VecGetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetOptionsPrefix/

**Contents:**
- VecGetOptionsPrefix#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Sets the prefix used for searching for all Vec options in the database.

prefix - pointer to the prefix string used

Vectors and Parallel Data, Vec, VecAppendOptionsPrefix()

src/vec/vec/interface/vector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetOptionsPrefix(Vec v, const char *prefix[])
```

Example 2 (unknown):
```unknown
VecAppendOptionsPrefix()
```

---

## VecGetOwnershipRanges#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetOwnershipRanges/

**Contents:**
- VecGetOwnershipRanges#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Returns the range of indices owned by EACH processor, The vector is laid out with the first n1 elements on the first processor, next n2 elements on the second, etc. For certain parallel layouts this range may not be well defined.

ranges - array of length size + 1 with the start and end+1 for each process

If the Vec was obtained from a DM with DMCreateGlobalVector(), then the range values are determined by the specific DM.

If the Vec was created directly the range values are determined by the local size passed to VecSetSizes() or VecCreateMPI(). If PETSC_DECIDE was passed as the local size, then the vector uses default values for the range using PetscSplitOwnership().

The high argument is one more than the last element stored locally.

For certain DM, such as DMDA, it is better to use DM specific routines, such as DMDAGetGhostCorners(), to determine the local values in the vector.

The high argument is one more than the last element stored locally.

If ranges are used after all vectors that share the ranges has been destroyed, then the program will crash accessing ranges.

The argument ranges must be declared as

and you have to return it with a call to VecRestoreOwnershipRanges() when no longer needed

Vectors and Parallel Data, Vec, MatGetOwnershipRange(), MatGetOwnershipRanges(), VecGetOwnershipRange(), PetscSplitOwnership(), VecSetSizes(), VecCreateMPI(), PetscLayout, DMDAGetGhostCorners(), DM

src/vec/vec/interface/vector.c

src/tao/pde_constrained/tutorials/elliptic.c src/vec/vec/tutorials/ex1f90.F90

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetOwnershipRanges(Vec x, const PetscInt *ranges[])
```

Example 2 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 3 (unknown):
```unknown
VecSetSizes()
```

Example 4 (unknown):
```unknown
VecCreateMPI()
```

---

## VecGetOwnershipRange#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetOwnershipRange/

**Contents:**
- VecGetOwnershipRange#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Returns the range of indices owned by this process. The vector is laid out with the first n1 elements on the first processor, next n2 elements on the second, etc. For certain parallel layouts this range may not be well defined.

low - the first local element, pass in NULL if not interested

high - one more than the last local element, pass in NULL if not interested

If the Vec was obtained from a DM with DMCreateGlobalVector(), then the range values are determined by the specific DM.

If the Vec was created directly the range values are determined by the local size passed to VecSetSizes() or VecCreateMPI(). If PETSC_DECIDE was passed as the local size, then the vector uses default values for the range using PetscSplitOwnership().

The high argument is one more than the last element stored locally.

For certain DM, such as DMDA, it is better to use DM specific routines, such as DMDAGetGhostCorners(), to determine the local values in the vector.

Vectors and Parallel Data, Vec, MatGetOwnershipRange(), MatGetOwnershipRanges(), VecGetOwnershipRanges(), PetscSplitOwnership(), VecSetSizes(), VecCreateMPI(), PetscLayout, DMDAGetGhostCorners(), DM

src/vec/vec/interface/vector.c

src/ksp/ksp/tutorials/ex5f.F90 src/snes/tutorials/ex73f90t.F90 src/ksp/ksp/tutorials/ex72.c src/ksp/ksp/tutorials/ex23.c src/ksp/ksp/tutorials/ex10.c src/ksp/ksp/tutorials/ex9.c src/ksp/ksp/tutorials/ex71.c src/snes/tutorials/ex70.c src/ksp/ksp/tutorials/ex49.c src/ksp/ksp/tutorials/ex74.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetOwnershipRange(Vec x, PetscInt *low, PetscInt *high)
```

Example 2 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 3 (unknown):
```unknown
VecSetSizes()
```

Example 4 (unknown):
```unknown
VecCreateMPI()
```

---

## VecGetPinnedMemoryMin#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetPinnedMemoryMin/

**Contents:**
- VecGetPinnedMemoryMin#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the minimum data size for which pinned memory will be used for host (CPU) allocations.

mbytes - minimum data size in bytes

Vectors and Parallel Data, Vec, VecSetPinnedMemoryMin()

src/vec/vec/interface/vector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetPinnedMemoryMin(Vec v, size_t *mbytes)
```

Example 2 (unknown):
```unknown
VecSetPinnedMemoryMin()
```

---

## VecGetSize#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetSize/

**Contents:**
- VecGetSize#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Returns the global number of elements of the vector.

size - the global length of the vector

Vectors and Parallel Data, Vec, VecGetLocalSize()

src/vec/vec/interface/vector.c

src/snes/tutorials/ex59.c src/snes/tutorials/ex55.c src/snes/tutorials/ex6.c src/ksp/ksp/tutorials/ex72.c src/snes/tutorials/ex5.c src/snes/tutorials/ex13.c src/snes/tutorials/ex2.c src/snes/tutorials/ex36.c src/snes/tutorials/ex56.c src/snes/tutorials/ex7.c

VecGetSize_MPI() in src/vec/vec/impls/mpi/pdvec.c VecGetSize_Nest() in src/vec/vec/impls/nest/vecnest.c VecGetSize_Seq() in src/vec/vec/impls/seq/bvec2.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetSize(Vec x, PetscInt *size)
```

Example 2 (unknown):
```unknown
VecGetLocalSize()
```

---

## VecGetState#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetState/

**Contents:**
- VecGetState#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the state of a Vec.

state - the object state

Object state is an integer which gets increased every time the object is changed. By saving and later querying the object state one can determine whether information about the object is still current.

Vectors and Parallel Data, Vec, VecCreate(), PetscObjectStateGet()

src/vec/vec/interface/vector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetState(Vec v, PetscObjectState *state)
```

Example 2 (unknown):
```unknown
VecCreate()
```

Example 3 (unknown):
```unknown
PetscObjectStateGet()
```

---

## VecGetSubVector#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetSubVector/

**Contents:**
- VecGetSubVector#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Gets a vector representing part of another vector

X - vector from which to extract a subvector

is - index set representing portion of X to extract

Y - subvector corresponding to is

The subvector Y should be returned with VecRestoreSubVector(). X and is must be defined on the same communicator

Changes to the subvector will be reflected in the X vector on the call to VecRestoreSubVector().

This function may return a subvector without making a copy, therefore it is not safe to use the original vector while modifying the subvector. Other non-overlapping subvectors can still be obtained from X using this function.

The resulting subvector inherits the block size from is if greater than one. Otherwise, the block size is guessed from the block size of the original X.

Vectors and Parallel Data, Vec, IS, VECNEST, MatCreateSubMatrix()

src/vec/vec/interface/rvector.c

src/dm/tutorials/ex22.c src/snes/tutorials/ex70.c src/ksp/ksp/tutorials/ex81.c src/ts/tutorials/ex77.c src/ksp/ksp/tutorials/ex81a.c src/vec/vec/tutorials/ex44.c

VecGetSubVector_MPIKokkos() in src/vec/vec/impls/mpi/kokkos/mpikok.kokkos.cxx VecGetSubVector_Nest() in src/vec/vec/impls/nest/vecnest.c VecGetSubVector_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetSubVector(Vec X, IS is, Vec *Y)
```

Example 2 (unknown):
```unknown
VecRestoreSubVector()
```

Example 3 (unknown):
```unknown
VecRestoreSubVector()
```

Example 4 (unknown):
```unknown
MatCreateSubMatrix()
```

---

## VecGetType#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetType/

**Contents:**
- VecGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets the vector type name (as a string) from a Vec.

type - The VecType of the vector

type should not be retained for later use as it will be an invalid pointer if the VecType of vec is changed.

Vectors and Parallel Data, Vec, VecType, VecCreate(), VecDuplicate(), VecDuplicateVecs(), PetscObjectTypeCompare(), PetscObjectTypeCompareAny()

src/vec/vec/interface/vecreg.c

src/snes/tutorials/ex7.c src/mat/tutorials/ex19.c src/ksp/ksp/tutorials/ex73.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"  
PetscErrorCode VecGetType(Vec vec, VecType *type)
```

Example 2 (unknown):
```unknown
VecCreate()
```

Example 3 (unknown):
```unknown
VecDuplicate()
```

Example 4 (unknown):
```unknown
VecDuplicateVecs()
```

---

## VecGetValuesSection#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetValuesSection/

**Contents:**
- VecGetValuesSection#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets all the values associated with a given point, according to the section, in the given Vec

s - the organizing PetscSection

values - the array of output values

PetscSection, PetscSectionCreate(), VecSetValuesSection()

src/vec/vec/utils/vsection.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
#include "petscvec.h"   
PetscErrorCode VecGetValuesSection(Vec v, PetscSection s, PetscInt point, PetscScalar *values[])
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (unknown):
```unknown
PetscSectionCreate()
```

---

## VecGetValues#

**URL:** https://petsc.org/release/manualpages/Vec/VecGetValues/

**Contents:**
- VecGetValues#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Gets values from certain locations of a vector. Currently can only get values on the same processor on which they are owned

x - vector to get values from

ni - number of elements to get

ix - indices where to get them from (in global 1d numbering)

y - array of values, must be passed in with a length of ni

The user provides the allocated array y; it is NOT allocated in this routine

VecGetValues() gets y[i] = x[ix[i]], for i=0,…,ni-1.

VecAssemblyBegin() and VecAssemblyEnd() MUST be called before calling this if VecSetValues() or related routine has been called

VecGetValues() uses 0-based indices in Fortran as well as in C.

If you call VecSetOption(x, VEC_IGNORE_NEGATIVE_INDICES,PETSC_TRUE), negative indices may be passed in ix. These rows are simply ignored.

Vectors and Parallel Data, Vec, VecAssemblyBegin(), VecAssemblyEnd(), VecSetValues()

src/vec/vec/interface/rvector.c

src/vec/vec/tutorials/ex2f.F90

VecGetValues_MPI() in src/vec/vec/impls/mpi/pdvec.c VecGetValues_Seq() in src/vec/vec/impls/seq/bvec2.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGetValues(Vec x, PetscInt ni, const PetscInt ix[], PetscScalar y[])
```

Example 2 (unknown):
```unknown
VecGetValues()
```

Example 3 (unknown):
```unknown
VecAssemblyBegin()
```

Example 4 (unknown):
```unknown
VecAssemblyEnd()
```

---

## VecGhostGetGhostIS#

**URL:** https://petsc.org/release/manualpages/Vec/VecGhostGetGhostIS/

**Contents:**
- VecGhostGetGhostIS#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Return ghosting indices of a ghost vector

ghost - ghosting indices

VecCreateGhostWithArray(), VecCreateMPIWithArray()

src/vec/vec/impls/mpi/pbvec.c

src/vec/vec/tutorials/ex9.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGhostGetGhostIS(Vec X, IS *ghost)
```

Example 2 (unknown):
```unknown
VecCreateGhostWithArray()
```

Example 3 (unknown):
```unknown
VecCreateMPIWithArray()
```

---

## VecGhostGetLocalForm#

**URL:** https://petsc.org/release/manualpages/Vec/VecGhostGetLocalForm/

**Contents:**
- VecGhostGetLocalForm#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Obtains the local ghosted representation of a parallel vector (obtained with VecCreateGhost(), VecCreateGhostWithArray() or VecCreateSeq()).

g - the global vector

l - the local (ghosted) representation,NULL if g is not ghosted

This routine does not actually update the ghost values, but rather it returns a sequential vector that includes the locations for the ghost values and their current values. The returned vector and the original vector passed in share the same array that contains the actual vector data.

To update the ghost values from the locations on the other processes one must call VecGhostUpdateBegin() and VecGhostUpdateEnd() before accessing the ghost values. Thus normal usage is

One must call VecGhostRestoreLocalForm() once finished using the object.

Vectors and Parallel Data, VecGhostUpdateBegin(), VecGhostUpdateEnd(), Vec, VecType, VecCreateGhost(), VecGhostRestoreLocalForm(), VecCreateGhostWithArray()

src/vec/vec/impls/mpi/commonmpvec.c

src/vec/vec/tutorials/ex9f.F90 src/vec/vec/tutorials/ex14f.F90 src/vec/vec/tutorials/ex9.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecCreateGhost()
```

Example 2 (unknown):
```unknown
VecCreateGhostWithArray()
```

Example 3 (unknown):
```unknown
VecCreateSeq()
```

Example 4 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGhostGetLocalForm(Vec g, Vec *l)
```

---

## VecGhostIsLocalForm#

**URL:** https://petsc.org/release/manualpages/Vec/VecGhostIsLocalForm/

**Contents:**
- VecGhostIsLocalForm#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Checks if a given vector is the local form of a global vector

g - the global vector

flg - PETSC_TRUE if l is the local form

Vectors and Parallel Data, Vec, VecType, VecCreateGhost(), VecGhostRestoreLocalForm(), VecCreateGhostWithArray(), VecGhostGetLocalForm()

src/vec/vec/impls/mpi/commonmpvec.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGhostIsLocalForm(Vec g, Vec l, PetscBool *flg)
```

Example 2 (unknown):
```unknown
VecCreateGhost()
```

Example 3 (unknown):
```unknown
VecGhostRestoreLocalForm()
```

Example 4 (unknown):
```unknown
VecCreateGhostWithArray()
```

---

## VecGhostRestoreLocalForm#

**URL:** https://petsc.org/release/manualpages/Vec/VecGhostRestoreLocalForm/

**Contents:**
- VecGhostRestoreLocalForm#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Restores the local ghosted representation of a parallel vector obtained with VecGhostGetLocalForm().

g - the global vector

l - the local (ghosted) representation

Vectors and Parallel Data, VecGhostUpdateBegin(), VecGhostUpdateEnd(), Vec, VecType, VecCreateGhost(), VecGhostGetLocalForm(), VecCreateGhostWithArray()

src/vec/vec/impls/mpi/commonmpvec.c

src/vec/vec/tutorials/ex9f.F90 src/vec/vec/tutorials/ex14f.F90 src/vec/vec/tutorials/ex9.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGhostGetLocalForm()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGhostRestoreLocalForm(Vec g, Vec *l)
```

Example 3 (unknown):
```unknown
VecGhostUpdateBegin()
```

Example 4 (unknown):
```unknown
VecGhostUpdateEnd()
```

---

## VecGhostUpdateBegin#

**URL:** https://petsc.org/release/manualpages/Vec/VecGhostUpdateBegin/

**Contents:**
- VecGhostUpdateBegin#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Begins the vector scatter to update the vector from local representation to global or global representation to local.

Neighbor-wise Collective

g - the vector (obtained with VecCreateGhost() or VecDuplicate())

insertmode - one of ADD_VALUES, MAX_VALUES, MIN_VALUES or INSERT_VALUES

scattermode - one of SCATTER_FORWARD (update ghosts) or SCATTER_REVERSE (update local values from ghosts)

Use the following to update the ghost regions with correct values from the owning process

Use the following to accumulate the ghost region values onto the owning processors

To accumulate the ghost region values onto the owning processors and then update the ghost regions correctly, call the latter followed by the former, i.e.,

Vectors and Parallel Data, Vec, VecType, VecCreateGhost(), VecGhostUpdateEnd(), VecGhostGetLocalForm(), VecGhostRestoreLocalForm(), VecCreateGhostWithArray()

src/vec/vec/impls/mpi/commonmpvec.c

src/vec/vec/tutorials/ex9f.F90 src/vec/vec/tutorials/ex14f.F90 src/vec/vec/tutorials/ex9.c src/snes/tutorials/ex42.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGhostUpdateBegin(Vec g, InsertMode insertmode, ScatterMode scattermode)
```

Example 2 (unknown):
```unknown
VecCreateGhost()
```

Example 3 (unknown):
```unknown
VecDuplicate()
```

Example 4 (unknown):
```unknown
INSERT_VALUES
```

---

## VecGhostUpdateEnd#

**URL:** https://petsc.org/release/manualpages/Vec/VecGhostUpdateEnd/

**Contents:**
- VecGhostUpdateEnd#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

End the vector scatter to update the vector from local representation to global or global representation to local.

Neighbor-wise Collective

g - the vector (obtained with VecCreateGhost() or VecDuplicate())

insertmode - one of ADD_VALUES, MAX_VALUES, MIN_VALUES or INSERT_VALUES

scattermode - one of SCATTER_FORWARD (update ghosts) or SCATTER_REVERSE (update local values from ghosts)

Use the following to update the ghost regions with correct values from the owning process

Use the following to accumulate the ghost region values onto the owning processors

To accumulate the ghost region values onto the owning processors and then update the ghost regions correctly, call the later followed by the former, i.e.,

Vectors and Parallel Data, Vec, VecType, VecCreateGhost(), VecGhostUpdateBegin(), VecGhostGetLocalForm(), VecGhostRestoreLocalForm(), VecCreateGhostWithArray()

src/vec/vec/impls/mpi/commonmpvec.c

src/vec/vec/tutorials/ex9f.F90 src/vec/vec/tutorials/ex14f.F90 src/vec/vec/tutorials/ex9.c src/snes/tutorials/ex42.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecGhostUpdateEnd(Vec g, InsertMode insertmode, ScatterMode scattermode)
```

Example 2 (unknown):
```unknown
VecCreateGhost()
```

Example 3 (unknown):
```unknown
VecDuplicate()
```

Example 4 (unknown):
```unknown
INSERT_VALUES
```

---

## VecHIPGetArrayRead#

**URL:** https://petsc.org/release/manualpages/Vec/VecHIPGetArrayRead/

**Contents:**
- VecHIPGetArrayRead#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Provides read access to the HIP buffer inside a vector.

Not Collective; Asynchronous; No Fortran Support

See VecHIPGetArray() for data movement semantics of this function.

This function assumes that the user will not modify the vector data. This is analgogous to intent(in) in Fortran.

The device pointer must be restored by calling VecHIPRestoreArrayRead(). If the data on the host side was previously up to date it will remain so, i.e. data on both the device and the host is up to date. Accessing data on the host side does not incur a device to host data transfer.

Vectors and Parallel Data, VecHIPRestoreArrayRead(), VecHIPGetArray(), VecHIPGetArrayWrite(), VecGetArray(), VecGetArrayRead()

src/vec/vec/impls/seq/cupm/hip/vecseqcupm.hip.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecHIPGetArrayRead(Vec v, const PetscScalar **a)
```

Example 2 (unknown):
```unknown
VecHIPGetArray()
```

Example 3 (unknown):
```unknown
VecHIPRestoreArrayRead()
```

Example 4 (unknown):
```unknown
VecHIPRestoreArrayRead()
```

---

## VecHIPGetArrayWrite#

**URL:** https://petsc.org/release/manualpages/Vec/VecHIPGetArrayWrite/

**Contents:**
- VecHIPGetArrayWrite#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Provides write access to the HIP buffer inside a vector.

Logically Collective; Asynchronous; No Fortran Support

The data pointed to by the device pointer is uninitialized. The user may not read from this data. Furthermore, the entire array needs to be filled by the user to obtain well-defined behaviour. The device memory will be allocated by this function if it hasn’t been allocated previously. This is analogous to intent(out) in Fortran.

The device pointer needs to be released with VecHIPRestoreArrayWrite(). When the pointer is released the host data of the vector is marked as out of data. Subsequent access of the host data with e.g. VecGetArray() incurs a device to host data transfer.

Vectors and Parallel Data, VecHIPRestoreArrayWrite(), VecHIPGetArray(), VecHIPGetArrayRead(), VecHIPGetArrayWrite(), VecGetArray(), VecGetArrayRead()

src/vec/vec/impls/seq/cupm/hip/vecseqcupm.hip.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecHIPGetArrayWrite(Vec v, PetscScalar **a)
```

Example 2 (unknown):
```unknown
VecHIPRestoreArrayWrite()
```

Example 3 (unknown):
```unknown
VecGetArray()
```

Example 4 (unknown):
```unknown
VecHIPRestoreArrayWrite()
```

---

## VecHIPGetArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecHIPGetArray/

**Contents:**
- VecHIPGetArray#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#

Provides access to the device buffer inside a vector

Logically Collective; Asynchronous; No Fortran Support

a - the device buffer

This routine has semantics similar to VecGetArray(); the returned buffer points to a consistent view of the vector data. This may involve copying data from the host to the device if the data on the device is out of date. It is also assumed that the returned buffer is immediately modified, marking the host data out of date. This is similar to intent(inout) in Fortran.

If the user does require strong memory guarantees, they are encouraged to use VecHIPGetArrayRead() and/or VecHIPGetArrayWrite() instead.

The user must call VecHIPRestoreArray() when they are finished using the array.

If the device memory hasn’t been allocated previously it will be allocated as part of this routine.

Vectors and Parallel Data, VecHIPRestoreArray(), VecHIPGetArrayRead(), VecHIPGetArrayWrite(), VecGetArray(), VecGetArrayRead(), VecGetArrayWrite()

src/vec/vec/impls/seq/cupm/hip/vecseqcupm.hip.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecHIPGetArray(Vec v, PetscScalar **a)
```

Example 2 (unknown):
```unknown
VecGetArray()
```

Example 3 (unknown):
```unknown
VecHIPGetArrayRead()
```

Example 4 (unknown):
```unknown
VecHIPGetArrayWrite()
```

---

## VecHIPPlaceArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecHIPPlaceArray/

**Contents:**
- VecHIPPlaceArray#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Allows one to replace the GPU array in a vector with a GPU array provided by the user.

Logically Collective; Asynchronous; No Fortran Support

array - the GPU array

Adding const to array was an oversight, see notes in VecPlaceArray().

This routine is useful to avoid copying an array into a vector, though you can return to the original GPU array with a call to VecHIPResetArray().

It is not possible to use VecHIPPlaceArray() and VecPlaceArray() at the same time on the same vector.

vec does not take ownership of array in any way. The user must free array themselves but be careful not to do so before the vector has either been destroyed, had its original array restored with VecHIPResetArray() or permanently replaced with VecHIPReplaceArray().

Vectors and Parallel Data, VecPlaceArray(), VecGetArray(), VecRestoreArray(), VecReplaceArray(), VecResetArray(), VecHIPResetArray(), VecHIPReplaceArray()

src/vec/vec/impls/seq/cupm/hip/vecseqcupm.hip.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecHIPPlaceArray(Vec vin, const PetscScalar array[])
```

Example 2 (unknown):
```unknown
VecPlaceArray()
```

Example 3 (unknown):
```unknown
VecHIPResetArray()
```

Example 4 (unknown):
```unknown
VecHIPPlaceArray()
```

---

## VecHIPReplaceArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecHIPReplaceArray/

**Contents:**
- VecHIPReplaceArray#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Permanently replace the GPU array in a vector with a GPU array provided by the user.

Logically Collective; No Fortran Support

array - the GPU array

Adding const to array was an oversight, see notes in VecPlaceArray().

This is useful to avoid copying a GPU array into a vector.

This frees the memory associated with the old GPU array. The vector takes ownership of the passed array so it CANNOT be freed by the user. It will be freed when the vector is destroyed.

Vectors and Parallel Data, VecGetArray(), VecRestoreArray(), VecPlaceArray(), VecResetArray(), VecHIPResetArray(), VecHIPPlaceArray(), VecReplaceArray()

src/vec/vec/impls/seq/cupm/hip/vecseqcupm.hip.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecHIPReplaceArray(Vec vin, const PetscScalar array[])
```

Example 2 (unknown):
```unknown
VecPlaceArray()
```

Example 3 (unknown):
```unknown
VecGetArray()
```

Example 4 (unknown):
```unknown
VecRestoreArray()
```

---

## VecHIPResetArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecHIPResetArray/

**Contents:**
- VecHIPResetArray#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Resets a vector to use its default memory.

Logically Collective; No Fortran Support

Call this after the use of VecHIPPlaceArray().

Vectors and Parallel Data, VecGetArray(), VecRestoreArray(), VecReplaceArray(), VecPlaceArray(), VecResetArray(), VecHIPPlaceArray(), VecHIPReplaceArray()

src/vec/vec/impls/seq/cupm/hip/vecseqcupm.hip.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecHIPResetArray(Vec vin)
```

Example 2 (unknown):
```unknown
VecHIPPlaceArray()
```

Example 3 (unknown):
```unknown
VecGetArray()
```

Example 4 (unknown):
```unknown
VecRestoreArray()
```

---

## VecHIPRestoreArrayRead#

**URL:** https://petsc.org/release/manualpages/Vec/VecHIPRestoreArrayRead/

**Contents:**
- VecHIPRestoreArrayRead#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Restore a HIP device pointer previously acquired with VecHIPGetArrayRead().

Not Collective; Asynchronous; No Fortran Support

a - the HIP device pointer

This routine does not modify the corresponding array on the host in any way. The pointer is invalid after this function returns.

Vectors and Parallel Data, VecHIPGetArrayRead(), VecHIPGetArrayWrite(), VecHIPGetArray(), VecGetArray(), VecRestoreArray(), VecGetArrayRead()

src/vec/vec/impls/seq/cupm/hip/vecseqcupm.hip.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecHIPGetArrayRead()
```

Example 2 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecHIPRestoreArrayRead(Vec v, const PetscScalar **a)
```

Example 3 (unknown):
```unknown
VecHIPGetArrayRead()
```

Example 4 (unknown):
```unknown
VecHIPGetArrayWrite()
```

---

## VecHIPRestoreArrayWrite#

**URL:** https://petsc.org/release/manualpages/Vec/VecHIPRestoreArrayWrite/

**Contents:**
- VecHIPRestoreArrayWrite#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Restore a HIP device pointer previously acquired with VecHIPGetArrayWrite().

Logically Collective; Asynchronous; No Fortran Support

a - the HIP device pointer. This pointer is invalid after VecHIPRestoreArrayWrite() returns.

Data on the host will be marked as out of date. Subsequent access of the data on the host side e.g. with VecGetArray() will incur a device to host data transfer.

Vectors and Parallel Data, VecHIPGetArrayWrite(), VecHIPGetArray(), VecHIPGetArrayRead(), VecHIPGetArrayWrite(), VecGetArray(), VecRestoreArray(), VecGetArrayRead()

src/vec/vec/impls/seq/cupm/hip/vecseqcupm.hip.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecHIPGetArrayWrite()
```

Example 2 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecHIPRestoreArrayWrite(Vec v, PetscScalar **a)
```

Example 3 (unknown):
```unknown
VecHIPRestoreArrayWrite()
```

Example 4 (unknown):
```unknown
VecGetArray()
```

---

## VecHIPRestoreArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecHIPRestoreArray/

**Contents:**
- VecHIPRestoreArray#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Restore a device buffer previously acquired with VecHIPGetArray().

Logically Collective; Asynchronous; No Fortran Support

a - the device buffer

The restored pointer is invalid after this function returns. This function also marks the host data as out of date. Subsequent access to the vector data on the host side via VecGetArray() will incur a (synchronous) data transfer.

Vectors and Parallel Data, VecHIPGetArray(), VecHIPGetArrayRead(), VecHIPGetArrayWrite(), VecGetArray(), VecRestoreArray(), VecGetArrayRead()

src/vec/vec/impls/seq/cupm/hip/vecseqcupm.hip.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecHIPGetArray()
```

Example 2 (cpp):
```cpp
#include <petscvec.h> 
PetscErrorCode VecHIPRestoreArray(Vec v, PetscScalar **a)
```

Example 3 (unknown):
```unknown
VecGetArray()
```

Example 4 (unknown):
```unknown
VecHIPGetArray()
```

---

## VECHIP#

**URL:** https://petsc.org/release/manualpages/Vec/VECHIP/

**Contents:**
- VECHIP#
- Options Database Key#
- See Also#
- Level#
- Location#

VECHIP = “hip” - A VECSEQHIP on a single-process MPI communicator, and VECMPIHIP otherwise.

-vec_type hip - sets the vector type to VECHIP during a call to VecSetFromOptions()

VecCreate(), VecSetType(), VecSetFromOptions(), VecCreateMPIWithArray(), VECSEQHIP, VECMPIHIP, VECSTANDARD, VecType, VecCreateMPI(), VecSetPinnedMemoryMin(), VECCUDA

src/vec/vec/impls/mpi/cupm/hip/vecmpicupm.hip.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecSetFromOptions()
```

Example 2 (unknown):
```unknown
VecCreate()
```

Example 3 (unknown):
```unknown
VecSetType()
```

Example 4 (unknown):
```unknown
VecSetFromOptions()
```

---

## VecImaginaryPart#

**URL:** https://petsc.org/release/manualpages/Vec/VecImaginaryPart/

**Contents:**
- VecImaginaryPart#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Replaces a complex vector with its imaginary part

Vec, VecNorm(), VecRealPart()

src/vec/vec/utils/vinv.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecImaginaryPart(Vec v)
```

Example 2 (unknown):
```unknown
VecRealPart()
```

---

## VecInitializePackage#

**URL:** https://petsc.org/release/manualpages/Vec/VecInitializePackage/

**Contents:**
- VecInitializePackage#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#

This function initializes everything in the Vec package. It is called from PetscDLLibraryRegister_petscvec() when using dynamic libraries, and on the first call to VecCreate() when using shared or static libraries.

This function never needs to be called by PETSc users.

src/vec/vec/interface/dlregisvec.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecCreate()
```

Example 2 (unknown):
```unknown
#include "petscvec.h" */
PetscErrorCode VecInitializePackage(void)
```

Example 3 (unknown):
```unknown
PetscInitialize()
```

---

## VecISAXPY#

**URL:** https://petsc.org/release/manualpages/Vec/VecISAXPY/

**Contents:**
- VecISAXPY#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Adds a reduced vector to the appropriate elements of a full-space vector. vfull[is[i]] += alpha*vreduced[i]

vfull - the full-space vector

is - the index set for the reduced space

alpha - the scalar coefficient

vreduced - the reduced-space vector

vfull - the sum of the full-space vector and reduced-space vector

The index set identifies entries in the global vector. Negative indices are skipped; indices outside the ownership range of vfull will raise an error.

VecISCopy(), VecISSet(), VecAXPY()

src/vec/vec/utils/projection.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"  
PetscErrorCode VecISAXPY(Vec vfull, IS is, PetscScalar alpha, Vec vreduced)
```

Example 2 (unknown):
```unknown
VecISCopy()
```

---

## VecISCopy#

**URL:** https://petsc.org/release/manualpages/Vec/VecISCopy/

**Contents:**
- VecISCopy#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Copies between a reduced vector and the appropriate elements of a full-space vector.

vfull - the full-space vector

is - the index set for the reduced space

mode - the direction of copying, SCATTER_FORWARD or SCATTER_REVERSE

vreduced - the reduced-space vector

vfull - the sum of the full-space vector and reduced-space vector

The index set identifies entries in the global vector. Negative indices are skipped; indices outside the ownership range of vfull will raise an error.

VecISSet(), VecISAXPY(), VecCopy()

src/vec/vec/utils/projection.c

src/snes/tutorials/ex13.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"  
PetscErrorCode VecISCopy(Vec vfull, IS is, ScatterMode mode, Vec vreduced)
```

Example 2 (unknown):
```unknown
SCATTER_FORWARD
```

Example 3 (unknown):
```unknown
SCATTER_REVERSE
```

Example 4 (unknown):
```unknown
mode == SCATTER_FORWARD: vfull[is[i]] = vreduced[i]
    mode == SCATTER_REVERSE: vreduced[i] = vfull[is[i]]
```

---

## VecISSet#

**URL:** https://petsc.org/release/manualpages/Vec/VecISSet/

**Contents:**
- VecISSet#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the elements of a vector, specified by an index set, to a constant

S - index set for the locations in the vector

The index set identifies entries in the global vector. Negative indices are skipped; indices outside the ownership range of V will raise an error.

VecISCopy(), VecISAXPY(), VecISShift(), VecSet()

src/vec/vec/utils/projection.c

src/ts/tutorials/ex30.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"  
PetscErrorCode VecISSet(Vec V, IS S, PetscScalar c)
```

Example 2 (unknown):
```unknown
VecISCopy()
```

Example 3 (unknown):
```unknown
VecISAXPY()
```

Example 4 (unknown):
```unknown
VecISShift()
```

---

## VecISShift#

**URL:** https://petsc.org/release/manualpages/Vec/VecISShift/

**Contents:**
- VecISShift#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Shifts the elements of a vector, specified by an index set, by a constant

S - index set for the locations in the vector

The index set identifies entries in the global vector. Negative indices are skipped; indices outside the ownership range of V will raise an error.

VecISCopy(), VecISAXPY(), VecISSet(), VecShift()

src/vec/vec/utils/projection.c

src/ts/tutorials/ex30.c src/snes/tutorials/ex11.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"  
PetscErrorCode VecISShift(Vec V, IS S, PetscScalar c)
```

Example 2 (unknown):
```unknown
VecISCopy()
```

Example 3 (unknown):
```unknown
VecISAXPY()
```

---

## VecKokkosPlaceArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecKokkosPlaceArray/

**Contents:**
- VecKokkosPlaceArray#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Allows one to replace the device array in a VecKokkos vector with a device array provided by the user. This is useful to avoid copying an array into a vector.

Logically Collective; No Fortran Support

v - the VecKokkos vector

You can return to the original array with a call to VecKokkosResetArray(). vec does not take ownership of array in any way.

The user manages the device array so PETSc doesn’t care how it was allocated.

The user must free array themselves but be careful not to do so before the vector has either been destroyed, had its original array restored with VecKokkosResetArray() or permanently replaced with VecReplaceArray().

Vectors and Parallel Data, Vec, VecGetArray(), VecKokkosResetArray(), VecReplaceArray(), VecResetArray()

src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode VecKokkosPlaceArray(Vec v, PetscScalar *a)
```

Example 2 (unknown):
```unknown
VecKokkosResetArray()
```

Example 3 (unknown):
```unknown
VecKokkosResetArray()
```

Example 4 (unknown):
```unknown
VecReplaceArray()
```

---

## VecKokkosResetArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecKokkosResetArray/

**Contents:**
- VecKokkosResetArray#
- Synopsis#
- Input Parameter#
- Notes#
- See Also#
- Level#
- Location#

Resets a vector to use its default memory. Call this after the use of VecKokkosPlaceArray().

After the call, the original array placed in with VecKokkosPlaceArray() will contain the latest value of the vector. Note that device kernels are asynchronous. Users are responsible to sync the device if they wish to have immediate access to the data in the array. Also, after the call, v will contain whatever data before VecKokkosPlaceArray().

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecReplaceArray(), VecKokkosPlaceArray()

src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecKokkosPlaceArray()
```

Example 2 (unknown):
```unknown
PetscErrorCode VecKokkosResetArray(Vec v)
```

Example 3 (unknown):
```unknown
VecKokkosPlaceArray()
```

Example 4 (unknown):
```unknown
VecKokkosPlaceArray()
```

---

## VECKOKKOS#

**URL:** https://petsc.org/release/manualpages/Vec/VECKOKKOS/

**Contents:**
- VECKOKKOS#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#

VECKOKKOS = “kokkos” - The basic vector, modified to use Kokkos

-vec_type kokkos - sets the vector type to VECKOKKOS during a call to VecSetFromOptions()

VecCreate(), VecSetType(), VecSetFromOptions(), VecCreateMPIKokkosWithArray(), VECMPI, VecType, VecCreateMPI()

src/vec/vec/impls/mpi/kokkos/mpikok.kokkos.cxx

src/snes/tutorials/ex55.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecCreate()
```

Example 2 (unknown):
```unknown
VecSetType()
```

Example 3 (unknown):
```unknown
VecSetFromOptions()
```

Example 4 (unknown):
```unknown
VecCreateMPIKokkosWithArray()
```

---

## VecLoad#

**URL:** https://petsc.org/release/manualpages/Vec/VecLoad/

**Contents:**
- VecLoad#
- Synopsis#
- Input Parameters#
- Notes#
- Notes for advanced users when using the binary viewer#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Loads a vector that has been stored in binary or HDF5 format with VecView().

vec - the newly loaded vector, this needs to have been created with VecCreate() or some related function before the call to VecLoad().

viewer - binary file viewer, obtained from PetscViewerBinaryOpen() or HDF5 file viewer, obtained from PetscViewerHDF5Open()

Defaults to the standard VECSEQ or VECMPI, if you want some other type of Vec call VecSetFromOptions() before calling this.

The input file must contain the full global vector, as written by the routine VecView().

If the type or size of vec is not set before a call to VecLoad(), PETSc sets the type and the local and global sizes based on the vector it is reading in. If type and/or sizes are already set, then the same are used.

If using the binary viewer and the blocksize of the vector is greater than one then you must provide a unique prefix to the vector with PetscObjectSetOptionsPrefix((PetscObject)vec,”uniqueprefix”); BEFORE calling VecView() on the vector to be stored and then set that same unique prefix on the vector that you pass to VecLoad(). The blocksize information is stored in an ASCII file with the same name as the binary file plus a “.info” appended to the filename. If you copy the binary file, make sure you copy the associated .info file with it.

If using HDF5, you must assign the Vec the same name as was used in the Vec that was stored in the file using PetscObjectSetName(). Otherwise you will get the error message: “Cannot H5DOpen2() with Vec name NAMEOFOBJECT”.

If the HDF5 file contains a two dimensional array the first dimension is treated as the block size in loading the vector. Hence, for example, using MATLAB notation h5create(‘vector.dat’,’/Test_Vec’,[27 1]); will load a vector of size 27 and block size 27 thus resulting in all 27 entries being on the first process of vectors communicator and the rest of the processes having zero entries

Most users should not need to know the details of the binary storage format, since VecLoad() and VecView() completely hide these details. But for anyone who’s interested, the standard binary vector storage format is

In addition, PETSc automatically uses byte swapping to work on all machines; the files are written ALWAYS using big-endian ordering. On small-endian machines the numbers are converted to the small-endian format when they are read in from the file. See PetscBinaryRead() and PetscBinaryWrite() to see how this may be done.

Vectors and Parallel Data, Vec, PetscViewerBinaryOpen(), VecView(), MatLoad()

src/vec/vec/interface/vector.c

src/ksp/pc/tutorials/ex4.c src/ksp/ksp/tutorials/ex41.c src/ksp/ksp/tutorials/ex72.c src/ksp/ksp/tutorials/ex10.c src/ksp/ksp/tutorials/ex75.c src/snes/tutorials/ex12.c src/ksp/ksp/tutorials/ex75f.F90 src/mat/tutorials/ex12.c src/ksp/ksp/tutorials/ex27.c

VecLoad_pforest() in src/dm/impls/forest/p4est/pforest.h VecLoad_Plex() in src/dm/impls/plex/plex.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecLoad(Vec vec, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
VecCreate()
```

Example 3 (unknown):
```unknown
PetscViewerBinaryOpen()
```

Example 4 (unknown):
```unknown
PetscViewerHDF5Open()
```

---

## VecLocked#

**URL:** https://petsc.org/release/manualpages/Vec/VecLocked/

**Contents:**
- VecLocked#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Deprecated alias for VecSetErrorIfLocked(); raises an error if the Vec is currently locked for read

Not Collective; No Fortran Support

arg - the argument position of x in the caller (used in the error message)

Use VecSetErrorIfLocked() in new code; this macro is retained only for backwards compatibility.

Vec, VecSetErrorIfLocked(), VecLockReadPush(), VecLockReadPop()

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecSetErrorIfLocked()
```

Example 2 (cpp):
```cpp
#include <petscvec.h>
PetscErrorCode VecLocked(Vec x, int arg)
```

Example 3 (unknown):
```unknown
VecSetErrorIfLocked()
```

Example 4 (unknown):
```unknown
VecSetErrorIfLocked()
```

---

## VecLockGetLocation#

**URL:** https://petsc.org/release/manualpages/Vec/VecLockGetLocation/

**Contents:**
- VecLockGetLocation#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Return the source code location where a Vec was most recently read-locked

file - the source file name of the most recent VecLockReadPush(), or NULL if none is active

func - the function name of the most recent VecLockReadPush(), or NULL if none is active

line - the source line number of the most recent VecLockReadPush(), or 0 if none is active

Only produces meaningful output when PETSc is built with PETSC_USE_DEBUG and without threadsafety; otherwise NULL and 0 are returned. Intended to help debug read-lock violations reported by VecGetArray() and similar routines.

Vec, VecLockGet(), VecLockReadPush(), VecLockReadPop(), VecGetArray()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecLockGetLocation(Vec x, const char *file[], const char *func[], int *line)
```

Example 2 (unknown):
```unknown
VecLockReadPush()
```

Example 3 (unknown):
```unknown
VecLockReadPush()
```

Example 4 (unknown):
```unknown
VecLockReadPush()
```

---

## VecLockGet#

**URL:** https://petsc.org/release/manualpages/Vec/VecLockGet/

**Contents:**
- VecLockGet#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the current lock status of a vector

state - greater than zero indicates the vector is locked for read; less than zero indicates the vector is locked for write; equal to zero means the vector is unlocked, that is, it is free to read or write.

Vectors and Parallel Data, Vec, VecRestoreArray(), VecGetArrayRead(), VecLockReadPush(), VecLockReadPop()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecLockGet(Vec x, PetscInt *state)
```

Example 2 (unknown):
```unknown
VecRestoreArray()
```

Example 3 (unknown):
```unknown
VecGetArrayRead()
```

Example 4 (unknown):
```unknown
VecLockReadPush()
```

---

## VecLockReadPop#

**URL:** https://petsc.org/release/manualpages/Vec/VecLockReadPop/

**Contents:**
- VecLockReadPop#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Pop a read-only lock from a vector

Vectors and Parallel Data, Vec, VecRestoreArray(), VecGetArrayRead(), VecLockReadPush(), VecLockGet()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecLockReadPop(Vec x)
```

Example 2 (unknown):
```unknown
VecRestoreArray()
```

Example 3 (unknown):
```unknown
VecGetArrayRead()
```

Example 4 (unknown):
```unknown
VecLockReadPush()
```

---

## VecLockReadPush#

**URL:** https://petsc.org/release/manualpages/Vec/VecLockReadPush/

**Contents:**
- VecLockReadPush#
- Synopsis#
- Input Parameter#
- Notes#
- See Also#
- Level#
- Location#

Push a read-only lock on a vector to prevent it from being written to

If this is set then calls to VecGetArray() or VecSetValues() or any other routines that change the vectors values will generate an error.

The call can be nested, i.e., called multiple times on the same vector, but each VecLockReadPush() has to have one matching VecLockReadPop(), which removes the latest read-only lock.

Vectors and Parallel Data, Vec, VecRestoreArray(), VecGetArrayRead(), VecLockReadPop(), VecLockGet()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecLockReadPush(Vec x)
```

Example 2 (unknown):
```unknown
VecGetArray()
```

Example 3 (unknown):
```unknown
VecSetValues()
```

Example 4 (unknown):
```unknown
VecLockReadPush()
```

---

## VecLockWriteSet#

**URL:** https://petsc.org/release/manualpages/Vec/VecLockWriteSet/

**Contents:**
- VecLockWriteSet#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Lock or unlock a vector for exclusive read/write access

flg - PETSC_TRUE to lock the vector for exclusive read/write access; PETSC_FALSE to unlock it.

The function is useful in split-phase computations, which usually have a begin phase and an end phase. One can call VecLockWriteSet(x,PETSC_TRUE) in the begin phase to lock a vector for exclusive access, and call VecLockWriteSet(x,PETSC_FALSE) in the end phase to unlock the vector from exclusive access. In this way, one is ensured no other operations can access the vector in between. The code may like

The call can not be nested on the same vector, in other words, one can not call VecLockWriteSet(x,PETSC_TRUE) again before calling VecLockWriteSet(v,PETSC_FALSE).

Vectors and Parallel Data, Vec, VecRestoreArray(), VecGetArrayRead(), VecLockReadPush(), VecLockReadPop(), VecLockGet()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecLockWriteSet(Vec x, PetscBool flg)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
VecLockWriteSet
```

Example 4 (unknown):
```unknown
VecLockWriteSet
```

---

## VecLog#

**URL:** https://petsc.org/release/manualpages/Vec/VecLog/

**Contents:**
- VecLog#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Replaces each component of a vector by log(x_i), the natural logarithm

v - The vector of logs

Vec, VecExp(), VecAbs(), VecSqrtAbs(), VecReciprocal()

src/vec/vec/utils/vinv.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecLog(Vec v)
```

Example 2 (unknown):
```unknown
VecSqrtAbs()
```

Example 3 (unknown):
```unknown
VecReciprocal()
```

---

## VecMAXPBY#

**URL:** https://petsc.org/release/manualpages/Vec/VecMAXPBY/

**Contents:**
- VecMAXPBY#
- Synopsis#
- Input Parameters#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#

Computes y = beta y + sum alpha[i] x[i]

nv - number of scalars and x vectors

alpha - array of scalars

y cannot be any of the x vectors.

This is a convenience routine, but implementations might be able to optimize it, for example, when beta is zero.

Vectors and Parallel Data, Vec, VecMAXPY(), VecAYPX(), VecWAXPY(), VecAXPY(), VecAXPBYPCZ(), VecAXPBY()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
y = beta y + sum alpha[i] x[i]
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecMAXPBY(Vec y, PetscInt nv, const PetscScalar alpha[], PetscScalar beta, Vec x[])
```

Example 3 (unknown):
```unknown
VecAXPBYPCZ()
```

---

## VecMaxPointwiseDivide#

**URL:** https://petsc.org/release/manualpages/Vec/VecMaxPointwiseDivide/

**Contents:**
- VecMaxPointwiseDivide#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Computes the maximum of the componentwise division max = max_i abs(x[i]/y[i]).

x and y may be the same vector

if a particular y[i] is zero, it is treated as 1 in the above formula

Vectors and Parallel Data, Vec, VecPointwiseDivide(), VecPointwiseMult(), VecPointwiseMax(), VecPointwiseMin(), VecPointwiseMaxAbs()

src/vec/vec/interface/rvector.c

VecMaxPointwiseDivide_MPI() in src/vec/vec/impls/mpi/pvec2.c VecMaxPointwiseDivide_Nest() in src/vec/vec/impls/nest/vecnest.c VecMaxPointwiseDivide_Seq() in src/vec/vec/impls/seq/dvec2.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
max = max_i abs(x[i]/y[i])
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecMaxPointwiseDivide(Vec x, Vec y, PetscReal *max)
```

Example 3 (unknown):
```unknown
VecPointwiseDivide()
```

Example 4 (unknown):
```unknown
VecPointwiseMult()
```

---

## VecMAXPY#

**URL:** https://petsc.org/release/manualpages/Vec/VecMAXPY/

**Contents:**
- VecMAXPY#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Computes y = y + sum alpha[i] x[i]

nv - number of scalars and x vectors

alpha - array of scalars

y cannot be any of the x vectors

The implementation may use BLAS 2 operations when the vectors y have been obtained with VecDuplicateVecs()

Vectors and Parallel Data, Vec, VecMAXPBY(), VecAYPX(), VecWAXPY(), VecAXPY(), VecAXPBYPCZ(), VecAXPBY(), VecDuplicateVecs()

src/vec/vec/interface/rvector.c

src/vec/vec/tutorials/ex20f90.F90 src/vec/vec/tutorials/ex1.c src/vec/vec/tutorials/ex1f90.F90 src/ts/tutorials/ex31.c

VecMAXPY_Nest() in src/vec/vec/impls/nest/vecnest.c VecMAXPY_Seq() in src/vec/vec/impls/seq/dvec2.c VecMAXPY_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecMAXPY_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
y = y + sum alpha[i] x[i]
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecMAXPY(Vec y, PetscInt nv, const PetscScalar alpha[], Vec x[])
```

Example 3 (unknown):
```unknown
VecDuplicateVecs()
```

Example 4 (unknown):
```unknown
VecMAXPBY()
```

---

## VecMax#

**URL:** https://petsc.org/release/manualpages/Vec/VecMax/

**Contents:**
- VecMax#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Determines the vector component with maximum real part and its location.

p - the index of val (pass NULL if you don’t want this) in the vector

val - the maximum component

Returns the value PETSC_MIN_REAL and negative p if the vector is of length 0.

Returns the smallest index with the maximum value

The Nag Fortran compiler does not like the symbol name VecMax

Vectors and Parallel Data, Vec, VecNorm(), VecMin()

src/vec/vec/interface/rvector.c

src/ts/tutorials/ex9.c src/ts/tutorials/ex17.c src/ksp/ksp/tutorials/ex72.c src/vec/vec/tutorials/ex1.c src/dm/tutorials/ex15.c

VecMax_MPIKokkos() in src/vec/vec/impls/mpi/kokkos/mpikok.kokkos.cxx VecMax_MPI() in src/vec/vec/impls/mpi/pvec2.c VecMax_Nest() in src/vec/vec/impls/nest/vecnest.c VecMax_Seq() in src/vec/vec/impls/seq/dvec2.c VecMax_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecMax(Vec x, PetscInt *p, PetscReal *val)
```

Example 2 (unknown):
```unknown
PETSC_MIN_REAL
```

---

## VecMDotBegin#

**URL:** https://petsc.org/release/manualpages/Vec/VecMDotBegin/

**Contents:**
- VecMDotBegin#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Starts a split phase multiple dot product computation.

nv - number of vectors

result - where the result will go (can be NULL)

Each call to VecMDotBegin() should be paired with a call to VecMDotEnd().

VecMDotEnd(), VecNormBegin(), VecNormEnd(), VecNorm(), VecDot(), VecMDot(), VecTDotBegin(), VecTDotEnd(), VecMTDotBegin(), VecMTDotEnd(), PetscCommSplitReductionBegin()

src/vec/vec/utils/comb.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"    
PetscErrorCode VecMDotBegin(Vec x, PetscInt nv, const Vec y[], PetscScalar result[])
```

Example 2 (unknown):
```unknown
VecMDotBegin()
```

Example 3 (unknown):
```unknown
VecMDotEnd()
```

Example 4 (unknown):
```unknown
VecMDotEnd()
```

---

## VecMDotEnd#

**URL:** https://petsc.org/release/manualpages/Vec/VecMDotEnd/

**Contents:**
- VecMDotEnd#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Ends a split phase multiple dot product computation.

x - the first vector (can be NULL)

nv - number of vectors

y - array of vectors (can be NULL)

result - where the result will go

Each call to VecMDotBegin() should be paired with a call to VecMDotEnd().

VecMDotBegin(), VecNormBegin(), VecNormEnd(), VecNorm(), VecDot(), VecMDot(), VecTDotBegin(), VecTDotEnd(), VecMTDotBegin(), VecMTDotEnd(), PetscCommSplitReductionBegin()

src/vec/vec/utils/comb.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"    
PetscErrorCode VecMDotEnd(Vec x, PetscInt nv, const Vec y[], PetscScalar result[])
```

Example 2 (unknown):
```unknown
VecMDotBegin()
```

Example 3 (unknown):
```unknown
VecMDotEnd()
```

Example 4 (unknown):
```unknown
VecMDotBegin()
```

---

## VecMDot#

**URL:** https://petsc.org/release/manualpages/Vec/VecMDot/

**Contents:**
- VecMDot#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes for Users of Complex Numbers#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Computes multiple vector dot products.

nv - number of vectors

y - array of vectors.

val - array of the dot products (does not allocate the array)

For complex vectors, VecMDot() computes

where y^H denotes the conjugate transpose of y.

Use VecMTDot() for the indefinite form

where y^T denotes the transpose of y.

The implementation may use BLAS 2 operations when the vectors y have been obtained with VecDuplicateVecs()

Vectors and Parallel Data, Vec, VecMTDot(), VecDot(), VecDuplicateVecs()

src/vec/vec/interface/rvector.c

src/vec/vec/tutorials/ex20f90.F90 src/vec/vec/tutorials/ex1.c src/vec/vec/tutorials/ex1f90.F90

VecMDot_MPIKokkos() in src/vec/vec/impls/mpi/kokkos/mpikok.kokkos.cxx VecMDot_MPIViennaCL() in src/vec/vec/impls/mpi/mpiviennacl/mpiviennacl.cxx VecMDot_MPI() in src/vec/vec/impls/mpi/pvec2.c VecMDot_Nest() in src/vec/vec/impls/nest/vecnest.c VecMDot_Seq() in src/vec/vec/impls/seq/dvec2.c VecMDot_Seq() in src/vec/vec/impls/seq/dvec2.c VecMDot_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecMDot_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecMDot(Vec x, PetscInt nv, const Vec y[], PetscScalar val[])
```

Example 2 (unknown):
```unknown
val = (x,y) = y^H x,
```

Example 3 (unknown):
```unknown
val = (x,y) = y^T x,
```

Example 4 (unknown):
```unknown
VecDuplicateVecs()
```

---

## VecMean#

**URL:** https://petsc.org/release/manualpages/Vec/VecMean/

**Contents:**
- VecMean#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Computes the arithmetic mean of all the components of a vector.

Vec, VecSum(), VecNorm()

src/vec/vec/utils/vinv.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecMean(Vec v, PetscScalar *mean)
```

---

## VecMedian#

**URL:** https://petsc.org/release/manualpages/Vec/VecMedian/

**Contents:**
- VecMedian#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Computes the componentwise median of three vectors and stores the result in this vector. Used primarily for projecting a vector within upper and lower bounds.

Vec1 - The first vector

Vec2 - The second vector

Vec3 - The third vector

VMedian - The median vector (this can be any one of the input vectors)

src/vec/vec/utils/projection.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"  
PetscErrorCode VecMedian(Vec Vec1, Vec Vec2, Vec Vec3, Vec VMedian)
```

---

## VecMin#

**URL:** https://petsc.org/release/manualpages/Vec/VecMin/

**Contents:**
- VecMin#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Determines the vector component with minimum real part and its location.

p - the index of val (pass NULL if you don’t want this location) in the vector

val - the minimum component

Returns the value PETSC_MAX_REAL and negative p if the vector is of length 0.

This returns the smallest index with the minimum value

The Nag Fortran compiler does not like the symbol name VecMin

Vectors and Parallel Data, Vec, VecMax()

src/vec/vec/interface/rvector.c

src/ts/tutorials/ex29.c src/ts/tutorials/ex9.c src/ts/tutorials/ex17.c src/ksp/ksp/tutorials/ex72.c src/vec/vec/tutorials/ex1.c src/ts/tutorials/ex27.c src/ts/tutorials/ex10.c src/dm/tutorials/ex15.c

VecMin_MPIKokkos() in src/vec/vec/impls/mpi/kokkos/mpikok.kokkos.cxx VecMin_MPI() in src/vec/vec/impls/mpi/pvec2.c VecMin_Nest() in src/vec/vec/impls/nest/vecnest.c VecMin_Seq() in src/vec/vec/impls/seq/dvec2.c VecMin_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecMin(Vec x, PetscInt *p, PetscReal *val)
```

Example 2 (unknown):
```unknown
PETSC_MAX_REAL
```

---

## VECMPICUDA#

**URL:** https://petsc.org/release/manualpages/Vec/VECMPICUDA/

**Contents:**
- VECMPICUDA#
- Options Database Keys#
- See Also#
- Level#
- Location#

VECMPICUDA = “mpicuda” - The basic parallel vector, modified to use CUDA

-vec_type mpicuda - sets the vector type to VECMPICUDA during a call to VecSetFromOptions()

VecCreate(), VecSetType(), VecSetFromOptions(), VecCreateMPIWithArray(), VECMPI, VecType, VecCreateMPI(), VecSetPinnedMemoryMin(), VECSEQHIP, VECMPIHIP

src/vec/vec/impls/mpi/cupm/cuda/vecmpicupm.cu

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecSetFromOptions()
```

Example 2 (unknown):
```unknown
VecCreate()
```

Example 3 (unknown):
```unknown
VecSetType()
```

Example 4 (unknown):
```unknown
VecSetFromOptions()
```

---

## VECMPIHIP#

**URL:** https://petsc.org/release/manualpages/Vec/VECMPIHIP/

**Contents:**
- VECMPIHIP#
- Options Database Key#
- See Also#
- Level#
- Location#

VECMPIHIP = “mpihip” - The basic parallel vector, modified to use HIP

-vec_type mpihip - sets the vector type to VECMPIHIP during a call to VecSetFromOptions()

VecCreate(), VecSetType(), VecSetFromOptions(), VecCreateMPIWithArray(), VECMPI, VecType, VecCreateMPI(), VecSetPinnedMemoryMin()

src/vec/vec/impls/mpi/cupm/hip/vecmpicupm.hip.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecSetFromOptions()
```

Example 2 (unknown):
```unknown
VecCreate()
```

Example 3 (unknown):
```unknown
VecSetType()
```

Example 4 (unknown):
```unknown
VecSetFromOptions()
```

---

## VECMPIKOKKOS#

**URL:** https://petsc.org/release/manualpages/Vec/VECMPIKOKKOS/

**Contents:**
- VECMPIKOKKOS#
- Options Database Keys#
- See Also#
- Level#
- Location#

VECMPIKOKKOS = “mpikokkos” - The basic parallel vector, modified to use Kokkos

-vec_type mpikokkos - sets the vector type to VECMPIKOKKOS during a call to VecSetFromOptions()

VecCreate(), VecSetType(), VecSetFromOptions(), VecCreateMPIKokkosWithArray(), VECMPI, VecType, VecCreateMPI()

src/vec/vec/impls/mpi/kokkos/mpikok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecCreate()
```

Example 2 (unknown):
```unknown
VecSetType()
```

Example 3 (unknown):
```unknown
VecSetFromOptions()
```

Example 4 (unknown):
```unknown
VecCreateMPIKokkosWithArray()
```

---

## VecMPISetGhost#

**URL:** https://petsc.org/release/manualpages/Vec/VecMPISetGhost/

**Contents:**
- VecMPISetGhost#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the ghost points for an MPI ghost vector

nghost - number of local ghost points

ghosts - global indices of ghost points, these do not need to be in increasing order (sorted)

Use VecGhostGetLocalForm() to access the local, ghosted representation of the vector.

This also automatically sets the ISLocalToGlobalMapping() for this vector.

You must call this AFTER you have set the type of the vector (with VecSetType()) and the size (with VecSetSizes()).

Vectors and Parallel Data, Vec, VecType, VecCreateSeq(), VecCreate(), VecDuplicate(), VecDuplicateVecs(), VecCreateMPI(), VecGhostGetLocalForm(), VecGhostRestoreLocalForm(), VecGhostUpdateBegin(), VecCreateGhostWithArray(), VecCreateMPIWithArray(), VecGhostUpdateEnd(), VecCreateGhostBlock(), VecCreateGhostBlockWithArray()

src/vec/vec/impls/mpi/pbvec.c

src/vec/vec/tutorials/ex9.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecMPISetGhost(Vec vv, PetscInt nghost, const PetscInt ghosts[])
```

Example 2 (unknown):
```unknown
VecGhostGetLocalForm()
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMapping()
```

Example 4 (unknown):
```unknown
VecSetType()
```

---

## VECMPIVIENNACL#

**URL:** https://petsc.org/release/manualpages/Vec/VECMPIVIENNACL/

**Contents:**
- VECMPIVIENNACL#
- Options Database Keys#
- See Also#
- Level#
- Location#

VECMPIVIENNACL = “mpiviennacl” - The basic parallel vector, modified to use ViennaCL

-vec_type mpiviennacl - sets the vector type to VECMPIVIENNACL during a call to VecSetFromOptions()

VecCreate(), VecSetType(), VecSetFromOptions(), VecCreateMPIWithArray(), VECMPI, VecType, VecCreateMPI()

src/vec/vec/impls/mpi/mpiviennacl/mpiviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecCreate()
```

Example 2 (unknown):
```unknown
VecSetType()
```

Example 3 (unknown):
```unknown
VecSetFromOptions()
```

Example 4 (unknown):
```unknown
VecCreateMPIWithArray()
```

---

## VECMPI#

**URL:** https://petsc.org/release/manualpages/Vec/VECMPI/

**Contents:**
- VECMPI#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

VECMPI = “mpi” - The basic parallel vector

-vec_type mpi - sets the vector type to VECMPI during a call to VecSetFromOptions()

Vectors and Parallel Data, Vec, VecType, VecCreate(), VecSetType(), VecSetFromOptions(), VecCreateMPIWithArray(), VECSEQ, VecCreateMPI()

src/vec/vec/impls/mpi/pbvec.c

src/vec/vec/tutorials/ex10.c src/vec/vec/tutorials/ex9.c src/snes/tutorials/ex70.c src/tao/pde_constrained/tutorials/hyperbolic.c src/tao/constrained/tutorials/maros.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecSetFromOptions()
```

Example 2 (unknown):
```unknown
VecCreate()
```

Example 3 (unknown):
```unknown
VecSetType()
```

Example 4 (unknown):
```unknown
VecSetFromOptions()
```

---

## VecMTDotBegin#

**URL:** https://petsc.org/release/manualpages/Vec/VecMTDotBegin/

**Contents:**
- VecMTDotBegin#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Starts a split phase transpose multiple dot product computation.

nv - number of vectors

result - where the result will go (can be NULL)

Each call to VecMTDotBegin() should be paired with a call to VecMTDotEnd().

VecMTDotEnd(), VecNormBegin(), VecNormEnd(), VecNorm(), VecDot(), VecMDot(), VecDotBegin(), VecDotEnd(), VecMDotBegin(), VecMDotEnd(), PetscCommSplitReductionBegin()

src/vec/vec/utils/comb.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"    
PetscErrorCode VecMTDotBegin(Vec x, PetscInt nv, const Vec y[], PetscScalar result[])
```

Example 2 (unknown):
```unknown
VecMTDotBegin()
```

Example 3 (unknown):
```unknown
VecMTDotEnd()
```

Example 4 (unknown):
```unknown
VecMTDotEnd()
```

---

## VecMTDotEnd#

**URL:** https://petsc.org/release/manualpages/Vec/VecMTDotEnd/

**Contents:**
- VecMTDotEnd#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Ends a split phase transpose multiple dot product computation.

x - the first vector (can be NULL)

nv - number of vectors

y - array of vectors (can be NULL)

result - where the result will go

Each call to VecTDotBegin() should be paired with a call to VecTDotEnd().

VecMTDotBegin(), VecNormBegin(), VecNormEnd(), VecNorm(), VecDot(), VecMDot(), VecDotBegin(), VecDotEnd(), VecMDotBegin(), VecMDotEnd(), PetscCommSplitReductionBegin()

src/vec/vec/utils/comb.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"    
PetscErrorCode VecMTDotEnd(Vec x, PetscInt nv, const Vec y[], PetscScalar result[])
```

Example 2 (unknown):
```unknown
VecTDotBegin()
```

Example 3 (unknown):
```unknown
VecTDotEnd()
```

Example 4 (unknown):
```unknown
VecMTDotBegin()
```

---

## VecMTDot#

**URL:** https://petsc.org/release/manualpages/Vec/VecMTDot/

**Contents:**
- VecMTDot#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes for Users of Complex Numbers#
- See Also#
- Level#
- Location#
- Implementations#

Computes indefinite vector multiple dot products. That is, it does NOT use the complex conjugate.

nv - number of vectors

y - array of vectors. Note that vectors are pointers

val - array of the dot products

For complex vectors, VecMTDot() computes the indefinite form

where y^T denotes the transpose of y.

Use VecMDot() for the inner product

where y^H denotes the conjugate transpose of y.

Vectors and Parallel Data, Vec, VecMDot(), VecTDot()

src/vec/vec/interface/rvector.c

VecMTDot_MPIKokkos() in src/vec/vec/impls/mpi/kokkos/mpikok.kokkos.cxx VecMTDot_MPI() in src/vec/vec/impls/mpi/pvec2.c VecMTDot_Nest() in src/vec/vec/impls/nest/vecnest.c VecMTDot_Seq() in src/vec/vec/impls/seq/dvec2.c VecMTDot_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecMTDot_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecMTDot(Vec x, PetscInt nv, const Vec y[], PetscScalar val[])
```

Example 2 (unknown):
```unknown
val = (x,y) = y^T x,
```

Example 3 (unknown):
```unknown
val = (x,y) = y^H x,
```

---

## VecNestGetSize#

**URL:** https://petsc.org/release/manualpages/Vec/VecNestGetSize/

**Contents:**
- VecNestGetSize#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Returns the size of the nest vector.

N - number of nested vecs

VECNEST, Vectors and Parallel Data, Vec, VecType, VecNestGetSubVec(), VecNestGetSubVecs()

src/vec/vec/impls/nest/vecnest.c

VecNestGetSize_Nest() in src/vec/vec/impls/nest/vecnest.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecNestGetSize(Vec X, PetscInt *N)
```

Example 2 (unknown):
```unknown
VecNestGetSubVec()
```

Example 3 (unknown):
```unknown
VecNestGetSubVecs()
```

---

## VecNestGetSubVecsRead#

**URL:** https://petsc.org/release/manualpages/Vec/VecNestGetSubVecsRead/

**Contents:**
- VecNestGetSubVecsRead#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#
- Implementations#

Access the subvecs of a VECNEST vector for read-only access

N - number of nested vecs

sx - array of read-locked vectors

Each of the subvecs will be read locked (VecLockReadPush()), which is a logically collective operation. When access is complete, you must call VecNestRestoreSubVecsRead() to release the locks.

This function does not increase the state of X (PetscObjectStateIncrease()).

VECNEST, Vectors and Parallel Data, Vec, VecType, VecNestGetSize(), VecNestGetSubVec(), VecNestRestoreSubVecsRead()

src/vec/vec/impls/nest/vecnest.c

VecNestGetSubVecsRead_Nest() in src/vec/vec/impls/nest/vecnest.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecNestGetSubVecsRead(Vec X, PetscInt *N, Vec *sx[])
```

Example 2 (unknown):
```unknown
VecLockReadPush()
```

Example 3 (unknown):
```unknown
VecNestRestoreSubVecsRead()
```

Example 4 (unknown):
```unknown
PetscObjectStateIncrease()
```

---

## VecNestGetSubVecs#

**URL:** https://petsc.org/release/manualpages/Vec/VecNestGetSubVecs/

**Contents:**
- VecNestGetSubVecs#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- Fortran Notes#
- See Also#
- Level#
- Location#
- Implementations#

Returns the entire array of vectors defining a nest vector.

N - number of nested vecs

sx - array of vectors, can pass in NULL

The user should not free the array sx.

The caller must allocate the array to hold the subvectors and pass it in.

VECNEST, Vectors and Parallel Data, Vec, VecType, VecNestGetSize(), VecNestGetSubVec(), VecNestGetSubVecsRead()

src/vec/vec/impls/nest/vecnest.c

VecNestGetSubVecs_Nest() in src/vec/vec/impls/nest/vecnest.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecNestGetSubVecs(Vec X, PetscInt *N, Vec *sx[])
```

Example 2 (unknown):
```unknown
VecNestGetSize()
```

Example 3 (unknown):
```unknown
VecNestGetSubVec()
```

Example 4 (unknown):
```unknown
VecNestGetSubVecsRead()
```

---

## VecNestGetSubVec#

**URL:** https://petsc.org/release/manualpages/Vec/VecNestGetSubVec/

**Contents:**
- VecNestGetSubVec#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Returns a single, sub-vector from a nest vector.

idxm - index of the vector within the nest

sx - vector at index idxm within the nest

VECNEST, Vectors and Parallel Data, Vec, VecType, VecNestGetSize(), VecNestGetSubVecs()

src/vec/vec/impls/nest/vecnest.c

src/ksp/ksp/tutorials/ex27.c

VecNestGetSubVec_Nest() in src/vec/vec/impls/nest/vecnest.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecNestGetSubVec(Vec X, PetscInt idxm, Vec *sx)
```

Example 2 (unknown):
```unknown
VecNestGetSize()
```

Example 3 (unknown):
```unknown
VecNestGetSubVecs()
```

---

## VecNestRestoreSubVecsRead#

**URL:** https://petsc.org/release/manualpages/Vec/VecNestRestoreSubVecsRead/

**Contents:**
- VecNestRestoreSubVecsRead#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Restore access the subvecs of a VECNEST vector obtained with VecNestGetSubVecsRead()

N - number of nested vecs

sx - array of read-locked vectors

The same arguments to VecNestGetSubVecsRead() should be the argument to VecNestRestoreSubVecsRead().

VECNEST, Vectors and Parallel Data, Vec, VecType, VecNestGetSize(), VecNestGetSubVec(), VecNestGetSubVecsRead()

src/vec/vec/impls/nest/vecnest.c

VecNestRestoreSubVecsRead_Nest() in src/vec/vec/impls/nest/vecnest.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecNestGetSubVecsRead()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecNestRestoreSubVecsRead(Vec X, PetscInt *N, Vec *sx[])
```

Example 3 (unknown):
```unknown
VecNestGetSubVecsRead()
```

Example 4 (unknown):
```unknown
VecNestRestoreSubVecsRead()
```

---

## VecNestSetSubVecs#

**URL:** https://petsc.org/release/manualpages/Vec/VecNestSetSubVecs/

**Contents:**
- VecNestSetSubVecs#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Sets the component vectors at the specified indices in a nest vector.

N - number of component vecs in sx

idxm - indices of component vectors that are to be replaced

sx - array of vectors

The components in the vector array sx do not have to be of the same size as corresponding components in X. The user can also free the array sx after the call.

The nest vector X keeps references to sx vectors rather than creating duplicates.

VECNEST, Vectors and Parallel Data, Vec, VecType, VecNestGetSize(), VecNestGetSubVec()

src/vec/vec/impls/nest/vecnest.c

VecNestSetSubVecs_Nest() in src/vec/vec/impls/nest/vecnest.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecNestSetSubVecs(Vec X, PetscInt N, PetscInt idxm[], Vec sx[])
```

Example 2 (unknown):
```unknown
VecNestGetSize()
```

Example 3 (unknown):
```unknown
VecNestGetSubVec()
```

---

## VecNestSetSubVec#

**URL:** https://petsc.org/release/manualpages/Vec/VecNestSetSubVec/

**Contents:**
- VecNestSetSubVec#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Set a single component vector in a nest vector at specified index.

idxm - index of the vector within the nest vector

sx - vector at index idxm within the nest vector

The new vector sx does not have to be of same size as X[idxm]. Arbitrary vector layouts are allowed.

The nest vector X keeps a reference to sx rather than creating a duplicate.

VECNEST, Vectors and Parallel Data, Vec, VecType, VecNestSetSubVecs(), VecNestGetSubVec()

src/vec/vec/impls/nest/vecnest.c

VecNestSetSubVec_Nest() in src/vec/vec/impls/nest/vecnest.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecNestSetSubVec(Vec X, PetscInt idxm, Vec sx)
```

Example 2 (unknown):
```unknown
VecNestSetSubVecs()
```

Example 3 (unknown):
```unknown
VecNestGetSubVec()
```

---

## VECNEST#

**URL:** https://petsc.org/release/manualpages/Vec/VECNEST/

**Contents:**
- VECNEST#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

VECNEST = “nest” - Vector type consisting of nested subvectors, each stored separately.

This vector type reduces the number of copies for certain solvers applied to multi-physics problems. It is usually used with MATNEST and DMCOMPOSITE via DMSetVecType().

Vectors and Parallel Data, Vec, VecType, VecCreate(), VecCreateNest(), MatCreateNest()

src/vec/vec/impls/nest/vecnest.c

src/ksp/ksp/tutorials/ex27.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCOMPOSITE
```

Example 2 (unknown):
```unknown
DMSetVecType()
```

Example 3 (unknown):
```unknown
VecCreate()
```

Example 4 (unknown):
```unknown
VecCreateNest()
```

---

## VecNormalize#

**URL:** https://petsc.org/release/manualpages/Vec/VecNormalize/

**Contents:**
- VecNormalize#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Normalizes a vector by its 2-norm.

val - the vector norm before normalization. May be NULL if the value is not needed.

Vectors and Parallel Data, Vec, VecNorm(), NORM_2, NormType

src/vec/vec/interface/rvector.c

src/snes/tutorials/ex76.c src/ts/tutorials/ex30.c src/ts/tutorials/ex76.c src/ts/tutorials/ex77.c src/ksp/ksp/tutorials/ex49.c src/snes/tutorials/ex69.c src/snes/tutorials/ex62.c src/ksp/ksp/tutorials/ex67.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecNormalize(Vec x, PetscReal *val)
```

---

## VecNormAvailable#

**URL:** https://petsc.org/release/manualpages/Vec/VecNormAvailable/

**Contents:**
- VecNormAvailable#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Returns the vector norm if it is already known. That is, it has been previously computed and cached in the vector

type - one of NORM_1 (sum_i |x[i]|), NORM_2 sqrt(sum_i (x[i])^2), NORM_INFINITY max_i |x[i]|. Also available NORM_1_AND_2, which computes both norms and stores them in a two element array.

available - PETSC_TRUE if the val returned is valid

Vectors and Parallel Data, Vec, VecDot(), VecTDot(), VecNorm(), VecDotBegin(), VecDotEnd(), VecNormBegin(), VecNormEnd()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecNormAvailable(Vec x, NormType type, PetscBool *available, PetscReal *val)
```

Example 2 (unknown):
```unknown
NORM_INFINITY
```

Example 3 (unknown):
```unknown
NORM_1_AND_2
```

Example 4 (unknown):
```unknown
VecDotBegin()
```

---

## VecNormBegin#

**URL:** https://petsc.org/release/manualpages/Vec/VecNormBegin/

**Contents:**
- VecNormBegin#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Starts a split phase norm computation.

ntype - norm type, one of NORM_1, NORM_2, NORM_MAX, NORM_1_AND_2

result - where the result will go (can be NULL)

Each call to VecNormBegin() should be paired with a call to VecNormEnd().

VecNormEnd(), VecNorm(), VecDot(), VecMDot(), VecDotBegin(), VecDotEnd(), PetscCommSplitReductionBegin()

src/vec/vec/utils/comb.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"    
PetscErrorCode VecNormBegin(Vec x, NormType ntype, PetscReal *result)
```

Example 2 (unknown):
```unknown
NORM_1_AND_2
```

Example 3 (unknown):
```unknown
VecNormBegin()
```

Example 4 (unknown):
```unknown
VecNormEnd()
```

---

## VecNormEnd#

**URL:** https://petsc.org/release/manualpages/Vec/VecNormEnd/

**Contents:**
- VecNormEnd#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Ends a split phase norm computation.

ntype - norm type, one of NORM_1, NORM_2, NORM_MAX, NORM_1_AND_2

result - where the result will go

Each call to VecNormBegin() should be paired with a call to VecNormEnd().

The x vector is not allowed to be NULL, otherwise the vector would not have its correctly cached norm value

VecNormBegin(), VecNorm(), VecDot(), VecMDot(), VecDotBegin(), VecDotEnd(), PetscCommSplitReductionBegin()

src/vec/vec/utils/comb.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"    
PetscErrorCode VecNormEnd(Vec x, NormType ntype, PetscReal *result)
```

Example 2 (unknown):
```unknown
NORM_1_AND_2
```

Example 3 (unknown):
```unknown
VecNormBegin()
```

Example 4 (unknown):
```unknown
VecNormEnd()
```

---

## VecNorm#

**URL:** https://petsc.org/release/manualpages/Vec/VecNorm/

**Contents:**
- VecNorm#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Computes the vector norm.

type - the type of the norm requested

See NormType for descriptions of each norm.

For complex numbers NORM_1 will return the traditional 1 norm of the 2 norm of the complex numbers; that is the 1 norm of the absolute values of the complex entries. In PETSc 3.6 and earlier releases it returned the 1 norm of the 1 norm of the complex entries (what is returned by the BLAS routine asum()). Both are valid norms but most people expect the former.

This routine stashes the computed norm value, repeated calls before the vector entries are changed are then rapid since the precomputed value is immediately available. Certain vector operations such as VecSet() store the norms so the value is immediately available and does not need to be explicitly computed. VecScale() updates any stashed norm values, thus calls after VecScale() do not need to explicitly recompute the norm.

Vectors and Parallel Data, Vec, NormType, VecDot(), VecTDot(), VecDotBegin(), VecDotEnd(), VecNormAvailable(), VecNormBegin(), VecNormEnd(), NormType()

src/vec/vec/interface/rvector.c

src/mat/tutorials/ex3.c src/snes/tutorials/ex73f90t.F90 src/mat/tutorials/ex9.c src/snes/tutorials/ex14.c src/snes/tutorials/ex9.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex70.c src/mat/tutorials/ex2.c src/snes/tutorials/ex15.c

VecNorm_MPIKokkos() in src/vec/vec/impls/mpi/kokkos/mpikok.kokkos.cxx VecNorm_MPIViennaCL() in src/vec/vec/impls/mpi/mpiviennacl/mpiviennacl.cxx VecNorm_MPI() in src/vec/vec/impls/mpi/pvec2.c VecNorm_Nest() in src/vec/vec/impls/nest/vecnest.c VecNorm_Seq() in src/vec/vec/impls/seq/bvec2.c VecNorm_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecNorm_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecNorm(Vec x, NormType type, PetscReal *val)
```

Example 2 (unknown):
```unknown
VecDotBegin()
```

Example 3 (unknown):
```unknown
VecDotEnd()
```

Example 4 (unknown):
```unknown
VecNormAvailable()
```

---

## VecOperation#

**URL:** https://petsc.org/release/manualpages/Vec/VecOperation/

**Contents:**
- VecOperation#
- Synopsis#
- Values#
- Notes#
- See Also#
- Level#
- Location#

Enumeration of overide-able methods in the Vec implementation function-table.

VECOP_DUPLICATE - VecDuplicate()

VECOP_VIEW - VecView()

VECOP_LOAD - VecLoad()

VECOP_VIEWNATIVE - VecViewNative()

VECOP_LOADNATIVE - VecLoadNative()

Some operations may serve as the implementation for other routines not listed above. For example VECOP_SET can be used to simultaneously overriding the implementation used in VecSet(), VecSetInf(), and VecZeroEntries().

Entries to VecOperation are added as needed so if you do not see the operation listed which you’d like to replace, please send mail to petsc-maint@mcs.anl.gov!

Vectors and Parallel Data, Vec, VecSetOperation()

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  VECOP_DUPLICATE  = 0,
  VECOP_SET        = 10,
  VECOP_VIEW       = 33,
  VECOP_LOAD       = 41,
  VECOP_VIEWNATIVE = 68,
  VECOP_LOADNATIVE = 69
} VecOperation;
```

Example 2 (unknown):
```unknown
VECOP_DUPLICATE
```

Example 3 (unknown):
```unknown
VecDuplicate()
```

Example 4 (unknown):
```unknown
VECOP_VIEWNATIVE
```

---

## VecOption#

**URL:** https://petsc.org/release/manualpages/Vec/VecOption/

**Contents:**
- VecOption#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#
- Examples#

Options that may be set for a vector regarding entries passed to VecSetValues() and related routines

VEC_IGNORE_OFF_PROC_ENTRIES - causes VecSetValues() to ignore entries destined to be stored on a separate processor. This can be used to eliminate the global reduction in VecAssemblyBegin() if you know that you have only used VecSetValues() to set local elements

VEC_IGNORE_NEGATIVE_INDICES - means you can pass negative indices in ix in calls to VecSetValues() or VecGetValues(). These rows are simply ignored.

VEC_SUBSET_OFF_PROC_ENTRIES - causes VecAssemblyBegin() to assume that the off-process entries will always be a subset (possibly equal) of the off-process entries set on the first assembly which had a true VEC_SUBSET_OFF_PROC_ENTRIES and the vector has not changed this flag afterwards. If this assembly is not such first assembly, then this assembly can reuse the communication pattern setup in that first assembly, thus avoiding a global reduction. Subsequent assemblies setting off-process values should use the same InsertMode as the first assembly.

Matrices, Vec, MatSetOption(), VecSetOption(), VecSetValues(), VecAssemblyBegin()

src/ksp/ksp/tutorials/ex71.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecSetValues()
```

Example 2 (unknown):
```unknown
typedef enum {
  VEC_IGNORE_OFF_PROC_ENTRIES,
  VEC_IGNORE_NEGATIVE_INDICES,
  VEC_SUBSET_OFF_PROC_ENTRIES
} VecOption;
```

Example 3 (unknown):
```unknown
VEC_IGNORE_OFF_PROC_ENTRIES
```

Example 4 (unknown):
```unknown
VecSetValues()
```

---

## VecPermute#

**URL:** https://petsc.org/release/manualpages/Vec/VecPermute/

**Contents:**
- VecPermute#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Permutes a vector in place using the given ordering.

inv - The flag for inverting the permutation

This function does not yet support parallel Index Sets with non-local permutations

src/vec/vec/utils/vinv.c

src/ksp/ksp/tutorials/ex10.c src/ksp/ksp/tutorials/ex18.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecPermute(Vec x, IS row, PetscBool inv)
```

Example 2 (unknown):
```unknown
MatPermute()
```

---

## VecPlaceArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecPlaceArray/

**Contents:**
- VecPlaceArray#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Allows one to replace the array in a vector with an array provided by the user. This is useful to avoid copying an array into a vector.

Adding const to array was an oversight, as subsequent operations on vec would likely modify the data in array. However, we have kept it to avoid breaking APIs.

Use VecReplaceArray() instead to permanently replace the array

You can return to the original array with a call to VecResetArray(). vec does not take ownership of array in any way.

The user must free array themselves but be careful not to do so before the vector has either been destroyed, had its original array restored with VecResetArray() or permanently replaced with VecReplaceArray().

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecReplaceArray(), VecResetArray()

src/vec/vec/interface/rvector.c

src/ksp/ksp/tutorials/ex13.c src/ksp/ksp/tutorials/ex13f90.F90 src/ksp/ksp/tutorials/ex61f.F90

VecPlaceArray_MPI() in src/vec/vec/impls/mpi/pbvec.c VecPlaceArray_Seq() in src/vec/vec/impls/seq/dvec2.c VecPlaceArray_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecPlaceArray_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecPlaceArray(Vec vec, const PetscScalar array[])
```

Example 2 (unknown):
```unknown
VecReplaceArray()
```

Example 3 (unknown):
```unknown
VecResetArray()
```

Example 4 (unknown):
```unknown
VecResetArray()
```

---

## VecPointwiseDivide#

**URL:** https://petsc.org/release/manualpages/Vec/VecPointwiseDivide/

**Contents:**
- VecPointwiseDivide#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Computes the component-wise division w[i] = x[i] / y[i].

x - the numerator vector

y - the denominator vector

Any subset of the x, y, and w may be the same vector.

Vectors and Parallel Data, Vec, VecPointwiseMult(), VecPointwiseMax(), VecPointwiseMin(), VecPointwiseMaxAbs(), VecMaxPointwiseDivide()

src/vec/vec/interface/vector.c

src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/tao/unconstrained/tutorials/burgers_spectral.c src/ksp/ksp/tutorials/ex72.c src/vec/vec/tutorials/ex1.c src/snes/tutorials/ex13.c src/tao/pde_constrained/tutorials/elliptic.c src/tao/constrained/tutorials/tomographyADMM.c src/tao/pde_constrained/tutorials/parabolic.c src/vec/vec/tutorials/ex1f90.F90 src/vec/vec/tutorials/ex20f90.F90

VecPointwiseDivide_Nest() in src/vec/vec/impls/nest/vecnest.c VecPointwiseDivide_Seq() in src/vec/vec/impls/seq/bvec2.c VecPointwiseDivide_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecPointwiseDivide_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
w[i] = x[i] / y[i]
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecPointwiseDivide(Vec w, Vec x, Vec y)
```

Example 3 (unknown):
```unknown
VecPointwiseMult()
```

Example 4 (unknown):
```unknown
VecPointwiseMax()
```

---

## VecPointwiseMaxAbs#

**URL:** https://petsc.org/release/manualpages/Vec/VecPointwiseMaxAbs/

**Contents:**
- VecPointwiseMaxAbs#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Computes the component-wise maximum of the absolute values w[i] = max(abs(x[i]), abs(y[i])).

x - the first input vector

y - the second input vector

Any subset of the x, y, and w may be the same vector.

Vectors and Parallel Data, Vec, VecPointwiseDivide(), VecPointwiseMult(), VecPointwiseMin(), VecPointwiseMax(), VecMaxPointwiseDivide()

src/vec/vec/interface/vector.c

VecPointwiseMaxAbs_Seq() in src/vec/vec/impls/seq/bvec2.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
w[i] = max(abs(x[i]), abs(y[i]))
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecPointwiseMaxAbs(Vec w, Vec x, Vec y)
```

Example 3 (unknown):
```unknown
VecPointwiseDivide()
```

Example 4 (unknown):
```unknown
VecPointwiseMult()
```

---

## VecPointwiseMax#

**URL:** https://petsc.org/release/manualpages/Vec/VecPointwiseMax/

**Contents:**
- VecPointwiseMax#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Computes the component-wise maximum w[i] = max(x[i], y[i]).

x - the first input vector

y - the second input vector

Any subset of the x, y, and w may be the same vector.

For complex numbers compares only the real part

Vectors and Parallel Data, Vec, VecPointwiseDivide(), VecPointwiseMult(), VecPointwiseMin(), VecPointwiseMaxAbs(), VecMaxPointwiseDivide()

src/vec/vec/interface/vector.c

VecPointwiseMax_Seq() in src/vec/vec/impls/seq/bvec2.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
w[i] = max(x[i], y[i])
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecPointwiseMax(Vec w, Vec x, Vec y)
```

Example 3 (unknown):
```unknown
VecPointwiseDivide()
```

Example 4 (unknown):
```unknown
VecPointwiseMult()
```

---

## VecPointwiseMin#

**URL:** https://petsc.org/release/manualpages/Vec/VecPointwiseMin/

**Contents:**
- VecPointwiseMin#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Computes the component-wise minimum w[i] = min(x[i], y[i]).

x - the first input vector

y - the second input vector

Any subset of the x, y, and w may be the same vector.

For complex numbers compares only the real part

Vectors and Parallel Data, Vec, VecPointwiseDivide(), VecPointwiseMult(), VecPointwiseMaxAbs(), VecMaxPointwiseDivide()

src/vec/vec/interface/vector.c

VecPointwiseMin_Seq() in src/vec/vec/impls/seq/bvec2.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
w[i] = min(x[i], y[i])
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecPointwiseMin(Vec w, Vec x, Vec y)
```

Example 3 (unknown):
```unknown
VecPointwiseDivide()
```

Example 4 (unknown):
```unknown
VecPointwiseMult()
```

---

## VecPointwiseMult#

**URL:** https://petsc.org/release/manualpages/Vec/VecPointwiseMult/

**Contents:**
- VecPointwiseMult#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Computes the component-wise multiplication w[i] = x[i] * y[i].

y - the second vector

Any subset of the x, y, and w may be the same vector.

Vectors and Parallel Data, Vec, VecPointwiseDivide(), VecPointwiseMax(), VecPointwiseMin(), VecPointwiseMaxAbs(), VecMaxPointwiseDivide()

src/vec/vec/interface/vector.c

src/snes/tutorials/ex11.c src/snes/tutorials/ex16.c src/vec/vec/tutorials/ex1.c src/ksp/ksp/tutorials/ex15f.F90 src/snes/tutorials/ex36.c src/tao/pde_constrained/tutorials/parabolic.c src/vec/vec/tutorials/ex1f90.F90 src/ksp/ksp/tutorials/ex15.c src/tao/pde_constrained/tutorials/hyperbolic.c src/vec/vec/tutorials/ex20f90.F90

VecPointwiseMult_Nest() in src/vec/vec/impls/nest/vecnest.c VecPointwiseMult_Seq() in src/vec/vec/impls/seq/bvec2.c VecPointwiseMult_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecPointwiseMult_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
w[i] = x[i] * y[i]
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecPointwiseMult(Vec w, Vec x, Vec y)
```

Example 3 (unknown):
```unknown
VecPointwiseDivide()
```

Example 4 (unknown):
```unknown
VecPointwiseMax()
```

---

## VecPointwiseSign#

**URL:** https://petsc.org/release/manualpages/Vec/VecPointwiseSign/

**Contents:**
- VecPointwiseSign#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Computes the component-wise sign y[i] = sign(x[i]).

sign_type - VecSignMode indicating how the function should map zero values.

y - the sign vector of x

Vectors and Parallel Data, Vec, VecSignMode

src/vec/vec/interface/vector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
y[i] = sign(x[i])
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecPointwiseSign(Vec y, Vec x, VecSignMode sign_type)
```

Example 3 (unknown):
```unknown
VecSignMode
```

Example 4 (unknown):
```unknown
VecSignMode
```

---

## VecPow#

**URL:** https://petsc.org/release/manualpages/Vec/VecPow/

**Contents:**
- VecPow#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Replaces each component of a vector by \( x_i^p \)

p - the exponent to use on each element

This handles negative values, in infinity, and NaN in the expected IEEE floating pointing manner. For example, the square root of a negative real number is NaN and 1/0.0 is infinity.

src/vec/vec/utils/projection.c

src/tao/constrained/tutorials/tomographyADMM.c src/tao/tutorials/ex4.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"  
PetscErrorCode VecPow(Vec v, PetscScalar p)
```

---

## VecRealPart#

**URL:** https://petsc.org/release/manualpages/Vec/VecRealPart/

**Contents:**
- VecRealPart#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#

Replaces a complex vector with its real part

Vec, VecNorm(), VecImaginaryPart()

src/vec/vec/utils/vinv.c

src/ksp/ksp/tutorials/ex71.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecRealPart(Vec v)
```

Example 2 (unknown):
```unknown
VecImaginaryPart()
```

---

## VecReciprocal#

**URL:** https://petsc.org/release/manualpages/Vec/VecReciprocal/

**Contents:**
- VecReciprocal#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Replaces each component of a vector by its reciprocal.

vec - the vector reciprocal

Vector entries with value 0.0 are not changed

Vectors and Parallel Data, Vec, VecLog(), VecExp(), VecSqrtAbs()

src/vec/vec/interface/vector.c

src/ksp/pc/tutorials/ex4.c src/tao/tutorials/ex4.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ksp/ksp/tutorials/ex15f.F90 src/snes/tutorials/ex70.c src/tao/constrained/tutorials/tomographyADMM.c src/tao/pde_constrained/tutorials/parabolic.c src/tao/pde_constrained/tutorials/elliptic.c src/ksp/ksp/tutorials/ex15.c src/tao/unconstrained/tutorials/burgers_spectral.c

VecReciprocal_Nest() in src/vec/vec/impls/nest/vecnest.c VecReciprocal_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecReciprocal(Vec vec)
```

Example 2 (unknown):
```unknown
VecSqrtAbs()
```

---

## VecRegisterAll#

**URL:** https://petsc.org/release/manualpages/Vec/VecRegisterAll/

**Contents:**
- VecRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the vector types in the Vec package.

Vectors and Parallel Data, Vec, VecType, VecRegister(), VecRegisterDestroy()

src/vec/vec/interface/vecregall.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode VecRegisterAll(void)
```

Example 2 (unknown):
```unknown
VecRegister()
```

Example 3 (unknown):
```unknown
VecRegisterDestroy()
```

---

## VecRegister#

**URL:** https://petsc.org/release/manualpages/Vec/VecRegister/

**Contents:**
- VecRegister#
- Synopsis#
- Input Parameters#
- Notes#
- Example Usage#
- See Also#
- Level#
- Location#

Adds a new vector component implementation

Not Collective, No Fortran Support

sname - The name of a new user-defined creation routine

function - The creation routine

VecRegister() may be called multiple times to add several user-defined vectors

Then, your vector type can be chosen with the procedural interface via

or at runtime via the option

VecRegisterAll(), VecRegisterDestroy()

src/vec/vec/interface/vecreg.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"  
PetscErrorCode VecRegister(const char sname[], PetscErrorCode (*function)(Vec))
```

Example 2 (unknown):
```unknown
VecRegister()
```

Example 3 (unknown):
```unknown
VecRegister("my_vec",MyVectorCreate);
```

Example 4 (unknown):
```unknown
VecCreate(MPI_Comm, Vec *);
    VecSetType(Vec,"my_vector_name");
```

---

## VecReplaceArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecReplaceArray/

**Contents:**
- VecReplaceArray#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Allows one to replace the array in a vector with an array provided by the user. This is useful to avoid copying an array into a vector.

Logically Collective; No Fortran Support

Adding const to array was an oversight, as subsequent operations on vec would likely modify the data in array. However, we have kept it to avoid breaking APIs.

This permanently replaces the array and frees the memory associated with the old array. Use VecPlaceArray() to temporarily replace the array.

The memory passed in MUST be obtained with PetscMalloc() and CANNOT be freed by the user. It will be freed when the vector is destroyed.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecPlaceArray(), VecResetArray()

src/vec/vec/interface/rvector.c

VecReplaceArray_Seq() in src/vec/vec/impls/seq/dvec2.c VecReplaceArray_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecReplaceArray_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecReplaceArray(Vec vec, const PetscScalar array[])
```

Example 2 (unknown):
```unknown
VecPlaceArray()
```

Example 3 (unknown):
```unknown
PetscMalloc()
```

Example 4 (unknown):
```unknown
VecGetArray()
```

---

## VecResetArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecResetArray/

**Contents:**
- VecResetArray#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Resets a vector to use its default memory. Call this after the use of VecPlaceArray().

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecReplaceArray(), VecPlaceArray()

src/vec/vec/interface/vector.c

src/ksp/ksp/tutorials/ex13.c src/ksp/ksp/tutorials/ex13f90.F90 src/ksp/ksp/tutorials/ex61f.F90

VecResetArray_MPI() in src/vec/vec/impls/mpi/pbvec.c VecResetArray_Seq() in src/vec/vec/impls/seq/bvec2.c VecResetArray_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecResetArray_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecPlaceArray()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecResetArray(Vec vec)
```

Example 3 (unknown):
```unknown
VecGetArray()
```

Example 4 (unknown):
```unknown
VecRestoreArray()
```

---

## VecRestoreArray1dRead#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreArray1dRead/

**Contents:**
- VecRestoreArray1dRead#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Restores a vector after VecGetArray1dRead() has been called.

m - first dimension of two dimensional array

mstart - first index you will use in first coordinate direction (often 0)

a - location of pointer to array obtained from VecGetArray1dRead()

For regular PETSc vectors this routine does not involve any copies. For any special vectors that do not store local vector data in a contiguous array, this routine will copy the data back into the underlying vector data structure from the array obtained with VecGetArray1dRead().

This routine actually zeros out the a pointer.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecRestoreArrays(), VecPlaceArray(), VecGetArray2d(), VecGetArray3d(), VecRestoreArray3d(), DMDAVecGetArray(), DMDAVecRestoreArray(), VecGetArray1d(), VecRestoreArray2d(), VecGetArray4d(), VecRestoreArray4d()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetArray1dRead()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecRestoreArray1dRead(Vec x, PetscInt m, PetscInt mstart, PetscScalar *a[])
```

Example 3 (unknown):
```unknown
VecGetArray1dRead()
```

Example 4 (unknown):
```unknown
VecGetArray1dRead()
```

---

## VecRestoreArray1dWrite#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreArray1dWrite/

**Contents:**
- VecRestoreArray1dWrite#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Restores a vector after VecGetArray1dWrite() has been called.

m - first dimension of two dimensional array

mstart - first index you will use in first coordinate direction (often 0)

a - location of pointer to array obtained from VecGetArray1d()

For regular PETSc vectors this routine does not involve any copies. For any special vectors that do not store local vector data in a contiguous array, this routine will copy the data back into the underlying vector data structure from the array obtained with VecGetArray1d().

This routine actually zeros out the a pointer.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecRestoreArrays(), VecPlaceArray(), VecGetArray2d(), VecGetArray3d(), VecRestoreArray3d(), DMDAVecGetArray(), DMDAVecRestoreArray(), VecGetArray1d(), VecRestoreArray2d(), VecGetArray4d(), VecRestoreArray4d()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetArray1dWrite()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecRestoreArray1dWrite(Vec x, PetscInt m, PetscInt mstart, PetscScalar *a[])
```

Example 3 (unknown):
```unknown
VecGetArray1d()
```

Example 4 (unknown):
```unknown
VecGetArray1d()
```

---

## VecRestoreArray1d#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreArray1d/

**Contents:**
- VecRestoreArray1d#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Restores a vector after VecGetArray1d() has been called.

m - first dimension of two dimensional array

mstart - first index you will use in first coordinate direction (often 0)

a - location of pointer to array obtained from VecGetArray1d()

For regular PETSc vectors this routine does not involve any copies. For any special vectors that do not store local vector data in a contiguous array, this routine will copy the data back into the underlying vector data structure from the array obtained with VecGetArray1d().

This routine actually zeros out the a pointer.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecRestoreArrays(), VecPlaceArray(), VecGetArray2d(), VecGetArray3d(), VecRestoreArray3d(), DMDAVecGetArray(), DMDAVecRestoreArray(), VecGetArray1d(), VecRestoreArray2d(), VecGetArray4d(), VecRestoreArray4d()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetArray1d()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecRestoreArray1d(Vec x, PetscInt m, PetscInt mstart, PetscScalar *a[])
```

Example 3 (unknown):
```unknown
VecGetArray1d()
```

Example 4 (unknown):
```unknown
VecGetArray1d()
```

---

## VecRestoreArray2dRead#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreArray2dRead/

**Contents:**
- VecRestoreArray2dRead#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Restores a vector after VecGetArray2dRead() has been called.

m - first dimension of two dimensional array

n - second dimension of the two dimensional array

mstart - first index you will use in first coordinate direction (often 0)

nstart - first index in the second coordinate direction (often 0)

a - location of pointer to array obtained from VecGetArray2d()

For regular PETSc vectors this routine does not involve any copies. For any special vectors that do not store local vector data in a contiguous array, this routine will copy the data back into the underlying vector data structure from the array obtained with VecGetArray().

This routine actually zeros out the a pointer.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecRestoreArrays(), VecPlaceArray(), VecGetArray2d(), VecGetArray3d(), VecRestoreArray3d(), DMDAVecGetArray(), DMDAVecRestoreArray(), VecGetArray1d(), VecRestoreArray1d(), VecGetArray4d(), VecRestoreArray4d()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetArray2dRead()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecRestoreArray2dRead(Vec x, PetscInt m, PetscInt n, PetscInt mstart, PetscInt nstart, PetscScalar **a[])
```

Example 3 (unknown):
```unknown
VecGetArray()
```

Example 4 (unknown):
```unknown
VecGetArray()
```

---

## VecRestoreArray2dWrite#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreArray2dWrite/

**Contents:**
- VecRestoreArray2dWrite#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Restores a vector after VecGetArray2dWrite() has been called.

m - first dimension of two dimensional array

n - second dimension of the two dimensional array

mstart - first index you will use in first coordinate direction (often 0)

nstart - first index in the second coordinate direction (often 0)

a - location of pointer to array obtained from VecGetArray2d()

For regular PETSc vectors this routine does not involve any copies. For any special vectors that do not store local vector data in a contiguous array, this routine will copy the data back into the underlying vector data structure from the array obtained with VecGetArray().

This routine actually zeros out the a pointer.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecRestoreArrays(), VecPlaceArray(), VecGetArray2d(), VecGetArray3d(), VecRestoreArray3d(), DMDAVecGetArray(), DMDAVecRestoreArray(), VecGetArray1d(), VecRestoreArray1d(), VecGetArray4d(), VecRestoreArray4d()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetArray2dWrite()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecRestoreArray2dWrite(Vec x, PetscInt m, PetscInt n, PetscInt mstart, PetscInt nstart, PetscScalar **a[])
```

Example 3 (unknown):
```unknown
VecGetArray2d()
```

Example 4 (unknown):
```unknown
VecGetArray()
```

---

## VecRestoreArray2d#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreArray2d/

**Contents:**
- VecRestoreArray2d#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Restores a vector after VecGetArray2d() has been called.

m - first dimension of two dimensional array

n - second dimension of the two dimensional array

mstart - first index you will use in first coordinate direction (often 0)

nstart - first index in the second coordinate direction (often 0)

a - location of pointer to array obtained from VecGetArray2d()

For regular PETSc vectors this routine does not involve any copies. For any special vectors that do not store local vector data in a contiguous array, this routine will copy the data back into the underlying vector data structure from the array obtained with VecGetArray().

This routine actually zeros out the a pointer.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecRestoreArrays(), VecPlaceArray(), VecGetArray2d(), VecGetArray3d(), VecRestoreArray3d(), DMDAVecGetArray(), DMDAVecRestoreArray(), VecGetArray1d(), VecRestoreArray1d(), VecGetArray4d(), VecRestoreArray4d()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetArray2d()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecRestoreArray2d(Vec x, PetscInt m, PetscInt n, PetscInt mstart, PetscInt nstart, PetscScalar **a[])
```

Example 3 (unknown):
```unknown
VecGetArray2d()
```

Example 4 (unknown):
```unknown
VecGetArray()
```

---

## VecRestoreArray3dRead#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreArray3dRead/

**Contents:**
- VecRestoreArray3dRead#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Restores a vector after VecGetArray3dRead() has been called.

m - first dimension of three dimensional array

n - second dimension of the three dimensional array

p - third dimension of the three dimensional array

mstart - first index you will use in first coordinate direction (often 0)

nstart - first index in the second coordinate direction (often 0)

pstart - first index in the third coordinate direction (often 0)

a - location of pointer to array obtained from VecGetArray3dRead()

For regular PETSc vectors this routine does not involve any copies. For any special vectors that do not store local vector data in a contiguous array, this routine will copy the data back into the underlying vector data structure from the array obtained with VecGetArray().

This routine actually zeros out the a pointer.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecRestoreArrays(), VecPlaceArray(), VecGetArray2d(), VecGetArray3d(), VecRestoreArray3d(), DMDAVecGetArray(), DMDAVecRestoreArray(), VecGetArray1d(), VecRestoreArray1d(), VecGetArray4d(), VecRestoreArray4d()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetArray3dRead()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecRestoreArray3dRead(Vec x, PetscInt m, PetscInt n, PetscInt p, PetscInt mstart, PetscInt nstart, PetscInt pstart, PetscScalar ***a[])
```

Example 3 (unknown):
```unknown
VecGetArray3dRead()
```

Example 4 (unknown):
```unknown
VecGetArray()
```

---

## VecRestoreArray3dWrite#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreArray3dWrite/

**Contents:**
- VecRestoreArray3dWrite#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Restores a vector after VecGetArray3dWrite() has been called.

m - first dimension of three dimensional array

n - second dimension of the three dimensional array

p - third dimension of the three dimensional array

mstart - first index you will use in first coordinate direction (often 0)

nstart - first index in the second coordinate direction (often 0)

pstart - first index in the third coordinate direction (often 0)

a - location of pointer to array obtained from VecGetArray3d()

For regular PETSc vectors this routine does not involve any copies. For any special vectors that do not store local vector data in a contiguous array, this routine will copy the data back into the underlying vector data structure from the array obtained with VecGetArray().

This routine actually zeros out the a pointer.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecRestoreArrays(), VecPlaceArray(), VecGetArray2d(), VecGetArray3d(), VecRestoreArray3d(), DMDAVecGetArray(), DMDAVecRestoreArray(), VecGetArray1d(), VecRestoreArray1d(), VecGetArray4d(), VecRestoreArray4d()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetArray3dWrite()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecRestoreArray3dWrite(Vec x, PetscInt m, PetscInt n, PetscInt p, PetscInt mstart, PetscInt nstart, PetscInt pstart, PetscScalar ***a[])
```

Example 3 (unknown):
```unknown
VecGetArray()
```

Example 4 (unknown):
```unknown
VecGetArray()
```

---

## VecRestoreArray3d#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreArray3d/

**Contents:**
- VecRestoreArray3d#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Restores a vector after VecGetArray3d() has been called.

m - first dimension of three dimensional array

n - second dimension of the three dimensional array

p - third dimension of the three dimensional array

mstart - first index you will use in first coordinate direction (often 0)

nstart - first index in the second coordinate direction (often 0)

pstart - first index in the third coordinate direction (often 0)

a - location of pointer to array obtained from VecGetArray3d()

For regular PETSc vectors this routine does not involve any copies. For any special vectors that do not store local vector data in a contiguous array, this routine will copy the data back into the underlying vector data structure from the array obtained with VecGetArray().

This routine actually zeros out the a pointer.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecRestoreArrays(), VecPlaceArray(), VecGetArray2d(), VecGetArray3d(), DMDAVecGetArray(), DMDAVecRestoreArray(), VecGetArray1d(), VecRestoreArray1d(), VecGetArray4d(), VecRestoreArray4d()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetArray3d()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecRestoreArray3d(Vec x, PetscInt m, PetscInt n, PetscInt p, PetscInt mstart, PetscInt nstart, PetscInt pstart, PetscScalar ***a[])
```

Example 3 (unknown):
```unknown
VecGetArray()
```

Example 4 (unknown):
```unknown
VecGetArray()
```

---

## VecRestoreArray4dRead#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreArray4dRead/

**Contents:**
- VecRestoreArray4dRead#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Restores a vector after VecGetArray4d() has been called.

m - first dimension of four dimensional array

n - second dimension of the four dimensional array

p - third dimension of the four dimensional array

q - fourth dimension of the four dimensional array

mstart - first index you will use in first coordinate direction (often 0)

nstart - first index in the second coordinate direction (often 0)

pstart - first index in the third coordinate direction (often 0)

qstart - first index in the fourth coordinate direction (often 0)

a - location of pointer to array obtained from VecGetArray4dRead()

For regular PETSc vectors this routine does not involve any copies. For any special vectors that do not store local vector data in a contiguous array, this routine will copy the data back into the underlying vector data structure from the array obtained with VecGetArray().

This routine actually zeros out the a pointer.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecRestoreArrays(), VecPlaceArray(), VecGetArray2d(), VecGetArray3d(), VecRestoreArray3d(), DMDAVecGetArray(), DMDAVecRestoreArray(), VecGetArray1d(), VecRestoreArray1d(), VecGetArray4d(), VecRestoreArray4d()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetArray4d()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecRestoreArray4dRead(Vec x, PetscInt m, PetscInt n, PetscInt p, PetscInt q, PetscInt mstart, PetscInt nstart, PetscInt pstart, PetscInt qstart, PetscScalar ****a[])
```

Example 3 (unknown):
```unknown
VecGetArray4dRead()
```

Example 4 (unknown):
```unknown
VecGetArray()
```

---

## VecRestoreArray4dWrite#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreArray4dWrite/

**Contents:**
- VecRestoreArray4dWrite#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Restores a vector after VecGetArray4dWrite() has been called.

m - first dimension of four dimensional array

n - second dimension of the four dimensional array

p - third dimension of the four dimensional array

q - fourth dimension of the four dimensional array

mstart - first index you will use in first coordinate direction (often 0)

nstart - first index in the second coordinate direction (often 0)

pstart - first index in the third coordinate direction (often 0)

qstart - first index in the fourth coordinate direction (often 0)

a - location of pointer to array obtained from VecGetArray4d()

For regular PETSc vectors this routine does not involve any copies. For any special vectors that do not store local vector data in a contiguous array, this routine will copy the data back into the underlying vector data structure from the array obtained with VecGetArray().

This routine actually zeros out the a pointer.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecRestoreArrays(), VecPlaceArray(), VecGetArray2d(), VecGetArray3d(), VecRestoreArray3d(), DMDAVecGetArray(), DMDAVecRestoreArray(), VecGetArray1d(), VecRestoreArray1d(), VecGetArray4d(), VecRestoreArray4d()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetArray4dWrite()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecRestoreArray4dWrite(Vec x, PetscInt m, PetscInt n, PetscInt p, PetscInt q, PetscInt mstart, PetscInt nstart, PetscInt pstart, PetscInt qstart, PetscScalar ****a[])
```

Example 3 (unknown):
```unknown
VecGetArray4d()
```

Example 4 (unknown):
```unknown
VecGetArray()
```

---

## VecRestoreArray4d#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreArray4d/

**Contents:**
- VecRestoreArray4d#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Restores a vector after VecGetArray4d() has been called.

m - first dimension of four dimensional array

n - second dimension of the four dimensional array

p - third dimension of the four dimensional array

q - fourth dimension of the four dimensional array

mstart - first index you will use in first coordinate direction (often 0)

nstart - first index in the second coordinate direction (often 0)

pstart - first index in the third coordinate direction (often 0)

qstart - first index in the fourth coordinate direction (often 0)

a - location of pointer to array obtained from VecGetArray4d()

For regular PETSc vectors this routine does not involve any copies. For any special vectors that do not store local vector data in a contiguous array, this routine will copy the data back into the underlying vector data structure from the array obtained with VecGetArray().

This routine actually zeros out the a pointer.

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecRestoreArrays(), VecPlaceArray(), VecGetArray2d(), VecGetArray3d(), VecRestoreArray3d(), DMDAVecGetArray(), DMDAVecRestoreArray(), VecGetArray1d(), VecRestoreArray1d(), VecGetArray4d()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetArray4d()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecRestoreArray4d(Vec x, PetscInt m, PetscInt n, PetscInt p, PetscInt q, PetscInt mstart, PetscInt nstart, PetscInt pstart, PetscInt qstart, PetscScalar ****a[])
```

Example 3 (unknown):
```unknown
VecGetArray()
```

Example 4 (unknown):
```unknown
VecGetArray()
```

---

## VecRestoreArrayAndMemType#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreArrayAndMemType/

**Contents:**
- VecRestoreArrayAndMemType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Restores a vector after VecGetArrayAndMemType() has been called.

Logically Collective; No Fortran Support

a - location of pointer to array obtained from VecGetArrayAndMemType()

Vectors and Parallel Data, Vec, VecGetArrayAndMemType(), VecGetArray(), VecRestoreArrayRead(), VecRestoreArrays(), VecPlaceArray(), VecRestoreArray2d(), VecGetArrayPair(), VecRestoreArrayPair()

src/vec/vec/interface/rvector.c

VecRestoreArrayAndMemType_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetArrayAndMemType()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecRestoreArrayAndMemType(Vec x, PetscScalar *a[])
```

Example 3 (unknown):
```unknown
VecGetArrayAndMemType()
```

Example 4 (unknown):
```unknown
VecGetArrayAndMemType()
```

---

## VecRestoreArrayPair#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreArrayPair/

**Contents:**
- VecRestoreArrayPair#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Returns a pair of pointers for two vectors that may be common obtained with VecGetArrayPair()

Logically Collective; No Fortran Support

y - the second vector

xv - location to put pointer to the first array

yv - location to put pointer to the second array

Vectors and Parallel Data, VecGetArray(), VecGetArrayRead(), VecGetArrayPair()

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetArrayPair()
```

Example 2 (unknown):
```unknown
static inline PetscErrorCode VecRestoreArrayPair(Vec x, Vec y, PetscScalar *xv[], PetscScalar *yv[])
```

Example 3 (unknown):
```unknown
VecGetArray()
```

Example 4 (unknown):
```unknown
VecGetArrayRead()
```

---

## VecRestoreArrayReadAndMemType#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreArrayReadAndMemType/

**Contents:**
- VecRestoreArrayReadAndMemType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Restore array obtained with VecGetArrayReadAndMemType()

Not Collective; No Fortran Support

Vectors and Parallel Data, Vec, VecGetArrayReadAndMemType(), VecRestoreArrayAndMemType(), VecRestoreArrayWriteAndMemType(), VecGetArray(), VecRestoreArray(), VecGetArrayPair(), VecRestoreArrayPair()

src/vec/vec/interface/rvector.c

src/mat/tutorials/ex19.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetArrayReadAndMemType()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecRestoreArrayReadAndMemType(Vec x, const PetscScalar *a[])
```

Example 3 (unknown):
```unknown
VecGetArrayReadAndMemType()
```

Example 4 (unknown):
```unknown
VecRestoreArrayAndMemType()
```

---

## VecRestoreArrayRead#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreArrayRead/

**Contents:**
- VecRestoreArrayRead#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Restore array obtained with VecGetArrayRead()

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArray(), VecGetArrayPair(), VecRestoreArrayPair()

src/vec/vec/interface/rvector.c

src/snes/tutorials/ex99.c src/snes/tutorials/ex59.c src/snes/tutorials/ex1.c src/snes/tutorials/ex6.c src/snes/tutorials/ex73f90t.F90 src/snes/tutorials/ex13.c src/snes/tutorials/ex70.c src/mat/tutorials/ex12.c src/snes/tutorials/ex48.c src/snes/tutorials/ex7.c

VecRestoreArrayRead_Nest() in src/vec/vec/impls/nest/vecnest.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetArrayRead()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecRestoreArrayRead(Vec x, const PetscScalar *a[])
```

Example 3 (unknown):
```unknown
VecGetArray()
```

Example 4 (unknown):
```unknown
VecRestoreArray()
```

---

## VecRestoreArrays#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreArrays/

**Contents:**
- VecRestoreArrays#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Restores a group of vectors after VecGetArrays() has been called.

Logically Collective; No Fortran Support

n - the number of vectors

a - location of pointer to arrays obtained from VecGetArrays()

For regular PETSc vectors this routine does not involve any copies. For any special vectors that do not store local vector data in a contiguous array, this routine will copy the data back into the underlying vector data structure from the arrays obtained with VecGetArrays().

Vectors and Parallel Data, Vec, VecGetArrays(), VecRestoreArray()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetArrays()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecRestoreArrays(const Vec x[], PetscInt n, PetscScalar **a[])
```

Example 3 (unknown):
```unknown
VecGetArrays()
```

Example 4 (unknown):
```unknown
VecGetArrays()
```

---

## VecRestoreArrayWriteAndMemType#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreArrayWriteAndMemType/

**Contents:**
- VecRestoreArrayWriteAndMemType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Restore array obtained with VecGetArrayWriteAndMemType()

Logically Collective; No Fortran Support

Vectors and Parallel Data, Vec, VecGetArrayWriteAndMemType(), VecRestoreArrayAndMemType(), VecGetArray(), VecRestoreArray(), VecGetArrayPair(), VecRestoreArrayPair()

src/vec/vec/interface/rvector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetArrayWriteAndMemType()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecRestoreArrayWriteAndMemType(Vec x, PetscScalar *a[])
```

Example 3 (unknown):
```unknown
VecGetArrayWriteAndMemType()
```

Example 4 (unknown):
```unknown
VecRestoreArrayAndMemType()
```

---

## VecRestoreArrayWrite#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreArrayWrite/

**Contents:**
- VecRestoreArrayWrite#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Restores a vector after VecGetArrayWrite() has been called.

a - location of pointer to array obtained from VecGetArray()

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArrayRead(), VecRestoreArrays(), VecPlaceArray(), VecRestoreArray2d(), VecGetArrayPair(), VecRestoreArrayPair(), VecGetArrayWrite()

src/vec/vec/interface/rvector.c

src/ts/tutorials/ex45.c src/ts/tutorials/ex36.c src/dm/impls/plex/tutorials/ex14.c src/ts/tutorials/ex77.c src/ts/tutorials/ex3.c src/snes/tutorials/ex17.c src/ts/tutorials/ex43.c src/ts/tutorials/ex23fwdadj.c src/tao/unconstrained/tutorials/rosenbrock3.c src/ksp/ksp/tutorials/ex27.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetArrayWrite()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecRestoreArrayWrite(Vec x, PetscScalar *a[])
```

Example 3 (unknown):
```unknown
VecGetArray()
```

Example 4 (unknown):
```unknown
VecGetArray()
```

---

## VecRestoreArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreArray/

**Contents:**
- VecRestoreArray#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Restores a vector after VecGetArray() has been called and the array is no longer needed

a - location of pointer to array obtained from VecGetArray()

Vectors and Parallel Data, Vec, VecGetArray(), VecRestoreArrayRead(), VecRestoreArrays(), VecPlaceArray(), VecRestoreArray2d(), VecGetArrayPair(), VecRestoreArrayPair()

src/vec/vec/interface/rvector.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex5f90.F90 src/snes/tutorials/ex99.c src/snes/tutorials/ex59.c src/snes/tutorials/ex1.c src/snes/tutorials/ex6.c src/snes/tutorials/ex13.c src/snes/tutorials/ex22.c src/snes/tutorials/ex7.c src/snes/tutorials/ex21.c

VecRestoreArray_Nest() in src/vec/vec/impls/nest/vecnest.c VecRestoreArray_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecRestoreArray_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetArray()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecRestoreArray(Vec x, PetscScalar *a[])
```

Example 3 (unknown):
```unknown
VecGetArray()
```

Example 4 (unknown):
```unknown
VecGetArray()
```

---

## VecRestoreKokkosViewWrite#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreKokkosViewWrite/

**Contents:**
- VecRestoreKokkosViewWrite#
- Synopsis#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Returns a Kokkos View gotten with VecGetKokkosViewWrite().

Logically Collective, No Fortran Support

v - the vector in type of VECKOKKOS

kv - the Kokkos View with a user-specified template parameter MemorySpace

If the vector is not of type VECKOKKOS, an error will be raised.

The function is similar to VecRestoreArrayWrite(). It is the counterpart of VecGetKokkosViewWrite().

VecGetKokkosViewWrite(), VecGetKokkosView(), VecGetKokkosView(), VecRestoreArray(), VecGetArrayRead(), VecGetArrays(), VecPlaceArray(), VecGetArray2d(), VecGetArrayPair(), VecRestoreArrayPair(), VecGetArrayWrite(), VecRestoreArrayWrite()

include/petscvec_kokkos.hpp

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetKokkosViewWrite()
```

Example 2 (jsx):
```jsx
template <class MemorySpace>
PetscErrorCode VecRestoreKokkosViewWrite(Vec, Kokkos::View<PetscScalar *, MemorySpace> *)
```

Example 3 (cpp):
```cpp
#include <petscvec_kokkos.hpp>
PetscErrorCode VecRestoreKokkosViewWrite  (Vec v,Kokkos::View<PetscScalar*,MemorySpace>* kv);
```

Example 4 (unknown):
```unknown
VecRestoreArrayWrite()
```

---

## VecRestoreKokkosView#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreKokkosView/

**Contents:**
- VecRestoreKokkosView#
- Synopsis#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Returns a Kokkos View gotten by VecGetKokkosView().

Logically Collective, No Fortran Support

v - the vector in type of VECKOKKOS

kv - the Kokkos View with a user-specified template parameter MemorySpace

If the vector is not of type VECKOKKOS, an error will be raised. The functions are similar to VecRestoreArrayRead() and VecRestoreArray() respectively. They are the counterpart of VecGetKokkosView().

VecGetKokkosView(), VecRestoreKokkosViewWrite(), VecRestoreArray(), VecGetArrayRead(), VecGetArrays(), VecPlaceArray(), VecGetArray2d(), VecGetArrayPair(), VecRestoreArrayPair(), VecGetArrayWrite(), VecRestoreArrayWrite()

include/petscvec_kokkos.hpp

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetKokkosView()
```

Example 2 (jsx):
```jsx
template <class MemorySpace>
PetscErrorCode VecRestoreKokkosView(Vec, Kokkos::View<const PetscScalar *, MemorySpace> *)
```

Example 3 (jsx):
```jsx
#include <petscvec_kokkos.hpp>
PetscErrorCode VecRestoreKokkosView  (Vec v,Kokkos::View<const PetscScalar*,MemorySpace>* kv);
PetscErrorCode VecRestoreKokkosView  (Vec v,Kokkos::View<PetscScalar*,MemorySpace>* kv);
```

Example 4 (unknown):
```unknown
VecRestoreArrayRead()
```

---

## VecRestoreLocalVectorRead#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreLocalVectorRead/

**Contents:**
- VecRestoreLocalVectorRead#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Unmaps the local portion of a vector previously mapped into a vector using VecGetLocalVectorRead().

v - The local portion of this vector was previously mapped into w using VecGetLocalVectorRead().

w - The vector into which the local portion of v was mapped.

Vectors and Parallel Data, Vec, VecCreateLocalVector(), VecGetLocalVectorRead(), VecGetLocalVector(), VecGetArrayRead(), VecGetArray()

src/vec/vec/interface/rvector.c

VecRestoreLocalVectorRead_Nest() in src/vec/vec/impls/nest/vecnest.c VecRestoreLocalVectorRead_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetLocalVectorRead()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecRestoreLocalVectorRead(Vec v, Vec w)
```

Example 3 (unknown):
```unknown
VecGetLocalVectorRead()
```

Example 4 (unknown):
```unknown
VecCreateLocalVector()
```

---

## VecRestoreLocalVector#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreLocalVector/

**Contents:**
- VecRestoreLocalVector#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Unmaps the local portion of a vector previously mapped into a vector using VecGetLocalVector().

Logically Collective.

v - The local portion of this vector was previously mapped into w using VecGetLocalVector().

w - The vector into which the local portion of v was mapped.

Vectors and Parallel Data, Vec, VecCreateLocalVector(), VecGetLocalVector(), VecGetLocalVectorRead(), VecRestoreLocalVectorRead(), LocalVectorRead(), VecGetArrayRead(), VecGetArray()

src/vec/vec/interface/rvector.c

VecRestoreLocalVector_Nest() in src/vec/vec/impls/nest/vecnest.c VecRestoreLocalVector_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetLocalVector()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecRestoreLocalVector(Vec v, Vec w)
```

Example 3 (unknown):
```unknown
VecGetLocalVector()
```

Example 4 (unknown):
```unknown
VecCreateLocalVector()
```

---

## VecRestoreSubVector#

**URL:** https://petsc.org/release/manualpages/Vec/VecRestoreSubVector/

**Contents:**
- VecRestoreSubVector#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Restores a subvector extracted using VecGetSubVector()

X - vector from which subvector was obtained

is - index set representing the subset of X

Y - subvector being restored

Vectors and Parallel Data, Vec, IS, VecGetSubVector()

src/vec/vec/interface/rvector.c

src/dm/tutorials/ex22.c src/snes/tutorials/ex70.c src/ksp/ksp/tutorials/ex81.c src/ts/tutorials/ex77.c src/ksp/ksp/tutorials/ex81a.c src/vec/vec/tutorials/ex44.c

VecRestoreSubVector_Nest() in src/vec/vec/impls/nest/vecnest.c VecRestoreSubVector_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecGetSubVector()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecRestoreSubVector(Vec X, IS is, Vec *Y)
```

Example 3 (unknown):
```unknown
VecGetSubVector()
```

---

## VecScale#

**URL:** https://petsc.org/release/manualpages/Vec/VecScale/

**Contents:**
- VecScale#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

For a vector with n components, VecScale() computes x[i] = alpha * x[i], for i=1,…,n.

Vectors and Parallel Data, Vec, VecSet()

src/vec/vec/interface/rvector.c

src/ksp/pc/tutorials/ex4.c src/ksp/ksp/tutorials/ex60.c src/ksp/ksp/tutorials/ex59.c src/mat/tutorials/ex9.c src/vec/vec/tutorials/ex1.c src/snes/tutorials/ex70.c src/ksp/ksp/tutorials/ex49.c src/snes/tutorials/ex15.c src/snes/tutorials/ex7.c src/ksp/ksp/tutorials/ex28.c

VecScale_Nest() in src/vec/vec/impls/nest/vecnest.c VecScale_Seq() in src/vec/vec/impls/seq/bvec1.c VecScale_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecScale_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecScale(Vec x, PetscScalar alpha)
```

---

## VecScatterBegin#

**URL:** https://petsc.org/release/manualpages/Vec/VecScatterBegin/

**Contents:**
- VecScatterBegin#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Begins a generalized scatter from one vector to another. Complete the scattering phase with VecScatterEnd().

Neighbor-wise Collective

sf - scatter context generated by VecScatterCreate()

x - the vector from which we scatter

y - the vector to which we scatter

addv - either ADD_VALUES, MAX_VALUES, MIN_VALUES or INSERT_VALUES, with INSERT_VALUES mode any location not scattered to retains its old value; i.e. the vector is NOT first zeroed.

mode - the scattering mode, usually SCATTER_FORWARD. The available modes are: SCATTER_FORWARD or SCATTER_REVERSE

The vectors x and y need not be the same vectors used in the call to VecScatterCreate(), but x must have the same parallel data layout as that passed in as the x to VecScatterCreate(), similarly for the y. Most likely they have been obtained from VecDuplicate().

You cannot change the values in the input vector between the calls to VecScatterBegin() and VecScatterEnd().

If you use SCATTER_REVERSE the two arguments x and y should be reversed, from the SCATTER_FORWARD.

This scatter is far more general than the conventional scatter, since it can be a gather or a scatter or a combination, depending on the indices ix and iy. If x is a parallel vector and y is sequential, VecScatterBegin() can serve to gather values to a single processor. Similarly, if y is parallel and x sequential, the routine can scatter from one processor to many processors.

Low-level Vector Communication, VecScatter, VecScatterCreate(), VecScatterEnd(), InsertMode, ScatterMode

src/vec/vec/utils/vscat.c

src/ts/tutorials/ex29.c src/tao/constrained/tutorials/ex1.c src/ksp/ksp/tutorials/ex73.c src/tao/pde_constrained/tutorials/elliptic.c src/tao/pde_constrained/tutorials/parabolic.c src/ksp/ksp/tutorials/ex49.c src/vec/vec/utils/tagger/tutorials/ex1.c src/ksp/ksp/tutorials/ex43.c src/tao/pde_constrained/tutorials/hyperbolic.c src/vec/vec/tutorials/ex44.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecScatterEnd()
```

Example 2 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode VecScatterBegin(VecScatter sf, Vec x, Vec y, InsertMode addv, ScatterMode mode)
```

Example 3 (unknown):
```unknown
VecScatterCreate()
```

Example 4 (unknown):
```unknown
INSERT_VALUES
```

---

## VecScatterCopy#

**URL:** https://petsc.org/release/manualpages/Vec/VecScatterCopy/

**Contents:**
- VecScatterCopy#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Makes a copy of a scatter context.

sf - the scatter context

newsf - the context copy

Low-level Vector Communication, VecScatter, VecScatterType, VecScatterCreate(), VecScatterDestroy()

src/vec/vec/utils/vscat.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode VecScatterCopy(VecScatter sf, VecScatter *newsf)
```

Example 2 (unknown):
```unknown
VecScatterType
```

Example 3 (unknown):
```unknown
VecScatterCreate()
```

Example 4 (unknown):
```unknown
VecScatterDestroy()
```

---

## VecScatterCreateToAll#

**URL:** https://petsc.org/release/manualpages/Vec/VecScatterCreateToAll/

**Contents:**
- VecScatterCreateToAll#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Example Usage#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates a vector and a scatter context that copies all vector values to each processor

ctx - scatter context

vout - output SEQVEC that is large enough to scatter into

vout may be NULL [PETSC_NULL_VEC from Fortran] if you do not need to have it created

Do NOT create a vector and then pass it in as the final argument vout! vout is created by this routine automatically (unless you pass NULL in for that argument if you do not need it).

Low-level Vector Communication, VecScatter, VecScatterCreate(), VecScatterCreateToZero(), VecScatterBegin(), VecScatterEnd()

src/vec/vec/utils/vscat.c

src/ksp/ksp/tutorials/ex43.c src/ksp/ksp/tutorials/ex49.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode VecScatterCreateToAll(Vec vin, VecScatter *ctx, Vec *vout)
```

Example 2 (typescript):
```typescript
VecScatterCreateToAll(vin, &ctx, &vout);

  // scatter as many times as you need
  VecScatterBegin(ctx, vin, vout, INSERT_VALUES, SCATTER_FORWARD);
  VecScatterEnd(ctx, vin, vout, INSERT_VALUES, SCATTER_FORWARD);

  // destroy scatter context and local vector when no longer needed
  VecScatterDestroy(&ctx);
  VecDestroy(&vout);
```

Example 3 (unknown):
```unknown
PETSC_NULL_VEC
```

Example 4 (unknown):
```unknown
VecScatterCreate()
```

---

## VecScatterCreateToZero#

**URL:** https://petsc.org/release/manualpages/Vec/VecScatterCreateToZero/

**Contents:**
- VecScatterCreateToZero#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Example Usage#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates an output vector and a scatter context used to copy all vector values into the output vector on the zeroth processor

vin - Vec of type MPIVEC

ctx - scatter context

vout - output SEQVEC that is large enough to scatter into on processor 0 and of length zero on all other processors

vout may be NULL [PETSC_NULL_VEC from Fortran] if you do not need to have it created

Do NOT create a vector and then pass it in as the final argument vout! vout is created by this routine automatically (unless you pass NULL in for that argument if you do not need it).

Low-level Vector Communication, VecScatter, VecScatterCreate(), VecScatterCreateToAll(), VecScatterBegin(), VecScatterEnd()

src/vec/vec/utils/vscat.c

src/tao/constrained/tutorials/ex1.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode VecScatterCreateToZero(Vec vin, VecScatter *ctx, Vec *vout)
```

Example 2 (typescript):
```typescript
VecScatterCreateToZero(vin, &ctx, &vout);

  // scatter as many times as you need
  VecScatterBegin(ctx, vin, vout, INSERT_VALUES, SCATTER_FORWARD);
  VecScatterEnd(ctx, vin, vout, INSERT_VALUES, SCATTER_FORWARD);

  // destroy scatter context and local vector when no longer needed
  VecScatterDestroy(&ctx);
  VecDestroy(&vout);
```

Example 3 (unknown):
```unknown
PETSC_NULL_VEC
```

Example 4 (unknown):
```unknown
VecScatterCreate()
```

---

## VecScatterCreate#

**URL:** https://petsc.org/release/manualpages/Vec/VecScatterCreate/

**Contents:**
- VecScatterCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#

Creates a vector scatter VecScatter context that is used to communicate entries between two vectors Vec

x - a vector that defines the shape (parallel data layout of the vector) of vectors from which we scatter

y - a vector that defines the shape (parallel data layout of the vector) of vectors to which we scatter

ix - the indices of x to scatter (if NULL scatters all values)

iy - the indices of y to hold results (if NULL fills entire vector yin in order)

newsf - location to store the new scatter context

-vecscatter_view - Prints detail of communications

-vecscatter_view ::ascii_info - Print less details about communication

-vecscatter_merge - VecScatterBegin() handles all of the communication, VecScatterEnd() is a nop eliminates the chance for overlap of computation and communication

If both x and y are parallel, their communicator must be on the same set of processes, but their process order can be different. In calls to the scatter options you can use different vectors than the x and y you used above; BUT they must have the same parallel data layout, for example, they could be obtained from VecDuplicate(). A VecScatter context CANNOT be used in two or more simultaneous scatters; that is you cannot call a second VecScatterBegin() with the same scatter context until the VecScatterEnd() has been called on the first VecScatterBegin(). In this case a separate VecScatter is needed for each concurrent scatter.

Both ix and iy cannot be NULL at the same time.

Use VecScatterCreateToAll() to create a VecScatter that copies an MPI vector to sequential vectors on all MPI processes. Use VecScatterCreateToZero() to create a VecScatter that copies an MPI vector to a sequential vector on MPI rank 0. These special VecScatter have better performance than general ones.

The implementations of most the VecScatter are done using PetscSF.

Low-level Vector Communication, VecScatter, VecScatterDestroy(), VecScatterCreateToAll(), VecScatterCreateToZero(), PetscSFCreate(), VecScatterType, InsertMode, ScatterMode, VecScatterBegin(), VecScatterEnd()

src/vec/vec/utils/vscat.c

src/dm/tutorials/ex14.c src/ts/tutorials/ex30.c src/ksp/ksp/tutorials/ex73.c src/dm/tutorials/ex6.c src/tao/pde_constrained/tutorials/elliptic.c src/tao/pde_constrained/tutorials/parabolic.c src/ksp/ksp/tutorials/ex49.c src/vec/vec/utils/tagger/tutorials/ex1.c src/tao/pde_constrained/tutorials/hyperbolic.c src/vec/vec/tutorials/ex44.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode VecScatterCreate(Vec x, IS ix, Vec y, IS iy, VecScatter *newsf)
```

Example 2 (unknown):
```unknown
VecScatterBegin()
```

Example 3 (unknown):
```unknown
VecScatterEnd()
```

Example 4 (unknown):
```unknown
VecDuplicate()
```

---

## VecScatterDestroy#

**URL:** https://petsc.org/release/manualpages/Vec/VecScatterDestroy/

**Contents:**
- VecScatterDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#

Destroys a scatter context created by VecScatterCreate()

sf - the scatter context

Low-level Vector Communication, VecScatter, VecScatterCreate(), VecScatterCopy()

src/vec/vec/utils/vscat.c

src/ts/tutorials/ex29.c src/tao/constrained/tutorials/ex1.c src/ksp/ksp/tutorials/ex73.c src/tao/pde_constrained/tutorials/elliptic.c src/tao/pde_constrained/tutorials/parabolic.c src/ksp/ksp/tutorials/ex49.c src/vec/vec/utils/tagger/tutorials/ex1.c src/ksp/ksp/tutorials/ex43.c src/tao/pde_constrained/tutorials/hyperbolic.c src/vec/vec/tutorials/ex44.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecScatterCreate()
```

Example 2 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode VecScatterDestroy(VecScatter *sf)
```

Example 3 (unknown):
```unknown
VecScatterCreate()
```

Example 4 (unknown):
```unknown
VecScatterCopy()
```

---

## VecScatterEnd#

**URL:** https://petsc.org/release/manualpages/Vec/VecScatterEnd/

**Contents:**
- VecScatterEnd#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Ends a generalized scatter from one vector to another. Call after first calling VecScatterBegin().

Neighbor-wise Collective

sf - scatter context generated by VecScatterCreate()

x - the vector from which we scatter

y - the vector to which we scatter

addv - one of ADD_VALUES, MAX_VALUES, MIN_VALUES or INSERT_VALUES

mode - the scattering mode, usually SCATTER_FORWARD. The available modes are: SCATTER_FORWARD, SCATTER_REVERSE

If you use SCATTER_REVERSE the arguments x and y should be reversed, from the SCATTER_FORWARD.

y[iy[i]] = x[ix[i]], for i=0,…,ni-1

Low-level Vector Communication, VecScatter, VecScatterBegin(), VecScatterCreate()

src/vec/vec/utils/vscat.c

src/ts/tutorials/ex29.c src/tao/constrained/tutorials/ex1.c src/ksp/ksp/tutorials/ex73.c src/tao/pde_constrained/tutorials/elliptic.c src/tao/pde_constrained/tutorials/parabolic.c src/ksp/ksp/tutorials/ex49.c src/vec/vec/utils/tagger/tutorials/ex1.c src/ksp/ksp/tutorials/ex43.c src/tao/pde_constrained/tutorials/hyperbolic.c src/vec/vec/tutorials/ex44.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecScatterBegin()
```

Example 2 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode VecScatterEnd(VecScatter sf, Vec x, Vec y, InsertMode addv, ScatterMode mode)
```

Example 3 (unknown):
```unknown
VecScatterCreate()
```

Example 4 (unknown):
```unknown
INSERT_VALUES
```

---

## VecScatterGetMerged#

**URL:** https://petsc.org/release/manualpages/Vec/VecScatterGetMerged/

**Contents:**
- VecScatterGetMerged#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns true if the scatter is completed in the VecScatterBegin() and the VecScatterEnd() does nothing

sf - scatter context created with VecScatterCreate()

flg - PETSC_TRUE if the VecScatterBegin()/VecScatterEnd() are all done during the VecScatterBegin()

Low-level Vector Communication, VecScatter, VecScatterCreate(), VecScatterEnd(), VecScatterBegin()

src/vec/vec/utils/vscat.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecScatterBegin()
```

Example 2 (unknown):
```unknown
VecScatterEnd()
```

Example 3 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode VecScatterGetMerged(VecScatter sf, PetscBool *flg)
```

Example 4 (unknown):
```unknown
VecScatterCreate()
```

---

## VecScatterGetType#

**URL:** https://petsc.org/release/manualpages/Vec/VecScatterGetType/

**Contents:**
- VecScatterGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the vector scatter type name (as a string) from the VecScatter.

sf - The vector scatter

type - The vector scatter type name

Low-level Vector Communication, VecScatter, VecScatterType, VecScatterSetType(), VecScatterCreate()

src/vec/vec/utils/vscat.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode VecScatterGetType(VecScatter sf, VecScatterType *type)
```

Example 2 (unknown):
```unknown
VecScatterType
```

Example 3 (unknown):
```unknown
VecScatterSetType()
```

Example 4 (unknown):
```unknown
VecScatterCreate()
```

---

## VecScatterRegister#

**URL:** https://petsc.org/release/manualpages/Vec/VecScatterRegister/

**Contents:**
- VecScatterRegister#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Adds a new vector scatter component implementation

sname - The name of a new user-defined creation routine

function - The creation routine

Low-level Vector Communication, VecScatter, VecScatterType, VecRegister()

src/vec/vec/utils/vscat.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode VecScatterRegister(const char sname[], PetscErrorCode (*function)(VecScatter))
```

Example 2 (unknown):
```unknown
VecScatterType
```

Example 3 (unknown):
```unknown
VecRegister()
```

---

## VecScatterRemap#

**URL:** https://petsc.org/release/manualpages/Vec/VecScatterRemap/

**Contents:**
- VecScatterRemap#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Remaps the “from” and “to” indices in a vector scatter context.

sf - vector scatter context

tomap - remapping plan for “to” indices (may be NULL).

frommap - remapping plan for “from” indices (may be NULL)

In the parallel case the todata contains indices from where the data is taken (and then sent to others)! The fromdata contains indices from where the received data is finally put locally.

In the sequential case the todata contains indices from where the data is put and the fromdata contains indices from where the data is taken from. This is backwards from the parallel case!

Low-level Vector Communication, VecScatter, VecScatterCreate()

src/vec/vec/utils/vscat.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode VecScatterRemap(VecScatter sf, PetscInt tomap[], PetscInt frommap[])
```

Example 2 (unknown):
```unknown
VecScatterCreate()
```

---

## VecScatterSetFromOptions#

**URL:** https://petsc.org/release/manualpages/Vec/VecScatterSetFromOptions/

**Contents:**
- VecScatterSetFromOptions#
- Synopsis#
- Input Parameter#
- Notes#
- See Also#
- Level#
- Location#

Configures the vector scatter from values in the options database.

sf - The vector scatter

To see all options, run your program with the -help option, or consult the users manual.

Must be called before VecScatterSetUp() and before the vector scatter is used.

Low-level Vector Communication, VecScatter, VecScatterCreate(), VecScatterDestroy(), VecScatterSetUp()

src/vec/vec/utils/vscat.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode VecScatterSetFromOptions(VecScatter sf)
```

Example 2 (unknown):
```unknown
VecScatterSetUp()
```

Example 3 (unknown):
```unknown
VecScatterCreate()
```

Example 4 (unknown):
```unknown
VecScatterDestroy()
```

---

## VecScatterSetType#

**URL:** https://petsc.org/release/manualpages/Vec/VecScatterSetType/

**Contents:**
- VecScatterSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Builds a vector scatter, for a particular vector scatter implementation.

sf - The VecScatter object

type - The name of the vector scatter type

-sf_type type - Sets the VecScatterType

Use VecScatterDuplicate() to form additional vectors scatter of the same type as an existing vector scatter.

Low-level Vector Communication, VecScatter, VecScatterType, VecScatterGetType(), VecScatterCreate()

src/vec/vec/utils/vscat.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode VecScatterSetType(VecScatter sf, VecScatterType type)
```

Example 2 (unknown):
```unknown
VecScatterType
```

Example 3 (unknown):
```unknown
VecScatterDuplicate()
```

Example 4 (unknown):
```unknown
VecScatterType
```

---

## VecScatterSetUp#

**URL:** https://petsc.org/release/manualpages/Vec/VecScatterSetUp/

**Contents:**
- VecScatterSetUp#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Sets up the VecScatter to be able to actually scatter information between vectors

sf - the scatter context

Low-level Vector Communication, VecScatter, VecScatterCreate(), VecScatterCopy()

src/vec/vec/utils/vscat.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode VecScatterSetUp(VecScatter sf)
```

Example 2 (unknown):
```unknown
VecScatterCreate()
```

Example 3 (unknown):
```unknown
VecScatterCopy()
```

---

## VecScatterViewFromOptions#

**URL:** https://petsc.org/release/manualpages/Vec/VecScatterViewFromOptions/

**Contents:**
- VecScatterViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

View a VecScatter object based on values in the options database

sf - the scatter context

obj - Optional object

name - command line option

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

Low-level Vector Communication, VecScatter, VecScatterView(), PetscObjectViewFromOptions(), VecScatterCreate()

src/vec/vec/utils/vscat.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode VecScatterViewFromOptions(VecScatter sf, PetscObject obj, const char name[])
```

Example 2 (unknown):
```unknown
PetscObjectViewFromOptions()
```

Example 3 (unknown):
```unknown
VecScatterView()
```

Example 4 (unknown):
```unknown
PetscObjectViewFromOptions()
```

---

## VecScatterView#

**URL:** https://petsc.org/release/manualpages/Vec/VecScatterView/

**Contents:**
- VecScatterView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Views a vector scatter context.

sf - the scatter context

viewer - the viewer for displaying the context

Low-level Vector Communication, VecScatter, PetscViewer, VecScatterViewFromOptions(), PetscObjectViewFromOptions(), VecScatterCreate()

src/vec/vec/utils/vscat.c

src/dm/tutorials/ex14.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode VecScatterView(VecScatter sf, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
VecScatterViewFromOptions()
```

Example 4 (unknown):
```unknown
PetscObjectViewFromOptions()
```

---

## VecsCreateSeqWithArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecsCreateSeqWithArray/

**Contents:**
- VecsCreateSeqWithArray#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Creates a Vecs object holding p sequential Vecs of length m that use a user-provided contiguous array as storage

comm - the MPI communicator (typically PETSC_COMM_SELF)

p - the number of vectors

m - the length of each vector

a - the array of length p*m used as storage for the vectors

x - the newly created Vecs

Vecs, VecsCreateSeq(), VecsDuplicate(), VecsDestroy(), VecCreateSeqWithArray()

src/vec/vec/utils/vecs.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode VecsCreateSeqWithArray(MPI_Comm comm, PetscInt p, PetscInt m, PetscScalar *a, Vecs *x)
```

Example 2 (unknown):
```unknown
PETSC_COMM_SELF
```

Example 3 (unknown):
```unknown
VecsCreateSeq()
```

Example 4 (unknown):
```unknown
VecsDuplicate()
```

---

## VecsCreateSeq#

**URL:** https://petsc.org/release/manualpages/Vec/VecsCreateSeq/

**Contents:**
- VecsCreateSeq#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Creates a Vecs object holding p sequential Vecs of length m, all stored contiguously in a single underlying Vec

comm - the MPI communicator (typically PETSC_COMM_SELF)

p - the number of vectors

m - the length of each vector

x - the newly created Vecs

Vecs, VecsCreateSeqWithArray(), VecsDuplicate(), VecsDestroy(), VecCreateSeq()

src/vec/vec/utils/vecs.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode VecsCreateSeq(MPI_Comm comm, PetscInt p, PetscInt m, Vecs *x)
```

Example 2 (unknown):
```unknown
PETSC_COMM_SELF
```

Example 3 (unknown):
```unknown
VecsCreateSeqWithArray()
```

Example 4 (unknown):
```unknown
VecsDuplicate()
```

---

## VecsDestroy#

**URL:** https://petsc.org/release/manualpages/Vec/VecsDestroy/

**Contents:**
- VecsDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Destroys a Vecs collection of vectors

x - the Vecs object to destroy

Vecs, VecsCreateSeq(), VecsCreateSeqWithArray(), VecsDuplicate()

src/vec/vec/utils/vecs.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode VecsDestroy(Vecs x)
```

Example 2 (unknown):
```unknown
VecsCreateSeq()
```

Example 3 (unknown):
```unknown
VecsCreateSeqWithArray()
```

Example 4 (unknown):
```unknown
VecsDuplicate()
```

---

## VecsDuplicate#

**URL:** https://petsc.org/release/manualpages/Vec/VecsDuplicate/

**Contents:**
- VecsDuplicate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Creates a new Vecs with the same size and layout as an existing Vecs, but does not copy the values

x - the existing Vecs

y - the newly created Vecs

Vecs, VecsCreateSeq(), VecsCreateSeqWithArray(), VecsDestroy(), VecDuplicate()

src/vec/vec/utils/vecs.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode VecsDuplicate(Vecs x, Vecs *y)
```

Example 2 (unknown):
```unknown
VecsCreateSeq()
```

Example 3 (unknown):
```unknown
VecsCreateSeqWithArray()
```

Example 4 (unknown):
```unknown
VecsDestroy()
```

---

## VECSEQCUDA#

**URL:** https://petsc.org/release/manualpages/Vec/VECSEQCUDA/

**Contents:**
- VECSEQCUDA#
- Options Database Key#
- See Also#
- Level#
- Location#

VECSEQCUDA = “seqcuda” - The basic sequential vector, modified to use CUDA

-vec_type seqcuda - sets the vector type to VECSEQCUDA during a call to VecSetFromOptions()

VecCreate(), VecSetType(), VecSetFromOptions(), VecCreateMPIWithArray(), VECSEQ, VecType, VecCreateMPI(), VecSetPinnedMemoryMin(), VECCUDA, VECHIP, VECMPICUDA, VECMPIHIP, VECSEQHIP

src/vec/vec/impls/seq/cupm/cuda/vecseqcupm.cu

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecSetFromOptions()
```

Example 2 (unknown):
```unknown
VecCreate()
```

Example 3 (unknown):
```unknown
VecSetType()
```

Example 4 (unknown):
```unknown
VecSetFromOptions()
```

---

## VECSEQHIP#

**URL:** https://petsc.org/release/manualpages/Vec/VECSEQHIP/

**Contents:**
- VECSEQHIP#
- Options Database Key#
- See Also#
- Level#
- Location#

VECSEQHIP = “seqcuda” - The basic sequential vector, modified to use HIP

-vec_type seqcuda - sets the vector type to VECSEQHIP during a call to VecSetFromOptions()

VecCreate(), VecSetType(), VecSetFromOptions(), VecCreateMPIWithArray(), VECSEQ, VecType, VecCreateMPI(), VecSetPinnedMemoryMin(), VECCUDA, VECHIP, VECMPICUDA, VECMPIHIP, VECSEQCUDA

src/vec/vec/impls/seq/cupm/hip/vecseqcupm.hip.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecSetFromOptions()
```

Example 2 (unknown):
```unknown
VecCreate()
```

Example 3 (unknown):
```unknown
VecSetType()
```

Example 4 (unknown):
```unknown
VecSetFromOptions()
```

---

## VECSEQKOKKOS#

**URL:** https://petsc.org/release/manualpages/Vec/VECSEQKOKKOS/

**Contents:**
- VECSEQKOKKOS#
- Options Database Keys#
- See Also#
- Level#
- Location#

VECSEQKOKKOS = “seqkokkos” - The basic sequential vector, modified to use Kokkos

-vec_type seqkokkos - sets the vector type to VECSEQKOKKOS during a call to VecSetFromOptions()

VecCreate(), VecSetType(), VecSetFromOptions(), VecCreateMPIWithArray(), VECMPI, VecType, VecCreateMPI()

src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecCreate()
```

Example 2 (unknown):
```unknown
VecSetType()
```

Example 3 (unknown):
```unknown
VecSetFromOptions()
```

Example 4 (unknown):
```unknown
VecCreateMPIWithArray()
```

---

## VECSEQVIENNACL#

**URL:** https://petsc.org/release/manualpages/Vec/VECSEQVIENNACL/

**Contents:**
- VECSEQVIENNACL#
- Options Database Keys#
- See Also#
- Level#
- Location#

VECSEQVIENNACL = “seqviennacl” - The basic sequential vector, modified to use ViennaCL

-vec_type seqviennacl - sets the vector type to VECSEQVIENNACL during a call to VecSetFromOptions()

VecCreate(), VecSetType(), VecSetFromOptions(), VecCreateSeqWithArray(), VECMPI, VecType, VecCreateMPI(), VecCreateSeq()

src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecCreate()
```

Example 2 (unknown):
```unknown
VecSetType()
```

Example 3 (unknown):
```unknown
VecSetFromOptions()
```

Example 4 (unknown):
```unknown
VecCreateSeqWithArray()
```

---

## VECSEQ#

**URL:** https://petsc.org/release/manualpages/Vec/VECSEQ/

**Contents:**
- VECSEQ#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#

VECSEQ = “seq” - The basic sequential vector

-vec_type seq - sets the vector type to VECSEQ during a call to VecSetFromOptions()

VecCreate(), VecSetType(), VecSetFromOptions(), VecCreateSeqWithArray(), VECMPI, VecType, VecCreateMPI(), VecCreateSeq()

src/vec/vec/impls/seq/bvec3.c

src/ksp/pc/tutorials/ex4.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecCreate()
```

Example 2 (unknown):
```unknown
VecSetType()
```

Example 3 (unknown):
```unknown
VecSetFromOptions()
```

Example 4 (unknown):
```unknown
VecCreateSeqWithArray()
```

---

## VecSetBindingPropagates#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetBindingPropagates/

**Contents:**
- VecSetBindingPropagates#
- Synopsis#
- Input Parameters#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#

Sets whether the state of being bound to the CPU for a GPU vector type propagates to child and some other associated objects

flg - flag indicating whether the boundtocpu flag should be propagated

If the value of flg is set to true, then VecDuplicate() and VecDuplicateVecs() will bind created vectors to GPU if the input vector is bound to the CPU. The created vectors will also have their bindingpropagates flag set to true.

If a DMDA has the -dm_bind_below option set to true, then vectors created by DMCreateGlobalVector() will have VecSetBindingPropagates() called on them to set their bindingpropagates flag to true.

Vectors and Parallel Data, Vec, MatSetBindingPropagates(), VecGetBindingPropagates()

src/vec/vec/interface/vector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecSetBindingPropagates(Vec v, PetscBool flg)
```

Example 2 (unknown):
```unknown
VecDuplicate()
```

Example 3 (unknown):
```unknown
VecDuplicateVecs()
```

Example 4 (unknown):
```unknown
-dm_bind_below option
```

---

## VecSetBlockSize#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetBlockSize/

**Contents:**
- VecSetBlockSize#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the block size for future calls to VecSetValuesBlocked() and VecSetValuesBlockedLocal().

All vectors obtained by VecDuplicate() inherit the same blocksize.

Vectors obtained with DMCreateGlobalVector() and DMCreateLocalVector() generally already have a blocksize set based on the state of the DM

Vectors and Parallel Data, Vec, VecSetValuesBlocked(), VecSetLocalToGlobalMapping(), VecGetBlockSize()

src/vec/vec/interface/vector.c

src/ksp/ksp/tutorials/ex56.c src/vec/vec/tutorials/ex12.c src/vec/vec/tutorials/ex12f.F90 src/ksp/ksp/tutorials/ex73.c src/vec/vec/tutorials/ex16.c src/vec/vec/tutorials/ex16f.F90 src/vec/vec/tutorials/ex11f90.F90 src/vec/vec/utils/tagger/tutorials/ex1.c src/vec/vec/tutorials/ex13.c src/vec/vec/tutorials/ex11f.F90

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecSetValuesBlocked()
```

Example 2 (unknown):
```unknown
VecSetValuesBlockedLocal()
```

Example 3 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecSetBlockSize(Vec v, PetscInt bs)
```

Example 4 (unknown):
```unknown
VecDuplicate()
```

---

## VecSetErrorIfLocked#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetErrorIfLocked/

**Contents:**
- VecSetErrorIfLocked#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Raise an error if the Vec is currently locked for read or write access.

Not Collective; No Fortran Support

arg - the argument position of x in the calling routine, used in the error message

This is intended as an internal check for routines that must have exclusive access to a Vec. A locked Vec typically indicates that another routine currently holds a read or write reference to it.

Vec, VecLockGet(), VecLockGetLocation(), VecLockReadPush(), VecLockReadPop(), VecLockWriteSet()

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
static inline PetscErrorCode VecSetErrorIfLocked(Vec x, PetscInt arg)
```

Example 2 (unknown):
```unknown
VecLockGet()
```

Example 3 (unknown):
```unknown
VecLockGetLocation()
```

Example 4 (unknown):
```unknown
VecLockReadPush()
```

---

## VecSetFromOptions#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetFromOptions/

**Contents:**
- VecSetFromOptions#
- Synopsis#
- Input Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Configures the vector from the options database.

To see all options, run your program with the -help option.

Must be called after VecCreate() but before the vector is used.

Vectors and Parallel Data, Vec, VecCreate(), VecSetOptionsPrefix()

src/vec/vec/interface/vector.c

src/snes/tutorials/ex99.c src/snes/tutorials/ex59.c src/snes/tutorials/ex1.c src/snes/tutorials/ex6.c src/snes/tutorials/ex73f90t.F90 src/mat/tutorials/ex19.c src/snes/tutorials/ex42.c src/snes/tutorials/ex2.c src/snes/tutorials/ex30.c src/snes/tutorials/ex31.c

VecSetFromOptions_MPI() in src/vec/vec/impls/mpi/pbvec.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecSetFromOptions(Vec vec)
```

Example 2 (unknown):
```unknown
VecCreate()
```

Example 3 (unknown):
```unknown
VecCreate()
```

Example 4 (unknown):
```unknown
VecSetOptionsPrefix()
```

---

## VecSetInf#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetInf/

**Contents:**
- VecSetInf#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

set infinity into the local part of the vector

Deprecated, see VecFlag() This is used for any subset of MPI processes to indicate an failure in a solver, after the next use of VecNorm() if KSPCheckNorm() detects an infinity and at least one of the MPI processes has a not converged reason then the KSP object collectively is labeled as not converged.

This cannot be called if xin has a cached norm available

Vectors and Parallel Data, VecFlag(), Vec, PetscLayout, VecGetLayout(), VecGetSize(), VecGetOwnershipRange(), VecGetOwnershipRanges()

src/vec/vec/interface/vector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecSetInf(Vec xin)
```

Example 2 (unknown):
```unknown
KSPCheckNorm()
```

Example 3 (unknown):
```unknown
PetscLayout
```

Example 4 (unknown):
```unknown
VecGetLayout()
```

---

## VecSetLayout#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetLayout/

**Contents:**
- VecSetLayout#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

set PetscLayout describing vector layout

It is normally only valid to replace the layout with a layout known to be equivalent.

Vectors and Parallel Data, Vec, PetscLayout, VecGetLayout(), VecGetSize(), VecGetOwnershipRange(), VecGetOwnershipRanges()

src/vec/vec/interface/vector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLayout
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecSetLayout(Vec x, PetscLayout map)
```

Example 3 (unknown):
```unknown
PetscLayout
```

Example 4 (unknown):
```unknown
VecGetLayout()
```

---

## VecSetLocalToGlobalMapping#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetLocalToGlobalMapping/

**Contents:**
- VecSetLocalToGlobalMapping#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets a local numbering to global numbering used by the routine VecSetValuesLocal() to allow users to insert vector entries using a local (per-processor) numbering.

mapping - mapping created with ISLocalToGlobalMappingCreate() or ISLocalToGlobalMappingCreateIS()

All vectors obtained with VecDuplicate() from this vector inherit the same mapping.

Vectors obtained with DMCreateGlobaVector() will often have this attribute attached to the vector so this call is not needed

Vectors and Parallel Data, Vec, VecAssemblyBegin(), VecAssemblyEnd(), VecSetValues(), VecSetValuesLocal(), VecGetLocalToGlobalMapping(), VecSetValuesBlockedLocal()

src/vec/vec/interface/vector.c

src/vec/vec/tutorials/ex8f.F90 src/vec/vec/tutorials/ex8.c src/ksp/ksp/tutorials/ex71.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecSetValuesLocal()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecSetLocalToGlobalMapping(Vec x, ISLocalToGlobalMapping mapping)
```

Example 3 (unknown):
```unknown
ISLocalToGlobalMappingCreate()
```

Example 4 (unknown):
```unknown
ISLocalToGlobalMappingCreateIS()
```

---

## VecSetOperation#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetOperation/

**Contents:**
- VecSetOperation#
- Synopsis#
- Input Parameters#
- Example Usage#
- Notes#
- See Also#
- Level#
- Location#

Allows the user to override a particular vector operation.

Logically Collective; No Fortran Support

vec - The vector to modify

op - The name of the operation

f - The function that provides the operation.

f may be NULL to remove the operation from vec. Depending on the operation this may be allowed, however some always expect a valid function. In these cases an error will be raised when calling the interface routine in question.

See VecOperation for an up-to-date list of override-able operations. The operations listed there have the form VECOP_<OPERATION>, where <OPERATION> is the suffix (in all capital letters) of the public interface routine (e.g., VecView() -> VECOP_VIEW).

Overriding a particular Vec’s operation has no affect on any other Vecs past, present, or future. The user should also note that overriding a method is “destructive”; the previous method is not retained in any way.

Each function MUST return PETSC_SUCCESS on success and nonzero on failure.

Vectors and Parallel Data, Vec, VecCreate(), VecGetOperation(), MatSetOperation(), MatShellSetOperation()

src/vec/vec/interface/vector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecSetOperation(Vec vec, VecOperation op, PetscErrorCodeFn *f)
```

Example 2 (lua):
```lua
// some new VecView() implementation, must have the same signature as the function it seeks
  // to replace
  PetscErrorCode UserVecView(Vec x, PetscViewer viewer)
  {
    PetscFunctionBeginUser;
    // ...
    PetscFunctionReturn(PETSC_SUCCESS);
  }

  // Create a VECMPI which has a pre-defined VecView() implementation
  VecCreateMPI(comm, n, N, &x);
  // Calls the VECMPI implementation for VecView()
  VecView(x, viewer);

  VecSetOperation(x, VECOP_VIEW, (PetscErrorCodeFn *)UserVecView);
  // Now calls UserVecView()
  VecView(x, viewer);
```

Example 3 (unknown):
```unknown
VecOperation
```

Example 4 (typescript):
```typescript
VECOP_<OPERATION>
```

---

## VecSetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetOptionsPrefix/

**Contents:**
- VecSetOptionsPrefix#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the prefix used for searching for all Vec options in the database.

prefix - the prefix to prepend to all option names

A hyphen (-) must NOT be given at the beginning of the prefix name. The first character of all runtime options is AUTOMATICALLY the hyphen.

Vectors and Parallel Data, Vec, VecSetFromOptions()

src/vec/vec/interface/vector.c

src/ts/tutorials/ex45.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecSetOptionsPrefix(Vec v, const char prefix[])
```

Example 2 (unknown):
```unknown
VecSetFromOptions()
```

---

## VecSetOption#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetOption/

**Contents:**
- VecSetOption#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets an option for controlling a vector’s behavior with VecSetValues() and related routines

flag - turn the option on or off

Vectors and Parallel Data, Vec, VecSetValues(), VecOption, MatSetOption()

src/vec/vec/interface/vector.c

src/ksp/ksp/tutorials/ex71.c

VecSetOption_MPI() in src/vec/vec/impls/mpi/pbvec.c VecSetOption_Seq() in src/vec/vec/impls/seq/bvec2.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecSetValues()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecSetOption(Vec x, VecOption op, PetscBool flag)
```

Example 3 (unknown):
```unknown
VecSetValues()
```

Example 4 (unknown):
```unknown
MatSetOption()
```

---

## VecSetPinnedMemoryMin#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetPinnedMemoryMin/

**Contents:**
- VecSetPinnedMemoryMin#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Set the minimum data size for which pinned memory will be used for host (CPU) allocations.

mbytes - minimum data size in bytes

-vec_pinned_memory_min size - minimum size (in bytes) for an allocation to use pinned memory on host.

Specifying -1 ensures that pinned memory will never be used.

Vectors and Parallel Data, Vec, VecGetPinnedMemoryMin()

src/vec/vec/interface/vector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecSetPinnedMemoryMin(Vec v, size_t mbytes)
```

Example 2 (unknown):
```unknown
VecGetPinnedMemoryMin()
```

---

## VecSetPreallocationCOOLocal#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetPreallocationCOOLocal/

**Contents:**
- VecSetPreallocationCOOLocal#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

set preallocation for vectors using a coordinate format of the entries with local indices

x - vector being preallocated

ncoo - number of entries

coo_i - row indices (local numbering; may be modified)

This and VecSetValuesCOO() provide an alternative API to using VecSetValuesLocal() to provide vector values.

This API is particularly efficient for use on GPUs.

The local indices are translated using the local to global mapping, thus VecSetLocalToGlobalMapping() must have been called prior to this function.

The indices coo_i may be modified within this function. They might be translated to corresponding global indices, but the caller should not rely on them having any specific value after this function returns. The arrays can be freed or reused immediately after this function returns.

Entries can be repeated. Negative indices and remote indices might be allowed. see VecSetPreallocationCOO().

Vectors and Parallel Data, Vec, VecSetPreallocationCOO(), VecSetValuesCOO()

src/vec/vec/interface/vector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecSetPreallocationCOOLocal(Vec x, PetscCount ncoo, PetscInt coo_i[])
```

Example 2 (unknown):
```unknown
VecSetValuesCOO()
```

Example 3 (unknown):
```unknown
VecSetValuesLocal()
```

Example 4 (unknown):
```unknown
VecSetLocalToGlobalMapping()
```

---

## VecSetPreallocationCOO#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetPreallocationCOO/

**Contents:**
- VecSetPreallocationCOO#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

set preallocation for a vector using a coordinate format of the entries with global indices

x - vector being preallocated

ncoo - number of entries

coo_i - entry indices

This and VecSetValuesCOO() provide an alternative API to using VecSetValues() to provide vector values.

This API is particularly efficient for use on GPUs.

Entries can be repeated, see VecSetValuesCOO(). Negative indices are not allowed unless vector option VEC_IGNORE_NEGATIVE_INDICES is set, in which case they, along with the corresponding entries in VecSetValuesCOO(), are ignored. If vector option VEC_NO_OFF_PROC_ENTRIES is set, remote entries are ignored, otherwise, they will be properly added or inserted to the vector.

The array coo_i[] may be freed immediately after calling this function.

Vectors and Parallel Data, Vec, VecSetValuesCOO(), VecSetPreallocationCOOLocal()

src/vec/vec/interface/vector.c

VecSetPreallocationCOO_MPIKokkos() in src/vec/vec/impls/mpi/kokkos/mpikok.kokkos.cxx VecSetPreallocationCOO_MPI() in src/vec/vec/impls/mpi/pdvec.c VecSetPreallocationCOO_Seq() in src/vec/vec/impls/seq/bvec2.c VecSetPreallocationCOO_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecSetPreallocationCOO(Vec x, PetscCount ncoo, const PetscInt coo_i[])
```

Example 2 (unknown):
```unknown
VecSetValuesCOO()
```

Example 3 (unknown):
```unknown
VecSetValues()
```

Example 4 (unknown):
```unknown
VecSetValuesCOO()
```

---

## VecSetRandomGaussian#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetRandomGaussian/

**Contents:**
- VecSetRandomGaussian#
- Synopsis#
- Input Parameters#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Fills a vector with Gaussian random values of the given mean and standard deviation.

v - the vector to fill

rng - PETSc random number generator

mean - desired mean of the Gaussian samples

std_dev - desired standard deviation

For complex builds where PetscScalar is complex the imaginary part of all the vector entries is zero

Uses the Box-Muller transform to generate normally distributed random numbers from uniform random numbers. Handles edge cases where uniform random values approach 0 or 1.

Vectors and Parallel Data, PetscDA: Data Assimilation, PetscDA, PetscRandom, PetscRandomSetInterval(), VecSetRandom()

src/vec/vec/interface/vector.c

src/ml/da/tutorials/ex3.c src/ml/da/tutorials/ex4.c src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex1.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecSetRandomGaussian(Vec v, PetscRandom rng, PetscReal mean, PetscReal std_dev)
```

Example 2 (unknown):
```unknown
PetscScalar
```

Example 3 (unknown):
```unknown
PetscRandom
```

Example 4 (unknown):
```unknown
PetscRandomSetInterval()
```

---

## VecSetRandom#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetRandom/

**Contents:**
- VecSetRandom#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Example of Usage#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets all components of a vector to random numbers.

rctx - the random number context, formed by PetscRandomCreate(), or use NULL and it will create one internally.

Vectors and Parallel Data, Vec, VecSet(), VecSetValues(), PetscRandomCreate(), PetscRandomDestroy()

src/vec/vec/interface/vector.c

src/ksp/pc/tutorials/ex4.c src/ksp/ksp/tutorials/ex2f.F90 src/snes/tutorials/ex11.c src/ksp/pc/tutorials/ex3.c src/ksp/ksp/tutorials/ex18.c src/ksp/ksp/tutorials/ex86.c src/snes/tutorials/ex69.c src/snes/tutorials/ex7.c src/snes/tutorials/ex64.c src/ksp/ksp/tutorials/ex82.c

VecSetRandom_Nest() in src/vec/vec/impls/nest/vecnest.c VecSetRandom_Seq() in src/vec/vec/impls/seq/bvec2.c VecSetRandom_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecSetRandom_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecSetRandom(Vec x, PetscRandom rctx)
```

Example 2 (unknown):
```unknown
PetscRandomCreate()
```

Example 3 (unknown):
```unknown
PetscRandomCreate(PETSC_COMM_WORLD,&rctx);
     VecSetRandom(x,rctx);
     PetscRandomDestroy(&rctx);
```

Example 4 (unknown):
```unknown
VecSetValues()
```

---

## VecSetSizes#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetSizes/

**Contents:**
- VecSetSizes#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the local and global sizes, and checks to determine compatibility of the sizes

n - the local size (or PETSC_DECIDE to have it set)

N - the global size (or PETSC_DETERMINE to have it set)

N cannot be PETSC_DETERMINE if n is PETSC_DECIDE

If one processor calls this with N of PETSC_DETERMINE then all processors must, otherwise the program will hang.

If n is not PETSC_DECIDE, then the value determines the PetscLayout of the vector and the ranges returned by VecGetOwnershipRange() and VecGetOwnershipRanges()

Vectors and Parallel Data, Vec, VecCreate(), VecCreateSeq(), VecCreateMPI(), VecGetSize(), PetscSplitOwnership(), PetscLayout, VecGetOwnershipRange(), VecGetOwnershipRanges(), MatSetSizes()

src/vec/vec/interface/vector.c

src/snes/tutorials/ex99.c src/snes/tutorials/ex59.c src/snes/tutorials/ex1.c src/snes/tutorials/ex6.c src/snes/tutorials/ex73f90t.F90 src/mat/tutorials/ex19.c src/snes/tutorials/ex42.c src/snes/tutorials/ex70.c src/snes/tutorials/ex7.c src/snes/tutorials/ex31.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecSetSizes(Vec v, PetscInt n, PetscInt N)
```

Example 2 (unknown):
```unknown
PETSC_DECIDE
```

Example 3 (unknown):
```unknown
PETSC_DETERMINE
```

Example 4 (unknown):
```unknown
PETSC_DETERMINE
```

---

## VecSetType#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetType/

**Contents:**
- VecSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Builds a vector, for a particular vector implementation.

vec - The vector object

newType - The name of the vector type

-vec_type type - Sets the vector type; see VecType

See VecType for available vector types (for instance, VECSEQ or VECMPI) Changing a vector to a new type will retain its old value if any.

Use VecDuplicate() or VecDuplicateVecs() to form additional vectors of the same type as an existing vector.

Vectors and Parallel Data, Vec, VecType, VecGetType(), VecCreate(), VecDuplicate(), VecDuplicateVecs()

src/vec/vec/interface/vecreg.c

src/ksp/pc/tutorials/ex4.c src/vec/vec/tutorials/ex10.c src/tao/pde_constrained/tutorials/hyperbolic.c src/ksp/ksp/tutorials/ex73.c src/vec/vec/tutorials/ex9.c src/snes/tutorials/ex70.c src/snes/tutorials/ex7.c src/tao/constrained/tutorials/maros.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"  
PetscErrorCode VecSetType(Vec vec, VecType newType)
```

Example 2 (unknown):
```unknown
VecDuplicate()
```

Example 3 (unknown):
```unknown
VecDuplicateVecs()
```

Example 4 (unknown):
```unknown
VecGetType()
```

---

## VecSetUp#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetUp/

**Contents:**
- VecSetUp#
- Synopsis#
- Input Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets up the internal vector data structures for the later use.

For basic use of the Vec classes the user need not explicitly call VecSetUp(), since these actions will happen automatically.

Vectors and Parallel Data, Vec, VecCreate(), VecDestroy()

src/vec/vec/interface/vector.c

src/vec/is/sf/tutorials/ex2.c src/ksp/ksp/tutorials/ex56.c src/ts/tutorials/ex51.c src/mat/tutorials/ex19.c src/ts/tutorials/ex40.c src/vec/is/sf/tutorials/ex3.c src/vec/vec/utils/tagger/tutorials/ex1.c src/tao/constrained/tutorials/ex1.c src/ts/tutorials/ex41.c src/vec/vec/tutorials/ex44.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecSetUp(Vec v)
```

Example 2 (unknown):
```unknown
VecCreate()
```

Example 3 (unknown):
```unknown
VecDestroy()
```

---

## VecSetValueLocal#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetValueLocal/

**Contents:**
- VecSetValueLocal#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Set a single entry into a vector using the local numbering of the vector, see VecSetValuesLocal()

row - the local row location of the entry

value - the value to insert

mode - either INSERT_VALUES or ADD_VALUES

For efficiency one should use VecSetValuesLocal() and set several or many values simultaneously if possible.

These values may be cached, so VecAssemblyBegin() and VecAssemblyEnd() MUST be called after all calls to VecSetValueLocal() have been completed.

See VecSetLocalToGlobalMapping() for how the local numbering is defined

VecSetValueLocal() uses 0-based indices in Fortran as well as in C.

Vectors and Parallel Data, VecSetValuesLocal(), VecSetValues(), VecAssemblyBegin(), VecAssemblyEnd(), VecSetValuesBlockedLocal(), VecSetValue(), VecSetLocalToGlobalMapping()

src/vec/vec/tutorials/ex9.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecSetValuesLocal()
```

Example 2 (unknown):
```unknown
static inline PetscErrorCode VecSetValueLocal(Vec v, PetscInt i, PetscScalar va, InsertMode mode)
```

Example 3 (unknown):
```unknown
INSERT_VALUES
```

Example 4 (unknown):
```unknown
VecSetValuesLocal()
```

---

## VecSetValuesBlockedLocal#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetValuesBlockedLocal/

**Contents:**
- VecSetValuesBlockedLocal#
- Synopsis#
- Input Parameters#
- Notes#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Inserts or adds values into certain locations of a vector, using a local ordering of the nodes.

x - vector to insert in

ni - number of blocks to add

ix - indices where to add in block count, not element count

y - array of values. Pass NULL to set all zeroes.

iora - either INSERT_VALUES replaces existing entries with new values, ADD_VALUES adds values to any existing entries

VecSetValuesBlockedLocal() sets x[bsix[i]+j] = y[bsi+j], for j=0,..bs-1, for i=0,…,ni-1, where bs has been set with VecSetBlockSize().

Calls to VecSetValuesBlockedLocal() with the INSERT_VALUES and ADD_VALUES options cannot be mixed without intervening calls to the assembly routines.

These values may be cached, so VecAssemblyBegin() and VecAssemblyEnd() MUST be called after all calls to VecSetValuesBlockedLocal() have been completed.

VecSetValuesBlockedLocal() uses 0-based indices in Fortran as well as in C.

If any of ix and y are scalars pass them using, for example,

Vectors and Parallel Data, Vec, VecAssemblyBegin(), VecAssemblyEnd(), VecSetValues(), VecSetValuesBlocked(), VecSetLocalToGlobalMapping()

src/vec/vec/interface/rvector.c

src/ksp/ksp/tutorials/ex71.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecSetValuesBlockedLocal(Vec x, PetscInt ni, const PetscInt ix[], const PetscScalar y[], InsertMode iora)
```

Example 2 (unknown):
```unknown
INSERT_VALUES
```

Example 3 (unknown):
```unknown
VecSetValuesBlockedLocal()
```

Example 4 (unknown):
```unknown
VecSetBlockSize()
```

---

## VecSetValuesBlocked#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetValuesBlocked/

**Contents:**
- VecSetValuesBlocked#
- Synopsis#
- Input Parameters#
- Notes#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Inserts or adds blocks of values into certain locations of a vector.

x - vector to insert in

ni - number of blocks to add

ix - indices where to add in block count, rather than element count

y - array of values. Pass NULL to set all zeroes.

iora - either INSERT_VALUES replaces existing entries with new values, ADD_VALUES, adds values to any existing entries

VecSetValuesBlocked() sets x[bsix[i]+j] = y[bsi+j], for j=0,…,bs-1, for i=0,…,ni-1. where bs was set with VecSetBlockSize().

Calls to VecSetValuesBlocked() with the INSERT_VALUES and ADD_VALUES options cannot be mixed without intervening calls to the assembly routines.

These values may be cached, so VecAssemblyBegin() and VecAssemblyEnd() MUST be called after all calls to VecSetValuesBlocked() have been completed.

VecSetValuesBlocked() uses 0-based indices in Fortran as well as in C.

Negative indices may be passed in ix, these rows are simply ignored. This allows easily inserting element load matrices with homogeneous Dirichlet boundary conditions that you don’t want represented in the vector.

If any of ix and y are scalars pass them using, for example,

Vectors and Parallel Data, Vec, VecAssemblyBegin(), VecAssemblyEnd(), VecSetValuesBlockedLocal(), VecSetValues()

src/vec/vec/interface/rvector.c

src/ksp/ksp/tutorials/ex56.c

VecSetValuesBlocked_MPI() in src/vec/vec/impls/mpi/pdvec.c VecSetValuesBlocked_Seq() in src/vec/vec/impls/seq/bvec2.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecSetValuesBlocked(Vec x, PetscInt ni, const PetscInt ix[], const PetscScalar y[], InsertMode iora)
```

Example 2 (unknown):
```unknown
INSERT_VALUES
```

Example 3 (unknown):
```unknown
VecSetValuesBlocked()
```

Example 4 (unknown):
```unknown
VecSetValuesBlocked()
```

---

## VecSetValuesCOO#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetValuesCOO/

**Contents:**
- VecSetValuesCOO#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

set values at once in a vector preallocated using VecSetPreallocationCOO()

coo_v - the value array

imode - the insert mode

This and VecSetPreallocationCOO() or ``VecSetPreallocationCOOLocal() provide an alternative API to using VecSetValues() to provide vector values.

This API is particularly efficient for use on GPUs.

The values must follow the order of the indices prescribed with VecSetPreallocationCOO() or VecSetPreallocationCOOLocal(). When repeated entries are specified in the COO indices the coo_v values are first properly summed, regardless of the value of imode. The imode flag indicates if coo_v must be added to the current values of the vector (ADD_VALUES) or overwritten (INSERT_VALUES). VecAssemblyBegin() and VecAssemblyEnd() do not need to be called after this routine. It automatically handles the assembly process.

Vectors and Parallel Data, Vec, VecSetPreallocationCOO(), VecSetPreallocationCOOLocal(), VecSetValues()

src/vec/vec/interface/vector.c

VecSetValuesCOO_MPIKokkos() in src/vec/vec/impls/mpi/kokkos/mpikok.kokkos.cxx VecSetValuesCOO_MPI() in src/vec/vec/impls/mpi/pdvec.c VecSetValuesCOO_Seq() in src/vec/vec/impls/seq/bvec2.c VecSetValuesCOO_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecSetPreallocationCOO()
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecSetValuesCOO(Vec x, const PetscScalar coo_v[], InsertMode imode)
```

Example 3 (unknown):
```unknown
VecSetPreallocationCOO() or ``VecSetPreallocationCOOLocal()
```

Example 4 (unknown):
```unknown
VecSetValues()
```

---

## VecSetValuesLocal#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetValuesLocal/

**Contents:**
- VecSetValuesLocal#
- Synopsis#
- Input Parameters#
- Notes#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Inserts or adds values into certain locations of a vector, using a local ordering of the nodes.

x - vector to insert in

ni - number of elements to add

ix - indices where to add

y - array of values. Pass NULL to set all zeroes.

iora - either INSERT_VALUES replaces existing entries with new values, ADD_VALUES adds values to any existing entries

VecSetValuesLocal() sets x[ix[i]] = y[i], for i=0,…,ni-1.

Calls to VecSetValuesLocal() with the INSERT_VALUES and ADD_VALUES options cannot be mixed without intervening calls to the assembly routines.

These values may be cached, so VecAssemblyBegin() and VecAssemblyEnd() MUST be called after all calls to VecSetValuesLocal() have been completed.

VecSetValuesLocal() uses 0-based indices in Fortran as well as in C.

If any of ix and y are scalars pass them using, for example,

Vectors and Parallel Data, Vec, VecAssemblyBegin(), VecAssemblyEnd(), VecSetValues(), VecSetLocalToGlobalMapping(), VecSetValuesBlockedLocal()

src/vec/vec/interface/rvector.c

src/vec/vec/tutorials/ex8f.F90 src/tao/unconstrained/tutorials/eptorsion2.c src/ksp/ksp/tutorials/ex35.cxx src/ksp/ksp/tutorials/ex36.cxx src/tao/unconstrained/tutorials/eptorsion2f.F90 src/vec/vec/tutorials/ex8.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecSetValuesLocal(Vec x, PetscInt ni, const PetscInt ix[], const PetscScalar y[], InsertMode iora)
```

Example 2 (unknown):
```unknown
INSERT_VALUES
```

Example 3 (unknown):
```unknown
VecSetValuesLocal()
```

Example 4 (unknown):
```unknown
VecSetValuesLocal()
```

---

## VecSetValuesSection#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetValuesSection/

**Contents:**
- VecSetValuesSection#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets all the values associated with a given point, according to the section, in the given Vec

s - the organizing PetscSection

values - the array of input values

mode - the insertion mode, either ADD_VALUES or INSERT_VALUES

PetscSection, PetscSectionCreate(), VecGetValuesSection()

src/vec/vec/utils/vsection.c

src/snes/tutorials/ex7.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
#include "petscvec.h"   
PetscErrorCode VecSetValuesSection(Vec v, PetscSection s, PetscInt point, const PetscScalar values[], InsertMode mode)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
INSERT_VALUES
```

Example 4 (unknown):
```unknown
PetscSection
```

---

## VecSetValues#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetValues/

**Contents:**
- VecSetValues#
- Synopsis#
- Input Parameters#
- Notes#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Inserts or adds values into certain locations of a vector.

x - vector to insert in

ni - number of elements to add

ix - indices where to add

y - array of values. Pass NULL to set all zeroes.

iora - either INSERT_VALUES to replace the current values or ADD_VALUES to add values to any existing entries

Calls to VecSetValues() with the INSERT_VALUES and ADD_VALUES options cannot be mixed without intervening calls to the assembly routines.

These values may be cached, so VecAssemblyBegin() and VecAssemblyEnd() MUST be called after all calls to VecSetValues() have been completed.

VecSetValues() uses 0-based indices in Fortran as well as in C.

If you call VecSetOption(x, VEC_IGNORE_NEGATIVE_INDICES,PETSC_TRUE), negative indices may be passed in ix. These rows are simply ignored. This allows easily inserting element load matrices with homogeneous Dirichlet boundary conditions that you don’t want represented in the vector.

If any of ix and y are scalars pass them using, for example,

Vectors and Parallel Data, Vec, VecAssemblyBegin(), VecAssemblyEnd(), VecSetValuesLocal(), VecSetValue(), VecSetValuesBlocked(), InsertMode, INSERT_VALUES, ADD_VALUES, VecGetValues(), VecOption, VecSetOption()

src/vec/vec/interface/rvector.c

src/snes/tutorials/ex59.c src/snes/tutorials/ex6.c src/snes/tutorials/ex73f90t.F90 src/ksp/ksp/tutorials/ex72.c src/snes/tutorials/ex2.c src/ksp/ksp/tutorials/ex49.c src/ksp/pc/tutorials/ex2.c src/ksp/ksp/tutorials/ex28.c src/ksp/pc/tutorials/ex1.c

VecSetValues_MPI() in src/vec/vec/impls/mpi/pdvec.c VecSetValues_Seq() in src/vec/vec/impls/seq/bvec2.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecSetValues(Vec x, PetscInt ni, const PetscInt ix[], const PetscScalar y[], InsertMode iora)
```

Example 2 (unknown):
```unknown
INSERT_VALUES
```

Example 3 (lua):
```lua
`VecSetValues()` sets x[ix[i]] = y[i], for i=0,...,ni-1.
```

Example 4 (unknown):
```unknown
VecSetValues()
```

---

## VecSetValue#

**URL:** https://petsc.org/release/manualpages/Vec/VecSetValue/

**Contents:**
- VecSetValue#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Set a single entry into a PETSc vector, Vec.

row - the row location of the entry

value - the value to insert

mode - either INSERT_VALUES or ADD_VALUES

For efficiency one should use VecSetValues() and set several or many values simultaneously if possible.

These values may be cached, so VecAssemblyBegin() and VecAssemblyEnd() MUST be called after all calls to VecSetValue() have been completed.

VecSetValue() uses 0-based indices in Python, C, and Fortran

Vectors and Parallel Data, VecSetValues(), VecAssemblyBegin(), VecAssemblyEnd(), VecSetValuesBlockedLocal(), VecSetValueLocal()

src/snes/tutorials/ex28.c src/mat/tutorials/ex3.c src/ksp/ksp/tutorials/ex56.c src/tao/constrained/tutorials/ex1.c src/vec/vec/tutorials/ex1.c src/snes/tutorials/ex70.c src/snes/tutorials/ex30.c src/snes/tutorials/ex56.c src/ksp/ksp/tutorials/ex49.c src/ksp/ksp/tutorials/ex43.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
static inline PetscErrorCode VecSetValue(Vec v, PetscInt i, PetscScalar va, InsertMode mode)
```

Example 2 (unknown):
```unknown
INSERT_VALUES
```

Example 3 (unknown):
```unknown
VecSetValues()
```

Example 4 (unknown):
```unknown
VecAssemblyBegin()
```

---

## VecSet#

**URL:** https://petsc.org/release/manualpages/Vec/VecSet/

**Contents:**
- VecSet#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets all components of a vector to a single scalar value.

For a vector of dimension n, VecSet() sets x[i] = alpha, for i=1,…,n, so that all vector entries then equal the identical scalar value, alpha. Use the more general routine VecSetValues() to set different vector entries.

You CANNOT call this after you have called VecSetValues() but before you call VecAssemblyBegin()

If alpha is zero and the norm of the vector is known to be zero then this skips the unneeded zeroing process

Vectors and Parallel Data, Vec, VecSetValues(), VecSetValuesBlocked(), VecSetRandom()

src/vec/vec/interface/rvector.c

src/snes/tutorials/ex99.c src/mat/tutorials/ex3.c src/snes/tutorials/ex1.c src/mat/tutorials/ex9.c src/snes/tutorials/ex9.c src/snes/tutorials/ex40f90.F90 src/snes/tutorials/ex35.c src/snes/tutorials/ex12.c src/snes/tutorials/ex17.c src/snes/tutorials/ex23.c

VecSet_Nest() in src/vec/vec/impls/nest/vecnest.c VecSet_Seq() in src/vec/vec/impls/seq/dvec2.c VecSet_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecSet_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecSet(Vec x, PetscScalar alpha)
```

Example 2 (unknown):
```unknown
VecSetValues()
```

Example 3 (unknown):
```unknown
VecSetValues()
```

Example 4 (unknown):
```unknown
VecAssemblyBegin()
```

---

## VecShift#

**URL:** https://petsc.org/release/manualpages/Vec/VecShift/

**Contents:**
- VecShift#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Shifts all of the components of a vector by computing x[i] = x[i] + shift.

src/vec/vec/utils/vinv.c

src/tao/bound/tutorials/plate2f.F90 src/ksp/ksp/tutorials/ex59.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/tao/pde_constrained/tutorials/elliptic.c src/tao/constrained/tutorials/tomographyADMM.c src/tao/pde_constrained/tutorials/parabolic.c src/tao/bound/tutorials/plate2.c src/tao/unconstrained/tutorials/minsurf2.c src/tao/pde_constrained/tutorials/hyperbolic.c src/tao/unconstrained/tutorials/elastic_net_regularization.c

VecShift_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
x[i] = x[i] + shift
```

Example 2 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecShift(Vec v, PetscScalar shift)
```

Example 3 (unknown):
```unknown
VecISShift()
```

---

## VecSignMode#

**URL:** https://petsc.org/release/manualpages/Vec/VecSignMode/

**Contents:**
- VecSignMode#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

How VecPointwiseSign() should handle zero value

VEC_SIGN_ZERO_TO_ZERO - -0.0 and 0.0 map to 0.0

VEC_SIGN_ZERO_TO_SIGNED_ZERO - -0.0 maps to -0.0 and 0.0 maps to 0.0

VEC_SIGN_ZERO_TO_SIGNED_UNIT - -0.0 maps to -1.0 and 0.0 maps to 1.0

Vectors and Parallel Data, VecPointwiseSign()

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecPointwiseSign()
```

Example 2 (unknown):
```unknown
typedef enum {
  VEC_SIGN_ZERO_TO_ZERO,
  VEC_SIGN_ZERO_TO_SIGNED_ZERO,
  VEC_SIGN_ZERO_TO_SIGNED_UNIT,
} VecSignMode;
```

Example 3 (unknown):
```unknown
VEC_SIGN_ZERO_TO_ZERO
```

Example 4 (unknown):
```unknown
VEC_SIGN_ZERO_TO_SIGNED_ZERO
```

---

## VecSqrtAbs#

**URL:** https://petsc.org/release/manualpages/Vec/VecSqrtAbs/

**Contents:**
- VecSqrtAbs#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Replaces each component of a vector by the square root of its magnitude.

The actual function is sqrt(|x_i|)

Vec, VecLog(), VecExp(), VecReciprocal(), VecAbs()

src/vec/vec/utils/vinv.c

src/tao/constrained/tutorials/tomographyADMM.c src/ksp/pc/tutorials/ex4.c src/tao/tutorials/ex4.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecSqrtAbs(Vec v)
```

Example 2 (unknown):
```unknown
VecReciprocal()
```

---

## VECSTANDARD#

**URL:** https://petsc.org/release/manualpages/Vec/VECSTANDARD/

**Contents:**
- VECSTANDARD#
- Options Database Key#
- See Also#
- Level#
- Location#

“standard” - A VECSEQ on one process and VECMPI on more than one process

-vec_type standard - sets a vector type to standard on calls to VecSetFromOptions()

Vectors and Parallel Data, Vec, VecType, VecCreateSeq(), VecCreateMPI()

src/vec/vec/impls/mpi/pbvec.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecSetFromOptions()
```

Example 2 (unknown):
```unknown
VecCreateSeq()
```

Example 3 (unknown):
```unknown
VecCreateMPI()
```

---

## VecStashGetInfo#

**URL:** https://petsc.org/release/manualpages/Vec/VecStashGetInfo/

**Contents:**
- VecStashGetInfo#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Gets how many values are currently in the vector stash, i.e. need to be communicated to other processors during the VecAssemblyBegin()/VecAssemblyEnd() process

nstash - the size of the stash

reallocs - the number of additional mallocs incurred in building the stash

bnstash - the size of the block stash

breallocs - the number of additional mallocs incurred in building the block stash (from VecSetValuesBlocked())

Vectors and Parallel Data, Vec, VecAssemblyBegin(), VecAssemblyEnd(), VecStashSetInitialSize(), VecStashView()

src/vec/vec/interface/vector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecAssemblyBegin()
```

Example 2 (unknown):
```unknown
VecAssemblyEnd()
```

Example 3 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecStashGetInfo(Vec vec, PetscInt *nstash, PetscInt *reallocs, PetscInt *bnstash, PetscInt *breallocs)
```

Example 4 (unknown):
```unknown
VecSetValuesBlocked()
```

---

## VecStashSetInitialSize#

**URL:** https://petsc.org/release/manualpages/Vec/VecStashSetInitialSize/

**Contents:**
- VecStashSetInitialSize#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#

sets the sizes of the vec-stash, that is used during the assembly process to store values that belong to other processors.

Not Collective, different processes can have different size stashes

size - the initial size of the stash.

bsize - the initial size of the block-stash(if used).

-vecstash_initial_size size or size0,size1,…,sizep- 1 - set initial size

-vecstash_block_initial_size bsize or bsize0,bsize1,…,bsizep- 1 - set initial block size

The block-stash is used for values set with VecSetValuesBlocked() while the stash is used for values set with VecSetValues()

Run with the option -info and look for output of the form VecAssemblyBegin_MPIXXX:Stash has MM entries, uses nn mallocs. to determine the appropriate value, MM, to use for size and VecAssemblyBegin_MPIXXX:Block-Stash has BMM entries, uses nn mallocs. to determine the value, BMM to use for bsize

PETSc attempts to smartly manage the stash size so there is little likelihood setting a a specific value here will affect performance

Vectors and Parallel Data, Vec, VecSetBlockSize(), VecSetValues(), VecSetValuesBlocked(), VecStashView()

src/vec/vec/interface/vector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecStashSetInitialSize(Vec vec, PetscInt size, PetscInt bsize)
```

Example 2 (unknown):
```unknown
VecSetValuesBlocked()
```

Example 3 (unknown):
```unknown
VecSetValues()
```

Example 4 (unknown):
```unknown
VecSetBlockSize()
```

---

## VecStashViewFromOptions#

**URL:** https://petsc.org/release/manualpages/Vec/VecStashViewFromOptions/

**Contents:**
- VecStashViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Developer Notes#
- See Also#
- Level#
- Location#

Processes command line options to determine if/how a VecStash object is to be viewed.

obj - the Vec containing a stash

bobj - optional other object that provides the prefix

name - option to activate viewing

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

This cannot use PetscObjectViewFromOptions() because it takes a Vec as an argument but does not use VecView()

Vectors and Parallel Data, Vec, VecStashSetInitialSize()

src/vec/vec/interface/vector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecStashViewFromOptions(Vec obj, PetscObject bobj, const char name[])
```

Example 2 (unknown):
```unknown
PetscObjectViewFromOptions()
```

Example 3 (unknown):
```unknown
PetscObjectViewFromOptions()
```

Example 4 (unknown):
```unknown
VecStashSetInitialSize()
```

---

## VecStashView#

**URL:** https://petsc.org/release/manualpages/Vec/VecStashView/

**Contents:**
- VecStashView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Prints the entries in the vector stash and block stash.

Vectors and Parallel Data, Vec, VecSetBlockSize(), VecSetValues(), VecSetValuesBlocked()

src/vec/vec/interface/vector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecStashView(Vec v, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
VecSetBlockSize()
```

Example 3 (unknown):
```unknown
VecSetValues()
```

Example 4 (unknown):
```unknown
VecSetValuesBlocked()
```

---

## VecStepBoundInfo#

**URL:** https://petsc.org/release/manualpages/Vec/VecStepBoundInfo/

**Contents:**
- VecStepBoundInfo#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

X - vector with no negative entries

DX - step direction, can have negative, positive or zero entries

boundmin - (may be NULL this it is not computed) maximum value so that XL[i] <= X[i] + boundmax*DX[i] <= XU[i]

wolfemin - (may be NULL this it is not computed)

boundmax - (may be NULL this it is not computed) minimum value so that X[i] + boundmaxDX[i] <= XL[i] or XU[i] <= X[i] + boundmaxDX[i]

For complex numbers only compares the real part

src/vec/vec/utils/projection.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"  
PetscErrorCode VecStepBoundInfo(Vec X, Vec DX, Vec XL, Vec XU, PetscReal *boundmin, PetscReal *wolfemin, PetscReal *boundmax)
```

---

## VecStepMaxBounded#

**URL:** https://petsc.org/release/manualpages/Vec/VecStepMaxBounded/

**Contents:**
- VecStepMaxBounded#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

X - vector with no negative entries

DX - step direction, can have negative, positive or zero entries

stepmax - minimum value so that X[i] + stepmaxDX[i] <= XL[i] or XU[i] <= X[i] + stepmaxDX[i]

src/vec/vec/utils/projection.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"  
PetscErrorCode VecStepMaxBounded(Vec X, Vec DX, Vec XL, Vec XU, PetscReal *stepmax)
```

---

## VecStepMax#

**URL:** https://petsc.org/release/manualpages/Vec/VecStepMax/

**Contents:**
- VecStepMax#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Returns the largest value so that x[i] + step*DX[i] >= 0 for all i

X - vector with no negative entries

DX - a step direction, can have negative, positive or zero entries

step - largest value such that x[i] + step*DX[i] >= 0 for all i

For complex numbers only compares the real part

src/vec/vec/utils/projection.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"  
PetscErrorCode VecStepMax(Vec X, Vec DX, PetscReal *step)
```

---

## VecStrideGatherAll#

**URL:** https://petsc.org/release/manualpages/Vec/VecStrideGatherAll/

**Contents:**
- VecStrideGatherAll#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Gathers all the single components from a multi-component vector into separate vectors.

addv - one of ADD_VALUES, INSERT_VALUES, MAX_VALUES

s - the location where the subvectors are stored

One must call VecSetBlockSize() before this routine to set the stride information, or use a vector created from a multicomponent DMDA.

If x is the array representing the vector x then this gathers the arrays (x[start],x[start+stride],x[start+2*stride], ….) for start=0,1,2,…bs-1

The parallel layout of the vector and the subvector must be the same; i.e., nlocal of v = stride*(nlocal of s)

Not optimized; could be easily

Vec, VecStrideNorm(), VecStrideScatter(), VecStrideMin(), VecStrideMax(), VecStrideGather(), VecStrideScatterAll()

src/vec/vec/utils/vinv.c

src/snes/tutorials/ex7.c src/vec/vec/tutorials/ex16f.F90 src/vec/vec/tutorials/ex16.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecStrideGatherAll(Vec v, Vec s[], InsertMode addv)
```

Example 2 (unknown):
```unknown
INSERT_VALUES
```

Example 3 (unknown):
```unknown
VecSetBlockSize()
```

Example 4 (unknown):
```unknown
VecStrideNorm()
```

---

## VecStrideGather#

**URL:** https://petsc.org/release/manualpages/Vec/VecStrideGather/

**Contents:**
- VecStrideGather#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Gathers a single component from a multi-component vector into another vector.

start - starting point of the subvector (defined by a stride)

addv - one of ADD_VALUES, INSERT_VALUES, MAX_VALUES

s - the location where the subvector is stored

One must call VecSetBlockSize() before this routine to set the stride information, or use a vector created from a multicomponent DMDA.

If x is the array representing the vector x then this gathers the array (x[start],x[start+stride],x[start+2*stride], ….)

The parallel layout of the vector and the subvector must be the same; i.e., nlocal of v = stride*(nlocal of s)

Not optimized; could be easily

Vec, VecStrideNorm(), VecStrideScatter(), VecStrideMin(), VecStrideMax(), VecStrideGatherAll(), VecStrideScatterAll()

src/vec/vec/utils/vinv.c

src/ts/tutorials/ex30.c src/vec/vec/tutorials/ex12.c src/vec/vec/tutorials/ex12f.F90 src/ml/da/tutorials/ex2.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecStrideGather(Vec v, PetscInt start, Vec s, InsertMode addv)
```

Example 2 (unknown):
```unknown
INSERT_VALUES
```

Example 3 (unknown):
```unknown
VecSetBlockSize()
```

Example 4 (unknown):
```unknown
VecStrideNorm()
```

---

## VecStrideMaxAll#

**URL:** https://petsc.org/release/manualpages/Vec/VecStrideMaxAll/

**Contents:**
- VecStrideMaxAll#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Computes the maximums of subvectors of a vector defined by a starting point and a stride and optionally its location.

idex - the location where the maximum occurred (not supported, pass NULL, if you need this, send mail to petsc-maint@mcs.anl.gov to request it)

nrm - the maximum values of each subvector

One must call VecSetBlockSize() before this routine to set the stride information, or use a vector created from a multicomponent DMDA.

The dimension of nrm must be the same as the vector block size

Vec, VecMax(), VecStrideNorm(), VecStrideGather(), VecStrideScatter(), VecStrideMin()

src/vec/vec/utils/vinv.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecStrideMaxAll(Vec v, PetscInt idex[], PetscReal nrm[])
```

Example 2 (unknown):
```unknown
VecSetBlockSize()
```

Example 3 (unknown):
```unknown
VecStrideNorm()
```

Example 4 (unknown):
```unknown
VecStrideGather()
```

---

## VecStrideMax#

**URL:** https://petsc.org/release/manualpages/Vec/VecStrideMax/

**Contents:**
- VecStrideMax#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Computes the maximum of subvector of a vector defined by a starting point and a stride and optionally its location.

start - starting point of the subvector (defined by a stride)

idex - the location where the maximum occurred (pass NULL if not required)

nrm - the maximum value in the subvector

One must call VecSetBlockSize() before this routine to set the stride information, or use a vector created from a multicomponent DMDA.

If xa is the array representing the vector x, then this computes the max of the array (xa[start],xa[start+stride],xa[start+2*stride], ….)

This is useful for computing, say the maximum of the pressure variable when the pressure is stored (interlaced) with other variables, e.g., density, etc. This will only work if the desire subvector is a stride subvector.

Vec, VecMax(), VecStrideNorm(), VecStrideGather(), VecStrideScatter(), VecStrideMin()

src/vec/vec/utils/vinv.c

src/ksp/ksp/tutorials/ex70.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecStrideMax(Vec v, PetscInt start, PetscInt *idex, PetscReal *nrm)
```

Example 2 (unknown):
```unknown
VecSetBlockSize()
```

Example 3 (unknown):
```unknown
VecStrideNorm()
```

Example 4 (unknown):
```unknown
VecStrideGather()
```

---

## VecStrideMinAll#

**URL:** https://petsc.org/release/manualpages/Vec/VecStrideMinAll/

**Contents:**
- VecStrideMinAll#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Computes the minimum of subvector of a vector defined by a starting point and a stride and optionally its location.

idex - the location where the minimum occurred (not supported, pass NULL, if you need this, send mail to petsc-maint@mcs.anl.gov to request it)

nrm - the minimums of each subvector

One must call VecSetBlockSize() before this routine to set the stride information, or use a vector created from a multicomponent DMDA.

The dimension of nrm must be the same as the vector block size

Vec, VecMin(), VecStrideNorm(), VecStrideGather(), VecStrideScatter(), VecStrideMax()

src/vec/vec/utils/vinv.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecStrideMinAll(Vec v, PetscInt idex[], PetscReal nrm[])
```

Example 2 (unknown):
```unknown
VecSetBlockSize()
```

Example 3 (unknown):
```unknown
VecStrideNorm()
```

Example 4 (unknown):
```unknown
VecStrideGather()
```

---

## VecStrideMin#

**URL:** https://petsc.org/release/manualpages/Vec/VecStrideMin/

**Contents:**
- VecStrideMin#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Computes the minimum of subvector of a vector defined by a starting point and a stride and optionally its location.

start - starting point of the subvector (defined by a stride)

idex - the location where the minimum occurred. (pass NULL if not required)

nrm - the minimum value in the subvector

One must call VecSetBlockSize() before this routine to set the stride information, or use a vector created from a multicomponent DMDA.

If xa is the array representing the vector x, then this computes the min of the array (xa[start],xa[start+stride],xa[start+2*stride], ….)

This is useful for computing, say the minimum of the pressure variable when the pressure is stored (interlaced) with other variables, e.g., density, etc. This will only work if the desire subvector is a stride subvector.

Vec, VecMin(), VecStrideNorm(), VecStrideGather(), VecStrideScatter(), VecStrideMax()

src/vec/vec/utils/vinv.c

src/ksp/ksp/tutorials/ex70.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecStrideMin(Vec v, PetscInt start, PetscInt *idex, PetscReal *nrm)
```

Example 2 (unknown):
```unknown
VecSetBlockSize()
```

Example 3 (unknown):
```unknown
VecStrideNorm()
```

Example 4 (unknown):
```unknown
VecStrideGather()
```

---

## VecStrideNormAll#

**URL:** https://petsc.org/release/manualpages/Vec/VecStrideNormAll/

**Contents:**
- VecStrideNormAll#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Computes the norms of subvectors of a vector defined by a starting point and a stride.

ntype - type of norm, one of NORM_1, NORM_2, NORM_INFINITY

One must call VecSetBlockSize() before this routine to set the stride information, or use a vector created from a multicomponent DMDA.

If x is the array representing the vector x then this computes the norm of the array (x[start],x[start+stride],x[start+2*stride], ….) for each start < stride

The dimension of nrm must be the same as the vector block size

This will only work if the desire subvector is a stride subvector

Vec, VecNorm(), VecStrideGather(), VecStrideScatter(), VecStrideMin(), VecStrideMax()

src/vec/vec/utils/vinv.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecStrideNormAll(Vec v, NormType ntype, PetscReal nrm[])
```

Example 2 (unknown):
```unknown
NORM_INFINITY
```

Example 3 (unknown):
```unknown
VecSetBlockSize()
```

Example 4 (unknown):
```unknown
VecStrideGather()
```

---

## VecStrideNorm#

**URL:** https://petsc.org/release/manualpages/Vec/VecStrideNorm/

**Contents:**
- VecStrideNorm#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Computes the norm of subvector of a vector defined by a starting point and a stride.

start - starting point of the subvector (defined by a stride)

ntype - type of norm, one of NORM_1, NORM_2, NORM_INFINITY

One must call VecSetBlockSize() before this routine to set the stride information, or use a vector created from a multicomponent DMDA.

If x is the array representing the vector x then this computes the norm of the array (x[start],x[start+stride],x[start+2*stride], ….)

This is useful for computing, say the norm of the pressure variable when the pressure is stored (interlaced) with other variables, say density etc.

This will only work if the desire subvector is a stride subvector

Vec, VecNorm(), VecStrideGather(), VecStrideScatter(), VecStrideMin(), VecStrideMax()

src/vec/vec/utils/vinv.c

src/vec/vec/tutorials/ex11f90.F90 src/ksp/ksp/tutorials/ex42.c src/ksp/ksp/tutorials/ex43.c src/snes/tutorials/ex22.c src/vec/vec/tutorials/ex11.c src/vec/vec/tutorials/ex11f.F90

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecStrideNorm(Vec v, PetscInt start, NormType ntype, PetscReal *nrm)
```

Example 2 (unknown):
```unknown
NORM_INFINITY
```

Example 3 (unknown):
```unknown
VecSetBlockSize()
```

Example 4 (unknown):
```unknown
VecStrideGather()
```

---

## VecStrideScaleAll#

**URL:** https://petsc.org/release/manualpages/Vec/VecStrideScaleAll/

**Contents:**
- VecStrideScaleAll#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Scales the subvectors of a vector defined by a starting point and a stride.

scales - values to multiply each subvector entry by

One must call VecSetBlockSize() before this routine to set the stride information, or use a vector created from a multicomponent DMDA.

The dimension of scales must be the same as the vector block size

Vec, VecNorm(), VecStrideScale(), VecScale(), VecStrideGather(), VecStrideScatter(), VecStrideMin(), VecStrideMax()

src/vec/vec/utils/vinv.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecStrideScaleAll(Vec v, const PetscScalar *scales)
```

Example 2 (unknown):
```unknown
VecSetBlockSize()
```

Example 3 (unknown):
```unknown
VecStrideScale()
```

Example 4 (unknown):
```unknown
VecStrideGather()
```

---

## VecStrideScale#

**URL:** https://petsc.org/release/manualpages/Vec/VecStrideScale/

**Contents:**
- VecStrideScale#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Scales a subvector of a vector defined by a starting point and a stride.

start - starting point of the subvector (defined by a stride)

scale - value to multiply each subvector entry by

One must call VecSetBlockSize() before this routine to set the stride information, or use a vector created from a multicomponent DMDA.

This will only work if the desire subvector is a stride subvector

Vec, VecNorm(), VecStrideGather(), VecStrideScatter(), VecStrideMin(), VecStrideMax()

src/vec/vec/utils/vinv.c

src/vec/vec/tutorials/ex13.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecStrideScale(Vec v, PetscInt start, PetscScalar scale)
```

Example 2 (unknown):
```unknown
VecSetBlockSize()
```

Example 3 (unknown):
```unknown
VecStrideGather()
```

Example 4 (unknown):
```unknown
VecStrideScatter()
```

---

## VecStrideScatterAll#

**URL:** https://petsc.org/release/manualpages/Vec/VecStrideScatterAll/

**Contents:**
- VecStrideScatterAll#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Scatters all the single components from separate vectors into a multi-component vector.

s - the location where the subvectors are stored

addv - one of ADD_VALUES, INSERT_VALUES, MAX_VALUES

v - the multicomponent vector

One must call VecSetBlockSize() before this routine to set the stride information, or use a vector created from a multicomponent DMDA.

The parallel layout of the vector and the subvector must be the same; i.e., nlocal of v = stride*(nlocal of s)

Not optimized; could be easily

Vec, VecStrideNorm(), VecStrideScatter(), VecStrideMin(), VecStrideMax(), VecStrideGather()

src/vec/vec/utils/vinv.c

src/snes/tutorials/ex7.c src/vec/vec/tutorials/ex16f.F90 src/vec/vec/tutorials/ex16.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecStrideScatterAll(Vec s[], Vec v, InsertMode addv)
```

Example 2 (unknown):
```unknown
INSERT_VALUES
```

Example 3 (unknown):
```unknown
VecSetBlockSize()
```

Example 4 (unknown):
```unknown
VecStrideNorm()
```

---

## VecStrideScatter#

**URL:** https://petsc.org/release/manualpages/Vec/VecStrideScatter/

**Contents:**
- VecStrideScatter#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Scatters a single component from a vector into a multi-component vector.

s - the single-component vector

start - starting point of the subvector (defined by a stride)

addv - one of ADD_VALUES, INSERT_VALUES, MAX_VALUES

v - the location where the subvector is scattered (the multi-component vector)

One must call VecSetBlockSize() on the multi-component vector before this routine to set the stride information, or use a vector created from a multicomponent DMDA.

The parallel layout of the vector and the subvector must be the same; i.e., nlocal of v = stride*(nlocal of s)

Not optimized; could be easily

Vec, VecStrideNorm(), VecStrideGather(), VecStrideMin(), VecStrideMax(), VecStrideGatherAll(), VecStrideScatterAll(), VecStrideSubSetScatter(), VecStrideSubSetGather()

src/vec/vec/utils/vinv.c

src/vec/vec/tutorials/ex12.c src/vec/vec/tutorials/ex12f.F90

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecStrideScatter(Vec s, PetscInt start, Vec v, InsertMode addv)
```

Example 2 (unknown):
```unknown
INSERT_VALUES
```

Example 3 (unknown):
```unknown
VecSetBlockSize()
```

Example 4 (unknown):
```unknown
VecStrideNorm()
```

---

## VecStrideSet#

**URL:** https://petsc.org/release/manualpages/Vec/VecStrideSet/

**Contents:**
- VecStrideSet#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Sets a subvector of a vector defined by a starting point and a stride with a given value

start - starting point of the subvector (defined by a stride)

s - value to set for each entry in that subvector

One must call VecSetBlockSize() before this routine to set the stride information, or use a vector created from a multicomponent DMDA.

This will only work if the desire subvector is a stride subvector

Vec, VecNorm(), VecStrideGather(), VecStrideScatter(), VecStrideMin(), VecStrideMax(), VecStrideScale()

src/vec/vec/utils/vinv.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecStrideSet(Vec v, PetscInt start, PetscScalar s)
```

Example 2 (unknown):
```unknown
VecSetBlockSize()
```

Example 3 (unknown):
```unknown
VecStrideGather()
```

Example 4 (unknown):
```unknown
VecStrideScatter()
```

---

## VecStrideSubSetGather#

**URL:** https://petsc.org/release/manualpages/Vec/VecStrideSubSetGather/

**Contents:**
- VecStrideSubSetGather#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Gathers a subset of components from a multi-component vector into another vector.

nidx - the number of indices

idxv - the indices of the components 0 <= idxv[0] …idxv[nidx-1] < bs(v), they need not be sorted

idxs - the indices of the components 0 <= idxs[0] …idxs[nidx-1] < bs(s), they need not be sorted, may be null if nidx == bs(s) or is PETSC_DETERMINE

addv - one of ADD_VALUES, INSERT_VALUES, MAX_VALUES

s - the location where the subvector is stored

One must call VecSetBlockSize() on both vectors before this routine to set the stride information, or use a vector created from a multicomponent DMDA.

The parallel layout of the vector and the subvector must be the same;

Not optimized; could be easily

Vec, VecStrideNorm(), VecStrideScatter(), VecStrideGather(), VecStrideSubSetScatter(), VecStrideMin(), VecStrideMax(), VecStrideGatherAll(), VecStrideScatterAll()

src/vec/vec/utils/vinv.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecStrideSubSetGather(Vec v, PetscInt nidx, const PetscInt idxv[], const PetscInt idxs[], Vec s, InsertMode addv)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
INSERT_VALUES
```

Example 4 (unknown):
```unknown
VecSetBlockSize()
```

---

## VecStrideSubSetScatter#

**URL:** https://petsc.org/release/manualpages/Vec/VecStrideSubSetScatter/

**Contents:**
- VecStrideSubSetScatter#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Scatters components from a vector into a subset of components of a multi-component vector.

s - the smaller-component vector

nidx - the number of indices in idx

idxs - the indices of the components in the smaller-component vector, 0 <= idxs[0] …idxs[nidx-1] < bs(s) they need not be sorted, may be null if nidx == bs(s) or is PETSC_DETERMINE

idxv - the indices of the components in the larger-component vector, 0 <= idx[0] …idx[nidx-1] < bs(v) they need not be sorted

addv - one of ADD_VALUES, INSERT_VALUES, MAX_VALUES

v - the location where the subvector is into scattered (the multi-component vector)

One must call VecSetBlockSize() on the vectors before this routine to set the stride information, or use a vector created from a multicomponent DMDA.

The parallel layout of the vector and the subvector must be the same;

Not optimized; could be easily

Vec, VecStrideNorm(), VecStrideGather(), VecStrideSubSetGather(), VecStrideMin(), VecStrideMax(), VecStrideGatherAll(), VecStrideScatterAll()

src/vec/vec/utils/vinv.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecStrideSubSetScatter(Vec s, PetscInt nidx, const PetscInt idxs[], const PetscInt idxv[], Vec v, InsertMode addv)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
INSERT_VALUES
```

Example 4 (unknown):
```unknown
VecSetBlockSize()
```

---

## VecStrideSumAll#

**URL:** https://petsc.org/release/manualpages/Vec/VecStrideSumAll/

**Contents:**
- VecStrideSumAll#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Computes the sums of subvectors of a vector defined by a stride.

One must call VecSetBlockSize() before this routine to set the stride information, or use a vector created from a multicomponent DMDA.

If x is the array representing the vector x then this computes the sum of the array (x[start],x[start+stride],x[start+2*stride], ….) for each start < stride

Vec, VecSum(), VecStrideGather(), VecStrideScatter(), VecStrideMin(), VecStrideMax()

src/vec/vec/utils/vinv.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecStrideSumAll(Vec v, PetscScalar sums[])
```

Example 2 (unknown):
```unknown
VecSetBlockSize()
```

Example 3 (unknown):
```unknown
VecStrideGather()
```

Example 4 (unknown):
```unknown
VecStrideScatter()
```

---

## VecStrideSum#

**URL:** https://petsc.org/release/manualpages/Vec/VecStrideSum/

**Contents:**
- VecStrideSum#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Computes the sum of subvector of a vector defined by a starting point and a stride.

start - starting point of the subvector (defined by a stride)

One must call VecSetBlockSize() before this routine to set the stride information, or use a vector created from a multicomponent DMDA.

If x is the array representing the vector x then this computes the sum of the array (x[start],x[start+stride],x[start+2*stride], ….)

Vec, VecSum(), VecStrideGather(), VecStrideScatter(), VecStrideMin(), VecStrideMax()

src/vec/vec/utils/vinv.c

src/vec/vec/tutorials/ex13.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecStrideSum(Vec v, PetscInt start, PetscScalar *sum)
```

Example 2 (unknown):
```unknown
VecSetBlockSize()
```

Example 3 (unknown):
```unknown
VecStrideGather()
```

Example 4 (unknown):
```unknown
VecStrideScatter()
```

---

## VecSum#

**URL:** https://petsc.org/release/manualpages/Vec/VecSum/

**Contents:**
- VecSum#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Computes the sum of all the components of a vector.

Vec, VecMean(), VecNorm()

src/vec/vec/utils/vinv.c

src/ts/tutorials/ex9.c src/vec/vec/tutorials/ex18f.F90 src/ts/tutorials/extchem.c src/ksp/ksp/tutorials/ex59.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/tao/pde_constrained/tutorials/elliptic.c src/tao/constrained/tutorials/tomographyADMM.c src/tao/pde_constrained/tutorials/hyperbolic.c src/vec/vec/tutorials/ex13.c src/vec/vec/tutorials/ex18.c

VecSum_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecSum(Vec v, PetscScalar *sum)
```

---

## VecSwap#

**URL:** https://petsc.org/release/manualpages/Vec/VecSwap/

**Contents:**
- VecSwap#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Swaps the values between two vectors, x and y.

y - the second vector

Vectors and Parallel Data, Vec, VecSet()

src/vec/vec/interface/vector.c

src/vec/vec/tutorials/ex20f90.F90 src/vec/vec/tutorials/ex1.c src/vec/vec/tutorials/ex1f90.F90

VecSwap_Nest() in src/vec/vec/impls/nest/vecnest.c VecSwap_Seq() in src/vec/vec/impls/seq/bvec2.c VecSwap_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecSwap_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecSwap(Vec x, Vec y)
```

---

## Vecs#

**URL:** https://petsc.org/release/manualpages/Vec/Vecs/

**Contents:**
- Vecs#
- Synopsis#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Collection of Vecs where the storage for the vectors is held in a single contiguous block of memory

Temporary construct for handling multiple right-hand side solves.

This is faked by storing a single Vec whose array is sized to hold n vectors back to back.

Vec, VecsCreateSeq(), VecsCreateSeqWithArray(), VecsDuplicate(), VecsDestroy()

src/ksp/ksp/tutorials/bench_kspsolve.c src/dm/impls/stag/tutorials/ex4.c src/tao/tutorials/ex3.c src/dm/impls/stag/tutorials/ex6.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _n_Vecs     *Vecs;
```

Example 2 (unknown):
```unknown
VecsCreateSeq()
```

Example 3 (unknown):
```unknown
VecsCreateSeqWithArray()
```

Example 4 (unknown):
```unknown
VecsDuplicate()
```

---

## VecTaggerAbsoluteGetBox#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerAbsoluteGetBox/

**Contents:**
- VecTaggerAbsoluteGetBox#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the box defining the values to be tagged by the tagger.

tagger - the VecTagger context

box - the box: a blocksize array of VecTaggerBox boxes

VecTagger, VecTaggerBox, VecTaggerAbsoluteSetBox()

src/vec/vec/utils/tagger/impls/absolute.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerAbsoluteGetBox(VecTagger tagger, const VecTaggerBox *box[])
```

Example 2 (unknown):
```unknown
VecTaggerBox
```

Example 3 (unknown):
```unknown
VecTaggerBox
```

Example 4 (unknown):
```unknown
VecTaggerAbsoluteSetBox()
```

---

## VecTaggerAbsoluteSetBox#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerAbsoluteSetBox/

**Contents:**
- VecTaggerAbsoluteSetBox#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the box defining the values to be tagged by the tagger.

tagger - the VecTagger context

box - the box: a blocksize array of VecTaggerBox boxes

VecTagger, VecTaggerBox, VecTaggerAbsoluteGetBox()

src/vec/vec/utils/tagger/impls/absolute.c

src/ts/tutorials/ex30.c src/ts/tutorials/ex11.c src/vec/vec/utils/tagger/tutorials/ex1.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerAbsoluteSetBox(VecTagger tagger, VecTaggerBox box[])
```

Example 2 (unknown):
```unknown
VecTaggerBox
```

Example 3 (unknown):
```unknown
VecTaggerBox
```

Example 4 (unknown):
```unknown
VecTaggerAbsoluteGetBox()
```

---

## VecTaggerAndGetSubs#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerAndGetSubs/

**Contents:**
- VecTaggerAndGetSubs#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Get the sub VecTaggers whose intersection defines the outer VecTagger

tagger - the VecTagger context

nsubs - the number of sub VecTaggers

subs - the sub VecTaggers

VecTagger, VecTaggerAndSetSubs()

src/vec/vec/utils/tagger/impls/and.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerAndGetSubs(VecTagger tagger, PetscInt *nsubs, VecTagger *subs[])
```

Example 2 (unknown):
```unknown
VecTaggerAndSetSubs()
```

---

## VecTaggerAndSetSubs#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerAndSetSubs/

**Contents:**
- VecTaggerAndSetSubs#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the sub VecTaggers whose intersection defines the outer VecTagger

tagger - the VecTagger context

nsubs - the number of sub VecTaggers

subs - the sub VecTaggers

mode - the copy mode to use for subs

src/vec/vec/utils/tagger/impls/and.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerAndSetSubs(VecTagger tagger, PetscInt nsubs, VecTagger subs[], PetscCopyMode mode)
```

---

## VecTaggerBox#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerBox/

**Contents:**
- VecTaggerBox#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#

A interval (box for complex numbers) range used to tag values. For real scalars, this is just a closed interval; for complex scalars, the box is the closed region in the complex plane such that real(min) <= real(z) <= real(max) and imag(min) <= imag(z) <= imag(max). INF is an acceptable endpoint.

Vectors and Parallel Data, Vec, VecTagger, VecTaggerType, VecTaggerCreate(), VecTaggerComputeIntervals()

src/ts/tutorials/ex30.c src/ts/tutorials/ex11.c src/vec/vec/utils/tagger/tutorials/ex1.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef struct {
  PetscScalar min;
  PetscScalar max;
} VecTaggerBox;
```

Example 2 (unknown):
```unknown
VecTaggerType
```

Example 3 (unknown):
```unknown
VecTaggerCreate()
```

Example 4 (unknown):
```unknown
VecTaggerComputeIntervals()
```

---

## VecTaggerCDFGetBox#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerCDFGetBox/

**Contents:**
- VecTaggerCDFGetBox#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the cumulative box (multi-dimensional box) defining the values to be tagged by the tagger, where cumulative boxes are subsets of [0,1], where 0 indicates the smallest value present in the vector and 1 indicates the largest.

tagger - the VecTagger context

box - a blocksize array of VecTaggerBox boxes

VecTagger, VecTaggerCDFSetBox(), VecTaggerBox

src/vec/vec/utils/tagger/impls/cdf.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerCDFGetBox(VecTagger tagger, const VecTaggerBox *box[])
```

Example 2 (unknown):
```unknown
VecTaggerBox
```

Example 3 (unknown):
```unknown
VecTaggerCDFSetBox()
```

Example 4 (unknown):
```unknown
VecTaggerBox
```

---

## VecTaggerCDFGetMethod#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerCDFGetMethod/

**Contents:**
- VecTaggerCDFGetMethod#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the method used to compute absolute boxes from CDF boxes

tagger - the VecTagger context

Vec, VecTagger, VecTaggerCDFMethod

src/vec/vec/utils/tagger/impls/cdf.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerCDFGetMethod(VecTagger tagger, VecTaggerCDFMethod *method)
```

Example 2 (unknown):
```unknown
VecTaggerCDFMethod
```

---

## VecTaggerCDFIterativeGetTolerances#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerCDFIterativeGetTolerances/

**Contents:**
- VecTaggerCDFIterativeGetTolerances#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Get the tolerances for iterative computation of absolute boxes from CDF boxes.

tagger - the VecTagger context

maxit - the maximum number of iterations: 0 indicates the absolute values will be estimated from an initial guess based only on the minimum, maximum, mean, and standard deviation of the box endpoints.

rtol - the acceptable relative tolerance in the absolute values from the initial guess

atol - the acceptable absolute tolerance in the absolute values from the initial guess

VecTagger, VecTaggerCDFSetMethod()

src/vec/vec/utils/tagger/impls/cdf.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerCDFIterativeGetTolerances(VecTagger tagger, PetscInt *maxit, PetscReal *rtol, PetscReal *atol)
```

Example 2 (unknown):
```unknown
VecTaggerCDFSetMethod()
```

---

## VecTaggerCDFIterativeSetTolerances#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerCDFIterativeSetTolerances/

**Contents:**
- VecTaggerCDFIterativeSetTolerances#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the tolerances for iterative computation of absolute boxes from CDF boxes.

tagger - the VecTagger context

maxit - the maximum number of iterations: 0 indicates the absolute values will be estimated from an initial guess based only on the minimum, maximum, mean, and standard deviation of the box endpoints.

rtol - the acceptable relative tolerance in the absolute values from the initial guess

atol - the acceptable absolute tolerance in the absolute values from the initial guess

VecTagger, VecTaggerCDFSetMethod()

src/vec/vec/utils/tagger/impls/cdf.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerCDFIterativeSetTolerances(VecTagger tagger, PetscInt maxit, PetscReal rtol, PetscReal atol)
```

Example 2 (unknown):
```unknown
VecTaggerCDFSetMethod()
```

---

## VecTaggerCDFMethod#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerCDFMethod/

**Contents:**
- VecTaggerCDFMethod#
- Synopsis#
- Values#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

Determines what method is used to compute absolute values from cumulative distribution values (e.g., what value is the preimage of .95 in the cdf).

VECTAGGER_CDF_GATHER - gather the data to MPI rank 0, perform the computation and broadcast the result

VECTAGGER_CDF_ITERATIVE - compute the results on all ranks iteratively using MPI_Allreduce()

Relevant only in parallel: in serial it is directly computed.

In PETSc enums of this type are referred to with the term type, not method.

Vectors and Parallel Data, Vec, VecTagger, VecTaggerType, VecTaggerCreate(), VecTaggerCDFSetMethod()

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  VECTAGGER_CDF_GATHER,
  VECTAGGER_CDF_ITERATIVE,
  VECTAGGER_CDF_NUM_METHODS
} VecTaggerCDFMethod;
```

Example 2 (unknown):
```unknown
VECTAGGER_CDF_GATHER
```

Example 3 (unknown):
```unknown
VECTAGGER_CDF_ITERATIVE
```

Example 4 (unknown):
```unknown
MPI_Allreduce()
```

---

## VecTaggerCDFSetBox#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerCDFSetBox/

**Contents:**
- VecTaggerCDFSetBox#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the cumulative box defining the values to be tagged by the tagger, where cumulative boxes are subsets of [0,1], where 0 indicates the smallest value present in the vector and 1 indicates the largest.

tagger - the VecTagger context

box - a blocksize array of VecTaggerBox boxes

VecTagger, VecTaggerCDFGetBox(), VecTaggerBox

src/vec/vec/utils/tagger/impls/cdf.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerCDFSetBox(VecTagger tagger, VecTaggerBox box[])
```

Example 2 (unknown):
```unknown
VecTaggerBox
```

Example 3 (unknown):
```unknown
VecTaggerCDFGetBox()
```

Example 4 (unknown):
```unknown
VecTaggerBox
```

---

## VecTaggerCDFSetMethod#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerCDFSetMethod/

**Contents:**
- VecTaggerCDFSetMethod#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the method used to compute absolute boxes from CDF boxes

tagger - the VecTagger context

Vec, VecTagger, VecTaggerCDFMethod

src/vec/vec/utils/tagger/impls/cdf.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerCDFSetMethod(VecTagger tagger, VecTaggerCDFMethod method)
```

Example 2 (unknown):
```unknown
VecTaggerCDFMethod
```

---

## VecTaggerComputeBoxes#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerComputeBoxes/

**Contents:**
- VecTaggerComputeBoxes#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

If the tagged index set can be summarized as a list of boxes of values, returns that list, otherwise returns in listed PETSC_FALSE

tagger - the VecTagger context

numBoxes - the number of boxes in the tag definition

boxes - a newly allocated list of boxes. This is a flat array of (BlockSize * numBoxes) pairs that the user can free with PetscFree().

listed - PETSC_TRUE if a list was created, pass in NULL if not needed

A value is tagged if it is in any of the boxes, unless the tagger has been inverted (see VecTaggerSetInvert()/VecTaggerGetInvert()), in which case a value is tagged if it is in none of the boxes.

VecTaggerComputeIS(), VecTagger, VecTaggerCreate()

src/vec/vec/utils/tagger/interface/tagger.c

src/vec/vec/utils/tagger/tutorials/ex1.c

VecTaggerComputeBoxes_Absolute() in src/vec/vec/utils/tagger/impls/absolute.c VecTaggerComputeBoxes_And() in src/vec/vec/utils/tagger/impls/and.c VecTaggerComputeBoxes_CDF() in src/vec/vec/utils/tagger/impls/cdf.c VecTaggerComputeBoxes_Or() in src/vec/vec/utils/tagger/impls/or.c VecTaggerComputeBoxes_Relative() in src/vec/vec/utils/tagger/impls/relative.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_FALSE
```

Example 2 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerComputeBoxes(VecTagger tagger, Vec vec, PetscInt *numBoxes, VecTaggerBox *boxes[], PetscBool *listed)
```

Example 3 (unknown):
```unknown
PetscFree()
```

Example 4 (unknown):
```unknown
VecTaggerSetInvert()
```

---

## VecTaggerComputeIS#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerComputeIS/

**Contents:**
- VecTaggerComputeIS#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Use a VecTagger context to tag a set of indices based on a vector’s values

tagger - the VecTagger context

is - a list of the indices tagged by the tagger, i.e., if the number of local indices will be n / bs, where n is VecGetLocalSize() and bs is VecTaggerGetBlockSize().

listed - routine was able to compute the IS, pass in NULL if not needed

VecTaggerComputeBoxes(), VecTagger, VecTaggerCreate()

src/vec/vec/utils/tagger/interface/tagger.c

src/snes/tutorials/ex27.c src/ts/tutorials/ex11.c src/vec/vec/utils/tagger/tutorials/ex1.c src/ts/tutorials/ex30.c

VecTaggerComputeIS_And() in src/vec/vec/utils/tagger/impls/and.c VecTaggerComputeIS_Or() in src/vec/vec/utils/tagger/impls/or.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerComputeIS(VecTagger tagger, Vec vec, IS is[], PetscBool *listed)
```

Example 2 (unknown):
```unknown
VecGetLocalSize()
```

Example 3 (unknown):
```unknown
VecTaggerGetBlockSize()
```

Example 4 (unknown):
```unknown
VecTaggerComputeBoxes()
```

---

## VecTaggerCreate#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerCreate/

**Contents:**
- VecTaggerCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

create a VecTagger context.

comm - communicator on which the VecTagger will operate

tagger - new Vec tagger context

This object is used to control the tagging/selection of index sets based on the values in a vector. This is used, for example, in adaptive simulations when aspects are selected for refinement or coarsening. The primary intent is that the selected index sets are based purely on the values in the vector, though implementations that do not follow this intent are possible.

Once a VecTagger is created (VecTaggerCreate()), optionally modified by options (VecTaggerSetFromOptions()), and set up (VecTaggerSetUp()), it is applied to vectors with VecTaggerComputeIS() to compute the selected index sets.

Provided implementations support tagging based on a box/interval of values (VECTAGGERABSOLUTE), based on a box of values of relative to the range of values present in the vector (VECTAGGERRELATIVE), based on where values fall in the cumulative distribution of values in the vector (VECTAGGERCDF), and based on unions (VECTAGGEROR) or intersections (VECTAGGERAND) of other criteria.

VecTagger, VecTaggerSetBlockSize(), VecTaggerSetFromOptions(), VecTaggerSetUp(), VecTaggerComputeIS(), VecTaggerComputeBoxes(), VecTaggerDestroy()

src/vec/vec/utils/tagger/interface/tagger.c

src/snes/tutorials/ex27.c src/ts/tutorials/ex11.c src/vec/vec/utils/tagger/tutorials/ex1.c src/ts/tutorials/ex30.c

VecTaggerCreate_Absolute() in src/vec/vec/utils/tagger/impls/absolute.c VecTaggerCreate_And() in src/vec/vec/utils/tagger/impls/and.c VecTaggerCreate_AndOr() in src/vec/vec/utils/tagger/impls/andor.c VecTaggerCreate_CDF() in src/vec/vec/utils/tagger/impls/cdf.c VecTaggerCreate_Or() in src/vec/vec/utils/tagger/impls/or.c VecTaggerCreate_Relative() in src/vec/vec/utils/tagger/impls/relative.c VecTaggerCreate_Simple() in src/vec/vec/utils/tagger/impls/simple.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerCreate(MPI_Comm comm, VecTagger *tagger)
```

Example 2 (unknown):
```unknown
VecTaggerCreate()
```

Example 3 (unknown):
```unknown
VecTaggerSetFromOptions()
```

Example 4 (unknown):
```unknown
VecTaggerSetUp()
```

---

## VecTaggerDestroy#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerDestroy/

**Contents:**
- VecTaggerDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

destroy a VecTagger context

tagger - address of tagger

VecTaggerCreate(), VecTaggerSetType(), VecTagger

src/vec/vec/utils/tagger/interface/tagger.c

src/snes/tutorials/ex27.c src/ts/tutorials/ex11.c src/vec/vec/utils/tagger/tutorials/ex1.c src/ts/tutorials/ex30.c

VecTaggerDestroy_AndOr() in src/vec/vec/utils/tagger/impls/andor.c VecTaggerDestroy_Simple() in src/vec/vec/utils/tagger/impls/simple.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerDestroy(VecTagger *tagger)
```

Example 2 (unknown):
```unknown
VecTaggerCreate()
```

Example 3 (unknown):
```unknown
VecTaggerSetType()
```

---

## VecTaggerFinalizePackage#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerFinalizePackage/

**Contents:**
- VecTaggerFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

Finalize VecTagger package, it is called from PetscFinalize()

VecTaggerInitializePackage()

src/vec/vec/utils/tagger/interface/dlregistagger.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerFinalizePackage(void)
```

Example 2 (unknown):
```unknown
VecTaggerInitializePackage()
```

---

## VecTaggerGetBlockSize#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerGetBlockSize/

**Contents:**
- VecTaggerGetBlockSize#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

get the block size of the indices created by VecTaggerComputeIS().

blocksize - block size of the vectors the tagger operates on

VecTaggerComputeIS(), VecTaggerSetBlockSize(), VecTagger, VecTaggerCreate()

src/vec/vec/utils/tagger/interface/tagger.c

src/vec/vec/utils/tagger/tutorials/ex1.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecTaggerComputeIS()
```

Example 2 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerGetBlockSize(VecTagger tagger, PetscInt *blocksize)
```

Example 3 (unknown):
```unknown
VecTaggerComputeIS()
```

Example 4 (unknown):
```unknown
VecTaggerSetBlockSize()
```

---

## VecTaggerGetInvert#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerGetInvert/

**Contents:**
- VecTaggerGetInvert#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

get whether the set of indices returned by VecTaggerComputeIS() are inverted

invert - PETSC_TRUE to invert, PETSC_FALSE to use the indices as is

VecTaggerComputeIS(), VecTaggerSetInvert(), VecTagger, VecTaggerCreate()

src/vec/vec/utils/tagger/interface/tagger.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecTaggerComputeIS()
```

Example 2 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerGetInvert(VecTagger tagger, PetscBool *invert)
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (unknown):
```unknown
VecTaggerComputeIS()
```

---

## VecTaggerGetType#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerGetType/

**Contents:**
- VecTaggerGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the VecTaggerType name (as a string) from the VecTagger.

tagger - The VecTagger context

type - The VecTagger type name

VecTaggerSetType(), VecTaggerCreate(), VecTaggerSetFromOptions(), VecTagger, VecTaggerType

src/vec/vec/utils/tagger/interface/tagger.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecTaggerType
```

Example 2 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerGetType(VecTagger tagger, VecTaggerType *type)
```

Example 3 (unknown):
```unknown
VecTaggerSetType()
```

Example 4 (unknown):
```unknown
VecTaggerCreate()
```

---

## VecTaggerInitializePackage#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerInitializePackage/

**Contents:**
- VecTaggerInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

Initialize VecTagger package

VecTaggerFinalizePackage()

src/vec/vec/utils/tagger/interface/dlregistagger.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerInitializePackage(void)
```

Example 2 (unknown):
```unknown
VecTaggerFinalizePackage()
```

---

## VecTaggerOrGetSubs#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerOrGetSubs/

**Contents:**
- VecTaggerOrGetSubs#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Get the sub VecTaggers whose union defines the outer VecTagger

tagger - the VecTagger context

nsubs - the number of sub VecTaggers

subs - the sub VecTaggers

src/vec/vec/utils/tagger/impls/or.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerOrGetSubs(VecTagger tagger, PetscInt *nsubs, VecTagger *subs[])
```

Example 2 (unknown):
```unknown
VecTaggerOrSetSubs()
```

---

## VecTaggerOrSetSubs#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerOrSetSubs/

**Contents:**
- VecTaggerOrSetSubs#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the sub VecTaggers whose union defines the outer VecTagger

tagger - the VecTagger context

nsubs - the number of sub VecTaggers

subs - the sub VecTaggers

mode - the copy mode to use for subs

VecTaggetOrGetStubs()

src/vec/vec/utils/tagger/impls/or.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerOrSetSubs(VecTagger tagger, PetscInt nsubs, VecTagger subs[], PetscCopyMode mode)
```

Example 2 (unknown):
```unknown
VecTaggetOrGetStubs()
```

---

## VecTaggerRegisterAll#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerRegisterAll/

**Contents:**
- VecTaggerRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all the VecTagger communication implementations

VecTaggerRegisterDestroy()

src/vec/vec/utils/tagger/interface/taggerregi.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"  
PetscErrorCode VecTaggerRegisterAll(void)
```

Example 2 (unknown):
```unknown
VecTaggerRegisterDestroy()
```

---

## VecTaggerRegister#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerRegister/

**Contents:**
- VecTaggerRegister#
- Synopsis#
- Input Parameters#
- Notes#
- Example Usage#
- See Also#
- Level#
- Location#

Adds an implementation of the VecTagger communication protocol.

Not Collective, No Fortran Support

sname - name of a new user-defined implementation

function - routine to create method context

VecTaggerRegister() may be called multiple times to add several user-defined implementations.

Then, this implementation can be chosen with the procedural interface via

or at runtime via the option

VecTaggerType, VecTaggerCreate(), VecTagger, VecTaggerRegisterAll(), VecTaggerRegisterDestroy()

src/vec/vec/utils/tagger/interface/taggerregi.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"  
PetscErrorCode VecTaggerRegister(const char sname[], PetscErrorCode (*function)(VecTagger))
```

Example 2 (unknown):
```unknown
VecTaggerRegister()
```

Example 3 (unknown):
```unknown
VecTaggerRegister("my_impl", MyImplCreate);
```

Example 4 (unknown):
```unknown
VecTaggerSetType(tagger, "my_impl")
```

---

## VecTaggerRelativeGetBox#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerRelativeGetBox/

**Contents:**
- VecTaggerRelativeGetBox#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the relative box defining the values to be tagged by the tagger, where relative boxess are subsets of [0,1] (or [0,1]+[0,1]i for complex scalars), where 0 indicates the smallest value present in the vector and 1 indicates the largest.

tagger - the VecTagger context

box - a blocksize list of VecTaggerBox boxes

VecTaggerRelativeSetBox()

src/vec/vec/utils/tagger/impls/relative.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerRelativeGetBox(VecTagger tagger, const VecTaggerBox *box[])
```

Example 2 (unknown):
```unknown
VecTaggerRelativeSetBox()
```

---

## VecTaggerRelativeSetBox#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerRelativeSetBox/

**Contents:**
- VecTaggerRelativeSetBox#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the relative box defining the values to be tagged by the tagger, where relative boxes are subsets of [0,1] (or [0,1]+[0,1]i for complex scalars), where 0 indicates the smallest value present in the vector and 1 indicates the largest.

tagger - the VecTagger context

box - a blocksize list of VecTaggerBox boxes

VecTaggerRelativeGetBox()

src/vec/vec/utils/tagger/impls/relative.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerRelativeSetBox(VecTagger tagger, VecTaggerBox box[])
```

Example 2 (unknown):
```unknown
VecTaggerRelativeGetBox()
```

---

## VecTaggerSetBlockSize#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerSetBlockSize/

**Contents:**
- VecTaggerSetBlockSize#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

set the block size of the set of indices returned by VecTaggerComputeIS().

blocksize - block size of the criteria used to tagger vectors

Values greater than one are useful when there are multiple criteria for determining which indices to include in the set. For example, consider adaptive mesh refinement in a multiphysics problem, with metrics of solution quality for multiple fields measure on each cell. The size of the vector will be [numCells * numFields]; the VecTaggerblock size should benumFields; VecTaggerComputeIS()will return indices in the range[0, numCells)`, i.e., one index is given for each block of values.

Note that the block size of the vector does not have to match this block size.

VecTaggerComputeIS(), VecTaggerGetBlockSize(), VecSetBlockSize(), VecGetBlockSize(), VecTagger, VecTaggerCreate()

src/vec/vec/utils/tagger/interface/tagger.c

src/vec/vec/utils/tagger/tutorials/ex1.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecTaggerComputeIS()
```

Example 2 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerSetBlockSize(VecTagger tagger, PetscInt blocksize)
```

Example 3 (unknown):
```unknown
block size should be
```

Example 4 (unknown):
```unknown
will return indices in the range
```

---

## VecTaggerSetFromOptions#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerSetFromOptions/

**Contents:**
- VecTaggerSetFromOptions#
- Synopsis#
- Input Parameter#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

set VecTagger options using the options database

-vec_tagger_type - implementation type, see VecTaggerSetType()

-vec_tagger_block_size - set the block size, see VecTaggerSetBlockSize()

-vec_tagger_invert - invert the index set returned by VecTaggerComputeIS()

VecTagger, VecTaggerCreate(), VecTaggerSetUp()

src/vec/vec/utils/tagger/interface/tagger.c

src/snes/tutorials/ex27.c src/ts/tutorials/ex11.c src/vec/vec/utils/tagger/tutorials/ex1.c src/ts/tutorials/ex30.c

VecTaggerSetFromOptions_AndOr() in src/vec/vec/utils/tagger/impls/andor.c VecTaggerSetFromOptions_CDF() in src/vec/vec/utils/tagger/impls/cdf.c VecTaggerSetFromOptions_Simple() in src/vec/vec/utils/tagger/impls/simple.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerSetFromOptions(VecTagger tagger)
```

Example 2 (unknown):
```unknown
VecTaggerSetType()
```

Example 3 (unknown):
```unknown
VecTaggerSetBlockSize()
```

Example 4 (unknown):
```unknown
VecTaggerComputeIS()
```

---

## VecTaggerSetInvert#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerSetInvert/

**Contents:**
- VecTaggerSetInvert#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

If the tagged index sets are based on boxes that can be returned by VecTaggerComputeBoxes(), then this option inverts values used to compute the IS, i.e., from being in the union of the boxes to being in the intersection of their exteriors.

invert - PETSC_TRUE to invert, PETSC_FALSE to use the indices as is

VecTaggerComputeIS(), VecTaggerGetInvert(), VecTagger, VecTaggerCreate()

src/vec/vec/utils/tagger/interface/tagger.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecTaggerComputeBoxes()
```

Example 2 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerSetInvert(VecTagger tagger, PetscBool invert)
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (unknown):
```unknown
VecTaggerComputeIS()
```

---

## VecTaggerSetType#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerSetType/

**Contents:**
- VecTaggerSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

set the Vec tagger implementation

tagger - the VecTagger context

type - a known method

-vec_tagger_type type - Sets the method; see VecTaggerType

See “include/petscvec.h” for available methods (for instance)

VECTAGGERABSOLUTE - tag based on a box of values

VECTAGGERRELATIVE - tag based on a box relative to the range of values present in the vector

VECTAGGERCDF - tag based on a box in the cumulative distribution of values present in the vector

VECTAGGEROR - tag based on the union of a set of VecTagger contexts

VECTAGGERAND - tag based on the intersection of a set of other VecTagger contexts

VecTaggerType, VecTaggerCreate(), VecTagger

src/vec/vec/utils/tagger/interface/tagger.c

src/ts/tutorials/ex30.c src/ts/tutorials/ex11.c src/vec/vec/utils/tagger/tutorials/ex1.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerSetType(VecTagger tagger, VecTaggerType type)
```

Example 2 (unknown):
```unknown
VecTaggerType
```

Example 3 (unknown):
```unknown
VECTAGGERABSOLUTE
```

Example 4 (unknown):
```unknown
VECTAGGERRELATIVE
```

---

## VecTaggerSetUp#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerSetUp/

**Contents:**
- VecTaggerSetUp#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

set up a VecTagger context

tagger - Vec tagger object

VecTaggerSetFromOptions(), VecTaggerSetType(), VecTagger, VecTaggerCreate()

src/vec/vec/utils/tagger/interface/tagger.c

src/snes/tutorials/ex27.c src/ts/tutorials/ex11.c src/vec/vec/utils/tagger/tutorials/ex1.c src/ts/tutorials/ex30.c

VecTaggerSetUp_AndOr() in src/vec/vec/utils/tagger/impls/andor.c VecTaggerSetUp_Simple() in src/vec/vec/utils/tagger/impls/simple.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerSetUp(VecTagger tagger)
```

Example 2 (unknown):
```unknown
VecTaggerSetFromOptions()
```

Example 3 (unknown):
```unknown
VecTaggerSetType()
```

Example 4 (unknown):
```unknown
VecTaggerCreate()
```

---

## VecTaggerType#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerType/

**Contents:**
- VecTaggerType#
- Synopsis#
- See Also#
- Level#
- Location#

String with the name of a VecTagger type

Vectors and Parallel Data, Vec, VecTagger, VecTaggerCreate()

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef const char *VecTaggerType;
#define VECTAGGERABSOLUTE "absolute"
#define VECTAGGERRELATIVE "relative"
#define VECTAGGERCDF      "cdf"
#define VECTAGGEROR       "or"
#define VECTAGGERAND      "and"
```

Example 2 (unknown):
```unknown
VecTaggerCreate()
```

---

## VecTaggerView#

**URL:** https://petsc.org/release/manualpages/Vec/VecTaggerView/

**Contents:**
- VecTaggerView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

view a VecTagger context

viewer - viewer to display tagger, for example PETSC_VIEWER_STDOUT_WORLD

VecTaggerCreate(), VecTagger

src/vec/vec/utils/tagger/interface/tagger.c

VecTaggerView_AndOr() in src/vec/vec/utils/tagger/impls/andor.c VecTaggerView_CDF() in src/vec/vec/utils/tagger/impls/cdf.c VecTaggerView_Simple() in src/vec/vec/utils/tagger/impls/simple.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecTaggerView(VecTagger tagger, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PETSC_VIEWER_STDOUT_WORLD
```

Example 3 (unknown):
```unknown
VecTaggerCreate()
```

---

## VecTagger#

**URL:** https://petsc.org/release/manualpages/Vec/VecTagger/

**Contents:**
- VecTagger#
- Synopsis#
- Values#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Object used to manage the tagging of a subset of indices based on the values of a vector. The motivating application is the selection of cells for refinement or coarsening based on vector containing the values in an error indicator metric.

VECTAGGERABSOLUTE - “absolute” values are in a interval (box for complex values) of explicitly defined values

VECTAGGERRELATIVE - “relative” values are in a interval (box for complex values) of values relative to the set of all values in the vector

VECTAGGERCDF - “cdf” values are in a relative range of the cumulative distribution of values in the vector

VECTAGGEROR - “or” values are in the union of other tags

VECTAGGERAND - “and” values are in the intersection of other tags

Why not use a DMLabel or similar object

Vectors and Parallel Data, Vec, VecTaggerType, VecTaggerCreate()

src/snes/tutorials/ex27.c src/ts/tutorials/ex11.c src/vec/vec/utils/tagger/tutorials/ex1.c src/ts/tutorials/ex30.c

_p_VecTagger in include/petsc/private/vecimpl.h VecTagger_AndOr in src/vec/vec/utils/tagger/impls/andor.h VecTagger_CDF in src/vec/vec/utils/tagger/impls/cdf.c VecTagger_Simple in src/vec/vec/utils/tagger/impls/simple.h

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_VecTagger *VecTagger;
```

Example 2 (unknown):
```unknown
VECTAGGERABSOLUTE
```

Example 3 (unknown):
```unknown
VECTAGGERRELATIVE
```

Example 4 (unknown):
```unknown
VECTAGGERCDF
```

---

## VecTDotBegin#

**URL:** https://petsc.org/release/manualpages/Vec/VecTDotBegin/

**Contents:**
- VecTDotBegin#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Starts a split phase transpose dot product computation.

y - the second vector

result - where the result will go (can be NULL)

Each call to VecTDotBegin() should be paired with a call to VecTDotEnd().

VecTDotEnd(), VecNormBegin(), VecNormEnd(), VecNorm(), VecDot(), VecMDot(), VecDotBegin(), VecDotEnd(), PetscCommSplitReductionBegin()

src/vec/vec/utils/comb.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"    
PetscErrorCode VecTDotBegin(Vec x, Vec y, PetscScalar *result)
```

Example 2 (unknown):
```unknown
VecTDotBegin()
```

Example 3 (unknown):
```unknown
VecTDotEnd()
```

Example 4 (unknown):
```unknown
VecTDotEnd()
```

---

## VecTDotEnd#

**URL:** https://petsc.org/release/manualpages/Vec/VecTDotEnd/

**Contents:**
- VecTDotEnd#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Ends a split phase transpose dot product computation.

x - the first vector (can be NULL)

y - the second vector (can be NULL)

result - where the result will go

Each call to VecTDotBegin() should be paired with a call to VecTDotEnd().

VecTDotBegin(), VecNormBegin(), VecNormEnd(), VecNorm(), VecDot(), VecMDot(), VecDotBegin(), VecDotEnd()

src/vec/vec/utils/comb.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"    
PetscErrorCode VecTDotEnd(Vec x, Vec y, PetscScalar *result)
```

Example 2 (unknown):
```unknown
VecTDotBegin()
```

Example 3 (unknown):
```unknown
VecTDotEnd()
```

Example 4 (unknown):
```unknown
VecTDotBegin()
```

---

## VecTDot#

**URL:** https://petsc.org/release/manualpages/Vec/VecTDot/

**Contents:**
- VecTDot#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes for Users of Complex Numbers#
- See Also#
- Level#
- Location#
- Implementations#

Computes an indefinite vector dot product. That is, this routine does NOT use the complex conjugate.

val - the dot product

For complex vectors, VecTDot() computes the indefinite form

where y^T denotes the transpose of y.

Use VecDot() for the inner product

where y^H denotes the conjugate transpose of y.

Vectors and Parallel Data, Vec, VecDot(), VecMTDot()

src/vec/vec/interface/rvector.c

VecTDot_MPIKokkos() in src/vec/vec/impls/mpi/kokkos/mpikok.kokkos.cxx VecTDot_MPIViennaCL() in src/vec/vec/impls/mpi/mpiviennacl/mpiviennacl.cxx VecTDot_MPI() in src/vec/vec/impls/mpi/pvec2.c VecTDot_Nest() in src/vec/vec/impls/nest/vecnest.c VecTDot_Seq() in src/vec/vec/impls/seq/bvec1.c VecTDot_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecTDot_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecTDot(Vec x, Vec y, PetscScalar *val)
```

Example 2 (unknown):
```unknown
val = (x,y) = y^T x,
```

Example 3 (unknown):
```unknown
val = (x,y) = y^H x,
```

---

## Vectors and Parallel Data#

**URL:** https://petsc.org/release/manual/vec/

**Contents:**
- Vectors and Parallel Data#
- Creating Vectors#
  - DMDA - Creating vectors for structured grids#
  - DMSTAG - Creating vectors for staggered grids#
  - DMPLEX - Creating vectors for unstructured grids#
  - DMNETWORK - Creating vectors for networks#
- Common vector functions and operations#
- Assembling (putting values in) vectors#
  - DMDA - Setting vector values#
  - DMSTAG - Setting vector values#

Vectors (denoted by Vec) are used to store discrete PDE solutions, right-hand sides for linear systems, etc. Users can create and manipulate entries in vectors directly with a basic, low-level interface or they can use the PETSc DM objects to connect actions on vectors to the type of discretization and grid that they are working with. These higher-level interfaces handle much of the details of the interactions with vectors and hence, are preferred in most situations. This chapter is organized as follows:

DMDA - Creating vectors for structured grids

DMSTAG - Creating vectors for staggered grids

DMPLEX - Creating vectors for unstructured grids

DMNETWORK - Creating vectors for networks

Setting vector values

DMDA - Setting vector values

DMSTAG - Setting vector values

DMPLEX - Setting vector values

DMNETWORK - Setting vector values

Basic Vector Operations

Local/global vectors and communicating between vectors

Low-level Vector Communication

Local to global mappings

Global Vectors with locations for ghost values

Application Orderings

PETSc provides many ways to create vectors. The most basic, where the user is responsible for managing the parallel distribution of the vector entries, and a variety of higher-level approaches, based on DM, for classes of problems such as structured grids, staggered grids, unstructured grids, networks, and particles.

The most basic way to create a vector with a local size of m and a global size of M, is to use

which automatically generates the appropriate vector type (sequential or parallel) over all processes in comm. The option -vec_type type can be used in conjunction with VecSetFromOptions() to specify the use of a particular type of vector. For example, for NVIDIA GPU CUDA, use cuda. The GPU-based vectors allow one to set values on either the CPU or GPU but do their computations on the GPU.

We emphasize that all processes in comm must call the vector creation routines since these routines are collective on all processes in the communicator. If you are unfamiliar with MPI communicators, see the discussion in Writing PETSc Programs. In addition, if a sequence of creation routines is used, they must be called in the same order for each process in the communicator.

Instead of, or before calling VecSetFromOptions(), one can call

One can create vectors whose entries are stored on GPUs using the convenience routine,

There are convenience creation routines for almost all vector types; we recommend using the more verbose form because it allows selecting CPU or GPU simulations at runtime.

For applications running in parallel that involve multi-dimensional structured grids, unstructured grids, networks, etc, it is cumbersome for users to explicitly manage the needed local and global sizes of the vectors. Hence, PETSc provides two powerful abstract objects (lower level) PetscSection (see PetscSection: Connecting Grids to Data) and (higher level) DM (see DM Basics) to help manage the vectors and matrices needed for such applications. Using DM, parallel vectors can be created easily with

The DM object, see DMDA - Creating vectors for structured grids, DMSTAG - Creating vectors for staggered grids, and DMPlex: Unstructured Grids for more details on DM for structured grids, staggered structured grids, and for unstructured grids, manages creating the correctly sized parallel vectors efficiently. One controls the type of vector that DM creates by calling

or by calling DMSetFromOptions(DM dm) and using the option -dm_vec_type (standard|cuda|kokkos|hip).

One can create appropriately sized vectors from Mat with MatCreateVecs(). One can also create appropriately sized vectors with KSPCreateVecs().

Regardless of how PETSc vectors are created all of their entries are initially zero until a routine such as VecSet(), VecSetRandom(), VecSetValues() or similar routines are called to change the entries. Thus, it is wasteful and unnecessary to call VecZeroEntries() on a newly created Vec.

Each DM type is suitable for a family of problems. The first of these, DMDA are intended for use with logically structured rectangular grids when communication of nonlocal data is needed before certain local computations can occur. DMDA is designed only for the case in which data can be thought of as being stored in a standard multidimensional array; thus, DMDA are not intended for parallelizing staggered arrays/grids, DMSTAG – DMSTAG: Staggered, Structured Grid, or unstructured grid problems, DMPLEX – DMPlex: Unstructured Grids, etc.

For example, a typical situation one encounters in solving PDEs in parallel is that, to evaluate a local function, f(x), each process requires its local portion of the vector x as well as its ghost points (the bordering portions of the vector that are owned by neighboring processes). Figure Ghost Points for Two Stencil Types on the Seventh Process illustrates the ghost points for the seventh process of a two-dimensional, structured parallel grid. Each box represents a process; the ghost points for the seventh process’s local part of a parallel array are shown in gray.

Fig. 3 Ghost Points for Two Stencil Types on the Seventh Process#

The DMDA object contains parallel data layout information and communication information and is used to create vectors and matrices with the proper layout.

One creates a DMDA two dimensions with the convenience routine

The arguments M and N indicate the global numbers of grid points in each direction, while m and n denote the process partition in each direction; m*n must equal the number of processes in the MPI communicator, comm. Instead of specifying the process layout, one may use PETSC_DECIDE for m and n so that PETSc will select the partition. The type of periodicity of the array is specified by xperiod and yperiod, which can be DM_BOUNDARY_NONE (no periodicity), DM_BOUNDARY_PERIODIC (periodic in that direction), DM_BOUNDARY_TWIST (periodic in that direction, but identified in reverse order), DM_BOUNDARY_GHOSTED , or DM_BOUNDARY_MIRROR. The argument dof indicates the number of degrees of freedom at each array point, and s is the stencil width (i.e., the width of the ghost point region). The optional arrays lx and ly may contain the number of nodes along the x and y axis for each cell, i.e. the dimension of lx is m and the dimension of ly is n; alternately, NULL may be passed in.

Two types of DMDA communication data structures can be created, as specified by st. Star-type stencils that radiate outward only in the coordinate directions are indicated by DMDA_STENCIL_STAR, while box-type stencils are specified by DMDA_STENCIL_BOX. For example, for the two-dimensional case, DMDA_STENCIL_STAR with width 1 corresponds to the standard 5-point stencil, while DMDA_STENCIL_BOX with width 1 denotes the standard 9-point stencil. In both instances, the ghost points are identical, the only difference being that with star-type stencils, certain ghost points are ignored, substantially decreasing the number of messages sent. Note that the DMDA_STENCIL_STAR stencils can save interprocess communication in two and three dimensions.

These DMDA stencils have nothing directly to do with a specific finite difference stencil one might choose to use for discretization; they only ensure that the correct values are in place for the application of a user-defined finite difference stencil (or any other discretization technique).

The commands for creating DMDA in one and three dimensions are analogous:

The routines to create a DM are collective so that all processes in the communicator comm must call the same creation routines in the same order.

A DM may be created, and its type set with

Then DMType specific operations can be performed to provide information from which the specifics of the DM will be provided. For example,

We now very briefly introduce a few more DMType.

For structured grids with staggered data (living on elements, faces, edges, and/or vertices), the DMSTAG object is available. It behaves much like DMDA. See DMSTAG: Staggered, Structured Grid for discussion of creating vectors with DMSTAG.

See DMPlex: Unstructured Grids for a discussion of creating vectors with DMPLEX.

See Networks for discussion of creating vectors with DMNETWORK.

One can examine (print out) a vector with the command

To print the vector to the screen, one can use the viewer PETSC_VIEWER_STDOUT_WORLD, which ensures that parallel vectors are printed correctly to stdout. To display the vector in an X-window, one can use the default X-windows viewer PETSC_VIEWER_DRAW_WORLD, or one can create a viewer with the routine PetscViewerDrawOpen(). A variety of viewers are discussed further in Viewers: Looking at PETSc Objects.

To create a new vector of the same format and parallel layout as an existing vector, use

To create several new vectors of the same format as an existing vector, use

This routine creates an array of pointers to vectors. The two routines are useful because they allow one to write library code that does not depend on the particular format of the vectors being used. Instead, the subroutines can automatically create work vectors based on the specified existing vector.

When a vector is no longer needed, it should be destroyed with the command

To destroy an array of vectors, use the command

It is also possible to create vectors that use an array the user provides rather than having PETSc internally allocate the array space. Such vectors can be created with the routines such as

The array pointer should be a GPU memory location for GPU vectors.

Note that here, one must provide the value n; it cannot be PETSC_DECIDE and the user is responsible for providing enough space in the array; n*sizeof(PetscScalar).

One can assign a single value to all components of a vector with

Assigning values to individual vector components is more complicated to make it possible to write efficient parallel code. Assigning a set of components on a CPU is a two-step process: one first calls

any number of times on any or all of the processes. The argument n gives the number of components being set in this insertion. The integer array indices contains the global component indices, and values is the array of values to be inserted at those global component index locations. Any process can set any vector components; PETSc ensures that they are automatically stored in the correct location. Once all of the values have been inserted with VecSetValues(), one must call

to perform any needed message passing of nonlocal components. In order to allow the overlap of communication and calculation, the user’s code can perform any series of other actions between these two calls while the messages are in transition.

Example usage of VecSetValues() may be found in src/vec/vec/tutorials/ex2.c or src/vec/vec/tutorials/exf.F90.

Rather than inserting elements in a vector, one may wish to add values. This process is also done with the command

Again, one must call the assembly routines VecAssemblyBegin() and VecAssemblyEnd() after all of the values have been added. Note that addition and insertion calls to VecSetValues() cannot be mixed. Instead, one must add and insert vector elements in phases, with intervening calls to the assembly routines. This phased assembly procedure overcomes the nondeterministic behavior that would occur if two different processes generated values for the same location, with one process adding while the other is inserting its value. (In this case, the addition and insertion actions could be performed in either order, thus resulting in different values at the particular location. Since PETSc does not allow the simultaneous use of INSERT_VALUES and ADD_VALUES this nondeterministic behavior will not occur in PETSc.)

You can call VecGetValues() to pull local values from a vector (but not off-process values).

For vectors obtained with DMCreateGlobalVector(), one can use VecSetValuesLocal() to set values into a global vector but using the local (ghosted) vector indexing of the vector entries. See also Local to global mappings that allows one to provide arbitrary local-to-global mapping when not working with a DM.

It is also possible to interact directly with the arrays that the vector values are stored in. The routine VecGetArray() returns a pointer to the elements local to the process:

When access to the array is no longer needed, the user should call

For vectors that may also have the array data in GPU memory, for example, VECCUDA, this call ensures the CPU array has the most recent array values by copying the data from the GPU memory if needed.

If the values do not need to be modified, the routines

should be used instead.

Listing: SNES Tutorial src/snes/tutorials/ex1.c

Minor differences exist in the Fortran interface for VecGetArray() and VecRestoreArray(), as discussed in Output Arrays from PETSc functions. It is important to note that VecGetArray() and VecRestoreArray() do not copy the vector elements; they merely give users direct access to the vector elements. Thus, these routines require essentially no time to call and can be used efficiently.

For GPU vectors, one can access either the values on the CPU as described above or one can call, for example,

Listing: SNES Tutorial src/snes/tutorials/ex47cu.cu

which, in the first case, returns a GPU memory address and, in the second case, returns either a CPU or GPU memory address depending on the type of the vector. One can then launch a GPU kernel function that accesses the vector’s memory for usage with GPUs. When computing on GPUs, VecSetValues() is not used! One always accesses the vector’s arrays and passes them to the GPU code.

It can also be convenient to treat the vector entries as a Kokkos view. One first creates Kokkos vectors and then calls

to set or access the vector entries.

Of course, to provide the correct values to a vector, one must know what parts of the vector are owned by each MPI process. For parallel vectors, either CPU or GPU-based, it is possible to determine a process’s local range with the routine

The argument start indicates the first component owned by the local process, while end specifies one more than the last owned by the local process. This command is useful, for instance, in assembling parallel vectors.

If the Vec was obtained from a DM with DMCreateGlobalVector(), then the range values are determined by the specific DM. If the Vec was created directly, the range values are determined by the local size passed to VecSetSizes() or VecCreateMPI(). If PETSC_DECIDE was passed as the local size, then the vector uses default values for the range using PetscSplitOwnership(). For certain DM, such as DMDA, it is better to use DM specific routines, such as DMDAGetGhostCorners(), to determine the local values in the vector.

Very occasionally, all MPI processes need to know all the range values, these can be obtained with

The number of elements stored locally can be accessed with

The global vector length can be determined by

PETSc provides an easy way to set values into the DMDA vectors and access them using the natural grid indexing. This is done with the routines

where array is a multidimensional C array with the same dimension as da, and

where array is a multidimensional C array with one more dimension than da. The vector l can be either a global vector or a local vector. The array is accessed using the usual global indexing on the entire grid, but the user may only refer to this array’s local and ghost entries as all other entries are undefined. For example, for a scalar problem in two dimensions, one could use

Listing: SNES Tutorial src/snes/tutorials/ex3.c

The recommended approach for multi-component PDEs is to declare a struct representing the fields defined at each node of the grid, e.g.

and write the residual evaluation using

The DMDAVecGetArray routines are also provided for GPU access with CUDA, HIP, and Kokkos. For example,

where *XX* can contain any number of *. This allows one to write very natural Kokkos multi-dimensional parallel for kernels that act on the local portion of DMDA vectors.

Listing: SNES Tutorial src/snes/tutorials/ex3k.kokkos.cxx

The global indices of the lower left corner of the local portion of vectors obtained from DMDA as well as the local array size can be obtained with the commands

These values can then be used as loop bounds for local function evaluations as demonstrated in the function examples above.

The first version excludes ghost points, while the second includes them. The routine DMDAGetGhostCorners() deals with the fact that subarrays along boundaries of the problem domain have ghost points only on their interior edges, but not on their boundary edges.

When either type of stencil is used, DMDA_STENCIL_STAR or DMDA_STENCIL_BOX, the local vectors (with the ghost points) represent rectangular arrays, including the extra corner elements in the DMDA_STENCIL_STAR case. This configuration provides simple access to the elements by employing two- (or three–) dimensional indexing. The only difference between the two cases is that when DMDA_STENCIL_STAR is used, the extra corner components are not scattered between the processes and thus contain undefined values that should not be used.

For structured grids with staggered data (living on elements, faces, edges, and/or vertices), the DMStag object is available. It behaves like DMDA; see the DMSTAG manual page for more information.

Listing: SNES Tutorial src/dm/impls/stag/tutorials/ex6.c

See DMPlex: Unstructured Grids for a discussion on setting vector values with DMPLEX.

See Networks for a discussion on setting vector values with DMNETWORK.

VecAXPY(Vec y, PetscScalar a, Vec x);

VecAYPX(Vec y, PetscScalar a, Vec x);

VecWAXPY(Vec w, PetscScalar a, Vec x, Vec y);

VecAXPBY(Vec y, PetscScalar a, PetscScalar b, Vec x);

VecAXPBYPCZ(Vec z, PetscScalar a, PetscScalar b, PetscScalar c, Vec x, Vec y);

\(z = a*x + b*y + c*z\)

VecScale(Vec x, PetscScalar a);

VecDot(Vec x, Vec y, PetscScalar *r);

VecTDot(Vec x, Vec y, PetscScalar *r);

VecNorm(Vec x, NormType type, PetscReal *r);

VecSum(Vec x, PetscScalar *r);

VecCopy(Vec x, Vec y);

VecSwap(Vec x, Vec y);

\(y = x\) while \(x = y\)

VecPointwiseMult(Vec w, Vec x, Vec y);

\(w_{i} = x_{i}*y_{i}\)

VecPointwiseDivide(Vec w, Vec x, Vec y);

\(w_{i} = x_{i}/y_{i}\)

VecMDot(Vec x, PetscInt n, Vec y[], PetscScalar *r);

\(r[i] = \bar{x}^T*y[i]\)

VecMTDot(Vec x, PetscInt n, Vec y[], PetscScalar *r);

VecMAXPY(Vec y, PetscInt n, PetscScalar *a, Vec x[]);

\(y = y + \sum_i a_{i}*x[i]\)

VecMax(Vec x, PetscInt *idx, PetscReal *r);

VecMin(Vec x, PetscInt *idx, PetscReal *r);

VecReciprocal(Vec x);

VecShift(Vec x, PetscScalar s);

VecSet(Vec x, PetscScalar alpha);

As the table lists, we have chosen certain basic vector operations to support within the PETSc vector library. These operations were selected because they often arise in application codes. The NormType argument to VecNorm() is one of NORM_1, NORM_2, or NORM_INFINITY. The 1-norm is \(\sum_i |x_{i}|\), the 2-norm is \(( \sum_{i} x_{i}^{2})^{1/2}\) and the infinity norm is \(\max_{i} |x_{i}|\).

In addition to VecDot() and VecMDot() and VecNorm(), PETSc provides split phase versions of this functionality that allow several independent inner products and/or norms to share the same communication (thus improving parallel efficiency). For example, one may have code such as

This code works fine, but it performs four separate parallel communication operations. Instead, one can write

With this code, the communication is delayed until the first call to VecxxxEnd() at which a single MPI reduction is used to communicate all the values. It is required that the calls to the VecxxxEnd() are performed in the same order as the calls to the VecxxxBegin(); however, if you mistakenly make the calls in the wrong order, PETSc will generate an error informing you of this. There are additional routines VecTDotBegin() and VecTDotEnd(), VecMTDotBegin(), VecMTDotEnd().

For GPU vectors (like CUDA), the numerical computations will, by default, run on the GPU. Any scalar output, like the result of a VecDot() are placed in CPU memory.

Many PDE problems require ghost (or halo) values in each MPI process or even more general parallel communication of vector values. These values are needed to perform function evaluation on that MPI process. The exact structure of the ghost values needed depends on the type of grid being used. DM provides a uniform API for communicating the needed values. We introduce the concept in detail for DMDA.

Each DM object defines the layout of two vectors: a distributed global vector and a local vector that includes room for the appropriate ghost points. The DM object provides information about the size and layout of these vectors. The user can create vector objects that use the DM layout information with the routines

These vectors will generally serve as the building blocks for local and global PDE solutions, etc. If additional vectors with such layout information are needed in a code, they can be obtained by duplicating l or g via VecDuplicate() or VecDuplicateVecs().

We emphasize that a DM provides the information needed to communicate the ghost value information between processes. In most cases, several different vectors can share the same communication information (or, in other words, can share a given DM). The design of the DM object makes this easy, as each DM operation may operate on vectors of the appropriate size, as obtained via DMCreateLocalVector() and DMCreateGlobalVector() or as produced by VecDuplicate().

At certain stages of many applications, there is a need to work on a local portion of the vector that includes the ghost points. This may be done by scattering a global vector into its local parts by using the two-stage commands

which allows the overlap of communication and computation. Since the global and local vectors, given by g and l, respectively, must be compatible with the DM, da, they should be generated by DMCreateGlobalVector() and DMCreateLocalVector() (or be duplicates of such a vector obtained via VecDuplicate()). The InsertMode can be ADD_VALUES or INSERT_VALUES among other possible values.

One can scatter the local vectors into the distributed global vector with the command

In general this is used with an InsertMode of ADD_VALUES, because if one wishes to insert values into the global vector, they should access the global vector directly and put in the values.

A third type of DM scatter is from a local vector (including ghost points that contain irrelevant values) to a local vector with correct ghost point values. This scatter may be done with the commands

Since both local vectors, l1 and l2, must be compatible with da, they should be generated by DMCreateLocalVector() (or be duplicates of such vectors obtained via VecDuplicate()). The InsertMode can be either ADD_VALUES or INSERT_VALUES.

In most applications, the local ghosted vectors are only needed temporarily during user “function evaluations”. PETSc provides an easy, light-weight (requiring essentially no CPU time) way to temporarily obtain these work vectors and return them when no longer needed. This is done with the routines

Most users of PETSc who can utilize a DM will not need to utilize the lower-level routines discussed in the rest of this section and should skip ahead to Matrices.

To facilitate creating general vector scatters and gathers used, for example, in updating ghost points for problems for which no DM currently exists PETSc employs the concept of an index set, via the IS class. An index set, a generalization of a set of integer indices, is used to define scatters, gathers, and similar operations on vectors and matrices. Much of the underlying code that implements DMGlobalToLocal communication is built on the infrastructure discussed below.

The following command creates an index set based on a list of integers:

When mode is PETSC_COPY_VALUES, this routine copies the n indices passed to it by the integer array indices. Thus, the user should be sure to free the integer array indices when it is no longer needed, perhaps directly after the call to ISCreateGeneral(). The communicator, comm, should include all processes using the IS.

Another standard index set is defined by a starting point (first) and a stride (step), and can be created with the command

The meaning of n, first, and step correspond to the MATLAB notation first:step:first+n*step.

Index sets can be destroyed with the command

On rare occasions, the user may need to access information directly from an index set. Several commands assist in this process:

The function ISGetIndices() returns a pointer to a list of the indices in the index set. For certain index sets, this may be a temporary array of indices created specifically for the call. Thus, once the user finishes using the array of indices, the routine

should be called to ensure that the system can free the space it may have used to generate the list of indices.

A blocked version of index sets can be created with the command

This version is used for defining operations in which each element of the index set refers to a block of bs vector entries. Related routines analogous to those described above exist as well, including ISBlockGetIndices(), ISBlockGetSize(), ISBlockGetLocalSize(), ISGetBlockSize().

Most PETSc applications use a particular DM object to manage the communication details needed for their grids. In some rare cases, however, codes need to directly set up their required communication patterns. This is done using PETSc’s VecScatter and PetscSF (for more general data than vectors). One can select any subset of the components of a vector to insert or add to any subset of the components of another vector. We refer to these operations as generalized scatters, though they are a combination of scatters and gathers.

To copy selected components from one vector to another, one uses the following set of commands:

Here ix denotes the index set of the first vector, while iy indicates the index set of the destination vector. The vectors can be parallel or sequential. The only requirements are that the number of entries in the index set of the first vector, ix, equals the number in the destination index set, iy, and that the vectors be long enough to contain all the indices referred to in the index sets. If both x and y are parallel, their communicator must have the same set of processes, but their process order can differ. The argument INSERT_VALUES specifies that the vector elements will be inserted into the specified locations of the destination vector, overwriting any existing values. To add the components, rather than insert them, the user should select the option ADD_VALUES instead of INSERT_VALUES. One can also use MAX_VALUES or MIN_VALUES to replace the destination with the maximal or minimal of its current value and the scattered values.

To perform a conventional gather operation, the user makes the destination index set, iy, be a stride index set with a stride of one. Similarly, a conventional scatter can be done with an initial (sending) index set consisting of a stride. The scatter routines are collective operations (i.e. all processes that own a parallel vector must call the scatter routines). When scattering from a parallel vector to sequential vectors, each process has its own sequential vector that receives values from locations as indicated in its own index set. Similarly, in scattering from sequential vectors to a parallel vector, each process has its own sequential vector that contributes to the parallel vector.

Caution: When INSERT_VALUES is used, if two different processes contribute different values to the same component in a parallel vector, either value may be inserted. When ADD_VALUES is used, the correct sum is added to the correct location.

In some cases, one may wish to “undo” a scatter, that is, perform the scatter backward, switching the roles of the sender and receiver. This is done by using

Note that the roles of the first two arguments to these routines must be swapped whenever the SCATTER_REVERSE option is used.

Once a VecScatter object has been created, it may be used with any vectors that have the same parallel data layout. That is, one can call VecScatterBegin() and VecScatterEnd() with different vectors than used in the call to VecScatterCreate() as long as they have the same parallel layout (the number of elements on each process are the same). Usually, these “different” vectors would have been obtained via calls to VecDuplicate() from the original vectors used in the call to VecScatterCreate().

VecGetValues() can only access local values from the vector. To get off-process values, the user should create a new vector where the components will be stored and then perform the appropriate vector scatter. For example, if one desires to obtain the values of the 100th and 200th entries of a parallel vector, p, one could use a code such as that below. In this example, the values of the 100th and 200th components are placed in the array values. In this example, each process now has the 100th and 200th component, but obviously, each process could gather any elements it needed, or none by creating an index set with no entries.

The scatter comprises two stages to allow for the overlap of communication and computation. The introduction of the VecScatter context allows the communication patterns for the scatter to be computed once and reused repeatedly. Generally, even setting up the communication for a scatter requires communication; hence, it is best to reuse such information when possible.

Scatters provide a very general method for managing the communication of required ghost values for unstructured grid computations. One scatters the global vector into a local “ghosted” work vector, performs the computation on the local work vectors, and then scatters back into the global solution vector. In the simplest case, this may be written as

In this case, the scatter is used in a way similar to the usage of DMGlobalToLocal() and DMLocalToGlobal() discussed above.

When working with a global representation of a vector (usually on a vector obtained with DMCreateGlobalVector()) and a local representation of the same vector that includes ghost points required for local computation (obtained with DMCreateLocalVector()). PETSc provides routines to help map indices from a local numbering scheme to the PETSc global numbering scheme, recall their use above for the routine VecSetValuesLocal() introduced above. This is done via the following routines

Here N denotes the number of local indices, globalnum contains the global number of each local number, and ISLocalToGlobalMapping is the resulting PETSc object that contains the information needed to apply the mapping with either ISLocalToGlobalMappingApply() or ISLocalToGlobalMappingApplyIS().

Note that the ISLocalToGlobalMapping routines serve a different purpose than the AO routines. In the former case, they provide a mapping from a local numbering scheme (including ghost points) to a global numbering scheme, while in the latter, they provide a mapping between two global numbering schemes. Many applications may use both AO and ISLocalToGlobalMapping routines. The AO routines are first used to map from an application global ordering (that has no relationship to parallel processing, etc.) to the PETSc ordering scheme (where each process has a contiguous set of indices in the numbering). Then, to perform function or Jacobian evaluations locally on each process, one works with a local numbering scheme that includes ghost points. The mapping from this local numbering scheme back to the global PETSc numbering can be handled with the ISLocalToGlobalMapping routines.

If one is given a list of block indices in a global numbering, the routine

will provide a new list of indices in the local numbering. Again, negative values in idxin are left unmapped. But in addition, if type is set to IS_GTOLM_MASK , then nout is set to nin and all global values in idxin that are not represented in the local to global mapping are replaced by -1. When type is set to IS_GTOLM_DROP, the values in idxin that are not represented locally in the mapping are not included in idxout, so that potentially nout is smaller than nin. One must pass in an array long enough to hold all the indices. One can call ISGlobalToLocalMappingApplyBlock() with idxout equal to NULL to determine the required length (returned in nout) and then allocate the required space and call ISGlobalToLocalMappingApplyBlock() a second time to set the values.

Often it is convenient to set elements into a vector using the local node numbering rather than the global node numbering (e.g., each process may maintain its own sublist of vertices and elements and number them locally). To set values into a vector with the local numbering, one must first call

Now the indices use the local numbering rather than the global, meaning the entries lie in \([0,n)\) where \(n\) is the local size of the vector. Global vectors obtained from a DM already have the global to local mapping provided by the DM.

One can use global indices with MatSetValues() or MatSetValuesStencil() to assemble global stiffness matrices. Alternately, the global node number of each local node, including the ghost nodes, can be obtained by calling

Now, entries may be added to the vector and matrix using the local numbering and VecSetValuesLocal() and MatSetValuesLocal().

The example SNES Tutorial ex5 illustrates the use of a DMDA in the solution of a nonlinear problem. The analogous Fortran program is SNES Tutorial ex5f90; see SNES: Nonlinear Solvers for a discussion of the nonlinear solvers.

There are two minor drawbacks to the basic approach described above for unstructured grids:

the extra memory requirement for the local work vector, localin, which duplicates the local values in the memory in globalin, and

the extra time required to copy the local values from localin to globalin.

An alternative approach is to allocate global vectors with space preallocated for the ghost values.

Here n is the number of local vector entries, N is the number of global entries (or NULL), and nghost is the number of ghost entries. The array ghosts is of size nghost and contains the global vector location for each local ghost location. Using VecDuplicate() or VecDuplicateVecs() on a ghosted vector will generate additional ghosted vectors.

In many ways, a ghosted vector behaves like any other MPI vector created by VecCreateMPI(). The difference is that the ghosted vector has an additional “local” representation that allows one to access the ghost locations. This is done through the call to

The vector l is a sequential representation of the parallel vector g that shares the same array space (and hence numerical values); but allows one to access the “ghost” values past “the end of the” array. Note that one accesses the entries in l using the local numbering of elements and ghosts, while they are accessed in g using the global numbering.

A common usage of a ghosted vector is given by

The routines VecGhostUpdateBegin() and VecGhostUpdateEnd() are equivalent to the routines VecScatterBegin() and VecScatterEnd() above, except that since they are scattering into the ghost locations, they do not need to copy the local vector values, which are already in place. In addition, the user does not have to allocate the local work vector since the ghosted vector already has allocated slots to contain the ghost values.

The input arguments INSERT_VALUES and SCATTER_FORWARD cause the ghost values to be correctly updated from the appropriate process. The arguments ADD_VALUES and SCATTER_REVERSE update the “local” portions of the vector from all the other processes’ ghost values. This would be appropriate, for example, when performing a finite element assembly of a load vector. One can also use MAX_VALUES or MIN_VALUES with SCATTER_REVERSE.

DMPLEX does not yet support ghosted vectors sharing memory with the global representation. This is a work in progress; if you are interested in this feature, please contact the PETSc community members.

Partitioning discusses the important topic of partitioning an unstructured grid.

When writing parallel PDE codes, there is extra complexity caused by having multiple ways of indexing (numbering) and ordering objects such as vertices and degrees of freedom. For example, a grid generator or partitioner may renumber the nodes, requiring adjustment of the other data structures that refer to these objects; see Figure Natural Ordering and PETSc Ordering for a 2D Distributed Array (Four Processes). PETSc provides various tools to help manage the mapping amongst the various numbering systems. The most basic is the AO (application ordering), which enables mapping between different global (cross-process) numbering schemes.

In many applications, it is desirable to work with one or more “orderings” (or numberings) of degrees of freedom, cells, nodes, etc. Doing so in a parallel environment is complicated by the fact that each process cannot keep complete lists of the mappings between different orderings. In addition, the orderings used in the PETSc linear algebra routines (often contiguous ranges) may not correspond to the “natural” orderings for the application.

PETSc provides certain utility routines that allow one to deal cleanly and efficiently with the various orderings. To define a new application ordering (called an AO in PETSc), one can call the routine

The arrays apordering and petscordering, respectively, contain a list of integers in the application ordering and their corresponding mapped values in the PETSc ordering. Each process can provide whatever subset of the ordering it chooses, but multiple processes should never contribute duplicate values. The argument n indicates the number of local contributed values.

For example, consider a vector of length 5, where node 0 in the application ordering corresponds to node 3 in the PETSc ordering. In addition, nodes 1, 2, 3, and 4 of the application ordering correspond, respectively, to nodes 2, 1, 4, and 0 of the PETSc ordering. We can write this correspondence as

The user can create the PETSc AO mappings in several ways. For example, if using two processes, one could call

on the first process and

on the other process.

Once the application ordering has been created, it can be used with either of the commands

Upon input, the n-dimensional array indices specifies the indices to be mapped, while upon output, indices contains the mapped values. Since we, in general, employ a parallel database for the AO mappings, it is crucial that all processes that called AOCreateBasic() also call these routines; these routines cannot be called by just a subset of processes in the MPI communicator that was used in the call to AOCreateBasic().

An alternative routine to create the application ordering, AO, is

where index sets are used instead of integer arrays.

will map index sets (IS objects) between orderings. Both the AOXxxToYyy() and AOXxxToYyyIS() routines can be used regardless of whether the AO was created with a AOCreateBasic() or AOCreateBasicIS().

The AO context should be destroyed with AODestroy(AO *ao) and viewed with AOView(AO ao,PetscViewer viewer).

Although we refer to the two orderings as “PETSc” and “application” orderings, the user is free to use them both for application orderings and to maintain relationships among a variety of orderings by employing several AO contexts.

The AOxxToxx() routines allow negative entries in the input integer array. These entries are not mapped; they remain unchanged. This functionality enables, for example, mapping neighbor lists that use negative numbers to indicate nonexistent neighbors due to boundary conditions, etc.

Since the global ordering that PETSc uses to manage its parallel vectors (and matrices) does not usually correspond to the “natural” ordering of a two- or three-dimensional array, the DMDA structure provides an application ordering AO (see Application Orderings) that maps between the natural ordering on a rectangular grid and the ordering PETSc uses to parallelize. This ordering context can be obtained with the command

In Figure Natural Ordering and PETSc Ordering for a 2D Distributed Array (Four Processes), we indicate the orderings for a two-dimensional DMDA, divided among four processes.

Fig. 4 Natural Ordering and PETSc Ordering for a 2D Distributed Array (Four Processes)#

As discussed above, the VecScatter object allows one to define parallel communication between vectors by listing, with IS objects, which vector entries from one vector are to be communicated to another vector and where in the second vector they are to be inserted. PetscSF provides a similar more general functionality for arrays of any MPI datatype.

PetscSF communicates between rootdata and leafdata arrays. rootdata is distributed across the MPI processes and its entries are indicated by a PetscSFNode pair consisting of the MPI rank the entry is located on and the index in the array on that MPI process.

Each entry is uniquely owned at that location; in the same way a PETSc global vector has unique MPI process ownership of each entry.

leafdata is similar to PETSc local vectors; each MPI process’s leafdata array can contain “ghost values” that match values in other locations of the leafdata (on the same or different MPI processes). All these matching ghost values share a common root value in rootdata.

We begin to explain the use of PetscSF with an example. First we construct an array that tells for each leaf entry on that MPI process where its root entry is:

Next, we construct the PetscSF that encapsulates this information needed for communication:

Next we fill rootdata:

Finally, we use the PetscSF to communicate rootdata to leafdata:

Now leafdata on MPI rank 0 contains (1, 3, 2) and on MPI rank 1 contains (1, 2, 3).

It is also possible to move leafdata to rootdata using

In this case, since the reduction operation performed (the final argument of PetscSFReduceBegin()), is MPIU_SUM the final result in each entry of rootdata is the sum of the previous value at that location plus all the values it that entries leafs. So rootdata on MPI rank 0 contains (3, 6) while on MPI rank 1 it contains (9).

As shown in the example above, PetscSFBcastBegin() and PetscSFBcastEnd() (as well as other PetscSF functions) also take an MPI_Op reduction argument, though that is almost always MPI_REPLACE.

In the example above we treated the leafdata as sitting in a contiguous array with entries from 0 to one less than nleaves. This is indicated by the NULL argument in the call to PetscSFSetGraph(). More generally the leafdata array can have entries in it that are not accessed by the PetscSF operations. For example,

means that the three entries of leafdata affected by PetscSF communication on MPI rank 0 are the array locations (1, 2, 4); meaning also that leafdata must be of length at least 5. On MPI rank 1, the arriving values from the three roots listed in roots are placed backwards in leafdata. Note that providing the leaves permutation array on MPI rank 1 is equivalent to listing the three values in roots in the opposite order.

If we reran the initial communication with PetscSFBcastBegin() and PetscSFBcastEnd() using the modified sf the resulting values in leavedata would be on MPI rank 0 (x, 1, 3, x, 2) and on MPI rank 1 (3, 2, 1) where x indicates the previous value in leafdata that was unchanged.

rootdata and leafdata can live either on CPU memory or GPU memory. The PetscSF routines automatically detect the memory type. But the time for the calls to the CUDA or HIP routines for doing this determination (cudaPointerGetAttributes() or hipPointerGetAttributes()) is not trivial. To avoid the cost of the check, PetscSF provides the routines PetscSFBcastWithMemTypeBegin() and PetscSFReduceWithMemTypeBegin() where the user provides the memory type information.

One may wish to gather the entries of the leafdata for each root but not reduce them to a single value. This is done with

Here multirootdata is (generally) an array larger than rootdata that has enough locations to store the value of each leaf of each local root. The values are stored contiguously for each root; that is multirootdata will contain

The number of leaves for each local root (sometimes called the degree of the root) can be obtained with calls to PetscSFComputeDegreeBegin() and PetscSFComputeDegreeEnd().

The data in multirootdata can be communicated to leafdata using

A performance drawback to using PetscSFSetGraph() is that it requires explicitly listing in arrays all the entries of roots. PetscSFSetGraphWithPattern() provides an alternative way to indicate the communication graph for specific communication patterns.

The Solvers in PETSc/TAO

**Examples:**

Example 1 (unknown):
```unknown
VecCreate(MPI_Comm comm, Vec *v);
VecSetSizes(Vec v, PetscInt m, PetscInt M);
VecSetFromOptions(Vec v);
```

Example 2 (unknown):
```unknown
-vec_type type
```

Example 3 (unknown):
```unknown
VecSetFromOptions()
```

Example 4 (unknown):
```unknown
VecSetFromOptions()
```

---

## Vector Operations (Vec)#

**URL:** https://petsc.org/release/manualpages/Vec/

**Contents:**
- Vector Operations (Vec)#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Deprecated - Functionality scheduled for removal in the future#
- Single list of manual pages#

PETSc vectors (Vec) are used to store the field variables in PDE-based (or other) simulations. Users guide chapter: Vectors and Parallel Data

REDUCTION_MEAN_IMAGINARYPART

REDUCTION_MEAN_REALPART

REDUCTION_SUM_IMAGINARYPART

REDUCTION_SUM_REALPART

VecGetArrayAndMemType

VecGetArrayReadAndMemType

VecGetArrayWriteAndMemType

VecGetKokkosViewWrite

VecGetLocalVectorRead

VecGetOwnershipRanges

VecRestoreArray4dRead

VecRestoreArrayAndMemType

VecRestoreArrayReadAndMemType

VecRestoreArrayWriteAndMemType

VecRestoreKokkosViewWrite

VecRestoreLocalVector

VecRestoreLocalVectorRead

VecScatterSetFromOptions

VecSetPreallocationCOO

VecSetPreallocationCOOLocal

VecCUDARestoreArrayRead

VecCUDARestoreArrayWrite

VecCreateMPICUDAWithArray

VecCreateMPICUDAWithArrays

VecCreateMPIHIPWithArray

VecCreateMPIHIPWithArrays

VecCreateMPIKokkosWithArray

VecCreateMPIViennaCLWithArray

VecCreateMPIViennaCLWithArrays

VecCreateMPIWithArray

VecCreateSeqCUDAWithArray

VecCreateSeqCUDAWithArrays

VecCreateSeqHIPWithArray

VecCreateSeqHIPWithArrays

VecCreateSeqKokkosWithArray

VecCreateSeqViennaCLWithArray

VecCreateSeqViennaCLWithArrays

VecCreateSeqWithArray

VecHIPRestoreArrayRead

VecHIPRestoreArrayWrite

VecScatterCreateToAll

VecScatterCreateToZero

VecScatterViewFromOptions

VecSetLocalToGlobalMapping

VecSetValuesBlockedLocal

VecStashSetInitialSize

VecStashViewFromOptions

VecViennaCLGetCLContext

VecViennaCLGetCLMemRead

VecViennaCLGetCLMemWrite

VecViennaCLGetCLQueue

VecViennaCLPlaceArray

VecViennaCLRestoreCLMem

VecViennaCLRestoreCLMemWrite

PetscCommSplitReductionBegin

VecAppendOptionsPrefix

VecBoundGradientProjection

VecCreateGhostBlockWithArray

VecCreateGhostWithArray

VecGetLocalToGlobalMapping

VecGhostRestoreLocalForm

VecMaxPointwiseDivide

VecNestGetSubVecsRead

VecNestRestoreSubVecsRead

VecStrideSubSetGather

VecStrideSubSetScatter

VecTaggerAbsoluteGetBox

VecTaggerAbsoluteSetBox

VecTaggerCDFGetMethod

VecTaggerCDFIterativeGetTolerances

VecTaggerCDFIterativeSetTolerances

VecTaggerCDFSetMethod

VecTaggerComputeBoxes

VecTaggerGetBlockSize

VecTaggerRelativeGetBox

VecTaggerRelativeSetBox

VecTaggerSetBlockSize

VecTaggerSetFromOptions

VecWhichBetweenOrEqual

VecsCreateSeqWithArray

SCATTER_FORWARD_LOCAL

SCATTER_REVERSE_LOCAL

VecErrorWeightedNorms

VecGetBindingPropagates

VecGetPinnedMemoryMin

VecRestoreArray1dRead

VecRestoreArray1dWrite

VecRestoreArray2dRead

VecRestoreArray2dWrite

VecRestoreArray3dRead

VecRestoreArray3dWrite

VecRestoreArray4dWrite

VecSetBindingPropagates

VecSetPinnedMemoryMin

VecTaggerFinalizePackage

VecTaggerInitializePackage

VecViennaCLResetArray

PetscCommSplitReductionBegin

REDUCTION_MEAN_IMAGINARYPART

REDUCTION_MEAN_REALPART

REDUCTION_SUM_IMAGINARYPART

REDUCTION_SUM_REALPART

SCATTER_FORWARD_LOCAL

SCATTER_REVERSE_LOCAL

VecAppendOptionsPrefix

VecBoundGradientProjection

VecCUDARestoreArrayRead

VecCUDARestoreArrayWrite

VecCreateGhostBlockWithArray

VecCreateGhostWithArray

VecCreateMPICUDAWithArray

VecCreateMPICUDAWithArrays

VecCreateMPIHIPWithArray

VecCreateMPIHIPWithArrays

VecCreateMPIKokkosWithArray

VecCreateMPIViennaCLWithArray

VecCreateMPIViennaCLWithArrays

VecCreateMPIWithArray

VecCreateSeqCUDAWithArray

VecCreateSeqCUDAWithArrays

VecCreateSeqHIPWithArray

VecCreateSeqHIPWithArrays

VecCreateSeqKokkosWithArray

VecCreateSeqViennaCLWithArray

VecCreateSeqViennaCLWithArrays

VecCreateSeqWithArray

VecErrorWeightedNorms

VecGetArrayAndMemType

VecGetArrayReadAndMemType

VecGetArrayWriteAndMemType

VecGetBindingPropagates

VecGetKokkosViewWrite

VecGetLocalToGlobalMapping

VecGetLocalVectorRead

VecGetOwnershipRanges

VecGetPinnedMemoryMin

VecGhostRestoreLocalForm

VecHIPRestoreArrayRead

VecHIPRestoreArrayWrite

VecMaxPointwiseDivide

VecNestGetSubVecsRead

VecNestRestoreSubVecsRead

VecRestoreArray1dRead

VecRestoreArray1dWrite

VecRestoreArray2dRead

VecRestoreArray2dWrite

VecRestoreArray3dRead

VecRestoreArray3dWrite

VecRestoreArray4dRead

VecRestoreArray4dWrite

VecRestoreArrayAndMemType

VecRestoreArrayReadAndMemType

VecRestoreArrayWriteAndMemType

VecRestoreKokkosViewWrite

VecRestoreLocalVector

VecRestoreLocalVectorRead

VecScatterCreateToAll

VecScatterCreateToZero

VecScatterSetFromOptions

VecScatterViewFromOptions

VecSetBindingPropagates

VecSetLocalToGlobalMapping

VecSetPinnedMemoryMin

VecSetPreallocationCOO

VecSetPreallocationCOOLocal

VecSetValuesBlockedLocal

VecStashSetInitialSize

VecStashViewFromOptions

VecStrideSubSetGather

VecStrideSubSetScatter

VecTaggerAbsoluteGetBox

VecTaggerAbsoluteSetBox

VecTaggerCDFGetMethod

VecTaggerCDFIterativeGetTolerances

VecTaggerCDFIterativeSetTolerances

VecTaggerCDFSetMethod

VecTaggerComputeBoxes

VecTaggerFinalizePackage

VecTaggerGetBlockSize

VecTaggerInitializePackage

VecTaggerRelativeGetBox

VecTaggerRelativeSetBox

VecTaggerSetBlockSize

VecTaggerSetFromOptions

VecViennaCLGetCLContext

VecViennaCLGetCLMemRead

VecViennaCLGetCLMemWrite

VecViennaCLGetCLQueue

VecViennaCLPlaceArray

VecViennaCLResetArray

VecViennaCLRestoreCLMem

VecViennaCLRestoreCLMemWrite

VecWhichBetweenOrEqual

VecsCreateSeqWithArray

Vectors and Index Sets

---

## VecType#

**URL:** https://petsc.org/release/manualpages/Vec/VecType/

**Contents:**
- VecType#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#

String with the name of a PETSc vector, Vec, type

Summary of Vector Types Available In PETSc, Vectors and Parallel Data, VecSetType(), Vec, VecCreate(), VecDestroy()

src/snes/tutorials/ex28.c src/ksp/ksp/tutorials/ex73.c src/mat/tutorials/ex19.c src/ksp/ksp/tutorials/ex76.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef const char *VecType;
#define VECSEQ         "seq"
#define VECMPI         "mpi"
#define VECSTANDARD    "standard" /* seq on one process and mpi on multiple */
#define VECSHARED      "shared"
#define VECSEQVIENNACL "seqviennacl"
#define VECMPIVIENNACL "mpiviennacl"
#define VECVIENNACL    "viennacl" /* seqviennacl on one process and mpiviennacl on multiple */
#define VECSEQCUDA     "seqcuda"
#define VECMPICUDA     "mpicuda"
#define VECCUDA        "cuda" /* seqcuda on one process and mpicuda on multiple */
#define VECSEQHIP      "seqhip"
#define VECMPIHIP      "mpihip"
#define VECHIP         "hip" /* seqhip on one process and mpihip on multiple */
#define VECNEST        "nest"
#define VECSEQKOKKOS   "seqkokkos"
#define VECMPIKOKKOS   "mpikokkos"
#define VECKOKKOS      "kokkos" /* seqkokkos on one process and mpikokkos on multiple */
```

Example 2 (unknown):
```unknown
VecSetType()
```

Example 3 (unknown):
```unknown
VecCreate()
```

Example 4 (unknown):
```unknown
VecDestroy()
```

---

## VecUniqueEntries#

**URL:** https://petsc.org/release/manualpages/Vec/VecUniqueEntries/

**Contents:**
- VecUniqueEntries#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Compute the number of unique entries, and those entries

n - The number of unique entries

e - The entries, each MPI process receives all the unique entries

src/vec/vec/utils/vinv.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PetscErrorCode VecUniqueEntries(Vec vec, PetscInt *n, PetscScalar *e[])
```

---

## VecViennaCLGetCLContext#

**URL:** https://petsc.org/release/manualpages/Vec/VecViennaCLGetCLContext/

**Contents:**
- VecViennaCLGetCLContext#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the OpenCL context in which the Vec resides.

Caller should cast (*ctx) to (const cl_context). Caller is responsible for invoking clReleaseContext().

ctx - pointer to the underlying CL context

VecViennaCLGetCLQueue(), VecViennaCLGetCLMemRead()

src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PETSC_EXTERN PetscErrorCode VecViennaCLGetCLContext(Vec v, PETSC_UINTPTR_T *ctx)
```

Example 2 (unknown):
```unknown
VecViennaCLGetCLQueue()
```

Example 3 (unknown):
```unknown
VecViennaCLGetCLMemRead()
```

---

## VecViennaCLGetCLMemRead#

**URL:** https://petsc.org/release/manualpages/Vec/VecViennaCLGetCLMemRead/

**Contents:**
- VecViennaCLGetCLMemRead#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Provides access to the CL buffer inside a Vec.

Caller should cast (*mem) to (const cl_mem). Caller is responsible for invoking clReleaseMemObject().

mem - pointer to the device buffer

VecViennaCLGetCLContext(), VecViennaCLGetCLMemWrite()

src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PETSC_EXTERN PetscErrorCode VecViennaCLGetCLMemRead(Vec v, PETSC_UINTPTR_T *mem)
```

Example 2 (unknown):
```unknown
VecViennaCLGetCLContext()
```

Example 3 (unknown):
```unknown
VecViennaCLGetCLMemWrite()
```

---

## VecViennaCLGetCLMemWrite#

**URL:** https://petsc.org/release/manualpages/Vec/VecViennaCLGetCLMemWrite/

**Contents:**
- VecViennaCLGetCLMemWrite#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Provides access to the CL buffer inside a Vec.

Caller should cast (*mem) to (const cl_mem). Caller is responsible for invoking clReleaseMemObject().

The device pointer has to be released by calling VecViennaCLRestoreCLMemWrite(). Upon restoring the vector data the data on the host will be marked as out of date. A subsequent access of the host data will thus incur a data transfer from the device to the host.

mem - pointer to the device buffer

VecViennaCLGetCLContext(), VecViennaCLRestoreCLMemWrite()

src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PETSC_EXTERN PetscErrorCode VecViennaCLGetCLMemWrite(Vec v, PETSC_UINTPTR_T *mem)
```

Example 2 (unknown):
```unknown
VecViennaCLGetCLContext()
```

Example 3 (unknown):
```unknown
VecViennaCLRestoreCLMemWrite()
```

---

## VecViennaCLGetCLMem#

**URL:** https://petsc.org/release/manualpages/Vec/VecViennaCLGetCLMem/

**Contents:**
- VecViennaCLGetCLMem#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Provides access to the CL buffer inside a Vec.

Caller should cast (*mem) to (const cl_mem). Caller is responsible for invoking clReleaseMemObject().

The device pointer has to be released by calling VecViennaCLRestoreCLMem(). Upon restoring the vector data the data on the host will be marked as out of date. A subsequent access of the host data will thus incur a data transfer from the device to the host.

mem - pointer to the device buffer

VecViennaCLGetCLContext(), VecViennaCLRestoreCLMem()

src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PETSC_EXTERN PetscErrorCode VecViennaCLGetCLMem(Vec v, PETSC_UINTPTR_T *mem)
```

Example 2 (unknown):
```unknown
VecViennaCLGetCLContext()
```

Example 3 (unknown):
```unknown
VecViennaCLRestoreCLMem()
```

---

## VecViennaCLGetCLQueue#

**URL:** https://petsc.org/release/manualpages/Vec/VecViennaCLGetCLQueue/

**Contents:**
- VecViennaCLGetCLQueue#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the OpenCL command queue to which all operations of the Vec are enqueued.

Caller should cast (*queue) to (const cl_command_queue). Caller is responsible for invoking clReleaseCommandQueue().

queue - pointer to the CL command queue

VecViennaCLGetCLContext(), VecViennaCLGetCLMemRead()

src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PETSC_EXTERN PetscErrorCode VecViennaCLGetCLQueue(Vec v, PETSC_UINTPTR_T *queue)
```

Example 2 (unknown):
```unknown
VecViennaCLGetCLContext()
```

Example 3 (unknown):
```unknown
VecViennaCLGetCLMemRead()
```

---

## VecViennaCLPlaceArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecViennaCLPlaceArray/

**Contents:**
- VecViennaCLPlaceArray#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Replace the viennacl vector in a Vec with the one provided by the user. This is useful to avoid a copy.

a - the ViennaCL vector

You can return to the original viennacl vector with a call to VecViennaCLResetArray(). It is not possible to use VecViennaCLPlaceArray() and VecPlaceArray() at the same time on the same vector.

VecPlaceArray(), VecSetValues(), VecViennaCLResetArray(), VecCUDAPlaceArray(),

src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PETSC_EXTERN PetscErrorCode VecViennaCLPlaceArray(Vec vin, const ViennaCLVector *a)
```

Example 2 (unknown):
```unknown
VecViennaCLResetArray()
```

Example 3 (unknown):
```unknown
VecViennaCLPlaceArray()
```

Example 4 (unknown):
```unknown
VecPlaceArray()
```

---

## VecViennaCLResetArray#

**URL:** https://petsc.org/release/manualpages/Vec/VecViennaCLResetArray/

**Contents:**
- VecViennaCLResetArray#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Resets a vector to use its default memory. Call this after the use of VecViennaCLPlaceArray().

VecViennaCLPlaceArray(), VecResetArray(), VecCUDAResetArray(), VecPlaceArray()

src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PETSC_EXTERN PetscErrorCode VecViennaCLResetArray(Vec vin)
```

Example 2 (unknown):
```unknown
VecViennaCLPlaceArray()
```

Example 3 (unknown):
```unknown
VecResetArray()
```

Example 4 (unknown):
```unknown
VecCUDAResetArray()
```

---

## VecViennaCLRestoreCLMemWrite#

**URL:** https://petsc.org/release/manualpages/Vec/VecViennaCLRestoreCLMemWrite/

**Contents:**
- VecViennaCLRestoreCLMemWrite#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Restores a CL buffer pointer previously acquired with VecViennaCLGetCLMemWrite().

This marks the host data as out of date. Subsequent access to the vector data on the host side with for instance VecGetArray() incurs a data transfer.

VecViennaCLGetCLContext(), VecViennaCLGetCLMemWrite()

src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PETSC_EXTERN PetscErrorCode VecViennaCLRestoreCLMemWrite(Vec v)
```

Example 2 (unknown):
```unknown
VecViennaCLGetCLContext()
```

Example 3 (unknown):
```unknown
VecViennaCLGetCLMemWrite()
```

---

## VecViennaCLRestoreCLMem#

**URL:** https://petsc.org/release/manualpages/Vec/VecViennaCLRestoreCLMem/

**Contents:**
- VecViennaCLRestoreCLMem#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Restores a CL buffer pointer previously acquired with VecViennaCLGetCLMem().

This marks the host data as out of date. Subsequent access to the vector data on the host side with for instance VecGetArray() incurs a data transfer.

VecViennaCLGetCLContext(), VecViennaCLGetCLMem()

src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h" 
PETSC_EXTERN PetscErrorCode VecViennaCLRestoreCLMem(Vec v)
```

Example 2 (unknown):
```unknown
VecViennaCLGetCLContext()
```

Example 3 (unknown):
```unknown
VecViennaCLGetCLMem()
```

---

## VECVIENNACL#

**URL:** https://petsc.org/release/manualpages/Vec/VECVIENNACL/

**Contents:**
- VECVIENNACL#
- Options Database Keys#
- See Also#
- Level#
- Location#

VECVIENNACL = “viennacl” - A VECSEQVIENNACL on a single-process communicator, and VECMPIVIENNACL otherwise.

-vec_type viennacl - sets the vector type to VECVIENNACL during a call to VecSetFromOptions()

VecCreate(), VecSetType(), VecSetFromOptions(), VecCreateMPIWithArray(), VECSEQVIENNACL, VECMPIVIENNACL, VECSTANDARD, VecType, VecCreateMPI()

src/vec/vec/impls/mpi/mpiviennacl/mpiviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VECSEQVIENNACL
```

Example 2 (unknown):
```unknown
VECMPIVIENNACL
```

Example 3 (unknown):
```unknown
VecSetFromOptions()
```

Example 4 (unknown):
```unknown
VecCreate()
```

---

## VecViewFromOptions#

**URL:** https://petsc.org/release/manualpages/Vec/VecViewFromOptions/

**Contents:**
- VecViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

View a vector based on values in the options database

obj - optional object that provides the options prefix for this viewing, use NULL to use the prefix of A

name - command line option

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

Vectors and Parallel Data, Vec, VecView, PetscObjectViewFromOptions(), VecCreate()

src/vec/vec/interface/vector.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex71.c src/mat/tutorials/ex3.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex26.c src/snes/tutorials/ex17.c src/snes/tutorials/ex23.c src/snes/tutorials/ex7.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecViewFromOptions(Vec A, PeOp PetscObject obj, const char name[])
```

Example 2 (unknown):
```unknown
PetscObjectViewFromOptions()
```

Example 3 (unknown):
```unknown
PetscObjectViewFromOptions()
```

Example 4 (unknown):
```unknown
VecCreate()
```

---

## VecViewNative#

**URL:** https://petsc.org/release/manualpages/Vec/VecViewNative/

**Contents:**
- VecViewNative#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Views a vector object with the original type specific viewer

viewer - an optional PetscViewer visualization context

This can be used with, for example, vectors obtained with DMCreateGlobalVector() for a DMDA to display the vector in the PETSc storage format (each MPI process values follow the previous MPI processes) instead of the “natural” grid ordering.

Vectors and Parallel Data, Vec, PetscViewerASCIIOpen(), PetscViewerDrawOpen(), PetscDrawLGCreate(), VecView(), PetscViewerSocketOpen(), PetscViewerBinaryOpen(), VecLoad(), PetscViewerCreate(), PetscRealView(), PetscScalarView(), PetscIntView(), PetscViewerHDF5SetTimestep()

src/vec/vec/interface/vector.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecViewNative(Vec vec, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 4 (unknown):
```unknown
PetscViewerASCIIOpen()
```

---

## VecView#

**URL:** https://petsc.org/release/manualpages/Vec/VecView/

**Contents:**
- VecView#
- Synopsis#
- Input Parameters#
- Notes#
- Notes for binary viewer#
- Notes for HDF5 Viewer#
- See Also#
- Level#
- Location#
- Examples#

Views a vector object.

viewer - an optional PetscViewer visualization context

The available visualization contexts include

PETSC_VIEWER_STDOUT_SELF - for sequential vectors

PETSC_VIEWER_STDOUT_WORLD - for parallel vectors created on PETSC_COMM_WORLD

PETSC_VIEWER_STDOUT_(comm) - for parallel vectors created on MPI communicator comm

You can change the format the vector is printed using the option PetscViewerPushFormat().

The user can open alternative viewers with

PetscViewerASCIIOpen() - Outputs vector to a specified file

PetscViewerBinaryOpen() - Outputs vector in binary to a specified file; corresponding input uses VecLoad()

PetscViewerDrawOpen() - Outputs vector to an X window display

PetscViewerSocketOpen() - Outputs vector to Socket viewer

PetscViewerHDF5Open() - Outputs vector to HDF5 file viewer

The user can call PetscViewerPushFormat() to specify the output format of ASCII printed objects (when using PETSC_VIEWER_STDOUT_SELF, PETSC_VIEWER_STDOUT_WORLD and PetscViewerASCIIOpen()). Available formats include

PETSC_VIEWER_DEFAULT - default, prints vector contents

PETSC_VIEWER_ASCII_MATLAB - prints vector contents in MATLAB format

PETSC_VIEWER_ASCII_INDEX - prints vector contents, including indices of vector elements

PETSC_VIEWER_ASCII_COMMON - prints vector contents, using a format common among all vector types

You can pass any number of vector objects, or other PETSc objects to the same viewer.

In the debugger you can do call VecView(v,0) to display the vector. (The same holds for any PETSc object viewer).

If you pass multiple vectors to a binary viewer you can read them back in the same order with VecLoad().

If the blocksize of the vector is greater than one then you must provide a unique prefix to the vector with PetscObjectSetOptionsPrefix((PetscObject)vec,”uniqueprefix”); BEFORE calling VecView() on the vector to be stored and then set that same unique prefix on the vector that you pass to VecLoad(). The blocksize information is stored in an ASCII file with the same name as the binary file plus a “.info” appended to the filename. If you copy the binary file, make sure you copy the associated .info file with it.

See the manual page for VecLoad() on the exact format the binary viewer stores the values in the file.

The name of the Vec (given with PetscObjectSetName() is the name that is used for the object in the HDF5 file. If you wish to store the same Vec into multiple datasets in the same file (typically with different values), you must change its name each time before calling the VecView(). To load the same vector, the name of the Vec object passed to VecLoad() must be the same.

If the block size of the vector is greater than 1 then it is used as the first dimension in the HDF5 array. If the function PetscViewerHDF5SetBaseDimension2()is called then even if the block size is one it will be used as the first dimension in the HDF5 array (that is the HDF5 array will always be two dimensional) See also PetscViewerHDF5SetTimestep() which adds an additional complication to reading and writing Vec with the HDF5 viewer.

Vectors and Parallel Data, Vec, VecViewFromOptions(), PetscViewerASCIIOpen(), PetscViewerDrawOpen(), PetscDrawLGCreate(), PetscViewerSocketOpen(), PetscViewerBinaryOpen(), VecLoad(), PetscViewerCreate(), PetscRealView(), PetscScalarView(), PetscIntView(), PetscViewerHDF5SetTimestep()

src/vec/vec/interface/vector.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex5f90.F90 src/snes/tutorials/ex99.c src/snes/tutorials/ex1.c src/snes/tutorials/ex15.c src/snes/tutorials/ex12.c src/snes/tutorials/ex22.c src/snes/tutorials/ex33.c src/snes/tutorials/ex21.c src/snes/tutorials/ex77.c

VecView_DMComposite() in src/dm/impls/composite/pack.c VecView_pforest() in src/dm/impls/forest/p4est/pforest.h VecView_Network() in src/dm/impls/network/networkcreate.c VecView_Plex() in src/dm/impls/plex/plex.c VecView_Swarm() in src/dm/impls/swarm/swarm.c VecView_MPI() in src/vec/vec/impls/mpi/pdvec.c VecView_Nest() in src/vec/vec/impls/nest/vecnest.c VecView_Seq() in src/vec/vec/impls/seq/bvec2.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecView(Vec vec, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSC_VIEWER_STDOUT_SELF
```

Example 4 (unknown):
```unknown
PETSC_VIEWER_STDOUT_WORLD
```

---

## VecWAXPY#

**URL:** https://petsc.org/release/manualpages/Vec/VecWAXPY/

**Contents:**
- VecWAXPY#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#

Computes w = alpha x + y.

x - first vector, multiplied by alpha

w cannot be either x or y, but x and y can be the same

The implementation is optimized for alpha of -1.0, 0.0, and 1.0

Vectors and Parallel Data, Vec, VecAXPY(), VecAYPX(), VecAXPBY(), VecMAXPY(), VecAXPBYPCZ()

src/vec/vec/interface/rvector.c

src/ml/da/tutorials/ex3.c src/vec/vec/tutorials/ex1.c src/ml/da/tutorials/ex1.c src/tao/constrained/tutorials/tomographyADMM.c src/tao/pde_constrained/tutorials/parabolic.c src/vec/vec/tutorials/ex1f90.F90 src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex4.c src/tao/pde_constrained/tutorials/hyperbolic.c src/vec/vec/tutorials/ex20f90.F90

VecWAXPY_Nest() in src/vec/vec/impls/nest/vecnest.c VecWAXPY_Seq() in src/vec/vec/impls/seq/dvec2.c VecWAXPY_SeqKokkos() in src/vec/vec/impls/seq/kokkos/veckok.kokkos.cxx VecWAXPY_SeqViennaCL() in src/vec/vec/impls/seq/seqviennacl/vecviennacl.cxx

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
w = alpha x + y
```

Example 2 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecWAXPY(Vec w, PetscScalar alpha, Vec x, Vec y)
```

Example 3 (unknown):
```unknown
VecAXPBYPCZ()
```

---

## VecWhichBetweenOrEqual#

**URL:** https://petsc.org/release/manualpages/Vec/VecWhichBetweenOrEqual/

**Contents:**
- VecWhichBetweenOrEqual#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Creates an index set containing the indices where VecLow <= V <= VecHigh

V - Vector to compare

VecHigh - higher bound

S - The index set containing the indices i where veclow[i] <= v[i] <= vechigh[i]

src/vec/vec/utils/projection.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"  
PetscErrorCode VecWhichBetweenOrEqual(Vec VecLow, Vec V, Vec VecHigh, IS *S)
```

---

## VecWhichBetween#

**URL:** https://petsc.org/release/manualpages/Vec/VecWhichBetween/

**Contents:**
- VecWhichBetween#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates an index set containing the indices where VecLow < V < VecHigh

V - Vector to compare

VecHigh - higher bound

S - The index set containing the indices i where veclow[i] < v[i] < vechigh[i]

The vectors must have the same parallel layout

For complex numbers this only compares the real part

src/vec/vec/utils/projection.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"  
PetscErrorCode VecWhichBetween(Vec VecLow, Vec V, Vec VecHigh, IS *S)
```

---

## VecWhichEqual#

**URL:** https://petsc.org/release/manualpages/Vec/VecWhichEqual/

**Contents:**
- VecWhichEqual#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Creates an index set containing the indices where the vectors Vec1 and Vec2 have identical elements.

Vec1 - the first vector to compare

Vec2 - the second two vector to compare

S - The index set containing the indices i where vec1[i] == vec2[i]

The two vectors must have the same parallel layout

src/vec/vec/utils/projection.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"  
PetscErrorCode VecWhichEqual(Vec Vec1, Vec Vec2, IS *S)
```

---

## VecWhichGreaterThan#

**URL:** https://petsc.org/release/manualpages/Vec/VecWhichGreaterThan/

**Contents:**
- VecWhichGreaterThan#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates an index set containing the indices where the vectors Vec1 > Vec2

Vec1 - the first vector to compare

Vec2 - the second vector to compare

S - The index set containing the indices i where vec1[i] > vec2[i]

The two vectors must have the same parallel layout

For complex numbers this only compares the real part

src/vec/vec/utils/projection.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"  
PetscErrorCode VecWhichGreaterThan(Vec Vec1, Vec Vec2, IS *S)
```

---

## VecWhichInactive#

**URL:** https://petsc.org/release/manualpages/Vec/VecWhichInactive/

**Contents:**
- VecWhichInactive#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates an IS based on a set of vectors

V - Vector to compare

D - Direction to compare

VecHigh - higher bound

Strong - indicator for applying strongly inactive test

S - The index set containing the indices i where the bound is inactive

Creates an index set containing the indices where one of the following holds:

src/vec/vec/utils/projection.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"  
PetscErrorCode VecWhichInactive(Vec VecLow, Vec V, Vec D, Vec VecHigh, PetscBool Strong, IS *S)
```

Example 2 (yaml):
```yaml
- VecLow(i)  < V(i) < VecHigh(i)
  - VecLow(i)  = V(i) and D(i) <= 0 (< 0 when Strong is true)
  - VecHigh(i) = V(i) and D(i) >= 0 (> 0 when Strong is true)
```

---

## VecWhichLessThan#

**URL:** https://petsc.org/release/manualpages/Vec/VecWhichLessThan/

**Contents:**
- VecWhichLessThan#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates an index set containing the indices where the vectors Vec1 < Vec2

Vec1 - the first vector to compare

Vec2 - the second vector to compare

S - The index set containing the indices i where vec1[i] < vec2[i]

The two vectors must have the same parallel layout

For complex numbers this only compares the real part

src/vec/vec/utils/projection.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"  
PetscErrorCode VecWhichLessThan(Vec Vec1, Vec Vec2, IS *S)
```

---

## VecZeroEntries#

**URL:** https://petsc.org/release/manualpages/Vec/VecZeroEntries/

**Contents:**
- VecZeroEntries#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

puts a 0.0 in each element of a vector

If the norm of the vector is known to be zero then this skips the unneeded zeroing process

Vectors and Parallel Data, Vec, VecCreate(), VecSetOptionsPrefix(), VecSet(), VecSetValues()

src/vec/vec/interface/vector.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex16.c src/snes/tutorials/ex73f90t.F90 src/ksp/ksp/tutorials/ex70.c src/ksp/ksp/tutorials/ex71.c src/ksp/ksp/tutorials/ex49.c src/snes/tutorials/ex56.c src/ksp/ksp/tutorials/ex42.c src/ksp/ksp/tutorials/ex43.c src/ksp/ksp/tutorials/ex69.c

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscvec.h"   
PetscErrorCode VecZeroEntries(Vec vec)
```

Example 2 (unknown):
```unknown
VecCreate()
```

Example 3 (unknown):
```unknown
VecSetOptionsPrefix()
```

Example 4 (unknown):
```unknown
VecSetValues()
```

---

## Vec#

**URL:** https://petsc.org/release/manualpages/Vec/Vec/

**Contents:**
- Vec#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Abstract PETSc vector object. Used for holding solutions and right-hand sides for linear systems, nonlinear systems, and time integrators

Internally the actual vector representation is generally a simple array but most PETSc code can work on other representations through this abstraction

Summary of Vector Types Available In PETSc, Vectors and Parallel Data, VecCreate(), VecType, VecSetType()

src/mat/tutorials/ex3.c src/snes/tutorials/ex1.c src/mat/tutorials/ex9.c src/mat/tutorials/ex19.c src/snes/tutorials/ex40f90.F90 src/mat/tutorials/ex2.c src/mat/tutorials/ex12.c src/mat/tutorials/ex7.c

_p_Vec in include/petsc/private/vecimpl.h Vec_MOAB in include/petsc/private/dmmbimpl.h Vec_Chain in src/tao/unconstrained/impls/bmrm/bmrm.h Vec_Seq in src/vec/vec/impls/dvecimpl.h Vec_MPI in src/vec/vec/impls/mpi/pvecimpl.h Vec_Nest in src/vec/vec/impls/nest/vecnestimpl.h

Index of all Vec routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_Vec *Vec;
```

Example 2 (unknown):
```unknown
VecCreate()
```

Example 3 (unknown):
```unknown
VecSetType()
```

---
