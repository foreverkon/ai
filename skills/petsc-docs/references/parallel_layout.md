# Petsc-Docs-Full-Raw - Parallel Layout

**Pages:** 115

---

## AOApplicationToPetscIS#

**URL:** https://petsc.org/release/manualpages/AO/AOApplicationToPetscIS/

**Contents:**
- AOApplicationToPetscIS#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Maps an index set in the application-defined ordering to the PETSc ordering.

ao - the application ordering context

is - the index set; this is replaced with its mapped values

is - the mapped index set

The index set cannot be of ISType ISSTRIDE or ISBLOCK

Any integers in is that are negative are left unchanged. This allows one to convert, for example, neighbor lists that use negative entries to indicate nonexistent neighbors due to boundary conditions, etc.

Application Orderings, AO, AOCreateBasic(), AOView(), AOPetscToApplication(), AOPetscToApplicationIS(), AOApplicationToPetsc(), ISSTRIDE, ISBLOCK

src/vec/is/ao/interface/ao.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h" 
PetscErrorCode AOApplicationToPetscIS(AO ao, IS is)
```

Example 2 (unknown):
```unknown
AOCreateBasic()
```

Example 3 (unknown):
```unknown
AOPetscToApplication()
```

Example 4 (unknown):
```unknown
AOPetscToApplicationIS()
```

---

## AOApplicationToPetscPermuteInt#

**URL:** https://petsc.org/release/manualpages/AO/AOApplicationToPetscPermuteInt/

**Contents:**
- AOApplicationToPetscPermuteInt#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Permutes an array of blocks of integers in the application-defined ordering to the PETSc ordering.

ao - The application ordering context

block - The block size

array - The integer array

array - The permuted array

The length of the array should be \( block*N \), where N is length provided to the AOCreate*() method that created the AO.

The permutation takes array[i_app] --> array[i_pet], where i_app is the index of i in the application ordering and i_pet is the index of i in the PETSc ordering.

Application Orderings, AO, AOCreateBasic(), AOView(), AOPetscToApplicationIS(), AOApplicationToPetsc()

src/vec/is/ao/interface/ao.c

AOApplicationToPetscPermuteInt_Basic() in src/vec/is/ao/impls/basic/aobasic.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h" 
PetscErrorCode AOApplicationToPetscPermuteInt(AO ao, PetscInt block, PetscInt array[])
```

Example 2 (perl):
```perl
array[i_app] --> array[i_pet]
```

Example 3 (unknown):
```unknown
AOCreateBasic()
```

Example 4 (unknown):
```unknown
AOPetscToApplicationIS()
```

---

## AOApplicationToPetscPermuteReal#

**URL:** https://petsc.org/release/manualpages/AO/AOApplicationToPetscPermuteReal/

**Contents:**
- AOApplicationToPetscPermuteReal#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Permutes an array of blocks of reals in the application-defined ordering to the PETSc ordering.

ao - The application ordering context

block - The block size

array - The integer array

array - The permuted array

The length of the array should be \(block*N\), where N is length provided to the AOCreate*() method that created the AO.

The permutation takes array[i_app] --> array[i_pet], where i_app is the index of i in the application ordering and i_pet is the index of i in the PETSc ordering.

Application Orderings, AO, AOCreateBasic(), AOView(), AOApplicationToPetsc(), AOPetscToApplicationIS()

src/vec/is/ao/interface/ao.c

AOApplicationToPetscPermuteReal_Basic() in src/vec/is/ao/impls/basic/aobasic.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h" 
PetscErrorCode AOApplicationToPetscPermuteReal(AO ao, PetscInt block, PetscReal array[])
```

Example 2 (perl):
```perl
array[i_app] --> array[i_pet]
```

Example 3 (unknown):
```unknown
AOCreateBasic()
```

Example 4 (unknown):
```unknown
AOApplicationToPetsc()
```

---

## AOApplicationToPetsc#

**URL:** https://petsc.org/release/manualpages/AO/AOApplicationToPetsc/

**Contents:**
- AOApplicationToPetsc#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Maps a set of integers in the application-defined ordering to the PETSc ordering.

ao - the application ordering context

n - the number of integers

ia - the integers; these are replaced with their mapped value

ia - the mapped integers

Any integers in ia that are negative are left unchanged. This allows one to convert, for example, neighbor lists that use negative entries to indicate nonexistent neighbors due to boundary conditions, etc.

Integers that are out of range are mapped to -1

Application Orderings, AOCreateBasic(), AOView(), AOPetscToApplication(), AOPetscToApplicationIS()

src/vec/is/ao/interface/ao.c

src/dm/tutorials/ex6.c src/ksp/ksp/tutorials/ex59.c

AOApplicationToPetsc_Basic() in src/vec/is/ao/impls/basic/aobasic.c AOApplicationToPetsc_Mapping() in src/vec/is/ao/impls/mapping/aomapping.c AOApplicationToPetsc_MemoryScalable() in src/vec/is/ao/impls/memscalable/aomemscalable.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h" 
PetscErrorCode AOApplicationToPetsc(AO ao, PetscInt n, PetscInt ia[])
```

Example 2 (unknown):
```unknown
AOCreateBasic()
```

Example 3 (unknown):
```unknown
AOPetscToApplication()
```

Example 4 (unknown):
```unknown
AOPetscToApplicationIS()
```

---

## AOCreateBasicIS#

**URL:** https://petsc.org/release/manualpages/AO/AOCreateBasicIS/

**Contents:**
- AOCreateBasicIS#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Creates a basic application ordering using two IS index sets.

isapp - index set that defines an ordering

ispetsc - index set that defines another ordering (may be NULL to use the natural ordering)

aoout - the new application ordering

The index sets isapp and ispetsc must contain the all the integers 0 to napp-1 (where napp is the length of the index sets) with no duplicates; that is there cannot be any “holes”

Application Orderings, Low-level Vector Communication, IS, AO, AOCreateBasic(), AODestroy()

src/vec/is/ao/impls/basic/aobasic.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h"   
PetscErrorCode AOCreateBasicIS(IS isapp, IS ispetsc, AO *aoout)
```

Example 2 (unknown):
```unknown
AOCreateBasic()
```

Example 3 (unknown):
```unknown
AODestroy()
```

---

## AOCreateBasic#

**URL:** https://petsc.org/release/manualpages/AO/AOCreateBasic/

**Contents:**
- AOCreateBasic#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Creates a basic application ordering using two integer arrays.

comm - MPI communicator that is to share AO

napp - size of myapp and mypetsc

myapp - integer array that defines an ordering

mypetsc - integer array that defines another ordering (may be NULL to indicate the natural ordering, that is 0,1,2,3,…)

aoout - the new application ordering

The arrays myapp and mypetsc must contain the all the integers 0 to napp-1 with no duplicates; that is there cannot be any “holes” in the indices. Use AOCreateMapping() or AOCreateMappingIS() if you wish to have “holes” in the indices.

Application Orderings, Low-level Vector Communication, AO, AOCreateBasicIS(), AODestroy(), AOPetscToApplication(), AOApplicationToPetsc()

src/vec/is/ao/impls/basic/aobasic.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h"   
PetscErrorCode AOCreateBasic(MPI_Comm comm, PetscInt napp, const PetscInt myapp[], const PetscInt mypetsc[], AO *aoout)
```

Example 2 (unknown):
```unknown
AOCreateMapping()
```

Example 3 (unknown):
```unknown
AOCreateMappingIS()
```

Example 4 (unknown):
```unknown
AOCreateBasicIS()
```

---

## AOCreateMappingIS#

**URL:** https://petsc.org/release/manualpages/AO/AOCreateMappingIS/

**Contents:**
- AOCreateMappingIS#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Creates an application mapping using two index sets.

isapp - index set that defines an ordering

ispetsc - index set that defines another ordering, maybe NULL for identity IS

aoout - the new application ordering

-ao_view - call AOView() at the conclusion of AOCreateMappingIS()

The index sets isapp and ispetsc need NOT contain the all the integers 0 to N-1, that is there CAN be “holes” in the indices. Use AOCreateBasic() or AOCreateBasicIS() if they do not have holes for better performance.

Application Orderings, Low-level Vector Communication, AOCreateBasic(), AOCreateMapping(), AODestroy()

src/vec/is/ao/impls/mapping/aomapping.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h" 
PetscErrorCode AOCreateMappingIS(IS isapp, IS ispetsc, AO *aoout)
```

Example 2 (unknown):
```unknown
AOCreateMappingIS()
```

Example 3 (unknown):
```unknown
AOCreateBasic()
```

Example 4 (unknown):
```unknown
AOCreateBasicIS()
```

---

## AOCreateMapping#

**URL:** https://petsc.org/release/manualpages/AO/AOCreateMapping/

**Contents:**
- AOCreateMapping#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Creates an application mapping using two integer arrays.

comm - MPI communicator that is to share the AO

napp - size of integer arrays

myapp - integer array that defines an ordering

mypetsc - integer array that defines another ordering (may be NULL to indicate the identity ordering)

aoout - the new application mapping

-ao_view - call AOView() at the conclusion of AOCreateMapping()

The arrays myapp and mypetsc need NOT contain the all the integers 0 to napp-1, that is there CAN be “holes” in the indices. Use AOCreateBasic() or AOCreateBasicIS() if they do not have holes for better performance.

Application Orderings, AOCreateBasic(), AOCreateMappingIS(), AODestroy()

src/vec/is/ao/impls/mapping/aomapping.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h" 
PetscErrorCode AOCreateMapping(MPI_Comm comm, PetscInt napp, const PetscInt myapp[], const PetscInt mypetsc[], AO *aoout)
```

Example 2 (unknown):
```unknown
AOCreateMapping()
```

Example 3 (unknown):
```unknown
AOCreateBasic()
```

Example 4 (unknown):
```unknown
AOCreateBasicIS()
```

---

## AOCreateMemoryScalableIS#

**URL:** https://petsc.org/release/manualpages/AO/AOCreateMemoryScalableIS/

**Contents:**
- AOCreateMemoryScalableIS#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a memory scalable application ordering using two index sets.

isapp - index set that defines an ordering

ispetsc - index set that defines another ordering (may be NULL to use the natural ordering)

aoout - the new application ordering

The index sets isapp and ispetsc must contain the all the integers 0 to napp-1 (where napp is the length of the index sets) with no duplicates; that is there cannot be any “holes”.

Comparing with AOCreateBasicIS(), this routine trades memory with message communication.

Application Orderings, Low-level Vector Communication, AO, AOCreateBasicIS(), AOCreateMemoryScalable(), AODestroy()

src/vec/is/ao/impls/memscalable/aomemscalable.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h"   
PetscErrorCode AOCreateMemoryScalableIS(IS isapp, IS ispetsc, AO *aoout)
```

Example 2 (unknown):
```unknown
AOCreateBasicIS()
```

Example 3 (unknown):
```unknown
AOCreateBasicIS()
```

Example 4 (unknown):
```unknown
AOCreateMemoryScalable()
```

---

## AOCreateMemoryScalable#

**URL:** https://petsc.org/release/manualpages/AO/AOCreateMemoryScalable/

**Contents:**
- AOCreateMemoryScalable#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Creates a memory scalable application ordering using two integer arrays.

comm - MPI communicator that is to share the AO

napp - size of myapp and mypetsc

myapp - integer array that defines an ordering

mypetsc - integer array that defines another ordering (may be NULL to indicate the natural ordering, that is 0,1,2,3,…)

aoout - the new application ordering

The arrays myapp and mypetsc must contain the all the integers 0 to napp-1 with no duplicates; that is there cannot be any “holes” in the indices. Use AOCreateMapping() or AOCreateMappingIS() if you wish to have “holes” in the indices. Comparing with AOCreateBasic(), this routine trades memory with message communication.

Application Orderings, Low-level Vector Communication, AO, AOCreateMemoryScalableIS(), AODestroy(), AOPetscToApplication(), AOApplicationToPetsc()

src/vec/is/ao/impls/memscalable/aomemscalable.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h"   
PetscErrorCode AOCreateMemoryScalable(MPI_Comm comm, PetscInt napp, const PetscInt myapp[], const PetscInt mypetsc[], AO *aoout)
```

Example 2 (unknown):
```unknown
AOCreateMapping()
```

Example 3 (unknown):
```unknown
AOCreateMappingIS()
```

Example 4 (unknown):
```unknown
AOCreateBasic()
```

---

## AOCreate#

**URL:** https://petsc.org/release/manualpages/AO/AOCreate/

**Contents:**
- AOCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

Creates an application ordering. That is an object that maps from an application ordering to a PETSc ordering and vice versa

comm - MPI communicator that is to share the AO

ao - the new application ordering

-ao_type (basic|advanced|mapping|memoryscalable) - Sets the AO type; see AOType

-ao_view - call AOView() at the conclusion of AOCreate()

Application Orderings, AO, AOView(), AOSetIS(), AODestroy(), AOPetscToApplication(), AOApplicationToPetsc()

src/vec/is/ao/interface/ao.c

AOCreate_Basic() in src/vec/is/ao/impls/basic/aobasic.c AOCreate_MemoryScalable() in src/vec/is/ao/impls/memscalable/aomemscalable.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h" 
PetscErrorCode AOCreate(MPI_Comm comm, AO *ao)
```

Example 2 (unknown):
```unknown
AODestroy()
```

Example 3 (unknown):
```unknown
AOPetscToApplication()
```

Example 4 (unknown):
```unknown
AOApplicationToPetsc()
```

---

## AODestroy#

**URL:** https://petsc.org/release/manualpages/AO/AODestroy/

**Contents:**
- AODestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Destroys an application ordering.

ao - the application ordering context

Application Orderings, AO, AOCreate()

src/vec/is/ao/interface/ao.c

AODestroy_Basic() in src/vec/is/ao/impls/basic/aobasic.c AODestroy_Mapping() in src/vec/is/ao/impls/mapping/aomapping.c AODestroy_MemoryScalable() in src/vec/is/ao/impls/memscalable/aomemscalable.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h" 
PetscErrorCode AODestroy(AO *ao)
```

---

## AOFinalizePackage#

**URL:** https://petsc.org/release/manualpages/AO/AOFinalizePackage/

**Contents:**
- AOFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function finalizes everything in the AO package. It is called from PetscFinalize().

AOInitializePackage(), PetscInitialize()

src/vec/is/ao/interface/aoreg.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
#include "petscao.h"  
PetscErrorCode AOFinalizePackage(void)
```

Example 3 (unknown):
```unknown
AOInitializePackage()
```

Example 4 (unknown):
```unknown
PetscInitialize()
```

---

## AOGetType#

**URL:** https://petsc.org/release/manualpages/AO/AOGetType/

**Contents:**
- AOGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the AO type name (as a string) from the AO.

type - The AO type name

type should not be retained for later use as it will be an invalid pointer if the AOType of ao is changed.

AO, AOType, AOSetType(), AOCreate(), PetscObjectTypeCompare(), PetscObjectTypeCompareAny()

src/vec/is/ao/interface/aoreg.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h"  
PetscErrorCode AOGetType(AO ao, AOType *type)
```

Example 2 (unknown):
```unknown
AOSetType()
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

## AOInitializePackage#

**URL:** https://petsc.org/release/manualpages/AO/AOInitializePackage/

**Contents:**
- AOInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function initializes everything in the AO package. It is called from PetscDLLibraryRegister_petscvec() when using dynamic libraries, and on the first call to AOCreate() when using static or shared libraries.

AOFinalizePackage(), PetscInitialize()

src/vec/is/ao/interface/aoreg.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDLLibraryRegister_petscvec()
```

Example 2 (unknown):
```unknown
#include "petscao.h"  
PetscErrorCode AOInitializePackage(void)
```

Example 3 (unknown):
```unknown
AOFinalizePackage()
```

Example 4 (unknown):
```unknown
PetscInitialize()
```

---

## AOMappingHasApplicationIndex#

**URL:** https://petsc.org/release/manualpages/AO/AOMappingHasApplicationIndex/

**Contents:**
- AOMappingHasApplicationIndex#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Developer Notes#
- See Also#
- Level#
- Location#

Checks if an AO has a requested application index.

idex - The application index

hasIndex - Flag is PETSC_TRUE if the index exists

The name of the function is wrong, it should be AOHasApplicationIndex

Application Orderings, AOMappingHasPetscIndex(), AOCreateMapping(), AO

