# Petsc-Docs-Full-Raw - Structured Meshes

**Pages:** 209

---

## DMCompositeAddDM#

**URL:** https://petsc.org/release/manualpages/DMComposite/DMCompositeAddDM/

**Contents:**
- DMCompositeAddDM#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

adds a DM vector to a DMCOMPOSITE

dmc - the DMCOMPOSITE object

DMCOMPOSITE, DM, DMDestroy(), DMCompositeGather(), DMCreateGlobalVector(), DMCompositeScatter(), DMCompositeCreate(), DMCompositeGetISLocalToGlobalMappings(), DMCompositeGetAccess(), DMCompositeGetLocalVectors(), DMCompositeRestoreLocalVectors(), DMCompositeGetEntries()

src/dm/impls/composite/pack.c

src/snes/tutorials/ex28.c src/ts/tutorials/ex14.c src/snes/tutorials/ex21.c src/snes/tutorials/ex73f90t.F90 src/snes/tutorials/ex22.c

Index of all DMComposite routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCOMPOSITE
```

Example 2 (unknown):
```unknown
#include "petscdmcomposite.h"  
PetscErrorCode DMCompositeAddDM(DM dmc, DM dm)
```

Example 3 (unknown):
```unknown
DMCOMPOSITE
```

Example 4 (unknown):
```unknown
DMCOMPOSITE
```

---

## DMCompositeCreate#

**URL:** https://petsc.org/release/manualpages/DMComposite/DMCompositeCreate/

**Contents:**
- DMCompositeCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Creates a DMCOMPOSITE, used to generate “composite” vectors made up of several subvectors.

comm - the processors that will share the global vector

packer - the DMCOMPOSITE object

DMCOMPOSITE, DM, DMDestroy(), DMCompositeAddDM(), DMCompositeScatter(), DMCreate(), DMCompositeGather(), DMCreateGlobalVector(), DMCompositeGetISLocalToGlobalMappings(), DMCompositeGetAccess(), DMCompositeGetLocalVectors(), DMCompositeRestoreLocalVectors(), DMCompositeGetEntries()

src/dm/impls/composite/pack.c

src/snes/tutorials/ex28.c src/ts/tutorials/ex14.c src/snes/tutorials/ex21.c src/snes/tutorials/ex73f90t.F90 src/snes/tutorials/ex22.c

Index of all DMComposite routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCOMPOSITE
```

Example 2 (unknown):
```unknown
#include "petscdmcomposite.h"  
PetscErrorCode DMCompositeCreate(MPI_Comm comm, DM *packer)
```

Example 3 (unknown):
```unknown
DMCOMPOSITE
```

Example 4 (unknown):
```unknown
DMCOMPOSITE
```

---

## DMCompositeGatherArray#

**URL:** https://petsc.org/release/manualpages/DMComposite/DMCompositeGatherArray/

**Contents:**
- DMCompositeGatherArray#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Gathers into a global packed vector from its individual local vectors

dm - the DMCOMPOSITE object

gvec - the global vector

imode - INSERT_VALUES or ADD_VALUES

lvecs - the individual sequential vectors, NULL for any that are not needed

This is a non-variadic alternative to DMCompositeGather().

DMCOMPOSITE, DM, DMDestroy(), DMCompositeAddDM(), DMCreateGlobalVector(), DMCompositeScatter(), DMCompositeCreate(), DMCompositeGetISLocalToGlobalMappings(), DMCompositeGetAccess(), DMCompositeGetLocalVectors(), DMCompositeRestoreLocalVectors(), DMCompositeGetEntries()

src/dm/impls/composite/pack.c

Index of all DMComposite routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmcomposite.h"  
PetscErrorCode DMCompositeGatherArray(DM dm, InsertMode imode, Vec gvec, Vec *lvecs)
```

Example 2 (unknown):
```unknown
DMCOMPOSITE
```

Example 3 (unknown):
```unknown
INSERT_VALUES
```

Example 4 (unknown):
```unknown
DMCompositeGather()
```

---

## DMCompositeGather#

**URL:** https://petsc.org/release/manualpages/DMComposite/DMCompositeGather/

**Contents:**
- DMCompositeGather#
- Synopsis#
- Input Parameters#
- Fortran Notes#
- See Also#
- Level#
- Location#
- Examples#

Gathers into a global packed vector from its individual local vectors

dm - the DMCOMPOSITE object

imode - INSERT_VALUES or ADD_VALUES

gvec - the global vector

… - the individual sequential vectors, NULL for any that are not needed

Fortran users should use DMCompositeGatherArray()

DMCOMPOSITE, DM, DMDestroy(), DMCompositeAddDM(), DMCreateGlobalVector(), DMCompositeScatter(), DMCompositeCreate(), DMCompositeGetISLocalToGlobalMappings(), DMCompositeGetAccess(), DMCompositeGetLocalVectors(), DMCompositeRestoreLocalVectors(), DMCompositeGetEntries()

src/dm/impls/composite/pack.c

src/snes/tutorials/ex21.c

Index of all DMComposite routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (lua):
```lua
#include "petscdmcomposite.h"  
PetscErrorCode DMCompositeGather(DM dm, InsertMode imode, Vec gvec, ...)
```

Example 2 (unknown):
```unknown
DMCOMPOSITE
```

Example 3 (unknown):
```unknown
INSERT_VALUES
```

Example 4 (unknown):
```unknown
DMCompositeGatherArray()
```

---

## DMCompositeGetAccessArray#

**URL:** https://petsc.org/release/manualpages/DMComposite/DMCompositeGetAccessArray/

**Contents:**
- DMCompositeGetAccessArray#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Allows one to access the individual packed vectors in their global representation.

nwanted - number of vectors wanted

wanted - sorted array of integers indicating thde vectors wanted, or NULL to get all vectors, length nwanted

vecs - array of requested global vectors (must be previously allocated and of length nwanted)

Use DMCompositeRestoreAccessArray() to return the vectors when you no longer need them

DMCOMPOSITE, DM, DMCompositeGetAccess(), DMCompositeGetEntries(), DMCompositeScatter(), DMCompositeGather()

src/dm/impls/composite/pack.c

src/snes/tutorials/ex73f90t.F90 src/ts/utils/dmplexlandau/tutorials/ex2.c src/ts/utils/dmplexlandau/tutorials/ex1.c

Index of all DMComposite routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmcomposite.h"  
PetscErrorCode DMCompositeGetAccessArray(DM dm, Vec pvec, PetscInt nwanted, const PetscInt wanted[], Vec vecs[])
```

Example 2 (unknown):
```unknown
DMCOMPOSITE
```

Example 3 (unknown):
```unknown
DMCompositeRestoreAccessArray()
```

Example 4 (unknown):
```unknown
DMCOMPOSITE
```

---

## DMCompositeGetAccess#

**URL:** https://petsc.org/release/manualpages/DMComposite/DMCompositeGetAccess/

**Contents:**
- DMCompositeGetAccess#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Allows one to access the individual packed vectors in their global representation.

dm - the DMCOMPOSITE object

gvec - the global vector

… - the packed parallel vectors, NULL for those that are not needed

Use DMCompositeRestoreAccess() to return the vectors when you no longer need them

DMCOMPOSITE, DM, DMCompositeGetEntries(), DMCompositeScatter()

src/dm/impls/composite/pack.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex22.c src/ts/tutorials/ex14.c src/snes/tutorials/ex21.c

Index of all DMComposite routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (lua):
```lua
#include "petscdmcomposite.h"  
PetscErrorCode DMCompositeGetAccess(DM dm, Vec gvec, ...)
```

Example 2 (unknown):
```unknown
DMCOMPOSITE
```

Example 3 (unknown):
```unknown
DMCompositeRestoreAccess()
```

Example 4 (unknown):
```unknown
DMCOMPOSITE
```

---

## DMCompositeGetEntriesArray#

**URL:** https://petsc.org/release/manualpages/DMComposite/DMCompositeGetEntriesArray/

**Contents:**
- DMCompositeGetEntriesArray#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the DM for each entry in a DMCOMPOSITE

dm - the DMCOMPOSITE object

dms - array of sufficient length (see DMCompositeGetNumberDM()) to hold the individual DM

DMCOMPOSITE, DM, DMDestroy(), DMCompositeAddDM(), DMCreateGlobalVector(), DMCompositeGetEntries(), DMCompositeGather(), DMCompositeCreate(), DMCompositeGetISLocalToGlobalMappings(), DMCompositeGetAccess(), DMCompositeRestoreLocalVectors(), DMCompositeGetLocalVectors(), DMCompositeScatter()

src/dm/impls/composite/pack.c

Index of all DMComposite routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCOMPOSITE
```

Example 2 (unknown):
```unknown
#include "petscdmcomposite.h"  
PetscErrorCode DMCompositeGetEntriesArray(DM dm, DM dms[])
```

Example 3 (unknown):
```unknown
DMCOMPOSITE
```

Example 4 (unknown):
```unknown
DMCompositeGetNumberDM()
```

---

## DMCompositeGetEntries#

**URL:** https://petsc.org/release/manualpages/DMComposite/DMCompositeGetEntries/

**Contents:**
- DMCompositeGetEntries#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Fortran Notes#
- See Also#
- Level#
- Location#
- Examples#

Gets the DM for each entry in a DMCOMPOSITE.

dm - the DMCOMPOSITE object

… - the individual entries DM

Use DMCompositeGetEntriesArray()

DMCOMPOSITE, DM, DMDestroy(), DMCompositeAddDM(), DMCreateGlobalVector(), DMCompositeGetEntriesArray() DMCompositeGather(), DMCompositeCreate(), DMCompositeGetISLocalToGlobalMappings(), DMCompositeGetAccess(), DMCompositeRestoreLocalVectors(), DMCompositeGetLocalVectors(), DMCompositeScatter()

src/dm/impls/composite/pack.c

src/snes/tutorials/ex28.c src/ts/tutorials/ex14.c src/snes/tutorials/ex22.c

Index of all DMComposite routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCOMPOSITE
```

Example 2 (lua):
```lua
#include "petscdmcomposite.h"  
PetscErrorCode DMCompositeGetEntries(DM dm, ...)
```

Example 3 (unknown):
```unknown
DMCOMPOSITE
```

Example 4 (unknown):
```unknown
DMCompositeGetEntriesArray()
```

---

## DMCompositeGetGlobalISs#

**URL:** https://petsc.org/release/manualpages/DMComposite/DMCompositeGetGlobalISs/

**Contents:**
- DMCompositeGetGlobalISs#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Gets the index sets for each composed object in a DMCOMPOSITE

dm - the DMCOMPOSITE object

is - the array of index sets

The is entries should be destroyed with ISDestroy(), is should be freed with PetscFree()

These could be used to extract a subset of vector entries for a “multi-physics” preconditioner

Use DMCompositeGetLocalISs() for index sets in the packed local numbering, and DMCompositeGetISLocalToGlobalMappings() for to map local sub-DM (including ghost) indices to packed global indices.

Use DMCompositeRestoreGlobalISs() to release the is.

DMCOMPOSITE, DM, DMDestroy(), DMCompositeAddDM(), DMCreateGlobalVector(), DMCompositeGather(), DMCompositeCreate(), DMCompositeGetAccess(), DMCompositeScatter(), DMCompositeGetLocalVectors(), DMCompositeRestoreLocalVectors(), DMCompositeGetEntries()

src/dm/impls/composite/pack.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex73f90t.F90

Index of all DMComposite routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCOMPOSITE
```

Example 2 (unknown):
```unknown
#include "petscdmcomposite.h"  
PetscErrorCode DMCompositeGetGlobalISs(DM dm, IS *is[])
```

Example 3 (unknown):
```unknown
DMCOMPOSITE
```

Example 4 (unknown):
```unknown
ISDestroy()
```

---

## DMCompositeGetISLocalToGlobalMappings#

**URL:** https://petsc.org/release/manualpages/DMComposite/DMCompositeGetISLocalToGlobalMappings/

**Contents:**
- DMCompositeGetISLocalToGlobalMappings#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

gets an ISLocalToGlobalMapping for each DM in the DMCOMPOSITE, maps to the composite global space

Collective; No Fortran Support

dm - the DMCOMPOSITE object

ltogs - the individual mappings for each packed vector. Note that this includes all the ghost points that individual ghosted DMDA may have.

Each entry of ltogs should be destroyed with ISLocalToGlobalMappingDestroy(), ltogs should be freed with PetscFree().

DMCOMPOSITE, DM, DMDestroy(), DMCompositeAddDM(), DMCreateGlobalVector(), DMCompositeGather(), DMCompositeCreate(), DMCompositeGetAccess(), DMCompositeScatter(), DMCompositeGetLocalVectors(), DMCompositeRestoreLocalVectors(), DMCompositeGetEntries()

src/dm/impls/composite/pack.c

Index of all DMComposite routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 2 (unknown):
```unknown
DMCOMPOSITE
```

Example 3 (unknown):
```unknown
#include "petscdmcomposite.h"  
PetscErrorCode DMCompositeGetISLocalToGlobalMappings(DM dm, ISLocalToGlobalMapping *ltogs[])
```

Example 4 (unknown):
```unknown
DMCOMPOSITE
```

---

## DMCompositeGetLocalAccessArray#

**URL:** https://petsc.org/release/manualpages/DMComposite/DMCompositeGetLocalAccessArray/

**Contents:**
- DMCompositeGetLocalAccessArray#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Allows one to access the individual packed vectors in their local representation.

nwanted - number of vectors wanted

wanted - sorted array of vectors wanted, or NULL to get all vectors, length nwanted

vecs - array of requested local vectors (must be allocated and of length nwanted)

Use DMCompositeRestoreLocalAccessArray() to return the vectors when you no longer need them.

DMCOMPOSITE, DM, DMCompositeRestoreLocalAccessArray(), DMCompositeGetAccess(), DMCompositeGetEntries(), DMCompositeScatter(), DMCompositeGather()

src/dm/impls/composite/pack.c

Index of all DMComposite routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmcomposite.h"  
PetscErrorCode DMCompositeGetLocalAccessArray(DM dm, Vec pvec, PetscInt nwanted, const PetscInt wanted[], Vec vecs[])
```

Example 2 (unknown):
```unknown
DMCOMPOSITE
```

Example 3 (unknown):
```unknown
DMCompositeRestoreLocalAccessArray()
```

Example 4 (unknown):
```unknown
DMCOMPOSITE
```

---

## DMCompositeGetLocalISs#

**URL:** https://petsc.org/release/manualpages/DMComposite/DMCompositeGetLocalISs/

**Contents:**
- DMCompositeGetLocalISs#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Gets index sets for each component of a composite local vector

Not Collective; No Fortran Support

is - array of serial index sets for each component of the DMCOMPOSITE

At present, a composite local vector does not normally exist. This function is used to provide index sets for MatGetLocalSubMatrix(). In the future, the scatters for each entry in the DMCOMPOSITE may be merged into a single scatter to a composite local vector. The user should not typically need to know which is being done.

To get the composite global indices at all local points (including ghosts), use DMCompositeGetISLocalToGlobalMappings().

To get index sets for pieces of the composite global vector, use DMCompositeGetGlobalISs().

Each returned IS should be destroyed with ISDestroy(), the array should be freed with PetscFree().

Use DMCompositeRestoreLocalISs() to release the is.

DMCOMPOSITE, DM, DMCompositeGetGlobalISs(), DMCompositeGetISLocalToGlobalMappings(), MatGetLocalSubMatrix(), MatCreateLocalRef(), DMCompositeGetNumberDM()

src/dm/impls/composite/pack.c

src/snes/tutorials/ex28.c src/ts/tutorials/ex14.c

Index of all DMComposite routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmcomposite.h"  
PetscErrorCode DMCompositeGetLocalISs(DM dm, IS *is[])
```

Example 2 (unknown):
```unknown
DMCOMPOSITE
```

Example 3 (unknown):
```unknown
DMCOMPOSITE
```

Example 4 (unknown):
```unknown
MatGetLocalSubMatrix()
```

---

## DMCompositeGetLocalVectors#

**URL:** https://petsc.org/release/manualpages/DMComposite/DMCompositeGetLocalVectors/

**Contents:**
- DMCompositeGetLocalVectors#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Gets local vectors for each part of a DMCOMPOSITE Use DMCompositeRestoreLocalVectors() to return them.

Not Collective; No Fortran Support

dm - the DMCOMPOSITE object

… - the individual sequential Vecs

DMCOMPOSITE, DM, DMDestroy(), DMCompositeAddDM(), DMCreateGlobalVector(), DMCompositeGather(), DMCompositeCreate(), DMCompositeGetISLocalToGlobalMappings(), DMCompositeGetAccess(), DMCompositeRestoreLocalVectors(), DMCompositeScatter(), DMCompositeGetEntries()

src/dm/impls/composite/pack.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex22.c src/ts/tutorials/ex14.c src/snes/tutorials/ex21.c

Index of all DMComposite routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCOMPOSITE
```

Example 2 (unknown):
```unknown
DMCompositeRestoreLocalVectors()
```

Example 3 (lua):
```lua
#include "petscdmcomposite.h"  
PetscErrorCode DMCompositeGetLocalVectors(DM dm, ...)
```

Example 4 (unknown):
```unknown
DMCOMPOSITE
```

---

## DMCompositeGetNumberDM#

**URL:** https://petsc.org/release/manualpages/DMComposite/DMCompositeGetNumberDM/

**Contents:**
- DMCompositeGetNumberDM#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Gets the number of DM objects in the DMCOMPOSITE representation.

dm - the DMCOMPOSITE object

nDM - the number of DM

src/dm/impls/composite/pack.c

src/ts/utils/dmplexlandau/tutorials/ex2.c src/ts/utils/dmplexlandau/tutorials/ex1.c

Index of all DMComposite routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCOMPOSITE
```

Example 2 (unknown):
```unknown
#include "petscdmcomposite.h"  
PetscErrorCode DMCompositeGetNumberDM(DM dm, PetscInt *nDM)
```

Example 3 (unknown):
```unknown
DMCOMPOSITE
```

Example 4 (unknown):
```unknown
DMCOMPOSITE
```

---

## DMCompositeRestoreAccessArray#

**URL:** https://petsc.org/release/manualpages/DMComposite/DMCompositeRestoreAccessArray/

**Contents:**
- DMCompositeRestoreAccessArray#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Returns the vectors obtained with DMCompositeGetAccessArray()

dm - the DMCOMPOSITE object

nwanted - number of vectors wanted

wanted - sorted array of vectors wanted, or NULL to restore all vectors

vecs - array of global vectors

DMCOMPOSITE, DM, DMCompositeRestoreAccess(), DMCompositeRestoreEntries(), DMCompositeScatter(), DMCompositeGather()

src/dm/impls/composite/pack.c

src/snes/tutorials/ex73f90t.F90 src/ts/utils/dmplexlandau/tutorials/ex2.c src/ts/utils/dmplexlandau/tutorials/ex1.c

Index of all DMComposite routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCompositeGetAccessArray()
```

Example 2 (unknown):
```unknown
#include "petscdmcomposite.h"  
PetscErrorCode DMCompositeRestoreAccessArray(DM dm, Vec pvec, PetscInt nwanted, const PetscInt wanted[], Vec vecs[])
```

Example 3 (unknown):
```unknown
DMCOMPOSITE
```

Example 4 (unknown):
```unknown
DMCOMPOSITE
```

---

## DMCompositeRestoreAccess#

**URL:** https://petsc.org/release/manualpages/DMComposite/DMCompositeRestoreAccess/

**Contents:**
- DMCompositeRestoreAccess#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Returns the vectors obtained with DMCompositeGetAccess() representation.

dm - the DMCOMPOSITE object

gvec - the global vector

… - the individual parallel vectors, NULL for those that are not needed

DMCOMPOSITE, DM, DMCompositeAddDM(), DMCreateGlobalVector(), DMCompositeGather(), DMCompositeCreate(), DMCompositeGetISLocalToGlobalMappings(), DMCompositeScatter(), DMCompositeGetAccess()

src/dm/impls/composite/pack.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex22.c src/ts/tutorials/ex14.c src/snes/tutorials/ex21.c

Index of all DMComposite routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCompositeGetAccess()
```

Example 2 (lua):
```lua
#include "petscdmcomposite.h"  
PetscErrorCode DMCompositeRestoreAccess(DM dm, Vec gvec, ...)
```

Example 3 (unknown):
```unknown
DMCOMPOSITE
```

Example 4 (unknown):
```unknown
DMCOMPOSITE
```

---

## DMCompositeRestoreLocalAccessArray#

**URL:** https://petsc.org/release/manualpages/DMComposite/DMCompositeRestoreLocalAccessArray/

**Contents:**
- DMCompositeRestoreLocalAccessArray#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Returns the vectors obtained with DMCompositeGetLocalAccessArray().

dm - the DMCOMPOSITE object

nwanted - number of vectors wanted

wanted - sorted array of vectors wanted, or NULL to restore all vectors

vecs - array of local vectors

nwanted and wanted must match the values given to DMCompositeGetLocalAccessArray() otherwise the call will fail.

DMCOMPOSITE, DM, DMCompositeGetLocalAccessArray(), DMCompositeRestoreAccessArray(), DMCompositeRestoreAccess(), DMCompositeRestoreEntries(), DMCompositeScatter(), DMCompositeGather()

src/dm/impls/composite/pack.c

Index of all DMComposite routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCompositeGetLocalAccessArray()
```

Example 2 (unknown):
```unknown
#include "petscdmcomposite.h"  
PetscErrorCode DMCompositeRestoreLocalAccessArray(DM dm, Vec pvec, PetscInt nwanted, const PetscInt wanted[], Vec *vecs)
```

Example 3 (unknown):
```unknown
DMCOMPOSITE
```

Example 4 (unknown):
```unknown
DMCompositeGetLocalAccessArray()
```

---

## DMCompositeRestoreLocalVectors#

**URL:** https://petsc.org/release/manualpages/DMComposite/DMCompositeRestoreLocalVectors/

**Contents:**
- DMCompositeRestoreLocalVectors#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Restores local vectors for each part of a DMCOMPOSITE

Not Collective; No Fortran Support

dm - the DMCOMPOSITE object

… - the individual sequential Vec

DMCOMPOSITE, DM, DMDestroy(), DMCompositeAddDM(), DMCreateGlobalVector(), DMCompositeGather(), DMCompositeCreate(), DMCompositeGetISLocalToGlobalMappings(), DMCompositeGetAccess(), DMCompositeGetLocalVectors(), DMCompositeScatter(), DMCompositeGetEntries()

src/dm/impls/composite/pack.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex22.c src/ts/tutorials/ex14.c src/snes/tutorials/ex21.c

Index of all DMComposite routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCOMPOSITE
```

Example 2 (lua):
```lua
#include "petscdmcomposite.h"  
PetscErrorCode DMCompositeRestoreLocalVectors(DM dm, ...)
```

Example 3 (unknown):
```unknown
DMCOMPOSITE
```

Example 4 (unknown):
```unknown
DMCOMPOSITE
```

---

## DMCompositeScatterArray#

**URL:** https://petsc.org/release/manualpages/DMComposite/DMCompositeScatterArray/

**Contents:**
- DMCompositeScatterArray#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Scatters from a global packed vector into its individual local vectors

dm - the DMCOMPOSITE object

gvec - the global vector

lvecs - array of local vectors, NULL for any that are not needed

This is a non-variadic alternative to DMCompositeScatter()

DMCOMPOSITE, DM, DMDestroy(), DMCompositeAddDM(), DMCreateGlobalVector(), DMCompositeGather(), DMCompositeCreate(), DMCompositeGetISLocalToGlobalMappings(), DMCompositeGetAccess(), DMCompositeGetLocalVectors(), DMCompositeRestoreLocalVectors(), DMCompositeGetEntries()

src/dm/impls/composite/pack.c

Index of all DMComposite routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmcomposite.h"  
PetscErrorCode DMCompositeScatterArray(DM dm, Vec gvec, Vec *lvecs)
```

Example 2 (unknown):
```unknown
DMCOMPOSITE
```

Example 3 (unknown):
```unknown
DMCompositeScatter()
```

Example 4 (unknown):
```unknown
DMCOMPOSITE
```

---

## DMCompositeScatter#

**URL:** https://petsc.org/release/manualpages/DMComposite/DMCompositeScatter/

**Contents:**
- DMCompositeScatter#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Scatters from a global packed vector into its individual local vectors

dm - the DMCOMPOSITE object

gvec - the global vector

… - the individual sequential vectors, NULL for those that are not needed

DMCompositeScatterArray() is a non-variadic alternative that is often more convenient for library callers and is accessible from Fortran.

DMCOMPOSITE, DM, DMDestroy(), DMCompositeAddDM(), DMCreateGlobalVector(), DMCompositeGather(), DMCompositeCreate(), DMCompositeGetISLocalToGlobalMappings(), DMCompositeGetAccess(), DMCompositeGetLocalVectors(), DMCompositeRestoreLocalVectors(), DMCompositeGetEntries() DMCompositeScatterArray()

src/dm/impls/composite/pack.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex22.c src/ts/tutorials/ex14.c src/snes/tutorials/ex21.c

Index of all DMComposite routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (lua):
```lua
#include "petscdmcomposite.h"  
PetscErrorCode DMCompositeScatter(DM dm, Vec gvec, ...)
```

Example 2 (unknown):
```unknown
DMCOMPOSITE
```

Example 3 (unknown):
```unknown
DMCompositeScatterArray()
```

Example 4 (unknown):
```unknown
DMCOMPOSITE
```

---

## DMCompositeSetCoupling#

**URL:** https://petsc.org/release/manualpages/DMComposite/DMCompositeSetCoupling/

**Contents:**
- DMCompositeSetCoupling#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Sets user provided routines that compute the coupling between the separate components DM in a DMCOMPOSITE to build the correct matrix nonzero structure.

Logically Collective; No Fortran Support

dm - the composite object

FormCoupleLocations - routine to set the nonzero locations in the matrix

See DMSetApplicationContext() and DMGetApplicationContext() for how to get user information into this routine

The provided function should have a signature matching

dm - the composite object

J - the constructed matrix, or NULL. If provided, the function should fill the existing nonzero pattern with zeros (only dm and rstart are valid in this case).

dnz - array counting the number of on-diagonal non-zero entries per row, where on-diagonal means that this process owns both the row and column

onz - array counting the number of off-diagonal non-zero entries per row, where off-diagonal means that this process owns the row

rstart - offset into *nz arrays, for local row index r, update onz[r - rstart] or dnz[r - rstart]

nrows - number of owned global rows

start - the first owned global index

end - the last owned global index + 1

If J is not NULL, then the only other valid parameter is rstart

The user coupling function has a weird and poorly documented interface and is not tested, it should be removed

src/dm/impls/composite/pack.c

Index of all DMComposite routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCOMPOSITE
```

Example 2 (unknown):
```unknown
#include "petscdmcomposite.h"  
PetscErrorCode DMCompositeSetCoupling(DM dm, PetscErrorCode (*FormCoupleLocations)(DM, Mat, PetscInt *, PetscInt *, PetscInt, PetscInt, PetscInt, PetscInt))
```

Example 3 (unknown):
```unknown
DMSetApplicationContext()
```

Example 4 (unknown):
```unknown
DMGetApplicationContext()
```

---

## DMCOMPOSITE#

**URL:** https://petsc.org/release/manualpages/DMComposite/DMCOMPOSITE/

**Contents:**
- DMCOMPOSITE#
- See Also#
- Level#
- Location#

“composite” - A DM object that is used to manage data for a collection of DM

DMType, DM, DMDACreate(), DMCreate(), DMSetType(), DMCompositeCreate()

src/dm/impls/composite/pack.c

Index of all DMComposite routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDACreate()
```

Example 2 (unknown):
```unknown
DMSetType()
```

Example 3 (unknown):
```unknown
DMCompositeCreate()
```

---

## DMComposite#

**URL:** https://petsc.org/release/manualpages/DMComposite/

**Contents:**
- DMComposite#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- No developer routines#
- Single list of manual pages#

Used to manage the use of multple DM

DMCompositeGetNumberDM

DMCompositeGetLocalISs

DMCompositeGatherArray

DMCompositeGetAccessArray

DMCompositeGetEntries

DMCompositeGetEntriesArray

DMCompositeGetGlobalISs

DMCompositeGetISLocalToGlobalMappings

DMCompositeGetLocalAccessArray

DMCompositeGetLocalVectors

DMCompositeRestoreAccess

DMCompositeRestoreAccessArray

DMCompositeRestoreLocalAccessArray

DMCompositeRestoreLocalVectors

DMCompositeScatterArray

DMCompositeSetCoupling

DMCompositeGatherArray

DMCompositeGetAccessArray

DMCompositeGetEntries

DMCompositeGetEntriesArray

DMCompositeGetGlobalISs

DMCompositeGetISLocalToGlobalMappings

DMCompositeGetLocalAccessArray

DMCompositeGetLocalISs

DMCompositeGetLocalVectors

DMCompositeGetNumberDM

DMCompositeRestoreAccess

DMCompositeRestoreAccessArray

DMCompositeRestoreLocalAccessArray

DMCompositeRestoreLocalVectors

DMCompositeScatterArray

DMCompositeSetCoupling

Tensor products of meshes (DMRODUCT)

Discretization and Function Spaces

---

## DMCreateAggregates#

**URL:** https://petsc.org/release/manualpages/DMDA/DMCreateAggregates/

**Contents:**
- DMCreateAggregates#
- Synopsis#
- Level#
- Location#

Deprecated, see DMDACreateAggregates.

src/dm/impls/da/dainterp.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMCreateAggregates(DM dac, DM daf, Mat *mat)
```

---

## DMDAConvertToCell#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAConvertToCell/

**Contents:**
- DMDAConvertToCell#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Convert a (i,j,k) location in a DMDA to its local cell or vertex number

s - a MatStencil that provides (i,j,k)

cell - the local cell or vertext number

The (i,j,k) are in the local numbering of the DMDA. That is they are non-negative offsets to the ghost corners returned by DMDAGetGhostCorners()

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAGetGhostCorners()

src/dm/impls/da/dageometry.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAConvertToCell(DM dm, MatStencil s, PetscInt *cell)
```

Example 2 (unknown):
```unknown
DMDAGetGhostCorners()
```

Example 3 (unknown):
```unknown
DMDAGetGhostCorners()
```

---

## DMDACoor2d#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDACoor2d/

**Contents:**
- DMDACoor2d#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#

Structure for holding 2d (x and y) coordinates when working with DMDA

DM Basics, DMDA, DMDACoor3d, DMDAVecRestoreArray(), DMDAVecGetArray(), DMGetCoordinateDM(), DMGetCoordinates()

src/snes/tutorials/ex55.c src/snes/tutorials/ex5.c src/ksp/ksp/tutorials/ex70.c src/snes/tutorials/ex46.c src/ksp/ksp/tutorials/ex49.c src/dm/tutorials/swarm_ex1.c src/dm/tutorials/ex3.c src/ksp/ksp/tutorials/ex43.c src/snes/tutorials/ex55k.kokkos.cxx

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (sass):
```sass
.vb
DMDACoor2d **coors;
Vec      vcoors;
DM       cda;
DMGetCoordinates(da,&vcoors);
DMGetCoordinateDM(da,&cda);
DMDAVecGetArray(cda,vcoors,&coors);
DMDAGetCorners(cda,&mstart,&nstart,0,&m,&n,0)
for (i=mstart; i<mstart+m; i++) {
for (j=nstart; j<nstart+n; j++) {
x = coors[j][i].x;
y = coors[j][i].y;
......
}
}
DMDAVecRestoreArray(dac,vcoors,&coors);
.ve
```

Example 2 (unknown):
```unknown
DMDAVecRestoreArray()
```

Example 3 (unknown):
```unknown
DMDAVecGetArray()
```

Example 4 (unknown):
```unknown
DMGetCoordinateDM()
```

---

## DMDACoor3d#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDACoor3d/

**Contents:**
- DMDACoor3d#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#

Structure for holding 3d (x, y and z) coordinates coordinates when working with DMDA

DM Basics, DMDA, DMDACoor2d, DMDAVecRestoreArray(), DMDAVecGetArray(), DMGetCoordinateDM(), DMGetCoordinates()

src/dm/tutorials/ex3.c src/ksp/ksp/tutorials/ex42.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (sass):
```sass
.vb
DMDACoor3d ***coors;
Vec      vcoors;
DM       cda;
DMGetCoordinates(da,&vcoors);
DMGetCoordinateDM(da,&cda);
DMDAVecGetArray(cda,vcoors,&coors);
DMDAGetCorners(cda,&mstart,&nstart,&pstart,&m,&n,&p)
for (i=mstart; i<mstart+m; i++) {
for (j=nstart; j<nstart+n; j++) {
for (k=pstart; k<pstart+p; k++) {
x = coors[k][j][i].x;
y = coors[k][j][i].y;
z = coors[k][j][i].z;
......
}
}
DMDAVecRestoreArray(dac,vcoors,&coors);
.ve
```

Example 2 (unknown):
```unknown
DMDAVecRestoreArray()
```

Example 3 (unknown):
```unknown
DMDAVecGetArray()
```

Example 4 (unknown):
```unknown
DMGetCoordinateDM()
```

---

## DMDACreate1d#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDACreate1d/

**Contents:**
- DMDACreate1d#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates an object that will manage the communication of one-dimensional regular array data that is distributed across one or mpre MPI processes.

comm - MPI communicator

bx - type of ghost cells at the boundary the array should have, if any. Use DM_BOUNDARY_NONE, DM_BOUNDARY_GHOSTED, or DM_BOUNDARY_PERIODIC.

M - global dimension of the array (that is the number of grid points)

dof - number of degrees of freedom per node

lx - array containing number of nodes in the X direction on each processor, or NULL. If non-null, must be of length as the number of processes in the MPI_Comm. The sum of these entries must equal M

da - the resulting distributed array object

-dm_view - Calls DMView() at the conclusion of DMDACreate1d()

-da_grid_x nx - number of grid points in the x direction

-da_refine_x rx - refinement factor

-da_refine n - refine the DMDA n times before creating it

