# Nonlinear solvers

## DMCopyDMSNES#

**URL:** https://petsc.org/release/manualpages/SNES/DMCopyDMSNES/

**Contents:**
- DMCopyDMSNES#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

copies a DMSNES context to a new DM

dmsrc - DM to obtain context from

dmdest - DM to add context to

The context is copied by reference. This function does not ensure that a context exists.

SNES: Nonlinear Solvers, DMSNES, DMGetDMSNES(), SNESSetDM()

src/snes/utils/dmsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
#include "petscdm.h" 
PetscErrorCode DMCopyDMSNES(DM dmsrc, DM dmdest)
```

Example 2 (unknown):
```unknown
DMGetDMSNES()
```

Example 3 (unknown):
```unknown
SNESSetDM()
```

---

## DMDASNESFunctionFn#

**URL:** https://petsc.org/release/manualpages/SNES/DMDASNESFunctionFn/

**Contents:**
- DMDASNESFunctionFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

Function type for the local residual callback set with DMDASNESSetFunctionLocal() on a DMDA-based SNES

info - the local grid information from the DMDA

u - pointer to the local input solution array

f - pointer to the local output residual array to be filled

ctx - optional user-provided context

DMDA, SNES, DMDASNESSetFunctionLocal(), DMDASNESJacobianFn, DMDASNESObjectiveFn, DMDASNESFunctionVecFn

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDASNESSetFunctionLocal()
```

Example 2 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode DMDASNESFunctionFn(DMDALocalInfo *info, void *u, void *f, PetscCtx ctx);
```

Example 3 (unknown):
```unknown
DMDASNESSetFunctionLocal()
```

Example 4 (unknown):
```unknown
DMDASNESJacobianFn
```

---

## DMDASNESFunctionVecFn#

**URL:** https://petsc.org/release/manualpages/SNES/DMDASNESFunctionVecFn/

**Contents:**
- DMDASNESFunctionVecFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

Vec-based variant of DMDASNESFunctionFn, set with DMDASNESSetFunctionLocalVec()

info - the local grid information from the DMDA

u - the local input solution Vec

f - the local output residual Vec

ctx - optional user-provided context

DMDA, SNES, DMDASNESSetFunctionLocalVec(), DMDASNESFunctionFn, DMDASNESJacobianVecFn, DMDASNESObjectiveVecFn

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDASNESFunctionFn
```

Example 2 (unknown):
```unknown
DMDASNESSetFunctionLocalVec()
```

Example 3 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode DMDASNESFunctionVecFn(DMDALocalInfo *info, Vec u, Vec f, PetscCtx ctx);
```

Example 4 (unknown):
```unknown
DMDASNESSetFunctionLocalVec()
```

---

## DMDASNESJacobianFn#

**URL:** https://petsc.org/release/manualpages/SNES/DMDASNESJacobianFn/

**Contents:**
- DMDASNESJacobianFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

Function type for the local Jacobian callback set with DMDASNESSetJacobianLocal() on a DMDA-based SNES

info - the local grid information from the DMDA

u - pointer to the local input solution array

J - the Jacobian matrix to assemble

Jp - the matrix from which the preconditioner for the Jacobian is to be constructed

ctx - optional user-provided context

DMDA, SNES, DMDASNESSetJacobianLocal(), DMDASNESFunctionFn, DMDASNESObjectiveFn, DMDASNESJacobianVecFn

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDASNESSetJacobianLocal()
```

Example 2 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode DMDASNESJacobianFn(DMDALocalInfo *info, void *u, Mat J, Mat Jp, PetscCtx ctx);
```

Example 3 (unknown):
```unknown
DMDASNESSetJacobianLocal()
```

Example 4 (unknown):
```unknown
DMDASNESFunctionFn
```

---

## DMDASNESJacobianVecFn#

**URL:** https://petsc.org/release/manualpages/SNES/DMDASNESJacobianVecFn/

**Contents:**
- DMDASNESJacobianVecFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

Vec-based variant of DMDASNESJacobianFn, set with DMDASNESSetJacobianLocalVec()

info - the local grid information from the DMDA

u - the local input solution Vec

J - the Jacobian matrix to assemble

Jp - the preconditioner matrix to assemble

ctx - optional user-provided context

DMDA, SNES, DMDASNESSetJacobianLocalVec(), DMDASNESJacobianFn, DMDASNESFunctionVecFn, DMDASNESObjectiveVecFn

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDASNESJacobianFn
```

Example 2 (unknown):
```unknown
DMDASNESSetJacobianLocalVec()
```

Example 3 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode DMDASNESJacobianVecFn(DMDALocalInfo *info, Vec u, Mat J, Mat Jp, PetscCtx ctx);
```

Example 4 (unknown):
```unknown
DMDASNESSetJacobianLocalVec()
```

---

## DMDASNESObjectiveFn#

**URL:** https://petsc.org/release/manualpages/SNES/DMDASNESObjectiveFn/

**Contents:**
- DMDASNESObjectiveFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

Function type for the local objective callback set with DMDASNESSetObjectiveLocal() on a DMDA-based SNES

info - the local grid information from the DMDA

u - pointer to the local input solution array

obj - on output, the local contribution to the objective function value

ctx - optional user-provided context

DMDA, SNES, DMDASNESSetObjectiveLocal(), DMDASNESFunctionFn, DMDASNESJacobianFn, DMDASNESObjectiveVecFn

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDASNESSetObjectiveLocal()
```

Example 2 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode DMDASNESObjectiveFn(DMDALocalInfo *info, void *u, PetscReal *obj, PetscCtx ctx);
```

Example 3 (unknown):
```unknown
DMDASNESSetObjectiveLocal()
```

Example 4 (unknown):
```unknown
DMDASNESFunctionFn
```

---

## DMDASNESObjectiveVecFn#

**URL:** https://petsc.org/release/manualpages/SNES/DMDASNESObjectiveVecFn/

**Contents:**
- DMDASNESObjectiveVecFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

Vec-based variant of DMDASNESObjectiveFn, set with DMDASNESSetObjectiveLocalVec()

info - the local grid information from the DMDA

u - the local input solution Vec

obj - on output, the local contribution to the objective function value

ctx - optional user-provided context

DMDA, SNES, DMDASNESSetObjectiveLocalVec(), DMDASNESObjectiveFn, DMDASNESFunctionVecFn, DMDASNESJacobianVecFn

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDASNESObjectiveFn
```

Example 2 (unknown):
```unknown
DMDASNESSetObjectiveLocalVec()
```

Example 3 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode DMDASNESObjectiveVecFn(DMDALocalInfo *info, Vec u, PetscReal *obj, PetscCtx ctx);
```

Example 4 (unknown):
```unknown
DMDASNESSetObjectiveLocalVec()
```

---

## DMDASNESSetFunctionLocalVec#

**URL:** https://petsc.org/release/manualpages/SNES/DMDASNESSetFunctionLocalVec/

**Contents:**
- DMDASNESSetFunctionLocalVec#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

set a local residual evaluation function that operates on a local vector for DMDA

dm - DM to associate callback with

imode - INSERT_VALUES if local function computes owned part, ADD_VALUES if it contributes to ghosted part

func - local residual evaluation

ctx - optional context for local residual evaluation

SNES: Nonlinear Solvers, DMDA, DMDASNESFunctionVecFn, DMDASNESSetFunctionLocal(), DMDASNESSetJacobianLocalVec(), DMSNESSetFunction(), DMDACreate1d(), DMDACreate2d(), DMDACreate3d()

src/snes/utils/dmdasnes.c

src/snes/tutorials/ex55.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h" 
#include "petscsnes.h" 
PetscErrorCode DMDASNESSetFunctionLocalVec(DM dm, InsertMode imode, DMDASNESFunctionVecFn *func, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
INSERT_VALUES
```

Example 3 (unknown):
```unknown
DMDASNESFunctionVecFn
```

Example 4 (unknown):
```unknown
DMDASNESSetFunctionLocal()
```

---

## DMDASNESSetFunctionLocal#

**URL:** https://petsc.org/release/manualpages/SNES/DMDASNESSetFunctionLocal/

**Contents:**
- DMDASNESSetFunctionLocal#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

set a local residual evaluation function for use with DMDA

dm - DM to associate callback with

imode - INSERT_VALUES if local function computes owned part, ADD_VALUES if it contributes to ghosted part

func - local residual evaluation

ctx - optional context for local residual evaluation

SNES: Nonlinear Solvers, DMDA, DMDASNESFunctionFn, DMDASNESSetJacobianLocal(), DMSNESSetFunction(), DMDACreate1d(), DMDACreate2d(), DMDACreate3d()

src/snes/utils/dmdasnes.c

src/snes/tutorials/ex55.c src/snes/tutorials/ex15.c src/snes/tutorials/ex9.c src/snes/tutorials/ex40f90.F90 src/snes/tutorials/ex46.c src/snes/tutorials/ex30.c src/snes/tutorials/ex48.c src/snes/tutorials/ex33.c src/snes/tutorials/ex25.c src/snes/tutorials/ex4.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h" 
#include "petscsnes.h" 
PetscErrorCode DMDASNESSetFunctionLocal(DM dm, InsertMode imode, DMDASNESFunctionFn *func, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
INSERT_VALUES
```

Example 3 (unknown):
```unknown
DMDASNESFunctionFn
```

Example 4 (unknown):
```unknown
DMDASNESSetJacobianLocal()
```

---

## DMDASNESSetJacobianLocalVec#

**URL:** https://petsc.org/release/manualpages/SNES/DMDASNESSetJacobianLocalVec/

**Contents:**
- DMDASNESSetJacobianLocalVec#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

set a local Jacobian evaluation function that operates on a local vector with DMDA

dm - DM to associate callback with

func - local Jacobian evaluation

ctx - optional context for local Jacobian evaluation

SNES: Nonlinear Solvers, DMDA, DMDASNESJacobianVecFn, DMDASNESSetJacobianLocal(), DMDASNESSetFunctionLocalVec(), DMSNESSetJacobian(), DMDACreate1d(), DMDACreate2d(), DMDACreate3d()

src/snes/utils/dmdasnes.c

src/snes/tutorials/ex55.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h" 
#include "petscsnes.h" 
PetscErrorCode DMDASNESSetJacobianLocalVec(DM dm, DMDASNESJacobianVecFn *func, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMDASNESJacobianVecFn
```

Example 3 (unknown):
```unknown
DMDASNESSetJacobianLocal()
```

Example 4 (unknown):
```unknown
DMDASNESSetFunctionLocalVec()
```

---

## DMDASNESSetJacobianLocal#

**URL:** https://petsc.org/release/manualpages/SNES/DMDASNESSetJacobianLocal/

**Contents:**
- DMDASNESSetJacobianLocal#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

set a local Jacobian evaluation function for use with DMDA

dm - DM to associate callback with

func - local Jacobian evaluation function

ctx - optional context for local Jacobian evaluation

The J and M matrices are created internally by DMCreateMatrix()

SNES: Nonlinear Solvers, DMDA, DMDASNESJacobianFn, DMDASNESSetFunctionLocal(), DMSNESSetJacobian(), DMDACreate1d(), DMDACreate2d(), DMDACreate3d()

src/snes/utils/dmdasnes.c

src/snes/tutorials/ex16.c src/snes/tutorials/ex55.c src/snes/tutorials/ex9.c src/snes/tutorials/ex5.c src/snes/tutorials/ex48.c src/snes/tutorials/ex15.c src/snes/tutorials/ex4.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h" 
#include "petscsnes.h" 
PetscErrorCode DMDASNESSetJacobianLocal(DM dm, DMDASNESJacobianFn *func, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMCreateMatrix()
```

Example 3 (unknown):
```unknown
DMDASNESJacobianFn
```

Example 4 (unknown):
```unknown
DMDASNESSetFunctionLocal()
```

---

## DMDASNESSetObjectiveLocalVec#

**URL:** https://petsc.org/release/manualpages/SNES/DMDASNESSetObjectiveLocalVec/

**Contents:**
- DMDASNESSetObjectiveLocalVec#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

set a local residual evaluation function that operates on a local vector with DMDA

dm - DM to associate callback with

func - local objective evaluation, see DMDASNESSetObjectiveLocalVec for the calling sequence

ctx - optional context for local residual evaluation

SNES: Nonlinear Solvers, DMDA, DMDASNESObjectiveVecFn, DMDASNESSetObjectiveLocal(), DMSNESSetFunction(), DMDASNESSetJacobianLocalVec(), DMDACreate1d(), DMDACreate2d(), DMDACreate3d(), DMDASNESObjectiveFn

src/snes/utils/dmdasnes.c

src/snes/tutorials/ex55.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h" 
#include "petscsnes.h" 
PetscErrorCode DMDASNESSetObjectiveLocalVec(DM dm, DMDASNESObjectiveVecFn *func, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMDASNESSetObjectiveLocalVec
```

Example 3 (unknown):
```unknown
DMDASNESObjectiveVecFn
```

Example 4 (unknown):
```unknown
DMDASNESSetObjectiveLocal()
```

---

## DMDASNESSetObjectiveLocal#

**URL:** https://petsc.org/release/manualpages/SNES/DMDASNESSetObjectiveLocal/

**Contents:**
- DMDASNESSetObjectiveLocal#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

set a local residual evaluation function to used with a DMDA

dm - DM to associate callback with

func - local objective evaluation, see DMDASNESSetObjectiveLocal for the calling sequence

ctx - optional context for local residual evaluation

SNES: Nonlinear Solvers, DMDA, DMDASNESObjectiveFn, DMSNESSetFunction(), DMDASNESSetJacobianLocal(), DMDACreate1d(), DMDACreate2d(), DMDACreate3d(), DMDASNESFunctionFn

src/snes/utils/dmdasnes.c

src/snes/tutorials/ex5.c src/snes/tutorials/ex55.c src/snes/tutorials/ex4.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h" 
#include "petscsnes.h" 
PetscErrorCode DMDASNESSetObjectiveLocal(DM dm, DMDASNESObjectiveFn *func, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMDASNESSetObjectiveLocal
```

Example 3 (unknown):
```unknown
DMDASNESObjectiveFn
```

Example 4 (unknown):
```unknown
DMSNESSetFunction()
```

---

## DMDASNESSetPicardLocal#

**URL:** https://petsc.org/release/manualpages/SNES/DMDASNESSetPicardLocal/

**Contents:**
- DMDASNESSetPicardLocal#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

set a local right-hand side and matrix evaluation function for Picard iteration with DMDA

dm - DM to associate callback with

imode - INSERT_VALUES if local function computes owned part, ADD_VALUES if it contributes to ghosted part

func - local residual evaluation

jac - function to compute Jacobian

ctx - optional context for local residual evaluation

The user must use SNESSetFunction(snes,NULL,SNESPicardComputeFunction,&user)); in their code before calling this routine.

SNES: Nonlinear Solvers, SNES, DMDA, DMDASNESFunctionFn, DMDASNESJacobianFn, DMSNESSetFunction(), DMDASNESSetJacobian(), DMDACreate1d(), DMDACreate2d(), DMDACreate3d()

src/snes/utils/dmdasnes.c

src/snes/tutorials/ex15.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h" 
#include "petscsnes.h" 
PetscErrorCode DMDASNESSetPicardLocal(DM dm, InsertMode imode, DMDASNESFunctionFn *func, DMDASNESJacobianFn *jac, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
INSERT_VALUES
```

Example 3 (unknown):
```unknown
SNESSetFunction
```

Example 4 (unknown):
```unknown
SNESPicardComputeFunction
```

---

## DMDestroyVI#

**URL:** https://petsc.org/release/manualpages/SNES/DMDestroyVI/

**Contents:**
- DMDestroyVI#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Frees the DM_SNESVI object contained in the DM and resets any function pointers the reduced-space SNESVI code composed onto it

dm - the DM from which the VI context should be removed (may be NULL)

DM, SNESVINEWTONRSLS, SNESVISetVariableBounds(), PetscObjectCompose()

src/snes/impls/vi/rs/virs.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode DMDestroyVI(DM dm)
```

Example 2 (unknown):
```unknown
SNESVINEWTONRSLS
```

Example 3 (unknown):
```unknown
SNESVISetVariableBounds()
```

Example 4 (unknown):
```unknown
PetscObjectCompose()
```

---

## DMGetDMSNESWrite#

**URL:** https://petsc.org/release/manualpages/SNES/DMGetDMSNESWrite/

**Contents:**
- DMGetDMSNESWrite#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

get write access to private DMSNES context from a DM

dm - DM to be used with SNES

snesdm - private DMSNES context

SNES: Nonlinear Solvers, DMSNES, DMGetDMSNES()

src/snes/utils/dmsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
#include "petscdm.h" 
PetscErrorCode DMGetDMSNESWrite(DM dm, DMSNES *snesdm)
```

Example 2 (unknown):
```unknown
DMGetDMSNES()
```

---

## DMGetDMSNES#

**URL:** https://petsc.org/release/manualpages/SNES/DMGetDMSNES/

**Contents:**
- DMGetDMSNES#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

get read-only private DMSNES context from a DM

dm - DM to be used with SNES

snesdm - private DMSNES context

Use DMGetDMSNESWrite() if write access is needed. The DMSNESSetXXX API should be used wherever possible.

SNES: Nonlinear Solvers, DMSNES, DMGetDMSNESWrite()

src/snes/utils/dmsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
#include "petscdm.h" 
PetscErrorCode DMGetDMSNES(DM dm, DMSNES *snesdm)
```

Example 2 (unknown):
```unknown
DMGetDMSNESWrite()
```

Example 3 (unknown):
```unknown
DMGetDMSNESWrite()
```

---

## DMPlexSetSNESLocalFEM#

**URL:** https://petsc.org/release/manualpages/SNES/DMPlexSetSNESLocalFEM/

**Contents:**
- DMPlexSetSNESLocalFEM#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Use DMPLEX’s internal FEM routines to compute SNES boundary values, objective, residual, and Jacobian.

use_obj - Use the objective function callback

ctx - The application context that will be passed to pointwise evaluation routines

SNES: Nonlinear Solvers, DMPLEX, SNES, PetscDSAddBoundary(), PetscDSSetObjective(), PetscDSSetResidual(), PetscDSSetJacobian()

src/snes/utils/dmplexsnes.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex26.c src/snes/tutorials/ex17.c src/snes/tutorials/ex8.c src/snes/tutorials/ex23.c src/snes/tutorials/ex64.c src/snes/tutorials/ex62.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMPlexSetSNESLocalFEM(DM dm, PetscBool use_obj, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
PetscDSAddBoundary()
```

Example 3 (unknown):
```unknown
PetscDSSetObjective()
```

Example 4 (unknown):
```unknown
PetscDSSetResidual()
```

---

## DMPlexSetSNESVariableBounds#

**URL:** https://petsc.org/release/manualpages/SNES/DMPlexSetSNESVariableBounds/

**Contents:**
- DMPlexSetSNESVariableBounds#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Compute upper and lower bounds for the solution using pointsie functions from the PetscDS

snes - the SNES object

This calls SNESVISetVariableBounds() after generating the bounds vectors, so it only applied to SNESVI solves.

We project the actual bounds into the current finite element space so that they become more accurate with refinement.

SNESVISetVariableBounds(), SNESVI, SNES: Nonlinear Solvers, DM

src/snes/utils/dmplexsnes.c

src/snes/tutorials/ex34.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMPlexSetSNESVariableBounds(DM dm, SNES snes)
```

Example 2 (unknown):
```unknown
SNESVISetVariableBounds()
```

Example 3 (unknown):
```unknown
SNESVISetVariableBounds()
```

---

## DMPlexSNESComputeBoundaryFEM#

**URL:** https://petsc.org/release/manualpages/SNES/DMPlexSNESComputeBoundaryFEM/

**Contents:**
- DMPlexSNESComputeBoundaryFEM#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Form the boundary values for the local input X

ctx - The application context

SNES: Nonlinear Solvers, DM, DMPLEX, DMPlexComputeJacobianAction()

src/snes/utils/dmplexsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMPlexSNESComputeBoundaryFEM(DM dm, Vec X, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMPlexComputeJacobianAction()
```

---

## DMPlexSNESComputeJacobianFEM#

**URL:** https://petsc.org/release/manualpages/SNES/DMPlexSNESComputeJacobianFEM/

**Contents:**
- DMPlexSNESComputeJacobianFEM#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Form the local portion of the Jacobian matrix Jac at the local solution X using pointwise functions specified by the user.

X - Local input vector

ctx - The application context

Jac - Jacobian matrix

JacP - approximate Jacobian from which the preconditioner will be built, often Jac

We form the residual one batch of elements at a time. This allows us to offload work onto an accelerator, like a GPU, or vectorize on a multicore machine.

SNES: Nonlinear Solvers, DMPLEX, Mat

src/snes/utils/dmplexsnes.c

src/tao/tutorials/ex3.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMPlexSNESComputeJacobianFEM(DM dm, Vec X, Mat Jac, Mat JacP, PetscCtx ctx)
```

---

## DMPlexSNESComputeObjectiveFEM#

**URL:** https://petsc.org/release/manualpages/SNES/DMPlexSNESComputeObjectiveFEM/

**Contents:**
- DMPlexSNESComputeObjectiveFEM#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Sums the local objectives from the local input X using pointwise functions specified by the user

ctx - The application context

obj - Local objective value

DM, DMPlexSNESComputeResidualFEM()

src/snes/utils/dmplexsnes.c

src/ts/tutorials/ex30.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMPlexSNESComputeObjectiveFEM(DM dm, Vec X, PetscReal *obj, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMPlexSNESComputeResidualFEM()
```

---

## DMPlexSNESComputeResidualCEED#

**URL:** https://petsc.org/release/manualpages/SNES/DMPlexSNESComputeResidualCEED/

**Contents:**
- DMPlexSNESComputeResidualCEED#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Assemble the local residual for a SNES on a DMPLEX using the libCEED operator attached to the DM

dm - the DMPLEX for which libCEED operators have been created by DMCeedCreate()

locX - local solution vector including ghost values

ctx - application context (unused)

locF - local residual vector to be assembled

This is normally installed as the SNES local residual callback via DMSNESSetFunctionLocal() when using libCEED for the finite-element evaluation.

SNES: Nonlinear Solvers, SNES, DMPLEX, DMCeedCreate(), DMSNESSetFunctionLocal(), DMPlexTSComputeRHSFunctionFVMCEED()

src/snes/utils/libceed/dmplexsnesceed.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMPlexSNESComputeResidualCEED(DM dm, Vec locX, Vec locF, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMCeedCreate()
```

Example 3 (unknown):
```unknown
DMSNESSetFunctionLocal()
```

Example 4 (unknown):
```unknown
DMCeedCreate()
```

---

## DMPlexSNESComputeResidualDS#

**URL:** https://petsc.org/release/manualpages/SNES/DMPlexSNESComputeResidualDS/

**Contents:**
- DMPlexSNESComputeResidualDS#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Sums the local residual into vector F from the local input X using all pointwise functions with unique keys in the PetscDS

ctx - The application context

F - Local output vector

The residual is summed into F; the caller is responsible for using VecZeroEntries() or otherwise ensuring that any data in F is intentional.

SNES: Nonlinear Solvers, DM, DMPLEX, DMPlexComputeJacobianAction()

src/snes/utils/dmplexsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMPlexSNESComputeResidualDS(DM dm, Vec X, Vec F, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
VecZeroEntries()
```

Example 3 (unknown):
```unknown
DMPlexComputeJacobianAction()
```

---

## DMPlexSNESComputeResidualFEM#

**URL:** https://petsc.org/release/manualpages/SNES/DMPlexSNESComputeResidualFEM/

**Contents:**
- DMPlexSNESComputeResidualFEM#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Sums the local residual into vector F from the local input X using pointwise functions specified by the user

ctx - The application context

F - Local output vector

The residual is summed into F; the caller is responsible for using VecZeroEntries() or otherwise ensuring that any data in F is intentional.

SNES: Nonlinear Solvers, DM, DMPLEX, DMSNESComputeJacobianAction()

src/snes/utils/dmplexsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMPlexSNESComputeResidualFEM(DM dm, Vec X, Vec F, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
VecZeroEntries()
```

Example 3 (unknown):
```unknown
DMSNESComputeJacobianAction()
```

---

## DMSetVI#

**URL:** https://petsc.org/release/manualpages/SNES/DMSetVI/

**Contents:**
- DMSetVI#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Marks a DM as associated with a VI problem. This causes the interpolation/restriction operators to be restricted to only those variables NOT associated with active constraints.

inactive - an IS indicating which points are currently not active

SNES: Nonlinear Solvers, SNES, SNESVINEWTONRSLS, SNESVIGetInactiveSet()

src/snes/impls/vi/rs/virs.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode DMSetVI(DM dm, IS inactive)
```

Example 2 (unknown):
```unknown
SNESVINEWTONRSLS
```

Example 3 (unknown):
```unknown
SNESVIGetInactiveSet()
```

---

## DMSNESCheckDiscretization#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESCheckDiscretization/

**Contents:**
- DMSNESCheckDiscretization#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

Check the discretization error of the exact solution

snes - the SNES object

tol - A tolerance for the check, or -1 to print the results instead

error - An array which holds the discretization error in each field, or NULL

The user must call PetscDSSetExactSolution() beforehand

How is this related to PetscConvEst?

SNES: Nonlinear Solvers, PetscDSSetExactSolution(), DNSNESCheckFromOptions(), DMSNESCheckResidual(), DMSNESCheckJacobian()

src/snes/utils/dmplexsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMSNESCheckDiscretization(SNES snes, DM dm, PetscReal t, Vec u, PetscReal tol, PetscReal error[])
```

Example 2 (unknown):
```unknown
PetscDSSetExactSolution()
```

Example 3 (unknown):
```unknown
PetscConvEst
```

Example 4 (unknown):
```unknown
PetscDSSetExactSolution()
```

---

## DMSNESCheckFromOptions#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESCheckFromOptions/

**Contents:**
- DMSNESCheckFromOptions#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Check the residual and Jacobian functions using the exact solution by outputting some diagnostic information

snes - the SNES object

u - representative SNES vector

The user must call PetscDSSetExactSolution() before this call

SNES: Nonlinear Solvers, SNES, DM

src/snes/utils/dmplexsnes.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex76.c src/snes/tutorials/ex69.c src/snes/tutorials/ex36.c src/snes/tutorials/ex26.c src/snes/tutorials/ex17.c src/snes/tutorials/ex24.c src/snes/tutorials/ex27.c src/snes/tutorials/ex23.c src/snes/tutorials/ex62.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMSNESCheckFromOptions(SNES snes, Vec u)
```

Example 2 (unknown):
```unknown
PetscDSSetExactSolution()
```

---

## DMSNESCheckJacobian#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESCheckJacobian/

**Contents:**
- DMSNESCheckJacobian#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Check the Jacobian of the exact solution against the residual using the Taylor Test

snes - the SNES object

tol - A tolerance for the check, or -1 to print the results instead

isLinear - Flag indicaing that the function looks linear, or NULL

convRate - The rate of convergence of the linear model, or NULL

SNES: Nonlinear Solvers, DNSNESCheckFromOptions(), DMSNESCheckDiscretization(), DMSNESCheckResidual()

src/snes/utils/dmplexsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMSNESCheckJacobian(SNES snes, DM dm, Vec u, PetscReal tol, PetscBool *isLinear, PetscReal *convRate)
```

Example 2 (unknown):
```unknown
DNSNESCheckFromOptions()
```

Example 3 (unknown):
```unknown
DMSNESCheckDiscretization()
```

Example 4 (unknown):
```unknown
DMSNESCheckResidual()
```

---

## DMSNESCheckResidual#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESCheckResidual/

**Contents:**
- DMSNESCheckResidual#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Check the residual of the exact solution

snes - the SNES object

tol - A tolerance for the check, or -1 to print the results instead

residual - The residual norm of the exact solution, or NULL

SNES: Nonlinear Solvers, DNSNESCheckFromOptions(), DMSNESCheckDiscretization(), DMSNESCheckJacobian()

src/snes/utils/dmplexsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMSNESCheckResidual(SNES snes, DM dm, Vec u, PetscReal tol, PetscReal *residual)
```

Example 2 (unknown):
```unknown
DNSNESCheckFromOptions()
```

Example 3 (unknown):
```unknown
DMSNESCheckDiscretization()
```

Example 4 (unknown):
```unknown
DMSNESCheckJacobian()
```

---

## DMSNESComputeJacobianAction#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESComputeJacobianAction/

**Contents:**
- DMSNESComputeJacobianAction#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

Compute the action of the Jacobian J(X) on Y

X - Local solution vector

Y - Local input vector

ctx - The application context

F - local output vector

Users will typically use DMSNESCreateJacobianMF() followed by MatMult() instead of calling this routine directly.

This only works with DMPLEX

This should be called DMPlexSNESComputeJacobianAction()

SNES: Nonlinear Solvers, DM, DMSNESCreateJacobianMF(), DMPlexSNESComputeResidualFEM()

src/snes/utils/dmplexsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMSNESComputeJacobianAction(DM dm, Vec X, Vec Y, Vec F, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMSNESCreateJacobianMF()
```

Example 3 (unknown):
```unknown
DMPlexSNESComputeJacobianAction()
```

Example 4 (unknown):
```unknown
DMSNESCreateJacobianMF()
```

---

## DMSNESCreateJacobianMF#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESCreateJacobianMF/

**Contents:**
- DMSNESCreateJacobianMF#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Create a Mat which computes the action of the Jacobian matrix-free

X - The evaluation point for the Jacobian

ctx - An application context, or NULL

Vec X is kept in J, so updating X then updates the evaluation point.

This only works for DMPLEX

SNES: Nonlinear Solvers, DM, SNES, DMSNESComputeJacobianAction()

src/snes/utils/dmplexsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMSNESCreateJacobianMF(DM dm, Vec X, PetscCtx ctx, Mat *J)
```

Example 2 (unknown):
```unknown
DMSNESComputeJacobianAction()
```

---

## DMSNESGetBoundaryLocal#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESGetBoundaryLocal/

**Contents:**
- DMSNESGetBoundaryLocal#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#

get the local boundary value function set with DMSNESSetBoundaryLocal().

dm - DM with the associated callback

func - local boundary value evaluation

ctx - context for local boundary value evaluation

X - ghosted solution vector, appropriate locations (such as essential boundary condition nodes) should be filled

ctx - option context passed in DMSNESSetBoundaryLocal()

SNES: Nonlinear Solvers, DMSNESSetFunctionLocal(), DMSNESSetBoundaryLocal(), DMSNESSetJacobianLocal()

src/snes/utils/dmlocalsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMSNESSetBoundaryLocal()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode DMSNESGetBoundaryLocal(DM dm, PetscErrorCode (**func)(DM dm, Vec X, PetscCtx ctx), PetscCtxRt ctx)
```

Example 3 (unknown):
```unknown
DMSNESSetBoundaryLocal()
```

Example 4 (unknown):
```unknown
DMSNESSetFunctionLocal()
```

---

## DMSNESGetFunctionLocal#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESGetFunctionLocal/

**Contents:**
- DMSNESGetFunctionLocal#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#

get the local residual evaluation function information set with DMSNESSetFunctionLocal().

dm - DM with the associated callback

func - local residual evaluation

ctx - context for local residual evaluation

dm - DM for the function

x - vector to state at which to evaluate residual

f - vector to hold the function evaluation

ctx - optional context passed above

SNES: Nonlinear Solvers, DMSNESSetFunction(), DMSNESSetFunctionLocal(), DMSNESSetJacobianLocal()

src/snes/utils/dmlocalsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMSNESSetFunctionLocal()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode DMSNESGetFunctionLocal(DM dm, PetscErrorCode (**func)(DM dm, Vec x, Vec f, PetscCtx ctx), PetscCtxRt ctx)
```

Example 3 (unknown):
```unknown
DMSNESSetFunction()
```

Example 4 (unknown):
```unknown
DMSNESSetFunctionLocal()
```

---

## DMSNESGetFunction#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESGetFunction/

**Contents:**
- DMSNESGetFunction#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

get SNES residual evaluation function from a DMSNES object

dm - DM to be used with SNES

f - residual evaluation function; see SNESFunctionFn for calling sequence

ctx - context for residual evaluation

SNESGetFunction() is normally used, but it calls this function internally because the application context is actually associated with the DM.

SNES: Nonlinear Solvers, DMSNES, DMSNESSetContext(), DMSNESSetFunction(), SNESSetFunction(), SNESFunctionFn

src/snes/utils/dmsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
#include "petscdm.h" 
PetscErrorCode DMSNESGetFunction(DM dm, SNESFunctionFn **f, PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
SNESFunctionFn
```

Example 3 (unknown):
```unknown
SNESGetFunction()
```

Example 4 (unknown):
```unknown
DMSNESSetContext()
```

---

## DMSNESGetJacobianLocal#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESGetJacobianLocal/

**Contents:**
- DMSNESGetJacobianLocal#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#

the local Jacobian evaluation function set with DMSNESSetJacobianLocal().

dm - DM with the associated callback

func - local Jacobian evaluation

ctx - context for local Jacobian evaluation

X - current solution vector (ghosted or not?)

Jp - approximate Jacobian used to compute the preconditioner, often J

ctx - a user provided context

SNES: Nonlinear Solvers, DMSNESSetJacobianLocal(), DMSNESSetJacobian()

src/snes/utils/dmlocalsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMSNESSetJacobianLocal()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode DMSNESGetJacobianLocal(DM dm, PetscErrorCode (**func)(DM dm, Vec X, Mat J, Mat Jp, PetscCtx ctx), PetscCtxRt ctx)
```

Example 3 (unknown):
```unknown
DMSNESSetJacobianLocal()
```

Example 4 (unknown):
```unknown
DMSNESSetJacobian()
```

---

## DMSNESGetJacobian#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESGetJacobian/

**Contents:**
- DMSNESGetJacobian#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

get SNES Jacobian evaluation function from a DMSNES object

dm - DM to be used with SNES

J - Jacobian evaluation function; for all calling sequence see SNESJacobianFn

ctx - context for residual evaluation

SNESGetJacobian() is normally used, but it calls this function internally because the application context is actually associated with the DM. This makes the interface consistent regardless of whether the user interacts with a DM or not.

If DM took a more central role at some later date, this could become the primary method of setting the Jacobian.

SNES: Nonlinear Solvers, DMSNES, DMSNESSetContext(), SNESSetFunction(), DMSNESSetJacobian(), SNESJacobianFn

src/snes/utils/dmsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
#include "petscdm.h" 
PetscErrorCode DMSNESGetJacobian(DM dm, SNESJacobianFn **J, PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
SNESJacobianFn
```

Example 3 (unknown):
```unknown
SNESGetJacobian()
```

Example 4 (unknown):
```unknown
DMSNESSetContext()
```

---

## DMSNESGetNGS#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESGetNGS/

**Contents:**
- DMSNESGetNGS#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

get SNES Gauss-Seidel relaxation function from a DMSNES object

dm - DM to be used with SNES

f - relaxation function which performs Gauss-Seidel sweeps, see SNESSetNGS()

ctx - context for residual evaluation

SNESGetNGS() is normally used, but it calls this function internally because the application context is actually associated with the DM.

This makes the interface consistent regardless of whether the user interacts with a DM or not. If DM took a more central role at some later date, this could become the primary method of setting the residual.

SNES: Nonlinear Solvers, DMSNES, DMSNESSetContext(), SNESGetNGS(), DMSNESGetJacobian(), DMSNESGetFunction()

src/snes/utils/dmsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
#include "petscdm.h" 
PetscErrorCode DMSNESGetNGS(DM dm, PetscErrorCode (**f)(SNES, Vec, Vec, void *), PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
SNESSetNGS()
```

Example 3 (unknown):
```unknown
SNESGetNGS()
```

Example 4 (unknown):
```unknown
DMSNESSetContext()
```

---

## DMSNESGetObjectiveLocal#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESGetObjectiveLocal/

**Contents:**
- DMSNESGetObjectiveLocal#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#

get the local objective evaluation function information set with DMSNESSetObjectiveLocal().

dm - DM with the associated callback

func - local objective evaluation

ctx - context for local residual evaluation

x - the location where the objective function is to be evaluated

obj - the value of the objective function

ctx - optional context for the local objective function evaluation

DMSNESSetObjective(), DMSNESSetObjectiveLocal(), DMSNESSetFunctionLocal()

src/snes/utils/dmlocalsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMSNESSetObjectiveLocal()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode DMSNESGetObjectiveLocal(DM dm, PetscErrorCode (**func)(DM dm, Vec x, PetscReal *obj, PetscCtx ctx), PetscCtxRt ctx) PeNSS
```

Example 3 (unknown):
```unknown
DMSNESSetObjective()
```

Example 4 (unknown):
```unknown
DMSNESSetObjectiveLocal()
```

---

## DMSNESGetObjective#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESGetObjective/

**Contents:**
- DMSNESGetObjective#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Returns the objective function set with DMSNESSetObjective()

dm - DM to be used with SNES

obj - objective evaluation routine (or NULL); see SNESObjectiveFn for the calling sequence

ctx - the function context (or NULL)

SNESGetFunction() is normally used, but it calls this function internally because the application context is actually associated with the DM.

SNES: Nonlinear Solvers, DMSNES, DMSNESSetContext(), DMSNESSetObjective(), SNESSetFunction(), SNESObjectiveFn

src/snes/utils/dmsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMSNESSetObjective()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
#include "petscdm.h" 
PetscErrorCode DMSNESGetObjective(DM dm, SNESObjectiveFn **obj, PetscCtxRt ctx)
```

Example 3 (unknown):
```unknown
SNESObjectiveFn
```

Example 4 (unknown):
```unknown
SNESGetFunction()
```

---

## DMSNESGetPicard#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESGetPicard/

**Contents:**
- DMSNESGetPicard#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

get SNES Picard iteration evaluation functions from a DMSNES object

dm - DM to be used with SNES

b - RHS evaluation function; see SNESFunctionFn for calling sequence

J - Jacobian evaluation function; see SNESJacobianFn for calling sequence

ctx - context for residual and matrix evaluation

SNES: Nonlinear Solvers, DMSNES, DMSNESSetContext(), SNESSetFunction(), DMSNESSetJacobian(), SNESFunctionFn, SNESJacobianFn

src/snes/utils/dmsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
#include "petscdm.h" 
PetscErrorCode DMSNESGetPicard(DM dm, SNESFunctionFn **b, SNESJacobianFn **J, PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
SNESFunctionFn
```

Example 3 (unknown):
```unknown
SNESJacobianFn
```

Example 4 (unknown):
```unknown
DMSNESSetContext()
```

---

## DMSNESSetBoundaryLocal#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESSetBoundaryLocal/

**Contents:**
- DMSNESSetBoundaryLocal#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#

set a function to insert, for example, essential boundary conditions into a ghosted solution vector

dm - DM to associate callback with

func - local boundary value evaluation

ctx - optional context for local boundary value evaluation

X - ghosted solution vector, appropriate locations (such as essential boundary condition nodes) should be filled

ctx - option context passed in DMSNESSetBoundaryLocal()

SNES: Nonlinear Solvers, DMSNESSetObjectiveLocal(), DMSNESSetFunctionLocal(), DMSNESSetJacobianLocal()

src/snes/utils/dmlocalsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode DMSNESSetBoundaryLocal(DM dm, PetscErrorCode (*func)(DM dm, Vec X, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMSNESSetBoundaryLocal()
```

Example 3 (unknown):
```unknown
DMSNESSetObjectiveLocal()
```

Example 4 (unknown):
```unknown
DMSNESSetFunctionLocal()
```

---

## DMSNESSetFunctionContextDestroy#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESSetFunctionContextDestroy/

**Contents:**
- DMSNESSetFunctionContextDestroy#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

set SNES residual evaluation context destroy function

dm - DM to be used with SNES

f - residual evaluation context destroy function, see PetscCtxDestroyFn for its calling sequence

SNES: Nonlinear Solvers, DMSNES, DMSNESSetFunction(), SNESSetFunction(), PetscCtxDestroyFn

src/snes/utils/dmsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
#include "petscdm.h" 
PetscErrorCode DMSNESSetFunctionContextDestroy(DM dm, PetscCtxDestroyFn *f)
```

Example 2 (unknown):
```unknown
PetscCtxDestroyFn
```

Example 3 (unknown):
```unknown
DMSNESSetFunction()
```

Example 4 (unknown):
```unknown
SNESSetFunction()
```

---

## DMSNESSetFunctionLocal#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESSetFunctionLocal/

**Contents:**
- DMSNESSetFunctionLocal#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#

set a local residual evaluation function. This function is called with local vector containing the local vector information PLUS ghost point information. It should compute a result for all local elements and DMSNES will automatically accumulate the overlapping values.

dm - DM to associate callback with

func - local residual evaluation

ctx - optional context for local residual evaluation

dm - DM for the function

x - vector to state at which to evaluate residual

f - vector to hold the function evaluation

ctx - optional context passed above

SNES: Nonlinear Solvers, DMSNESSetFunction(), DMSNESSetJacobianLocal()

src/snes/utils/dmlocalsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode DMSNESSetFunctionLocal(DM dm, PetscErrorCode (*func)(DM dm, Vec x, Vec f, PetscCtx ctx), PetscCtx ctx) PeNSS
```

Example 2 (unknown):
```unknown
DMSNESSetFunction()
```

Example 3 (unknown):
```unknown
DMSNESSetJacobianLocal()
```

---

## DMSNESSetFunction#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESSetFunction/

**Contents:**
- DMSNESSetFunction#
- Synopsis#
- Input Parameters#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

set SNES residual evaluation function

dm - DM to be used with SNES

f - residual evaluation function; see SNESFunctionFn for calling sequence

ctx - context for residual evaluation

SNESSetFunction() is normally used, but it calls this function internally because the application context is actually associated with the DM. This makes the interface consistent regardless of whether the user interacts with a DM or not.

If DM took a more central role at some later date, this could become the primary method of setting the residual.

SNES: Nonlinear Solvers, DMSNES, DMSNESSetContext(), SNESSetFunction(), DMSNESSetJacobian(), SNESFunctionFn

src/snes/utils/dmsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
#include "petscdm.h" 
PetscErrorCode DMSNESSetFunction(DM dm, SNESFunctionFn *f, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESFunctionFn
```

Example 3 (unknown):
```unknown
SNESSetFunction()
```

Example 4 (unknown):
```unknown
DMSNESSetContext()
```

---

## DMSNESSetJacobianContextDestroy#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESSetJacobianContextDestroy/

**Contents:**
- DMSNESSetJacobianContextDestroy#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

set SNES Jacobian evaluation context destroy function into a DMSNES object

dm - DM to be used with SNES

f - Jacobian evaluation context destroy function, see PetscCtxDestroyFn for its calling sequence

SNES: Nonlinear Solvers, DMSNES, DMSNESSetJacobian()

src/snes/utils/dmsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
#include "petscdm.h" 
PetscErrorCode DMSNESSetJacobianContextDestroy(DM dm, PetscCtxDestroyFn *f)
```

Example 2 (unknown):
```unknown
PetscCtxDestroyFn
```

Example 3 (unknown):
```unknown
DMSNESSetJacobian()
```

---

## DMSNESSetJacobianLocal#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESSetJacobianLocal/

**Contents:**
- DMSNESSetJacobianLocal#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#

set a local Jacobian evaluation function

dm - DM to associate callback with

func - local Jacobian evaluation

ctx - optional context for local Jacobian evaluation

X - current solution vector (ghosted or not?)

Jp - approximate Jacobian used to compute the preconditioner, often J

ctx - a user provided context

SNES: Nonlinear Solvers, DMSNESSetObjectiveLocal(), DMSNESSetFunctionLocal(), DMSNESSetBoundaryLocal()

src/snes/utils/dmlocalsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode DMSNESSetJacobianLocal(DM dm, PetscErrorCode (*func)(DM dm, Vec X, Mat J, Mat Jp, PetscCtx ctx), PetscCtx ctx) PeNSS
```

Example 2 (unknown):
```unknown
DMSNESSetObjectiveLocal()
```

Example 3 (unknown):
```unknown
DMSNESSetFunctionLocal()
```

Example 4 (unknown):
```unknown
DMSNESSetBoundaryLocal()
```

---

## DMSNESSetJacobian#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESSetJacobian/

**Contents:**
- DMSNESSetJacobian#
- Synopsis#
- Input Parameters#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

set SNES Jacobian evaluation function into a DMSNES object

dm - DM to be used with SNES

J - Jacobian evaluation function, see SNESJacobianFn

ctx - context for Jacobian evaluation

SNESSetJacobian() is normally used, but it calls this function internally because the application context is actually associated with the DM.

This makes the interface consistent regardless of whether the user interacts with a DM or not. If DM took a more central role at some later date, this could become the primary method of setting the Jacobian.

SNES: Nonlinear Solvers, DMSNES, DMSNESSetContext(), SNESSetFunction(), DMSNESGetJacobian(), SNESSetJacobian(), SNESJacobianFn

src/snes/utils/dmsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
#include "petscdm.h" 
PetscErrorCode DMSNESSetJacobian(DM dm, SNESJacobianFn *J, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESJacobianFn
```

Example 3 (unknown):
```unknown
SNESSetJacobian()
```

Example 4 (unknown):
```unknown
DMSNESSetContext()
```

---

## DMSNESSetMFFunction#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESSetMFFunction/

**Contents:**
- DMSNESSetMFFunction#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

set SNES residual evaluation function used in applying the matrix-free Jacobian with -snes_mf_operator

dm - DM to be used with SNES

func - residual evaluation function; see SNESFunctionFn for calling sequence

ctx - optional function context

If not provided then the function provided with SNESSetFunction() is used

SNES: Nonlinear Solvers, DMSNES, DMSNESSetContext(), SNESSetFunction(), DMSNESSetJacobian(), DMSNESSetFunction(), SNESFunctionFn

src/snes/utils/dmsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
-snes_mf_operator
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
#include "petscdm.h" 
PetscErrorCode DMSNESSetMFFunction(DM dm, SNESFunctionFn *func, PetscCtx ctx)
```

Example 3 (unknown):
```unknown
SNESFunctionFn
```

Example 4 (unknown):
```unknown
SNESSetFunction()
```

---

## DMSNESSetNGS#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESSetNGS/

**Contents:**
- DMSNESSetNGS#
- Synopsis#
- Input Parameters#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

set SNES Gauss-Seidel relaxation function into a DMSNES object

dm - DM to be used with SNES

f - relaxation function, see SNESGSFunction

ctx - context for residual evaluation

SNESSetNGS() is normally used, but it calls this function internally because the application context is actually associated with the DM. This makes the interface consistent regardless of whether the user interacts with a DM or not.

If DM took a more central role at some later date, this could become the primary method of supplying the smoother

SNES: Nonlinear Solvers, DMSNES, DMSNESSetContext(), SNESSetFunction(), DMSNESSetJacobian(), DMSNESSetFunction(), SNESGSFunction

src/snes/utils/dmsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
#include "petscdm.h" 
PetscErrorCode DMSNESSetNGS(DM dm, PetscErrorCode (*f)(SNES, Vec, Vec, void *), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESGSFunction
```

Example 3 (unknown):
```unknown
SNESSetNGS()
```

Example 4 (unknown):
```unknown
DMSNESSetContext()
```

---

## DMSNESSetObjectiveLocal#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESSetObjectiveLocal/

**Contents:**
- DMSNESSetObjectiveLocal#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#

set a local objective evaluation function. This function is called with local vector containing the local vector information PLUS ghost point information. It should compute a result for all local elements and DMSNES will automatically accumulate the overlapping values.

dm - DM to associate callback with

func - local objective evaluation

ctx - optional context for local objective function evaluation

x - the location where the objective is to be evaluated

obj - the value of the objective function

ctx - optional context for the local objective function evaluation

DMSNESSetFunctionLocal(), DMSNESSetJacobianLocal()

src/snes/utils/dmlocalsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode DMSNESSetObjectiveLocal(DM dm, PetscErrorCode (*func)(DM dm, Vec x, PetscReal *obj, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMSNESSetFunctionLocal()
```

Example 3 (unknown):
```unknown
DMSNESSetJacobianLocal()
```

---

## DMSNESSetObjective#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESSetObjective/

**Contents:**
- DMSNESSetObjective#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the objective function minimized by some of the SNES linesearch methods into a DMSNES object, used instead of the 2-norm of the residual

dm - DM to be used with SNES

obj - objective evaluation routine; see SNESObjectiveFn for the calling sequence

ctx - [optional] user-defined context for private data for the objective evaluation routine (may be NULL)

SNES: Nonlinear Solvers, DMSNES, DMSNESSetContext(), SNESGetObjective(), DMSNESSetFunction(), SNESObjectiveFn

src/snes/utils/dmsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
#include "petscdm.h" 
PetscErrorCode DMSNESSetObjective(DM dm, SNESObjectiveFn *obj, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESObjectiveFn
```

Example 3 (unknown):
```unknown
DMSNESSetContext()
```

Example 4 (unknown):
```unknown
SNESGetObjective()
```

---

## DMSNESSetPicard#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNESSetPicard/

**Contents:**
- DMSNESSetPicard#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

set SNES Picard iteration matrix and RHS evaluation functions into a DMSNES object

dm - DM to be used with SNES

b - RHS evaluation function; see SNESFunctionFn for calling sequence

J - Picard matrix evaluation function; see SNESJacobianFn for calling sequence

ctx - context for residual and matrix evaluation

SNES: Nonlinear Solvers, DMSNES, SNESSetPicard(), DMSNESSetFunction(), DMSNESSetJacobian(), SNESFunctionFn, SNESJacobianFn

src/snes/utils/dmsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
#include "petscdm.h" 
PetscErrorCode DMSNESSetPicard(DM dm, SNESFunctionFn *b, SNESJacobianFn *J, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESFunctionFn
```

Example 3 (unknown):
```unknown
SNESJacobianFn
```

Example 4 (unknown):
```unknown
SNESSetPicard()
```

---

## DMSNES#

**URL:** https://petsc.org/release/manualpages/SNES/DMSNES/

**Contents:**
- DMSNES#
- Synopsis#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#

Object held by a DM that contains all the callback functions and their contexts needed by a SNES

Users provides callback functions and their contexts to SNES using, for example, SNESSetFunction(). These values are stored in a DMSNES that is contained in the DM associated with the SNES. If no DM was provided by the user with SNESSetDM() it is automatically created by SNESGetDM() with DMShellCreate().

Users very rarely need to worked directly with the DMSNES object, rather they work with the SNES and the DM they created

Multiple DM can share a single DMSNES, often each DM is associated with a grid refinement level. DMGetDMSNES() returns the DMSNES associated with a DM. DMGetDMSNESWrite() returns a unique DMSNES that is only associated with the current DM, making a copy of the shared DMSNES if needed (copy-on-write).

See DMKSP for details on why there is a needed for DMSNES instead of simply storing the user callbacks directly in the DM or the TS

The originaldm inside the DMSNES is NOT reference counted (to prevent a reference count loop between a DM and a DMSNES). The DM on which this context was first created is cached here to implement one-way copy-on-write. When DMGetDMSNESWrite() sees a request using a different DM, it makes a copy of the TSDM. Thus, if a user only interacts directly with one level, e.g., using TSSetIFunction(), then coarse levels of a multilevel item integrator are built, then the user changes the routine with another call to TSSetIFunction(), it automatically propagates to all the levels. If instead, they get out a specific level and set the function on that level, subsequent changes to the original level will no longer propagate to that level.

SNES: Nonlinear Solvers, SNES, SNESCreate(), DM, DMGetDMSNESWrite(), DMGetDMSNES(), DMKSP, DMTS, DMSNESSetFunction(), DMSNESGetFunction(), DMSNESSetFunctionContextDestroy(), DMSNESSetMFFunction(), DMSNESSetNGS(), DMSNESGetNGS(), DMSNESSetJacobian(), DMSNESGetJacobian(), DMSNESSetJacobianContextDestroy(), DMSNESSetPicard(), DMSNESGetPicard(), DMSNESSetObjective(), DMSNESGetObjective(), DMCopyDMSNES()

include/petsc/private/snesimpl.h

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (swift):
```swift
struct _p_DMSNES {
  PETSCHEADER(struct _DMSNESOps);
  PetscContainer functionctxcontainer;
  PetscContainer jacobianctxcontainer;
  void          *mffunctionctx;
  void          *gsctx;
  void          *pctx;
  void          *objectivectx;

  void *data;

  /* See developer note for DMSNES above */
  DM originaldm;
};
```

Example 2 (unknown):
```unknown
SNESSetFunction()
```

Example 3 (unknown):
```unknown
SNESSetDM()
```

Example 4 (unknown):
```unknown
SNESGetDM()
```

---

## Full Approximation Scheme (FAS) nonlinear multigrid#

**URL:** https://petsc.org/release/manualpages/SNESFAS/

**Contents:**
- Full Approximation Scheme (FAS) nonlinear multigrid#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Single list of manual pages#

The SNESFAS subclass of SNES is a nonlinear multigrid solver which uses the Full Approximation Scheme.

SNESFASCycleGetCorrection

SNESFASCycleGetInjection

SNESFASCycleGetInterpolation

SNESFASCycleGetRScale

SNESFASCycleGetRestriction

SNESFASCycleGetSmoother

SNESFASCycleGetSmootherDown

SNESFASCycleGetSmootherUp

SNESFASCycleSetCycles

SNESFASFullSetDownSweep

SNESFASGetCoarseSolve

SNESFASGetInterpolation

SNESFASGetRestriction

SNESFASGetSmootherDown

SNESFASSetContinuation

SNESFASSetInterpolation

SNESFASSetNumberSmoothDown

SNESFASSetNumberSmoothUp

SNESFASSetRestriction

SNESFASCreateCoarseVec

SNESFASGalerkinFunctionDefault

SNESFASCreateCoarseVec

SNESFASCycleGetCorrection

SNESFASCycleGetInjection

SNESFASCycleGetInterpolation

SNESFASCycleGetRScale

SNESFASCycleGetRestriction

SNESFASCycleGetSmoother

SNESFASCycleGetSmootherDown

SNESFASCycleGetSmootherUp

SNESFASCycleSetCycles

SNESFASFullSetDownSweep

SNESFASGalerkinFunctionDefault

SNESFASGetCoarseSolve

SNESFASGetInterpolation

SNESFASGetRestriction

SNESFASGetSmootherDown

SNESFASSetContinuation

SNESFASSetInterpolation

SNESFASSetNumberSmoothDown

SNESFASSetNumberSmoothUp

SNESFASSetRestriction

Nonlinear Solvers (SNES)

Forward and Adjoint Timestepping

---

## KSPMonitorSNESResidualDrawLGCreate#

**URL:** https://petsc.org/release/manualpages/SNES/KSPMonitorSNESResidualDrawLGCreate/

**Contents:**
- KSPMonitorSNESResidualDrawLGCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Creates the PetscViewer used by KSPMonitorSNESResidualDrawLG()

viewer - The PetscViewer

format - The viewer format

ctx - An optional application context

vf - The viewer context

SNES: Nonlinear Solvers, KSP, SNES, PetscViewerFormat, PetscViewerAndFormat, KSPMonitorSet(), KSPMonitorTrueResidual()

src/snes/interface/snesut.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
KSPMonitorSNESResidualDrawLG()
```

Example 3 (unknown):
```unknown
#include "petsc/private/snesimpl.h"   
PetscErrorCode KSPMonitorSNESResidualDrawLGCreate(PetscViewer viewer, PetscViewerFormat format, PetscCtx ctx, PetscViewerAndFormat **vf)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## KSPMonitorSNESResidualDrawLG#

**URL:** https://petsc.org/release/manualpages/SNES/KSPMonitorSNESResidualDrawLG/

**Contents:**
- KSPMonitorSNESResidualDrawLG#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Plots the linear KSP residual norm and the SNES residual norm of a KSPSolve() called within a SNESSolve().

ksp - iterative context

rnorm - 2-norm (preconditioned) residual value (may be estimated).

vf - The viewer context, created with KSPMonitorSNESResidualDrawLGCreate()

-snes_monitor_ksp draw::draw_lg - Activates KSPMonitorSNESResidualDrawLG()

This is not called directly by users, rather one calls SNESMonitorSet(), with this function as an argument, to cause the monitor to be used during the SNESSolve()

SNES: Nonlinear Solvers, KSPMonitorSet(), KSPMonitorTrueResidual(), SNESMonitor(), KSPMonitor(), KSPMonitorSNESResidualDrawLGCreate()

src/snes/interface/snesut.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petsc/private/snesimpl.h"   
PetscErrorCode KSPMonitorSNESResidualDrawLG(KSP ksp, PetscInt n, PetscReal rnorm, PetscViewerAndFormat *vf)
```

Example 3 (unknown):
```unknown
KSPMonitorSNESResidualDrawLGCreate()
```

Example 4 (unknown):
```unknown
KSPMonitorSNESResidualDrawLG()
```

---

## KSPMonitorSNESResidual#

**URL:** https://petsc.org/release/manualpages/SNES/KSPMonitorSNESResidual/

**Contents:**
- KSPMonitorSNESResidual#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Prints the SNES residual norm, as well as the KSP residual norm, at each iteration of a KSPSolve() called within a SNESSolve().

ksp - iterative context

rnorm - 2-norm (preconditioned) residual value (may be estimated).

vf - The viewer context

-snes_monitor_ksp - Activates KSPMonitorSNESResidual()

This is not called directly by users, rather one calls KSPMonitorSet(), with this function as an argument, to cause the monitor to be used during the KSP solve.

SNES: Nonlinear Solvers, SNES, KSPMonitorSet(), KSPMonitorResidual(), KSPMonitorTrueResidualMaxNorm(), KSPMonitor(), SNESMonitor(), PetscViewerAndFormat()

src/snes/interface/snesut.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petsc/private/snesimpl.h"   
PetscErrorCode KSPMonitorSNESResidual(KSP ksp, PetscInt n, PetscReal rnorm, PetscViewerAndFormat *vf)
```

Example 3 (unknown):
```unknown
KSPMonitorSNESResidual()
```

Example 4 (unknown):
```unknown
KSPMonitorSet()
```

---

## MatCreateSNESMFMore#

**URL:** https://petsc.org/release/manualpages/SNES/MatCreateSNESMFMore/

**Contents:**
- MatCreateSNESMFMore#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#

Creates a matrix-free matrix context for use with a SNES solver that uses the More method to compute an optimal h based on the noise of the function. This matrix can be used as the Jacobian argument for the routine SNESSetJacobian().

snes - the SNES context

x - vector where SNES solution is to be stored.

J - the matrix-free matrix

-snes_mf_err error_rel - see MatCreateSNESMF()

-snes_mf_umin umin - see MatCreateSNESMF()

-snes_mf_compute_err - compute the square root or relative error in function

-snes_mf_freq_err freq - set the frequency to recompute the parameters

-snes_mf_jorge - use the method of Jorge More

This is an experimental approach, use MatCreateSNESMF().

The matrix-free matrix context merely contains the function pointers and work space for performing finite difference approximations of Jacobian-vector products, J(u)*a, via

The user can set these parameters via MatMFFDSetFunctionError().

The user should call MatDestroy() when finished with the matrix-free matrix context.

SNES: Nonlinear Solvers, SNESCreateMF(), MatCreateMFFD(), MatDestroy(), MatMFFDSetFunctionError()

src/snes/interface/noise/snesmfj2.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetJacobian()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode MatCreateSNESMFMore(SNES snes, Vec x, Mat *J)
```

Example 3 (unknown):
```unknown
MatCreateSNESMF()
```

Example 4 (unknown):
```unknown
MatCreateSNESMF()
```

---

## MatCreateSNESMF#

**URL:** https://petsc.org/release/manualpages/SNES/MatCreateSNESMF/

**Contents:**
- MatCreateSNESMF#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Creates a finite differencing based matrix-free matrix context for use with a SNES solver. This matrix can be used as the Jacobian argument for the routine SNESSetJacobian(). See MatCreateMFFD() for details on how the finite difference computation is done.

snes - the SNES context

J - the matrix-free matrix which is of type MATMFFD

You can call SNESSetJacobian() with MatMFFDComputeJacobian() if you are not using a different matrix to construct the preconditioner.

If you wish to provide a different function to do differencing on to compute the matrix-free operator than that provided to SNESSetFunction() then call MatMFFDSetFunction() with your function after this call.

The difference between this routine and MatCreateMFFD() is that this matrix automatically gets the current base vector from the SNES object and not from an explicit call to MatMFFDSetBase().

If MatMFFDSetBase() is ever called on jac then this routine will NO longer get the x from the SNES object and MatMFFDSetBase() must from that point on be used to change the base vector x.

Using a different function for the differencing will not work if you are using non-linear left preconditioning.

This uses finite-differencing to apply the operator. To create a matrix-free Mat whose matrix-vector operator you provide with your own function use MatCreateShell().

This function should really be called MatCreateSNESMFFD() in correspondence to MatCreateMFFD() to clearly indicate that this is for using finite differences to apply the operator matrix-free.

SNES: Nonlinear Solvers, SNES, MATMFFD, MatDestroy(), MatMFFDSetFunction(), MatMFFDSetFunctionError(), MatMFFDDSSetUmin(), MatMFFDSetHHistory(), MatMFFDResetHHistory(), MatCreateMFFD(), MatCreateShell(), MatMFFDGetH(), MatMFFDRegister(), MatMFFDComputeJacobian(), MatSNESMFSetReuseBase(), MatSNESMFGetReuseBase()

src/snes/mf/snesmfj.c

src/ts/tutorials/ex15.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetJacobian()
```

Example 2 (unknown):
```unknown
MatCreateMFFD()
```

Example 3 (unknown):
```unknown
#include "petscsnes.h" 
#include "petscdm.h"   
PetscErrorCode MatCreateSNESMF(SNES snes, Mat *J)
```

Example 4 (unknown):
```unknown
SNESSetJacobian()
```

---

## MatMFFDComputeJacobian#

**URL:** https://petsc.org/release/manualpages/SNES/MatMFFDComputeJacobian/

**Contents:**
- MatMFFDComputeJacobian#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Tells the matrix-free Jacobian object the new location at which Jacobian matrix-vector products will be computed at, i.e. J(x) * a. The x is obtained from the SNES object (using SNESGetSolution()).

snes - the nonlinear solver context

x - the point at which the Jacobian-vector products will be performed

jac - the matrix-free Jacobian object of MatType MATMFFD, likely obtained with MatCreateSNESMF()

B - either the same as jac or another matrix type (ignored)

dummy - the application context (ignored)

-snes_mf - use the matrix created with MatSNESMFCreate() to setup the Jacobian for each new solution in the Newton process

If MatMFFDSetBase() is ever called on jac then this routine will NO longer get the x from the SNES object and MatMFFDSetBase() must from that point on be used to change the base vector x.

This can be passed into SNESSetJacobian() as the Jacobian evaluation function argument when using a completely matrix-free solver, that is the B matrix is also the same matrix operator. This is used when you select -snes_mf but rarely used directly by users. (All this routine does is call MatAssemblyBegin/End() on the Mat jac.)

SNES: Nonlinear Solvers, MatMFFDGetH(), MatCreateSNESMF(), MatMFFDSetBase(), MatCreateMFFD(), MATMFFD, MatMFFDSetHHistory(), MatMFFDSetFunctionError(), SNESSetJacobian()

src/snes/mf/snesmfj.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESGetSolution()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
#include "petscdm.h"   
PetscErrorCode MatMFFDComputeJacobian(SNES snes, Vec x, Mat jac, Mat B, void *dummy)
```

Example 3 (unknown):
```unknown
MatCreateSNESMF()
```

Example 4 (unknown):
```unknown
MatSNESMFCreate()
```

---

## MatSNESMFGetReuseBase#

**URL:** https://petsc.org/release/manualpages/SNES/MatSNESMFGetReuseBase/

**Contents:**
- MatSNESMFGetReuseBase#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Determines if the base vector is to be used for differencing even if the function provided to SNESSetFunction() is not the same as that provided to MatMFFDSetFunction().

J - the MATMFFD matrix

use - if true always reuse the base vector instead of recomputing f(u) even if the function in the MATMFFD is not SNESComputeFunction()

See MatSNESMFSetReuseBase()

SNES: Nonlinear Solvers, Mat, SNES, MatSNESMFSetReuseBase(), MatCreateSNESMF()

src/snes/mf/snesmfj.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetFunction()
```

Example 2 (unknown):
```unknown
MatMFFDSetFunction()
```

Example 3 (unknown):
```unknown
#include "petscsnes.h" 
#include "petscdm.h"   
PetscErrorCode MatSNESMFGetReuseBase(Mat J, PetscBool *use)
```

Example 4 (unknown):
```unknown
SNESComputeFunction()
```

---

## MatSNESMFGetSNES#

**URL:** https://petsc.org/release/manualpages/SNES/MatSNESMFGetSNES/

**Contents:**
- MatSNESMFGetSNES#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

returns the SNES associated with a matrix created with MatCreateSNESMF()

snes - the SNES object

SNES: Nonlinear Solvers, Mat, SNES, MatCreateSNESMF()

src/snes/mf/snesmfj.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
MatCreateSNESMF()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
#include "petscdm.h"   
PetscErrorCode MatSNESMFGetSNES(Mat J, SNES *snes)
```

Example 3 (unknown):
```unknown
MatCreateSNESMF()
```

---

## MatSNESMFMoreSetParameters#

**URL:** https://petsc.org/release/manualpages/SNES/MatSNESMFMoreSetParameters/

**Contents:**
- MatSNESMFMoreSetParameters#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#

Sets the parameters for the approximation of matrix-vector products using finite differences, see MatCreateSNESMFMore()

error - relative error (should be set to the square root of the relative error in the function evaluations)

umin - minimum allowable u-value

h - differencing parameter

-snes_mf_err error_rel - see MatCreateSNESMF()

-snes_mf_umin umin - see MatCreateSNESMF()

-snes_mf_compute_err - compute the square root or relative error in function

-snes_mf_freq_err freq - set the frequency to recompute the parameters

-snes_mf_jorge - use the method of Jorge More

If the user sets the parameter h directly, then this value will be used instead of the default computation as discussed in MatCreateSNESMFMore()

SNES: Nonlinear Solvers, SNES, MatCreateSNESMF(), MatCreateSNESMFMore()

src/snes/interface/noise/snesmfj2.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
MatCreateSNESMFMore()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode MatSNESMFMoreSetParameters(Mat mat, PetscReal error, PetscReal umin, PetscReal h)
```

Example 3 (unknown):
```unknown
MatCreateSNESMF()
```

Example 4 (unknown):
```unknown
MatCreateSNESMF()
```

---

## MatSNESMFSetReuseBase#

**URL:** https://petsc.org/release/manualpages/SNES/MatSNESMFSetReuseBase/

**Contents:**
- MatSNESMFSetReuseBase#
- Synopsis#
- Input Parameters#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#

Causes the base vector to be used for differencing even if the function provided to SNESSetFunction() is not the same as that provided to MatMFFDSetFunction().

J - the MATMFFD matrix

use - if true always reuse the base vector instead of recomputing f(u) even if the function in the MATMFFD is not SNESComputeFunction()

Care must be taken when using this routine to insure that the function provided to MatMFFDSetFunction(), call it F_MF() is compatible with with that provided to SNESSetFunction(), call it F_SNES(). That is, (F_MF(u + h*d) - F_SNES(u))/h has to approximate the derivative

This was provided for the MOOSE team who desired to have a SNESSetFunction() function that could change configurations (similar to variable switching) to contacts while the function provided to MatMFFDSetFunction() cannot. Except for the possibility of changing the configuration both functions compute the same mathematical function so the differencing makes sense.

SNES: Nonlinear Solvers, SNES, MATMFFD, MatMFFDSetFunction(), SNESSetFunction(), MatCreateSNESMF(), MatSNESMFGetReuseBase()

src/snes/mf/snesmfj.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetFunction()
```

Example 2 (unknown):
```unknown
MatMFFDSetFunction()
```

Example 3 (unknown):
```unknown
#include "petscsnes.h" 
#include "petscdm.h"   
PetscErrorCode MatSNESMFSetReuseBase(Mat J, PetscBool use)
```

Example 4 (unknown):
```unknown
SNESComputeFunction()
```

---

## Nonlinear Solvers (SNES)#

**URL:** https://petsc.org/release/manualpages/SNES/

**Contents:**
- Nonlinear Solvers (SNES)#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Deprecated - Functionality scheduled for removal in the future#
- Single list of manual pages#

The Scalable Nonlinear Equations Solvers (SNES) component provides an easy-to-use interface to Newton-type, quasi-Newton, full approximation scheme (FAS) multigrid, and other methods for solving systems of nonlinear equations. User guide chapter: SNES: Nonlinear Solvers.

SNES internally employs KSP for the solution of its linear systems. SNES users can also set KSP options directly in application codes by first extracting the KSP context from the SNES context via SNESGetKSP() and then directly calling various KSP (and PC) routines,

DMDASNESSetFunctionLocal

DMDASNESSetFunctionLocalVec

DMDASNESSetJacobianLocal

DMDASNESSetJacobianLocalVec

DMDASNESSetObjectiveLocal

DMDASNESSetObjectiveLocalVec

DMDASNESSetPicardLocal

DMSNESGetFunctionLocal

DMSNESGetJacobianLocal

DMSNESGetObjectiveLocal

PetscConvEstSetFromOptions

SNESConvergedReasonView

SNESGetConvergedReasonString

SNES_CONERGED_ITERATING

SNES_CONVERGED_FNORM_ABS

SNES_CONVERGED_FNORM_RELATIVE

SNES_CONVERGED_SNORM_RELATIVE

SNES_DIVERGED_FUNCTION_COUNT

SNES_DIVERGED_FUNCTION_DOMAIN

SNES_DIVERGED_FUNCTION_NANORINF

SNES_DIVERGED_JACOBIAN_DOMAIN

SNES_DIVERGED_LINE_SEARCH

SNES_DIVERGED_LOCAL_MIN

SNES_DIVERGED_OBJECTIVE_DOMAIN

DMDASNESFunctionVecFn

DMDASNESJacobianVecFn

DMDASNESObjectiveVecFn

DMPlexSetSNESVariableBounds

DMSNESGetBoundaryLocal

KSPMonitorSNESResidual

KSPMonitorSNESResidualDrawLG

KSPMonitorSNESResidualDrawLGCreate

PetscConvEstGetConvRate

PetscConvEstGetSolver

PetscConvEstMonitorDefault

PetscConvEstSetSolver

SNESCompositeSetDamping

SNESComputeJacobianDefault

SNESComputeJacobianDefaultColor

SNESConvergedReasonViewCancel

SNESConvergedReasonViewSet

SNESGetApplicationContext

SNESGetConvergedReason

SNESGetConvergenceHistory

SNESGetDivergenceTolerance

SNESGetErrorIfNotConverged

SNESGetForceIteration

SNESGetIterationNumber

SNESGetLagPreconditioner

SNESGetLinearSolveFailures

SNESGetLinearSolveIterations

SNESGetMaxLinearSolveFailures

SNESGetMaxNonlinearStepFailures

SNESGetNonlinearStepFailures

SNESGetNumberFunctionEvals

SNESLINESEARCHBISECTION

SNESLineSearchBTGetAlpha

SNESLineSearchBTSetAlpha

SNESLineSearchComputeNorms

SNESLineSearchGetDefaultMonitor

SNESLineSearchGetOrder

SNESLineSearchGetPostCheck

SNESLineSearchGetPreCheck

SNESLineSearchGetTolerances

SNESLineSearchGetType

SNESLineSearchMonitorSet

SNESLineSearchSetComputeNorms

SNESLineSearchSetDamping

SNESLineSearchSetDefaultMonitor

SNESLineSearchSetFromOptions

SNESLineSearchSetOrder

SNESLineSearchSetPostCheck

SNESLineSearchSetPreCheck

SNESLineSearchSetTolerances

SNESLineSearchSetType

SNESMonitorDefaultField

SNESMonitorJacUpdateSpectrum

SNESMonitorRatioSetUp

SNESMonitorSolutionUpdate

SNESMultiblockSetBlockSize

SNESMultiblockSetFields

SNESNASMGetSubdomains

SNESNASMSetSubdomains

SNESNGMRESRestartType

SNESNGMRESSetRestartType

SNESNGMRESSetSelectType

SNESNewtonALCorrectionType

SNESNewtonALGetFunction

SNESNewtonALGetLoadParameter

SNESNewtonALSetCorrectionType

SNESNewtonALSetDiagonalScaling

SNESNewtonALSetFunction

SNESNewtonTRDCGetPostCheck

SNESNewtonTRDCGetPreCheck

SNESNewtonTRDCSetPostCheck

SNESNewtonTRDCSetPreCheck

SNESNewtonTRFallbackType

SNESNewtonTRGetPostCheck

SNESNewtonTRGetPreCheck

SNESNewtonTRGetTolerances

SNESNewtonTRGetUpdateParameters

SNESNewtonTRPostCheck

SNESNewtonTRSetFallbackType

SNESNewtonTRSetNormType

SNESNewtonTRSetPostCheck

SNESNewtonTRSetPreCheck

SNESNewtonTRSetQNType

SNESNewtonTRSetTolerances

SNESNewtonTRSetUpdateParameters

SNESPruneJacobianColor

SNESSetApplicationContext

SNESSetComputeApplicationContext

SNESSetComputeInitialGuess

SNESSetConvergenceHistory

SNESSetDivergenceTolerance

SNESSetErrorIfNotConverged

SNESSetForceIteration

SNESSetLagPreconditioner

SNESSetMaxLinearSolveFailures

SNESSetMaxNonlinearStepFailures

DMSNESCreateJacobianMF

DMSNESSetBoundaryLocal

DMSNESSetFunctionLocal

DMSNESSetJacobianLocal

DMSNESSetObjectiveLocal

MatSNESMFGetReuseBase

MatSNESMFMoreSetParameters

MatSNESMFSetReuseBase

SNESAppendOptionsPrefix

SNESConvergedCorrectPressure

SNESConvergedReasonViewFromOptions

SNESGetAlwaysComputesFinalResidual

SNESGetCheckJacobianDomainError

SNESGetSolutionUpdate

SNESKSPGetParametersEW

SNESKSPSetParametersEW

SNESLINESEARCHNCGLINEAR

SNESLINESEARCHNLEQERR

SNESLineSearchAppendOptionsPrefix

SNESLineSearchGetDamping

SNESLineSearchGetLambda

SNESLineSearchGetOptionsPrefix

SNESLineSearchGetVIFunctions

SNESLineSearchGetVecs

SNESLineSearchMonitorCancel

SNESLineSearchMonitorSetFromOptions

SNESLineSearchPreCheck

SNESLineSearchPreCheckPicard

SNESLineSearchRegister

SNESLineSearchRegisterAll

SNESLineSearchSetLambda

SNESLineSearchSetVIFunctions

SNESLineSearchShellGetApply

SNESLineSearchShellSetApply

SNESLineSearchVIDirDerivFn

SNESLineSearchVINormFn

SNESLineSearchVIProjectFn

SNESMonitorSetFromOptions

SNESMultiblockGetSubSNES

SNESMultiblockSetType

SNESNGMRESGetRestartFmRise

SNESNGMRESSetRestartFmRise

SNESObjectiveComputeFunctionDefaultFD

SNESPatchSetCellNumbering

SNESPatchSetComputeFunction

SNESPatchSetComputeOperator

SNESPatchSetConstructType

SNESPatchSetDiscretisationInfo

SNESSetAlwaysComputesFinalResidual

SNESSetCheckJacobianDomainError

SNESSetConvergenceTest

SNESSetFunctionDomainError

SNESSetJacobianDomainError

SNESSetLagJacobianPersists

SNESSetObjectiveDomainError

SNESVIGetVariableBounds

SNESVISetComputeVariableBounds

SNESVISetRedundancyCheck

SNESVISetVariableBounds

SNES_NORM_INITIAL_FINAL_ONLY

SNES_NORM_INITIAL_ONLY

DMPlexSNESComputeBoundaryFEM

DMPlexSNESComputeJacobianFEM

DMPlexSNESComputeObjectiveFEM

DMPlexSNESComputeResidualCEED

DMPlexSNESComputeResidualDS

DMPlexSNESComputeResidualFEM

DMPlexSetSNESLocalFEM

DMSNESCheckDiscretization

DMSNESCheckFromOptions

DMSNESComputeJacobianAction

DMSNESSetFunctionContextDestroy

DMSNESSetJacobianContextDestroy

MatMFFDComputeJacobian

PetscConvEstComputeError

PetscConvEstComputeInitialGuess

SNESAddOptionsChecker

SNESCheckFunctionDomainError

SNESCompositeGetNumber

SNESComputeFunctionDefaultNPC

SNESComputeMFFunction

SNESInitializePackage

SNESLineSearchApplyFn

SNESLineSearchDestroy

SNESLineSearchGetNorms

SNESLineSearchGetReason

SNESLineSearchGetSNES

SNESLineSearchMonitor

SNESLineSearchMonitorSolutionUpdate

SNESLineSearchPostCheck

SNESLineSearchSetFunction

SNESLineSearchSetNorms

SNESLineSearchSetReason

SNESLineSearchSetSNES

SNESLineSearchSetVecs

SNESLineSearchSetWorkVecs

SNESLineSearchShellApplyFn

SNESMSFinalizePackage

SNESMSInitializePackage

SNESMSRegisterDestroy

SNESMonitorDefaultSetUp

SNESMonitorSAWsCreate

SNESMonitorSAWsDestroy

SNESNASMGetSubdomainVecs

SNESNASMSetComputeFinalJacobian

SNESNewtonALComputeFunction

SNESNewtonTRDCGetRhoFlag

SNESNewtonTRDCPostCheck

SNESNewtonTRDCPreCheck

SNESParametersInitialize

SNESPicardComputeFunction

SNESPicardComputeJacobian

SNESPicardComputeMFFunction

SNESSetConvergedReason

SNESSetInitialFunction

SNESSetIterationNumber

SNESSetLagPreconditionerPersists

SNESVIComputeFunction

SNESVIComputeInactiveSetFnorm

SNESVIComputeInactiveSetFtY

SNESVIComputeMeritFunction

SNESSetTrustRegionTolerance

DMDASNESFunctionVecFn

DMDASNESJacobianVecFn

DMDASNESObjectiveVecFn

DMDASNESSetFunctionLocal

DMDASNESSetFunctionLocalVec

DMDASNESSetJacobianLocal

DMDASNESSetJacobianLocalVec

DMDASNESSetObjectiveLocal

DMDASNESSetObjectiveLocalVec

DMDASNESSetPicardLocal

DMPlexSNESComputeBoundaryFEM

DMPlexSNESComputeJacobianFEM

DMPlexSNESComputeObjectiveFEM

DMPlexSNESComputeResidualCEED

DMPlexSNESComputeResidualDS

DMPlexSNESComputeResidualFEM

DMPlexSetSNESLocalFEM

DMPlexSetSNESVariableBounds

DMSNESCheckDiscretization

DMSNESCheckFromOptions

DMSNESComputeJacobianAction

DMSNESCreateJacobianMF

DMSNESGetBoundaryLocal

DMSNESGetFunctionLocal

DMSNESGetJacobianLocal

DMSNESGetObjectiveLocal

DMSNESSetBoundaryLocal

DMSNESSetFunctionContextDestroy

DMSNESSetFunctionLocal

DMSNESSetJacobianContextDestroy

DMSNESSetJacobianLocal

DMSNESSetObjectiveLocal

KSPMonitorSNESResidual

KSPMonitorSNESResidualDrawLG

KSPMonitorSNESResidualDrawLGCreate

MatMFFDComputeJacobian

MatSNESMFGetReuseBase

MatSNESMFMoreSetParameters

MatSNESMFSetReuseBase

PetscConvEstComputeError

PetscConvEstComputeInitialGuess

PetscConvEstGetConvRate

PetscConvEstGetSolver

PetscConvEstMonitorDefault

PetscConvEstSetFromOptions

PetscConvEstSetSolver

SNESAddOptionsChecker

SNESAppendOptionsPrefix

SNESCheckFunctionDomainError

SNESCompositeGetNumber

SNESCompositeSetDamping

SNESComputeFunctionDefaultNPC

SNESComputeJacobianDefault

SNESComputeJacobianDefaultColor

SNESComputeMFFunction

SNESConvergedCorrectPressure

SNESConvergedReasonView

SNESConvergedReasonViewCancel

SNESConvergedReasonViewFromOptions

SNESConvergedReasonViewSet

SNESGetAlwaysComputesFinalResidual

SNESGetApplicationContext

SNESGetCheckJacobianDomainError

SNESGetConvergedReason

SNESGetConvergedReasonString

SNESGetConvergenceHistory

SNESGetDivergenceTolerance

SNESGetErrorIfNotConverged

SNESGetForceIteration

SNESGetIterationNumber

SNESGetLagPreconditioner

SNESGetLinearSolveFailures

SNESGetLinearSolveIterations

SNESGetMaxLinearSolveFailures

SNESGetMaxNonlinearStepFailures

SNESGetNonlinearStepFailures

SNESGetNumberFunctionEvals

SNESGetSolutionUpdate

SNESInitializePackage

SNESKSPGetParametersEW

SNESKSPSetParametersEW

SNESLINESEARCHBISECTION

SNESLINESEARCHNCGLINEAR

SNESLINESEARCHNLEQERR

SNESLineSearchAppendOptionsPrefix

SNESLineSearchApplyFn

SNESLineSearchBTGetAlpha

SNESLineSearchBTSetAlpha

SNESLineSearchComputeNorms

SNESLineSearchDestroy

SNESLineSearchGetDamping

SNESLineSearchGetDefaultMonitor

SNESLineSearchGetLambda

SNESLineSearchGetNorms

SNESLineSearchGetOptionsPrefix

SNESLineSearchGetOrder

SNESLineSearchGetPostCheck

SNESLineSearchGetPreCheck

SNESLineSearchGetReason

SNESLineSearchGetSNES

SNESLineSearchGetTolerances

SNESLineSearchGetType

SNESLineSearchGetVIFunctions

SNESLineSearchGetVecs

SNESLineSearchMonitor

SNESLineSearchMonitorCancel

SNESLineSearchMonitorSet

SNESLineSearchMonitorSetFromOptions

SNESLineSearchMonitorSolutionUpdate

SNESLineSearchPostCheck

SNESLineSearchPreCheck

SNESLineSearchPreCheckPicard

SNESLineSearchRegister

SNESLineSearchRegisterAll

SNESLineSearchSetComputeNorms

SNESLineSearchSetDamping

SNESLineSearchSetDefaultMonitor

SNESLineSearchSetFromOptions

SNESLineSearchSetFunction

SNESLineSearchSetLambda

SNESLineSearchSetNorms

SNESLineSearchSetOrder

SNESLineSearchSetPostCheck

SNESLineSearchSetPreCheck

SNESLineSearchSetReason

SNESLineSearchSetSNES

SNESLineSearchSetTolerances

SNESLineSearchSetType

SNESLineSearchSetVIFunctions

SNESLineSearchSetVecs

SNESLineSearchSetWorkVecs

SNESLineSearchShellApplyFn

SNESLineSearchShellGetApply

SNESLineSearchShellSetApply

SNESLineSearchVIDirDerivFn

SNESLineSearchVINormFn

SNESLineSearchVIProjectFn

SNESMSFinalizePackage

SNESMSInitializePackage

SNESMSRegisterDestroy

SNESMonitorDefaultField

SNESMonitorDefaultSetUp

SNESMonitorJacUpdateSpectrum

SNESMonitorRatioSetUp

SNESMonitorSAWsCreate

SNESMonitorSAWsDestroy

SNESMonitorSetFromOptions

SNESMonitorSolutionUpdate

SNESMultiblockGetSubSNES

SNESMultiblockSetBlockSize

SNESMultiblockSetFields

SNESMultiblockSetType

SNESNASMGetSubdomainVecs

SNESNASMGetSubdomains

SNESNASMSetComputeFinalJacobian

SNESNASMSetSubdomains

SNESNGMRESGetRestartFmRise

SNESNGMRESRestartType

SNESNGMRESSetRestartFmRise

SNESNGMRESSetRestartType

SNESNGMRESSetSelectType

SNESNewtonALComputeFunction

SNESNewtonALCorrectionType

SNESNewtonALGetFunction

SNESNewtonALGetLoadParameter

SNESNewtonALSetCorrectionType

SNESNewtonALSetDiagonalScaling

SNESNewtonALSetFunction

SNESNewtonTRDCGetPostCheck

SNESNewtonTRDCGetPreCheck

SNESNewtonTRDCGetRhoFlag

SNESNewtonTRDCPostCheck

SNESNewtonTRDCPreCheck

SNESNewtonTRDCSetPostCheck

SNESNewtonTRDCSetPreCheck

SNESNewtonTRFallbackType

SNESNewtonTRGetPostCheck

SNESNewtonTRGetPreCheck

SNESNewtonTRGetTolerances

SNESNewtonTRGetUpdateParameters

SNESNewtonTRPostCheck

SNESNewtonTRSetFallbackType

SNESNewtonTRSetNormType

SNESNewtonTRSetPostCheck

SNESNewtonTRSetPreCheck

SNESNewtonTRSetQNType

SNESNewtonTRSetTolerances

SNESNewtonTRSetUpdateParameters

SNESObjectiveComputeFunctionDefaultFD

SNESParametersInitialize

SNESPatchSetCellNumbering

SNESPatchSetComputeFunction

SNESPatchSetComputeOperator

SNESPatchSetConstructType

SNESPatchSetDiscretisationInfo

SNESPicardComputeFunction

SNESPicardComputeJacobian

SNESPicardComputeMFFunction

SNESPruneJacobianColor

SNESSetAlwaysComputesFinalResidual

SNESSetApplicationContext

SNESSetCheckJacobianDomainError

SNESSetComputeApplicationContext

SNESSetComputeInitialGuess

SNESSetConvergedReason

SNESSetConvergenceHistory

SNESSetConvergenceTest

SNESSetDivergenceTolerance

SNESSetErrorIfNotConverged

SNESSetForceIteration

SNESSetFunctionDomainError

SNESSetInitialFunction

SNESSetIterationNumber

SNESSetJacobianDomainError

SNESSetLagJacobianPersists

SNESSetLagPreconditioner

SNESSetLagPreconditionerPersists

SNESSetMaxLinearSolveFailures

SNESSetMaxNonlinearStepFailures

SNESSetObjectiveDomainError

SNESSetTrustRegionTolerance

SNESVIComputeFunction

SNESVIComputeInactiveSetFnorm

SNESVIComputeInactiveSetFtY

SNESVIComputeMeritFunction

SNESVIGetVariableBounds

SNESVISetComputeVariableBounds

SNESVISetRedundancyCheck

SNESVISetVariableBounds

SNES_CONERGED_ITERATING

SNES_CONVERGED_FNORM_ABS

SNES_CONVERGED_FNORM_RELATIVE

SNES_CONVERGED_SNORM_RELATIVE

SNES_DIVERGED_FUNCTION_COUNT

SNES_DIVERGED_FUNCTION_DOMAIN

SNES_DIVERGED_FUNCTION_NANORINF

SNES_DIVERGED_JACOBIAN_DOMAIN

SNES_DIVERGED_LINE_SEARCH

SNES_DIVERGED_LOCAL_MIN

SNES_DIVERGED_OBJECTIVE_DOMAIN

SNES_NORM_INITIAL_FINAL_ONLY

SNES_NORM_INITIAL_ONLY

Full Approximation Scheme (FAS) nonlinear multigrid

**Examples:**

Example 1 (unknown):
```unknown
SNESGetKSP()
```

---

## PetscConvEstComputeError#

**URL:** https://petsc.org/release/manualpages/SNES/PetscConvEstComputeError/

**Contents:**
- PetscConvEstComputeError#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Compute per-field discretization errors of u on refinement level r

ce - the PetscConvEst object

r - the refinement level

dm - the DM on which u is defined (may be NULL)

u - the computed solution

errors - array of length Nf (number of fields in the DS) filled with the error in each field

PetscConvEst, PetscConvEstComputeInitialGuess(), PetscConvEstGetConvRate()

src/snes/utils/convest.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscconvest.h" 
PetscErrorCode PetscConvEstComputeError(PetscConvEst ce, PetscInt r, DM dm, Vec u, PetscReal errors[])
```

Example 2 (unknown):
```unknown
PetscConvEst
```

Example 3 (unknown):
```unknown
PetscConvEst
```

Example 4 (unknown):
```unknown
PetscConvEstComputeInitialGuess()
```

---

## PetscConvEstComputeInitialGuess#

**URL:** https://petsc.org/release/manualpages/SNES/PetscConvEstComputeInitialGuess/

**Contents:**
- PetscConvEstComputeInitialGuess#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Fill u with the initial guess to use on refinement level r of a convergence-estimation run

ce - the PetscConvEst object

r - the refinement level

dm - the DM on which u is defined (may be NULL)

u - the initial-guess vector

PetscConvEst, PetscConvEstComputeError(), PetscConvEstGetConvRate()

src/snes/utils/convest.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscconvest.h" 
PetscErrorCode PetscConvEstComputeInitialGuess(PetscConvEst ce, PetscInt r, DM dm, Vec u)
```

Example 2 (unknown):
```unknown
PetscConvEst
```

Example 3 (unknown):
```unknown
PetscConvEst
```

Example 4 (unknown):
```unknown
PetscConvEstComputeError()
```

---

## PetscConvEstCreate#

**URL:** https://petsc.org/release/manualpages/SNES/PetscConvEstCreate/

**Contents:**
- PetscConvEstCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Create a PetscConvEst object. This is used to study the convergence rate of approximations on grids to a continuum solution

comm - The communicator for the PetscConvEst object

ce - The PetscConvEst object

PetscConvEst, PetscConvEstDestroy(), PetscConvEstGetConvRate(), DMAdaptorCreate(), DMAdaptor

src/snes/utils/convest.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscConvEst
```

Example 2 (unknown):
```unknown
#include "petscconvest.h" 
PetscErrorCode PetscConvEstCreate(MPI_Comm comm, PetscConvEst *ce)
```

Example 3 (unknown):
```unknown
PetscConvEst
```

Example 4 (unknown):
```unknown
PetscConvEst
```

---

## PetscConvEstDestroy#

**URL:** https://petsc.org/release/manualpages/SNES/PetscConvEstDestroy/

**Contents:**
- PetscConvEstDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Destroys a PETSc convergence estimator PetscConvEst object

ce - The PetscConvEst object

PetscConvEst, PetscConvEstCreate(), PetscConvEstGetConvRate()

src/snes/utils/convest.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscConvEst
```

Example 2 (unknown):
```unknown
#include "petscconvest.h" 
PetscErrorCode PetscConvEstDestroy(PetscConvEst *ce)
```

Example 3 (unknown):
```unknown
PetscConvEst
```

Example 4 (unknown):
```unknown
PetscConvEst
```

---

## PetscConvEstGetConvRate#

**URL:** https://petsc.org/release/manualpages/SNES/PetscConvEstGetConvRate/

**Contents:**
- PetscConvEstGetConvRate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#

Returns an estimate of the convergence rate for the discretization

ce - The PetscConvEst object

alpha - The convergence rate for each field

-snes_convergence_estimate - Execute convergence estimation inside SNESSolve() and print out the rate

-ts_convergence_estimate - Execute convergence estimation inside TSSolve() and print out the rate

The convergence rate alpha is defined by

where \(u_{\Delta} \) is the discrete solution, and \(\Delta\) is a measure of the discretization size. We usually use \(h\) for the spatial resolution and \(\Delta t \) for the temporal resolution.

We solve a series of problems using increasing resolution (refined meshes or decreased timesteps), calculate an error based upon the exact solution in the PetscDS, and then fit the result to our model above using linear regression.

PetscConvEstSetSolver(), PetscConvEstCreate(), SNESSolve(), TSSolve()

src/snes/utils/convest.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscconvest.h" 
PetscErrorCode PetscConvEstGetConvRate(PetscConvEst ce, PetscReal alpha[])
```

Example 2 (unknown):
```unknown
PetscConvEst
```

Example 3 (unknown):
```unknown
SNESSolve()
```

Example 4 (unknown):
```unknown
PetscConvEstSetSolver()
```

---

## PetscConvEstGetSolver#

**URL:** https://petsc.org/release/manualpages/SNES/PetscConvEstGetSolver/

**Contents:**
- PetscConvEstGetSolver#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the solver used to produce discrete solutions

ce - The PetscConvEst object

PetscConvEst, PetscConvEstSetSolver(), PetscConvEstCreate(), PetscConvEstGetConvRate()

src/snes/utils/convest.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscconvest.h" 
PetscErrorCode PetscConvEstGetSolver(PetscConvEst ce, PetscObject *solver)
```

Example 2 (unknown):
```unknown
PetscConvEst
```

Example 3 (unknown):
```unknown
PetscConvEst
```

Example 4 (unknown):
```unknown
PetscConvEstSetSolver()
```

---

## PetscConvEstMonitorDefault#

**URL:** https://petsc.org/release/manualpages/SNES/PetscConvEstMonitorDefault/

**Contents:**
- PetscConvEstMonitorDefault#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Monitors the convergence estimation loop

ce - The PetscConvEst object

r - The refinement level

-convest_monitor - Activate the monitor

PetscConvEst, PetscConvEstCreate(), PetscConvEstGetConvRate(), SNESSolve(), TSSolve()

src/snes/utils/convest.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscconvest.h" 
PetscErrorCode PetscConvEstMonitorDefault(PetscConvEst ce, PetscInt r)
```

Example 2 (unknown):
```unknown
PetscConvEst
```

Example 3 (unknown):
```unknown
PetscConvEst
```

Example 4 (unknown):
```unknown
PetscConvEstCreate()
```

---

## PetscConvEstRateView#

**URL:** https://petsc.org/release/manualpages/SNES/PetscConvEstRateView/

**Contents:**
- PetscConvEstRateView#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Displays the convergence rate obtained from PetscConvEstGetConvRate() using a PetscViewer

ce - iterative context obtained from SNESCreate()

alpha - the convergence rate for each field

viewer - the viewer to display the reason

-snes_convergence_estimate - print the convergence rate

PetscConvEst, PetscConvEstGetConvRate()

src/snes/utils/convest.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscConvEstGetConvRate()
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
#include "petscconvest.h" 
PetscErrorCode PetscConvEstRateView(PetscConvEst ce, const PetscReal alpha[], PetscViewer viewer)
```

Example 4 (unknown):
```unknown
SNESCreate()
```

---

## PetscConvEstSetFromOptions#

**URL:** https://petsc.org/release/manualpages/SNES/PetscConvEstSetFromOptions/

**Contents:**
- PetscConvEstSetFromOptions#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Sets a convergence estimator PetscConvEst object based on values in the options database

ce - The PetscConvEst object

PetscConvEst, PetscConvEstCreate(), PetscConvEstGetConvRate()

src/snes/utils/convest.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscConvEst
```

Example 2 (unknown):
```unknown
#include "petscconvest.h" 
PetscErrorCode PetscConvEstSetFromOptions(PetscConvEst ce)
```

Example 3 (unknown):
```unknown
PetscConvEst
```

Example 4 (unknown):
```unknown
PetscConvEst
```

---

## PetscConvEstSetSolver#

**URL:** https://petsc.org/release/manualpages/SNES/PetscConvEstSetSolver/

**Contents:**
- PetscConvEstSetSolver#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the solver used to produce discrete solutions

ce - The PetscConvEst object

solver - The solver, must be a KSP, SNES, or TS object with an attached DM/DS, that can compute an exact solution

PetscConvEst, PetscConvEstGetSNES(), PetscConvEstCreate(), PetscConvEstGetConvRate()

src/snes/utils/convest.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscconvest.h" 
PetscErrorCode PetscConvEstSetSolver(PetscConvEst ce, PetscObject solver)
```

Example 2 (unknown):
```unknown
PetscConvEst
```

Example 3 (unknown):
```unknown
PetscConvEst
```

Example 4 (unknown):
```unknown
PetscConvEstGetSNES()
```

---

## PetscConvEstSetUp#

**URL:** https://petsc.org/release/manualpages/SNES/PetscConvEstSetUp/

**Contents:**
- PetscConvEstSetUp#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

After the solver is specified, create data structures needed for estimating convergence

ce - The PetscConvEst object

PetscConvEst, PetscConvEstCreate(), PetscConvEstGetConvRate()

src/snes/utils/convest.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscconvest.h" 
PetscErrorCode PetscConvEstSetUp(PetscConvEst ce)
```

Example 2 (unknown):
```unknown
PetscConvEst
```

Example 3 (unknown):
```unknown
PetscConvEst
```

Example 4 (unknown):
```unknown
PetscConvEstCreate()
```

---

## PetscConvEstView#

**URL:** https://petsc.org/release/manualpages/SNES/PetscConvEstView/

**Contents:**
- PetscConvEstView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Views a PetscConvEst object

ce - The PetscConvEst object

viewer - The PetscViewer

PetscConvEst, PetscViewer, PetscConvEstCreate(), PetscConvEstGetConvRate()

src/snes/utils/convest.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscConvEst
```

Example 2 (unknown):
```unknown
#include "petscconvest.h" 
PetscErrorCode PetscConvEstView(PetscConvEst ce, PetscViewer viewer)
```

Example 3 (unknown):
```unknown
PetscConvEst
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscConvEst#

**URL:** https://petsc.org/release/manualpages/SNES/PetscConvEst/

**Contents:**
- PetscConvEst#
- Synopsis#
- See Also#
- Level#
- Location#
- Implementations#

Object that manages convergence rate estimates for a discretized problem

PetscConvEstCreate(), PetscConvEstDestroy(), PetscConvEstView(), PetscConvEstSetFromOptions(), PetscConvEstGetSolver(), PetscConvEstSetSolver(), PetscConvEstSetUp(), PetscConvEstComputeInitialGuess(), PetscConvEstComputeError(), PetscConvEstGetConvRate(), PetscConvEstMonitorDefault(), PetscConvEstRateView()

include/petscconvest.h

_p_PetscConvEst in include/petsc/private/petscconvestimpl.h

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_PetscConvEst *PetscConvEst;
```

Example 2 (unknown):
```unknown
PetscConvEstCreate()
```

Example 3 (unknown):
```unknown
PetscConvEstDestroy()
```

Example 4 (unknown):
```unknown
PetscConvEstView()
```

---

## SNESAddOptionsChecker#

**URL:** https://petsc.org/release/manualpages/SNES/SNESAddOptionsChecker/

**Contents:**
- SNESAddOptionsChecker#
- Synopsis#
- Input Parameter#
- Calling sequence of snescheck#
- See Also#
- Level#
- Location#

Adds an additional function to check for SNES options.

snescheck - function that checks for options

snes - the SNES object for which it is checking options

SNES: Nonlinear Solvers, SNES, SNESSetFromOptions()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESAddOptionsChecker(PetscErrorCode (*snescheck)(SNES snes))
```

Example 2 (unknown):
```unknown
SNESSetFromOptions()
```

---

## SNESANDERSON#

**URL:** https://petsc.org/release/manualpages/SNES/SNESANDERSON/

**Contents:**
- SNESANDERSON#
- Options Database Keys#
- Notes#
- References#
- See Also#
- Level#
- Location#

Implements the Anderson Mixing nonlinear solver [And65], [BKST15]

-snes_anderson_m m - Number of stored previous solutions and residuals

-snes_anderson_beta beta - Anderson mixing parameter

-snes_anderson_restart_type type - Type of restart (see SNESNGMRES)

-snes_anderson_restart_it its - Number of iterations of restart conditions before restart

-snes_anderson_restart restart - Number of iterations before periodic restart

-snes_anderson_monitor - Prints relevant information about the Anderson mixing iteration

The Anderson Mixing method combines m previous solutions into a minimum-residual solution by solving a small linearized optimization problem at each iteration.

Very similar to the SNESNGMRES algorithm.

This algorithm ignores any Jacobian provided with SNESSetJacobian()

Only supports left non-linear preconditioning.

Donald G Anderson. Iterative procedures for nonlinear integral equations. Journal of the ACM (JACM), 12(4):547–560, 1965.

Peter R. Brune, Matthew G. Knepley, Barry F. Smith, and Xuemin Tu. Composing scalable nonlinear algebraic solvers. SIAM Review, 57(4):535–565, 2015. http://www.mcs.anl.gov/papers/P2010-0112.pdf. URL: http://www.mcs.anl.gov/papers/P2010-0112.pdf, doi:10.1137/130936725.

SNES: Nonlinear Solvers, SNESNGMRES, SNESCreate(), SNES, SNESSetType(), SNESType

src/snes/impls/ngmres/anderson.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetJacobian()
```

Example 2 (unknown):
```unknown
SNESCreate()
```

Example 3 (unknown):
```unknown
SNESSetType()
```

---

## SNESAppendOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/SNES/SNESAppendOptionsPrefix/

**Contents:**
- SNESAppendOptionsPrefix#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Appends to the prefix used for searching for all SNES options in the database.

snes - the SNES context

prefix - the prefix to prepend to all option names

A hyphen (-) must NOT be given at the beginning of the prefix name. The first character of all runtime options is AUTOMATICALLY the hyphen.

SNES: Nonlinear Solvers, SNESGetOptionsPrefix(), SNESSetOptionsPrefix()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESAppendOptionsPrefix(SNES snes, const char prefix[])
```

Example 2 (unknown):
```unknown
SNESGetOptionsPrefix()
```

Example 3 (unknown):
```unknown
SNESSetOptionsPrefix()
```

---

## SNESApplyNPC#

**URL:** https://petsc.org/release/manualpages/SNES/SNESApplyNPC/

**Contents:**
- SNESApplyNPC#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Calls SNESSolve() on the preconditioner for the SNES

snes - the SNES context

f - optional; the function evaluation on x

y - function vector, as set by SNESSetFunction()

SNESComputeFunction() should be called on x before SNESApplyNPC() is called, as it is with SNESComuteJacobian().

SNES: Nonlinear Solvers, SNES, SNESGetNPC(), SNESSetNPC(), SNESComputeFunction()

src/snes/interface/snespc.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESApplyNPC(SNES snes, Vec x, Vec f, Vec y)
```

Example 3 (unknown):
```unknown
SNESSetFunction()
```

Example 4 (unknown):
```unknown
SNESComputeFunction()
```

---

## SNESASPIN#

**URL:** https://petsc.org/release/manualpages/SNES/SNESASPIN/

**Contents:**
- SNESASPIN#
- Options Database Keys#
- Notes#
- References#
- See Also#
- Level#
- Location#

Helper SNES type for Additive-Schwarz Preconditioned Inexact Newton [CK02], [BKST15]

-npc_snes_ - options prefix of the nonlinear subdomain solver (must be of type NASM)

-npc_sub_snes_ - options prefix of the subdomain nonlinear solves

-npc_sub_ksp_ - options prefix of the subdomain Krylov solver

-npc_sub_pc_ - options prefix of the subdomain preconditioner

This solver transform the given nonlinear problem to a new form and then runs matrix-free Newton-Krylov with no preconditioner on that transformed problem.

This routine sets up an instance of SNESNETWONLS with nonlinear left preconditioning. It differs from other similar functionality in SNES as it creates a linear shell matrix that corresponds to the product

which is the ASPIN preconditioned matrix. Similar solvers may be constructed by having matrix-free differencing of nonlinear solves per linear iteration, but this is far more efficient when subdomain sparse-direct preconditioner factorizations are reused on each application of \(J_b^{-1}\).

The Krylov method used in this nonlinear solver is run with NO preconditioner, because the preconditioning is done at the nonlinear level, but the Jacobian for the original function must be provided (or calculated via coloring and finite differences automatically) in the Pmat location of SNESSetJacobian() because the action of the original Jacobian is needed by the shell matrix used to apply the Jacobian of the nonlinear preconditioned problem (see above). Note that since the Pmat is not used to construct a preconditioner it could be provided in a matrix-free form. The code for this implementation is a bit confusing because the Amat of SNESSetJacobian() applies the Jacobian of the nonlinearly preconditioned function Jacobian while the Pmat provides the Jacobian of the original user provided function. Note that the original SNES and nonlinear preconditioner (see SNESGetNPC()), in this case SNESNASM, share the same Jacobian matrices. SNESNASM computes the needed Jacobian in SNESNASMComputeFinalJacobian_Private().

Peter R. Brune, Matthew G. Knepley, Barry F. Smith, and Xuemin Tu. Composing scalable nonlinear algebraic solvers. SIAM Review, 57(4):535–565, 2015. http://www.mcs.anl.gov/papers/P2010-0112.pdf. URL: http://www.mcs.anl.gov/papers/P2010-0112.pdf, doi:10.1137/130936725.

X.-C. Cai and D. E. Keyes. Nonlinearly preconditioned inexact Newton algorithms. SIAM J. Sci. Comput., 24:183–200, 2002. URL: http://www.cs.colorado.edu/homes/cai/public_html/papers/aspin.ps.

SNES: Nonlinear Solvers, SNESCreate(), SNES, SNESSetType(), SNESNEWTONLS, SNESNASM, SNESGetNPC(), SNESGetNPCSide()

src/snes/impls/nasm/aspin.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESNETWONLS
```

Example 2 (unknown):
```unknown
SNESSetJacobian()
```

Example 3 (unknown):
```unknown
SNESSetJacobian()
```

Example 4 (unknown):
```unknown
SNESGetNPC()
```

---

## SNESCheckFunctionDomainError#

**URL:** https://petsc.org/release/manualpages/SNES/SNESCheckFunctionDomainError/

**Contents:**
- SNESCheckFunctionDomainError#
- Synopsis#
- Input Parameters#
- Notes#
- Developer Note#
- See Also#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#

Called after a SNESComputeFunction() and VecNorm() in a SNES solver to check if the function norm is infinity or NaN and if the function callback set with SNESSetFunction() called SNESSetFunctionDomainError().

snes - the SNES solver object

fnorm - the value of the norm

If fnorm is infinity or NaN and SNESSetErrorIfNotConverged() was set, this immediately generates a PETSC_ERR_CONV_FAILED.

If fnorm is infinity or NaN and SNESSetFunctionDomainError() was called, this sets the SNESConvergedReason to SNES_DIVERGED_FUNCTION_DOMAIN and exits the solver

Otherwise if fnorm is infinity or NaN, this sets the SNESConvergedReason to SNES_DIVERGED_FUNCTION_NANORINF and exits the solver

This function exists so that SNESSetFunctionDomainError() does not need to be a collective operation since making it collective would be cumbersome in most applications and require extra communication. Instead, SNESSetFunctionDomainError() sets the functiondomainerror flag in the SNES object to true, SNESComputeFunction() checks that flag and sets a NaN into its local part of the vector if the flag has been set. Then, when VecNorm() is called on the vector containing the computed function value, any NaN is propagated to all MPI processes without any additional communication. Virtually all nonlinear solvers need to compute the function norm at some point so no extra communication needs to take place.

SNES: Nonlinear Solvers, SNESSetFunctionDomainError(), SNESCheckObjectiveDomainError(), PETSC_ERR_CONV_FAILED, SNESSetErrorIfNotConverged(), SNES_DIVERGED_FUNCTION_DOMAIN, SNESConvergedReason, SNES_DIVERGED_FUNCTION_NAN MC*/ #define SNESCheckFunctionDomainError(snes, fnorm) do { if (PetscIsInfOrNanReal(fnorm)) { PetscCheck(!snes->errorifnotconverged, PetscObjectComm((PetscObject)snes), PETSC_ERR_NOT_CONVERGED, “SNESSolve has not converged due to infinity or NaN norm”); { PetscBool domainerror; PetscCallMPI(MPIU_Allreduce(&snes->functiondomainerror, &domainerror, 1, MPI_C_BOOL, MPI_LOR, PetscObjectComm((PetscObject)snes))); if (domainerror) snes->reason = SNES_DIVERGED_FUNCTION_DOMAIN; else snes->reason = SNES_DIVERGED_FUNCTION_NANORINF; PetscFunctionReturn(PETSC_SUCCESS); } } } while (0)

/*MC SNESCheckObjectiveDomainError - Called after a SNESComputeObjective() in a SNES solver to check if the objective value is infinity or NaN and/or if the function callback set with SNESSetObjective() called SNESSetObjectiveDomainError().

snes - the SNES solver object

fobj - the value of the objective function

If fobj is infinity or NaN and SNESSetErrorIfNotConverged() was set, this immediately generates a PETSC_ERR_CONV_FAILED.

If SNESSetObjectiveDomainError() was called, this sets the SNESConvergedReason to SNES_DIVERGED_OBJECTIVE_DOMAIN and exits the solver

Otherwise if fobj is infinity or NaN, this sets the SNESConvergedReason to SNES_DIVERGED_OBJECTIVE_NANORINF and exits the solver

SNES: Nonlinear Solvers, SNESSetObjectiveDomainError(), PETSC_ERR_CONV_FAILED, SNESSetErrorIfNotConverged(), SNES_DIVERGED_OBJECTIVE_DOMAIN, SNES_DIVERGED_FUNCTION_DOMAIN, SNESSetFunctionDomainError(), SNESConvergedReason, SNES_DIVERGED_OBJECTIVE_NANORINF, SNES_DIVERGED_FUNCTION_NAN, SNESLineSearchCheckObjectiveDomainError() MC*/ #define SNESCheckObjectiveDomainError(snes, fobj) do { if (snes->errorifnotconverged) { PetscCheck(!snes->objectivedomainerror, PetscObjectComm((PetscObject)snes), PETSC_ERR_NOT_CONVERGED, “SNESSolve has not converged due objective domain error”); PetscCheck(!PetscIsInfOrNanReal(fobj), PetscObjectComm((PetscObject)snes), PETSC_ERR_NOT_CONVERGED, “SNESSolve has not converged due to infinity or NaN norm”); } if (snes->objectivedomainerror) { snes->reason = SNES_DIVERGED_OBJECTIVE_DOMAIN; PetscFunctionReturn(PETSC_SUCCESS); } else if (PetscIsInfOrNanReal(fobj)) { snes->reason = SNES_DIVERGED_OBJECTIVE_NANORINF; PetscFunctionReturn(PETSC_SUCCESS); } } while (0)

/*MC SNESCheckJacobianDomainError - Called after a SNESComputeJacobian() in a SNES solver to check if SNESSetJacobianDomainError() has been called.

snes - the SNES solver object

This turns the non-collective SNESSetJacobianDomainError() into a collective operation

This check is done in debug mode or if SNESSetCheckJacobianDomainError() has been called

SNES: Nonlinear Solvers, SNESSetCheckJacobianDomainError(), SNESCheckObjectiveDomainError(), SNESSetFunctionDomainError(), PETSC_ERR_CONV_FAILED, SNESSetErrorIfNotConverged(), SNES_DIVERGED_FUNCTION_DOMAIN, SNESConvergedReason, SNES_DIVERGED_FUNCTION_NAN MC*/ #define SNESCheckJacobianDomainError(snes) do { if (snes->checkjacdomainerror) { PetscBool domainerror; PetscCallMPI(MPIU_Allreduce(&snes->jacobiandomainerror, &domainerror, 1, MPI_C_BOOL, MPI_LOR, PetscObjectComm((PetscObject)snes))); if (domainerror) { snes->reason = SNES_DIVERGED_JACOBIAN_DOMAIN; PetscCheck(!snes->errorifnotconverged, PetscObjectComm((PetscObject)snes), PETSC_ERR_NOT_CONVERGED, “SNESSolve has not converged due to Jacobian domain error”); PetscFunctionReturn(PETSC_SUCCESS); } } } while (0)

/*MC SNESCheckLineSearchFailure - Checks if a SNESLineSearchApply() has failed and possibly ends the current SNESSolve() if so

snes - the SNES solver object

If SNESLineSearchApply() produces a SNES_LINESEARCH_FAILED_NANORINF or SNES_LINESEARCH_FAILED_NANORINF the SNESSolve() is ended.

If the SNESLineSearchApply() produces any other failure reason and the number of failed steps is greater than the number set with SNESSetMaxNonlinearStepFailures() the SNESSolve() is ended

SNES: Nonlinear Solvers, SNESLineSearchApply(), SNESSetFunctionDomainError(), PETSC_ERR_CONV_FAILED, SNESSetErrorIfNotConverged(), SNES_DIVERGED_FUNCTION_DOMAIN, SNESConvergedReason, SNES_DIVERGED_FUNCTION_NAN, SNESSolve(), SNESSetMaxNonlinearStepFailures() MC*/ #define SNESCheckLineSearchFailure(snes) do { SNESLineSearchReason lsreason; PetscCall(SNESLineSearchGetReason(snes->linesearch, &lsreason)); if (lsreason) { if (lsreason == SNES_LINESEARCH_FAILED_FUNCTION_DOMAIN) { PetscCheck(!snes->errorifnotconverged, PetscObjectComm((PetscObject)snes), PETSC_ERR_NOT_CONVERGED, “SNESLineSearchApply() has produced failure with function domain”); snes->reason = SNES_DIVERGED_FUNCTION_DOMAIN; PetscFunctionReturn(PETSC_SUCCESS); } if (lsreason == SNES_LINESEARCH_FAILED_NANORINF) { PetscCheck(!snes->errorifnotconverged, PetscObjectComm((PetscObject)snes), PETSC_ERR_NOT_CONVERGED, “SNESLineSearchApply() has produced failure with infinity or NaN”); snes->reason = SNES_DIVERGED_FUNCTION_NANORINF; PetscFunctionReturn(PETSC_SUCCESS); } if (lsreason == SNES_LINESEARCH_FAILED_OBJECTIVE_DOMAIN) { PetscCheck(!snes->errorifnotconverged, PetscObjectComm((PetscObject)snes), PETSC_ERR_NOT_CONVERGED, “SNESLineSearchApply() has produced failure with objective function domain”); snes->reason = SNES_DIVERGED_FUNCTION_DOMAIN; PetscFunctionReturn(PETSC_SUCCESS); } if (lsreason == SNES_LINESEARCH_FAILED_JACOBIAN_DOMAIN) { PetscCheck(!snes->errorifnotconverged, PetscObjectComm((PetscObject)snes), PETSC_ERR_NOT_CONVERGED, “SNESLineSearchApply() has produced failure with Jacobian domain”); snes->reason = SNES_DIVERGED_JACOBIAN_DOMAIN; PetscFunctionReturn(PETSC_SUCCESS); } if (++snes->numFailures >= snes->maxFailures) { PetscCheck(!snes->errorifnotconverged, PetscObjectComm((PetscObject)snes), PETSC_ERR_NOT_CONVERGED, “SNESLineSearchApply() has produced failure”); snes->reason = SNES_DIVERGED_LINE_SEARCH; PetscFunctionReturn(PETSC_SUCCESS); } } } while (0)

#define SNESCheckKSPSolve(snes) do { KSPConvergedReason kspreason; PetscInt lits; PetscCall(KSPGetIterationNumber(snes->ksp, &lits)); snes->linear_its += lits; PetscCall(KSPGetConvergedReason(snes->ksp, &kspreason)); if (kspreason < 0) { if (kspreason == KSP_DIVERGED_NANORINF) { PetscBool domainerror; PetscCallMPI(MPIU_Allreduce(&snes->functiondomainerror, &domainerror, 1, MPI_C_BOOL, MPI_LOR, PetscObjectComm((PetscObject)snes))); if (domainerror) { snes->reason = SNES_DIVERGED_FUNCTION_DOMAIN; snes->functiondomainerror = PETSC_FALSE; } else snes->reason = SNES_DIVERGED_LINEAR_SOLVE; PetscFunctionReturn(PETSC_SUCCESS); } else { if (++snes->numLinearSolveFailures >= snes->maxLinearSolveFailures) { PetscCall(PetscInfo(snes, “iter=%” PetscInt_FMT “, number linear solve failures %” PetscInt_FMT “ greater than current SNES allowed %” PetscInt_FMT “, stopping solve\n”, snes->iter, snes->numLinearSolveFailures, snes->maxLinearSolveFailures)); snes->reason = SNES_DIVERGED_LINEAR_SOLVE; PetscFunctionReturn(PETSC_SUCCESS); } } } } while (0)

#define SNESNeedNorm_Private(snes, iter) (((iter) == (snes)->max_its && ((snes)->normschedule == SNES_NORM_FINAL_ONLY || (snes)->normschedule == SNES_NORM_INITIAL_FINAL_ONLY)) || ((iter) == 0 && ((snes)->normschedule == SNES_NORM_INITIAL_ONLY || (snes)->normschedule == SNES_NORM_INITIAL_FINAL_ONLY)) || (snes)->normschedule == SNES_NORM_ALWAYS)

include/petsc/private/snesimpl.h

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESComputeFunction()
```

Example 2 (unknown):
```unknown
SNESSetFunction()
```

Example 3 (unknown):
```unknown
SNESSetFunctionDomainError()
```

Example 4 (cpp):
```cpp
#include <snesimpl.h>
void SNESCheckFunctionDomainError(SNES snes, PetscReal fnorm)
```

---

## SNESCompositeAddSNES#

**URL:** https://petsc.org/release/manualpages/SNES/SNESCompositeAddSNES/

**Contents:**
- SNESCompositeAddSNES#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Adds another SNES to the SNESCOMPOSITE

snes - the SNES context of type SNESCOMPOSITE

type - the SNESType of the new solver

SNES: Nonlinear Solvers, SNES, SNESCOMPOSITE, SNESCompositeGetSNES()

src/snes/impls/composite/snescomposite.c

SNESCompositeAddSNES_Composite() in src/snes/impls/composite/snescomposite.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESCOMPOSITE
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESCompositeAddSNES(SNES snes, SNESType type)
```

Example 3 (unknown):
```unknown
SNESCOMPOSITE
```

Example 4 (unknown):
```unknown
SNESCOMPOSITE
```

---

## SNESCompositeGetNumber#

**URL:** https://petsc.org/release/manualpages/SNES/SNESCompositeGetNumber/

**Contents:**
- SNESCompositeGetNumber#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the number of subsolvers in the SNESCOMPOSITE

snes - the SNES context

n - the number of subsolvers

SNES: Nonlinear Solvers, SNES, SNESCOMPOSITE, SNESCompositeAddSNES(), SNESCompositeGetSNES()

src/snes/impls/composite/snescomposite.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESCOMPOSITE
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESCompositeGetNumber(SNES snes, PetscInt *n)
```

Example 3 (unknown):
```unknown
SNESCOMPOSITE
```

Example 4 (unknown):
```unknown
SNESCompositeAddSNES()
```

---

## SNESCompositeGetSNES#

**URL:** https://petsc.org/release/manualpages/SNES/SNESCompositeGetSNES/

**Contents:**
- SNESCompositeGetSNES#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Gets one of the SNES objects in the SNES of SNESType SNESCOMPOSITE

snes - the SNES context

n - the number of the composed SNES requested

subsnes - the SNES requested

SNES: Nonlinear Solvers, SNES, SNESCOMPOSITE, SNESCompositeAddSNES(), SNESCompositeGetNumber()

src/snes/impls/composite/snescomposite.c

SNESCompositeGetSNES_Composite() in src/snes/impls/composite/snescomposite.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESCOMPOSITE
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESCompositeGetSNES(SNES snes, PetscInt n, SNES *subsnes)
```

Example 3 (unknown):
```unknown
SNESCOMPOSITE
```

Example 4 (unknown):
```unknown
SNESCompositeAddSNES()
```

---

## SNESCompositeSetDamping#

**URL:** https://petsc.org/release/manualpages/SNES/SNESCompositeSetDamping/

**Contents:**
- SNESCompositeSetDamping#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Sets the damping of a subsolver when using SNES_COMPOSITE_ADDITIVE with a SNES of SNESType SNESCOMPOSITE

snes - the SNES context

n - the number of the sub-SNES object requested

SNES: Nonlinear Solvers, SNES, SNESCOMPOSITE, SNESCompositeAddSNES(), SNESCompositeGetSNES(), SNES_COMPOSITE_ADDITIVE, SNES_COMPOSITE_MULTIPLICATIVE, SNESCompositeType, SNESCompositeSetType()

src/snes/impls/composite/snescomposite.c

SNESCompositeSetDamping_Composite() in src/snes/impls/composite/snescomposite.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNES_COMPOSITE_ADDITIVE
```

Example 2 (unknown):
```unknown
SNESCOMPOSITE
```

Example 3 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESCompositeSetDamping(SNES snes, PetscInt n, PetscReal dmp)
```

Example 4 (unknown):
```unknown
SNESCOMPOSITE
```

---

## SNESCompositeSetType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESCompositeSetType/

**Contents:**
- SNESCompositeSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

Sets the type of composite preconditioner.

snes - the preconditioner context

type - SNES_COMPOSITE_ADDITIVE (default), SNES_COMPOSITE_MULTIPLICATIVE, or SNES_COMPOSITE_ADDITIVEOPTIMAL

-snes_composite_type (multiplicative|additive|additive_optimal) - Sets composite preconditioner type

SNES: Nonlinear Solvers, SNES_COMPOSITE_ADDITIVE, SNES_COMPOSITE_MULTIPLICATIVE, SNESCompositeType, SNESCOMPOSITE, SNES_COMPOSITE_ADDITIVEOPTIMAL, PCCompositeType

src/snes/impls/composite/snescomposite.c

SNESCompositeSetType_Composite() in src/snes/impls/composite/snescomposite.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESCompositeSetType(SNES snes, SNESCompositeType type)
```

Example 2 (unknown):
```unknown
SNES_COMPOSITE_ADDITIVE
```

Example 3 (unknown):
```unknown
SNES_COMPOSITE_MULTIPLICATIVE
```

Example 4 (unknown):
```unknown
SNES_COMPOSITE_ADDITIVEOPTIMAL
```

---

## SNESCompositeType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESCompositeType/

**Contents:**
- SNESCompositeType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Determines how two or more preconditioners are composed with the SNESType of SNESCOMPOSITE

SNES_COMPOSITE_ADDITIVE - results from application of all preconditioners are added together

SNES_COMPOSITE_MULTIPLICATIVE - preconditioners are applied sequentially to the residual freshly computed after the previous preconditioner application

SNES_COMPOSITE_ADDITIVEOPTIMAL - uses a linear combination of the solutions obtained with each preconditioner that approximately minimize the function value at the new iteration.

Preconditioners, PCCOMPOSITE, PCFIELDSPLIT, PC, PCCompositeSetType(), PCCompositeType

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESCOMPOSITE
```

Example 2 (unknown):
```unknown
typedef enum {
  SNES_COMPOSITE_ADDITIVE,
  SNES_COMPOSITE_MULTIPLICATIVE,
  SNES_COMPOSITE_ADDITIVEOPTIMAL
} SNESCompositeType;
```

Example 3 (unknown):
```unknown
SNES_COMPOSITE_ADDITIVE
```

Example 4 (unknown):
```unknown
SNES_COMPOSITE_MULTIPLICATIVE
```

---

## SNESCOMPOSITE#

**URL:** https://petsc.org/release/manualpages/SNES/SNESCOMPOSITE/

**Contents:**
- SNESCOMPOSITE#
- Options Database Keys#
- References#
- See Also#
- Level#
- Location#

Builds a nonlinear solver/preconditioner by composing together several SNES nonlinear solvers [BKST15]

-snes_composite_type (multiplicative|additive|additiveoptimal) - Sets composite preconditioner type

-snes_composite_sneses snes0,snes1,… - list of SNES to compose

Peter R. Brune, Matthew G. Knepley, Barry F. Smith, and Xuemin Tu. Composing scalable nonlinear algebraic solvers. SIAM Review, 57(4):535–565, 2015. http://www.mcs.anl.gov/papers/P2010-0112.pdf. URL: http://www.mcs.anl.gov/papers/P2010-0112.pdf, doi:10.1137/130936725.

SNES: Nonlinear Solvers, SNES, SNESCOMPOSITE, SNESCompositeAddSNES(), SNESCompositeGetSNES(), SNES_COMPOSITE_ADDITIVE, SNES_COMPOSITE_ADDITIVEOPTIMAL, SNES_COMPOSITE_MULTIPLICATIVE, SNESCompositeType, SNESCompositeSetType(), SNESCompositeSetDamping(), SNESCompositeGetNumber(), PCCompositeType

src/snes/impls/composite/snescomposite.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESCOMPOSITE
```

Example 2 (unknown):
```unknown
SNESCompositeAddSNES()
```

Example 3 (unknown):
```unknown
SNESCompositeGetSNES()
```

Example 4 (unknown):
```unknown
SNES_COMPOSITE_ADDITIVE
```

---

## SNESComputeFunctionDefaultNPC#

**URL:** https://petsc.org/release/manualpages/SNES/SNESComputeFunctionDefaultNPC/

**Contents:**
- SNESComputeFunctionDefaultNPC#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Compute the residual by applying the attached nonlinear preconditioner when one is present, otherwise defer to SNESComputeFunction()

snes - the SNES context

X - the current iterate

F - the residual vector produced by the nonlinear preconditioner (or the standard function evaluation)

Used as the residual callback for SNESMF when a nonlinear preconditioner is set on the outer SNES.

SNES: Nonlinear Solvers, SNES, SNESSetNPC(), SNESApplyNPC(), SNESComputeFunction(), SNESGetNPCFunction()

src/snes/interface/snespc.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESComputeFunction()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESComputeFunctionDefaultNPC(SNES snes, Vec X, Vec F)
```

Example 3 (unknown):
```unknown
SNESSetNPC()
```

Example 4 (unknown):
```unknown
SNESApplyNPC()
```

---

## SNESComputeFunction#

**URL:** https://petsc.org/release/manualpages/SNES/SNESComputeFunction/

**Contents:**
- SNESComputeFunction#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Calls the function that has been set with SNESSetFunction().

snes - the SNES context

f - function vector, as set by SNESSetFunction()

SNESComputeFunction() is typically used within nonlinear solvers implementations, so users would not generally call this routine themselves.

When solving for \(F(x) = b\), this routine computes \(f = F(x) - b\).

This function usually appears in the pattern.

to collectively handle the use of SNESSetFunctionDomainError() in the provided callback function.

SNES: Nonlinear Solvers, SNES, SNESSetFunction(), SNESGetFunction(), SNESComputeMFFunction(), SNESSetFunctionDomainError()

src/snes/interface/snes.c

src/snes/tutorials/ex73f90t.F90 src/snes/tutorials/ex77.c src/snes/tutorials/ex1f.F90 src/snes/tutorials/ex12.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetFunction()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESComputeFunction(SNES snes, Vec x, Vec f)
```

Example 3 (unknown):
```unknown
SNESSetFunction()
```

Example 4 (unknown):
```unknown
SNESComputeFunction()
```

---

## SNESComputeJacobianDefaultColor#

**URL:** https://petsc.org/release/manualpages/SNES/SNESComputeJacobianDefaultColor/

**Contents:**
- SNESComputeJacobianDefaultColor#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Options Database Keys#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#

Computes the Jacobian using finite differences and coloring to exploit matrix sparsity.

snes - nonlinear solver object

x1 - location at which to evaluate Jacobian

ctx - MatFDColoring context or NULL

J - Jacobian matrix (not altered in this routine)

B - newly computed Jacobian matrix to use with preconditioner (generally the same as J)

-snes_fd_color_use_mat - use a matrix coloring from the explicit matrix nonzero pattern instead of from the DM providing the matrix

-snes_fd_color - Activates SNESComputeJacobianDefaultColor() in SNESSetFromOptions()

-mat_fd_coloring_err err - Sets err (square root of relative error in the function)

-mat_fd_coloring_umin umin - Sets umin, the minimum allowable u-value magnitude

-mat_fd_type - Either wp or ds (see MATMFFD_WP or MATMFFD_DS)

-snes_mf_operator - Use matrix-free application of Jacobian

-snes_mf - Use matrix-free Jacobian with no explicit Jacobian representation

If the coloring is not provided through the context, this will first try to get the coloring from the DM. If the DM has no coloring routine, then it will try to get the coloring from the matrix. This requires that the matrix have its nonzero locations already provided.

SNES supports three approaches for computing (approximate) Jacobians: user provided via SNESSetJacobian(), matrix-free via SNESSetUseMatrixFree(), and computing explicitly with finite differences and coloring using MatFDColoring. It is also possible to use automatic differentiation and the MatFDColoring object, see src/ts/tutorials/autodiff/ex16adj_tl.cxx

This function can be provided to SNESSetJacobian() along with an appropriate sparse matrix to hold the Jacobian

The function has a poorly chosen name since it does not mention the use of finite differences

SNES: Nonlinear Solvers, SNES, SNESSetJacobian(), SNESTestJacobian(), SNESComputeJacobianDefault(), SNESSetUseMatrixFree(), MatFDColoringCreate(), MatFDColoringSetFunction()

src/snes/interface/snesj2.c

src/snes/tutorials/ex14.c src/ts/tutorials/ex17.c src/ts/tutorials/ex15.c src/ts/tutorials/ex10.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscdm.h"    
PetscErrorCode SNESComputeJacobianDefaultColor(SNES snes, Vec x1, Mat J, Mat B, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
MatFDColoring
```

Example 3 (unknown):
```unknown
SNESComputeJacobianDefaultColor()
```

Example 4 (unknown):
```unknown
SNESSetFromOptions()
```

---

## SNESComputeJacobianDefault#

**URL:** https://petsc.org/release/manualpages/SNES/SNESComputeJacobianDefault/

**Contents:**
- SNESComputeJacobianDefault#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Options Database Keys#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#

Computes the Jacobian using finite differences.

snes - the SNES context

x1 - compute Jacobian at this point

ctx - application’s function context, as set with SNESSetFunction()

J - Jacobian matrix (not altered in this routine)

B - newly computed Jacobian matrix to use with preconditioner (generally the same as J)

-snes_fd - Activates SNESComputeJacobianDefault()

-snes_fd_coloring - Activates a faster computation that uses a graph coloring of the matrix

-snes_test_err etol - Square root of function error tolerance, default square root of machine epsilon (1.e-8 in double, 3.e-4 in single)

-mat_fd_type (wp|ds) - See MATMFFD_WP and MATMFFD_DS

This routine is slow and expensive, and is not currently optimized to take advantage of sparsity in the problem. Although SNESComputeJacobianDefault() is not recommended for general use in large-scale applications, It can be useful in checking the correctness of a user-provided Jacobian.

An alternative routine that uses coloring to exploit matrix sparsity is SNESComputeJacobianDefaultColor().

This routine ignores the maximum number of function evaluations set with SNESSetTolerances() and the function evaluations it performs are not counted in what is returned by of SNESGetNumberFunctionEvals().

This function can be provided to SNESSetJacobian() along with a dense matrix to hold the Jacobian

The function has a poorly chosen name since it does not mention the use of finite differences

SNES: Nonlinear Solvers, SNES, SNESSetJacobian(), SNESComputeJacobianDefaultColor(), MatCreateSNESMF()

src/snes/interface/snesj.c

src/ts/tutorials/ex4.c src/ts/tutorials/ex17.c src/ts/tutorials/ex15.c src/ts/tutorials/ex10.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESComputeJacobianDefault(SNES snes, Vec x1, Mat J, Mat B, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESSetFunction()
```

Example 3 (unknown):
```unknown
SNESComputeJacobianDefault()
```

Example 4 (unknown):
```unknown
SNESComputeJacobianDefault()
```

---

## SNESComputeJacobian#

**URL:** https://petsc.org/release/manualpages/SNES/SNESComputeJacobian/

**Contents:**
- SNESComputeJacobian#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Options Database Keys#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

Computes the Jacobian matrix that has been set with SNESSetJacobian().

snes - the SNES context

B - optional matrix for building the preconditioner, usually the same as A

-snes_lag_preconditioner lag - how often to rebuild preconditioner

-snes_lag_jacobian lag - how often to rebuild Jacobian

-snes_test_jacobian [threshold] - compare the user provided Jacobian with one compute via finite differences to check for errors. If a threshold is given, display only those entries whose difference is greater than the threshold.

-snes_test_jacobian_view [viewer] - display the user provided Jacobian, the finite difference Jacobian and the difference between them to help users detect the location of errors in the user provided Jacobian

-snes_compare_explicit - Compare the computed Jacobian to the finite difference Jacobian and output the differences

-snes_compare_explicit_draw - Compare the computed Jacobian to the finite difference Jacobian and draw the result

-snes_compare_explicit_contour - Compare the computed Jacobian to the finite difference Jacobian and draw a contour plot with the result

-snes_compare_operator - Make the comparison options above use the operator instead of the matrix used to construct the preconditioner

-snes_compare_coloring - Compute the finite difference Jacobian using coloring and display norms of difference

-snes_compare_coloring_display - Compute the finite difference Jacobian using coloring and display verbose differences

-snes_compare_coloring_threshold - Display only those matrix entries that differ by more than a given threshold

-snes_compare_coloring_threshold_atol - Absolute tolerance for difference in matrix entries to be displayed by -snes_compare_coloring_threshold

-snes_compare_coloring_threshold_rtol - Relative tolerance for difference in matrix entries to be displayed by -snes_compare_coloring_threshold

-snes_compare_coloring_draw - Compute the finite difference Jacobian using coloring and draw differences

-snes_compare_coloring_draw_contour - Compute the finite difference Jacobian using coloring and show contours of matrices and differences

Most users should not need to explicitly call this routine, as it is used internally within the nonlinear solvers.

This has duplicative ways of checking the accuracy of the user provided Jacobian (see the options above). This is for historical reasons, the routine SNESTestJacobian() use to used with the SNESType of test that has been removed.

SNES: Nonlinear Solvers, SNESSetJacobian(), KSPSetOperators(), MatStructure, SNESSetLagPreconditioner(), SNESSetLagJacobian(), SNESSetJacobianDomainError(), SNESCheckJacobianDomainError(), SNESSetCheckJacobianDomainError()

src/snes/interface/snes.c

src/snes/tutorials/ex77.c src/snes/tutorials/ex56.c src/snes/tutorials/ex12.c

SNESComputeJacobian_MATLMVM() in src/snes/impls/tr/tr.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetJacobian()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESComputeJacobian(SNES snes, Vec X, Mat A, Mat B)
```

Example 3 (unknown):
```unknown
-snes_compare_coloring_threshold
```

Example 4 (unknown):
```unknown
-snes_compare_coloring_threshold
```

---

## SNESComputeMFFunction#

**URL:** https://petsc.org/release/manualpages/SNES/SNESComputeMFFunction/

**Contents:**
- SNESComputeMFFunction#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Calls the function that has been set with DMSNESSetMFFunction().

snes - the SNES context

SNESComputeMFFunction() is used within the matrix-vector products called by the matrix created with MatCreateSNESMF() so users would not generally call this routine themselves.

Since this function is intended for use with finite differencing it does not subtract the right-hand side vector provided with SNESSolve() while SNESComputeFunction() does. As such, this routine cannot be used with MatMFFDSetBase() with a provided F function value even if it applies the same function as SNESComputeFunction() if a SNESSolve() right-hand side vector is use because the two functions difference would include this right hand side function.

SNES: Nonlinear Solvers, SNES, SNESSetFunction(), SNESGetFunction(), SNESComputeFunction(), MatCreateSNESMF(), DMSNESSetMFFunction()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMSNESSetMFFunction()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESComputeMFFunction(SNES snes, Vec x, Vec y)
```

Example 3 (unknown):
```unknown
SNESComputeMFFunction()
```

Example 4 (unknown):
```unknown
MatCreateSNESMF()
```

---

## SNESComputeNGS#

**URL:** https://petsc.org/release/manualpages/SNES/SNESComputeNGS/

**Contents:**
- SNESComputeNGS#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Calls the Gauss-Seidel function that has been set with SNESSetNGS().

snes - the SNES context

x - new solution vector

SNESComputeNGS() is typically used within composed nonlinear solver implementations, so most users would not generally call this routine themselves.

SNES: Nonlinear Solvers, SNESNGSFn, SNESSetNGS(), SNESComputeFunction(), SNESNGS

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetNGS()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESComputeNGS(SNES snes, Vec b, Vec x)
```

Example 3 (unknown):
```unknown
SNESComputeNGS()
```

Example 4 (unknown):
```unknown
SNESSetNGS()
```

---

## SNESComputeObjective#

**URL:** https://petsc.org/release/manualpages/SNES/SNESComputeObjective/

**Contents:**
- SNESComputeObjective#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Computes the objective function that has been provided by SNESSetObjective()

snes - the SNES context

ob - the objective value

SNESComputeObjective() is typically used within line-search routines, so users would not generally call this routine themselves.

When solving for \(F(x) = b\), this routine computes \(objective(x) - x^T b\) where \(objective(x)\) is the function provided with SNESSetObjective()

SNES: Nonlinear Solvers, SNESLineSearch, SNES, SNESSetObjective(), SNESGetSolution()

src/snes/interface/snesob.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetObjective()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESComputeObjective(SNES snes, Vec X, PetscReal *ob)
```

Example 3 (unknown):
```unknown
SNESComputeObjective()
```

Example 4 (unknown):
```unknown
SNESSetObjective()
```

---

## SNESConvergedCorrectPressure#

**URL:** https://petsc.org/release/manualpages/SNES/SNESConvergedCorrectPressure/

**Contents:**
- SNESConvergedCorrectPressure#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Key#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#

The regular SNES convergence test that, up on convergence, adds a vector in the nullspace to make the continuum integral of the pressure field equal to zero.

snes - the SNES context

it - the iteration (0 indicates before any Newton steps)

xnorm - 2-norm of current iterate

gnorm - 2-norm of current step

f - 2-norm of function at current iterate

ctx - Optional application context

reason - SNES_CONVERGED_ITERATING, SNES_CONVERGED_ITS, or SNES_DIVERGED_FUNCTION_NANORINF

-snes_convergence_test correct_pressure - see SNESSetFromOptions()

In order to use this convergence test, you must set up several PETSc structures. First fields must be added to the DM, and a PetscDS must be created with discretizations of those fields. We currently assume that the pressure field has index 1. The pressure field must have a nullspace, likely created using the DMSetNullSpaceConstructor() interface. Last we must be able to integrate the pressure over the domain, so the DM attached to the SNES must be a DMPLEX at this time.

This is a total misuse of the SNES convergence test handling system. It should be removed. Perhaps a SNESSetPostSolve() could be constructed to handle this process.

SNES: Nonlinear Solvers, SNES, DM, SNESConvergedDefault(), SNESSetConvergenceTest(), DMSetNullSpaceConstructor()

src/snes/utils/dmplexsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode SNESConvergedCorrectPressure(SNES snes, PetscInt it, PetscReal xnorm, PetscReal gnorm, PetscReal f, SNESConvergedReason *reason, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNES_CONVERGED_ITERATING
```

Example 3 (unknown):
```unknown
SNES_CONVERGED_ITS
```

Example 4 (unknown):
```unknown
SNES_DIVERGED_FUNCTION_NANORINF
```

---

## SNESConvergedDefault#

**URL:** https://petsc.org/release/manualpages/SNES/SNESConvergedDefault/

**Contents:**
- SNESConvergedDefault#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Default convergence test for SNESSolve().

snes - the SNES context

it - the iteration (0 indicates before any Newton steps)

xnorm - 2-norm of current iterate

snorm - 2-norm of current step

fnorm - 2-norm of function at current iterate

reason - converged reason, see SNESConvergedReason

-snes_convergence_test default - see SNESSetFromOptions()

-snes_stol - convergence tolerance in terms of the norm of the change in the solution between steps

-snes_atol abstol - absolute tolerance of residual norm

-snes_rtol rtol - relative decrease in tolerance norm from the initial 2-norm of the solution

-snes_divergence_tolerance divtol - if the residual goes above divtol*rnorm0, exit with divergence

-snes_max_funcs max_funcs - maximum number of function evaluations, use unlimited for no maximum

-snes_max_fail max_fail - maximum number of line search failures allowed before stopping, default is none

-snes_max_linear_solve_fail - number of linear solver failures before SNESSolve() stops

This routine is not generally called directly. It is set with SNESSetConvergenceTest() automatically before the SNESSolve().

It can be called within a custom convergence test that should also apply the standard convergence tests

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESSetConvergenceTest(), SNESConvergedSkip(), SNESSetTolerances(), SNESSetDivergenceTolerance(), SNESConvergedReason

src/snes/interface/snesut.c

src/snes/tutorials/ex30.c src/snes/tutorials/ex69.c

SNESConvergedDefault_VI() in src/snes/impls/vi/vi.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petsc/private/snesimpl.h"   
PetscErrorCode SNESConvergedDefault(SNES snes, PetscInt it, PetscReal xnorm, PetscReal snorm, PetscReal fnorm, SNESConvergedReason *reason, PetscCtx ctx)
```

Example 3 (unknown):
```unknown
SNESConvergedReason
```

Example 4 (unknown):
```unknown
SNESSetFromOptions()
```

---

## SNESConvergedReasonViewCancel#

**URL:** https://petsc.org/release/manualpages/SNES/SNESConvergedReasonViewCancel/

**Contents:**
- SNESConvergedReasonViewCancel#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Clears all the reason view functions for a SNES object provided with SNESConvergedReasonViewSet() also removes the default viewer.

snes - the nonlinear iterative solver context obtained from SNESCreate()

SNES: Nonlinear Solvers, SNES, SNESCreate(), SNESDestroy(), SNESReset(), SNESConvergedReasonViewSet()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESConvergedReasonViewSet()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESConvergedReasonViewCancel(SNES snes)
```

Example 3 (unknown):
```unknown
SNESCreate()
```

Example 4 (unknown):
```unknown
SNESCreate()
```

---

## SNESConvergedReasonViewFromOptions#

**URL:** https://petsc.org/release/manualpages/SNES/SNESConvergedReasonViewFromOptions/

**Contents:**
- SNESConvergedReasonViewFromOptions#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#

Processes command line options to determine if/how a SNESConvergedReason is to be viewed at the end of SNESSolve() All the user-provided viewer routines set with SNESConvergedReasonViewSet() will be called, if they exist.

snes - the SNES object

This function has a different API and behavior than PetscObjectViewFromOptions()

SNES: Nonlinear Solvers, SNES, SNESConvergedReason, SNESConvergedReasonViewSet(), SNESCreate(), SNESSetUp(), SNESDestroy(), SNESSetTolerances(), SNESConvergedDefault(), SNESGetConvergedReason(), SNESConvergedReasonView()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESConvergedReason
```

Example 2 (unknown):
```unknown
SNESSolve()
```

Example 3 (unknown):
```unknown
SNESConvergedReasonViewSet()
```

Example 4 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESConvergedReasonViewFromOptions(SNES snes)
```

---

## SNESConvergedReasonViewSet#

**URL:** https://petsc.org/release/manualpages/SNES/SNESConvergedReasonViewSet/

**Contents:**
- SNESConvergedReasonViewSet#
- Synopsis#
- Input Parameters#
- Calling sequence of f#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets an ADDITIONAL function that is to be used at the end of the nonlinear solver to display the convergence reason of the nonlinear solver.

snes - the SNES context

f - the SNESConvergedReason view function

vctx - [optional] user-defined context for private data for the SNESConvergedReason view function (use NULL if no context is desired)

reasonviewdestroy - [optional] routine that frees the context (may be NULL), see PetscCtxDestroyFn for the calling sequence

snes - the SNES context

vctx - [optional] context for private data for the function

-snes_converged_reason - sets a default SNESConvergedReasonView()

-snes_converged_reason_view_cancel - cancels all converged reason viewers that have been hardwired into a code by calls to SNESConvergedReasonViewSet(), but does not cancel those set via the options database.

Several different converged reason view routines may be set by calling SNESConvergedReasonViewSet() multiple times; all will be called in the order in which they were set.

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESConvergedReason, SNESGetConvergedReason(), SNESConvergedReasonView(), SNESConvergedReasonViewCancel(), PetscCtxDestroyFn

src/snes/interface/snes.c

src/snes/tutorials/ex6.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESConvergedReasonViewSet(SNES snes, PetscErrorCode (*f)(SNES snes, PetscCtx vctx), PetscCtx vctx, PetscCtxDestroyFn *reasonviewdestroy)
```

Example 2 (unknown):
```unknown
SNESConvergedReason
```

Example 3 (unknown):
```unknown
SNESConvergedReason
```

Example 4 (unknown):
```unknown
PetscCtxDestroyFn
```

---

## SNESConvergedReasonView#

**URL:** https://petsc.org/release/manualpages/SNES/SNESConvergedReasonView/

**Contents:**
- SNESConvergedReasonView#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Displays the reason a SNES solve converged or diverged to a viewer

snes - iterative context obtained from SNESCreate()

viewer - the viewer to display the reason

-snes_converged_reason - print reason for converged or diverged, also prints number of iterations

-snes_converged_reason ::failed - only print reason and number of iterations when diverged

To change the format of the output call PetscViewerPushFormat(viewer,format) before this call. Use PETSC_VIEWER_DEFAULT for the default, use PETSC_VIEWER_FAILED to only display a reason if it fails.

SNES: Nonlinear Solvers, SNESConvergedReason, PetscViewer, SNES, SNESCreate(), SNESSetUp(), SNESDestroy(), SNESSetTolerances(), SNESConvergedDefault(), SNESGetConvergedReason(), SNESConvergedReasonViewFromOptions(), PetscViewerPushFormat(), PetscViewerPopFormat()

src/snes/interface/snes.c

src/snes/tutorials/ex1f.F90

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESConvergedReasonView(SNES snes, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
SNESCreate()
```

Example 3 (unknown):
```unknown
PetscViewerPushFormat
```

Example 4 (unknown):
```unknown
PETSC_VIEWER_DEFAULT
```

---

## SNESConvergedReason#

**URL:** https://petsc.org/release/manualpages/SNES/SNESConvergedReason/

**Contents:**
- SNESConvergedReason#
- Synopsis#
- Values#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

reason a SNESSolve() was determined to have converged or diverged

SNES_CONVERGED_FNORM_ABS - \( ||F|| \le abstol \)

SNES_CONVERGED_FNORM_RELATIVE - \( ||F|| <= rtol*||F(x_0))|| \) where \(x_0 \) is the initial guess

SNES_CONVERGED_SNORM_RELATIVE - The 2-norm of the last step \( \le stol * ||x|| \) where \( x \) is the current solution

SNES_CONVERGED_USER - The user has indicated convergence for an arbitrary reason

SNES_DIVERGED_FUNCTION_COUNT - The user provided function has been called more times than the maximum set in SNESSetTolerances()

SNES_DIVERGED_DTOL - The norm of the function has increased by a factor of divtol set with SNESSetDivergenceTolerance()

SNES_DIVERGED_FUNCTION_NANORINF - the 2-norm of the current function evaluation is not-a-number (NaN) or infinity, (this is usually caused by a division of 0 by 0) and the solver could not recover from this (by, for example, cutting the step size)

SNES_DIVERGED_OBJECTIVE_NANORINF - the object function evaluation is not-a-number (NaN) or infinity, (this is usually caused by a division of 0 by 0) and the solver could not recover from this (by, for example, cutting the step size)

SNES_DIVERGED_FUNCTION_DOMAIN - the function evaluation occurred outside the function’s domain (function callback provided by SNESSetFunction() called SNESSetObjectiveDomainError()) and the solver could not recover from this (by, for example, cutting the step size)

SNES_DIVERGED_OBJECTIVE_DOMAIN - the object function evaluation occurred outside the function’s domain (function callback provided by SNESSetObjective() called SNESSetObjectiveDomainError()) and the solver could not recover from this (by, for example, cutting the step size)

SNES_DIVERGED_JACOBIAN_DOMAIN - the Jacobian evaluation occurred outside the function’s domain (function callback provided by SNESSetJacobian() called SNESSetJacobianDomainError())

SNES_DIVERGED_MAX_IT - SNESSolve() has reached the maximum number of iterations requested

SNES_DIVERGED_LINE_SEARCH - The line search has failed. This only occurs for SNES solvers that use a line search

SNES_DIVERGED_LOCAL_MIN - the algorithm seems to have stagnated at a local minimum that is not zero.

***SNES_CONVERGED_ITERATING -*** this only occurs if SNESGetConvergedReason()is called during theSNESSolve()`

The two most common reasons for divergence are an incorrectly coded or computed Jacobian or failure or lack of convergence in the linear system (in this case we recommend testing with -pc_type lu to eliminate the linear solver as the cause of the problem).

SNES_DIVERGED_LOCAL_MIN can only occur when using a SNES solver that uses a line search (SNESLineSearch). The line search wants to \( \min Q(\alpha) = 1/2 || F(x + \alpha s) ||^2_2 \) this occurs at \( Q'(\alpha) = s^T F'(x+\alpha s)^T F(x+\alpha s) = 0\). If \(s\) is the Newton direction \( - F'(x)^(-1)F(x)\) then \( Q'(\alpha) = -F(x)^T F'(x)^(-1)^T F'(x+\alpha s)F(x+\alpha s)\); when \(\alpha = 0\) \(Q'(0) = - ||F(x)||^2_2 \) which is always NEGATIVE if \(F'(x)\) is invertible. This means the Newton direction is a descent direction and the line search should succeed if \(\alpha \) is small enough.

If \(F'(x)\) is NOT invertible AND \(F'(x)^T F(x) = 0 \) then \(Q'(0) = 0 \) and the Newton direction is NOT a descent direction so the line search will fail. All one can do at this point is change the initial guess and try again.

An alternative explanation: Newton’s method can be regarded as replacing the function with its linear approximation and minimizing the 2-norm of that. That is \(F(x+s) \approx F(x) + F'(x)s\) so we minimize \( || F(x) + F'(x) s ||^2_2\) using Least Squares. If \(F'(x)\) is invertible then \(s = - F'(x)^(-1)F(x)\) otherwise \(F'(x)^T F'(x) s = -F'(x)^T F(x)\). If \(F'(x)^T F(x)\) is NOT zero then there exists a nontrivial (that is \(F'(x)s \ne 0\)) solution to the equation and this direction is \(s = - [F'(x)^T F'(x)]^(-1) F'(x)^T F(x)\) so \(Q'(0) = - F(x)^T F'(x) [F'(x)^T F'(x)]^(-T) F'(x)^T F(x) = - (F'(x)^T F(x)) [F'(x)^T F'(x)]^(-T) (F'(x)^T F(x))\). Since we are assuming \((F'(x)^T F(x)) \ne 0\) and \(F'(x)^T F'(x)\) has no negative eigenvalues \(Q'(0) < 0\) so \(s\) is a descent direction and the line search should succeed for small enough \(\alpha\).

Note that this RARELY happens in practice. Far more likely the linear system is not being solved (well enough?) or the Jacobian is wrong.

SNES_DIVERGED_MAX_IT means that the solver reached the maximum number of iterations without satisfying any convergence criteria. SNES_CONVERGED_ITS means that SNESConvergedSkip() was chosen as the convergence test; thus the usual convergence criteria have not been checked and may or may not be satisfied.

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESGetConvergedReason(), KSPConvergedReason, SNESSetConvergenceTest(), SNESSetTolerances()

src/ts/tutorials/ex14.c src/snes/tutorials/ex5f.F90 src/snes/tutorials/ex6.c src/snes/tutorials/ex42.c src/snes/tutorials/ex2.c src/snes/tutorials/ex30.c src/ts/tutorials/ex48.c src/snes/tutorials/ex48.c src/snes/tutorials/ex15.c src/snes/tutorials/ex69.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
typedef enum {                       /* converged */
  SNES_CONVERGED_FNORM_ABS      = 2, /* ||F|| < atol */
  SNES_CONVERGED_FNORM_RELATIVE = 3, /* ||F|| < rtol*||F_initial|| */
  SNES_CONVERGED_SNORM_RELATIVE = 4, /* Newton computed step size small; || delta x || < stol || x || */
  SNES_CONVERGED_ITS            = 5, /* maximum iterations reached */
  SNES_BREAKOUT_INNER_ITER      = 6, /* Flag to break out of inner loop after checking custom convergence, used in multi-phase flow when state changes */
  SNES_CONVERGED_USER           = 7, /* The user has indicated convergence for an arbitrary reason */
  /* diverged */
  SNES_DIVERGED_FUNCTION_DOMAIN      = -1, /* the new x location passed the function is not in the domain of F */
  SNES_DIVERGED_FUNCTION_COUNT       = -2,
  SNES_DIVERGED_LINEAR_SOLVE         = -3, /* the linear solve failed */
  SNES_DIVERGED_FUNCTION_NANORINF    = -4,
  SNES_DIVERGED_FNORM_NAN_DEPRECATED = -4,
  SNES_DIVERGED_MAX_IT               = -5,
  SNES_DIVERGED_LINE_SEARCH          = -6,  /* the line search failed */
  SNES_DIVERGED_INNER                = -7,  /* inner solve failed */
  SNES_DIVERGED_LOCAL_MIN            = -8,  /* || J^T b || is small, implies converged to local minimum of F() */
  SNES_DIVERGED_DTOL                 = -9,  /* || F || > divtol*||F_initial|| */
  SNES_DIVERGED_JACOBIAN_DOMAIN      = -10, /* Jacobian calculation does not make sense */
  SNES_DIVERGED_TR_DELTA             = -11,
  SNES_CONVERGED_TR_DELTA_DEPRECATED = -11,
  SNES_DIVERGED_USER                 = -12, /* The user has indicated divergence for an arbitrary reason */
  SNES_DIVERGED_OBJECTIVE_DOMAIN     = -13,
  SNES_DIVERGED_OBJECTIVE_NANORINF   = -14,

  SNES_CONVERGED_ITERATING = 0
} SNESConvergedReason;
```

Example 3 (unknown):
```unknown
SNES_CONVERGED_FNORM_ABS
```

Example 4 (unknown):
```unknown
SNES_CONVERGED_FNORM_RELATIVE
```

---

## SNESConvergedSkip#

**URL:** https://petsc.org/release/manualpages/SNES/SNESConvergedSkip/

**Contents:**
- SNESConvergedSkip#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Convergence test for SNES that NEVER returns as converged, UNLESS the maximum number of iteration have been reached.

snes - the SNES context

it - the iteration (0 indicates before any Newton steps)

xnorm - 2-norm of current iterate

snorm - 2-norm of current step

fnorm - 2-norm of function at current iterate

reason - SNES_CONVERGED_ITERATING, SNES_CONVERGED_ITS, or SNES_DIVERGED_FUNCTION_NANORINF

-snes_convergence_test skip - see SNESSetFromOptions()

This is often used if snes is being used as a nonlinear smoother in SNESFAS or possibly other SNESType

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESConvergedDefault(), SNESSetConvergenceTest(), SNESConvergedReason

src/snes/interface/snesut.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsc/private/snesimpl.h"   
PetscErrorCode SNESConvergedSkip(SNES snes, PetscInt it, PetscReal xnorm, PetscReal snorm, PetscReal fnorm, SNESConvergedReason *reason, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNES_CONVERGED_ITERATING
```

Example 3 (unknown):
```unknown
SNES_CONVERGED_ITS
```

Example 4 (unknown):
```unknown
SNES_DIVERGED_FUNCTION_NANORINF
```

---

## SNESConverged#

**URL:** https://petsc.org/release/manualpages/SNES/SNESConverged/

**Contents:**
- SNESConverged#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Run the convergence test and update the SNESConvergedReason.

snes - the SNES context

it - current iteration

xnorm - 2-norm of current iterate

snorm - 2-norm of current step

fnorm - 2-norm of function

This routine is called by the SNESSolve() implementations. It does not typically need to be called by the user.

SNES: Nonlinear Solvers, SNES, SNESSolve, SNESSetConvergenceTest()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESConvergedReason
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESConverged(SNES snes, PetscInt it, PetscReal xnorm, PetscReal snorm, PetscReal fnorm)
```

Example 3 (unknown):
```unknown
SNESSolve()
```

Example 4 (unknown):
```unknown
SNESSetConvergenceTest()
```

---

## SNESCreate#

**URL:** https://petsc.org/release/manualpages/SNES/SNESCreate/

**Contents:**
- SNESCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Options Database Keys#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates a nonlinear solver context used to manage a set of nonlinear solves

comm - MPI communicator

outsnes - the new SNES context

-snes_mf - Activates default matrix-free Jacobian-vector products, and no matrix to construct a preconditioner

-snes_mf_operator - Activates default matrix-free Jacobian-vector products, and a user-provided matrix as set by SNESSetJacobian()

-snes_fd_coloring - uses a relative fast computation of the Jacobian using finite differences and a graph coloring

-snes_fd - Uses (slow!) finite differences to compute Jacobian

SNES always creates a KSP object even though many SNES methods do not use it. This is unfortunate and should be fixed at some point. The flag snes->usesksp indicates if the particular method does use KSP and regulates if the information about the KSP is printed in SNESView().

TSSetFromOptions() does call SNESSetFromOptions() which can lead to users being confused by help messages about meaningless SNES options.

SNES always creates the snes->kspconvctx even though it is used by only one type. This should be fixed.

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESDestroy(), SNESSetLagPreconditioner(), SNESSetLagJacobian()

src/snes/interface/snes.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex99.c src/snes/tutorials/ex1.c src/snes/tutorials/ex14.c src/snes/tutorials/ex35.c src/snes/tutorials/ex40f90.F90 src/snes/tutorials/ex17.c src/snes/tutorials/ex33.c src/snes/tutorials/ex23.c src/snes/tutorials/ex21.c

SNESCreate_NEWTONAL() in src/snes/impls/al/al.c SNESCreate_Composite() in src/snes/impls/composite/snescomposite.c SNESCreate_FAS() in src/snes/impls/fas/fas.c SNESCreate_NGS() in src/snes/impls/gs/snesgs.c SNESCreate_KSPONLY() in src/snes/impls/ksponly/ksponly.c SNESCreate_KSPTRANSPOSEONLY() in src/snes/impls/ksponly/ksponly.c SNESCreate_NEWTONLS() in src/snes/impls/ls/ls.c SNESCreate_MS() in src/snes/impls/ms/ms.c SNESCreate_Multiblock() in src/snes/impls/multiblock/multiblock.c SNESCreate_ASPIN() in src/snes/impls/nasm/aspin.c SNESCreate_NASM() in src/snes/impls/nasm/nasm.c SNESCreate_NCG() in src/snes/impls/ncg/snesncg.c SNESCreate_Anderson() in src/snes/impls/ngmres/anderson.c SNESCreate_NGMRES() in src/snes/impls/ngmres/snesngmres.c SNESCreate_NEWTONTRDC() in src/snes/impls/ntrdc/ntrdc.c SNESCreate_Patch() in src/snes/impls/patch/snespatch.c SNESCreate_QN() in src/snes/impls/qn/qn.c SNESCreate_NRichardson() in src/snes/impls/richardson/snesrichardson.c SNESCreate_Shell() in src/snes/impls/shell/snesshell.c SNESCreate_NEWTONTR() in src/snes/impls/tr/tr.c SNESCreate_VINEWTONRSLS() in src/snes/impls/vi/rs/virs.c SNESCreate_VINEWTONSSLS() in src/snes/impls/vi/ss/viss.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESCreate(MPI_Comm comm, SNES *outsnes)
```

Example 2 (unknown):
```unknown
SNESSetJacobian()
```

Example 3 (unknown):
```unknown
TSSetFromOptions()
```

Example 4 (unknown):
```unknown
SNESSetFromOptions()
```

---

## SNESDestroy#

**URL:** https://petsc.org/release/manualpages/SNES/SNESDestroy/

**Contents:**
- SNESDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Destroys the nonlinear solver context that was created with SNESCreate().

snes - the SNES context

SNES: Nonlinear Solvers, SNES, SNESCreate(), SNESSolve()

src/snes/interface/snes.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex99.c src/snes/tutorials/ex1.c src/snes/tutorials/ex14.c src/snes/tutorials/ex35.c src/snes/tutorials/ex40f90.F90 src/snes/tutorials/ex17.c src/snes/tutorials/ex33.c src/snes/tutorials/ex23.c src/snes/tutorials/ex21.c

SNESDestroy_NEWTONAL() in src/snes/impls/al/al.c SNESDestroy_Composite() in src/snes/impls/composite/snescomposite.c SNESDestroy_FAS() in src/snes/impls/fas/fas.c SNESDestroy_NGS() in src/snes/impls/gs/snesgs.c SNESDestroy_KSPONLY() in src/snes/impls/ksponly/ksponly.c SNESDestroy_NEWTONLS() in src/snes/impls/ls/ls.c SNESDestroy_MS() in src/snes/impls/ms/ms.c SNESDestroy_Multiblock() in src/snes/impls/multiblock/multiblock.c SNESDestroy_ASPIN() in src/snes/impls/nasm/aspin.c SNESDestroy_NASM() in src/snes/impls/nasm/nasm.c SNESDestroy_NCG() in src/snes/impls/ncg/snesncg.c SNESDestroy_NGMRES() in src/snes/impls/ngmres/snesngmres.c SNESDestroy_NEWTONTRDC() in src/snes/impls/ntrdc/ntrdc.c SNESDestroy_Patch() in src/snes/impls/patch/snespatch.c SNESDestroy_QN() in src/snes/impls/qn/qn.c SNESDestroy_NRichardson() in src/snes/impls/richardson/snesrichardson.c SNESDestroy_Shell() in src/snes/impls/shell/snesshell.c SNESDestroy_NEWTONTR() in src/snes/impls/tr/tr.c SNESDestroy_VI() in src/snes/impls/vi/vi.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESCreate()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESDestroy(SNES *snes)
```

Example 3 (unknown):
```unknown
SNESCreate()
```

Example 4 (unknown):
```unknown
SNESSolve()
```

---

## SNESFASCreateCoarseVec#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASCreateCoarseVec/

**Contents:**
- SNESFASCreateCoarseVec#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

create a Vec corresponding to a state vector on one level coarser than the current level

snes - SNESFAS object

Xcoarse - vector on level one coarser than the current level

SNES: Nonlinear Solvers, SNESFASSetRestriction(), SNESFASRestrict(), SNESFAS

src/snes/impls/fas/fas.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASCreateCoarseVec(SNES snes, Vec *Xcoarse)
```

Example 2 (unknown):
```unknown
SNESFASSetRestriction()
```

Example 3 (unknown):
```unknown
SNESFASRestrict()
```

---

## SNESFASCycleGetCorrection#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASCycleGetCorrection/

**Contents:**
- SNESFASCycleGetCorrection#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the coarse correction SNESFAS context for this level

snes - the SNESFAS obtained with SNESFASGetCycleSNES()

correction - the coarse correction solve on this level

Returns NULL on the coarsest level.

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASCycleGetSmootherUp(), SNESFASCycleGetSmoother()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASCycleGetCorrection(SNES snes, SNES *correction)
```

Example 2 (unknown):
```unknown
SNESFASGetCycleSNES()
```

Example 3 (unknown):
```unknown
SNESFASCycleGetSmootherUp()
```

Example 4 (unknown):
```unknown
SNESFASCycleGetSmoother()
```

---

## SNESFASCycleGetInjection#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASCycleGetInjection/

**Contents:**
- SNESFASCycleGetInjection#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the injection on a level

snes - the SNESFAS obtained with SNESFASGetCycleSNES()

mat - the restriction operator on this level

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASGetInjection(), SNESFASCycleGetRestriction()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASCycleGetInjection(SNES snes, Mat *mat)
```

Example 2 (unknown):
```unknown
SNESFASGetCycleSNES()
```

Example 3 (unknown):
```unknown
SNESFASGetInjection()
```

Example 4 (unknown):
```unknown
SNESFASCycleGetRestriction()
```

---

## SNESFASCycleGetInterpolation#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASCycleGetInterpolation/

**Contents:**
- SNESFASCycleGetInterpolation#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the interpolation on a level

snes - the SNESFAS obtained with SNESFASGetCycleSNES()

mat - the interpolation operator on this level

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASCycleGetSmootherUp(), SNESFASCycleGetSmoother()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASCycleGetInterpolation(SNES snes, Mat *mat)
```

Example 2 (unknown):
```unknown
SNESFASGetCycleSNES()
```

Example 3 (unknown):
```unknown
SNESFASCycleGetSmootherUp()
```

Example 4 (unknown):
```unknown
SNESFASCycleGetSmoother()
```

---

## SNESFASCycleGetRestriction#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASCycleGetRestriction/

**Contents:**
- SNESFASCycleGetRestriction#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the restriction on a level

snes - the SNESFAS obtained with SNESFASGetCycleSNES()

mat - the restriction operator on this level

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASGetRestriction(), SNESFASCycleGetInterpolation()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASCycleGetRestriction(SNES snes, Mat *mat)
```

Example 2 (unknown):
```unknown
SNESFASGetCycleSNES()
```

Example 3 (unknown):
```unknown
SNESFASGetRestriction()
```

Example 4 (unknown):
```unknown
SNESFASCycleGetInterpolation()
```

---

## SNESFASCycleGetRScale#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASCycleGetRScale/

**Contents:**
- SNESFASCycleGetRScale#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the injection scale-factor on a level

snes - the SNESFAS obtained with SNESFASGetCycleSNES()

vec - the restriction operator on this level

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASCycleGetRestriction(), SNESFASGetRScale()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASCycleGetRScale(SNES snes, Vec *vec)
```

Example 2 (unknown):
```unknown
SNESFASGetCycleSNES()
```

Example 3 (unknown):
```unknown
SNESFASCycleGetRestriction()
```

Example 4 (unknown):
```unknown
SNESFASGetRScale()
```

---

## SNESFASCycleGetSmootherDown#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASCycleGetSmootherDown/

**Contents:**
- SNESFASCycleGetSmootherDown#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the down smoother on a particular cycle level.

snes - SNESFAS obtained with SNESFASGetCycleSNES()

smoothd - the smoother

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASCycleGetSmootherUp(), SNESFASCycleGetSmoother(), SNESFASGetCycleSNES()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASCycleGetSmootherDown(SNES snes, SNES *smoothd)
```

Example 2 (unknown):
```unknown
SNESFASGetCycleSNES()
```

Example 3 (unknown):
```unknown
SNESFASCycleGetSmootherUp()
```

Example 4 (unknown):
```unknown
SNESFASCycleGetSmoother()
```

---

## SNESFASCycleGetSmootherUp#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASCycleGetSmootherUp/

**Contents:**
- SNESFASCycleGetSmootherUp#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the up smoother on a particular cycle level.

snes - the SNESFAS obtained with SNESFASGetCycleSNES()

smoothu - the smoother

Returns the downsmoother if no up smoother is available. This enables transparent default behavior in the process of the solve.

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASCycleGetSmoother(), SNESFASCycleGetSmootherDown(), SNESFASGetCycleSNES()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASCycleGetSmootherUp(SNES snes, SNES *smoothu)
```

Example 2 (unknown):
```unknown
SNESFASGetCycleSNES()
```

Example 3 (unknown):
```unknown
SNESFASCycleGetSmoother()
```

Example 4 (unknown):
```unknown
SNESFASCycleGetSmootherDown()
```

---

## SNESFASCycleGetSmoother#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASCycleGetSmoother/

**Contents:**
- SNESFASCycleGetSmoother#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the smoother on a particular cycle level.

snes - the SNESFAS obtained with SNESFASGetCycleSNES()

smooth - the smoother

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASCycleGetSmootherUp(), SNESFASCycleGetSmootherDown(), SNESFASGetCycleSNES()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASCycleGetSmoother(SNES snes, SNES *smooth)
```

Example 2 (unknown):
```unknown
SNESFASGetCycleSNES()
```

Example 3 (unknown):
```unknown
SNESFASCycleGetSmootherUp()
```

Example 4 (unknown):
```unknown
SNESFASCycleGetSmootherDown()
```

---

## SNESFASCycleIsFine#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASCycleIsFine/

**Contents:**
- SNESFASCycleIsFine#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Determines if a given SNES is the finest level in a SNESFAS

snes - the SNESFAS context obtained with SNESFASGetCycleSNES()

flg - indicates if this is the fine level or not

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetLevels()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASCycleIsFine(SNES snes, PetscBool *flg)
```

Example 2 (unknown):
```unknown
SNESFASGetCycleSNES()
```

Example 3 (unknown):
```unknown
SNESFASSetLevels()
```

---

## SNESFASCycleSetCycles#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASCycleSetCycles/

**Contents:**
- SNESFASCycleSetCycles#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the number of cycles for all levels in a SNESFAS

snes - the SNESFAS nonlinear multigrid context

cycles - the number of cycles – 1 for V-cycle, 2 for W-cycle

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetCycles()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASCycleSetCycles(SNES snes, PetscInt cycles)
```

Example 2 (unknown):
```unknown
SNESFASSetCycles()
```

---

## SNESFASFullGetTotal#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASFullGetTotal/

**Contents:**
- SNESFASFullGetTotal#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Use total residual restriction and total interpolation on the initial down and up sweep of full FAS cycles

snes - the SNESFAS nonlinear multigrid context

total - whether to use total restriction / interpolatiaon or not (the alternative is defect restriction and correction interpolation)

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetNumberSmoothUp(), DMInterpolateSolution(), SNESFullSetTotal()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASFullGetTotal(SNES snes, PetscBool *total)
```

Example 2 (unknown):
```unknown
SNESFASSetNumberSmoothUp()
```

Example 3 (unknown):
```unknown
DMInterpolateSolution()
```

Example 4 (unknown):
```unknown
SNESFullSetTotal()
```

---

## SNESFASFullSetDownSweep#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASFullSetDownSweep/

**Contents:**
- SNESFASFullSetDownSweep#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Smooth during the initial downsweep for SNESFAS

snes - the SNESFAS nonlinear multigrid context

swp - whether to downsweep or not

-snes_fas_full_downsweep - Sets whether to smooth on the initial downsweep

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetNumberSmoothUp()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASFullSetDownSweep(SNES snes, PetscBool swp)
```

Example 2 (unknown):
```unknown
SNESFASSetNumberSmoothUp()
```

---

## SNESFASFullSetTotal#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASFullSetTotal/

**Contents:**
- SNESFASFullSetTotal#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Use total residual restriction and total interpolation on the initial down and up sweep of full SNESFAS cycles

snes - the SNESFAS nonlinear multigrid context

total - whether to use total restriction / interpolatiaon or not (the alternative is defect restriction and correction interpolation)

-snes_fas_full_total - Use total restriction and interpolation on the initial down and up sweeps for the full SNESFAS cycle

This option is only significant if the interpolation of a coarse correction (MatInterpolate()) is significantly different from total solution interpolation (DMInterpolateSolution()).

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetNumberSmoothUp(), DMInterpolateSolution()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASFullSetTotal(SNES snes, PetscBool total)
```

Example 2 (unknown):
```unknown
MatInterpolate()
```

Example 3 (unknown):
```unknown
DMInterpolateSolution()
```

Example 4 (unknown):
```unknown
SNESFASSetNumberSmoothUp()
```

---

## SNESFASGalerkinFunctionDefault#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASGalerkinFunctionDefault/

**Contents:**
- SNESFASGalerkinFunctionDefault#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Computes the Galerkin FAS function

snes - the SNESFAS nonlinear solver context

ctx - the application context

The Galerkin FAS function evaluation is defined as

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASGetGalerkin(), SNESFASSetGalerkin()

src/snes/impls/fas/fasgalerkin.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASGalerkinFunctionDefault(SNES snes, Vec X, Vec F, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESFASGetGalerkin()
```

Example 3 (unknown):
```unknown
SNESFASSetGalerkin()
```

---

## SNESFASGetCoarseSolve#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASGetCoarseSolve/

**Contents:**
- SNESFASGetCoarseSolve#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the coarsest level solver.

snes - the SNESFAS nonlinear multigrid context

coarse - the coarse-level solver

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetInjection(), SNESFASSetRestriction()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASGetCoarseSolve(SNES snes, SNES *coarse)
```

Example 2 (unknown):
```unknown
SNESFASSetInjection()
```

Example 3 (unknown):
```unknown
SNESFASSetRestriction()
```

---

## SNESFASGetCycleSNES#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASGetCycleSNES/

**Contents:**
- SNESFASGetCycleSNES#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the SNES corresponding to a particular level of the SNESFAS hierarchy

snes - the SNES nonlinear multigrid context

level - the level to get

lsnes - the SNES for the requested level

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetLevels(), SNESFASGetLevels()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASGetCycleSNES(SNES snes, PetscInt level, SNES *lsnes)
```

Example 2 (unknown):
```unknown
SNESFASSetLevels()
```

Example 3 (unknown):
```unknown
SNESFASGetLevels()
```

---

## SNESFASGetGalerkin#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASGetGalerkin/

**Contents:**
- SNESFASGetGalerkin#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets if the coarse problems are formed by projection to the fine problem

Not Collective but the result would be the same on all MPI processes

snes - the SNESFAS nonlinear solver context

flg - PETSC_TRUE if the coarse problem is formed by projection

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetLevels(), SNESFASSetGalerkin()

src/snes/impls/fas/fasgalerkin.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASGetGalerkin(SNES snes, PetscBool *flg)
```

Example 2 (unknown):
```unknown
SNESFASSetLevels()
```

Example 3 (unknown):
```unknown
SNESFASSetGalerkin()
```

---

## SNESFASGetInjection#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASGetInjection/

**Contents:**
- SNESFASGetInjection#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the matrix used to calculate the injection from l-1 to the lth level

snes - the SNESFAS nonlinear multigrid context

level - the level (0 is coarsest) to supply [do not supply 0]

mat - the injection operator

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetInjection(), SNESFASGetRestriction(), SNESFASGetInterpolation(), SNESFASGetRScale()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASGetInjection(SNES snes, PetscInt level, Mat *mat)
```

Example 2 (unknown):
```unknown
SNESFASSetInjection()
```

Example 3 (unknown):
```unknown
SNESFASGetRestriction()
```

Example 4 (unknown):
```unknown
SNESFASGetInterpolation()
```

---

## SNESFASGetInterpolation#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASGetInterpolation/

**Contents:**
- SNESFASGetInterpolation#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the matrix used to calculate the interpolation from l-1 to the lth level

snes - the SNESFAS nonlinear multigrid context

level - the level (0 is coarsest) to supply [do not supply 0]

mat - the interpolation operator

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetInterpolation(), SNESFASGetInjection(), SNESFASGetRestriction(), SNESFASGetRScale()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASGetInterpolation(SNES snes, PetscInt level, Mat *mat)
```

Example 2 (unknown):
```unknown
SNESFASSetInterpolation()
```

Example 3 (unknown):
```unknown
SNESFASGetInjection()
```

Example 4 (unknown):
```unknown
SNESFASGetRestriction()
```

---

## SNESFASGetLevels#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASGetLevels/

**Contents:**
- SNESFASGetLevels#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the number of levels in a SNESFAS, including fine and coarse grids

snes - the SNES nonlinear solver context of SNESType SNESFAS

levels - the number of levels

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetLevels(), PCMGGetLevels()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASGetLevels(SNES snes, PetscInt *levels)
```

Example 2 (unknown):
```unknown
SNESFASSetLevels()
```

Example 3 (unknown):
```unknown
PCMGGetLevels()
```

---

## SNESFASGetRestriction#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASGetRestriction/

**Contents:**
- SNESFASGetRestriction#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the matrix used to calculate the restriction from l to the l-1th level

snes - the SNESFAS nonlinear multigrid context

level - the level (0 is coarsest) to supply [do not supply 0]

mat - the interpolation operator

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetRestriction(), SNESFASGetInjection(), SNESFASGetInterpolation(), SNESFASGetRScale()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASGetRestriction(SNES snes, PetscInt level, Mat *mat)
```

Example 2 (unknown):
```unknown
SNESFASSetRestriction()
```

Example 3 (unknown):
```unknown
SNESFASGetInjection()
```

Example 4 (unknown):
```unknown
SNESFASGetInterpolation()
```

---

## SNESFASGetSmootherDown#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASGetSmootherDown/

**Contents:**
- SNESFASGetSmootherDown#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the downsmoother on a level.

snes - the SNESFAS nonlinear multigrid context

level - the level (0 is coarsest) to supply

smooth - the smoother

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetInjection(), SNESFASSetRestriction()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASGetSmootherDown(SNES snes, PetscInt level, SNES *smooth)
```

Example 2 (unknown):
```unknown
SNESFASSetInjection()
```

Example 3 (unknown):
```unknown
SNESFASSetRestriction()
```

---

## SNESFASGetSmootherUp#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASGetSmootherUp/

**Contents:**
- SNESFASGetSmootherUp#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the upsmoother on a level.

snes - the SNESFAS nonlinear multigrid context

level - the level (0 is coarsest)

smooth - the smoother

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetInjection(), SNESFASSetRestriction()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASGetSmootherUp(SNES snes, PetscInt level, SNES *smooth)
```

Example 2 (unknown):
```unknown
SNESFASSetInjection()
```

Example 3 (unknown):
```unknown
SNESFASSetRestriction()
```

---

## SNESFASGetSmoother#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASGetSmoother/

**Contents:**
- SNESFASGetSmoother#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the default smoother on a level.

snes - the SNESFAS nonlinear multigrid context

level - the level (0 is coarsest) to supply

smooth - the smoother

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetInjection(), SNESFASSetRestriction()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASGetSmoother(SNES snes, PetscInt level, SNES *smooth)
```

Example 2 (unknown):
```unknown
SNESFASSetInjection()
```

Example 3 (unknown):
```unknown
SNESFASSetRestriction()
```

---

## SNESFASGetType#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASGetType/

**Contents:**
- SNESFASGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the update and correction type used for SNESFAS.

snes - SNESFAS context

fastype - SNES_FAS_ADDITIVE, SNES_FAS_MULTIPLICATIVE, SNES_FAS_FULL, or SNES_FAS_KASKADE

SNES: Nonlinear Solvers, SNES, SNESFAS, PCMGSetType(), SNESFASSetType(), SNES_FAS_ADDITIVE, SNES_FAS_MULTIPLICATIVE, SNES_FAS_FULL, SNES_FAS_KASKADE

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASGetType(SNES snes, SNESFASType *fastype)
```

Example 2 (unknown):
```unknown
SNES_FAS_ADDITIVE
```

Example 3 (unknown):
```unknown
SNES_FAS_MULTIPLICATIVE
```

Example 4 (unknown):
```unknown
SNES_FAS_FULL
```

---

## SNESFASRestrict#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASRestrict/

**Contents:**
- SNESFASRestrict#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

restrict a Vec to the next coarser level

fine - SNES from which to restrict

Xfine - vector to restrict

Xcoarse - result of restriction

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetRestriction(), SNESFASSetInjection(), SNESFASCreateCoarseVec()

src/snes/impls/fas/fas.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASRestrict(SNES fine, Vec Xfine, Vec Xcoarse)
```

Example 2 (unknown):
```unknown
SNESFASSetRestriction()
```

Example 3 (unknown):
```unknown
SNESFASSetInjection()
```

Example 4 (unknown):
```unknown
SNESFASCreateCoarseVec()
```

---

## SNESFASSetContinuation#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASSetContinuation/

**Contents:**
- SNESFASSetContinuation#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Sets the SNESFAS cycle to default to using exact Newton solves on the upsweep

snes - the SNESFAS nonlinear multigrid context

continuation - whether to use continuation

-snes_fas_continuation - sets continuation to true

This sets the prefix on the upsweep smoothers to -fas_continuation

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetNumberSmoothUp()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASSetContinuation(SNES snes, PetscBool continuation)
```

Example 2 (unknown):
```unknown
SNESFASSetNumberSmoothUp()
```

---

## SNESFASSetCycles#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASSetCycles/

**Contents:**
- SNESFASSetCycles#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Sets the number of SNESFAS multigrid cycles to use each time a grid is visited. Use SNESFASSetCyclesOnLevel() for more complicated cycling.

snes - the SNESFAS nonlinear multigrid context

cycles - the number of cycles – 1 for V-cycle, 2 for W-cycle

-snes_fas_cycles (1|2) - 1 for V-cycle, 2 for W-cycle

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetCyclesOnLevel()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESFASSetCyclesOnLevel()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASSetCycles(SNES snes, PetscInt cycles)
```

Example 3 (unknown):
```unknown
SNESFASSetCyclesOnLevel()
```

---

## SNESFASSetGalerkin#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASSetGalerkin/

**Contents:**
- SNESFASSetGalerkin#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets coarse problems as formed by projection to the fine problem

snes - the SNESFAS nonlinear solver context

flg - PETSC_TRUE to use the projection process

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetLevels(), SNESFASGetGalerkin()

src/snes/impls/fas/fasgalerkin.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASSetGalerkin(SNES snes, PetscBool flg)
```

Example 2 (unknown):
```unknown
SNESFASSetLevels()
```

Example 3 (unknown):
```unknown
SNESFASGetGalerkin()
```

---

## SNESFASSetInjection#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASSetInjection/

**Contents:**
- SNESFASSetInjection#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the matrix to be used to inject the solution from level to level-1.

snes - the SNESFAS nonlinear multigrid context

mat - the injection matrix

level - the level (0 is coarsest) to supply [Do not supply 0]

If you do not set this, the restriction and rscale is used to project the solution instead.

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetInterpolation(), SNESFASSetRestriction()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASSetInjection(SNES snes, PetscInt level, Mat mat)
```

Example 2 (unknown):
```unknown
SNESFASSetInterpolation()
```

Example 3 (unknown):
```unknown
SNESFASSetRestriction()
```

---

## SNESFASSetInterpolation#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASSetInterpolation/

**Contents:**
- SNESFASSetInterpolation#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Sets the Mat to be used to apply the interpolation from l-1 to the lth level

snes - the SNESFAS nonlinear multigrid context

mat - the interpolation operator

level - the level (0 is coarsest) to supply [do not supply 0]

Usually this is the same matrix used also to set the restriction for the same level.

One can pass in the interpolation matrix or its transpose; PETSc figures out from the matrix dimensions which one it is.

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetInjection(), SNESFASSetRestriction(), SNESFASSetRScale()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASSetInterpolation(SNES snes, PetscInt level, Mat mat)
```

Example 2 (unknown):
```unknown
SNESFASSetInjection()
```

Example 3 (unknown):
```unknown
SNESFASSetRestriction()
```

Example 4 (unknown):
```unknown
SNESFASSetRScale()
```

---

## SNESFASSetLevels#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASSetLevels/

**Contents:**
- SNESFASSetLevels#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the number of levels to use with SNESFAS. Must be called before any other SNESFAS routine.

snes - the SNES context of SNESType SNESFAS

levels - the number of levels

comms - optional communicators for each level; this is to allow solving the coarser problems on smaller sets of processors.

If the number of levels is one then the solver uses the -fas_levels prefix for setting the level options rather than the -fas_coarse prefix.

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASGetLevels()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASSetLevels(SNES snes, PetscInt levels, MPI_Comm *comms)
```

Example 2 (unknown):
```unknown
-fas_levels
```

Example 3 (unknown):
```unknown
-fas_coarse
```

Example 4 (unknown):
```unknown
SNESFASGetLevels()
```

---

## SNESFASSetLog#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASSetLog/

**Contents:**
- SNESFASSetLog#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets or unsets time logging for various SNESFAS stages on all levels

snes - the SNESFAS context

flg - whether to log or not

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetMonitor()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASSetLog(SNES snes, PetscBool flg)
```

Example 2 (unknown):
```unknown
SNESFASSetMonitor()
```

---

## SNESFASSetMonitor#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASSetMonitor/

**Contents:**
- SNESFASSetMonitor#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the method-specific cycle monitoring

snes - the SNESFAS context

vf - viewer and format structure (may be NULL if flg is PETSC_FALSE)

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESMonitorSet(), SNESFASSetCyclesOnLevel()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASSetMonitor(SNES snes, PetscViewerAndFormat *vf, PetscBool flg)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
SNESMonitorSet()
```

Example 4 (unknown):
```unknown
SNESFASSetCyclesOnLevel()
```

---

## SNESFASSetNumberSmoothDown#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASSetNumberSmoothDown/

**Contents:**
- SNESFASSetNumberSmoothDown#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Sets the number of pre-smoothing steps to use on all levels.

snes - the SNESFAS nonlinear multigrid context

n - the number of smoothing steps to use

-snes_fas_smoothdown n - Sets number of pre-smoothing steps

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetNumberSmoothUp()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASSetNumberSmoothDown(SNES snes, PetscInt n)
```

Example 2 (unknown):
```unknown
SNESFASSetNumberSmoothUp()
```

---

## SNESFASSetNumberSmoothUp#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASSetNumberSmoothUp/

**Contents:**
- SNESFASSetNumberSmoothUp#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Sets the number of post-smoothing steps to use on all levels.

snes - the SNES nonlinear multigrid context

n - the number of smoothing steps to use

-snes_fas_smoothup n - Sets number of pre-smoothing steps

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetNumberSmoothDown()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASSetNumberSmoothUp(SNES snes, PetscInt n)
```

Example 2 (unknown):
```unknown
SNESFASSetNumberSmoothDown()
```

---

## SNESFASSetRestriction#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASSetRestriction/

**Contents:**
- SNESFASSetRestriction#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Sets the matrix to be used to restrict the defect from level l to l-1.

snes - the SNESFAS nonlinear multigrid context

mat - the restriction matrix

level - the level (0 is coarsest) to supply [Do not supply 0]

Usually this is the same matrix used also to set the interpolation for the same level.

One can pass in the interpolation matrix or its transpose; PETSc figures out from the matrix dimensions which one it is.

If you do not set this, the transpose of the Mat set with SNESFASSetInterpolation() is used.

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetInterpolation(), SNESFASSetInjection()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASSetRestriction(SNES snes, PetscInt level, Mat mat)
```

Example 2 (unknown):
```unknown
SNESFASSetInterpolation()
```

Example 3 (unknown):
```unknown
SNESFASSetInjection()
```

---

## SNESFASSetRScale#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASSetRScale/

**Contents:**
- SNESFASSetRScale#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the scaling factor of the restriction operator from level l to l-1.

snes - the SNESFAS nonlinear multigrid context

rscale - the restriction scaling

level - the level (0 is coarsest) to supply [Do not supply 0]

This is only used when the injection is not set.

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESFASSetInjection(), SNESFASSetRestriction()

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASSetRScale(SNES snes, PetscInt level, Vec rscale)
```

Example 2 (unknown):
```unknown
SNESFASSetInjection()
```

Example 3 (unknown):
```unknown
SNESFASSetRestriction()
```

---

## SNESFASSetType#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFASSetType/

**Contents:**
- SNESFASSetType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the update and correction type used for SNESFAS.

snes - SNESFAS context

fastype - SNES_FAS_ADDITIVE, SNES_FAS_MULTIPLICATIVE, SNES_FAS_FULL, or SNES_FAS_KASKADE

SNES: Nonlinear Solvers, SNES, SNESFAS, PCMGSetType(), SNESFASGetType(), SNES_FAS_ADDITIVE, SNES_FAS_MULTIPLICATIVE, SNES_FAS_FULL, SNES_FAS_KASKADE

src/snes/impls/fas/fasfunc.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESFASSetType(SNES snes, SNESFASType fastype)
```

Example 2 (unknown):
```unknown
SNES_FAS_ADDITIVE
```

Example 3 (unknown):
```unknown
SNES_FAS_MULTIPLICATIVE
```

Example 4 (unknown):
```unknown
SNES_FAS_FULL
```

---

## SNESFASType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESFASType/

**Contents:**
- SNESFASType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Determines the type of nonlinear multigrid method that is run.

SNES_FAS_MULTIPLICATIVE (default) - traditional V or W cycle as determined by SNESFASSetCycles()

SNES_FAS_ADDITIVE - additive FAS cycle

SNES_FAS_FULL - full FAS cycle

SNES_FAS_KASKADE - Kaskade FAS cycle

SNES: Nonlinear Solvers, SNESFAS, PCMGSetType(), PCMGType

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  SNES_FAS_MULTIPLICATIVE,
  SNES_FAS_ADDITIVE,
  SNES_FAS_FULL,
  SNES_FAS_KASKADE
} SNESFASType;
```

Example 2 (unknown):
```unknown
SNES_FAS_MULTIPLICATIVE
```

Example 3 (unknown):
```unknown
SNESFASSetCycles()
```

Example 4 (unknown):
```unknown
SNES_FAS_ADDITIVE
```

---

## SNESFAS#

**URL:** https://petsc.org/release/manualpages/SNESFAS/SNESFAS/

**Contents:**
- SNESFAS#
- Options Database Keys and Prefixes#
- Note#
- References#
- See Also#
- Level#
- Location#

An implementation of the Full Approximation Scheme nonlinear multigrid solver, FAS, or nonlinear multigrid [BKST15] for solving nonlinear systems of equations with SNES. The nonlinear problem is solved by correction using coarse versions of the nonlinear problem. This problem is perturbed so that a projected solution of the fine problem elicits no correction from the coarse problem.

-snes_fas_levels l - The number of levels

-snes_fas_cycles (1|2) - The number of cycles – 1 for V, 2 for W

-snes_fas_type (additive|multiplicative|full|kaskade) - Additive or multiplicative cycle

-snes_fas_galerkin (true|false) - Form coarse problems by projection back upon the fine problem

-snes_fas_smoothup u - The number of iterations of the post-smoother

-snes_fas_smoothdown d - The number of iterations of the pre-smoother

-snes_fas_monitor - Monitor progress of all of the levels

-snes_fas_full_downsweep (true|false) - call the downsmooth on the initial downsweep of full FAS

-fas_levels_snes_ - prefix for SNES options for all smoothers

-fas_levels_cycle_snes_ - prefix for SNES options for all cycles

-fas_levels_i_snes_ - prefix SNES options for the smoothers on level i

-fas_levels_i_cycle_snes_ - prefix for SNES options for the cycle on level i

-fas_coarse_snes_ - prefix for SNES options for the coarsest smoother

The organization of the SNESFAS solver is slightly different from the organization of PCMG As each level has smoother SNES instances(down and potentially up) and a cycle SNES instance. The cycle SNES instance may be used for monitoring convergence on a particular level.

Peter R. Brune, Matthew G. Knepley, Barry F. Smith, and Xuemin Tu. Composing scalable nonlinear algebraic solvers. SIAM Review, 57(4):535–565, 2015. http://www.mcs.anl.gov/papers/P2010-0112.pdf. URL: http://www.mcs.anl.gov/papers/P2010-0112.pdf, doi:10.1137/130936725.

SNES: Nonlinear Solvers, PCMG, SNESCreate(), SNES, SNESSetType(), SNESType, SNESFASSetRestriction(), SNESFASSetInjection(), SNESFASFullGetTotal(), SNESFASSetType(), SNESFASGetType(), SNESFASSetLevels(), SNESFASGetLevels(), SNESFASGetCycleSNES(), SNESFASSetNumberSmoothUp(), SNESFASSetNumberSmoothDown(), SNESFASSetContinuation(), SNESFASSetCycles(), SNESFASSetMonitor(), SNESFASSetLog(), SNESFASCycleSetCycles(), SNESFASCycleGetSmoother(), SNESFASCycleGetSmootherUp(), SNESFASCycleGetSmootherDown(), SNESFASCycleGetCorrection(), SNESFASCycleGetInterpolation(), SNESFASCycleGetRestriction(), SNESFASCycleGetInjection(), SNESFASCycleGetRScale(), SNESFASCycleIsFine(), SNESFASSetInterpolation(), SNESFASGetInterpolation(), SNESFASGetRestriction(), SNESFASGetInjection(), SNESFASSetRScale(), SNESFASGetSmoother(), SNESFASGetSmootherDown(), SNESFASGetSmootherUp(), SNESFASGetCoarseSolve(), SNESFASFullSetDownSweep(), SNESFASFullSetTotal()

src/snes/impls/fas/fas.c

Index of all SNESFAS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESCreate()
```

Example 2 (unknown):
```unknown
SNESSetType()
```

Example 3 (unknown):
```unknown
SNESFASSetRestriction()
```

Example 4 (unknown):
```unknown
SNESFASSetInjection()
```

---

## SNESFinalizePackage#

**URL:** https://petsc.org/release/manualpages/SNES/SNESFinalizePackage/

**Contents:**
- SNESFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys everything in the PETSc interface to the SNES package. It is called from PetscFinalize().

SNES: Nonlinear Solvers, SNES, PetscFinalize()

src/snes/interface/dlregissnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
PetscErrorCode SNESFinalizePackage(void)
```

Example 3 (unknown):
```unknown
PetscFinalize()
```

---

## SNESFunctionFn#

**URL:** https://petsc.org/release/manualpages/SNES/SNESFunctionFn/

**Contents:**
- SNESFunctionFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

A prototype of a SNES evaluation function that would be passed to SNESSetFunction()

ctx - [optional] user-defined function context

SNES: Nonlinear Solvers, SNES, SNESSetFunction(), SNESGetFunction(), SNESJacobianFn, SNESNGSFn

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetFunction()
```

Example 2 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode SNESFunctionFn(SNES snes, Vec u, Vec F, PetscCtx ctx);
```

Example 3 (unknown):
```unknown
SNESSetFunction()
```

Example 4 (unknown):
```unknown
SNESGetFunction()
```

---

## SNESFunctionType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESFunctionType/

**Contents:**
- SNESFunctionType#
- Synopsis#
- Values#
- Note#
- See Also#
- Level#
- Location#

Type of function computed

SNES_FUNCTION_DEFAULT - the default behavior for the current SNESType

SNES_FUNCTION_UNPRECONDITIONED - the original function provided

SNES_FUNCTION_PRECONDITIONED - the modification of the function by the preconditioner

Support for these is dependent on the solver.

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESGetConvergedReason(), KSPSetNormType(), KSPSetConvergenceTest(), KSPSetPCSide()

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  SNES_FUNCTION_DEFAULT          = -1,
  SNES_FUNCTION_UNPRECONDITIONED = 0,
  SNES_FUNCTION_PRECONDITIONED   = 1
} SNESFunctionType;
```

Example 2 (unknown):
```unknown
SNES_FUNCTION_DEFAULT
```

Example 3 (unknown):
```unknown
SNES_FUNCTION_UNPRECONDITIONED
```

Example 4 (unknown):
```unknown
SNES_FUNCTION_PRECONDITIONED
```

---

## SNESGetAlwaysComputesFinalResidual#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetAlwaysComputesFinalResidual/

**Contents:**
- SNESGetAlwaysComputesFinalResidual#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

checks if the SNES always computes the residual at the final solution

snes - the SNES context

flg - PETSC_TRUE if the residual is computed

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESSolve(), SNESSetAlwaysComputesFinalResidual()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetAlwaysComputesFinalResidual(SNES snes, PetscBool *flg)
```

Example 2 (unknown):
```unknown
SNESSolve()
```

Example 3 (unknown):
```unknown
SNESSetAlwaysComputesFinalResidual()
```

---

## SNESGetApplicationContext#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetApplicationContext/

**Contents:**
- SNESGetApplicationContext#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Fortran Notes#
- See Also#
- Level#
- Location#
- Examples#

Gets the user-defined context for the nonlinear solvers set with SNESGetApplicationContext() or SNESSetComputeApplicationContext()

ctx - the application context

This only works when the context is a Fortran derived type or a PetscObject. Declare ctx with

SNES: Nonlinear Solvers, SNESSetApplicationContext(), SNESSetComputeApplicationContext()

src/snes/interface/snes.c

src/snes/tutorials/ex73f90t.F90 src/snes/tutorials/ex5f90.F90 src/snes/tutorials/ex5f90t.F90 src/snes/tutorials/ex58.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESGetApplicationContext()
```

Example 2 (unknown):
```unknown
SNESSetComputeApplicationContext()
```

Example 3 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetApplicationContext(SNES snes, PetscCtxRt ctx)
```

Example 4 (unknown):
```unknown
PetscObject
```

---

## SNESGetCheckJacobianDomainError#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetCheckJacobianDomainError/

**Contents:**
- SNESGetCheckJacobianDomainError#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get an indicator whether or not SNES is checking Jacobian domain errors after each Jacobian evaluation.

snes - the SNES context

flg - PETSC_FALSE indicates that it is not checking Jacobian domain errors after each Jacobian evaluation

SNES: Nonlinear Solvers, SNES, SNESCreate(), SNESSetFunction(), SNESFunctionFn, SNESSetFunctionDomainError(), SNESSetCheckJacobianDomainError()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetCheckJacobianDomainError(SNES snes, PetscBool *flg)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
SNESCreate()
```

Example 4 (unknown):
```unknown
SNESSetFunction()
```

---

## SNESGetConvergedReasonString#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetConvergedReasonString/

**Contents:**
- SNESGetConvergedReasonString#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Return a human readable string for SNESConvergedReason

snes - the SNES context

strreason - a human readable string that describes SNES converged reason

SNES: Nonlinear Solvers, SNES, SNESGetConvergedReason()

src/snes/interface/snes.c

src/snes/tutorials/ex6.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESConvergedReason
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetConvergedReasonString(SNES snes, const char **strreason)
```

Example 3 (unknown):
```unknown
SNESGetConvergedReason()
```

---

## SNESGetConvergedReason#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetConvergedReason/

**Contents:**
- SNESGetConvergedReason#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets the reason the SNES iteration was stopped, which may be due to convergence, divergence, or stagnation

snes - the SNES context

reason - negative value indicates diverged, positive value converged, see SNESConvergedReason for the individual convergence tests for complete lists

-snes_converged_reason - prints the reason to standard out

Should only be called after the call the SNESSolve() is complete, if it is called earlier it returns the value SNES__CONVERGED_ITERATING.

SNES: Nonlinear Solvers, SNESSolve(), SNESSetConvergenceTest(), SNESSetConvergedReason(), SNESConvergedReason, SNESGetConvergedReasonString()

src/snes/interface/snes.c

src/ts/tutorials/ex14.c src/snes/tutorials/ex6.c src/snes/tutorials/ex42.c src/snes/tutorials/ex2.c src/snes/tutorials/ex30.c src/ts/tutorials/ex48.c src/snes/tutorials/ex48.c src/snes/tutorials/ex15.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetConvergedReason(SNES snes, SNESConvergedReason *reason)
```

Example 2 (unknown):
```unknown
SNESConvergedReason
```

Example 3 (unknown):
```unknown
SNESSolve()
```

Example 4 (unknown):
```unknown
SNES__CONVERGED_ITERATING
```

---

## SNESGetConvergenceHistory#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetConvergenceHistory/

**Contents:**
- SNESGetConvergenceHistory#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- Fortran Notes#
- See Also#
- Level#
- Location#
- Examples#

Gets the arrays used to hold the convergence history.

snes - iterative context obtained from SNESCreate()

a - array to hold history, usually was set with SNESSetConvergenceHistory()

its - integer array holds the number of linear iterations (or negative if not converged) for each solve.

na - size of a and its

This routine is useful, e.g., when running a code for purposes of accurate performance monitoring, when no I/O should be done during the section of code that is being timed.

Return the arrays with ``SNESRestoreConvergenceHistory()`

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESSetConvergenceHistory()

src/snes/interface/snes.c

src/snes/tutorials/ex1f.F90

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetConvergenceHistory(SNES snes, PetscReal *a[], PetscInt *its[], PetscInt *na)
```

Example 2 (unknown):
```unknown
SNESCreate()
```

Example 3 (unknown):
```unknown
SNESSetConvergenceHistory()
```

Example 4 (julia):
```julia
PetscReal, pointer :: a(:)
  PetscInt, pointer :: its(:)
```

---

## SNESGetDivergenceTolerance#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetDivergenceTolerance/

**Contents:**
- SNESGetDivergenceTolerance#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Gets divergence tolerance used in divergence test.

snes - the SNES context

divtol - divergence tolerance

SNES: Nonlinear Solvers, SNES, SNESSetDivergenceTolerance()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetDivergenceTolerance(SNES snes, PetscReal *divtol)
```

Example 2 (unknown):
```unknown
SNESSetDivergenceTolerance()
```

---

## SNESGetDM#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetDM/

**Contents:**
- SNESGetDM#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Gets the DM that may be used by some SNES nonlinear solvers/preconditioners

Not Collective but dm obtained is parallel on snes

snes - the SNES context

SNES: Nonlinear Solvers, DM, SNES, SNESSetDM(), KSPSetDM(), KSPGetDM()

src/snes/interface/snes.c

src/snes/tutorials/ex5f90.F90 src/snes/tutorials/ex14.c src/snes/tutorials/ex18.c src/snes/tutorials/ex9.c src/snes/tutorials/ex12.c src/snes/tutorials/ex35.c src/snes/tutorials/ex48.c src/snes/tutorials/ex15.c src/snes/tutorials/ex22.c src/snes/tutorials/ex4.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetDM(SNES snes, DM *dm)
```

Example 2 (unknown):
```unknown
SNESSetDM()
```

---

## SNESGetErrorIfNotConverged#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetErrorIfNotConverged/

**Contents:**
- SNESGetErrorIfNotConverged#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Indicates if SNESSolve() will generate an error if the solver does not converge?

snes - iterative context obtained from SNESCreate()

flag - PETSC_TRUE if it will generate an error, else PETSC_FALSE

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESSetErrorIfNotConverged(), KSPGetErrorIfNotConverged(), KSPSetErrorIfNotConverged()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetErrorIfNotConverged(SNES snes, PetscBool *flag)
```

Example 3 (unknown):
```unknown
SNESCreate()
```

Example 4 (unknown):
```unknown
PETSC_FALSE
```

---

## SNESGetForceIteration#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetForceIteration/

**Contents:**
- SNESGetForceIteration#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Check whether or not SNESSolve() take at least one iteration regardless of the initial residual norm

snes - the SNES context

force - PETSC_TRUE requires at least one iteration.

SNES: Nonlinear Solvers, SNES, SNESSetForceIteration(), SNESSetDivergenceTolerance()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetForceIteration(SNES snes, PetscBool *force)
```

Example 3 (unknown):
```unknown
SNESSetForceIteration()
```

Example 4 (unknown):
```unknown
SNESSetDivergenceTolerance()
```

---

## SNESGetFunctionNorm#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetFunctionNorm/

**Contents:**
- SNESGetFunctionNorm#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the last computed norm of the residual

snes - the SNES context

norm - the last computed residual norm

SNES: Nonlinear Solvers, SNES, SNESSetNormSchedule(), SNESComputeFunction(), VecNorm(), SNESSetFunction(), SNESSetInitialFunction(), SNESNormSchedule

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetFunctionNorm(SNES snes, PetscReal *norm)
```

Example 2 (unknown):
```unknown
SNESSetNormSchedule()
```

Example 3 (unknown):
```unknown
SNESComputeFunction()
```

Example 4 (unknown):
```unknown
SNESSetFunction()
```

---

## SNESGetFunctionType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetFunctionType/

**Contents:**
- SNESGetFunctionType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Gets the SNESFunctionType used in convergence and monitoring set with SNESSetFunctionType() of the SNES method.

snes - the SNES context

type - the type of the function evaluation, see SNESSetFunctionType()

SNES: Nonlinear Solvers, SNESSetFunctionType(), SNESFunctionType, SNESSetNormSchedule(), SNESComputeFunction(), VecNorm(), SNESSetFunction(), SNESSetInitialFunction(), SNESNormSchedule

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESFunctionType
```

Example 2 (unknown):
```unknown
SNESSetFunctionType()
```

Example 3 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetFunctionType(SNES snes, SNESFunctionType *type)
```

Example 4 (unknown):
```unknown
SNESSetFunctionType()
```

---

## SNESGetFunction#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetFunction/

**Contents:**
- SNESGetFunction#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Returns the function that defines the nonlinear system set with SNESSetFunction()

Not Collective, but r is parallel if snes is parallel. Collective if r is requested, but has not been created yet.

snes - the SNES context

r - the vector that is used to store residuals (or NULL if you don’t want it)

f - the function (or NULL if you don’t want it); for calling sequence see SNESFunctionFn

ctx - the function context (or NULL if you don’t want it)

The vector r DOES NOT, in general, contain the current value of the SNES nonlinear function

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESSetFunction(), SNESGetSolution(), SNESFunctionFn

src/snes/interface/snes.c

src/snes/tutorials/ex21.c src/snes/tutorials/ex1.c src/ts/tutorials/ex30.c src/snes/tutorials/ex12.c src/ts/tutorials/ex48.c src/snes/tutorials/ex30.c src/snes/tutorials/ex22.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetFunction()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetFunction(SNES snes, Vec *r, SNESFunctionFn **f, PetscCtxRt ctx)
```

Example 3 (unknown):
```unknown
SNESFunctionFn
```

Example 4 (unknown):
```unknown
SNESSolve()
```

---

## SNESGetGridSequence#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetGridSequence/

**Contents:**
- SNESGetGridSequence#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

gets the number of steps of grid sequencing that SNES will do

snes - the SNES context

steps - the number of refinements to do, defaults to 0

SNES: Nonlinear Solvers, SNESGetLagPreconditioner(), SNESSetLagJacobian(), SNESGetLagJacobian(), SNESSetGridSequence()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetGridSequence(SNES snes, PetscInt *steps)
```

Example 2 (unknown):
```unknown
SNESGetLagPreconditioner()
```

Example 3 (unknown):
```unknown
SNESSetLagJacobian()
```

Example 4 (unknown):
```unknown
SNESGetLagJacobian()
```

---

## SNESGetIterationNumber#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetIterationNumber/

**Contents:**
- SNESGetIterationNumber#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Gets the number of nonlinear iterations completed in the current or most recent SNESSolve()

iter - iteration number

For example, during the computation of iteration 2 this would return 1.

This is useful for using lagged Jacobians (where one does not recompute the Jacobian at each SNES iteration). For example, the code

can be used in your function that computes the Jacobian to cause the Jacobian to be recomputed every second SNES iteration. See also SNESSetLagJacobian()

After the SNES solve is complete this will return the number of nonlinear iterations used.

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESSetLagJacobian(), SNESGetLinearSolveIterations(), SNESSetMonitor()

src/snes/interface/snes.c

src/snes/tutorials/ex5f90.F90 src/snes/tutorials/ex59.c src/snes/tutorials/ex6.c src/snes/tutorials/ex14.c src/snes/tutorials/ex18.c src/snes/tutorials/ex73f90t.F90 src/snes/tutorials/ex35.c src/snes/tutorials/ex46.c src/snes/tutorials/ex15.c src/snes/tutorials/ex21.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetIterationNumber(SNES snes, PetscInt *iter)
```

Example 3 (json):
```json
ierr = SNESGetIterationNumber(snes,&it);
      if (!(it % 2)) {
        [compute Jacobian here]
      }
```

Example 4 (unknown):
```unknown
SNESSetLagJacobian()
```

---

## SNESGetJacobian#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetJacobian/

**Contents:**
- SNESGetJacobian#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#

Returns the Jacobian matrix and optionally the user provided context for evaluating the Jacobian.

Not Collective, but Mat object will be parallel if SNES is

snes - the nonlinear solver context

Amat - location to stash (approximate) Jacobian matrix (or NULL)

Pmat - location to stash matrix used to compute the preconditioner (or NULL)

J - location to put Jacobian function (or NULL), for calling sequence see SNESJacobianFn

ctx - location to stash Jacobian ctx (or NULL)

SNES: Nonlinear Solvers, SNES, Mat, SNESSetJacobian(), SNESComputeJacobian(), SNESJacobianFn, SNESGetFunction()

src/snes/interface/snes.c

src/snes/tutorials/ex69.c src/snes/tutorials/ex62.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetJacobian(SNES snes, Mat *Amat, Mat *Pmat, SNESJacobianFn **J, PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
SNESJacobianFn
```

Example 3 (unknown):
```unknown
SNESSetJacobian()
```

Example 4 (unknown):
```unknown
SNESComputeJacobian()
```

---

## SNESGetKSP#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetKSP/

**Contents:**
- SNESGetKSP#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Returns the KSP context for a SNES solver.

Not Collective, but if snes is parallel, then ksp is parallel

snes - the SNES context

ksp - the KSP context

The user can then directly manipulate the KSP context to set various options, etc. Likewise, the user can then extract and manipulate the PC contexts as well.

Some SNESTypes do not use a KSP but a KSP is still returned by this function, changes to that KSP will have no effect.

SNES: Nonlinear Solvers, SNES, KSP, PC, KSPGetPC(), SNESCreate(), KSPCreate(), SNESSetKSP()

src/snes/interface/snes.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex99.c src/snes/tutorials/ex55.c src/snes/tutorials/ex1.c src/snes/tutorials/ex6.c src/snes/tutorials/ex12.c src/snes/tutorials/ex30.c src/snes/tutorials/ex69.c src/snes/tutorials/ex3.c src/snes/tutorials/ex31.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetKSP(SNES snes, KSP *ksp)
```

Example 2 (unknown):
```unknown
SNESCreate()
```

Example 3 (unknown):
```unknown
KSPCreate()
```

Example 4 (unknown):
```unknown
SNESSetKSP()
```

---

## SNESGetLagJacobian#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetLagJacobian/

**Contents:**
- SNESGetLagJacobian#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Get how often the Jacobian is rebuilt. See SNESGetLagPreconditioner() to determine when the preconditioner is rebuilt

snes - the SNES context

lag - -1 indicates NEVER rebuild, 1 means rebuild every time the Jacobian is computed within a single nonlinear solve, 2 means every second time the Jacobian is built etc.

The jacobian is ALWAYS built in the first iteration of a nonlinear solve unless lag is -1 or SNESSetLagJacobianPersists() was called.

SNES: Nonlinear Solvers, SNES, SNESSetLagJacobian(), SNESSetLagPreconditioner(), SNESGetLagPreconditioner(), SNESSetLagJacobianPersists(), SNESSetLagPreconditionerPersists()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESGetLagPreconditioner()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetLagJacobian(SNES snes, PetscInt *lag)
```

Example 3 (unknown):
```unknown
SNESSetLagJacobianPersists()
```

Example 4 (unknown):
```unknown
SNESSetLagJacobian()
```

---

## SNESGetLinearSolveFailures#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetLinearSolveFailures/

**Contents:**
- SNESGetLinearSolveFailures#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Gets the number of failed (non-converged) linear solvers in the current or most recent SNESSolve()

nfails - number of failed solves

-snes_max_linear_solve_fail num - The number of failures before the solve is terminated

This counter is reset to zero for each successive call to SNESSolve().

SNES: Nonlinear Solvers, SNESGetMaxLinearSolveFailures(), SNESGetLinearSolveIterations(), SNESSetMaxLinearSolveFailures()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetLinearSolveFailures(SNES snes, PetscInt *nfails)
```

Example 3 (unknown):
```unknown
SNESSolve()
```

Example 4 (unknown):
```unknown
SNESGetMaxLinearSolveFailures()
```

---

## SNESGetLinearSolveIterations#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetLinearSolveIterations/

**Contents:**
- SNESGetLinearSolveIterations#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Gets the total number of linear iterations used by the nonlinear solver in the most recent SNESSolve()

lits - number of linear iterations

This counter is reset to zero for each successive call to SNESSolve() unless SNESSetCountersReset() is used.

If the linear solver fails inside the SNESSolve() the iterations for that call to the linear solver are not included. If you wish to count them then call KSPGetIterationNumber() after the failed solve.

SNES: Nonlinear Solvers, SNES, SNESGetIterationNumber(), SNESGetLinearSolveFailures(), SNESGetMaxLinearSolveFailures(), SNESSetCountersReset()

src/snes/interface/snes.c

src/ts/tutorials/ex14.c src/snes/tutorials/ex55.c src/ts/tutorials/ex30.c src/snes/tutorials/ex18.c src/snes/tutorials/ex5.c src/ts/tutorials/ex24.c src/snes/tutorials/ex48.c src/snes/tutorials/ex25.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetLinearSolveIterations(SNES snes, PetscInt *lits)
```

Example 3 (unknown):
```unknown
SNESSolve()
```

Example 4 (unknown):
```unknown
SNESSetCountersReset()
```

---

## SNESGetLineSearch#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetLineSearch/

**Contents:**
- SNESGetLineSearch#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Returns the line search associated with the SNES.

snes - iterative context obtained from SNESCreate()

linesearch - linesearch context

It creates a default line search instance which can be configured as needed in case it has not been already set with SNESSetLineSearch().

You can also use the options database keys -snes_linesearch_* to configure the line search. See SNESLineSearchSetFromOptions() for the possible options.

SNES: Nonlinear Solvers, SNESLineSearch, SNESSetLineSearch(), SNESLineSearchCreate(), SNESLineSearchSetFromOptions()

src/snes/interface/snes.c

src/snes/tutorials/ex1f.F90 src/ts/tutorials/ex27.c src/ts/tutorials/ex22.c src/snes/tutorials/ex15.c src/snes/tutorials/ex3.c src/ts/tutorials/ex22f.F90 src/ts/utils/dmplexlandau/tutorials/ex1f90.F90

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetLineSearch(SNES snes, SNESLineSearch *linesearch)
```

Example 2 (unknown):
```unknown
SNESCreate()
```

Example 3 (unknown):
```unknown
SNESSetLineSearch()
```

Example 4 (unknown):
```unknown
-snes_linesearch_*
```

---

## SNESGetMaxLinearSolveFailures#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetMaxLinearSolveFailures/

**Contents:**
- SNESGetMaxLinearSolveFailures#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

gets the maximum number of linear solve failures that are allowed before SNES returns as unsuccessful

maxFails - maximum of unsuccessful solves allowed

By default this is 1; that is SNES returns on the first failed linear solve

SNES: Nonlinear Solvers, SNESSetErrorIfNotConverged(), SNESGetLinearSolveFailures(), SNESGetLinearSolveIterations(), SNESSetMaxLinearSolveFailures()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetMaxLinearSolveFailures(SNES snes, PetscInt *maxFails)
```

Example 2 (unknown):
```unknown
SNESSetErrorIfNotConverged()
```

Example 3 (unknown):
```unknown
SNESGetLinearSolveFailures()
```

Example 4 (unknown):
```unknown
SNESGetLinearSolveIterations()
```

---

## SNESGetMaxNonlinearStepFailures#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetMaxNonlinearStepFailures/

**Contents:**
- SNESGetMaxNonlinearStepFailures#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the maximum number of unsuccessful steps attempted by the nonlinear solver before it gives up and returns unconverged or generates an error

maxFails - maximum of unsuccessful steps

SNES: Nonlinear Solvers, SNESSetErrorIfNotConverged(), SNESGetMaxLinearSolveFailures(), SNESGetLinearSolveIterations(), SNESSetMaxLinearSolveFailures(), SNESGetLinearSolveFailures(), SNESSetMaxNonlinearStepFailures(), SNESGetNonlinearStepFailures()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetMaxNonlinearStepFailures(SNES snes, PetscInt *maxFails)
```

Example 2 (unknown):
```unknown
SNESSetErrorIfNotConverged()
```

Example 3 (unknown):
```unknown
SNESGetMaxLinearSolveFailures()
```

Example 4 (unknown):
```unknown
SNESGetLinearSolveIterations()
```

---

## SNESGetNGS#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetNGS/

**Contents:**
- SNESGetNGS#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Returns the function and context set with SNESSetNGS()

snes - the SNES context

f - the function (or NULL) see SNESNGSFn for calling sequence

ctx - the function context (or NULL)

SNES: Nonlinear Solvers, SNESSetNGS(), SNESGetFunction(), SNESNGSFn

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetNGS()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetNGS(SNES snes, SNESNGSFn **f, PetscCtxRt ctx)
```

Example 3 (unknown):
```unknown
SNESSetNGS()
```

Example 4 (unknown):
```unknown
SNESGetFunction()
```

---

## SNESGetNonlinearStepFailures#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetNonlinearStepFailures/

**Contents:**
- SNESGetNonlinearStepFailures#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Gets the number of unsuccessful steps taken by the nonlinear solver in the current or most recent SNESSolve() .

nfails - number of unsuccessful steps attempted

A failed step is a step that was generated and taken but did not satisfy the requested step criteria. For example, the SNESLineSearchApply() could not generate a sufficient decrease in the function norm (in fact it may have produced an increase).

Taken steps that produce a infinity or NaN in the function evaluation or generate a SNESSetFunctionDomainError() will always immediately terminate the SNESSolve() regardless of the value of maxFails.

SNESSetMaxNonlinearStepFailures() determines how many unsuccessful steps are allowed before the SNESSolve() terminates

This counter is reset to zero for each successive call to SNESSolve().

SNES: Nonlinear Solvers, SNES, SNESGetMaxLinearSolveFailures(), SNESGetLinearSolveIterations(), SNESSetMaxLinearSolveFailures(), SNESGetLinearSolveFailures(), SNESSetMaxNonlinearStepFailures(), SNESGetMaxNonlinearStepFailures()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetNonlinearStepFailures(SNES snes, PetscInt *nfails)
```

Example 3 (unknown):
```unknown
SNESLineSearchApply()
```

Example 4 (unknown):
```unknown
SNESSetFunctionDomainError()
```

---

## SNESGetNormSchedule#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetNormSchedule/

**Contents:**
- SNESGetNormSchedule#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Gets the SNESNormSchedule used in convergence and monitoring of the SNES method.

snes - the SNES context

normschedule - the type of the norm used

SNES: Nonlinear Solvers, SNES, SNESSetNormSchedule(), SNESComputeFunction(), VecNorm(), SNESSetFunction(), SNESSetInitialFunction(), SNESNormSchedule

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESNormSchedule
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetNormSchedule(SNES snes, SNESNormSchedule *normschedule)
```

Example 3 (unknown):
```unknown
SNESSetNormSchedule()
```

Example 4 (unknown):
```unknown
SNESComputeFunction()
```

---

## SNESGetNPCFunction#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetNPCFunction/

**Contents:**
- SNESGetNPCFunction#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Gets the current function value (for the callback function provided by SNESSetFunction(), and its norm from a nonlinear preconditioner after SNESSolve() has been called on that SNES

snes - the SNES context

fnorm - the norm of F

SNES: Nonlinear Solvers, SNES, SNESGetNPC(), SNESSetNPC(), SNESComputeFunction(), SNESApplyNPC(), SNESSolve()

src/snes/interface/snespc.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetFunction()
```

Example 2 (unknown):
```unknown
SNESSolve()
```

Example 3 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESGetNPCFunction(SNES snes, Vec F, PetscReal *fnorm)
```

Example 4 (unknown):
```unknown
SNESGetNPC()
```

---

## SNESGetNPCSide#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetNPCSide/

**Contents:**
- SNESGetNPCSide#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the preconditioning side used by the nonlinear preconditioner inside SNES.

snes - iterative context obtained from SNESCreate()

side - the preconditioning side, where side is one of

SNES: Nonlinear Solvers, SNES, SNESGetNPC(), SNESSetNPCSide(), KSPGetPCSide(), PC_LEFT, PC_RIGHT, PCSide

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetNPCSide(SNES snes, PCSide *side)
```

Example 2 (unknown):
```unknown
SNESCreate()
```

Example 3 (unknown):
```unknown
`PC_LEFT` - left preconditioning
      `PC_RIGHT` - right preconditioning (default for most nonlinear solvers)
```

Example 4 (unknown):
```unknown
SNESGetNPC()
```

---

## SNESGetNPC#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetNPC/

**Contents:**
- SNESGetNPC#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Gets a nonlinear preconditioning solver SNES` to be used to precondition the original nonlinear solver.

Not Collective; but any changes to the obtained the pc object must be applied collectively

snes - iterative context obtained from SNESCreate()

pc - the SNES preconditioner context

-npc_snes_type type - set the type of the SNES to use as the nonlinear preconditioner

If a SNES was previously set with SNESSetNPC() then that value is returned, otherwise a new SNES object is created that will be used as the nonlinear preconditioner for the current SNES.

The (preconditioner) SNES returned automatically inherits the same nonlinear function and Jacobian supplied to the original SNES. These may be overwritten if needed.

Use the options database prefixes -npc_snes, -npc_ksp, etc., to control the configuration of the nonlinear preconditioner

SNES: Nonlinear Solvers, SNESSetNPC(), SNESHasNPC(), SNES, SNESCreate()

src/snes/interface/snes.c

src/snes/tutorials/ex35.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetNPC(SNES snes, SNES *pc)
```

Example 2 (unknown):
```unknown
SNESCreate()
```

Example 3 (unknown):
```unknown
SNESSetNPC()
```

Example 4 (unknown):
```unknown
SNESSetNPC()
```

---

## SNESGetNumberFunctionEvals#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetNumberFunctionEvals/

**Contents:**
- SNESGetNumberFunctionEvals#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets the number of user provided function evaluations done by the SNES object in the current or most recent SNESSolve()

nfuncs - number of evaluations

Reset every time SNESSolve() is called unless SNESSetCountersReset() is used.

SNES: Nonlinear Solvers, SNES, SNESGetMaxLinearSolveFailures(), SNESGetLinearSolveIterations(), SNESSetMaxLinearSolveFailures(), SNESGetLinearSolveFailures(), SNESSetCountersReset()

src/snes/interface/snes.c

src/ts/tutorials/ex30.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetNumberFunctionEvals(SNES snes, PetscInt *nfuncs)
```

Example 3 (unknown):
```unknown
SNESSolve()
```

Example 4 (unknown):
```unknown
SNESSetCountersReset()
```

---

## SNESGetObjective#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetObjective/

**Contents:**
- SNESGetObjective#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Returns the objective function set with SNESSetObjective()

snes - the SNES context

obj - objective evaluation routine (or NULL); see SNESObjectiveFn for the calling sequence

ctx - the function context (or NULL)

SNES: Nonlinear Solvers, SNES, SNESSetObjective(), SNESGetSolution(), SNESObjectiveFn

src/snes/interface/snesob.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetObjective()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESGetObjective(SNES snes, SNESObjectiveFn **obj, PetscCtxRt ctx)
```

Example 3 (unknown):
```unknown
SNESObjectiveFn
```

Example 4 (unknown):
```unknown
SNESSetObjective()
```

---

## SNESGetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetOptionsPrefix/

**Contents:**
- SNESGetOptionsPrefix#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the prefix used for searching for all SNES options in the database.

snes - the SNES context

prefix - pointer to the prefix string used

SNES: Nonlinear Solvers, SNES, SNESSetOptionsPrefix(), SNESAppendOptionsPrefix()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetOptionsPrefix(SNES snes, const char *prefix[])
```

Example 2 (unknown):
```unknown
SNESSetOptionsPrefix()
```

Example 3 (unknown):
```unknown
SNESAppendOptionsPrefix()
```

---

## SNESGetPicard#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetPicard/

**Contents:**
- SNESGetPicard#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Returns the context for the Picard iteration

Not Collective, but Vec is parallel if SNES is parallel. Collective if Vec is requested, but has not been created yet.

snes - the SNES context

r - the function (or NULL)

f - the function (or NULL); for calling sequence see SNESFunctionFn

Amat - the matrix used to defined the operation A(x) x - b(x) (or NULL)

Pmat - the matrix from which the preconditioner will be constructed (or NULL)

J - the function for matrix evaluation (or NULL); for calling sequence see SNESJacobianFn

ctx - the function context (or NULL)

SNES: Nonlinear Solvers, SNESSetFunction(), SNESSetPicard(), SNESGetFunction(), SNESGetJacobian(), SNESGetDM(), SNESFunctionFn, SNESJacobianFn

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetPicard(SNES snes, Vec *r, SNESFunctionFn **f, Mat *Amat, Mat *Pmat, SNESJacobianFn **J, PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
SNESFunctionFn
```

Example 3 (unknown):
```unknown
SNESJacobianFn
```

Example 4 (unknown):
```unknown
SNESSetFunction()
```

---

## SNESGetRhs#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetRhs/

**Contents:**
- SNESGetRhs#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the vector for solving F(x) = rhs. If rhs is not set it assumes a zero right-hand side.

snes - the SNES context

rhs - the right-hand side vector or NULL if there is no right-hand side vector

SNES: Nonlinear Solvers, SNES, SNESGetSolution(), SNESGetFunction(), SNESComputeFunction(), SNESSetJacobian(), SNESSetFunction()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetRhs(SNES snes, Vec *rhs)
```

Example 2 (unknown):
```unknown
SNESGetSolution()
```

Example 3 (unknown):
```unknown
SNESGetFunction()
```

Example 4 (unknown):
```unknown
SNESComputeFunction()
```

---

## SNESGetSolutionNorm#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetSolutionNorm/

**Contents:**
- SNESGetSolutionNorm#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the last computed norm of the solution

snes - the SNES context

xnorm - the last computed solution norm

SNES: Nonlinear Solvers, SNES, SNESSetNormSchedule(), SNESComputeFunction(), SNESGetFunctionNorm(), SNESGetUpdateNorm()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetSolutionNorm(SNES snes, PetscReal *xnorm)
```

Example 2 (unknown):
```unknown
SNESSetNormSchedule()
```

Example 3 (unknown):
```unknown
SNESComputeFunction()
```

Example 4 (unknown):
```unknown
SNESGetFunctionNorm()
```

---

## SNESGetSolutionUpdate#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetSolutionUpdate/

**Contents:**
- SNESGetSolutionUpdate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the vector where the solution update is stored.

Not Collective, but x is parallel if snes is parallel

snes - the SNES context

x - the solution update

SNES: Nonlinear Solvers, SNES, SNESGetSolution(), SNESGetFunction()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetSolutionUpdate(SNES snes, Vec *x)
```

Example 2 (unknown):
```unknown
SNESGetSolution()
```

Example 3 (unknown):
```unknown
SNESGetFunction()
```

---

## SNESGetSolution#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetSolution/

**Contents:**
- SNESGetSolution#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Returns the vector where the approximate solution is stored. This is the fine grid solution when using SNESSetGridSequence().

Not Collective, but x is parallel if snes is parallel

snes - the SNES context

SNES: Nonlinear Solvers, SNESSetSolution(), SNESSolve(), SNES, SNESGetSolutionUpdate(), SNESGetFunction()

src/snes/interface/snes.c

src/snes/tutorials/ex9.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex26.c src/snes/tutorials/ex22.c src/snes/tutorials/ex17.c src/snes/tutorials/ex48.c src/snes/tutorials/ex23.c src/snes/tutorials/ex21.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetGridSequence()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetSolution(SNES snes, Vec *x)
```

Example 3 (unknown):
```unknown
SNESSetSolution()
```

Example 4 (unknown):
```unknown
SNESSolve()
```

---

## SNESGetTolerances#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetTolerances/

**Contents:**
- SNESGetTolerances#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Gets various parameters used in SNES convergence tests.

snes - the SNES context

atol - the absolute convergence tolerance

rtol - the relative convergence tolerance

stol - convergence tolerance in terms of the norm of the change in the solution between steps

maxit - the maximum number of iterations allowed

maxf - the maximum number of function evaluations allowed, PETSC_UNLIMITED indicates no bound

See SNESSetTolerances() for details on the parameters.

The user can specify NULL for any parameter that is not needed.

SNES: Nonlinear Solvers, SNES, SNESSetTolerances()

src/snes/interface/snes.c

src/snes/tutorials/ex3.c src/snes/tutorials/ex35.c src/snes/tutorials/ex3k.kokkos.cxx src/snes/tutorials/ex2.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetTolerances(SNES snes, PetscReal *atol, PetscReal *rtol, PetscReal *stol, PetscInt *maxit, PetscInt *maxf)
```

Example 2 (unknown):
```unknown
PETSC_UNLIMITED
```

Example 3 (unknown):
```unknown
SNESSetTolerances()
```

Example 4 (unknown):
```unknown
SNESSetTolerances()
```

---

## SNESGetType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetType/

**Contents:**
- SNESGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets the SNES method type and name (as a string).

snes - nonlinear solver context

type - SNES method (a character string)

type should not be retained for later use as it will be an invalid pointer if the SNESType of snes is changed.

SNES: Nonlinear Solvers, SNESSetType(), SNESType, SNESSetFromOptions(), SNES, PetscObjectTypeCompare(), PetscObjectTypeCompareAny()

src/snes/interface/snes.c

src/snes/tutorials/ex3.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetType(SNES snes, SNESType *type)
```

Example 2 (unknown):
```unknown
SNESSetType()
```

Example 3 (unknown):
```unknown
SNESSetFromOptions()
```

Example 4 (unknown):
```unknown
PetscObjectTypeCompare()
```

---

## SNESGetUpdateNorm#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetUpdateNorm/

**Contents:**
- SNESGetUpdateNorm#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the last computed norm of the solution update

snes - the SNES context

ynorm - the last computed update norm

The new solution is the current solution plus the update, so this norm is an indication of the size of the update

SNES: Nonlinear Solvers, SNES, SNESSetNormSchedule(), SNESComputeFunction(), SNESGetFunctionNorm()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetUpdateNorm(SNES snes, PetscReal *ynorm)
```

Example 2 (unknown):
```unknown
SNESSetNormSchedule()
```

Example 3 (unknown):
```unknown
SNESComputeFunction()
```

Example 4 (unknown):
```unknown
SNESGetFunctionNorm()
```

---

## SNESGetUseMatrixFree#

**URL:** https://petsc.org/release/manualpages/SNES/SNESGetUseMatrixFree/

**Contents:**
- SNESGetUseMatrixFree#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

indicates if the SNES uses matrix-free finite difference matrix vector products to apply the Jacobian.

Not Collective, but the resulting flags will be the same on all MPI processes

mf_operator - use matrix-free only for the Amat used by SNESSetJacobian(), this means the user provided Pmat will continue to be used

mf - use matrix-free for both the Amat and Pmat used by SNESSetJacobian(), both the Amat and Pmat set in SNESSetJacobian() will be ignored

SNES: Nonlinear Solvers, SNES, SNESSetUseMatrixFree(), MatCreateSNESMF()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESGetUseMatrixFree(SNES snes, PetscBool *mf_operator, PetscBool *mf)
```

Example 2 (unknown):
```unknown
SNESSetJacobian()
```

Example 3 (unknown):
```unknown
SNESSetJacobian()
```

Example 4 (unknown):
```unknown
SNESSetJacobian()
```

---

## SNESHasNPC#

**URL:** https://petsc.org/release/manualpages/SNES/SNESHasNPC/

**Contents:**
- SNESHasNPC#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns whether a nonlinear preconditioner is associated with the given SNES

snes - iterative context obtained from SNESCreate()

has_npc - whether the SNES has a nonlinear preconditioner or not

SNES: Nonlinear Solvers, SNESSetNPC(), SNESGetNPC()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESHasNPC(SNES snes, PetscBool *has_npc)
```

Example 2 (unknown):
```unknown
SNESCreate()
```

Example 3 (unknown):
```unknown
SNESSetNPC()
```

Example 4 (unknown):
```unknown
SNESGetNPC()
```

---

## SNESInitialGuessFn#

**URL:** https://petsc.org/release/manualpages/SNES/SNESInitialGuessFn/

**Contents:**
- SNESInitialGuessFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

A prototype of a SNES compute initial guess function that would be passed to SNESSetComputeInitialGuess()

u - output vector to contain initial guess

ctx - [optional] user-defined function context

SNES: Nonlinear Solvers, SNES, SNESSetComputeInitialGuess(), SNESSetFunction(), SNESGetFunction(), SNESJacobianFn, SNESFunctionFn

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetComputeInitialGuess()
```

Example 2 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode SNESInitialGuessFn(SNES snes, Vec u, PetscCtx ctx);
```

Example 3 (unknown):
```unknown
SNESSetComputeInitialGuess()
```

Example 4 (unknown):
```unknown
SNESSetFunction()
```

---

## SNESInitializePackage#

**URL:** https://petsc.org/release/manualpages/SNES/SNESInitializePackage/

**Contents:**
- SNESInitializePackage#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#

This function initializes everything in the SNES package. It is called from PetscDLLibraryRegister_petscsnes() when using dynamic libraries, and on the first call to SNESCreate() when using shared or static libraries.

This function never needs to be called by PETSc users.

SNES: Nonlinear Solvers, SNES, PetscInitialize()

src/snes/interface/dlregissnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESCreate()
```

Example 2 (unknown):
```unknown
PetscErrorCode SNESInitializePackage(void)
```

Example 3 (unknown):
```unknown
PetscInitialize()
```

---

## SNESJacobianFn#

**URL:** https://petsc.org/release/manualpages/SNES/SNESJacobianFn/

**Contents:**
- SNESJacobianFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

A prototype of a SNES Jacobian evaluation function that would be passed to SNESSetJacobian()

snes - the SNES context obtained from SNESCreate()

Amat - (approximate) Jacobian matrix

Pmat - matrix used to construct the preconditioner, often the same as Amat

ctx - [optional] user-defined context for matrix evaluation routine

SNES: Nonlinear Solvers, SNES, SNESSetJacobian(), SNESGetJacobian(), SNESFunctionFn, SNESNGSFn

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetJacobian()
```

Example 2 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode SNESJacobianFn(SNES snes, Vec u, Mat Amat, Mat Pmat, PetscCtx ctx);
```

Example 3 (unknown):
```unknown
SNESCreate()
```

Example 4 (unknown):
```unknown
SNESSetJacobian()
```

---

## SNESKSPGetParametersEW#

**URL:** https://petsc.org/release/manualpages/SNES/SNESKSPGetParametersEW/

**Contents:**
- SNESKSPGetParametersEW#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Gets parameters for Eisenstat-Walker convergence criteria for the linear solvers within an inexact Newton method.

version - version 1, 2 (default is 2), 3 or 4

rtol_0 - initial relative tolerance (0 <= rtol_0 < 1)

rtol_max - maximum relative tolerance (0 <= rtol_max < 1)

gamma - multiplicative factor for version 2 rtol computation (0 <= gamma2 <= 1)

alpha - power for version 2 rtol computation (1 < alpha <= 2)

alpha2 - power for safeguard

threshold - threshold for imposing safeguard (0 < threshold < 1)

SNES: Nonlinear Solvers, SNES, SNESKSPSetUseEW(), SNESKSPGetUseEW(), SNESKSPSetParametersEW()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESKSPGetParametersEW(SNES snes, PetscInt *version, PetscReal *rtol_0, PetscReal *rtol_max, PetscReal *gamma, PetscReal *alpha, PetscReal *alpha2, PetscReal *threshold)
```

Example 2 (unknown):
```unknown
SNESKSPSetUseEW()
```

Example 3 (unknown):
```unknown
SNESKSPGetUseEW()
```

Example 4 (unknown):
```unknown
SNESKSPSetParametersEW()
```

---

## SNESKSPGetUseEW#

**URL:** https://petsc.org/release/manualpages/SNES/SNESKSPGetUseEW/

**Contents:**
- SNESKSPGetUseEW#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets if SNES is using Eisenstat-Walker method for computing relative tolerance for linear solvers within an inexact Newton method.

flag - PETSC_TRUE or PETSC_FALSE

SNES: Nonlinear Solvers, SNESKSPSetUseEW(), SNESKSPGetParametersEW(), SNESKSPSetParametersEW()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESKSPGetUseEW(SNES snes, PetscBool *flag)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
SNESKSPSetUseEW()
```

Example 4 (unknown):
```unknown
SNESKSPGetParametersEW()
```

---

## SNESKSPONLY#

**URL:** https://petsc.org/release/manualpages/SNES/SNESKSPONLY/

**Contents:**
- SNESKSPONLY#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Nonlinear solver that performs one Newton step with KSPSolve() and does not compute any norms.

The main purpose of this solver is to solve linear problems using the SNES interface, without any additional overhead in the form of vector norm operations.

Use SNESKSPTRANSPOSEONLY for solving transposed systems.

SNES: Nonlinear Solvers, SNES, SNESType, SNESKSPTRANSPOSEONLY, SNESCreate(), SNESSetType(), SNESNEWTONLS, SNESNEWTONTR

src/snes/impls/ksponly/ksponly.c

src/snes/tutorials/ex64.c src/snes/tutorials/ex11.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESKSPTRANSPOSEONLY
```

Example 2 (unknown):
```unknown
SNESKSPTRANSPOSEONLY
```

Example 3 (unknown):
```unknown
SNESCreate()
```

Example 4 (unknown):
```unknown
SNESSetType()
```

---

## SNESKSPSetParametersEW#

**URL:** https://petsc.org/release/manualpages/SNES/SNESKSPSetParametersEW/

**Contents:**
- SNESKSPSetParametersEW#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Sets parameters for Eisenstat-Walker convergence criteria for the linear solvers within an inexact Newton method.

version - version 1, 2 (default is 2), 3 or 4

rtol_0 - initial relative tolerance (0 <= rtol_0 < 1)

rtol_max - maximum relative tolerance (0 <= rtol_max < 1)

gamma - multiplicative factor for version 2 rtol computation (0 <= gamma2 <= 1)

alpha - power for version 2 rtol computation (1 < alpha <= 2)

alpha2 - power for safeguard

threshold - threshold for imposing safeguard (0 < threshold < 1)

Version 3 was contributed by Luis Chacon, June 2006.

Use PETSC_CURRENT to retain the default for any of the parameters.

SNES: Nonlinear Solvers, SNES, SNESKSPSetUseEW(), SNESKSPGetUseEW(), SNESKSPGetParametersEW()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESKSPSetParametersEW(SNES snes, PetscInt version, PetscReal rtol_0, PetscReal rtol_max, PetscReal gamma, PetscReal alpha, PetscReal alpha2, PetscReal threshold)
```

Example 2 (unknown):
```unknown
PETSC_CURRENT
```

Example 3 (unknown):
```unknown
SNESKSPSetUseEW()
```

Example 4 (unknown):
```unknown
SNESKSPGetUseEW()
```

---

## SNESKSPSetUseEW#

**URL:** https://petsc.org/release/manualpages/SNES/SNESKSPSetUseEW/

**Contents:**
- SNESKSPSetUseEW#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Note#
- References#
- See Also#
- Level#
- Location#

Sets SNES to the use Eisenstat-Walker method for computing relative tolerance for linear solvers within an inexact Newton method.

flag - PETSC_TRUE or PETSC_FALSE

-snes_ksp_ew - use Eisenstat-Walker method for determining linear system convergence

-snes_ksp_ew_version ver - version of Eisenstat-Walker method

-snes_ksp_ew_rtol0 rtol0 - Sets rtol0

-snes_ksp_ew_rtolmax rtolmax - Sets rtolmax

-snes_ksp_ew_gamma gamma - Sets gamma

-snes_ksp_ew_alpha alpha - Sets alpha

-snes_ksp_ew_alpha2 alpha2 - Sets alpha2

-snes_ksp_ew_threshold threshold - Sets threshold

The default is to use a constant relative tolerance for the inner linear solvers. Alternatively, one can use the Eisenstat-Walker method [EW96], where the relative convergence tolerance is reset at each Newton iteration according progress of the nonlinear solver.

S. C. Eisenstat and H. F. Walker. Choosing the forcing terms in an inexact Newton method. SIAM J. Scientific Computing, 17:16–32, 1996.

SNES: Nonlinear Solvers, KSP, SNES, SNESKSPGetUseEW(), SNESKSPGetParametersEW(), SNESKSPSetParametersEW()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESKSPSetUseEW(SNES snes, PetscBool flag)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
SNESKSPGetUseEW()
```

Example 4 (unknown):
```unknown
SNESKSPGetParametersEW()
```

---

## SNESKSPTRANSPOSEONLY#

**URL:** https://petsc.org/release/manualpages/SNES/SNESKSPTRANSPOSEONLY/

**Contents:**
- SNESKSPTRANSPOSEONLY#
- Notes#
- See Also#
- Level#
- Location#

Nonlinear solver that performs one linear solve with KSPSolveTranspose() and does not compute any norms.

The main purpose of this solver is to solve transposed linear problems using the SNES interface, without any additional overhead in the form of vector operations within adjoint solvers.

Use SNESKSPONLY for solving non-transposed systems.

SNES: Nonlinear Solvers, SNES, SNESType, SNESKSPONLY, SNESCreate(), SNESSetType(), SNESNEWTONLS, SNESNEWTONTR

src/snes/impls/ksponly/ksponly.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
KSPSolveTranspose()
```

Example 2 (unknown):
```unknown
SNESKSPONLY
```

Example 3 (unknown):
```unknown
SNESKSPONLY
```

Example 4 (unknown):
```unknown
SNESCreate()
```

---

## SNESLineSearchAppendOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchAppendOptionsPrefix/

**Contents:**
- SNESLineSearchAppendOptionsPrefix#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Appends to the prefix used for searching for all SNESLineSearch options in the database.

linesearch - the SNESLineSearch context

prefix - the prefix to prepend to all option names

A hyphen (-) must NOT be given at the beginning of the prefix name. The first character of all runtime options is AUTOMATICALLY the hyphen.

SNES: Nonlinear Solvers, SNES, SNESLineSearch(), SNESLineSearchSetFromOptions(), SNESGetOptionsPrefix()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLineSearch
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchAppendOptionsPrefix(SNESLineSearch linesearch, const char prefix[])
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
SNESLineSearch()
```

---

## SNESLineSearchApplyFn#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchApplyFn/

**Contents:**
- SNESLineSearchApplyFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

Function type for a SNESLineSearch implementation’s apply routine

ls - the SNESLineSearch object whose internal state holds the current step, search direction and other data

SNESLineSearch, SNESLineSearchType, SNESLineSearchSetType(), SNESLineSearchShellApplyFn

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLineSearch
```

Example 2 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode         SNESLineSearchApplyFn(SNESLineSearch ls);
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
SNESLineSearch
```

---

## SNESLineSearchApply#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchApply/

**Contents:**
- SNESLineSearchApply#
- Synopsis#
- Input Parameter#
- Input/Output Parameters#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Computes the line-search update.

linesearch - The line search context

X - The current solution, on output the new solution

F - The current function value, on output the new function value at the solution value X

fnorm - The current norm of F, on output the new norm of F

Y - The current search direction, on output the direction determined by the linesearch, i.e. Xnew = Xold - lambda*Y

-snes_linesearch_type (none|basic|bt|secant|cp|nleqerr|bisection|shell) - Line search type, see SNESLineSearchType

-snes_linesearch_monitor [:filename] - Print progress of line searches

-snes_linesearch_damping damping - The linesearch damping parameter, default is 1.0 (no damping)

-snes_linesearch_norms (true|false) - Turn on/off the linesearch norms computation (SNESLineSearchSetComputeNorms())

-snes_linesearch_keeplambda (true|false) - Keep the previous lambda as the initial guess

-snes_linesearch_max_it it - The number of iterations for iterative line searches

This is typically called from within a SNESSolve() implementation in order to help with convergence of the nonlinear method. Various SNES types use line searches in different ways, but the overarching theme is that a line search is used to determine an optimal damping parameter (that is lambda) of a step at each iteration of the method. Each application of the line search may invoke SNESComputeFunction() several times, and therefore may be fairly expensive.

In certain situations SNESLineSearchApply() may directly set a SNESConvergedReason in the SNES object so one should always check this value immediately after the call to SNESLineSearchApply().

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESGetLineSearch(), SNESLineSearchCreate(), SNESLineSearchGetLambda(), SNESLineSearchPreCheck(), SNESLineSearchPostCheck(), SNESSolve(), SNESComputeFunction(), SNESLineSearchSetComputeNorms(), SNESLineSearchType, SNESLineSearchSetType()

src/snes/linesearch/interface/linesearch.c

SNESLineSearchApply_NCGLinear() in src/snes/impls/ncg/snesncg.c SNESLineSearchApply_Basic() in src/snes/linesearch/impls/basic/linesearchbasic.c SNESLineSearchApply_Bisection() in src/snes/linesearch/impls/bisection/linesearchbisection.c SNESLineSearchApply_BT() in src/snes/linesearch/impls/bt/linesearchbt.c SNESLineSearchApply_CP() in src/snes/linesearch/impls/cp/linesearchcp.c SNESLineSearchApply_NLEQERR() in src/snes/linesearch/impls/nleqerr/linesearchnleqerr.c SNESLineSearchApply_Secant() in src/snes/linesearch/impls/secant/linesearchsecant.c SNESLineSearchApply_Shell() in src/snes/linesearch/impls/shell/linesearchshell.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchApply(SNESLineSearch linesearch, Vec X, Vec F, PetscReal *fnorm, Vec Y)
```

Example 2 (unknown):
```unknown
Xnew = Xold - lambda*Y
```

Example 3 (unknown):
```unknown
SNESLineSearchType
```

Example 4 (unknown):
```unknown
SNESSolve()
```

---

## SNESLINESEARCHBASIC#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLINESEARCHBASIC/

**Contents:**
- SNESLINESEARCHBASIC#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#
- Examples#

This line search implementation is not a line search at all; it simply uses the full step \(x_{k+1} = x_k - \lambda Y_k\) with \(\lambda=1\). Alternatively, \(\lambda\) can be configured to be a constant damping factor by setting snes_linesearch_damping. Thus, this routine is intended for methods with well-scaled updates; i.e. Newton’s method (SNESNEWTONLS), on well-behaved problems. Also named SNESLINESEARCHNONE.

-snes_linesearch_damping damp - step length is scaled by this factor

-snes_linesearch_norms (true|false) - whether to compute norms or not (SNESLineSearchSetComputeNorms())

For methods with ill-scaled updates (SNESNRICHARDSON, SNESNCG), a small damping parameter may yield satisfactory, but slow convergence, despite the lack of the line search.

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchType, SNESGetLineSearch(), SNESLineSearchCreate(), SNESLineSearchSetType(), SNESLineSearchSetDamping(), SNESLineSearchSetComputeNorms()

src/snes/linesearch/impls/basic/linesearchbasic.c

src/ts/tutorials/ex22.c src/ts/tutorials/ex22f.F90 src/ts/utils/dmplexlandau/tutorials/ex1f90.F90

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
snes_linesearch_damping
```

Example 2 (unknown):
```unknown
SNESNEWTONLS
```

Example 3 (unknown):
```unknown
SNESLINESEARCHNONE
```

Example 4 (unknown):
```unknown
SNESLineSearchSetComputeNorms()
```

---

## SNESLINESEARCHBISECTION#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLINESEARCHBISECTION/

**Contents:**
- SNESLINESEARCHBISECTION#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#

Bisection line search. Similar to the critical point line search, SNESLINESEARCHCP, the bisection line search assumes that there exists some \(G(x)\) for which the SNESFunctionFn \(F(x) = grad G(x)\). This line search seeks to find the root of the directional derivative, that is \(F(x_k - \lambda Y_k) \cdot Y_k / ||Y_k|| = 0\), along the search direction \(Y_k\) through bisection.

-snes_linesearch_max_it 50 - maximum number of bisection iterations for the line search

-snes_linesearch_damping 1.0 - initial lambda on entry to the line search

-snes_linesearch_rtol 1e-8 - relative tolerance for the directional derivative

-snes_linesearch_atol 1e-6 - absolute tolerance for the directional derivative

-snes_linesearch_ltol 1e-6 - minimum absolute change in lambda allowed (this is an alternative to setting a maximum number of iterations)

lambda is the scaling of the search direction (vector) that is computed by this algorithm. If there is no change of sign in the directional derivative from \(\lambda=0\) to the initial lambda (the damping), then the initial lambda will be used. Hence, this line search will always give a lambda in the interval \([0, damping]\). This method does NOT use the objective function if it is provided with SNESSetObjective().

SNES: Nonlinear Solvers, SNESLineSearch, SNESLineSearchType, SNESLineSearchCreate(), SNESLineSearchSetType(), SNESLINESEARCHCP

src/snes/linesearch/impls/bisection/linesearchbisection.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLINESEARCHCP
```

Example 2 (unknown):
```unknown
SNESFunctionFn
```

Example 3 (unknown):
```unknown
SNESSetObjective()
```

Example 4 (unknown):
```unknown
SNESLineSearch
```

---

## SNESLineSearchBTGetAlpha#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchBTGetAlpha/

**Contents:**
- SNESLineSearchBTGetAlpha#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the descent parameter, alpha, in the SNESLINESEARCHBT variant that was set with SNESLineSearchBTSetAlpha()

linesearch - linesearch context

alpha - The descent parameter

SNES: Nonlinear Solvers, SNESLineSearch, SNESLineSearchGetLambda(), SNESLineSearchGetTolerances(), SNESLINESEARCHBT, SNESLineSearchBTSetAlpha()

src/snes/linesearch/impls/bt/linesearchbt.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLINESEARCHBT
```

Example 2 (unknown):
```unknown
SNESLineSearchBTSetAlpha()
```

Example 3 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESLineSearchBTGetAlpha(SNESLineSearch linesearch, PetscReal *alpha)
```

Example 4 (unknown):
```unknown
SNESLineSearch
```

---

## SNESLineSearchBTSetAlpha#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchBTSetAlpha/

**Contents:**
- SNESLineSearchBTSetAlpha#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the descent parameter, alpha, in the SNESLINESEARCHBT SNESLineSearch variant.

linesearch - linesearch context

alpha - The descent parameter

SNES: Nonlinear Solvers, SNESLineSearch, SNESLineSearchSetLambda(), SNESLineSearchGetTolerances(), SNESLINESEARCHBT, SNESLineSearchBTGetAlpha()

src/snes/linesearch/impls/bt/linesearchbt.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLINESEARCHBT
```

Example 2 (unknown):
```unknown
SNESLineSearch
```

Example 3 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESLineSearchBTSetAlpha(SNESLineSearch linesearch, PetscReal alpha)
```

Example 4 (unknown):
```unknown
SNESLineSearch
```

---

## SNESLINESEARCHBT#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLINESEARCHBT/

**Contents:**
- SNESLINESEARCHBT#
- Options Database Keys#
- Note#
- References#
- See Also#
- Level#
- Location#

Backtracking line search [DennisJrS83]. This line search finds the minimum of a polynomial fitting either \(1/2 ||F(x_k + \lambda Y_k)||_2^2\), or the objective function \(G(x_k + \lambda Y_k)\) if it is provided with SNESSetObjective(). If this fit does not satisfy the sufficient decrease conditions, the interval shrinks and the fit is reattempted at most max_it times or until \(\lambda\) is below minlambda.

-snes_linesearch_alpha 1e-4 - slope descent parameter

-snes_linesearch_damping 1.0 - initial lambda on entry to the line search

-snes_linesearch_max_it 40 - maximum number of shrinking iterations in the line search

-snes_linesearch_minlambda 1e-12 - minimum lambda (scaling of solution update) allowed

-snes_linesearch_order 3 - order of the polynomial fit, must be 1, 2, or 3. With order 1, it performs a simple backtracking without any curve fitting

This line search will always produce a step that is less than or equal to, in length, the full step size.

J. E. Dennis Jr. and Robert B. Schnabel. Numerical Methods for Unconstrained Optimization and Nonlinear Equations. Prentice-Hall, Inc., Englewood Cliffs, NJ, 1983.

SNES: Nonlinear Solvers, SNESLineSearch, SNESLineSearchType, SNESLineSearchCreate(), SNESLineSearchSetType()

src/snes/linesearch/impls/bt/linesearchbt.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetObjective()
```

Example 2 (unknown):
```unknown
SNESLineSearch
```

Example 3 (unknown):
```unknown
SNESLineSearchType
```

Example 4 (unknown):
```unknown
SNESLineSearchCreate()
```

---

## SNESLineSearchComputeNorms#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchComputeNorms/

**Contents:**
- SNESLineSearchComputeNorms#
- Synopsis#
- Input Parameter#
- Options Database Key#
- Developer Note#
- See Also#
- Level#
- Location#

Explicitly computes the norms of the current solution X, the current update Y, and the current function value F.

linesearch - the line search context

-snes_linesearch_norms (true|false) - turn norm computation on or off

The options database key is misnamed. It should be -snes_linesearch_compute_norms

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchGetNorms, SNESLineSearchSetNorms(), SNESLineSearchSetComputeNorms()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchComputeNorms(SNESLineSearch linesearch)
```

Example 2 (unknown):
```unknown
-snes_linesearch_compute_norms
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
SNESLineSearchGetNorms
```

---

## SNESLINESEARCHCP#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLINESEARCHCP/

**Contents:**
- SNESLINESEARCHCP#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#

Critical point line search. This line search assumes that there exists some artificial \(G(x)\) for which the SNESFunctionFn \(F(x) = grad G(x)\). Therefore, this line search seeks to find roots of the directional derivative via a secant method, that is \(F(x_k - \lambda Y_k) \cdot Y_k / ||Y_k|| = 0\).

-snes_linesearch_minlambda 1e-12 - the minimum acceptable lambda (scaling of solution update)

-snes_linesearch_maxlambda 1.0 - the algorithm ensures that lambda is never larger than this value

-snes_linesearch_damping 1.0 - initial lambda on entry to the line search

-snes_linesearch_order 1 - order of the approximation in the secant method, must be 1, 2, or 3

-snes_linesearch_max_it 1 - the maximum number of secant iterations performed

-snes_linesearch_rtol 1e-8 - relative tolerance for the directional derivative

-snes_linesearch_atol 1e-15 - absolute tolerance for the directional derivative

-snes_linesearch_ltol 1e-8 - minimum absolute change in lambda allowed

This method does NOT use the objective function if it is provided with SNESSetObjective().

This method is the preferred line search for SNESQN and SNESNCG.

SNES: Nonlinear Solvers, SNESLineSearch, SNESLineSearchType, SNESLineSearchCreate(), SNESLineSearchSetType(), SNESLINESEARCHBISECTION

src/snes/linesearch/impls/cp/linesearchcp.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESFunctionFn
```

Example 2 (unknown):
```unknown
SNESSetObjective()
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
SNESLineSearchType
```

---

## SNESLineSearchCreate#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchCreate/

**Contents:**
- SNESLineSearchCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Creates a SNESLineSearch context.

comm - MPI communicator for the line search (typically from the associated SNES context).

outlinesearch - the new line search context

The preferred calling sequence is to use SNESGetLineSearch() to acquire the SNESLineSearch instance already associated with the SNES.

SNES: Nonlinear Solvers, SNES, SNESLineSearch, LineSearchDestroy(), SNESGetLineSearch()

src/snes/linesearch/interface/linesearch.c

SNESLineSearchCreate_NCGLinear() in src/snes/impls/ncg/snesncg.c SNESLineSearchCreate_Basic() in src/snes/linesearch/impls/basic/linesearchbasic.c SNESLineSearchCreate_Bisection() in src/snes/linesearch/impls/bisection/linesearchbisection.c SNESLineSearchCreate_BT() in src/snes/linesearch/impls/bt/linesearchbt.c SNESLineSearchCreate_CP() in src/snes/linesearch/impls/cp/linesearchcp.c SNESLineSearchCreate_NLEQERR() in src/snes/linesearch/impls/nleqerr/linesearchnleqerr.c SNESLineSearchCreate_Secant() in src/snes/linesearch/impls/secant/linesearchsecant.c SNESLineSearchCreate_Shell() in src/snes/linesearch/impls/shell/linesearchshell.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLineSearch
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchCreate(MPI_Comm comm, SNESLineSearch *outlinesearch)
```

Example 3 (unknown):
```unknown
SNESGetLineSearch()
```

Example 4 (unknown):
```unknown
SNESLineSearch
```

---

## SNESLineSearchDestroy#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchDestroy/

**Contents:**
- SNESLineSearchDestroy#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Destroys the line search instance.

linesearch - The line search context

The line search in SNES is automatically called on SNESDestroy() so this call is rarely needed

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESGetLineSearch(), SNESLineSearchCreate(), SNESLineSearchReset(), SNESDestroy()

src/snes/linesearch/interface/linesearch.c

SNESLineSearchDestroy_BT() in src/snes/linesearch/impls/bt/linesearchbt.c SNESLineSearchDestroy_NLEQERR() in src/snes/linesearch/impls/nleqerr/linesearchnleqerr.c SNESLineSearchDestroy_Shell() in src/snes/linesearch/impls/shell/linesearchshell.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchDestroy(SNESLineSearch *linesearch)
```

Example 2 (unknown):
```unknown
SNESDestroy()
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
SNESGetLineSearch()
```

---

## SNESLineSearchGetDamping#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchGetDamping/

**Contents:**
- SNESLineSearchGetDamping#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the line search damping parameter.

linesearch - the line search context

damping - The damping parameter

SNES: Nonlinear Solvers, SNES, SNESLineSearchGetStepTolerance(), SNESQN

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchGetDamping(SNESLineSearch linesearch, PetscReal *damping)
```

Example 2 (unknown):
```unknown
SNESLineSearchGetStepTolerance()
```

---

## SNESLineSearchGetDefaultMonitor#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchGetDefaultMonitor/

**Contents:**
- SNESLineSearchGetDefaultMonitor#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the PetscViewer instance for the default line search monitor that is turned on with SNESLineSearchSetDefaultMonitor()

linesearch - the line search context

monitor - monitor context

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESGetLineSearch(), SNESLineSearchSetDefaultMonitor(), PetscViewer

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
SNESLineSearchSetDefaultMonitor()
```

Example 3 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchGetDefaultMonitor(SNESLineSearch linesearch, PetscViewer *monitor)
```

Example 4 (unknown):
```unknown
SNESLineSearch
```

---

## SNESLineSearchGetLambda#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchGetLambda/

**Contents:**
- SNESLineSearchGetLambda#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the last line search lambda used

linesearch - the line search context

lambda - The last lambda (scaling of the solution update) computed during SNESLineSearchApply()

This is useful in methods where the solver is ill-scaled and requires some adaptive notion of the difference in scale between the solution and the function. For instance, SNESQN may be scaled by the line search lambda using the argument -snes_qn_scaling ls.

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchSetLambda(), SNESLineSearchGetDamping(), SNESLineSearchApply()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchGetLambda(SNESLineSearch linesearch, PetscReal *lambda)
```

Example 2 (unknown):
```unknown
SNESLineSearchApply()
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
SNESLineSearchSetLambda()
```

---

## SNESLineSearchGetNorms#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchGetNorms/

**Contents:**
- SNESLineSearchGetNorms#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Gets the norms for the current solution X, the current update Y, and the current function value F.

linesearch - the line search context

xnorm - The norm of the current solution

fnorm - The norm of the current function, this is the norm(function(X)) where X is the current solution.

ynorm - The norm of the current update (after scaling by the linesearch computed lambda)

Some values may not be up-to-date at particular points in the code.

This, in combination with SNESLineSearchSetNorms(), allow the line search and the SNESSolve_XXX() to share computed values.

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchSetNorms(), SNESLineSearchGetVecs()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchGetNorms(SNESLineSearch linesearch, PetscReal *xnorm, PetscReal *fnorm, PetscReal *ynorm)
```

Example 2 (r):
```r
norm(function(X))
```

Example 3 (unknown):
```unknown
SNESLineSearchSetNorms()
```

Example 4 (unknown):
```unknown
SNESSolve_XXX()
```

---

## SNESLineSearchGetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchGetOptionsPrefix/

**Contents:**
- SNESLineSearchGetOptionsPrefix#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the prefix used for searching for all SNESLineSearch options in the database.

linesearch - the SNESLineSearch context

prefix - pointer to the prefix string used

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESAppendOptionsPrefix()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchGetOptionsPrefix(SNESLineSearch linesearch, const char *prefix[])
```

Example 2 (unknown):
```unknown
SNESLineSearch
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
SNESAppendOptionsPrefix()
```

---

## SNESLineSearchGetOrder#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchGetOrder/

**Contents:**
- SNESLineSearchGetOrder#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the line search approximation order.

linesearch - the line search context

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchSetOrder()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchGetOrder(SNESLineSearch linesearch, PetscInt *order)
```

Example 2 (unknown):
```unknown
SNESLineSearch
```

Example 3 (unknown):
```unknown
SNESLineSearchSetOrder()
```

---

## SNESLineSearchGetPostCheck#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchGetPostCheck/

**Contents:**
- SNESLineSearchGetPostCheck#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Gets the post-check function for the line search routine.

linesearch - the SNESLineSearch context

func - [optional] function evaluation routine, see for the calling sequence SNESLineSearchSetPostCheck()

ctx - [optional] user-defined context for private data for the function evaluation routine (may be NULL)

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESGetLineSearch(), SNESLineSearchGetPreCheck(), SNESLineSearchSetPostCheck(), SNESLineSearchPostCheck(), SNESLineSearchSetPreCheck()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchGetPostCheck(SNESLineSearch linesearch, PetscErrorCode (**func)(SNESLineSearch, Vec, Vec, Vec, PetscBool *, PetscBool *, void *), PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
SNESLineSearch
```

Example 3 (unknown):
```unknown
SNESLineSearchSetPostCheck()
```

Example 4 (unknown):
```unknown
SNESLineSearch
```

---

## SNESLineSearchGetPreCheck#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchGetPreCheck/

**Contents:**
- SNESLineSearchGetPreCheck#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Gets the pre-check function for the line search routine.

linesearch - the SNESLineSearch context

func - [optional] function evaluation routine, for calling sequence see SNESLineSearchSetPreCheck()

ctx - [optional] user-defined context for private data for the function evaluation routine (may be NULL)

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESGetLineSearch(), SNESLineSearchPreCheck(), SNESLineSearchGetPostCheck(), SNESLineSearchSetPreCheck(), SNESLineSearchSetPostCheck()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchGetPreCheck(SNESLineSearch linesearch, PetscErrorCode (**func)(SNESLineSearch, Vec, Vec, PetscBool *, void *), PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
SNESLineSearch
```

Example 3 (unknown):
```unknown
SNESLineSearchSetPreCheck()
```

Example 4 (unknown):
```unknown
SNESLineSearch
```

---

## SNESLineSearchGetReason#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchGetReason/

**Contents:**
- SNESLineSearchGetReason#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the success/failure status of the last line search application

linesearch - the line search context

reason - The success or failure status

This is typically called after SNESLineSearchApply() in order to determine if the line search failed (and set into the SNES convergence accordingly).

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchSetReason(), SNESLineSearchReason

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchGetReason(SNESLineSearch linesearch, SNESLineSearchReason *reason)
```

Example 2 (unknown):
```unknown
SNESLineSearchApply()
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
SNESLineSearchSetReason()
```

---

## SNESLineSearchGetSNES#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchGetSNES/

**Contents:**
- SNESLineSearchGetSNES#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Gets the SNES instance associated with the line search.

linesearch - the line search context

snes - The SNES instance

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESType, SNESLineSearchSetVecs()

src/snes/linesearch/interface/linesearch.c

src/snes/tutorials/ex15.c src/snes/tutorials/ex1f.F90 src/snes/tutorials/ex3.c src/ts/tutorials/ex27.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchGetSNES(SNESLineSearch linesearch, SNES *snes)
```

Example 2 (unknown):
```unknown
SNESLineSearch
```

Example 3 (unknown):
```unknown
SNESLineSearchSetVecs()
```

---

## SNESLineSearchGetTolerances#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchGetTolerances/

**Contents:**
- SNESLineSearchGetTolerances#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Gets the tolerances for the line search.

linesearch - the line search context

minlambda - The minimum lambda allowed

maxlambda - The maximum lambda allowed

rtol - The relative tolerance for iterative line searches

atol - The absolute tolerance for iterative line searches

ltol - The change in lambda tolerance for iterative line searches

max_it - The maximum number of iterations of the line search

Different line searches may implement these parameters slightly differently as the type requires.

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchSetTolerances()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchGetTolerances(SNESLineSearch linesearch, PetscReal *minlambda, PetscReal *maxlambda, PetscReal *rtol, PetscReal *atol, PetscReal *ltol, PetscInt *max_it)
```

Example 2 (unknown):
```unknown
SNESLineSearch
```

Example 3 (unknown):
```unknown
SNESLineSearchSetTolerances()
```

---

## SNESLineSearchGetType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchGetType/

**Contents:**
- SNESLineSearchGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the SNESLinesearchType of a SNESLineSearch

linesearch - the line search context

type - The type of line search, or NULL if not set

type should not be retained for later use as it will be an invalid pointer if the SNESLineSearchType of linesearch is changed.

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchType, SNESLineSearchCreate(), SNESLineSearchSetFromOptions(), SNESLineSearchSetType(), PetscObjectTypeCompare(), PetscObjectTypeCompareAny()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLinesearchType
```

Example 2 (unknown):
```unknown
SNESLineSearch
```

Example 3 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchGetType(SNESLineSearch linesearch, SNESLineSearchType *type)
```

Example 4 (unknown):
```unknown
SNESLineSearchType
```

---

## SNESLineSearchGetVecs#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchGetVecs/

**Contents:**
- SNESLineSearchGetVecs#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Gets the vectors from the SNESLineSearch context

Not Collective but the vectors are parallel

linesearch - the line search context

Y - Search direction vector

W - Solution work vector

G - Function work vector

At the beginning of a line search application, X should contain a solution and the vector F the function computed at X. At the end of the line search application, X should contain the new solution, and F the function evaluated at the new solution.

These vectors are owned by the SNESLineSearch and should not be destroyed by the caller

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchGetNorms(), SNESLineSearchSetVecs()

src/snes/linesearch/interface/linesearch.c

src/snes/tutorials/ex1f.F90

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLineSearch
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchGetVecs(SNESLineSearch linesearch, Vec *X, Vec *F, Vec *Y, Vec *W, Vec *G)
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
SNESLineSearch
```

---

## SNESLineSearchGetVIFunctions#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchGetVIFunctions/

**Contents:**
- SNESLineSearchGetVIFunctions#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Sets VI-specific functions for line search computation.

linesearch - the line search context, obtain with SNESGetLineSearch()

projectfunc - function for projecting the function to the bounds, see SNESLineSearchVIProjectFn for calling sequence

normfunc - function for computing the norm of an active set, see SNESLineSearchVINormFn for calling sequence

dirderivfunc - function for computing the directional derivative of an active set, see SNESLineSearchVIDirDerivFn for calling sequence

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchSetVIFunctions(), SNESLineSearchGetPostCheck(), SNESLineSearchGetPreCheck(), SNESLineSearchVIProjectFn, SNESLineSearchVINormFn

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchGetVIFunctions(SNESLineSearch linesearch, SNESLineSearchVIProjectFn **projectfunc, SNESLineSearchVINormFn **normfunc, SNESLineSearchVIDirDerivFn **dirderivfunc)
```

Example 2 (unknown):
```unknown
SNESGetLineSearch()
```

Example 3 (unknown):
```unknown
SNESLineSearchVIProjectFn
```

Example 4 (unknown):
```unknown
SNESLineSearchVINormFn
```

---

## SNESLineSearchMonitorCancel#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchMonitorCancel/

**Contents:**
- SNESLineSearchMonitorCancel#
- Synopsis#
- Input Parameter#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Clears all the monitor functions for a SNESLineSearch object.

ls - the SNESLineSearch context

-snes_linesearch_monitor_cancel - cancels all monitors that have been hardwired into a code by calls to SNESLineSearchMonitorSet(), but does not cancel those set via the options database

There is no way to clear one specific monitor from a SNESLineSearch object.

This does not clear the monitor set with SNESLineSearchSetDefaultMonitor() use SNESLineSearchSetDefaultMonitor(ls,NULL) to cancel it that one.

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESGetLineSearch(), SNESLineSearchMonitorDefault(), SNESLineSearchMonitorSet()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLineSearch
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchMonitorCancel(SNESLineSearch ls)
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
SNESLineSearchMonitorSet()
```

---

## SNESLineSearchMonitorSetFromOptions#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchMonitorSetFromOptions/

**Contents:**
- SNESLineSearchMonitorSetFromOptions#
- Synopsis#
- Input Parameters#
- Calling sequence of monitor#
- Calling sequence of monitorsetup#
- See Also#
- Level#
- Location#

Sets a monitor function and viewer appropriate for the type indicated in the options database

ls - SNESLineSearch object to monitor

name - the monitor type

help - message indicating what monitoring is done

manual - manual page for the monitor

monitor - the monitor function, must use PetscViewerAndFormat as its context

monitorsetup - a function that is called once ONLY if the user selected this monitor that may set additional features of the SNESLineSearch or PetscViewer

ls - SNESLineSearch object being monitored

vf - a PetscViewerAndFormat struct that provides the PetscViewer and PetscViewerFormat being used

ls - SNESLineSearch object being monitored

vf - a PetscViewerAndFormat struct that provides the PetscViewer and PetscViewerFormat being used

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchSetMonitor(), PetscOptionsCreateViewer(), PetscOptionsGetReal(), PetscOptionsHasName(), PetscOptionsGetString(), PetscOptionsGetIntArray(), PetscOptionsGetRealArray(), PetscOptionsBool(), PetscOptionsInt(), PetscOptionsString(), PetscOptionsReal(), PetscOptionsName(), PetscOptionsBegin(), PetscOptionsEnd(), PetscOptionsHeadBegin(), PetscOptionsStringArray(), PetscOptionsRealArray(), PetscOptionsScalar(), PetscOptionsBoolGroupBegin(), PetscOptionsBoolGroup(), PetscOptionsBoolGroupEnd(), PetscOptionsFList(), PetscOptionsEList()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchMonitorSetFromOptions(SNESLineSearch ls, const char name[], const char help[], const char manual[], PetscErrorCode (*monitor)(SNESLineSearch ls, PetscViewerAndFormat *vf), PetscErrorCode (*monitorsetup)(SNESLineSearch ls, PetscViewerAndFormat *vf))
```

Example 2 (unknown):
```unknown
SNESLineSearch
```

Example 3 (unknown):
```unknown
PetscViewerAndFormat
```

Example 4 (unknown):
```unknown
SNESLineSearch
```

---

## SNESLineSearchMonitorSet#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchMonitorSet/

**Contents:**
- SNESLineSearchMonitorSet#
- Synopsis#
- Input Parameters#
- Calling sequence of f#
- Note#
- Fortran Note#
- See Also#
- Level#
- Location#

Sets an ADDITIONAL function that is to be used at every iteration of the nonlinear solver to display the iteration’s progress.

ls - the SNESLineSearch context

f - the monitor function

mctx - [optional] user-defined context for private data for the monitor routine (use NULL if no context is desired)

monitordestroy - [optional] routine that frees monitor context (may be NULL), see PetscCtxDestroyFn for the calling sequence

ls - the SNESLineSearch context

mctx - [optional] user-defined context for private data for the monitor routine

Several different monitoring routines may be set by calling SNESLineSearchMonitorSet() multiple times; all will be called in the order in which they were set.

Only a single monitor function can be set for each SNESLineSearch object

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESGetLineSearch(), SNESLineSearchMonitorDefault(), SNESLineSearchMonitorCancel(), PetscCtxDestroyFn

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchMonitorSet(SNESLineSearch ls, PetscErrorCode (*f)(SNESLineSearch ls, PetscCtx mctx), PetscCtx mctx, PetscCtxDestroyFn *monitordestroy)
```

Example 2 (unknown):
```unknown
SNESLineSearch
```

Example 3 (unknown):
```unknown
PetscCtxDestroyFn
```

Example 4 (unknown):
```unknown
SNESLineSearch
```

---

## SNESLineSearchMonitorSolutionUpdate#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchMonitorSolutionUpdate/

**Contents:**
- SNESLineSearchMonitorSolutionUpdate#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Monitors each update of the function value the linesearch tries

ls - the SNESLineSearch object

vf - the context for the monitor, in this case it is an PetscViewerAndFormat

-snes_linesearch_monitor_solution_update [viewer:filename:format] - view each update tried by line search routine

This is not normally called directly but is passed to SNESLineSearchMonitorSet()

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESGetLineSearch(), SNESLineSearchMonitorSet(), SNESMonitorSolution()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchMonitorSolutionUpdate(SNESLineSearch ls, PetscViewerAndFormat *vf)
```

Example 2 (unknown):
```unknown
SNESLineSearch
```

Example 3 (unknown):
```unknown
PetscViewerAndFormat
```

Example 4 (unknown):
```unknown
SNESLineSearchMonitorSet()
```

---

## SNESLineSearchMonitor#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchMonitor/

**Contents:**
- SNESLineSearchMonitor#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#

runs the user provided monitor routines, if they exist

ls - the linesearch object

This routine is called by the SNESLineSearch implementations. It does not typically need to be called by the user.

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESGetLineSearch(), SNESLineSearchMonitorSet()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchMonitor(SNESLineSearch ls)
```

Example 2 (unknown):
```unknown
SNESLineSearch
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
SNESGetLineSearch()
```

---

## SNESLINESEARCHNCGLINEAR#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLINESEARCHNCGLINEAR/

**Contents:**
- SNESLINESEARCHNCGLINEAR#
- Notes#
- See Also#
- Level#
- Location#

Special line search only for the nonlinear CG solver SNESNCG This line search uses the length “as if” the problem is linear (that is what is computed by the linear CG method) using the Jacobian of the function. alpha = (r, r) / (p, Ap) = (f, f) / (y, Jy) where r (f) is the current residual (function value), p (y) is the current search direction.

This requires a Jacobian-vector product but does not require the solution of a linear system with the Jacobian

This is a “odd-ball” line search, we don’t know if it is in the literature or used in practice by anyone.

SNES: Nonlinear Solvers, SNES, SNESNCG, SNESLineSearchCreate(), SNESLineSearchSetType()

src/snes/impls/ncg/snesncg.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLineSearchCreate()
```

Example 2 (unknown):
```unknown
SNESLineSearchSetType()
```

---

## SNESLINESEARCHNLEQERR#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLINESEARCHNLEQERR/

**Contents:**
- SNESLINESEARCHNLEQERR#
- Options Database Keys#
- Note#
- References#
- See Also#
- Level#
- Location#

Error-oriented affine-covariant globalised Newton algorithm of Deuflhard [Deu11] This linesearch is intended for Newton-type methods which are affine covariant. Affine covariance means that Newton’s method will give the same iterations for F(x) = 0 and AF(x) = 0 for any nonsingular matrix A. This is a fundamental property; the philosophy of this linesearch is that globalisations of Newton’s method should carefully preserve it.

-snes_linesearch_damping 1.0 - initial lambda

-snes_linesearch_max_it 40 - maximum number of iterations for the line search

-snes_linesearch_minlambda 1e-12 - minimum lambda allowed

Contributed by Patrick Farrell patrick.farrell@maths.ox.ac.uk

Peter Deuflhard. Newton Methods for Nonlinear Problems. Volume 35. Springer-Verlag, Berlin, Heidelberg, 2011. ISBN 978-3-642-23898-7. doi:10.1007/978-3-642-23899-4.

SNES: Nonlinear Solvers, SNESLineSearch, SNES, SNESLineSearchCreate(), SNESLineSearchSetType()

src/snes/linesearch/impls/nleqerr/linesearchnleqerr.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLineSearch
```

Example 2 (unknown):
```unknown
SNESLineSearchCreate()
```

Example 3 (unknown):
```unknown
SNESLineSearchSetType()
```

---

## SNESLineSearchPostCheck#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchPostCheck/

**Contents:**
- SNESLineSearchPostCheck#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

Hook to modify step direction or updated solution after a successful linesearch

linesearch - The line search context

X - The last solution

Y - The step direction

W - The updated solution, W = X - lambda * Y for some lambda

changed_Y - Indicator if the direction Y has been changed.

changed_W - Indicator if the new candidate solution W has been changed.

This calls any function provided with SNESLineSearchSetPostCheck() and is called automatically inside the line search routines

The use of PetscObjectGetState() would eliminate the need for the changed_Y and changed_W arguments to be provided

SNES: Nonlinear Solvers, SNES, SNESGetLineSearch(), SNESLineSearchPreCheck(), SNESLineSearchSetPostCheck(), SNESLineSearchGetPostCheck(), SNESLineSearchSetPrecheck(), SNESLineSearchGetPrecheck()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchPostCheck(SNESLineSearch linesearch, Vec X, Vec Y, Vec W, PetscBool *changed_Y, PetscBool *changed_W)
```

Example 2 (unknown):
```unknown
W = X - lambda * Y
```

Example 3 (unknown):
```unknown
SNESLineSearchSetPostCheck()
```

Example 4 (unknown):
```unknown
PetscObjectGetState()
```

---

## SNESLineSearchPreCheckPicard#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchPreCheckPicard/

**Contents:**
- SNESLineSearchPreCheckPicard#
- Synopsis#
- Input Parameters#
- Input/Output Parameter#
- Output Parameter#
- Options Database Keys#
- Notes#
- Developer Note#
- References#
- See Also#

Implements a correction that is sometimes useful to improve the convergence rate of Picard iteration [HP96]

linesearch - the line search context

X - base state for this step

ctx - context for this function

Y - correction, possibly modified

changed - flag indicating that Y was modified

-snes_linesearch_precheck_picard (true|false) - activate this routine

-snes_linesearch_precheck_picard_angle angle - the angle to use

This function should be passed to SNESLineSearchSetPreCheck()

The justification for this method involves the linear convergence of a Picard iteration so the Picard linearization should be provided in place of the “Jacobian” [HP96]. This correction is generally not useful when using a Newton linearization.

The use of PetscObjectGetState() would eliminate the need for the changed argument to be provided

Richard CA Hindmarsh and Antony J Payne. Time-step limits for stable solutions of the ice-sheet equation. Annals of Glaciology, 23:74–85, 1996.

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESSetPicard(), SNESGetLineSearch(), SNESLineSearchSetPreCheck(), SNESLineSearchSetPostCheck()

src/snes/linesearch/interface/linesearch.c

src/snes/tutorials/ex15.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchPreCheckPicard(SNESLineSearch linesearch, Vec X, Vec Y, PetscBool *changed, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESLineSearchSetPreCheck()
```

Example 3 (unknown):
```unknown
PetscObjectGetState()
```

Example 4 (unknown):
```unknown
SNESLineSearch
```

---

## SNESLineSearchPreCheck#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchPreCheck/

**Contents:**
- SNESLineSearchPreCheck#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

Prepares the line search for being applied.

linesearch - The linesearch instance.

X - The current solution

Y - The step direction

changed - Indicator that the precheck routine has changed Y

This calls any function provided with SNESLineSearchSetPreCheck() and is called automatically inside the line search routines

The use of PetscObjectGetState() would eliminate the need for the changed argument to be provided

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESGetLineSearch(), SNESLineSearchPostCheck(), SNESLineSearchSetPreCheck(), SNESLineSearchGetPreCheck(), SNESLineSearchSetPostCheck(), SNESLineSearchGetPostCheck()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchPreCheck(SNESLineSearch linesearch, Vec X, Vec Y, PetscBool *changed)
```

Example 2 (unknown):
```unknown
SNESLineSearchSetPreCheck()
```

Example 3 (unknown):
```unknown
PetscObjectGetState()
```

Example 4 (unknown):
```unknown
SNESLineSearch
```

---

## SNESLineSearchReason#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchReason/

**Contents:**
- SNESLineSearchReason#
- Synopsis#
- Values#
- Developer Note#
- See Also#
- Level#
- Location#

indication if the line search has succeeded or failed and why

SNES_LINESEARCH_SUCCEEDED - the line search succeeded

SNES_LINESEARCH_FAILED_NANORINF - a not a number of infinity appeared in the computions

SNES_LINESEARCH_FAILED_FUNCTION_DOMAIN - the function was evaluated outside of its domain, see SNESSetFunctionDomainError()

SNES_LINESEARCH_FAILED_OBJECTIVE_DOMAIN- the objective function was evaluated outside of its domain, see SNESSetObjectiveDomainError()

SNES_LINESEARCH_FAILED_JACOBIAN_DOMAIN - the Jacobian was evaluated outside of its domain, see SNESSetJacobianDomainError()

SNES_LINESEARCH_FAILED_REDUCT - the linear search failed to get the requested decrease in its norm or objective

SNES_LINESEARCH_FAILED_USER - used by SNESLINESEARCHNLEQERR to indicate the user changed the search direction inappropriately

SNES_LINESEARCH_FAILED_FUNCTION - indicates the maximum number of function evaluations allowed has been surpassed, SNESConvergedReason is also set to SNES_DIVERGED_FUNCTION_COUNT

Some of these reasons overlap with values of SNESConvergedReason. It is possibly a better design to have SNESConvergedReaon alone used also for indicating line search failures.

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESGetConvergedReason(), KSPConvergedReason, SNESSetConvergenceTest(), SNESSetFunctionDomainError(), SNESSetJacobianDomainError()

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  SNES_LINESEARCH_SUCCEEDED,
  SNES_LINESEARCH_FAILED_NANORINF,
  SNES_LINESEARCH_FAILED_FUNCTION_DOMAIN,
  SNES_LINESEARCH_FAILED_OBJECTIVE_DOMAIN,
  SNES_LINESEARCH_FAILED_JACOBIAN_DOMAIN,
  SNES_LINESEARCH_FAILED_REDUCT, /* INSUFFICIENT REDUCTION */
  SNES_LINESEARCH_FAILED_USER,
  SNES_LINESEARCH_FAILED_FUNCTION
} SNESLineSearchReason;
```

Example 2 (unknown):
```unknown
SNES_LINESEARCH_SUCCEEDED
```

Example 3 (unknown):
```unknown
SNES_LINESEARCH_FAILED_NANORINF
```

Example 4 (unknown):
```unknown
SNES_LINESEARCH_FAILED_FUNCTION_DOMAIN
```

---

## SNESLineSearchRegisterAll#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchRegisterAll/

**Contents:**
- SNESLineSearchRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the nonlinear solver methods in the SNESLineSearch package.

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchRegister(), SNESLineSearchRegisterDestroy()

src/snes/linesearch/interface/linesearchregi.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLineSearch
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESLineSearchRegisterAll(void)
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
SNESLineSearchRegister()
```

---

## SNESLineSearchRegister#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchRegister/

**Contents:**
- SNESLineSearchRegister#
- Synopsis#
- Input Parameters#
- Calling sequence of function#
- See Also#
- Level#
- Location#

register a line search type SNESLineSearchType

Logically Collective, No Fortran Support

sname - name of the SNESLineSearchType()

function - the creation function for that type

ls - the line search context

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchType, SNESLineSearchSetType()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLineSearchType
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchRegister(const char sname[], PetscErrorCode (*function)(SNESLineSearch ls))
```

Example 3 (unknown):
```unknown
SNESLineSearchType()
```

Example 4 (unknown):
```unknown
SNESLineSearch
```

---

## SNESLineSearchReset#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchReset/

**Contents:**
- SNESLineSearchReset#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Undoes the SNESLineSearchSetUp() and deletes any Vecs or Mats allocated by the line search.

linesearch - The SNESLineSearch instance.

Usually only called by SNESReset()

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESGetLineSearch(), SNESLineSearchSetUp()

src/snes/linesearch/interface/linesearch.c

SNESLineSearchReset_NLEQERR() in src/snes/linesearch/impls/nleqerr/linesearchnleqerr.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLineSearchSetUp()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchReset(SNESLineSearch linesearch)
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
SNESReset()
```

---

## SNESLINESEARCHSECANT#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLINESEARCHSECANT/

**Contents:**
- SNESLINESEARCHSECANT#
- Options Database Keys#
- See Also#
- Level#
- Location#

Secant search in the L2 norm of the function or the objective function. Attempts to solve \( \min_{\lambda} f(x_k + \lambda Y_k) \) using the secant method with the initial bracketing of \( \lambda \) between [0,damping]. \(f(x_k + \lambda Y_k)\) is either the squared L2-norm of the function \(||F(x_k + \lambda Y_k)||_2^2\), or the objective function \(G(x_k + \lambda Y_k)\) if it is provided with SNESSetObjective() Differences of \(f()\) are used to approximate the first and second derivative of \(f()\) with respect to \(\lambda\), \(f'()\) and \(f''()\).

When an objective function is provided \(f(w)\) is the objective function otherwise \(f(w) = ||F(w)||^2\). \(x\) is the current step and \(y\) is the search direction.

-snes_linesearch_max_it 1 - maximum number of iterations within the line search

-snes_linesearch_damping 1.0 - initial lambda on entry to the line search

-snes_linesearch_minlambda 1e-12 - minimum allowable lambda

-snes_linesearch_maxlambda 1.0 - maximum lambda (scaling of solution update) allowed

-snes_linesearch_atol 1e-15 - absolute tolerance for the secant method \( f'() < atol \)

-snes_linesearch_ltol 1e-8 - minimum absolute change in lambda allowed

SNES: Nonlinear Solvers, SNESLINESEARCHBT, SNESLINESEARCHCP, SNESLineSearch, SNESLineSearchType, SNESLineSearchCreate(), SNESLineSearchSetType()

src/snes/linesearch/impls/secant/linesearchsecant.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetObjective()
```

Example 2 (unknown):
```unknown
SNESLINESEARCHBT
```

Example 3 (unknown):
```unknown
SNESLINESEARCHCP
```

Example 4 (unknown):
```unknown
SNESLineSearch
```

---

## SNESLineSearchSetComputeNorms#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchSetComputeNorms/

**Contents:**
- SNESLineSearchSetComputeNorms#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

Turns on or off the computation of final norms in the line search.

linesearch - the line search context

flg - indicates whether or not to compute norms

-snes_linesearch_norms (true|false) - Turns on/off computation of the norms for basic (none) SNESLINESEARCHBASIC line search

This is most relevant to the SNESLINESEARCHBASIC (or equivalently SNESLINESEARCHNONE) line search type since most line searches have a stopping criteria involving the norm.

The options database key is misnamed. It should be -snes_linesearch_compute_norms

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchGetNorms(), SNESLineSearchSetNorms(), SNESLineSearchComputeNorms(), SNESLINESEARCHBASIC

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchSetComputeNorms(SNESLineSearch linesearch, PetscBool flg)
```

Example 2 (unknown):
```unknown
SNESLINESEARCHBASIC
```

Example 3 (unknown):
```unknown
SNESLINESEARCHBASIC
```

Example 4 (unknown):
```unknown
SNESLINESEARCHNONE
```

---

## SNESLineSearchSetDamping#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchSetDamping/

**Contents:**
- SNESLineSearchSetDamping#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Sets the line search damping parameter.

linesearch - the line search context

damping - The damping parameter

-snes_linesearch_damping damping - the damping value

The SNESLINESEARCHNONE line search merely takes the update step scaled by the damping parameter. The use of the damping parameter in the SNESLINESEARCHSECANT and SNESLINESEARCHCP line searches is much more subtle; it is used as a starting point for the secant method. Depending on the choice for maxlambda, the eventual lambda may be greater than the damping parameter however. For SNESLINESEARCHBISECTION and SNESLINESEARCHBT the damping is instead used as the initial guess, below which the line search will not go. Hence, it is the maximum possible value for lambda.

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchGetDamping()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchSetDamping(SNESLineSearch linesearch, PetscReal damping)
```

Example 2 (unknown):
```unknown
SNESLINESEARCHNONE
```

Example 3 (unknown):
```unknown
SNESLINESEARCHSECANT
```

Example 4 (unknown):
```unknown
SNESLINESEARCHCP
```

---

## SNESLineSearchSetDefaultMonitor#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchSetDefaultMonitor/

**Contents:**
- SNESLineSearchSetDefaultMonitor#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Developer Notes#
- See Also#
- Level#
- Location#

Turns on/off printing useful information and debugging output about the line search.

linesearch - the linesearch object

viewer - an PETSCVIEWERASCII PetscViewer or NULL to turn off monitor

-snes_linesearch_monitor [:filename] - enables the monitor

This monitor is implemented differently than the other line search monitors that are set with SNESLineSearchMonitorSet() since it is called in many locations of the line search routines to display aspects of the line search that are not visible to the other monitors.

SNES: Nonlinear Solvers, SNES, SNESLineSearch, PETSCVIEWERASCII, SNESGetLineSearch(), SNESLineSearchGetDefaultMonitor(), PetscViewer, SNESLineSearchSetMonitor(), SNESLineSearchMonitorSetFromOptions()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchSetDefaultMonitor(SNESLineSearch linesearch, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PETSCVIEWERASCII
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
SNESLineSearchMonitorSet()
```

---

## SNESLineSearchSetFromOptions#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchSetFromOptions/

**Contents:**
- SNESLineSearchSetFromOptions#
- Synopsis#
- Input Parameter#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Implementations#

Sets options for the line search

linesearch - a SNESLineSearch line search context

-snes_linesearch_type (none|basic|bt|secant|cp|nleqerr|bisection|shell) - Line search type, see SNESLineSearchType

-snes_linesearch_order order - 1, 2, 3. Most types only support certain orders (bt supports 1, 2 or 3)

-snes_linesearch_norms (true|false) - Turn on/off the linesearch norms for the basic linesearch typem (SNESLineSearchSetComputeNorms())

-snes_linesearch_minlambda minlambda - The minimum lambda

-snes_linesearch_maxlambda maxlambda - The maximum lambda

-snes_linesearch_rtol rtol - Relative tolerance for iterative line searches

-snes_linesearch_atol atol - Absolute tolerance for iterative line searches

-snes_linesearch_ltol ltol - Change in lambda tolerance for iterative line searches

-snes_linesearch_max_it max_it - The number of iterations for iterative line searches

-snes_linesearch_monitor [:filename] - Print progress of line searches

-snes_linesearch_monitor_solution_update [viewer:filename:format] - view each update tried by line search routine

-snes_linesearch_damping damping - The linesearch damping parameter

-snes_linesearch_keeplambda (true|false) - Keep the previous lambda as the initial guess.

-snes_linesearch_precheck_picard (true|false) - Use precheck that speeds up convergence of picard method

-snes_linesearch_precheck_picard_angle angle - Angle used in Picard precheck method

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESGetLineSearch(), SNESLineSearchCreate(), SNESLineSearchSetOrder(), SNESLineSearchSetType(), SNESLineSearchSetTolerances(), SNESLineSearchSetDamping(), SNESLineSearchPreCheckPicard(), SNESLineSearchType, SNESLineSearchSetComputeNorms()

src/snes/linesearch/interface/linesearch.c

SNESLineSearchSetFromOptions_BT() in src/snes/linesearch/impls/bt/linesearchbt.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchSetFromOptions(SNESLineSearch linesearch)
```

Example 2 (unknown):
```unknown
SNESLineSearch
```

Example 3 (unknown):
```unknown
SNESLineSearchType
```

Example 4 (unknown):
```unknown
SNESLineSearchSetComputeNorms()
```

---

## SNESLineSearchSetFunction#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchSetFunction/

**Contents:**
- SNESLineSearchSetFunction#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Note#
- See Also#
- Level#
- Location#

Sets the function evaluation used by the SNES line search `

linesearch - the SNESLineSearch context

func - function evaluation routine, this is usually the function provided with SNESSetFunction()

snes - the SNES with which the SNESLineSearch context is associated with

f - the computed value of the function

By default the SNESLineSearch uses the function provided by SNESSetFunction() so this is rarely needed

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESGetLineSearch(), SNESSetFunction()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchSetFunction(SNESLineSearch linesearch, PetscErrorCode (*func)(SNES snes, Vec x, Vec f))
```

Example 2 (unknown):
```unknown
SNESLineSearch
```

Example 3 (unknown):
```unknown
SNESSetFunction()
```

Example 4 (unknown):
```unknown
SNESLineSearch
```

---

## SNESLineSearchSetLambda#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchSetLambda/

**Contents:**
- SNESLineSearchSetLambda#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the line search lambda (scaling of the solution update)

linesearch - line search context

lambda - The lambda to use

This routine is typically used within implementations of SNESLineSearchApply() to set the final lambda. This routine (and SNESLineSearchGetLambda()) were added to facilitate Quasi-Newton methods that use the previous lambda as an inner scaling parameter.

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchGetLambda()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchSetLambda(SNESLineSearch linesearch, PetscReal lambda)
```

Example 2 (unknown):
```unknown
SNESLineSearchApply()
```

Example 3 (unknown):
```unknown
SNESLineSearchGetLambda()
```

Example 4 (unknown):
```unknown
SNESLineSearch
```

---

## SNESLineSearchSetNorms#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchSetNorms/

**Contents:**
- SNESLineSearchSetNorms#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the computed norms for the current solution X, the current update Y, and the current function value F.

linesearch - the line search context

xnorm - The norm of the current solution

fnorm - The norm of the current function, this is the norm(function(X)) where X is the current solution

ynorm - The norm of the current update (after scaling by the linesearch computed lambda)

This is called by the line search routines to store the values they have just computed

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchGetNorms(), SNESLineSearchSetVecs()

src/snes/linesearch/interface/linesearch.c

src/snes/tutorials/ex1f.F90

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchSetNorms(SNESLineSearch linesearch, PetscReal xnorm, PetscReal fnorm, PetscReal ynorm)
```

Example 2 (r):
```r
norm(function(X))
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
SNESLineSearchGetNorms()
```

---

## SNESLineSearchSetOrder#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchSetOrder/

**Contents:**
- SNESLineSearchSetOrder#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Sets the maximum order of the polynomial fit used in the line search

linesearch - the line search context

1 or SNES_LINESEARCH_ORDER_LINEAR - linear order

2 or SNES_LINESEARCH_ORDER_QUADRATIC - quadratic order

3 or SNES_LINESEARCH_ORDER_CUBIC - cubic order

-snes_linesearch_order order - 1, 2, 3. Most types only support certain orders (SNESLINESEARCHBT supports 2 or 3)

These orders are supported by SNESLINESEARCHBT and SNESLINESEARCHCP

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchGetOrder(), SNESLineSearchSetDamping()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchSetOrder(SNESLineSearch linesearch, PetscInt order)
```

Example 2 (unknown):
```unknown
SNES_LINESEARCH_ORDER_LINEAR
```

Example 3 (unknown):
```unknown
SNES_LINESEARCH_ORDER_QUADRATIC
```

Example 4 (unknown):
```unknown
SNES_LINESEARCH_ORDER_CUBIC
```

---

## SNESLineSearchSetPostCheck#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchSetPostCheck/

**Contents:**
- SNESLineSearchSetPostCheck#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets a user function that is called after the line search has been applied to determine the step direction and length. Allows the user a chance to change or override the decision of the line search routine

linesearch - the SNESLineSearch context

func - [optional] function evaluation routine

ctx - [optional] user-defined context for private data for the function evaluation routine (may be NULL)

ls - the SNESLineSearch context

x - the current solution

d - the current search direction

w - \( w = x + lambda*d \) for some lambda

changed_d - indicates if the search direction d has been changed

changed_w - indicates w has been changed

ctx - the context passed to SNESLineSearchSetPreCheck()

Use SNESLineSearchSetPreCheck() to change the step before the line search is completed. The calling sequence of the callback does not contain the current scaling factor. To access the value, use SNESLineSearchGetLambda().

Use SNESVISetVariableBounds() and SNESVISetComputeVariableBounds() to cause SNES to automatically control the ranges of variables allowed.

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESGetLineSearch(), SNESLineSearchPostCheck(), SNESLineSearchSetPreCheck(), SNESLineSearchGetPreCheck(), SNESLineSearchGetPostCheck(), SNESVISetVariableBounds(), SNESVISetComputeVariableBounds(), SNESSetFunctionDomainError(), SNESSetJacobianDomainError()

src/snes/linesearch/interface/linesearch.c

src/snes/tutorials/ex3.c src/ts/tutorials/ex27.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchSetPostCheck(SNESLineSearch linesearch, PetscErrorCode (*func)(SNESLineSearch ls, Vec x, Vec d, Vec w, PetscBool *changed_d, PetscBool *changed_w, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESLineSearch
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
SNESLineSearchSetPreCheck()
```

---

## SNESLineSearchSetPreCheck#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchSetPreCheck/

**Contents:**
- SNESLineSearchSetPreCheck#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets a function that is called after the initial search direction has been computed but before the line search routine has been applied. Allows adjusting the result of (usually a linear solve) that determined the search direction.

linesearch - the SNESLineSearch context

func - [optional] function evaluation routine

ctx - [optional] user-defined context for private data for the function evaluation routine (may be NULL)

ls - the SNESLineSearch context

x - the current solution

d - the current search direction

changed_d - indicates if the search direction has been changed

ctx - the context passed to SNESLineSearchSetPreCheck()

Use SNESLineSearchSetPostCheck() to change the step after the line search is complete.

Use SNESVISetVariableBounds() and SNESVISetComputeVariableBounds() to cause SNES to automatically control the ranges of variables allowed.

SNES: Nonlinear Solvers, SNES, SNESGetLineSearch(), SNESLineSearchPreCheck(), SNESLineSearchSetPostCheck(), SNESLineSearchGetPostCheck(), SNESLineSearchGetPreCheck(), SNESVISetVariableBounds(), SNESVISetComputeVariableBounds(), SNESSetFunctionDomainError(), SNESSetJacobianDomainError()

src/snes/linesearch/interface/linesearch.c

src/snes/tutorials/ex15.c src/snes/tutorials/ex3.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchSetPreCheck(SNESLineSearch linesearch, PetscErrorCode (*func)(SNESLineSearch ls, Vec x, Vec d, PetscBool *changed_d, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESLineSearch
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
SNESLineSearchSetPreCheck()
```

---

## SNESLineSearchSetReason#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchSetReason/

**Contents:**
- SNESLineSearchSetReason#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Sets the success/failure reason of the line search application

Logically Collective; No Fortran Support

linesearch - the line search context

reason - The success or failure reason

This is typically called in a SNESLineSearchType implementation of SNESLineSearchApply() or a SNESLINESEARCHSHELL implementation to set the success or failure of the line search method.

Do not call this from callbacks provided with SNESSetFunction(), instead perhaps use SNESSetFunctionDomainError()

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchReason, SNESLineSearchGetSResult(), SNESSetFunctionDomainError(), SNESSetFunction()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchSetReason(SNESLineSearch linesearch, SNESLineSearchReason reason)
```

Example 2 (unknown):
```unknown
SNESLineSearchType
```

Example 3 (unknown):
```unknown
SNESLineSearchApply()
```

Example 4 (unknown):
```unknown
SNESLINESEARCHSHELL
```

---

## SNESLineSearchSetSNES#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchSetSNES/

**Contents:**
- SNESLineSearchSetSNES#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the SNES for the linesearch for function evaluation.

linesearch - the line search context

snes - The SNES instance

This happens automatically when the line search is obtained/created with SNESGetLineSearch(). This routine is therefore mainly called within SNES implementations.

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchGetSNES(), SNESLineSearchSetVecs()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchSetSNES(SNESLineSearch linesearch, SNES snes)
```

Example 2 (unknown):
```unknown
SNESGetLineSearch()
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
SNESLineSearchGetSNES()
```

---

## SNESLineSearchSetTolerances#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchSetTolerances/

**Contents:**
- SNESLineSearchSetTolerances#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#

Sets the tolerances for the linesearch.

linesearch - the line search context

minlambda - The minimum lambda allowed

maxlambda - The maximum lambda allowed

rtol - The relative tolerance for iterative line searches

atol - The absolute tolerance for iterative line searches

ltol - The change in lambda tolerance for iterative line searches

max_it - The maximum number of iterations of the line search

-snes_linesearch_minlambda - The minimum lambda allowed

-snes_linesearch_maxlambda - The maximum lambda allowed

-snes_linesearch_rtol - Relative tolerance for iterative line searches

-snes_linesearch_atol - Absolute tolerance for iterative line searches

-snes_linesearch_ltol - Change in lambda tolerance for iterative line searches

-snes_linesearch_max_it - The number of iterations for iterative line searches

The user may choose to not set any of the tolerances using PETSC_DEFAULT in place of an argument.

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchGetTolerances()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchSetTolerances(SNESLineSearch linesearch, PetscReal minlambda, PetscReal maxlambda, PetscReal rtol, PetscReal atol, PetscReal ltol, PetscInt max_it)
```

Example 2 (unknown):
```unknown
PETSC_DEFAULT
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
SNESLineSearchGetTolerances()
```

---

## SNESLineSearchSetType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchSetType/

**Contents:**
- SNESLineSearchSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the SNESLinesearchType of a SNESLineSearch object to indicate the line search algorithm that should be used by a given SNES solver

linesearch - the line search context

type - The type of line search to be used, see SNESLineSearchType

-snes_linesearch_type (none|basic|bt|secant|cp|nleqerr|bisection|shell) - Line search type to use, see SNESLineSearchType

The SNESLineSearch object is generally obtained with SNESGetLineSearch()

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchType, SNESLineSearchCreate(), SNESLineSearchSetFromOptions(), SNESLineSearchGetType(), SNESGetLineSearch()

src/snes/linesearch/interface/linesearch.c

src/snes/tutorials/ex1f.F90 src/ts/tutorials/ex22.c src/ts/tutorials/ex22f.F90 src/ts/utils/dmplexlandau/tutorials/ex1f90.F90

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLinesearchType
```

Example 2 (unknown):
```unknown
SNESLineSearch
```

Example 3 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchSetType(SNESLineSearch linesearch, SNESLineSearchType type)
```

Example 4 (unknown):
```unknown
SNESLineSearchType
```

---

## SNESLineSearchSetUp#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchSetUp/

**Contents:**
- SNESLineSearchSetUp#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#

Prepares the line search for being applied by allocating any required vectors.

linesearch - The SNESLineSearch instance.

For most cases, this needn’t be called by users or outside of SNESLineSearchApply(). The only current case where this is called outside of this is for the VI solvers, which modify the solution and work vectors before the first call of SNESLineSearchApply(), requiring the SNESLineSearch work vectors to be allocated upfront.

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESGetLineSearch(), SNESLineSearchReset()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchSetUp(SNESLineSearch linesearch)
```

Example 2 (unknown):
```unknown
SNESLineSearch
```

Example 3 (unknown):
```unknown
SNESLineSearchApply()
```

Example 4 (unknown):
```unknown
SNESLineSearchApply()
```

---

## SNESLineSearchSetVecs#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchSetVecs/

**Contents:**
- SNESLineSearchSetVecs#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the vectors on the SNESLineSearch context

linesearch - the line search context

Y - Search direction vector

W - Solution work vector

G - Function work vector

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchSetNorms(), SNESLineSearchGetVecs()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLineSearch
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchSetVecs(SNESLineSearch linesearch, Vec X, Vec F, Vec Y, Vec W, Vec G)
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
SNESLineSearchSetNorms()
```

---

## SNESLineSearchSetVIFunctions#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchSetVIFunctions/

**Contents:**
- SNESLineSearchSetVIFunctions#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Sets VI-specific functions for line search computation.

linesearch - the linesearch object

projectfunc - function for projecting the function to the bounds, see SNESLineSearchVIProjectFn for calling sequence

normfunc - function for computing the norm of an active set, see SNESLineSearchVINormFn for calling sequence

dirderivfunc - function for computing the directional derivative of an active set, see SNESLineSearchVIDirDerivFn for calling sequence

The VI solvers require projection of the solution to the feasible set. projectfunc should implement this.

The VI solvers require special evaluation of the function norm such that the norm is only calculated on the inactive set. This should be implemented by normfunc.

The VI solvers further require special evaluation of the directional derivative (when assuming that there exists some \(G(x)\) for which the SNESFunctionFn \(F(x) = grad G(x)\)) such that it is only calculated on the inactive set. This should be implemented by dirderivfunc.

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchGetVIFunctions(), SNESLineSearchSetPostCheck(), SNESLineSearchSetPreCheck(), SNESLineSearchVIProjectFn, SNESLineSearchVINormFn, SNESLineSearchVIDirDerivFn

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchSetVIFunctions(SNESLineSearch linesearch, SNESLineSearchVIProjectFn *projectfunc, SNESLineSearchVINormFn *normfunc, SNESLineSearchVIDirDerivFn *dirderivfunc)
```

Example 2 (unknown):
```unknown
SNESLineSearchVIProjectFn
```

Example 3 (unknown):
```unknown
SNESLineSearchVINormFn
```

Example 4 (unknown):
```unknown
SNESLineSearchVIDirDerivFn
```

---

## SNESLineSearchSetWorkVecs#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchSetWorkVecs/

**Contents:**
- SNESLineSearchSetWorkVecs#
- Synopsis#
- Input Parameters#
- Developer Note#
- See Also#
- Level#
- Location#

Sets work vectors for the line search.

linesearch - the SNESLineSearch context

nwork - the number of work vectors

This is called from within the set up routines for each of the line search types SNESLineSearchType

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESSetWorkVecs()

src/snes/linesearch/interface/linesearch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchSetWorkVecs(SNESLineSearch linesearch, PetscInt nwork)
```

Example 2 (unknown):
```unknown
SNESLineSearch
```

Example 3 (unknown):
```unknown
SNESLineSearchType
```

Example 4 (unknown):
```unknown
SNESLineSearch
```

---

## SNESLineSearchShellApplyFn#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchShellApplyFn/

**Contents:**
- SNESLineSearchShellApplyFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

Function type for the user-supplied apply routine registered with the SNESLINESEARCHSHELL line-search

ls - the SNESLineSearch object

ctx - optional user-provided context set with SNESLineSearchShellSetApply()

SNESLineSearch, SNESLINESEARCHSHELL, SNESLineSearchShellSetApply(), SNESLineSearchApplyFn

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLINESEARCHSHELL
```

Example 2 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode              SNESLineSearchShellApplyFn(SNESLineSearch ls, PetscCtx ctx);
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
SNESLineSearchShellSetApply()
```

---

## SNESLineSearchShellGetApply#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchShellGetApply/

**Contents:**
- SNESLineSearchShellGetApply#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Gets the apply function and context for the SNESLINESEARCHSHELL

linesearch - the line search object

func - the user function; can be NULL if it is not needed, see SNESLineSearchShellApplyFn for calling sequence

ctx - the user function context; can be NULL if it is not needed

SNES: Nonlinear Solvers, SNESLineSearchShellSetApply(), SNESLINESEARCHSHELL, SNESLineSearchType, SNESLineSearch, SNESLineSearchShellApplyFn

src/snes/linesearch/impls/shell/linesearchshell.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLINESEARCHSHELL
```

Example 2 (unknown):
```unknown
PetscErrorCode SNESLineSearchShellGetApply(SNESLineSearch linesearch, SNESLineSearchShellApplyFn **func, PetscCtxRt ctx)
```

Example 3 (unknown):
```unknown
SNESLineSearchShellApplyFn
```

Example 4 (unknown):
```unknown
SNESLineSearchShellSetApply()
```

---

## SNESLineSearchShellSetApply#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchShellSetApply/

**Contents:**
- SNESLineSearchShellSetApply#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the apply function for the SNESLINESEARCHSHELL implementation.

linesearch - SNESLineSearch context

func - function implementing the linesearch shell, see SNESLineSearchShellApplyFn for calling sequence

ctx - context for func

SNES: Nonlinear Solvers, SNESLineSearchShellGetApply(), SNESLINESEARCHSHELL, SNESLineSearchType, SNESLineSearch, SNESLineSearchShellApplyFn

src/snes/linesearch/impls/shell/linesearchshell.c

src/snes/tutorials/ex1f.F90

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLINESEARCHSHELL
```

Example 2 (unknown):
```unknown
PetscErrorCode SNESLineSearchShellSetApply(SNESLineSearch linesearch, SNESLineSearchShellApplyFn *func, PetscCtx ctx)
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
SNESLineSearchShellApplyFn
```

---

## SNESLINESEARCHSHELL#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLINESEARCHSHELL/

**Contents:**
- SNESLINESEARCHSHELL#
- See Also#
- Level#
- Location#

Provides an API for a user-provided line search routine. Any of the other line searches may serve as a guide to how this is to be done. There is also a basic template in the documentation for SNESLineSearchShellSetApply().

SNES: Nonlinear Solvers, SNESLineSearch, SNES, SNESLineSearchCreate(), SNESLineSearchSetType(), SNESLineSearchShellSetApply(), SNESLineSearchShellApplyFn

src/snes/linesearch/impls/shell/linesearchshell.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLineSearchShellSetApply()
```

Example 2 (unknown):
```unknown
SNESLineSearch
```

Example 3 (unknown):
```unknown
SNESLineSearchCreate()
```

Example 4 (unknown):
```unknown
SNESLineSearchSetType()
```

---

## SNESLineSearchType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchType/

**Contents:**
- SNESLineSearchType#
- Synopsis#
- Values#
- Note#
- See Also#
- Level#
- Location#

String with the name of a PETSc line search method SNESLineSearch. Provides all the linesearches for the nonlinear solvers, SNES, in PETSc.

SNESLINESEARCHBASIC - (or equivalently SNESLINESEARCHNONE) Simple damping line search, defaults to using the full Newton step

SNESLINESEARCHBT - Backtracking line search over the L2 norm of the function or an objective function

SNESLINESEARCHSECANT - Secant line search over the L2 norm of the function or an objective function

SNESLINESEARCHCP - Critical point secant line search assuming \(F(x) = \nabla G(x)\) for some unknown \(G(x)\)

SNESLINESEARCHNLEQERR - Affine-covariant error-oriented linesearch

SNESLINESEARCHBISECTION - bisection line search for a root in the directional derivative

SNESLINESEARCHSHELL - User provided SNESLineSearch implementation

Use SNESLineSearchSetType() or the options database key -snes_linesearch_type to set the specific line search algorithm to use with a given SNES object. Not all SNESType can utilize a line search.

SNES: Nonlinear Solvers, SNESLineSearch, SNESLineSearchSetType(), SNES

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLineSearch
```

Example 2 (rust):
```rust
typedef const char *SNESLineSearchType;
#define SNESLINESEARCHBT        "bt"
#define SNESLINESEARCHNLEQERR   "nleqerr"
#define SNESLINESEARCHBASIC     "basic"
#define SNESLINESEARCHNONE      "none"
#define SNESLINESEARCHSECANT    "secant"
#define SNESLINESEARCHL2        PETSC_DEPRECATED_MACRO(3, 24, 0, "SNESLINESEARCHSECANT", ) "secant"
#define SNESLINESEARCHCP        "cp"
#define SNESLINESEARCHSHELL     "shell"
#define SNESLINESEARCHNCGLINEAR "ncglinear"
#define SNESLINESEARCHBISECTION "bisection"
```

Example 3 (unknown):
```unknown
SNESLINESEARCHBASIC
```

Example 4 (unknown):
```unknown
SNESLINESEARCHNONE
```

---

## SNESLineSearchVIDirDerivFn#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchVIDirDerivFn/

**Contents:**
- SNESLineSearchVIDirDerivFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

A prototype of a SNES function that computes the directional derivative considering the VI bounds, passed to SNESLineSearchSetVIFunctions()

f - the function vector to compute the directional derivative with

u - the current solution, entries that are on the VI bounds are ignored

y - the direction to compute the directional derivative

fty - the resulting directional derivative

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESLineSearchVINormFn, SNESLineSearchVIProjectFn, SNESLineSearchSetVIFunctions(), SNESLineSearchGetVIFunctions()

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLineSearchSetVIFunctions()
```

Example 2 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode SNESLineSearchVIDirDerivFn(SNES snes, Vec f, Vec u, Vec y, PetscScalar *fty);
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
SNESLineSearchVINormFn
```

---

## SNESLineSearchView#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchView/

**Contents:**
- SNESLineSearchView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Prints useful information about the line search

linesearch - line search context

viewer - the PetscViewer to display the line search information to

SNES: Nonlinear Solvers, SNES, SNESLineSearch, PetscViewer, SNESLineSearchCreate()

src/snes/linesearch/interface/linesearch.c

SNESLineSearchView_BT() in src/snes/linesearch/impls/bt/linesearchbt.c SNESLineSearchView_NLEQERR() in src/snes/linesearch/impls/nleqerr/linesearchnleqerr.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESLineSearchView(SNESLineSearch linesearch, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## SNESLineSearchVINormFn#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchVINormFn/

**Contents:**
- SNESLineSearchVINormFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

A prototype of a SNES function that computes the norm of the active set variables in a vector in a variational inequality (VI) solve, passed to SNESLineSearchSetVIFunctions()

f - the vector to compute the norm of

u - the current solution, entries that are on the variational inequality (VI) bounds are ignored

fnorm - the resulting norm

SNES: Nonlinear Solvers, SNES, SNESLineSearch

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLineSearchSetVIFunctions()
```

Example 2 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode          SNESLineSearchVINormFn(SNES snes, Vec f, Vec u, PetscReal *fnorm);
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

---

## SNESLineSearchVIProjectFn#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearchVIProjectFn/

**Contents:**
- SNESLineSearchVIProjectFn#
- Synopsis#
- Calling Sequence#
- Note#
- See Also#
- Level#
- Location#

A prototype of a SNES function that projects a vector onto the VI bounds, passed to SNESLineSearchSetVIFunctions()

u - the vector to project to the bounds

The deprecated SNESLineSearchVIProjectFunc still works as a replacement for SNESLineSearchVIProjectFn *.

SNES: Nonlinear Solvers, SNES, SNESLineSearch

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLineSearchSetVIFunctions()
```

Example 2 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode             SNESLineSearchVIProjectFn(SNES snes, Vec u);
```

Example 3 (unknown):
```unknown
SNESLineSearchVIProjectFunc
```

Example 4 (unknown):
```unknown
SNESLineSearchVIProjectFn
```

---

## SNESLineSearch#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLineSearch/

**Contents:**
- SNESLineSearch#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#

Abstract PETSc object that manages line-search operations for nonlinear solvers

SNES: Nonlinear Solvers, SNESLineSearchType, SNESLineSearchCreate(), SNESLineSearchSetType(), SNES

src/snes/tutorials/ex1f.F90 src/ts/tutorials/ex27.c src/ts/tutorials/ex22.c src/snes/tutorials/ex15.c src/snes/tutorials/ex3.c src/ts/tutorials/ex22f.F90 src/ts/utils/dmplexlandau/tutorials/ex1f90.F90

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_LineSearch *SNESLineSearch;
```

Example 2 (unknown):
```unknown
SNESLineSearchType
```

Example 3 (unknown):
```unknown
SNESLineSearchCreate()
```

Example 4 (unknown):
```unknown
SNESLineSearchSetType()
```

---

## SNESLoad#

**URL:** https://petsc.org/release/manualpages/SNES/SNESLoad/

**Contents:**
- SNESLoad#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Loads a SNES that has been stored in PETSCVIEWERBINARY with SNESView().

snes - the newly loaded SNES, this needs to have been created with SNESCreate() or some related function before a call to SNESLoad().

viewer - binary file viewer, obtained from PetscViewerBinaryOpen()

The SNESType is determined by the data in the file, any type set into the SNES before this call is ignored.

SNES: Nonlinear Solvers, SNES, PetscViewer, SNESCreate(), SNESType, PetscViewerBinaryOpen(), SNESView(), MatLoad(), VecLoad()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCVIEWERBINARY
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESLoad(SNES snes, PetscViewer viewer)
```

Example 3 (unknown):
```unknown
SNESCreate()
```

Example 4 (unknown):
```unknown
PetscViewerBinaryOpen()
```

---

## SNESMonitorCancel#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMonitorCancel/

**Contents:**
- SNESMonitorCancel#
- Synopsis#
- Input Parameter#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Clears all the monitor functions for a SNES object.

snes - the SNES context

-snes_monitor_cancel - cancels all monitors that have been hardwired into a code by calls to SNESMonitorSet(), but does not cancel those set via the options database

There is no way to clear one specific monitor from a SNES object.

SNES: Nonlinear Solvers, SNES, SNESMonitorDefault(), SNESMonitorSet()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESMonitorCancel(SNES snes)
```

Example 2 (unknown):
```unknown
SNESMonitorSet()
```

Example 3 (unknown):
```unknown
SNESMonitorDefault()
```

Example 4 (unknown):
```unknown
SNESMonitorSet()
```

---

## SNESMonitorDefaultField#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMonitorDefaultField/

**Contents:**
- SNESMonitorDefaultField#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Monitors progress of a SNESSolve(), separated into fields.

snes - the SNES context

its - iteration number

fgnorm - 2-norm of residual

-snes_monitor_field - activate this monitor

This routine uses the DM attached to the residual vector to define the fields.

This is not called directly by users, rather one calls SNESMonitorSet(), with this function as an argument, to cause the monitor to be used during the SNES solve.

SNES: Nonlinear Solvers, SNESMonitorSet(), SNESMonitorSolution(), SNESMonitorDefault(), PetscViewerFormat, PetscViewerAndFormat

src/snes/interface/snesut.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petsc/private/snesimpl.h"   
PetscErrorCode SNESMonitorDefaultField(SNES snes, PetscInt its, PetscReal fgnorm, PetscViewerAndFormat *vf)
```

Example 3 (unknown):
```unknown
SNESMonitorSet()
```

Example 4 (unknown):
```unknown
SNESMonitorSet()
```

---

## SNESMonitorDefaultSetUp#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMonitorDefaultSetUp/

**Contents:**
- SNESMonitorDefaultSetUp#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Prepare the PetscViewerAndFormat associated with SNESMonitorDefault(), in particular by initializing the underlying PetscDrawLG when the viewer format is PETSC_VIEWER_DRAW_LG

snes - the SNES context

vf - the viewer/format pair passed to SNESMonitorSet() along with SNESMonitorDefault()

SNES: Nonlinear Solvers, SNES, SNESMonitorSet(), SNESMonitorDefault(), PetscViewerAndFormat, PetscViewerMonitorLGSetUp()

src/snes/interface/snesut.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewerAndFormat
```

Example 2 (unknown):
```unknown
SNESMonitorDefault()
```

Example 3 (unknown):
```unknown
PetscDrawLG
```

Example 4 (unknown):
```unknown
PETSC_VIEWER_DRAW_LG
```

---

## SNESMonitorDefault#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMonitorDefault/

**Contents:**
- SNESMonitorDefault#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Monitors progress of a SNESSolve() (default).

snes - the SNES context

its - iteration number

fgnorm - 2-norm of residual

vf - viewer and format structure

-snes_monitor - use this function to monitor the convergence of the nonlinear solver

Prints the residual norm at each iteration.

This is not called directly by users, rather one calls SNESMonitorSet(), with this function as an argument, to cause the monitor to be used during the SNES solve.

SNES: Nonlinear Solvers, SNESMonitorSet(), SNESMonitorSolution(), SNESMonitorFunction(), SNESMonitorResidual(), SNESMonitorSolutionUpdate(), SNESMonitorScaling(), SNESMonitorRange(), SNESMonitorRatio(), SNESMonitorDefaultField(), PetscViewerFormat, PetscViewerAndFormat

src/snes/interface/snesut.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petsc/private/snesimpl.h"   
PetscErrorCode SNESMonitorDefault(SNES snes, PetscInt its, PetscReal fgnorm, PetscViewerAndFormat *vf)
```

Example 3 (unknown):
```unknown
SNESMonitorSet()
```

Example 4 (unknown):
```unknown
SNESMonitorSet()
```

---

## SNESMonitorFields#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMonitorFields/

**Contents:**
- SNESMonitorFields#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Monitors the residual for each field separately

snes - the SNES context, must have an attached DM

its - iteration number

fgnorm - 2-norm of residual

vf - PetscViewerAndFormat of PetscViewerType PETSCVIEWERASCII

This routine prints the residual norm at each iteration.

SNES: Nonlinear Solvers, SNES, SNESMonitorSet(), SNESMonitorDefault()

src/snes/utils/dmplexsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode SNESMonitorFields(SNES snes, PetscInt its, PetscReal fgnorm, PetscViewerAndFormat *vf)
```

Example 2 (unknown):
```unknown
PetscViewerAndFormat
```

Example 3 (unknown):
```unknown
PetscViewerType
```

Example 4 (unknown):
```unknown
PETSCVIEWERASCII
```

---

## SNESMonitorFunction#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMonitorFunction/

**Contents:**
- SNESMonitorFunction#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

functional form passed to SNESMonitorSet() to monitor convergence of nonlinear solver

snes - the SNES context

its - iteration number

norm - 2-norm function value (may be estimated)

mctx - [optional] monitoring context

SNES: Nonlinear Solvers, SNESMonitorSet(), PetscCtx

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESMonitorSet()
```

Example 2 (cpp):
```cpp
#include <petscsnes.h>
PetscErrorCode SNESMonitorFunction(SNES snes, PetscInt its, PetscReal norm, PetscCtx mctx)
```

Example 3 (unknown):
```unknown
SNESMonitorSet()
```

---

## SNESMonitorJacUpdateSpectrum#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMonitorJacUpdateSpectrum/

**Contents:**
- SNESMonitorJacUpdateSpectrum#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Monitors the spectrun of the change in the Jacobian from the last Jacobian evaluation of a SNESSolve()

snes - the SNES context

it - iteration number

fnorm - 2-norm of residual

vf - viewer and format structure

-snes_monitor_jacupdate_spectrum - activates this monitor

This routine prints the eigenvalues of the difference in the Jacobians

This is not called directly by users, rather one calls SNESMonitorSet(), with this function as an argument, to cause the monitor to be used during the SNES solve.

SNES: Nonlinear Solvers, SNESMonitorSet(), SNESMonitorSolution(), SNESMonitorRange(), PetscViewerFormat, PetscViewerAndFormat

src/snes/interface/snesut.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petsc/private/snesimpl.h"   
PetscErrorCode SNESMonitorJacUpdateSpectrum(SNES snes, PetscInt it, PetscReal fnorm, PetscViewerAndFormat *vf)
```

Example 3 (unknown):
```unknown
SNESMonitorSet()
```

Example 4 (unknown):
```unknown
SNESMonitorSet()
```

---

## SNESMonitorLGRange#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMonitorLGRange/

**Contents:**
- SNESMonitorLGRange#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Line-graph monitor that plots the residual norm together with residual-range statistics for a SNESSolve()

snes - the SNES context

n - the iteration number

rnorm - the 2-norm of the residual

monctx - a PetscViewer of type PETSCVIEWERDRAW set up with PetscViewerMonitorLGSetUp()

Plots four line graphs in the viewer: the residual norm (log scale), the fraction of residual entries larger than 20% of the maximum entry, the relative decrease (prev - rnorm)/prev, and their product.

SNES: Nonlinear Solvers, SNES, SNESMonitorSet(), SNESMonitorDefault(), PetscViewerDrawGetDrawLG(), PetscDrawLG

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESMonitorLGRange(SNES snes, PetscInt n, PetscReal rnorm, PetscCtx monctx)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PETSCVIEWERDRAW
```

---

## SNESMonitorRange#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMonitorRange/

**Contents:**
- SNESMonitorRange#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Prints the percentage of residual elements that are more than 10 percent of the maximum entry in the residual in each iteration of a SNESSolve()

snes - SNES iterative context

it - iteration number

rnorm - 2-norm (preconditioned) residual value (may be estimated).

vf - unused monitor context

-snes_monitor_range - Activates SNESMonitorRange()

This is not called directly by users, rather one calls SNESMonitorSet(), with this function as an argument, to cause the monitor to be used during the SNES solve.

SNES: Nonlinear Solvers, SNESMonitorSet(), SNESMonitorDefault(), SNESMonitorLGCreate(), SNESMonitorScaling(), PetscViewerFormat, PetscViewerAndFormat

src/snes/interface/snesut.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petsc/private/snesimpl.h"   
PetscErrorCode SNESMonitorRange(SNES snes, PetscInt it, PetscReal rnorm, PetscViewerAndFormat *vf)
```

Example 3 (unknown):
```unknown
SNESMonitorRange()
```

Example 4 (unknown):
```unknown
SNESMonitorSet()
```

---

## SNESMonitorRatioSetUp#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMonitorRatioSetUp/

**Contents:**
- SNESMonitorRatioSetUp#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Insures the SNES object is saving its history since this monitor needs access to it

snes - the SNES context

vf - PetscViewerAndFormat (ignored)

SNES: Nonlinear Solvers, SNESMonitorSet(), SNESMonitorSolution(), SNESMonitorDefault(), SNESMonitorRatio(), PetscViewerFormat, PetscViewerAndFormat

src/snes/interface/snesut.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsc/private/snesimpl.h"   
PetscErrorCode SNESMonitorRatioSetUp(SNES snes, PetscViewerAndFormat *vf)
```

Example 2 (unknown):
```unknown
PetscViewerAndFormat
```

Example 3 (unknown):
```unknown
SNESMonitorSet()
```

Example 4 (unknown):
```unknown
SNESMonitorSolution()
```

---

## SNESMonitorRatio#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMonitorRatio/

**Contents:**
- SNESMonitorRatio#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Monitors progress of a SNESSolve() by printing the ratio of residual norm at each iteration to the previous.

snes - the SNES context

its - iteration number

fgnorm - 2-norm of residual (or gradient)

vf - context of monitor

-snes_monitor_ratio - activate this monitor

This is not called directly by users, rather one calls SNESMonitorSet(), with this function as an argument, to cause the monitor to be used during the SNES solve.

Be sure to call SNESMonitorRationSetUp() before using this monitor.

SNES: Nonlinear Solvers, SNESMonitorRationSetUp(), SNESMonitorSet(), SNESMonitorSolution(), SNESMonitorDefault(), PetscViewerFormat, PetscViewerAndFormat

src/snes/interface/snesut.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petsc/private/snesimpl.h"   
PetscErrorCode SNESMonitorRatio(SNES snes, PetscInt its, PetscReal fgnorm, PetscViewerAndFormat *vf)
```

Example 3 (unknown):
```unknown
SNESMonitorSet()
```

Example 4 (unknown):
```unknown
SNESMonitorRationSetUp()
```

---

## SNESMonitorResidual#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMonitorResidual/

**Contents:**
- SNESMonitorResidual#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Monitors progress of a SNESSolve() by calling VecView() for the residual at each iteration.

snes - the SNES context

its - iteration number

fgnorm - 2-norm of residual

-snes_monitor_residual [ascii binary draw][:filename][:viewer format] - plots residual (not its norm) at each iteration

This is not called directly by users, rather one calls SNESMonitorSet(), with this function as an argument, to cause the monitor to be used during the SNES solve.

SNES: Nonlinear Solvers, SNES, SNESMonitorSet(), SNESMonitorDefault(), VecView(), SNESMonitor()

src/snes/interface/snesut.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petsc/private/snesimpl.h"   
PetscErrorCode SNESMonitorResidual(SNES snes, PetscInt its, PetscReal fgnorm, PetscViewerAndFormat *vf)
```

Example 3 (unknown):
```unknown
SNESMonitorSet()
```

Example 4 (unknown):
```unknown
SNESMonitorSet()
```

---

## SNESMonitorSAWsCreate#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMonitorSAWsCreate/

**Contents:**
- SNESMonitorSAWsCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

create an SAWs monitor context for SNES

snes - SNES to monitor

ctx - context for monitor

SNES: Nonlinear Solvers, SNESMonitorSet(), SNES, SNESMonitorSAWs(), SNESMonitorSAWsDestroy()

src/snes/interface/saws/snessaws.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESMonitorSAWsCreate(SNES snes, void **ctx)
```

Example 2 (unknown):
```unknown
SNESMonitorSet()
```

Example 3 (unknown):
```unknown
SNESMonitorSAWs()
```

Example 4 (unknown):
```unknown
SNESMonitorSAWsDestroy()
```

---

## SNESMonitorSAWsDestroy#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMonitorSAWsDestroy/

**Contents:**
- SNESMonitorSAWsDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

destroy a monitor context created with SNESMonitorSAWsCreate()

ctx - monitor context

SNES: Nonlinear Solvers, SNESMonitorSAWsCreate()

src/snes/interface/saws/snessaws.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESMonitorSAWsCreate()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESMonitorSAWsDestroy(PetscCtxRt ctx)
```

Example 3 (unknown):
```unknown
SNESMonitorSAWsCreate()
```

---

## SNESMonitorSAWs#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMonitorSAWs/

**Contents:**
- SNESMonitorSAWs#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

monitor solution process of SNES using SAWs

snes - iterative context

rnorm - 2-norm (preconditioned) residual value (may be estimated).

ctx - PetscViewer of type PETSCVIEWERSAWS

SNES: Nonlinear Solvers, PetscViewerSAWsOpen(), SNESMonitorSAWsDestroy(), SNESMonitorSAWsCreate()

src/snes/interface/saws/snessaws.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESMonitorSAWs(SNES snes, PetscInt n, PetscReal rnorm, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PETSCVIEWERSAWS
```

Example 4 (unknown):
```unknown
PetscViewerSAWsOpen()
```

---

## SNESMonitorScaling#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMonitorScaling/

**Contents:**
- SNESMonitorScaling#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Monitors the largest value in each row of the Jacobian of a SNESSolve()

snes - the SNES context

its - iteration number

fgnorm - 2-norm of residual

vf - viewer and format structure

This routine prints the largest value in each row of the Jacobian

This is not called directly by users, rather one calls SNESMonitorSet(), with this function as an argument, to cause the monitor to be used during the SNES solve.

SNES: Nonlinear Solvers, SNESMonitorSet(), SNESMonitorSolution(), SNESMonitorRange(), SNESMonitorJacUpdateSpectrum(), PetscViewerFormat, PetscViewerAndFormat

src/snes/interface/snesut.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petsc/private/snesimpl.h"   
PetscErrorCode SNESMonitorScaling(SNES snes, PetscInt its, PetscReal fgnorm, PetscViewerAndFormat *vf)
```

Example 3 (unknown):
```unknown
SNESMonitorSet()
```

Example 4 (unknown):
```unknown
SNESMonitorSet()
```

---

## SNESMonitorSetFromOptions#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMonitorSetFromOptions/

**Contents:**
- SNESMonitorSetFromOptions#
- Synopsis#
- Input Parameters#
- Calling sequence of monitor#
- Calling sequence of monitorsetup#
- Options Database Key#
- See Also#
- Level#
- Location#

Sets a monitor function and viewer appropriate for the type indicated by the user

snes - SNES object you wish to monitor

name - the monitor type one is seeking

help - message indicating what monitoring is done

manual - manual page for the monitor

monitor - the monitor function, this must use a PetscViewerFormat as its context

monitorsetup - a function that is called once ONLY if the user selected this monitor that may set additional features of the SNES or PetscViewer objects

snes - the nonlinear solver context

it - the current iteration

r - the current function norm

vf - a PetscViewerAndFormat struct that contains the PetscViewer and PetscViewerFormat to use

snes - the nonlinear solver context

vf - a PetscViewerAndFormat struct that contains the PetscViewer and PetscViewerFormat to use

-name - trigger the use of this monitor in SNESSetFromOptions()

SNES: Nonlinear Solvers, PetscOptionsCreateViewer(), PetscOptionsGetReal(), PetscOptionsHasName(), PetscOptionsGetString(), PetscOptionsGetIntArray(), PetscOptionsGetRealArray(), PetscOptionsBool(), PetscOptionsInt(), PetscOptionsString(), PetscOptionsReal(), PetscOptionsName(), PetscOptionsBegin(), PetscOptionsEnd(), PetscOptionsHeadBegin(), PetscOptionsStringArray(), PetscOptionsRealArray(), PetscOptionsScalar(), PetscOptionsBoolGroupBegin(), PetscOptionsBoolGroup(), PetscOptionsBoolGroupEnd(), PetscOptionsFList(), PetscOptionsEList()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESMonitorSetFromOptions(SNES snes, const char name[], const char help[], const char manual[], PetscErrorCode (*monitor)(SNES snes, PetscInt it, PetscReal r, PetscViewerAndFormat *vf), PetscErrorCode (*monitorsetup)(SNES snes, PetscViewerAndFormat *vf))
```

Example 2 (unknown):
```unknown
PetscViewerFormat
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewerAndFormat
```

---

## SNESMonitorSet#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMonitorSet/

**Contents:**
- SNESMonitorSet#
- Synopsis#
- Input Parameters#
- Calling sequence of f#
- Options Database Keys#
- Note#
- Fortran Note#
- See Also#
- Level#
- Location#

Sets an ADDITIONAL function that is to be used at every iteration of the SNES nonlinear solver to display the iteration’s progress.

snes - the SNES context

f - the monitor function, for the calling sequence see SNESMonitorFunction

mctx - [optional] user-defined context for private data for the monitor routine (use NULL if no context is desired)

monitordestroy - [optional] routine that frees monitor context (may be NULL), see PetscCtxDestroyFn for the calling sequence

snes - the SNES object

it - the current iteration

rnorm - norm of the residual

mctx - the optional monitor context

-snes_monitor - sets SNESMonitorDefault()

-snes_monitor draw::draw_lg - sets line graph monitor

-snes_monitor_cancel - cancels all monitors that have been hardwired into a code by calls to SNESMonitorSet(), but does not cancel those set via the options database.

Several different monitoring routines may be set by calling SNESMonitorSet() multiple times; all will be called in the order in which they were set.

Only a single monitor function can be set for each SNES object

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESMonitorDefault(), SNESMonitorCancel(), SNESMonitorFunction, PetscCtxDestroyFn

src/snes/interface/snes.c

src/snes/tutorials/ex21.c src/ts/tutorials/ex30.c src/ts/tutorials/ex52.c src/ts/tutorials/ex7.c src/snes/tutorials/ex3.c src/snes/tutorials/ex2.c src/snes/tutorials/ex22.c src/ts/tutorials/ex12.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESMonitorSet(SNES snes, PetscErrorCode (*f)(SNES snes, PetscInt it, PetscReal rnorm, PetscCtx mctx), PetscCtx mctx, PetscCtxDestroyFn *monitordestroy)
```

Example 2 (unknown):
```unknown
SNESMonitorFunction
```

Example 3 (unknown):
```unknown
PetscCtxDestroyFn
```

Example 4 (unknown):
```unknown
SNESMonitorDefault()
```

---

## SNESMonitorSolutionUpdate#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMonitorSolutionUpdate/

**Contents:**
- SNESMonitorSolutionUpdate#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Monitors progress of a SNESSolve() by calling VecView() for the UPDATE to the solution at each iteration.

snes - the SNES context

its - iteration number

fgnorm - 2-norm of residual

-snes_monitor_solution_update [ascii binary draw][:filename][:viewer format] - plots update to solution at each iteration

This is not called directly by users, rather one calls SNESMonitorSet(), with this function as an argument, to cause the monitor to be used during the SNES solve.

SNES: Nonlinear Solvers, SNESMonitorSet(), SNESMonitorDefault(), VecView(), SNESMonitor()

src/snes/interface/snesut.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petsc/private/snesimpl.h"   
PetscErrorCode SNESMonitorSolutionUpdate(SNES snes, PetscInt its, PetscReal fgnorm, PetscViewerAndFormat *vf)
```

Example 3 (unknown):
```unknown
SNESMonitorSet()
```

Example 4 (unknown):
```unknown
SNESMonitorSet()
```

---

## SNESMonitorSolution#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMonitorSolution/

**Contents:**
- SNESMonitorSolution#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Monitors progress of a SNES SNESSolve() by calling VecView() for the approximate solution at each iteration.

snes - the SNES context

its - iteration number

fgnorm - 2-norm of residual

-snes_monitor_solution [ascii binary draw][:filename][:viewer format] - plots solution at each iteration

This is not called directly by users, rather one calls SNESMonitorSet(), with this function as an argument, to cause the monitor to be used during the SNESSolve()

SNES: Nonlinear Solvers, SNES, SNESMonitorSet(), SNESMonitorDefault(), VecView()

src/snes/interface/snesut.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petsc/private/snesimpl.h"   
PetscErrorCode SNESMonitorSolution(SNES snes, PetscInt its, PetscReal fgnorm, PetscViewerAndFormat *vf)
```

Example 3 (unknown):
```unknown
SNESMonitorSet()
```

Example 4 (unknown):
```unknown
SNESSolve()
```

---

## SNESMonitor#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMonitor/

**Contents:**
- SNESMonitor#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

runs any SNES monitor routines provided with SNESMonitor() or the options database

snes - nonlinear solver context obtained from SNESCreate()

iter - current iteration number

rnorm - current relative norm of the residual

This routine is called by the SNESSolve() implementations. It does not typically need to be called by the user.

SNES: Nonlinear Solvers, SNES, SNESMonitorSet()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESMonitor()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESMonitor(SNES snes, PetscInt iter, PetscReal rnorm)
```

Example 3 (unknown):
```unknown
SNESCreate()
```

Example 4 (unknown):
```unknown
SNESSolve()
```

---

## SNESMSFinalizePackage#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMSFinalizePackage/

**Contents:**
- SNESMSFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys everything in the SNESMS package. It is called from PetscFinalize().

SNES: Nonlinear Solvers, SNES, SNESMS, SNESMSRegister(), SNESMSRegisterAll(), SNESMSInitializePackage(), PetscFinalize()

src/snes/impls/ms/ms.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESMSFinalizePackage(void)
```

Example 3 (unknown):
```unknown
SNESMSRegister()
```

Example 4 (unknown):
```unknown
SNESMSRegisterAll()
```

---

## SNESMSGetDamping#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMSGetDamping/

**Contents:**
- SNESMSGetDamping#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get the damping parameter of SNESMS multistage scheme

snes - nonlinear solver context

damping - damping parameter

SNES: Nonlinear Solvers, SNESMSSetDamping(), SNESMS

src/snes/impls/ms/ms.c

SNESMSGetDamping_MS() in src/snes/impls/ms/ms.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESMSGetDamping(SNES snes, PetscReal *damping)
```

Example 2 (unknown):
```unknown
SNESMSSetDamping()
```

---

## SNESMSGetType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMSGetType/

**Contents:**
- SNESMSGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get the type of multistage smoother SNESMS

snes - nonlinear solver context

mstype - type of multistage method

SNES: Nonlinear Solvers, SNESMS, SNESMSSetType(), SNESMSType

src/snes/impls/ms/ms.c

SNESMSGetType_MS() in src/snes/impls/ms/ms.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESMSGetType(SNES snes, SNESMSType *mstype)
```

Example 2 (unknown):
```unknown
SNESMSSetType()
```

---

## SNESMSInitializePackage#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMSInitializePackage/

**Contents:**
- SNESMSInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function initializes everything in the SNESMS package. It is called from SNESInitializePackage().

SNES: Nonlinear Solvers, SNES, SNESMS, SNESMSRegister(), SNESMSRegisterAll(), PetscInitialize()

src/snes/impls/ms/ms.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESInitializePackage()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESMSInitializePackage(void)
```

Example 3 (unknown):
```unknown
SNESMSRegister()
```

Example 4 (unknown):
```unknown
SNESMSRegisterAll()
```

---

## SNESMSRegisterAll#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMSRegisterAll/

**Contents:**
- SNESMSRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the multi-stage methods in SNESMS

SNES: Nonlinear Solvers, SNES, SNESMS, SNESMSRegisterDestroy()

src/snes/impls/ms/ms.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESMSRegisterAll(void)
```

Example 2 (unknown):
```unknown
SNESMSRegisterDestroy()
```

---

## SNESMSRegisterDestroy#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMSRegisterDestroy/

**Contents:**
- SNESMSRegisterDestroy#
- Synopsis#
- See Also#
- Level#
- Location#

Frees the list of schemes that were registered by SNESMSRegister().

SNES: Nonlinear Solvers, SNES, SNESMS, SNESMSRegister(), SNESMSRegisterAll()

src/snes/impls/ms/ms.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESMSRegister()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESMSRegisterDestroy(void)
```

Example 3 (unknown):
```unknown
SNESMSRegister()
```

Example 4 (unknown):
```unknown
SNESMSRegisterAll()
```

---

## SNESMSRegister#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMSRegister/

**Contents:**
- SNESMSRegister#
- Synopsis#
- Input Parameters#
- Notes#
- References#
- See Also#
- Level#
- Location#

register a multistage scheme for SNESMS

Logically Collective, No Fortran Support

name - identifier for method

nstages - number of stages

nregisters - number of registers used by low-storage implementation

stability - scaled stability region

gamma - coefficients, see Ketcheson’s paper [Ket10]

delta - coefficients, see Ketcheson’s paper [Ket10]

betasub - subdiagonal of Shu-Osher form

The notation is described in [Ket10] Ketcheson (2010) Runge-Kutta methods with minimum storage implementations.

Many multistage schemes are of the form

These methods can be registered with

David I Ketcheson. Runge–Kutta methods with minimum storage implementations. Journal of Computational Physics, 229(5):1763–1773, 2010.

SNES: Nonlinear Solvers, SNES, SNESMS

src/snes/impls/ms/ms.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESMSRegister(SNESMSType name, PetscInt nstages, PetscInt nregisters, PetscReal stability, const PetscReal gamma[], const PetscReal delta[], const PetscReal betasub[])
```

Example 2 (unknown):
```unknown
SNESMSRegister("name",s,1,stability,NULL,NULL,alpha);
```

---

## SNESMSSetDamping#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMSSetDamping/

**Contents:**
- SNESMSSetDamping#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set the damping parameter for a SNESMS multistage scheme

snes - nonlinear solver context

damping - damping parameter

SNES: Nonlinear Solvers, SNESMSGetDamping(), SNESMS

src/snes/impls/ms/ms.c

SNESMSSetDamping_MS() in src/snes/impls/ms/ms.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESMSSetDamping(SNES snes, PetscReal damping)
```

Example 2 (unknown):
```unknown
SNESMSGetDamping()
```

---

## SNESMSSetType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMSSetType/

**Contents:**
- SNESMSSetType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set the type of multistage smoother SNESMS

snes - nonlinear solver context

mstype - type of multistage method

SNES: Nonlinear Solvers, SNESMS, SNESMSGetType(), SNESMSType

src/snes/impls/ms/ms.c

SNESMSSetType_MS() in src/snes/impls/ms/ms.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESMSSetType(SNES snes, SNESMSType mstype)
```

Example 2 (unknown):
```unknown
SNESMSGetType()
```

---

## SNESMSType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMSType/

**Contents:**
- SNESMSType#
- Synopsis#
- See Also#
- Level#
- Location#

String with the name of a PETSc SNESMS method.

SNES: Nonlinear Solvers, SNESMS, SNESMSGetType(), SNESMSSetType(), SNES

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef const char *SNESMSType;
#define SNESMSM62       "m62"
#define SNESMSEULER     "euler"
#define SNESMSJAMESON83 "jameson83"
#define SNESMSVLTP11    "vltp11"
#define SNESMSVLTP21    "vltp21"
#define SNESMSVLTP31    "vltp31"
#define SNESMSVLTP41    "vltp41"
#define SNESMSVLTP51    "vltp51"
#define SNESMSVLTP61    "vltp61"
```

Example 2 (unknown):
```unknown
SNESMSGetType()
```

Example 3 (unknown):
```unknown
SNESMSSetType()
```

---

## SNESMS#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMS/

**Contents:**
- SNESMS#
- Options Database Keys#
- Notes#
- References#
- See Also#
- Level#
- Location#

multi-stage smoothers

-snes_ms_type - type of multi-stage smoother

-snes_ms_damping - damping for multi-stage method

These multistage methods are explicit Runge-Kutta methods that are often used as smoothers for FAS multigrid for transport problems. In the linear case, these are equivalent to polynomial smoothers (such as Chebyshev).

Multi-stage smoothers should usually be preconditioned by point-block Jacobi to ensure proper scaling and to normalize the wave speeds.

The methods are specified in low storage form (Ketcheson 2010). New methods can be registered with SNESMSRegister().

See [Ket10], [Jam83], [PG97], and [VLTP81]

Antony Jameson. Solution of the euler equations for two dimensional transonic flow by a multigrid method. Applied mathematics and computation, 13(3-4):327–355, 1983.

David I Ketcheson. Runge–Kutta methods with minimum storage implementations. Journal of Computational Physics, 229(5):1763–1773, 2010.

Niles A Pierce and Michael B Giles. Preconditioned multigrid methods for compressible flow calculations on stretched meshes. Journal of Computational Physics, 136(2):425–445, 1997.

Bram Van Leer, Chang-Hsien Tai, and Kenneth Powell. Design of optimally smoothing multi-stage schemes for the Euler equations. In 9th Computational Fluid Dynamics Conference, 1933. 1981.

SNES: Nonlinear Solvers, SNESCreate(), SNES, SNESSetType(), SNESMS, SNESFAS, KSPCHEBYSHEV, SNESMSSetDamping(), SNESMSGetDamping(), SNESMSSetType(), SNESMSGetType()

src/snes/impls/ms/ms.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESMSRegister()
```

Example 2 (unknown):
```unknown
SNESCreate()
```

Example 3 (unknown):
```unknown
SNESSetType()
```

Example 4 (unknown):
```unknown
KSPCHEBYSHEV
```

---

## SNESMultiblockGetSubSNES#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMultiblockGetSubSNES/

**Contents:**
- SNESMultiblockGetSubSNES#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Gets the SNES contexts for all blocks in a SNESMULTIBLOCK solver.

Not Collective but each SNES obtained is parallel

snes - the solver context

n - the number of blocks

subsnes - the array of SNES contexts

After SNESMultiblockGetSubSNES() the array of SNESs MUST be freed by the user (not each SNES, just the array that contains them).

You must call SNESSetUp() before calling SNESMultiblockGetSubSNES().

SNES: Nonlinear Solvers, SNES, SNESMULTIBLOCK, SNESMultiblockSetIS(), SNESMultiblockSetFields()

src/snes/impls/multiblock/multiblock.c

SNESMultiblockGetSubSNES_Default() in src/snes/impls/multiblock/multiblock.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESMULTIBLOCK
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESMultiblockGetSubSNES(SNES snes, PetscInt *n, SNES *subsnes[])
```

Example 3 (unknown):
```unknown
SNESMultiblockGetSubSNES()
```

Example 4 (unknown):
```unknown
SNESSetUp()
```

---

## SNESMultiblockSetBlockSize#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMultiblockSetBlockSize/

**Contents:**
- SNESMultiblockSetBlockSize#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Sets the block size for structured block division in a SNESMULTIBLOCK solver. If not set the matrix block size is used.

snes - the solver context

SNES: Nonlinear Solvers, SNES, SNESMULTIBLOCK, SNESMultiblockGetSubSNES(), SNESMultiblockSetFields()

src/snes/impls/multiblock/multiblock.c

SNESMultiblockSetBlockSize_Default() in src/snes/impls/multiblock/multiblock.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESMULTIBLOCK
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESMultiblockSetBlockSize(SNES snes, PetscInt bs)
```

Example 3 (unknown):
```unknown
SNESMULTIBLOCK
```

Example 4 (unknown):
```unknown
SNESMultiblockGetSubSNES()
```

---

## SNESMultiblockSetFields#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMultiblockSetFields/

**Contents:**
- SNESMultiblockSetFields#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Sets the fields for one particular block in a SNESMULTIBLOCK solver

name - name of this block, if NULL the number of the block is used

n - the number of fields in this block

fields - the fields in this block

Use SNESMultiblockSetIS() to set a completely general set of row indices as a block.

The SNESMultiblockSetFields() is for defining blocks as a group of strided indices, or fields. For example, if the vector block size is three then one can define a block as field 0, or 1 or 2, or field 0,1 or 0,2 or 1,2 which means 0xx3xx6xx9xx12 … x1xx4xx7xx … xx2xx5xx8xx.. 01x34x67x… 0x23x56x8.. x12x45x78x…. where the numbered entries indicate what is in the block.

This function is called once per block (it creates a new block each time). Solve options for this block will be available under the prefix -multiblock_BLOCKNAME_.

SNES: Nonlinear Solvers, SNES, SNESMULTIBLOCK, SNESMultiblockGetSubSNES(), SNESMultiblockSetBlockSize(), SNESMultiblockSetIS()

src/snes/impls/multiblock/multiblock.c

SNESMultiblockSetFields_Default() in src/snes/impls/multiblock/multiblock.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESMULTIBLOCK
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESMultiblockSetFields(SNES snes, const char name[], PetscInt n, const PetscInt *fields)
```

Example 3 (unknown):
```unknown
SNESMultiblockSetIS()
```

Example 4 (unknown):
```unknown
SNESMultiblockSetFields()
```

---

## SNESMultiblockSetIS#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMultiblockSetIS/

**Contents:**
- SNESMultiblockSetIS#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Sets the global row indices for one particular block in a SNESMULTIBLOCK solver

snes - the solver context

name - name of this block, if NULL the number of the block is used

is - the index set that defines the global row indices in this block

Use SNESMultiblockSetFields(), for blocks defined by strides.

This function is called once per block (it creates a new block each time). Solve options for this block will be available under the prefix -multiblock_BLOCKNAME_.

SNES: Nonlinear Solvers, SNES, SNESMULTIBLOCK, SNESMultiblockGetSubSNES(), SNESMultiblockSetBlockSize(), SNESMultiblockSetFields()

src/snes/impls/multiblock/multiblock.c

SNESMultiblockSetIS_Default() in src/snes/impls/multiblock/multiblock.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESMULTIBLOCK
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESMultiblockSetIS(SNES snes, const char name[], IS is)
```

Example 3 (unknown):
```unknown
SNESMultiblockSetFields()
```

Example 4 (unknown):
```unknown
SNESMULTIBLOCK
```

---

## SNESMultiblockSetType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMultiblockSetType/

**Contents:**
- SNESMultiblockSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Developer Note#
- See Also#
- Level#
- Location#
- Implementations#

Sets the type of block combination used for a SNESMULTIBLOCK solver

snes - the solver context

type - PC_COMPOSITE_ADDITIVE, PC_COMPOSITE_MULTIPLICATIVE (default), PC_COMPOSITE_SYMMETRIC_MULTIPLICATIVE

-snes_multiblock_type (multiplicative|additive|symmetric_multiplicative) - Sets block combination type

This SNESType uses PCCompositeType, while SNESCompositeSetType() uses SNESCOMPOSITE, perhaps they should be unified in the future

SNES: Nonlinear Solvers, SNES, SNESMULTIBLOCK, PCCompositeSetType(), PC_COMPOSITE_ADDITIVE, PC_COMPOSITE_MULTIPLICATIVE, PC_COMPOSITE_SYMMETRIC_MULTIPLICATIVE, PCCompositeType, SNESCOMPOSITE, SNESCompositeSetType()

src/snes/impls/multiblock/multiblock.c

SNESMultiblockSetType_Default() in src/snes/impls/multiblock/multiblock.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESMULTIBLOCK
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESMultiblockSetType(SNES snes, PCCompositeType type)
```

Example 3 (unknown):
```unknown
PC_COMPOSITE_ADDITIVE
```

Example 4 (unknown):
```unknown
PC_COMPOSITE_MULTIPLICATIVE
```

---

## SNESMULTIBLOCK#

**URL:** https://petsc.org/release/manualpages/SNES/SNESMULTIBLOCK/

**Contents:**
- SNESMULTIBLOCK#
- Note#
- See Also#
- Level#
- Location#

Multiblock nonlinear solver that can use overlapping or nonoverlapping blocks, organized additively (Jacobi) or multiplicatively (Gauss-Seidel).

This is much like PCASM, PCBJACOBI, and PCFIELDSPLIT are for linear problems.

SNES: Nonlinear Solvers, SNES, SNESCreate(), SNES, SNESSetType(), SNESNEWTONLS, SNESNEWTONTR, SNESNRICHARDSON, SNESMultiblockSetType(), PC_COMPOSITE_ADDITIVE, PC_COMPOSITE_MULTIPLICATIVE, PC_COMPOSITE_SYMMETRIC_MULTIPLICATIVE, SNESMultiblockSetBlockSize(), SNESMultiblockGetBlockSize(), SNESMultiblockSetFields(), SNESMultiblockSetIS(), SNESMultiblockGetSubSNES(), PCASM, PCBJACOBI

src/snes/impls/multiblock/multiblock.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PCFIELDSPLIT
```

Example 2 (unknown):
```unknown
SNESCreate()
```

Example 3 (unknown):
```unknown
SNESSetType()
```

Example 4 (unknown):
```unknown
SNESNEWTONLS
```

---

## SNESNASMGetDamping#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNASMGetDamping/

**Contents:**
- SNESNASMGetDamping#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Gets the update damping for SNESNASM the nonlinear additive Schwarz solver

snes - the SNES context

SNES: Nonlinear Solvers, SNES, SNESNASM, SNESNASMSetDamping()

src/snes/impls/nasm/nasm.c

SNESNASMGetDamping_NASM() in src/snes/impls/nasm/nasm.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNASMGetDamping(SNES snes, PetscReal *dmp)
```

Example 2 (unknown):
```unknown
SNESNASMSetDamping()
```

---

## SNESNASMGetNumber#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNASMGetNumber/

**Contents:**
- SNESNASMGetNumber#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets number of subsolvers

snes - the SNES context

n - the number of subsolvers

SNES: Nonlinear Solvers, SNESNASM, SNESNASMGetSNES()

src/snes/impls/nasm/nasm.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNASMGetNumber(SNES snes, PetscInt *n)
```

Example 2 (unknown):
```unknown
SNESNASMGetSNES()
```

---

## SNESNASMGetSNES#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNASMGetSNES/

**Contents:**
- SNESNASMGetSNES#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

snes - the SNES context

i - the number of the subsnes to get

subsnes - the subsolver context

SNES: Nonlinear Solvers, SNESNASM, SNESNASMGetNumber()

src/snes/impls/nasm/nasm.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNASMGetSNES(SNES snes, PetscInt i, SNES *subsnes)
```

Example 2 (unknown):
```unknown
SNESNASMGetNumber()
```

---

## SNESNASMGetSubdomains#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNASMGetSubdomains/

**Contents:**
- SNESNASMGetSubdomains#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Get the local subdomain contexts for the nonlinear additive Schwarz solver

Not Collective but some of the objects returned will be parallel

snes - the SNES context

n - the number of local subdomains

subsnes - solvers defined on the local subdomains

iscatter - scatters into the nonoverlapping portions of the local subdomains

oscatter - scatters into the overlapping portions of the local subdomains

gscatter - scatters into the (ghosted) local vector of the local subdomain

SNES: Nonlinear Solvers, SNES, SNESNASM, SNESNASMSetSubdomains()

src/snes/impls/nasm/nasm.c

SNESNASMGetSubdomains_NASM() in src/snes/impls/nasm/nasm.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNASMGetSubdomains(SNES snes, PetscInt *n, SNES *subsnes[], VecScatter *iscatter[], VecScatter *oscatter[], VecScatter *gscatter[])
```

Example 2 (unknown):
```unknown
SNESNASMSetSubdomains()
```

---

## SNESNASMGetSubdomainVecs#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNASMGetSubdomainVecs/

**Contents:**
- SNESNASMGetSubdomainVecs#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Get the processor-local subdomain vectors for the nonlinear additive Schwarz solver

snes - the SNES context

n - the number of local subdomains

x - The subdomain solution vector

y - The subdomain step vector

b - The subdomain RHS vector

xl - The subdomain local vectors (ghosted)

SNES: Nonlinear Solvers, SNES, SNESNASM, SNESNASMGetSubdomains()

src/snes/impls/nasm/nasm.c

SNESNASMGetSubdomainVecs_NASM() in src/snes/impls/nasm/nasm.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNASMGetSubdomainVecs(SNES snes, PetscInt *n, Vec *x[], Vec *y[], Vec *b[], Vec *xl[])
```

Example 2 (unknown):
```unknown
SNESNASMGetSubdomains()
```

---

## SNESNASMGetType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNASMGetType/

**Contents:**
- SNESNASMGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get the type of subdomain update used for the nonlinear additive Schwarz solver SNESNASM

snes - the SNES context

type - the type of update

SNES: Nonlinear Solvers, SNES, SNESNASM, SNESNASMSetType(), PCASMGetType(), PC_ASM_BASIC, PC_ASM_RESTRICT, PCASMType

src/snes/impls/nasm/nasm.c

SNESNASMGetType_NASM() in src/snes/impls/nasm/nasm.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNASMGetType(SNES snes, PCASMType *type)
```

Example 2 (unknown):
```unknown
SNESNASMSetType()
```

Example 3 (unknown):
```unknown
PCASMGetType()
```

Example 4 (unknown):
```unknown
PC_ASM_BASIC
```

---

## SNESNASMSetComputeFinalJacobian#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNASMSetComputeFinalJacobian/

**Contents:**
- SNESNASMSetComputeFinalJacobian#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Schedules the computation of the global and subdomain Jacobians upon convergence for the nonlinear additive Schwarz solver

snes - the SNES context

flg - PETSC_TRUE to compute the Jacobians

This is used almost exclusively in the implementation of SNESASPIN, where the converged subdomain and global Jacobian is needed at each linear iteration.

SNES: Nonlinear Solvers, SNES, SNESNASM, SNESNASMGetSubdomains()

src/snes/impls/nasm/nasm.c

SNESNASMSetComputeFinalJacobian_NASM() in src/snes/impls/nasm/nasm.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNASMSetComputeFinalJacobian(SNES snes, PetscBool flg)
```

Example 2 (unknown):
```unknown
SNESNASMGetSubdomains()
```

---

## SNESNASMSetDamping#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNASMSetDamping/

**Contents:**
- SNESNASMSetDamping#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Sets the update damping for SNESNASM the nonlinear additive Schwarz solver

snes - the SNES context

-snes_nasm_damping dmp - the new solution is obtained as old solution plus dmp times (sum of the solutions on the subdomains)

The new solution is obtained as old solution plus dmp times (sum of the solutions on the subdomains)

SNES: Nonlinear Solvers, SNES, SNESNASM, SNESNASMGetDamping()

src/snes/impls/nasm/nasm.c

SNESNASMSetDamping_NASM() in src/snes/impls/nasm/nasm.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNASMSetDamping(SNES snes, PetscReal dmp)
```

Example 2 (unknown):
```unknown
SNESNASMGetDamping()
```

---

## SNESNASMSetSubdomains#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNASMSetSubdomains/

**Contents:**
- SNESNASMSetSubdomains#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Manually Set the context required to restrict and solve subdomain problems in the nonlinear additive Schwarz solver

snes - the SNES context

n - the number of local subdomains

subsnes - solvers defined on the local subdomains

iscatter - scatters into the nonoverlapping portions of the local subdomains

oscatter - scatters into the overlapping portions of the local subdomains

gscatter - scatters into the (ghosted) local vector of the local subdomain

SNES: Nonlinear Solvers, SNES, SNESNASM, SNESNASMGetSubdomains()

src/snes/impls/nasm/nasm.c

SNESNASMSetSubdomains_NASM() in src/snes/impls/nasm/nasm.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNASMSetSubdomains(SNES snes, PetscInt n, SNES subsnes[], VecScatter iscatter[], VecScatter oscatter[], VecScatter gscatter[])
```

Example 2 (unknown):
```unknown
SNESNASMGetSubdomains()
```

---

## SNESNASMSetType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNASMSetType/

**Contents:**
- SNESNASMSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

Set the type of subdomain update used for the nonlinear additive Schwarz solver SNESNASM

snes - the SNES context

type - the type of update, PC_ASM_BASIC or PC_ASM_RESTRICT

-snes_nasm_type (basic|restrict) - type of subdomain update used

SNES: Nonlinear Solvers, SNES, SNESNASM, SNESNASMGetType(), PCASMSetType(), PC_ASM_BASIC, PC_ASM_RESTRICT, PCASMType

src/snes/impls/nasm/nasm.c

SNESNASMSetType_NASM() in src/snes/impls/nasm/nasm.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNASMSetType(SNES snes, PCASMType type)
```

Example 2 (unknown):
```unknown
PC_ASM_BASIC
```

Example 3 (unknown):
```unknown
PC_ASM_RESTRICT
```

Example 4 (unknown):
```unknown
SNESNASMGetType()
```

---

## SNESNASMSetWeight#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNASMSetWeight/

**Contents:**
- SNESNASMSetWeight#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets weight to use when adding overlapping updates

snes - the SNES context

weight - the weights to use (typically 1/N for each dof, where N is the number of patches it appears in)

SNES: Nonlinear Solvers, SNESNASM

src/snes/impls/nasm/nasm.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNASMSetWeight(SNES snes, Vec weight)
```

---

## SNESNASM#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNASM/

**Contents:**
- SNESNASM#
- Options Database Keys#
- Note#
- Developer Note#
- References#
- See Also#
- Level#
- Location#

Nonlinear Additive Schwarz solver [CK02], [BKST15]

-snes_nasm_log - enable logging events for the communication and solve stages

-snes_nasm_type (basic|restrict) - type of subdomain update used

-snes_nasm_damping dmp - the new solution is obtained as old solution plus dmp times (sum of the solutions on the subdomains)

-snes_nasm_finaljacobian - compute the local and global Jacobians of the final iterate

-snes_nasm_finaljacobian_type (finalinner|finalouter|initial) - pick state the Jacobian is calculated at

-sub_snes_ - options prefix of the subdomain nonlinear solves

-sub_ksp_ - options prefix of the subdomain Krylov solver

-sub_pc_ - options prefix of the subdomain preconditioner

This is not often used directly as a solver, it converges too slowly. However it works well as a nonlinear preconditioner for the SNESASPIN solver

This is a non-Newton based nonlinear solver that does not directly require a Jacobian; hence the flag snes->usesksp is set to false and SNESView() and -snes_view do not display a KSP object. However, if the flag nasm->finaljacobian is set (for example, if SNESNASM is used as a nonlinear preconditioner for SNESASPIN) then SNESSetUpMatrices() is called to generate the Jacobian (needed by SNESASPIN) and this utilizes the inner KSP object for storing the matrices, but the KSP is never used for solving a linear system. When SNESNASM is used by SNESASPIN they share the same Jacobian matrices because SNESSetUp() (called on the outer SNESASPIN) causes the inner SNES object (in this case SNESNASM) to inherit the outer Jacobian matrices.

Peter R. Brune, Matthew G. Knepley, Barry F. Smith, and Xuemin Tu. Composing scalable nonlinear algebraic solvers. SIAM Review, 57(4):535–565, 2015. http://www.mcs.anl.gov/papers/P2010-0112.pdf. URL: http://www.mcs.anl.gov/papers/P2010-0112.pdf, doi:10.1137/130936725.

X.-C. Cai and D. E. Keyes. Nonlinearly preconditioned inexact Newton algorithms. SIAM J. Sci. Comput., 24:183–200, 2002. URL: http://www.cs.colorado.edu/homes/cai/public_html/papers/aspin.ps.

SNES: Nonlinear Solvers, SNESCreate(), SNES, SNESSetType(), SNESType, SNESNASMSetType(), SNESNASMGetType(), SNESNASMSetSubdomains(), SNESNASMGetSubdomains(), SNESNASMGetSubdomainVecs(), SNESNASMSetComputeFinalJacobian(), SNESNASMSetDamping(), SNESNASMGetDamping(), SNESNASMSetWeight(), SNESNASMGetSNES(), SNESNASMGetNumber()

src/snes/impls/nasm/nasm.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetUpMatrices()
```

Example 2 (unknown):
```unknown
SNESSetUp()
```

Example 3 (unknown):
```unknown
SNESCreate()
```

Example 4 (unknown):
```unknown
SNESSetType()
```

---

## SNESNCGSetType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNCGSetType/

**Contents:**
- SNESNCGSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Sets the conjugate update type for nonlinear CG SNESNCG.

snes - the iterative context

btype - update type, see SNESNCGType

-snes_ncg_type (prp|fr|hs|dy|cd) - strategy for selecting algorithm for computing beta

SNES_NCG_PRP is the default, and the only one that tolerates generalized search directions.

It is not clear what “generalized search directions” means, does it mean use with a nonlinear preconditioner, that is using -npc_snes_type , SNESSetNPC(), or SNESGetNPC()?

SNES: Nonlinear Solvers, SNES, SNESNCG, SNESNCGType, SNES_NCG_FR, SNES_NCG_PRP, SNES_NCG_HS, SNES_NCG_DY, SNES_NCG_CD

src/snes/impls/ncg/snesncg.c

SNESNCGSetType_NCG() in src/snes/impls/ncg/snesncg.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESNCGSetType(SNES snes, SNESNCGType btype)
```

Example 2 (unknown):
```unknown
SNESNCGType
```

Example 3 (unknown):
```unknown
SNES_NCG_PRP
```

Example 4 (unknown):
```unknown
SNESSetNPC()
```

---

## SNESNCGType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNCGType/

**Contents:**
- SNESNCGType#
- Values#
- Options Database Key#
- See Also#
- Level#
- Location#

the conjugate update approach for SNESNCG

SNES_NCG_FR - Fletcher-Reeves update

SNES_NCG_PRP - Polak-Ribiere-Polyak update, the default and the only one that tolerates generalized search directions

SNES_NCG_HS - Hestenes-Steifel update

SNES_NCG_DY - Dai-Yuan update

SNES_NCG_CD - Conjugate Descent update

-snes_ncg_type (fr|prp|hs|dy|cd) - select the type

SNES, SNESNCG, SNESNCGSetType()

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNES_NCG_FR
```

Example 2 (unknown):
```unknown
SNES_NCG_PRP
```

Example 3 (unknown):
```unknown
SNES_NCG_HS
```

Example 4 (unknown):
```unknown
SNES_NCG_DY
```

---

## SNESNCG#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNCG/

**Contents:**
- SNESNCG#
- Options Database Keys#
- Notes#
- References#
- See Also#
- Level#
- Location#

Nonlinear Conjugate-Gradient method for the solution of nonlinear systems [BKST15].

-snes_ncg_type (fr|prp|dy|hs|cd) - Choice of conjugate-gradient update parameter, default is prp.

-snes_linesearch_type (none|basic|bt|secant|cp|nleqerr|bisection|shell|ncglinear) - Line search type, see SNESLineSearchType

-snes_ncg_monitor - Print the beta values nonlinear Conjugate-Gradient used in the iteration, .

This solves the nonlinear system of equations \( F(x) = 0 \) using the nonlinear generalization of the conjugate gradient method. This may be used with a nonlinear preconditioner used to pick the new search directions, but otherwise chooses the initial search direction as \( F(x) \) for the initial guess \(x\).

Only supports left non-linear preconditioning.

Default line search is SNESLINESEARCHCP, unless a nonlinear preconditioner is used with -npc_snes_type , SNESSetNPC(), or SNESGetNPC() then SNESLINESEARCHSECANT is used. Also supports the special-purpose line search SNESLINESEARCHNCGLINEAR

Peter R. Brune, Matthew G. Knepley, Barry F. Smith, and Xuemin Tu. Composing scalable nonlinear algebraic solvers. SIAM Review, 57(4):535–565, 2015. http://www.mcs.anl.gov/papers/P2010-0112.pdf. URL: http://www.mcs.anl.gov/papers/P2010-0112.pdf, doi:10.1137/130936725.

SNES: Nonlinear Solvers, SNES, SNESNCG, SNESCreate(), SNESType, SNESSetType(), SNESNEWTONLS, SNESNEWTONTR, SNESNGMRES, SNESQN, SNESLINESEARCHNCGLINEAR, SNESNCGSetType(), SNESLineSearchSetType()

src/snes/impls/ncg/snesncg.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLineSearchType
```

Example 2 (unknown):
```unknown
SNESLINESEARCHCP
```

Example 3 (unknown):
```unknown
-npc_snes_type
```

Example 4 (unknown):
```unknown
SNESSetNPC()
```

---

## SNESNewtonALComputeFunction#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonALComputeFunction/

**Contents:**
- SNESNewtonALComputeFunction#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Calls the function that has been set with SNESNewtonALSetFunction().

snes - the SNES context

Q - tangent load vector, as set by SNESNewtonALSetFunction()

SNESNewtonALComputeFunction() is typically used within nonlinear solvers implementations, so users would not generally call this routine themselves.

SNES: Nonlinear Solvers, SNES, SNESNewtonALSetFunction(), SNESNewtonALGetFunction()

src/snes/impls/al/al.c

SNESNewtonALComputeFunction_NEWTONAL() in src/snes/impls/al/al.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESNewtonALSetFunction()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESNewtonALComputeFunction(SNES snes, Vec X, Vec Q)
```

Example 3 (unknown):
```unknown
SNESNewtonALSetFunction()
```

Example 4 (unknown):
```unknown
SNESNewtonALComputeFunction()
```

---

## SNESNewtonALCorrectionType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonALCorrectionType/

**Contents:**
- SNESNewtonALCorrectionType#
- Values#
- Options Database Key#
- See Also#
- Level#
- Location#

the approach used by SNESNEWTONAL to determine the correction to the current increment. While the exact correction satisfies the constraint surface at every iteration, it also requires solving a quadratic equation which may not have real roots. Conversely, the normal correction is more efficient and always yields a real correction and is the default.

SNES_NEWTONAL_CORRECTION_EXACT - choose the correction which exactly satisfies the constraint

SNES_NEWTONAL_CORRECTION_NORMAL - choose the correction in the updated normal hyper-surface to the constraint surface

-snes_newtonal_correction_type (exact|normal) - exactly satisfy the constraint or satisfy it on the normal hyper-surface

SNES, SNESNEWTONAL, SNESNewtonALSetCorrectionType()

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESNEWTONAL
```

Example 2 (unknown):
```unknown
SNES_NEWTONAL_CORRECTION_EXACT
```

Example 3 (unknown):
```unknown
SNES_NEWTONAL_CORRECTION_NORMAL
```

Example 4 (unknown):
```unknown
SNESNEWTONAL
```

---

## SNESNewtonALGetFunction#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonALGetFunction/

**Contents:**
- SNESNewtonALGetFunction#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Get the user function and context set with SNESNewtonALSetFunction

snes - the nonlinear solver object

func - [optional] tangent load function evaluation routine, see SNESNewtonALSetFunction() for the call sequence

ctx - [optional] user-defined context for private data for the function evaluation routine (may be NULL)

SNES: Nonlinear Solvers, SNES, SNESNEWTONAL, SNESNewtonALSetFunction()

src/snes/impls/al/al.c

SNESNewtonALGetFunction_NEWTONAL() in src/snes/impls/al/al.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESNewtonALSetFunction
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESNewtonALGetFunction(SNES snes, SNESFunctionFn **func, PetscCtxRt ctx)
```

Example 3 (unknown):
```unknown
SNESNewtonALSetFunction()
```

Example 4 (unknown):
```unknown
SNESNEWTONAL
```

---

## SNESNewtonALGetLoadParameter#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonALGetLoadParameter/

**Contents:**
- SNESNewtonALGetLoadParameter#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Get the value of the load parameter lambda for the arc-length continuation method.

snes - the nonlinear solver object

lambda - the arc-length parameter

This function should be used in the functions provided to SNESSetFunction() and SNESNewtonALSetFunction() to compute the residual and tangent load vectors for a given value of lambda (0 <= lambda <= 1).

Usually, lambda is used to scale the external force vector in the residual function, i.e. proportional loading, in which case the tangent load vector is the full external force vector.

SNES: Nonlinear Solvers, SNES, SNESNEWTONAL, SNESNewtonALSetFunction()

src/snes/impls/al/al.c

src/snes/tutorials/ex16.c

SNESNewtonALGetLoadParameter_NEWTONAL() in src/snes/impls/al/al.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESNewtonALGetLoadParameter(SNES snes, PetscReal *lambda)
```

Example 2 (unknown):
```unknown
SNESSetFunction()
```

Example 3 (unknown):
```unknown
SNESNewtonALSetFunction()
```

Example 4 (unknown):
```unknown
SNESNEWTONAL
```

---

## SNESNewtonALSetCorrectionType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonALSetCorrectionType/

**Contents:**
- SNESNewtonALSetCorrectionType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

Set the type of correction to use in the arc-length continuation method.

snes - the nonlinear solver object

ctype - the type of correction to use

-snes_newtonal_correction_type type - Set the type of correction to use; use -help for a list of available types

SNES: Nonlinear Solvers, SNES, SNESNEWTONAL, SNESNewtonALCorrectionType

src/snes/impls/al/al.c

SNESNewtonALSetCorrectionType_NEWTONAL() in src/snes/impls/al/al.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESNewtonALSetCorrectionType(SNES snes, SNESNewtonALCorrectionType ctype)
```

Example 2 (unknown):
```unknown
SNESNEWTONAL
```

Example 3 (unknown):
```unknown
SNESNewtonALCorrectionType
```

---

## SNESNewtonALSetDiagonalScaling#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonALSetDiagonalScaling/

**Contents:**
- SNESNewtonALSetDiagonalScaling#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Set the global vector used to rescale DoFs for computation of arc length.

snes - the nonlinear solver object

v - the Vec containing diagonal scaling for each DoF, must be the same size as the solution vector (may be NULL)

This function stores a reference to v. Any changes to the vector will be reflected automatically in the arc length computation.

SNES: Nonlinear Solvers, SNES, SNESNEWTONAL, SNESNewtonALSetFunction(), SNESNewtonALGetLoadParameter()

src/snes/impls/al/al.c

src/snes/tutorials/ex16.c

SNESNewtonALSetDiagonalScaling_NEWTONAL() in src/snes/impls/al/al.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESNewtonALSetDiagonalScaling(SNES snes, Vec v)
```

Example 2 (unknown):
```unknown
SNESNEWTONAL
```

Example 3 (unknown):
```unknown
SNESNewtonALSetFunction()
```

Example 4 (unknown):
```unknown
SNESNewtonALGetLoadParameter()
```

---

## SNESNewtonALSetFunction#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonALSetFunction/

**Contents:**
- SNESNewtonALSetFunction#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets a user function that is called at each function evaluation to compute the tangent load vector for the arc-length continuation method.

snes - the nonlinear solver object

func - [optional] tangent load function evaluation routine, see SNESFunctionFn for the calling sequence. U is the current solution vector, Q is the output tangent load vector

ctx - [optional] user-defined context for private data for the function evaluation routine (may be NULL)

If the current value of the load parameter is needed in func, it can be obtained with SNESNewtonALGetLoadParameter().

The tangent load vector is the partial derivative of external load with respect to the load parameter. In the case of proportional loading, the tangent load vector is the full external load vector at the end of the load step.

SNES: Nonlinear Solvers, SNES, SNESNEWTONAL, SNESNewtonALGetFunction(), SNESNewtonALGetLoadParameter()

src/snes/impls/al/al.c

src/snes/tutorials/ex16.c

SNESNewtonALSetFunction_NEWTONAL() in src/snes/impls/al/al.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESNewtonALSetFunction(SNES snes, SNESFunctionFn *func, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESFunctionFn
```

Example 3 (unknown):
```unknown
SNESNewtonALGetLoadParameter()
```

Example 4 (unknown):
```unknown
SNESNEWTONAL
```

---

## SNESNEWTONAL#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNEWTONAL/

**Contents:**
- SNESNEWTONAL#
- Options Database Keys#
- Note#
- References#
- See Also#
- Level#
- Location#
- Examples#

Newton based nonlinear solver that uses a arc-length continuation method to solve the nonlinear system.

-snes_newtonal_step_size step - Initial arc length increment step size

-snes_newtonal_max_continuation_steps max - Maximum number of continuation steps, or negative for no limit (not recommended)

-snes_newtonal_psisq psisq - Regularization parameter for arc length continuation, 0 for cylindrical. Larger values generally lead to more steps.

-snes_newtonal_lambda_min lambda_min - Minimum value of the load parameter lambda

-snes_newtonal_lambda_max lambda_max - Maximum value of the load parameter lambda

-snes_newtonal_scale_rhs (true|false) - Scale the constant vector passed to SNESSolve by the load parameter lambda

-snes_newtonal_correction_type (exact|normal) - Type of correction to use in the arc-length continuation method

The exact correction scheme with partial updates is detailed in [RCorreaC08] and the implementation of the normal correction scheme is based on [LPP+11].

Sofie E. Leon, Glaucio H. Paulino, Anderson Pereira, Ivan F. M. Menezes, and Eduardo N. Lages. A unified library of nonlinear solution schemes. Applied Mechanics Reviews, 64(4):040803, July 2011. doi:10.1115/1.4006992.

Manuel Ritto-Corrêa and Dinar Camotim. On the arc-length and other quadratic control methods: established, less known and new implementation procedures. Computers & Structures, 86(11):1353–1368, June 2008. doi:10.1016/j.compstruc.2007.08.003.

SNES: Nonlinear Solvers, SNESCreate(), SNES, SNESSetType(), SNESNEWTONAL, SNESNewtonALSetFunction(), SNESNewtonALGetFunction(), SNESNewtonALGetLoadParameter()

src/snes/impls/al/al.c

src/snes/tutorials/ex16.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESCreate()
```

Example 2 (unknown):
```unknown
SNESSetType()
```

Example 3 (unknown):
```unknown
SNESNEWTONAL
```

Example 4 (unknown):
```unknown
SNESNewtonALSetFunction()
```

---

## SNESNEWTONLS#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNEWTONLS/

**Contents:**
- SNESNEWTONLS#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Newton based nonlinear solver that uses a line search

-snes_linesearch_type (none|basic|bt|secant|cp|nleqerr|bisection|shell) - Line search type, see SNESLineSearchType

-snes_linesearch_order 3 - 2, 3. Selects the order of the line search for bt, see SNESLineSearchSetOrder()

-snes_linesearch_norms true - Turns on/off computation of the norms for basic linesearch (SNESLineSearchSetComputeNorms())

-snes_linesearch_alpha alpha - Sets alpha used in determining if reduction in function norm is sufficient

-snes_linesearch_maxstep maxstep - Sets the maximum stepsize the line search will use (if the \( ||y|| > maxstep \) then scale y to be \(y = y * maxstep/||y||.\)

-snes_linesearch_minlambda minlambda - Sets the minimum lambda the line search will tolerate

-snes_linesearch_monitor - print information about the progress of line searches

-snes_linesearch_damping - damping factor used for the basic line search

This is the default nonlinear solver in SNES

SNES: Nonlinear Solvers, SNESCreate(), SNES, SNESSetType(), SNESNEWTONTR, SNESQN, SNESLineSearchSetType(), SNESLineSearchSetOrder(), SNESLineSearchSetPostCheck(), SNESLineSearchSetPreCheck(), SNESLineSearchSetComputeNorms(), SNESGetLineSearch()

src/snes/impls/ls/ls.c

src/snes/tutorials/ex1.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLineSearchType
```

Example 2 (unknown):
```unknown
SNESLineSearchSetOrder()
```

Example 3 (unknown):
```unknown
SNESLineSearchSetComputeNorms()
```

Example 4 (unknown):
```unknown
SNESCreate()
```

---

## SNESNewtonTRDCGetPostCheck#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonTRDCGetPostCheck/

**Contents:**
- SNESNewtonTRDCGetPostCheck#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#

Gets the post-check function optionally set with SNESNewtonTRDCSetPostCheck()

snes - the nonlinear solver context

func - [optional] function evaluation routine, for the calling sequence see SNESNewtonTRDCPostCheck()

ctx - [optional] context for private data for the function evaluation routine (may be NULL)

snes - the nonlinear solver object

X - the current solution value

Y - the tentative update step

W - the tentative new solution value

changed_y - output, flag indicated Y has been changed by the post-check

changed_w - output, flag indicated W has been changed by the post-check

ctx - the optional application context

SNES: Nonlinear Solvers, SNES, SNESNEWTONTRDC, SNESNewtonTRDCSetPostCheck(), SNESNewtonTRDCPostCheck(), SNESNewtonTRDCSetPreCheck(), SNESNewtonTRDCGetPreCheck()

src/snes/impls/ntrdc/ntrdc.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESNewtonTRDCSetPostCheck()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNewtonTRDCGetPostCheck(SNES snes, PetscErrorCode (**func)(SNES snes, Vec X, Vec Y, Vec W, PetscBool *changed_y, PetscBool *changed_w, PetscCtx ctx), PetscCtxRt ctx)
```

Example 3 (unknown):
```unknown
SNESNewtonTRDCPostCheck()
```

Example 4 (unknown):
```unknown
SNESNEWTONTRDC
```

---

## SNESNewtonTRDCGetPreCheck#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonTRDCGetPreCheck/

**Contents:**
- SNESNewtonTRDCGetPreCheck#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#

Gets the pre-check function optionally set with SNESNewtonTRDCSetPreCheck()

snes - the nonlinear solver context

func - [optional] function evaluation routine, for the calling sequence see SNESNewtonTRDCPreCheck()

ctx - [optional] context for private data for the function evaluation routine (may be NULL)

snes - the nonlinear solver object

X - the current solution value

Y - the tentative update step

changed - output, flag indicating Y has been changed by the pre-check

ctx - the optional application context

SNES: Nonlinear Solvers, SNES, SNESNEWTONTRDC, SNESNewtonTRDCSetPreCheck(), SNESNewtonTRDCPreCheck()

src/snes/impls/ntrdc/ntrdc.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESNewtonTRDCSetPreCheck()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNewtonTRDCGetPreCheck(SNES snes, PetscErrorCode (**func)(SNES snes, Vec X, Vec Y, PetscBool *changed, PetscCtx ctx), PetscCtxRt ctx)
```

Example 3 (unknown):
```unknown
SNESNewtonTRDCPreCheck()
```

Example 4 (unknown):
```unknown
SNESNEWTONTRDC
```

---

## SNESNewtonTRDCGetRhoFlag#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonTRDCGetRhoFlag/

**Contents:**
- SNESNewtonTRDCGetRhoFlag#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get whether the current solution update is within the trust-region.

snes - the nonlinear solver object

rho_flag - PETSC_FALSE or PETSC_TRUE

SNES: Nonlinear Solvers, SNES, SNESNEWTONTRDC, SNESNewtonTRDCPreCheck(), SNESNewtonTRDCGetPreCheck(), SNESNewtonTRDCSetPreCheck(), SNESNewtonTRDCSetPostCheck(), SNESNewtonTRDCGetPostCheck()

src/snes/impls/ntrdc/ntrdc.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNewtonTRDCGetRhoFlag(SNES snes, PetscBool *rho_flag)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
SNESNEWTONTRDC
```

Example 4 (unknown):
```unknown
SNESNewtonTRDCPreCheck()
```

---

## SNESNewtonTRDCPostCheck#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonTRDCPostCheck/

**Contents:**
- SNESNewtonTRDCPostCheck#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Called after the step has been determined in SNESNEWTONTRDC but before the function evaluation at that step

X - The last solution

Y - The full step direction

W - The updated solution, \(W = X - Y\)

changed_Y - indicator if the step Y has been changed

changed_W - Indicator if the new candidate solution W has been changed.

If Y is changed then W is recomputed as X - Y

SNES: Nonlinear Solvers, SNES, SNESNEWTONTRDC, SNESNEWTONTRDC, SNESNewtonTRDCSetPostCheck(), SNESNewtonTRDCGetPostCheck(), `SNESNewtonTRDCPreCheck()

src/snes/impls/ntrdc/ntrdc.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESNEWTONTRDC
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"   
static PetscErrorCode SNESNewtonTRDCPostCheck(SNES snes, Vec X, Vec Y, Vec W, PetscBool *changed_Y, PetscBool *changed_W)
```

Example 3 (unknown):
```unknown
SNESNEWTONTRDC
```

Example 4 (unknown):
```unknown
SNESNEWTONTRDC
```

---

## SNESNewtonTRDCPreCheck#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonTRDCPreCheck/

**Contents:**
- SNESNewtonTRDCPreCheck#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Called before the step has been determined in SNESNEWTONTRDC

X - The last solution

Y - The step direction

changed_y - Indicator that the step direction Y has been changed.

SNES: Nonlinear Solvers, SNES, SNESNEWTONTRDC, SNESNewtonTRDCSetPreCheck(), SNESNewtonTRDCGetPreCheck(), SNESNewtonTRDCPostCheck()

src/snes/impls/ntrdc/ntrdc.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESNEWTONTRDC
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"   
static PetscErrorCode SNESNewtonTRDCPreCheck(SNES snes, Vec X, Vec Y, PetscBool *changed_Y)
```

Example 3 (unknown):
```unknown
SNESNEWTONTRDC
```

Example 4 (unknown):
```unknown
SNESNewtonTRDCSetPreCheck()
```

---

## SNESNewtonTRDCSetPostCheck#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonTRDCSetPostCheck/

**Contents:**
- SNESNewtonTRDCSetPostCheck#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Note#
- See Also#
- Level#
- Location#

Sets a user function that is called after the search step has been determined but before the next function evaluation. Allows the user a chance to change or override the decision of the line search routine

snes - the nonlinear solver object

func - [optional] function evaluation routine, for the calling sequence see SNESNewtonTRDCPostCheck()

ctx - [optional] context for private data for the function evaluation routine (may be NULL)

snes - the nonlinear solver object

X - the current solution value

Y - the tentative update step

W - the tentative new solution value

changed_y - output, flag indicated Y has been changed by the post-check

changed_w - output, flag indicated W has been changed by the post-check

ctx - the optional application context

This function is called BEFORE the function evaluation within the SNESNEWTONTRDC solver while the function set in SNESLineSearchSetPostCheck() is called AFTER the function evaluation.

SNES: Nonlinear Solvers, SNES, SNESNEWTONTRDC, SNESNewtonTRDCPostCheck(), SNESNewtonTRDCGetPostCheck(), SNESNewtonTRDCSetPreCheck(), SNESNewtonTRDCGetPreCheck()

src/snes/impls/ntrdc/ntrdc.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNewtonTRDCSetPostCheck(SNES snes, PetscErrorCode (*func)(SNES snes, Vec X, Vec Y, Vec W, PetscBool *changed_y, PetscBool *changed_w, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESNewtonTRDCPostCheck()
```

Example 3 (unknown):
```unknown
SNESNEWTONTRDC
```

Example 4 (unknown):
```unknown
SNESLineSearchSetPostCheck()
```

---

## SNESNewtonTRDCSetPreCheck#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonTRDCSetPreCheck/

**Contents:**
- SNESNewtonTRDCSetPreCheck#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Note#
- See Also#
- Level#
- Location#

Sets a user function that is called before the search step has been determined. Allows the user a chance to change or override the trust region decision.

snes - the nonlinear solver object

func - [optional] function evaluation routine, for the calling sequence see SNESNewtonTRDCPreCheck()

ctx - [optional] application context for private data for the function evaluation routine (may be NULL)

snes - the nonlinear solver object

X - the current solution value

Y - the tentative update step

changed - output, flag indicating Y has been changed by the pre-check

ctx - the optional application context

This function is called BEFORE the function evaluation within the SNESNEWTONTRDC solver.

SNES: Nonlinear Solvers, SNES, SNESNEWTONTRDC, SNESNewtonTRDCPreCheck(), SNESNewtonTRDCGetPreCheck(), SNESNewtonTRDCSetPostCheck(), SNESNewtonTRDCGetPostCheck(), SNESNewtonTRDCGetRhoFlag()

src/snes/impls/ntrdc/ntrdc.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNewtonTRDCSetPreCheck(SNES snes, PetscErrorCode (*func)(SNES snes, Vec X, Vec Y, PetscBool *changed, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESNewtonTRDCPreCheck()
```

Example 3 (unknown):
```unknown
SNESNEWTONTRDC
```

Example 4 (unknown):
```unknown
SNESNEWTONTRDC
```

---

## SNESNEWTONTRDC#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNEWTONTRDC/

**Contents:**
- SNESNEWTONTRDC#
- Options Database Keys#
- Notes#
- References#
- See Also#
- Level#
- Location#

Newton based nonlinear solver that uses trust-region dogleg method with Cauchy direction

-snes_trdc_tol tol - trust region tolerance

-snes_trdc_eta1 eta1 - trust region parameter 0.0 <= eta1 <= eta2, rho >= eta1 breaks out of the inner iteration (default: eta1=0.001)

-snes_trdc_eta2 eta2 - trust region parameter 0.0 <= eta1 <= eta2, rho <= eta2 shrinks the trust region (default: eta2=0.25)

-snes_trdc_eta3 eta3 - trust region parameter eta3 > eta2, rho >= eta3 expands the trust region (default: eta3=0.75)

-snes_trdc_t1 t1 - trust region parameter, shrinking factor of trust region (default: 0.25)

-snes_trdc_t2 t2 - trust region parameter, expanding factor of trust region (default: 2.0)

-snes_trdc_deltaM deltaM - trust region parameter, max size of trust region, \(deltaM*norm2(x)\) (default: 0.5)

-snes_trdc_delta0 delta0 - trust region parameter, initial size of trust region, \(delta0*norm2(x)\) (default: 0.1)

-snes_trdc_auto_scale_max auto_scale_max - used with auto_scale_multiphase, caps the maximum auto-scaling factor

-snes_trdc_use_cauchy use_cauchy - True uses dogleg Cauchy (Steepest Descent direction) step & direction in the trust region algorithm

-snes_trdc_auto_scale_multiphase auto_scale_multiphase - True turns on auto-scaling for multivariable block matrix for Cauchy and trust region

SNESNEWTONTRDC only works for root-finding problems and does not support objective functions. The main difference with respect to SNESNEWTONTR is that SNESNEWTONTRDC scales the trust region by the norm of the current linearization point. Future version may extend the SNESNEWTONTR code and deprecate SNESNEWTONTRDC.

For details, see [PHVL21]

Heeho D Park, Glenn E Hammond, Albert J Valocchi, and Tara LaForce. Linear and nonlinear solvers for simulating multiphase flow within large-scale engineered subsurface systems. Advances in Water Resources, 156:104029, 2021.

SNES: Nonlinear Solvers, SNESCreate(), SNES, SNESSetType(), SNESNEWTONLS, SNESNewtonTRSetTolerances(), SNESNewtonTRDCPreCheck(), SNESNewtonTRDCGetPreCheck(), SNESNewtonTRDCSetPostCheck(), SNESNewtonTRDCGetPostCheck(), SNESNewtonTRDCGetRhoFlag(), SNESNewtonTRDCSetPreCheck()

src/snes/impls/ntrdc/ntrdc.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESNEWTONTRDC
```

Example 2 (unknown):
```unknown
SNESNEWTONTR
```

Example 3 (unknown):
```unknown
SNESNEWTONTRDC
```

Example 4 (unknown):
```unknown
SNESNEWTONTR
```

---

## SNESNewtonTRFallbackType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonTRFallbackType/

**Contents:**
- SNESNewtonTRFallbackType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

type of fallback in case the solution of the trust-region subproblem is outside of the radius

SNES_TR_FALLBACK_NEWTON - use scaled Newton step

SNES_TR_FALLBACK_CAUCHY - use Cauchy direction

SNES_TR_FALLBACK_DOGLEG - use dogleg method

SNES: Nonlinear Solvers, SNES, SNESNEWTONTR, SNESNEWTONTRDC

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  SNES_TR_FALLBACK_NEWTON,
  SNES_TR_FALLBACK_CAUCHY,
  SNES_TR_FALLBACK_DOGLEG,
} SNESNewtonTRFallbackType;
```

Example 2 (unknown):
```unknown
SNES_TR_FALLBACK_NEWTON
```

Example 3 (unknown):
```unknown
SNES_TR_FALLBACK_CAUCHY
```

Example 4 (unknown):
```unknown
SNES_TR_FALLBACK_DOGLEG
```

---

## SNESNewtonTRGetPostCheck#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonTRGetPostCheck/

**Contents:**
- SNESNewtonTRGetPostCheck#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#

Gets the post-check function

snes - the nonlinear solver context

func - [optional] function evaluation routine, for the calling sequence see SNESNewtonTRPostCheck()

ctx - [optional] user-defined context for private data for the function evaluation routine (may be NULL)

snes - the nonlinear solver object

X - the current solution value

Y - the tentative update step

W - the tentative new solution value

changed_Y - output, flag indicated Y has been changed by the post-check

changed_W - output, flag indicated W has been changed by the post-check

ctx - the optional application context

SNES: Nonlinear Solvers, SNESNEWTONTR, SNESNewtonTRSetPostCheck(), SNESNewtonTRPostCheck()

src/snes/impls/tr/tr.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNewtonTRGetPostCheck(SNES snes, PetscErrorCode (**func)(SNES snes, Vec X, Vec Y, Vec W, PetscBool *changed_Y, PetscBool *changed_W, PetscCtx ctx), PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
SNESNewtonTRPostCheck()
```

Example 3 (unknown):
```unknown
SNESNEWTONTR
```

Example 4 (unknown):
```unknown
SNESNewtonTRSetPostCheck()
```

---

## SNESNewtonTRGetPreCheck#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonTRGetPreCheck/

**Contents:**
- SNESNewtonTRGetPreCheck#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#

Gets the pre-check function

snes - the nonlinear solver context

func - [optional] function evaluation routine, for the calling sequence see SNESNewtonTRPreCheck()

ctx - [optional] user-defined context for private data for the function evaluation routine (may be NULL)

snes - the nonlinear solver object

X - the current solution value

Y - the tentative update step

changed - output, flag indicating Y has been changed by the pre-check

ctx - the optional application context

SNES: Nonlinear Solvers, SNESNEWTONTR, SNESNewtonTRSetPreCheck(), SNESNewtonTRPreCheck()

src/snes/impls/tr/tr.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNewtonTRGetPreCheck(SNES snes, PetscErrorCode (**func)(SNES snes, Vec X, Vec Y, PetscBool *changed, PetscCtx ctx), PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
SNESNewtonTRPreCheck()
```

Example 3 (unknown):
```unknown
SNESNEWTONTR
```

Example 4 (unknown):
```unknown
SNESNewtonTRSetPreCheck()
```

---

## SNESNewtonTRGetTolerances#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonTRGetTolerances/

**Contents:**
- SNESNewtonTRGetTolerances#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Gets the trust region parameter tolerances.

snes - the SNES context

delta_min - minimum allowed trust region size or NULL

delta_max - maximum allowed trust region size or NULL

delta_0 - initial trust region size or NULL

SNES: Nonlinear Solvers, SNES, SNESNEWTONTR, SNESNewtonTRSetTolerances()

src/snes/impls/tr/tr.c

SNESNewtonTRGetTolerances_TR() in src/snes/impls/tr/tr.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNewtonTRGetTolerances(SNES snes, PetscReal *delta_min, PetscReal *delta_max, PetscReal *delta_0)
```

Example 2 (unknown):
```unknown
SNESNEWTONTR
```

Example 3 (unknown):
```unknown
SNESNewtonTRSetTolerances()
```

---

## SNESNewtonTRGetUpdateParameters#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonTRGetUpdateParameters/

**Contents:**
- SNESNewtonTRGetUpdateParameters#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Gets the trust region update parameters.

snes - the SNES context

eta1 - acceptance tolerance

eta2 - shrinking tolerance

eta3 - enlarging tolerance

SNES: Nonlinear Solvers, SNES, SNESNEWTONTR, SNESNewtonTRSetUpdateParameters()

src/snes/impls/tr/tr.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNewtonTRGetUpdateParameters(SNES snes, PetscReal *eta1, PetscReal *eta2, PetscReal *eta3, PetscReal *t1, PetscReal *t2)
```

Example 2 (unknown):
```unknown
SNESNEWTONTR
```

Example 3 (unknown):
```unknown
SNESNewtonTRSetUpdateParameters()
```

---

## SNESNewtonTRPostCheck#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonTRPostCheck/

**Contents:**
- SNESNewtonTRPostCheck#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Runs the postcheck routine

X - The last solution

Y - The full step direction

W - The updated solution, W = X - Y

changed_Y - indicator if step has been changed

changed_W - Indicator if the new candidate solution W has been changed.

If Y is changed then W is recomputed as X - Y

SNES: Nonlinear Solvers, SNESNEWTONTR, SNESNewtonTRSetPostCheck(), SNESNewtonTRGetPostCheck(), SNESNewtonTRPreCheck()

src/snes/impls/tr/tr.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNewtonTRPostCheck(SNES snes, Vec X, Vec Y, Vec W, PetscBool *changed_Y, PetscBool *changed_W)
```

Example 2 (unknown):
```unknown
SNESNEWTONTR
```

Example 3 (unknown):
```unknown
SNESNewtonTRSetPostCheck()
```

Example 4 (unknown):
```unknown
SNESNewtonTRGetPostCheck()
```

---

## SNESNewtonTRPreCheck#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonTRPreCheck/

**Contents:**
- SNESNewtonTRPreCheck#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Runs the precheck routine

X - The last solution

Y - The step direction

changed_Y - Indicator that the step direction Y has been changed.

SNES: Nonlinear Solvers, SNESNEWTONTR, SNESNewtonTRSetPreCheck(), SNESNewtonTRGetPreCheck(), SNESNewtonTRPostCheck()

src/snes/impls/tr/tr.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNewtonTRPreCheck(SNES snes, Vec X, Vec Y, PetscBool *changed_Y)
```

Example 2 (unknown):
```unknown
SNESNEWTONTR
```

Example 3 (unknown):
```unknown
SNESNewtonTRSetPreCheck()
```

Example 4 (unknown):
```unknown
SNESNewtonTRGetPreCheck()
```

---

## SNESNewtonTRQNType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonTRQNType/

**Contents:**
- SNESNewtonTRQNType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

type of quasi-Newton model to use

SNES_TR_QN_NONE - do not use a quasi-Newton model

SNES_TR_QN_SAME - use the same quasi-Newton model for matrix and the generation of the preconditioner

SNES_TR_QN_DIFFERENT - use different quasi-Newton models for matrix and the generation of the preconditioner

SNES: Nonlinear Solvers, SNES, SNESNEWTONTR

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  SNES_TR_QN_NONE,
  SNES_TR_QN_SAME,
  SNES_TR_QN_DIFFERENT,
} SNESNewtonTRQNType;
```

Example 2 (unknown):
```unknown
SNES_TR_QN_NONE
```

Example 3 (unknown):
```unknown
SNES_TR_QN_SAME
```

Example 4 (unknown):
```unknown
SNES_TR_QN_DIFFERENT
```

---

## SNESNewtonTRSetFallbackType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonTRSetFallbackType/

**Contents:**
- SNESNewtonTRSetFallbackType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the type of fallback to use if the solution of the trust region subproblem is outside the radius

snes - the nonlinear solver object

ftype - the fallback type, see SNESNewtonTRFallbackType

SNES: Nonlinear Solvers, SNESNEWTONTR, SNESNewtonTRPreCheck(), SNESNewtonTRGetPreCheck(), SNESNewtonTRSetPreCheck(), SNESNewtonTRSetPostCheck(), SNESNewtonTRGetPostCheck()

src/snes/impls/tr/tr.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNewtonTRSetFallbackType(SNES snes, SNESNewtonTRFallbackType ftype)
```

Example 2 (unknown):
```unknown
SNESNewtonTRFallbackType
```

Example 3 (unknown):
```unknown
SNESNEWTONTR
```

Example 4 (unknown):
```unknown
SNESNewtonTRPreCheck()
```

---

## SNESNewtonTRSetNormType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonTRSetNormType/

**Contents:**
- SNESNewtonTRSetNormType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Specify the type of norm to use for the computation of the trust region.

snes - the nonlinear solver object

SNESNEWTONTR, NormType

src/snes/impls/tr/tr.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNewtonTRSetNormType(SNES snes, NormType norm)
```

Example 2 (unknown):
```unknown
SNESNEWTONTR
```

---

## SNESNewtonTRSetPostCheck#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonTRSetPostCheck/

**Contents:**
- SNESNewtonTRSetPostCheck#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Note#
- See Also#
- Level#
- Location#

Sets a user function that is called after the search step has been determined but before the next function evaluation. Allows the user a chance to change or override the internal decision of the solver

snes - the nonlinear solver object

func - [optional] function evaluation routine, for the calling sequence see SNESNewtonTRPostCheck()

ctx - [optional] user-defined context for private data for the function evaluation routine (may be NULL)

snes - the nonlinear solver object

X - the current solution value

Y - the tentative update step

W - the tentative new solution value

changed_Y - output, flag indicated Y has been changed by the post-check

changed_W - output, flag indicated W has been changed by the post-check

ctx - the optional application context

This function is called BEFORE the function evaluation within the solver while the function set in SNESLineSearchSetPostCheck() is called AFTER the function evaluation.

SNES: Nonlinear Solvers, SNESNEWTONTR, SNESNewtonTRPostCheck(), SNESNewtonTRGetPostCheck(), SNESNewtonTRSetPreCheck(), SNESNewtonTRGetPreCheck()

src/snes/impls/tr/tr.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNewtonTRSetPostCheck(SNES snes, PetscErrorCode (*func)(SNES snes, Vec X, Vec Y, Vec W, PetscBool *changed_Y, PetscBool *changed_W, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESNewtonTRPostCheck()
```

Example 3 (unknown):
```unknown
SNESLineSearchSetPostCheck()
```

Example 4 (unknown):
```unknown
SNESNEWTONTR
```

---

## SNESNewtonTRSetPreCheck#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonTRSetPreCheck/

**Contents:**
- SNESNewtonTRSetPreCheck#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Note#
- See Also#
- Level#
- Location#

Sets a user function that is called before the search step has been determined. Allows the user a chance to change or override the trust region decision.

snes - the nonlinear solver object

func - [optional] function evaluation routine, for the calling sequence see SNESNewtonTRPreCheck()

ctx - [optional] user-defined context for private data for the function evaluation routine (may be NULL)

snes - the nonlinear solver object

X - the current solution value

Y - the tentative update step

changed - output, flag indicating Y has been changed by the pre-check

ctx - the optional application context

This function is called BEFORE the function evaluation within the solver.

SNES: Nonlinear Solvers, SNESNEWTONTR, SNESNewtonTRPreCheck(), SNESNewtonTRGetPreCheck(), SNESNewtonTRSetPostCheck(), SNESNewtonTRGetPostCheck()

src/snes/impls/tr/tr.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNewtonTRSetPreCheck(SNES snes, PetscErrorCode (*func)(SNES snes, Vec X, Vec Y, PetscBool *changed, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESNewtonTRPreCheck()
```

Example 3 (unknown):
```unknown
SNESNEWTONTR
```

Example 4 (unknown):
```unknown
SNESNewtonTRPreCheck()
```

---

## SNESNewtonTRSetQNType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonTRSetQNType/

**Contents:**
- SNESNewtonTRSetQNType#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Specify to use a quasi-Newton model.

snes - the nonlinear solver object

use - the type of approximations to be used

Options for the approximations can be set with the snes_tr_qn_ and snes_tr_qn_pre_ prefixes.

SNESNEWTONTR, SNESNewtonTRQNType, MATLMVM

src/snes/impls/tr/tr.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNewtonTRSetQNType(SNES snes, SNESNewtonTRQNType use)
```

Example 2 (unknown):
```unknown
snes_tr_qn_
```

Example 3 (unknown):
```unknown
snes_tr_qn_pre_
```

Example 4 (unknown):
```unknown
SNESNEWTONTR
```

---

## SNESNewtonTRSetTolerances#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonTRSetTolerances/

**Contents:**
- SNESNewtonTRSetTolerances#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- Fortran Note#
- See Also#
- Level#
- Location#
- Implementations#

Sets the trust region parameter tolerances.

snes - the SNES context

delta_min - minimum allowed trust region size

delta_max - maximum allowed trust region size

delta_0 - initial trust region size

-snes_tr_deltamin tol - Set minimum size

-snes_tr_deltamax tol - Set maximum size

-snes_tr_delta0 tol - Set initial size

Use PETSC_DETERMINE to use the default value for the given SNES. Use PETSC_CURRENT to retain a value.

Use PETSC_DETERMINE_REAL, PETSC_CURRENT_REAL

SNES: Nonlinear Solvers, SNES, SNESNEWTONTR, SNESNewtonTRGetTolerances()

src/snes/impls/tr/tr.c

SNESNewtonTRSetTolerances_TRDC() in src/snes/impls/ntrdc/ntrdc.c SNESNewtonTRSetTolerances_TR() in src/snes/impls/tr/tr.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNewtonTRSetTolerances(SNES snes, PetscReal delta_min, PetscReal delta_max, PetscReal delta_0)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
PETSC_CURRENT
```

Example 4 (unknown):
```unknown
PETSC_DETERMINE_REAL
```

---

## SNESNewtonTRSetUpdateParameters#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNewtonTRSetUpdateParameters/

**Contents:**
- SNESNewtonTRSetUpdateParameters#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- Fortran Note#
- See Also#
- Level#
- Location#

Sets the trust region update parameters.

snes - the SNES context

eta1 - acceptance tolerance

eta2 - shrinking tolerance

eta3 - enlarging tolerance

-snes_tr_eta1 tol - Set eta1

-snes_tr_eta2 tol - Set eta2

-snes_tr_eta3 tol - Set eta3

-snes_tr_t1 tol - Set t1

-snes_tr_t2 tol - Set t2

Given the ratio \(\rho = \frac{f(x_k) - f(x_k+s_k)}{m(0) - m(s_k)}\), with \(x_k\) the current iterate, \(s_k\) the computed step, \(f\) the objective function, and \(m\) the quadratic model, the trust region radius is modified as follows

\( \delta = \begin{cases} \delta * t_1 ,& \rho < \eta_2 \\ \delta * t_2 ,& \rho > \eta_3 \\ \end{cases} \)

The step is accepted if \(\rho > \eta_1\). Use PETSC_DETERMINE to use the default value for the given SNES. Use PETSC_CURRENT to retain a value.

Use PETSC_DETERMINE_REAL, PETSC_CURRENT_REAL

SNES: Nonlinear Solvers, SNES, SNESNEWTONTR, SNESSetObjective(), SNESNewtonTRGetUpdateParameters()

src/snes/impls/tr/tr.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESNewtonTRSetUpdateParameters(SNES snes, PetscReal eta1, PetscReal eta2, PetscReal eta3, PetscReal t1, PetscReal t2)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
PETSC_CURRENT
```

Example 4 (unknown):
```unknown
PETSC_DETERMINE_REAL
```

---

## SNESNEWTONTR#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNEWTONTR/

**Contents:**
- SNESNEWTONTR#
- Options Database Keys#
- Notes#
- References#
- See Also#
- Level#
- Location#

Newton based nonlinear solver that uses a trust-region strategy

-snes_tr_deltamin deltamin - trust region parameter, minimum size of trust region

-snes_tr_deltamax deltamax - trust region parameter, max size of trust region (default: 1e10)

-snes_tr_delta0 delta0 - trust region parameter, initial size of trust region (default: 0.2)

-snes_tr_eta1 eta1 - trust region parameter \(eta1 \le eta2\), \(rho > eta1\) breaks out of the inner iteration (default: 0.001)

-snes_tr_eta2 eta2 - trust region parameter, \(rho \le eta2\) shrinks the trust region (default: 0.25)

-snes_tr_eta3 eta3 - trust region parameter \(eta3 > eta2\), \(rho \ge eta3\) expands the trust region (default: 0.75)

-snes_tr_t1 t1 - trust region parameter, shrinking factor of trust region (default: 0.25)

-snes_tr_t2 t2 - trust region parameter, expanding factor of trust region (default: 2.0)

-snes_tr_norm_type (1|2|infinity) - Type of norm for trust region bounds (default: 2)

-snes_tr_fallback_type (newton,cauchy,dogleg) - Solution strategy to test reduction when step is outside of trust region. Can use scaled Newton direction, Cauchy point (Steepest Descent direction) or dogleg method.

The code is largely based on the book [NW06] and supports minimizing objective functions using a quadratic model. Quasi-Newton models are also supported.

Default step computation uses the Newton direction, but a dogleg type update is also supported. The 1- and infinity-norms are also supported, via SNESNewtonTRSetNormType(), when computing the trust region bounds.

Jorge Nocedal and Stephen Wright. Numerical optimization. Springer Science & Business Media, 2006.

SNES: Nonlinear Solvers, SNESCreate(), SNES, SNESSetType(), SNESSetObjective(), SNESNewtonTRSetTolerances(), SNESNewtonTRSetUpdateParameters(), SNESNewtonTRSetNormType(), SNESNewtonTRSetFallbackType(), SNESNewtonTRSetQNType(), SNESNewtonTRSetPostCheck(), SNESNewtonTRSetPreCheck()

src/snes/impls/tr/tr.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESNewtonTRSetNormType()
```

Example 2 (unknown):
```unknown
SNESCreate()
```

Example 3 (unknown):
```unknown
SNESSetType()
```

Example 4 (unknown):
```unknown
SNESSetObjective()
```

---

## SNESNGMRESGetRestartFmRise#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNGMRESGetRestartFmRise/

**Contents:**
- SNESNGMRESGetRestartFmRise#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get whether SNESNGMRES increases the restart count when a step \(x_M\) increases the residual \(F_M\)

snes - the SNES context

flg - PETSC_TRUE if the option is enabled

SNES: Nonlinear Solvers, SNES, SNESNGMRES, SNESNGMRESSetRestartFmRise(), SNESNGMRESSetRestartType()

src/snes/impls/ngmres/snesngmres.c

SNESNGMRESGetRestartFmRise_NGMRES() in src/snes/impls/ngmres/snesngmres.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESNGMRESGetRestartFmRise(SNES snes, PetscBool *flg)
```

Example 2 (unknown):
```unknown
SNESNGMRESSetRestartFmRise()
```

Example 3 (unknown):
```unknown
SNESNGMRESSetRestartType()
```

---

## SNESNGMRESRestartType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNGMRESRestartType/

**Contents:**
- SNESNGMRESRestartType#
- Values#
- Options Database Keys#
- See Also#
- Level#
- Location#

the restart approach used by SNESNGMRES

SNES_NGMRES_RESTART_NONE - never restart

SNES_NGMRES_RESTART_DIFFERENCE - restart based upon difference criteria

SNES_NGMRES_RESTART_PERIODIC - restart after a fixed number of iterations

-snes_ngmres_restart_type (difference|periodic|none) - set the restart type

-snes_ngmres_restart 30 - sets the number of iterations before restart for periodic

SNES, SNESNGMRES, SNESNGMRESSetSelectType(), SNESNGMRESGetSelectType(), SNESNGMRESSetRestartType(), SNESNGMRESGetRestartType(), SNESNGMRESSelectType

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNES_NGMRES_RESTART_NONE
```

Example 2 (unknown):
```unknown
SNES_NGMRES_RESTART_DIFFERENCE
```

Example 3 (unknown):
```unknown
SNES_NGMRES_RESTART_PERIODIC
```

Example 4 (unknown):
```unknown
SNESNGMRESSetSelectType()
```

---

## SNESNGMRESSelectType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNGMRESSelectType/

**Contents:**
- SNESNGMRESSelectType#
- Values#
- Options Database Key#
- See Also#
- Level#
- Location#

the approach used by SNESNGMRES to determine how the candidate solution and combined solution are used to create the next iterate.

SNES_NGMRES_SELECT_NONE - choose the combined solution all the time

SNES_NGMRES_SELECT_DIFFERENCE - choose based upon the selection criteria

SNES_NGMRES_SELECT_LINESEARCH - choose based upon line search combination

-snes_ngmres_select_type (difference|none|linesearch) - select how the next iterate is created

SNES, SNESNGMRES, SNESNGMRESSetSelectType(), SNESNGMRESGetSelectType(), SNESNGMRESSetRestartType(), SNESNGMRESGetRestartType(), SNESNGMRESRestartType

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNES_NGMRES_SELECT_NONE
```

Example 2 (unknown):
```unknown
SNES_NGMRES_SELECT_DIFFERENCE
```

Example 3 (unknown):
```unknown
SNES_NGMRES_SELECT_LINESEARCH
```

Example 4 (unknown):
```unknown
SNESNGMRESSetSelectType()
```

---

## SNESNGMRESSetRestartFmRise#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNGMRESSetRestartFmRise/

**Contents:**
- SNESNGMRESSetRestartFmRise#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Increase the restart count if the step x_M increases the residual F_M inside a SNESNGMRES solve

snes - the SNES context.

flg - boolean value deciding whether to use the option or not, default is PETSC_FALSE

-snes_ngmres_restart_fm_rise (true|false) - Increase the restart count if the step x_M increases the residual F_M

If the proposed step x_M increases the residual F_M, it might be trying to get out of a stagnation area. To help the solver do that, remove the current stored solutions and residuals whenever F_M increases.

This option must be used with the SNESNGMRES SNESNGMRESRestartType of SNES_NGMRES_RESTART_DIFFERENCE

SNES: Nonlinear Solvers, SNES, SNES_NGMRES_RESTART_DIFFERENCE, SNESNGMRES, SNESNGMRESRestartType, SNESNGMRESSetRestartType()

src/snes/impls/ngmres/snesngmres.c

SNESNGMRESSetRestartFmRise_NGMRES() in src/snes/impls/ngmres/snesngmres.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESNGMRESSetRestartFmRise(SNES snes, PetscBool flg)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
SNESNGMRESRestartType
```

Example 4 (unknown):
```unknown
SNES_NGMRES_RESTART_DIFFERENCE
```

---

## SNESNGMRESSetRestartType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNGMRESSetRestartType/

**Contents:**
- SNESNGMRESSetRestartType#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Implementations#

Sets the restart type for SNESNGMRES.

snes - the iterative context

rtype - restart type, see SNESNGMRESRestartType

-snes_ngmres_restart_type (difference|periodic|none) - set the restart type

-snes_ngmres_restart restart - sets the number of iterations before restart for periodic

SNES: Nonlinear Solvers, SNES, SNES_NGMRES_RESTART_DIFFERENCE, SNESNGMRES, SNESNGMRESRestartType, SNESNGMRESSetRestartFmRise(), SNESNGMRESSetSelectType()

src/snes/impls/ngmres/snesngmres.c

SNESNGMRESSetRestartType_NGMRES() in src/snes/impls/ngmres/snesngmres.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESNGMRESSetRestartType(SNES snes, SNESNGMRESRestartType rtype)
```

Example 2 (unknown):
```unknown
SNESNGMRESRestartType
```

Example 3 (unknown):
```unknown
SNES_NGMRES_RESTART_DIFFERENCE
```

Example 4 (unknown):
```unknown
SNESNGMRESRestartType
```

---

## SNESNGMRESSetSelectType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNGMRESSetSelectType/

**Contents:**
- SNESNGMRESSetSelectType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Sets the selection type for SNESNGMRES. This determines how the candidate solution and combined solution are used to create the next iterate.

snes - the iterative context

stype - selection type, see SNESNGMRESSelectType

-snes_ngmres_select_type (difference|none|linesearch) - select type

The default line search used is the SNESLINESEARCHSECANT line search and it requires two additional function evaluations.

SNES: Nonlinear Solvers, SNES, SNESNGMRES, SNESNGMRESSelectType, SNES_NGMRES_SELECT_NONE, SNES_NGMRES_SELECT_DIFFERENCE, SNES_NGMRES_SELECT_LINESEARCH, SNESNGMRESSetRestartType()

src/snes/impls/ngmres/snesngmres.c

SNESNGMRESSetSelectType_NGMRES() in src/snes/impls/ngmres/snesngmres.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESNGMRESSetSelectType(SNES snes, SNESNGMRESSelectType stype)
```

Example 2 (unknown):
```unknown
SNESNGMRESSelectType
```

Example 3 (unknown):
```unknown
SNESLINESEARCHSECANT
```

Example 4 (unknown):
```unknown
SNESNGMRESSelectType
```

---

## SNESNGMRES#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNGMRES/

**Contents:**
- SNESNGMRES#
- Options Database Keys#
- Notes#
- References#
- See Also#
- Level#
- Location#

An implementation of the Nonlinear Generalized Minimum Residual method, Nonlinear GMRES, or N-GMRES [WO00], [BKST15] for solving nonlinear systems with SNES.

-snes_ngmres_select_type (difference|none|linesearch) - choose the select between candidate and combined solution

-snes_ngmres_restart_type (difference|none|periodic) - choose the restart conditions

-snes_ngmres_candidate - Use SNESNGMRES variant which combines candidate solutions instead of actual solutions

-snes_ngmres_m m - Number of stored previous solutions and residuals

-snes_ngmres_restart_it it - Number of iterations the restart conditions hold before restart

-snes_ngmres_gammaA gammaA - Residual tolerance for solution select between the candidate and combination

-snes_ngmres_gammaC gammaB - Residual tolerance for restart

-snes_ngmres_epsilonB epsilonB - Difference tolerance between subsequent solutions triggering restart

-snes_ngmres_deltaB deltaB - Difference tolerance between residuals triggering restart

-snes_ngmres_restart_fm_rise (true|false) - Restart on residual rise from \(x_M\) step

-snes_ngmres_monitor - Prints relevant information about the nonlinear GNMRES iterations

-snes_linesearch_type (none|basic|bt|secant|cp|nleqerr|bisection|shell) - Line search type used for the default smoother, see SNESLineSearchType

-snes_ngmres_additive_snes_linesearch_type type - line search type used to select between the candidate and combined solution with additive select type, see SNESLineSearchType

The N-GMRES method combines m previous solutions into a minimum-residual solution by solving a small linearized optimization problem at each iteration.

Very similar to the SNESANDERSON algorithm.

Unlike the linear GMRES algorithm this algorithm does not compute a Krylov subspace using the Arnoldi process. Instead it stores a collection of previous solutions and the residuals \( F(x) - b \) at those solutions.

This algorithm ignores any Jacobian provided with SNESSetJacobian()

Only supports left non-linear preconditioning.

Peter R. Brune, Matthew G. Knepley, Barry F. Smith, and Xuemin Tu. Composing scalable nonlinear algebraic solvers. SIAM Review, 57(4):535–565, 2015. http://www.mcs.anl.gov/papers/P2010-0112.pdf. URL: http://www.mcs.anl.gov/papers/P2010-0112.pdf, doi:10.1137/130936725.

T. Washio and C. W. Oosterlee. Krylov subspace acceleration for nonlinear multigrid schemes with application to recirculating flow. SIAM Journal on Scientific Computing, 21(5):1670–1690, 2000.

SNES: Nonlinear Solvers, SNESCreate(), SNES, SNESSetType(), SNESType, SNESANDERSON, SNESNGMRESSetSelectType(), SNESNGMRESSetRestartType(), SNESNGMRESSetRestartFmRise(), SNESNGMRESSelectType, SNESNGMRESRestartType

src/snes/impls/ngmres/snesngmres.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLineSearchType
```

Example 2 (unknown):
```unknown
SNESLineSearchType
```

Example 3 (unknown):
```unknown
SNESANDERSON
```

Example 4 (unknown):
```unknown
SNESSetJacobian()
```

---

## SNESNGSFn#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNGSFn/

**Contents:**
- SNESNGSFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

A prototype of a SNES nonlinear Gauss-Seidel function that would be passed to SNESSetNGS()

snes - the SNES context obtained from SNESCreate()

u - the current solution, updated in place

b - the right-hand side vector (which may be NULL)

ctx - [optional] user-defined context for matrix evaluation routine

SNES: Nonlinear Solvers, SNES, SNESSetJacobian(), SNESGetJacobian(), SNESFunctionFn, SNESSetFunction(), SNESGetFunction(), SNESJacobianFn

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetNGS()
```

Example 2 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode SNESNGSFn(SNES snes, Vec u, Vec b, PetscCtx ctx);
```

Example 3 (unknown):
```unknown
SNESCreate()
```

Example 4 (unknown):
```unknown
SNESSetJacobian()
```

---

## SNESNGSGetSweeps#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNGSGetSweeps/

**Contents:**
- SNESNGSGetSweeps#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Gets the number of sweeps nonlinear GS will use in SNESNCG

snes - the SNES context

sweeps - the number of sweeps of nonlinear GS to perform.

SNES: Nonlinear Solvers, SNES, SNESNCG, SNESSetNGS(), SNESGetNGS(), SNESSetNPC(), SNESNGSSetSweeps()

src/snes/impls/gs/snesgs.c

src/snes/tutorials/ex15.c src/snes/tutorials/ex5.c src/snes/tutorials/ex19.c src/snes/tutorials/ex55.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESNGSGetSweeps(SNES snes, PetscInt *sweeps)
```

Example 2 (unknown):
```unknown
SNESSetNGS()
```

Example 3 (unknown):
```unknown
SNESGetNGS()
```

Example 4 (unknown):
```unknown
SNESSetNPC()
```

---

## SNESNGSGetTolerances#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNGSGetTolerances/

**Contents:**
- SNESNGSGetTolerances#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets various parameters used in convergence tests for nonlinear Gauss-Seidel SNESNCG

snes - the SNES context

atol - absolute convergence tolerance

rtol - relative convergence tolerance

stol - convergence tolerance in terms of the norm of the change in the solution between steps

maxit - maximum number of iterations

The user can specify NULL for any parameter that is not needed.

SNES: Nonlinear Solvers, SNES, SNESNCG, SNESSetTolerances()

src/snes/impls/gs/snesgs.c

src/snes/tutorials/ex15.c src/snes/tutorials/ex5.c src/snes/tutorials/ex19.c src/snes/tutorials/ex55.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESNGSGetTolerances(SNES snes, PetscReal *atol, PetscReal *rtol, PetscReal *stol, PetscInt *maxit)
```

Example 2 (unknown):
```unknown
SNESSetTolerances()
```

---

## SNESNGSSetSweeps#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNGSSetSweeps/

**Contents:**
- SNESNGSSetSweeps#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Sets the number of sweeps of nonlinear GS to use in SNESNCG

snes - the SNES context

sweeps - the number of sweeps of nonlinear GS to perform.

-snes_ngs_sweeps n - Number of sweeps of nonlinear GS to apply

SNES: Nonlinear Solvers, SNES, SNESNCG, SNESSetNGS(), SNESGetNGS(), SNESSetNPC(), SNESNGSGetSweeps()

src/snes/impls/gs/snesgs.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESNGSSetSweeps(SNES snes, PetscInt sweeps)
```

Example 2 (unknown):
```unknown
SNESSetNGS()
```

Example 3 (unknown):
```unknown
SNESGetNGS()
```

Example 4 (unknown):
```unknown
SNESSetNPC()
```

---

## SNESNGSSetTolerances#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNGSSetTolerances/

**Contents:**
- SNESNGSSetTolerances#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#

Sets various parameters used in convergence tests for nonlinear Gauss-Seidel SNESNCG

snes - the SNES context

abstol - absolute convergence tolerance

rtol - relative convergence tolerance

stol - convergence tolerance in terms of the norm of the change in the solution between steps, || delta x || < stol*|| x ||

maxit - maximum number of iterations

-snes_ngs_atol abstol - Sets abstol

-snes_ngs_rtol rtol - Sets rtol

-snes_ngs_stol stol - Sets stol

-snes_max_it maxit - Sets maxit

Use PETSC_CURRENT to retain the value for any parameter

All parameters must be non-negative

Why can’t the values set with SNESSetTolerances() be used?

SNES: Nonlinear Solvers, SNES, SNESNCG

src/snes/impls/gs/snesgs.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESNGSSetTolerances(SNES snes, PetscReal abstol, PetscReal rtol, PetscReal stol, PetscInt maxit)
```

Example 2 (unknown):
```unknown
PETSC_CURRENT
```

Example 3 (unknown):
```unknown
SNESSetTolerances()
```

---

## SNESNGS#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNGS/

**Contents:**
- SNESNGS#
- Options Database Keys#
- Notes#
- References#
- See Also#
- Level#
- Location#

Either calls the user-provided Gauss-Seidel solution routine provided with SNESSetNGS() or does a finite difference secant approximation using coloring [BKST15].

-snes_ngs_sweeps n - Number of sweeps of nonlinear GS to apply

-snes_ngs_atol atol - Absolute residual tolerance for nonlinear GS iteration

-snes_ngs_rtol rtol - Relative residual tolerance for nonlinear GS iteration

-snes_ngs_stol stol - Absolute update tolerance for nonlinear GS iteration

-snes_ngs_max_it maxit - Maximum number of sweeps of nonlinea GS to apply

-snes_ngs_secant - Use pointwise secant local Jacobian approximation with coloring instead of user provided Gauss-Seidel routine, this is used by default if no user provided Gauss-Seidel routine is available. Requires either that a DM that can compute a coloring is available or a Jacobian sparse matrix is provided (from which to get the coloring).

-snes_ngs_secant_h h - Differencing parameter for secant approximation

-snes_ngs_secant_mat_coloring - Use the graph (matrix) coloring of the Jacobian for the secant GS even if a DM is available.

-snes_norm_schedule (none|always|initialonly|finalonly|initialfinalonly) - how often the residual norms are computed

the Gauss-Seidel smoother is inherited through composition. If a solver has been created with SNESGetNPC(), it will have its parent’s Gauss-Seidel routine associated with it.

By default this routine computes the solution norm at each iteration, this can be time consuming, you can turn this off with SNESSetNormSchedule() or -snes_norm_schedule none

Peter R. Brune, Matthew G. Knepley, Barry F. Smith, and Xuemin Tu. Composing scalable nonlinear algebraic solvers. SIAM Review, 57(4):535–565, 2015. http://www.mcs.anl.gov/papers/P2010-0112.pdf. URL: http://www.mcs.anl.gov/papers/P2010-0112.pdf, doi:10.1137/130936725.

SNES: Nonlinear Solvers, SNESNCG, SNESCreate(), SNES, SNESSetType(), SNESSetNGS(), SNESType, SNESNGSSetSweeps(), SNESNGSSetTolerances(), SNESSetNormSchedule(), SNESNGSGetTolerances(), SNESNGSGetSweeps()

src/snes/impls/gs/snesgs.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetNGS()
```

Example 2 (unknown):
```unknown
SNESGetNPC()
```

Example 3 (unknown):
```unknown
SNESSetNormSchedule()
```

Example 4 (rust):
```rust
-snes_norm_schedule none
```

---

## SNESNormSchedule#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNormSchedule/

**Contents:**
- SNESNormSchedule#
- Synopsis#
- Values#
- Notes#
- See Also#
- Level#
- Location#

Frequency with which the norm is computed during a nonliner solve

SNES_NORM_DEFAULT - use the default behavior for the current SNESType

SNES_NORM_NONE - avoid all norm computations

SNES_NORM_ALWAYS - compute the norms whenever possible

SNES_NORM_INITIAL_ONLY - compute the norm only when the algorithm starts

SNES_NORM_FINAL_ONLY - compute the norm only when the algorithm finishes

SNES_NORM_INITIAL_FINAL_ONLY - compute the norm at the start and end of the algorithm

Support for these is highly dependent on the solver.

Some options limit the convergence tests that can be used.

The SNES_NORM_NONE option is most commonly used when the nonlinear solver is being used as a smoother, for example for SNESFAS

This is primarily used to turn off extra norm and function computation when the solvers are composed.

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESGetConvergedReason(), KSPSetNormType(), KSPSetConvergenceTest(), KSPSetPCSide()

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  SNES_NORM_DEFAULT            = -1,
  SNES_NORM_NONE               = 0,
  SNES_NORM_ALWAYS             = 1,
  SNES_NORM_INITIAL_ONLY       = 2,
  SNES_NORM_FINAL_ONLY         = 3,
  SNES_NORM_INITIAL_FINAL_ONLY = 4
} SNESNormSchedule;
```

Example 2 (unknown):
```unknown
SNES_NORM_DEFAULT
```

Example 3 (unknown):
```unknown
SNES_NORM_NONE
```

Example 4 (unknown):
```unknown
SNES_NORM_ALWAYS
```

---

## SNESNRICHARDSON#

**URL:** https://petsc.org/release/manualpages/SNES/SNESNRICHARDSON/

**Contents:**
- SNESNRICHARDSON#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#

Richardson nonlinear solver that uses successive substitutions, also sometimes known as Picard iteration.

-snes_linesearch_type (none|basic|bt|secant|cp|nleqerr|bisection|shell) - Line search type, see SNESLineSearchType

-snes_linesearch_damping damping - Damping for the line search.

If no inner nonlinear preconditioner is provided then solves \(F(x) - b = 0\) using \(x^{n+1} = x^{n} - \lambda (F(x^n) - b)\), where \(\lambda\) is obtained with either SNESLineSearchSetDamping() or -snes_linesearch_damping if using the basic (or, equivalently, the none) line search type, or determined by an actual line search algorithm. If an inner nonlinear preconditioner is provided (either with -npc_snes_type or SNESSetNPC()), then the inner solver is called on the initial solution \(x^n\) and the nonlinear Richardson uses \( x^{n+1} = x^{n} + \lambda d^{n}\) where \(d^{n} = \hat{x}^{n} - x^{n}\) where \(\hat{x}^{n}\) is the solution returned from the inner solver.

The update, especially without inner nonlinear preconditioner, may be ill-scaled. If using the basic (or none) line search, one may have to scale the update with either SNESLineSearchSetDamping() or -snes_linesearch_damping as mentioned above.

This uses no derivative information provided with SNESSetJacobian() thus it will be much slower than Newton’s method obtained with -snes_type newtonls

Only supports left non-linear preconditioning.

SNES: Nonlinear Solvers, SNESCreate(), SNES, SNESSetType(), SNESNEWTONLS, SNESNEWTONTR, SNESNGMRES, SNESQN, SNESNCG, SNESLineSearchSetDamping(), SNESLineSearchType

src/snes/impls/richardson/snesrichardson.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLineSearchType
```

Example 2 (unknown):
```unknown
SNESLineSearchSetDamping()
```

Example 3 (unknown):
```unknown
-snes_linesearch_damping
```

Example 4 (unknown):
```unknown
-npc_snes_type
```

---

## SNESObjectiveComputeFunctionDefaultFD#

**URL:** https://petsc.org/release/manualpages/SNES/SNESObjectiveComputeFunctionDefaultFD/

**Contents:**
- SNESObjectiveComputeFunctionDefaultFD#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#

Computes the gradient of a user provided objective function

snes - the SNES context

ctx - the (ignored) function context

F - the function value

-snes_fd_function_eps - Tolerance for including non-zero entries into the gradient, default is 1.e-6

-snes_fd_function - Computes function from user provided objective function (set with SNESSetObjective()) with finite difference

This function can be used with SNESSetFunction() to have the nonlinear function solved for with SNES defined by the gradient of an objective function SNESObjectiveComputeFunctionDefaultFD() is similar in character to SNESComputeJacobianDefault(). Therefore, it should be used for debugging purposes only. Using it in conjunction with SNESComputeJacobianDefault() is excessively costly and produces a Jacobian that is quite noisy. This is often necessary, but should be done with care, even when debugging small problems.

This uses quadratic interpolation of the objective to form each value in the function.

SNES: Nonlinear Solvers, SNESSetObjective(), SNESSetFunction(), SNESComputeObjective(), SNESComputeJacobianDefault(), SNESObjectiveFn

src/snes/interface/snesob.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESObjectiveComputeFunctionDefaultFD(SNES snes, Vec X, Vec F, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESSetObjective()
```

Example 3 (unknown):
```unknown
SNESSetFunction()
```

Example 4 (unknown):
```unknown
SNESObjectiveComputeFunctionDefaultFD()
```

---

## SNESObjectiveFn#

**URL:** https://petsc.org/release/manualpages/SNES/SNESObjectiveFn/

**Contents:**
- SNESObjectiveFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

A prototype of a SNES objective evaluation function that would be passed to SNESSetObjective()

ctx - [optional] user-defined function context

SNES: Nonlinear Solvers, SNES, SNESSetFunction(), SNESGetFunction(), SNESJacobianFn, SNESNGSFn

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetObjective()
```

Example 2 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode SNESObjectiveFn(SNES snes, Vec u, PetscReal *o, PetscCtx ctx);
```

Example 3 (unknown):
```unknown
SNESSetFunction()
```

Example 4 (unknown):
```unknown
SNESGetFunction()
```

---

## SNESParametersInitialize#

**URL:** https://petsc.org/release/manualpages/SNES/SNESParametersInitialize/

**Contents:**
- SNESParametersInitialize#
- Synopsis#
- Input Parameter#
- Developer Note#
- See Also#
- Level#
- Location#

Sets all the parameters in snes to their default value (when SNESCreate() was called) if they currently contain default values

snes - the SNES object

This is called by all the SNESCreate_XXX() routines.

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESDestroy(), SNESSetLagPreconditioner(), SNESSetLagJacobian(), PetscObjectParameterSetDefault()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESCreate()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESParametersInitialize(SNES snes)
```

Example 3 (unknown):
```unknown
SNESCreate_XXX()
```

Example 4 (unknown):
```unknown
SNESSolve()
```

---

## SNESPatchSetCellNumbering#

**URL:** https://petsc.org/release/manualpages/SNES/SNESPatchSetCellNumbering/

**Contents:**
- SNESPatchSetCellNumbering#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the PetscSection that provides a numbering of the cells used to define patches in a SNESPATCH solver

snes - the SNESPATCH solver

cellNumbering - the PetscSection giving the cell numbering; forwarded to the underlying PCPATCH via PCPatchSetCellNumbering()

SNES: Nonlinear Solvers, SNESPATCH, PCPATCH, PCPatchSetCellNumbering(), PetscSection

src/snes/impls/patch/snespatch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESPatchSetCellNumbering(SNES snes, PetscSection cellNumbering)
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (unknown):
```unknown
PCPatchSetCellNumbering()
```

---

## SNESPatchSetComputeFunction#

**URL:** https://petsc.org/release/manualpages/SNES/SNESPatchSetComputeFunction/

**Contents:**
- SNESPatchSetComputeFunction#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#

Set the callback used to compute the per-patch nonlinear residual for a SNESPATCH solver

snes - the SNESPATCH solver

func - callback that computes the patch residual; forwarded to the underlying PCPATCH via PCPatchSetComputeFunction()

ctx - optional application context passed to func

pc - the PC associated with the SNESPATCH solver

x - the input solution (not used in linear problems)

f - the patch residual vector

cellIS - an array of the cell numbers

n - the size of dofsArray

dofsArray - the dofmap for the dofs to be solved for

dofsArrayWithAll - the dofmap for all dofs on the patch

ctx - the application context

SNES: Nonlinear Solvers, SNESPATCH, PCPATCH, PCPatchSetComputeFunction(), SNESPatchSetComputeOperator()

src/snes/impls/patch/snespatch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESPatchSetComputeFunction(SNES snes, PetscErrorCode (*func)(PC pc, PetscInt point, Vec x, Vec f, IS cellIS, PetscInt n, const PetscInt *dofsArray, const PetscInt *dofsArrayWithAll, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
PCPatchSetComputeFunction()
```

Example 3 (unknown):
```unknown
PCPatchSetComputeFunction()
```

Example 4 (unknown):
```unknown
SNESPatchSetComputeOperator()
```

---

## SNESPatchSetComputeOperator#

**URL:** https://petsc.org/release/manualpages/SNES/SNESPatchSetComputeOperator/

**Contents:**
- SNESPatchSetComputeOperator#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#

Set the callback used to assemble the per-patch Jacobian for a SNESPATCH solver

snes - the SNESPATCH solver

func - callback that assembles the patch Jacobian; forwarded to the underlying PCPATCH via PCPatchSetComputeOperator()

ctx - optional application context passed to func

pc - the PC associated with the SNESPATCH solver

x - the input solution (not used in linear problems)

mat - the patch matrix

cellIS - an array of the cell numbers

n - the size of dofsArray

dofsArray - the dofmap for the dofs to be solved for

dofsArrayWithAll - the dofmap for all dofs on the patch

ctx - the application context

SNES: Nonlinear Solvers, SNESPATCH, PCPATCH, PCPatchSetComputeOperator(), SNESPatchSetComputeFunction()

src/snes/impls/patch/snespatch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESPatchSetComputeOperator(SNES snes, PetscErrorCode (*func)(PC pc, PetscInt point, Vec x, Mat mat, IS cellIS, PetscInt n, const PetscInt *dofsArray, const PetscInt *dofsArrayWithAll, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
PCPatchSetComputeOperator()
```

Example 3 (unknown):
```unknown
PCPatchSetComputeOperator()
```

Example 4 (unknown):
```unknown
SNESPatchSetComputeFunction()
```

---

## SNESPatchSetConstructType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESPatchSetConstructType/

**Contents:**
- SNESPatchSetConstructType#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#

Set the way patches are constructed for a SNESPATCH solver

snes - the SNESPATCH solver

ctype - the PCPatchConstructType selecting the patch construction strategy

func - user callback that builds the patches, used only when ctype is PC_PATCH_USER or PC_PATCH_PYTHON; may be NULL otherwise

ctx - optional application context passed to func

pc - the PC associated with the SNESPATCH solver

npatch - number of patches

patches - the IS that define each patch

patchIterationSet - how the patches are iterated over

ctx - optional application context

SNES: Nonlinear Solvers, SNESPATCH, PCPATCH, PCPatchSetConstructType(), PCPatchConstructType

src/snes/impls/patch/snespatch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESPatchSetConstructType(SNES snes, PCPatchConstructType ctype, PetscErrorCode (*func)(PC pc, PetscInt *npatch, IS *patches[], IS *patchIterationSet, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
PCPatchConstructType
```

Example 3 (unknown):
```unknown
PC_PATCH_USER
```

Example 4 (unknown):
```unknown
PC_PATCH_PYTHON
```

---

## SNESPatchSetDiscretisationInfo#

**URL:** https://petsc.org/release/manualpages/SNES/SNESPatchSetDiscretisationInfo/

**Contents:**
- SNESPatchSetDiscretisationInfo#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Provide the per-subspace discretisation information required by a SNESPATCH to build patch problems

snes - the SNESPATCH solver

nsubspaces - the number of discretisation subspaces (e.g. fields)

dms - array of length nsubspaces of DMs, one per subspace

bs - array of length nsubspaces giving the block size of each subspace

nodesPerCell - array of length nsubspaces giving the number of nodes per cell for each subspace

cellNodeMap - array of length nsubspaces; entry i is a cell-to-node map for subspace i

subspaceOffsets - array of length nsubspaces + 1 giving the starting global dof offset of each subspace

numGhostBcs - number of ghost (off-process) boundary-condition dofs

ghostBcNodes - array of length numGhostBcs of the ghost boundary-condition dof indices

numGlobalBcs - number of global boundary-condition dofs

globalBcNodes - array of length numGlobalBcs of the global boundary-condition dof indices

A DM must already be attached to snes (via SNESSetDM()) before calling this routine. Internally, the information is forwarded to the underlying PCPATCH via PCPatchSetDiscretisationInfo().

SNES: Nonlinear Solvers, SNESPATCH, PCPATCH, PCPatchSetDiscretisationInfo(), SNESPatchSetComputeOperator(), SNESPatchSetComputeFunction()

src/snes/impls/patch/snespatch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESPatchSetDiscretisationInfo(SNES snes, PetscInt nsubspaces, DM dms[], PetscInt bs[], PetscInt nodesPerCell[], const PetscInt **cellNodeMap, const PetscInt subspaceOffsets[], PetscInt numGhostBcs, const PetscInt ghostBcNodes[], PetscInt numGlobalBcs, const PetscInt globalBcNodes[])
```

Example 2 (unknown):
```unknown
nsubspaces + 1
```

Example 3 (unknown):
```unknown
numGhostBcs
```

Example 4 (unknown):
```unknown
numGlobalBcs
```

---

## SNESPATCH#

**URL:** https://petsc.org/release/manualpages/SNES/SNESPATCH/

**Contents:**
- SNESPATCH#
- References#
- See Also#
- Level#
- Location#

Solve a nonlinear problem or apply a nonlinear smoother by composing together many nonlinear solvers on (often overlapping) patches [BKST15]

Peter R. Brune, Matthew G. Knepley, Barry F. Smith, and Xuemin Tu. Composing scalable nonlinear algebraic solvers. SIAM Review, 57(4):535–565, 2015. http://www.mcs.anl.gov/papers/P2010-0112.pdf. URL: http://www.mcs.anl.gov/papers/P2010-0112.pdf, doi:10.1137/130936725.

SNES: Nonlinear Solvers, SNESFAS, SNESCreate(), SNESSetType(), SNESType, SNES, PCPATCH

src/snes/impls/patch/snespatch.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESCreate()
```

Example 2 (unknown):
```unknown
SNESSetType()
```

---

## SNESPicardComputeFunction#

**URL:** https://petsc.org/release/manualpages/SNES/SNESPicardComputeFunction/

**Contents:**
- SNESPicardComputeFunction#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Compute the residual \(A(x) x - b(x)\) using the callbacks registered by SNESSetPicard()

snes - the SNES context

x - the current iterate

ctx - unused application context; the Picard callbacks are retrieved from the attached DMSNES

f - the residual vector

SNES: Nonlinear Solvers, SNES, SNESSetPicard(), SNESPicardComputeMFFunction(), SNESPicardComputeJacobian()

src/snes/interface/snes.c

src/snes/tutorials/ex15.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetPicard()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESPicardComputeFunction(SNES snes, Vec x, Vec f, PetscCtx ctx)
```

Example 3 (unknown):
```unknown
SNESSetPicard()
```

Example 4 (unknown):
```unknown
SNESPicardComputeMFFunction()
```

---

## SNESPicardComputeJacobian#

**URL:** https://petsc.org/release/manualpages/SNES/SNESPicardComputeJacobian/

**Contents:**
- SNESPicardComputeJacobian#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Trivial Jacobian assembly callback used by SNESSetPicard(); the Picard operator is filled in by SNESPicardComputeFunction()

snes - the SNES context

x1 - the current iterate (unused)

J - the Jacobian matrix to assemble

B - the preconditioning matrix (unused)

ctx - unused application context

Only calls MatAssemblyBegin()/MatAssemblyEnd() on J, because the Picard iteration reuses the operator already assembled by SNESPicardComputeFunction().

SNES: Nonlinear Solvers, SNES, SNESSetPicard(), SNESPicardComputeFunction(), SNESPicardComputeMFFunction()

src/snes/interface/snes.c

src/snes/tutorials/ex15.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetPicard()
```

Example 2 (unknown):
```unknown
SNESPicardComputeFunction()
```

Example 3 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESPicardComputeJacobian(SNES snes, Vec x1, Mat J, Mat B, PetscCtx ctx)
```

Example 4 (unknown):
```unknown
MatAssemblyBegin()
```

---

## SNESPicardComputeMFFunction#

**URL:** https://petsc.org/release/manualpages/SNES/SNESPicardComputeMFFunction/

**Contents:**
- SNESPicardComputeMFFunction#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Matrix-free residual \(A(x) x - b(x)\) used by SNESSetPicard() when the operator is applied through -snes_mf_operator

snes - the SNES context

x - the current iterate

ctx - unused application context; the Picard callbacks are retrieved from the attached DMSNES

f - the residual vector

Uses a duplicate of snes->jacobian_pre because snes->jacobian_pre cannot be changed during the KSPSolve().

SNES: Nonlinear Solvers, SNES, SNESSetPicard(), SNESPicardComputeFunction(), SNESPicardComputeJacobian()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetPicard()
```

Example 2 (unknown):
```unknown
-snes_mf_operator
```

Example 3 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESPicardComputeMFFunction(SNES snes, Vec x, Vec f, PetscCtx ctx)
```

Example 4 (perl):
```perl
snes->jacobian_pre
```

---

## SNESPruneJacobianColor#

**URL:** https://petsc.org/release/manualpages/SNES/SNESPruneJacobianColor/

**Contents:**
- SNESPruneJacobianColor#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Remove nondiagonal zeros in the Jacobian matrix and update the MatMFFD coloring information based on the new nonzero structure

snes - the SNES context

J - Jacobian matrix (not altered in this routine)

B - newly computed Jacobian matrix to use with preconditioner (generally the same as J)

This function improves the MatMFFD coloring performance when the Jacobian matrix is overallocated or contains many constant zeros entries, which is typically the case when the matrix is generated by a DM and multiple fields are involved.

Users need to make sure that the Jacobian matrix is properly filled to reflect the sparsity structure. For MatMFFD coloring, the values of nonzero entries are not important. So one can usually call SNESComputeJacobian() with randomized input vectors to generate a dummy Jacobian. SNESComputeJacobian() should be called before SNESSolve() but after SNESSetUp().

SNES: Nonlinear Solvers, SNESComputeJacobianDefaultColor(), MatEliminateZeros(), MatFDColoringCreate(), MatFDColoringSetFunction()

src/snes/interface/snesj2.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscdm.h"    
PetscErrorCode SNESPruneJacobianColor(SNES snes, Mat J, Mat B)
```

Example 2 (unknown):
```unknown
SNESComputeJacobian()
```

Example 3 (unknown):
```unknown
SNESComputeJacobian()
```

Example 4 (unknown):
```unknown
SNESSolve()
```

---

## SNESPythonGetType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESPythonGetType/

**Contents:**
- SNESPythonGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the type of a SNES object implemented in Python set with SNESPythonSetType()

snes - the nonlinear solver (SNES) context.

pyname - full dotted Python name [package].module[.{class|function}]

SNES: Nonlinear Solvers, SNES, SNESCreate(), SNESSetType(), SNESPYTHON, PetscPythonInitialize(), SNESPythonSetType()

src/snes/impls/python/pythonsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESPythonSetType()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESPythonGetType(SNES snes, const char *pyname[])
```

Example 3 (unknown):
```unknown
SNESCreate()
```

Example 4 (unknown):
```unknown
SNESSetType()
```

---

## SNESPythonSetType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESPythonSetType/

**Contents:**
- SNESPythonSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Initialize a SNES object implemented in Python.

snes - the nonlinear solver (SNES) context.

pyname - full dotted Python name [package].module[.{class|function}]

-snes_python_type pyname - python class

SNES: Nonlinear Solvers, SNES, SNESCreate(), SNESSetType(), SNESPYTHON, PetscPythonInitialize(), SNESPythonGetType()

src/snes/impls/python/pythonsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESPythonSetType(SNES snes, const char pyname[])
```

Example 2 (unknown):
```unknown
SNESCreate()
```

Example 3 (unknown):
```unknown
SNESSetType()
```

Example 4 (unknown):
```unknown
PetscPythonInitialize()
```

---

## SNESPYTHON#

**URL:** https://petsc.org/release/manualpages/SNES/SNESPYTHON/

**Contents:**
- SNESPYTHON#
- See Also#
- Level#
- Location#

a SNESType that is implemented as a Python class using SNESPythonSetType()

SNES: Nonlinear Solvers, SNES, SNESCreate(), SNESSHELL, SNESSetType(), PetscPythonInitialize(), SNESPythonSetType(), SNESPythonGetType(), TSPYTHON, TAOPYTHON

src/snes/impls/python/pythonsnes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESPythonSetType()
```

Example 2 (unknown):
```unknown
SNESCreate()
```

Example 3 (unknown):
```unknown
SNESSetType()
```

Example 4 (unknown):
```unknown
PetscPythonInitialize()
```

---

## SNESQNRestartType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESQNRestartType/

**Contents:**
- SNESQNRestartType#
- Values#
- Options Database Keys#
- See Also#
- Level#
- Location#

the restart approached used by SNESQN

SNES_QN_RESTART_NONE - never restart

SNES_QN_RESTART_POWELL - restart based upon descent criteria

SNES_QN_RESTART_PERIODIC - restart after a fixed number of iterations

-snes_qn_restart_type (powell|periodic|none) - set the restart type

-snes_qn_m m - sets the number of stored updates and the restart period for periodic

SNES, SNESQN, SNESQNSetScaleType(), SNESQNType, SNESQNSetType(), SNESQNSetRestartType(), SNESQNScaleType

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNES_QN_RESTART_NONE
```

Example 2 (unknown):
```unknown
SNES_QN_RESTART_POWELL
```

Example 3 (unknown):
```unknown
SNES_QN_RESTART_PERIODIC
```

Example 4 (unknown):
```unknown
SNESQNSetScaleType()
```

---

## SNESQNScaleType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESQNScaleType/

**Contents:**
- SNESQNScaleType#
- Values#
- Options Database Key#
- See Also#
- Level#
- Location#

the scaling type used by SNESQN

SNES_QN_SCALE_NONE - don’t scale the problem

SNES_QN_SCALE_SCALAR - use Shanno scaling

SNES_QN_SCALE_DIAGONAL - scale with a diagonalized BFGS formula (see Gilbert and Lemarechal 1989), available

SNES_QN_SCALE_JACOBIAN - scale by solving a linear system coming from the Jacobian you provided with SNESSetJacobian() computed at the first iteration of SNESQN and at ever restart.

-snes_qn_scale_type (diagonal|none|scalar|jacobian) - Select the scaling type

SNES, SNESQN, SNESQNSetScaleType(), SNESQNType, SNESQNSetType(), SNESQNSetRestartType(), SNESQNRestartType

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNES_QN_SCALE_NONE
```

Example 2 (unknown):
```unknown
SNES_QN_SCALE_SCALAR
```

Example 3 (unknown):
```unknown
SNES_QN_SCALE_DIAGONAL
```

Example 4 (unknown):
```unknown
SNES_QN_SCALE_JACOBIAN
```

---

## SNESQNSetRestartType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESQNSetRestartType/

**Contents:**
- SNESQNSetRestartType#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Implementations#

Sets the restart type for SNESQN.

snes - the iterative context

rtype - restart type, see SNESQNRestartType

-snes_qn_restart_type (powell|periodic|none) - set the restart type

-snes_qn_m m - sets the number of stored updates and the restart period for periodic

SNES: Nonlinear Solvers, SNES, SNESQN, SNESQNRestartType, SNES_QN_RESTART_NONE, SNES_QN_RESTART_POWELL, SNES_QN_RESTART_PERIODIC, SNESQNType, SNESQNScaleType

src/snes/impls/qn/qn.c

SNESQNSetRestartType_QN() in src/snes/impls/qn/qn.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESQNSetRestartType(SNES snes, SNESQNRestartType rtype)
```

Example 2 (unknown):
```unknown
SNESQNRestartType
```

Example 3 (unknown):
```unknown
SNESQNRestartType
```

Example 4 (unknown):
```unknown
SNES_QN_RESTART_NONE
```

---

## SNESQNSetScaleType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESQNSetScaleType/

**Contents:**
- SNESQNSetScaleType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

Sets the scaling type for the inner inverse Jacobian in SNESQN.

snes - the nonlinear solver context

stype - scale type, see SNESQNScaleType

-snes_qn_scale_type (diagonal|none|scalar|jacobian) - Scaling type

SNES: Nonlinear Solvers, SNES, SNESQN, SNESLineSearch, SNESQNScaleType, SNESSetJacobian(), SNESQNType, SNESQNRestartType

src/snes/impls/qn/qn.c

SNESQNSetScaleType_QN() in src/snes/impls/qn/qn.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESQNSetScaleType(SNES snes, SNESQNScaleType stype)
```

Example 2 (unknown):
```unknown
SNESQNScaleType
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
SNESQNScaleType
```

---

## SNESQNSetType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESQNSetType/

**Contents:**
- SNESQNSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

Sets the quasi-Newton variant to be used in SNESQN.

snes - the iterative context

qtype - variant type, see SNESQNType

-snes_qn_type (lbfgs|broyden|badbroyden) - quasi-Newton type

SNES: Nonlinear Solvers, SNESQN, SNES_QN_LBFGS, SNES_QN_BROYDEN, SNES_QN_BADBROYDEN, SNESQNType, SNESQNScaleType, TAOLMVM, TAOBLMVM

src/snes/impls/qn/qn.c

SNESQNSetType_QN() in src/snes/impls/qn/qn.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESQNSetType(SNES snes, SNESQNType qtype)
```

Example 2 (unknown):
```unknown
SNES_QN_LBFGS
```

Example 3 (unknown):
```unknown
SNES_QN_BROYDEN
```

Example 4 (unknown):
```unknown
SNES_QN_BADBROYDEN
```

---

## SNESQNType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESQNType/

**Contents:**
- SNESQNType#
- Values#
- Options Database Key#
- See Also#
- Level#
- Location#

the type used by SNESQN

SNES_QN_LBFGS - LBFGS variant

SNES_QN_BROYDEN - Broyden variant

SNES_QN_BADBROYDEN - Bad Broyden variant

-snes_qn_type (lbfgs|broyden|badbroyden) - quasi-Newton type

SNES, SNESQN, SNESQNSetScaleType(), SNESQNSetType(), SNESQNScaleType, SNESQNRestartType, SNESQNSetRestartType()

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNES_QN_LBFGS
```

Example 2 (unknown):
```unknown
SNES_QN_BROYDEN
```

Example 3 (unknown):
```unknown
SNES_QN_BADBROYDEN
```

Example 4 (unknown):
```unknown
SNESQNSetScaleType()
```

---

## SNESQN#

**URL:** https://petsc.org/release/manualpages/SNES/SNESQN/

**Contents:**
- SNESQN#
- Options Database Keys#
- Notes#
- References#
- See Also#
- Level#
- Location#

Limited-Memory Quasi-Newton methods for the solution of nonlinear systems.

-snes_qn_m m - Number of past states saved for the L-Broyden methods.

-snes_qn_restart_type (powell|periodic|none) - set the restart type

-snes_qn_powell_gamma gamma - Angle condition for restart.

-snes_qn_powell_descent - Descent condition for restart.

-snes_qn_type (lbfgs|broyden|badbroyden) - QN type

-snes_qn_scale_type (diagonal|none|scalar|jacobian) - scaling performed on inner Jacobian

-snes_linesearch_type (none|basic|bt|secant|cp|nleqerr|bisection|shell) - Line search type, see SNESLineSearchType

-snes_qn_monitor - Monitors the quasi-newton Jacobian.

This implements the L-BFGS, Broyden, and “Bad” Broyden algorithms for the solution of \(F(x) = b\) using previous change in \(F(x)\) and \(x\) to form the approximate inverse Jacobian using a series of multiplicative rank-one updates.

When using a nonlinear preconditioner, one has two options as to how the preconditioner is applied. The first of these options, sequential, uses the preconditioner to generate a new solution and function and uses those at this iteration as the current iteration’s values when constructing the approximate Jacobian. The second, composed, perturbs the problem the Jacobian represents to be \(P(x, b) - x = 0 \), where \(P(x, b)\) is the preconditioner.

Uses left nonlinear preconditioning by default.

See [BNS94], [Kel95], [BHW85], [Gri12], [GLemarechal89], [DM19], and [BKST15]

P.N. Brown, A.C. Hindmarsh, and H.F. Walker. Experiments with quasi-Newton methods in solving stiff ODE systems. SIAM Journal on Scientific and Statistical Computing, 6(2):297–313, 1985.

Peter R. Brune, Matthew G. Knepley, Barry F. Smith, and Xuemin Tu. Composing scalable nonlinear algebraic solvers. SIAM Review, 57(4):535–565, 2015. http://www.mcs.anl.gov/papers/P2010-0112.pdf. URL: http://www.mcs.anl.gov/papers/P2010-0112.pdf, doi:10.1137/130936725.

Richard H Byrd, Jorge Nocedal, and Robert B Schnabel. Representations of quasi-Newton matrices and their use in limited memory methods. Mathematical Programming, 63(1-3):129–156, 1994.

Alp Dener and Todd Munson. Accelerating limited-memory quasi-Newton convergence for large-scale optimization. In Computational Science–ICCS 2019: 19th International Conference, Faro, Portugal, June 12–14, 2019, Proceedings, Part III 19, 495–507. Springer, 2019.

Jean Charles Gilbert and Claude Lemaréchal. Some numerical experiments with variable-storage quasi-Newton algorithms. Mathematical programming, 45(1-3):407–435, 1989.

Andreas Griewank. Broyden updating, the good and the bad! Optimization Stories, Documenta Mathematica. Extra Volume: Optimization Stories, pages 301–315, 2012.

C. T. Kelley. Iterative Methods for Linear and Nonlinear Equations. SIAM, Philadelphia, 1995.

SNES: Nonlinear Solvers, SNESQNRestartType, SNESQNSetRestartType(), SNESCreate(), SNES, SNESSetType(), SNESNEWTONLS, SNESNEWTONTR, SNESQNScaleType, SNESQNSetScaleType(), SNESQNType, SNESQNSetType()

src/snes/impls/qn/qn.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLineSearchType
```

Example 2 (unknown):
```unknown
SNESQNRestartType
```

Example 3 (unknown):
```unknown
SNESQNSetRestartType()
```

Example 4 (unknown):
```unknown
SNESCreate()
```

---

## SNESRegisterAll#

**URL:** https://petsc.org/release/manualpages/SNES/SNESRegisterAll/

**Contents:**
- SNESRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the nonlinear solver methods in the SNES package.

SNES: Nonlinear Solvers, SNES, SNESRegisterDestroy()

src/snes/interface/snesregi.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
PetscErrorCode SNESRegisterAll(void)
```

Example 2 (unknown):
```unknown
SNESRegisterDestroy()
```

---

## SNESRegister#

**URL:** https://petsc.org/release/manualpages/SNES/SNESRegister/

**Contents:**
- SNESRegister#
- Synopsis#
- Input Parameters#
- Note#
- Example Usage#
- See Also#
- Level#
- Location#

Adds a method to the nonlinear solver package.

sname - name of a new user-defined solver

function - routine to create method context

SNESRegister() may be called multiple times to add several user-defined solvers.

Then, your solver can be chosen with the procedural interface via

or at runtime via the option

SNES: Nonlinear Solvers, SNESRegisterAll(), SNESRegisterDestroy()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESRegister(const char sname[], PetscErrorCode (*function)(SNES))
```

Example 2 (unknown):
```unknown
SNESRegister()
```

Example 3 (unknown):
```unknown
SNESRegister("my_solver", MySolverCreate);
```

Example 4 (unknown):
```unknown
SNESSetType(snes, "my_solver")
```

---

## SNESResetCounters#

**URL:** https://petsc.org/release/manualpages/SNES/SNESResetCounters/

**Contents:**
- SNESResetCounters#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Reset counters for linear iterations and function evaluations.

It honors the flag set with SNESSetCountersReset()

SNES: Nonlinear Solvers, SNESGetNumberFunctionEvals(), SNESGetLinearSolveIterations(), SNESGetNPC()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESResetCounters(SNES snes)
```

Example 2 (unknown):
```unknown
SNESSetCountersReset()
```

Example 3 (unknown):
```unknown
SNESGetNumberFunctionEvals()
```

Example 4 (unknown):
```unknown
SNESGetLinearSolveIterations()
```

---

## SNESResetFromOptions#

**URL:** https://petsc.org/release/manualpages/SNES/SNESResetFromOptions/

**Contents:**
- SNESResetFromOptions#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Sets various SNES and KSP parameters from user options ONLY if the SNESSetFromOptions() was previously called

snes - the SNES context

SNES: Nonlinear Solvers, SNES, SNESSetFromOptions(), SNESSetOptionsPrefix()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetFromOptions()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESResetFromOptions(SNES snes)
```

Example 3 (unknown):
```unknown
SNESSetFromOptions()
```

Example 4 (unknown):
```unknown
SNESSetOptionsPrefix()
```

---

## SNESReset#

**URL:** https://petsc.org/release/manualpages/SNES/SNESReset/

**Contents:**
- SNESReset#
- Synopsis#
- Input Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Resets a SNES context to the state it was in before SNESSetUp() was called and removes any allocated Vec and Mat from its data structures

snes - the nonlinear iterative solver context obtained from SNESCreate()

Any options set on the SNES object, including those set with SNESSetFromOptions() remain.

Call this if you wish to reuse a SNES but with different size vectors

Also calls the application context destroy routine set with SNESSetComputeApplicationContext()

SNES: Nonlinear Solvers, SNES, SNESDestroy(), SNESCreate(), SNESSetUp(), SNESSolve()

src/snes/interface/snes.c

SNESReset_NEWTONAL() in src/snes/impls/al/al.c SNESReset_Composite() in src/snes/impls/composite/snescomposite.c SNESReset_FAS() in src/snes/impls/fas/fas.c SNESReset_NGS() in src/snes/impls/gs/snesgs.c SNESReset_Multiblock() in src/snes/impls/multiblock/multiblock.c SNESReset_NASM() in src/snes/impls/nasm/nasm.c SNESReset_NGMRES() in src/snes/impls/ngmres/snesngmres.c SNESReset_Patch() in src/snes/impls/patch/snespatch.c SNESReset_QN() in src/snes/impls/qn/qn.c SNESReset_NEWTONTR() in src/snes/impls/tr/tr.c SNESReset_VINEWTONRSLS() in src/snes/impls/vi/rs/virs.c SNESReset_VINEWTONSSLS() in src/snes/impls/vi/ss/viss.c SNESReset_VI() in src/snes/impls/vi/vi.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetUp()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESReset(SNES snes)
```

Example 3 (unknown):
```unknown
SNESCreate()
```

Example 4 (unknown):
```unknown
SNESSetFromOptions()
```

---

## SNESSetAlwaysComputesFinalResidual#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetAlwaysComputesFinalResidual/

**Contents:**
- SNESSetAlwaysComputesFinalResidual#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

tells the SNES to always compute the residual (nonlinear function value) at the final solution

snes - the shell SNES

flg - PETSC_TRUE to always compute the residual

Some solvers (such as smoothers in a SNESFAS) do not need the residual computed at the final solution so skip computing it to save time.

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESSolve(), SNESGetAlwaysComputesFinalResidual()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetAlwaysComputesFinalResidual(SNES snes, PetscBool flg)
```

Example 2 (unknown):
```unknown
SNESSolve()
```

Example 3 (unknown):
```unknown
SNESGetAlwaysComputesFinalResidual()
```

---

## SNESSetApplicationContext#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetApplicationContext/

**Contents:**
- SNESSetApplicationContext#
- Synopsis#
- Input Parameters#
- Notes#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the optional user-defined context for the nonlinear solvers.

snes - the SNES context

ctx - the application context

Users can provide a context when constructing the SNES options and then access it inside their function, Jacobian computation, or other evaluation function with SNESGetApplicationContext()

To provide a function that computes the context for you use SNESSetComputeApplicationContext()

This only works when ctx is a Fortran derived type (it cannot be a PetscObject), we recommend writing a Fortran interface definition for this function that tells the Fortran compiler the derived data type that is passed in as the ctx argument. See SNESGetApplicationContext() for an example.

SNES: Nonlinear Solvers, SNES, SNESSetComputeApplicationContext(), SNESGetApplicationContext()

src/snes/interface/snes.c

src/snes/tutorials/ex73f90t.F90 src/snes/tutorials/ex5f90.F90 src/snes/tutorials/ex5f90t.F90 src/snes/tutorials/ex4.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetApplicationContext(SNES snes, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESGetApplicationContext()
```

Example 3 (unknown):
```unknown
SNESSetComputeApplicationContext()
```

Example 4 (unknown):
```unknown
PetscObject
```

---

## SNESSetCheckJacobianDomainError#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetCheckJacobianDomainError/

**Contents:**
- SNESSetCheckJacobianDomainError#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

tells SNESSolve() whether to check if the user called SNESSetJacobianDomainError() to indicate a Jacobian domain error after each Jacobian evaluation.

snes - the SNES context

flg - indicates if or not to check Jacobian domain error after each Jacobian evaluation

By default, it checks for the Jacobian domain error in the debug mode, and does not check it in the optimized mode.

Checks require one extra parallel synchronization for each Jacobian evaluation

SNES: Nonlinear Solvers, SNES, SNESConvergedReason, SNESCreate(), SNESSetFunction(), SNESFunctionFn, SNESSetFunctionDomainError(), SNESGetCheckJacobianDomainError()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
SNESSetJacobianDomainError()
```

Example 3 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetCheckJacobianDomainError(SNES snes, PetscBool flg)
```

Example 4 (unknown):
```unknown
SNESConvergedReason
```

---

## SNESSetComputeApplicationContext#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetComputeApplicationContext/

**Contents:**
- SNESSetComputeApplicationContext#
- Synopsis#
- Input Parameters#
- Calling sequence of compute#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets an optional function to compute a user-defined context for the nonlinear solvers.

Logically Collective; No Fortran Support

snes - the SNES context

compute - function to compute the context

destroy - function to destroy the context, see PetscCtxDestroyFn for the calling sequence

snes - the SNES context

ctx - context to be computed

This routine is useful if you are performing grid sequencing or using SNESFAS and need the appropriate context generated for each level.

Use SNESSetApplicationContext() to see the context immediately

SNES: Nonlinear Solvers, SNESGetApplicationContext(), SNESSetApplicationContext(), PetscCtxDestroyFn

src/snes/interface/snes.c

src/snes/tutorials/ex58.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetComputeApplicationContext(SNES snes, PetscErrorCode (*compute)(SNES snes, PetscCtxRt ctx), PetscCtxDestroyFn *destroy)
```

Example 2 (unknown):
```unknown
PetscCtxDestroyFn
```

Example 3 (unknown):
```unknown
SNESSetApplicationContext()
```

Example 4 (unknown):
```unknown
SNESGetApplicationContext()
```

---

## SNESSetComputeInitialGuess#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetComputeInitialGuess/

**Contents:**
- SNESSetComputeInitialGuess#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets a routine used to compute an initial guess for the nonlinear problem

snes - the SNES context

func - function evaluation routine, see SNESInitialGuessFn for the calling sequence

ctx - [optional] user-defined context for private data for the function evaluation routine (may be NULL)

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESSetFunction(), SNESGetFunction(), SNESComputeFunction(), SNESSetJacobian(), SNESInitialGuessFn

src/snes/interface/snes.c

src/snes/tutorials/ex18.c src/snes/tutorials/ex58.c src/snes/tutorials/ex48.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetComputeInitialGuess(SNES snes, SNESInitialGuessFn *func, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESInitialGuessFn
```

Example 3 (unknown):
```unknown
SNESSolve()
```

Example 4 (unknown):
```unknown
SNESSetFunction()
```

---

## SNESSetConvergedReason#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetConvergedReason/

**Contents:**
- SNESSetConvergedReason#
- Synopsis#
- Input Parameters#
- Developer Note#
- See Also#
- Level#
- Location#

Sets the reason the SNES iteration was stopped.

snes - the SNES context

reason - negative value indicates diverged, positive value converged, see SNESConvergedReason or the manual pages for the individual convergence tests for complete lists

Called inside the various SNESSolve() implementations

SNES: Nonlinear Solvers, SNESGetConvergedReason(), SNESSetConvergenceTest(), SNESConvergedReason

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetConvergedReason(SNES snes, SNESConvergedReason reason)
```

Example 2 (unknown):
```unknown
SNESConvergedReason
```

Example 3 (unknown):
```unknown
SNESSolve()
```

Example 4 (unknown):
```unknown
SNESGetConvergedReason()
```

---

## SNESSetConvergenceHistory#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetConvergenceHistory/

**Contents:**
- SNESSetConvergenceHistory#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the arrays used to hold the convergence history.

snes - iterative context obtained from SNESCreate()

a - array to hold history, this array will contain the function norms computed at each step

its - integer array holds the number of linear iterations for each solve.

na - size of a and its

reset - PETSC_TRUE indicates each new nonlinear solve resets the history counter to zero, else it continues storing new values for new nonlinear solves after the old ones

If ‘a’ and ‘its’ are NULL then space is allocated for the history. If ‘na’ is PETSC_DECIDE (or, deprecated, PETSC_DEFAULT) then a default array of length 1,000 is allocated.

This routine is useful, e.g., when running a code for purposes of accurate performance monitoring, when no I/O should be done during the section of code that is being timed.

If the arrays run out of space after a number of iterations then the later values are not saved in the history

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESGetConvergenceHistory()

src/snes/interface/snes.c

src/snes/tutorials/ex1f.F90

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetConvergenceHistory(SNES snes, PetscReal a[], PetscInt its[], PetscInt na, PetscBool reset)
```

Example 2 (unknown):
```unknown
SNESCreate()
```

Example 3 (unknown):
```unknown
PETSC_DECIDE
```

Example 4 (unknown):
```unknown
PETSC_DEFAULT
```

---

## SNESSetConvergenceTest#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetConvergenceTest/

**Contents:**
- SNESSetConvergenceTest#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

Sets the function that is to be used to test for convergence of the nonlinear iterative solution.

snes - the SNES context

func - routine to test for convergence

ctx - [optional] context for private data for the convergence routine (may be NULL)

destroy - [optional] destructor for the context (may be NULL; PETSC_NULL_FUNCTION in Fortran)

snes - the SNES context

it - the current iteration number

xnorm - the norm of the new solution

snorm - the norm of the step

fnorm - the norm of the function value

reason - output, the reason convergence or divergence as declared

ctx - the optional convergence test context

SNES: Nonlinear Solvers, SNES, SNESConvergedDefault(), SNESConvergedSkip()

src/snes/interface/snes.c

src/snes/tutorials/ex30.c src/snes/tutorials/ex69.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetConvergenceTest(SNES snes, PetscErrorCode (*func)(SNES snes, PetscInt it, PetscReal xnorm, PetscReal snorm, PetscReal fnorm, SNESConvergedReason *reason, PetscCtx ctx), PetscCtx ctx, PetscCtxDestroyFn *destroy)
```

Example 2 (unknown):
```unknown
PETSC_NULL_FUNCTION
```

Example 3 (unknown):
```unknown
SNESConvergedDefault()
```

Example 4 (unknown):
```unknown
SNESConvergedSkip()
```

---

## SNESSetCountersReset#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetCountersReset/

**Contents:**
- SNESSetCountersReset#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets whether or not the counters for linear iterations and function evaluations are reset every time SNESSolve() is called.

reset - whether to reset the counters or not, defaults to PETSC_TRUE

SNES: Nonlinear Solvers, SNESGetNumberFunctionEvals(), SNESGetLinearSolveIterations(), SNESGetNPC()

src/snes/interface/snes.c

src/snes/tutorials/ex5.c src/snes/tutorials/ex55.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetCountersReset(SNES snes, PetscBool reset)
```

Example 3 (unknown):
```unknown
SNESGetNumberFunctionEvals()
```

Example 4 (unknown):
```unknown
SNESGetLinearSolveIterations()
```

---

## SNESSetDivergenceTolerance#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetDivergenceTolerance/

**Contents:**
- SNESSetDivergenceTolerance#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- Fortran Note#
- See Also#
- Level#
- Location#

Sets the divergence tolerance used for the SNES divergence test.

snes - the SNES context

divtol - the divergence tolerance. Use PETSC_UNLIMITED to deactivate the test. If the residual norm \( F(x^n) \ge divtol * F(x^0) \) the solver is stopped due to divergence.

-snes_divergence_tolerance divtol - Sets divtol

Use PETSC_DETERMINE to use the default value from when the object’s type was set.

Use ``PETSC_DETERMINE_REALorPETSC_UNLIMITED_REAL`

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESSetTolerances(), SNESGetDivergenceTolerance()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetDivergenceTolerance(SNES snes, PetscReal divtol)
```

Example 2 (unknown):
```unknown
PETSC_UNLIMITED
```

Example 3 (unknown):
```unknown
PETSC_DETERMINE
```

Example 4 (unknown):
```unknown
SNESSolve()
```

---

## SNESSetDM#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetDM/

**Contents:**
- SNESSetDM#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the DM that may be used by some SNES nonlinear solvers or their underlying preconditioners

snes - the nonlinear solver context

dm - the DM, cannot be NULL

A DM can only be used for solving one problem at a time because information about the problem is stored on the DM, even when not using interfaces like DMSNESSetFunction(). Use DMClone() to get a distinct DM when solving different problems using the same function space.

SNES: Nonlinear Solvers, DM, SNES, SNESGetDM(), KSPSetDM(), KSPGetDM()

src/snes/interface/snes.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex14.c src/snes/tutorials/ex18.c src/snes/tutorials/ex15.c src/snes/tutorials/ex35.c src/snes/tutorials/ex40f90.F90 src/snes/tutorials/ex12.c src/snes/tutorials/ex17.c src/snes/tutorials/ex33.c src/snes/tutorials/ex23.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetDM(SNES snes, DM dm)
```

Example 2 (unknown):
```unknown
DMSNESSetFunction()
```

Example 3 (unknown):
```unknown
SNESGetDM()
```

---

## SNESSetErrorIfNotConverged#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetErrorIfNotConverged/

**Contents:**
- SNESSetErrorIfNotConverged#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Causes SNESSolve() to generate an error immediately if the solver has not converged.

snes - iterative context obtained from SNESCreate()

flg - PETSC_TRUE indicates you want the error generated

-snes_error_if_not_converged (true|false) - cause an immediate error condition and stop the program if the solver does not converge

Normally PETSc continues if a solver fails to converge, you can call SNESGetConvergedReason() after a SNESSolve() to determine if it has converged. Otherwise the solution may be inaccurate or wrong

SNES: Nonlinear Solvers, SNES, SNESGetErrorIfNotConverged(), KSPGetErrorIfNotConverged(), KSPSetErrorIfNotConverged()

src/snes/interface/snes.c

src/ts/tutorials/ex30.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetErrorIfNotConverged(SNES snes, PetscBool flg)
```

Example 3 (unknown):
```unknown
SNESCreate()
```

Example 4 (unknown):
```unknown
SNESGetConvergedReason()
```

---

## SNESSetForceIteration#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetForceIteration/

**Contents:**
- SNESSetForceIteration#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

force SNESSolve() to take at least one iteration regardless of the initial residual norm

snes - the SNES context

force - PETSC_TRUE require at least one iteration

-snes_force_iteration force - Sets forcing an iteration

This is used sometimes with TS to prevent TS from detecting a false steady state solution

SNES: Nonlinear Solvers, SNES, TS, SNESSetDivergenceTolerance()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetForceIteration(SNES snes, PetscBool force)
```

Example 3 (unknown):
```unknown
SNESSetDivergenceTolerance()
```

---

## SNESSetFromOptions#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetFromOptions/

**Contents:**
- SNESSetFromOptions#
- Synopsis#
- Input Parameter#
- Options Database Keys#
- Options Database Keys for Eisenstat-Walker method#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets various SNES and KSP parameters from user options.

snes - the SNES context

-snes_type type - newtonls, newtontr, ngmres, ncg, nrichardson, qn, vi, fas, SNESType for complete list

-snes_rtol rtol - relative decrease in tolerance norm from initial

-snes_atol abstol - absolute tolerance of residual norm

-snes_stol stol - convergence tolerance in terms of the norm of the change in the solution between steps

-snes_divergence_tolerance divtol - if the residual goes above divtol*rnorm0, exit with divergence

-snes_max_it max_it - maximum number of iterations

-snes_max_funcs max_funcs - maximum number of function evaluations

-snes_force_iteration force - force SNESSolve() to take at least one iteration

-snes_max_fail max_fail - maximum number of line search failures allowed before stopping, default is none

-snes_max_linear_solve_fail - number of linear solver failures before SNESSolve() stops

-snes_lag_preconditioner lag - how often preconditioner is rebuilt (use -1 to never rebuild)

-snes_lag_preconditioner_persists (true|false) - retains the -snes_lag_preconditioner information across multiple SNESSolve()

-snes_lag_jacobian lag - how often Jacobian is rebuilt (use -1 to never rebuild)

-snes_lag_jacobian_persists (true|false) - retains the -snes_lag_jacobian information across multiple SNESSolve()

-snes_convergence_test (default|skip|correct_pressure) - convergence test in nonlinear solver. default SNESConvergedDefault(). skip SNESConvergedSkip() means continue iterating until max_it or some other criterion is reached, saving expense of convergence test. correct_pressure SNESConvergedCorrectPressure() has special handling of a pressure null space.

-snes_monitor [ascii][:filename][:viewer format] - prints residual norm at each iteration. if no filename given prints to stdout

-snes_monitor_solution [ascii binary draw][:filename][:viewer format] - plots solution at each iteration

-snes_monitor_residual [ascii binary draw][:filename][:viewer format] - plots residual (not its norm) at each iteration

-snes_monitor_solution_update [ascii binary draw][:filename][:viewer format] - plots update to solution at each iteration

-snes_monitor draw::draw_lg - plots residual norm at each iteration

-snes_monitor_lg_range - plots function range at each iteration

-snes_monitor_pause_final - Pauses all monitor drawing after the solver ends

-snes_fd - use finite differences to compute Jacobian; very slow, only for testing

-snes_fd_color - use finite differences with coloring to compute Jacobian

-snes_mf_ksp_monitor - if using matrix-free multiply then print h at each KSP iteration

-snes_converged_reason - print the reason for convergence/divergence after each solve

-npc_snes_type type - the SNES type to use as a nonlinear preconditioner

-snes_test_jacobian [threshold] - compare the user provided Jacobian with one computed via finite differences to check for errors. If a threshold is given, display only those entries whose difference is greater than the threshold.

-snes_test_jacobian_view - display the user provided Jacobian, the finite difference Jacobian and the difference between them to help users detect the location of errors in the user provided Jacobian.

-snes_ksp_ew - use Eisenstat-Walker method for determining linear system convergence

-snes_ksp_ew_version ver - version of Eisenstat-Walker method

-snes_ksp_ew_rtol0 rtol0 - Sets rtol0

-snes_ksp_ew_rtolmax rtolmax - Sets rtolmax

-snes_ksp_ew_gamma gamma - Sets gamma

-snes_ksp_ew_alpha alpha - Sets alpha

-snes_ksp_ew_alpha2 alpha2 - Sets alpha2

-snes_ksp_ew_threshold threshold - Sets threshold

To see all options, run your program with the -help option or consult the users manual

SNES supports three approaches for computing (approximate) Jacobians: user provided via SNESSetJacobian(), matrix-free using MatCreateSNESMF(), and computing explicitly with finite differences and coloring using MatFDColoring. It is also possible to use automatic differentiation and the MatFDColoring object.

SNES: Nonlinear Solvers, SNESType, SNESSetOptionsPrefix(), SNESResetFromOptions(), SNES, SNESCreate(), MatCreateSNESMF(), MatFDColoring

src/snes/interface/snes.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex99.c src/snes/tutorials/ex1.c src/snes/tutorials/ex14.c src/snes/tutorials/ex35.c src/snes/tutorials/ex40f90.F90 src/snes/tutorials/ex17.c src/snes/tutorials/ex33.c src/snes/tutorials/ex23.c src/snes/tutorials/ex21.c

SNESSetFromOptions_NEWTONAL() in src/snes/impls/al/al.c SNESSetFromOptions_Composite() in src/snes/impls/composite/snescomposite.c SNESSetFromOptions_FAS() in src/snes/impls/fas/fas.c SNESSetFromOptions_NGS() in src/snes/impls/gs/snesgs.c SNESSetFromOptions_MS() in src/snes/impls/ms/ms.c SNESSetFromOptions_Multiblock() in src/snes/impls/multiblock/multiblock.c SNESSetFromOptions_NASM() in src/snes/impls/nasm/nasm.c SNESSetFromOptions_NCG() in src/snes/impls/ncg/snesncg.c SNESSetFromOptions_Anderson() in src/snes/impls/ngmres/anderson.c SNESSetFromOptions_NGMRES() in src/snes/impls/ngmres/snesngmres.c SNESSetFromOptions_NEWTONTRDC() in src/snes/impls/ntrdc/ntrdc.c SNESSetFromOptions_Patch() in src/snes/impls/patch/snespatch.c SNESSetFromOptions_QN() in src/snes/impls/qn/qn.c SNESSetFromOptions_NRichardson() in src/snes/impls/richardson/snesrichardson.c SNESSetFromOptions_NEWTONTR() in src/snes/impls/tr/tr.c SNESSetFromOptions_VINEWTONSSLS() in src/snes/impls/vi/ss/viss.c SNESSetFromOptions_VI() in src/snes/impls/vi/vi.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetFromOptions(SNES snes)
```

Example 2 (unknown):
```unknown
SNESSolve()
```

Example 3 (unknown):
```unknown
SNESConvergedDefault()
```

Example 4 (unknown):
```unknown
SNESConvergedSkip()
```

---

## SNESSetFunctionDomainError#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetFunctionDomainError/

**Contents:**
- SNESSetFunctionDomainError#
- Synopsis#
- Input Parameter#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

tells SNES that the input vector, a proposed new solution, to your function you provided to SNESSetFunction() is not in the function’s domain. For example, a step with negative pressure.

snes - the SNES context

This does not need to be called by all processes in the SNES MPI communicator.

A few solvers will try to cut the step size to avoid the domain error but for other solvers SNESSolve() stops iterating and returns with a SNESConvergedReason of SNES_DIVERGED_FUNCTION_DOMAIN

You can direct SNES to avoid certain steps by using SNESVISetVariableBounds(), SNESVISetComputeVariableBounds() or SNESLineSearchSetPreCheck(), SNESLineSearchSetPostCheck()

You should always call SNESGetConvergedReason() after each SNESSolve() and verify if the iteration converged (positive result) or diverged (negative result).

You can call SNESSetJacobianDomainError() during a Jacobian computation to indicate the proposed solution is not in the domain.

This value is used by SNESCheckFunctionDomainError() to determine if the SNESConvergedReason is set to SNES_DIVERGED_FUNCTION_DOMAIN

SNES: Nonlinear Solvers, SNESCreate(), SNESSetFunction(), SNESFunctionFn, SNESSetJacobianDomainError(), SNESVISetVariableBounds(), SNESVISetComputeVariableBounds(), SNESLineSearchSetPreCheck(), SNESLineSearchSetPostCheck(), SNESConvergedReason, SNESGetConvergedReason(), SNES_DIVERGED_FUNCTION_DOMAIN, SNESSetObjectiveDomainError(), SNES_DIVERGED_OBJECTIVE_DOMAIN

src/snes/interface/snes.c

src/ts/tutorials/ex30.c src/ts/tutorials/ex10.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetFunction()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetFunctionDomainError(SNES snes)
```

Example 3 (unknown):
```unknown
SNESSolve()
```

Example 4 (unknown):
```unknown
SNESConvergedReason
```

---

## SNESSetFunctionNorm#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetFunctionNorm/

**Contents:**
- SNESSetFunctionNorm#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the last computed residual norm.

snes - the SNES context

norm - the value of the norm

SNES: Nonlinear Solvers, SNES, SNESGetNormSchedule(), SNESComputeFunction(), VecNorm(), SNESSetFunction(), SNESSetInitialFunction(), SNESNormSchedule

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetFunctionNorm(SNES snes, PetscReal norm)
```

Example 2 (unknown):
```unknown
SNESGetNormSchedule()
```

Example 3 (unknown):
```unknown
SNESComputeFunction()
```

Example 4 (unknown):
```unknown
SNESSetFunction()
```

---

## SNESSetFunctionType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetFunctionType/

**Contents:**
- SNESSetFunctionType#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the SNESFunctionType of the SNES method.

snes - the SNES context

type - the function type

Values of the function type:

SNES_FUNCTION_DEFAULT - the default for the given SNESType

SNES_FUNCTION_UNPRECONDITIONED - an unpreconditioned function evaluation (this is the function provided with SNESSetFunction()

SNES_FUNCTION_PRECONDITIONED - a transformation of the function provided with SNESSetFunction()

Different SNESTypes use this value in different ways

SNES: Nonlinear Solvers, SNES, SNESFunctionType, SNESGetNormSchedule(), SNESComputeFunction(), VecNorm(), SNESSetFunction(), SNESSetInitialFunction(), SNESNormSchedule

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESFunctionType
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetFunctionType(SNES snes, SNESFunctionType type)
```

Example 3 (unknown):
```unknown
SNES_FUNCTION_DEFAULT
```

Example 4 (unknown):
```unknown
SNES_FUNCTION_UNPRECONDITIONED
```

---

## SNESSetFunction#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetFunction/

**Contents:**
- SNESSetFunction#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the function evaluation routine and function vector for use by the SNES routines in solving systems of nonlinear equations.

snes - the SNES context

r - vector to store function values, may be NULL

f - function evaluation routine; for calling sequence see SNESFunctionFn

ctx - [optional] user-defined context for private data for the function evaluation routine (may be NULL)

SNES: Nonlinear Solvers, SNES, SNESGetFunction(), SNESComputeFunction(), SNESSetJacobian(), SNESSetPicard(), SNESFunctionFn

src/snes/interface/snes.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex99.c src/snes/tutorials/ex1.c src/snes/tutorials/ex6.c src/snes/tutorials/ex14.c src/snes/tutorials/ex18.c src/snes/tutorials/ex35.c src/snes/tutorials/ex22.c src/snes/tutorials/ex15.c src/snes/tutorials/ex21.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetFunction(SNES snes, Vec r, SNESFunctionFn *f, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESFunctionFn
```

Example 3 (unknown):
```unknown
SNESGetFunction()
```

Example 4 (unknown):
```unknown
SNESComputeFunction()
```

---

## SNESSetGridSequence#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetGridSequence/

**Contents:**
- SNESSetGridSequence#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

sets the number of steps of grid sequencing that SNES will do

snes - the SNES context

steps - the number of refinements to do, defaults to 0

-snes_grid_sequence steps - Use grid sequencing to generate initial guess

Once grid sequencing is turned on SNESSolve() will automatically perform the solve on each grid refinement.

Use SNESGetSolution() to extract the fine grid solution after grid sequencing.

SNES: Nonlinear Solvers, SNES, SNESGetLagPreconditioner(), SNESSetLagJacobian(), SNESGetLagJacobian(), SNESGetGridSequence(), SNESSetDM(), SNESSolve()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetGridSequence(SNES snes, PetscInt steps)
```

Example 2 (unknown):
```unknown
SNESSolve()
```

Example 3 (unknown):
```unknown
SNESGetSolution()
```

Example 4 (unknown):
```unknown
SNESGetLagPreconditioner()
```

---

## SNESSetInitialFunction#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetInitialFunction/

**Contents:**
- SNESSetInitialFunction#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Set an already computed function evaluation at the initial guess to be reused by SNESSolve().

snes - the SNES context

f - vector to store function value

This should not be modified during the solution procedure.

This is used extensively in the SNESFAS hierarchy and in nonlinear preconditioning.

SNES: Nonlinear Solvers, SNES, SNESFAS, SNESSetFunction(), SNESComputeFunction(), SNESSetInitialFunctionNorm()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetInitialFunction(SNES snes, Vec f)
```

Example 3 (unknown):
```unknown
SNESSetFunction()
```

Example 4 (unknown):
```unknown
SNESComputeFunction()
```

---

## SNESSetIterationNumber#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetIterationNumber/

**Contents:**
- SNESSetIterationNumber#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the current iteration number.

iter - iteration number

This should only be called inside a SNES nonlinear solver.

SNES: Nonlinear Solvers, SNESGetLinearSolveIterations()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetIterationNumber(SNES snes, PetscInt iter)
```

Example 2 (unknown):
```unknown
SNESGetLinearSolveIterations()
```

---

## SNESSetJacobianDomainError#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetJacobianDomainError/

**Contents:**
- SNESSetJacobianDomainError#
- Synopsis#
- Input Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

tells SNES that the function you provided to SNESSetJacobian() at the proposed step. For example there is a negative element transformation.

snes - the SNES context

If this is called the SNESSolve() stops iterating and returns with a SNESConvergedReason of SNES_DIVERGED_JACOBIAN_DOMAIN

You should always call SNESGetConvergedReason() after each SNESSolve() and verify if the iteration converged (positive result) or diverged (negative result).

You can direct SNES to avoid certain steps by using SNESVISetVariableBounds(), SNESVISetComputeVariableBounds() or SNESLineSearchSetPreCheck(), SNESLineSearchSetPostCheck()

SNES: Nonlinear Solvers, SNESCreate(), SNESSetFunction(), SNESFunctionFn, SNESSetFunctionDomainError(), SNESVISetVariableBounds(), SNESVISetComputeVariableBounds(), SNESLineSearchSetPreCheck(), SNESLineSearchSetPostCheck(), SNESConvergedReason, SNESGetConvergedReason()

src/snes/interface/snes.c

src/snes/tutorials/ex3.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetJacobian()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetJacobianDomainError(SNES snes)
```

Example 3 (unknown):
```unknown
SNESSolve()
```

Example 4 (unknown):
```unknown
SNESConvergedReason
```

---

## SNESSetJacobian#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetJacobian/

**Contents:**
- SNESSetJacobian#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the function to compute Jacobian as well as the location to store the matrix.

snes - the SNES context

Amat - the matrix that defines the (approximate) Jacobian

Pmat - the matrix to be used in constructing the preconditioner, usually the same as Amat.

J - Jacobian evaluation routine (if NULL then SNES retains any previously set value), see SNESJacobianFn for details

ctx - [optional] user-defined context for private data for the Jacobian evaluation routine (may be NULL) (if NULL then SNES retains any previously set value)

If the Amat matrix and Pmat matrix are different you must call MatAssemblyBegin()/MatAssemblyEnd() on each matrix.

If you know the operator Amat has a null space you can use MatSetNullSpace() and MatSetTransposeNullSpace() to supply the null space to Amat and the KSP solvers will automatically use that null space as needed during the solution process.

If using SNESComputeJacobianDefaultColor() to assemble a Jacobian, the ctx argument must be a MatFDColoring.

Other defect-correction schemes can be used by computing a different matrix in place of the Jacobian. One common example is to use the “Picard linearization” which only differentiates through the highest order parts of each term using SNESSetPicard()

SNES: Nonlinear Solvers, SNES, KSPSetOperators(), SNESSetFunction(), MatMFFDComputeJacobian(), SNESComputeJacobianDefaultColor(), MatStructure, SNESSetPicard(), SNESJacobianFn, SNESFunctionFn

src/snes/interface/snes.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex99.c src/snes/tutorials/ex1.c src/snes/tutorials/ex6.c src/snes/tutorials/ex14.c src/snes/tutorials/ex18.c src/snes/tutorials/ex35.c src/snes/tutorials/ex12.c src/snes/tutorials/ex15.c src/snes/tutorials/ex22.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetJacobian(SNES snes, Mat Amat, Mat Pmat, SNESJacobianFn *J, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESJacobianFn
```

Example 3 (unknown):
```unknown
MatAssemblyBegin()
```

Example 4 (unknown):
```unknown
MatAssemblyEnd()
```

---

## SNESSetKSP#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetKSP/

**Contents:**
- SNESSetKSP#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Sets a KSP context for the SNES object to use

Not Collective, but the SNES and KSP objects must live on the same MPI_Comm

snes - the SNES context

ksp - the KSP context

The SNES object already has its KSP object, you can obtain with SNESGetKSP() so this routine is rarely needed.

The KSP object that is already in the SNES object has its reference count decreased by one when this is called.

SNES: Nonlinear Solvers, SNES, KSP, KSPGetPC(), SNESCreate(), KSPCreate()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetKSP(SNES snes, KSP ksp)
```

Example 2 (unknown):
```unknown
SNESGetKSP()
```

Example 3 (unknown):
```unknown
SNESCreate()
```

Example 4 (unknown):
```unknown
KSPCreate()
```

---

## SNESSetLagJacobianPersists#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetLagJacobianPersists/

**Contents:**
- SNESSetLagJacobianPersists#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#

Set whether or not the Jacobian lagging persists through multiple nonlinear solves

snes - the SNES context

flg - jacobian lagging persists if true

-snes_lag_jacobian_persists (true|false) - sets the persistence through multiple SNES solves

-snes_lag_jacobian (- 2|1|2|…) - sets the lag

-snes_lag_preconditioner_persists (true|false) - sets the persistence through multiple SNES solves

-snes_lag_preconditioner (- 2|1|2|…) - sets the lag

Normally when SNESSetLagJacobian() is used, the Jacobian is always rebuilt at the beginning of each new nonlinear solve, this removes that behavior

This is useful both for nonlinear preconditioning, where it’s appropriate to have the Jacobian be stale by several solves, and for implicit time-stepping, where Jacobian lagging in the inner nonlinear solve over several timesteps may present huge efficiency gains.

SNES: Nonlinear Solvers, SNES, SNESSetLagPreconditionerPersists(), SNESSetLagJacobian(), SNESGetLagJacobian(), SNESGetNPC()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetLagJacobianPersists(SNES snes, PetscBool flg)
```

Example 2 (unknown):
```unknown
SNESSetLagJacobian()
```

Example 3 (unknown):
```unknown
SNESSetLagPreconditionerPersists()
```

Example 4 (unknown):
```unknown
SNESSetLagJacobian()
```

---

## SNESSetLagJacobian#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetLagJacobian/

**Contents:**
- SNESSetLagJacobian#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#

Set when the Jacobian is rebuilt in the nonlinear solve. See SNESSetLagPreconditioner() for determining how often the preconditioner is rebuilt.

snes - the SNES context

lag - -1 indicates NEVER rebuild, 1 means rebuild every time the Jacobian is computed within a single nonlinear solve, 2 means every second time the Jacobian is built etc. -2 means rebuild at next chance but then never again

-snes_lag_jacobian_persists (true|false) - sets the persistence through multiple SNES solves

-snes_lag_jacobian (- 2|1|2|…) - sets the lag

-snes_lag_preconditioner_persists (true|false) - sets the persistence through multiple SNES solves

-snes_lag_preconditioner (- 2|1|2|…) - sets the lag.

The Jacobian is ALWAYS built in the first iteration of a nonlinear solve unless lag is -1

If -1 is used before the very first nonlinear solve the CODE WILL FAIL! because no Jacobian is used, use -2 to indicate you want it recomputed at the next Newton step but never again (unless it is reset to another value)

SNES: Nonlinear Solvers, SNES, SNESGetLagPreconditioner(), SNESSetLagPreconditioner(), SNESGetLagJacobianPersists(), SNESSetLagPreconditionerPersists()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetLagPreconditioner()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetLagJacobian(SNES snes, PetscInt lag)
```

Example 3 (unknown):
```unknown
SNESGetLagPreconditioner()
```

Example 4 (unknown):
```unknown
SNESSetLagPreconditioner()
```

---

## SNESSetLineSearch#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetLineSearch/

**Contents:**
- SNESSetLineSearch#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the SNESLineSearch to be used for a given SNES

snes - iterative context obtained from SNESCreate()

linesearch - the linesearch object

This is almost never used, rather one uses SNESGetLineSearch() to retrieve the line search and set options on it to configure it using the API).

SNES: Nonlinear Solvers, SNES, SNESLineSearch, SNESGetLineSearch()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESLineSearch
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetLineSearch(SNES snes, SNESLineSearch linesearch)
```

Example 3 (unknown):
```unknown
SNESCreate()
```

Example 4 (unknown):
```unknown
SNESGetLineSearch()
```

---

## SNESSetMaxLinearSolveFailures#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetMaxLinearSolveFailures/

**Contents:**
- SNESSetMaxLinearSolveFailures#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

the number of failed linear solve attempts allowed before SNES returns with a diverged reason of SNES_DIVERGED_LINEAR_SOLVE

maxFails - maximum allowed linear solve failures, use PETSC_UNLIMITED to have no limit on the number of failures

-snes_max_linear_solve_fail num - The number of failures before the solve is terminated

By default this is 0; that is SNES returns on the first failed linear solve

The options database key is wrong for this function name

SNES: Nonlinear Solvers, SNESSetErrorIfNotConverged(), SNESGetLinearSolveFailures(), SNESGetMaxLinearSolveFailures(), SNESGetLinearSolveIterations()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNES_DIVERGED_LINEAR_SOLVE
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetMaxLinearSolveFailures(SNES snes, PetscInt maxFails)
```

Example 3 (unknown):
```unknown
PETSC_UNLIMITED
```

Example 4 (unknown):
```unknown
SNESSetErrorIfNotConverged()
```

---

## SNESSetMaxNonlinearStepFailures#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetMaxNonlinearStepFailures/

**Contents:**
- SNESSetMaxNonlinearStepFailures#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

Sets the maximum number of unsuccessful steps attempted by the nonlinear solver before it gives up and returns unconverged or generates an error

maxFails - maximum of unsuccessful steps allowed, use PETSC_UNLIMITED to have no limit on the number of failures

-snes_max_fail n - maximum number of unsuccessful steps allowed

A failed step is a step that was generated and taken but did not satisfy the requested criteria. For example, the SNESLineSearchApply() could not generate a sufficient decrease in the function norm (in fact it may have produced an increase).

Taken steps that produce a infinity or NaN in the function evaluation or generate a SNESSetFunctionDomainError() will always immediately terminate the SNESSolve() regardless of the value of maxFails.

The options database key is wrong for this function name

SNES: Nonlinear Solvers, SNESSetErrorIfNotConverged(), SNESGetMaxLinearSolveFailures(), SNESGetLinearSolveIterations(), SNESSetMaxLinearSolveFailures(), SNESGetLinearSolveFailures(), SNESGetMaxNonlinearStepFailures(), SNESGetNonlinearStepFailures(), SNESCheckLineSearchFailure()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetMaxNonlinearStepFailures(SNES snes, PetscInt maxFails)
```

Example 2 (unknown):
```unknown
PETSC_UNLIMITED
```

Example 3 (unknown):
```unknown
SNESLineSearchApply()
```

Example 4 (unknown):
```unknown
SNESSetFunctionDomainError()
```

---

## SNESSetNGS#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetNGS/

**Contents:**
- SNESSetNGS#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the user nonlinear Gauss-Seidel routine for use with composed nonlinear solvers.

snes - the SNES context, usually of the SNESType SNESNGS

f - function evaluation routine to apply Gauss-Seidel, see SNESNGSFn for calling sequence

ctx - [optional] user-defined context for private data for the smoother evaluation routine (may be NULL)

The SNESNGS routines are used by the composed nonlinear solver to generate a problem appropriate update to the solution, particularly SNESFAS.

SNES: Nonlinear Solvers, SNESNGS, SNESGetNGS(), SNESNCG, SNESGetFunction(), SNESComputeNGS(), SNESNGSFn

src/snes/interface/snes.c

src/snes/tutorials/ex15.c src/snes/tutorials/ex5.c src/snes/tutorials/ex19.c src/snes/tutorials/ex55.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetNGS(SNES snes, SNESNGSFn *f, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESGetNGS()
```

Example 3 (unknown):
```unknown
SNESGetFunction()
```

Example 4 (unknown):
```unknown
SNESComputeNGS()
```

---

## SNESSetNormSchedule#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetNormSchedule/

**Contents:**
- SNESSetNormSchedule#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Sets the SNESNormSchedule used in convergence and monitoring of the SNES method, when norms are computed in the solving process

snes - the SNES context

normschedule - the frequency of norm computation

-snes_norm_schedule (none|always|initialonly|finalonly|initialfinalonly) - set the schedule

Only certain SNES methods support certain SNESNormSchedules. Most require evaluation of the nonlinear function and the taking of its norm at every iteration to even ensure convergence at all. However, methods such as custom Gauss-Seidel methods SNESNGS and the like do not require the norm of the function to be computed, and therefore may either be monitored for convergence or not. As these are often used as nonlinear preconditioners, monitoring the norm of their error is not a useful enterprise within their solution.

SNES: Nonlinear Solvers, SNESNormSchedule, SNESGetNormSchedule(), SNESComputeFunction(), VecNorm(), SNESSetFunction(), SNESSetInitialFunction()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESNormSchedule
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetNormSchedule(SNES snes, SNESNormSchedule normschedule)
```

Example 3 (unknown):
```unknown
SNESNormSchedules
```

Example 4 (unknown):
```unknown
SNESNormSchedule
```

---

## SNESSetNPCSide#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetNPCSide/

**Contents:**
- SNESSetNPCSide#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Sets the nonlinear preconditioning side used by the nonlinear preconditioner inside SNES.

snes - iterative context obtained from SNESCreate()

side - the preconditioning side, where side is one of

-snes_npc_side (right|left) - nonlinear preconditioner side

SNESNRICHARDSON and SNESNCG only support left preconditioning.

SNES: Nonlinear Solvers, SNES, SNESGetNPC(), SNESNRICHARDSON, SNESNCG, SNESType, SNESGetNPCSide(), KSPSetPCSide(), PC_LEFT, PC_RIGHT, PCSide

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetNPCSide(SNES snes, PCSide side)
```

Example 2 (unknown):
```unknown
SNESCreate()
```

Example 3 (unknown):
```unknown
PC_LEFT  - left preconditioning
      PC_RIGHT - right preconditioning (default for most nonlinear solvers)
```

Example 4 (unknown):
```unknown
SNESNRICHARDSON
```

---

## SNESSetNPC#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetNPC/

**Contents:**
- SNESSetNPC#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Sets the nonlinear preconditioner to be used.

snes - iterative context obtained from SNESCreate()

npc - the SNES nonlinear preconditioner object

-npc_snes_type type - set the type of the SNES to use as the nonlinear preconditioner

This is rarely used, rather use SNESGetNPC() to retrieve the preconditioner and configure it using the API.

Only some SNESType can use a nonlinear preconditioner

SNES: Nonlinear Solvers, SNES, SNESNGS, SNESFAS, SNESGetNPC(), SNESHasNPC()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetNPC(SNES snes, SNES npc)
```

Example 2 (unknown):
```unknown
SNESCreate()
```

Example 3 (unknown):
```unknown
SNESGetNPC()
```

Example 4 (unknown):
```unknown
SNESGetNPC()
```

---

## SNESSetObjectiveDomainError#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetObjectiveDomainError/

**Contents:**
- SNESSetObjectiveDomainError#
- Synopsis#
- Input Parameter#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#

tells SNES that the input vector, a proposed new solution, to your function you provided to SNESSetObjective() is not in the function’s domain. For example, a step with negative pressure.

snes - the SNES context

This does not need to be called by all processes in the SNES MPI communicator.

A few solvers will try to cut the step size to avoid the domain error but for other solvers SNESSolve() stops iterating and returns with a SNESConvergedReason of SNES_DIVERGED_OBJECTIVE_DOMAIN

You can direct SNES to avoid certain steps by using SNESVISetVariableBounds(), SNESVISetComputeVariableBounds() or SNESLineSearchSetPreCheck(), SNESLineSearchSetPostCheck()

You should always call SNESGetConvergedReason() after each SNESSolve() and verify if the iteration converged (positive result) or diverged (negative result).

You can call SNESSetJacobianDomainError() during a Jacobian computation to indicate the proposed solution is not in the domain.

This value is used by SNESCheckObjectiveDomainError() to determine if the SNESConvergedReason is set to SNES_DIVERGED_OBJECTIVE_DOMAIN

SNES: Nonlinear Solvers, SNESCreate(), SNESSetFunction(), SNESFunctionFn, SNESSetJacobianDomainError(), SNESVISetVariableBounds(), SNESVISetComputeVariableBounds(), SNESLineSearchSetPreCheck(), SNESLineSearchSetPostCheck(), SNESConvergedReason, SNESGetConvergedReason(), SNES_DIVERGED_OBJECTIVE_DOMAIN, SNESSetFunctionDomainError(), SNES_DIVERGED_FUNCTION_DOMAIN

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetObjective()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetObjectiveDomainError(SNES snes)
```

Example 3 (unknown):
```unknown
SNESSolve()
```

Example 4 (unknown):
```unknown
SNESConvergedReason
```

---

## SNESSetObjective#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetObjective/

**Contents:**
- SNESSetObjective#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the objective function minimized by some of the SNES linesearch methods, used instead of the 2-norm of the residual in the line search

snes - the SNES context

obj - objective evaluation routine; see SNESObjectiveFn for the calling sequence

ctx - [optional] user-defined context for private data for the objective evaluation routine (may be NULL)

Some of the SNESLineSearch methods attempt to minimize a given objective provided by this function to determine a step length.

If not provided then this defaults to the two-norm of the function evaluation (set with SNESSetFunction())

This is not used in the SNESLINESEARCHCP line search.

SNES: Nonlinear Solvers, SNES, SNESLineSearch(), SNESGetObjective(), SNESComputeObjective(), SNESSetFunction(), SNESSetJacobian(), SNESObjectiveFn, SNESSetObjectiveDomainError()

src/snes/interface/snesob.c

src/snes/tutorials/ex73f90t.F90

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESSetObjective(SNES snes, SNESObjectiveFn *obj, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESObjectiveFn
```

Example 3 (unknown):
```unknown
SNESLineSearch
```

Example 4 (unknown):
```unknown
SNESSetFunction()
```

---

## SNESSetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetOptionsPrefix/

**Contents:**
- SNESSetOptionsPrefix#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the prefix used for searching for all SNES options in the database.

snes - the SNES context

prefix - the prefix to prepend to all option names

A hyphen (-) must NOT be given at the beginning of the prefix name. The first character of all runtime options is AUTOMATICALLY the hyphen.

SNES: Nonlinear Solvers, SNES, SNESSetFromOptions(), SNESAppendOptionsPrefix()

src/snes/interface/snes.c

src/snes/tutorials/ex27.c src/ts/utils/dmplexlandau/tutorials/ex1f90.F90 src/ts/tutorials/ex30.c src/snes/tutorials/ex1.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetOptionsPrefix(SNES snes, const char prefix[])
```

Example 2 (unknown):
```unknown
SNESSetFromOptions()
```

Example 3 (unknown):
```unknown
SNESAppendOptionsPrefix()
```

---

## SNESSetPicard#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetPicard/

**Contents:**
- SNESSetPicard#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Use SNES to solve the system \(A(x) x = bp(x) + b \) via a Picard type iteration (Picard linearization)

snes - the SNES context

r - vector to store function values, may be NULL

bp - function evaluation routine, may be NULL, for the calling sequence see SNESFunctionFn

Amat - matrix with which \(A(x) x - bp(x) - b\) is to be computed

Pmat - matrix from which preconditioner is computed (usually the same as Amat)

J - function to compute matrix values, for the calling sequence see SNESJacobianFn

ctx - [optional] user-defined context for private data for the function evaluation routine (may be NULL)

It is often better to provide the nonlinear function \(F()\) and some approximation to its Jacobian directly and use an approximate Newton solver. This interface is provided to allow porting/testing a previous Picard based code in PETSc before converting it to approximate Newton.

One can call SNESSetPicard() or SNESSetFunction() (and possibly SNESSetJacobian()) but cannot call both

Solves the equation \(A(x) x = bp(x) - b\) via the defect correction algorithm \(A(x^{n}) (x^{n+1} - x^{n}) = bp(x^{n}) + b - A(x^{n})x^{n}\). When an exact solver is used this corresponds to the “classic” Picard \(A(x^{n}) x^{n+1} = bp(x^{n}) + b\) iteration.

Run with -snes_mf_operator to solve the system with Newton’s method using \(A(x^{n})\) to construct the preconditioner.

We implement the defect correction form of the Picard iteration because it converges much more generally when inexact linear solvers are used then the direct Picard iteration \(A(x^n) x^{n+1} = bp(x^n) + b\)

There is some controversity over the definition of a Picard iteration for nonlinear systems but almost everyone agrees that it involves a linear solve and some believe it is the iteration \(A(x^{n}) x^{n+1} = b(x^{n})\) hence we use the name Picard. If anyone has an authoritative reference that defines the Picard iteration different please contact us at petsc-dev@mcs.anl.gov and we’ll have an entirely new argument :-).

When used with -snes_mf_operator this will run matrix-free Newton’s method where the matrix-vector product is of the true Jacobian of \(A(x)x - bp(x) - b\) and \(A(x^{n})\) is used to build the preconditioner

When used with -snes_fd this will compute the true Jacobian (very slowly one column at a time) and thus represent Newton’s method.

When used with -snes_fd_coloring this will compute the Jacobian via coloring and thus represent a faster implementation of Newton’s method. But the the nonzero structure of the Jacobian is, in general larger than that of the Picard matrix \(A\) so you must provide in \(A\) the needed nonzero structure for the correct coloring. When using DMDA this may mean creating the matrix \(A\) with DMCreateMatrix() using a wider stencil than strictly needed for \(A\) or with a DMDA_STENCIL_BOX. See the comment in src/snes/tutorials/ex15.c.

SNES: Nonlinear Solvers, SNES, SNESGetFunction(), SNESSetFunction(), SNESComputeFunction(), SNESSetJacobian(), SNESGetPicard(), SNESLineSearchPreCheckPicard(), SNESFunctionFn, SNESJacobianFn

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetPicard(SNES snes, Vec r, SNESFunctionFn *bp, Mat Amat, Mat Pmat, SNESJacobianFn *J, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESFunctionFn
```

Example 3 (unknown):
```unknown
SNESJacobianFn
```

Example 4 (unknown):
```unknown
SNESSetPicard()
```

---

## SNESSetSolution#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetSolution/

**Contents:**
- SNESSetSolution#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the solution vector for use by the SNES routines.

snes - the SNES context obtained from SNESCreate()

u - the solution vector

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESGetSolution(), Vec

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetSolution(SNES snes, Vec u)
```

Example 2 (unknown):
```unknown
SNESCreate()
```

Example 3 (unknown):
```unknown
SNESSolve()
```

Example 4 (unknown):
```unknown
SNESGetSolution()
```

---

## SNESSetTolerances#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetTolerances/

**Contents:**
- SNESSetTolerances#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Note#
- Fortran Note#
- See Also#
- Level#
- Location#

Sets various parameters used in SNES convergence tests.

snes - the SNES context

abstol - the absolute convergence tolerance, \( F(x^n) \le abstol \)

rtol - the relative convergence tolerance, \( F(x^n) \le reltol * F(x^0) \)

stol - convergence tolerance in terms of the norm of the change in the solution between steps, || delta x || < stol*|| x ||

maxit - the maximum number of iterations allowed in the solver, default 50.

maxf - the maximum number of function evaluations allowed in the solver (use PETSC_UNLIMITED indicates no limit), default 10,000

-snes_atol abstol - Sets abstol

-snes_rtol rtol - Sets rtol

-snes_stol stol - Sets stol

-snes_max_it maxit - Sets maxit

-snes_max_funcs maxf - Sets maxf (use unlimited to have no maximum)

All parameters must be non-negative

Use PETSC_CURRENT to retain the current value of any parameter and PETSC_DETERMINE to use the default value for the given SNES. The default value is the value in the object when its type is set.

Use PETSC_UNLIMITED on maxit or maxf to indicate there is no bound on the number of iterations or number of function evaluations.

Use PETSC_CURRENT_INTEGER, PETSC_CURRENT_REAL, PETSC_UNLIMITED_INTEGER, PETSC_DETERMINE_INTEGER, or PETSC_DETERMINE_REAL

SNES: Nonlinear Solvers, SNESSolve(), SNES, SNESSetDivergenceTolerance(), SNESSetForceIteration()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetTolerances(SNES snes, PetscReal abstol, PetscReal rtol, PetscReal stol, PetscInt maxit, PetscInt maxf)
```

Example 2 (unknown):
```unknown
PETSC_UNLIMITED
```

Example 3 (unknown):
```unknown
PETSC_CURRENT
```

Example 4 (unknown):
```unknown
PETSC_DETERMINE
```

---

## SNESSetTrustRegionTolerance#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetTrustRegionTolerance/

**Contents:**
- SNESSetTrustRegionTolerance#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the trust region parameter tolerance.

snes - the SNES context

SNES: Nonlinear Solvers, SNES, SNESNEWTONTR, SNESSetTolerances()

src/snes/impls/tr/tr.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESSetTrustRegionTolerance(SNES snes, PetscReal tol)
```

Example 2 (unknown):
```unknown
SNESNEWTONTR
```

Example 3 (unknown):
```unknown
SNESSetTolerances()
```

---

## SNESSetType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetType/

**Contents:**
- SNESSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the algorithm/method to be used to solve the nonlinear system with the given SNES

snes - the SNES context

type - a known method

-snes_type type - Sets the method; see SNESType

See SNESType for available methods (for instance)

SNESNEWTONLS - Newton’s method with line search (systems of nonlinear equations)

SNESNEWTONTR - Newton’s method with trust region (systems of nonlinear equations)

Normally, it is best to use the SNESSetFromOptions() command and then set the SNES solver type from the options database rather than by using this routine. Using the options database provides the user with maximum flexibility in evaluating the many nonlinear solvers. The SNESSetType() routine is provided for those situations where it is necessary to set the nonlinear solver independently of the command line or options database. This might be the case, for example, when the choice of solver changes during the execution of the program, and the user’s application is taking responsibility for choosing the appropriate method.

SNESRegister() adds a constructor for a new SNESType to SNESList, SNESSetType() locates the constructor in that list and calls it to create the specific object.

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESType, SNESCreate(), SNESDestroy(), SNESGetType(), SNESSetFromOptions()

src/snes/interface/snes.c

src/snes/tutorials/ex11.c src/snes/tutorials/ex1.c src/snes/tutorials/ex9.c src/snes/tutorials/ex35.c src/snes/tutorials/ex64.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetType(SNES snes, SNESType type)
```

Example 2 (unknown):
```unknown
SNESNEWTONLS
```

Example 3 (unknown):
```unknown
SNESNEWTONTR
```

Example 4 (unknown):
```unknown
SNESSetFromOptions()
```

---

## SNESSetUpdate#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetUpdate/

**Contents:**
- SNESSetUpdate#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Sets the general-purpose update function called at the beginning of every iteration of the nonlinear solve. Specifically it is called just before the Jacobian is “evaluated” and after the function evaluation.

snes - The nonlinear solver context

func - The update function; for calling sequence see SNESUpdateFn

This is NOT what one uses to update the ghost points before a function evaluation, that should be done at the beginning of your function provided to SNESSetFunction(), or SNESSetPicard() This is not used by most users, and it is intended to provide a general hook that is run right before the direction step is computed.

Users are free to modify the current residual vector, the current linearization point, or any other vector associated to the specific solver used. If such modifications take place, it is the user responsibility to update all the relevant vectors. For example, if one is adjusting the model parameters at each Newton step their code may look like

There are a variety of function hooks one many set that are called at different stages of the nonlinear solution process, see the functions listed below.

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESSetJacobian(), SNESLineSearchSetPreCheck(), SNESLineSearchSetPostCheck(), SNESNewtonTRSetPreCheck(), SNESNewtonTRSetPostCheck(), SNESMonitorSet()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetUpdate(SNES snes, SNESUpdateFn *func)
```

Example 2 (unknown):
```unknown
SNESUpdateFn
```

Example 3 (unknown):
```unknown
SNESSetFunction()
```

Example 4 (unknown):
```unknown
SNESSetPicard()
```

---

## SNESSetUpMatrices#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetUpMatrices/

**Contents:**
- SNESSetUpMatrices#
- Synopsis#
- Input Parameter#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

ensures that matrices are available for SNES Newton-like methods, this is called by SNESSetUp_XXX()

snes - SNES object to configure

If the matrices do not yet exist it attempts to create them based on options previously set for the SNES such as -snes_mf

The functionality of this routine overlaps in a confusing way with the functionality of SNESSetUpMatrixFree_Private() which is called by SNESSetUp() but sometimes SNESSetUpMatrices() is called without SNESSetUp() being called. A refactorization to simplify the logic that handles the matrix-free case is desirable.

SNES: Nonlinear Solvers, SNES, SNESSetUp()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetUp_XXX()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetUpMatrices(SNES snes)
```

Example 3 (unknown):
```unknown
SNESSetUpMatrixFree_Private()
```

Example 4 (unknown):
```unknown
SNESSetUp()
```

---

## SNESSetUp#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetUp/

**Contents:**
- SNESSetUp#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets up the internal data structures for the later use of a nonlinear solver SNESSolve().

snes - the SNES context

For basic use of the SNES solvers the user does not need to explicitly call SNESSetUp(), since these actions will automatically occur during the call to SNESSolve(). However, if one wishes to control this phase separately, SNESSetUp() should be called after SNESCreate() and optional routines of the form SNESSetXXX(), but before SNESSolve().

SNES: Nonlinear Solvers, SNES, SNESCreate(), SNESSolve(), SNESDestroy(), SNESSetFromOptions()

src/snes/interface/snes.c

src/ts/tutorials/ex30.c src/snes/tutorials/ex69.c src/snes/tutorials/ex62.c

SNESSetUp_NEWTONAL() in src/snes/impls/al/al.c SNESSetUp_Composite() in src/snes/impls/composite/snescomposite.c SNESSetUp_FAS() in src/snes/impls/fas/fas.c SNESSetUp_NGS() in src/snes/impls/gs/snesgs.c SNESSetUp_KSPONLY() in src/snes/impls/ksponly/ksponly.c SNESSetUp_NEWTONLS() in src/snes/impls/ls/ls.c SNESSetUp_MS() in src/snes/impls/ms/ms.c SNESSetUp_Multiblock() in src/snes/impls/multiblock/multiblock.c SNESSetUp_NASM() in src/snes/impls/nasm/nasm.c SNESSetUp_NCG() in src/snes/impls/ncg/snesncg.c SNESSetUp_NGMRES() in src/snes/impls/ngmres/snesngmres.c SNESSetUp_NEWTONTRDC() in src/snes/impls/ntrdc/ntrdc.c SNESSetUp_Patch() in src/snes/impls/patch/snespatch.c SNESSetUp_QN() in src/snes/impls/qn/qn.c SNESSetUp_NRichardson() in src/snes/impls/richardson/snesrichardson.c SNESSetUp_NEWTONTR() in src/snes/impls/tr/tr.c SNESSetUp_VINEWTONRSLS() in src/snes/impls/vi/rs/virs.c SNESSetUp_VINEWTONSSLS() in src/snes/impls/vi/ss/viss.c SNESSetUp_VI() in src/snes/impls/vi/vi.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetUp(SNES snes)
```

Example 3 (unknown):
```unknown
SNESSetUp()
```

Example 4 (unknown):
```unknown
SNESSolve()
```

---

## SNESSetUseMatrixFree#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetUseMatrixFree/

**Contents:**
- SNESSetUseMatrixFree#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#

indicates that SNES should use matrix-free finite difference matrix-vector products to apply the Jacobian.

mf_operator - use matrix-free only for the Amat used by SNESSetJacobian(), this means the user provided Pmat will continue to be used

mf - use matrix-free for both the Amat and Pmat used by SNESSetJacobian(), both the Amat and Pmat set in SNESSetJacobian() will be ignored. With this option no matrix-element based preconditioners can be used in the linear solve since the matrix won’t be explicitly available

-snes_mf_operator - use matrix-free only for the mat operator

-snes_mf - use matrix-free for both the mat and pmat operator

-snes_fd_color - compute the Jacobian via coloring and finite differences.

-snes_fd - compute the Jacobian via finite differences (slow)

SNES supports three approaches for computing (approximate) Jacobians: user provided via SNESSetJacobian(), matrix-free using MatCreateSNESMF(), and computing explicitly with finite differences and coloring using MatFDColoring. It is also possible to use automatic differentiation and the MatFDColoring object.

SNES: Nonlinear Solvers, SNES, SNESGetUseMatrixFree(), MatCreateSNESMF(), SNESComputeJacobianDefaultColor(), MatFDColoring

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSetUseMatrixFree(SNES snes, PetscBool mf_operator, PetscBool mf)
```

Example 2 (unknown):
```unknown
SNESSetJacobian()
```

Example 3 (unknown):
```unknown
SNESSetJacobian()
```

Example 4 (unknown):
```unknown
SNESSetJacobian()
```

---

## SNESSetWorkVecs#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSetWorkVecs/

**Contents:**
- SNESSetWorkVecs#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Allocates a number of work vectors to be used internally by the SNES solver

snes - the SNES context

nw - number of work vectors to allocate

Each SNESType calls this with the number of work vectors that particular type needs.

SNES: Nonlinear Solvers, SNES

src/snes/interface/snesut.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsc/private/snesimpl.h"   
PetscErrorCode SNESSetWorkVecs(SNES snes, PetscInt nw)
```

---

## SNESShellGetContext#

**URL:** https://petsc.org/release/manualpages/SNES/SNESShellGetContext/

**Contents:**
- SNESShellGetContext#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Fortran Notes#
- See Also#
- Level#
- Location#
- Examples#

Returns the user-provided context associated with a SNESSHELL

snes - should have been created with SNESSetType(snes,SNESSHELL);

ctx - the user provided context

This only works when the context is a Fortran derived type or a PetscObject. Declare ctx with

SNES: Nonlinear Solvers, SNES, SNESSHELL, SNESCreateShell(), SNESShellSetContext()

src/snes/impls/shell/snesshell.c

src/snes/tutorials/ex35.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESShellGetContext(SNES snes, PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
SNESSetType
```

Example 3 (unknown):
```unknown
PetscObject
```

Example 4 (julia):
```julia
type(tUsertype), pointer :: ctx
```

---

## SNESShellSetContext#

**URL:** https://petsc.org/release/manualpages/SNES/SNESShellSetContext/

**Contents:**
- SNESShellSetContext#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

sets the context for a SNESSHELL

SNES: Nonlinear Solvers, SNES, SNESSHELL, SNESCreateShell(), SNESShellGetContext()

src/snes/impls/shell/snesshell.c

src/snes/tutorials/ex35.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESShellSetContext(SNES snes, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESCreateShell()
```

Example 3 (unknown):
```unknown
SNESShellGetContext()
```

---

## SNESShellSetSolve#

**URL:** https://petsc.org/release/manualpages/SNES/SNESShellSetSolve/

**Contents:**
- SNESShellSetSolve#
- Synopsis#
- Input Parameters#
- Calling sequence of apply#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets routine to apply as solver to a SNESSHELL SNES object

snes - the SNES nonlinear solver context

solve - the application-provided solver routine

snes - the preconditioner, get the application context with SNESShellGetContext() provided with SNESShellSetContext()

xout - solution vector

SNES: Nonlinear Solvers, SNES, SNESSHELL, SNESShellSetContext(), SNESShellGetContext()

src/snes/impls/shell/snesshell.c

src/snes/tutorials/ex35.c

SNESShellSetSolve_Shell(SNES snes, PetscErrorCode (*solve)() in src/snes/impls/shell/snesshell.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"   
PetscErrorCode SNESShellSetSolve(SNES snes, PetscErrorCode (*solve)(SNES snes, Vec xout))
```

Example 2 (unknown):
```unknown
SNESShellGetContext()
```

Example 3 (unknown):
```unknown
SNESShellSetContext()
```

Example 4 (unknown):
```unknown
SNESShellSetContext()
```

---

## SNESSHELL#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSHELL/

**Contents:**
- SNESSHELL#
- See Also#
- Level#
- Location#
- Examples#

a user provided nonlinear solver

SNES: Nonlinear Solvers, SNESCreate(), SNES, SNESSetType(), SNESType, SNESShellGetContext(), SNESShellSetContext(), SNESShellSetSolve()

src/snes/impls/shell/snesshell.c

src/snes/tutorials/ex35.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESCreate()
```

Example 2 (unknown):
```unknown
SNESSetType()
```

Example 3 (unknown):
```unknown
SNESShellGetContext()
```

Example 4 (unknown):
```unknown
SNESShellSetContext()
```

---

## SNESSolve#

**URL:** https://petsc.org/release/manualpages/SNES/SNESSolve/

**Contents:**
- SNESSolve#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Solves a nonlinear system \(F(x) = b \) associated with a SNES object

snes - the SNES context

b - the constant part of the equation \(F(x) = b\), or NULL to use zero.

x - the solution vector.

The user should initialize the vector, x, with the initial guess for the nonlinear solve prior to calling SNESSolve() .

SNES: Nonlinear Solvers, SNES, SNESCreate(), SNESDestroy(), SNESSetFunction(), SNESSetJacobian(), SNESSetGridSequence(), SNESGetSolution(), SNESNewtonTRSetPreCheck(), SNESNewtonTRGetPreCheck(), SNESNewtonTRSetPostCheck(), SNESNewtonTRGetPostCheck(), SNESLineSearchSetPostCheck(), SNESLineSearchGetPostCheck(), SNESLineSearchSetPreCheck(), SNESLineSearchGetPreCheck()

src/snes/interface/snes.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex99.c src/snes/tutorials/ex1.c src/snes/tutorials/ex14.c src/snes/tutorials/ex35.c src/snes/tutorials/ex40f90.F90 src/snes/tutorials/ex17.c src/snes/tutorials/ex33.c src/snes/tutorials/ex23.c src/snes/tutorials/ex21.c

SNESSolve_NEWTONAL() in src/snes/impls/al/al.c SNESSolve_Composite() in src/snes/impls/composite/snescomposite.c SNESSolve_FAS() in src/snes/impls/fas/fas.c SNESSolve_NGS() in src/snes/impls/gs/snesgs.c SNESSolve_KSPONLY() in src/snes/impls/ksponly/ksponly.c SNESSolve_NEWTONLS() in src/snes/impls/ls/ls.c SNESSolve_MS() in src/snes/impls/ms/ms.c SNESSolve_Multiblock() in src/snes/impls/multiblock/multiblock.c SNESSolve_NASM() in src/snes/impls/nasm/nasm.c SNESSolve_NCG() in src/snes/impls/ncg/snesncg.c SNESSolve_Anderson() in src/snes/impls/ngmres/anderson.c SNESSolve_NGMRES() in src/snes/impls/ngmres/snesngmres.c SNESSolve_NEWTONTRDC() in src/snes/impls/ntrdc/ntrdc.c SNESSolve_Patch() in src/snes/impls/patch/snespatch.c SNESSolve_QN() in src/snes/impls/qn/qn.c SNESSolve_NRichardson() in src/snes/impls/richardson/snesrichardson.c SNESSolve_Shell() in src/snes/impls/shell/snesshell.c SNESSolve_NEWTONTR() in src/snes/impls/tr/tr.c SNESSolve_VINEWTONRSLS() in src/snes/impls/vi/rs/virs.c SNESSolve_VINEWTONSSLS() in src/snes/impls/vi/ss/viss.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESSolve(SNES snes, Vec b, Vec x)
```

Example 2 (unknown):
```unknown
SNESSolve()
```

Example 3 (unknown):
```unknown
SNESCreate()
```

Example 4 (unknown):
```unknown
SNESDestroy()
```

---

## SNESTestFunction#

**URL:** https://petsc.org/release/manualpages/SNES/SNESTestFunction/

**Contents:**
- SNESTestFunction#
- Synopsis#
- Input Parameter#
- Options Database Keys#
- See Also#
- Level#
- Location#

Computes the difference between the computed and finite-difference functions

snes - the SNES context

-snes_test_function - compare the user provided function with one compute via finite differences to check for errors.

-snes_test_function_view - display the user provided function, the finite difference function and the difference

SNES: Nonlinear Solvers, SNESTestJacobian(), SNESSetFunction(), SNESComputeFunction()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESTestFunction(SNES snes)
```

Example 2 (unknown):
```unknown
SNESTestJacobian()
```

Example 3 (unknown):
```unknown
SNESSetFunction()
```

Example 4 (unknown):
```unknown
SNESComputeFunction()
```

---

## SNESTestJacobian#

**URL:** https://petsc.org/release/manualpages/SNES/SNESTestJacobian/

**Contents:**
- SNESTestJacobian#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#

Computes the difference between the computed and finite-difference Jacobians

snes - the SNES context

Jnorm - the Frobenius norm of the computed Jacobian, or NULL

diffNorm - the Frobenius norm of the difference of the computed and finite-difference Jacobians, or NULL

-snes_test_jacobian [threshold] - compare the user provided Jacobian with one compute via finite differences to check for errors. If a threshold is given, display only those entries whose difference is greater than the threshold.

-snes_test_jacobian_view - display the user provided Jacobian, the finite difference Jacobian and the difference

Directions and norms are printed to stdout if diffNorm is NULL.

SNES: Nonlinear Solvers, SNESTestFunction(), SNESSetJacobian(), SNESComputeJacobian()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESTestJacobian(SNES snes, PetscReal *Jnorm, PetscReal *diffNorm)
```

Example 2 (unknown):
```unknown
SNESTestFunction()
```

Example 3 (unknown):
```unknown
SNESSetJacobian()
```

Example 4 (unknown):
```unknown
SNESComputeJacobian()
```

---

## SNESTestLocalMin#

**URL:** https://petsc.org/release/manualpages/SNES/SNESTestLocalMin/

**Contents:**
- SNESTestLocalMin#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#

Diagnostic that probes each entry of the current SNES solution to check whether the residual norm has a local minimum along the coordinate directions

snes - the SNES context

Currently intended for serial runs. For each degree of freedom it perturbs the solution by increasing amounts and prints the resulting SNESComputeFunction() residual norms so the user can inspect local behavior.

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESComputeFunction()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESTestLocalMin(SNES snes)
```

Example 2 (unknown):
```unknown
SNESComputeFunction()
```

Example 3 (unknown):
```unknown
SNESSolve()
```

Example 4 (unknown):
```unknown
SNESComputeFunction()
```

---

## SNESType#

**URL:** https://petsc.org/release/manualpages/SNES/SNESType/

**Contents:**
- SNESType#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#
- Examples#

String with the name of a PETSc SNES method. These are all the nonlinear solvers that PETSc provides.

Use SNESSetType() or the options database key -snes_type to set the specific nonlinear solver algorithm to use with a given SNES object

Summary of Nonlinear Solvers Available In PETSc, SNES: Nonlinear Solvers, SNESSetType(), SNES, SNESCreate(), SNESDestroy(), SNESSetFromOptions()

src/snes/tutorials/ex3.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef const char *SNESType;
#define SNESNEWTONLS         "newtonls"
#define SNESNEWTONTR         "newtontr"
#define SNESNEWTONTRDC       "newtontrdc"
#define SNESPYTHON           "python"
#define SNESNRICHARDSON      "nrichardson"
#define SNESKSPONLY          "ksponly"
#define SNESKSPTRANSPOSEONLY "ksptransposeonly"
#define SNESVINEWTONRSLS     "vinewtonrsls"
#define SNESVINEWTONSSLS     "vinewtonssls"
#define SNESNGMRES           "ngmres"
#define SNESQN               "qn"
#define SNESSHELL            "shell"
#define SNESNGS              "ngs"
#define SNESNCG              "ncg"
#define SNESFAS              "fas"
#define SNESMS               "ms"
#define SNESNASM             "nasm"
#define SNESANDERSON         "anderson"
#define SNESASPIN            "aspin"
#define SNESCOMPOSITE        "composite"
#define SNESPATCH            "patch"
#define SNESNEWTONAL         "newtonal"
```

Example 2 (unknown):
```unknown
SNESSetType()
```

Example 3 (unknown):
```unknown
SNESSetType()
```

Example 4 (unknown):
```unknown
SNESCreate()
```

---

## SNESUpdateFn#

**URL:** https://petsc.org/release/manualpages/SNES/SNESUpdateFn/

**Contents:**
- SNESUpdateFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

A prototype of a SNES update function that would be passed to SNESSetUpdate()

step - the current iteration index

SNES: Nonlinear Solvers, SNES, SNESSetUpdate()

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetUpdate()
```

Example 2 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode SNESUpdateFn(SNES snes, PetscInt step);
```

Example 3 (unknown):
```unknown
SNESSetUpdate()
```

---

## SNESVIComputeFunction#

**URL:** https://petsc.org/release/manualpages/SNES/SNESVIComputeFunction/

**Contents:**
- SNESVIComputeFunction#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Provides the function that reformulates a system of nonlinear equations in mixed complementarity form to a system of nonlinear equations in semismooth form.

snes - the SNES context

functx - user defined function context

phi - the evaluation of semismooth function at X

SNES: Nonlinear Solvers, SNES, SNESVINEWTONSSLS, SNESVIComputeMeritFunction()

src/snes/impls/vi/ss/viss.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESVIComputeFunction(SNES snes, Vec X, Vec phi, void *functx)
```

Example 2 (unknown):
```unknown
SNESVINEWTONSSLS
```

Example 3 (unknown):
```unknown
SNESVIComputeMeritFunction()
```

---

## SNESVIComputeInactiveSetFnorm#

**URL:** https://petsc.org/release/manualpages/SNES/SNESVIComputeInactiveSetFnorm/

**Contents:**
- SNESVIComputeInactiveSetFnorm#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Computes the function norm for variational inequalities on the inactive set

snes - the SNES context

F - the nonlinear function vector

X - the SNES solution vector

fnorm - the function norm

See SNESVINEWTONRSLS for a concise description of the active and inactive sets

SNES: Nonlinear Solvers, SNES, SNESVINEWTONRSLS, SNESVINEWTONSSLS, SNESLineSearchSetVIFunctions()

src/snes/impls/vi/vi.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESVIComputeInactiveSetFnorm(SNES snes, Vec F, Vec X, PetscReal *fnorm)
```

Example 2 (unknown):
```unknown
SNESVINEWTONRSLS
```

Example 3 (unknown):
```unknown
SNESVINEWTONRSLS
```

Example 4 (unknown):
```unknown
SNESVINEWTONSSLS
```

---

## SNESVIComputeInactiveSetFtY#

**URL:** https://petsc.org/release/manualpages/SNES/SNESVIComputeInactiveSetFtY/

**Contents:**
- SNESVIComputeInactiveSetFtY#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Computes the directional derivative for variational inequalities on the inactive set, assuming that there exists some \(G(x)\) for which the SNESFunctionFn \(F(x) = grad G(x)\) (relevant for some line search algorithms)

snes - the SNES context

F - the nonlinear function vector

X - the SNES solution vector

Y - the direction vector

fty - the directional derivative

See SNESVINEWTONRSLS for a concise description of the active and inactive sets

SNES: Nonlinear Solvers, SNES, SNESVINEWTONRSLS, SNESVINEWTONSSLS

src/snes/impls/vi/vi.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESFunctionFn
```

Example 2 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESVIComputeInactiveSetFtY(SNES snes, Vec F, Vec X, Vec Y, PetscScalar *fty)
```

Example 3 (unknown):
```unknown
SNESVINEWTONRSLS
```

Example 4 (unknown):
```unknown
SNESVINEWTONRSLS
```

---

## SNESVIComputeMeritFunction#

**URL:** https://petsc.org/release/manualpages/SNES/SNESVIComputeMeritFunction/

**Contents:**
- SNESVIComputeMeritFunction#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Evaluates the merit function for the mixed complementarity problem.

phi - the Vec holding the evaluation of the semismooth function

merit - the merit function 1/2 ||phi||^2

phinorm - the two-norm of the vector, ||phi||

SNES: Nonlinear Solvers, SNES, SNESVINEWTONSSLS, SNESVIComputeFunction()

src/snes/impls/vi/ss/viss.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESVIComputeMeritFunction(Vec phi, PetscReal *merit, PetscReal *phinorm)
```

Example 2 (unknown):
```unknown
SNESVINEWTONSSLS
```

Example 3 (unknown):
```unknown
SNESVIComputeFunction()
```

---

## SNESViewFromOptions#

**URL:** https://petsc.org/release/manualpages/SNES/SNESViewFromOptions/

**Contents:**
- SNESViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

View a SNES based on values in the options database

obj - Optional object that provides the options prefix for the checks

name - command line option

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

SNES: Nonlinear Solvers, SNES, SNESView, PetscObjectViewFromOptions(), SNESCreate()

src/snes/interface/snes.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESViewFromOptions(SNES A, PetscObject obj, const char name[])
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
SNESCreate()
```

---

## SNESView#

**URL:** https://petsc.org/release/manualpages/SNES/SNESView/

**Contents:**
- SNESView#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Prints or visualizes the SNES data structure.

snes - the SNES context

viewer - the PetscViewer

-snes_view - Calls SNESView() at end of SNESSolve()

The available visualization contexts include

PETSC_VIEWER_STDOUT_SELF - standard output (default)

PETSC_VIEWER_STDOUT_WORLD - synchronized standard output where only the first processor opens the file. All other processors send their data to the first processor to print.

The available formats include

PETSC_VIEWER_DEFAULT - standard output (default)

PETSC_VIEWER_ASCII_INFO_DETAIL - more verbose output for SNESNASM

The user can open an alternative visualization context with PetscViewerASCIIOpen() - output to a specified file.

In the debugger you can do “call SNESView(snes,0)” to display the SNES solver. (The same holds for any PETSc object viewer).

SNES: Nonlinear Solvers, SNES, SNESLoad(), SNESCreate(), PetscViewerASCIIOpen()

src/snes/interface/snes.c

SNESView_Composite() in src/snes/impls/composite/snescomposite.c SNESView_FAS() in src/snes/impls/fas/fas.c SNESView_NGS() in src/snes/impls/gs/snesgs.c SNESView_MS() in src/snes/impls/ms/ms.c SNESView_Multiblock() in src/snes/impls/multiblock/multiblock.c SNESView_NASM() in src/snes/impls/nasm/nasm.c SNESView_NCG() in src/snes/impls/ncg/snesncg.c SNESView_NGMRES() in src/snes/impls/ngmres/snesngmres.c SNESView_NEWTONTRDC() in src/snes/impls/ntrdc/ntrdc.c SNESView_Patch() in src/snes/impls/patch/snespatch.c SNESView_QN() in src/snes/impls/qn/qn.c SNESView_NEWTONTR() in src/snes/impls/tr/tr.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h"  
#include "petscsnes.h"  
PetscErrorCode SNESView(SNES snes, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
SNESSolve()
```

Example 4 (unknown):
```unknown
PETSC_VIEWER_STDOUT_SELF
```

---

## SNESVIGetActiveSetIS#

**URL:** https://petsc.org/release/manualpages/SNES/SNESVIGetActiveSetIS/

**Contents:**
- SNESVIGetActiveSetIS#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the global indices for the active set variables

snes - the SNES context

X - the snes solution vector

F - the nonlinear function vector

ISact - active set index set

See SNESVINEWTONRSLS for a concise description of the active and inactive sets

SNES: Nonlinear Solvers, SNES, SNESVINEWTONRSLS, SNESVINEWTONSSLS

src/snes/impls/vi/vi.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESVIGetActiveSetIS(SNES snes, Vec X, Vec F, IS *ISact)
```

Example 2 (unknown):
```unknown
SNESVINEWTONRSLS
```

Example 3 (unknown):
```unknown
SNESVINEWTONRSLS
```

Example 4 (unknown):
```unknown
SNESVINEWTONSSLS
```

---

## SNESVIGetInactiveSet#

**URL:** https://petsc.org/release/manualpages/SNES/SNESVIGetInactiveSet/

**Contents:**
- SNESVIGetInactiveSet#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the global indices for the inactive set variables (these correspond to the degrees of freedom the linear system is solved on)

snes - the SNES context

inact - inactive set index set

See SNESVINEWTONRSLS for a concise description of the active and inactive sets

SNES: Nonlinear Solvers, SNES, SNESVINEWTONRSLS

src/snes/impls/vi/rs/virs.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESVIGetInactiveSet(SNES snes, IS *inact)
```

Example 2 (unknown):
```unknown
SNESVINEWTONRSLS
```

Example 3 (unknown):
```unknown
SNESVINEWTONRSLS
```

---

## SNESVIGetVariableBounds#

**URL:** https://petsc.org/release/manualpages/SNES/SNESVIGetVariableBounds/

**Contents:**
- SNESVIGetVariableBounds#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Gets the lower and upper bounds for the solution vector. xl <= x <= xu. These are used in solving (differential) variable inequalities.

snes - the SNES context.

xl - lower bound (may be NULL)

xu - upper bound (may be NULL)

These vectors are owned by the SNESVI and should not be destroyed by the caller

Variational Inequalities, SNES, SNESVISetVariableBounds(), SNESVISetComputeVariableBounds(), SNESSetFunctionDomainError(), SNESSetJacobianDomainError(), SNESVINEWTONRSLS, SNESVINEWTONSSLS, SNESSetType(), PETSC_NINFINITY, PETSC_INFINITY

src/snes/impls/vi/vi.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESVIGetVariableBounds(SNES snes, Vec *xl, Vec *xu)
```

Example 2 (unknown):
```unknown
SNESVISetVariableBounds()
```

Example 3 (unknown):
```unknown
SNESVISetComputeVariableBounds()
```

Example 4 (unknown):
```unknown
SNESSetFunctionDomainError()
```

---

## SNESVINEWTONRSLS#

**URL:** https://petsc.org/release/manualpages/SNES/SNESVINEWTONRSLS/

**Contents:**
- SNESVINEWTONRSLS#
- Options Database Keys#
- Note#
- References#
- See Also#
- Level#
- Location#
- Examples#

Reduced space active set solvers for variational inequalities based on Newton’s method

-snes_type (vinewtonssls|vinewtonrsls) - A semi-smooth solver or a reduced space active set method

-snes_vi_zero_tolerance - Tolerance for considering \(u_i\) value to be on a bound.

-snes_vi_monitor - Prints the number of active constraints (inactive set points) at each iteration.

-snes_vi_monitor_residual - View the residual vector at each iteration, using zero for active constraints (i.e. the inactive variables).

-snes_vi_monitor_active - View the active set by outputting a one for vector components in the active set and zero for the inactive.

Reduced-space (active set methods) work as follows at each iteration:

The algorithm produces an inactive set of variables, that is a list of variables whose values will not be changed in the current iteration, i.e. they are to be constrained to their current values. These are all the variables that are on the lower bound, that is \(u_i = L_i\) with also \([F(u)]_i \ge 0\) or the upper bound \(u_i = U_i\) with also \([F(u)]_i \le 0.\)

A step direction is obtained by solving the linear system arising from the Jacobian used in Newton’s method but with the inactive variables removed from both the rows and columns.

A line search is then used to update the active variables (the inactive set of variables are not changed).

The inactive set is chosen based on the sign of \([F(u)]_i\) because this gives exactly the set of points that would be moved outside of the domain given an infinitesimal Newton (or even Richardson) step and our goal is to remain within the bounds, that is, to continue to satisfy the inequality constraints.

Steven J Benson and Todd S Munson. Flexible complementarity solvers for large-scale applications. Optimization Methods and Software, 21(1):155–168, 2006.

SNES: Nonlinear Solvers, SNESVISetVariableBounds(), SNESVISetComputeVariableBounds(), SNESCreate(), SNES, SNESSetType(), SNESVINEWTONSSLS, SNESNEWTONTR, SNESLineSearchSetType(), SNESLineSearchSetPostCheck(), SNESLineSearchSetPreCheck(), SNESVIGetInactiveSet(), DMSetVI(), SNESVISetRedundancyCheck()

src/snes/impls/vi/rs/virs.c

src/snes/tutorials/ex9.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESVISetVariableBounds()
```

Example 2 (unknown):
```unknown
SNESVISetComputeVariableBounds()
```

Example 3 (unknown):
```unknown
SNESCreate()
```

Example 4 (unknown):
```unknown
SNESSetType()
```

---

## SNESVINEWTONSSLS#

**URL:** https://petsc.org/release/manualpages/SNES/SNESVINEWTONSSLS/

**Contents:**
- SNESVINEWTONSSLS#
- Options Database Keys#
- Notes#
- References#
- See Also#
- Level#
- Location#

Semi-smooth solver for variational inequalities based on Newton’s method

-snes_type <vinewtonssls,vinewtonrsls> a semi- smooth solver, a reduced space active set method

-snes_vi_monitor - prints the number of active constraints at each iteration.

This family of algorithms is much like an interior point method.

The reduced space active set solvers SNESVINEWTONRSLS provide an alternative approach that does not result in extremely ill-conditioned linear systems

See [MFF+01] and [BM06]

Steven J Benson and Todd S Munson. Flexible complementarity solvers for large-scale applications. Optimization Methods and Software, 21(1):155–168, 2006.

T. S. Munson, F. Facchinei, M. C. Ferris, A. Fischer, and C. Kanzow. The semismooth algorithm for large scale complementarity problems. INFORMS Journal on Computing, 2001.

SNES: Nonlinear Solvers, SNESVINEWTONRSLS, SNESVISetVariableBounds(), SNESVISetComputeVariableBounds(), SNESCreate(), SNES, SNESSetType(), SNESNEWTONTR, SNESLineSearchSetType(), SNESLineSearchSetPostCheck(), SNESLineSearchSetPreCheck()

src/snes/impls/vi/ss/viss.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESVINEWTONRSLS
```

Example 2 (unknown):
```unknown
SNESVINEWTONRSLS
```

Example 3 (unknown):
```unknown
SNESVISetVariableBounds()
```

Example 4 (unknown):
```unknown
SNESVISetComputeVariableBounds()
```

---

## SNESVISetComputeVariableBounds#

**URL:** https://petsc.org/release/manualpages/SNES/SNESVISetComputeVariableBounds/

**Contents:**
- SNESVISetComputeVariableBounds#
- Synopsis#
- Input Parameters#
- Calling sequence of compute#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets a function that is called to compute the bounds on variable for (differential) variable inequalities.

snes - the SNES context

compute - function that computes the bounds

snes - the SNES context

lower - vector to hold lower bounds

higher - vector to hold upper bounds

Problems with bound constraints can be solved with the reduced space, SNESVINEWTONRSLS, and semi-smooth SNESVINEWTONSSLS solvers.

For entries with no bounds you can set PETSC_NINFINITY or PETSC_INFINITY

You may use SNESVISetVariableBounds() to provide the bounds once if they will never change

If you have associated a DM with the SNES and provided a function to the DM via DMSetVariableBounds() that will be used automatically to provide the bounds and you need not use this function.

See SNESVINEWTONRSLS for a concise description of the active and inactive sets

Variational Inequalities, SNES, SNESVISetVariableBounds(), DMSetVariableBounds(), SNESSetFunctionDomainError(), SNESSetJacobianDomainError(), SNESVINEWTONRSLS, SNESVINEWTONSSLS, SNESSetType(), PETSC_NINFINITY, PETSC_INFINITY

src/snes/impls/vi/vi.c

src/snes/tutorials/ex9.c src/snes/tutorials/ex58.c

SNESVISetComputeVariableBounds_VI() in src/snes/impls/vi/vi.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESVISetComputeVariableBounds(SNES snes, PetscErrorCode (*compute)(SNES snes, Vec lower, Vec higher))
```

Example 2 (unknown):
```unknown
SNESVINEWTONRSLS
```

Example 3 (unknown):
```unknown
SNESVINEWTONSSLS
```

Example 4 (unknown):
```unknown
PETSC_NINFINITY
```

---

## SNESVISetRedundancyCheck#

**URL:** https://petsc.org/release/manualpages/SNES/SNESVISetRedundancyCheck/

**Contents:**
- SNESVISetRedundancyCheck#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Note#
- See Also#
- Level#
- Location#

Provide a function to check for any redundancy in the VI active set

snes - the SNESVINEWTONRSLS context

func - the function to check of redundancies

ctx - optional context used by the function

snes - the SNES context

is_act - the set of points in the active sets

is_redact - output, the set of points in the non-redundant active set

ctx - optional context

Sometimes the inactive set will result in a singular sub-Jacobian problem that needs to be solved, this allows the user, when they know more about their specific problem to provide a function that removes the redundancy that results in the singular linear system

See SNESVINEWTONRSLS for a concise description of the active and inactive sets

SNES: Nonlinear Solvers, SNES, SNESVINEWTONRSLS, SNESVIGetInactiveSet(), DMSetVI()

src/snes/impls/vi/rs/virs.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESVISetRedundancyCheck(SNES snes, PetscErrorCode (*func)(SNES snes, IS is_act, IS *is_redact, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESVINEWTONRSLS
```

Example 3 (unknown):
```unknown
SNESVINEWTONRSLS
```

Example 4 (unknown):
```unknown
SNESVINEWTONRSLS
```

---

## SNESVISetVariableBounds#

**URL:** https://petsc.org/release/manualpages/SNES/SNESVISetVariableBounds/

**Contents:**
- SNESVISetVariableBounds#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Sets the lower and upper bounds for the solution vector. xl <= x <= xu. This allows solving (differential) variable inequalities.

snes - the SNES context.

If this routine is not called then the lower and upper bounds are set to PETSC_NINFINITY and PETSC_INFINITY respectively during SNESSetUp().

Problems with bound constraints can be solved with the reduced space, SNESVINEWTONRSLS or semi-smooth SNESVINEWTONSSLS solvers.

For particular components that have no bounds you can use PETSC_NINFINITY or PETSC_INFINITY

SNESVISetComputeVariableBounds() can be used to provide a function that computes the bounds. This should be used if you are using, for example, grid sequencing and need bounds set for a variety of vectors

See SNESVINEWTONRSLS for a concise description of the active and inactive sets

Variational Inequalities, SNES, SNESVIGetVariableBounds(), SNESVISetComputeVariableBounds(), SNESSetFunctionDomainError(), SNESSetJacobianDomainError(), SNESVINEWTONRSLS, SNESVINEWTONSSLS, SNESSetType(), PETSC_NINFINITY, PETSC_INFINITY

src/snes/impls/vi/vi.c

SNESVISetVariableBounds_VI() in src/snes/impls/vi/vi.c

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsnes.h" 
PetscErrorCode SNESVISetVariableBounds(SNES snes, Vec xl, Vec xu)
```

Example 2 (unknown):
```unknown
PETSC_NINFINITY
```

Example 3 (unknown):
```unknown
PETSC_INFINITY
```

Example 4 (unknown):
```unknown
SNESSetUp()
```

---

## SNES#

**URL:** https://petsc.org/release/manualpages/SNES/SNES/

**Contents:**
- SNES#
- Synopsis#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Abstract PETSc object that manages nonlinear solves

The most commonly used SNESType is SNESNEWTONLS which uses Newton’s method with a line search. For all the Newton based SNES nonlinear solvers, KSP, the PETSc abstract linear solver object, is used to (approximately) solve the required linear systems.

See SNESType for a list of all the nonlinear solver algorithms provided by PETSc.

Some of the SNES solvers support nonlinear preconditioners, which themselves are also SNES objects managed with SNESGetNPC()

Summary of Nonlinear Solvers Available In PETSc, SNES: Nonlinear Solvers, SNESCreate(), SNESSolve(), SNESSetType(), SNESType, TS, KSP, PC, SNESDestroy()

include/petscsnestypes.h

src/snes/tutorials/ex28.c src/snes/tutorials/ex99.c src/snes/tutorials/ex1.c src/snes/tutorials/ex14.c src/snes/tutorials/ex35.c src/snes/tutorials/ex40f90.F90 src/snes/tutorials/ex17.c src/snes/tutorials/ex33.c src/snes/tutorials/ex23.c src/snes/tutorials/ex21.c

_p_SNES in include/petsc/private/snesimpl.h SNES_NEWTONAL in src/snes/impls/al/alimpl.h SNES_Composite in src/snes/impls/composite/snescomposite.c SNES_FAS in src/snes/impls/fas/fasimpls.h SNES_NGS in src/snes/impls/gs/gsimpl.h SNES_KSPONLY in src/snes/impls/ksponly/ksponly.c SNES_NEWTONLS in src/snes/impls/ls/lsimpl.h SNES_MS in src/snes/impls/ms/ms.c SNES_Multiblock in src/snes/impls/multiblock/multiblock.c SNES_NASM in src/snes/impls/nasm/nasm.c SNES_NCG in src/snes/impls/ncg/snesncgimpl.h SNES_NGMRES in src/snes/impls/ngmres/snesngmres.h SNES_NEWTONTRDC in src/snes/impls/ntrdc/ntrdcimpl.h SNES_Patch in src/snes/impls/patch/snespatch.c SNES_QN in src/snes/impls/qn/qn.c SNES_NRichardson in src/snes/impls/richardson/snesrichardsonimpl.h SNES_Shell in src/snes/impls/shell/snesshell.c SNES_NEWTONTR in src/snes/impls/tr/trimpl.h SNES_VINEWTONRSLS in src/snes/impls/vi/rs/virsimpl.h SNES_VINEWTONSSLS in src/snes/impls/vi/ss/vissimpl.h

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_SNES *SNES;
```

Example 2 (unknown):
```unknown
SNESNEWTONLS
```

Example 3 (unknown):
```unknown
SNESGetNPC()
```

Example 4 (unknown):
```unknown
SNESCreate()
```

---

## SNES_CONERGED_ITERATING#

**URL:** https://petsc.org/release/manualpages/SNES/SNES_CONERGED_ITERATING/

**Contents:**
- SNES_CONERGED_ITERATING#
- See Also#
- Level#
- Location#

this only occurs if SNESGetConvergedReason() is called during the SNESSolve()

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESGetConvergedReason(), SNESConvergedReason, SNESSetTolerances()

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESGetConvergedReason()
```

Example 2 (unknown):
```unknown
SNESSolve()
```

Example 3 (unknown):
```unknown
SNESSolve()
```

Example 4 (unknown):
```unknown
SNESGetConvergedReason()
```

---

## SNES_CONVERGED_FNORM_ABS#

**URL:** https://petsc.org/release/manualpages/SNES/SNES_CONVERGED_FNORM_ABS/

**Contents:**
- SNES_CONVERGED_FNORM_ABS#
- See Also#
- Level#
- Location#

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESGetConvergedReason(), SNESConvergedReason, SNESSetTolerances()

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
SNESGetConvergedReason()
```

Example 3 (unknown):
```unknown
SNESConvergedReason
```

Example 4 (unknown):
```unknown
SNESSetTolerances()
```

---

## SNES_CONVERGED_FNORM_RELATIVE#

**URL:** https://petsc.org/release/manualpages/SNES/SNES_CONVERGED_FNORM_RELATIVE/

**Contents:**
- SNES_CONVERGED_FNORM_RELATIVE#
- See Also#
- Level#
- Location#

\(||F|| \le rtol*||F(x_0)||\) where \(x_0\) is the initial guess

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESGetConvergedReason(), SNESConvergedReason, SNESSetTolerances()

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
SNESGetConvergedReason()
```

Example 3 (unknown):
```unknown
SNESConvergedReason
```

Example 4 (unknown):
```unknown
SNESSetTolerances()
```

---

## SNES_CONVERGED_SNORM_RELATIVE#

**URL:** https://petsc.org/release/manualpages/SNES/SNES_CONVERGED_SNORM_RELATIVE/

**Contents:**
- SNES_CONVERGED_SNORM_RELATIVE#
- Options Database Key#
- See Also#
- Level#
- Location#

The 2-norm of the last step \(\le stol * ||x||\) where x is the current solution and stol is the 4th argument to SNESSetTolerances()

-snes_stol stol - the step tolerance

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESGetConvergedReason(), SNESConvergedReason, SNESSetTolerances()

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetTolerances()
```

Example 2 (unknown):
```unknown
SNESSolve()
```

Example 3 (unknown):
```unknown
SNESGetConvergedReason()
```

Example 4 (unknown):
```unknown
SNESConvergedReason
```

---

## SNES_DIVERGED_DTOL#

**URL:** https://petsc.org/release/manualpages/SNES/SNES_DIVERGED_DTOL/

**Contents:**
- SNES_DIVERGED_DTOL#
- See Also#
- Level#
- Location#

The norm of the function has increased by a factor of divtol set with SNESSetDivergenceTolerance()

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESGetConvergedReason(), SNESConvergedReason, SNESSetTolerances(), SNESSetDivergenceTolerance()

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetDivergenceTolerance()
```

Example 2 (unknown):
```unknown
SNESSolve()
```

Example 3 (unknown):
```unknown
SNESGetConvergedReason()
```

Example 4 (unknown):
```unknown
SNESConvergedReason
```

---

## SNES_DIVERGED_FUNCTION_COUNT#

**URL:** https://petsc.org/release/manualpages/SNES/SNES_DIVERGED_FUNCTION_COUNT/

**Contents:**
- SNES_DIVERGED_FUNCTION_COUNT#
- See Also#
- Level#
- Location#

The user provided function has been called more times then the final argument to SNESSetTolerances()

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESGetConvergedReason(), SNESConvergedReason, SNESSetTolerances()

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetTolerances()
```

Example 2 (unknown):
```unknown
SNESSolve()
```

Example 3 (unknown):
```unknown
SNESGetConvergedReason()
```

Example 4 (unknown):
```unknown
SNESConvergedReason
```

---

## SNES_DIVERGED_FUNCTION_DOMAIN#

**URL:** https://petsc.org/release/manualpages/SNES/SNES_DIVERGED_FUNCTION_DOMAIN/

**Contents:**
- SNES_DIVERGED_FUNCTION_DOMAIN#
- See Also#
- Level#
- Location#

the function provided with SNESSetFunction() called SNESSetFunctionDomainError() and the solver could not recoverer.

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESGetConvergedReason(), SNESConvergedReason, SNESSetTolerances()

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetFunction()
```

Example 2 (unknown):
```unknown
SNESSetFunctionDomainError()
```

Example 3 (unknown):
```unknown
SNESSolve()
```

Example 4 (unknown):
```unknown
SNESGetConvergedReason()
```

---

## SNES_DIVERGED_FUNCTION_NANORINF#

**URL:** https://petsc.org/release/manualpages/SNES/SNES_DIVERGED_FUNCTION_NANORINF/

**Contents:**
- SNES_DIVERGED_FUNCTION_NANORINF#
- See Also#
- Level#
- Location#

the 2-norm of the current function evaluation is not-a-number (NaN) or infinity, this is usually caused by a division of 0 by 0, or infinity. See SNESSetFunctionDomainError()

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESGetConvergedReason(), SNESConvergedReason, SNESSetTolerances()

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetFunctionDomainError()
```

Example 2 (unknown):
```unknown
SNESSolve()
```

Example 3 (unknown):
```unknown
SNESGetConvergedReason()
```

Example 4 (unknown):
```unknown
SNESConvergedReason
```

---

## SNES_DIVERGED_JACOBIAN_DOMAIN#

**URL:** https://petsc.org/release/manualpages/SNES/SNES_DIVERGED_JACOBIAN_DOMAIN/

**Contents:**
- SNES_DIVERGED_JACOBIAN_DOMAIN#
- See Also#
- Level#
- Location#

the function provided with SNESSetJacobian() called SNESSetJacobianDomainError()

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESGetConvergedReason(), SNESConvergedReason, SNESSetTolerances()

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetJacobian()
```

Example 2 (unknown):
```unknown
SNESSetJacobianDomainError()
```

Example 3 (unknown):
```unknown
SNESSolve()
```

Example 4 (unknown):
```unknown
SNESGetConvergedReason()
```

---

## SNES_DIVERGED_LINE_SEARCH#

**URL:** https://petsc.org/release/manualpages/SNES/SNES_DIVERGED_LINE_SEARCH/

**Contents:**
- SNES_DIVERGED_LINE_SEARCH#
- See Also#
- Level#
- Location#

The line search has failed. This only occurs for a SNES solvers that use a line search

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESGetConvergedReason(), SNESConvergedReason, SNESSetTolerances(), SNESLineSearch

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
SNESGetConvergedReason()
```

Example 3 (unknown):
```unknown
SNESConvergedReason
```

Example 4 (unknown):
```unknown
SNESSetTolerances()
```

---

## SNES_DIVERGED_LOCAL_MIN#

**URL:** https://petsc.org/release/manualpages/SNES/SNES_DIVERGED_LOCAL_MIN/

**Contents:**
- SNES_DIVERGED_LOCAL_MIN#
- See Also#
- Level#
- Location#

the algorithm seems to have stagnated at a local minimum that is not zero. See the manual page for SNESConvergedReason for more details

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESGetConvergedReason(), SNESConvergedReason, SNESSetTolerances()

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESConvergedReason
```

Example 2 (unknown):
```unknown
SNESSolve()
```

Example 3 (unknown):
```unknown
SNESGetConvergedReason()
```

Example 4 (unknown):
```unknown
SNESConvergedReason
```

---

## SNES_DIVERGED_MAX_IT#

**URL:** https://petsc.org/release/manualpages/SNES/SNES_DIVERGED_MAX_IT/

**Contents:**
- SNES_DIVERGED_MAX_IT#
- See Also#
- Level#
- Location#

SNESSolve() has reached the maximum number of iterations requested

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESGetConvergedReason(), SNESConvergedReason, SNESSetTolerances()

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
SNESGetConvergedReason()
```

Example 3 (unknown):
```unknown
SNESConvergedReason
```

Example 4 (unknown):
```unknown
SNESSetTolerances()
```

---

## SNES_DIVERGED_OBJECTIVE_DOMAIN#

**URL:** https://petsc.org/release/manualpages/SNES/SNES_DIVERGED_OBJECTIVE_DOMAIN/

**Contents:**
- SNES_DIVERGED_OBJECTIVE_DOMAIN#
- See Also#
- Level#
- Location#

the function provided with SNESSetObjective() called SNESSetObjectiveDomainError() and the solver could not recoverer.

SNES: Nonlinear Solvers, SNES, SNESSolve(), SNESGetConvergedReason(), SNESConvergedReason, SNESSetTolerances()

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSetObjective()
```

Example 2 (unknown):
```unknown
SNESSetObjectiveDomainError()
```

Example 3 (unknown):
```unknown
SNESSolve()
```

Example 4 (unknown):
```unknown
SNESGetConvergedReason()
```

---

## SNES: Nonlinear Solvers#

**URL:** https://petsc.org/release/manual/snes/

**Contents:**
- SNES: Nonlinear Solvers#
- Basic SNES Usage#
  - Nonlinear Function Evaluation#
  - Jacobian Evaluation#
- Function Domain Errors and infinity or NaN#
- The Nonlinear Solvers#
  - Line Search Newton#
  - Trust Region Methods#
  - Newton with Arc Length Continuation#
  - Nonlinear Krylov Methods#

The solution of large-scale nonlinear problems pervades many facets of computational science and demands robust and flexible solution strategies. The SNES library of PETSc provides a powerful suite of data-structure-neutral numerical routines for such problems. Built on top of the linear solvers and data structures discussed in preceding chapters, SNES enables the user to easily customize the nonlinear solvers according to the application at hand. Also, the SNES interface is identical for the uniprocess and parallel cases; the only difference in the parallel version is that each process typically forms only its local contribution to various matrices and vectors.

The SNES class includes methods for solving systems of nonlinear equations of the form

where \(\mathbf{F}: \, \Re^n \to \Re^n\). Newton-like methods provide the core of the package, including both line search and trust region techniques. A suite of nonlinear Krylov methods and methods based upon problem decomposition are also included. The solvers are discussed further in The Nonlinear Solvers. Following the PETSc design philosophy, the interfaces to the various solvers are all virtually identical. In addition, the SNES software is completely flexible, so that the user can at runtime change any facet of the solution process.

PETSc’s default method for solving the nonlinear equation is Newton’s method with line search, SNESNEWTONLS. The general form of the \(n\)-dimensional Newton’s method for solving (3) is

where \(\mathbf{x}_0\) is an initial approximation to the solution and \(\mathbf{J}(\mathbf{x}_k) = \mathbf{F}'(\mathbf{x}_k)\), the Jacobian, is nonsingular at each iteration. In practice, the Newton iteration (4) is implemented by the following two steps:

Other defect-correction algorithms can be implemented by using different choices for \(J(\mathbf{x}_k)\).

In the simplest usage of the nonlinear solvers, the user must merely provide a C, C++, Fortran, or Python routine to evaluate the nonlinear function (3). The corresponding Jacobian matrix can be approximated with finite differences. For codes that are typically more efficient and accurate, the user can provide a routine to compute the Jacobian; details regarding these application-provided routines are discussed below. To provide an overview of the use of the nonlinear solvers, browse the concrete example in ex1.c or skip ahead to the discussion.

Listing: src/snes/tutorials/ex1.c

To create a SNES solver, one must first call SNESCreate() as follows:

The user must then set routines for evaluating the residual function (3) and, possibly, its associated Jacobian matrix, as discussed in the following sections.

To choose a nonlinear solution method, the user can either call

or use the option -snes_type type, where details regarding the available methods are presented in The Nonlinear Solvers. The application code can take complete control of the linear and nonlinear techniques used in the Newton-like method by calling

This routine provides an interface to the PETSc options database, so that at runtime the user can select a particular nonlinear solver, set various parameters and customized routines (e.g., specialized line search variants), prescribe the convergence tolerance, and set monitoring routines. With this routine the user can also control all linear solver options in the KSP, and PC modules, as discussed in KSP: Linear System Solvers.

After having set these routines and options, the user solves the problem by calling

where x should be initialized to the initial guess before calling and contains the solution on return. In particular, to employ an initial guess of zero, the user should explicitly set this vector to zero by calling VecZeroEntries(x). Finally, after solving the nonlinear system (or several systems), the user should destroy the SNES context with

When solving a system of nonlinear equations, the user must provide a a residual function (3), which is set using

The argument f is an optional vector for storing the solution; pass NULL to have the SNES allocate it for you. The argument ctx is an optional user-defined context, which can store any private, application-specific data required by the function evaluation routine; NULL should be used if such information is not needed. In C and C++, a user-defined context is merely a structure in which various objects can be stashed; in Fortran an application context can be a PETSc object or a derived type. SNES Tutorial ex5 and SNES Tutorial ex5f90 give examples of user-defined application contexts in C and Fortran, respectively.

The user may also specify a routine to form some approximation of the Jacobian matrix, A, at the current iterate, x, as is typically done with

The arguments of the routine FormJacobian() are the current iterate, x; the (approximate) Jacobian matrix, Amat; the matrix from which the preconditioner is constructed, Pmat (which is usually the same as Amat); and an optional user-defined Jacobian context, ctx, for application-specific data. The FormJacobian() callback is only invoked if the solver requires it, always after FormFunction() has been called at the current iterate.

Note that the SNES solvers are all data-structure neutral, so the full range of PETSc matrix formats (including “matrix-free” methods) can be used. Matrices discusses information regarding available matrix formats and options, while Matrix-Free Methods focuses on matrix-free methods in SNES. We briefly touch on a few details of matrix usage that are particularly important for efficient use of the nonlinear solvers.

A common usage paradigm is to assemble the problem Jacobian in the preconditioner storage B, rather than A. In the case where they are identical, as in many simulations, this makes no difference. However, it allows us to check the analytic Jacobian we construct in FormJacobian() by passing the -snes_mf_operator flag. This causes PETSc to approximate the Jacobian using finite differencing of the function evaluation (discussed in Finite Difference Jacobian Approximations), and the analytic Jacobian becomes merely the preconditioner. Even if the analytic Jacobian is incorrect, it is likely that the finite difference approximation will converge, and thus this is an excellent method to verify the analytic Jacobian. Moreover, if the analytic Jacobian is incomplete (some terms are missing or approximate), -snes_mf_operator may be used to obtain the exact solution, where the Jacobian approximation has been transferred to the preconditioner.

One such approximate Jacobian comes from “Picard linearization”, use SNESSetPicard(), which writes the nonlinear system as

where \(\mathbf{A}(\mathbf{x})\) usually contains the lower-derivative parts of the equation. For example, the nonlinear diffusion problem

would be linearized as

Usually this linearization is simpler to implement than Newton and the linear problems are somewhat easier to solve. In addition to using -snes_mf_operator with this approximation to the Jacobian, the Picard iterative procedure can be performed by defining \(\mathbf{J}(\mathbf{x})\) to be \(\mathbf{A}(\mathbf{x})\). Sometimes this iteration exhibits better global convergence than Newton linearization.

During successive calls to FormJacobian(), the user can either insert new matrix contexts or reuse old ones, depending on the application requirements. For many sparse matrix formats, reusing the old space (and merely changing the matrix elements) is more efficient; however, if the matrix nonzero structure completely changes, creating an entirely new matrix context may be preferable. Upon subsequent calls to the FormJacobian() routine, the user may wish to reinitialize the matrix entries to zero by calling MatZeroEntries(). See Other Matrix Operations for details on the reuse of the matrix context.

The directory $PETSC_DIR/src/snes/tutorials provides a variety of examples.

Sometimes a nonlinear solver may produce a step that is not within the domain of a given function, for example one with a negative pressure. When this occurs one can call SNESSetFunctionDomainError() or SNESSetJacobianDomainError() to indicate to SNES the step is not valid. One must also use SNESGetConvergedReason() and check the reason to confirm if the solver succeeded. See Variational Inequalities for how to provide SNES with bounds on the variables to solve (differential) variational inequalities and how to control properties of the line step computed.

Occasionally nonlinear solvers will propose solutions \(u\), where the function value (or the objective function set with SNESSetObjective()) contains infinity or NaN. This can be due to bugs in the application code or because the proposed solution is not in the domain of the function. The application function can call SNESSetFunctionDomainError() or SNESSetObjectiveDomainError() to indicate \(u\) is not in the function’s domain.

Some SNESSolve() implementations (and related SNESLineSearchApply() routines) attempt to recover from the infinity or NaN; generally by shrinking the step size. If they are unable to recover the SNESConvergedReason returned will be SNES_DIVERGED_FUNCTION_DOMAIN, SNES_DIVERGED_OJECTIVE_DOMAIN, SNES_DIVERGED_FUNCTION_NANORINF, or SNES_DIVERGED_OJECTIVE_NANORINF.

As summarized in Table PETSc Nonlinear Solvers, SNES includes several Newton-like nonlinear solvers based on line search techniques and trust region methods. Also provided are several nonlinear Krylov methods, as well as nonlinear methods involving decompositions of the problem.

Each solver may have associated with it a set of options, which can be set with routines and options database commands provided for this purpose. A complete list can be found by consulting the manual pages or by running a program with the -help option; we discuss just a few in the sections below.

Newton with Arc Length Continuation

see PETSc quasi-Newton solvers

Full Approximation Scheme

Nonlinear Gauss-Seidel

Newton with constraints (1)

Newton with constraints (2)

Multi-stage Smoothers

The method SNESNEWTONLS (-snes_type newtonls) provides a line search Newton method for solving systems of nonlinear equations. By default, this technique employs cubic backtracking [DennisJrS83]. Alternative line search techniques are listed in Table PETSc Line Search Methods.

SNESLINESEARCHNLEQERR

SNESLINESEARCHBISECTION

Every SNES has a line search context of type SNESLineSearch that may be retrieved using

There are several default options for the line searches. The order of polynomial approximation may be set with -snes_linesearch_order or

for instance, 2 for quadratic or 3 for cubic. Sometimes, it may not be necessary to monitor the progress of the nonlinear iteration. In this case, -snes_linesearch_norms or

may be used to turn off function, step, and solution norm computation at the end of the linesearch.

The default line search for the line search Newton method, SNESLINESEARCHBT involves several parameters, which are set to defaults that are reasonable for many applications. The user can override the defaults by using the following options:

-snes_linesearch_alpha alpha

-snes_linesearch_maxstep max

-snes_linesearch_minlambda tol

Besides the backtracking linesearch, there are SNESLINESEARCHSECANT, which uses a polynomial secant minimization of \(||F(x)||_2\) or an objective function if set, and SNESLINESEARCHCP, which minimizes \(F(x) \cdot Y\) where \(Y\) is the search direction. These are both potentially iterative line searches, which may be used to find a better-fitted steplength in the case where a single secant search is not sufficient. The number of iterations may be set with -snes_linesearch_max_it. In addition, the convergence criteria of the iterative line searches may be set using function tolerances -snes_linesearch_rtol and -snes_linesearch_atol, and steplength tolerance snes_linesearch_ltol.

For highly non-linear problems, the bisection line search SNESLINESEARCHBISECTION may prove useful due to its robustness. Similar to the critical point line search SNESLINESEARCHCP, it seeks to find the root of \(F(x) \cdot Y\). While the latter does so through a secant method, the bisection line search does so by iteratively bisecting the step length interval. It works as follows (with \(f(\lambda)=F(x-\lambda Y) \cdot Y / ||Y||\) for brevity):

initialize: \(j=1\), \(\lambda_0 = \lambda_{\text{left}} = 0.0\), \(\lambda_j = \lambda_{\text{right}} = \alpha\), compute \(f(\lambda_0)\) and \(f(\lambda_j)\)

check whether there is a change of sign in the interval: \(f(\lambda_{\text{left}}) f(\lambda_j) \leq 0\); if not accept the full step length \(\lambda_1\)

if there is a change of sign, enter iterative bisection procedure

check convergence/ exit criteria:

absolute tolerance \(f(\lambda_j) < \mathtt{atol}\)

relative tolerance \(f(\lambda_j) < \mathtt{rtol} \cdot f(\lambda_0)\)

change of step length \(\lambda_j - \lambda_{j-1} < \mathtt{ltol}\)

number of iterations \(j < \mathtt{max\_it}\)

if \(j > 1\), determine direction of bisection

bisect the interval: \(\lambda_{j+1} = (\lambda_{\text{left}} + \lambda_{\text{right}})/2\), compute \(f(\lambda_{j+1})\)

update variables for the next iteration: \(\lambda_j \gets \lambda_{j+1}\), \(f(\lambda_j) \gets f(\lambda_{j+1})\), \(j \gets j+1\)

Custom line search types may either be defined using SNESLineSearchShell, or by creating a custom user line search type in the model of the preexisting ones and register it using

The trust region method in SNES for solving systems of nonlinear equations, SNESNEWTONTR (-snes_type newtontr), is similar to the one developed in the MINPACK project [MoreSGH84]. Several parameters can be set to control the variation of the trust region size during the solution process. In particular, the user can control the initial trust region radius, computed by

by setting \(\Delta_0\) via the option -snes_tr_delta0 delta0.

The Newton method with arc length continuation reformulates the linearized system \(K\delta \mathbf x = -\mathbf F(\mathbf x)\) by introducing the load parameter \(\lambda\) and splitting the residual into two components, commonly corresponding to internal and external forces:

Often, \(\mathbf F^{\mathrm{ext}}(\mathbf x, \lambda)\) is linear in \(\lambda\), which can be thought of as applying the external force in proportional load increments. By default, this is how the right-hand side vector is handled in the implemented method. Generally, however, \(\mathbf F^{\mathrm{ext}}(\mathbf x, \lambda)\) may depend non-linearly on \(\lambda\) or \(\mathbf x\), or both. To accommodate this possibility, we provide the SNESNewtonALGetLoadParameter() function, which allows for the current value of \(\lambda\) to be queried in the functions provided to SNESSetFunction() and SNESSetJacobian().

Additionally, we split the solution update into two components:

where \(\delta s = 1\) unless partial corrections are used (discussed more below). Each of \(\delta \mathbf x^F\) and \(\delta \mathbf x^Q\) are found via solving a linear system with the Jacobian \(K\):

\(\delta \mathbf x^F\) is the full Newton step for a given value of \(\lambda\): \(K \delta \mathbf x^F = -\mathbf F(\mathbf x, \lambda)\)

\(\delta \mathbf x^Q\) is the variation in \(\mathbf x\) with respect to \(\lambda\), computed by \(K \delta\mathbf x^Q = \mathbf Q(\mathbf x, \lambda)\), where \(\mathbf Q(\mathbf x, \lambda) = -\partial \mathbf F (\mathbf x, \lambda) / \partial \lambda\) is the tangent load vector.

Often, the tangent load vector \(\mathbf Q\) is constant within a load increment, which corresponds to the case of proportional loading discussed above. By default, \(\mathbf Q\) is the full right-hand-side vector, if one was provided. The user can also provide a function which computes \(\mathbf Q\) to SNESNewtonALSetFunction(). This function should have the same signature as for SNESSetFunction, and the user should use SNESNewtonALGetLoadParameter() to get \(\lambda\) if it is needed.

The Constraint Surface. Considering the \(n+1\) dimensional space of \(\mathbf x\) and \(\lambda\), we define the linearized equilibrium line to be the set of points for which the linearized equilibrium equations are satisfied. Given the previous iterative solution \(\mathbf t^{(j-1)} = [\mathbf x^{(j-1)}, \lambda^{(j-1)}]\), this line is defined by the point \(\mathbf t^{(j-1)} + [\delta\mathbf x^F, 0]\) and the vector \(\mathbf t^Q [\delta\mathbf x^Q, 1]\). The arc length method seeks the intersection of this linearized equilibrium line with a quadratic constraint surface, defined by

where \(L\) is a user-provided step size corresponding to the radius of the constraint surface, \(\Delta\mathbf x\) and \(\Delta\lambda\) are the accumulated updates over the current load step, and \(\psi^2\) is a user-provided consistency parameter determining the shape of the constraint surface. Generally, \(\psi^2 > 0\) leads to a hyper-sphere constraint surface, while \(\psi^2 = 0\) leads to a hyper-cylinder constraint surface.

Since the solution will always fall on the constraint surface, the method will often require multiple incremental steps to fully solve the non-linear problem. This is necessary to accurately trace the equilibrium path. Importantly, this is fundamentally different from time stepping. While a similar process could be implemented as a TS, this method is particularly designed to be used as a SNES, either standalone or within a TS.

To this end, by default, the load parameter is used such that the full external forces are applied at \(\lambda = 1\), although we allow for the user to specify a different value via -snes_newtonal_lambda_max. To ensure that the solution corresponds exactly to the external force prescribed by the user, i.e. that the load parameter is exactly \(\lambda_{max}\) at the end of the SNES solve, we clamp the value before computing the solution update. As such, the final increment will likely be a hybrid of arc length continuation and normal Newton iterations.

Choosing the Continuation Step. For the first iteration from an equilibrium point, there is a single correct way to choose \(\delta\lambda\), which follows from the constraint equations. Specifically the constraint equations yield the quadratic equation \(a\delta\lambda^2 + b\delta\lambda + c = 0\), where

Since in the first iteration, \(\Delta\mathbf x = \delta\mathbf x^F = \mathbf 0\) and \(\Delta\lambda = 0\), \(b = 0\) and the equation simplifies to a pair of real roots:

where the sign is positive for the first increment and is determined by the previous increment otherwise as

where \((\Delta\mathbf x)_{i-1}\) and \((\Delta\lambda)_{i-1}\) are the accumulated updates over the previous load step.

In subsequent iterations, there are different approaches to selecting \(\delta\lambda\), all of which have trade-offs. The main difference is whether the iterative solution falls on the constraint surface at every iteration, or only when fully converged. PETSc implements two approaches, set via SNESNewtonALSetCorrectionType() or -snes_newtonal_correction_type (normal|exact) on the command line.

Corrections in the Normal Hyperplane. The SNES_NEWTONAL_CORRECTION_NORMAL option is simpler and computationally less expensive, but may fail to converge, as the constraint equation is not satisfied at every iteration. The update \(\delta \lambda\) is chosen such that the update is within the normal hyper-surface to the quadratic constraint surface. Mathematically, that is

This implementation is based on [LPP+11].

Exact Corrections. The SNES_NEWTONAL_CORRECTION_EXACT option is far more complex, but ensures that the constraint is exactly satisfied at every Newton iteration. As such, it is generally more robust. By evaluating the intersection of constraint surface and equilibrium line at each iteration, \(\delta\lambda\) is chosen as one of the roots of the above quadratic equation \(a\delta\lambda^2 + b\delta\lambda + c = 0\). This method encounters issues, however, if the linearized equilibrium line and constraint surface do not intersect due to particularly large linearized error. In this case, the roots are complex. To continue progressing toward a solution, this method uses a partial correction by choosing \(\delta s\) such that the quadratic equation has a single real root. Geometrically, this is selecting the point on the constraint surface closest to the linearized equilibrium line. See the code or [RCorreaC08] for a mathematical description of these partial corrections.

A number of nonlinear Krylov methods are provided, including Nonlinear Richardson (SNESNRICHARDSON), nonlinear conjugate gradient (SNESNCG), nonlinear GMRES (SNESNGMRES), and Anderson Mixing (SNESANDERSON). These methods are described individually below. They are all instrumental to PETSc’s nonlinear preconditioning.

Nonlinear Richardson. The nonlinear Richardson iteration, SNESNRICHARDSON, merely takes the form of a line search-damped fixed-point iteration of the form

where the default linesearch is SNESLINESEARCHSECANT. This simple solver is mostly useful as a nonlinear smoother, or to provide line search stabilization to an inner method.

Nonlinear Conjugate Gradients. Nonlinear CG, SNESNCG, is equivalent to linear CG, but with the steplength determined by line search (SNESLINESEARCHCP by default). Five variants (Fletcher-Reed, Hestenes-Steifel, Polak-Ribiere-Polyak, Dai-Yuan, and Conjugate Descent) are implemented in PETSc and may be chosen using

Anderson Mixing and Nonlinear GMRES Methods. Nonlinear GMRES (SNESNGMRES), and Anderson Mixing (SNESANDERSON) methods combine the last \(m\) iterates, plus a new fixed-point iteration iterate, into an approximate residual-minimizing new iterate.

All of the above methods have support for using a nonlinear preconditioner to compute the preliminary update step, rather than the default which is the nonlinear function’s residual, \(\mathbf{F}(\mathbf{x}_k)\). The different update is obtained by solving a nonlinear preconditioner nonlinear problem, which has its own SNES object that may be obtained with SNESGetNPC().

Quasi-Newton methods store iterative rank-one updates to the Jacobian instead of computing the Jacobian directly. Three limited-memory quasi-Newton methods are provided, L-BFGS, which are described in Table PETSc quasi-Newton solvers. These all are encapsulated under -snes_type qn and may be changed with snes_qn_type. The default is L-BFGS, which provides symmetric updates to an approximate Jacobian. This iteration is similar to the line search Newton methods.

The quasi-Newton methods support the use of a nonlinear preconditioner that can be obtained with SNESGetNPC() and then configured; or that can be configured with SNES, KSP, and PC options using the options database prefix -npc_.

SNESLINESEARCHBASIC (or equivalently SNESLINESEARCHNONE)

One may also control the form of the initial Jacobian approximation with

and the restart type with

The Nonlinear Full Approximation Scheme (FAS) SNESFAS, is a nonlinear multigrid method. At each level, there is a recursive cycle control SNES instance, and either one or two nonlinear solvers that act as smoothers (up and down). Problems set up using the SNES DMDA interface are automatically coarsened. FAS, SNESFAS, differs slightly from linear multigrid PCMG, in that the hierarchy is constructed recursively. However, much of the interface is a one-to-one map. We describe the “get” operations here, and it can be assumed that each has a corresponding “set” operation. For instance, the number of levels in the hierarchy may be retrieved using

There are four SNESFAS cycle types, SNES_FAS_MULTIPLICATIVE, SNES_FAS_ADDITIVE, SNES_FAS_FULL, and SNES_FAS_KASKADE. The type may be set with

and the cycle type, 1 for V, 2 for W, may be set with

Much like the interface to PCMG described in Multigrid Preconditioners, there are interfaces to recover the various levels’ cycles and smoothers. The level smoothers may be accessed with

and the level cycles with

Also akin to PCMG, the restriction and prolongation at a level may be acquired with

In addition, FAS requires special restriction for solution-like variables, called injection. This may be set with

The coarse solve context may be acquired with

Nonlinear Additive Schwarz methods (NASM) take a number of local nonlinear subproblems, solves them independently in parallel, and combines those solutions into a new approximate solution.

allows for the user to create these local subdomains. Problems set up using the SNES DMDA interface are automatically decomposed. To begin, the type of subdomain updates to the whole solution are limited to two types borrowed from PCASM: PC_ASM_BASIC, in which the overlapping updates added. PC_ASM_RESTRICT updates in a nonoverlapping fashion. This may be set with

SNESASPIN is a helper SNES type that sets up a nonlinearly preconditioned Newton’s method using NASM as the preconditioner.

This section discusses options and routines that apply to all SNES solvers and problem classes. In particular, we focus on convergence tests, monitoring routines, and tools for checking derivative computations.

Convergence of the nonlinear solvers can be detected in a variety of ways; the user can even specify a customized test, as discussed below. Most of the nonlinear solvers use SNESConvergenceTestDefault(), however, SNESNEWTONTR uses a method-specific additional convergence test as well. The convergence tests involves several parameters, which are set by default to values that should be reasonable for a wide range of problems. The user can customize the parameters to the problem at hand by using some of the following routines and options.

One method of convergence testing is to declare convergence when the norm of the change in the solution between successive iterations is less than some tolerance, stol. Convergence can also be determined based on the norm of the function. Such a test can use either the absolute size of the norm, atol, or its relative decrease, rtol, from an initial guess. The following routine sets these parameters, which are used in many of the default SNES convergence tests:

This routine also sets the maximum numbers of allowable nonlinear iterations, its, and function evaluations, fcts. The corresponding options database commands for setting these parameters are:

-snes_max_funcs fcts (use unlimited for no maximum)

A related routine is SNESGetTolerances(). PETSC_CURRENT may be used for any parameter to indicate the current value should be retained; use PETSC_DETERMINE to restore to the default value from when the object was created.

Users can set their own customized convergence tests in SNES by using the command

The final argument of the convergence test routine, cctx, denotes an optional user-defined context for private data. When solving systems of nonlinear equations, the arguments xnorm, gnorm, and f are the current iterate norm, current step norm, and function norm, respectively. SNESConvergedReason should be set positive for convergence and negative for divergence. See include/petscsnes.h for a list of values for SNESConvergedReason.

By default the SNES solvers run silently without displaying information about the iterations. The user can initiate monitoring with the command

The routine, mon, indicates a user-defined monitoring routine, where its and mctx respectively denote the iteration number and an optional user-defined context for private data for the monitor routine. The argument norm is the function norm.

The routine set by SNESMonitorSet() is called once after every successful step computation within the nonlinear solver. Hence, the user can employ this routine for any application-specific computations that should be done after the solution update. The option -snes_monitor activates the default SNES monitor routine, SNESMonitorDefault(), while -snes_monitor_lg_residualnorm draws a simple line graph of the residual norm’s convergence.

One can cancel hardwired monitoring routines for SNES at runtime with -snes_monitor_cancel.

As the Newton method converges so that the residual norm is small, say \(10^{-10}\), many of the final digits printed with the -snes_monitor option are meaningless. Worse, they are different on different machines; due to different round-off rules used by, say, the IBM RS6000 and the Sun SPARC. This makes testing between different machines difficult. The option -snes_monitor_short causes PETSc to print fewer of the digits of the residual norm as it gets smaller; thus on most of the machines it will always print the same numbers making cross-process testing easier.

return the solution vector and function vector from a SNES context. These routines are useful, for instance, if the convergence test requires some property of the solution or function other than those passed with routine arguments.

Since hand-coding routines for Jacobian matrix evaluation can be error prone, SNES provides easy-to-use support for checking these matrices against finite difference versions. In the simplest form of comparison, users can employ the option -snes_test_jacobian to compare the matrices at several points. Although not exhaustive, this test will generally catch obvious problems. One can compare the elements of the two matrices by using the option -snes_test_jacobian_view , which causes the two matrices to be printed to the screen.

Another means for verifying the correctness of a code for Jacobian computation is running the problem with either the finite difference or matrix-free variant, -snes_fd or -snes_mf; see Finite Difference Jacobian Approximations or Matrix-Free Methods. If a problem converges well with these matrix approximations but not with a user-provided routine, the problem probably lies with the hand-coded matrix. See the note in Jacobian Evaluation about assembling your Jabobian in the “preconditioner” slot Pmat.

The correctness of user provided MATSHELL Jacobians in general can be checked with MatShellTestMultTranspose() and MatShellTestMult().

The correctness of user provided MATSHELL Jacobians via TSSetRHSJacobian() can be checked with TSRHSJacobianTestTranspose() and TSRHSJacobianTest() that check the correction of the matrix-transpose vector product and the matrix-product. From the command line, these can be checked with

-ts_rhs_jacobian_test_mult_transpose

-mat_shell_test_mult_transpose_view

-ts_rhs_jacobian_test_mult

-mat_shell_test_mult_view

Since exact solution of the linear Newton systems within (4) at each iteration can be costly, modifications are often introduced that significantly reduce these expenses and yet retain the rapid convergence of Newton’s method. Inexact or truncated Newton techniques approximately solve the linear systems using an iterative scheme. In comparison with using direct methods for solving the Newton systems, iterative methods have the virtue of requiring little space for matrix storage and potentially saving significant computational work. Within the class of inexact Newton methods, of particular interest are Newton-Krylov methods, where the subsidiary iterative technique for solving the Newton system is chosen from the class of Krylov subspace projection methods. Note that at runtime the user can set any of the linear solver options discussed in KSP: Linear System Solvers, such as -ksp_type ksp_type and -pc_type pc_method, to set the Krylov subspace and preconditioner methods.

Two levels of iterations occur for the inexact techniques, where during each global or outer Newton iteration a sequence of subsidiary inner iterations of a linear solver is performed. Appropriate control of the accuracy to which the subsidiary iterative method solves the Newton system at each global iteration is critical, since these inner iterations determine the asymptotic convergence rate for inexact Newton techniques. While the Newton systems must be solved well enough to retain fast local convergence of the Newton’s iterates, use of excessive inner iterations, particularly when \(\| \mathbf{x}_k - \mathbf{x}_* \|\) is large, is neither necessary nor economical. Thus, the number of required inner iterations typically increases as the Newton process progresses, so that the truncated iterates approach the true Newton iterates.

A sequence of nonnegative numbers \(\{\eta_k\}\) can be used to indicate the variable convergence criterion. In this case, when solving a system of nonlinear equations, the update step of the Newton process remains unchanged, and direct solution of the linear system is replaced by iteration on the system until the residuals

Here \(\mathbf{x}_0\) is an initial approximation of the solution, and \(\| \cdot \|\) denotes an arbitrary norm in \(\Re^n\) .

By default a constant relative convergence tolerance is used for solving the subsidiary linear systems within the Newton-like methods of SNES. When solving a system of nonlinear equations, one can instead employ the techniques of Eisenstat and Walker [EW96] to compute \(\eta_k\) at each step of the nonlinear solver by using the option -snes_ksp_ew . In addition, by adding one’s own KSP convergence test (see Convergence Tests), one can easily create one’s own, problem-dependent, inner convergence tests.

The SNES class fully supports matrix-free methods. The matrices specified in the Jacobian evaluation routine need not be conventional matrices; instead, they can point to the data required to implement a particular matrix-free method. The matrix-free variant is allowed only when the linear systems are solved by an iterative method in combination with no preconditioning (PCNONE or -pc_type none), a user-provided matrix from which to construct the preconditioner, or a user-provided preconditioner shell (PCSHELL, discussed in Preconditioners); that is, obviously matrix-free methods cannot be used with a direct solver, approximate factorization, or other preconditioner which requires access to explicit matrix entries.

The user can create a matrix-free context for use within SNES with the routine

This routine creates the data structures needed for the matrix-vector products that arise within Krylov space iterative methods [BS90]. The default SNES matrix-free approximations can also be invoked with the command -snes_mf. Or, one can retain the user-provided Jacobian preconditioner, but replace the user-provided Jacobian matrix with the default matrix-free variant with the option -snes_mf_operator.

MatCreateSNESMF() uses

which can also be used directly for users who need a matrix-free matrix but are not using SNES.

The user can set one parameter to control the Jacobian-vector product approximation with the command

The parameter rerror should be set to the square root of the relative error in the function evaluations, \(e_{rel}\); the default is the square root of machine epsilon (about \(10^{-8}\) in double precision), which assumes that the functions are evaluated to full floating-point precision accuracy. This parameter can also be set from the options database with -mat_mffd_err err

In addition, PETSc provides ways to register new routines to compute the differencing parameter (\(h\)); see the manual page for MatMFFDSetType() and MatMFFDRegister(). We currently provide two default routines accessible via -mat_mffd_type (ds|wp). For the default approach there is one “tuning” parameter, set with

This parameter, umin (or \(u_{min}\)), is a bit involved; its default is \(10^{-6}\) . Its command line form is -mat_mffd_umin umin.

The Jacobian-vector product is approximated via the formula

where \(h\) is computed via

This approach is taken from Brown and Saad [BS90]. The second approach, taken from Walker and Pernice, [PW98], computes \(h\) via

This has no tunable parameters, but note that inside the nonlinear solve for the entire linear iterative process \(u\) does not change hence \(\sqrt{1 + ||u||}\) need be computed only once. This information may be set with the options

or -mat_mffd_compute_normu (true|false). This information is used to eliminate the redundant computation of these parameters, therefore reducing the number of collective operations and improving the efficiency of the application code. This takes place automatically for the PETSc GMRES solver with left preconditioning.

It is also possible to monitor the differencing parameters h that are computed via the routines

We include an explicit example of using matrix-free methods in ex3.c. Note that by using the option -snes_mf one can easily convert any SNES code to use a matrix-free Newton-Krylov method without a preconditioner. As shown in this example, SNESSetFromOptions() must be called after SNESSetJacobian() to enable runtime switching between the user-specified Jacobian and the default SNES matrix-free form.

Listing: src/snes/tutorials/ex3.c

Table Jacobian Options summarizes the various matrix situations that SNES supports. In particular, different linear system matrices and preconditioning matrices are allowed, as well as both matrix-free and application-provided preconditioners. If ex3.c is run with the options -snes_mf and -user_precond then it uses a matrix-free application of the matrix-vector multiple and a user provided matrix-free Jacobian.

Conventional Matrix Formats

Create matrix with MatCreate()\(^*\). Assemble matrix with user-defined routine \(^\dagger\)

Create matrix with MatCreateShell(). Use MatShellSetOperation() to set various matrix actions, or use MatCreateMFFD() or MatCreateSNESMF().

Matrix used to construct the preconditioner

Create matrix with MatCreate()\(^*\). Assemble matrix with user-defined routine \(^\dagger\)

Use SNESGetKSP() and KSPGetPC() to access the PC, then use PCSetType(pc, PCSHELL) followed by PCShellSetApply().

\(^*\) Use either the generic MatCreate() or a format-specific variant such as MatCreateAIJ().

\(^\dagger\) Set user-defined matrix formation routine with SNESSetJacobian() or with a DM variant such as DMDASNESSetJacobianLocal()

SNES also provides some less well-integrated code to apply matrix-free finite differencing using an automatically computed measurement of the noise of the functions. This can be selected with -snes_mf_version 2; it does not use MatCreateMFFD() but has similar options that start with -snes_mf_ instead of -mat_mffd_. Note that this alternative prefix only works for version 2 differencing.

PETSc provides some tools to help approximate the Jacobian matrices efficiently via finite differences. These tools are intended for use in certain situations where one is unable to compute Jacobian matrices analytically, and matrix-free methods do not work well without a preconditioner, due to very poor conditioning. The approximation requires several steps:

First, one colors the columns of the (not yet built) Jacobian matrix, so that columns of the same color do not share any common rows.

Next, one creates a MatFDColoring data structure that will be used later in actually computing the Jacobian.

Finally, one tells the nonlinear solvers of SNES to use the SNESComputeJacobianDefaultColor() routine to compute the Jacobians.

A code fragment that demonstrates this process is given below.

Of course, we are cheating a bit. If we do not have an analytic formula for computing the Jacobian, then how do we know what its nonzero structure is so that it may be colored? Determining the structure is problem dependent, but fortunately, for most structured grid problems (the class of problems for which PETSc was originally designed) if one knows the stencil used for the nonlinear function one can usually fairly easily obtain an estimate of the location of nonzeros in the matrix. This is harder in the unstructured case, but one typically knows where the nonzero entries are from the mesh topology and distribution of degrees of freedom. If using DMPlex (DMPlex: Unstructured Grids) for unstructured meshes, the nonzero locations will be identified in DMCreateMatrix() and the procedure above can be used. Most external packages for unstructured meshes have similar functionality.

One need not necessarily use a MatColoring object to determine a coloring. For example, if a grid can be colored directly (without using the associated matrix), then that coloring can be provided to MatFDColoringCreate(). Note that the user must always preset the nonzero structure in the matrix regardless of which coloring routine is used.

PETSc provides the following coloring algorithms, which can be selected using MatColoringSetType() or via the command line argument -mat_coloring_type.

smallest-last [MoreSGH84]

largest-first [MoreSGH84]

incidence-degree [MoreSGH84]

Jones-Plassmann [JP93]

Natural (1 color per column)

Power (\(A^k\) followed by 1-coloring)

As for the matrix-free computation of Jacobians (Matrix-Free Methods), two parameters affect the accuracy of the finite difference Jacobian approximation. These are set with the command

The parameter rerror is the square root of the relative error in the function evaluations, \(e_{rel}\); the default is the square root of machine epsilon (about \(10^{-8}\) in double precision), which assumes that the functions are evaluated approximately to floating-point precision accuracy. The second parameter, umin, is a bit more involved; its default is \(10^{-6}\). Column \(i\) of the Jacobian matrix (denoted by \(F_{:i}\)) is approximated by the formula

where \(h\) is computed via:

for MATMFFD_WP (default). These parameters may be set from the options database with

Note that MatColoring type MATCOLORINGSL, MATCOLORINGLF, and MATCOLORINGID are sequential algorithms. MATCOLORINGJP and MATCOLORINGGREEDY are parallel algorithms, although in practice they may create more colors than the sequential algorithms. If one computes the coloring iscoloring reasonably with a parallel algorithm or by knowledge of the discretization, the routine MatFDColoringCreate() is scalable. An example of this for 2D distributed arrays is given below that uses the utility routine DMCreateColoring().

Note that the routine MatFDColoringCreate() currently is only supported for the AIJ and BAIJ matrix formats.

SNES can also solve (differential) variational inequalities with box (bound) constraints. These are nonlinear algebraic systems with additional inequality constraints on some or all of the variables: \(L_i \le u_i \le H_i\). For example, the pressure variable cannot be negative. Some, or all, of the lower bounds may be negative infinity (indicated to PETSc with SNES_VI_NINF) and some, or all, of the upper bounds may be infinity (indicated by SNES_VI_INF). The commands

are used to indicate that one is solving a variational inequality. Problems with box constraints can be solved with the reduced space, SNESVINEWTONRSLS, and semi-smooth SNESVINEWTONSSLS solvers.

Reduced space methods are also known as active set methods to capture the idea that at each Newton step a linear problem on a reduced space (the active set of variables) is solved to produce an update. See SNESVINEWTONRSLS for a concise definition of the (in)active set used by the algorithms.

The options -snes_vi_monitor, -snes_vi_monitor_residual, and -snes_vi_monitor_active turn on extra monitoring of the active set associated with the bounds.

The option -snes_vi_type allows selecting from several VI solvers, the default is preferred.

SNESLineSearchSetPreCheck() and SNESLineSearchSetPostCheck() can also be used to control properties of the steps selected by SNES.

The mathematical framework of nonlinear preconditioning is explained in detail in [BKST15]. Nonlinear preconditioning in PETSc involves the use of an inner SNES instance to define the step for an outer SNES instance. The inner instance may be extracted using

and passed run-time options using the -npc_ prefix. Nonlinear preconditioning comes in two flavors: left and right. The side may be changed using -snes_npc_side or SNESSetNPCSide(). Left nonlinear preconditioning redefines the nonlinear function as the action of the nonlinear preconditioner \(\mathbf{M}\);

Right nonlinear preconditioning redefines the nonlinear function as the function on the action of the nonlinear preconditioner;

which can be interpreted as putting the preconditioner into “striking distance” of the solution by outer acceleration.

In addition, basic patterns of solver composition are available with the SNESType SNESCOMPOSITE. This allows for two or more SNES instances to be combined additively or multiplicatively. By command line, a set of SNES types may be given by comma separated list argument to -snes_composite_sneses. There are additive (SNES_COMPOSITE_ADDITIVE), additive with optimal damping (SNES_COMPOSITE_ADDITIVEOPTIMAL), and multiplicative (SNES_COMPOSITE_MULTIPLICATIVE) variants which may be set with

New subsolvers may be added to the composite solver with

Peter N. Brown and Youcef Saad. Hybrid Krylov methods for nonlinear systems of equations. SIAM J. Sci. Stat. Comput., 11:450–481, 1990.

Peter R. Brune, Matthew G. Knepley, Barry F. Smith, and Xuemin Tu. Composing scalable nonlinear algebraic solvers. SIAM Review, 57(4):535–565, 2015. http://www.mcs.anl.gov/papers/P2010-0112.pdf. URL: http://www.mcs.anl.gov/papers/P2010-0112.pdf, doi:10.1137/130936725.

S. C. Eisenstat and H. F. Walker. Choosing the forcing terms in an inexact Newton method. SIAM J. Scientific Computing, 17:16–32, 1996.

Mark T. Jones and Paul E. Plassmann. A parallel graph coloring heuristic. SIAM J. Sci. Comput., 14(3):654–669, 1993.

Sofie E. Leon, Glaucio H. Paulino, Anderson Pereira, Ivan F. M. Menezes, and Eduardo N. Lages. A unified library of nonlinear solution schemes. Applied Mechanics Reviews, 64(4):040803, July 2011. doi:10.1115/1.4006992.

Jorge J. Moré, Danny C. Sorenson, Burton S. Garbow, and Kenneth E. Hillstrom. The MINPACK project. In Wayne R. Cowell, editor, Sources and Development of Mathematical Software, 88–111. 1984.

M. Pernice and H. F. Walker. NITSOL: a Newton iterative solver for nonlinear systems. SIAM J. Sci. Stat. Comput., 19:302–318, 1998.

Manuel Ritto-Corrêa and Dinar Camotim. On the arc-length and other quadratic control methods: established, less known and new implementation procedures. Computers & Structures, 86(11):1353–1368, June 2008. doi:10.1016/j.compstruc.2007.08.003.

J. E. Dennis Jr. and Robert B. Schnabel. Numerical Methods for Unconstrained Optimization and Nonlinear Equations. Prentice-Hall, Inc., Englewood Cliffs, NJ, 1983.

KSP: Linear System Solvers

TS: Scalable ODE and DAE Solvers

**Examples:**

Example 1 (unknown):
```unknown
SNESNEWTONLS
```

Example 2 (unknown):
```unknown
src/snes/tutorials/ex1.c
```

Example 3 (cpp):
```cpp
static char help[] = "Newton's method for a two-variable system, sequential.\n\n";

/*
   Include "petscsnes.h" so that we can use SNES solvers.  Note that this
   file automatically includes:
     petscsys.h       - base PETSc routines   petscvec.h - vectors
     petscmat.h - matrices
     petscis.h     - index sets            petscksp.h - Krylov subspace methods
     petscviewer.h - viewers               petscpc.h  - preconditioners
     petscksp.h   - linear solvers
*/
/*F
This examples solves either
\begin{equation}
  F\genfrac{(}{)}{0pt}{}{x_0}{x_1} = \genfrac{(}{)}{0pt}{}{x^2_0 + x_0 x_1 - 3}{x_0 x_1 + x^2_1 - 6}
\end{equation}
or if the {\tt -hard} options is given
\begin{equation}
  F\genfrac{(}{)}{0pt}{}{x_0}{x_1} = \genfrac{(}{)}{0pt}{}{\sin(3 x_0) + x_0}{x_1}
\end{equation}
F*/
#include <petscsnes.h>

/*
   User-defined routines
*/
extern PetscErrorCode FormJacobian1(SNES, Vec, Mat, Mat, void *);
extern PetscErrorCode FormFunction1(SNES, Vec, Vec, void *);
extern PetscErrorCode FormJacobian2(SNES, Vec, Mat, Mat, void *);
extern PetscErrorCode FormFunction2(SNES, Vec, Vec, void *);

int main(int argc, char **argv)
{
  SNES        snes; /* nonlinear solver context */
  KSP         ksp;  /* linear solver context */
  PC          pc;   /* preconditioner context */
  Vec         x, r; /* solution, residual vectors */
  Mat         J;    /* Jacobian matrix */
  PetscMPIInt size;
  PetscScalar pfive = .5, *xx;
  PetscBool   flg;

  PetscFunctionBeginUser;
  PetscCall(PetscInitialize(&argc, &argv, NULL, help));
  PetscCallMPI(MPI_Comm_size(PETSC_COMM_WORLD, &size));
  PetscCheck(size == 1, PETSC_COMM_WORLD, PETSC_ERR_WRONG_MPI_SIZE, "Example is only for sequential runs");

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Create nonlinear solver context
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  PetscCall(SNESCreate(PETSC_COMM_WORLD, &snes));
  PetscCall(SNESSetType(snes, SNESNEWTONLS));
  PetscCall(SNESSetOptionsPrefix(snes, "mysolver_"));

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Create matrix and vector data structures; set corresponding routines
     - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  /*
     Create vectors for solution and nonlinear function
  */
  PetscCall(VecCreate(PETSC_COMM_WORLD, &x));
  PetscCall(VecSetSizes(x, PETSC_DECIDE, 2));
  PetscCall(VecSetFromOptions(x));
  PetscCall(VecDuplicate(x, &r));

  /*
     Create Jacobian matrix data structure
  */
  PetscCall(MatCreate(PETSC_COMM_WORLD, &J));
  PetscCall(MatSetSizes(J, PETSC_DECIDE, PETSC_DECIDE, 2, 2));
  PetscCall(MatSetFromOptions(J));
  PetscCall(MatSetUp(J));

  PetscCall(PetscOptionsHasName(NULL, NULL, "-hard", &flg));
  if (!flg) {
    /*
     Set function evaluation routine and vector.
    */
    PetscCall(SNESSetFunction(snes, r, FormFunction1, NULL));

    /*
     Set Jacobian matrix data structure and Jacobian evaluation routine
    */
    PetscCall(SNESSetJacobian(snes, J, J, FormJacobian1, NULL));
  } else {
    PetscCall(SNESSetFunction(snes, r, FormFunction2, NULL));
    PetscCall(SNESSetJacobian(snes, J, J, FormJacobian2, NULL));
  }

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Customize nonlinear solver; set runtime options
   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  /*
     Set linear solver defaults for this problem. By extracting the
     KSP and PC contexts from the SNES context, we can then
     directly call any KSP and PC routines to set various options.
  */
  PetscCall(SNESGetKSP(snes, &ksp));
  PetscCall(KSPGetPC(ksp, &pc));
  PetscCall(PCSetType(pc, PCNONE));
  PetscCall(KSPSetTolerances(ksp, 1.e-4, PETSC_CURRENT, PETSC_CURRENT, 20));

  /*
     Set SNES/KSP/KSP/PC runtime options, e.g.,
         -snes_view -snes_monitor -ksp_type <ksp> -pc_type <pc>
     These options will override those specified above as long as
     SNESSetFromOptions() is called _after_ any other customization
     routines.
  */
  PetscCall(SNESSetFromOptions(snes));

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Evaluate initial guess; then solve nonlinear system
   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
  if (!flg) PetscCall(VecSet(x, pfive));
  else {
    PetscCall(VecGetArray(x, &xx));
    xx[0] = 2.0;
    xx[1] = 3.0;
    PetscCall(VecRestoreArray(x, &xx));
  }
  /*
     Note: The user should initialize the vector, x, with the initial guess
     for the nonlinear solver prior to calling SNESSolve().  In particular,
     to employ an initial guess of zero, the user should explicitly set
     this vector to zero by calling VecSet().
  */

  PetscCall(SNESSolve(snes, NULL, x));
  if (flg) {
    Vec f;
    PetscCall(VecView(x, PETSC_VIEWER_STDOUT_WORLD));
    PetscCall(SNESGetFunction(snes, &f, 0, 0));
    PetscCall(VecView(r, PETSC_VIEWER_STDOUT_WORLD));
  }

  /* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
     Free work space.  All PETSc objects should be destroyed when they
     are no longer needed.
   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */

  PetscCall(VecDestroy(&x));
  PetscCall(VecDestroy(&r));
  PetscCall(MatDestroy(&J));
  PetscCall(SNESDestroy(&snes));
  PetscCall(PetscFinalize());
  return 0;
}
/* ------------------------------------------------------------------- */
/*
   FormFunction1 - Evaluates nonlinear function, F(x).

   Input Parameters:
.  snes - the SNES context
.  x    - input vector
.  ctx  - optional user-defined context

   Output Parameter:
.  f - function vector
 */
PetscErrorCode FormFunction1(SNES snes, Vec x, Vec f, PetscCtx ctx)
{
  const PetscScalar *xx;
  PetscScalar       *ff;

  PetscFunctionBeginUser;
  /*
   Get pointers to vector data.
      - For default PETSc vectors, VecGetArray() returns a pointer to
        the data array.  Otherwise, the routine is implementation dependent.
      - You MUST call VecRestoreArray() when you no longer need access to
        the array.
   */
  PetscCall(VecGetArrayRead(x, &xx));
  PetscCall(VecGetArray(f, &ff));

  /* Compute function */
  ff[0] = xx[0] * xx[0] + xx[0] * xx[1] - 3.0;
  ff[1] = xx[0] * xx[1] + xx[1] * xx[1] - 6.0;

  /* Restore vectors */
  PetscCall(VecRestoreArrayRead(x, &xx));
  PetscCall(VecRestoreArray(f, &ff));
  PetscFunctionReturn(PETSC_SUCCESS);
}
/* ------------------------------------------------------------------- */
/*
   FormJacobian1 - Evaluates Jacobian matrix.

   Input Parameters:
.  snes - the SNES context
.  x - input vector
.  dummy - optional user-defined context (not used here)

   Output Parameters:
.  jac - Jacobian matrix
.  B - optionally different matrix used to construct the preconditioner

*/
PetscErrorCode FormJacobian1(SNES snes, Vec x, Mat jac, Mat B, void *dummy)
{
  const PetscScalar *xx;
  PetscScalar        A[4];
  PetscInt           idx[2] = {0, 1};

  PetscFunctionBeginUser;
  /*
     Get pointer to vector data
  */
  PetscCall(VecGetArrayRead(x, &xx));

  /*
     Compute Jacobian entries and insert into matrix.
      - Since this is such a small problem, we set all entries for
        the matrix at once.
  */
  A[0] = 2.0 * xx[0] + xx[1];
  A[1] = xx[0];
  A[2] = xx[1];
  A[3] = xx[0] + 2.0 * xx[1];
  PetscCall(MatSetValues(B, 2, idx, 2, idx, A, INSERT_VALUES));

  /*
     Restore vector
  */
  PetscCall(VecRestoreArrayRead(x, &xx));

  /*
     Assemble matrix
  */
  PetscCall(MatAssemblyBegin(B, MAT_FINAL_ASSEMBLY));
  PetscCall(MatAssemblyEnd(B, MAT_FINAL_ASSEMBLY));
  if (jac != B) {
    PetscCall(MatAssemblyBegin(jac, MAT_FINAL_ASSEMBLY));
    PetscCall(MatAssemblyEnd(jac, MAT_FINAL_ASSEMBLY));
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}

/* ------------------------------------------------------------------- */
PetscErrorCode FormFunction2(SNES snes, Vec x, Vec f, void *dummy)
{
  const PetscScalar *xx;
  PetscScalar       *ff;

  PetscFunctionBeginUser;
  /*
     Get pointers to vector data.
       - For default PETSc vectors, VecGetArray() returns a pointer to
         the data array.  Otherwise, the routine is implementation dependent.
       - You MUST call VecRestoreArray() when you no longer need access to
         the array.
  */
  PetscCall(VecGetArrayRead(x, &xx));
  PetscCall(VecGetArray(f, &ff));

  /*
     Compute function
  */
  ff[0] = PetscSinScalar(3.0 * xx[0]) + xx[0];
  ff[1] = xx[1];

  /*
     Restore vectors
  */
  PetscCall(VecRestoreArrayRead(x, &xx));
  PetscCall(VecRestoreArray(f, &ff));
  PetscFunctionReturn(PETSC_SUCCESS);
}
/* ------------------------------------------------------------------- */
PetscErrorCode FormJacobian2(SNES snes, Vec x, Mat jac, Mat B, void *dummy)
{
  const PetscScalar *xx;
  PetscScalar        A[4];
  PetscInt           idx[2] = {0, 1};

  PetscFunctionBeginUser;
  /*
     Get pointer to vector data
  */
  PetscCall(VecGetArrayRead(x, &xx));

  /*
     Compute Jacobian entries and insert into matrix.
      - Since this is such a small problem, we set all entries for
        the matrix at once.
  */
  A[0] = 3.0 * PetscCosScalar(3.0 * xx[0]) + 1.0;
  A[1] = 0.0;
  A[2] = 0.0;
  A[3] = 1.0;
  PetscCall(MatSetValues(B, 2, idx, 2, idx, A, INSERT_VALUES));

  /*
     Restore vector
  */
  PetscCall(VecRestoreArrayRead(x, &xx));

  /*
     Assemble matrix
  */
  PetscCall(MatAssemblyBegin(B, MAT_FINAL_ASSEMBLY));
  PetscCall(MatAssemblyEnd(B, MAT_FINAL_ASSEMBLY));
  if (jac != B) {
    PetscCall(MatAssemblyBegin(jac, MAT_FINAL_ASSEMBLY));
    PetscCall(MatAssemblyEnd(jac, MAT_FINAL_ASSEMBLY));
  }
  PetscFunctionReturn(PETSC_SUCCESS);
}
```

Example 4 (unknown):
```unknown
SNESCreate()
```

---

## SNES_NORM_ALWAYS#

**URL:** https://petsc.org/release/manualpages/SNES/SNES_NORM_ALWAYS/

**Contents:**
- SNES_NORM_ALWAYS#
- Note#
- See Also#
- Level#
- Location#

Compute the function and its L2 norm at each iteration.

Most solvers will use this no matter what norm type is passed to them.

SNES: Nonlinear Solvers, SNESNormSchedule, SNES, SNESSetNormSchedule(), SNES_NORM_NONE

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESNormSchedule
```

Example 2 (unknown):
```unknown
SNESSetNormSchedule()
```

Example 3 (unknown):
```unknown
SNES_NORM_NONE
```

---

## SNES_NORM_FINAL_ONLY#

**URL:** https://petsc.org/release/manualpages/SNES/SNES_NORM_FINAL_ONLY/

**Contents:**
- SNES_NORM_FINAL_ONLY#
- Note#
- See Also#
- Level#
- Location#

Compute the function and its L2 norm on only the final iteration.

For solvers that require the computation of the L2 norm of the function as part of the method, behaves exactly as SNES_NORM_DEFAULT. This method is useful when the function is gotten after SNESSolve() and used in subsequent computation for methods that do not need the norm computed during the rest of the solution procedure.

SNES: Nonlinear Solvers, SNESNormSchedule, SNES, SNESSetNormSchedule(), SNES_NORM_INITIAL_ONLY, SNES_NORM_INITIAL_FINAL_ONLY

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNES_NORM_DEFAULT
```

Example 2 (unknown):
```unknown
SNESSolve()
```

Example 3 (unknown):
```unknown
SNESNormSchedule
```

Example 4 (unknown):
```unknown
SNESSetNormSchedule()
```

---

## SNES_NORM_INITIAL_FINAL_ONLY#

**URL:** https://petsc.org/release/manualpages/SNES/SNES_NORM_INITIAL_FINAL_ONLY/

**Contents:**
- SNES_NORM_INITIAL_FINAL_ONLY#
- Note#
- See Also#
- Level#
- Location#

Compute the function and its L2 norm on only the initial and final iterations.

This method combines the benefits of SNES_NORM_INITIAL_ONLY and SNES_NORM_FINAL_ONLY.

SNES: Nonlinear Solvers, SNESNormSchedule, SNES, SNESSetNormSchedule(), SNES_NORM_SNES_NORM_INITIAL_ONLY, SNES_NORM_FINAL_ONLY

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNES_NORM_INITIAL_ONLY
```

Example 2 (unknown):
```unknown
SNES_NORM_FINAL_ONLY
```

Example 3 (unknown):
```unknown
SNESNormSchedule
```

Example 4 (unknown):
```unknown
SNESSetNormSchedule()
```

---

## SNES_NORM_INITIAL_ONLY#

**URL:** https://petsc.org/release/manualpages/SNES/SNES_NORM_INITIAL_ONLY/

**Contents:**
- SNES_NORM_INITIAL_ONLY#
- Notes#
- See Also#
- Level#
- Location#

Compute the function and its L2 at iteration 0, but do not update it.

This method is useful in composed methods, when a true solution might actually be found before SNESSolve() is called. This option enables the solve to abort on the zeroth iteration if this is the case.

For solvers that require the computation of the L2 norm of the function as part of the method, this merely cancels the norm computation at the last iteration (if possible).

SNES: Nonlinear Solvers, SNESNormSchedule, SNES, SNESSetNormSchedule(), SNES_NORM_FINAL_ONLY, SNES_NORM_INITIAL_FINAL_ONLY

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (unknown):
```unknown
SNESNormSchedule
```

Example 3 (unknown):
```unknown
SNESSetNormSchedule()
```

Example 4 (unknown):
```unknown
SNES_NORM_FINAL_ONLY
```

---

## SNES_NORM_NONE#

**URL:** https://petsc.org/release/manualpages/SNES/SNES_NORM_NONE/

**Contents:**
- SNES_NORM_NONE#
- Note#
- See Also#
- Level#
- Location#

Don’t compute function and its L2 norm when possible

This is most useful for stationary solvers with a fixed number of iterations used as smoothers.

SNES: Nonlinear Solvers, SNESNormSchedule, SNES, SNESSetNormSchedule(), SNES_NORM_DEFAULT

Index of all SNES routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESNormSchedule
```

Example 2 (unknown):
```unknown
SNESSetNormSchedule()
```

Example 3 (unknown):
```unknown
SNES_NORM_DEFAULT
```

---