src/vec/is/ao/impls/mapping/aomapping.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h" 
PetscErrorCode AOMappingHasApplicationIndex(AO ao, PetscInt idex, PetscBool *hasIndex)
```

Example 2 (unknown):
```unknown
AOHasApplicationIndex
```

Example 3 (unknown):
```unknown
AOMappingHasPetscIndex()
```

Example 4 (unknown):
```unknown
AOCreateMapping()
```

---

## AOMappingHasPetscIndex#

**URL:** https://petsc.org/release/manualpages/AO/AOMappingHasPetscIndex/

**Contents:**
- AOMappingHasPetscIndex#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Developer Notes#
- See Also#
- Level#
- Location#

checks if an AO has a requested PETSc index.

idex - The PETSc index

hasIndex - Flag is PETSC_TRUE if the index exists

The name of the function is wrong, it should be AOHasPetscIndex

Application Orderings, AOMappingHasApplicationIndex(), AOCreateMapping()

src/vec/is/ao/impls/mapping/aomapping.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h" 
PetscErrorCode AOMappingHasPetscIndex(AO ao, PetscInt idex, PetscBool *hasIndex)
```

Example 2 (unknown):
```unknown
AOHasPetscIndex
```

Example 3 (unknown):
```unknown
AOMappingHasApplicationIndex()
```

Example 4 (unknown):
```unknown
AOCreateMapping()
```

---

## AOPetscToApplicationIS#

**URL:** https://petsc.org/release/manualpages/AO/AOPetscToApplicationIS/

**Contents:**
- AOPetscToApplicationIS#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Maps an index set in the PETSc ordering to the application-defined ordering.

ao - the application ordering context

is - the index set; this is replaced with its mapped values

is - the mapped index set

The index set cannot be of ISType ISSTRIDE or ISBLOCK.

Any integers in is that are negative are left unchanged. This allows one to convert, for example, neighbor lists that use negative entries to indicate nonexistent neighbors due to boundary conditions etc.

Application Orderings, AO, AOCreateBasic(), AOView(), AOApplicationToPetsc(), AOApplicationToPetscIS(), AOPetscToApplication(), ISSTRIDE, ISBLOCK

src/vec/is/ao/interface/ao.c

src/dm/tutorials/ex22.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h" 
PetscErrorCode AOPetscToApplicationIS(AO ao, IS is)
```

Example 2 (unknown):
```unknown
AOCreateBasic()
```

Example 3 (unknown):
```unknown
AOApplicationToPetsc()
```

Example 4 (unknown):
```unknown
AOApplicationToPetscIS()
```

---

## AOPetscToApplicationPermuteInt#

**URL:** https://petsc.org/release/manualpages/AO/AOPetscToApplicationPermuteInt/

**Contents:**
- AOPetscToApplicationPermuteInt#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Permutes an array of blocks of integers in the PETSc ordering to the application-defined ordering.

ao - The application ordering context

block - The block size

array - The integer array

array - The permuted array

The length of the array should be \(block*N\), where N is length provided to the AOCreate*() method that created the AO.

The permutation takes array[i_pet] --> array[i_app], where i_app is the index of i in the application ordering and i_pet is the index of i in the PETSc ordering.

Application Orderings, AO, AOCreateBasic(), AOView(), AOApplicationToPetsc(), AOPetscToApplicationIS()

src/vec/is/ao/interface/ao.c

AOPetscToApplicationPermuteInt_Basic() in src/vec/is/ao/impls/basic/aobasic.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h" 
PetscErrorCode AOPetscToApplicationPermuteInt(AO ao, PetscInt block, PetscInt array[])
```

Example 2 (perl):
```perl
array[i_pet] --> array[i_app]
```

Example 3 (unknown):
```unknown
AOCreateBasic()
```

Example 4 (unknown):
```unknown
AOApplicationToPetsc()
```

---

## AOPetscToApplicationPermuteReal#

**URL:** https://petsc.org/release/manualpages/AO/AOPetscToApplicationPermuteReal/

**Contents:**
- AOPetscToApplicationPermuteReal#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Permutes an array of blocks of reals in the PETSc ordering to the application-defined ordering.

ao - The application ordering context

block - The block size

array - The integer array

array - The permuted array

The length of the array should be \(block*N\), where N is length provided to the AOCreate*() method that created the AO.

The permutation takes array[i_pet] --> array[i_app], where i_app is the index of i in the application ordering and i_pet is the index of i in the PETSc ordering.

Application Orderings, AO, AOCreateBasic(), AOView(), AOApplicationToPetsc(), AOPetscToApplicationIS()

src/vec/is/ao/interface/ao.c

AOPetscToApplicationPermuteReal_Basic() in src/vec/is/ao/impls/basic/aobasic.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h" 
PetscErrorCode AOPetscToApplicationPermuteReal(AO ao, PetscInt block, PetscReal array[])
```

Example 2 (perl):
```perl
array[i_pet] --> array[i_app]
```

Example 3 (unknown):
```unknown
AOCreateBasic()
```

Example 4 (unknown):
```unknown
AOApplicationToPetsc()
```

---

## AOPetscToApplication#

**URL:** https://petsc.org/release/manualpages/AO/AOPetscToApplication/

**Contents:**
- AOPetscToApplication#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Maps a set of integers in the PETSc ordering to the application-defined ordering.

ao - the application ordering context

n - the number of integers

ia - the integers; these are replaced with their mapped value

ia - the mapped integers

Any integers in ia that are negative are left unchanged. This allows one to convert, for example, neighbor lists that use negative entries to indicate nonexistent neighbors due to boundary conditions, etc.

Integers that are out of range are mapped to -1

Application Orderings, AO, AOCreateBasic(), AOView(), AOApplicationToPetsc(), AOPetscToApplicationIS()

src/vec/is/ao/interface/ao.c

AOPetscToApplication_Basic() in src/vec/is/ao/impls/basic/aobasic.c AOPetscToApplication_Mapping() in src/vec/is/ao/impls/mapping/aomapping.c AOPetscToApplication_MemoryScalable() in src/vec/is/ao/impls/memscalable/aomemscalable.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h" 
PetscErrorCode AOPetscToApplication(AO ao, PetscInt n, PetscInt ia[])
```

Example 2 (unknown):
```unknown
AOCreateBasic()
```

Example 3 (unknown):
```unknown
AOApplicationToPetsc()
```

Example 4 (unknown):
```unknown
AOPetscToApplicationIS()
```

---

## AORegisterAll#

**URL:** https://petsc.org/release/manualpages/AO/AORegisterAll/

**Contents:**
- AORegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the application ordering components in the AO package.

AO, AOType, AORegister(), AORegisterDestroy()

src/vec/is/ao/interface/aoreg.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h"  
PetscErrorCode AORegisterAll(void)
```

Example 2 (unknown):
```unknown
AORegister()
```

Example 3 (unknown):
```unknown
AORegisterDestroy()
```

---

## AORegister#

**URL:** https://petsc.org/release/manualpages/AO/AORegister/

**Contents:**
- AORegister#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Register an application ordering method

Not Collective, No Fortran Support

sname - the name (AOType) of the AO scheme

function - the create routine for the application ordering method

AO, AOType, AOCreate(), AORegisterAll(), AOBASIC, AOADVANCED, AOMAPPING, AOMEMORYSCALABLE

src/vec/is/ao/interface/aoreg.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h"  
PetscErrorCode AORegister(const char sname[], PetscErrorCode (*function)(AO))
```

Example 2 (unknown):
```unknown
AORegisterAll()
```

Example 3 (unknown):
```unknown
AOMEMORYSCALABLE
```

---

## AOSetFromOptions#

**URL:** https://petsc.org/release/manualpages/AO/AOSetFromOptions/

**Contents:**
- AOSetFromOptions#
- Synopsis#
- Input Parameter#
- Options Database Key#
- See Also#
- Level#
- Location#

Sets AO options from the options database.

ao - the application ordering

-ao_type (basic|memoryscalable) - sets the type of the AO

Application Orderings, AO, AOCreate(), AOSetType(), AODestroy(), AOPetscToApplication(), AOApplicationToPetsc()

src/vec/is/ao/interface/ao.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h" 
PetscErrorCode AOSetFromOptions(AO ao)
```

Example 2 (unknown):
```unknown
AOSetType()
```

Example 3 (unknown):
```unknown
AODestroy()
```

Example 4 (unknown):
```unknown
AOPetscToApplication()
```

---

## AOSetIS#

**URL:** https://petsc.org/release/manualpages/AO/AOSetIS/

**Contents:**
- AOSetIS#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the IS associated with the application ordering.

ao - the application ordering

isapp - index set that defines an ordering

ispetsc - index set that defines another ordering (may be NULL to use the natural ordering)

This routine increases the reference count of isapp and ispetsc so you may/should destroy these arguments after this call if you no longer need them

Application Orderings, Low-level Vector Communication, AO, AOCreate(), AODestroy(), AOPetscToApplication(), AOApplicationToPetsc()

src/vec/is/ao/interface/ao.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h" 
PetscErrorCode AOSetIS(AO ao, IS isapp, IS ispetsc)
```

Example 2 (unknown):
```unknown
AODestroy()
```

Example 3 (unknown):
```unknown
AOPetscToApplication()
```

Example 4 (unknown):
```unknown
AOApplicationToPetsc()
```

---

## AOSetType#

**URL:** https://petsc.org/release/manualpages/AO/AOSetType/

**Contents:**
- AOSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Builds an application ordering for a particular AOType

method - The name of the AO type

-ao_type (basic|advanced|mapping|memoryscalable) - Sets the AO type; see AOType

See AOType for available AO types (for instance, AOBASIC and AOMEMORYSCALABLE).

AO are usually created via the convenience routines such as AOCreateBasic() or AOCreateMemoryScalable()

AO, AOType, AOCreateBasic(), AOCreateMemoryScalable(), AOGetType(), AOCreate()

src/vec/is/ao/interface/aoreg.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h"  
PetscErrorCode AOSetType(AO ao, AOType method)
```

Example 2 (unknown):
```unknown
AOMEMORYSCALABLE
```

Example 3 (unknown):
```unknown
AOCreateBasic()
```

Example 4 (unknown):
```unknown
AOCreateMemoryScalable()
```

---

## AOType#

**URL:** https://petsc.org/release/manualpages/AO/AOType/

**Contents:**
- AOType#
- Synopsis#
- See Also#
- Level#
- Location#

String with the name of a PETSc application ordering type

AOSetType(), AO, AOApplicationToPetsc(), AOCreateBasic(), AOCreate()

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef const char *AOType;
#define AOBASIC          "basic"
#define AOADVANCED       "advanced"
#define AOMAPPING        "mapping"
#define AOMEMORYSCALABLE "memoryscalable"
```

Example 2 (unknown):
```unknown
AOSetType()
```

Example 3 (unknown):
```unknown
AOApplicationToPetsc()
```

Example 4 (unknown):
```unknown
AOCreateBasic()
```

---

## AOViewFromOptions#

**URL:** https://petsc.org/release/manualpages/AO/AOViewFromOptions/

**Contents:**
- AOViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

View an AO based on values in the options database

ao - the application ordering context

obj - optional object that provides the prefix used to search the options database

name - command line option

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

Application Orderings, AO, AOView(), PetscObjectViewFromOptions(), AOCreate()

src/vec/is/ao/interface/ao.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h" 
PetscErrorCode AOViewFromOptions(AO ao, PetscObject obj, const char name[])
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

## AOView#

**URL:** https://petsc.org/release/manualpages/AO/AOView/

**Contents:**
- AOView#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Displays an application ordering.

ao - the application ordering context

viewer - viewer used for display

-ao_view - calls AOView() at end of AOCreate()

The available visualization contexts include

PETSC_VIEWER_STDOUT_SELF - standard output (default)

PETSC_VIEWER_STDOUT_WORLD - synchronized standard output where only the first processor opens the file. All other processors send their data to the first processor to print.

The user can open an alternative visualization context with PetscViewerASCIIOpen() - output to a specified file.

Application Orderings, AO, PetscViewer, PetscViewerASCIIOpen(), AOViewFromOptions()

src/vec/is/ao/interface/ao.c