The array data itself is NOT stored in the DMDA, it is stored in Vec objects; The appropriate vector objects can be obtained with calls to DMCreateGlobalVector() and DMCreateLocalVector() and calls to VecDuplicate() if more are needed.

You must call DMSetUp() after this call before using this DM.

If you wish to use the options database to change values in the DMDA call DMSetFromOptions() after this call but before DMSetUp().

DMDA - Creating vectors for structured grids, DMDA, DM, DMDestroy(), DMView(), DMDACreate2d(), DMDACreate3d(), DMGlobalToLocalBegin(), DMDASetRefinementFactor(), DMGlobalToLocalEnd(), DMLocalToGlobalBegin(), DMLocalToLocalBegin(), DMLocalToLocalEnd(), DMDAGetRefinementFactor(), DMDAGetInfo(), DMCreateGlobalVector(), DMCreateLocalVector(), DMDACreateNaturalVector(), DMLoad(), DMDAGetOwnershipRanges(), DMStagCreate1d(), DMBoundaryType

src/dm/impls/da/da1.c

src/snes/tutorials/ex21.c src/snes/tutorials/ex28.c src/snes/tutorials/ex3k.kokkos.cxx src/snes/tutorials/ex3.c src/snes/tutorials/ex78.c src/snes/tutorials/ex33.c src/snes/tutorials/ex22.c src/ksp/ksp/tutorials/ex65.c src/ksp/ksp/tutorials/ex28.c src/ksp/ksp/tutorials/ex67.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDACreate1d(MPI_Comm comm, DMBoundaryType bx, PetscInt M, PetscInt dof, PetscInt s, const PetscInt lx[], DM *da)
```

Example 2 (unknown):
```unknown
DM_BOUNDARY_NONE
```

Example 3 (unknown):
```unknown
DM_BOUNDARY_GHOSTED
```

Example 4 (unknown):
```unknown
DM_BOUNDARY_PERIODIC
```

---

## DMDACreate2d#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDACreate2d/

**Contents:**
- DMDACreate2d#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates an object that will manage the communication of two-dimensional regular array data that is distributed across one or more MPI processes.

comm - MPI communicator

bx - type of ghost nodes the x array have. Use one of DM_BOUNDARY_NONE, DM_BOUNDARY_GHOSTED, DM_BOUNDARY_PERIODIC.

by - type of ghost nodes the y array have. Use one of DM_BOUNDARY_NONE, DM_BOUNDARY_GHOSTED, DM_BOUNDARY_PERIODIC.

stencil_type - stencil type. Use either DMDA_STENCIL_BOX or DMDA_STENCIL_STAR.

M - global dimension in the x direction of the array

N - global dimension in the y direction of the array

m - corresponding number of processors in the x dimension (or PETSC_DECIDE to have calculated)

n - corresponding number of processors in the y dimension (or PETSC_DECIDE to have calculated)

dof - number of degrees of freedom per node

lx - arrays containing the number of nodes in each cell along the x coordinates, or NULL.

ly - arrays containing the number of nodes in each cell along the y coordinates, or NULL.

da - the resulting distributed array object

-dm_view - Calls DMView() at the conclusion of DMDACreate2d()

-da_grid_x nx - number of grid points in the x direction

-da_grid_y ny - number of grid points in the y direction

-da_processors_x nx - number of processors in the x direction

-da_processors_y ny - number of processors in the y direction

-da_bd_x bx - boundary type in the x direction

-da_bd_y by - boundary type in the y direction

-da_bd_all bt - boundary type in all directions

-da_refine_x rx - refinement ratio in the x direction

-da_refine_y ry - refinement ratio in the y direction

-da_refine n - refine the DMDA n times before creating

If lx or ly are non-null, these must be of length as m and n, and the corresponding m and n cannot be PETSC_DECIDE. The sum of the lx entries must be M, and the sum of the ly entries must be N.

The stencil type DMDA_STENCIL_STAR with width 1 corresponds to the standard 5-pt stencil, while DMDA_STENCIL_BOX with width 1 denotes the standard 9-pt stencil.

The array data itself is NOT stored in the DMDA, it is stored in Vec objects; The appropriate vector objects can be obtained with calls to DMCreateGlobalVector() and DMCreateLocalVector() and calls to VecDuplicate() if more are needed.

You must call DMSetUp() after this call before using this DM.

To use the options database to change values in the DMDA call DMSetFromOptions() after this call but before DMSetUp().

DMDA - Creating vectors for structured grids, DM, DMDA, DMDestroy(), DMView(), DMDACreate1d(), DMDACreate3d(), DMGlobalToLocalBegin(), DMDAGetRefinementFactor(), DMGlobalToLocalEnd(), DMLocalToGlobalBegin(), DMLocalToLocalBegin(), DMLocalToLocalEnd(), DMDASetRefinementFactor(), DMDAGetInfo(), DMCreateGlobalVector(), DMCreateLocalVector(), DMDACreateNaturalVector(), DMLoad(), DMDAGetOwnershipRanges(), DMStagCreate2d(), DMBoundaryType

src/dm/impls/da/da2.c

src/snes/tutorials/ex5f90.F90 src/snes/tutorials/ex73f90t.F90 src/snes/tutorials/ex18.c src/snes/tutorials/ex9.c src/snes/tutorials/ex35.c src/snes/tutorials/ex40f90.F90 src/snes/tutorials/ex46.c src/snes/tutorials/ex48.c src/snes/tutorials/ex15.c src/snes/tutorials/ex4.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDACreate2d(MPI_Comm comm, DMBoundaryType bx, DMBoundaryType by, DMDAStencilType stencil_type, PetscInt M, PetscInt N, PetscInt m, PetscInt n, PetscInt dof, PetscInt s, const PetscInt lx[], const PetscInt ly[], DM *da)
```

Example 2 (unknown):
```unknown
DM_BOUNDARY_NONE
```

Example 3 (unknown):
```unknown
DM_BOUNDARY_GHOSTED
```

Example 4 (unknown):
```unknown
DM_BOUNDARY_PERIODIC
```

---

## DMDACreate3d#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDACreate3d/

**Contents:**
- DMDACreate3d#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates an object that will manage the communication of three-dimensional regular array data that is distributed across one or more MPI processes.

comm - MPI communicator

bx - type of x ghost nodes the array have. Use one of DM_BOUNDARY_NONE, DM_BOUNDARY_GHOSTED, DM_BOUNDARY_PERIODIC.

by - type of y ghost nodes the array have. Use one of DM_BOUNDARY_NONE, DM_BOUNDARY_GHOSTED, DM_BOUNDARY_PERIODIC.

bz - type of z ghost nodes the array have. Use one of DM_BOUNDARY_NONE, DM_BOUNDARY_GHOSTED, DM_BOUNDARY_PERIODIC.

stencil_type - Type of stencil (DMDA_STENCIL_STAR or DMDA_STENCIL_BOX)

M - global dimension in the x direction of the array

N - global dimension in the y direction of the array

P - global dimension in the z direction of the array

m - corresponding number of processors in the x dimension (or PETSC_DECIDE to have calculated)

n - corresponding number of processors in the y dimension (or PETSC_DECIDE to have calculated)

p - corresponding number of processors in the z dimension (or PETSC_DECIDE to have calculated)

dof - number of degrees of freedom per node

lx - arrays containing the number of nodes in each cell along the x coordinates, or NULL.

ly - arrays containing the number of nodes in each cell along the y coordinates, or NULL.

lz - arrays containing the number of nodes in each cell along the z coordinates, or NULL.

da - the resulting distributed array object

-dm_view - Calls DMView() at the conclusion of DMDACreate3d()

-da_grid_x nx - number of grid points in the x direction

-da_grid_y ny - number of grid points in the y direction

-da_grid_z nz - number of grid points in the z direction

-da_processors_x MX - number of processors in the x direction

-da_processors_y MY - number of processors in the y direction

-da_processors_z MZ - number of processors in the z direction

-da_bd_x bx - boundary type in the x direction

-da_bd_y by - boundary type in the y direction

-da_bd_z bz - boundary type in the z direction

-da_bd_all bt - boundary type in all directions

-da_refine_x rx - refinement ratio in the x direction

-da_refine_y ry - refinement ratio in the y direction

-da_refine_z rz - refinement ratio in the z direction

-da_refine n - refine the DMDA n times before creating it

If lx, ly, or lz are non-null, these must be of length as m, n, p and the corresponding m, n, or p cannot be PETSC_DECIDE. Sum of the lx entries must be M, sum of the ly must N, sum of the lz must be P.

The stencil type DMDA_STENCIL_STAR with width 1 corresponds to the standard 7-pt stencil, while DMDA_STENCIL_BOX with width 1 denotes the standard 27-pt stencil.

The array data itself is NOT stored in the DMDA, it is stored in Vec objects; The appropriate vector objects can be obtained with calls to DMCreateGlobalVector() and DMCreateLocalVector() and calls to VecDuplicate() if more are needed.

You must call DMSetUp() after this call before using this DM.

To use the options database to change values in the DMDA call DMSetFromOptions() after this call but before DMSetUp().

DMDA - Creating vectors for structured grids, DM, DMDA, DMDestroy(), DMView(), DMDACreate1d(), DMDACreate2d(), DMGlobalToLocalBegin(), DMDAGetRefinementFactor(), DMGlobalToLocalEnd(), DMLocalToGlobalBegin(), DMLocalToLocalBegin(), DMLocalToLocalEnd(), DMDASetRefinementFactor(), DMDAGetInfo(), DMCreateGlobalVector(), DMCreateLocalVector(), DMDACreateNaturalVector(), DMLoad(), DMDAGetOwnershipRanges(), DMStagCreate3d(), DMBoundaryType

src/dm/impls/da/da3.c

src/ts/tutorials/ex14.c src/snes/tutorials/ex16.c src/ksp/ksp/tutorials/ex59.c src/snes/tutorials/ex14.c src/ksp/ksp/tutorials/ex71.c src/ksp/ksp/tutorials/ex34.c src/snes/tutorials/ex48.c src/ksp/ksp/tutorials/ex42.c src/ksp/ksp/tutorials/ex45.c src/ksp/ksp/tutorials/ex22f.F90

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"    
PetscErrorCode DMDACreate3d(MPI_Comm comm, DMBoundaryType bx, DMBoundaryType by, DMBoundaryType bz, DMDAStencilType stencil_type, PetscInt M, PetscInt N, PetscInt P, PetscInt m, PetscInt n, PetscInt p, PetscInt dof, PetscInt s, const PetscInt lx[], const PetscInt ly[], const PetscInt lz[], DM *da)
```

Example 2 (unknown):
```unknown
DM_BOUNDARY_NONE
```

Example 3 (unknown):
```unknown
DM_BOUNDARY_GHOSTED
```

Example 4 (unknown):
```unknown
DM_BOUNDARY_PERIODIC
```

---

## DMDACreateAggregates#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDACreateAggregates/

**Contents:**
- DMDACreateAggregates#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the aggregates that map between grids associated with two DMDA

dac - the coarse grid DMDA

daf - the fine grid DMDA

rest - the restriction matrix (transpose of the projection matrix)

This routine is not used by PETSc. It is not clear what its use case is and it may be removed in a future release. Users should contact petsc-maint@mcs.anl.gov if they plan to use it.

DMDA - Creating vectors for structured grids, DMRefine(), DMCreateInjection(), DMCreateInterpolation()

src/dm/impls/da/dainterp.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDACreateAggregates(DM dac, DM daf, Mat *rest)
```

Example 2 (unknown):
```unknown
DMCreateInjection()
```

Example 3 (unknown):
```unknown
DMCreateInterpolation()
```

---

## DMDACreateCompatibleDMDA#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDACreateCompatibleDMDA/

**Contents:**
- DMDACreateCompatibleDMDA#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Creates a DMDA with the same layout as given DMDA but with fewer or more fields

nfields - number of fields in new DMDA

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAGetGhostCorners(), DMSetCoordinates(), DMDASetUniformCoordinates(), DMGetCoordinates(), DMDAGetGhostedCoordinates(), DMStagCreateCompatibleDMStag()

src/dm/impls/da/dacorn.c

src/ksp/ksp/tutorials/ex43.c src/ts/tutorials/ex29.c src/ksp/ksp/tutorials/ex70.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDACreateCompatibleDMDA(DM da, PetscInt nfields, DM *nda)
```

Example 2 (unknown):
```unknown
DMDAGetGhostCorners()
```

Example 3 (unknown):
```unknown
DMSetCoordinates()
```

Example 4 (unknown):
```unknown
DMDASetUniformCoordinates()
```

---

## DMDACreateNaturalVector#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDACreateNaturalVector/

**Contents:**
- DMDACreateNaturalVector#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates a parallel PETSc vector that will hold vector values in the natural numbering, rather than in the PETSc parallel numbering associated with the DMDA.

g - the distributed global vector

The natural numbering is a number of grid nodes that starts with, in three dimensions, with (0,0,0), (1,0,0), (2,0,0), …, (m-1,0,0) followed by (0,1,0), (1,1,0), (2,1,0), …, (m,1,0) etc up to (0,n-1,p-1), (1,n-1,p-1), (2,n-1,p-1), …, (m-1,n-1,p-1).

The output parameter, g, is a regular Vec that should be destroyed with a call to VecDestroy() when usage is finished.

The number of local entries in the vector on each process is the same as in a vector created with DMCreateGlobalVector().

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAGlobalToNaturalBegin(), DMDAGlobalToNaturalEnd(), DMDANaturalToGlobalBegin(), DMDANaturalToGlobalEnd(), DMCreateLocalVector(), VecDuplicate(), VecDuplicateVecs(), DMDACreate1d(), DMDACreate2d(), DMDACreate3d(), DMGlobalToLocalBegin(), DMGlobalToLocalEnd(), DMLocalToGlobalBegin()

src/dm/impls/da/dadist.c

src/dm/tutorials/ex6.c src/ksp/ksp/tutorials/ex71.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDACreateNaturalVector(DM da, Vec *g)
```

Example 2 (unknown):
```unknown
VecDestroy()
```

Example 3 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 4 (unknown):
```unknown
DMDAGlobalToNaturalBegin()
```

---

## DMDACreatePatchIS#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDACreatePatchIS/

**Contents:**
- DMDACreatePatchIS#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates an index set corresponding to a logically rectangular patch of the DMDA.

lower - a MatStencil with i, j and k entries corresponding to the lower corner of the patch

upper - a MatStencil with i, j and k entries corresponding to the upper corner of the patch

offproc - indicate whether the returned IS will contain off process indices

is - the IS corresponding to the patch

This routine always returns an IS on the DMDA communicator.

If offproc is set to PETSC_TRUE, the routine returns an IS with all the indices requested regardless of whether these indices are present on the requesting MPI process or not. Thus, it is upon the caller to ensure that the indices returned in this mode are appropriate.

If offproc is set to PETSC_FALSE, the IS only returns the subset of indices that are present on the requesting MPI process and there is no duplication of indices between multiple MPI processes.

DMDA - Creating vectors for structured grids, DM, DMDA, DMCreateDomainDecomposition(), DMCreateDomainDecompositionScatters()

src/dm/impls/da/dadd.c

src/dm/tutorials/ex22.c src/dm/tutorials/ex14.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDACreatePatchIS(DM da, MatStencil *lower, MatStencil *upper, IS *is, PetscBool offproc)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
DMCreateDomainDecomposition()
```

Example 4 (unknown):
```unknown
DMCreateDomainDecompositionScatters()
```

---

## DMDACreatePF#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDACreatePF/

**Contents:**
- DMDACreatePF#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Creates an appropriately dimensioned PF mathematical function object from a DMDA.

Collective; No Fortran Support

da - initial distributed array

pf - the mathematical function object

DM, PF, DMDA, DMDACreate1d(), DMDACreate2d(), DMDACreate3d(), DMDestroy(), DMCreateGlobalVector()

src/dm/impls/da/dapf.c

src/dm/tutorials/ex4.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDACreatePF(DM da, PF *pf)
```

Example 2 (unknown):
```unknown
DMDACreate1d()
```

Example 3 (unknown):
```unknown
DMDACreate2d()
```

Example 4 (unknown):
```unknown
DMDACreate3d()
```

---

## DMDACreate#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDACreate/

**Contents:**
- DMDACreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates a DMDA object for managing structured grids.

comm - The communicator for the DMDA object

See DMDA - Creating vectors for structured grids for details on the construction of a DMDA

DMDACreate1d(), DMDACreate2d(), and DMDACreate3d() are convenience routines to quickly completely create a DMDA

DMDA - Creating vectors for structured grids, DM, DMDA, DMSetUp(), DMDASetSizes(), DMClone(), DMDACreate1d(), DMDACreate2d(), DMDACreate3d()

src/dm/impls/da/dacreate.c

src/dm/tutorials/ex19.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDACreate(MPI_Comm comm, DM *da)
```

Example 2 (unknown):
```unknown
DMDACreate1d()
```

Example 3 (unknown):
```unknown
DMDACreate2d()
```

Example 4 (unknown):
```unknown
DMDACreate3d()
```

---

## DMDAElementType#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAElementType/

**Contents:**
- DMDAElementType#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#
- Examples#

Defines the type of elements that will be returned by DMDAGetElements()

DM Basics, DMDA, DMDACreate1d(), DMDACreate2d(), DMDACreate3d(), DMCreateInterpolation(), DMDASetInterpolationType(), DMDASetElementType(), DMDAGetElements(), DMDARestoreElements(), DMDACreate()

include/petscdmdatypes.h

src/dm/tutorials/ex5.c

src/dm/tutorials/ex20.c src/ksp/ksp/tutorials/ex70.c src/dm/tutorials/ex21.c src/ksp/ksp/tutorials/ex71.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDAGetElements()
```

Example 2 (unknown):
```unknown
typedef enum {
  DMDA_ELEMENT_P1,
  DMDA_ELEMENT_Q1
} DMDAElementType;
```

Example 3 (unknown):
```unknown
DMDACreate1d()
```

Example 4 (unknown):
```unknown
DMDACreate2d()
```

---

## DMDAGetAO#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetAO/

**Contents:**
- DMDAGetAO#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Gets the application ordering context for a distributed array.

ao - the application ordering context for DMDA

In this case, the AO maps to the natural grid ordering that would be used for the DMDA if only 1 processor were employed (ordering most rapidly in the x-direction, then y, then z). Multiple degrees of freedom are numbered for each node (rather than 1 component for the whole grid, then the next component, etc.)

Do NOT call AODestroy() on the ao returned by this function.

DMDA - Creating vectors for structured grids, DM, DMDA, DMDACreate2d(), DMDASetAOType(), DMDAGetGhostCorners(), DMDAGetCorners(), DMLocalToGlobal(), DMGlobalToLocalBegin(), DMGlobalToLocalEnd(), DMLocalToLocalBegin(), DMLocalToLocalEnd(), DMDAGetOwnershipRanges(), AO, AOPetscToApplication(), AOApplicationToPetsc()

src/dm/impls/da/daindex.c

src/dm/tutorials/ex22.c src/dm/tutorials/ex6.c src/ksp/ksp/tutorials/ex59.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetAO(DM da, AO *ao)
```

Example 2 (unknown):
```unknown
AODestroy()
```

Example 3 (unknown):
```unknown
DMDACreate2d()
```

Example 4 (unknown):
```unknown
DMDASetAOType()
```

---

## DMDAGetArray#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetArray/

**Contents:**
- DMDAGetArray#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Gets a work array for a DMDA

ghosted - do you want arrays for the ghosted or nonghosted patch

vptr - array data structured

The vector values are NOT initialized and may have garbage in them, so you may need to zero them.

Use DMDARestoreArray() to return the array

DMDA - Creating vectors for structured grids, DM, DMDA, DMDARestoreArray()

src/dm/impls/da/dalocal.c

src/ts/tutorials/ex9.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetArray(DM da, PetscBool ghosted, void *vptr)
```

Example 2 (unknown):
```unknown
DMDARestoreArray()
```

Example 3 (unknown):
```unknown
DMDARestoreArray()
```

---

## DMDAGetBoundaryType#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetBoundaryType/

**Contents:**
- DMDAGetBoundaryType#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Gets the type of ghost nodes on domain boundaries.

bx - x boundary type, one of DM_BOUNDARY_NONE, DM_BOUNDARY_GHOSTED, DM_BOUNDARY_PERIODIC

by - y boundary type, one of DM_BOUNDARY_NONE, DM_BOUNDARY_GHOSTED, DM_BOUNDARY_PERIODIC

bz - z boundary type, one of DM_BOUNDARY_NONE, DM_BOUNDARY_GHOSTED, DM_BOUNDARY_PERIODIC

DMDA - Creating vectors for structured grids, DMDASetBoundaryType(), DM, DMDA, DMDACreate(), DMDestroy(), DMBoundaryType, DM_BOUNDARY_NONE, DM_BOUNDARY_GHOSTED, DM_BOUNDARY_PERIODIC

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetBoundaryType(DM da, PeOp DMBoundaryType *bx, PeOp DMBoundaryType *by, PeOp DMBoundaryType *bz)
```

Example 2 (unknown):
```unknown
DM_BOUNDARY_NONE
```

Example 3 (unknown):
```unknown
DM_BOUNDARY_GHOSTED
```

Example 4 (unknown):
```unknown
DM_BOUNDARY_PERIODIC
```

---

## DMDAGetCellPoint#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetCellPoint/

**Contents:**
- DMDAGetCellPoint#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the DM point corresponding to the tuple (i, j, k) in the DMDA

i - The global x index for the cell

j - The global y index for the cell

k - The global z index for the cell

point - The local DM point

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAGetNumCells()

src/dm/impls/da/dalocal.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetCellPoint(DM dm, PetscInt i, PetscInt j, PetscInt k, PetscInt *point)
```

Example 2 (unknown):
```unknown
DMDAGetNumCells()
```

---

## DMDAGetCoordinateArray#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetCoordinateArray/

**Contents:**
- DMDAGetCoordinateArray#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets an array containing the coordinates of the DMDA

Not Collective; No Fortran Support

Use DMDARestoreCoordinateArray() to return the array

DMDA - Creating vectors for structured grids, DM, DMDA, DMDASetCoordinateName(), DMDASetFieldName(), DMDAGetFieldName(), DMDARestoreCoordinateArray()

src/dm/impls/da/dacorn.c

src/ts/tutorials/extchemfield.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetCoordinateArray(DM dm, void *xc)
```

Example 2 (unknown):
```unknown
DMDARestoreCoordinateArray()
```

Example 3 (unknown):
```unknown
DMDASetCoordinateName()
```

Example 4 (unknown):
```unknown
DMDASetFieldName()
```

---

## DMDAGetCoordinateName#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetCoordinateName/

**Contents:**
- DMDAGetCoordinateName#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the name of a coordinate direction associated with a DMDA.

Not Collective; name will contain a common value; No Fortran Support

nf - number for the DMDA (0, 1, … dim-1)

name - the name of the coordinate direction

It must be called after having called DMSetUp().

DMDA - Creating vectors for structured grids, DM, DMDA, DMDASetCoordinateName(), DMDASetFieldName(), DMDAGetFieldName(), DMSetUp()

src/dm/impls/da/dacorn.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetCoordinateName(DM dm, PetscInt nf, const char *name[])
```

Example 2 (unknown):
```unknown
DMDASetCoordinateName()
```

Example 3 (unknown):
```unknown
DMDASetFieldName()
```

Example 4 (unknown):
```unknown
DMDAGetFieldName()
```

---

## DMDAGetCorners#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetCorners/

**Contents:**
- DMDAGetCorners#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Returns the global (x,y,z) indices of the lower left corner and size of the local region, excluding ghost points.

x - the corner index for the first dimension

y - the corner index for the second dimension (only used in 2D and 3D problems)

z - the corner index for the third dimension (only used in 3D problems)

m - the width in the first dimension

n - the width in the second dimension (only used in 2D and 3D problems)

p - the width in the third dimension (only used in 3D problems)

Any of y, z, n, and p can be passed in as NULL if not needed.

The corner information is independent of the number of degrees of freedom per node set with the DMDACreateXX() routine. Thus the x, y, and z can be thought of as the lower left coordinates of the patch of values on process on a logical grid and m, n, and p as the extent of the patch, where each grid point has (potentially) several degrees of freedom.

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAGetGhostCorners(), DMDAGetOwnershipRanges(), DMStagGetCorners(), DMSTAG

src/dm/impls/da/dacorn.c

src/snes/tutorials/ex5f90.F90 src/snes/tutorials/ex14.c src/snes/tutorials/ex18.c src/snes/tutorials/ex15.c src/snes/tutorials/ex35.c src/snes/tutorials/ex22.c src/snes/tutorials/ex78.c src/snes/tutorials/ex48.c src/snes/tutorials/ex33.c src/snes/tutorials/ex21.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetCorners(DM da, PeOp PetscInt *x, PeOp PetscInt *y, PeOp PetscInt *z, PeOp PetscInt *m, PeOp PetscInt *n, PeOp PetscInt *p)
```

Example 2 (unknown):
```unknown
DMDACreateXX()
```

Example 3 (unknown):
```unknown
DMDAGetGhostCorners()
```

Example 4 (unknown):
```unknown
DMDAGetOwnershipRanges()
```

---

## DMDAGetDepthStratum#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetDepthStratum/

**Contents:**
- DMDAGetDepthStratum#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Get the bounds [start, end) for all points at a certain depth.

depth - The requested depth

pStart - The first point at this depth

pEnd - One beyond the last point at this depth

See DMPlexGetDepthStratum() for the meaning of these values

DMPlex: Unstructured Grids, DM, DMDA, DMPlexGetDepthStratum(), DMPlexGetHeightStratum(), DMPlexGetCellTypeStratum(), DMPlexGetDepth(), DMPlexGetDepthLabel(), DMPlexGetPointDepth(), DMPlexSymmetrize(), DMPlexInterpolate(), DMDAGetHeightStratum()

src/dm/impls/da/dalocal.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetDepthStratum(DM dm, PetscInt depth, PeOp PetscInt *pStart, PeOp PetscInt *pEnd)
```

Example 2 (unknown):
```unknown
DMPlexGetDepthStratum()
```

Example 3 (unknown):
```unknown
DMPlexGetDepthStratum()
```

Example 4 (unknown):
```unknown
DMPlexGetHeightStratum()
```

---

## DMDAGetDof#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetDof/

**Contents:**
- DMDAGetDof#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the number of degrees of freedom per vertex

dof - Number of degrees of freedom per vertex

DMDA - Creating vectors for structured grids, DM, DMDA, DMDASetDof(), DMDACreate(), DMDestroy()

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetDof(DM da, PetscInt *dof)
```

Example 2 (unknown):
```unknown
DMDASetDof()
```

Example 3 (unknown):
```unknown
DMDACreate()
```

Example 4 (unknown):
```unknown
DMDestroy()
```

---

## DMDAGetElementsCorners#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetElementsCorners/

**Contents:**
- DMDAGetElementsCorners#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#

Returns the global (i,j,k) indices of the lower left corner of the non-overlapping decomposition of elements identified by DMDAGetElements()

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAElementType, DMDASetElementType(), DMDAGetElements(), DMDAGetCorners(), DMDAGetGhostCorners(), DMDAGetElementsSizes(), DMDAGetElementsCornersIS(), DMDARestoreElementsCornersIS()

src/dm/impls/da/dagetelem.c

src/ksp/ksp/tutorials/ex43.c src/ksp/ksp/tutorials/ex49.c src/ksp/ksp/tutorials/ex42.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDAGetElements()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetElementsCorners(DM da, PeOp PetscInt *gx, PeOp PetscInt *gy, PeOp PetscInt *gz)
```

Example 3 (unknown):
```unknown
DMDAElementType
```

Example 4 (unknown):
```unknown
DMDASetElementType()
```

---

## DMDAGetElementsSizes#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetElementsSizes/

**Contents:**
- DMDAGetElementsSizes#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets the local number of elements per coordinate direction for the non-overlapping decomposition identified by DMDAGetElements()

mx - number of local elements in x-direction

my - number of local elements in y-direction

mz - number of local elements in z-direction

Returns the same number of elements, irrespective of the DMDAElementType

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAElementType, DMDASetElementType(), DMDAGetElements(), DMDAGetElementsCorners()

src/dm/impls/da/dagetelem.c

src/ksp/ksp/tutorials/ex43.c src/ksp/ksp/tutorials/ex49.c src/ksp/ksp/tutorials/ex42.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDAGetElements()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetElementsSizes(DM da, PeOp PetscInt *mx, PeOp PetscInt *my, PeOp PetscInt *mz)
```

Example 3 (unknown):
```unknown
DMDAElementType
```

Example 4 (unknown):
```unknown
DMDAElementType
```

---

## DMDAGetElements#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetElements/

**Contents:**
- DMDAGetElements#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Gets an array containing the indices (in local indexing) of all the local elements

nel - number of local elements

nen - number of nodes in each element (for example in one dimension it is 2, in two dimensions it is 3 (for DMDA_ELEMENT_P1) and 4 (for DMDA_ELEMENT_Q1)

e - the local indices of the elements’ vertices, of length nel * nen

Call DMDARestoreElements() once you have finished accessing the elements.

Each process uniquely owns a subset of the elements. That is no element is owned by two or more processes.

If on each process you integrate over its owned elements and use ADD_VALUES in Vec/MatSetValuesLocal() then you’ll obtain the correct result.

to declare the element array

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAElementType, DMDASetElementType(), VecSetValuesLocal(), MatSetValuesLocal(), DMGlobalToLocalBegin(), DMLocalToGlobalBegin(), DMDARestoreElements(), DMDA_ELEMENT_P1, DMDA_ELEMENT_Q1, DMDAGetElementsSizes(), DMDAGetElementsCorners()

src/dm/impls/da/dagetelem.c

src/ksp/ksp/tutorials/ex70.c src/dm/tutorials/ex11f90.F90 src/dm/tutorials/ex5.c src/ksp/ksp/tutorials/ex71.c

DMDAGetElements_1D() in src/dm/impls/da/dagetelem.c DMDAGetElements_2D() in src/dm/impls/da/dagetelem.c DMDAGetElements_3D() in src/dm/impls/da/dagetelem.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetElements(DM dm, PetscInt *nel, PetscInt *nen, const PetscInt *e[])
```

Example 2 (unknown):
```unknown
DMDA_ELEMENT_P1
```

Example 3 (unknown):
```unknown
DMDA_ELEMENT_Q1
```

Example 4 (unknown):
```unknown
DMDARestoreElements()
```

---

## DMDAGetElementType#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetElementType/

**Contents:**
- DMDAGetElementType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the element type to be returned by DMDAGetElements()

etype - the element type, currently either DMDA_ELEMENT_P1 or DMDA_ELEMENT_Q1

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAElementType, DMDASetElementType(), DMDAGetElements(), DMDARestoreElements(), DMDA_ELEMENT_P1, DMDA_ELEMENT_Q1

src/dm/impls/da/dagetelem.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDAGetElements()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetElementType(DM da, DMDAElementType *etype)
```

Example 3 (unknown):
```unknown
DMDA_ELEMENT_P1
```

Example 4 (unknown):
```unknown
DMDA_ELEMENT_Q1
```

---

## DMDAGetFieldNames#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetFieldNames/

**Contents:**
- DMDAGetFieldNames#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Gets the name of all the components in the vector associated with the DMDA

Not Collective; names will contain a common value; No Fortran Support

names - the names of the components, final string is NULL, will have the same number of entries as the dof used in creating the DMDA

Use DMDAGetFieldName()

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAGetFieldName(), DMDASetCoordinateName(), DMDAGetCoordinateName(), DMDASetFieldName(), DMDASetFieldNames()

src/dm/impls/da/dacorn.c

src/ts/tutorials/extchemfield.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetFieldNames(DM da, const char *const **names)
```

Example 2 (unknown):
```unknown
DMDAGetFieldName()
```

Example 3 (unknown):
```unknown
DMDAGetFieldName()
```

Example 4 (unknown):
```unknown
DMDASetCoordinateName()
```

---

## DMDAGetFieldName#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetFieldName/

**Contents:**
- DMDAGetFieldName#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets the names of individual field components in multicomponent vectors associated with a DMDA.

Not Collective; name will contain a common value

nf - field number for the DMDA (0, 1, … dof-1), where dof indicates the number of degrees of freedom per node within the DMDA

name - the name of the field (component)

It must be called after having called DMSetUp().

DMDA - Creating vectors for structured grids, DM, DMDA, DMDASetFieldName(), DMDASetCoordinateName(), DMDAGetCoordinateName(), DMSetUp()

src/dm/impls/da/dacorn.c

src/ksp/ksp/tutorials/ex43.c src/ts/tutorials/ex14.c src/ksp/ksp/tutorials/ex49.c src/ksp/ksp/tutorials/ex42.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetFieldName(DM da, PetscInt nf, const char *name[])
```

Example 2 (unknown):
```unknown
DMDASetFieldName()
```

Example 3 (unknown):
```unknown
DMDASetCoordinateName()
```

Example 4 (unknown):
```unknown
DMDAGetCoordinateName()
```

---

## DMDAGetGhostCorners#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetGhostCorners/

**Contents:**
- DMDAGetGhostCorners#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Returns the global (i,j,k) indices of the lower left corner and size of the local region, including ghost points.

x - the corner index for the first dimension

y - the corner index for the second dimension (only used in 2D and 3D problems)

z - the corner index for the third dimension (only used in 3D problems)

m - the width in the first dimension

n - the width in the second dimension (only used in 2D and 3D problems)

p - the width in the third dimension (only used in 3D problems)

Any of y, z, n, and p can be passed in as NULL if not needed.

The corner information is independent of the number of degrees of freedom per node set with the DMDACreateXX() routine. Thus the x, y, and z can be thought of as the lower left coordinates of the patch of values on process on a logical grid and m, n, and p as the extent of the patch. Where grid point has (potentially) several degrees of freedom.

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAGetCorners(), DMDACreate1d(), DMDACreate2d(), DMDACreate3d(), DMDAGetOwnershipRanges(), DMStagGetGhostCorners(), DMSTAG

src/dm/impls/da/daghost.c

src/tao/bound/tutorials/plate2f.F90 src/snes/tutorials/ex5f90.F90 src/tao/bound/tutorials/jbearing2.c src/ksp/ksp/tutorials/ex70.c src/ksp/ksp/tutorials/ex14f.F90 src/ksp/ksp/tutorials/ex49.c src/ksp/ksp/tutorials/ex42.c src/snes/tutorials/ex48.c src/ksp/ksp/tutorials/ex43.c src/snes/tutorials/ex5f90t.F90

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetGhostCorners(DM da, PeOp PetscInt *x, PeOp PetscInt *y, PeOp PetscInt *z, PeOp PetscInt *m, PeOp PetscInt *n, PeOp PetscInt *p)
```