AOView_Basic() in src/vec/is/ao/impls/basic/aobasic.c AOView_Mapping() in src/vec/is/ao/impls/mapping/aomapping.c AOView_MemoryScalable() in src/vec/is/ao/impls/memscalable/aomemscalable.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscao.h" 
PetscErrorCode AOView(AO ao, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PETSC_VIEWER_STDOUT_SELF
```

Example 3 (unknown):
```unknown
PETSC_VIEWER_STDOUT_WORLD
```

Example 4 (unknown):
```unknown
PetscViewerASCIIOpen()
```

---

## AO#

**URL:** https://petsc.org/release/manualpages/AO/AO/

**Contents:**
- AO#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Abstract PETSc object that manages mapping between different global numberings

An application ordering is usually a mapping between an application-centric numbering (the ordering that is “natural” for the application) and the parallel numbering (\(0\) to \(n_0-1\) on the first MPI process, \(n_0\) to \(n_1 - 1\) on the second MPI process, etc) that PETSc uses.

AOCreateBasic(), AOCreateBasicIS(), AOPetscToApplication(), AOView(), AOApplicationToPetsc(), AOType, AOSetType()

src/dm/tutorials/ex22.c src/dm/tutorials/ex6.c src/ksp/ksp/tutorials/ex59.c

_p_AO in src/vec/is/ao/aoimpl.h AO_Basic in src/vec/is/ao/impls/basic/aobasic.c AO_Mapping in src/vec/is/ao/impls/mapping/aomapping.c AO_MemoryScalable in src/vec/is/ao/impls/memscalable/aomemscalable.c

Index of all AO routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_AO *AO;
```

Example 2 (unknown):
```unknown
AOCreateBasic()
```

Example 3 (unknown):
```unknown
AOCreateBasicIS()
```

Example 4 (unknown):
```unknown
AOPetscToApplication()
```

---

## Application Orderings (AO)#

**URL:** https://petsc.org/release/manualpages/AO/

**Contents:**
- Application Orderings (AO)#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Single list of manual pages#

Application Orderings (AO) are objects that manage mappings between different global orderings. Users guide section: Application Orderings.

AOApplicationToPetscIS

AOApplicationToPetscPermuteInt

AOApplicationToPetscPermuteReal

AOCreateMemoryScalable

AOCreateMemoryScalableIS

AOPetscToApplicationPermuteInt

AOPetscToApplicationPermuteReal

AOMappingHasApplicationIndex

AOMappingHasPetscIndex

AOPetscToApplicationIS

AOApplicationToPetscIS

AOApplicationToPetscPermuteInt

AOApplicationToPetscPermuteReal

AOCreateMemoryScalable

AOCreateMemoryScalableIS

AOMappingHasApplicationIndex

AOMappingHasPetscIndex

AOPetscToApplicationIS

AOPetscToApplicationPermuteInt

AOPetscToApplicationPermuteReal

Section Data Layout (PetscSection)

Data Management between Vec and Mat, and Distributed Mesh Data Structures

---

## Data Layout and Communication#

**URL:** https://petsc.org/release/manualpages/DataLayout/

**Contents:**
- Data Layout and Communication#

Finite difference computation of Jacobians (MatFD)

Star Forest Communication (PetscSF)

---

## PetscLayoutMapLocal#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscLayoutMapLocal/

**Contents:**
- PetscLayoutMapLocal#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Developer Note#
- See Also#
- Level#
- Location#

Maps a set of global indices to the subset owned locally by each MPI process according to a PetscLayout

map - the PetscLayout describing global ownership

N - the number of input indices

idxs - the global indices; negative entries are ignored

on - number of indices in the returned local set (may be NULL)

oidxs - the local (0-based) indices owned by this MPI process (may be NULL); caller must PetscFree()

ogidxs - the corresponding global indices in a compact numbering (may be NULL); caller must PetscFree()

Uses a PetscSF internally to route each input index to its owner and reduce with MPI_LOR, producing on each MPI process the sorted, deduplicated list of local indices for which at least one process supplied a matching global index.

PetscLayout, PetscSF, PetscLayoutFindOwner(), PetscSFCreateFromLayouts()

src/vec/is/sf/utils/sfutils.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLayout
```

Example 2 (unknown):
```unknown
#include "petscsf.h"   
PetscErrorCode PetscLayoutMapLocal(PetscLayout map, PetscInt N, const PetscInt idxs[], PetscInt *on, PetscInt *oidxs[], PetscInt *ogidxs[])
```

Example 3 (unknown):
```unknown
PetscLayout
```

Example 4 (unknown):
```unknown
PetscFree()
```

---

## PetscNvshmemFinalize#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscNvshmemFinalize/

**Contents:**
- PetscNvshmemFinalize#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#

Tear down NVSHMEM after PETSc is done using it

Called internally during PetscFinalize() if PETSc previously initialized NVSHMEM. Users normally do not need to call this directly.

PetscFinalize(), PetscSF

src/vec/is/sf/impls/basic/nvshmem/sfnvshmem.cu

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscNvshmemFinalize(void)
```

Example 2 (unknown):
```unknown
PetscFinalize()
```

Example 3 (unknown):
```unknown
PetscFinalize()
```

---

## PetscSFBackend#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFBackend/

**Contents:**
- PetscSFBackend#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Device backend used by a PetscSF to pack, unpack, and exchange data when doing device-aware communication

PETSCSF_BACKEND_INVALID - no backend has been selected (the default for a host-only SF)

PETSCSF_BACKEND_CUDA - use CUDA-aware pack/unpack and MPI

PETSCSF_BACKEND_HIP - use HIP-aware pack/unpack and MPI

PETSCSF_BACKEND_KOKKOS - use the Kokkos backend (which itself may dispatch to CUDA, HIP, or OpenMP)

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFLink, PetscSFDirection, PetscSFOperation

include/petscsftypes.h

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
/* When doing device-aware MPI, a backend refers to the SF/device interface */typedef enum {
  PETSCSF_BACKEND_INVALID = 0,
  PETSCSF_BACKEND_CUDA    = 1,
  PETSCSF_BACKEND_HIP     = 2,
  PETSCSF_BACKEND_KOKKOS  = 3
} PetscSFBackend;
```

Example 2 (unknown):
```unknown
PETSCSF_BACKEND_INVALID
```

Example 3 (unknown):
```unknown
PETSCSF_BACKEND_CUDA
```

Example 4 (unknown):
```unknown
PETSCSF_BACKEND_HIP
```

---

## PetscSFBcastBegin#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFBcastBegin/

**Contents:**
- PetscSFBcastBegin#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

begin pointwise broadcast with root value being reduced to leaf value, to be concluded with call to PetscSFBcastEnd()

sf - star forest on which to communicate

unit - data type associated with each node

rootdata - buffer to broadcast

op - operation to use for reduction

leafdata - buffer to be reduced with values from each leaf’s respective root

When PETSc is configured with device support, it will use PetscGetMemType() to determine whether the given data pointers are host pointers or device pointers, which may incur a noticeable cost. If you already knew the memory type, you should use PetscSFBcastWithMemTypeBegin() instead.

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFBcastEnd(), PetscSFBcastWithMemTypeBegin()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex2.c src/vec/is/sf/tutorials/ex1f.F90 src/ts/tutorials/ex30.c src/dm/impls/plex/tutorials/ex14.c src/dm/impls/plex/tutorials/ex14f90.F90 src/vec/is/sf/tutorials/ex3.c src/dm/impls/plex/tutorials/ex15.c src/vec/is/sf/tutorials/ex1.c

PetscSFBcastBegin_Allgather() in src/vec/is/sf/impls/basic/allgather/sfallgather.c PetscSFBcastBegin_Allgatherv() in src/vec/is/sf/impls/basic/allgatherv/sfallgatherv.c PetscSFBcastBegin_Basic() in src/vec/is/sf/impls/basic/sfbasic.c PetscSFBcastBegin_Window() in src/vec/is/sf/impls/window/sfwindow.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSFBcastEnd()
```

Example 2 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFBcastBegin(PetscSF sf, MPI_Datatype unit, const void *rootdata, void *leafdata, MPI_Op op)
```

Example 3 (unknown):
```unknown
PetscGetMemType()
```

Example 4 (unknown):
```unknown
PetscSFBcastWithMemTypeBegin()
```

---

## PetscSFBcastEnd#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFBcastEnd/

**Contents:**
- PetscSFBcastEnd#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

end a broadcast and reduce operation started with PetscSFBcastBegin() or PetscSFBcastWithMemTypeBegin()

rootdata - buffer to broadcast

op - operation to use for reduction

leafdata - buffer to be reduced with values from each leaf’s respective root

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFSetGraph(), PetscSFReduceEnd()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex2.c src/vec/is/sf/tutorials/ex1f.F90 src/ts/tutorials/ex30.c src/dm/impls/plex/tutorials/ex14.c src/dm/impls/plex/tutorials/ex14f90.F90 src/vec/is/sf/tutorials/ex3.c src/dm/impls/plex/tutorials/ex15.c src/vec/is/sf/tutorials/ex1.c

PetscSFBcastEnd_Basic() in src/vec/is/sf/impls/basic/sfbasic.c PetscSFBcastEnd_Window() in src/vec/is/sf/impls/window/sfwindow.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSFBcastBegin()
```

Example 2 (unknown):
```unknown
PetscSFBcastWithMemTypeBegin()
```

Example 3 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFBcastEnd(PetscSF sf, MPI_Datatype unit, const void *rootdata, void *leafdata, MPI_Op op)
```

Example 4 (unknown):
```unknown
PetscSFSetGraph()
```

---

## PetscSFBcastWithMemTypeBegin#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFBcastWithMemTypeBegin/

**Contents:**
- PetscSFBcastWithMemTypeBegin#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

begin pointwise broadcast with root value being reduced to leaf value with explicit memory types, to be concluded with call to PetscSFBcastEnd()

sf - star forest on which to communicate

unit - data type associated with each node

rootmtype - memory type of rootdata

rootdata - buffer to broadcast

leafmtype - memory type of leafdata

op - operation to use for reduction

leafdata - buffer to be reduced with values from each leaf’s respective root

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFBcastEnd(), PetscSFBcastBegin()

src/vec/is/sf/interface/sf.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSFBcastEnd()
```

Example 2 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFBcastWithMemTypeBegin(PetscSF sf, MPI_Datatype unit, PetscMemType rootmtype, const void *rootdata, PetscMemType leafmtype, void *leafdata, MPI_Op op)
```

Example 3 (unknown):
```unknown
PetscSFBcastEnd()
```

Example 4 (unknown):
```unknown
PetscSFBcastBegin()
```

---

## PetscSFComposeInverse#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFComposeInverse/

**Contents:**
- PetscSFComposeInverse#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Compose a new PetscSF by putting the inverse of the second PetscSF under the first one

sfA - The first PetscSF

sfB - The second PetscSF

sfBA - The composite PetscSF.

Currently, the two PetscSFs must be defined on congruent communicators and they must be true star forests, i.e. the same leaf is not connected with different roots. Even more, all roots of the second PetscSF must have a degree of 1, i.e., no roots have more than one leaf connected.

sfA’s leaf space and sfB’s leaf space might be partially overlapped. The composition builds a graph with sfA’s roots and sfB’s roots only when there is a path between them. Unconnected roots are not in sfBA. Doing a PetscSFBcastBegin() and PetscSFBcastEnd() on the new PetscSF is equivalent to doing a PetscSFBcastBegin() and PetscSFBcastEnd() on sfA, then a PetscSFReduceBegin() and PetscSFReduceEnd() on sfB, on connected roots.

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFCompose(), PetscSFGetGraph(), PetscSFSetGraph(), PetscSFCreateInverseSF()

src/vec/is/sf/interface/sf.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFComposeInverse(PetscSF sfA, PetscSF sfB, PetscSF *sfBA)
```

Example 2 (unknown):
```unknown
PetscSFBcastBegin()
```

Example 3 (unknown):
```unknown
PetscSFBcastEnd()
```

Example 4 (unknown):
```unknown
PetscSFBcastBegin()
```

---

## PetscSFCompose#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFCompose/

**Contents:**
- PetscSFCompose#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Compose a new PetscSF by putting the second PetscSF under the first one in a top (roots) down (leaves) view

sfA - The first PetscSF

sfB - The second PetscSF

sfBA - The composite PetscSF

Currently, the two PetscSFs must be defined on congruent communicators and they must be true star forests, i.e. the same leaf is not connected with different roots.

sfA’s leaf space and sfB’s root space might be partially overlapped. The composition builds a graph with sfA’s roots and sfB’s leaves only when there is a path between them. Unconnected nodes (roots or leaves) are not in sfBA. Doing a PetscSFBcastBegin() and PetscSFBcastEnd() on the new PetscSF is equivalent to doing a PetscSFBcastBegin() and PetscSFBcastEnd() on sfA, then a PetscSFBcastBegin() and PetscSFBcastEnd() on sfB, on connected nodes.

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFComposeInverse(), PetscSFGetGraph(), PetscSFSetGraph()

src/vec/is/sf/interface/sf.c

src/ts/tutorials/ex30.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFCompose(PetscSF sfA, PetscSF sfB, PetscSF *sfBA)
```

Example 2 (unknown):
```unknown
PetscSFBcastBegin()
```

Example 3 (unknown):
```unknown
PetscSFBcastEnd()
```

Example 4 (unknown):
```unknown
PetscSFBcastBegin()
```

---

## PetscSFComputeDegreeBegin#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFComputeDegreeBegin/

**Contents:**
- PetscSFComputeDegreeBegin#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

begin computation of the degree of each root vertex, to be completed with PetscSFComputeDegreeEnd()

degree - degree (the number of leaves) of each root vertex

The returned array is owned by PetscSF and automatically freed by PetscSFDestroy(). Hence there is no need to call PetscFree() on it.

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFGatherBegin(), PetscSFComputeDegreeEnd()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex1.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSFComputeDegreeEnd()
```

Example 2 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFComputeDegreeBegin(PetscSF sf, const PetscInt *degree[])
```

Example 3 (unknown):
```unknown
PetscSFDestroy()
```

Example 4 (unknown):
```unknown
PetscFree()
```

---

## PetscSFComputeDegreeEnd#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFComputeDegreeEnd/

**Contents:**
- PetscSFComputeDegreeEnd#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

complete computation of degree for each root vertex, started with PetscSFComputeDegreeBegin()

degree - degree of each root vertex

The returned array is owned by PetscSF and automatically freed by PetscSFDestroy(). Hence there is no need to call PetscFree() on it.

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFGatherBegin(), PetscSFComputeDegreeBegin()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex1.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSFComputeDegreeBegin()
```

Example 2 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFComputeDegreeEnd(PetscSF sf, const PetscInt *degree[])
```

Example 3 (unknown):
```unknown
PetscSFDestroy()
```

Example 4 (unknown):
```unknown
PetscFree()
```

---

## PetscSFComputeMultiRootOriginalNumbering#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFComputeMultiRootOriginalNumbering/

**Contents:**
- PetscSFComputeMultiRootOriginalNumbering#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Returns original numbering of multi-roots (roots of multi-PetscSF returned by PetscSFGetMultiSF()). Each multi-root is assigned index of the corresponding original root.

degree - degree of each root vertex, computed with PetscSFComputeDegreeBegin() and PetscSFComputeDegreeEnd()

nMultiRoots - (optional) number of multi-roots (roots of multi-PetscSF)

multiRootsOrigNumbering - original indices of multi-roots; length of this array is nMultiRoots

The returned array multiRootsOrigNumbering should be destroyed with PetscFree() when no longer needed.

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFComputeDegreeBegin(), PetscSFComputeDegreeEnd(), PetscSFGetMultiSF()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex1.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSFGetMultiSF()
```

Example 2 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFComputeMultiRootOriginalNumbering(PetscSF sf, const PetscInt degree[], PetscInt *nMultiRoots, PetscInt *multiRootsOrigNumbering[])
```

Example 3 (unknown):
```unknown
PetscSFComputeDegreeBegin()
```

Example 4 (unknown):
```unknown
PetscSFComputeDegreeEnd()
```

---

## PetscSFConcatenateRootMode#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFConcatenateRootMode/

**Contents:**
- PetscSFConcatenateRootMode#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Modes of root concatenation when concatenating PetscSFs

PETSCSF_CONCATENATE_ROOTMODE_LOCAL - concatenate root spaces locally (separately on each rank)

PETSCSF_CONCATENATE_ROOTMODE_SHARED - do not concatenate roots; root space is considered the same for each input PetscSF (checked in debug mode)

PETSCSF_CONCATENATE_ROOTMODE_GLOBAL - concatenate root spaces globally

PetscSF, PetscSFConcatenate()

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  PETSCSF_CONCATENATE_ROOTMODE_LOCAL,
  PETSCSF_CONCATENATE_ROOTMODE_SHARED,
  PETSCSF_CONCATENATE_ROOTMODE_GLOBAL,
} PetscSFConcatenateRootMode;
```

Example 2 (unknown):
```unknown
PETSCSF_CONCATENATE_ROOTMODE_LOCAL
```

Example 3 (unknown):
```unknown
PETSCSF_CONCATENATE_ROOTMODE_SHARED
```

Example 4 (unknown):
```unknown
PETSCSF_CONCATENATE_ROOTMODE_GLOBAL
```

---

## PetscSFConcatenate#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFConcatenate/

**Contents:**
- PetscSFConcatenate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- Example#
- See Also#
- Level#
- Location#

concatenate multiple PetscSF into a new PetscSF

comm - the communicator

nsfs - the number of input PetscSF

sfs - the array of input PetscSF

rootMode - the root mode specifying how roots are handled

leafOffsets - the array of local leaf offsets, one for each input PetscSF, or NULL for contiguous storage

newsf - The resulting PetscSF

The communicator of all PetscSFs in sfs must be comm.

Leaves are always concatenated locally, keeping them ordered by the input PetscSF index and original local order.

The offsets in leafOffsets are added to the original leaf indices.

If all input PetscSFs use contiguous leaf storage (ilocal = NULL), leafOffsets can be passed as NULL as well. In this case, NULL is also passed as ilocal to the resulting PetscSF.

If any input PetscSF has non-null ilocal, leafOffsets is needed to distinguish leaves from different input PetscSFs. In this case, user is responsible to provide correct offsets so that the resulting leaves are unique (otherwise an error occurs).

All root modes retain the essential connectivity condition.

If two leaves of the same input PetscSF are connected (sharing the same root), they are also connected in the output PetscSF.

Parameter rootMode controls how the input root spaces are combined. For PETSCSF_CONCATENATE_ROOTMODE_SHARED, the root space is considered the same for each input PetscSF (checked in debug mode) and is also the same in the output PetscSF.

For PETSCSF_CONCATENATE_ROOTMODE_LOCAL and PETSCSF_CONCATENATE_ROOTMODE_GLOBAL, the input root spaces are taken as separate and joined. PETSCSF_CONCATENATE_ROOTMODE_LOCAL joins the root spaces locally; roots of sfs[0], sfs[1], sfs[2], … are joined on each MPI process separately, ordered by input PetscSF and original local index, and renumbered contiguously. PETSCSF_CONCATENATE_ROOTMODE_GLOBAL joins the root spaces globally; roots of sfs[0], sfs[1], sfs[2], … are joined globally, ordered by input PetscSF index and original global index, and renumbered contiguously; the original root MPI processes are ignored. For both PETSCSF_CONCATENATE_ROOTMODE_LOCAL and PETSCSF_CONCATENATE_ROOTMODE_GLOBAL, the output PetscSF’s root layout is such that the local number of roots is a sum of the input PetscSF’s local numbers of roots on each MPI process to keep the load balancing. However, for PETSCSF_CONCATENATE_ROOTMODE_GLOBAL, roots can move to different MPI processes.

We can use src/vec/is/sf/tests/ex18.c to compare the root modes. By running

we generate two identical PetscSFs sf_0 and sf_1,

and pass them to PetscSFConcatenate() along with different choices of rootMode, yielding different result_sf:

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFCompose(), PetscSFGetGraph(), PetscSFSetGraph(), PetscSFConcatenateRootMode

src/vec/is/sf/interface/sf.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFConcatenate(MPI_Comm comm, PetscInt nsfs, PetscSF sfs[], PetscSFConcatenateRootMode rootMode, PetscInt leafOffsets[], PetscSF *newsf)
```

Example 2 (unknown):
```unknown
leafOffsets
```

Example 3 (unknown):
```unknown
leafOffsets
```

Example 4 (unknown):
```unknown
leafOffsets
```

---

## PetscSFCreateByMatchingIndices#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFCreateByMatchingIndices/

**Contents:**
- PetscSFCreateByMatchingIndices#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Example 1#
- Example 2#
- Example 3#
- Notes#
- Developer Notes#
- See Also#

Create PetscSF by matching root and leaf indices

layout - PetscLayout defining the global index space and the MPI rank that brokers each index

numRootIndices - size of rootIndices

rootIndices - array of global indices of which this process requests ownership

rootLocalIndices - root local index permutation (NULL if no permutation)

rootLocalOffset - offset to be added to rootLocalIndices

numLeafIndices - size of leafIndices

leafIndices - array of global indices with which this process requires data associated

leafLocalIndices - leaf local index permutation (NULL if no permutation)

leafLocalOffset - offset to be added to leafLocalIndices

sfA - star forest representing the communication pattern from the layout space to the leaf space (NULL if not needed)

sf - star forest representing the communication pattern from the root space to the leaf space

layout represents any partitioning of [0, N), where N is the total number of global indices, and its local size can be set to PETSC_DECIDE.

If a global index x lies in the partition owned by process i, each process whose rootIndices contains x requests ownership of x and sends its own rank and the local index of x to process i. If multiple processes request ownership of x, the one with the highest rank is to own x. Process i then broadcasts the ownership information, so that each process whose leafIndices contains x knows the ownership information of x. The output sf is constructed by associating each leaf point to a root point in this way.

Suppose there is point data ordered according to the global indices and partitioned according to the given layout. The optional output sfA can be used to push such data to leaf points.

All indices in rootIndices and leafIndices must lie in the layout range. The union (over all processes) of rootIndices must cover that of leafIndices, but need not cover the entire layout.

If (leafIndices, leafLocalIndices, leafLocalOffset) == (rootIndices, rootLocalIndices, rootLocalOffset), the output star forest is almost identity, so will only include non-trivial part of the map.

Current approach of a process of the highest rank gaining the ownership may cause load imbalance; consider using hash(rank, root_local_index) as the bid for the ownership determination.

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFCreate()

src/vec/is/sf/utils/sfutils.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h"   
PetscErrorCode PetscSFCreateByMatchingIndices(PetscLayout layout, PetscInt numRootIndices, const PetscInt rootIndices[], const PetscInt rootLocalIndices[], PetscInt rootLocalOffset, PetscInt numLeafIndices, const PetscInt leafIndices[], const PetscInt leafLocalIndices[], PetscInt leafLocalOffset, PetscSF *sfA, PetscSF *sf)
```

Example 2 (unknown):
```unknown
PetscLayout
```

Example 3 (unknown):
```unknown
rootIndices
```

Example 4 (unknown):
```unknown
rootLocalIndices
```

---

## PetscSFCreateEmbeddedLeafSF#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFCreateEmbeddedLeafSF/

**Contents:**
- PetscSFCreateEmbeddedLeafSF#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

removes edges from all but the selected leaves of a PetscSF, does not remap indices

sf - original star forest

nselected - number of selected leaves on this MPI process

selected - indices of the selected leaves on this MPI process

newsf - new star forest

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFCreateEmbeddedRootSF(), PetscSFSetGraph(), PetscSFGetGraph()

src/vec/is/sf/interface/sf.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFCreateEmbeddedLeafSF(PetscSF sf, PetscInt nselected, const PetscInt selected[], PetscSF *newsf)
```

Example 2 (unknown):
```unknown
PetscSFCreateEmbeddedRootSF()
```

Example 3 (unknown):
```unknown
PetscSFSetGraph()
```

Example 4 (unknown):
```unknown
PetscSFGetGraph()
```

---

## PetscSFCreateEmbeddedRootSF#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFCreateEmbeddedRootSF/

**Contents:**
- PetscSFCreateEmbeddedRootSF#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

removes edges from all but the selected roots of a PetscSF, does not remap indices

sf - original star forest

nselected - number of selected roots on this MPI process

selected - indices of the selected roots on this MPI process

esf - new star forest

To use the new PetscSF, it may be necessary to know the indices of the leaves that are still participating. This can be done by calling PetscSFGetGraph().

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFSetGraph(), PetscSFGetGraph()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex1.c

PetscSFCreateEmbeddedRootSF_Alltoall() in src/vec/is/sf/impls/basic/alltoall/sfalltoall.c PetscSFCreateEmbeddedRootSF_Basic() in src/vec/is/sf/impls/basic/sfbasic.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFCreateEmbeddedRootSF(PetscSF sf, PetscInt nselected, const PetscInt selected[], PetscSF *esf)
```

Example 2 (unknown):
```unknown
PetscSFSetGraph()
```

Example 3 (unknown):
```unknown
PetscSFGetGraph()
```

---

## PetscSFCreateFromLayouts#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFCreateFromLayouts/

**Contents:**
- PetscSFCreateFromLayouts#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a parallel star forest mapping between two PetscLayout objects

rmap - PetscLayout defining the global root space

lmap - PetscLayout defining the global leaf space

sf - The parallel star forest

If the global length of lmap differs from the global length of rmap then the excess entries are ignored.

The resulting sf used with PetscSFBcastBegin() and PetscSFBcastEnd() merely copies the array entries of rootdata to leafdata; moving them between MPI processes if needed. For example, if rmap is [0, 3, 5) and lmap is [0, 2, 6) and rootdata is (1, 2, 3) on MPI rank 0 and (4, 5) on MPI rank 1 then the leafdata would become (1, 2) on MPI rank 0 and (3, 4, 5, x) on MPI rank 1.

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscLayout, PetscSFCreate(), PetscSFSetGraph(), PetscLayoutCreate(), PetscSFSetGraphLayout()

src/vec/is/sf/utils/sfutils.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLayout
```

Example 2 (unknown):
```unknown
#include "petscsf.h"   
PetscErrorCode PetscSFCreateFromLayouts(PetscLayout rmap, PetscLayout lmap, PetscSF *sf)
```

Example 3 (unknown):
```unknown
PetscLayout
```

Example 4 (unknown):
```unknown
PetscLayout
```

---

## PetscSFCreateInverseSF#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFCreateInverseSF/

**Contents:**
- PetscSFCreateInverseSF#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

given a PetscSF in which all roots have degree 1 (exactly one leaf), creates the inverse map

sf - star forest to invert

All roots must have degree 1.

The local space may be a permutation, but cannot be sparse.

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFType, PetscSFSetGraph()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex1.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFCreateInverseSF(PetscSF sf, PetscSF *isf)
```

Example 2 (unknown):
```unknown
PetscSFType
```

Example 3 (unknown):
```unknown
PetscSFSetGraph()
```

---

## PetscSFCreateRemoteOffsets#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFCreateRemoteOffsets/

**Contents:**
- PetscSFCreateRemoteOffsets#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Create offsets for point data on remote processes

rootSection - Data layout of remote points for outgoing data (this is layout for roots)

leafSection - Data layout of local points for incoming data (this is layout for leaves)

remoteOffsets - Offsets for point data on remote processes (these are offsets from the root section), or NULL

Caller must PetscFree() remoteOffsets if it was requested

Use PetscSFDestroyRemoteOffsets() when remoteOffsets is no longer needed.

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFCreate()

src/vec/is/sf/utils/sfutils.c

src/dm/impls/plex/tutorials/ex14.c src/dm/impls/plex/tutorials/ex14f90.F90

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h"   
PetscErrorCode PetscSFCreateRemoteOffsets(PetscSF sf, PetscSection rootSection, PetscSection leafSection, PetscInt *remoteOffsets[])
```

Example 2 (unknown):
```unknown
PetscFree()
```

Example 3 (unknown):
```unknown
remoteOffsets
```

Example 4 (unknown):
```unknown
PetscSFDestroyRemoteOffsets()
```

---

## PetscSFCreateSectionSF#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFCreateSectionSF/

**Contents:**
- PetscSFCreateSectionSF#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Create an expanded PetscSF of dofs, assuming the input PetscSF relates points

rootSection - Data layout of remote points for outgoing data (this is usually the serial section)

remoteOffsets - Offsets for point data on remote processes (these are offsets from the root section), or NULL

leafSection - Data layout of local points for incoming data (this is the distributed section)

sectionSF - The new PetscSF

remoteOffsets can be NULL if sf does not reference any points in leafSection

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFCreate(), PetscSFDistributeSection()

src/vec/is/sf/utils/sfutils.c

src/dm/impls/plex/tutorials/ex14.c src/dm/impls/plex/tutorials/ex14f90.F90

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h"   
PetscErrorCode PetscSFCreateSectionSF(PetscSF sf, PetscSection rootSection, PetscInt remoteOffsets[], PetscSection leafSection, PetscSF *sectionSF)
```

Example 2 (unknown):
```unknown
remoteOffsets
```

Example 3 (unknown):
```unknown
leafSection
```

Example 4 (unknown):
```unknown
PetscSFCreate()
```

---

## PetscSFCreateStridedSF#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFCreateStridedSF/

**Contents:**
- PetscSFCreateStridedSF#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#

Create an PetscSF to communicate interleaved blocks of data

ldr - leading dimension of root space

ldl - leading dimension of leaf space

vsf - the new PetscSF

This can be useful to perform communications on multiple right-hand sides stored in a Fortran-style two dimensional array. For example, the calling sequence

Should this functionality be handled with a new API instead of creating a new object?

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFCreate(), PetscSFSetGraph()

src/vec/is/sf/utils/sfutils.c

src/vec/is/sf/tutorials/ex1.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h"   
PetscErrorCode PetscSFCreateStridedSF(PetscSF sf, PetscInt bs, PetscInt ldr, PetscInt ldl, PetscSF *vsf)
```

Example 2 (bash):
```bash
c_datatype *roots, *leaves;
  for i in [0,bs) do
    PetscSFBcastBegin(sf, mpi_datatype, roots + i*ldr, leaves + i*ldl, op)
    PetscSFBcastEnd(sf, mpi_datatype, roots + i*ldr, leaves + i*ldl, op)
```

Example 3 (unknown):
```unknown
c_datatype *roots, *leaves;
  PetscSFCreateStridedSF(sf, bs, ldr, ldl, &vsf)
  PetscSFBcastBegin(vsf, mpi_datatype, roots, leaves, op)
  PetscSFBcastEnd(vsf, mpi_datatype, roots, leaves, op)
```

Example 4 (unknown):
```unknown
PetscSFCreate()
```

---

## PetscSFCreate#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFCreate/

**Contents:**
- PetscSFCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#
- Examples#

create a star forest communication context

comm - communicator on which the star forest will operate

sf - new star forest context

-sf_type (basic|window|neighbor) - Use MPI persistent Isend/Irecv, or MPI-3 one-sided window, or MPI-3 neighborhood collectives for communication

-sf_neighbor_persistent (true|false) - Use MPI-4 persistent neighborhood collectives for communication (used along with -sf_type neighbor)

When one knows the communication graph is one of the predefined graph, such as MPI_Alltoall(), MPI_Allgatherv(), MPI_Gatherv(), one can create a PetscSF and then set its graph with PetscSFSetGraphWithPattern(). These special PetscSFs are optimized and have better performance than the general PetscSFs.

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFSetType, PetscSFSetGraph(), PetscSFSetGraphWithPattern(), PetscSFDestroy()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex2.c src/vec/is/sf/tutorials/ex1f.F90 src/vec/is/sf/tutorials/ex3.c src/dm/impls/plex/tutorials/ex15.c src/vec/is/sf/tutorials/ex1.c

PetscSFCreate_Allgather() in src/vec/is/sf/impls/basic/allgather/sfallgather.c PetscSFCreate_Allgatherv() in src/vec/is/sf/impls/basic/allgatherv/sfallgatherv.c PetscSFCreate_Alltoall() in src/vec/is/sf/impls/basic/alltoall/sfalltoall.c PetscSFCreate_Gather() in src/vec/is/sf/impls/basic/gather/sfgather.c PetscSFCreate_Gatherv() in src/vec/is/sf/impls/basic/gatherv/sfgatherv.c PetscSFCreate_Neighbor() in src/vec/is/sf/impls/basic/neighbor/sfneighbor.c PetscSFCreate_Basic() in src/vec/is/sf/impls/basic/sfbasic.c PetscSFCreate_Window() in src/vec/is/sf/impls/window/sfwindow.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFCreate(MPI_Comm comm, PetscSF *sf)
```

Example 2 (unknown):
```unknown
-sf_type neighbor
```

Example 3 (unknown):
```unknown
MPI_Alltoall()
```

Example 4 (unknown):
```unknown
MPI_Allgatherv()
```

---

## PetscSFDeregisterPersistent#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFDeregisterPersistent/

**Contents:**
- PetscSFDeregisterPersistent#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Signal that repeated usage of rootdata and leafdata for PetscSF communication has concluded.

unit - the data type contained within the rootdata and leafdata

rootdata - root data that was previously registered with PetscSFRegisterPersistent()

leafdata - leaf data that was previously registered with PetscSFRegisterPersistent()

See PetscSFRegisterPersistent() for when and how to use this function.

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PETSCSFWINDOW, PetscSFRegisterPersistent()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex1.c src/vec/is/sf/tutorials/ex3.c

PetscSFDeregisterPersistent_Window() in src/vec/is/sf/impls/window/sfwindow.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFDeregisterPersistent(PetscSF sf, MPI_Datatype unit, const void *rootdata, const void *leafdata)
```

Example 2 (unknown):
```unknown
PetscSFRegisterPersistent()
```

Example 3 (unknown):
```unknown
PetscSFRegisterPersistent()
```

Example 4 (unknown):
```unknown
PetscSFRegisterPersistent()
```

---

## PetscSFDestroy#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFDestroy/

**Contents:**
- PetscSFDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

destroy a star forest

sf - address of star forest

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFType, PetscSFCreate(), PetscSFReset()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex2.c src/dm/tutorials/ex25.c src/vec/is/sf/tutorials/ex1f.F90 src/ts/tutorials/ex30.c src/dm/impls/plex/tutorials/ex14.c src/dm/impls/plex/tutorials/ex14f90.F90 src/vec/is/sf/tutorials/ex3.c src/dm/impls/plex/tutorials/ex15.c src/vec/is/sf/tutorials/ex1.c

PetscSFDestroy_Allgatherv() in src/vec/is/sf/impls/basic/allgatherv/sfallgatherv.c PetscSFDestroy_Neighbor() in src/vec/is/sf/impls/basic/neighbor/sfneighbor.c PetscSFDestroy_Basic() in src/vec/is/sf/impls/basic/sfbasic.c PetscSFDestroy_Window() in src/vec/is/sf/impls/window/sfwindow.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFDestroy(PetscSF *sf)
```

Example 2 (unknown):
```unknown
PetscSFType
```

Example 3 (unknown):
```unknown
PetscSFCreate()
```

Example 4 (unknown):
```unknown
PetscSFReset()
```

---

## PetscSFDirection#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFDirection/

**Contents:**
- PetscSFDirection#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Direction in which a PetscSF communication is performed

PETSCSF_ROOT2LEAF - data flows from roots to leaves (broadcast direction)

PETSCSF_LEAF2ROOT - data flows from leaves to roots (reduce/fetch direction)

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFOperation, PetscSFBcastBegin(), PetscSFReduceBegin()

include/petscsftypes.h

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  PETSCSF_ROOT2LEAF = 0,
  PETSCSF_LEAF2ROOT = 1
} PetscSFDirection;
```

Example 2 (unknown):
```unknown
PETSCSF_ROOT2LEAF
```

Example 3 (unknown):
```unknown
PETSCSF_LEAF2ROOT
```

Example 4 (unknown):
```unknown
PetscSFOperation
```

---

## PetscSFDistributeSection#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFDistributeSection/

**Contents:**
- PetscSFDistributeSection#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- Fortran Note#
- See Also#
- Level#
- Location#

Create a new PetscSection reorganized, moving from the root to the leaves of the PetscSF

rootSection - Section defined on root space

remoteOffsets - root offsets in leaf storage, or NULL, its length will be the size of the chart of leafSection

leafSection - Section defined on the leaf space

Caller must PetscFree() remoteOffsets if it was requested

To distribute data from the rootSection to the leafSection, see PetscSFCreateSectionSF() or PetscSectionMigrateData().

Use PetscSFDestroyRemoteOffsets() when remoteOffsets is no longer needed.

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFCreate(), PetscSFCreateSectionSF()

src/vec/is/sf/utils/sfutils.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsf.h"   
PetscErrorCode PetscSFDistributeSection(PetscSF sf, PetscSection rootSection, PetscInt *remoteOffsets[], PetscSection leafSection)
```

Example 3 (unknown):
```unknown
leafSection
```

Example 4 (unknown):
```unknown
PetscFree()
```

---

## PetscSFDuplicateOption#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFDuplicateOption/

**Contents:**
- PetscSFDuplicateOption#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Aspects to preserve when duplicating a PetscSF

PETSCSF_DUPLICATE_CONFONLY - configuration only, user must call PetscSFSetGraph()

PETSCSF_DUPLICATE_RANKS - communication ranks preserved, but different graph (allows simpler setup after calling PetscSFSetGraph())

PETSCSF_DUPLICATE_GRAPH - entire graph duplicated

PetscSF, PetscSFDuplicate()

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  PETSCSF_DUPLICATE_CONFONLY,
  PETSCSF_DUPLICATE_RANKS,
  PETSCSF_DUPLICATE_GRAPH
} PetscSFDuplicateOption;
```

Example 2 (unknown):
```unknown
PETSCSF_DUPLICATE_CONFONLY
```

Example 3 (unknown):
```unknown
PetscSFSetGraph()
```

Example 4 (unknown):
```unknown
PETSCSF_DUPLICATE_RANKS
```

---

## PetscSFDuplicate#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFDuplicate/

**Contents:**
- PetscSFDuplicate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

duplicate a PetscSF, optionally preserving rank connectivity and graph

sf - communication object to duplicate

opt - PETSCSF_DUPLICATE_CONFONLY, PETSCSF_DUPLICATE_RANKS, or PETSCSF_DUPLICATE_GRAPH (see PetscSFDuplicateOption)

newsf - new communication object

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFType, PetscSFCreate(), PetscSFSetType(), PetscSFSetGraph()

src/vec/is/sf/interface/sf.c

PetscSFDuplicate_Window() in src/vec/is/sf/impls/window/sfwindow.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFDuplicate(PetscSF sf, PetscSFDuplicateOption opt, PetscSF *newsf)
```