Example 2 (unknown):
```unknown
DMDACreateXX()
```

Example 3 (unknown):
```unknown
DMDAGetCorners()
```

Example 4 (unknown):
```unknown
DMDACreate1d()
```

---

## DMDAGetHeightStratum#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetHeightStratum/

**Contents:**
- DMDAGetHeightStratum#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Get the bounds [start, end) for all points at a certain height.

height - The requested height

pStart - The first point at this height

pEnd - One beyond the last point at this height

See DMPlexGetHeightStratum() for the meaning of these values

DMPlex: Unstructured Grids, DM, DMDA, DMPlexGetDepthStratum(), DMPlexGetHeightStratum(), DMPlexGetCellTypeStratum(), DMPlexGetDepth(), DMPlexGetDepthLabel(), DMPlexGetPointDepth(), DMPlexSymmetrize(), DMPlexInterpolate(), DMDAGetDepthStratum()

src/dm/impls/da/dalocal.c

src/dm/field/tutorials/ex1.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetHeightStratum(DM dm, PetscInt height, PeOp PetscInt *pStart, PeOp PetscInt *pEnd)
```

Example 2 (unknown):
```unknown
DMPlexGetHeightStratum()
```

Example 3 (unknown):
```unknown
DMPlexGetDepthStratum()
```

Example 4 (unknown):
```unknown
DMPlexGetHeightStratum()
```

---

## DMDAGetInfo#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetInfo/

**Contents:**
- DMDAGetInfo#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets information about a given distributed array.

dim - dimension of the DMDA (1, 2, or 3)

M - global dimension in first direction of the array

N - global dimension in second direction of the array

P - global dimension in third direction of the array

m - corresponding number of MPI processes in first dimension

n - corresponding number of MPI processes in second dimension

p - corresponding number of MPI processes in third dimension

dof - number of degrees of freedom per node

bx - type of ghost nodes at boundary in first dimension

by - type of ghost nodes at boundary in second dimension

bz - type of ghost nodes at boundary in third dimension

st - stencil type, either DMDA_STENCIL_STAR or DMDA_STENCIL_BOX

Use NULL (PETSC_NULL_INTEGER in Fortran) in place of any output parameter that is not of interest.

DMDA - Creating vectors for structured grids, DM, DMDA, DMView(), DMDAGetCorners(), DMDAGetLocalInfo()

src/dm/impls/da/daview.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex73f90t.F90 src/snes/tutorials/ex14.c src/snes/tutorials/ex18.c src/snes/tutorials/ex35.c src/snes/tutorials/ex22.c src/snes/tutorials/ex78.c src/snes/tutorials/ex15.c src/snes/tutorials/ex21.c src/snes/tutorials/ex4.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetInfo(DM da, PeOp PetscInt *dim, PeOp PetscInt *M, PeOp PetscInt *N, PeOp PetscInt *P, PeOp PetscInt *m, PeOp PetscInt *n, PeOp PetscInt *p, PeOp PetscInt *dof, PeOp PetscInt *s, PeOp DMBoundaryType *bx, PeOp DMBoundaryType *by, PeOp DMBoundaryType *bz, PeOp DMDAStencilType *st)
```

Example 2 (unknown):
```unknown
DMDA_STENCIL_STAR
```

Example 3 (unknown):
```unknown
DMDA_STENCIL_BOX
```

Example 4 (unknown):
```unknown
PETSC_NULL_INTEGER
```

---

## DMDAGetInterpolationType#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetInterpolationType/

**Contents:**
- DMDAGetInterpolationType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the type of interpolation that will be used by DMCreateInterpolation()

da - distributed array

ctype - interpolation type (DMDA_Q1 and DMDA_Q0 are currently the only supported forms)

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAInterpolationType, DMDASetInterpolationType(), DMCreateInterpolation(), DMDA_Q1, DMDA_Q0

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateInterpolation()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetInterpolationType(DM da, DMDAInterpolationType *ctype)
```

Example 3 (unknown):
```unknown
DMDAInterpolationType
```

Example 4 (unknown):
```unknown
DMDASetInterpolationType()
```

---

## DMDAGetLocalInfo#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetLocalInfo/

**Contents:**
- DMDAGetLocalInfo#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets information about a given DMDA and this MPI process’s location in it

info - structure containing the information

See DMDALocalInfo for the information that is returned

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAGetInfo(), DMDAGetCorners(), DMDALocalInfo

src/dm/impls/da/daview.c

src/snes/tutorials/ex28.c src/ts/tutorials/ex14.c src/ts/tutorials/ex9.c src/snes/tutorials/ex9.c src/snes/tutorials/ex35.c src/ksp/ksp/tutorials/ex46.c src/snes/tutorials/ex19.c src/ts/tutorials/ex22.c src/snes/tutorials/ex15.c src/ts/tutorials/ex13.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetLocalInfo(DM da, DMDALocalInfo *info)
```

Example 2 (unknown):
```unknown
DMDALocalInfo
```

Example 3 (unknown):
```unknown
DMDAGetInfo()
```

Example 4 (unknown):
```unknown
DMDAGetCorners()
```

---

## DMDAGetLogicalCoordinate#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetLogicalCoordinate/

**Contents:**
- DMDAGetLogicalCoordinate#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Returns a the i,j,k logical coordinate for the closest mesh point to a x, y, z point in the coordinates of the DMDA

x - the first physical coordinate

y - the second physical coordinate

z - the third physical coordinate

II - the first logical coordinate (-1 on processes that do not contain that point)

JJ - the second logical coordinate (-1 on processes that do not contain that point)

KK - the third logical coordinate (-1 on processes that do not contain that point)

X - (optional) the first coordinate of the located grid point

Y - (optional) the second coordinate of the located grid point

Z - (optional) the third coordinate of the located grid point

All processors that share the DMDA must call this with the same coordinate value

DMDA - Creating vectors for structured grids, DM, DMDA

src/dm/impls/da/dasub.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetLogicalCoordinate(DM da, PetscScalar x, PetscScalar y, PetscScalar z, PetscInt *II, PetscInt *JJ, PetscInt *KK, PetscScalar *X, PetscScalar *Y, PetscScalar *Z)
```

---

## DMDAGetNeighbors#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetNeighbors/

**Contents:**
- DMDAGetNeighbors#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- Fortran Note#
- See Also#
- Level#
- Location#

Gets an array containing the MPI rank of all the current processes neighbors.

ranks - the neighbors ranks, stored with the x index increasing most rapidly. The process itself is in the list

In 2d the ranks is of length 9, in 3d of length 27

Do not free the array, it is freed when the DMDA is destroyed.

Use DMDARestoreNeighbors() to return the array when no longer needed

DMDA - Creating vectors for structured grids, DMDA, DM

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetNeighbors(DM da, const PetscMPIInt *ranks[])
```

Example 2 (unknown):
```unknown
DMDARestoreNeighbors()
```

---

## DMDAGetNonOverlappingRegion#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetNonOverlappingRegion/

**Contents:**
- DMDAGetNonOverlappingRegion#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Gets the indices of the nonoverlapping region of a subdomain DMDA.

xs - The start of the region in x

ys - The start of the region in y

zs - The start of the region in z

xm - The size of the region in x

ym - The size of the region in y

zm - The size of the region in z

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAGetOffset(), DMDAVecGetArray()

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetNonOverlappingRegion(DM da, PeOp PetscInt *xs, PeOp PetscInt *ys, PeOp PetscInt *zs, PeOp PetscInt *xm, PeOp PetscInt *ym, PeOp PetscInt *zm)
```

Example 2 (unknown):
```unknown
DMDAGetOffset()
```

Example 3 (unknown):
```unknown
DMDAVecGetArray()
```

---

## DMDAGetNumCells#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetNumCells/

**Contents:**
- DMDAGetNumCells#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Get the number of cells (or vertices) in the local piece of the DMDA. This includes ghost cells.

numCellsX - The number of local cells in the x-direction

numCellsY - The number of local cells in the y-direction

numCellsZ - The number of local cells in the z-direction

numCells - The number of local cells

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAGetCellPoint()

src/dm/impls/da/dalocal.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetNumCells(DM dm, PeOp PetscInt *numCellsX, PeOp PetscInt *numCellsY, PeOp PetscInt *numCellsZ, PeOp PetscInt *numCells)
```

Example 2 (unknown):
```unknown
DMDAGetCellPoint()
```

---

## DMDAGetNumFaces#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetNumFaces/

**Contents:**
- DMDAGetNumFaces#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Return the number of local mesh faces of each orientation (including ghost faces) for a DMDA.

numXFacesX - number of X-normal faces along the x direction, or NULL if not needed

numXFaces - total number of X-normal faces, or NULL if not needed

numYFacesY - number of Y-normal faces along the y direction, or NULL if not needed

numYFaces - total number of Y-normal faces (0 for 1D), or NULL if not needed

numZFacesZ - number of Z-normal faces along the z direction, or NULL if not needed

numZFaces - total number of Z-normal faces (0 for 1D/2D), or NULL if not needed

DM, DMDA, DMDAGetNumVertices(), DMDAGetNumCells()

src/dm/impls/da/dalocal.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetNumFaces(DM dm, PetscInt *numXFacesX, PetscInt *numXFaces, PetscInt *numYFacesY, PetscInt *numYFaces, PetscInt *numZFacesZ, PetscInt *numZFaces)
```

Example 2 (unknown):
```unknown
DMDAGetNumVertices()
```

Example 3 (unknown):
```unknown
DMDAGetNumCells()
```

---

## DMDAGetNumLocalSubDomains#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetNumLocalSubDomains/

**Contents:**
- DMDAGetNumLocalSubDomains#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the number of local subdomains that would be created upon decomposition.

Nsub - Number of local subdomains created upon decomposition

DMDA - Creating vectors for structured grids, DM, DMDA, DMCreateDomainDecomposition(), DMDASetNumLocalSubDomains()

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetNumLocalSubDomains(DM da, PetscInt *Nsub)
```

Example 2 (unknown):
```unknown
DMCreateDomainDecomposition()
```

Example 3 (unknown):
```unknown
DMDASetNumLocalSubDomains()
```

---

## DMDAGetNumVertices#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetNumVertices/

**Contents:**
- DMDAGetNumVertices#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Return the number of local vertices (including ghost vertices) of a DMDA in each dimension and in total.

numVerticesX - number of vertices in the x direction, or NULL if not needed

numVerticesY - number of vertices in the y direction (1 if dim < 2), or NULL if not needed

numVerticesZ - number of vertices in the z direction (1 if dim < 3), or NULL if not needed

numVertices - total number of vertices, or NULL if not needed

DM, DMDA, DMDAGetNumCells(), DMDAGetNumFaces()

src/dm/impls/da/dalocal.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetNumVertices(DM dm, PetscInt *numVerticesX, PetscInt *numVerticesY, PetscInt *numVerticesZ, PetscInt *numVertices)
```

Example 2 (unknown):
```unknown
DMDAGetNumCells()
```

Example 3 (unknown):
```unknown
DMDAGetNumFaces()
```

---

## DMDAGetOffset#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetOffset/

**Contents:**
- DMDAGetOffset#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Gets the index offset of the DMDA.

xo - The offset in the x direction

yo - The offset in the y direction

zo - The offset in the z direction

Mo - The global size in the x direction

No - The global size in the y direction

Po - The global size in the z direction

DMDA - Creating vectors for structured grids, DM, DMDA, DMDASetOffset(), DMDAVecGetArray()

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetOffset(DM da, PeOp PetscInt *xo, PeOp PetscInt *yo, PeOp PetscInt *zo, PeOp PetscInt *Mo, PeOp PetscInt *No, PeOp PetscInt *Po)
```

Example 2 (unknown):
```unknown
DMDASetOffset()
```

Example 3 (unknown):
```unknown
DMDAVecGetArray()
```

---

## DMDAGetOverlap#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetOverlap/

**Contents:**
- DMDAGetOverlap#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Gets the size of the per-processor overlap.

x - Overlap in the x direction

y - Overlap in the y direction

z - Overlap in the z direction

DMDA - Creating vectors for structured grids, DM, DMDA, DMCreateDomainDecomposition(), DMDASetOverlap()

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetOverlap(DM da, PeOp PetscInt *x, PeOp PetscInt *y, PeOp PetscInt *z)
```

Example 2 (unknown):
```unknown
DMCreateDomainDecomposition()
```

Example 3 (unknown):
```unknown
DMDASetOverlap()
```

---

## DMDAGetOwnershipRanges#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetOwnershipRanges/

**Contents:**
- DMDAGetOwnershipRanges#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- Fortran Notes#
- See Also#
- Level#
- Location#
- Examples#

Gets the number of indices in the x, y and z direction that are owned by each process in that direction

lx - ownership along x direction (optional), its length is m the number of processes in the x-direction

ly - ownership along y direction (optional), its length is n the number of processes in the y-direction

lz - ownership along z direction (optional), its length is p the number of processes in the z-direction

These correspond to the optional final arguments passed to DMDACreate(), DMDACreate2d(), DMDACreate3d()

You should not free these arrays, nor change the values in them. They will only have valid values while the DMDA they came from still exists (has not been destroyed).

These numbers are NOT multiplied by the number of dof per node.

The meaning of these is different than that returned by VecGetOwnerShipRanges()

Pass PETSC_NULL_INT_POINTER for any array not needed.

Use DMDARestoreOwershipRange() to return the arrays when no longer needed

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAGetCorners(), DMDAGetGhostCorners(), DMDACreate(), DMDACreate1d(), DMDACreate2d(), DMDACreate3d(), VecGetOwnershipRanges()

src/snes/tutorials/ex28.c src/dm/tutorials/ex51.c src/ksp/ksp/tutorials/ex73.c src/dm/tutorials/ex22.c src/ksp/ksp/tutorials/ex42.c src/ts/tutorials/ex10.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetOwnershipRanges(DM da, PeOp const PetscInt *lx[], PeOp const PetscInt *ly[], PeOp const PetscInt *lz[])
```

Example 2 (unknown):
```unknown
DMDACreate()
```

Example 3 (unknown):
```unknown
DMDACreate2d()
```

Example 4 (unknown):
```unknown
DMDACreate3d()
```

---

## DMDAGetPreallocationCenterDimension#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetPreallocationCenterDimension/

**Contents:**
- DMDAGetPreallocationCenterDimension#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Return the topology used to determine adjacency

preallocCenterDim - The dimension of points which connect adjacent entries

DMDA - Creating vectors for structured grids, DM, DMDA, DMCreateMatrix(), DMDAPreallocateOperator(), DMDASetPreallocationCenterDimension()

src/dm/impls/da/dapreallocate.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetPreallocationCenterDimension(DM dm, PetscInt *preallocCenterDim)
```

Example 2 (sass):
```sass
FEM:   Two points p and q are adjacent if q \in closure(star(p)), preallocCenterDim = dim
     FVM:   Two points p and q are adjacent if q \in star(cone(p)),    preallocCenterDim = dim-1
     FVM++: Two points p and q are adjacent if q \in star(closure(p)), preallocCenterDim = 0
```

Example 3 (unknown):
```unknown
DMCreateMatrix()
```

Example 4 (unknown):
```unknown
DMDAPreallocateOperator()
```

---

## DMDAGetProcessorSubsets#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetProcessorSubsets/

**Contents:**
- DMDAGetProcessorSubsets#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Returns communicators consisting only of the processors in a DMDA adjacent in a particular dimension, corresponding to a logical plane in a 3D grid or a line in a 2D grid.

Collective; No Fortran Support

dir - Cartesian direction, either DM_X, DM_Y, or DM_Z

subcomm - new communicator

This routine is useful for distributing one-dimensional data in a tensor product grid.

After use, comm should be freed with MPI_Comm_free()

DMDA - Creating vectors for structured grids, DM, DMDA, DMDirection, DMDAGetProcessorSubset(), DM_X, DM_Y, DM_Z

src/dm/impls/da/dasub.c

src/dm/tutorials/ex51.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetProcessorSubsets(DM da, DMDirection dir, MPI_Comm *subcomm)
```

Example 2 (unknown):
```unknown
MPI_Comm_free()
```

Example 3 (unknown):
```unknown
DMDirection
```

Example 4 (unknown):
```unknown
DMDAGetProcessorSubset()
```

---

## DMDAGetProcessorSubset#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetProcessorSubset/

**Contents:**
- DMDAGetProcessorSubset#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Returns a communicator consisting only of the processors in a DMDA that own a particular global x, y, or z grid point (corresponding to a logical plane in a 3D grid or a line in a 2D grid).

Collective; No Fortran Support

dir - Cartesian direction, either DM_X, DM_Y, or DM_Z

gp - global grid point number in this direction

comm - new communicator

All processors that share the DMDA must call this with the same gp value

After use, comm should be freed with MPI_Comm_free()

This routine is particularly useful to compute boundary conditions or other application-specific calculations that require manipulating sets of data throughout a logical plane of grid points.

DMDA - Creating vectors for structured grids, DM, DMDA, DMDirection, DM_X, DM_Y, DM_Z, DMDAGetProcessorSubsets()

src/dm/impls/da/dasub.c

src/dm/tutorials/ex22.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetProcessorSubset(DM da, DMDirection dir, PetscInt gp, MPI_Comm *comm)
```

Example 2 (unknown):
```unknown
MPI_Comm_free()
```

Example 3 (unknown):
```unknown
DMDirection
```

Example 4 (unknown):
```unknown
DMDAGetProcessorSubsets()
```

---

## DMDAGetRay#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetRay/

**Contents:**
- DMDAGetRay#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Returns a vector on process zero that contains a row or column of the values in a DMDA vector

dir - Cartesian direction, either DM_X, DM_Y, or DM_Z

gp - global grid point number in this direction

newvec - the new vector that can hold the values (size zero on all processes except MPI rank 0)

scatter - the VecScatter that will map from the original vector to the ray

All processors that share the DMDA must call this with the same gp value

DMDA - Creating vectors for structured grids, DM, DMDA, DMDirection, Vec, VecScatter

src/dm/impls/da/dasub.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetRay(DM da, DMDirection dir, PetscInt gp, Vec *newvec, VecScatter *scatter)
```

Example 2 (unknown):
```unknown
DMDirection
```

---

## DMDAGetReducedDMDA#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetReducedDMDA/

**Contents:**
- DMDAGetReducedDMDA#
- Synopsis#
- Level#
- Location#

Deprecated; use DMDACreateCompatibleDMDA()

src/dm/impls/da/dacorn.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetReducedDMDA(DM da, PetscInt nfields, DM *nda)
```

---

## DMDAGetRefinementFactor#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetRefinementFactor/

**Contents:**
- DMDAGetRefinementFactor#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Gets the ratios that the DMDA grid is refined

refine_x - ratio of fine grid to coarse in x direction (2 by default)

refine_y - ratio of fine grid to coarse in y direction (2 by default)

refine_z - ratio of fine grid to coarse in z direction (2 by default)

Pass NULL for values you do not need

DMDA - Creating vectors for structured grids, DM, DMDA, DMRefine(), DMDASetRefinementFactor()

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetRefinementFactor(DM da, PeOp PetscInt *refine_x, PeOp PetscInt *refine_y, PeOp PetscInt *refine_z)
```

Example 2 (unknown):
```unknown
DMDASetRefinementFactor()
```

---

## DMDAGetScatter#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetScatter/

**Contents:**
- DMDAGetScatter#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Gets the global-to-local, and local-to-local vector scatter contexts for a DMDA distributed array.

gtol - global-to-local scatter context (may be NULL)

ltol - local-to-local scatter context (may be NULL)

The output contexts are valid only as long as the input da is valid. If you delete the da, the scatter contexts will become invalid.

DMDA - Creating vectors for structured grids, DM, DMDA, DMGlobalToLocalBegin(), DMGlobalToLocalEnd(), DMLocalToGlobalBegin()

src/dm/impls/da/dascatter.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetScatter(DM da, PeOp VecScatter *gtol, PeOp VecScatter *ltol)
```

Example 2 (unknown):
```unknown
DMGlobalToLocalBegin()
```

Example 3 (unknown):
```unknown
DMGlobalToLocalEnd()
```

Example 4 (unknown):
```unknown
DMLocalToGlobalBegin()
```

---

## DMDAGetStencilType#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetStencilType/

**Contents:**
- DMDAGetStencilType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the type of the communication stencil

stype - The stencil type, use either DMDA_STENCIL_BOX or DMDA_STENCIL_STAR.

DMDA - Creating vectors for structured grids, DM, DMDA, DMDACreate(), DMDestroy(), DMDAStencilType, DMDA_STENCIL_BOX, DMDA_STENCIL_STAR.

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetStencilType(DM da, DMDAStencilType *stype)
```

Example 2 (unknown):
```unknown
DMDA_STENCIL_BOX
```

Example 3 (unknown):
```unknown
DMDA_STENCIL_STAR
```

Example 4 (unknown):
```unknown
DMDACreate()
```

---

## DMDAGetStencilWidth#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetStencilWidth/

**Contents:**
- DMDAGetStencilWidth#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the width of the communication stencil

width - The stencil width

DMDA - Creating vectors for structured grids, DM, DMDA, DMDACreate(), DMDestroy(), DMDAStencilType, DMDA_STENCIL_BOX, DMDA_STENCIL_STAR.

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetStencilWidth(DM da, PetscInt *width)
```

Example 2 (unknown):
```unknown
DMDACreate()
```

Example 3 (unknown):
```unknown
DMDestroy()
```

Example 4 (unknown):
```unknown
DMDAStencilType
```

---

## DMDAGetSubdomainCornersIS#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGetSubdomainCornersIS/

**Contents:**
- DMDAGetSubdomainCornersIS#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets an index set containing the corner indices (in local indexing) of the non-overlapping decomposition identified by DMDAGetElements()

Call DMDARestoreSubdomainCornersIS() once you have finished accessing the index set.

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAElementType, DMDASetElementType(), DMDAGetElements(), DMDARestoreElementsCornersIS(), DMDAGetElementsSizes(), DMDAGetElementsCorners()

src/dm/impls/da/dagetelem.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDAGetElements()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGetSubdomainCornersIS(DM dm, IS *is)
```

Example 3 (unknown):
```unknown
DMDARestoreSubdomainCornersIS()
```

Example 4 (unknown):
```unknown
DMDAElementType
```

---

## DMDAGlobalToNaturalAllCreate#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGlobalToNaturalAllCreate/

**Contents:**
- DMDAGlobalToNaturalAllCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Creates a scatter context that maps from a global vector, obtained with DMCreateGlobalVector(), to the entire vector to each processor in natural numbering

da - the DMDA context

scatter - the scatter context

DMDA - Creating vectors for structured grids, DM, DMDA, DMDANaturalAllToGlobalCreate(), DMDAGlobalToNaturalEnd(), DMLocalToGlobalBegin(), DMDACreate2d(), DMGlobalToLocalBegin(), DMGlobalToLocalEnd(), DMDACreateNaturalVector()

src/dm/impls/da/dagtona.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGlobalToNaturalAllCreate(DM da, VecScatter *scatter)
```

Example 3 (unknown):
```unknown
DMDANaturalAllToGlobalCreate()
```

Example 4 (unknown):
```unknown
DMDAGlobalToNaturalEnd()
```

---

## DMDAGlobalToNaturalBegin#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGlobalToNaturalBegin/

**Contents:**
- DMDAGlobalToNaturalBegin#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Maps values from the global vector obtained with DMCreateGlobalVector() to a global vector in the “natural” grid ordering. Must be followed by DMDAGlobalToNaturalEnd() to complete the exchange.

Neighbor-wise Collective

da - the DMDA context

g - the global vector, see DMCreateGlobalVector()

mode - one of INSERT_VALUES or ADD_VALUES

n - the natural ordering values, see DMDACreateNaturalVector()

The global and natural vectors used here need not be the same as those obtained from DMCreateGlobalVector() and DMDACreateNaturalVector(), BUT they must have the same parallel data layout; they could, for example, be obtained with VecDuplicate() from the DMDA originating vectors.

You must call DMDACreateNaturalVector() before using this routine

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAGlobalToNaturalEnd(), DMLocalToGlobalBegin(), DMDACreate2d(), DMGlobalToLocalBegin(), DMGlobalToLocalEnd(), DMDACreateNaturalVector()

src/dm/impls/da/dagtol.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 2 (unknown):
```unknown
DMDAGlobalToNaturalEnd()
```

Example 3 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGlobalToNaturalBegin(DM da, Vec g, InsertMode mode, Vec n)
```

Example 4 (unknown):
```unknown
DMCreateGlobalVector()
```

---

## DMDAGlobalToNaturalEnd#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAGlobalToNaturalEnd/

**Contents:**
- DMDAGlobalToNaturalEnd#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Maps values from the global vector obtained with DMCreateGlobalVector() to a global vector in the natural ordering. Must be preceded by DMDAGlobalToNaturalBegin().

Neighbor-wise Collective

da - the DMDA context

g - the global vector, see DMCreateGlobalVector()

mode - one of INSERT_VALUES or ADD_VALUES

n - the global values in the natural ordering, see DMDACreateNaturalVector()

The global and local vectors used here need not be the same as those obtained from DMCreateGlobalVector() and DMDACreateNaturalVector(), BUT they must have the same parallel data layout; they could, for example, be obtained with VecDuplicate() from the DMDA originating vectors.

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAGlobalToNaturalBegin(), DMLocalToGlobalBegin(), DMDACreate2d(), DMGlobalToLocalBegin(), DMGlobalToLocalEnd(), DMDACreateNaturalVector()

src/dm/impls/da/dagtol.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 2 (unknown):
```unknown
DMDAGlobalToNaturalBegin()
```

Example 3 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAGlobalToNaturalEnd(DM da, Vec g, InsertMode mode, Vec n)
```

Example 4 (unknown):
```unknown
DMCreateGlobalVector()
```

---

## DMDAInterpolationType#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAInterpolationType/

**Contents:**
- DMDAInterpolationType#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#

Defines the type of interpolation that will be returned by DMCreateInterpolation().

DM Basics, DMDA, DMDACreate1d(), DMDACreate2d(), DMDACreate3d(), DMCreateInterpolation(), DMDASetInterpolationType(), DMDACreate()

include/petscdmdatypes.h

src/ksp/ksp/tutorials/ex34.c src/ksp/ksp/tutorials/ex32.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateInterpolation()
```

Example 2 (unknown):
```unknown
typedef enum {
  DMDA_Q0,
  DMDA_Q1
} DMDAInterpolationType;
```

Example 3 (unknown):
```unknown
DMDACreate1d()
```

Example 4 (unknown):
```unknown
DMDACreate2d()
```

---

## DMDALocalInfo#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDALocalInfo/

**Contents:**
- DMDALocalInfo#
- Synopsis#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

C struct that contains information about a structured grid and a processes logical location in it.

This is a derived type whose entries can be directly accessed

DM Basics, DMDA, DMDACreate1d(), DMDACreate2d(), DMDACreate3d(), DMDestroy(), DM, DMDAGetLocalInfo(), DMDAGetInfo()

include/petscdmdatypes.h

src/snes/tutorials/ex28.c src/ts/tutorials/ex14.c src/ts/tutorials/ex9.c src/snes/tutorials/ex5f.F90 src/snes/tutorials/ex9.c src/snes/tutorials/ex35.c src/snes/tutorials/ex40f90.F90 src/ksp/ksp/tutorials/ex46.c src/snes/tutorials/ex19.c src/snes/tutorials/ex15.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef struct {
  DM              da;
  PetscInt        dim, dof, sw;
  PetscInt        mx, my, mz;    /* global number of grid points in each direction */
  PetscInt        xs, ys, zs;    /* starting point of this processor, excluding ghosts */
  PetscInt        xm, ym, zm;    /* number of grid points on this processor, excluding ghosts */
  PetscInt        gxs, gys, gzs; /* starting point of this processor including ghosts */
  PetscInt        gxm, gym, gzm; /* number of grid points on this processor including ghosts */
  DMBoundaryType  bx, by, bz;    /* type of ghost nodes at boundary */
  DMDAStencilType st;
} DMDALocalInfo;
```

Example 2 (unknown):
```unknown
DMDACreate1d()
```

Example 3 (unknown):
```unknown
DMDACreate2d()
```

Example 4 (unknown):
```unknown
DMDACreate3d()
```

---

## DMDAMapMatStencilToGlobal#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAMapMatStencilToGlobal/

**Contents:**
- DMDAMapMatStencilToGlobal#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Map a list of MatStencil on a grid to global indices.

m - number of MatStencil to map

idxm - grid points (and component number when dof > 1)

gidxm - global row indices

DMDA - Creating vectors for structured grids, DM, DMDA, MatStencil

src/snes/tutorials/ex55k.kokkos.cxx

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAMapMatStencilToGlobal(DM da, PetscInt m, const MatStencil idxm[], PetscInt gidxm[])
```

---

## DMDANaturalAllToGlobalCreate#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDANaturalAllToGlobalCreate/

**Contents:**
- DMDANaturalAllToGlobalCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Creates a scatter context that maps from a copy of the entire vector on each processor (in the natural ordering) to its local part in the global vector, obtained with DMCreateGlobalVector().

da - the DMDA context

scatter - the scatter context

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAGlobalToNaturalAllCreate(), DMDAGlobalToNaturalEnd(), DMLocalToGlobalBegin(), DMDACreate2d(), DMGlobalToLocalBegin(), DMGlobalToLocalEnd(), DMDACreateNaturalVector()

src/dm/impls/da/dagtona.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDANaturalAllToGlobalCreate(DM da, VecScatter *scatter)
```

Example 3 (unknown):
```unknown
DMDAGlobalToNaturalAllCreate()
```

Example 4 (unknown):
```unknown
DMDAGlobalToNaturalEnd()
```

---

## DMDANaturalToGlobalBegin#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDANaturalToGlobalBegin/

**Contents:**
- DMDANaturalToGlobalBegin#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Maps values from a global vector in the “natural” ordering to a global vector in the PETSc DMDA grid ordering. Must be followed by DMDANaturalToGlobalEnd() to complete the exchange.

Neighbor-wise Collective

da - the DMDA context

g - the global vector in a natural ordering, see DMDACreateNaturalVector()

mode - one of INSERT_VALUES or ADD_VALUES

n - the values in the DMDA ordering

The global and natural vectors used here need not be the same as those obtained from DMCreateGlobalVector() and DMDACreateNaturalVector(), BUT they must have the same parallel data layout; they could, for example, be obtained with VecDuplicate() from the DMDA originating vectors.

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAGlobalToNaturalEnd(), DMDAGlobalToNaturalBegin(), DMLocalToGlobalBegin(), DMDACreate2d(), DMGlobalToLocalBegin(), DMGlobalToLocalEnd(), DMDACreateNaturalVector()

src/dm/impls/da/dagtol.c

src/dm/tutorials/ex6.c src/ksp/ksp/tutorials/ex71.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDANaturalToGlobalEnd()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDANaturalToGlobalBegin(DM da, Vec n, InsertMode mode, Vec g)
```

Example 3 (unknown):
```unknown
DMDACreateNaturalVector()
```

Example 4 (unknown):
```unknown
INSERT_VALUES
```

---

## DMDANaturalToGlobalEnd#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDANaturalToGlobalEnd/

**Contents:**
- DMDANaturalToGlobalEnd#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Maps values from the natural ordering global vector to a global vector in the PETSc DMDA ordering. Must be preceded by DMDANaturalToGlobalBegin().

Neighbor-wise Collective

da - the DMDA context

g - the global vector in a natural ordering

mode - one of INSERT_VALUES or ADD_VALUES

n - the global values in the PETSc DMDA ordering

The global and local vectors used here need not be the same as those obtained from DMCreateGlobalVector() and DMDACreateNaturalVector(), BUT they must have the same parallel data layout; they could, for example, be obtained with VecDuplicate() from the DMDA originating vectors.

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAGlobalToNaturalBegin(), DMDAGlobalToNaturalEnd(), DMLocalToGlobalBegin(), DMDACreate2d(), DMGlobalToLocalBegin(), DMGlobalToLocalEnd(), DMDACreateNaturalVector()

src/dm/impls/da/dagtol.c

src/dm/tutorials/ex6.c src/ksp/ksp/tutorials/ex71.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDANaturalToGlobalBegin()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDANaturalToGlobalEnd(DM da, Vec n, InsertMode mode, Vec g)
```

Example 3 (unknown):
```unknown
INSERT_VALUES
```

Example 4 (unknown):
```unknown
DMCreateGlobalVector()
```

---

## DMDARestoreArray#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDARestoreArray/

**Contents:**
- DMDARestoreArray#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Restores an array for a DMDA obtained with DMDAGetArray()

da - information about my local patch

ghosted - do you want arrays for the ghosted or nonghosted patch

vptr - array data structured

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAGetArray()

src/dm/impls/da/dalocal.c

src/ts/tutorials/ex9.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDAGetArray()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDARestoreArray(DM da, PetscBool ghosted, void *vptr)
```

Example 3 (unknown):
```unknown
DMDAGetArray()
```

---

## DMDARestoreCoordinateArray#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDARestoreCoordinateArray/

**Contents:**
- DMDARestoreCoordinateArray#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Returns an array containing the coordinates of the DMDA obtained with DMDAGetCoordinateArray()

Not Collective; No Fortran Support

DMDA - Creating vectors for structured grids, DM, DMDA, DMDASetCoordinateName(), DMDASetFieldName(), DMDAGetFieldName(), DMDAGetCoordinateArray()