Example 2 (unknown):
```unknown
PETSCSF_DUPLICATE_CONFONLY
```

Example 3 (unknown):
```unknown
PETSCSF_DUPLICATE_RANKS
```

Example 4 (unknown):
```unknown
PETSCSF_DUPLICATE_GRAPH
```

---

## PetscSFFetchAndOpBegin#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFFetchAndOpBegin/

**Contents:**
- PetscSFFetchAndOpBegin#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

begin operation that fetches values from rootdata and updates it atomically by applying operation using leafdata, to be completed with PetscSFFetchAndOpEnd()

leafdata - leaf values to use in reduction

op - operation to use for reduction

rootdata - root values to be updated, input state is seen by first process to perform an update

leafupdate - state at each leaf’s respective root immediately prior to atomic update

The update is only atomic at the granularity provided by the hardware. Different roots referenced by the same process might be updated in a different order. Furthermore, if a composite type is used for the unit datatype, atomicity is not guaranteed across the whole vertex. Therefore, this function is mostly only used with primitive types such as integers.

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFComputeDegreeBegin(), PetscSFReduceBegin(), PetscSFSetGraph()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex1.c

PetscSFFetchAndOpBegin_Allgatherv() in src/vec/is/sf/impls/basic/allgatherv/sfallgatherv.c PetscSFFetchAndOpBegin_Gatherv() in src/vec/is/sf/impls/basic/gatherv/sfgatherv.c PetscSFFetchAndOpBegin_Basic() in src/vec/is/sf/impls/basic/sfbasic.c PetscSFFetchAndOpBegin_Window() in src/vec/is/sf/impls/window/sfwindow.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSFFetchAndOpEnd()
```

Example 2 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFFetchAndOpBegin(PetscSF sf, MPI_Datatype unit, void *rootdata, const void *leafdata, void *leafupdate, MPI_Op op)
```

Example 3 (unknown):
```unknown
PetscSFComputeDegreeBegin()
```

Example 4 (unknown):
```unknown
PetscSFReduceBegin()
```

---

## PetscSFFetchAndOpEnd#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFFetchAndOpEnd/

**Contents:**
- PetscSFFetchAndOpEnd#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

end operation started in matching call to PetscSFFetchAndOpBegin() or PetscSFFetchAndOpWithMemTypeBegin() to fetch values from roots and update atomically by applying operation using leafdata

leafdata - leaf values to use in reduction

op - operation to use for reduction

rootdata - root values to be updated, input state is seen by first process to perform an update

leafupdate - state at each leaf’s respective root immediately prior to atomic update

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFComputeDegreeEnd(), PetscSFReduceEnd(), PetscSFSetGraph(), PetscSFFetchAndOpBegin(), PetscSFFetchAndOpWithMemTypeBegin()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex1.c

PetscSFFetchAndOpEnd_Allgatherv() in src/vec/is/sf/impls/basic/allgatherv/sfallgatherv.c PetscSFFetchAndOpEnd_Basic() in src/vec/is/sf/impls/basic/sfbasic.c PetscSFFetchAndOpEnd_Window() in src/vec/is/sf/impls/window/sfwindow.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSFFetchAndOpBegin()
```

Example 2 (unknown):
```unknown
PetscSFFetchAndOpWithMemTypeBegin()
```

Example 3 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFFetchAndOpEnd(PetscSF sf, MPI_Datatype unit, void *rootdata, const void *leafdata, void *leafupdate, MPI_Op op)
```

Example 4 (unknown):
```unknown
PetscSFComputeDegreeEnd()
```

---

## PetscSFFetchAndOpWithMemTypeBegin#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFFetchAndOpWithMemTypeBegin/

**Contents:**
- PetscSFFetchAndOpWithMemTypeBegin#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

begin operation with explicit memory types that fetches values from root and updates atomically by applying operation using leafdata, to be completed with PetscSFFetchAndOpEnd()

rootmtype - memory type of rootdata

leafmtype - memory type of leafdata

leafdata - leaf values to use in reduction

leafupdatemtype - memory type of leafupdate

op - operation to use for reduction

rootdata - root values to be updated, input state is seen by first process to perform an update

leafupdate - state at each leaf’s respective root immediately prior to atomic update

See PetscSFFetchAndOpBegin() for more details.

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFFetchAndOpBegin(), PetscSFComputeDegreeBegin(), PetscSFReduceBegin(), PetscSFSetGraph(), PetscSFFetchAndOpEnd()

src/vec/is/sf/interface/sf.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSFFetchAndOpEnd()
```

Example 2 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFFetchAndOpWithMemTypeBegin(PetscSF sf, MPI_Datatype unit, PetscMemType rootmtype, void *rootdata, PetscMemType leafmtype, const void *leafdata, PetscMemType leafupdatemtype, void *leafupdate, MPI_Op op)
```

Example 3 (unknown):
```unknown
PetscSFFetchAndOpBegin()
```

Example 4 (unknown):
```unknown
PetscSFFetchAndOpBegin()
```

---

## PetscSFFinalizePackage#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFFinalizePackage/

**Contents:**
- PetscSFFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

Finalize PetscSF package, it is called from PetscFinalize()

PetscSF, PetscSFInitializePackage()

src/vec/is/sf/interface/dlregissf.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscSFFinalizePackage(void)
```

Example 3 (unknown):
```unknown
PetscSFInitializePackage()
```

---

## PetscSFGatherBegin#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFGatherBegin/

**Contents:**
- PetscSFGatherBegin#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

begin pointwise gather of all leaves into multi-roots, to be completed with PetscSFGatherEnd()

leafdata - leaf data to gather to roots

multirootdata - root buffer to gather into, amount of space per root is equal to its degree (which is the number of leaves that root has)

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFComputeDegreeBegin(), PetscSFScatterBegin()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex1.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSFGatherEnd()
```

Example 2 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFGatherBegin(PetscSF sf, MPI_Datatype unit, const void *leafdata, void *multirootdata)
```

Example 3 (unknown):
```unknown
PetscSFComputeDegreeBegin()
```

Example 4 (unknown):
```unknown
PetscSFScatterBegin()
```

---

## PetscSFGatherEnd#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFGatherEnd/

**Contents:**
- PetscSFGatherEnd#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

ends pointwise gather operation that was started with PetscSFGatherBegin()

leafdata - leaf data to gather to roots

multirootdata - root buffer to gather into, amount of space per root is equal to its degree (which is the number of leaves that root has)

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFComputeDegreeEnd(), PetscSFScatterEnd()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex1.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSFGatherBegin()
```

Example 2 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFGatherEnd(PetscSF sf, MPI_Datatype unit, const void *leafdata, void *multirootdata)
```

Example 3 (unknown):
```unknown
PetscSFComputeDegreeEnd()
```

Example 4 (unknown):
```unknown
PetscSFScatterEnd()
```

---

## PetscSFGetGraphLayout#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFGetGraphLayout/

**Contents:**
- PetscSFGetGraphLayout#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Get the global indices and PetscLayout that describe a PetscSF

layout - PetscLayout defining the global space for roots

nleaves - number of leaf vertices on the current process, each of these references a root on any process

ilocal - locations of leaves in leafdata buffers, or NULL for contiguous storage

gremote - root vertices in global numbering corresponding to the leaves

The outputs are such that passing them as inputs to PetscSFSetGraphLayout() would lead to the same star forest. The outputs layout and gremote are freshly created each time this function is called, so they need to be freed (with PetscLayoutDestroy() and PetscFree()) by the user.

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFSetGraphLayout(), PetscSFCreate(), PetscSFView(), PetscSFSetGraph(), PetscSFGetGraph()

src/vec/is/sf/utils/sfutils.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLayout
```

Example 2 (unknown):
```unknown
#include "petscsf.h"   
PetscErrorCode PetscSFGetGraphLayout(PetscSF sf, PetscLayout *layout, PetscInt *nleaves, const PetscInt *ilocal[], PetscInt *gremote[])
```

Example 3 (unknown):
```unknown
PetscLayout
```

Example 4 (unknown):
```unknown
PetscSFSetGraphLayout()
```

---

## PetscSFGetGraph#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFGetGraph/

**Contents:**
- PetscSFGetGraph#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Get the graph specifying a parallel star forest

nroots - number of root vertices on the current process (these are possible targets for other MPI process to attach leaves)

nleaves - number of leaf vertices on the current process, each of these references a root on any MPI process

ilocal - locations of leaves in leafdata buffers (if returned value is NULL, it means leaves are in contiguous storage)

iremote - remote locations of root vertices for each leaf on the current process

We are not currently requiring that the graph is set, thus returning nroots = -1 if it has not been set yet

The returned ilocal and iremote might contain values in different order than the input ones in PetscSFSetGraph()

Use PetscSFRestoreGraph() when access to the arrays is no longer needed

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFType, PetscSFCreate(), PetscSFView(), PetscSFSetGraph()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex1f.F90 src/vec/is/sf/tutorials/ex1.c src/ts/tutorials/ex30.c

PetscSFGetGraph_Allgatherv() in src/vec/is/sf/impls/basic/allgatherv/sfallgatherv.c PetscSFGetGraph_Alltoall() in src/vec/is/sf/impls/basic/alltoall/sfalltoall.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFGetGraph(PetscSF sf, PetscInt *nroots, PetscInt *nleaves, const PetscInt *ilocal[], const PetscSFNode *iremote[])
```

Example 2 (unknown):
```unknown
PetscSFSetGraph()
```

Example 3 (unknown):
```unknown
PetscSFRestoreGraph()
```

Example 4 (unknown):
```unknown
PetscSFType
```

---

## PetscSFGetGroups#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFGetGroups/

**Contents:**
- PetscSFGetGroups#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

gets incoming and outgoing process groups

incoming - group of origin processes for incoming edges (leaves that reference my roots)

outgoing - group of destination processes for outgoing edges (roots that I reference)

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFGetWindow(), PetscSFRestoreWindow()

src/vec/is/sf/interface/sf.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFGetGroups(PetscSF sf, MPI_Group *incoming, MPI_Group *outgoing)
```

Example 2 (unknown):
```unknown
PetscSFGetWindow()
```

Example 3 (unknown):
```unknown
PetscSFRestoreWindow()
```

---

## PetscSFGetLeafRange#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFGetLeafRange/

**Contents:**
- PetscSFGetLeafRange#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Get the active leaf ranges

minleaf - minimum active leaf on this MPI process. Returns 0 if there are no leaves.

maxleaf - maximum active leaf on this MPI process. Returns -1 if there are no leaves.

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFType, PetscSFCreate(), PetscSFView(), PetscSFSetGraph(), PetscSFGetGraph()

src/vec/is/sf/interface/sf.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFGetLeafRange(PetscSF sf, PetscInt *minleaf, PetscInt *maxleaf)
```

Example 2 (unknown):
```unknown
PetscSFType
```

Example 3 (unknown):
```unknown
PetscSFCreate()
```

Example 4 (unknown):
```unknown
PetscSFView()
```

---

## PetscSFGetLeafRanks#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFGetLeafRanks/

**Contents:**
- PetscSFGetLeafRanks#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Get leaf MPI ranks referencing roots on this process

niranks - number of leaf MPI processes referencing roots on this process

iranks - [niranks] array of MPI ranks

ioffset - [niranks+1] offset in irootloc for each MPI process

irootloc - [ioffset[niranks]] concatenated array holding local indices of roots referenced by each leaf MPI process

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFGetRootRanks()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex1f.F90

PetscSFGetLeafRanks_Allgatherv() in src/vec/is/sf/impls/basic/allgatherv/sfallgatherv.c PetscSFGetLeafRanks_Basic() in src/vec/is/sf/impls/basic/sfbasic.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFGetLeafRanks(PetscSF sf, PetscMPIInt *niranks, const PetscMPIInt *iranks[], const PetscInt *ioffset[], const PetscInt *irootloc[])
```

Example 2 (unknown):
```unknown
PetscSFGetRootRanks()
```

---

## PetscSFGetMultiSF#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFGetMultiSF/

**Contents:**
- PetscSFGetMultiSF#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

gets the inner PetscSF implementing gathers and scatters

sf - star forest that may contain roots with 0 or with more than 1 vertex

multi - star forest with split roots, such that each root has degree exactly 1 (has one leaf)

In most cases, users should use PetscSFGatherBegin() and PetscSFScatterBegin() instead of manipulating multi directly. Since multi satisfies the stronger condition that each entry in the global space has exactly one incoming edge, it is a candidate for future optimization that might involve its removal.

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFSetGraph(), PetscSFGatherBegin(), PetscSFScatterBegin(), PetscSFComputeMultiRootOriginalNumbering()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex1.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFGetMultiSF(PetscSF sf, PetscSF *multi)
```

Example 2 (unknown):
```unknown
PetscSFGatherBegin()
```

Example 3 (unknown):
```unknown
PetscSFScatterBegin()
```

Example 4 (unknown):
```unknown
PetscSFSetGraph()
```

---

## PetscSFGetRanksSF#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFGetRanksSF/

**Contents:**
- PetscSFGetRanksSF#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

gets the PetscSF to perform communications with root ranks

rsf - the star forest with a single root per MPI process to perform communications

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFSetGraph(), PetscSFGetRootRanks()

src/vec/is/sf/interface/sf.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFGetRanksSF(PetscSF sf, PetscSF *rsf)
```

Example 2 (unknown):
```unknown
PetscSFSetGraph()
```

Example 3 (unknown):
```unknown
PetscSFGetRootRanks()
```

---

## PetscSFGetRootRanks#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFGetRootRanks/

**Contents:**
- PetscSFGetRootRanks#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Get the root MPI ranks and number of vertices referenced by leaves on this process

nranks - number of MPI processes referenced by local part

ranks - [nranks] array of MPI ranks

roffset - [nranks+1] offset in rmine and rremote for each MPI process

rmine - [roffset[nranks]] concatenated array holding local indices referencing each remote MPI process, or NULL

rremote - [roffset[nranks]] concatenated array holding remote indices referenced for each remote MPI process, or NULL

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFGetLeafRanks()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex1f.F90 src/vec/is/sf/tutorials/ex1.c

PetscSFGetRootRanks_Allgatherv() in src/vec/is/sf/impls/basic/allgatherv/sfallgatherv.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFGetRootRanks(PetscSF sf, PetscMPIInt *nranks, const PetscMPIInt *ranks[], const PetscInt *roffset[], const PetscInt *rmine[], const PetscInt *rremote[])
```

Example 2 (unknown):
```unknown
PetscSFGetLeafRanks()
```

---

## PetscSFGetType#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFGetType/

**Contents:**
- PetscSFGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the PetscSF communication implementation

sf - the PetscSF context

type - the PetscSF type name

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFType, PetscSFSetType(), PetscSFCreate()

src/vec/is/sf/interface/sf.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFGetType(PetscSF sf, PetscSFType *type)
```

Example 2 (unknown):
```unknown
PetscSFType
```

Example 3 (unknown):
```unknown
PetscSFSetType()
```

Example 4 (unknown):
```unknown
PetscSFCreate()
```

---

## PetscSFInitializePackage#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFInitializePackage/

**Contents:**
- PetscSFInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

Initialize PetscSF package

PetscSF, PetscSFFinalizePackage()

src/vec/is/sf/interface/dlregissf.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscSFInitializePackage(void)
```

Example 2 (unknown):
```unknown
PetscSFFinalizePackage()
```

---

## PetscSFLink#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFLink/

**Contents:**
- PetscSFLink#
- Synopsis#
- See Also#
- Level#
- Location#

Opaque internal scratch object used by PetscSF to pair a packed buffer with the appropriate pack/unpack and MPI operations for a given root-data layout and PetscSFBackend

PetscSF, PetscSFBackend, PetscSFBcastBegin(), PetscSFReduceBegin()

include/petscsftypes.h

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSFBackend
```

Example 2 (julia):
```julia
typedef struct _n_PetscSFLink *PetscSFLink;
```

Example 3 (unknown):
```unknown
PetscSFBackend
```

Example 4 (unknown):
```unknown
PetscSFBcastBegin()
```

---

## PetscSFMerge#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFMerge/

**Contents:**
- PetscSFMerge#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

append/merge indices of sfb into sfa, with preference for sfb

sfa - default PetscSF

sfb - additional edges to add/replace edges in sfa

merged - new PetscSF with combined edges

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFCompose()

src/vec/is/sf/utils/sfutils.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h"   
PetscErrorCode PetscSFMerge(PetscSF sfa, PetscSF sfb, PetscSF *merged)
```

Example 2 (unknown):
```unknown
PetscSFCompose()
```

---

## PetscSFNode#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFNode/

**Contents:**
- PetscSFNode#
- Synopsis#
- Sample Usage#
- Sample Fortran Usage#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

specifier of MPI rank owner and local index for array or Vec entry locations that are to be communicated with a PetscSF

Use MPIU_SF_NODE when performing MPI operations on arrays of PetscSFNode

Generally the values of rank should be in \([ 0,size)\) and the value of index greater than or equal to 0, but there are some situations that violate this.

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFSetGraph()

include/petscsftypes.h

src/vec/is/sf/tutorials/ex2.c src/vec/is/sf/tutorials/ex1f.F90 src/vec/is/sf/tutorials/ex3.c src/dm/tutorials/swarm_ex3.c src/vec/is/sf/tutorials/ex1.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef struct {
  PetscInt rank;  /* MPI rank of owner */
  PetscInt index; /* Index of node on rank */
} PetscSFNode;
```

Example 2 (sass):
```sass
PetscSFNode    *remote;
    PetscCall(PetscMalloc1(nleaves,&remote));
    for (i=0; i<size; i++) {
      remote[i].rank = i;
      remote[i].index = rank;
    }
```

Example 3 (perl):
```perl
type(PetscSFNode) remote(6)
    remote(1)%rank  = modulo(rank+size-1,size)
    remote(1)%index = 1 * stride
```

Example 4 (unknown):
```unknown
MPIU_SF_NODE
```

---

## PetscSFOperation#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFOperation/

**Contents:**
- PetscSFOperation#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Identifies the high-level operation being performed by a PetscSF communication

PETSCSF_BCAST - broadcast from roots to leaves

PETSCSF_REDUCE - reduce from leaves to roots with an MPI_Op

PETSCSF_FETCH - fetch-and-op: each leaf receives the current root value and contributes its own

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFDirection, PetscSFBcastBegin(), PetscSFReduceBegin(), PetscSFFetchAndOpBegin()

include/petscsftypes.h

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  PETSCSF_BCAST  = 0,
  PETSCSF_REDUCE = 1,
  PETSCSF_FETCH  = 2
} PetscSFOperation;
```

Example 2 (unknown):
```unknown
PETSCSF_BCAST
```

Example 3 (unknown):
```unknown
PETSCSF_REDUCE
```

Example 4 (unknown):
```unknown
PETSCSF_FETCH
```

---

## PetscSFPattern#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFPattern/

**Contents:**
- PetscSFPattern#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Pattern of the PetscSF graph

PETSCSF_PATTERN_GENERAL - A general graph. One sets the graph with PetscSFSetGraph() and usually does not use this enum directly.

PETSCSF_PATTERN_ALLGATHER - A graph that every MPI process gathers all roots from all MPI processes (like MPI_Allgather()). One sets the graph with PetscSFSetGraphWithPattern().

PETSCSF_PATTERN_GATHER - A graph that MPI rank 0 gathers all roots from all MPI processes (like MPI_Gatherv() with root=0). One sets the graph with PetscSFSetGraphWithPattern().

PETSCSF_PATTERN_ALLTOALL - A graph that every MPI process gathers different roots from all MPI processes (like MPI_Alltoall()). One sets the graph with PetscSFSetGraphWithPattern(). We assume each process has size leaves and size roots, with each leaf connecting to a remote root. Here size is the size of the communicator. This does not mean one can not communicate multiple data items between a pair of processes. One just needs to create a new MPI datatype for the multiple data items, e.g., by MPI_Type_contiguous.

PetscSF, PetscSFSetGraph(), PetscSFSetGraphWithPattern()

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  PETSCSF_PATTERN_GENERAL,
  PETSCSF_PATTERN_ALLGATHER,
  PETSCSF_PATTERN_GATHER,
  PETSCSF_PATTERN_ALLTOALL
} PetscSFPattern;
```

Example 2 (unknown):
```unknown
PETSCSF_PATTERN_GENERAL
```

Example 3 (unknown):
```unknown
PetscSFSetGraph()
```

Example 4 (unknown):
```unknown
PETSCSF_PATTERN_ALLGATHER
```

---

## PetscSFReduceBegin#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFReduceBegin/

**Contents:**
- PetscSFReduceBegin#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

begin reduction (communication) of leafdata into rootdata, to be completed with call to PetscSFReduceEnd()

leafdata - values to reduce (communicate)

op - reduction operation

rootdata - result of reduction of values (leafdata) from all leaves to each root

When PETSc is configured with device support, it will use PetscGetMemType() to determine whether the given data pointers are host pointers or device pointers, which may incur a noticeable cost. If you already knew the memory type, you should use PetscSFReduceWithMemTypeBegin() instead.

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFBcastBegin(), PetscSFReduceWithMemTypeBegin(), PetscSFReduceEnd(), MPI_Datatype

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex1f.F90 src/vec/is/sf/tutorials/ex1.c src/ts/tutorials/ex30.c

PetscSFReduceBegin_Allgather() in src/vec/is/sf/impls/basic/allgather/sfallgather.c PetscSFReduceBegin_Allgatherv() in src/vec/is/sf/impls/basic/allgatherv/sfallgatherv.c PetscSFReduceBegin_Basic() in src/vec/is/sf/impls/basic/sfbasic.c PetscSFReduceBegin_Window() in src/vec/is/sf/impls/window/sfwindow.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSFReduceEnd()
```

Example 2 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFReduceBegin(PetscSF sf, MPI_Datatype unit, const void *leafdata, void *rootdata, MPI_Op op)
```

Example 3 (unknown):
```unknown
PetscGetMemType()
```

Example 4 (unknown):
```unknown
PetscSFReduceWithMemTypeBegin()
```

---

## PetscSFReduceEnd#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFReduceEnd/

**Contents:**
- PetscSFReduceEnd#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

end a reduction operation started with PetscSFReduceBegin() or PetscSFReduceWithMemTypeBegin()

leafdata - values to reduce

op - reduction operation

rootdata - result of reduction of values from all leaves of each root

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFSetGraph(), PetscSFBcastEnd(), PetscSFReduceBegin(), PetscSFReduceWithMemTypeBegin()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex1f.F90 src/vec/is/sf/tutorials/ex1.c src/ts/tutorials/ex30.c

PetscSFReduceEnd_Allgatherv() in src/vec/is/sf/impls/basic/allgatherv/sfallgatherv.c PetscSFReduceEnd_Basic() in src/vec/is/sf/impls/basic/sfbasic.c PetscSFReduceEnd_Window() in src/vec/is/sf/impls/window/sfwindow.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSFReduceBegin()
```

Example 2 (unknown):
```unknown
PetscSFReduceWithMemTypeBegin()
```

Example 3 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFReduceEnd(PetscSF sf, MPI_Datatype unit, const void *leafdata, void *rootdata, MPI_Op op)
```

Example 4 (unknown):
```unknown
PetscSFSetGraph()
```

---

## PetscSFReduceWithMemTypeBegin#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFReduceWithMemTypeBegin/

**Contents:**
- PetscSFReduceWithMemTypeBegin#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

begin reduction of leafdata into rootdata with explicit memory types, to be completed with call to PetscSFReduceEnd()

leafmtype - memory type of leafdata

leafdata - values to reduce

rootmtype - memory type of rootdata

op - reduction operation

rootdata - result of reduction of values from all leaves of each root

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFBcastBegin(), PetscSFReduceBegin(), PetscSFReduceEnd()

src/vec/is/sf/interface/sf.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSFReduceEnd()
```

Example 2 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFReduceWithMemTypeBegin(PetscSF sf, MPI_Datatype unit, PetscMemType leafmtype, const void *leafdata, PetscMemType rootmtype, void *rootdata, MPI_Op op)
```

Example 3 (unknown):
```unknown
PetscSFBcastBegin()
```

Example 4 (unknown):
```unknown
PetscSFReduceBegin()
```

---

## PetscSFRegisterAll#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFRegisterAll/

**Contents:**
- PetscSFRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all the PetscSF communication implementations

PetscSF, PetscSFRegister(), PetscSFRegisterDestroy()

src/vec/is/sf/interface/sfregi.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h"  
PetscErrorCode PetscSFRegisterAll(void)
```

Example 2 (unknown):
```unknown
PetscSFRegister()
```

Example 3 (unknown):
```unknown
PetscSFRegisterDestroy()
```

---

## PetscSFRegisterPersistent#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFRegisterPersistent/

**Contents:**
- PetscSFRegisterPersistent#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Register root and leaf data as memory regions that will be used for repeated PetscSF communications.

unit - the data type contained within rootdata and leafdata

rootdata - root data that will be used for multiple PetscSF communications

leafdata - leaf data that will be used for multiple PetscSF communications

Implementations of PetscSF can make optimizations for repeated communication using the same memory regions, but these optimizations can be unsound if rootdata or leafdata is deallocated and the PetscSF is not informed. The intended pattern is

If you do not register rootdata and leafdata it will not cause an error, but optimizations that reduce the setup time for each communication cannot be made. Currently, the only implementation of PetscSF that benefits from PetscSFRegisterPersistent() is PETSCSFWINDOW. For the default PETSCSFBASIC there is no benefit to using PetscSFRegisterPersistent().

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PETSCSFWINDOW, PetscSFDeregisterPersistent()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex1.c src/vec/is/sf/tutorials/ex3.c

PetscSFRegisterPersistent_Window() in src/vec/is/sf/impls/window/sfwindow.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFRegisterPersistent(PetscSF sf, MPI_Datatype unit, const void *rootdata, const void *leafdata)
```

Example 2 (lua):
```lua
PetscMalloc2(nroots, &rootdata, nleaves, &leafdata);

  PetscSFRegisterPersistent(sf, unit, rootdata, leafdata);
  // repeated use of rootdata and leafdata will now be optimized

  PetscSFBcastBegin(sf, unit, rootdata, leafdata, MPI_REPLACE);
  PetscSFBcastEnd(sf, unit, rootdata, leafdata, MPI_REPLACE);
  // ...
  PetscSFReduceBegin(sf, unit, leafdata, rootdata, MPI_SUM);
  PetscSFReduceEnd(sf, unit, leafdata, rootdata, MPI_SUM);
  // ... (other communications)

  // rootdata and leafdata must be deregistered before freeing
  // skipping this can lead to undefined behavior including
  // deadlocks
  PetscSFDeregisterPersistent(sf, unit, rootdata, leafdata);

  // it is now safe to free rootdata and leafdata
  PetscFree2(rootdata, leafdata);
```

Example 3 (unknown):
```unknown
PetscSFRegisterPersistent()
```

Example 4 (unknown):
```unknown
PETSCSFWINDOW
```

---

## PetscSFRegister#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFRegister/

**Contents:**
- PetscSFRegister#
- Synopsis#
- Input Parameters#
- Example Usage#
- Note#
- See Also#
- Level#
- Location#

Adds an implementation of the PetscSF communication protocol.

Not Collective, No Fortran Support

name - name of a new user-defined implementation

create - routine to create method context

Then, this implementation can be chosen with the procedural interface via

or at runtime via the option

PetscSFRegister() may be called multiple times to add several user-defined implementations.

PetscSF, PetscSFType, PetscSFRegisterAll(), PetscSFInitializePackage()

src/vec/is/sf/interface/sfregi.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h"  
PetscErrorCode PetscSFRegister(const char name[], PetscErrorCode (*create)(PetscSF))
```

Example 2 (unknown):
```unknown
PetscSFRegister("my_impl", MyImplCreate);
```

Example 3 (unknown):
```unknown
PetscSFSetType(sf, "my_impl")
```

Example 4 (unknown):
```unknown
-sf_type my_impl
```

---

## PetscSFReset#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFReset/

**Contents:**
- PetscSFReset#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Reset a star forest so that different sizes or neighbors can be used

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFCreate(), PetscSFSetGraph(), PetscSFDestroy()

src/vec/is/sf/interface/sf.c

PetscSFReset_Allgatherv() in src/vec/is/sf/impls/basic/allgatherv/sfallgatherv.c PetscSFReset_Neighbor() in src/vec/is/sf/impls/basic/neighbor/sfneighbor.c PetscSFReset_Basic() in src/vec/is/sf/impls/basic/sfbasic.c PetscSFReset_Window() in src/vec/is/sf/impls/window/sfwindow.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFReset(PetscSF sf)
```

Example 2 (unknown):
```unknown
PetscSFCreate()
```

Example 3 (unknown):
```unknown
PetscSFSetGraph()
```

Example 4 (unknown):
```unknown
PetscSFDestroy()
```

---

## PetscSFScatterBegin#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFScatterBegin/

**Contents:**
- PetscSFScatterBegin#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

begin pointwise scatter operation from multi-roots to leaves, to be completed with PetscSFScatterEnd()

multirootdata - root buffer to send to each leaf, one unit of data is provided to each leaf thus the amount of space per root is equal to its degree (which is the number of leaves that root has)

leafdata - leaf data to be update with personal data from each respective root

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFComputeDegreeBegin(), PetscSFComputeDegreeEnd(), PetscSFScatterEnd()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex1.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSFScatterEnd()
```

Example 2 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFScatterBegin(PetscSF sf, MPI_Datatype unit, const void *multirootdata, void *leafdata)
```

Example 3 (unknown):
```unknown
PetscSFComputeDegreeBegin()
```

Example 4 (unknown):
```unknown
PetscSFComputeDegreeEnd()
```

---

## PetscSFScatterEnd#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFScatterEnd/

**Contents:**
- PetscSFScatterEnd#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

ends pointwise scatter operation that was started with PetscSFScatterBegin()

multirootdata - root buffer to send to each leaf, one unit of data per leaf

leafdata - leaf data to be update with personal data from each respective root

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFComputeDegreeBegin(), PetscSFComputeDegreeEnd(), PetscSFScatterBegin()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex1.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSFScatterBegin()
```

Example 2 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFScatterEnd(PetscSF sf, MPI_Datatype unit, const void *multirootdata, void *leafdata)
```

Example 3 (unknown):
```unknown
PetscSFComputeDegreeBegin()
```

Example 4 (unknown):
```unknown
PetscSFComputeDegreeEnd()
```

---

## PetscSFSetFromOptions#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFSetFromOptions/

**Contents:**
- PetscSFSetFromOptions#
- Synopsis#
- Input Parameter#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

set PetscSF options using the options database

-sf_type (basic|window|neighbor) - implementation type, see PetscSFSetType()

-sf_rank_order (true|false) - sort composite points for gathers and scatters in MPI rank order, gathers are non-deterministic otherwise

-sf_use_default_stream - Assume callers of PetscSF computed the input root/leafdata with the default CUDA stream. PetscSF will also use the default stream to process data. Therefore, no stream synchronization is needed between PetscSF and its caller (default: true). If true, this option only works with -use_gpu_aware_mpi 1.

-sf_use_stream_aware_mpi - Assume the underlying MPI is CUDA-stream aware and PetscSF won’t sync streams for send/recv buffers passed to MPI (default: false). If true, this option only works with -use_gpu_aware_mpi 1.