src/dm/impls/da/dacorn.c

src/ts/tutorials/extchemfield.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDAGetCoordinateArray()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDARestoreCoordinateArray(DM dm, void *xc)
```

Example 3 (unknown):
```unknown
DMDASetCoordinateName()
```

Example 4 (unknown):
```unknown
DMDASetFieldName()
```

---

## DMDARestoreElements#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDARestoreElements/

**Contents:**
- DMDARestoreElements#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Restores the array obtained with DMDAGetElements()

nel - number of local elements

nen - number of nodes in each element

e - the local indices of the elements’ vertices

This restore signals the DMDA object that you no longer need access to the array information.

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAElementType, DMDASetElementType(), DMDAGetElements()

src/dm/impls/da/dagetelem.c

src/ksp/ksp/tutorials/ex70.c src/dm/tutorials/ex11f90.F90 src/dm/tutorials/ex5.c src/ksp/ksp/tutorials/ex71.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDAGetElements()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDARestoreElements(DM dm, PetscInt *nel, PetscInt *nen, const PetscInt *e[])
```

Example 3 (unknown):
```unknown
DMDAElementType
```

Example 4 (unknown):
```unknown
DMDASetElementType()
```

---

## DMDARestoreSubdomainCornersIS#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDARestoreSubdomainCornersIS/

**Contents:**
- DMDARestoreSubdomainCornersIS#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Restores the IS obtained with DMDAGetSubdomainCornersIS()

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAElementType, DMDASetElementType(), DMDAGetSubdomainCornersIS()

src/dm/impls/da/dagetelem.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDAGetSubdomainCornersIS()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDARestoreSubdomainCornersIS(DM dm, IS *is)
```

Example 3 (unknown):
```unknown
DMDAElementType
```

Example 4 (unknown):
```unknown
DMDASetElementType()
```

---

## DMDASetAOType#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetAOType/

**Contents:**
- DMDASetAOType#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the type of application ordering to create with DMDAGetAO(), for a distributed array.

aotype - type of AO. AOType which can be AOBASIC, AOADVANCED, AOMAPPING, or AOMEMORYSCALABLE

It will generate an error if an AO has already been obtained with a call to DMDAGetAO() and the user sets a different AOType

DMDA - Creating vectors for structured grids, DM, DMDA, DMDACreate2d(), DMDAGetAO(), DMDAGetGhostCorners(), DMDAGetCorners(), DMLocalToGlobal(), DMGlobalToLocalBegin(), DMGlobalToLocalEnd(), DMLocalToLocalBegin(), DMLocalToLocalEnd(), DMDAGetGlobalIndices(), DMDAGetOwnershipRanges(), AO, AOPetscToApplication(), AOApplicationToPetsc(), AOType, AOBASIC, AOADVANCED, AOMAPPING, AOMEMORYSCALABLE

src/dm/impls/da/daindex.c

src/ksp/ksp/tutorials/ex59.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDAGetAO()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDASetAOType(DM da, AOType aotype)
```

Example 3 (unknown):
```unknown
AOMEMORYSCALABLE
```

Example 4 (unknown):
```unknown
DMDAGetAO()
```

---

## DMDASetBlockFillsSparse#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetBlockFillsSparse/

**Contents:**
- DMDASetBlockFillsSparse#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Sets the fill pattern in each block for a multi-component problem of the matrix returned by DMCreateMatrix(), using sparse representations of fill patterns.

dfillsparse - the sparse fill pattern in the diagonal block (may be NULL, means use dense block)

ofillsparse - the sparse fill pattern in the off-diagonal blocks

This only makes sense when you are doing multicomponent problems but using the MATMPIAIJ matrix format

The format for dfill and ofill is a sparse representation of a dof-by-dof matrix with 1 entries representing coupling and 0 entries for missing coupling. The sparse representation is a 1 dimensional array of length nz + dof + 1, where nz is the number of non-zeros in the matrix. The first dof entries in the array give the starting array indices of each row’s items in the rest of the array, the dof+1st item contains the value nz + dof + 1 (i.e. the entire length of the array) and the remaining nz items give the column indices of each of the 1s within the logical 2D matrix. Each row’s items within the array are the column indices of the 1s within that row of the 2D matrix. PETSc developers may recognize that this is the same format as that computed by the DMDASetBlockFills_Private() function from a dense 2D matrix representation.

DMDASetGetMatrix() allows you to provide general code for those more complicated nonzero patterns then can be represented in the dfill, ofill format

Contributed by: Philip C. Roth

DMDA - Creating vectors for structured grids, DM, DMDA, DMDASetBlockFills(), DMCreateMatrix(), DMDASetGetMatrix(), DMSetMatrixPreallocateOnly()

src/dm/impls/da/fdda.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateMatrix()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"     
PetscErrorCode DMDASetBlockFillsSparse(DM da, const PetscInt *dfillsparse, const PetscInt *ofillsparse)
```

Example 3 (unknown):
```unknown
DMDASetBlockFills_Private()
```

Example 4 (unknown):
```unknown
DMDASetGetMatrix()
```

---

## DMDASetBlockFills#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetBlockFills/

**Contents:**
- DMDASetBlockFills#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Sets the fill pattern in each block for a multi-component problem of the matrix returned by DMCreateMatrix().

dfill - the fill pattern in the diagonal block (may be NULL, means use dense block)

ofill - the fill pattern in the off-diagonal blocks

This only makes sense when you are doing multicomponent problems but using the MATMPIAIJ matrix format

The format for dfill and ofill is a 2 dimensional dof by dof matrix with 1 entries representing coupling and 0 entries for missing coupling. For example

means that row 0 is coupled with only itself in the diagonal block, row 1 is coupled with itself and row 0 (in the diagonal block) and row 2 is coupled with itself and row 1 (in the diagonal block).

DMDASetGetMatrix() allows you to provide general code for those more complicated nonzero patterns then can be represented in the dfill, ofill format

Contributed by: Glenn Hammond

DMDA - Creating vectors for structured grids, DM, DMDA, DMCreateMatrix(), DMDASetGetMatrix(), DMSetMatrixPreallocateOnly(), DMDASetBlockFillsSparse()

src/dm/impls/da/fdda.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateMatrix()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"     
PetscErrorCode DMDASetBlockFills(DM da, const PetscInt *dfill, const PetscInt *ofill)
```

Example 3 (unknown):
```unknown
dfill[9] = {1, 0, 0,
                        1, 1, 0,
                        0, 1, 1}
```

Example 4 (unknown):
```unknown
DMDASetGetMatrix()
```

---

## DMDASetBoundaryType#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetBoundaryType/

**Contents:**
- DMDASetBoundaryType#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the type of ghost nodes on domain boundaries for a DMDA object.

bx - x boundary type, one of DM_BOUNDARY_NONE, DM_BOUNDARY_GHOSTED, DM_BOUNDARY_PERIODIC

by - y boundary type, one of DM_BOUNDARY_NONE, DM_BOUNDARY_GHOSTED, DM_BOUNDARY_PERIODIC

bz - z boundary type, one of DM_BOUNDARY_NONE, DM_BOUNDARY_GHOSTED, DM_BOUNDARY_PERIODIC

The default is DM_BOUNDARY_NONE

DMDA - Creating vectors for structured grids, DMDAGetBoundaryType(), DM, DMDA, DMDACreate(), DMDestroy(), DMBoundaryType, DM_BOUNDARY_NONE, DM_BOUNDARY_GHOSTED, DM_BOUNDARY_PERIODIC

src/dm/tutorials/ex19.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDASetBoundaryType(DM da, DMBoundaryType bx, DMBoundaryType by, DMBoundaryType bz)
```

Example 2 (unknown):
```unknown
DM_BOUNDARY_NONE
```

Example 3 (unknown):
```unknown
DM_BOUNDARY_GHOSTED
```

Example 4 (unknown):
```unknown
DM_BOUNDARY_PERIODIC
```

---

## DMDASetCoordinateName#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetCoordinateName/

**Contents:**
- DMDASetCoordinateName#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the name of the coordinate directions associated with a DMDA, for example “x” or “y”

Logically Collective; name must contain a common value; No Fortran Support

nf - coordinate number for the DMDA (0, 1, … dim-1),

name - the name of the coordinate

Must be called after having called DMSetUp().

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAGetCoordinateName(), DMDASetFieldName(), DMDAGetFieldName(), DMSetUp()

src/dm/impls/da/dacorn.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDASetCoordinateName(DM dm, PetscInt nf, const char name[])
```

Example 2 (unknown):
```unknown
DMDAGetCoordinateName()
```

Example 3 (unknown):
```unknown
DMDASetFieldName()
```

Example 4 (unknown):
```unknown
DMDAGetFieldName()
```

---

## DMDASetDof#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetDof/

**Contents:**
- DMDASetDof#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the number of degrees of freedom per vertex

dof - Number of degrees of freedom per vertex

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAGetDof(), DMDACreate(), DMDestroy()

src/dm/tutorials/ex19.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDASetDof(DM da, PetscInt dof)
```

Example 2 (unknown):
```unknown
DMDAGetDof()
```

Example 3 (unknown):
```unknown
DMDACreate()
```

Example 4 (unknown):
```unknown
DMDestroy()
```

---

## DMDASetElementType#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetElementType/

**Contents:**
- DMDASetElementType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Sets the element type to be returned by DMDAGetElements()

etype - the element type, currently either DMDA_ELEMENT_P1 or DMDA_ELEMENT_Q1

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAElementType, DMDAGetElementType(), DMDAGetElements(), DMDARestoreElements(), DMDA_ELEMENT_P1, DMDA_ELEMENT_Q1

src/dm/impls/da/dagetelem.c

src/ksp/ksp/tutorials/ex70.c src/ksp/ksp/tutorials/ex71.c src/dm/tutorials/ex21.c src/dm/tutorials/ex5.c src/dm/tutorials/ex20.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDAGetElements()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDASetElementType(DM da, DMDAElementType etype)
```

Example 3 (unknown):
```unknown
DMDA_ELEMENT_P1
```

Example 4 (unknown):
```unknown
DMDA_ELEMENT_Q1
```

---

## DMDASetFieldNames#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetFieldNames/

**Contents:**
- DMDASetFieldNames#
- Synopsis#
- Input Parameters#
- Note#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the name of each component in the vector associated with the DMDA

Logically Collective; names must contain a common value; No Fortran Support

names - the names of the components, final string must be NULL, must have the same number of entries as the dof used in creating the DMDA

It must be called after having called DMSetUp().

Use DMDASetFieldName()

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAGetFieldName(), DMDASetCoordinateName(), DMDAGetCoordinateName(), DMDASetFieldName(), DMSetUp()

src/dm/impls/da/dacorn.c

src/ts/tutorials/extchemfield.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDASetFieldNames(DM da, const char *const names[])
```

Example 2 (unknown):
```unknown
DMDASetFieldName()
```

Example 3 (unknown):
```unknown
DMDAGetFieldName()
```

Example 4 (unknown):
```unknown
DMDASetCoordinateName()
```

---

## DMDASetFieldName#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetFieldName/

**Contents:**
- DMDASetFieldName#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the names of individual field components in multicomponent vectors associated with a DMDA.

Logically Collective; name must contain a common value

nf - field number for the DMDA (0, 1, … dof-1), where dof indicates the number of degrees of freedom per node within the DMDA

name - the name of the field (component)

It must be called after having called DMSetUp().

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAGetFieldName(), DMDASetCoordinateName(), DMDAGetCoordinateName(), DMDASetFieldNames(), DMSetUp()

src/dm/impls/da/dacorn.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex21.c src/snes/tutorials/ex16.c src/ksp/ksp/tutorials/ex70.c src/snes/tutorials/ex30.c src/ksp/ksp/tutorials/ex49.c src/snes/tutorials/ex19.c src/snes/tutorials/ex48.c src/ksp/ksp/tutorials/ex43.c src/snes/tutorials/ex22.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDASetFieldName(DM da, PetscInt nf, const char name[])
```

Example 2 (unknown):
```unknown
DMDAGetFieldName()
```

Example 3 (unknown):
```unknown
DMDASetCoordinateName()
```

Example 4 (unknown):
```unknown
DMDAGetCoordinateName()
```

---

## DMDASetGetMatrix#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetGetMatrix/

**Contents:**
- DMDASetGetMatrix#
- Synopsis#
- Input Parameters#
- Calling sequence of f#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#

Sets the routine used by the DMDA to allocate a matrix.

Logically Collective; No Fortran Support

f - the function that allocates the matrix for that specific DMDA

A - the created matrix

If the function is not provided a default function is used that uses the DMDAStencilType, DMBoundaryType, and value of DMDASetStencilWidth() to construct the matrix.

See DMDASetBlockFills() that provides a simple way to provide the nonzero structure for the diagonal and off-diagonal blocks of the matrix without providing a custom function

This should be called DMDASetCreateMatrix()

DMDA - Creating vectors for structured grids, DM, DMDA, DMCreateMatrix(), DMDASetBlockFills()

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDASetGetMatrix(DM da, PetscErrorCode (*f)(DM da, Mat *A))
```

Example 2 (unknown):
```unknown
DMDAStencilType
```

Example 3 (unknown):
```unknown
DMBoundaryType
```

Example 4 (unknown):
```unknown
DMDASetStencilWidth()
```

---

## DMDASetGLLCoordinates#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetGLLCoordinates/

**Contents:**
- DMDASetGLLCoordinates#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets the global coordinates from -1 to 1 to the GLL points of as many GLL elements that fit the number of grid points

n - the number of GLL nodes

nodes - the GLL nodes

The parallel decomposition of grid points must correspond to the degree of the GLL. That is, the number of grid points on each process much be divisible by the number of GLL elements needed per process. This depends on whether the DMDA is periodic or not.

DMDA - Creating vectors for structured grids, DM, DMDA, DMDACreate(), PetscDTGaussLobattoLegendreQuadrature(), DMGetCoordinates()

src/ksp/ksp/tutorials/ex69.c

DMDASetGLLCoordinates_1d() in src/dm/impls/da/da.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDASetGLLCoordinates(DM da, PetscInt n, PetscReal *nodes)
```

Example 2 (unknown):
```unknown
DMDACreate()
```

Example 3 (unknown):
```unknown
PetscDTGaussLobattoLegendreQuadrature()
```

Example 4 (unknown):
```unknown
DMGetCoordinates()
```

---

## DMDASetInterpolationType#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetInterpolationType/

**Contents:**
- DMDASetInterpolationType#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the type of interpolation that will be returned by DMCreateInterpolation()

da - initial distributed array

ctype - DMDA_Q1 and DMDA_Q0 are currently the only supported forms

You should call this on the coarser of the two DMDA you pass to DMCreateInterpolation()

DMDA - Creating vectors for structured grids, DM, DMDA, DMDACreate1d(), DMDACreate2d(), DMDACreate3d(), DMDestroy(), DMDAInterpolationType, DMDA_Q1, DMDA_Q0

src/ksp/ksp/tutorials/ex34.c src/ksp/ksp/tutorials/ex32.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateInterpolation()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDASetInterpolationType(DM da, DMDAInterpolationType ctype)
```

Example 3 (unknown):
```unknown
DMCreateInterpolation()
```

Example 4 (unknown):
```unknown
DMDACreate1d()
```

---

## DMDASetNonOverlappingRegion#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetNonOverlappingRegion/

**Contents:**
- DMDASetNonOverlappingRegion#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the indices of the nonoverlapping region of a subdomain DMDA.

xs - The start of the region in x

ys - The start of the region in y

zs - The start of the region in z

xm - The size of the region in x

ym - The size of the region in y

zm - The size of the region in z

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAGetOffset(), DMDAVecGetArray()

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDASetNonOverlappingRegion(DM da, PetscInt xs, PetscInt ys, PetscInt zs, PetscInt xm, PetscInt ym, PetscInt zm)
```

Example 2 (unknown):
```unknown
DMDAGetOffset()
```

Example 3 (unknown):
```unknown
DMDAVecGetArray()
```

---

## DMDASetNumLocalSubDomains#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetNumLocalSubDomains/

**Contents:**
- DMDASetNumLocalSubDomains#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the number of local subdomains to create when decomposing with DMCreateDomainDecomposition()

Nsub - The number of local subdomains requested

DMDA - Creating vectors for structured grids, DM, DMDA, DMCreateDomainDecomposition(), DMDAGetNumLocalSubDomains()

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateDomainDecomposition()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDASetNumLocalSubDomains(DM da, PetscInt Nsub)
```

Example 3 (unknown):
```unknown
DMCreateDomainDecomposition()
```

Example 4 (unknown):
```unknown
DMDAGetNumLocalSubDomains()
```

---

## DMDASetNumProcs#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetNumProcs/

**Contents:**
- DMDASetNumProcs#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the number of processes in each dimension

m - the number of X processes (or PETSC_DECIDE)

n - the number of Y processes (or PETSC_DECIDE)

p - the number of Z processes (or PETSC_DECIDE)

DMDA - Creating vectors for structured grids, DM, DMDA, DMDASetSizes(), PetscSplitOwnership()

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDASetNumProcs(DM da, PetscInt m, PetscInt n, PetscInt p)
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
PETSC_DECIDE
```

---

## DMDASetOffset#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetOffset/

**Contents:**
- DMDASetOffset#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the index offset of the DMDA.

xo - The offset in the x direction

yo - The offset in the y direction

zo - The offset in the z direction

Mo - The problem offset in the x direction

No - The problem offset in the y direction

Po - The problem offset in the z direction

This is used primarily to overlap a computation on a local DMDA with that on a global DMDA without changing boundary conditions or subdomain features that depend upon the global offsets.

DMDA - Creating vectors for structured grids, DM, DMDA, DMDAGetOffset(), DMDAVecGetArray()

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDASetOffset(DM da, PetscInt xo, PetscInt yo, PetscInt zo, PetscInt Mo, PetscInt No, PetscInt Po)
```

Example 2 (unknown):
```unknown
DMDAGetOffset()
```

Example 3 (unknown):
```unknown
DMDAVecGetArray()
```

---

## DMDASetOverlap#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetOverlap/

**Contents:**
- DMDASetOverlap#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the size of the per-processor overlap.

x - Overlap in the x direction

y - Overlap in the y direction

z - Overlap in the z direction

DMDA - Creating vectors for structured grids, DM, DMDA, DMCreateDomainDecomposition(), DMDAGetOverlap()

src/dm/tutorials/ex19.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDASetOverlap(DM da, PetscInt x, PetscInt y, PetscInt z)
```

Example 2 (unknown):
```unknown
DMCreateDomainDecomposition()
```

Example 3 (unknown):
```unknown
DMDAGetOverlap()
```

---

## DMDASetOwnershipRanges#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetOwnershipRanges/

**Contents:**
- DMDASetOwnershipRanges#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the number of nodes in each direction on each process

lx - array containing number of nodes in the X direction on each process, or NULL. If non-null, must be of length da->m

ly - array containing number of nodes in the Y direction on each process, or NULL. If non-null, must be of length da->n

lz - array containing number of nodes in the Z direction on each process, or NULL. If non-null, must be of length da->p.

These numbers are NOT multiplied by the number of dof per node.

DMDA - Creating vectors for structured grids, DM, DMDA, DMDACreate(), DMDestroy()

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDASetOwnershipRanges(DM da, const PetscInt lx[], const PetscInt ly[], const PetscInt lz[])
```

Example 2 (unknown):
```unknown
DMDACreate()
```

Example 3 (unknown):
```unknown
DMDestroy()
```

---

## DMDASetPreallocationCenterDimension#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetPreallocationCenterDimension/

**Contents:**
- DMDASetPreallocationCenterDimension#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Determine the topology used to determine adjacency

preallocCenterDim - The dimension of points which connect adjacent entries

DMDA - Creating vectors for structured grids, DM, DMDA, DMCreateMatrix(), DMDAPreallocateOperator()

src/dm/impls/da/dapreallocate.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDASetPreallocationCenterDimension(DM dm, PetscInt preallocCenterDim)
```

Example 2 (sass):
```sass
FEM:   Two points p and q are adjacent if q \in closure(star(p)), preallocCenterDim = dim
     FVM:   Two points p and q are adjacent if q \in star(cone(p)),    preallocCenterDim = dim-1
     FVM++: Two points p and q are adjacent if q \in star(closure(p)), preallocCenterDim = 0
```

Example 3 (unknown):
```unknown
DMCreateMatrix()
```

Example 4 (unknown):
```unknown
DMDAPreallocateOperator()
```

---

## DMDASetRefinementFactor#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetRefinementFactor/

**Contents:**
- DMDASetRefinementFactor#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#

Set the ratios that the DMDA grid is refined

refine_x - ratio of fine grid to coarse in the x direction (2 by default)

refine_y - ratio of fine grid to coarse in the y direction (2 by default)

refine_z - ratio of fine grid to coarse in the z direction (2 by default)

-da_refine_x refine_x - refinement ratio in the x direction

-da_refine_y rafine_y - refinement ratio in the y direction

-da_refine_z refine_z - refinement ratio in the z direction

-da_refine n - refine the DMDA object n times when it is created.

Pass PETSC_IGNORE to leave a value unchanged

DMDA - Creating vectors for structured grids, DM, DMDA, DMRefine(), DMDAGetRefinementFactor()

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDASetRefinementFactor(DM da, PetscInt refine_x, PetscInt refine_y, PetscInt refine_z)
```

Example 2 (unknown):
```unknown
PETSC_IGNORE
```

Example 3 (unknown):
```unknown
DMDAGetRefinementFactor()
```

---

## DMDASetSizes#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetSizes/

**Contents:**
- DMDASetSizes#
- Synopsis#
- Input Parameters#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the number of grid points in the three dimensional directions

M - the global X size

N - the global Y size

P - the global Z size

Since the dimension may not yet have been set the code cannot error check for non-positive Y and Z number of grid points

DMDA - Creating vectors for structured grids, DM, DMDA, PetscSplitOwnership()

src/dm/tutorials/ex19.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDASetSizes(DM da, PetscInt M, PetscInt N, PetscInt P)
```

Example 2 (unknown):
```unknown
PetscSplitOwnership()
```

---

## DMDASetStencilType#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetStencilType/

**Contents:**
- DMDASetStencilType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the type of the communication stencil

stype - The stencil type, use either DMDA_STENCIL_BOX or DMDA_STENCIL_STAR.

DMDA - Creating vectors for structured grids, DM, DMDA, DMDACreate(), DMDestroy(), DMDAStencilType, DMDA_STENCIL_BOX, DMDA_STENCIL_STAR.

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDASetStencilType(DM da, DMDAStencilType stype)
```

Example 2 (unknown):
```unknown
DMDA_STENCIL_BOX
```

Example 3 (unknown):
```unknown
DMDA_STENCIL_STAR
```

Example 4 (unknown):
```unknown
DMDACreate()
```

---

## DMDASetStencilWidth#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetStencilWidth/

**Contents:**
- DMDASetStencilWidth#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the width of the communication stencil

width - The stencil width

DMDA - Creating vectors for structured grids, DM, DMDA, DMDACreate(), DMDestroy(), DMDAStencilType, DMDA_STENCIL_BOX, DMDA_STENCIL_STAR.

src/dm/tutorials/ex19.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDASetStencilWidth(DM da, PetscInt width)
```

Example 2 (unknown):
```unknown
DMDACreate()
```

Example 3 (unknown):
```unknown
DMDestroy()
```

Example 4 (unknown):
```unknown
DMDAStencilType
```

---

## DMDASetUniformCoordinates#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetUniformCoordinates/

**Contents:**
- DMDASetUniformCoordinates#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets a DMDA coordinates to be a uniform grid

xmin - min extreme in the x direction

xmax - max extreme in the x direction

ymin - min extreme in the y direction (value ignored for 1 dimensional problems)

ymax - max extreme in the y direction (value ignored for 1 dimensional problems)

zmin - min extreme in the z direction (value ignored for 1 or 2 dimensional problems)

zmax - max extreme in the z direction (value ignored for 1 or 2 dimensional problems)

DMDA - Creating vectors for structured grids, DM, DMDA, DMSetCoordinates(), DMGetCoordinates(), DMDACreate1d(), DMDACreate2d(), DMDACreate3d(), DMStagSetUniformCoordinates()

src/dm/impls/da/gr1.c

src/snes/tutorials/ex55.c src/snes/tutorials/ex9.c src/snes/tutorials/ex5.c src/ksp/ksp/tutorials/ex70.c src/snes/tutorials/ex46.c src/snes/tutorials/ex35.c src/ksp/ksp/tutorials/ex49.c src/snes/tutorials/ex33.c src/snes/tutorials/ex22.c src/snes/tutorials/ex4.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDASetUniformCoordinates(DM da, PetscReal xmin, PetscReal xmax, PetscReal ymin, PetscReal ymax, PetscReal zmin, PetscReal zmax)
```

Example 2 (unknown):
```unknown
DMSetCoordinates()
```

Example 3 (unknown):
```unknown
DMGetCoordinates()
```

Example 4 (unknown):
```unknown
DMDACreate1d()
```

---

## DMDASetVertexCoordinates#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDASetVertexCoordinates/

**Contents:**
- DMDASetVertexCoordinates#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the lower and upper coordinates for a DMDA

xl - the lower x coordinate

xu - the upper x coordinate

yl - the lower y coordinate

yu - the upper y coordinate

zl - the lower z coordinate

zu - the upper z coordinate

DMPlex: Unstructured Grids, DM, DMDA

src/dm/impls/da/dalocal.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDASetVertexCoordinates(DM dm, PetscReal xl, PetscReal xu, PetscReal yl, PetscReal yu, PetscReal zl, PetscReal zu)
```

---

## DMDAStencilType#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAStencilType/

**Contents:**
- DMDAStencilType#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#
- Examples#
- Examples#

Determines if the stencil extends only along the coordinate directions, or also to the northeast, northwest etc

DM Basics, DMDA, DMDA_STENCIL_BOX, DMDA_STENCIL_STAR, DMDACreate1d(), DMDACreate2d(), DMDACreate3d(), DMDACreate(), DMDASetStencilType()

include/petscdmdatypes.h

src/snes/tutorials/ex55.c src/snes/tutorials/ex5f.F90 src/snes/tutorials/ex14.c src/snes/tutorials/ex18.c src/snes/tutorials/ex9.c src/snes/tutorials/ex35.c src/snes/tutorials/ex46.c src/snes/tutorials/ex5.c src/snes/tutorials/ex15.c src/snes/tutorials/ex25.c

src/snes/tutorials/ex5f90.F90 src/snes/tutorials/ex16.c src/snes/tutorials/ex73f90t.F90 src/snes/tutorials/ex40f90.F90 src/snes/tutorials/ex58.c src/ksp/ksp/tutorials/ex49.c src/snes/tutorials/ex48.c src/snes/tutorials/ex15.c src/snes/tutorials/ex5f90t.F90 src/snes/tutorials/ex4.c

src/ts/tutorials/ex14.c src/dm/tutorials/ex1.c src/ksp/ksp/tutorials/ex59.c src/dm/tutorials/ex12.c src/snes/tutorials/ex30.c src/dm/tutorials/ex3.c src/dm/tutorials/ex5.c src/snes/tutorials/ex48.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  DMDA_STENCIL_STAR,
  DMDA_STENCIL_BOX
} DMDAStencilType;
```

Example 2 (unknown):
```unknown
DMDA_STENCIL_BOX
```

Example 3 (unknown):
```unknown
DMDA_STENCIL_STAR
```

Example 4 (unknown):
```unknown
DMDACreate1d()
```

---

## DMDAVecGetArrayDOFRead#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAVecGetArrayDOFRead/

**Contents:**
- DMDAVecGetArrayDOFRead#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- Fortran Notes#
- See Also#
- Level#
- Location#
- Examples#

Returns a multiple dimension array that shares data with the underlying vector and is indexed using the global or local dimensions of a DMDA

vec - a vector the same size as one obtained with DMCreateGlobalVector() or DMCreateLocalVector()

Call DMDAVecRestoreArrayDOFRead() once you have finished accessing the vector entries.

In C, the indexing is “backwards” from what expects: array[k][j][i][DOF] NOT array[i][j][k][DOF]!

The accessible indices are array[zs:zs+zm-1][ys:ys+ym-1][xs:xs+xm-1] where the values are obtained from DMDAGetCorners() for a global vector or DMDAGetGhostCorners() for a local vector.

Use DMDAVecGetArrayRead() and pass for the array type PetscScalar,pointer :: array(:,…,:) of the appropriate dimension. For a DMDA created with a dof of 1 use the dimension of the DMDA, for a DMDA created with a dof greater than 1 use one more than the dimension of the DMDA.

The order of the indices is array(xs:xs+xm-1,ys:ys+ym-1,zs:zs+zm-1) (when dof is 1) otherwise array(0:dof-1,xs:xs+xm-1,ys:ys+ym-1,zs:zs+zm-1) where the values are obtained from DMDAGetCorners() for a global vector or DMDAGetGhostCorners() for a local vector.

DMDA - Creating vectors for structured grids, DMDA - Setting vector values, DM, DMDA, DMDAGetGhostCorners(), DMDAGetCorners(), VecGetArray(), VecRestoreArray(), DMDAVecRestoreArray(), DMDAVecGetArray(), DMDAVecGetArrayDOF(), DMDAVecGetArrayWrite(), DMDAVecRestoreArrayWrite(), DMDAVecGetArrayRead(), DMDAVecRestoreArrayRead()

src/dm/impls/da/dagetarray.c

src/ml/da/tutorials/ex4.c src/ts/tutorials/extchemfield.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAVecGetArrayDOFRead(DM da, Vec vec, void *array)
```

Example 2 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 3 (unknown):
```unknown
DMCreateLocalVector()
```

Example 4 (unknown):
```unknown
DMDAVecRestoreArrayDOFRead()
```

---

## DMDAVecGetArrayDOFWrite#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAVecGetArrayDOFWrite/

**Contents:**
- DMDAVecGetArrayDOFWrite#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- Fortran Notes#
- See Also#
- Level#
- Location#
- Examples#

Returns a multiple dimension array that shares data with the underlying vector and is indexed using the global or local dimensions of a DMDA

vec - a vector the same size as one obtained with DMCreateGlobalVector() or DMCreateLocalVector()

Call DMDAVecRestoreArrayDOFWrite() once you have finished accessing the vector entries.

In C, the indexing is “backwards” from what expects: array[k][j][i][DOF] NOT array[i][j][k][DOF]!

The accessible indices are array[zs:zs+zm-1][ys:ys+ym-1][xs:xs+xm-1][0:dof-1] where the values are obtained from DMDAGetCorners() for a global vector or DMDAGetGhostCorners() for a local vector.

Use DMDAVecGetArrayWrite() and pass for the array type PetscScalar,pointer :: array(:,…,:) of the appropriate dimension. For a DMDA created with a dof of 1 use the dimension of the DMDA, for a DMDA created with a dof greater than 1 use one more than the dimension of the DMDA.

The order of the indices is array(xs:xs+xm-1,ys:ys+ym-1,zs:zs+zm-1) (when dof is 1) otherwise array(0:dof-1,xs:xs+xm-1,ys:ys+ym-1,zs:zs+zm-1) where the values are obtained from DMDAGetCorners() for a global vector or DMDAGetGhostCorners() for a local vector.

DMDA - Creating vectors for structured grids, DMDA - Setting vector values, DM, DMDA, DMDAGetGhostCorners(), DMDAGetCorners(), VecGetArray(), VecRestoreArray(), DMDAVecRestoreArray(), DMDAVecGetArray(), DMDAVecGetArrayDOF(), DMDAVecGetArrayWrite(), DMDAVecRestoreArrayWrite()

src/dm/impls/da/dagetarray.c

src/ksp/ksp/tutorials/ex34.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAVecGetArrayDOFWrite(DM da, Vec vec, void *array)
```

Example 2 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 3 (unknown):
```unknown
DMCreateLocalVector()
```

Example 4 (unknown):
```unknown
DMDAVecRestoreArrayDOFWrite()
```

---

## DMDAVecGetArrayDOF#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAVecGetArrayDOF/

**Contents:**
- DMDAVecGetArrayDOF#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- Fortran Notes#
- See Also#
- Level#
- Location#
- Examples#

Returns a multiple dimension array that shares data with the underlying vector and is indexed using the global or local dimensions of a DMDA

vec - a vector the same size as one obtained with DMCreateGlobalVector() or DMCreateLocalVector()

array - the array pointer

Call DMDAVecRestoreArrayDOF() once you have finished accessing the vector entries.

In C, the indexing is “backwards” from what expects: array[k][j][i][DOF] NOT array[i][j][k][DOF]

The accessible indices are array[zs:zs+zm-1][ys:ys+ym-1][xs:xs+xm-1][0:ndof-1] where the values are obtained from DMDAGetCorners() for a global vector or DMDAGetGhostCorners() for a local vector.

Use DMDAVecGetArray() and pass for the array type PetscScalar,pointer :: array(:,…,:) of the appropriate dimension. For a DMDA created with a dof of 1 use the dimension of the DMDA, for a DMDA created with a dof greater than 1 use one more than the dimension of the DMDA.

The order of the indices is array(xs:xs+xm-1,ys:ys+ym-1,zs:zs+zm-1) (when ndof is 1) otherwise array(0:dof-1,xs:xs+xm-1,ys:ys+ym-1,zs:zs+zm-1) where the values are obtained from DMDAGetCorners() for a global vector or DMDAGetGhostCorners() for a local vector.

DMDA - Creating vectors for structured grids, DMDA - Setting vector values, DM, DMDA, DMDAGetGhostCorners(), DMDAGetCorners(), VecGetArray(), VecRestoreArray(), DMDAVecRestoreArray(), DMDAVecGetArray(), DMDAVecRestoreArrayDOF(), DMDAVecGetArrayWrite(), DMDAVecRestoreArrayWrite(), DMDAVecGetArrayRead(), DMDAVecRestoreArrayRead(), DMDAVecGetArrayDOFRead()

src/dm/impls/da/dagetarray.c

src/dm/tutorials/ex51.c src/ksp/ksp/tutorials/ex34.c src/dm/tutorials/ex15.c src/ml/da/tutorials/ex4.c src/ts/tutorials/ex12.c src/ts/tutorials/extchemfield.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAVecGetArrayDOF(DM da, Vec vec, void *array)
```