-sf_backend (cuda|hip|kokkos) - Select the device backend PetscSF uses. On CUDA (HIP) devices, one can choose cuda (hip) or kokkos with the default being kokkos. On other devices, the only available is kokkos.

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFCreate(), PetscSFSetType()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex1f.F90 src/vec/is/sf/tutorials/ex1.c src/vec/is/sf/tutorials/ex3.c src/vec/is/sf/tutorials/ex2.c

PetscSFSetFromOptions_Window() in src/vec/is/sf/impls/window/sfwindow.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFSetFromOptions(PetscSF sf)
```

Example 2 (unknown):
```unknown
PetscSFSetType()
```

Example 3 (unknown):
```unknown
-use_gpu_aware_mpi 1
```

Example 4 (unknown):
```unknown
-use_gpu_aware_mpi 1
```

---

## PetscSFSetGraphFromCoordinates#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFSetGraphFromCoordinates/

**Contents:**
- PetscSFSetGraphFromCoordinates#
- Synopsis#
- Input Parameters#
- Notes#
- Example#
- See Also#
- Level#
- Location#
- Examples#

Create SF by fuzzy matching leaf coordinates to root coordinates

sf - PetscSF to set graph on

nroots - number of root coordinates

nleaves - number of leaf coordinates

dim - spatial dimension of coordinates

tol - positive tolerance for matching

rootcoords - array of root coordinates in which root i component d is [i*dim+d]

leafcoords - array of root coordinates in which leaf i component d is [i*dim+d]

The tolerance typically represents the rounding error incurred by numerically computing coordinates via possibly-different procedures. Passing anything from PETSC_SMALL to 100 * PETSC_MACHINE_EPSILON is appropriate for most use cases.

As a motivating example, consider fluid flow in the x direction with y (distance from a wall). The spanwise direction, z, has periodic boundary conditions and needs some spanwise length to allow turbulent structures to develop. The distribution is stationary with respect to z, so you want to average turbulence variables (like Reynolds stress) over the z direction. It is complicated in a 3D simulation with arbitrary partitioner to uniquely number the nodes or quadrature point coordinates to average these quantities into a 2D plane where they will be visualized, but it’s easy to compute the projection of each 3D point into the 2D plane.

Suppose a 2D target mesh and 3D source mesh (logically an extrusion of the 2D, though perhaps not created in that way) are distributed independently on a communicator. Each rank passes its 2D target points as root coordinates and the 2D projection of its 3D source points as leaf coordinates. Calling PetscSFReduceBegin()/PetscSFReduceEnd() on the result will sum data from the 3D sources to the 2D targets.

As a concrete example, consider three MPI ranks with targets (roots)

Note that targets must be uniquely owned. Suppose also that we identify the following leaf coordinates (perhaps via projection from a 3D space).

Leaf coordinates may be repeated, both on a rank and between ranks. This example yields the following PetscSF capable of reducing from sources to targets.

PetscSFCreate(), PetscSFSetGraph(), PetscSFCreateByMatchingIndices()

src/vec/is/sf/utils/sfcoord.c

src/dm/impls/plex/tutorials/ex15.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h"   
PetscErrorCode PetscSFSetGraphFromCoordinates(PetscSF sf, PetscInt nroots, PetscInt nleaves, PetscInt dim, PetscReal tol, const PetscReal rootcoords[], const PetscReal leafcoords[])
```

Example 2 (unknown):
```unknown
PETSC_SMALL
```

Example 3 (unknown):
```unknown
100 * PETSC_MACHINE_EPSILON
```

Example 4 (unknown):
```unknown
PetscSFReduceBegin()
```

---

## PetscSFSetGraphLayout#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFSetGraphLayout/

**Contents:**
- PetscSFSetGraphLayout#
- Synopsis#
- Input Parameters#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#

Set a PetscSF communication pattern using global indices and a PetscLayout

layout - PetscLayout defining the global space for roots, i.e. which roots are owned by each MPI process

nleaves - number of leaf vertices on the current process, each of these references a root on any MPI process

ilocal - locations of leaves in leafdata buffers, pass NULL for contiguous storage, that is the locations are in [0,nleaves)

localmode - copy mode for ilocal

gremote - root vertices in global numbering corresponding to the leaves

Global indices must lie in [0, N) where N is the global size of layout. Leaf indices in ilocal get sorted; this means the user-provided array gets sorted if localmode is PETSC_OWN_POINTER.

Local indices which are the identity permutation in the range [0,nleaves) are discarded as they encode contiguous storage. In such case, if localmode is PETSC_OWN_POINTER, the memory is deallocated as it is not needed

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFGetGraphLayout(), PetscSFCreate(), PetscSFView(), PetscSFSetGraph(), PetscSFGetGraph()

src/vec/is/sf/utils/sfutils.c

src/ts/tutorials/ex30.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLayout
```

Example 2 (unknown):
```unknown
#include "petscsf.h"   
PetscErrorCode PetscSFSetGraphLayout(PetscSF sf, PetscLayout layout, PetscInt nleaves, PetscInt ilocal[], PetscCopyMode localmode, const PetscInt gremote[])
```

Example 3 (unknown):
```unknown
PetscLayout
```

Example 4 (unknown):
```unknown
PETSC_OWN_POINTER
```

---

## PetscSFSetGraphSection#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFSetGraphSection/

**Contents:**
- PetscSFSetGraphSection#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the PetscSF graph (communication pattern) encoding the parallel dof overlap based upon the PetscSection describing the data layout.

localSection - PetscSection describing the local data layout

globalSection - PetscSection describing the global data layout

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFSetGraph(), PetscSFSetGraphLayout()

src/vec/is/sf/utils/sfutils.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsf.h"   
PetscErrorCode PetscSFSetGraphSection(PetscSF sf, PetscSection localSection, PetscSection globalSection)
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (unknown):
```unknown
PetscSection
```

---

## PetscSFSetGraphWithPattern#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFSetGraphWithPattern/

**Contents:**
- PetscSFSetGraphWithPattern#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Sets the graph of a PetscSF with a specific pattern

map - Layout of roots over all processes (not used when pattern is PETSCSF_PATTERN_ALLTOALL)

pattern - One of PETSCSF_PATTERN_ALLGATHER, PETSCSF_PATTERN_GATHER, PETSCSF_PATTERN_ALLTOALL

It is easier to explain PetscSFPattern using vectors. Suppose we have an MPI vector root and its PetscLayout is map. n and N are the local and global sizes of root respectively.

With PETSCSF_PATTERN_ALLGATHER, the routine creates a graph that if one does PetscSFBcastBegin() and PetscSFBcastEnd() on it, it will copy root to sequential vectors leaves on all MPI processes.

With PETSCSF_PATTERN_GATHER, the routine creates a graph that if one does PetscSFBcastBegin() and PetscSFBcastEnd() on it, it will copy root to a sequential vector leaves on MPI rank 0.

With PETSCSF_PATTERN_ALLTOALL, map is not used. Suppose NP is the size of sf’s communicator. The routine creates a graph where every MPI process has NP leaves and NP roots. On MPI rank i, its leaf j is connected to root i of rank j. Here 0 <=i,j<NP. It is a kind of MPI_Alltoall() with sendcount/recvcount being 1. Note that it does not mean one can not send multiple items. One needs to create a new MPI datatype for the multiple data items with MPI_Type_contiguous and use that as the argument in the PetscSF routines. In this case, roots and leaves are symmetric.

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFCreate(), PetscSFView(), PetscSFGetGraph()

src/vec/is/sf/interface/sf.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFSetGraphWithPattern(PetscSF sf, PetscLayout map, PetscSFPattern pattern)
```

Example 2 (unknown):
```unknown
PETSCSF_PATTERN_ALLTOALL
```

Example 3 (unknown):
```unknown
PETSCSF_PATTERN_ALLGATHER
```

Example 4 (unknown):
```unknown
PETSCSF_PATTERN_GATHER
```

---

## PetscSFSetGraph#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFSetGraph/

**Contents:**
- PetscSFSetGraph#
- Synopsis#
- Input Parameters#
- Notes#
- Fortran Notes#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#

Set a parallel star forest

nroots - number of root vertices on the current MPI process (these are possible targets for other process to attach leaves)

nleaves - number of leaf vertices on the current MPI process, each of these references a root on any process

ilocal - locations of leaves in leafdata buffers (locations must be >= 0, enforced during setup in debug mode), pass NULL for contiguous storage (same as passing (0, 1, 2, …, nleaves-1))

localmode - copy mode for ilocal

iremote - remote locations of root vertices for each leaf on the current process, length is `nleaves’ (locations must be >= 0, enforced during setup in debug mode)

remotemode - copy mode for iremote

Leaf indices in ilocal must be unique, otherwise an error occurs.

Input arrays ilocal and iremote follow the PetscCopyMode semantics. In particular, if localmode or remotemode is PETSC_OWN_POINTER or PETSC_USE_POINTER, PETSc might modify the respective array; if PETSC_USE_POINTER, the user must delete the array after PetscSFDestroy(). If PETSC_COPY_VALUES is used, the respective array is guaranteed to stay intact and a const array can be passed (but a cast to non-const is needed).

PetscSFSetGraphWithPattern() is an alternative approach to provide certain communication patterns that have extra optimizations.

In Fortran you must use PETSC_COPY_VALUES for localmode and remotemode.

We sort leaves to check for duplicates and contiguousness and to find minleaf/maxleaf. This also allows to compare leaf sets of two PetscSFs easily.

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFType, PetscSFCreate(), PetscSFView(), PetscSFGetGraph(), PetscSFSetGraphWithPattern()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex2.c src/vec/is/sf/tutorials/ex1f.F90 src/vec/is/sf/tutorials/ex3.c src/dm/tutorials/swarm_ex3.c src/vec/is/sf/tutorials/ex1.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFSetGraph(PetscSF sf, PetscInt nroots, PetscInt nleaves, PetscInt ilocal[], PetscCopyMode localmode, PetscSFNode iremote[], PetscCopyMode remotemode)
```

Example 2 (unknown):
```unknown
PetscCopyMode
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

## PetscSFSetRankOrder#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFSetRankOrder/

**Contents:**
- PetscSFSetRankOrder#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

sort multi-points for gathers and scatters by MPI rank order

flg - PETSC_TRUE to sort, PETSC_FALSE to skip sorting (false has a lower setup cost, but is non-deterministic)

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFType, PetscSFGatherBegin(), PetscSFScatterBegin()

src/vec/is/sf/interface/sf.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFSetRankOrder(PetscSF sf, PetscBool flg)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
PetscSFType
```

Example 4 (unknown):
```unknown
PetscSFGatherBegin()
```

---

## PetscSFSetType#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFSetType/

**Contents:**
- PetscSFSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Set the PetscSF communication implementation

sf - the PetscSF context

type - a known method

-sf_type (basic|window|neighbor) - Sets the method; see PetscSFType

See PetscSFType for possible values

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFType, PetscSFCreate()

src/vec/is/sf/interface/sf.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFSetType(PetscSF sf, PetscSFType type)
```

Example 2 (julia):
```julia
PETSCSFWINDOW - MPI-2/3 one-sided
    PETSCSFBASIC - basic implementation using MPI-1 two-sided
```

Example 3 (unknown):
```unknown
PetscSFType
```

Example 4 (unknown):
```unknown
PetscSFType
```

---

## PetscSFSetUpRanks#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFSetUpRanks/

**Contents:**
- PetscSFSetUpRanks#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set up data structures associated with MPI ranks; this is for internal use by PetscSF implementations.

sf - PetscSF to set up; PetscSFSetGraph() must have been called

dgroup - MPI_Group of ranks to be distinguished (e.g., for self or shared memory exchange)

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFGetRootRanks()

src/vec/is/sf/interface/sf.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFSetUpRanks(PetscSF sf, MPI_Group dgroup)
```

Example 2 (unknown):
```unknown
PetscSFSetGraph()
```

Example 3 (unknown):
```unknown
PetscSFGetRootRanks()
```

---

## PetscSFSetUp#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFSetUp/

**Contents:**
- PetscSFSetUp#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

set up communication structures for a PetscSF, after this is done it may be used to perform communication

sf - star forest communication object

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFType, PetscSFSetFromOptions(), PetscSFSetType()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex1f.F90 src/vec/is/sf/tutorials/ex1.c src/vec/is/sf/tutorials/ex3.c src/vec/is/sf/tutorials/ex2.c

PetscSFSetUp_Allgather() in src/vec/is/sf/impls/basic/allgather/sfallgather.c PetscSFSetUp_Allgatherv() in src/vec/is/sf/impls/basic/allgatherv/sfallgatherv.c PetscSFSetUp_Neighbor() in src/vec/is/sf/impls/basic/neighbor/sfneighbor.c PetscSFSetUp_Basic() in src/vec/is/sf/impls/basic/sfbasic.c PetscSFSetUp_Window() in src/vec/is/sf/impls/window/sfwindow.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFSetUp(PetscSF sf)
```

Example 2 (unknown):
```unknown
PetscSFType
```

Example 3 (unknown):
```unknown
PetscSFSetFromOptions()
```

Example 4 (unknown):
```unknown
PetscSFSetType()
```

---

## PetscSFType#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFType/

**Contents:**
- PetscSFType#
- Synopsis#
- Available Types#
- Note#
- See Also#
- Level#
- Location#

String with the name of a PetscSF type. Each PetscSFType uses different mechanisms to perform the communication.

PETSCSFBASIC - use MPI sends and receives

PETSCSFNEIGHBOR - use MPI_Neighbor operations

PETSCSFALLGATHERV - use MPI_Allgatherv operations

PETSCSFALLGATHER - use MPI_Allgather operations

PETSCSFGATHERV - use MPI_Igatherv and MPI_Iscatterv operations

PETSCSFGATHER - use MPI_Igather and MPI_Iscatter operations

PETSCSFALLTOALL - use MPI_Ialltoall operations

PETSCSFWINDOW - use MPI_Win operations

Some PetscSFType only provide specialized code for a subset of the PetscSF operations and use PETSCSFBASIC for the others.

PetscSF - an alternative to low-level MPI calls for data communication, PetscSFSetType(), PetscSF

include/petscsftypes.h

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSFType
```

Example 2 (unknown):
```unknown
typedef const char *PetscSFType;
#define PETSCSFBASIC      "basic"
#define PETSCSFNEIGHBOR   "neighbor"
#define PETSCSFALLGATHERV "allgatherv"
#define PETSCSFALLGATHER  "allgather"
#define PETSCSFGATHERV    "gatherv"
#define PETSCSFGATHER     "gather"
#define PETSCSFALLTOALL   "alltoall"
#define PETSCSFWINDOW     "window"
```

Example 3 (unknown):
```unknown
PETSCSFBASIC
```

Example 4 (unknown):
```unknown
PETSCSFNEIGHBOR
```

---

## PetscSFViewFromOptions#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFViewFromOptions/

**Contents:**
- PetscSFViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

View a PetscSF based on arguments in the options database

obj - Optional object that provides the prefix for the option names

name - command line option

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscSFView, PetscObjectViewFromOptions(), PetscSFCreate()

src/vec/is/sf/interface/sf.c

src/dm/impls/plex/tutorials/ex15.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFViewFromOptions(PetscSF A, PetscObject obj, const char name[])
```

Example 2 (unknown):
```unknown
PetscObjectViewFromOptions()
```

Example 3 (unknown):
```unknown
PetscSFView
```

Example 4 (unknown):
```unknown
PetscObjectViewFromOptions()
```

---

## PetscSFView#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFView/

**Contents:**
- PetscSFView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

viewer - viewer to display graph, for example PETSC_VIEWER_STDOUT_WORLD

PetscSF - an alternative to low-level MPI calls for data communication, PetscSF, PetscViewer, PetscSFCreate(), PetscSFSetGraph()

src/vec/is/sf/interface/sf.c

src/vec/is/sf/tutorials/ex1f.F90 src/vec/is/sf/tutorials/ex1.c src/vec/is/sf/tutorials/ex3.c src/vec/is/sf/tutorials/ex2.c

PetscSFView_Basic() in src/vec/is/sf/impls/basic/sfbasic.c PetscSFView_Window() in src/vec/is/sf/impls/window/sfwindow.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFView(PetscSF sf, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PETSC_VIEWER_STDOUT_WORLD
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscSFCreate()
```

---

## PetscSFWindowFlavorType#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFWindowFlavorType/

**Contents:**
- PetscSFWindowFlavorType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Flavor for the creation of MPI windows for PETSCSFWINDOW

PETSCSF_WINDOW_FLAVOR_CREATE - Use MPI_Win_create(), no reuse

PETSCSF_WINDOW_FLAVOR_DYNAMIC - Use MPI_Win_create_dynamic() and dynamically attach pointers

PETSCSF_WINDOW_FLAVOR_ALLOCATE - Use MPI_Win_allocate()

PETSCSF_WINDOW_FLAVOR_SHARED - Use MPI_Win_allocate_shared()

PetscSF, PetscSFWindowSyncType, PetscSFWindowSetFlavorType(), PetscSFWindowGetFlavorType()

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCSFWINDOW
```

Example 2 (unknown):
```unknown
typedef enum {
  PETSCSF_WINDOW_FLAVOR_CREATE,
  PETSCSF_WINDOW_FLAVOR_DYNAMIC,
  PETSCSF_WINDOW_FLAVOR_ALLOCATE,
  PETSCSF_WINDOW_FLAVOR_SHARED
} PetscSFWindowFlavorType;
```

Example 3 (unknown):
```unknown
PETSCSF_WINDOW_FLAVOR_CREATE
```

Example 4 (unknown):
```unknown
MPI_Win_create()
```

---

## PetscSFWindowGetFlavorType#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFWindowGetFlavorType/

**Contents:**
- PetscSFWindowGetFlavorType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get PETSCSFWINDOW flavor type for PetscSF communication

sf - star forest for communication of type PETSCSFWINDOW

PetscSF, PETSCSFWINDOW, PetscSFSetFromOptions(), PetscSFWindowSetFlavorType()

src/vec/is/sf/impls/window/sfwindow.c

PetscSFWindowGetFlavorType_Window() in src/vec/is/sf/impls/window/sfwindow.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCSFWINDOW
```

Example 2 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFWindowGetFlavorType(PetscSF sf, PetscSFWindowFlavorType *flavor)
```

Example 3 (unknown):
```unknown
PETSCSFWINDOW
```

Example 4 (unknown):
```unknown
PETSCSFWINDOW
```

---

## PetscSFWindowGetInfo#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFWindowGetInfo/

**Contents:**
- PetscSFWindowGetInfo#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Get the MPI_Info handle used for windows allocation

sf - star forest for communication

info - MPI_Info handle

If PetscSFWindowSetInfo() has not be called, this returns MPI_INFO_NULL

PetscSF, PETSCSFWINDOW, PetscSFSetFromOptions(), PetscSFWindowSetInfo()

src/vec/is/sf/impls/window/sfwindow.c

PetscSFWindowGetInfo_Window() in src/vec/is/sf/impls/window/sfwindow.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFWindowGetInfo(PetscSF sf, MPI_Info *info)
```

Example 2 (unknown):
```unknown
PetscSFWindowSetInfo()
```

Example 3 (unknown):
```unknown
MPI_INFO_NULL
```

Example 4 (unknown):
```unknown
PETSCSFWINDOW
```

---

## PetscSFWindowGetSyncType#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFWindowGetSyncType/

**Contents:**
- PetscSFWindowGetSyncType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get synchronization type for PetscSF communication of type PETSCSFWINDOW

sf - star forest for communication

sync - synchronization type

PetscSF, PETSCSFWINDOW, PetscSFSetFromOptions(), PetscSFWindowSetSyncType(), PetscSFWindowSyncType

src/vec/is/sf/impls/window/sfwindow.c

PetscSFWindowGetSyncType_Window() in src/vec/is/sf/impls/window/sfwindow.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCSFWINDOW
```

Example 2 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFWindowGetSyncType(PetscSF sf, PetscSFWindowSyncType *sync)
```

Example 3 (unknown):
```unknown
PETSCSFWINDOW
```

Example 4 (unknown):
```unknown
PetscSFSetFromOptions()
```

---

## PetscSFWindowSetFlavorType#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFWindowSetFlavorType/

**Contents:**
- PetscSFWindowSetFlavorType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Set flavor type for MPI_Win creation

sf - star forest for communication of type PETSCSFWINDOW

-sf_window_flavor flavor - sets the flavor type CREATE, DYNAMIC, ALLOCATE or SHARED (see PetscSFWindowFlavorType)

Windows reuse follows these rules:

PetscSF, PETSCSFWINDOW, PetscSFSetFromOptions(), PetscSFWindowGetFlavorType()

src/vec/is/sf/impls/window/sfwindow.c

PetscSFWindowSetFlavorType_Window() in src/vec/is/sf/impls/window/sfwindow.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFWindowSetFlavorType(PetscSF sf, PetscSFWindowFlavorType flavor)
```

Example 2 (unknown):
```unknown
PETSCSFWINDOW
```

Example 3 (unknown):
```unknown
PetscSFWindowFlavorType
```

Example 4 (sass):
```sass
PETSCSF_WINDOW_FLAVOR_CREATE: creates a new window every time, uses MPI_Win_create

     PETSCSF_WINDOW_FLAVOR_DYNAMIC: uses MPI_Win_create_dynamic/MPI_Win_attach and tries to reuse windows by comparing the root array. Intended to be used on repeated applications of the same SF, e.g.
       PetscSFRegisterPersistent(sf,rootdata1,leafdata);
       for i=1 to K
         PetscSFOperationBegin(sf,rootdata1,leafdata);
         PetscSFOperationEnd(sf,rootdata1,leafdata);
         ...
         PetscSFOperationBegin(sf,rootdata1,leafdata);
         PetscSFOperationEnd(sf,rootdata1,leafdata);
       endfor
       PetscSFDeregisterPersistent(sf,rootdata1,leafdata);

       The following pattern will instead raise an error
         PetscSFOperationBegin(sf,rootdata1,leafdata);
         PetscSFOperationEnd(sf,rootdata1,leafdata);
         PetscSFOperationBegin(sf,rank ? rootdata1 : rootdata2,leafdata);
         PetscSFOperationEnd(sf,rank ? rootdata1 : rootdata2,leafdata);

     PETSCSF_WINDOW_FLAVOR_ALLOCATE: uses MPI_Win_allocate, reuses any pre-existing window which fits the data and it is not in use

     PETSCSF_WINDOW_FLAVOR_SHARED: uses MPI_Win_allocate_shared, reusage policy as for PETSCSF_WINDOW_FLAVOR_ALLOCATE
```

---

## PetscSFWindowSetInfo#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFWindowSetInfo/

**Contents:**
- PetscSFWindowSetInfo#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Set the MPI_Info handle that will be used for subsequent windows allocation

sf - star forest for communication

info - MPI_Info handle

The info handle is duplicated with a call to MPI_Info_dup() unless info = MPI_INFO_NULL.

PetscSF, PETSCSFWINDOW, PetscSFSetFromOptions(), PetscSFWindowGetInfo()

src/vec/is/sf/impls/window/sfwindow.c

PetscSFWindowSetInfo_Window() in src/vec/is/sf/impls/window/sfwindow.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFWindowSetInfo(PetscSF sf, MPI_Info info)
```

Example 2 (unknown):
```unknown
MPI_Info_dup()
```

Example 3 (unknown):
```unknown
MPI_INFO_NULL
```

Example 4 (unknown):
```unknown
PETSCSFWINDOW
```

---

## PetscSFWindowSetSyncType#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFWindowSetSyncType/

**Contents:**
- PetscSFWindowSetSyncType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

Set synchronization type for PetscSF communication of type PETSCSFWINDOW

sf - star forest for communication

sync - synchronization type

-sf_window_sync sync - sets the synchronization type FENCE, LOCK, or ACTIVE (see PetscSFWindowSyncType)

PetscSF, PETSCSFWINDOW, PetscSFSetFromOptions(), PetscSFWindowGetSyncType(), PetscSFWindowSyncType

src/vec/is/sf/impls/window/sfwindow.c

PetscSFWindowSetSyncType_Window() in src/vec/is/sf/impls/window/sfwindow.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCSFWINDOW
```

Example 2 (unknown):
```unknown
#include "petscsf.h" 
PetscErrorCode PetscSFWindowSetSyncType(PetscSF sf, PetscSFWindowSyncType sync)
```

Example 3 (unknown):
```unknown
PetscSFWindowSyncType
```

Example 4 (unknown):
```unknown
PETSCSFWINDOW
```

---

## PetscSFWindowSyncType#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSFWindowSyncType/

**Contents:**
- PetscSFWindowSyncType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Type of synchronization for PETSCSFWINDOW

PETSCSF_WINDOW_SYNC_FENCE - simplest model, synchronizing across communicator

PETSCSF_WINDOW_SYNC_LOCK - passive model, less synchronous, requires less setup than PETSCSF_WINDOW_SYNC_ACTIVE, but may require more handshakes

PETSCSF_WINDOW_SYNC_ACTIVE - active model, provides most information to MPI implementation, needs to construct 2-way process groups (more setup than PETSCSF_WINDOW_SYNC_LOCK)

PetscSF, PetscSFWindowFlavorType, PetscSFWindowSetSyncType(), PetscSFWindowGetSyncType()

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCSFWINDOW
```

Example 2 (unknown):
```unknown
typedef enum {
  PETSCSF_WINDOW_SYNC_FENCE,
  PETSCSF_WINDOW_SYNC_LOCK,
  PETSCSF_WINDOW_SYNC_ACTIVE
} PetscSFWindowSyncType;
```

Example 3 (unknown):
```unknown
PETSCSF_WINDOW_SYNC_FENCE
```

Example 4 (unknown):
```unknown
PETSCSF_WINDOW_SYNC_LOCK
```

---

## PetscSF#

**URL:** https://petsc.org/release/manualpages/PetscSF/PetscSF/

**Contents:**
- PetscSF#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

PETSc object for managing the communication of certain entries of arrays and Vec between MPI processes.

PetscSF uses the concept of star forests to indicate and determine the communication patterns concisely and efficiently. A star https://en.wikipedia.org/wiki/Star_(graph_theory) forest is simply a collection of trees of height 1. The leave nodes represent “ghost locations” for the root nodes.

The standard usage paradigm for PetscSF is to provide the communication pattern with PetscSFSetGraph() or PetscSFSetGraphWithPattern() and then perform the communication using PetscSFBcastBegin() and PetscSFBcastEnd(), PetscSFReduceBegin() and PetscSFReduceEnd().

PetscSF - an alternative to low-level MPI calls for data communication, PetscSFCreate(), PetscSFSetGraph(), PetscSFSetGraphWithPattern(), PetscSFBcastBegin(), PetscSFBcastEnd(), PetscSFReduceBegin(), PetscSFReduceEnd(), VecScatter, VecScatterCreate()

include/petscsftypes.h

src/vec/is/sf/tutorials/ex2.c src/ts/tutorials/ex11.c src/dm/tutorials/ex25.c src/vec/is/sf/tutorials/ex1f.F90 src/ts/tutorials/ex30.c src/dm/impls/plex/tutorials/ex14.c src/dm/tutorials/swarm_ex3.c src/vec/is/sf/tutorials/ex3.c src/dm/impls/plex/tutorials/ex15.c src/vec/is/sf/tutorials/ex1.c

_p_PetscSF in include/petsc/private/sfimpl.h PetscSF_Allgatherv in src/vec/is/sf/impls/basic/allgatherv/sfallgatherv.h PetscSF_Neighbor in src/vec/is/sf/impls/basic/neighbor/sfneighbor.c PetscSF_Basic in src/vec/is/sf/impls/basic/sfbasic.h PetscSF_Window in src/vec/is/sf/impls/window/sfwindow.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_PetscSF *PetscSF;
```

Example 2 (unknown):
```unknown
PetscSFSetGraph()
```

Example 3 (unknown):
```unknown
PetscSFSetGraphWithPattern()
```

Example 4 (unknown):
```unknown
PetscSFBcastBegin()
```

---

## Star Forest Communication (PetscSF)#

**URL:** https://petsc.org/release/manualpages/PetscSF/

**Contents:**
- Star Forest Communication (PetscSF)#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Single list of manual pages#

PetscSF provides an interface to “star forest” communication patterns that form much of the distributed memory communication in PETSc.

PetscSFDuplicateOption

PetscSFBcastWithMemTypeBegin

PetscSFCreateFromLayouts

PetscSFCreateStridedSF

PetscSFGetGraphLayout

PetscSFReduceWithMemTypeBegin

PetscSFSetFromOptions

PetscSFSetGraphLayout

PetscSFSetGraphWithPattern

PetscSFViewFromOptions

PetscSFComputeDegreeBegin

PetscSFConcatenateRootMode

PetscSFCreateByMatchingIndices

PetscSFCreateEmbeddedLeafSF

PetscSFCreateEmbeddedRootSF

PetscSFCreateInverseSF

PetscSFCreateSectionSF

PetscSFDeregisterPersistent

PetscSFDistributeSection

PetscSFFetchAndOpBegin

PetscSFFetchAndOpWithMemTypeBegin

PetscSFRegisterPersistent

PetscSFSetGraphFromCoordinates

PetscSFWindowFlavorType

PetscSFWindowGetFlavorType

PetscSFWindowGetSyncType

PetscSFWindowSetFlavorType

PetscSFWindowSetSyncType

PetscSFWindowSyncType

PetscSFComposeInverse

PetscSFComputeDegreeEnd

PetscSFComputeMultiRootOriginalNumbering

PetscSFCreateRemoteOffsets

PetscSFFinalizePackage

PetscSFInitializePackage

PetscSFSetGraphSection

PetscSFBcastWithMemTypeBegin

PetscSFComposeInverse

PetscSFComputeDegreeBegin

PetscSFComputeDegreeEnd

PetscSFComputeMultiRootOriginalNumbering

PetscSFConcatenateRootMode

PetscSFCreateByMatchingIndices

PetscSFCreateEmbeddedLeafSF

PetscSFCreateEmbeddedRootSF

PetscSFCreateFromLayouts

PetscSFCreateInverseSF

PetscSFCreateRemoteOffsets

PetscSFCreateSectionSF

PetscSFCreateStridedSF

PetscSFDeregisterPersistent

PetscSFDistributeSection

PetscSFDuplicateOption

PetscSFFetchAndOpBegin

PetscSFFetchAndOpWithMemTypeBegin

PetscSFFinalizePackage

PetscSFGetGraphLayout

PetscSFInitializePackage

PetscSFReduceWithMemTypeBegin

PetscSFRegisterPersistent

PetscSFSetFromOptions

PetscSFSetGraphFromCoordinates

PetscSFSetGraphLayout

PetscSFSetGraphSection

PetscSFSetGraphWithPattern

PetscSFViewFromOptions

PetscSFWindowFlavorType

PetscSFWindowGetFlavorType

PetscSFWindowGetSyncType

PetscSFWindowSetFlavorType

PetscSFWindowSetSyncType

PetscSFWindowSyncType

Data Layout and Communication

Section Data Layout (PetscSection)

---

## VecScatterType#

**URL:** https://petsc.org/release/manualpages/PetscSF/VecScatterType/

**Contents:**
- VecScatterType#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#

String with the name of a PETSc vector scatter type

This is an alias for PetscSFType

PetscSF - an alternative to low-level MPI calls for data communication, PetscSFType, VecScatterSetType(), VecScatter, VecScatterCreate(), VecScatterDestroy()

include/petscsftypes.h

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef PetscSFType VecScatterType;
```

Example 2 (unknown):
```unknown
PetscSFType
```

Example 3 (unknown):
```unknown
PetscSFType
```

Example 4 (unknown):
```unknown
VecScatterSetType()
```

---

## VecScatter#

**URL:** https://petsc.org/release/manualpages/PetscSF/VecScatter/

**Contents:**
- VecScatter#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Object used to manage communication of data between vectors in parallel or between parallel and sequential vectors. Manages both scatters and gathers

This is an alias for PetscSF.

PetscSF - an alternative to low-level MPI calls for data communication, Vec, PetscSF, VecScatterCreate(), VecScatterBegin(), VecScatterEnd()

include/petscsftypes.h

src/tao/constrained/tutorials/ex1.c src/ksp/ksp/tutorials/ex73.c src/tao/pde_constrained/tutorials/elliptic.c src/tao/pde_constrained/tutorials/parabolic.c src/ksp/ksp/tutorials/ex49.c src/vec/vec/utils/tagger/tutorials/ex1.c src/ksp/ksp/tutorials/ex43.c src/tao/pde_constrained/tutorials/hyperbolic.c src/vec/vec/tutorials/ex44.c

Index of all PetscSF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef PetscSF VecScatter;
```

Example 2 (unknown):
```unknown
VecScatterCreate()
```

Example 3 (unknown):
```unknown
VecScatterBegin()
```

Example 4 (unknown):
```unknown
VecScatterEnd()
```

---