Example 2 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 3 (unknown):
```unknown
DMCreateLocalVector()
```

Example 4 (unknown):
```unknown
DMDAVecRestoreArrayDOF()
```

---

## DMDAVecGetArrayRead#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAVecGetArrayRead/

**Contents:**
- DMDAVecGetArrayRead#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- Fortran Notes#
- See Also#
- Level#
- Location#
- Examples#

Returns a multiple dimension array that shares data with the underlying vector and is indexed using the global or local dimensions of a DMDA.

vec - a vector the same size as one obtained with DMCreateGlobalVector() or DMCreateLocalVector()

Call DMDAVecRestoreArrayRead() once you have finished accessing the vector entries.

In C, the indexing is “backwards” from what expects: array[k][j][i] NOT array[i][j][k]!

If vec is a local vector (obtained with DMCreateLocalVector() etc) then the ghost point locations are accessible. If it is a global vector then the ghost points are not accessible. Of course with the local vector you will have had to do the appropriate DMGlobalToLocalBegin() and DMGlobalToLocalEnd() to have correct values in the ghost locations.

The accessible indices are array[zs:zs+zm-1][ys:ys+ym-1][xs:xs+xm-1] where the values are obtained from DMDAGetCorners() for a global vector or DMDAGetGhostCorners() for a local vector.

Use DMDAVecGetArrayRead() and pass for the array type PetscScalar,pointer :: array(:,…,:) of the appropriate dimension. For a DMDA created with a dof of 1 use the dimension of the DMDA, for a DMDA created with a dof greater than 1 use one more than the dimension of the DMDA.

The order of the indices is array(xs:xs+xm-1,ys:ys+ym-1,zs:zs+zm-1) (when dof is 1) otherwise array(0:dof-1,xs:xs+xm-1,ys:ys+ym-1,zs:zs+zm-1) where the values are obtained from DMDAGetCorners() for a global vector or DMDAGetGhostCorners() for a local vector.

DMDA - Creating vectors for structured grids, DMDA - Setting vector values, DM, DMDA, DMDAGetGhostCorners(), DMDAGetCorners(), VecGetArray(), VecRestoreArray(), DMDAVecRestoreArrayRead(), DMDAVecRestoreArrayDOF(), DMDAVecGetArrayDOF(), DMDAVecGetArray(), DMDAVecRestoreArray(), DMStagVecGetArrayRead()

src/dm/impls/da/dagetarray.c

src/ml/da/tutorials/ex3.c src/snes/tutorials/ex3k.kokkos.cxx src/snes/tutorials/ex14.c src/ml/da/tutorials/ex1.c src/snes/tutorials/ex19.c src/snes/tutorials/ex78.c src/ksp/ksp/tutorials/ex43.c src/snes/tutorials/ex15.c src/snes/tutorials/ex3.c src/ml/da/tutorials/ex2.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAVecGetArrayRead(DM da, Vec vec, void *array)
```

Example 2 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 3 (unknown):
```unknown
DMCreateLocalVector()
```

Example 4 (unknown):
```unknown
DMDAVecRestoreArrayRead()
```

---

## DMDAVecGetArrayWrite#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAVecGetArrayWrite/

**Contents:**
- DMDAVecGetArrayWrite#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- Fortran Notes#
- Developer Note#
- See Also#
- Level#
- Location#

Returns a multiple dimension array that shares data with the underlying vector and is indexed using the global or local dimensions of a DMDA.

vec - a vector the same size as one obtained with DMCreateGlobalVector() or DMCreateLocalVector()

Call DMDAVecRestoreArray() once you have finished accessing the vector entries.

In C, the indexing is “backwards” from what expects: array[k][j][i] NOT array[i][j][k]!

if vec is a local vector (obtained with DMCreateLocalVector() etc) then the ghost point locations are accessible. If it is a global vector then the ghost points are not accessible. Of course with the local vector you will have had to do the appropriate DMGlobalToLocalBegin() and DMGlobalToLocalEnd() to have correct values in the ghost locations.

The accessible indices are array[zs:zs+zm-1][ys:ys+ym-1][xs:xs+xm-1] where the values are obtained from DMDAGetCorners() for a global vector or DMDAGetGhostCorners() for a local vector.

Use DMDAVecGetArrayWrite() and pass for the array type PetscScalar,pointer :: array(:,…,:) of the appropriate dimension. For a DMDA created with a dof of 1 use the dimension of the DMDA, for a DMDA created with a dof greater than 1 use one more than the dimension of the DMDA.

The order of the indices is array(xs:xs+xm-1,ys:ys+ym-1,zs:zs+zm-1) (when dof is 1) otherwise array(0:dof-1,xs:xs+xm-1,ys:ys+ym-1,zs:zs+zm-1) where the values are obtained from DMDAGetCorners() for a global vector or DMDAGetGhostCorners() for a local vector.

This has code duplication with DMDAVecGetArray() and DMDAVecGetArrayRead()

DMDA - Creating vectors for structured grids, DMDA - Setting vector values, DM, DMDA, DMDAGetGhostCorners(), DMDAGetCorners(), VecGetArray(), VecRestoreArray(), DMDAVecRestoreArrayWrite(), DMDAVecRestoreArrayDOF(), DMDAVecGetArrayDOF(), DMDAVecGetArray(), DMDAVecRestoreArray(), DMDAVecGetArrayRead(), DMDAVecRestoreArrayRead()

src/dm/impls/da/dagetarray.c

src/dm/tutorials/ex2.c src/snes/tutorials/ex19.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAVecGetArrayWrite(DM da, Vec vec, void *array)
```

Example 2 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 3 (unknown):
```unknown
DMCreateLocalVector()
```

Example 4 (unknown):
```unknown
DMDAVecRestoreArray()
```

---

## DMDAVecGetArray#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAVecGetArray/

**Contents:**
- DMDAVecGetArray#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- Fortran Notes#
- See Also#
- Level#
- Location#
- Examples#

Returns a multiple dimension array that shares data with the underlying vector and is indexed using the global or local dimensions of a DMDA.

vec - a vector the same size as one obtained with DMCreateGlobalVector() or DMCreateLocalVector()

Call DMDAVecRestoreArray() once you have finished accessing the vector entries.

In C, the indexing is “backwards” from what expects: array[k][j][i] NOT array[i][j][k]!

If vec is a local vector (obtained with DMCreateLocalVector() etc) then the ghost point locations are accessible. If it is a global vector then the ghost points are not accessible. Of course, with a local vector you will have had to do the appropriate DMGlobalToLocalBegin() and DMGlobalToLocalEnd() to have correct values in the ghost locations.

The accessible indices are array[zs:zs+zm-1][ys:ys+ym-1][xs:xs+xm-1] where the values are obtained from DMDAGetCorners() for a global vector or DMDAGetGhostCorners() for a local vector.

Use DMDAVecGetArray() and pass for the array type PetscScalar,pointer :: array(:,…,:) of the appropriate dimension. For a DMDA created with a dof of 1 use the dimension of the DMDA, for a DMDA created with a dof greater than 1 use one more than the dimension of the DMDA.

The order of the indices is array(xs:xs+xm-1,ys:ys+ym-1,zs:zs+zm-1) (when dof is 1) otherwise array(0:dof-1,xs:xs+xm-1,ys:ys+ym-1,zs:zs+zm-1) where the values are obtained from DMDAGetCorners() for a global vector or DMDAGetGhostCorners() for a local vector.

DMDA - Creating vectors for structured grids, DMDA - Setting vector values, DM, DMDA, DMDAGetGhostCorners(), DMDAGetCorners(), VecGetArray(), VecRestoreArray(), DMDAVecRestoreArray(), DMDAVecRestoreArrayDOF(), DMDAVecGetArrayDOF(), DMDAVecGetArrayWrite(), DMDAVecRestoreArrayWrite(), DMDAVecGetArrayRead(), DMDAVecRestoreArrayRead(), DMStagVecGetArray()

src/dm/impls/da/dagetarray.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex14.c src/snes/tutorials/ex18.c src/snes/tutorials/ex15.c src/snes/tutorials/ex35.c src/snes/tutorials/ex46.c src/snes/tutorials/ex9.c src/snes/tutorials/ex22.c src/snes/tutorials/ex33.c src/snes/tutorials/ex21.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAVecGetArray(DM da, Vec vec, void *array)
```

Example 2 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 3 (unknown):
```unknown
DMCreateLocalVector()
```

Example 4 (unknown):
```unknown
DMDAVecRestoreArray()
```

---

## DMDAVecGetKokkosOffsetViewDOF#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAVecGetKokkosOffsetViewDOF/

**Contents:**
- DMDAVecGetKokkosOffsetViewDOF#
- Synopsis#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Gets a Kokkos OffsetView that contains up-to-date data of a vector in the given memory space, with DOF as the rightest dimension of the OffsetView

Logically Collective, No Fortran Support

da - the distributed array

v - the vector, either a vector the same size as one obtained with DMCreateGlobalVector() or DMCreateLocalVector()

kv - the Kokkos OffsetView with a user-specified template parameter MemorySpace

Call DMDAVecRestoreKokkosOffsetViewDOF() or DMDAVecRestoreKokkosOffsetViewDOFWrite() once you have finished accessing the OffsetView.

If the vector is not a VECKOKKOS an error will be raised.

If the vector is a local vector (obtained with DMCreateLocalVector() etc) then the ghost point locations are accessible. If it is a global vector then the ghost points are not accessible. Of course with the local vector you will have to do the appropriate DMGlobalToLocalBegin() and DMGlobalToLocalEnd() to have correct values in the ghost locations.

These routines are similar to DMDAVecGetArrayDOF() and friends. One can read-only, write-only or read/write access the returned Kokkos OffsetView. Note that passing in a constant OffsetView enables read-only access. Currently, only two memory spaces are supported: HostMirrorMemorySpace and Kokkos::DefaultExecutionSpace::memory_space. If needed, a memory copy will be internally called to copy the latest vector data to the given memory space.

In C, to access the returned array of DMDAVecGetArrayDOF(), the indexing is “backwards”, i.e., array[k][j][i][c] (instead of array[c][i][j][k]), where i, j, k are loop variables for the x, y, z dimensions respectively, and c is the loop variable for DOFs, as specified in DMDACreate3d(), for example.

To give users the same experience as DMDAVecGetArrayDOF(), we mandate the returned OffsetView always has Kokkos::LayoutRight (that is, rightest subscript has a stride 1, as in C multi-dimensional arrays), regardless of whether the memory space is host or device. Thus it is important to use Iterate::Right as IterateInner if one uses Kokkos::MDRangePolicy to access the OffsetView.

Note that for a 3D DMDA, the OffsetView kv’s first dimension (i.e., the leftest, dim 0) corresponds to DMDA’s z direction, and its second-to-last dimension (rightest) corresponds to DMDA’s x direction.

If the vector is a global vector, we have

If the vector is a local vector, we have

The starts and widths above are obtained by

For example, to initialize a grid,

DMDAVecRestoreKokkosOffsetViewDOF(), DMDAGetGhostCorners(), DMDAGetCorners(), VecGetArray(), VecRestoreArray(), DMDAVecRestoreArray(), DMDAVecRestoreArrayDOF() DMDAVecGetArrayDOF(), DMDAVecGetArrayWrite(), DMDAVecRestoreArrayWrite(), DMDAVecGetArrayRead(), DMDAVecRestoreArrayRead(), DMStagVecGetArray()

include/petscdmda_kokkos.hpp

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (jsx):
```jsx
template <class MemorySpace>
PetscErrorCode DMDAVecGetKokkosOffsetViewDOF(DM, Vec, Kokkos::Experimental::OffsetView<const PetscScalar **, Kokkos::LayoutRight, MemorySpace> *)
```

Example 2 (jsx):
```jsx
#include <petscdmda_kokkos.hpp>
PetscErrorCode DMDAVecGetKokkosOffsetViewDOF(DM da,Vec v,Kokkos::Experimental::OffsetView<const PetscScalar**,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecGetKokkosOffsetViewDOF(DM da,Vec v,Kokkos::Experimental::OffsetView<PetscScalar**,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecGetKokkosOffsetViewDOFWrite(DM da,Vec v,Kokkos::Experimental::OffsetView<PetscScalar**,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecGetKokkosOffsetViewDOF(DM da,Vec v,Kokkos::Experimental::OffsetView<const PetscScalar***,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecGetKokkosOffsetViewDOF(DM da,Vec v,Kokkos::Experimental::OffsetView<PetscScalar***,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecGetKokkosOffsetViewDOFWrite(DM da,Vec v,Kokkos::Experimental::OffsetView<PetscScalar***,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecGetKokkosOffsetViewDOF(DM da,Vec v,Kokkos::Experimental::OffsetView<const PetscScalar****,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecGetKokkosOffsetViewDOF(DM da,Vec v,Kokkos::Experimental::OffsetView<PetscScalar****,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecGetKokkosOffsetViewDOFWrite(DM da,Vec v,Kokkos::Experimental::OffsetView<PetscScalar****,Kokkos::LayoutRight,MemorySpace>* kv);
```

Example 3 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 4 (unknown):
```unknown
DMCreateLocalVector()
```

---

## DMDAVecGetKokkosOffsetView#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAVecGetKokkosOffsetView/

**Contents:**
- DMDAVecGetKokkosOffsetView#
- Synopsis#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Gets a Kokkos OffsetView that contains up-to-date data of a vector in the given memory space.

Logically Collective, No Fortran Support

da - the distributed array

v - the vector, either a vector the same size as one obtained with DMCreateGlobalVector() or DMCreateLocalVector()

kv - the Kokkos OffsetView with a user-specified template parameter MemorySpace

Call DMDAVecRestoreKokkosOffsetView() or DMDAVecRestoreKokkosOffsetViewWrite() once you have finished accessing the OffsetView.

If the vector is not of type VECKOKKOS, an error will be raised.

If the vector is a local vector (obtained with DMCreateLocalVector() etc) then the ghost point locations are accessible. If it is a global vector then the ghost points are not accessible. Of course with the local vector you will have to do the appropriate DMGlobalToLocalBegin() and DMGlobalToLocalEnd() to have correct values in the ghost locations.

These routines are similar to DMDAVecGetArray() and friends. One can read-only, write-only or read/write access the returned Kokkos OffsetView. Note that passing in a constant OffsetView enables read-only access. Currently, only two memory spaces are supported: HostMirrorMemorySpace and Kokkos::DefaultExecutionSpace::memory_space. If needed, a memory copy will be internally called to copy the latest vector data to the specified memory space.

In C, to access the returned array of DMDAVecGetArray(), the indexing is “backwards”, i.e., array[k][j][i] (instead of array[i][j][k]), where i, j, k are loop variables for the x, y, z dimensions respectively specified in DMDACreate3d(), for example.

To give users the same experience as DMDAVecGetArray(), we mandate the returned OffsetView always has Kokkos::LayoutRight (that is, rightest subscript has a stride 1, as in C multi-dimensional arrays), regardless of whether the memory space is host or device. Thus it is important to use Iterate::Right as IterateInner if one uses Kokkos::MDRangePolicy to access the OffsetView.

Note that the OffsetView kv’s first dimension (i.e., the leftest, dim 0) corresponds to the DMDA’s z direction, and its last dimension (rightest) corresponds to DMDA’s x direction.

If the vector is a global vector, we have

If the vector is a local vector, we have

The starts and widths above are obtained by

For example, to initialize a grid,

For a multi-component problem, one could cast the returned OffsetView to a user’s type. But one has also to shrink the OffsetView’s extent accordingly. For example,

DMDAVecRestoreKokkosOffsetView(), DMDAGetGhostCorners(), DMDAGetCorners(), VecGetArray(), VecRestoreArray(), DMDAVecRestoreArray(), DMDAVecRestoreArrayDOF() DMDAVecGetArrayDOF(), DMDAVecGetArrayWrite(), DMDAVecRestoreArrayWrite(), DMDAVecGetArrayRead(), DMDAVecRestoreArrayRead(), DMStagVecGetArray()

include/petscdmda_kokkos.hpp

src/snes/tutorials/ex55k.kokkos.cxx src/snes/tutorials/ex3k.kokkos.cxx

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (jsx):
```jsx
template <class MemorySpace>
PetscErrorCode DMDAVecGetKokkosOffsetView(DM, Vec, Kokkos::Experimental::OffsetView<const PetscScalar *, MemorySpace> *)
```

Example 2 (jsx):
```jsx
#include <petscdmda_kokkos.hpp>
PetscErrorCode DMDAVecGetKokkosOffsetView(DM da,Vec v,Kokkos::Experimental::OffsetView<const PetscScalar*,MemorySpace>* kv);
PetscErrorCode DMDAVecGetKokkosOffsetView(DM da,Vec v,Kokkos::Experimental::OffsetView<PetscScalar*,MemorySpace>* kv);
PetscErrorCode DMDAVecGetKokkosOffsetViewWrite(DM da,Vec v,Kokkos::Experimental::OffsetView<PetscScalar*,MemorySpace>* kv);
PetscErrorCode DMDAVecGetKokkosOffsetView(DM da,Vec v,Kokkos::Experimental::OffsetView<const PetscScalar**,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecGetKokkosOffsetView(DM da,Vec v,Kokkos::Experimental::OffsetView<PetscScalar**,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecGetKokkosOffsetViewWrite(DM da,Vec v,Kokkos::Experimental::OffsetView<PetscScalar**,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecGetKokkosOffsetView(DM da,Vec v,Kokkos::Experimental::OffsetView<const PetscScalar***,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecGetKokkosOffsetView(DM da,Vec v,Kokkos::Experimental::OffsetView<PetscScalar***,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecGetKokkosOffsetViewWrite(DM da,Vec v,Kokkos::Experimental::OffsetView<PetscScalar***,Kokkos::LayoutRight,MemorySpace>* kv);
```

Example 3 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 4 (unknown):
```unknown
DMCreateLocalVector()
```

---

## DMDAVecRestoreArrayDOFRead#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAVecRestoreArrayDOFRead/

**Contents:**
- DMDAVecRestoreArrayDOFRead#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Restores a multiple dimension array obtained with DMDAVecGetArrayDOFRead()

vec - a vector the same size as one obtained with DMCreateGlobalVector() or DMCreateLocalVector()

array - the array pointer

DMDA - Creating vectors for structured grids, DMDA - Setting vector values, DM, DMDA, DMDAGetGhostCorners(), DMDAGetCorners(), VecGetArray(), VecRestoreArray(), DMDAVecGetArray(), DMDAVecGetArrayDOF(), DMDAVecRestoreArrayDOF(), DMDAVecGetArrayWrite(), DMDAVecRestoreArrayWrite(), DMDAVecGetArrayRead(), DMDAVecRestoreArrayRead()

src/dm/impls/da/dagetarray.c

src/ml/da/tutorials/ex4.c src/ts/tutorials/extchemfield.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDAVecGetArrayDOFRead()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAVecRestoreArrayDOFRead(DM da, Vec vec, void *array)
```

Example 3 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 4 (unknown):
```unknown
DMCreateLocalVector()
```

---

## DMDAVecRestoreArrayDOFWrite#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAVecRestoreArrayDOFWrite/

**Contents:**
- DMDAVecRestoreArrayDOFWrite#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Restores a multiple dimension array obtained with DMDAVecGetArrayDOFWrite()

vec - a vector the same size as one obtained with DMCreateGlobalVector() or DMCreateLocalVector()

array - the array pointer

DMDA - Creating vectors for structured grids, DMDA - Setting vector values, DM, DMDA, DMDAGetGhostCorners(), DMDAGetCorners(), VecGetArray(), VecRestoreArray(), DMDAVecGetArray(), DMDAVecGetArrayDOF(), DMDAVecRestoreArrayDOF(), DMDAVecGetArrayWrite(), DMDAVecRestoreArrayWrite()

src/dm/impls/da/dagetarray.c

src/ksp/ksp/tutorials/ex34.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDAVecGetArrayDOFWrite()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAVecRestoreArrayDOFWrite(DM da, Vec vec, void *array)
```

Example 3 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 4 (unknown):
```unknown
DMCreateLocalVector()
```

---

## DMDAVecRestoreArrayDOF#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAVecRestoreArrayDOF/

**Contents:**
- DMDAVecRestoreArrayDOF#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Restores a multiple dimension array obtained with DMDAVecGetArrayDOF()

vec - vector the same size as one obtained with DMCreateGlobalVector() or DMCreateLocalVector()

array - the array point

DMDA - Creating vectors for structured grids, DMDA - Setting vector values, DM, DMDA, DMDAGetGhostCorners(), DMDAGetCorners(), VecGetArray(), VecRestoreArray(), DMDAVecGetArray(), DMDAVecGetArrayDOF(), DMDAVecGetArrayWrite(), DMDAVecRestoreArrayWrite(), DMDAVecGetArrayRead(), DMDAVecRestoreArrayRead()

src/dm/impls/da/dagetarray.c

src/dm/tutorials/ex51.c src/ksp/ksp/tutorials/ex34.c src/dm/tutorials/ex15.c src/ml/da/tutorials/ex4.c src/ts/tutorials/ex12.c src/ts/tutorials/extchemfield.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDAVecGetArrayDOF()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAVecRestoreArrayDOF(DM da, Vec vec, void *array)
```

Example 3 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 4 (unknown):
```unknown
DMCreateLocalVector()
```

---

## DMDAVecRestoreArrayRead#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAVecRestoreArrayRead/

**Contents:**
- DMDAVecRestoreArrayRead#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Restores a multiple dimension array obtained with DMDAVecGetArrayRead()

vec - vector the same size as one obtained with DMCreateGlobalVector() or DMCreateLocalVector()

array - the array pointer

DMDA - Creating vectors for structured grids, DMDA - Setting vector values, DM, DMDA, DMDAGetGhostCorners(), DMDAGetCorners(), VecGetArray(), VecRestoreArray(), DMDAVecGetArrayRead(), DMDAVecGetArray(), DMDAVecRestoreArray(), DMDAVecGetArrayWrite(), DMDAVecRestoreArrayWrite(), DMStagVecRestoreArrayRead()

src/dm/impls/da/dagetarray.c

src/ml/da/tutorials/ex3.c src/snes/tutorials/ex3k.kokkos.cxx src/snes/tutorials/ex14.c src/ml/da/tutorials/ex1.c src/snes/tutorials/ex19.c src/snes/tutorials/ex78.c src/ksp/ksp/tutorials/ex43.c src/snes/tutorials/ex15.c src/snes/tutorials/ex3.c src/ml/da/tutorials/ex2.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDAVecGetArrayRead()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAVecRestoreArrayRead(DM da, Vec vec, void *array)
```

Example 3 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 4 (unknown):
```unknown
DMCreateLocalVector()
```

---

## DMDAVecRestoreArrayWrite#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAVecRestoreArrayWrite/

**Contents:**
- DMDAVecRestoreArrayWrite#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Restores a multiple dimension array obtained with DMDAVecGetArrayWrite()

vec - a vector the same size as one obtained with DMCreateGlobalVector() or DMCreateLocalVector()

array - the array pointer

DMDA - Creating vectors for structured grids, DMDA - Setting vector values, DM, DMDA, DMDAGetGhostCorners(), DMDAGetCorners(), VecGetArray(), VecRestoreArray(), DMDAVecGetArrayWrite(), DMDAVecGetArray(), DMDAVecRestoreArray(), DMDAVecGetArrayRead(), DMDAVecRestoreArrayRead()

src/dm/impls/da/dagetarray.c

src/dm/tutorials/ex2.c src/snes/tutorials/ex19.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDAVecGetArrayWrite()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAVecRestoreArrayWrite(DM da, Vec vec, void *array)
```

Example 3 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 4 (unknown):
```unknown
DMCreateLocalVector()
```

---

## DMDAVecRestoreArray#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAVecRestoreArray/

**Contents:**
- DMDAVecRestoreArray#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Restores a multiple dimension array obtained with DMDAVecGetArray()

vec - a vector the same size as one obtained with DMCreateGlobalVector() or DMCreateLocalVector()

array - the array pointer

DMDA - Creating vectors for structured grids, DMDA - Setting vector values, DM, DMDA, DMDAGetGhostCorners(), DMDAGetCorners(), VecGetArray(), VecRestoreArray(), DMDAVecGetArray(), DMDAVecGetArrayWrite(), DMDAVecRestoreArrayWrite(), DMDAVecGetArrayRead(), DMDAVecRestoreArrayRead(), DMStagVecRestoreArray()

src/dm/impls/da/dagetarray.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex14.c src/snes/tutorials/ex18.c src/snes/tutorials/ex15.c src/snes/tutorials/ex35.c src/snes/tutorials/ex46.c src/snes/tutorials/ex9.c src/snes/tutorials/ex22.c src/snes/tutorials/ex33.c src/snes/tutorials/ex21.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDAVecGetArray()
```

Example 2 (unknown):
```unknown
#include "petscdmda.h"   
PetscErrorCode DMDAVecRestoreArray(DM da, Vec vec, void *array)
```

Example 3 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 4 (unknown):
```unknown
DMCreateLocalVector()
```

---

## DMDAVecRestoreKokkosOffsetViewDOF#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAVecRestoreKokkosOffsetViewDOF/

**Contents:**
- DMDAVecRestoreKokkosOffsetViewDOF#
- Synopsis#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Returns the Kokkos OffsetView that was gotten from DMDAVecGetKokkosOffsetViewDOF()

Logically Collective, No Fortran Support

da - the distributed array

v - the vector, either a vector the same size as one obtained with DMCreateGlobalVector() or DMCreateLocalVector()

kv - the Kokkos OffsetView with a user-specified template parameter MemorySpace

If the vector is not of type VECKOKKOS, an error will be raised.

DMDAVecGetKokkosOffsetViewDOF(), DMDAVecGetKokkosOffsetView(), DMDAGetGhostCorners(), DMDAGetCorners(), VecGetArray(), VecRestoreArray(), DMDAVecRestoreArray(), DMDAVecRestoreArrayDOF() DMDAVecGetArrayDOF(), DMDAVecGetArrayWrite(), DMDAVecRestoreArrayWrite(), DMDAVecGetArrayRead(), DMDAVecRestoreArrayRead(), DMStagVecGetArray()

include/petscdmda_kokkos.hpp

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDAVecGetKokkosOffsetViewDOF()
```

Example 2 (jsx):
```jsx
template <class MemorySpace>
PetscErrorCode DMDAVecRestoreKokkosOffsetViewDOF(DM, Vec, Kokkos::Experimental::OffsetView<const PetscScalar **, Kokkos::LayoutRight, MemorySpace> *)
```

Example 3 (jsx):
```jsx
#include <petscdmda_kokkos.hpp>
PetscErrorCode DMDAVecRestoreKokkosOffsetViewDOF(DM da,Vec v,Kokkos::Experimental::OffsetView<const PetscScalar**,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecRestoreKokkosOffsetViewDOF(DM da,Vec v,Kokkos::Experimental::OffsetView<PetscScalar**,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecRestoreKokkosOffsetViewDOFWrite(DM da,Vec v,Kokkos::Experimental::OffsetView<PetscScalar**,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecRestoreKokkosOffsetViewDOF(DM da,Vec v,Kokkos::Experimental::OffsetView<const PetscScalar***,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecRestoreKokkosOffsetViewDOF(DM da,Vec v,Kokkos::Experimental::OffsetView<PetscScalar***,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecRestoreKokkosOffsetViewDOFWrite(DM da,Vec v,Kokkos::Experimental::OffsetView<PetscScalar***,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecRestoreKokkosOffsetViewDOF(DM da,Vec v,Kokkos::Experimental::OffsetView<const PetscScalar****,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecRestoreKokkosOffsetViewDOF(DM da,Vec v,Kokkos::Experimental::OffsetView<PetscScalar****,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecRestoreKokkosOffsetViewDOFWrite(DM da,Vec v,Kokkos::Experimental::OffsetView<PetscScalar****,Kokkos::LayoutRight,MemorySpace>* kv);
```

Example 4 (unknown):
```unknown
DMCreateGlobalVector()
```

---

## DMDAVecRestoreKokkosOffsetView#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAVecRestoreKokkosOffsetView/

**Contents:**
- DMDAVecRestoreKokkosOffsetView#
- Synopsis#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Returns the Kokkos OffsetView that was gotten with DMDAVecGetKokkosOffsetView()

Logically Collective, No Fortran Support

da - the distributed array

v - the vector, either a vector the same size as one obtained with DMCreateGlobalVector() or DMCreateLocalVector()

kv - the Kokkos OffsetView with a user-specified template parameter MemorySpace

If the vector is not of type VECKOKKOS, an error will be raised.

DMDAVecGetKokkosOffsetView(), DMDAGetGhostCorners(), DMDAGetCorners(), VecGetArray(), VecRestoreArray(), DMDAVecRestoreArray(), DMDAVecRestoreArrayDOF() DMDAVecGetArrayDOF(), DMDAVecGetArrayWrite(), DMDAVecRestoreArrayWrite(), DMDAVecGetArrayRead(), DMDAVecRestoreArrayRead(), DMStagVecGetArray()

include/petscdmda_kokkos.hpp

src/snes/tutorials/ex55k.kokkos.cxx src/snes/tutorials/ex3k.kokkos.cxx

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDAVecGetKokkosOffsetView()
```

Example 2 (jsx):
```jsx
template <class MemorySpace>
PetscErrorCode DMDAVecRestoreKokkosOffsetView(DM, Vec, Kokkos::Experimental::OffsetView<const PetscScalar *, MemorySpace> *)
```

Example 3 (jsx):
```jsx
#include <petscdmda_kokkos.hpp>
PetscErrorCode DMDAVecRestoreKokkosOffsetView(DM da,Vec v,Kokkos::Experimental::OffsetView<const PetscScalar*,MemorySpace>* kv);
PetscErrorCode DMDAVecRestoreKokkosOffsetView(DM da,Vec v,Kokkos::Experimental::OffsetView<PetscScalar*,MemorySpace>* kv);
PetscErrorCode DMDAVecRestoreKokkosOffsetViewWrite(DM da,Vec v,Kokkos::Experimental::OffsetView<PetscScalar*,MemorySpace>* kv);
PetscErrorCode DMDAVecRestoreKokkosOffsetView(DM da,Vec v,Kokkos::Experimental::OffsetView<const PetscScalar**,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecRestoreKokkosOffsetView(DM da,Vec v,Kokkos::Experimental::OffsetView<PetscScalar**,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecRestoreKokkosOffsetViewWrite(DM da,Vec v,Kokkos::Experimental::OffsetView<PetscScalar**,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecRestoreKokkosOffsetView(DM da,Vec v,Kokkos::Experimental::OffsetView<const PetscScalar***,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecRestoreKokkosOffsetView(DM da,Vec v,Kokkos::Experimental::OffsetView<PetscScalar***,Kokkos::LayoutRight,MemorySpace>* kv);
PetscErrorCode DMDAVecRestoreKokkosOffsetViewWrite(DM da,Vec v,Kokkos::Experimental::OffsetView<PetscScalar***,Kokkos::LayoutRight,MemorySpace>* kv);
```

Example 4 (unknown):
```unknown
DMCreateGlobalVector()
```

---

## DMDAVTKWriteAll#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDAVTKWriteAll/

**Contents:**
- DMDAVTKWriteAll#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Write a file containing all the fields that have been provided to the viewer

odm - DMDA specifying the grid layout, passed as a PetscObject

viewer - viewer of type PETSCVIEWERVTK

This function is a callback used by the PETSCVIEWERVTK viewer to actually write the file. The reason for this odd model is that the VTK file format does not provide any way to write one field at a time. Instead, metadata for the entire file needs to be available up-front before you can start writing the file.

If any fields have been named (see e.g. DMDASetFieldName()), then individual scalar fields are written. Otherwise, a single multi-dof (vector) field is written.

DMDA - Creating vectors for structured grids, DMDA, DM, PETSCVIEWERVTK, DMDASetFieldName()

src/dm/impls/da/grvtk.c

DMDAVTKWriteAll_VTS() in src/dm/impls/da/grvtk.c DMDAVTKWriteAll_VTR() in src/dm/impls/da/grvtk.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"    
PetscErrorCode DMDAVTKWriteAll(PetscObject odm, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscObject
```

Example 3 (unknown):
```unknown
PETSCVIEWERVTK
```

Example 4 (unknown):
```unknown
PETSCVIEWERVTK
```

---

## DMDA#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDA/

**Contents:**
- DMDA#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

“da” - A DM object that is used to help solve PDEs on a structured grid (or mesh) in 1, 2, or 3 dimensions.

In the global representation of the vectors each process stores a non-overlapping rectangular (or slab in 3d) portion of the grid points. In the local representation these rectangular regions (slabs) are extended in all directions by a stencil width set with DMDASetStencilWidth().

The vectors can be thought of as either cell centered or vertex centered on the grid (or mesh). But some variables cannot be cell centered and others vertex centered; see the documentation for DMSTAG, a similar DM implementation which supports more general staggered grids.

Periodic boundary conditions can be handled by using a DMBoundaryType of DM_BOUNDARY_PERIODIC provided with DMDASetBoundaryType(). Other DMBoundaryTypevalues allow for different handling of terms along the boundary of the grid (or mesh).

DMDA - Creating vectors for structured grids, DMType, DMCOMPOSITE, DMSTAG, DMDACreate(), DMCreate(), DMSetType(), DMDASetStencilWidth(), DMDASetStencilType(), DMDAStencilType

src/dm/impls/da/dacreate.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex5f90.F90 src/snes/tutorials/ex5f.F90 src/snes/tutorials/ex14.c src/snes/tutorials/ex18.c src/snes/tutorials/ex9.c src/snes/tutorials/ex35.c src/snes/tutorials/ex78.c src/snes/tutorials/ex48.c src/snes/tutorials/ex15.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDASetStencilWidth()
```

Example 2 (unknown):
```unknown
DMBoundaryType
```

Example 3 (unknown):
```unknown
DM_BOUNDARY_PERIODIC
```

Example 4 (unknown):
```unknown
DMDASetBoundaryType()
```

---

## DMDA_STENCIL_BOX#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDA_STENCIL_BOX/

**Contents:**
- DMDA_STENCIL_BOX#
- Note#
- See Also#
- Level#
- Location#

“Box”-type stencil. In logical grid coordinates, any of (i,j,k), (i+s,j+r,k+t) may be in the stencil.

Determines what ghost point values are brought over to each process in DMGlobalToLocalBegin()/ DMGlobalToLocalEnd()

DM Basics, DMDA, DMDA_STENCIL_STAR, DMDAStencilType, DMDASetStencilType()

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMGlobalToLocalBegin()
```

Example 2 (unknown):
```unknown
DMGlobalToLocalEnd()
```

Example 3 (unknown):
```unknown
DMDA_STENCIL_STAR
```

Example 4 (unknown):
```unknown
DMDAStencilType
```

---

## DMDA_STENCIL_STAR#

**URL:** https://petsc.org/release/manualpages/DMDA/DMDA_STENCIL_STAR/

**Contents:**
- DMDA_STENCIL_STAR#
- Note#
- See Also#
- Level#
- Location#

“Star”-type stencil. In logical grid coordinates, only (i,j,k), (i+s,j,k), (i,j+s,k), (i,j,k+s) are in the stencil NOT, for example, (i+s,j+s,k)

Determines what ghost point values are brought over to each process in DMGlobalToLocalBegin()/ DMGlobalToLocalEnd(); in this case the “corner” values are not brought over and hence should not be accessed locally

DM Basics, DMDA, DMDA_STENCIL_BOX, DMDAStencilType, DMDASetStencilType()

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMGlobalToLocalBegin()
```

Example 2 (unknown):
```unknown
DMGlobalToLocalEnd()
```

Example 3 (unknown):
```unknown
DMDA_STENCIL_BOX
```

Example 4 (unknown):
```unknown
DMDAStencilType
```

---

## DMPatchCreateGrid#

**URL:** https://petsc.org/release/manualpages/DMPatch/DMPatchCreateGrid/

**Contents:**
- DMPatchCreateGrid#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Create a DMPATCH whose coarse DM is a structured DMDA of the requested global size, with the given patch and process-grid sizes

comm - the MPI communicator

dim - the spatial dimension (1, 2, or 3); unused dimensions of gridSize and patchSize are forced to 1

patchSize - MatStencil giving the size of each patch in cells

commSize - MatStencil giving the process grid used per patch (see DMPatchSetCommSize())

gridSize - MatStencil giving the global cell count of the underlying DMDA in each dimension

dm - the newly created DMPATCH

The coarse DM is created as a DMDA with a single degree of freedom per node, stencil width 1, and DM_BOUNDARY_NONE on every side.

DMPATCH, DMPatchCreate(), DMPatchSetPatchSize(), DMPatchSetCommSize(), DMDA, MatStencil

src/dm/impls/patch/patchcreate.c

Index of all DMPatch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmpatch.h"   
PetscErrorCode DMPatchCreateGrid(MPI_Comm comm, PetscInt dim, MatStencil patchSize, MatStencil commSize, MatStencil gridSize, DM *dm)
```

Example 2 (unknown):
```unknown
DMPatchSetCommSize()
```

Example 3 (unknown):
```unknown
DM_BOUNDARY_NONE
```

Example 4 (unknown):
```unknown
DMPatchCreate()
```

---

## DMPatchCreate#

**URL:** https://petsc.org/release/manualpages/DMPatch/DMPatchCreate/

**Contents:**
- DMPatchCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a DMPatch object, which is a collections of DMs called patches.

comm - The communicator for the DMPatch object

mesh - The DMPatch object

This code is incomplete and not used by other parts of PETSc.

src/dm/impls/patch/patchcreate.c

Index of all DMPatch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmpatch.h"   
PetscErrorCode DMPatchCreate(MPI_Comm comm, DM *mesh)
```

Example 2 (unknown):
```unknown
DMPatchZoom()
```

---

## DMPatchGetCoarse#

**URL:** https://petsc.org/release/manualpages/DMPatch/DMPatchGetCoarse/

**Contents:**
- DMPatchGetCoarse#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the coarse DM associated with a DMPATCH

dmCoarse - the coarse DM

DMPATCH, DMPatchCreate(), DMPatchZoom()

src/dm/impls/patch/patch.c

Index of all DMPatch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmpatch.h"   
PetscErrorCode DMPatchGetCoarse(DM dm, DM *dmCoarse)
```

Example 2 (unknown):
```unknown
DMPatchCreate()
```

Example 3 (unknown):
```unknown
DMPatchZoom()
```

---

## DMPatchGetCommSize#

**URL:** https://petsc.org/release/manualpages/DMPatch/DMPatchGetCommSize/

**Contents:**
- DMPatchGetCommSize#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the process grid used for each patch of a DMPATCH

commSize - a MatStencil whose i, j, k fields hold the number of processes used per patch in each dimension

DMPATCH, DMPatchSetCommSize(), DMPatchGetPatchSize(), MatStencil

src/dm/impls/patch/patch.c

Index of all DMPatch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmpatch.h"   
PetscErrorCode DMPatchGetCommSize(DM dm, MatStencil *commSize)
```

Example 2 (unknown):
```unknown
DMPatchSetCommSize()
```

Example 3 (unknown):
```unknown
DMPatchGetPatchSize()
```

---

## DMPatchGetPatchSize#

**URL:** https://petsc.org/release/manualpages/DMPatch/DMPatchGetPatchSize/

**Contents:**
- DMPatchGetPatchSize#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the size of a single patch of a DMPATCH, in grid cells

patchSize - a MatStencil whose i, j, k, c fields hold the patch extent in each dimension

DMPATCH, DMPatchSetPatchSize(), DMPatchGetCommSize(), MatStencil

src/dm/impls/patch/patch.c

Index of all DMPatch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmpatch.h"   
PetscErrorCode DMPatchGetPatchSize(DM dm, MatStencil *patchSize)
```

Example 2 (unknown):
```unknown
DMPatchSetPatchSize()
```

Example 3 (unknown):
```unknown
DMPatchGetCommSize()
```

---

## DMPatchSetCommSize#

**URL:** https://petsc.org/release/manualpages/DMPatch/DMPatchSetCommSize/

**Contents:**
- DMPatchSetCommSize#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the process grid used for each patch of a DMPATCH

commSize - a MatStencil whose i, j, k fields hold the number of processes to use per patch in each dimension

DMPATCH, DMPatchGetCommSize(), DMPatchSetPatchSize(), MatStencil

src/dm/impls/patch/patch.c

Index of all DMPatch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmpatch.h"   
PetscErrorCode DMPatchSetCommSize(DM dm, MatStencil commSize)
```

Example 2 (unknown):
```unknown
DMPatchGetCommSize()
```

Example 3 (unknown):
```unknown
DMPatchSetPatchSize()
```

---

## DMPatchSetPatchSize#

**URL:** https://petsc.org/release/manualpages/DMPatch/DMPatchSetPatchSize/

**Contents:**
- DMPatchSetPatchSize#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the size of a single patch of a DMPATCH, in grid cells

patchSize - a MatStencil whose i, j, k, c fields hold the patch extent in each dimension

DMPATCH, DMPatchGetPatchSize(), DMPatchSetCommSize(), MatStencil

src/dm/impls/patch/patch.c

Index of all DMPatch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmpatch.h"   
PetscErrorCode DMPatchSetPatchSize(DM dm, MatStencil patchSize)
```

Example 2 (unknown):
```unknown
DMPatchGetPatchSize()
```

Example 3 (unknown):
```unknown
DMPatchSetCommSize()
```

---

## DMPatchSolve#

**URL:** https://petsc.org/release/manualpages/DMPatch/DMPatchSolve/

**Contents:**
- DMPatchSolve#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#

Iterate over all patches of a DMPATCH, zooming the coarse DM onto each patch and scattering data between the coarse and zoomed representations

This code is a work in progress and is not currently used by other parts of PETSc. It implements the outer loop of the FAS/multigrid-like patch solver sketched at the top of the source file.

DMPATCH, DMPatchZoom(), DMPatchGetCoarse(), DMPatchGetPatchSize(), DMPatchGetCommSize()

src/dm/impls/patch/patch.c

Index of all DMPatch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmpatch.h"   
PetscErrorCode DMPatchSolve(DM dm)
```

Example 2 (unknown):
```unknown
DMPatchZoom()
```

Example 3 (unknown):
```unknown
DMPatchGetCoarse()
```

Example 4 (unknown):
```unknown
DMPatchGetPatchSize()
```

---

## DMPatchZoom#

**URL:** https://petsc.org/release/manualpages/DMPatch/DMPatchZoom/

**Contents:**
- DMPatchZoom#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#

Create patches of a DMDA on subsets of processes, indicated by commz

lower - the lower left corner of the requested patch

upper - the upper right corner of the requested patch

commz - the new communicator for the patch, MPI_COMM_NULL indicates that the given rank will not own a patch

sfz - the PetscSF mapping the patch+halo to the zoomed version (optional)

sfzr - the PetscSF mapping the patch to the restricted zoomed version

DMPatchSolve(), DMDACreatePatchIS()

src/dm/impls/patch/patch.c

src/dm/tutorials/ex25.c

Index of all DMPatch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmpatch.h"   
PetscErrorCode DMPatchZoom(DM dm, MatStencil lower, MatStencil upper, MPI_Comm commz, DM *dmz, PeOp PetscSF *sfz, PeOp PetscSF *sfzr)
```

Example 2 (unknown):
```unknown
MPI_COMM_NULL
```

Example 3 (unknown):
```unknown
DMPatchSolve()
```

Example 4 (unknown):
```unknown
DMDACreatePatchIS()
```

---

## DMPATCH#

**URL:** https://petsc.org/release/manualpages/DMPatch/DMPATCH/

**Contents:**
- DMPATCH#
- Synopsis#
- See Also#
- Level#
- Location#

DM object that encapsulates a domain divided into many patches

DM, DMPatchCreate(), DMPatchSolve(), DMPatchZoom(), DMPatchGetPatchSize(), DMPatchSetPatchSize(), DMPatchGetCommSize(), DMPatchSetCommSize(), DMPatchGetCoarse(), DMPatchCreateGrid()

include/petscdmpatch.h

Index of all DMPatch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_EXTERN PetscErrorCode DMPatchCreate(MPI_Comm, DM *);
```

Example 2 (unknown):
```unknown
DMPatchCreate()
```

Example 3 (unknown):
```unknown
DMPatchSolve()
```

Example 4 (unknown):
```unknown
DMPatchZoom()
```

---

## DMStagCreate1d#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagCreate1d/

**Contents:**
- DMStagCreate1d#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Create an object to manage data living on the elements and vertices of a parallelized regular 1D grid.

comm - MPI communicator

bndx - boundary type: DM_BOUNDARY_NONE, DM_BOUNDARY_PERIODIC, or DM_BOUNDARY_GHOSTED

M - global number of elements

dof0 - number of degrees of freedom per vertex/0-cell

dof1 - number of degrees of freedom per element/1-cell

stencilType - ghost/halo region type: DMSTAG_STENCIL_BOX or DMSTAG_STENCIL_NONE

stencilWidth - width, in elements, of halo/ghost region

lx - array of local sizes, of length equal to the comm size, summing to M or NULL

dm - the new DMSTAG object

-dm_view - calls DMViewFromOptions() at the conclusion of DMSetUp()

-stag_grid_x nx - number of elements in the x direction

-stag_ghost_stencil_width - width of ghost region, in elements

-stag_boundary_type_x (none|ghosted|periodic) - DMBoundaryType value

You must call DMSetUp() after this call before using the DM. If you wish to use the options database (see the keys above) to change values in the DMSTAG, you must call DMSetFromOptions() after this function but before DMSetUp().

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagCreate2d(), DMStagCreate3d(), DMDestroy(), DMView(), DMCreateGlobalVector(), DMCreateLocalVector(), DMLocalToGlobalBegin(), DMDACreate1d()

src/dm/impls/stag/stag1d.c

src/dm/impls/stag/tutorials/ex1.c src/dm/impls/stag/tutorials/ex8.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
PetscErrorCode DMStagCreate1d(MPI_Comm comm, DMBoundaryType bndx, PetscInt M, PetscInt dof0, PetscInt dof1, DMStagStencilType stencilType, PetscInt stencilWidth, const PetscInt lx[], DM *dm)
```

Example 2 (unknown):
```unknown
DM_BOUNDARY_NONE
```

Example 3 (unknown):
```unknown
DM_BOUNDARY_PERIODIC
```

Example 4 (unknown):
```unknown
DM_BOUNDARY_GHOSTED
```

---

## DMStagCreate2d#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagCreate2d/

**Contents:**
- DMStagCreate2d#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Create an object to manage data living on the elements, faces, and vertices of a parallelized regular 2D grid.

comm - MPI communicator

bndx - x boundary type, DM_BOUNDARY_NONE, DM_BOUNDARY_PERIODIC, or DM_BOUNDARY_GHOSTED

bndy - y boundary type, DM_BOUNDARY_NONE, DM_BOUNDARY_PERIODIC, or DM_BOUNDARY_GHOSTED

M - global number of elements in x direction

N - global number of elements in y direction

m - number of ranks in the x direction (may be PETSC_DECIDE)

n - number of ranks in the y direction (may be PETSC_DECIDE)

dof0 - number of degrees of freedom per vertex/0-cell

dof1 - number of degrees of freedom per face/1-cell

dof2 - number of degrees of freedom per element/2-cell

stencilType - ghost/halo region type: DMSTAG_STENCIL_NONE, DMSTAG_STENCIL_BOX, or DMSTAG_STENCIL_STAR

stencilWidth - width, in elements, of halo/ghost region

lx - array of local x element counts, of length equal to m, summing to M, or NULL

ly - array of local y element counts, of length equal to n, summing to N, or NULL

dm - the new DMSTAG object

-dm_view - calls DMViewFromOptions() at the conclusion of DMSetUp()

-stag_grid_x nx - number of elements in the x direction

-stag_grid_y ny - number of elements in the y direction

-stag_ranks_x rx - number of ranks in the x direction

-stag_ranks_y ry - number of ranks in the y direction

-stag_ghost_stencil_width - width of ghost region, in elements

-stag_boundary_type_x (none|ghosted|periodic) - DMBoundaryType value

-stag_boundary_type_y (none|ghosted|periodic) - DMBoundaryType value

You must call DMSetUp() after this call, before using the DM. If you wish to use the options database (see the keys above) to change values in the DMSTAG, you must call DMSetFromOptions() after this function but before DMSetUp().

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagCreate1d(), DMStagCreate3d(), DMDestroy(), DMView(), DMCreateGlobalVector(), DMCreateLocalVector(), DMLocalToGlobalBegin(), DMDACreate2d()

src/dm/impls/stag/stag2d.c

src/dm/impls/stag/tutorials/ex2.c src/dm/impls/stag/tutorials/ex4.c src/dm/impls/stag/tutorials/ex6.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
PetscErrorCode DMStagCreate2d(MPI_Comm comm, DMBoundaryType bndx, DMBoundaryType bndy, PetscInt M, PetscInt N, PetscInt m, PetscInt n, PetscInt dof0, PetscInt dof1, PetscInt dof2, DMStagStencilType stencilType, PetscInt stencilWidth, const PetscInt lx[], const PetscInt ly[], DM *dm)
```

Example 2 (unknown):
```unknown
DM_BOUNDARY_NONE
```

Example 3 (unknown):
```unknown
DM_BOUNDARY_PERIODIC
```

Example 4 (unknown):
```unknown
DM_BOUNDARY_GHOSTED
```

---

## DMStagCreate3d#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagCreate3d/

**Contents:**
- DMStagCreate3d#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Create an object to manage data living on the elements, faces, edges, and vertices of a parallelized regular 3D grid.

comm - MPI communicator

bndx - x boundary type, DM_BOUNDARY_NONE, DM_BOUNDARY_PERIODIC, or DM_BOUNDARY_GHOSTED

bndy - y boundary type, DM_BOUNDARY_NONE, DM_BOUNDARY_PERIODIC, or DM_BOUNDARY_GHOSTED

bndz - z boundary type, DM_BOUNDARY_NONE, DM_BOUNDARY_PERIODIC, or DM_BOUNDARY_GHOSTED

M - global number of elements in x direction

N - global number of elements in y direction

P - global number of elements in z direction

m - number of ranks in the x direction (may be PETSC_DECIDE)

n - number of ranks in the y direction (may be PETSC_DECIDE)

p - number of ranks in the z direction (may be PETSC_DECIDE)

dof0 - number of degrees of freedom per vertex/0-cell

dof1 - number of degrees of freedom per edge/1-cell

dof2 - number of degrees of freedom per face/2-cell

dof3 - number of degrees of freedom per element/3-cell

stencilType - ghost/halo region type: DMSTAG_STENCIL_NONE, DMSTAG_STENCIL_BOX, or DMSTAG_STENCIL_STAR

stencilWidth - width, in elements, of halo/ghost region

lx - array of local x element counts, of length equal to m, summing to M, or NULL

ly - arrays of local y element counts, of length equal to n, summing to N, or NULL

lz - arrays of local z element counts, of length equal to p, summing to P, or NULL

dm - the new DMSTAG object

-dm_view - calls DMViewFromOptions() at the conclusion of DMSetUp()

-stag_grid_x nx - number of elements in the x direction

-stag_grid_y ny - number of elements in the y direction

-stag_grid_z nz - number of elements in the z direction

-stag_ranks_x rx - number of ranks in the x direction

-stag_ranks_y ry - number of ranks in the y direction

-stag_ranks_z rz - number of ranks in the z direction

-stag_ghost_stencil_width - width of ghost region, in elements

-stag_boundary_type x (none|ghosted|periodic) - DMBoundaryType value

-stag_boundary_type y (none|ghosted|periodic) - DMBoundaryType value

-stag_boundary_type z (none|ghosted|periodic) - DMBoundaryType value

You must call DMSetUp() after this call before using the DM. If you wish to use the options database (see the keys above) to change values in the DMSTAG, you must call DMSetFromOptions() after this function but before DMSetUp().

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagCreate1d(), DMStagCreate2d(), DMDestroy(), DMView(), DMCreateGlobalVector(), DMCreateLocalVector(), DMLocalToGlobalBegin(), DMDACreate3d()

src/dm/impls/stag/stag3d.c

src/dm/impls/stag/tutorials/ex3.c src/dm/impls/stag/tutorials/ex4.c src/dm/impls/stag/tutorials/ex6.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
PetscErrorCode DMStagCreate3d(MPI_Comm comm, DMBoundaryType bndx, DMBoundaryType bndy, DMBoundaryType bndz, PetscInt M, PetscInt N, PetscInt P, PetscInt m, PetscInt n, PetscInt p, PetscInt dof0, PetscInt dof1, PetscInt dof2, PetscInt dof3, DMStagStencilType stencilType, PetscInt stencilWidth, const PetscInt lx[], const PetscInt ly[], const PetscInt lz[], DM *dm)
```

Example 2 (unknown):
```unknown
DM_BOUNDARY_NONE
```

Example 3 (unknown):
```unknown
DM_BOUNDARY_PERIODIC
```

Example 4 (unknown):
```unknown
DM_BOUNDARY_GHOSTED
```

---

## DMStagCreateCompatibleDMStag#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagCreateCompatibleDMStag/

**Contents:**
- DMStagCreateCompatibleDMStag#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

create a compatible DMSTAG with different dof/stratum

dm - the DMSTAG object

dof0 - number of dof on the first stratum in the new DMSTAG

dof1 - number of dof on the second stratum in the new DMSTAG

dof2 - number of dof on the third stratum in the new DMSTAG

dof3 - number of dof on the fourth stratum in the new DMSTAG

newdm - the new, compatible DMSTAG

DOF supplied for strata too big for the dimension are ignored; these may be set to 0. For example, for a 2-dimensional DMSTAG, dof2 sets the number of dof per element, and dof3 is unused. For a 3-dimensional DMSTAG, dof3 sets the number of DOF per element.

In contrast to DMDACreateCompatibleDMDA(), coordinates are not reused.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMDACreateCompatibleDMDA(), DMGetCompatibility(), DMStagMigrateVec()

src/dm/impls/stag/stagutils.c

src/dm/impls/stag/tutorials/ex4.c src/dm/impls/stag/tutorials/ex1.c src/dm/impls/stag/tutorials/ex6.c src/dm/impls/stag/tutorials/ex3.c src/dm/impls/stag/tutorials/ex2.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagCreateCompatibleDMStag(DM dm, PetscInt dof0, PetscInt dof1, PetscInt dof2, PetscInt dof3, DM *newdm)
```

Example 2 (unknown):
```unknown
DMDACreateCompatibleDMDA()
```

Example 3 (unknown):
```unknown
DMDACreateCompatibleDMDA()
```

Example 4 (unknown):
```unknown
DMGetCompatibility()
```

---

## DMStagCreateISFromStencils#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagCreateISFromStencils/

**Contents:**
- DMStagCreateISFromStencils#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Create an IS, using global numberings, for a subset of DOF in a DMSTAG object

dm - the DMSTAG object

n_stencil - the number of stencils provided

stencils - an array of DMStagStencil objects (i, j, and k are ignored)

Redundant entries in the stencils argument are ignored

DMSTAG: Staggered, Structured Grid, DMSTAG, IS, DMStagStencil, DMCreateGlobalVector

src/dm/impls/stag/stagstencil.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
PetscErrorCode DMStagCreateISFromStencils(DM dm, PetscInt n_stencil, DMStagStencil stencils[], IS *is)
```

Example 2 (unknown):
```unknown
DMStagStencil
```

Example 3 (unknown):
```unknown
DMStagStencil
```

Example 4 (unknown):
```unknown
DMCreateGlobalVector
```

---

## DMStagGetBoundaryTypes#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagGetBoundaryTypes/

**Contents:**
- DMStagGetBoundaryTypes#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#

dm - the DMSTAG object

boundaryTypeX - boundary type for x direction

boundaryTypeY - boundary type for y direction, not set for one dimensional problems

boundaryTypeZ - boundary type for z direction, not set for one and two dimensional problems

DMSTAG: Staggered, Structured Grid, DMSTAG, DMBoundaryType

src/dm/impls/stag/stagutils.c

src/dm/impls/stag/tutorials/ex1.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagGetBoundaryTypes(DM dm, DMBoundaryType *boundaryTypeX, DMBoundaryType *boundaryTypeY, DMBoundaryType *boundaryTypeZ)
```

Example 2 (unknown):
```unknown
DMBoundaryType
```

---

## DMStagGetCorners#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagGetCorners/

**Contents:**
- DMStagGetCorners#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

return global element indices of the local region (excluding ghost points)

dm - the DMSTAG object

x - starting element index in first direction

y - starting element index in second direction

z - starting element index in third direction

m - element width in first direction

n - element width in second direction

p - element width in third direction

nExtrax - number of extra partial elements in first direction

nExtray - number of extra partial elements in second direction

nExtraz - number of extra partial elements in third direction

Arguments corresponding to higher dimensions are ignored for 1D and 2D grids. These arguments may be set to NULL in this case.

The number of extra partial elements is either 1 or 0. The value is 1 on right, top, and front non-periodic domain (“physical”) boundaries, in the x, y, and z directions respectively, and otherwise 0.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagGetGhostCorners(), DMDAGetCorners()

src/dm/impls/stag/stagutils.c

src/dm/impls/stag/tutorials/ex4.c src/dm/impls/stag/tutorials/ex1.c src/dm/impls/stag/tutorials/ex8.c src/dm/impls/stag/tutorials/ex6.c src/dm/impls/stag/tutorials/ex3.c src/dm/impls/stag/tutorials/ex2.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagGetCorners(DM dm, PetscInt *x, PetscInt *y, PetscInt *z, PetscInt *m, PetscInt *n, PetscInt *p, PetscInt *nExtrax, PetscInt *nExtray, PetscInt *nExtraz)
```

Example 2 (unknown):
```unknown
DMStagGetGhostCorners()
```

Example 3 (unknown):
```unknown
DMDAGetCorners()
```

---

## DMStagGetDOF#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagGetDOF/

**Contents:**
- DMStagGetDOF#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

get number of DOF associated with each stratum of the grid

dm - the DMSTAG object

dof0 - the number of points per 0-cell (vertex/node)

dof1 - the number of points per 1-cell (element in 1D, edge in 2D and 3D)

dof2 - the number of points per 2-cell (element in 2D, face in 3D)

dof3 - the number of points per 3-cell (element in 3D)

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagGetCorners(), DMStagGetGhostCorners(), DMStagGetGlobalSizes(), DMStagGetStencilWidth(), DMStagGetBoundaryTypes(), DMStagGetLocationDOF(), DMDAGetDof()

src/dm/impls/stag/stagutils.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagGetDOF(DM dm, PetscInt *dof0, PetscInt *dof1, PetscInt *dof2, PetscInt *dof3)
```

Example 2 (unknown):
```unknown
DMStagGetCorners()
```

Example 3 (unknown):
```unknown
DMStagGetGhostCorners()
```

Example 4 (unknown):
```unknown
DMStagGetGlobalSizes()
```

---

## DMStagGetEntriesLocal#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagGetEntriesLocal/

**Contents:**
- DMStagGetEntriesLocal#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

get number of entries in the local representation

dm - the DMSTAG object

entries - number of entries in the local representation

This is the number of entries on this rank in the local representation. That is, it is value of size returned by VecGetSize(vec,&size) or VecGetLocalSize(vec,&size) when DMCreateLocalVector(dm,&vec) is used to create a Vec. Users would typically use these functions.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagGetDOF(), DMStagGetEntries(), DMStagGetEntriesPerElement(), DMCreateLocalVector()

src/dm/impls/stag/stagutils.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagGetEntriesLocal(DM dm, PetscInt *entries)
```

Example 2 (unknown):
```unknown
VecGetSize(vec,&size)
```

Example 3 (unknown):
```unknown
VecGetLocalSize(vec,&size)
```

Example 4 (unknown):
```unknown
DMCreateLocalVector(dm,&vec)
```

---

## DMStagGetEntriesPerElement#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagGetEntriesPerElement/

**Contents:**
- DMStagGetEntriesPerElement#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

get number of entries per element in the local representation

dm - the DMSTAG object

entriesPerElement - number of entries associated with each element in the local representation

This is the natural block size for most local operations. In 1D it is equal to dof0 \(+\) dof1, in 2D it is equal to dof0 \(+ 2\)dof1 \(+\) dof2, and in 3D it is equal to dof0 \(+ 3\)dof1 \(+ 3\)dof2 \(+\) dof3

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagGetDOF()

src/dm/impls/stag/stagutils.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagGetEntriesPerElement(DM dm, PetscInt *entriesPerElement)
```

Example 2 (unknown):
```unknown
DMStagGetDOF()
```

---

## DMStagGetEntries#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagGetEntries/

**Contents:**
- DMStagGetEntries#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

get number of native entries in the global representation

dm - the DMSTAG object

entries - number of rank-native entries in the global representation

This is the number of entries on this rank for a global vector associated with dm. That is, it is value of size returned by VecGetLocalSize(vec,&size) when DMCreateGlobalVector(dm,&vec) is used to create a Vec`. Users would typically use these functions.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagGetDOF(), DMStagGetEntriesLocal(), DMStagGetEntriesPerElement(), DMCreateLocalVector()

src/dm/impls/stag/stagutils.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagGetEntries(DM dm, PetscInt *entries)
```

Example 2 (unknown):
```unknown
VecGetLocalSize(vec,&size)
```

Example 3 (unknown):
```unknown
DMCreateGlobalVector(dm,&vec) is used to create a
```

Example 4 (unknown):
```unknown
DMStagGetDOF()
```

---

## DMStagGetGhostCorners#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagGetGhostCorners/

**Contents:**
- DMStagGetGhostCorners#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

return global element indices of the local region, including ghost points

dm - the DMSTAG object

x - the starting element index in the first direction

y - the starting element index in the second direction

z - the starting element index in the third direction

m - the element width in the first direction

n - the element width in the second direction

p - the element width in the third direction

Arguments corresponding to higher dimensions are ignored for 1D and 2D grids. These arguments may be set to NULL in this case.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagGetCorners(), DMDAGetGhostCorners()

src/dm/impls/stag/stagutils.c

src/dm/impls/stag/tutorials/ex4.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagGetGhostCorners(DM dm, PetscInt *x, PetscInt *y, PetscInt *z, PetscInt *m, PetscInt *n, PetscInt *p)
```

Example 2 (unknown):
```unknown
DMStagGetCorners()
```

Example 3 (unknown):
```unknown
DMDAGetGhostCorners()
```

---

## DMStagGetGlobalSizes#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagGetGlobalSizes/

**Contents:**
- DMStagGetGlobalSizes#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

get global element counts

dm - the DMSTAG object

M - global element counts in the x direction

N - global element counts in the y direction

P - global element counts in the z direction

Arguments corresponding to higher dimensions are ignored for 1D and 2D grids. These arguments may be set to NULL in this case.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagGetLocalSizes(), DMDAGetInfo()

src/dm/impls/stag/stagutils.c

src/dm/impls/stag/tutorials/ex4.c src/dm/impls/stag/tutorials/ex8.c src/dm/impls/stag/tutorials/ex6.c src/dm/impls/stag/tutorials/ex3.c src/dm/impls/stag/tutorials/ex2.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagGetGlobalSizes(DM dm, PetscInt *M, PetscInt *N, PetscInt *P)
```

Example 2 (unknown):
```unknown
DMStagGetLocalSizes()
```

Example 3 (unknown):
```unknown
DMDAGetInfo()
```

---

## DMStagGetIsFirstRank#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagGetIsFirstRank/

**Contents:**
- DMStagGetIsFirstRank#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

get boolean value for whether this rank is first in each direction in the rank grid

dm - the DMSTAG object

isFirstRank0 - whether this rank is first in the x direction

isFirstRank1 - whether this rank is first in the y direction

isFirstRank2 - whether this rank is first in the z direction

Arguments corresponding to higher dimensions are ignored for 1D and 2D grids. These arguments may be set to NULL in this case.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagGetIsLastRank()

src/dm/impls/stag/stagutils.c

src/dm/impls/stag/tutorials/ex1.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagGetIsFirstRank(DM dm, PetscBool *isFirstRank0, PetscBool *isFirstRank1, PetscBool *isFirstRank2)
```

Example 2 (unknown):
```unknown
DMStagGetIsLastRank()
```

---

## DMStagGetIsLastRank#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagGetIsLastRank/

**Contents:**
- DMStagGetIsLastRank#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

get boolean value for whether this rank is last in each direction in the rank grid

dm - the DMSTAG object

isLastRank0 - whether this rank is last in the x direction

isLastRank1 - whether this rank is last in the y direction

isLastRank2 - whether this rank is last in the z direction

Arguments corresponding to higher dimensions are ignored for 1D and 2D grids. These arguments may be set to NULL in this case.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagGetIsFirstRank()

src/dm/impls/stag/stagutils.c

src/dm/impls/stag/tutorials/ex1.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagGetIsLastRank(DM dm, PetscBool *isLastRank0, PetscBool *isLastRank1, PetscBool *isLastRank2)
```

Example 2 (unknown):
```unknown
DMStagGetIsFirstRank()
```

---

## DMStagGetLocalSizes#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagGetLocalSizes/

**Contents:**
- DMStagGetLocalSizes#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

get local elementwise sizes

dm - the DMSTAG object

m - local element counts (excluding ghosts) in the x direction

n - local element counts (excluding ghosts) in the y direction

p - local element counts (excluding ghosts) in the z direction

Arguments corresponding to higher dimensions are ignored for 1D and 2D grids. These arguments may be set to NULL in this case.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagGetGlobalSizes(), DMStagGetDOF(), DMStagGetNumRanks(), DMDAGetLocalInfo()

src/dm/impls/stag/stagutils.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagGetLocalSizes(DM dm, PetscInt *m, PetscInt *n, PetscInt *p)
```

Example 2 (unknown):
```unknown
DMStagGetGlobalSizes()
```

Example 3 (unknown):
```unknown
DMStagGetDOF()
```

Example 4 (unknown):
```unknown
DMStagGetNumRanks()
```

---

## DMStagGetLocationDOF#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagGetLocationDOF/

**Contents:**
- DMStagGetLocationDOF#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Get number of DOF associated with a given point in a DMSTAG grid

dm - the DMSTAG object

loc - grid point (see DMStagStencilLocation)

dof - the number of DOF (components) living at loc in dm

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagStencilLocation, DMStagStencil, DMDAGetDof()

src/dm/impls/stag/stagstencil.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
PetscErrorCode DMStagGetLocationDOF(DM dm, DMStagStencilLocation loc, PetscInt *dof)
```

Example 2 (unknown):
```unknown
DMStagStencilLocation
```

Example 3 (unknown):
```unknown
DMStagStencilLocation
```

Example 4 (unknown):
```unknown
DMStagStencil
```

---

## DMStagGetLocationSlot#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagGetLocationSlot/

**Contents:**
- DMStagGetLocationSlot#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

get index to use in accessing raw local arrays

dm - the DMSTAG object

loc - location relative to an element

Provides an appropriate index to use with DMStagVecGetArray() and friends. This is required so that the user doesn’t need to know about the ordering of dof associated with each local element.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagVecGetArray(), DMStagVecGetArrayRead(), DMStagGetDOF(), DMStagGetEntriesPerElement()

src/dm/impls/stag/stagutils.c

src/dm/impls/stag/tutorials/ex4.c src/dm/impls/stag/tutorials/ex1.c src/dm/impls/stag/tutorials/ex6.c src/dm/impls/stag/tutorials/ex3.c src/dm/impls/stag/tutorials/ex2.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagGetLocationSlot(DM dm, DMStagStencilLocation loc, PetscInt c, PetscInt *slot)
```

Example 2 (unknown):
```unknown
DMStagVecGetArray()
```

Example 3 (unknown):
```unknown
DMStagVecGetArray()
```

Example 4 (unknown):
```unknown
DMStagVecGetArrayRead()
```

---

## DMStagGetNumRanks#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagGetNumRanks/

**Contents:**
- DMStagGetNumRanks#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

get number of ranks in each direction in the global grid decomposition

dm - the DMSTAG object

nRanks0 - number of ranks in the x direction in the grid decomposition

nRanks1 - number of ranks in the y direction in the grid decomposition

nRanks2 - number of ranks in the z direction in the grid decomposition

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagGetGlobalSizes(), DMStagGetLocalSize(), DMStagSetNumRanks(), DMDAGetInfo()

src/dm/impls/stag/stagutils.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagGetNumRanks(DM dm, PetscInt *nRanks0, PetscInt *nRanks1, PetscInt *nRanks2)
```

Example 2 (unknown):
```unknown
DMStagGetGlobalSizes()
```

Example 3 (unknown):
```unknown
DMStagGetLocalSize()
```

Example 4 (unknown):
```unknown
DMStagSetNumRanks()
```

---

## DMStagGetOwnershipRanges#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagGetOwnershipRanges/

**Contents:**
- DMStagGetOwnershipRanges#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

get elements per rank in each direction

dm - the DMSTAG object

lx - ownership along x direction (optional)

ly - ownership along y direction (optional)

lz - ownership along z direction (optional)

These correspond to the optional final arguments passed to DMStagCreate1d(), DMStagCreate2d(), and DMStagCreate3d().

Arguments corresponding to higher dimensions are ignored for 1D and 2D grids. These arguments may be set to NULL in this case.

In C you should not free these arrays, nor change the values in them. They will only have valid values while the DMSTAG they came from still exists (has not been destroyed).

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagSetGlobalSizes(), DMStagSetOwnershipRanges(), DMStagCreate1d(), DMStagCreate2d(), DMStagCreate3d(), DMDAGetOwnershipRanges()

src/dm/impls/stag/stagutils.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagGetOwnershipRanges(DM dm, const PetscInt *lx[], const PetscInt *ly[], const PetscInt *lz[])
```

Example 2 (unknown):
```unknown
DMStagCreate1d()
```

Example 3 (unknown):
```unknown
DMStagCreate2d()
```

Example 4 (unknown):
```unknown
DMStagCreate3d()
```

---

## DMStagGetProductCoordinateArraysRead#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagGetProductCoordinateArraysRead/

**Contents:**
- DMStagGetProductCoordinateArraysRead#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

extract product coordinate arrays, read-only

dm - the DMSTAG object

arrX - local 1D coordinate arrays for x direction

arrY - local 1D coordinate arrays for y direction, not set for one dimensional problems

arrZ - local 1D coordinate arrays for z direction, not set for one and two dimensional problems

See DMStagGetProductCoordinateArrays() for more information.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMPRODUCT, DMStagGetProductCoordinateArrays(), DMStagSetUniformCoordinates(), DMStagSetUniformCoordinatesProduct(), DMStagGetProductCoordinateLocationSlot()

src/dm/impls/stag/stagutils.c

src/dm/impls/stag/tutorials/ex2.c src/dm/impls/stag/tutorials/ex4.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagGetProductCoordinateArraysRead(DM dm, void *arrX, void *arrY, void *arrZ)
```

Example 2 (unknown):
```unknown
DMStagGetProductCoordinateArrays()
```

Example 3 (unknown):
```unknown
DMStagGetProductCoordinateArrays()
```

Example 4 (unknown):
```unknown
DMStagSetUniformCoordinates()
```

---

## DMStagGetProductCoordinateArrays#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagGetProductCoordinateArrays/

**Contents:**
- DMStagGetProductCoordinateArrays#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

extract local product coordinate arrays, one per dimension

dm - the DMSTAG object

arrX - local 1D coordinate arrays for x direction

arrY - local 1D coordinate arrays for y direction, not set for one dimensional problems

arrZ - local 1D coordinate arrays for z direction, not set for one and two dimensional problems

A high-level helper function to quickly extract local coordinate arrays.

Note that 2-dimensional arrays are returned. See DMStagVecGetArray(), which is called internally to produce these arrays representing coordinates on elements and vertices (element boundaries) for a 1-dimensional DMSTAG in each coordinate direction.

One should use DMStagGetProductCoordinateLocationSlot() to determine appropriate indices for the second dimension in these returned arrays. This function checks that the coordinate array is a suitable product of 1-dimensional DMSTAG objects.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMPRODUCT, DMStagGetProductCoordinateArraysRead(), DMStagSetUniformCoordinates(), DMStagSetUniformCoordinatesProduct(), DMStagGetProductCoordinateLocationSlot()

src/dm/impls/stag/stagutils.c

src/dm/impls/stag/tutorials/ex6.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagGetProductCoordinateArrays(DM dm, void *arrX, void *arrY, void *arrZ)
```

Example 2 (unknown):
```unknown
DMStagVecGetArray()
```

Example 3 (unknown):
```unknown
DMStagGetProductCoordinateLocationSlot()
```

Example 4 (unknown):
```unknown
DMStagGetProductCoordinateArraysRead()
```

---

## DMStagGetProductCoordinateLocationSlot#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagGetProductCoordinateLocationSlot/

**Contents:**
- DMStagGetProductCoordinateLocationSlot#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

get slot for use with local product coordinate arrays

dm - the DMSTAG object

loc - the grid location

slot - the index to use in local arrays

High-level helper function to get slot indices for 1D coordinate DMs, for use with DMStagGetProductCoordinateArrays() and related functions.

For loc, one should use DMSTAG_LEFT, DMSTAG_ELEMENT, or DMSTAG_RIGHT for “previous”, “center” and “next” locations, respectively, in each dimension. One can equivalently use DMSTAG_DOWN or DMSTAG_BACK in place of DMSTAG_LEFT, and DMSTAG_UP or DMSTACK_FRONT in place of DMSTAG_RIGHT;

This function checks that the coordinates are actually set up so that using the slots from any of the 1D coordinate sub-DMs are valid for all the 1D coordinate sub-DMs.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMPRODUCT, DMStagGetProductCoordinateArrays(), DMStagGetProductCoordinateArraysRead(), DMStagSetUniformCoordinates()

src/dm/impls/stag/stagutils.c

src/dm/impls/stag/tutorials/ex2.c src/dm/impls/stag/tutorials/ex4.c src/dm/impls/stag/tutorials/ex6.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PETSC_EXTERN PetscErrorCode DMStagGetProductCoordinateLocationSlot(DM dm, DMStagStencilLocation loc, PetscInt *slot)
```

Example 2 (unknown):
```unknown
DMStagGetProductCoordinateArrays()
```

Example 3 (unknown):
```unknown
DMSTAG_LEFT
```

Example 4 (unknown):
```unknown
DMSTAG_ELEMENT
```

---

## DMStagGetRefinementFactor#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagGetRefinementFactor/

**Contents:**
- DMStagGetRefinementFactor#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

get refinement ratios in each direction

dm - the DMSTAG object

refine_x - ratio of fine grid to coarse in x-direction (2 by default)

refine_y - ratio of fine grid to coarse in y-direction (2 by default)

refine_z - ratio of fine grid to coarse in z-direction (2 by default)

DMSTAG: Staggered, Structured Grid, DMSTAG, DMRefine(), DMCoarsen(), DMStagSetRefinementFactor(), DMDASetRefinementFactor()

src/dm/impls/stag/stagutils.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagGetRefinementFactor(DM dm, PetscInt *refine_x, PetscInt *refine_y, PetscInt *refine_z)
```

Example 2 (unknown):
```unknown
DMCoarsen()
```

Example 3 (unknown):
```unknown
DMStagSetRefinementFactor()
```

Example 4 (unknown):
```unknown
DMDASetRefinementFactor()
```

---

## DMStagGetStencilType#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagGetStencilType/

**Contents:**
- DMStagGetStencilType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

get elementwise ghost/halo stencil type

dm - the DMSTAG object

stencilType - the elementwise ghost stencil type: DMSTAG_STENCIL_BOX, DMSTAG_STENCIL_STAR, or DMSTAG_STENCIL_NONE

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagSetStencilType(), DMStagGetStencilWidth, DMStagStencilType

src/dm/impls/stag/stagutils.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagGetStencilType(DM dm, DMStagStencilType *stencilType)
```

Example 2 (unknown):
```unknown
DMSTAG_STENCIL_BOX
```

Example 3 (unknown):
```unknown
DMSTAG_STENCIL_STAR
```

Example 4 (unknown):
```unknown
DMSTAG_STENCIL_NONE
```

---

## DMStagGetStencilWidth#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagGetStencilWidth/

**Contents:**
- DMStagGetStencilWidth#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

get elementwise stencil width

dm - the DMSTAG object

stencilWidth - stencil/halo/ghost width in elements

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagSetStencilWidth(), DMStagGetStencilType(), DMDAGetStencilType()

src/dm/impls/stag/stagutils.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagGetStencilWidth(DM dm, PetscInt *stencilWidth)
```

Example 2 (unknown):
```unknown
DMStagSetStencilWidth()
```

Example 3 (unknown):
```unknown
DMStagGetStencilType()
```

Example 4 (unknown):
```unknown
DMDAGetStencilType()
```

---

## DMStagMatGetValuesStencil#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagMatGetValuesStencil/

**Contents:**
- DMStagMatGetValuesStencil#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

retrieve local matrix entries using grid indexing

dm - the DMSTAG object

nRow - number of rows

posRow - grid locations (including components) of rows

nCol - number of columns

posCol - grid locations (including components) of columns

val - logically two-dimensional array of values

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagStencil, DMStagStencilLocation, DMStagVecGetValuesStencil(), DMStagVecSetValuesStencil(), DMStagMatSetValuesStencil(), MatSetValuesStencil(), MatAssemblyBegin(), MatAssemblyEnd(), DMCreateMatrix()

src/dm/impls/stag/stagstencil.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
PetscErrorCode DMStagMatGetValuesStencil(DM dm, Mat mat, PetscInt nRow, const DMStagStencil *posRow, PetscInt nCol, const DMStagStencil *posCol, PetscScalar *val)
```

Example 2 (unknown):
```unknown
DMStagStencil
```

Example 3 (unknown):
```unknown
DMStagStencilLocation
```

Example 4 (unknown):
```unknown
DMStagVecGetValuesStencil()
```

---

## DMStagMatSetValuesStencil#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagMatSetValuesStencil/

**Contents:**
- DMStagMatSetValuesStencil#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

insert or add matrix entries using grid indexing

dm - the DMSTAG object

nRow - number of rows

posRow - grid locations (including components) of rows

nCol - number of columns

posCol - grid locations (including components) of columns

val - logically two-dimensional array of values

insertMode - INSERT_VALUES or ADD_VALUES

See notes for MatSetValuesStencil()

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagStencil, DMStagStencilLocation, DMStagVecGetValuesStencil(), DMStagVecSetValuesStencil(), DMStagMatGetValuesStencil(), MatSetValuesStencil(), MatAssemblyBegin(), MatAssemblyEnd(), DMCreateMatrix()

src/dm/impls/stag/stagstencil.c

src/dm/impls/stag/tutorials/ex4.c src/dm/impls/stag/tutorials/ex1.c src/dm/impls/stag/tutorials/ex8.c src/dm/impls/stag/tutorials/ex3.c src/dm/impls/stag/tutorials/ex2.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
PetscErrorCode DMStagMatSetValuesStencil(DM dm, Mat mat, PetscInt nRow, const DMStagStencil *posRow, PetscInt nCol, const DMStagStencil *posCol, const PetscScalar *val, InsertMode insertMode)
```

Example 2 (unknown):
```unknown
INSERT_VALUES
```

Example 3 (unknown):
```unknown
MatSetValuesStencil()
```

Example 4 (unknown):
```unknown
DMStagStencil
```

---

## DMStagMigrateVec#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagMigrateVec/

**Contents:**
- DMStagMigrateVec#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

transfer a vector associated with a DMSTAG to a vector associated with a compatible DMSTAG

dm - the source DMSTAG object

vec - the source vector, compatible with dm

dmTo - the compatible destination DMSTAG object

vecTo - the destination vector, compatible with dmTo

Extra dof are ignored, and unfilled dof are zeroed. Currently only implemented to migrate global vectors to global vectors. For the definition of compatibility of DMs, see DMGetCompatibility().

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagCreateCompatibleDMStag(), DMGetCompatibility(), DMStagVecSplitToDMDA()

src/dm/impls/stag/stagutils.c

src/dm/impls/stag/tutorials/ex1.c src/dm/impls/stag/tutorials/ex2.c src/dm/impls/stag/tutorials/ex4.c src/dm/impls/stag/tutorials/ex3.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagMigrateVec(DM dm, Vec vec, DM dmTo, Vec vecTo)
```

Example 2 (unknown):
```unknown
DMGetCompatibility()
```

Example 3 (unknown):
```unknown
DMStagCreateCompatibleDMStag()
```

Example 4 (unknown):
```unknown
DMGetCompatibility()
```

---

## DMStagPopulateLocalToGlobalInjective#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagPopulateLocalToGlobalInjective/

**Contents:**
- DMStagPopulateLocalToGlobalInjective#
- Synopsis#
- Input Parameter#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#
- Implementations#

populate an internal 1-to-1 local-to-global map

Creates an internal object which explicitly maps a single local degree of freedom to each global degree of freedom. This is used, if populated, instead of SCATTER_REVERSE_LOCAL with the (1-to-many, in general) global-to-local map, when DMLocalToGlobal() is called with INSERT_VALUES. This allows usage, for example, even in the periodic, 1-rank case, where the inverse of the global-to-local map, even when restricted to on-rank communication, is non-injective. This is at the cost of storing an additional VecScatter object inside each DMSTAG object.

dm - the DMSTAG object

In normal usage, library users shouldn’t be concerned with this function, as it is called during DMSetUp(), when required.

Returns immediately if the internal map is already populated.

This could, if desired, be moved up to a general DM routine. It would allow, for example, DMDA to support DMLocalToGlobal() with INSERT_VALUES, even in the single-rank periodic case.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMLocalToGlobal(), VecScatter

src/dm/impls/stag/stagutils.c

DMStagPopulateLocalToGlobalInjective_1d() in src/dm/impls/stag/stag1d.c DMStagPopulateLocalToGlobalInjective_2d() in src/dm/impls/stag/stag2d.c DMStagPopulateLocalToGlobalInjective_3d() in src/dm/impls/stag/stag3d.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagPopulateLocalToGlobalInjective(DM dm)
```

Example 2 (unknown):
```unknown
DMLocalToGlobal()
```

Example 3 (unknown):
```unknown
INSERT_VALUES
```

Example 4 (unknown):
```unknown
DMLocalToGlobal()
```

---

## DMStagRestoreProductCoordinateArraysRead#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagRestoreProductCoordinateArraysRead/

**Contents:**
- DMStagRestoreProductCoordinateArraysRead#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

restore local product array access, read-only

dm - the DMSTAG object

arrX - local 1D coordinate arrays for x direction

arrY - local 1D coordinate arrays for y direction

arrZ - local 1D coordinate arrays for z direction

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagGetProductCoordinateArrays(), DMStagGetProductCoordinateArraysRead()

src/dm/impls/stag/stagutils.c

src/dm/impls/stag/tutorials/ex2.c src/dm/impls/stag/tutorials/ex4.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagRestoreProductCoordinateArraysRead(DM dm, void *arrX, void *arrY, void *arrZ)
```

Example 2 (unknown):
```unknown
DMStagGetProductCoordinateArrays()
```

Example 3 (unknown):
```unknown
DMStagGetProductCoordinateArraysRead()
```

---

## DMStagRestoreProductCoordinateArrays#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagRestoreProductCoordinateArrays/

**Contents:**
- DMStagRestoreProductCoordinateArrays#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

restore local array access

dm - the DMSTAG object

arrX - local 1D coordinate arrays for x direction

arrY - local 1D coordinate arrays for y direction

arrZ - local 1D coordinate arrays for z direction

This function does not automatically perform a local->global scatter to populate global coordinates from the local coordinates. Thus, it may be required to explicitly perform these operations in some situations, as in the following partial example:

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagGetProductCoordinateArrays(), DMStagGetProductCoordinateArraysRead()

src/dm/impls/stag/stagutils.c

src/dm/impls/stag/tutorials/ex6.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagRestoreProductCoordinateArrays(DM dm, void *arrX, void *arrY, void *arrZ)
```

Example 2 (sass):
```sass
PetscCall(DMGetCoordinateDM(dm, &cdm));
  for (PetscInt d = 0; d < 3; ++d) {
    DM  subdm;
    Vec coor, coor_local;

    PetscCall(DMProductGetDM(cdm, d, &subdm));
    PetscCall(DMGetCoordinates(subdm, &coor));
    PetscCall(DMGetCoordinatesLocal(subdm, &coor_local));
    PetscCall(DMLocalToGlobal(subdm, coor_local, INSERT_VALUES, coor));
    PetscCall(PetscPrintf(PETSC_COMM_WORLD, "Coordinates dim %" PetscInt_FMT ":\n", d));
    PetscCall(VecView(coor, PETSC_VIEWER_STDOUT_WORLD));
  }
```

Example 3 (unknown):
```unknown
DMStagGetProductCoordinateArrays()
```

Example 4 (unknown):
```unknown
DMStagGetProductCoordinateArraysRead()
```

---

## DMStagRestrictSimple#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagRestrictSimple/

**Contents:**
- DMStagRestrictSimple#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

restricts data from a fine to a coarse DMSTAG, in the simplest way

Values on coarse cells are averages of all fine cells that they cover. Thus, values on vertices are injected, values on edges are averages of the underlying two fine edges, and values on elements in d dimensions are averages of \(2^d\) underlying elements.

xc - data on coarse DM

DMSTAG: Staggered, Structured Grid, DMSTAG, DM, DMRestrict(), DMCoarsen(), DMCreateInjection()

src/dm/impls/stag/stagmulti.c

DMStagRestrictSimple_1d() in src/dm/impls/stag/stag1d.c DMStagRestrictSimple_2d() in src/dm/impls/stag/stag2d.c DMStagRestrictSimple_3d() in src/dm/impls/stag/stag3d.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
PetscErrorCode DMStagRestrictSimple(DM dmf, Vec xf, DM dmc, Vec xc)
```

Example 2 (unknown):
```unknown
DMRestrict()
```

Example 3 (unknown):
```unknown
DMCoarsen()
```

Example 4 (unknown):
```unknown
DMCreateInjection()
```

---

## DMStagSetBoundaryTypes#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagSetBoundaryTypes/

**Contents:**
- DMStagSetBoundaryTypes#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

set DMSTAG boundary types

Logically Collective; boundaryType0, boundaryType1, and boundaryType2 must contain common values

dm - the DMSTAG object

boundaryType2 - boundary type for x direction

boundaryType1 - boundary type for y direction, not set for one dimensional problems

boundaryType0 - boundary type for z direction, not set for one and two dimensional problems

Arguments corresponding to higher dimensions are ignored for 1D and 2D grids.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMBoundaryType, DMStagCreate1d(), DMStagCreate2d(), DMStagCreate3d(), DMDASetBoundaryType()

src/dm/impls/stag/stagutils.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagSetBoundaryTypes(DM dm, DMBoundaryType boundaryType0, DMBoundaryType boundaryType1, DMBoundaryType boundaryType2)
```

Example 2 (unknown):
```unknown
DMBoundaryType
```

Example 3 (unknown):
```unknown
DMStagCreate1d()
```

Example 4 (unknown):
```unknown
DMStagCreate2d()
```

---

## DMStagSetCoordinateDMType#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagSetCoordinateDMType/

**Contents:**
- DMStagSetCoordinateDMType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

set DM type to store coordinates

Logically Collective; dmtype must contain common value

dm - the DMSTAG object

dmtype - DMtype for coordinates, either DMSTAG or DMPRODUCT

DMSTAG: Staggered, Structured Grid, DMSTAG, DMPRODUCT, DMGetCoordinateDM(), DMStagSetUniformCoordinates(), DMStagSetUniformCoordinatesExplicit(), DMStagSetUniformCoordinatesProduct(), DMType

src/dm/impls/stag/stagutils.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagSetCoordinateDMType(DM dm, DMType dmtype)
```

Example 2 (unknown):
```unknown
DMGetCoordinateDM()
```

Example 3 (unknown):
```unknown
DMStagSetUniformCoordinates()
```

Example 4 (unknown):
```unknown
DMStagSetUniformCoordinatesExplicit()
```

---

## DMStagSetDOF#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagSetDOF/

**Contents:**
- DMStagSetDOF#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Logically Collective; dof0, dof1, dof2, and dof3 must contain common values

dm - the DMSTAG object

dof0 - the number of points per 0-cell (vertex/node)

dof1 - the number of points per 1-cell (element in 1D, edge in 2D and 3D)

dof2 - the number of points per 2-cell (element in 2D, face in 3D)

dof3 - the number of points per 3-cell (element in 3D)

Arguments corresponding to higher dimensions are ignored for 1D and 2D grids.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMDASetDof()

src/dm/impls/stag/stagutils.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagSetDOF(DM dm, PetscInt dof0, PetscInt dof1, PetscInt dof2, PetscInt dof3)
```

Example 2 (unknown):
```unknown
DMDASetDof()
```

---

## DMStagSetGlobalSizes#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagSetGlobalSizes/

**Contents:**
- DMStagSetGlobalSizes#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

set global element counts in each direction

Logically Collective; N0, N1, and N2 must contain common values

dm - the DMSTAG object

N0 - global elementwise size in the x direction

N1 - global elementwise size in the y direction

N2 - global elementwise size in the z direction

Arguments corresponding to higher dimensions are ignored for 1D and 2D grids.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagGetGlobalSizes(), DMDASetSizes()

src/dm/impls/stag/stagutils.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagSetGlobalSizes(DM dm, PetscInt N0, PetscInt N1, PetscInt N2)
```

Example 2 (unknown):
```unknown
DMStagGetGlobalSizes()
```

Example 3 (unknown):
```unknown
DMDASetSizes()
```

---

## DMStagSetNumRanks#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagSetNumRanks/

**Contents:**
- DMStagSetNumRanks#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

set ranks in each direction in the global rank grid

Logically Collective; nRanks0, nRanks1, and nRanks2 must contain common values

dm - the DMSTAG object

nRanks0 - number of ranks in the x direction

nRanks1 - number of ranks in the y direction

nRanks2 - number of ranks in the z direction

Arguments corresponding to higher dimensions are ignored for 1D and 2D grids.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMDASetNumProcs()

src/dm/impls/stag/stagutils.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagSetNumRanks(DM dm, PetscInt nRanks0, PetscInt nRanks1, PetscInt nRanks2)
```

Example 2 (unknown):
```unknown
DMDASetNumProcs()
```

---

## DMStagSetOwnershipRanges#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagSetOwnershipRanges/

**Contents:**
- DMStagSetOwnershipRanges#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

set elements per rank in each direction

Logically Collective; lx, ly, and lz must contain common values

dm - the DMSTAG object

lx - element counts for each rank in the x direction, may be NULL

ly - element counts for each rank in the y direction, may be NULL

lz - element counts for each rank in the z direction, may be NULL

Arguments corresponding to higher dimensions are ignored for 1D and 2D grids. These arguments may be set to NULL in this case.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagSetGlobalSizes(), DMStagGetOwnershipRanges(), DMDASetOwnershipRanges()

src/dm/impls/stag/stagutils.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagSetOwnershipRanges(DM dm, const PetscInt lx[], const PetscInt ly[], const PetscInt lz[])
```

Example 2 (unknown):
```unknown
DMStagSetGlobalSizes()
```

Example 3 (unknown):
```unknown
DMStagGetOwnershipRanges()
```

Example 4 (unknown):
```unknown
DMDASetOwnershipRanges()
```

---

## DMStagSetRefinementFactor#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagSetRefinementFactor/

**Contents:**
- DMStagSetRefinementFactor#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

set refinement ratios in each direction

dm - the DMSTAG object

refine_x - ratio of fine grid to coarse in x-direction (2 by default)

refine_y - ratio of fine grid to coarse in y-direction (2 by default)

refine_z - ratio of fine grid to coarse in z-direction (2 by default)

Pass PETSC_IGNORE to leave a value unchanged

DMSTAG: Staggered, Structured Grid, DMSTAG, DMRefine(), DMCoarsen(), DMStagGetRefinementFactor(), DMDAGetRefinementFactor()

src/dm/impls/stag/stagutils.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagSetRefinementFactor(DM dm, PetscInt refine_x, PetscInt refine_y, PetscInt refine_z)
```

Example 2 (unknown):
```unknown
PETSC_IGNORE
```

Example 3 (unknown):
```unknown
DMCoarsen()
```

Example 4 (unknown):
```unknown
DMStagGetRefinementFactor()
```

---

## DMStagSetStencilType#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagSetStencilType/

**Contents:**
- DMStagSetStencilType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

set elementwise ghost/halo stencil type

Logically Collective; stencilType must contain common value

dm - the DMSTAG object

stencilType - the elementwise ghost stencil type: DMSTAG_STENCIL_BOX, DMSTAG_STENCIL_STAR, or DMSTAG_STENCIL_NONE

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagGetStencilType(), DMStagSetStencilWidth(), DMStagStencilType

src/dm/impls/stag/stagutils.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagSetStencilType(DM dm, DMStagStencilType stencilType)
```

Example 2 (unknown):
```unknown
stencilType
```

Example 3 (unknown):
```unknown
DMSTAG_STENCIL_BOX
```

Example 4 (unknown):
```unknown
DMSTAG_STENCIL_STAR
```

---

## DMStagSetStencilWidth#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagSetStencilWidth/

**Contents:**
- DMStagSetStencilWidth#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

set elementwise stencil width

Logically Collective; stencilWidth must contain common value

dm - the DMSTAG object

stencilWidth - stencil/halo/ghost width in elements

The width value is not used when DMSTAG_STENCIL_NONE is specified.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagGetStencilWidth(), DMStagGetStencilType(), DMStagStencilType

src/dm/impls/stag/stagutils.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagSetStencilWidth(DM dm, PetscInt stencilWidth)
```

Example 2 (unknown):
```unknown
stencilWidth
```

Example 3 (unknown):
```unknown
DMSTAG_STENCIL_NONE
```

Example 4 (unknown):
```unknown
DMStagGetStencilWidth()
```

---

## DMStagSetUniformCoordinatesExplicit#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagSetUniformCoordinatesExplicit/

**Contents:**
- DMStagSetUniformCoordinatesExplicit#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

set DMSTAG coordinates to be a uniform grid, storing all values

dm - the DMSTAG object

xmin - minimum global coordinate value in the x direction

xmax - maximum global coordinate value in the x direction

ymin - minimum global coordinate value in the y direction

ymax - maximum global coordinate value in the y direction

zmin - minimum global coordinate value in the z direction

zmax - maximum global coordinate value in the z direction

DMSTAG supports 2 different types of coordinate DM: either another DMSTAG, or a DMPRODUCT. If the grid is orthogonal, using DMPRODUCT should be more efficient.

Arguments corresponding to higher dimensions are ignored for 1D and 2D grids.

See the manual page for DMStagSetUniformCoordinates() for information on how coordinates for dummy cells outside the physical domain boundary are populated.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagSetUniformCoordinates(), DMStagSetUniformCoordinatesProduct(), DMStagSetCoordinateDMType()

src/dm/impls/stag/stagutils.c

src/dm/impls/stag/tutorials/ex1.c src/dm/impls/stag/tutorials/ex3.c

DMStagSetUniformCoordinatesExplicit_1d() in src/dm/impls/stag/stag1d.c DMStagSetUniformCoordinatesExplicit_2d() in src/dm/impls/stag/stag2d.c DMStagSetUniformCoordinatesExplicit_3d() in src/dm/impls/stag/stag3d.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagSetUniformCoordinatesExplicit(DM dm, PetscReal xmin, PetscReal xmax, PetscReal ymin, PetscReal ymax, PetscReal zmin, PetscReal zmax)
```

Example 2 (unknown):
```unknown
DMStagSetUniformCoordinates()
```

Example 3 (unknown):
```unknown
DMStagSetUniformCoordinates()
```

Example 4 (unknown):
```unknown
DMStagSetUniformCoordinatesProduct()
```

---

## DMStagSetUniformCoordinatesProduct#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagSetUniformCoordinatesProduct/

**Contents:**
- DMStagSetUniformCoordinatesProduct#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

create uniform coordinates, as a product of 1D arrays

Set the coordinate DM to be a DMPRODUCT of 1D DMSTAG objects, each of which have a coordinate DM (also a 1d DMSTAG) holding uniform coordinates.

dm - the DMSTAG object

xmin - minimum global coordinate value in the x direction

xmax - maximum global coordinate value in the x direction

ymin - minimum global coordinate value in the y direction

ymax - maximum global coordinate value in the y direction

zmin - minimum global coordinate value in the z direction

zmax - maximum global coordinate value in the z direction

Arguments corresponding to higher dimensions are ignored for 1D and 2D grids.

The per-dimension 1-dimensional DMSTAG objects that comprise the product always have active 0-cells (vertices, element boundaries) and 1-cells (element centers).

See the manual page for DMStagSetUniformCoordinates() for information on how coordinates for dummy cells outside the physical domain boundary are populated.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMPRODUCT, DMStagSetUniformCoordinates(), DMStagSetUniformCoordinatesExplicit(), DMStagSetCoordinateDMType()

src/dm/impls/stag/stagutils.c

src/dm/impls/stag/tutorials/ex2.c src/dm/impls/stag/tutorials/ex4.c src/dm/impls/stag/tutorials/ex6.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagSetUniformCoordinatesProduct(DM dm, PetscReal xmin, PetscReal xmax, PetscReal ymin, PetscReal ymax, PetscReal zmin, PetscReal zmax)
```

Example 2 (unknown):
```unknown
DMStagSetUniformCoordinates()
```

Example 3 (unknown):
```unknown
DMStagSetUniformCoordinates()
```

Example 4 (unknown):
```unknown
DMStagSetUniformCoordinatesExplicit()
```

---

## DMStagSetUniformCoordinates#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagSetUniformCoordinates/

**Contents:**
- DMStagSetUniformCoordinates#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

set DMSTAG coordinates to be a uniform grid

dm - the DMSTAG object

xmin - minimum global coordinate value in the x direction

xmax - maximum global coordinate values in the x direction

ymin - minimum global coordinate value in the y direction

ymax - maximum global coordinate value in the y direction

zmin - minimum global coordinate value in the z direction

zmax - maximum global coordinate value in the z direction

DMSTAG supports 2 different types of coordinate DM: DMSTAG and DMPRODUCT. Arguments corresponding to higher dimensions are ignored for 1D and 2D grids.

Local coordinates are populated (using DMSetCoordinatesLocal()), linearly extrapolated to ghost cells, including those outside the physical domain. This is also done in case of periodic boundaries, meaning that the same global point may have different coordinates in different local representations, which are equivalent assuming a periodicity implied by the arguments to this function, i.e. two points are equivalent if their difference is a multiple of \((\)xmax \(-\) xmin \()\) in the x direction, \((\) ymax \(-\) ymin \()\) in the y direction, and \((\) zmax \(-\) zmin \()\) in the z direction.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMPRODUCT, DMStagSetUniformCoordinatesExplicit(), DMStagSetUniformCoordinatesProduct(), DMStagSetCoordinateDMType(), DMGetCoordinateDM(), DMGetCoordinates(), DMDASetUniformCoordinates(), DMBoundaryType

src/dm/impls/stag/stagutils.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagSetUniformCoordinates(DM dm, PetscReal xmin, PetscReal xmax, PetscReal ymin, PetscReal ymax, PetscReal zmin, PetscReal zmax)
```

Example 2 (unknown):
```unknown
DMSetCoordinatesLocal()
```

Example 3 (unknown):
```unknown
DMStagSetUniformCoordinatesExplicit()
```

Example 4 (unknown):
```unknown
DMStagSetUniformCoordinatesProduct()
```

---

## DMStagStencilLocation#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagStencilLocation/

**Contents:**
- DMStagStencilLocation#
- Synopsis#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#
- Examples#
- Examples#
- Examples#

enumerated type denoting a location relative to an element in a DMSTAG grid

The interpretation of these values is dimension-dependent.

The order of the enum entries is significant, as it corresponds to the canonical numbering of DOFs, and the fact that the numbering starts at 0 may also be used by the implementation.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMDA, DMStagStencil, DMStagGetLocationSlot(), DMStagStencilType

include/petscdmstag.h

src/dm/impls/stag/tutorials/ex1.c src/dm/impls/stag/tutorials/ex2.c src/dm/impls/stag/tutorials/ex3.c

src/dm/impls/stag/tutorials/ex6.c

src/dm/impls/stag/tutorials/ex6.c

src/dm/impls/stag/tutorials/ex6.c

src/dm/impls/stag/tutorials/ex6.c

src/dm/impls/stag/tutorials/ex4.c src/dm/impls/stag/tutorials/ex6.c

src/dm/impls/stag/tutorials/ex4.c src/dm/impls/stag/tutorials/ex6.c

src/dm/impls/stag/tutorials/ex4.c src/dm/impls/stag/tutorials/ex6.c

src/dm/impls/stag/tutorials/ex6.c

src/dm/impls/stag/tutorials/ex4.c src/dm/impls/stag/tutorials/ex6.c

src/dm/impls/stag/tutorials/ex6.c

src/dm/impls/stag/tutorials/ex6.c

src/dm/impls/stag/tutorials/ex6.c

src/dm/impls/stag/tutorials/ex6.c

src/dm/impls/stag/tutorials/ex6.c

src/dm/impls/stag/tutorials/ex4.c src/dm/impls/stag/tutorials/ex6.c

src/dm/impls/stag/tutorials/ex6.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  DMSTAG_NULL_LOCATION,
  DMSTAG_BACK_DOWN_LEFT,
  DMSTAG_BACK_DOWN,
  DMSTAG_BACK_DOWN_RIGHT,
  DMSTAG_BACK_LEFT,
  DMSTAG_BACK,
  DMSTAG_BACK_RIGHT,
  DMSTAG_BACK_UP_LEFT,
  DMSTAG_BACK_UP,
  DMSTAG_BACK_UP_RIGHT,
  DMSTAG_DOWN_LEFT,
  DMSTAG_DOWN,
  DMSTAG_DOWN_RIGHT,
  DMSTAG_LEFT,
  DMSTAG_ELEMENT,
  DMSTAG_RIGHT,
  DMSTAG_UP_LEFT,
  DMSTAG_UP,
  DMSTAG_UP_RIGHT,
  DMSTAG_FRONT_DOWN_LEFT,
  DMSTAG_FRONT_DOWN,
  DMSTAG_FRONT_DOWN_RIGHT,
  DMSTAG_FRONT_LEFT,
  DMSTAG_FRONT,
  DMSTAG_FRONT_RIGHT,
  DMSTAG_FRONT_UP_LEFT,
  DMSTAG_FRONT_UP,
  DMSTAG_FRONT_UP_RIGHT
} DMStagStencilLocation;
```

Example 2 (unknown):
```unknown
DMStagStencil
```

Example 3 (unknown):
```unknown
DMStagGetLocationSlot()
```

Example 4 (unknown):
```unknown
DMStagStencilType
```

---

## DMStagStencilToIndexLocal#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagStencilToIndexLocal/

**Contents:**
- DMStagStencilToIndexLocal#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#

Convert an array of DMStagStencil objects to an array of indices into a local vector.

dm - the DMSTAG object

dim - the dimension of the DMSTAG object

n - the number of DMStagStencil objects

pos - an array of n DMStagStencil objects

ix - output array of n indices

The DMStagStencil objects in pos use global element indices.

The .c fields in pos must always be set (even if to 0).

This is a “hot” function, and accepts the dimension redundantly to avoid having to perform any error checking inside the function.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagStencilLocation, DMStagStencil, DMGetLocalVector, DMCreateLocalVector

src/dm/impls/stag/stagstencil.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMStagStenci
```

Example 2 (unknown):
```unknown
#include "petscdmstag.h"   
PetscErrorCode DMStagStencilToIndexLocal(DM dm, PetscInt dim, PetscInt n, const DMStagStencil *pos, PetscInt *ix)
```

Example 3 (unknown):
```unknown
DMStagStencil
```

Example 4 (unknown):
```unknown
DMStagStencil
```

---

## DMStagStencilType#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagStencilType/

**Contents:**
- DMStagStencilType#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#

Elementwise stencil type, determining which neighbors participate in communication

DMSTAG: Staggered, Structured Grid, DMSTAG, DMDA, DMStagCreate1d(), DMStagCreate2d(), DMStagCreate3d(), DMStagStencil, DMDAStencilType, DMStagStencilLocation

include/petscdmstag.h

src/dm/impls/stag/tutorials/ex4.c src/dm/impls/stag/tutorials/ex1.c src/dm/impls/stag/tutorials/ex8.c src/dm/impls/stag/tutorials/ex6.c src/dm/impls/stag/tutorials/ex3.c src/dm/impls/stag/tutorials/ex2.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  DMSTAG_STENCIL_NONE,
  DMSTAG_STENCIL_STAR,
  DMSTAG_STENCIL_BOX
} DMStagStencilType;
```

Example 2 (unknown):
```unknown
DMStagCreate1d()
```

Example 3 (unknown):
```unknown
DMStagCreate2d()
```

Example 4 (unknown):
```unknown
DMStagCreate3d()
```

---

## DMStagStencil#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagStencil/

**Contents:**
- DMStagStencil#
- Synopsis#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

data structure representing a degree of freedom on a DMSTAG grid

Data structure (C struct), analogous to describing a degree of freedom associated with a DMSTAG object, in terms of a global element index in each of up to three directions, a “location” as defined by DMStagStencilLocation, and a component number. Primarily for use with DMStagMatSetValuesStencil() (compare with use of MatStencil with MatSetValuesStencil()).

The component (c) field must always be set, even if there is a single component at a given location (in which case c should be set to 0).

This is a struct, not a PetscObject.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMDA, DMStagMatSetValuesStencil(), DMStagVecSetValuesStencil(), DMStagStencilLocation, DMStagSetStencilWidth(), DMStagSetStencilType(), DMStagVecGetValuesStencil()

include/petscdmstag.h

src/dm/impls/stag/tutorials/ex4.c src/dm/impls/stag/tutorials/ex1.c src/dm/impls/stag/tutorials/ex8.c src/dm/impls/stag/tutorials/ex6.c src/dm/impls/stag/tutorials/ex3.c src/dm/impls/stag/tutorials/ex2.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef struct {
  DMStagStencilLocation loc;
  PetscInt              i, j, k, c;
} DMStagStencil;
```

Example 2 (unknown):
```unknown
DMStagStencilLocation
```

Example 3 (unknown):
```unknown
DMStagMatSetValuesStencil()
```

Example 4 (unknown):
```unknown
MatSetValuesStencil()
```

---

## DMStagVecGetArrayRead#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagVecGetArrayRead/

**Contents:**
- DMStagVecGetArrayRead#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

get read-only access to a local array

See the man page for DMStagVecGetArray() for more information.

dm - the DMSTAG object

array - the read-only array

DMStagVecRestoreArrayRead() must be called, once finished with the array

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagGetLocationSlot(), DMGetLocalVector(), DMCreateLocalVector(), DMGetGlobalVector(), DMCreateGlobalVector(), DMDAVecGetArrayRead(), DMDAVecGetArrayDOFRead()

src/dm/impls/stag/stagutils.c

src/dm/impls/stag/tutorials/ex1.c src/dm/impls/stag/tutorials/ex3.c src/dm/impls/stag/tutorials/ex6.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagVecGetArrayRead(DM dm, Vec vec, void *array)
```

Example 2 (unknown):
```unknown
DMStagVecGetArray()
```

Example 3 (unknown):
```unknown
DMStagVecRestoreArrayRead()
```

Example 4 (unknown):
```unknown
DMStagGetLocationSlot()
```

---

## DMStagVecGetArray#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagVecGetArray/

**Contents:**
- DMStagVecGetArray#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

get access to local array

dm - the DMSTAG object

This function returns a (dim+1)-dimensional array for a dim-dimensional DMSTAG.

The first 1-3 dimensions indicate an element in the global numbering, using the standard C ordering.

The final dimension in this array corresponds to a degree of freedom with respect to this element, for example corresponding to the element or one of its neighboring faces, edges, or vertices.

For example, for a 3D DMSTAG, indexing is array[k][j][i][slot], where k is the index in the z-direction, j is the index in the y-direction, and i is the index in the x-direction.

slot is obtained with DMStagGetLocationSlot(), since the correct offset into the \((d+1)\)-dimensional C array for a \(d\)-dimensional DMSTAG depends on the grid size and the number of DOF stored at each location.

DMStagVecRestoreArray() must be called, once finished with the array

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagVecGetArrayRead(), DMStagGetLocationSlot(), DMGetLocalVector(), DMCreateLocalVector(), DMGetGlobalVector(), DMCreateGlobalVector(), DMDAVecGetArray(), DMDAVecGetArrayDOF()

src/dm/impls/stag/stagutils.c

src/dm/impls/stag/tutorials/ex4.c src/dm/impls/stag/tutorials/ex1.c src/dm/impls/stag/tutorials/ex6.c src/dm/impls/stag/tutorials/ex3.c src/dm/impls/stag/tutorials/ex2.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagVecGetArray(DM dm, Vec vec, void *array)
```

Example 2 (unknown):
```unknown
array[k][j][i][slot]
```

Example 3 (unknown):
```unknown
DMStagGetLocationSlot()
```

Example 4 (unknown):
```unknown
DMStagVecRestoreArray()
```

---

## DMStagVecGetValuesStencil#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagVecGetValuesStencil/

**Contents:**
- DMStagVecGetValuesStencil#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

get vector values using grid indexing

dm - the DMSTAG object

vec - the vector object

n - the number of values to obtain

pos - locations to obtain values from (as an array of DMStagStencil values)

val - value at the point

Accepts stencils which refer to global element numbers, but only allows access to entries in the local representation (including ghosts).

This approach is not as efficient as getting values directly with DMStagVecGetArray(), which is recommended for matrix-free operators.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagStencil, DMStagStencilLocation, DMStagVecSetValuesStencil(), DMStagMatSetValuesStencil(), DMStagVecGetArray()

src/dm/impls/stag/stagstencil.c

src/dm/impls/stag/tutorials/ex1.c src/dm/impls/stag/tutorials/ex4.c src/dm/impls/stag/tutorials/ex6.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
PetscErrorCode DMStagVecGetValuesStencil(DM dm, Vec vec, PetscInt n, const DMStagStencil *pos, PetscScalar *val)
```

Example 2 (unknown):
```unknown
DMStagStencil
```

Example 3 (unknown):
```unknown
DMStagVecGetArray()
```

Example 4 (unknown):
```unknown
DMStagStencil
```

---

## DMStagVecRestoreArrayRead#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagVecRestoreArrayRead/

**Contents:**
- DMStagVecRestoreArrayRead#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

restore read-only access to a raw array

dm - the DMSTAG object

array - the read-only array

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagVecGetArrayRead(), DMDAVecRestoreArrayRead(), DMDAVecRestoreArrayDOFRead()

src/dm/impls/stag/stagutils.c

src/dm/impls/stag/tutorials/ex1.c src/dm/impls/stag/tutorials/ex3.c src/dm/impls/stag/tutorials/ex6.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagVecRestoreArrayRead(DM dm, Vec vec, void *array)
```

Example 2 (unknown):
```unknown
DMStagVecGetArrayRead()
```

Example 3 (unknown):
```unknown
DMDAVecRestoreArrayRead()
```

Example 4 (unknown):
```unknown
DMDAVecRestoreArrayDOFRead()
```

---

## DMStagVecRestoreArray#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagVecRestoreArray/

**Contents:**
- DMStagVecRestoreArray#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

restore access to a raw array

dm - the DMSTAG object

DMSTAG: Staggered, Structured Grid, DMSTAG, DMStagVecGetArray(), DMDAVecRestoreArray(), DMDAVecRestoreArrayDOF()

src/dm/impls/stag/stagutils.c

src/dm/impls/stag/tutorials/ex4.c src/dm/impls/stag/tutorials/ex1.c src/dm/impls/stag/tutorials/ex6.c src/dm/impls/stag/tutorials/ex3.c src/dm/impls/stag/tutorials/ex2.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
#include "petscdmproduct.h"   
PetscErrorCode DMStagVecRestoreArray(DM dm, Vec vec, void *array)
```

Example 2 (unknown):
```unknown
DMStagVecGetArray()
```

Example 3 (unknown):
```unknown
DMDAVecRestoreArray()
```

Example 4 (unknown):
```unknown
DMDAVecRestoreArrayDOF()
```

---

## DMStagVecSetValuesStencil#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagVecSetValuesStencil/

**Contents:**
- DMStagVecSetValuesStencil#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Set Vec values using global grid indexing

dm - the DMSTAG object

n - the number of values to set

pos - the locations to set values, as an array of DMStagStencil structs

val - the values to set

insertMode - INSERT_VALUES or ADD_VALUES

The vector is expected to be a global vector compatible with the DM (usually obtained by DMGetGlobalVector() or DMCreateGlobalVector()).

This approach is not as efficient as setting values directly with DMStagVecGetArray(), which is recommended for matrix-free operators. For assembling systems, where overhead may be less important than convenience, this routine could be helpful in assembling a righthand side and a matrix (using DMStagMatSetValuesStencil()).

DMSTAG: Staggered, Structured Grid, DMSTAG, Vec, DMStagStencil, DMStagStencilLocation, DMStagVecGetValuesStencil(), DMStagMatSetValuesStencil(), DMCreateGlobalVector(), DMGetLocalVector(), DMStagVecGetArray()

src/dm/impls/stag/stagstencil.c

src/dm/impls/stag/tutorials/ex4.c src/dm/impls/stag/tutorials/ex1.c src/dm/impls/stag/tutorials/ex8.c src/dm/impls/stag/tutorials/ex6.c src/dm/impls/stag/tutorials/ex3.c src/dm/impls/stag/tutorials/ex2.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmstag.h"   
PetscErrorCode DMStagVecSetValuesStencil(DM dm, Vec vec, PetscInt n, const DMStagStencil *pos, const PetscScalar *val, InsertMode insertMode)
```

Example 2 (unknown):
```unknown
DMStagStencil
```

Example 3 (unknown):
```unknown
INSERT_VALUES
```

Example 4 (unknown):
```unknown
DMGetGlobalVector()
```

---

## DMStagVecSplitToDMDA#

**URL:** https://petsc.org/release/manualpages/DMStag/DMStagVecSplitToDMDA/

**Contents:**
- DMStagVecSplitToDMDA#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

create a DMDA and Vec from a subgrid of a DMSTAG and its Vec

dm - the DMSTAG object

vec - Vec object associated with dm

loc - which subgrid to extract (see DMStagStencilLocation)

c - which component to extract (see note below)

If a c value of -k is provided, the first k DOF for that position are extracted, padding with zero values if needed. If a non-negative value is provided, a single DOF is extracted.

The caller is responsible for destroying the created DMDA and Vec.

DMSTAG: Staggered, Structured Grid, DMSTAG, DMDA, DMStagStencilLocation, DM, Vec, DMStagMigrateVec(), DMStagCreateCompatibleDMStag()

src/dm/impls/stag/stagda.c

src/dm/impls/stag/tutorials/ex4.c src/dm/impls/stag/tutorials/ex6.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h"   
#include "petscdmstag.h"   
PetscErrorCode DMStagVecSplitToDMDA(DM dm, Vec vec, DMStagStencilLocation loc, PetscInt c, DM *pda, Vec *pdavec)
```

Example 2 (unknown):
```unknown
DMStagStencilLocation
```

Example 3 (unknown):
```unknown
DMStagStencilLocation
```

Example 4 (unknown):
```unknown
DMStagMigrateVec()
```

---

## DMSTAG#

**URL:** https://petsc.org/release/manualpages/DMStag/DMSTAG/

**Contents:**
- DMSTAG#
- Notes#
- See Also#
- Level#
- Location#

"stag" - A DM object for working with a staggered grid (or mesh) or a structured cell complex.

This implementation parallels the DMDA implementation in many ways, but allows degrees of freedom to be associated with all “strata” in a logically-rectangular grid. That is, points, edges, faces, and cells (called elements).

Each stratum can be characterized by the dimension of the entities (“points”, to borrow the DMPLEX terminology), from 0- to 3-dimensional.

In some cases this numbering is used directly, for example with DMStagGetDOF(). To allow easier reading and to some extent more similar code between different-dimensional implementations of the same problem, we associate canonical names for each type of point, for each dimension of DMStag.

1-dimensional DMSTAG objects have vertices (0D) and elements (cells) (1D).

2-dimensional DMSTAG objects have vertices (0D), faces (1D), and elements (cells) (2D).

3-dimensional DMSTAG objects have vertices (0D), edges (1D), faces (2D), and elements (cells) (3D).

This naming is reflected when viewing a DMSTAG object with DMView(), and in forming convenient options prefixes when creating a decomposition with DMCreateFieldDecomposition().

For a DMSTAG each point on the same dimension has the same number of dof associated with it. For example, all cell points may have a single degree of freedom representing a pressure. This uniformity makes it possible to more efficiently “index into” (using a computable offset) vectors and arrays than for DMPLEX where each point may have a different number of degrees of freedom so the each offset (as well as the dof) must be explicitly stored.

DMSTAG: Staggered, Structured Grid, DM, DMPRODUCT, DMDA, DMPLEX, DMStagCreate1d(), DMStagCreate2d(), DMStagCreate3d(), DMType, DMCreate(), DMSetType(), DMStagVecSplitToDMDA()

src/dm/impls/stag/stag.c

Index of all DMStag routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMStagGetDOF()
```

Example 2 (unknown):
```unknown
DMCreateFieldDecomposition()
```

Example 3 (unknown):
```unknown
DMStagCreate1d()
```

Example 4 (unknown):
```unknown
DMStagCreate2d()
```

---

## DMSTAG: Staggered, Structured Grid#

**URL:** https://petsc.org/release/manual/dmstag/

**Contents:**
- DMSTAG: Staggered, Structured Grid#
- Terminology#
- Working with vectors and operators (matrices)#
- Coordinates#
- Numberings and internal data layout#

For structured (aka “regular”) grids with staggered data (degrees of freedom potentially living on elements, faces, edges, and/or vertices), the DMSTAG object is available. This can be useful for problems in many domains, including fluid flow, MHD, and seismology.

It is possible, though extremely cumbersome, to implement a staggered-grid code using multiple DMDA objects, or a single multi-component DMDA object where some degrees of freedom are unused. DMSTAG was developed for two main purposes:

To help manage some of the burden of choosing and adhering to the complex indexing conventions needed for staggered grids (in parallel)

To provide a uniform abstraction for which scalable solvers and preconditioners may be developed (in particular, using PCFIELDSPLIT and PCMG).

DMSTAG is design to behave much like DMDA, with a couple of important distinctions, and borrows some terminology from DMPLEX.

Like a DMPLEX object, a DMSTAG represents a cell complex, distributed in parallel over the ranks of an MPI_Comm. It is, however, a very regular complex, consisting of a structured grid of \(d\)-dimensional cells, with \(d \in \{1,2,3\}\), which are referred to as elements, \(d-1\) dimensional cells defining boundaries between these elements, and the boundaries of the domain, and in 2 or more dimensions, boundaries of these cells, all the way down to 0 dimensional cells referred to as vertices. In 2 dimensions, the 1-dimensional element boundaries are referred to as edges or faces. In 3 dimensions, the 2-dimensional element boundaries are referred to as faces and the 1-dimensional boundaries between faces are referred to as edges The set of cells of a given dimension is referred to as a stratum (which one can think of as a level in DAG representation of the mesh); a DMSTAG object of dimension \(d\) represents a complete cell complex with \(d+1\) strata (levels).

In the description of any:ch_unstructured the cells at each level are referred to as points. Thus we adopt that terminology uniformly in PETSc and so furthermore in this document, point will refer to a cell.

Each stratum has a constant number of unknowns (which may be zero) associated with each point (cell) on that level. The distinct unknowns associated with each point are referred to as components. For a DMPLEX there may be a different number of unknowns for each point on the same level.

The structured grid, is like with DMDA, decomposed via a Cartesian product of decompositions in each dimension, giving a rectangular local subdomain on each rank. This is extended by an element-wise stencil width of ghost elements to create an atlas of overlapping patches.

DMSTAG allows the user to reason almost entirely about a global indexing of elements. Element indices are simply 1-3 PetscInt values, starting at \(0\), in the back, bottom, left corner of the domain. For instance, element \((1,2,3)\), in 3D, is the element second from the left, third from the bottom, and fourth from the back (regardless of how many MPI ranks are used).

To refer to points (elements, faces, edges, and vertices), a value of DMStagStencilLocation is used, relative to the element index. The element itself is referred to with DMSTAG_ELEMENT, the top right vertex (in 2D) or the top right edge (in 3D) with DMSTAG_UP_RIGHT, the back bottom left corner in 3D with DMSTAG_BACK_DOWN_LEFT, and so on.

Fig. 10 gives a few examples in 2D.

Fig. 10 Locations in DMSTAG are indexed according to global element indices (here, two in 2D) and a location name. Elements have unique names but other locations can be referred to in more than one way. Element colors correspond to a parallel decomposition, but locations on the grid have names which are invariant to this. Note that the face on the top right can be referred to as being to the left of a “dummy” element \((3,3)\) outside the physical domain.#

Crucially, this global indexing scheme does not include any “ghost” or “padding” unknowns outside the physical domain. This is useful for higher-level operations such as computing norms or developing physics-based solvers. However (unlike DMDA), this implies that the global Vec do not have a natural block structure, as different strata have different numbers of points (e.g. in 1D there is an “extra” vertex on the right). This regular block structure is, however, very useful for the local representation of the data, so in that case dummy DOF are included, drawn as grey in Fig. 11.

Fig. 11 Local and global representations for a 2D DMSTAG object, 3 by 4 elements, with one degree of freedom on each of the three strata: element (squares), faces (triangles), and vertices (circles). The cell complex is parallelized across 4 MPI ranks. In the global representation, the colors correspond to which rank holds the native representation of the unknown. The 4 local representations are shown, with an (elementwise) stencil “box” stencil width of 1. Unknowns are colored by their native rank. Dummy unknowns, which correspond to no global degree of freedom, are colored grey. Note that the local representations have a natural block size of 4, and the global representation has no natural block size.#

For working with Vec data, this approach is used to allow direct access to a multi-dimensional, regular-blocked array. To avoid the user having to know about the internal numbering conventions used, helper functions are used to produce the proper final integer index for a given location and component, referred to as a “slot”. Similarly to DMDAVecGetArrayDOF(), this uses a \(d+1\) dimensional array in \(d\) dimensions. The following snippet give an example of this usage.

DMSTAG provides a stencil-based method for getting and setting entries of Mat and Vec objects. The follow excerpt from DMSTAG Tutorial ex1 demonstrates the idea. For more, see the manual page for DMStagMatSetValuesStencil().

The array-based approach for Vec is likely to be more efficient than the stencil-based method just introduced above.

DMSTAG, unlike DMDA, supports two approaches to defining coordinates. This is captured by which type of DM is used to represent the coordinates. No default is imposed, so the user must directly or indirectly call DMStagSetCoordinateDMType().

If a second DMSTAG object is used to represent coordinates in “explicit” form, behavior is much like with DMDA - the coordinate DM has \(d\) DOF on each stratum corresponding to coordinates associated with each point.

If DMPRODUCT is used instead, coordinates are represented by a DMPRODUCT object referring to a Cartesian product of 1D DMSTAG objects, each of which features explicit coordinates as just mentioned.

Navigating these nested DM in DMPRODUCT can be tedious, but note the existence of helper functions like DMStagSetUniformCoordinatesProduct() and DMStagGetProductCoordinateArrays().

While DMSTAG aims to hide the details of its internal data layout, for debugging, optimization, and customization purposes, it can be important to know how DMSTAG internally numbers unknowns.

Internally, each point is canonically associated with an element (top-level point (cell)). For purposes of local, regular-blocked storage, an element is grouped with lower-dimensional points left of, below (“down”), and behind (“back”) it. This means that “canonical” values of DMStagStencilLocation are DMSTAG_ELEMENT, plus all entries consisting only of “LEFT”, “DOWN”, and “BACK”. In general, these are the most efficient values to use, unless convenience dictates otherwise, as they are the ones used internally.

When creating the decomposition of the domain to local ranks, and extending these local domains to handle overlapping halo regions and boundary ghost unknowns, this same per-element association is used. This has the advantage of maintaining a regular blocking, but may not be optimal in some situations in terms of data movement.

Numberings are, like DMDA, based on a local “x-fastest, z-slowest” or “PETSc” ordering of elements (see Application Orderings), with ordering of locations canonically associated with each element decided by considering unknowns on each point to be located at the center of their point, and using a nested ordering of the same style. Thus, in 3-D, the ordering of the 8 canonical DMStagStencilLocation values associated with an element is

Multiple DOF associated with a given point are stored sequentially (as with DMDA).

For local Vecs, this gives a regular-blocked numbering, with the same number of unknowns associated with each element, including some “dummy” unknowns which to not correspond to any (local or global) unknown in the global representation. See Fig. 13 for an example.

In the global representation, only physical unknowns are numbered (using the same “Z” ordering for unknowns which are present), giving irregular numbers of unknowns, depending on whether a domain boundary is present. See Fig. 12 for an example.

Fig. 12 Global numbering scheme for a 2D DMSTAG object with one DOF per stratum. Note that the numbering depends on the parallel decomposition (over 4 ranks, here).#

Fig. 13 Local numbering scheme on rank 1 (Cf. Fig. 11) for a 2D DMSTAG object with one DOF per stratum. Note that dummy locations (grey) are used to give a regular block size (here, 4).#

It should be noted that this is an interlaced (AoS) representation. If a segregated (SoA) representation is required, one should use DMCOMPOSITE collecting several DMSTAG objects, perhaps using DMStagCreateCompatibleDMStag() to quickly create additional DMSTAG objects from an initial one.

DMPlex: Unstructured Grids

**Examples:**

Example 1 (unknown):
```unknown
PCFIELDSPLIT
```

Example 2 (unknown):
```unknown
ch_unstructured
```

Example 3 (unknown):
```unknown
DMStagStencilLocation
```

Example 4 (unknown):
```unknown
DMSTAG_ELEMENT
```

---

## MATHYPRESSTRUCT#

**URL:** https://petsc.org/release/manualpages/DMDA/MATHYPRESSTRUCT/

**Contents:**
- MATHYPRESSTRUCT#
- Notes#
- See Also#
- Level#
- Location#

MATHYPRESSTRUCT = “hypresstruct” - A matrix type to be used for parallel sparse matrices based on the hypre HYPRE_SStructMatrix.

Unlike hypre’s general semi-struct object consisting of a collection of structured-grid objects and unstructured grid objects, we restrict the semi-struct objects to consist of only structured-grid components.

Unlike the more general support for parts and blocks in hypre this allows only one part, and one block per process and requires the block be defined by a DMDA.

The matrix needs a DMDA associated with it by either a call to MatSetDM() or if the matrix is obtained from DMCreateMatrix()

src/dm/impls/da/hypre/mhyp.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

---

## MATHYPRESTRUCT#

**URL:** https://petsc.org/release/manualpages/DMDA/MATHYPRESTRUCT/

**Contents:**
- MATHYPRESTRUCT#
- Notes#
- See Also#
- Level#
- Location#

MATHYPRESTRUCT = “hyprestruct” - A matrix type to be used for parallel sparse matrices based on the hypre HYPRE_StructMatrix.

Unlike the more general support for blocks in hypre this allows only one block per process and requires the block be defined by a DMDA.

The matrix needs a DMDA associated with it by either a call to MatSetDM() or if the matrix is obtained from DMCreateMatrix()

MatCreate(), PCPFMG, MatSetDM(), DMCreateMatrix()

src/dm/impls/da/hypre/mhyp.c

Index of all DMDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateMatrix()
```

Example 2 (unknown):
```unknown
MatCreate()
```

Example 3 (unknown):
```unknown
DMCreateMatrix()
```

---

## Sequences of parallel mesh patches (DMPATCH)#

**URL:** https://petsc.org/release/manualpages/DMPatch/

**Contents:**
- Sequences of parallel mesh patches (DMPATCH)#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- No advanced routines#
- Developer - Interfaces rarely needed by applications programmers#
- Single list of manual pages#

The DMPATCH subclass of DM is intended to handle adaptive refinement calculated in serial using patches that fill the local machine. It is currently not working.

A Forest of Trees and Structured Adaptive Refinement (DMFOREST)

Particle Discretizations (DMSWARM)

---

## Staggered, Structured Grids (DMSTAG)#

**URL:** https://petsc.org/release/manualpages/DMStag/

**Contents:**
- Staggered, Structured Grids (DMSTAG)#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Single list of manual pages#

The DMSTAG subclass of DM encapsulates a Cartesian structured mesh, with “staggered” data living on elements, faces, edges, and vertices. Users guide chapter DMSTAG: Staggered, Structured Grid.

DMStagGetGhostCorners

DMStagGetLocationSlot

DMStagGetStencilWidth

DMStagSetStencilWidth

DMStagSetUniformCoordinatesExplicit

DMStagStencilLocation

DMStagVecGetArrayRead

DMStagVecRestoreArray

DMStagVecRestoreArrayRead

DMStagCreateCompatibleDMStag

DMStagGetBoundaryTypes

DMStagGetOwnershipRanges

DMStagGetProductCoordinateArrays

DMStagGetProductCoordinateArraysRead

DMStagGetProductCoordinateLocationSlot

DMStagGetRefinementFactor

DMStagMatSetValuesStencil

DMStagRestoreProductCoordinateArrays

DMStagRestoreProductCoordinateArraysRead

DMStagSetRefinementFactor

DMStagSetUniformCoordinatesProduct

DMStagCreateISFromStencils

DMStagMatGetValuesStencil

DMStagSetBoundaryTypes

DMStagSetCoordinateDMType

DMStagSetUniformCoordinates

DMStagVecGetValuesStencil

DMStagVecSetValuesStencil

DMStagGetEntriesLocal

DMStagGetEntriesPerElement

DMStagPopulateLocalToGlobalInjective

DMStagSetOwnershipRanges

DMStagStencilToIndexLocal

DMStagCreateCompatibleDMStag

DMStagCreateISFromStencils

DMStagGetBoundaryTypes

DMStagGetEntriesLocal

DMStagGetEntriesPerElement

DMStagGetGhostCorners

DMStagGetLocationSlot

DMStagGetOwnershipRanges

DMStagGetProductCoordinateArrays

DMStagGetProductCoordinateArraysRead

DMStagGetProductCoordinateLocationSlot

DMStagGetRefinementFactor

DMStagGetStencilWidth

DMStagMatGetValuesStencil

DMStagMatSetValuesStencil

DMStagPopulateLocalToGlobalInjective

DMStagRestoreProductCoordinateArrays

DMStagRestoreProductCoordinateArraysRead

DMStagSetBoundaryTypes

DMStagSetCoordinateDMType

DMStagSetOwnershipRanges

DMStagSetRefinementFactor

DMStagSetStencilWidth

DMStagSetUniformCoordinates

DMStagSetUniformCoordinatesExplicit

DMStagSetUniformCoordinatesProduct

DMStagStencilLocation

DMStagStencilToIndexLocal

DMStagVecGetArrayRead

DMStagVecGetValuesStencil

DMStagVecRestoreArray

DMStagVecRestoreArrayRead

DMStagVecSetValuesStencil

Structured Grids (DMDA)

Unstructured Grids and Cell Complexes (DMPLEX)

---

## Structured Grids (DMDA)#

**URL:** https://petsc.org/release/manualpages/DMDA/

**Contents:**
- Structured Grids (DMDA)#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Deprecated - Functionality scheduled for removal in the future#
- Single list of manual pages#

The DMDA subclass of DM encapsulates a Cartesian structured mesh, with interfaces for both topology and geometry. It is capable of parallel refinement and coarsening. Some support for parallel redistribution is available through the PCTELESCOPE object. A piecewise linear discretization is assumed for operations which require this information.

DMDAInterpolationType

DMDASetUniformCoordinates

DMDACreateCompatibleDMDA

DMDAGetCoordinateArray

DMDAGetCoordinateName

DMDAGetElementsCorners

DMDAGetInterpolationType

DMDAGetNonOverlappingRegion

DMDAGetNumLocalSubDomains

DMDAGetOwnershipRanges

DMDAGetRefinementFactor

DMDAGetSubdomainCornersIS

DMDAMapMatStencilToGlobal

DMDARestoreCoordinateArray

DMDARestoreSubdomainCornersIS

DMDASetCoordinateName

DMDASetInterpolationType

DMDASetNonOverlappingRegion

DMDASetNumLocalSubDomains

DMDASetOwnershipRanges

DMDASetRefinementFactor

DMDASetVertexCoordinates

DMDAVecGetArrayDOFRead

DMDAVecGetArrayDOFWrite

DMDAVecGetKokkosOffsetView

DMDAVecGetKokkosOffsetViewDOF

DMDAVecRestoreArrayDOF

DMDAVecRestoreArrayDOFRead

DMDAVecRestoreArrayDOFWrite

DMDAVecRestoreArrayRead

DMDAVecRestoreArrayWrite

DMDAVecRestoreKokkosOffsetView

DMDAVecRestoreKokkosOffsetViewDOF

DMDACreateNaturalVector

DMDAGetLogicalCoordinate

DMDAGetProcessorSubset

DMDAGetProcessorSubsets

DMDAGlobalToNaturalAllCreate

DMDAGlobalToNaturalBegin

DMDAGlobalToNaturalEnd

DMDANaturalAllToGlobalCreate

DMDANaturalToGlobalBegin

DMDANaturalToGlobalEnd

DMDASetGLLCoordinates

DMDAGetPreallocationCenterDimension

DMDASetBlockFillsSparse

DMDASetPreallocationCenterDimension

DMDACreateCompatibleDMDA

DMDACreateNaturalVector

DMDAGetCoordinateArray

DMDAGetCoordinateName

DMDAGetElementsCorners

DMDAGetInterpolationType

DMDAGetLogicalCoordinate

DMDAGetNonOverlappingRegion

DMDAGetNumLocalSubDomains

DMDAGetOwnershipRanges

DMDAGetPreallocationCenterDimension

DMDAGetProcessorSubset

DMDAGetProcessorSubsets

DMDAGetRefinementFactor

DMDAGetSubdomainCornersIS

DMDAGlobalToNaturalAllCreate

DMDAGlobalToNaturalBegin

DMDAGlobalToNaturalEnd

DMDAInterpolationType

DMDAMapMatStencilToGlobal

DMDANaturalAllToGlobalCreate

DMDANaturalToGlobalBegin

DMDANaturalToGlobalEnd

DMDARestoreCoordinateArray

DMDARestoreSubdomainCornersIS

DMDASetBlockFillsSparse

DMDASetCoordinateName

DMDASetGLLCoordinates

DMDASetInterpolationType

DMDASetNonOverlappingRegion

DMDASetNumLocalSubDomains

DMDASetOwnershipRanges

DMDASetPreallocationCenterDimension

DMDASetRefinementFactor

DMDASetUniformCoordinates

DMDASetVertexCoordinates

DMDAVecGetArrayDOFRead

DMDAVecGetArrayDOFWrite

DMDAVecGetKokkosOffsetView

DMDAVecGetKokkosOffsetViewDOF

DMDAVecRestoreArrayDOF

DMDAVecRestoreArrayDOFRead

DMDAVecRestoreArrayDOFWrite

DMDAVecRestoreArrayRead

DMDAVecRestoreArrayWrite

DMDAVecRestoreKokkosOffsetView

DMDAVecRestoreKokkosOffsetViewDOF

Staggered, Structured Grids (DMSTAG)

**Examples:**

Example 1 (unknown):
```unknown
PCTELESCOPE
```

---
