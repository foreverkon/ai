# Time stepping and sensitivity analysis

## CharacteristicCreate#

**URL:** https://petsc.org/release/manualpages/Characteristic/CharacteristicCreate/

**Contents:**
- CharacteristicCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Creates a Characteristic context for use with the Method of Characteristics

comm - MPI communicator

c - the Characteristic context

Characteristic, CharacteristicDestroy()

src/ts/characteristic/interface/characteristic.c

CharacteristicCreate_DA() in src/ts/characteristic/impls/da/slda.c

Index of all Characteristic routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
Characteristic
```

Example 2 (unknown):
```unknown
#include "petsccharacteristic.h" 
PetscErrorCode CharacteristicCreate(MPI_Comm comm, Characteristic *c)
```

Example 3 (unknown):
```unknown
Characteristic
```

Example 4 (unknown):
```unknown
Characteristic
```

---

## CharacteristicDestroy#

**URL:** https://petsc.org/release/manualpages/Characteristic/CharacteristicDestroy/

**Contents:**
- CharacteristicDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Destroys a Characteristic context created with CharacteristicCreate()

c - the Characteristic context

Characteristic, CharacteristicCreate()

src/ts/characteristic/interface/characteristic.c

CharacteristicDestroy_DA() in src/ts/characteristic/impls/da/slda.c

Index of all Characteristic routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
Characteristic
```

Example 2 (unknown):
```unknown
CharacteristicCreate()
```

Example 3 (unknown):
```unknown
#include "petsccharacteristic.h" 
PetscErrorCode CharacteristicDestroy(Characteristic *c)
```

Example 4 (unknown):
```unknown
Characteristic
```

---

## CharacteristicFinalizePackage#

**URL:** https://petsc.org/release/manualpages/Characteristic/CharacteristicFinalizePackage/

**Contents:**
- CharacteristicFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys everything in the Characteristics package. It is called from PetscFinalize().

TS: Scalable ODE and DAE Solvers, PetscFinalize(), CharacteristicInitializePackage()

src/ts/characteristic/interface/slregis.c

Index of all Characteristic routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
Characteristics
```

Example 2 (unknown):
```unknown
PetscFinalize()
```

Example 3 (unknown):
```unknown
PetscErrorCode CharacteristicFinalizePackage(void)
```

Example 4 (unknown):
```unknown
PetscFinalize()
```

---

## CharacteristicInitializePackage#

**URL:** https://petsc.org/release/manualpages/Characteristic/CharacteristicInitializePackage/

**Contents:**
- CharacteristicInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function initializes everything in the Characteristic package. It is called from PetscDLLibraryRegister() when using dynamic libraries, and on the first call to CharacteristicCreate() when using static libraries.

TS: Scalable ODE and DAE Solvers, PetscInitialize(), CharacteristicFinalizePackage()

src/ts/characteristic/interface/slregis.c

Index of all Characteristic routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode CharacteristicInitializePackage(void)
```

Example 2 (unknown):
```unknown
PetscInitialize()
```

Example 3 (unknown):
```unknown
CharacteristicFinalizePackage()
```

---

## CharacteristicRegisterAll#

**URL:** https://petsc.org/release/manualpages/Characteristic/CharacteristicRegisterAll/

**Contents:**
- CharacteristicRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the methods in the Characteristic package.

TS: Scalable ODE and DAE Solvers, CharacteristicRegisterDestroy()

src/ts/characteristic/interface/mocregis.c

Index of all Characteristic routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
Characteristic
```

Example 2 (unknown):
```unknown
#include "petsccharacteristic.h" 
PetscErrorCode CharacteristicRegisterAll(void)
```

Example 3 (unknown):
```unknown
CharacteristicRegisterDestroy()
```

---

## CharacteristicRegister#

**URL:** https://petsc.org/release/manualpages/Characteristic/CharacteristicRegister/

**Contents:**
- CharacteristicRegister#
- Synopsis#
- Input Parameters#
- Example Usage#
- Notes#
- See Also#
- Level#
- Location#

Adds an approarch to the method of characteristics package.

Not Collective, No Fortran Support

sname - name of a new approach

function - routine to create method context

Then, your Characteristic type can be chosen with the procedural interface via

or at runtime via the option

CharacteristicRegister() may be called multiple times to add several approaches.

TS: Scalable ODE and DAE Solvers, CharacteristicRegisterAll(), CharacteristicRegisterDestroy()

src/ts/characteristic/interface/characteristic.c

Index of all Characteristic routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsccharacteristic.h" 
PetscErrorCode CharacteristicRegister(const char sname[], PetscErrorCode (*function)(Characteristic))
```

Example 2 (unknown):
```unknown
CharacteristicRegister("my_char", MyCharCreate);
```

Example 3 (unknown):
```unknown
CharacteristicCreate(MPI_Comm, Characteristic* &char);
    CharacteristicSetType(char,"my_char");
```

Example 4 (unknown):
```unknown
-characteristic_type my_char
```

---

## CharacteristicSetFieldInterpolationLocal#

**URL:** https://petsc.org/release/manualpages/Characteristic/CharacteristicSetFieldInterpolationLocal/

**Contents:**
- CharacteristicSetFieldInterpolationLocal#
- Synopsis#
- Input Parameters#
- Calling sequence of interp#
- See Also#
- Level#
- Location#

Sets the routine used to interpolate the field being advected at the foot of a characteristic using a locally-accessible array

c - the Characteristic context

da - the DM describing the layout of the field vector

v - the field vector to be advected

numComponents - the number of field components to interpolate

components - the indices of the field components in v

interp - the interpolation routine, called with a local array pointer rather than a Vec

ctx - context passed to the interpolation routine

array - the locally-accessible array of the field vector obtained from the DM

interpIndices - the coordinates at which to interpolate

numComponents - the number of components to interpolate

components - the indices of the components in the array

values - the interpolated values, one per component per point

ctx - the application context

TS: Scalable ODE and DAE Solvers, Characteristic, CharacteristicSetFieldInterpolation(), CharacteristicSetVelocityInterpolationLocal()

src/ts/characteristic/interface/characteristic.c

Index of all Characteristic routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsccharacteristic.h" 
PetscErrorCode CharacteristicSetFieldInterpolationLocal(Characteristic c, DM da, Vec v, PetscInt numComponents, PetscInt components[], PetscErrorCode (*interp)(void *array, PetscReal interpIndices[], PetscInt numComponents, PetscInt components[], PetscScalar values[], PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
Characteristic
```

Example 3 (unknown):
```unknown
Characteristic
```

Example 4 (unknown):
```unknown
CharacteristicSetFieldInterpolation()
```

---

## CharacteristicSetFieldInterpolation#

**URL:** https://petsc.org/release/manualpages/Characteristic/CharacteristicSetFieldInterpolation/

**Contents:**
- CharacteristicSetFieldInterpolation#
- Synopsis#
- Input Parameters#
- Calling sequence of interp#
- See Also#
- Level#
- Location#

Sets the routine used to interpolate the field being advected at the foot of a characteristic

c - the Characteristic context

da - the DM describing the layout of the field vector

v - the field vector to be advected

numComponents - the number of field components to interpolate

components - the indices of the field components in v

interp - the interpolation routine, called with the global vector

ctx - context passed to the interpolation routine

v - the field Vec from which to interpolate

interpIndices - the coordinates at which to interpolate

numComponents - the number of components to interpolate

components - the indices of the components in v

values - the interpolated values, one per component per point

ctx - the application context

TS: Scalable ODE and DAE Solvers, Characteristic, CharacteristicSetFieldInterpolationLocal(), CharacteristicSetVelocityInterpolation()

src/ts/characteristic/interface/characteristic.c

Index of all Characteristic routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsccharacteristic.h" 
PetscErrorCode CharacteristicSetFieldInterpolation(Characteristic c, DM da, Vec v, PetscInt numComponents, PetscInt components[], PetscErrorCode (*interp)(Vec v, PetscReal interpIndices[], PetscInt numComponents, PetscInt components[], PetscScalar values[], PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
Characteristic
```

Example 3 (unknown):
```unknown
Characteristic
```

Example 4 (unknown):
```unknown
CharacteristicSetFieldInterpolationLocal()
```

---

## CharacteristicSetType#

**URL:** https://petsc.org/release/manualpages/Characteristic/CharacteristicSetType/

**Contents:**
- CharacteristicSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Builds Characteristic for a particular solver.

c - the method of characteristics context

type - a known method

-characteristic_type method - Sets the method; use -help for a list of available methods

See “include/petsccharacteristic.h” for available methods

TS: Scalable ODE and DAE Solvers, CharacteristicType

src/ts/characteristic/interface/characteristic.c

Index of all Characteristic routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsccharacteristic.h" 
PetscErrorCode CharacteristicSetType(Characteristic c, CharacteristicType type)
```

Example 2 (unknown):
```unknown
CharacteristicType
```

---

## CharacteristicSetUp#

**URL:** https://petsc.org/release/manualpages/Characteristic/CharacteristicSetUp/

**Contents:**
- CharacteristicSetUp#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Sets up the internal data structures for the later use of a Charactoristic .

c - context obtained from CharacteristicCreate()

TS: Scalable ODE and DAE Solvers, Characteristic, CharacteristicCreate(), CharacteristicSolve(), CharacteristicDestroy()

src/ts/characteristic/interface/characteristic.c

CharacteristicSetUp_DA() in src/ts/characteristic/impls/da/slda.c

Index of all Characteristic routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
Charactoristic
```

Example 2 (unknown):
```unknown
#include "petsccharacteristic.h" 
PetscErrorCode CharacteristicSetUp(Characteristic c)
```

Example 3 (unknown):
```unknown
Characteristic
```

Example 4 (unknown):
```unknown
CharacteristicCreate()
```

---

## CharacteristicSetVelocityInterpolationLocal#

**URL:** https://petsc.org/release/manualpages/Characteristic/CharacteristicSetVelocityInterpolationLocal/

**Contents:**
- CharacteristicSetVelocityInterpolationLocal#
- Synopsis#
- Input Parameters#
- Calling sequence of interp#
- See Also#
- Level#
- Location#

Sets the routine used to interpolate the velocity field along a characteristic using a locally-accessible array

c - the Characteristic context

da - the DM describing the layout of the velocity vectors

v - the current velocity vector

vOld - the previous-time-step velocity vector

numComponents - the number of velocity components to interpolate

components - the indices of the velocity components in v and vOld

interp - the interpolation routine, called with a local array pointer rather than a Vec

ctx - context passed to the interpolation routine

array - the locally-accessible array of the velocity vector obtained from the DM

interpIndices - the coordinates at which to interpolate

numComponents - the number of components to interpolate

components - the indices of the components in the array

values - the interpolated values, one per component per point

ctx - the application context

TS: Scalable ODE and DAE Solvers, Characteristic, CharacteristicSetVelocityInterpolation(), CharacteristicSetFieldInterpolationLocal()

src/ts/characteristic/interface/characteristic.c

Index of all Characteristic routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsccharacteristic.h" 
PetscErrorCode CharacteristicSetVelocityInterpolationLocal(Characteristic c, DM da, Vec v, Vec vOld, PetscInt numComponents, PetscInt components[], PetscErrorCode (*interp)(void *array, PetscReal interpIndices[], PetscInt numComponents, PetscInt components[], PetscScalar values[], PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
Characteristic
```

Example 3 (unknown):
```unknown
Characteristic
```

Example 4 (unknown):
```unknown
CharacteristicSetVelocityInterpolation()
```

---

## CharacteristicSetVelocityInterpolation#

**URL:** https://petsc.org/release/manualpages/Characteristic/CharacteristicSetVelocityInterpolation/

**Contents:**
- CharacteristicSetVelocityInterpolation#
- Synopsis#
- Input Parameters#
- Calling sequence of interp#
- See Also#
- Level#
- Location#

Sets the routine used to interpolate the velocity field at points along a characteristic

c - the Characteristic context

da - the DM describing the layout of the velocity vectors

v - the current velocity vector

vOld - the previous-time-step velocity vector

numComponents - the number of velocity components to interpolate

components - the indices of the velocity components in v and vOld

interp - the interpolation routine, called with the global vector

ctx - context passed to the interpolation routine

v - the velocity Vec from which to interpolate

interpIndices - the coordinates at which to interpolate

numComponents - the number of components to interpolate

components - the indices of the components in v

values - the interpolated values, one per component per point

ctx - the application context

TS: Scalable ODE and DAE Solvers, Characteristic, CharacteristicSetVelocityInterpolationLocal(), CharacteristicSetFieldInterpolation()

src/ts/characteristic/interface/characteristic.c

Index of all Characteristic routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsccharacteristic.h" 
PetscErrorCode CharacteristicSetVelocityInterpolation(Characteristic c, DM da, Vec v, Vec vOld, PetscInt numComponents, PetscInt components[], PetscErrorCode (*interp)(Vec v, PetscReal interpIndices[], PetscInt numComponents, PetscInt components[], PetscScalar values[], PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
Characteristic
```

Example 3 (unknown):
```unknown
Characteristic
```

Example 4 (unknown):
```unknown
CharacteristicSetVelocityInterpolationLocal()
```

---

## CharacteristicSolve#

**URL:** https://petsc.org/release/manualpages/Characteristic/CharacteristicSolve/

**Contents:**
- CharacteristicSolve#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Apply the Method of Characteristics solver

c - context obtained from CharacteristicCreate()

solution - vector holding the solution

TS: Scalable ODE and DAE Solvers, Characteristic, CharacteristicCreate(), CharacteristicDestroy()

src/ts/characteristic/interface/characteristic.c

Index of all Characteristic routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsccharacteristic.h" 
PetscErrorCode CharacteristicSolve(Characteristic c, PetscReal dt, Vec solution)
```

Example 2 (unknown):
```unknown
CharacteristicCreate()
```

Example 3 (unknown):
```unknown
Characteristic
```

Example 4 (unknown):
```unknown
CharacteristicCreate()
```

---

## CharacteristicType#

**URL:** https://petsc.org/release/manualpages/Characteristic/CharacteristicType/

**Contents:**
- CharacteristicType#
- Synopsis#
- See Also#
- Level#
- Location#

String with the name of a characteristics method.

CharacteristicSetType(), Characteristic

include/petsccharacteristic.h

Index of all Characteristic routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef const char *CharacteristicType;
#define CHARACTERISTICDA "da"
```

Example 2 (unknown):
```unknown
CharacteristicSetType()
```

Example 3 (unknown):
```unknown
Characteristic
```

---

## Characteristic#

**URL:** https://petsc.org/release/manualpages/Characteristic/Characteristic/

**Contents:**
- Characteristic#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Abstract PETSc object that manages method of characteristics solves

CharacteristicCreate(), CharacteristicSetType(), CharacteristicType, SNES, TS, PC, KSP

include/petsccharacteristic.h

src/ts/tutorials/ex9.c

_p_Characteristic in include/petsc/private/characteristicimpl.h Characteristic_DA in src/ts/characteristic/impls/da/slda.h

Index of all Characteristic routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_Characteristic *Characteristic;
```

Example 2 (unknown):
```unknown
CharacteristicCreate()
```

Example 3 (unknown):
```unknown
CharacteristicSetType()
```

Example 4 (unknown):
```unknown
CharacteristicType
```

---

## DMCopyDMTS#

**URL:** https://petsc.org/release/manualpages/TS/DMCopyDMTS/

**Contents:**
- DMCopyDMTS#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

copies a DMTS context to a new DM

dmsrc - DM to obtain context from

dmdest - DM to add context to

The context is copied by reference. This function does not ensure that a context exists.

TS: Scalable ODE and DAE Solvers, DMTS, DMGetDMTS(), TSSetDM()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMCopyDMTS(DM dmsrc, DM dmdest)
```

Example 2 (unknown):
```unknown
DMGetDMTS()
```

---

## DMDAMapCoordsToPeriodicDomain#

**URL:** https://petsc.org/release/manualpages/Characteristic/DMDAMapCoordsToPeriodicDomain/

**Contents:**
- DMDAMapCoordsToPeriodicDomain#
- Synopsis#
- Input Parameter#
- Input/Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Maps a (x, y) coordinate pair that lies outside a 2D DMDA domain back into the domain along any periodic boundaries

da - the 2D DMDA context

x - the x coordinate; wrapped in place if the x boundary is periodic

y - the y coordinate; wrapped in place if the y boundary is periodic

Coordinates along non-periodic boundaries are left unchanged. This helper is used internally by the method-of-characteristics solver on structured grids.

TS: Scalable ODE and DAE Solvers, Characteristic, DMDA, CharacteristicSolve()

src/ts/characteristic/impls/da/slda.c

Index of all Characteristic routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsccharacteristic.h"  
PetscErrorCode DMDAMapCoordsToPeriodicDomain(DM da, PetscScalar *x, PetscScalar *y)
```

Example 2 (unknown):
```unknown
Characteristic
```

Example 3 (unknown):
```unknown
CharacteristicSolve()
```

---

## DMDATSIFunctionLocalFn#

**URL:** https://petsc.org/release/manualpages/TS/DMDATSIFunctionLocalFn/

**Contents:**
- DMDATSIFunctionLocalFn#
- Synopsis#
- Calling Sequence#
- Note#
- See Also#
- Level#
- Location#

A prototype of a local residual evaluation function for use with DMDA that would be passed to DMDATSSetIFunctionLocal()

info - defines the subdomain to evaluate the residual on

t - time at which to evaluate residual

x - array of local state information

xdot - array of local time derivative information

imode - output array of local function evaluation information

ctx - optional context

The deprecated DMDATSIFunctionLocal still works as a replacement for DMDATSIFunctionLocalFn *.

DMDA, DMDATSSetIFunctionLocal(), DMDATSIJacobianLocalFn, TSIFunctionFn

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDATSSetIFunctionLocal()
```

Example 2 (cpp):
```cpp
#include <petscts.h> 
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode DMDATSIFunctionLocalFn(DMDALocalInfo *info, PetscReal t, void *x, void *xdot, void *imode, PetscCtx ctx);
```

Example 3 (unknown):
```unknown
DMDATSIFunctionLocal
```

Example 4 (unknown):
```unknown
DMDATSIFunctionLocalFn
```

---

## DMDATSIJacobianLocalFn#

**URL:** https://petsc.org/release/manualpages/TS/DMDATSIJacobianLocalFn/

**Contents:**
- DMDATSIJacobianLocalFn#
- Synopsis#
- Calling Sequence#
- Note#
- See Also#
- Level#
- Location#

A prototype of a local residual evaluation function for use with DMDA that would be passed to DMDATSSetIJacobianLocal()

info - defines the subdomain to evaluate the residual on

t - time at which to evaluate the jacobian

x - array of local state information

xdot - time derivative at this state

shift - see TSSetIJacobian() for the meaning of this parameter

B - matrix from which to construct the preconditioner; often same as J

ctx - optional context

The deprecated DMDATSIJacobianLocal still works as a replacement for DMDATSIJacobianLocalFn *.

DMDA, DMDATSSetIJacobianLocal(), TSIJacobianFn, DMDATSIFunctionLocalFn, DMDATSRHSFunctionLocalFn, DMDATSRHSJacobianlocal()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDATSSetIJacobianLocal()
```

Example 2 (cpp):
```cpp
#include <petscts.h> 
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode DMDATSIJacobianLocalFn(DMDALocalInfo *info, PetscReal t, void *x, void *xdot, PetscReal shift, Mat J, Mat B, PetscCtx ctx);
```

Example 3 (unknown):
```unknown
TSSetIJacobian()
```

Example 4 (unknown):
```unknown
DMDATSIJacobianLocal
```

---

## DMDATSRHSFunctionLocalFn#

**URL:** https://petsc.org/release/manualpages/TS/DMDATSRHSFunctionLocalFn/

**Contents:**
- DMDATSRHSFunctionLocalFn#
- Synopsis#
- Calling Sequence#
- Note#
- See Also#
- Level#
- Location#

A prototype of a local TS right-hand side residual evaluation function for use with DMDA that would be passed to DMDATSSetRHSFunctionLocal()

info - defines the subdomain to evaluate the residual on

t - time at which to evaluate residual

x - array of local state information

f - output array of local residual information

ctx - optional application context

The deprecated DMDATSRHSFunctionLocal still works as a replacement for DMDATSRHSFunctionLocalFn *.

DMDA, DMDATSSetRHSFunctionLocal(), TSRHSFunctionFn, DMDATSRHSJacobianLocalFn, DMDATSIJacobianLocalFn, DMDATSIFunctionLocalFn

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDATSSetRHSFunctionLocal()
```

Example 2 (cpp):
```cpp
#include <petscts.h> 
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode DMDATSRHSFunctionLocalFn(DMDALocalInfo *info, PetscReal t, void *x, void *f, PetscCtx ctx);
```

Example 3 (unknown):
```unknown
DMDATSRHSFunctionLocal
```

Example 4 (unknown):
```unknown
DMDATSRHSFunctionLocalFn
```

---

## DMDATSRHSJacobianLocalFn#

**URL:** https://petsc.org/release/manualpages/TS/DMDATSRHSJacobianLocalFn/

**Contents:**
- DMDATSRHSJacobianLocalFn#
- Synopsis#
- Calling Sequence#
- Note#
- See Also#
- Level#
- Location#

A prototype of a local residual evaluation function for use with DMDA that would be passed to DMDATSSetRHSJacobianLocal()

info - defines the subdomain to evaluate the residual on

t - time at which to evaluate residual

x - array of local state information

B - matrix from which to construct the preconditioner; often same as J

ctx - optional context

The deprecated DMDATSRHSJacobianLocal still works as a replacement for DMDATSRHSJacobianLocalFn *.

DMDA, DMDATSSetRHSJacobianLocal(), TSRHSJacobianFn, DMDATSRHSFunctionLocalFn, DMDATSIJacobianLocalFn, DMDATSIFunctionLocalFn

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMDATSSetRHSJacobianLocal()
```

Example 2 (cpp):
```cpp
#include <petscts.h> 
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode DMDATSRHSJacobianLocalFn(DMDALocalInfo *info, PetscReal t, void *x, Mat J, Mat B, PetscCtx ctx);
```

Example 3 (unknown):
```unknown
DMDATSRHSJacobianLocal
```

Example 4 (unknown):
```unknown
DMDATSRHSJacobianLocalFn
```

---

## DMDATSSetIFunctionLocal#

**URL:** https://petsc.org/release/manualpages/TS/DMDATSSetIFunctionLocal/

**Contents:**
- DMDATSSetIFunctionLocal#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

set a local residual evaluation function for use with DMDA

dm - DM to associate callback with

imode - the insert mode of the function

func - local residual evaluation, see DMDATSIFunctionLocalFn for the calling sequence

ctx - optional context for local residual evaluation

TS: Scalable ODE and DAE Solvers, DMDA, DMDATSIFunctionLocalFn, DMTSSetIFunction(), DMDATSSetIJacobianLocal(), DMDASNESSetFunctionLocal()

src/ts/utils/dmdats.c

src/ts/tutorials/ex26.c src/ts/tutorials/ex29.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h" 
#include "petscts.h" 
PetscErrorCode DMDATSSetIFunctionLocal(DM dm, InsertMode imode, DMDATSIFunctionLocalFn *func, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMDATSIFunctionLocalFn
```

Example 3 (unknown):
```unknown
DMDATSIFunctionLocalFn
```

Example 4 (unknown):
```unknown
DMTSSetIFunction()
```

---

## DMDATSSetIJacobianLocal#

**URL:** https://petsc.org/release/manualpages/TS/DMDATSSetIJacobianLocal/

**Contents:**
- DMDATSSetIJacobianLocal#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

set a local residual evaluation function for use with DMDA

dm - DM to associate callback with

func - local residual evaluation, see DMDATSIJacobianLocalFn for the calling sequence

ctx - optional context for local residual evaluation

TS: Scalable ODE and DAE Solvers, DMDA, DMDATSIJacobianLocalFn, DMTSSetIJacobian(), DMDATSSetIFunctionLocal(), DMDASNESSetJacobianLocal()

src/ts/utils/dmdats.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h" 
#include "petscts.h" 
PetscErrorCode DMDATSSetIJacobianLocal(DM dm, DMDATSIJacobianLocalFn *func, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMDATSIJacobianLocalFn
```

Example 3 (unknown):
```unknown
DMDATSIJacobianLocalFn
```

Example 4 (unknown):
```unknown
DMTSSetIJacobian()
```

---

## DMDATSSetRHSFunctionLocal#

**URL:** https://petsc.org/release/manualpages/TS/DMDATSSetRHSFunctionLocal/

**Contents:**
- DMDATSSetRHSFunctionLocal#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

set a local residual evaluation function for use with DMDA

dm - DM to associate callback with

imode - insert mode for the residual

func - local residual evaluation, see DMDATSRHSFunctionLocalFn for the calling sequence

ctx - optional context for local residual evaluation

TS: Scalable ODE and DAE Solvers, DMDA, DMDATSRHSFunctionLocalFn, TS, TSSetRHSFunction(), DMTSSetRHSFunction(), DMDATSSetRHSJacobianLocal(), DMDASNESSetFunctionLocal()

src/ts/utils/dmdats.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h" 
#include "petscts.h" 
PetscErrorCode DMDATSSetRHSFunctionLocal(DM dm, InsertMode imode, DMDATSRHSFunctionLocalFn *func, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMDATSRHSFunctionLocalFn
```

Example 3 (unknown):
```unknown
DMDATSRHSFunctionLocalFn
```

Example 4 (unknown):
```unknown
TSSetRHSFunction()
```

---

## DMDATSSetRHSJacobianLocal#

**URL:** https://petsc.org/release/manualpages/TS/DMDATSSetRHSJacobianLocal/

**Contents:**
- DMDATSSetRHSJacobianLocal#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

set a local residual evaluation function for use with DMDA

dm - DM to associate callback with

func - local RHS Jacobian evaluation routine, see DMDATSRHSJacobianLocalFn for the calling sequence

ctx - optional context for local jacobian evaluation

TS: Scalable ODE and DAE Solvers, DMDA, DMDATSRHSJacobianLocalFn, DMTSSetRHSJacobian(), DMDATSSetRHSFunctionLocal(), DMDASNESSetJacobianLocal()

src/ts/utils/dmdats.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h" 
#include "petscts.h" 
PetscErrorCode DMDATSSetRHSJacobianLocal(DM dm, DMDATSRHSJacobianLocalFn *func, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMDATSRHSJacobianLocalFn
```

Example 3 (unknown):
```unknown
DMDATSRHSJacobianLocalFn
```

Example 4 (unknown):
```unknown
DMTSSetRHSJacobian()
```

---

## DMGetDMTSWrite#

**URL:** https://petsc.org/release/manualpages/TS/DMGetDMTSWrite/

**Contents:**
- DMGetDMTSWrite#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

get write access to private DMTS context from a DM

dm - DM to be used with TS

tsdm - private DMTS context

TS: Scalable ODE and DAE Solvers, DMTS, DMGetDMTS()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMGetDMTSWrite(DM dm, DMTS *tsdm)
```

Example 2 (unknown):
```unknown
DMGetDMTS()
```

---

## DMGetDMTS#

**URL:** https://petsc.org/release/manualpages/TS/DMGetDMTS/

**Contents:**
- DMGetDMTS#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

get read-only private DMTS context from a DM

dm - DM to be used with TS

tsdm - private DMTS context

Use DMGetDMTSWrite() if write access is needed. The DMTSSetXXX() API should be used wherever possible.

TS: Scalable ODE and DAE Solvers, DMTS, DMGetDMTSWrite()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMGetDMTS(DM dm, DMTS *tsdm)
```

Example 2 (unknown):
```unknown
DMGetDMTSWrite()
```

Example 3 (unknown):
```unknown
DMTSSetXXX()
```

Example 4 (unknown):
```unknown
DMGetDMTSWrite()
```

---

## DMPlexTSComputeBoundary#

**URL:** https://petsc.org/release/manualpages/TS/DMPlexTSComputeBoundary/

**Contents:**
- DMPlexTSComputeBoundary#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Insert the essential boundary values into the local input locX and/or its time derivative locX_t using pointwise functions specified by the user

locX - Local solution

locX_t - Local solution time derivative, or NULL

ctx - The application context

TS: Scalable ODE and DAE Solvers, DMPLEX, TS, DMPlexComputeJacobianActionFEM()

src/ts/utils/dmplexts.c

src/ts/tutorials/ex45.c src/ts/tutorials/ex11.c src/ts/tutorials/ex46.c src/ts/tutorials/ex30.c src/ts/tutorials/ex18.c src/ts/tutorials/ex76.c src/ts/tutorials/ex48.c src/ts/tutorials/ex77.c src/ts/tutorials/ex53.c src/ts/tutorials/ex47.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscts.h" 
PetscErrorCode DMPlexTSComputeBoundary(DM dm, PetscReal time, Vec locX, Vec locX_t, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMPlexComputeJacobianActionFEM()
```

---

## DMPlexTSComputeIFunctionFEM#

**URL:** https://petsc.org/release/manualpages/TS/DMPlexTSComputeIFunctionFEM/

**Contents:**
- DMPlexTSComputeIFunctionFEM#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Form the local residual locF from the local input locX using pointwise functions specified by the user

locX - Local solution

locX_t - Local solution time derivative, or NULL

ctx - The application context

locF - Local output vector

TS: Scalable ODE and DAE Solvers, DMPLEX, TS, DMPlexTSComputeRHSFunctionFEM()

src/ts/utils/dmplexts.c

src/ts/tutorials/ex45.c src/ts/tutorials/ex46.c src/ts/tutorials/ex30.c src/ts/tutorials/ex18.c src/ts/tutorials/ex76.c src/ts/tutorials/ex48.c src/ts/tutorials/ex77.c src/ts/tutorials/ex53.c src/ts/tutorials/ex47.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscts.h" 
PetscErrorCode DMPlexTSComputeIFunctionFEM(DM dm, PetscReal time, Vec locX, Vec locX_t, Vec locF, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMPlexTSComputeRHSFunctionFEM()
```

---

## DMPlexTSComputeIJacobianFEM#

**URL:** https://petsc.org/release/manualpages/TS/DMPlexTSComputeIJacobianFEM/

**Contents:**
- DMPlexTSComputeIJacobianFEM#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#

Form the Jacobian Jac from the local input locX using pointwise functions specified by the user

locX - Local solution

locX_t - Local solution time derivative, or NULL

X_tShift - The multiplicative parameter for dF/du_t

ctx - The application context

JacP - an additional approximation for the Jacobian to be used to compute the preconditioner (often is Jac)

TS: Scalable ODE and DAE Solvers, TS, DM, DMPlexTSComputeIFunctionFEM(), DMPlexTSComputeRHSFunctionFEM()

src/ts/utils/dmplexts.c

src/ts/tutorials/ex45.c src/ts/tutorials/ex46.c src/ts/tutorials/ex30.c src/ts/tutorials/ex18.c src/ts/tutorials/ex76.c src/ts/tutorials/ex48.c src/ts/tutorials/ex77.c src/ts/tutorials/ex53.c src/ts/tutorials/ex47.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscts.h" 
PetscErrorCode DMPlexTSComputeIJacobianFEM(DM dm, PetscReal time, Vec locX, Vec locX_t, PetscReal X_tShift, Mat Jac, Mat JacP, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMPlexTSComputeIFunctionFEM()
```

Example 3 (unknown):
```unknown
DMPlexTSComputeRHSFunctionFEM()
```

---

## DMPlexTSComputeRHSFunctionFEM#

**URL:** https://petsc.org/release/manualpages/TS/DMPlexTSComputeRHSFunctionFEM/

**Contents:**
- DMPlexTSComputeRHSFunctionFEM#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Form the local residual locG from the local input locX using pointwise functions specified by the user

locX - Local solution

ctx - The application context

locG - Local output vector

TS: Scalable ODE and DAE Solvers, TS, DM, DMPlexTSComputeIFunctionFEM(), DMPlexTSComputeIJacobianFEM()

src/ts/utils/dmplexts.c

src/ts/tutorials/ex45.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscts.h" 
PetscErrorCode DMPlexTSComputeRHSFunctionFEM(DM dm, PetscReal time, Vec locX, Vec locG, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMPlexTSComputeIFunctionFEM()
```

Example 3 (unknown):
```unknown
DMPlexTSComputeIJacobianFEM()
```

---

## DMPlexTSComputeRHSFunctionFVMCEED#

**URL:** https://petsc.org/release/manualpages/TS/DMPlexTSComputeRHSFunctionFVMCEED/

**Contents:**
- DMPlexTSComputeRHSFunctionFVMCEED#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Assemble the right-hand-side vector of a finite-volume TS step using the libCEED operator attached to a DMPLEX

dm - the DMPLEX for which libCEED operators have been created by DMCeedCreate()

time - the current time

locX - local solution vector including ghost values

F - the global right-hand-side vector to assemble

ctx - application context (unused)

This is normally installed as the TS RHS function callback via DMTSSetRHSFunctionLocal() when using libCEED for the finite-volume evaluation.

TS: Scalable ODE and DAE Solvers, TS, DMPLEX, DMCeedCreate(), DMPlexSNESComputeResidualCEED(), DMTSSetRHSFunctionLocal()

src/ts/utils/libceed/dmplextsceed.c

src/ts/tutorials/ex11.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscts.h" 
PetscErrorCode DMPlexTSComputeRHSFunctionFVMCEED(DM dm, PetscReal time, Vec locX, Vec F, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMCeedCreate()
```

Example 3 (unknown):
```unknown
DMTSSetRHSFunctionLocal()
```

Example 4 (unknown):
```unknown
DMCeedCreate()
```

---

## DMPlexTSComputeRHSFunctionFVM#

**URL:** https://petsc.org/release/manualpages/TS/DMPlexTSComputeRHSFunctionFVM/

**Contents:**
- DMPlexTSComputeRHSFunctionFVM#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Form the forcing F from the local input locX using pointwise functions specified by the user

locX - Local solution

ctx - The application context

F - Global output vector

TS: Scalable ODE and DAE Solvers, DMPLEX, TS, DMPlexComputeJacobianActionFEM()

src/ts/utils/dmplexts.c

src/ts/tutorials/ex11.c src/ts/tutorials/ex18.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscts.h" 
PetscErrorCode DMPlexTSComputeRHSFunctionFVM(DM dm, PetscReal time, Vec locX, Vec F, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMPlexComputeJacobianActionFEM()
```

---

## DMTSCheckFromOptions#

**URL:** https://petsc.org/release/manualpages/TS/DMTSCheckFromOptions/

**Contents:**
- DMTSCheckFromOptions#
- Synopsis#
- Input Parameters#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#

Check the residual and Jacobian functions using the exact solution by outputting some diagnostic information based on values in the options database

u - representative TS vector

The user must call PetscDSSetExactSolution() beforehand

What is the purpose of u, does it need to already have a solution or some other value in it?

src/ts/utils/dmplexts.c

src/ts/tutorials/ex45.c src/ts/tutorials/ex46.c src/ts/tutorials/ex18.c src/ts/tutorials/ex76.c src/ts/tutorials/ex77.c src/ts/tutorials/ex53.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscts.h" 
PetscErrorCode DMTSCheckFromOptions(TS ts, Vec u)
```

Example 2 (unknown):
```unknown
PetscDSSetExactSolution()
```

---

## DMTSCheckJacobian#

**URL:** https://petsc.org/release/manualpages/TS/DMTSCheckJacobian/

**Contents:**
- DMTSCheckJacobian#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Check the Jacobian of the exact solution against the residual using the Taylor Test

tol - A tolerance for the check, or -1 to print the results instead

isLinear - Flag indicating that the function looks linear, or NULL

convRate - The rate of convergence of the linear model, or NULL

TS: Scalable ODE and DAE Solvers, DNTSCheckFromOptions(), DMTSCheckResidual(), DNSNESCheckFromOptions(), DMSNESCheckDiscretization(), DMSNESCheckResidual()

src/ts/utils/dmplexts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscts.h" 
PetscErrorCode DMTSCheckJacobian(TS ts, DM dm, PetscReal t, Vec u, Vec u_t, PetscReal tol, PetscBool *isLinear, PetscReal *convRate)
```

Example 2 (unknown):
```unknown
DNTSCheckFromOptions()
```

Example 3 (unknown):
```unknown
DMTSCheckResidual()
```

Example 4 (unknown):
```unknown
DNSNESCheckFromOptions()
```

---

## DMTSCheckResidual#

**URL:** https://petsc.org/release/manualpages/TS/DMTSCheckResidual/

**Contents:**
- DMTSCheckResidual#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Check the residual of the exact solution

tol - A tolerance for the check, or -1 to print the results instead

residual - The residual norm of the exact solution, or NULL

TS: Scalable ODE and DAE Solvers, DM, DMTSCheckFromOptions(), DMTSCheckJacobian(), DNSNESCheckFromOptions(), DMSNESCheckDiscretization(), DMSNESCheckJacobian()

src/ts/utils/dmplexts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscts.h" 
PetscErrorCode DMTSCheckResidual(TS ts, DM dm, PetscReal t, Vec u, Vec u_t, PetscReal tol, PetscReal *residual)
```

Example 2 (unknown):
```unknown
DMTSCheckFromOptions()
```

Example 3 (unknown):
```unknown
DMTSCheckJacobian()
```

Example 4 (unknown):
```unknown
DNSNESCheckFromOptions()
```

---

## DMTSCopy#

**URL:** https://petsc.org/release/manualpages/TS/DMTSCopy/

**Contents:**
- DMTSCopy#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

copies the information in a DMTS to another DMTS

nkdm - DMTS to receive the data, should have been created with DMTSCreate()

TS: Scalable ODE and DAE Solvers, DMTSCreate(), DMTSDestroy()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSCopy(DMTS kdm, DMTS nkdm)
```

Example 2 (unknown):
```unknown
DMTSCreate()
```

Example 3 (unknown):
```unknown
DMTSCreate()
```

Example 4 (unknown):
```unknown
DMTSDestroy()
```

---

## DMTSCreateRHSMassMatrixLumped#

**URL:** https://petsc.org/release/manualpages/TS/DMTSCreateRHSMassMatrixLumped/

**Contents:**
- DMTSCreateRHSMassMatrixLumped#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

This creates the lumped mass matrix associated with the given DM, and a solver to invert it, and stores them in the DM context.

dm - DM providing the mass matrix

The idea here is that an explicit system can be given a mass matrix, based on the DM, which is inverted on the RHS at each step. Since the matrix is lumped, inversion is trivial.

TS: Scalable ODE and DAE Solvers, DM, DMTSCreateRHSMassMatrix(), DMTSDestroyRHSMassMatrix(), DMCreateMassMatrix(), DMTS

src/ts/utils/dmlocalts.c

src/ts/tutorials/ex45.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSCreateRHSMassMatrixLumped(DM dm)
```

Example 2 (unknown):
```unknown
DMTSCreateRHSMassMatrix()
```

Example 3 (unknown):
```unknown
DMTSDestroyRHSMassMatrix()
```

Example 4 (unknown):
```unknown
DMCreateMassMatrix()
```

---

## DMTSCreateRHSMassMatrix#

**URL:** https://petsc.org/release/manualpages/TS/DMTSCreateRHSMassMatrix/

**Contents:**
- DMTSCreateRHSMassMatrix#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

This creates the mass matrix associated with the given DM, and a solver to invert it, and stores them in the DM context.

dm - DM providing the mass matrix

The idea here is that an explicit system can be given a mass matrix, based on the DM, which is inverted on the RHS at each step.

TS: Scalable ODE and DAE Solvers, DM, DMTSCreateRHSMassMatrixLumped(), DMTSDestroyRHSMassMatrix(), DMCreateMassMatrix(), DMTS

src/ts/utils/dmlocalts.c

src/ts/tutorials/ex45.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSCreateRHSMassMatrix(DM dm)
```

Example 2 (unknown):
```unknown
DMTSCreateRHSMassMatrixLumped()
```

Example 3 (unknown):
```unknown
DMTSDestroyRHSMassMatrix()
```

Example 4 (unknown):
```unknown
DMCreateMassMatrix()
```

---

## DMTSDestroyRHSMassMatrix#

**URL:** https://petsc.org/release/manualpages/TS/DMTSDestroyRHSMassMatrix/

**Contents:**
- DMTSDestroyRHSMassMatrix#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#

Destroys the mass matrix and solver stored in the DM context, if they exist.

dm - DM providing the mass matrix

TS: Scalable ODE and DAE Solvers, DM, DMTSCreateRHSMassMatrixLumped(), DMCreateMassMatrix(), DMTS

src/ts/utils/dmlocalts.c

src/ts/tutorials/ex45.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSDestroyRHSMassMatrix(DM dm)
```

Example 2 (unknown):
```unknown
DMTSCreateRHSMassMatrixLumped()
```

Example 3 (unknown):
```unknown
DMCreateMassMatrix()
```

---

## DMTSGetForcingFunction#

**URL:** https://petsc.org/release/manualpages/TS/DMTSGetForcingFunction/

**Contents:**
- DMTSGetForcingFunction#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

get TS forcing function evaluation function from a DMTS

dm - DM to be used with TS

f - forcing function evaluation function; see TSForcingFn for the calling sequence

ctx - context for solution evaluation

TSSetForcingFunction() is normally used, but it calls this function internally because the application context is actually associated with the DM. This makes the interface consistent regardless of whether the user interacts with a DM or not. If DM took a more central role at some later date, this could become the primary method of setting the residual.

TS: Scalable ODE and DAE Solvers, DMTS, TS, DM, TSSetForcingFunction(), TSForcingFn

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSGetForcingFunction(DM dm, TSForcingFn **f, PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
TSForcingFn
```

Example 3 (unknown):
```unknown
TSSetForcingFunction()
```

Example 4 (unknown):
```unknown
TSSetForcingFunction()
```

---

## DMTSGetI2Function#

**URL:** https://petsc.org/release/manualpages/TS/DMTSGetI2Function/

**Contents:**
- DMTSGetI2Function#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

get TS implicit residual evaluation function for 2nd order systems from a DMTS

dm - DM to be used with TS

fun - function evaluation function, for calling sequence see TSSetI2Function()

ctx - context for residual evaluation

TSGetI2Function() is normally used, but it calls this function internally because the application context is actually associated with the DM.

TS: Scalable ODE and DAE Solvers, DMTS, DM, TS, DMTSSetI2Function(), TSGetI2Function()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSGetI2Function(DM dm, TSI2FunctionFn **fun, PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
TSSetI2Function()
```

Example 3 (unknown):
```unknown
TSGetI2Function()
```

Example 4 (unknown):
```unknown
DMTSSetI2Function()
```

---

## DMTSGetI2Jacobian#

**URL:** https://petsc.org/release/manualpages/TS/DMTSGetI2Jacobian/

**Contents:**
- DMTSGetI2Jacobian#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

get TS implicit Jacobian evaluation function for 2nd order systems from a DMTS

dm - DM to be used with TS

jac - Jacobian evaluation function, for calling sequence see TSI2JacobianFn

ctx - context for Jacobian evaluation

TSGetI2Jacobian() is normally used, but it calls this function internally because the application context is actually associated with the DM.

TS: Scalable ODE and DAE Solvers, DMTS, DM, TS, DMTSSetI2Jacobian(), TSGetI2Jacobian(), TSI2JacobianFn

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSGetI2Jacobian(DM dm, TSI2JacobianFn **jac, PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
TSI2JacobianFn
```

Example 3 (unknown):
```unknown
TSGetI2Jacobian()
```

Example 4 (unknown):
```unknown
DMTSSetI2Jacobian()
```

---

## DMTSGetIFunctionLocal#

**URL:** https://petsc.org/release/manualpages/TS/DMTSGetIFunctionLocal/

**Contents:**
- DMTSGetIFunctionLocal#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#

get the local implicit function evaluation function. This function is called with local vector containing the local vector information PLUS ghost point information. It should compute a result for all local elements and DM will automatically accumulate the overlapping values.

dm - DM to associate callback with

func - local function evaluation

ctx - context for function evaluation

u - the current solution

udot - the derivative of u

F - output, the computed implicit function

ctx - the application context for the function

TS: Scalable ODE and DAE Solvers, DM, DMTSSetIFunctionLocal(), DMTSSetIFunction(), DMTSSetIJacobianLocal()

src/ts/utils/dmlocalts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSGetIFunctionLocal(DM dm, PetscErrorCode (**func)(DM dm, PetscReal t, Vec u, Vec udot, Vec F, PetscCtx ctx), PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
DMTSSetIFunctionLocal()
```

Example 3 (unknown):
```unknown
DMTSSetIFunction()
```

Example 4 (unknown):
```unknown
DMTSSetIJacobianLocal()
```

---

## DMTSGetIFunction#

**URL:** https://petsc.org/release/manualpages/TS/DMTSGetIFunction/

**Contents:**
- DMTSGetIFunction#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

get TS implicit residual evaluation function from a DMTS

dm - DM to be used with TS

func - function evaluation function, for calling sequence see TSIFunctionFn

ctx - context for residual evaluation

TSGetIFunction() is normally used, but it calls this function internally because the application context is actually associated with the DM.

TS: Scalable ODE and DAE Solvers, DMTS, TS, DM, DMTSSetIFunction(), TSIFunctionFn

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSGetIFunction(DM dm, TSIFunctionFn **func, PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
TSIFunctionFn
```

Example 3 (unknown):
```unknown
TSGetIFunction()
```

Example 4 (unknown):
```unknown
DMTSSetIFunction()
```

---

## DMTSGetIJacobianLocal#

**URL:** https://petsc.org/release/manualpages/TS/DMTSGetIJacobianLocal/

**Contents:**
- DMTSGetIJacobianLocal#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#

get a local Jacobian evaluation function

dm - DM to associate callback with

func - local Jacobian evaluation

ctx - optional context for local Jacobian evaluation

u - the current solution

udot - the derivative of u

shift - the shift factoring arising from the implicit time-step

J - output, the Jacobian

Jpre - output, matrix from which to compute the preconditioner for J, often the same as J

ctx - the application context for the function

TS: Scalable ODE and DAE Solvers, DM, DMTSSetIJacobianLocal(), DMTSSetIFunctionLocal(), DMTSSetIJacobian(), DMTSSetIFunction()

src/ts/utils/dmlocalts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSGetIJacobianLocal(DM dm, PetscErrorCode (**func)(DM dm, PetscReal t, Vec u, Vec udot, PetscReal shift, Mat J, Mat Jpre, PetscCtx ctx), PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
DMTSSetIJacobianLocal()
```

Example 3 (unknown):
```unknown
DMTSSetIFunctionLocal()
```

Example 4 (unknown):
```unknown
DMTSSetIJacobian()
```

---

## DMTSGetIJacobian#

**URL:** https://petsc.org/release/manualpages/TS/DMTSGetIJacobian/

**Contents:**
- DMTSGetIJacobian#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

get TS Jacobian evaluation function from a DMTS

dm - DM to be used with TS

func - Jacobian evaluation function, for calling sequence see TSIJacobianFn

ctx - context for residual evaluation

TSGetIJacobian() is normally used, but it calls this function internally because the application context is actually associated with the DM. This makes the interface consistent regardless of whether the user interacts with a DM or not. If DM took a more central role at some later date, this could become the primary method of setting the Jacobian.

TS: Scalable ODE and DAE Solvers, DMTS, DM, TS, DMTSSetIJacobian(), TSIJacobianFn

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSGetIJacobian(DM dm, TSIJacobianFn **func, PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
TSIJacobianFn
```

Example 3 (unknown):
```unknown
TSGetIJacobian()
```

Example 4 (unknown):
```unknown
DMTSSetIJacobian()
```

---

## DMTSGetRHSFunctionLocal#

**URL:** https://petsc.org/release/manualpages/TS/DMTSGetRHSFunctionLocal/

**Contents:**
- DMTSGetRHSFunctionLocal#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#

get a local rhs function evaluation function. This function is called with local vector containing the local vector information PLUS ghost point information. It should compute a result for all local elements and DM will automatically accumulate the overlapping values.

dm - DM to associate callback with

func - local function evaluation

ctx - context for function evaluation

u - the current solution

udot - output, the evaluated right hand side

ctx - the application context for the function

TS: Scalable ODE and DAE Solvers, DM, DMTSSetRHSFunctionLocal(), DMTSSetRHSFunction(), DMTSSetIFunction(), DMTSSetIJacobianLocal()

src/ts/utils/dmlocalts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSGetRHSFunctionLocal(DM dm, PetscErrorCode (**func)(DM dm, PetscReal t, Vec u, Vec udot, PetscCtx ctx), PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
DMTSSetRHSFunctionLocal()
```

Example 3 (unknown):
```unknown
DMTSSetRHSFunction()
```

Example 4 (unknown):
```unknown
DMTSSetIFunction()
```

---

## DMTSGetRHSFunction#

**URL:** https://petsc.org/release/manualpages/TS/DMTSGetRHSFunction/

**Contents:**
- DMTSGetRHSFunction#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

get TS explicit residual evaluation function from a DMTS

dm - DM to be used with TS

func - residual evaluation function, for calling sequence see TSRHSFunctionFn

ctx - context for residual evaluation

TSGetRHSFunction() is normally used, but it calls this function internally because the application context is actually associated with the DM.

TS: Scalable ODE and DAE Solvers, DMTS, DM, TS, TSRHSFunctionFn, TSGetRHSFunction()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSGetRHSFunction(DM dm, TSRHSFunctionFn **func, PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
TSRHSFunctionFn
```

Example 3 (unknown):
```unknown
TSGetRHSFunction()
```

Example 4 (unknown):
```unknown
TSRHSFunctionFn
```

---

## DMTSGetRHSJacobian#

**URL:** https://petsc.org/release/manualpages/TS/DMTSGetRHSJacobian/

**Contents:**
- DMTSGetRHSJacobian#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

get TS Jacobian evaluation function from a DMTS

dm - DM to be used with TS

func - Jacobian evaluation function, for calling sequence see TSRHSJacobianFn

ctx - context for residual evaluation

TSGetRHSJacobian() is normally used, but it calls this function internally because the application context is actually associated with the DM. This makes the interface consistent regardless of whether the user interacts with a DM or not. If DM took a more central role at some later date, this could become the primary method of setting the Jacobian.

TS: Scalable ODE and DAE Solvers, DMTS, DM, TS, DMTSSetRHSJacobian(), TSRHSJacobianFn

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSGetRHSJacobian(DM dm, TSRHSJacobianFn **func, PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
TSRHSJacobianFn
```

Example 3 (unknown):
```unknown
TSGetRHSJacobian()
```

Example 4 (unknown):
```unknown
DMTSSetRHSJacobian()
```

---

## DMTSGetSolutionFunction#

**URL:** https://petsc.org/release/manualpages/TS/DMTSGetSolutionFunction/

**Contents:**
- DMTSGetSolutionFunction#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

gets the TS solution evaluation function from a DMTS

dm - DM to be used with TS

func - solution function evaluation function, for calling sequence see TSSolutionFn

ctx - context for solution evaluation

TS: Scalable ODE and DAE Solvers, DMTS, TS, DM, DMTSSetSolutionFunction(), TSSolutionFn

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSGetSolutionFunction(DM dm, TSSolutionFn **func, PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
TSSolutionFn
```

Example 3 (unknown):
```unknown
DMTSSetSolutionFunction()
```

Example 4 (unknown):
```unknown
TSSolutionFn
```

---

## DMTSGetTransientVariable#

**URL:** https://petsc.org/release/manualpages/TS/DMTSGetTransientVariable/

**Contents:**
- DMTSGetTransientVariable#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

gets function to transform from state to transient variables set with DMTSSetTransientVariable() from a TSDM

dm - DM to be used with TS

tvar - a function that transforms to transient variables, see TSTransientVariableFn for the calling sequence

ctx - a context for tvar

Normally TSSetTransientVariable() is used

TS: Scalable ODE and DAE Solvers, DMTS, DM, DMTSSetTransientVariable(), DMTSGetIFunction(), DMTSGetIJacobian(), TSTransientVariableFn

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMTSSetTransientVariable()
```

Example 2 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSGetTransientVariable(DM dm, TSTransientVariableFn **tvar, PetscCtx ctx)
```

Example 3 (unknown):
```unknown
TSTransientVariableFn
```

Example 4 (unknown):
```unknown
TSSetTransientVariable()
```

---

## DMTSSetBoundaryLocal#

**URL:** https://petsc.org/release/manualpages/TS/DMTSSetBoundaryLocal/

**Contents:**
- DMTSSetBoundaryLocal#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

set the function for essential boundary data for a local implicit function evaluation.

dm - DM to associate callback with

func - local function evaluation

ctx - context for function evaluation

u - the current solution

f - output, the computed right hand side function

ctx - the application context for the function

func should set the essential boundary data for the local portion of the solution, as well its time derivative (if it is not NULL).

Vectors are initialized to zero before this function, so it is only needed for non homogeneous data.

This function is somewhat optional: boundary data could potentially be inserted by a function passed to DMTSSetIFunctionLocal(). The use case for this function is for discretizations with constraints (see DMGetDefaultConstraints()): this function inserts boundary values before constraint interpolation.

TS: Scalable ODE and DAE Solvers, DM, TS, DMTSSetIFunction(), DMTSSetIJacobianLocal()

src/ts/utils/dmlocalts.c

src/ts/tutorials/ex45.c src/ts/tutorials/ex11.c src/ts/tutorials/ex46.c src/ts/tutorials/ex30.c src/ts/tutorials/ex18.c src/ts/tutorials/ex76.c src/ts/tutorials/ex48.c src/ts/tutorials/ex77.c src/ts/tutorials/ex53.c src/ts/tutorials/ex47.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSSetBoundaryLocal(DM dm, PetscErrorCode (*func)(DM dm, PetscReal t, Vec u, Vec f, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMTSSetIFunctionLocal()
```

Example 3 (unknown):
```unknown
DMGetDefaultConstraints()
```

Example 4 (unknown):
```unknown
DMTSSetIFunction()
```

---

## DMTSSetForcingFunction#

**URL:** https://petsc.org/release/manualpages/TS/DMTSSetForcingFunction/

**Contents:**
- DMTSSetForcingFunction#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

set TS forcing function evaluation function into a DMTS

dm - DM to be used with TS

func - forcing function evaluation routine, for calling sequence see TSForcingFn

ctx - context for solution evaluation

TSSetForcingFunction() is normally used, but it calls this function internally because the application context is actually associated with the DM. This makes the interface consistent regardless of whether the user interacts with a DM or not. If DM took a more central role at some later date, this could become the primary method of setting the residual.

TS: Scalable ODE and DAE Solvers, DMTS, DM, TS, TSForcingFn, TSSetForcingFunction(), DMTSGetForcingFunction()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSSetForcingFunction(DM dm, TSForcingFn *func, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSForcingFn
```

Example 3 (unknown):
```unknown
TSSetForcingFunction()
```

Example 4 (unknown):
```unknown
TSForcingFn
```

---

## DMTSSetI2FunctionContextDestroy#

**URL:** https://petsc.org/release/manualpages/TS/DMTSSetI2FunctionContextDestroy/

**Contents:**
- DMTSSetI2FunctionContextDestroy#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

set TS implicit evaluation for 2nd order systems context destroy into a DMTS

dm - DM to be used with TS

f - implicit evaluation context destroy function, see PetscCtxDestroyFn for its calling sequence

TSSetI2FunctionContextDestroy() is normally used, but it calls this function internally because the application context is actually associated with the DM.

TS: Scalable ODE and DAE Solvers, DMTS, TSSetI2FunctionContextDestroy(), DMTSSetI2Function(), TSSetI2Function()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSSetI2FunctionContextDestroy(DM dm, PetscCtxDestroyFn *f)
```

Example 2 (unknown):
```unknown
PetscCtxDestroyFn
```

Example 3 (unknown):
```unknown
TSSetI2FunctionContextDestroy()
```

Example 4 (unknown):
```unknown
TSSetI2FunctionContextDestroy()
```

---

## DMTSSetI2Function#

**URL:** https://petsc.org/release/manualpages/TS/DMTSSetI2Function/

**Contents:**
- DMTSSetI2Function#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

set TS implicit function evaluation function for 2nd order systems into a TSDM

dm - DM to be used with TS

fun - function evaluation routine

ctx - context for residual evaluation

TSSetI2Function() is normally used, but it calls this function internally because the application context is actually associated with the DM.

TS: Scalable ODE and DAE Solvers, DMTS, DM, TS, TSSetI2Function()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSSetI2Function(DM dm, TSI2FunctionFn *fun, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSSetI2Function()
```

Example 3 (unknown):
```unknown
TSSetI2Function()
```

---

## DMTSSetI2JacobianContextDestroy#

**URL:** https://petsc.org/release/manualpages/TS/DMTSSetI2JacobianContextDestroy/

**Contents:**
- DMTSSetI2JacobianContextDestroy#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

set TS implicit Jacobian evaluation for 2nd order systems context destroy function into a DMTS

dm - DM to be used with TS

f - implicit Jacobian evaluation context destroy function, see PetscCtxDestroyFn for its calling sequence

Normally TSSetI2JacobianContextDestroy() is used

TS: Scalable ODE and DAE Solvers, DMTS, DM, TS, TSSetI2JacobianContextDestroy(), DMTSSetI2Jacobian(), TSSetI2Jacobian()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSSetI2JacobianContextDestroy(DM dm, PetscCtxDestroyFn *f)
```

Example 2 (unknown):
```unknown
PetscCtxDestroyFn
```

Example 3 (unknown):
```unknown
TSSetI2JacobianContextDestroy()
```

Example 4 (unknown):
```unknown
TSSetI2JacobianContextDestroy()
```

---

## DMTSSetI2Jacobian#

**URL:** https://petsc.org/release/manualpages/TS/DMTSSetI2Jacobian/

**Contents:**
- DMTSSetI2Jacobian#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

set TS implicit Jacobian evaluation function for 2nd order systems from a DMTS

dm - DM to be used with TS

jac - Jacobian evaluation routine

ctx - context for Jacobian evaluation

TSSetI2Jacobian() is normally used, but it calls this function internally because the application context is actually associated with the DM.

TS: Scalable ODE and DAE Solvers, DMTS, DM, TS, TSI2JacobianFn, TSSetI2Jacobian()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSSetI2Jacobian(DM dm, TSI2JacobianFn *jac, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSSetI2Jacobian()
```

Example 3 (unknown):
```unknown
TSI2JacobianFn
```

Example 4 (unknown):
```unknown
TSSetI2Jacobian()
```

---

## DMTSSetIFunctionContextDestroy#

**URL:** https://petsc.org/release/manualpages/TS/DMTSSetIFunctionContextDestroy/

**Contents:**
- DMTSSetIFunctionContextDestroy#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

set TS implicit evaluation context destroy function into a DMTS

dm - DM to be used with TS

f - implicit evaluation context destroy function, see PetscCtxDestroyFn for its calling sequence

TS: Scalable ODE and DAE Solvers, DMTS, DM, TS, DMTSSetIFunction(), TSSetIFunction(), PetscCtxDestroyFn

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSSetIFunctionContextDestroy(DM dm, PetscCtxDestroyFn *f)
```

Example 2 (unknown):
```unknown
PetscCtxDestroyFn
```

Example 3 (unknown):
```unknown
DMTSSetIFunction()
```

Example 4 (unknown):
```unknown
TSSetIFunction()
```

---

## DMTSSetIFunctionLocal#

**URL:** https://petsc.org/release/manualpages/TS/DMTSSetIFunctionLocal/

**Contents:**
- DMTSSetIFunctionLocal#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

set a local implicit function evaluation function. This function is called with local vector containing the local vector information PLUS ghost point information. It should compute a result for all local elements and DM will automatically accumulate the overlapping values.

dm - DM to associate callback with

func - local function evaluation

ctx - context for function evaluation

u - the current solution

udot - the derivative of u

F - output, the computed implicit function

ctx - the application context for the function

TS: Scalable ODE and DAE Solvers, DM, DMTSGetIFunctionLocal(), DMTSSetIFunction(), DMTSSetIJacobianLocal()

src/ts/utils/dmlocalts.c

src/ts/tutorials/ex45.c src/ts/tutorials/ex46.c src/ts/tutorials/ex30.c src/ts/tutorials/ex18.c src/ts/tutorials/ex76.c src/ts/tutorials/ex48.c src/ts/tutorials/ex77.c src/ts/tutorials/ex53.c src/ts/tutorials/ex47.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSSetIFunctionLocal(DM dm, PetscErrorCode (*func)(DM dm, PetscReal t, Vec u, Vec udot, Vec F, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMTSGetIFunctionLocal()
```

Example 3 (unknown):
```unknown
DMTSSetIFunction()
```

Example 4 (unknown):
```unknown
DMTSSetIJacobianLocal()
```

---

## DMTSSetIFunctionSerialize#

**URL:** https://petsc.org/release/manualpages/TS/DMTSSetIFunctionSerialize/

**Contents:**
- DMTSSetIFunctionSerialize#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

sets functions used to view and load a TSIFunctionFn context

dm - DM to be used with TS

view - viewer function

load - loading function

TS: Scalable ODE and DAE Solvers, DMTS, DM, TS

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSIFunctionFn
```

Example 2 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSSetIFunctionSerialize(DM dm, PetscErrorCode (*view)(void *, PetscViewer), PetscErrorCode (*load)(void **, PetscViewer))
```

---

## DMTSSetIFunction#

**URL:** https://petsc.org/release/manualpages/TS/DMTSSetIFunction/

**Contents:**
- DMTSSetIFunction#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

set TS implicit function evaluation function into a DMTS

dm - DM to be used with TS

func - function evaluating f(t,u,u_t)

ctx - context for residual evaluation

TSSetIFunction() is normally used, but it calls this function internally because the application context is actually associated with the DM. This makes the interface consistent regardless of whether the user interacts with a DM or not. If DM took a more central role at some later date, this could become the primary method of setting the residual.

TS: Scalable ODE and DAE Solvers, DMTS, TS, DM, TSIFunctionFn

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSSetIFunction(DM dm, TSIFunctionFn *func, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSSetIFunction()
```

Example 3 (unknown):
```unknown
TSIFunctionFn
```

---

## DMTSSetIJacobianContextDestroy#

**URL:** https://petsc.org/release/manualpages/TS/DMTSSetIJacobianContextDestroy/

**Contents:**
- DMTSSetIJacobianContextDestroy#
- Synopsis#
- Input Parameters#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#

set TS Jacobian evaluation context destroy function into a DMTS

dm - DM to be used with TS

f - Jacobian evaluation context destroy function, see PetscCtxDestroyFn for its calling sequence

TSSetIJacobianContextDestroy() is normally used, but it calls this function internally because the application context is actually associated with the DM. This makes the interface consistent regardless of whether the user interacts with a DM or not.

If DM took a more central role at some later date, this could become the primary method of setting the Jacobian.

TS: Scalable ODE and DAE Solvers, DMTS, TSSetIJacobianContextDestroy(), TSSetI2JacobianContextDestroy(), DMTSSetIJacobian(), TSSetIJacobian()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSSetIJacobianContextDestroy(DM dm, PetscCtxDestroyFn *f)
```

Example 2 (unknown):
```unknown
PetscCtxDestroyFn
```

Example 3 (unknown):
```unknown
TSSetIJacobianContextDestroy()
```

Example 4 (unknown):
```unknown
TSSetIJacobianContextDestroy()
```

---

## DMTSSetIJacobianLocal#

**URL:** https://petsc.org/release/manualpages/TS/DMTSSetIJacobianLocal/

**Contents:**
- DMTSSetIJacobianLocal#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

set a local Jacobian evaluation function

dm - DM to associate callback with

func - local Jacobian evaluation

ctx - optional context for local Jacobian evaluation

u - the current solution

udot - the derivative of u

shift - the shift factoring arising from the implicit time-step

J - output, the Jacobian

Jpre - output, matrix from which to compute the preconditioner for J, often the same as J

ctx - the application context for the function

TS: Scalable ODE and DAE Solvers, DM, DMTSGetIJacobianLocal(), DMTSSetIFunctionLocal(), DMTSSetIJacobian(), DMTSSetIFunction()

src/ts/utils/dmlocalts.c

src/ts/tutorials/ex45.c src/ts/tutorials/ex46.c src/ts/tutorials/ex30.c src/ts/tutorials/ex18.c src/ts/tutorials/ex76.c src/ts/tutorials/ex48.c src/ts/tutorials/ex77.c src/ts/tutorials/ex53.c src/ts/tutorials/ex47.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSSetIJacobianLocal(DM dm, PetscErrorCode (*func)(DM dm, PetscReal t, Vec u, Vec udot, PetscReal shift, Mat J, Mat Jpre, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMTSGetIJacobianLocal()
```

Example 3 (unknown):
```unknown
DMTSSetIFunctionLocal()
```

Example 4 (unknown):
```unknown
DMTSSetIJacobian()
```

---

## DMTSSetIJacobianSerialize#

**URL:** https://petsc.org/release/manualpages/TS/DMTSSetIJacobianSerialize/

**Contents:**
- DMTSSetIJacobianSerialize#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

sets functions used to view and load a TSIJacobianFn context

dm - DM to be used with TS

view - viewer function

load - loading function

TS: Scalable ODE and DAE Solvers, DMTS, DM, TS

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSIJacobianFn
```

Example 2 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSSetIJacobianSerialize(DM dm, PetscErrorCode (*view)(void *, PetscViewer), PetscErrorCode (*load)(void **, PetscViewer))
```

---

## DMTSSetIJacobian#

**URL:** https://petsc.org/release/manualpages/TS/DMTSSetIJacobian/

**Contents:**
- DMTSSetIJacobian#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

set TS Jacobian evaluation function into a DMTS

dm - DM to be used with TS

func - Jacobian evaluation routine, see TSIJacobianFn for the calling sequence

ctx - context for residual evaluation

TSSetIJacobian() is normally used, but it calls this function internally because the application context is actually associated with the DM. This makes the interface consistent regardless of whether the user interacts with a DM or not. If DM took a more central role at some later date, this could become the primary method of setting the Jacobian.

TS: Scalable ODE and DAE Solvers, DMTS, TS, DM, TSIJacobianFn, DMTSGetIJacobian(), TSSetIJacobian()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSSetIJacobian(DM dm, TSIJacobianFn *func, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSIJacobianFn
```

Example 3 (unknown):
```unknown
TSSetIJacobian()
```

Example 4 (unknown):
```unknown
TSIJacobianFn
```

---

## DMTSSetRHSFunctionContextDestroy#

**URL:** https://petsc.org/release/manualpages/TS/DMTSSetRHSFunctionContextDestroy/

**Contents:**
- DMTSSetRHSFunctionContextDestroy#
- Synopsis#
- Input Parameters#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#

set TS explicit residual evaluation context destroy function into a DMTS

dm - DM to be used with TS

f - explicit evaluation context destroy function, see PetscCtxDestroyFn for its calling sequence

TSSetRHSFunctionContextDestroy() is normally used, but it calls this function internally because the application context is actually associated with the DM. This makes the interface consistent regardless of whether the user interacts with a DM or not.

If DM took a more central role at some later date, this could become the primary method of setting the residual.

TS: Scalable ODE and DAE Solvers, DMTS, TSSetRHSFunctionContextDestroy(), DMTSSetRHSFunction(), TSSetRHSFunction()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSSetRHSFunctionContextDestroy(DM dm, PetscCtxDestroyFn *f)
```

Example 2 (unknown):
```unknown
PetscCtxDestroyFn
```

Example 3 (unknown):
```unknown
TSSetRHSFunctionContextDestroy()
```

Example 4 (unknown):
```unknown
TSSetRHSFunctionContextDestroy()
```

---

## DMTSSetRHSFunctionLocal#

**URL:** https://petsc.org/release/manualpages/TS/DMTSSetRHSFunctionLocal/

**Contents:**
- DMTSSetRHSFunctionLocal#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

set a local rhs function evaluation function. This function is called with local vector containing the local vector information PLUS ghost point information. It should compute a result for all local elements and DM will automatically accumulate the overlapping values.

dm - DM to associate callback with

func - local function evaluation

ctx - context for function evaluation

u - the current solution

f - output, the evaluated right hand side

ctx - the application context for the function

TS: Scalable ODE and DAE Solvers, DM, DMTSGetRHSFunctionLocal(), DMTSSetRHSFunction(), DMTSSetIFunction(), DMTSSetIJacobianLocal()

src/ts/utils/dmlocalts.c

src/ts/tutorials/ex45.c src/ts/tutorials/ex11.c src/ts/tutorials/ex18.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSSetRHSFunctionLocal(DM dm, PetscErrorCode (*func)(DM dm, PetscReal t, Vec u, Vec f, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMTSGetRHSFunctionLocal()
```

Example 3 (unknown):
```unknown
DMTSSetRHSFunction()
```

Example 4 (unknown):
```unknown
DMTSSetIFunction()
```

---

## DMTSSetRHSFunction#

**URL:** https://petsc.org/release/manualpages/TS/DMTSSetRHSFunction/

**Contents:**
- DMTSSetRHSFunction#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

set TS explicit residual evaluation function into a DMTS

dm - DM to be used with TS

func - RHS function evaluation routine, see TSRHSFunctionFn for the calling sequence

ctx - context for residual evaluation

TSSetRHSFunction() is normally used, but it calls this function internally because the application context is actually associated with the DM. This makes the interface consistent regardless of whether the user interacts with a DM or not. If DM took a more central role at some later date, this could become the primary method of setting the residual.

TS: Scalable ODE and DAE Solvers, DMTS, DM, TS, TSRHSFunctionFn

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSSetRHSFunction(DM dm, TSRHSFunctionFn *func, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSRHSFunctionFn
```

Example 3 (unknown):
```unknown
TSSetRHSFunction()
```

Example 4 (unknown):
```unknown
TSRHSFunctionFn
```

---

## DMTSSetRHSJacobianContextDestroy#

**URL:** https://petsc.org/release/manualpages/TS/DMTSSetRHSJacobianContextDestroy/

**Contents:**
- DMTSSetRHSJacobianContextDestroy#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

set TS Jacobian evaluation context destroy function from a DMTS

dm - DM to be used with TS

f - Jacobian evaluation context destroy function, see PetscCtxDestroyFn for its calling sequence

The user usually calls TSSetRHSJacobianContextDestroy() which calls this routine

TS: Scalable ODE and DAE Solvers, DMTS, TS, TSSetRHSJacobianContextDestroy(), DMTSSetRHSJacobian(), TSSetRHSJacobian()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSSetRHSJacobianContextDestroy(DM dm, PetscCtxDestroyFn *f)
```

Example 2 (unknown):
```unknown
PetscCtxDestroyFn
```

Example 3 (unknown):
```unknown
TSSetRHSJacobianContextDestroy()
```

Example 4 (unknown):
```unknown
TSSetRHSJacobianContextDestroy()
```

---

## DMTSSetRHSJacobian#

**URL:** https://petsc.org/release/manualpages/TS/DMTSSetRHSJacobian/

**Contents:**
- DMTSSetRHSJacobian#
- Synopsis#
- Input Parameters#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#

set TS Jacobian evaluation function into a DMTS

dm - DM to be used with TS

func - Jacobian evaluation routine, for calling sequence see TSIJacobianFn

ctx - context for residual evaluation

TSSetRHSJacobian() is normally used, but it calls this function internally because the application context is actually associated with the DM. This makes the interface consistent regardless of whether the user interacts with a DM or not.

If DM took a more central role at some later date, this could become the primary method of setting the Jacobian.

TS: Scalable ODE and DAE Solvers, DMTS, TSRHSJacobianFn, DMTSGetRHSJacobian(), TSSetRHSJacobian()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSSetRHSJacobian(DM dm, TSRHSJacobianFn *func, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSIJacobianFn
```

Example 3 (unknown):
```unknown
TSSetRHSJacobian()
```

Example 4 (unknown):
```unknown
TSRHSJacobianFn
```

---

## DMTSSetSolutionFunction#

**URL:** https://petsc.org/release/manualpages/TS/DMTSSetSolutionFunction/

**Contents:**
- DMTSSetSolutionFunction#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

set TS solution evaluation function into a DMTS

dm - DM to be used with TS

func - solution function evaluation routine, for calling sequence see TSSolutionFn

ctx - context for solution evaluation

TSSetSolutionFunction() is normally used, but it calls this function internally because the application context is actually associated with the DM. This makes the interface consistent regardless of whether the user interacts with a DM or not. If DM took a more central role at some later date, this could become the primary method of setting the residual.

TS: Scalable ODE and DAE Solvers, DMTS, DM, TS, DMTSGetSolutionFunction(), TSSolutionFn

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSSetSolutionFunction(DM dm, TSSolutionFn *func, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSSolutionFn
```

Example 3 (unknown):
```unknown
TSSetSolutionFunction()
```

Example 4 (unknown):
```unknown
DMTSGetSolutionFunction()
```

---

## DMTSSetTransientVariable#

**URL:** https://petsc.org/release/manualpages/TS/DMTSSetTransientVariable/

**Contents:**
- DMTSSetTransientVariable#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

sets function to transform from state to transient variables into a DMTS

dm - DM to be used with TS

tvar - a function that transforms to transient variables, see TSTransientVariableFn for the calling sequence

ctx - a context for tvar

Normally TSSetTransientVariable() is used

This is typically used to transform from primitive to conservative variables so that a time integrator (e.g., TSBDF) can be conservative. In this context, primitive variables P are used to model the state (e.g., because they lead to well-conditioned formulations even in limiting cases such as low-Mach or zero porosity). The transient variable is C(P), specified by calling this function. An IFunction thus receives arguments (P, Cdot) and the IJacobian must be evaluated via the chain rule, as in

TS: Scalable ODE and DAE Solvers, DMTS, TS, TSBDF, TSSetTransientVariable(), DMTSGetTransientVariable(), DMTSSetIFunction(), DMTSSetIJacobian(), TSTransientVariableFn

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode DMTSSetTransientVariable(DM dm, TSTransientVariableFn *tvar, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSTransientVariableFn
```

Example 3 (unknown):
```unknown
TSSetTransientVariable()
```

Example 4 (unknown):
```unknown
TSSetTransientVariable()
```

---

## DMTS#

**URL:** https://petsc.org/release/manualpages/TS/DMTS/

**Contents:**
- DMTS#
- Synopsis#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#
- Implementations#

Object held by a DM that contains all the callback functions and their contexts needed by a TS

Users provide callback functions and their contexts to TS using, for example, TSSetIFunction(). These values are stored in a DMTS that is contained in the DM associated with the TS. If no DM was provided by the user with TSSetDM() it is automatically created by TSGetDM() with DMShellCreate().

Users very rarely need to worked directly with the DMTS object, rather they work with the TS and the DM they created

Multiple DM can share a single DMTS, often each DM is associated with a grid refinement level. DMGetDMTS() returns the DMTS associated with a DM. DMGetDMTSWrite() returns a unique DMTS that is only associated with the current DM, making a copy of the shared DMTS if needed (copy-on-write).

See DMKSP for details on why there is a needed for DMTS instead of simply storing the user callbacks directly in the DM or the TS

The original dm inside the DMTS is NOT reference counted (to prevent a reference count loop between a DM and a DMSNES). The DM on which this context was first created is cached here to implement one-way copy-on-write. When DMGetDMTSWrite() sees a request using a different DM, it makes a copy of the DMTS.

TS: Scalable ODE and DAE Solvers, TSCreate(), DM, DMGetDMTSWrite(), DMGetDMTS(), TSSetIFunction(), DMTSSetRHSFunctionContextDestroy(), DMTSSetRHSJacobian(), DMTSGetRHSJacobian(), DMTSSetRHSJacobianContextDestroy(), DMTSSetIFunction(), DMTSGetIFunction(), DMTSSetIFunctionContextDestroy(), DMTSSetIJacobian(), DMTSGetIJacobian(), DMTSSetIJacobianContextDestroy(), DMTSSetI2Function(), DMTSGetI2Function(), DMTSSetI2FunctionContextDestroy(), DMTSSetI2Jacobian(), DMTSGetI2Jacobian(), DMTSSetI2JacobianContextDestroy(), DMKSP, DMSNES

include/petsc/private/tsimpl.h

_p_DMTS in include/petsc/private/tsimpl.h DMTS_DA in src/ts/utils/dmdats.c DMTS_Local in src/ts/utils/dmlocalts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_DMTS *DMTS;
```

Example 2 (unknown):
```unknown
TSSetIFunction()
```

Example 3 (unknown):
```unknown
DMShellCreate()
```

Example 4 (unknown):
```unknown
DMGetDMTS()
```

---

## Forward and Adjoint Timestepping#

**URL:** https://petsc.org/release/manualpages/Timestepping/

**Contents:**
- Forward and Adjoint Timestepping#

Full Approximation Scheme (FAS) nonlinear multigrid

Time Stepping ODE and DAE Solvers (TS)

---

## PetscConvEstUseTS#

**URL:** https://petsc.org/release/manualpages/TS/PetscConvEstUseTS/

**Contents:**
- PetscConvEstUseTS#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Configure a PetscConvEst object to use a TS solver for a convergence study

ce - the convergence estimator

checkTemporal - PETSC_TRUE to run a temporal convergence study (refining the time step), PETSC_FALSE to run a spatial convergence study (refining the mesh)

This installs the appropriate callbacks on ce so that the enclosed TS solver is run at each refinement level and the resulting errors are used to estimate the observed convergence rate.

TS: Scalable ODE and DAE Solvers, PetscConvEst, TS, PetscConvEstGetConvRate()

src/ts/utils/tsconvest.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscConvEst
```

Example 2 (unknown):
```unknown
#include "petscconvest.h" 
PetscErrorCode PetscConvEstUseTS(PetscConvEst ce, PetscBool checkTemporal)
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (unknown):
```unknown
PetscConvEst
```

---

## Semi-Lagrangian Solves using the Method of Characteristics#

**URL:** https://petsc.org/release/manualpages/Characteristic/

**Contents:**
- Semi-Lagrangian Solves using the Method of Characteristics#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Single list of manual pages#

Characteristic objects are used to manage parallel Semi-Lagrangian methods (method of characteristics) for structured mesh (DMDA) problems in PDE-based simulations.

CharacteristicDestroy

CharacteristicSetType

CharacteristicRegister

CharacteristicRegisterAll

CharacteristicFinalizePackage

CharacteristicInitializePackage

CharacteristicSetFieldInterpolation

CharacteristicSetFieldInterpolationLocal

CharacteristicSetVelocityInterpolation

CharacteristicSetVelocityInterpolationLocal

DMDAMapCoordsToPeriodicDomain

CharacteristicDestroy

CharacteristicFinalizePackage

CharacteristicInitializePackage

CharacteristicRegister

CharacteristicRegisterAll

CharacteristicSetFieldInterpolation

CharacteristicSetFieldInterpolationLocal

CharacteristicSetType

CharacteristicSetVelocityInterpolation

CharacteristicSetVelocityInterpolationLocal

DMDAMapCoordsToPeriodicDomain

Sensitivity Analysis for ODE and DAE

**Examples:**

Example 1 (unknown):
```unknown
Characteristic
```

---

## Sensitivity Analysis for ODE and DAE#

**URL:** https://petsc.org/release/manualpages/Sensitivity/

**Contents:**
- Sensitivity Analysis for ODE and DAE#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Deprecated - Functionality scheduled for removal in the future#
- Single list of manual pages#

The TS library provides discrete adjoint models (TSAdjoint) and tangent linear models (TSForward) for sensitivity analysis for ODEs and DAEs. Users guide section: Performing sensitivity analysis with the TS ODE Solvers.

The adjoint solvers support gradient calculation for multiple cost functions, and the tangent linear solvers support gradient calculation with respect to multiple parameters. Adjoint is particularly efficient when the number of cost functions is much less than the number of parameters. Note that the parameters can be initial states or system parameters as used in the calculation of ODE/DAE right-hand sides.

Typical cost functions of interest may depend on the final solution to the ODE/DAE or on the whole trajectory (taking an integral form). The integral can be evaluated together with the time integration.

TSForwardSetSensitivities

TSSetCostHessianProducts

TSAdjointMonitorCancel

TSAdjointMonitorDefault

TSAdjointMonitorDrawSensi

TSAdjointMonitorSensi

TSAdjointResetForward

TSForwardGetSensitivities

TSForwardSetInitialSensitivities

TSGetCostHessianProducts

TSSetRHSHessianProduct

TSAdjointCostIntegral

TSForwardCostIntegral

TSAdjointMonitorSetFromOptions

TSAdjointSetFromOptions

TSComputeIHessianProductFunctionPP

TSComputeIHessianProductFunctionPU

TSComputeIHessianProductFunctionUP

TSComputeIHessianProductFunctionUU

TSComputeRHSHessianProductFunctionPP

TSComputeRHSHessianProductFunctionPU

TSComputeRHSHessianProductFunctionUP

TSComputeRHSHessianProductFunctionUU

TSComputeRHSJacobianP

TSComputeSNESJacobian

TSAdjointComputeDRDPFunction

TSAdjointComputeDRDYFunction

TSAdjointComputeRHSJacobian

TSAdjointSetRHSJacobian

TSComputeCostIntegrand

TSComputeDRDPFunction

TSComputeDRDUFunction

TSForwardGetIntegralGradients

TSForwardSetIntegralGradients

TSAdjointComputeDRDPFunction

TSAdjointComputeDRDYFunction

TSAdjointComputeRHSJacobian

TSAdjointCostIntegral

TSAdjointMonitorCancel

TSAdjointMonitorDefault

TSAdjointMonitorDrawSensi

TSAdjointMonitorSensi

TSAdjointMonitorSetFromOptions

TSAdjointResetForward

TSAdjointSetFromOptions

TSAdjointSetRHSJacobian

TSComputeCostIntegrand

TSComputeDRDPFunction

TSComputeDRDUFunction

TSComputeIHessianProductFunctionPP

TSComputeIHessianProductFunctionPU

TSComputeIHessianProductFunctionUP

TSComputeIHessianProductFunctionUU

TSComputeRHSHessianProductFunctionPP

TSComputeRHSHessianProductFunctionPU

TSComputeRHSHessianProductFunctionUP

TSComputeRHSHessianProductFunctionUU

TSComputeRHSJacobianP

TSComputeSNESJacobian

TSForwardCostIntegral

TSForwardGetIntegralGradients

TSForwardGetSensitivities

TSForwardSetInitialSensitivities

TSForwardSetIntegralGradients

TSForwardSetSensitivities

TSGetCostHessianProducts

TSSetCostHessianProducts

TSSetRHSHessianProduct

Time Stepping ODE and DAE Solvers (TS)

Semi-Lagrangian Solves using the Method of Characteristics

---

## SNESTSFormFunction#

**URL:** https://petsc.org/release/manualpages/TS/SNESTSFormFunction/

**Contents:**
- SNESTSFormFunction#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Function to evaluate nonlinear residual defined by an ODE solver algorithm implemented within TS

snes - nonlinear solver

U - the current state at which to evaluate the residual

ctx - application context, must be a TS

F - the nonlinear residual

This function is not normally called by users and is automatically registered with the SNES used by TS. It is most frequently passed to MatFDColoringSetFunction().

TS: Scalable ODE and DAE Solvers, SNESSetFunction(), MatFDColoringSetFunction()

src/ts/interface/ts.c

SNESTSFormFunction_ARKIMEX() in src/ts/impls/arkimex/arkimex.c SNESTSFormFunction_BDF() in src/ts/impls/bdf/bdf.c SNESTSFormFunction_EIMEX() in src/ts/impls/eimex/eimex.c SNESTSFormFunction_RK() in src/ts/impls/explicit/rk/rk.c SNESTSFormFunction_GLEE() in src/ts/impls/glee/glee.c SNESTSFormFunction_Alpha() in src/ts/impls/implicit/alpha/alpha1.c SNESTSFormFunction_Alpha() in src/ts/impls/implicit/alpha/alpha2.c SNESTSFormFunction_DiscGrad() in src/ts/impls/implicit/discgrad/tsdiscgrad.c SNESTSFormFunction_GLLE() in src/ts/impls/implicit/glle/glle.c SNESTSFormFunction_IRK() in src/ts/impls/implicit/irk/irk.c SNESTSFormFunction_Theta() in src/ts/impls/implicit/theta/theta.c SNESTSFormFunction_Mimex() in src/ts/impls/mimex/mimex.c SNESTSFormFunction_Pseudo() in src/ts/impls/pseudo/posindep.c SNESTSFormFunction_RosW() in src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode SNESTSFormFunction(SNES snes, Vec U, Vec F, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
MatFDColoringSetFunction()
```

Example 3 (unknown):
```unknown
SNESSetFunction()
```

Example 4 (unknown):
```unknown
MatFDColoringSetFunction()
```

---

## SNESTSFormJacobian#

**URL:** https://petsc.org/release/manualpages/TS/SNESTSFormJacobian/

**Contents:**
- SNESTSFormJacobian#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Function to evaluate the Jacobian defined by an ODE solver algorithm implemented within TS

snes - nonlinear solver

U - the current state at which to evaluate the residual

ctx - application context, must be a TS

B - the matrix used to construct the preconditioner (often the same as A)

This function is not normally called by users and is automatically registered with the SNES used by TS.

TS: Scalable ODE and DAE Solvers, SNESSetJacobian()

src/ts/interface/ts.c

SNESTSFormJacobian_ARKIMEX() in src/ts/impls/arkimex/arkimex.c SNESTSFormJacobian_BDF() in src/ts/impls/bdf/bdf.c SNESTSFormJacobian_EIMEX() in src/ts/impls/eimex/eimex.c SNESTSFormJacobian_RK() in src/ts/impls/explicit/rk/rk.c SNESTSFormJacobian_GLEE() in src/ts/impls/glee/glee.c SNESTSFormJacobian_Alpha() in src/ts/impls/implicit/alpha/alpha1.c SNESTSFormJacobian_Alpha() in src/ts/impls/implicit/alpha/alpha2.c SNESTSFormJacobian_DiscGrad() in src/ts/impls/implicit/discgrad/tsdiscgrad.c SNESTSFormJacobian_GLLE() in src/ts/impls/implicit/glle/glle.c SNESTSFormJacobian_IRK() in src/ts/impls/implicit/irk/irk.c SNESTSFormJacobian_Theta() in src/ts/impls/implicit/theta/theta.c SNESTSFormJacobian_Mimex() in src/ts/impls/mimex/mimex.c SNESTSFormJacobian_Pseudo() in src/ts/impls/pseudo/posindep.c SNESTSFormJacobian_RosW() in src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode SNESTSFormJacobian(SNES snes, Vec U, Mat A, Mat B, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESSetJacobian()
```

---

## Time Stepping ODE and DAE Solvers (TS)#

**URL:** https://petsc.org/release/manualpages/TS/

**Contents:**
- Time Stepping ODE and DAE Solvers (TS)#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Deprecated - Functionality scheduled for removal in the future#
- Single list of manual pages#

The time-stepping (TS) component provides ODE and DAE integrators as well as pseudo-timestepping. TS internally employs SNES to solve the nonlinear problems that arise with implicit methods. User guide chapter: TS: Scalable ODE and DAE Solvers.

DMDATSIFunctionLocalFn

DMDATSIJacobianLocalFn

DMDATSRHSFunctionLocalFn

DMDATSRHSJacobianLocalFn

DMDATSSetIFunctionLocal

DMDATSSetIJacobianLocal

DMDATSSetRHSFunctionLocal

DMDATSSetRHSJacobianLocal

DMTSGetIFunctionLocal

DMTSGetIJacobianLocal

DMTSGetRHSFunctionLocal

DMTSSetIFunctionLocal

DMTSSetIJacobianLocal

DMTSSetRHSFunctionLocal

TSBasicSymplecticType

TSExactFinalTimeOption

TSSundialsMonitorInternalSteps

TSSundialsSetMaxTimeStep

TSSundialsSetMinTimeStep

TS_CONVERGED_ITERATING

TS_CONVERGED_PSEUDO_FATOL

TS_CONVERGED_PSEUDO_FRTOL

TS_DIVERGED_NONLINEAR_SOLVE

TS_DIVERGED_STEP_REJECTED

TSARKIMEXGetFastSlowSplit

TSARKIMEXGetFullyImplicit

TSARKIMEXSetFastSlowSplit

TSARKIMEXSetFullyImplicit

TSAdaptGetScaleSolveFailed

TSAdaptSetAlwaysAccept

TSAdaptSetScaleSolveFailed

TSBASICSYMPLECTICSIEULER

TSBASICSYMPLECTICVELVERLET

TSBasicSymplecticGetType

TSBasicSymplecticSetType

TSComputeIFunctionLinear

TSComputeIJacobianDefaultColor

TSComputeRHSFunctionLinear

TSComputeRHSJacobianConstant

TSDMSwarmMonitorMoments

TSDiscGradGetFormulation

TSDiscGradSetFormulation

TSGetApplicationContext

TSGetEvaluationSolutions

TSGetUseSplitRHSFunction

TSMonitorDrawCtxCreate

TSMonitorDrawCtxDestroy

TSMonitorDrawSolution

TSMonitorDrawSolutionFunction

TSMonitorDrawSolutionPhase

TSMonitorEnvelopeCtxCreate

TSMonitorEnvelopeCtxDestroy

TSMonitorEnvelopeGetBounds

TSMonitorHGCtxDestroy

TSMonitorHGSwarmSolution

TSMonitorLGCtxDestroy

TSMonitorLGCtxNetworkCreate

TSMonitorLGCtxNetworkDestroy

TSMonitorLGCtxNetworkSolution

TSMonitorLGCtxSetDisplayVariables

TSMonitorLGCtxSetTransform

TSMonitorLGCtxSetVariableNames

TSMonitorLGGetVariableNames

TSMonitorLGKSPIterations

TSMonitorLGSNESIterations

TSMonitorLGSetDisplayVariables

TSMonitorLGSetTransform

TSMonitorLGSetVariableNames

TSMonitorSPCtxDestroy

TSMonitorSPEigCtxCreate

TSMonitorSPEigCtxDestroy

TSMonitorSPSwarmSolution

TSMonitorSolutionSetup

TSMonitorWallClockTime

TSMonitorWallClockTimeSetUp

TSPruneIJacobianColor

TSRHSJacobianSetReuse

TSRHSSplitSetIFunction

TSRHSSplitSetIJacobian

TSRHSSplitSetRHSFunction

TSRosWSetRecomputeJacobian

TSSetApplicationContext

TSSetErrorIfStepFails

TSSetFunctionDomainError

TSSetMaxStepRejections

TSSetSolutionFunction

TSSetUseSplitRHSFunction

TSSundialsSetTolerance

TSTRAJECTORYSINGLEFILE

TSTRAJECTORYVISUALIZATION

TSTrajectoryMemorySetType

TSTrajectorySetMaxCpsDisk

TSTrajectorySetMaxCpsRAM

TSTrajectorySetMaxUnitsDisk

TSTrajectorySetMaxUnitsRAM

TSTrajectorySetTransform

TSTrajectorySetVariableNames

TSTrajectoryViewFromOptions

TSARKIMEXRegisterDestroy

TSAdaptHistoryGetStep

TSAdaptHistorySetHistory

TSAdaptHistorySetTrajectory

TSAdaptSetFromOptions

TSAdaptSetOptionsPrefix

TSAdaptSetTimeStepIncreaseDelay

TSAppendOptionsPrefix

TSBasicSymplecticRegister

TSBasicSymplecticRegisterAll

TSBasicSymplecticRegisterDestroy

TSComputeIJacobianConstant

TSComputeInitialCondition

TSGLEERegisterDestroy

TSGLLEAdaptRegisterAll

TSGLLEAdaptSetFromOptions

TSGLLEAdaptSetOptionsPrefix

TSGetComputeExactError

TSGetComputeInitialCondition

TSGetSolutionComponents

TSMPRKRegisterDestroy

TSPseudoComputeFunction

TSPseudoIncrementDtFromInitialDt

TSPseudoSetMaxTimeStep

TSPseudoSetTimeStepIncrement

TSPseudoSetVerifyTimeStep

TSPseudoTimeStepDefault

TSRHSJacobianTestTranspose

TSRosWRegisterDestroy

TSSetComputeExactError

TSSetComputeInitialCondition

TSSetPostEventSecondStep

TSSetTransientVariable

TSSundialsGetIterations

TSSundialsGramSchmidtType

TSSundialsSetGramSchmidtType

TSSundialsSetLinearTolerance

TSSundialsSetUseDense

TSTrajectoryMemoryType

TSTrajectorySetKeepFiles

TSTrajectorySetUseHistory

TSTransientVariableFn

TSVISetVariableBounds

DMPlexTSComputeBoundary

DMPlexTSComputeIFunctionFEM

DMPlexTSComputeIJacobianFEM

DMPlexTSComputeRHSFunctionFEM

DMPlexTSComputeRHSFunctionFVM

DMPlexTSComputeRHSFunctionFVMCEED

DMTSCreateRHSMassMatrix

DMTSCreateRHSMassMatrixLumped

DMTSDestroyRHSMassMatrix

DMTSGetForcingFunction

DMTSGetSolutionFunction

DMTSGetTransientVariable

DMTSSetForcingFunction

DMTSSetI2FunctionContextDestroy

DMTSSetI2JacobianContextDestroy

DMTSSetIFunctionContextDestroy

DMTSSetIFunctionSerialize

DMTSSetIJacobianContextDestroy

DMTSSetIJacobianSerialize

DMTSSetRHSFunctionContextDestroy

DMTSSetRHSJacobianContextDestroy

DMTSSetSolutionFunction

DMTSSetTransientVariable

TSARKIMEXFinalizePackage

TSARKIMEXInitializePackage

TSAdaptCandidatesClear

TSAdaptFinalizePackage

TSAdaptInitializePackage

TSBasicSymplecticFinalizePackage

TSBasicSymplecticInitializePackage

TSComputeForcingFunction

TSComputeLinearStability

TSComputeSolutionFunction

TSComputeTransientVariable

TSFunctionDomainError

TSGLEEFinalizePackage

TSGLEEInitializePackage

TSGLLEAdaptFinalizePackage

TSGLLEAdaptInitializePackage

TSGLLEFinalizePackage

TSGLLEInitializePackage

TSHasTransientVariable

TSIRKInitializePackage

TSMPRKFinalizePackage

TSMPRKInitializePackage

TSMonitorDMDARayDestroy

TSMonitorLGCtxNetwork

TSMonitorSetFromOptions

TSMonitorSolutionVTKCtxCreate

TSMonitorSolutionVTKDestroy

TSRKInitializePackage

TSRosWFinalizePackage

TSRosWInitializePackage

TSSSPInitializePackage

TSTrajectoryGetNumSteps

TSTrajectoryGetSolutionOnly

TSTrajectoryGetUpdatedHistoryVecs

TSTrajectoryRegisterAll

TSTrajectoryRestoreUpdatedHistoryVecs

TSTrajectorySetDirname

TSTrajectorySetFiletemplate

TSTrajectorySetFromOptions

TSTrajectorySetMonitor

TSTrajectorySetSolutionOnly

TSGetTimeSpanSolutions

DMDATSIFunctionLocalFn

DMDATSIJacobianLocalFn

DMDATSRHSFunctionLocalFn

DMDATSRHSJacobianLocalFn

DMDATSSetIFunctionLocal

DMDATSSetIJacobianLocal

DMDATSSetRHSFunctionLocal

DMDATSSetRHSJacobianLocal

DMPlexTSComputeBoundary

DMPlexTSComputeIFunctionFEM

DMPlexTSComputeIJacobianFEM

DMPlexTSComputeRHSFunctionFEM

DMPlexTSComputeRHSFunctionFVM

DMPlexTSComputeRHSFunctionFVMCEED

DMTSCreateRHSMassMatrix

DMTSCreateRHSMassMatrixLumped

DMTSDestroyRHSMassMatrix

DMTSGetForcingFunction

DMTSGetIFunctionLocal

DMTSGetIJacobianLocal

DMTSGetRHSFunctionLocal

DMTSGetSolutionFunction

DMTSGetTransientVariable

DMTSSetForcingFunction

DMTSSetI2FunctionContextDestroy

DMTSSetI2JacobianContextDestroy

DMTSSetIFunctionContextDestroy

DMTSSetIFunctionLocal

DMTSSetIFunctionSerialize

DMTSSetIJacobianContextDestroy

DMTSSetIJacobianLocal

DMTSSetIJacobianSerialize

DMTSSetRHSFunctionContextDestroy

DMTSSetRHSFunctionLocal

DMTSSetRHSJacobianContextDestroy

DMTSSetSolutionFunction

DMTSSetTransientVariable

TSARKIMEXFinalizePackage

TSARKIMEXGetFastSlowSplit

TSARKIMEXGetFullyImplicit

TSARKIMEXInitializePackage

TSARKIMEXRegisterDestroy

TSARKIMEXSetFastSlowSplit

TSARKIMEXSetFullyImplicit

TSAdaptCandidatesClear

TSAdaptFinalizePackage

TSAdaptGetScaleSolveFailed

TSAdaptHistoryGetStep

TSAdaptHistorySetHistory

TSAdaptHistorySetTrajectory

TSAdaptInitializePackage

TSAdaptSetAlwaysAccept

TSAdaptSetFromOptions

TSAdaptSetOptionsPrefix

TSAdaptSetScaleSolveFailed

TSAdaptSetTimeStepIncreaseDelay

TSAppendOptionsPrefix

TSBASICSYMPLECTICSIEULER

TSBASICSYMPLECTICVELVERLET

TSBasicSymplecticFinalizePackage

TSBasicSymplecticGetType

TSBasicSymplecticInitializePackage

TSBasicSymplecticRegister

TSBasicSymplecticRegisterAll

TSBasicSymplecticRegisterDestroy

TSBasicSymplecticSetType

TSBasicSymplecticType

TSComputeForcingFunction

TSComputeIFunctionLinear

TSComputeIJacobianConstant

TSComputeIJacobianDefaultColor

TSComputeInitialCondition

TSComputeLinearStability

TSComputeRHSFunctionLinear

TSComputeRHSJacobianConstant

TSComputeSolutionFunction

TSComputeTransientVariable

TSDMSwarmMonitorMoments

TSDiscGradGetFormulation

TSDiscGradSetFormulation

TSExactFinalTimeOption

TSFunctionDomainError

TSGLEEFinalizePackage

TSGLEEInitializePackage

TSGLEERegisterDestroy

TSGLLEAdaptFinalizePackage

TSGLLEAdaptInitializePackage

TSGLLEAdaptRegisterAll

TSGLLEAdaptSetFromOptions

TSGLLEAdaptSetOptionsPrefix

TSGLLEFinalizePackage

TSGLLEInitializePackage

TSGetApplicationContext

TSGetComputeExactError

TSGetComputeInitialCondition

TSGetEvaluationSolutions

TSGetSolutionComponents

TSGetTimeSpanSolutions

TSGetUseSplitRHSFunction

TSHasTransientVariable

TSIRKInitializePackage

TSMPRKFinalizePackage

TSMPRKInitializePackage

TSMPRKRegisterDestroy

TSMonitorDMDARayDestroy

TSMonitorDrawCtxCreate

TSMonitorDrawCtxDestroy

TSMonitorDrawSolution

TSMonitorDrawSolutionFunction

TSMonitorDrawSolutionPhase

TSMonitorEnvelopeCtxCreate

TSMonitorEnvelopeCtxDestroy

TSMonitorEnvelopeGetBounds

TSMonitorHGCtxDestroy

TSMonitorHGSwarmSolution

TSMonitorLGCtxDestroy

TSMonitorLGCtxNetwork

TSMonitorLGCtxNetworkCreate

TSMonitorLGCtxNetworkDestroy

TSMonitorLGCtxNetworkSolution

TSMonitorLGCtxSetDisplayVariables

TSMonitorLGCtxSetTransform

TSMonitorLGCtxSetVariableNames

TSMonitorLGGetVariableNames

TSMonitorLGKSPIterations

TSMonitorLGSNESIterations

TSMonitorLGSetDisplayVariables

TSMonitorLGSetTransform

TSMonitorLGSetVariableNames

TSMonitorSPCtxDestroy

TSMonitorSPEigCtxCreate

TSMonitorSPEigCtxDestroy

TSMonitorSPSwarmSolution

TSMonitorSetFromOptions

TSMonitorSolutionSetup

TSMonitorSolutionVTKCtxCreate

TSMonitorSolutionVTKDestroy

TSMonitorWallClockTime

TSMonitorWallClockTimeSetUp

TSPruneIJacobianColor

TSPseudoComputeFunction

TSPseudoIncrementDtFromInitialDt

TSPseudoSetMaxTimeStep

TSPseudoSetTimeStepIncrement

TSPseudoSetVerifyTimeStep

TSPseudoTimeStepDefault

TSRHSJacobianSetReuse

TSRHSJacobianTestTranspose

TSRHSSplitSetIFunction

TSRHSSplitSetIJacobian

TSRHSSplitSetRHSFunction

TSRKInitializePackage

TSRosWFinalizePackage

TSRosWInitializePackage

TSRosWRegisterDestroy

TSRosWSetRecomputeJacobian

TSSSPInitializePackage

TSSetApplicationContext

TSSetComputeExactError

TSSetComputeInitialCondition

TSSetErrorIfStepFails

TSSetFunctionDomainError

TSSetMaxStepRejections

TSSetPostEventSecondStep

TSSetSolutionFunction

TSSetTransientVariable

TSSetUseSplitRHSFunction

TSSundialsGetIterations

TSSundialsGramSchmidtType

TSSundialsMonitorInternalSteps

TSSundialsSetGramSchmidtType

TSSundialsSetLinearTolerance

TSSundialsSetMaxTimeStep

TSSundialsSetMinTimeStep

TSSundialsSetTolerance

TSSundialsSetUseDense

TSTRAJECTORYSINGLEFILE

TSTRAJECTORYVISUALIZATION

TSTrajectoryGetNumSteps

TSTrajectoryGetSolutionOnly

TSTrajectoryGetUpdatedHistoryVecs

TSTrajectoryMemorySetType

TSTrajectoryMemoryType

TSTrajectoryRegisterAll

TSTrajectoryRestoreUpdatedHistoryVecs

TSTrajectorySetDirname

TSTrajectorySetFiletemplate

TSTrajectorySetFromOptions

TSTrajectorySetKeepFiles

TSTrajectorySetMaxCpsDisk

TSTrajectorySetMaxCpsRAM

TSTrajectorySetMaxUnitsDisk

TSTrajectorySetMaxUnitsRAM

TSTrajectorySetMonitor

TSTrajectorySetSolutionOnly

TSTrajectorySetTransform

TSTrajectorySetUseHistory

TSTrajectorySetVariableNames

TSTrajectoryViewFromOptions

TSTransientVariableFn

TSVISetVariableBounds

TS_CONVERGED_ITERATING

TS_CONVERGED_PSEUDO_FATOL

TS_CONVERGED_PSEUDO_FRTOL

TS_DIVERGED_NONLINEAR_SOLVE

TS_DIVERGED_STEP_REJECTED

Forward and Adjoint Timestepping

Sensitivity Analysis for ODE and DAE

---

## TS2GetSolution#

**URL:** https://petsc.org/release/manualpages/TS/TS2GetSolution/

**Contents:**
- TS2GetSolution#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Returns the solution and time derivative at the present timestep for second order equations.

ts - the TS context obtained from TSCreate()

u - the vector containing the solution

v - the vector containing the time derivative

It is valid to call this routine inside the function that you are evaluating in order to move to the new timestep. This vector not changed until the solution at the next timestep has been calculated.

TS: Scalable ODE and DAE Solvers, TS, TS2SetSolution(), TSGetTimeStep(), TSGetTime()

src/ts/interface/ts.c

src/ts/tutorials/ex44.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TS2GetSolution(TS ts, Vec *u, Vec *v)
```

Example 2 (unknown):
```unknown
TS2SetSolution()
```

Example 3 (unknown):
```unknown
TSGetTimeStep()
```

Example 4 (unknown):
```unknown
TSGetTime()
```

---

## TS2SetSolution#

**URL:** https://petsc.org/release/manualpages/TS/TS2SetSolution/

**Contents:**
- TS2SetSolution#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the initial solution and time derivative vectors for use by the TS routines handling second order equations.

ts - the TS context obtained from TSCreate()

u - the solution vector

v - the time derivative vector

TS: Scalable ODE and DAE Solvers, TS

src/ts/interface/ts.c

src/ts/tutorials/ex44.c src/ts/tutorials/ex43.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TS2SetSolution(TS ts, Vec u, Vec v)
```

---

## TSADAPTBASIC#

**URL:** https://petsc.org/release/manualpages/TS/TSADAPTBASIC/

**Contents:**
- TSADAPTBASIC#
- See Also#
- Level#
- Location#
- Examples#

Basic adaptive controller for time stepping

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TS, TSAdapt, TSGetAdapt(), TSAdaptType

src/ts/adapt/impls/basic/adaptbasic.c

src/ts/tutorials/ex41.c src/ts/tutorials/ex40.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGetAdapt()
```

Example 2 (unknown):
```unknown
TSAdaptType
```

---

## TSAdaptCandidateAdd#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptCandidateAdd/

**Contents:**
- TSAdaptCandidateAdd#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

add a candidate scheme for the adaptive controller to select from

Logically Collective; No Fortran Support

adapt - time step adaptivity context, obtained with TSGetAdapt() or TSAdaptCreate()

name - name of the candidate scheme to add

order - order of the candidate scheme

stageorder - stage order of the candidate scheme

ccfl - stability coefficient relative to explicit Euler, used for CFL constraints

cost - relative measure of the amount of work required for the candidate scheme

inuse - indicates that this scheme is the one currently in use, this flag can only be set for one scheme

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt, TSAdaptCandidatesClear(), TSAdaptChoose()

src/ts/adapt/interface/tsadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptCandidateAdd(TSAdapt adapt, const char name[], PetscInt order, PetscInt stageorder, PetscReal ccfl, PetscReal cost, PetscBool inuse)
```

Example 2 (unknown):
```unknown
TSGetAdapt()
```

Example 3 (unknown):
```unknown
TSAdaptCreate()
```

Example 4 (unknown):
```unknown
TSAdaptCandidatesClear()
```

---

## TSAdaptCandidatesClear#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptCandidatesClear/

**Contents:**
- TSAdaptCandidatesClear#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

clear any previously set candidate schemes

adapt - adaptive controller

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt, TSAdaptCreate(), TSAdaptCandidateAdd(), TSAdaptChoose()

src/ts/adapt/interface/tsadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptCandidatesClear(TSAdapt adapt)
```

Example 2 (unknown):
```unknown
TSAdaptCreate()
```

Example 3 (unknown):
```unknown
TSAdaptCandidateAdd()
```

Example 4 (unknown):
```unknown
TSAdaptChoose()
```

---

## TSAdaptCandidatesGet#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptCandidatesGet/

**Contents:**
- TSAdaptCandidatesGet#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Get the list of candidate orders of accuracy and cost

adapt - time step adaptivity context

n - number of candidate schemes, always at least 1

order - the order of each candidate scheme

stageorder - the stage order of each candidate scheme

ccfl - the CFL coefficient of each scheme

cost - the relative cost of each scheme

The current scheme is always returned in the first slot

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt, TSAdaptCandidatesClear(), TSAdaptCandidateAdd(), TSAdaptChoose()

src/ts/adapt/interface/tsadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptCandidatesGet(TSAdapt adapt, PetscInt *n, const PetscInt **order, const PetscInt **stageorder, const PetscReal **ccfl, const PetscReal **cost)
```

Example 2 (unknown):
```unknown
TSAdaptCandidatesClear()
```

Example 3 (unknown):
```unknown
TSAdaptCandidateAdd()
```

Example 4 (unknown):
```unknown
TSAdaptChoose()
```

---

## TSADAPTCFL#

**URL:** https://petsc.org/release/manualpages/TS/TSADAPTCFL/

**Contents:**
- TSADAPTCFL#
- See Also#
- Level#
- Location#

CFL adaptive controller for time stepping

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TS, TSAdapt, TSGetAdapt(), TSAdaptType

src/ts/adapt/impls/cfl/adaptcfl.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGetAdapt()
```

Example 2 (unknown):
```unknown
TSAdaptType
```

---

## TSAdaptCheckStage#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptCheckStage/

**Contents:**
- TSAdaptCheckStage#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

checks whether to accept a stage, (e.g. reject and change time step size if nonlinear solve fails or solution vector is infeasible)

adapt - adaptive controller context

t - Current simulation time

Y - Current solution vector

accept - PETSC_TRUE to accept the stage, PETSC_FALSE to reject

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt

src/ts/adapt/interface/tsadapt.c

TSAdaptCheckStage_TSPseudo() in src/ts/impls/pseudo/posindep.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptCheckStage(TSAdapt adapt, TS ts, PetscReal t, Vec Y, PetscBool *accept)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

---

## TSAdaptChoose#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptChoose/

**Contents:**
- TSAdaptChoose#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

choose which method and step size to use for the next step

adapt - adaptive controller

h - current step size

next_sc - optional, scheme to use for the next step

next_h - step size to use for the next step

accept - PETSC_TRUE to accept the current step, PETSC_FALSE to repeat the current step with the new step size

The input value of parameter accept is retained from the last time step, so it will be PETSC_FALSE if the step is being retried after an initial rejection.

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt, TSAdaptCandidatesClear(), TSAdaptCandidateAdd()

src/ts/adapt/interface/tsadapt.c

TSAdaptChoose_Basic() in src/ts/adapt/impls/basic/adaptbasic.c TSAdaptChoose_CFL() in src/ts/adapt/impls/cfl/adaptcfl.c TSAdaptChoose_DSP() in src/ts/adapt/impls/dsp/adaptdsp.c TSAdaptChoose_GLEE() in src/ts/adapt/impls/glee/adaptglee.c TSAdaptChoose_History() in src/ts/adapt/impls/history/adapthist.c TSAdaptChoose_None() in src/ts/adapt/impls/none/adaptnone.c TSAdaptChoose_TSPseudo() in src/ts/impls/pseudo/posindep.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptChoose(TSAdapt adapt, TS ts, PetscReal h, PetscInt *next_sc, PetscReal *next_h, PetscBool *accept)
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
TSAdaptCandidatesClear()
```

---

## TSAdaptCreate#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptCreate/

**Contents:**
- TSAdaptCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

create an adaptive controller context for time stepping

comm - The communicator

inadapt - new TSAdapt object

TSAdapt creation is handled by TS, so users should not need to call this function.

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt, TSGetAdapt(), TSAdaptSetType(), TSAdaptDestroy()

src/ts/adapt/interface/tsadapt.c

TSAdaptCreate_Basic() in src/ts/adapt/impls/basic/adaptbasic.c TSAdaptCreate_CFL() in src/ts/adapt/impls/cfl/adaptcfl.c TSAdaptCreate_DSP() in src/ts/adapt/impls/dsp/adaptdsp.c TSAdaptCreate_GLEE() in src/ts/adapt/impls/glee/adaptglee.c TSAdaptCreate_History() in src/ts/adapt/impls/history/adapthist.c TSAdaptCreate_None() in src/ts/adapt/impls/none/adaptnone.c TSAdaptCreate_TSPseudo() in src/ts/impls/pseudo/posindep.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptCreate(MPI_Comm comm, TSAdapt *inadapt)
```

Example 2 (unknown):
```unknown
TSGetAdapt()
```

Example 3 (unknown):
```unknown
TSAdaptSetType()
```

Example 4 (unknown):
```unknown
TSAdaptDestroy()
```

---

## TSAdaptDestroy#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptDestroy/

**Contents:**
- TSAdaptDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Destroys a TSAdapt context

adapt - the TSAdapt context obtained from TSGetAdapt() or TSAdaptCreate()

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt, TSAdaptCreate(), TSGetAdapt()

src/ts/adapt/interface/tsadapt.c

TSAdaptDestroy_DSP() in src/ts/adapt/impls/dsp/adaptdsp.c TSAdaptDestroy_GLEE() in src/ts/adapt/impls/glee/adaptglee.c TSAdaptDestroy_History() in src/ts/adapt/impls/history/adapthist.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptDestroy(TSAdapt *adapt)
```

Example 2 (unknown):
```unknown
TSGetAdapt()
```

Example 3 (unknown):
```unknown
TSAdaptCreate()
```

Example 4 (unknown):
```unknown
TSAdaptCreate()
```

---

## TSAdaptDSPSetFilter#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptDSPSetFilter/

**Contents:**
- TSAdaptDSPSetFilter#
- Synopsis#
- Input Parameters#
- Options Database Key#
- References#
- See Also#
- Level#
- Location#
- Implementations#

Sets internal parameters corresponding to the named filter [SoderlindW06] [Soderlind03]

adapt - adaptive controller context

-ts_adapt_dsp_filter name - Sets predefined controller by name; use -help for a list of available controllers

basic - similar to TSADAPTBASIC but with different criteria for step rejections.

PI30, PI42, PI33, PI34 - PI controllers.

PC11, PC47, PC36 - predictive controllers.

H0211, H211b, H211PI - digital filters with orders dynamics=2, adaptivity=1, filter=1.

H0312, H312b, H312PID - digital filters with orders dynamics=3, adaptivity=1, filter=2.

H0321, H321 - digital filters with orders dynamics=3, adaptivity=2, filter=1.

Gustaf Söderlind. Digital filters in adaptive time-stepping. ACM Transactions on Mathematical Software (TOMS), 29(1):1–26, 2003.

Gustaf Söderlind and Lina Wang. Adaptive time-stepping and computational stability. Journal of Computational and Applied Mathematics, 185(2):225–243, 2006.

TS: Scalable ODE and DAE Solvers, TSADAPTDSP, TS, TSAdapt, TSGetAdapt(), TSAdaptDSPSetPID()

src/ts/adapt/impls/dsp/adaptdsp.c

TSAdaptDSPSetFilter_DSP() in src/ts/adapt/impls/dsp/adaptdsp.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptDSPSetFilter(TSAdapt adapt, const char name[])
```

Example 2 (unknown):
```unknown
TSADAPTBASIC
```

Example 3 (unknown):
```unknown
TSGetAdapt()
```

Example 4 (unknown):
```unknown
TSAdaptDSPSetPID()
```

---

## TSAdaptDSPSetPID#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptDSPSetPID/

**Contents:**
- TSAdaptDSPSetPID#
- Synopsis#
- Input Parameters#
- Options Database Key#
- References#
- See Also#
- Level#
- Location#
- Implementations#

Set the PID controller parameters [SoderlindW06] [Soderlind03]

adapt - adaptive controller context

kkI - Integral parameter

kkP - Proportional parameter

kkD - Derivative parameter

-ts_adapt_dsp_pid kkI,kkP,kkD - Sets PID controller parameters

Gustaf Söderlind. Digital filters in adaptive time-stepping. ACM Transactions on Mathematical Software (TOMS), 29(1):1–26, 2003.

Gustaf Söderlind and Lina Wang. Adaptive time-stepping and computational stability. Journal of Computational and Applied Mathematics, 185(2):225–243, 2006.

TS: Scalable ODE and DAE Solvers, TS, TSAdapt, TSGetAdapt(), TSAdaptDSPSetFilter()

src/ts/adapt/impls/dsp/adaptdsp.c

TSAdaptDSPSetPID_DSP() in src/ts/adapt/impls/dsp/adaptdsp.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptDSPSetPID(TSAdapt adapt, PetscReal kkI, PetscReal kkP, PetscReal kkD)
```

Example 2 (unknown):
```unknown
TSGetAdapt()
```

Example 3 (unknown):
```unknown
TSAdaptDSPSetFilter()
```

---

## TSADAPTDSP#

**URL:** https://petsc.org/release/manualpages/TS/TSADAPTDSP/

**Contents:**
- TSADAPTDSP#
- Options Database Keys#
- References#
- See Also#
- Level#
- Location#

Adaptive controller for time-stepping based on digital signal processing (DSP) [SoderlindW06] [Soderlind03]

-ts_adapt_dsp_filter name - Sets predefined controller by name; use -help for a list of available controllers

-ts_adapt_dsp_pid kkI,kkP,kkD - Sets PID controller parameters

-ts_adapt_dsp_kbeta b1,b2,b2 - Sets general filter parameters

-ts_adapt_dsp_alpha a2,a3 - Sets general filter parameters

Gustaf Söderlind. Digital filters in adaptive time-stepping. ACM Transactions on Mathematical Software (TOMS), 29(1):1–26, 2003.

Gustaf Söderlind and Lina Wang. Adaptive time-stepping and computational stability. Journal of Computational and Applied Mathematics, 185(2):225–243, 2006.

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TS, TSAdapt, TSGetAdapt(), TSAdaptDSPSetPID(), TSAdaptDSPSetFilter(), TSAdaptType

src/ts/adapt/impls/dsp/adaptdsp.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGetAdapt()
```

Example 2 (unknown):
```unknown
TSAdaptDSPSetPID()
```

Example 3 (unknown):
```unknown
TSAdaptDSPSetFilter()
```

Example 4 (unknown):
```unknown
TSAdaptType
```

---

## TSAdaptFinalizePackage#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptFinalizePackage/

**Contents:**
- TSAdaptFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys everything in the TS package. It is called from PetscFinalize().

TS: Scalable ODE and DAE Solvers, PetscFinalize()

src/ts/adapt/interface/tsadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptFinalizePackage(void)
```

Example 3 (unknown):
```unknown
PetscFinalize()
```

---

## TSAdaptGetClip#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptGetClip/

**Contents:**
- TSAdaptGetClip#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Gets the admissible decrease/increase factor in step size in the time step adapter

adapt - adaptive controller context

low - optional, admissible decrease factor

high - optional, admissible increase factor

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt, TSAdaptChoose(), TSAdaptSetClip(), TSAdaptSetScaleSolveFailed()

src/ts/adapt/interface/tsadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptGetClip(TSAdapt adapt, PetscReal *low, PetscReal *high)
```

Example 2 (unknown):
```unknown
TSAdaptChoose()
```

Example 3 (unknown):
```unknown
TSAdaptSetClip()
```

Example 4 (unknown):
```unknown
TSAdaptSetScaleSolveFailed()
```

---

## TSAdaptGetMaxIgnore#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptGetMaxIgnore/

**Contents:**
- TSAdaptGetMaxIgnore#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get error estimation threshold. Solution components below this threshold value will not be considered when computing error norms for time step adaptivity (in absolute value).

adapt - adaptive controller context

max_ignore - threshold for solution components that are ignored during error estimation

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt, TSAdaptSetMaxIgnore(), TSAdaptChoose()

src/ts/adapt/interface/tsadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptGetMaxIgnore(TSAdapt adapt, PetscReal *max_ignore)
```

Example 2 (unknown):
```unknown
TSAdaptSetMaxIgnore()
```

Example 3 (unknown):
```unknown
TSAdaptChoose()
```

---

## TSAdaptGetSafety#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptGetSafety/

**Contents:**
- TSAdaptGetSafety#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Get safety factors for time step adapter

adapt - adaptive controller context

safety - safety factor relative to target error/stability goal

reject_safety - extra safety factor to apply if the last step was rejected

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt, TSAdaptSetSafety(), TSAdaptChoose()

src/ts/adapt/interface/tsadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptGetSafety(TSAdapt adapt, PetscReal *safety, PetscReal *reject_safety)
```

Example 2 (unknown):
```unknown
TSAdaptSetSafety()
```

Example 3 (unknown):
```unknown
TSAdaptChoose()
```

---

## TSAdaptGetScaleSolveFailed#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptGetScaleSolveFailed/

**Contents:**
- TSAdaptGetScaleSolveFailed#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the admissible decrease/increase factor in step size

adapt - adaptive controller context

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt, TSAdaptChoose(), TSAdaptSetScaleSolveFailed(), TSAdaptSetClip()

src/ts/adapt/interface/tsadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptGetScaleSolveFailed(TSAdapt adapt, PetscReal *scale)
```

Example 2 (unknown):
```unknown
TSAdaptChoose()
```

Example 3 (unknown):
```unknown
TSAdaptSetScaleSolveFailed()
```

Example 4 (unknown):
```unknown
TSAdaptSetClip()
```

---

## TSAdaptGetStepLimits#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptGetStepLimits/

**Contents:**
- TSAdaptGetStepLimits#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Get the minimum and maximum step sizes to be considered by the time step controller

adapt - time step adaptivity context, usually gotten with TSGetAdapt()

hmin - minimum time step

hmax - maximum time step

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt, TSAdaptSetStepLimits(), TSAdaptChoose()

src/ts/adapt/interface/tsadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptGetStepLimits(TSAdapt adapt, PetscReal *hmin, PetscReal *hmax)
```

Example 2 (unknown):
```unknown
TSGetAdapt()
```

Example 3 (unknown):
```unknown
TSAdaptSetStepLimits()
```

Example 4 (unknown):
```unknown
TSAdaptChoose()
```

---

## TSAdaptGetType#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptGetType/

**Contents:**
- TSAdaptGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

gets the TS adapter method type (as a string).

adapt - The TS adapter, most likely obtained with TSGetAdapt()

type - The name of TS adapter method

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt, TSAdaptType, TSAdaptSetType()

src/ts/adapt/interface/tsadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptGetType(TSAdapt adapt, TSAdaptType *type)
```

Example 2 (unknown):
```unknown
TSGetAdapt()
```

Example 3 (unknown):
```unknown
TSAdaptType
```

Example 4 (unknown):
```unknown
TSAdaptSetType()
```

---

## TSADAPTGLEE#

**URL:** https://petsc.org/release/manualpages/TS/TSADAPTGLEE/

**Contents:**
- TSADAPTGLEE#
- See Also#
- Level#
- Location#

GLEE adaptive controller for time stepping

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TS, TSAdapt, TSGetAdapt(), TSAdaptType

src/ts/adapt/impls/glee/adaptglee.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGetAdapt()
```

Example 2 (unknown):
```unknown
TSAdaptType
```

---

## TSAdaptHistoryGetStep#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptHistoryGetStep/

**Contents:**
- TSAdaptHistoryGetStep#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets time and time step for a given step number in the history

adapt - the TSAdapt context

step - the step number

t - the time corresponding to the requested step (can be NULL)

dt - the time step to be taken at the requested step (can be NULL)

The time history is internally copied, and the user can free the hist array. The user still needs to specify the termination of the solve via TSSetMaxSteps().

TS: Scalable ODE and DAE Solvers, TS, TSGetAdapt(), TSAdaptSetType(), TSAdaptHistorySetTrajectory(), TSADAPTHISTORY

src/ts/adapt/impls/history/adapthist.c

src/ts/tutorials/ex41.c src/ts/tutorials/ex40.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptHistoryGetStep(TSAdapt adapt, PetscInt step, PetscReal *t, PetscReal *dt)
```

Example 2 (unknown):
```unknown
TSSetMaxSteps()
```

Example 3 (unknown):
```unknown
TSGetAdapt()
```

Example 4 (unknown):
```unknown
TSAdaptSetType()
```

---

## TSAdaptHistorySetHistory#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptHistorySetHistory/

**Contents:**
- TSAdaptHistorySetHistory#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the time history in the adaptor

adapt - the TSAdapt context

n - size of the time history

hist - the time history

backward - if the time history has to be followed backward

The time history is internally copied, and the user can free the hist array. The user still needs to specify the termination of the solve via TSSetMaxSteps().

TS: Scalable ODE and DAE Solvers, TSGetAdapt(), TSAdaptSetType(), TSAdaptHistorySetTrajectory(), TSADAPTHISTORY

src/ts/adapt/impls/history/adapthist.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptHistorySetHistory(TSAdapt adapt, PetscInt n, PetscReal hist[], PetscBool backward)
```

Example 2 (unknown):
```unknown
TSSetMaxSteps()
```

Example 3 (unknown):
```unknown
TSGetAdapt()
```

Example 4 (unknown):
```unknown
TSAdaptSetType()
```

---

## TSAdaptHistorySetTrajectory#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptHistorySetTrajectory/

**Contents:**
- TSAdaptHistorySetTrajectory#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets a time history in the adaptor from a given TSTrajectory

adapt - the TSAdapt context

tj - the TSTrajectory context

backward - if the time history has to be followed backward

The time history is internally copied, and the user can destroy the TSTrajectory if not needed.

The user still needs to specify the termination of the solve via TSSetMaxSteps().

TS: Scalable ODE and DAE Solvers, TSGetAdapt(), TSAdaptSetType(), TSAdaptHistorySetHistory(), TSADAPTHISTORY, TSAdapt

src/ts/adapt/impls/history/adapthist.c

src/ts/tutorials/ex41.c src/ts/tutorials/ex40.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSTrajectory
```

Example 2 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptHistorySetTrajectory(TSAdapt adapt, TSTrajectory tj, PetscBool backward)
```

Example 3 (unknown):
```unknown
TSTrajectory
```

Example 4 (unknown):
```unknown
TSTrajectory
```

---

## TSADAPTHISTORY#

**URL:** https://petsc.org/release/manualpages/TS/TSADAPTHISTORY/

**Contents:**
- TSADAPTHISTORY#
- See Also#
- Level#
- Location#
- Examples#

Time stepping controller that follows a given time history, used for Tangent Linear Model simulations

TS: Scalable ODE and DAE Solvers, TS, TSAdapt, TSGetAdapt(), TSAdaptHistorySetHistory(), TSAdaptType

src/ts/adapt/impls/history/adapthist.c

src/ts/tutorials/ex41.c src/ts/tutorials/ex40.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGetAdapt()
```

Example 2 (unknown):
```unknown
TSAdaptHistorySetHistory()
```

Example 3 (unknown):
```unknown
TSAdaptType
```

---

## TSAdaptInitializePackage#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptInitializePackage/

**Contents:**
- TSAdaptInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function initializes everything in the TSAdapt package. It is called from TSInitializePackage().

TS: Scalable ODE and DAE Solvers, PetscInitialize()

src/ts/adapt/interface/tsadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSInitializePackage()
```

Example 2 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptInitializePackage(void)
```

Example 3 (unknown):
```unknown
PetscInitialize()
```

---

## TSAdaptLoad#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptLoad/

**Contents:**
- TSAdaptLoad#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Loads a TSAdapt that has been stored in binary with TSAdaptView().

adapt - the newly loaded TSAdapt, this needs to have been created with TSAdaptCreate() or some related function before a call to TSAdaptLoad().

viewer - binary file viewer, obtained from PetscViewerBinaryOpen() or HDF5 file viewer, obtained from PetscViewerHDF5Open()

The type is determined by the data in the file, any type set into the TSAdapt before this call is ignored.

TS: Scalable ODE and DAE Solvers, PetscViewerBinaryOpen(), TSAdaptView(), MatLoad(), VecLoad(), TSAdapt

src/ts/adapt/interface/tsadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSAdaptView()
```

Example 2 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptLoad(TSAdapt adapt, PetscViewer viewer)
```

Example 3 (unknown):
```unknown
TSAdaptCreate()
```

Example 4 (unknown):
```unknown
TSAdaptLoad()
```

---

## TSADAPTNONE#

**URL:** https://petsc.org/release/manualpages/TS/TSADAPTNONE/

**Contents:**
- TSADAPTNONE#
- See Also#
- Level#
- Location#
- Examples#

Time stepping controller that always accepts the current step and does not change it

TS: Scalable ODE and DAE Solvers, TS, TSAdapt, TSAdaptChoose(), TSAdaptType

src/ts/adapt/impls/none/adaptnone.c

src/ts/tutorials/ex51.c src/ts/utils/dmplexlandau/tutorials/ex1.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSAdaptChoose()
```

Example 2 (unknown):
```unknown
TSAdaptType
```

---

## TSAdaptRegisterAll#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptRegisterAll/

**Contents:**
- TSAdaptRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the adaptivity schemes in TSAdapt

TS: Scalable ODE and DAE Solvers, TSAdaptRegisterDestroy()

src/ts/adapt/interface/tsadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptRegisterAll(void)
```

Example 2 (unknown):
```unknown
TSAdaptRegisterDestroy()
```

---

## TSAdaptRegister#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptRegister/

**Contents:**
- TSAdaptRegister#
- Synopsis#
- Input Parameters#
- Notes#
- Example Usage#
- See Also#
- Level#
- Location#

adds a TSAdapt implementation

Not Collective, No Fortran Support

sname - name of user-defined adaptivity scheme

function - routine to create method context

TSAdaptRegister() may be called multiple times to add several user-defined families.

Then, your scheme can be chosen with the procedural interface via

or at runtime via the option

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdaptRegisterAll()

src/ts/adapt/interface/tsadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptRegister(const char sname[], PetscErrorCode (*function)(TSAdapt))
```

Example 2 (unknown):
```unknown
TSAdaptRegister()
```

Example 3 (unknown):
```unknown
TSAdaptRegister("my_scheme", MySchemeCreate);
```

Example 4 (unknown):
```unknown
TSAdaptSetType(ts, "my_scheme")
```

---

## TSAdaptReset#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptReset/

**Contents:**
- TSAdaptReset#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Resets a TSAdapt context to its defaults

adapt - the TSAdapt context obtained from TSGetAdapt() or TSAdaptCreate()

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSGetAdapt(), TSAdapt, TSAdaptCreate(), TSAdaptDestroy()

src/ts/adapt/interface/tsadapt.c

TSAdaptReset_GLEE() in src/ts/adapt/impls/glee/adaptglee.c TSAdaptReset_History() in src/ts/adapt/impls/history/adapthist.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptReset(TSAdapt adapt)
```

Example 2 (unknown):
```unknown
TSGetAdapt()
```

Example 3 (unknown):
```unknown
TSAdaptCreate()
```

Example 4 (unknown):
```unknown
TSGetAdapt()
```

---

## TSAdaptSetAlwaysAccept#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptSetAlwaysAccept/

**Contents:**
- TSAdaptSetAlwaysAccept#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Set whether to always accept steps regardless of any error or stability condition not meeting the prescribed goal.

adapt - time step adaptivity context, usually gotten with TSGetAdapt()

flag - whether to always accept steps

-ts_adapt_always_accept - to always accept steps

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt, TSGetAdapt(), TSAdaptChoose()

src/ts/adapt/interface/tsadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptSetAlwaysAccept(TSAdapt adapt, PetscBool flag)
```

Example 2 (unknown):
```unknown
TSGetAdapt()
```

Example 3 (unknown):
```unknown
TSGetAdapt()
```

Example 4 (unknown):
```unknown
TSAdaptChoose()
```

---

## TSAdaptSetCheckStage#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptSetCheckStage/

**Contents:**
- TSAdaptSetCheckStage#
- Synopsis#
- Input Parameters#
- Calling sequence#
- See Also#
- Level#
- Location#

Set a callback to check convergence for a stage

adapt - adaptive controller context

func - stage check function

adapt - adaptive controller context

ts - time stepping context

Y - current solution vector

accept - pending choice of whether to accept, can be modified by this routine

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt, TSGetAdapt(), TSAdaptChoose()

src/ts/adapt/interface/tsadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptSetCheckStage(TSAdapt adapt, PetscErrorCode (*func)(TSAdapt adapt, TS ts, PetscReal t, Vec Y, PetscBool *accept))
```

Example 2 (unknown):
```unknown
TSGetAdapt()
```

Example 3 (unknown):
```unknown
TSAdaptChoose()
```

---

## TSAdaptSetClip#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptSetClip/

**Contents:**
- TSAdaptSetClip#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- Fortran Note#
- See Also#
- Level#
- Location#

Sets the admissible decrease/increase factor in step size in the time step adapter

adapt - adaptive controller context

low - admissible decrease factor

high - admissible increase factor

-ts_adapt_clip low,high - to set admissible time step decrease and increase factors

Use PETSC_CURRENT to keep the current value for either parameter

Use PETSC_CURRENT_REAL

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt, TSAdaptChoose(), TSAdaptGetClip(), TSAdaptSetScaleSolveFailed()

src/ts/adapt/interface/tsadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptSetClip(TSAdapt adapt, PetscReal low, PetscReal high)
```

Example 2 (unknown):
```unknown
PETSC_CURRENT
```

Example 3 (unknown):
```unknown
PETSC_CURRENT_REAL
```

Example 4 (unknown):
```unknown
TSAdaptChoose()
```

---

## TSAdaptSetFromOptions#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptSetFromOptions/

**Contents:**
- TSAdaptSetFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Sets various TSAdapt parameters from user options.

adapt - the TSAdapt context

PetscOptionsObject - object created by PetscOptionsBegin()

-ts_adapt_type (basic|dsp|none|cfl|glee|history) - algorithm to use for adaptivity

-ts_adapt_always_accept (true|false) - always accept steps regardless of error/stability goals

-ts_adapt_safety safety - safety factor relative to target error/stability goal

-ts_adapt_reject_safety safety - extra safety factor to apply if the last step was rejected

-ts_adapt_clip low,high - admissible time step decrease and increase factors

-ts_adapt_dt_min min - minimum timestep to use

-ts_adapt_dt_max max - maximum timestep to use

-ts_adapt_scale_solve_failed scale - scale timestep by this factor if a solve fails

-ts_adapt_wnormtype (2|infinity) - type of norm for computing error estimates

-ts_adapt_time_step_increase_delay steps - number of timesteps to delay increasing the time step after it has been decreased due to failed solver

This function is automatically called by TSSetFromOptions()

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt, TSGetAdapt(), TSAdaptSetType(), TSAdaptSetAlwaysAccept(), TSAdaptSetSafety(), TSAdaptSetClip(), TSAdaptSetScaleSolveFailed(), TSAdaptSetStepLimits(), TSAdaptSetMonitor()

src/ts/adapt/interface/tsadapt.c

TSAdaptSetFromOptions_DSP() in src/ts/adapt/impls/dsp/adaptdsp.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptSetFromOptions(TSAdapt adapt, PetscOptionItems PetscOptionsObject)
```

Example 2 (unknown):
```unknown
PetscOptionsBegin()
```

Example 3 (unknown):
```unknown
TSSetFromOptions()
```

Example 4 (unknown):
```unknown
TSGetAdapt()
```

---

## TSAdaptSetMaxIgnore#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptSetMaxIgnore/

**Contents:**
- TSAdaptSetMaxIgnore#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Set error estimation threshold. Solution components below this threshold value will not be considered when computing error norms for time step adaptivity (in absolute value). A negative value (default) of the threshold leads to considering all solution components.

adapt - adaptive controller context

max_ignore - threshold for solution components that are ignored during error estimation

-ts_adapt_max_ignore max_ignore - to set the threshold

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt, TSAdaptGetMaxIgnore(), TSAdaptChoose()

src/ts/adapt/interface/tsadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptSetMaxIgnore(TSAdapt adapt, PetscReal max_ignore)
```

Example 2 (unknown):
```unknown
TSAdaptGetMaxIgnore()
```

Example 3 (unknown):
```unknown
TSAdaptChoose()
```

---

## TSAdaptSetMonitor#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptSetMonitor/

**Contents:**
- TSAdaptSetMonitor#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Monitor the choices made by the adaptive controller

adapt - adaptive controller context

flg - PETSC_TRUE to active a monitor, PETSC_FALSE to disable

-ts_adapt_monitor - to turn on monitoring

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt, TSGetAdapt(), TSAdaptChoose()

src/ts/adapt/interface/tsadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptSetMonitor(TSAdapt adapt, PetscBool flg)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
TSGetAdapt()
```

Example 4 (unknown):
```unknown
TSAdaptChoose()
```

---

## TSAdaptSetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptSetOptionsPrefix/

**Contents:**
- TSAdaptSetOptionsPrefix#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the prefix used for searching for TSAdapt options in the options database

adapt - the TSAdapt context, most likely obtained with TSGetAdapt()

prefix - the prefix to prepend to all option names

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt, TSGetAdapt(), TSSetOptionsPrefix()

src/ts/adapt/interface/tsadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptSetOptionsPrefix(TSAdapt adapt, const char prefix[])
```

Example 2 (unknown):
```unknown
TSGetAdapt()
```

Example 3 (unknown):
```unknown
TSGetAdapt()
```

Example 4 (unknown):
```unknown
TSSetOptionsPrefix()
```

---

## TSAdaptSetSafety#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptSetSafety/

**Contents:**
- TSAdaptSetSafety#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Note#
- Fortran Note#
- See Also#
- Level#
- Location#

Set safety factors for time step adaptor

adapt - adaptive controller context

safety - safety factor relative to target error/stability goal

reject_safety - extra safety factor to apply if the last step was rejected

-ts_adapt_safety safety - to set safety factor

-ts_adapt_reject_safety reject_safety - to set reject safety factor

Use PETSC_CURRENT to keep the current value for either parameter

Use PETSC_CURRENT_REAL

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt, TSAdaptGetSafety(), TSAdaptChoose()

src/ts/adapt/interface/tsadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptSetSafety(TSAdapt adapt, PetscReal safety, PetscReal reject_safety)
```

Example 2 (unknown):
```unknown
PETSC_CURRENT
```

Example 3 (unknown):
```unknown
PETSC_CURRENT_REAL
```

Example 4 (unknown):
```unknown
TSAdaptGetSafety()
```

---

## TSAdaptSetScaleSolveFailed#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptSetScaleSolveFailed/

**Contents:**
- TSAdaptSetScaleSolveFailed#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Scale step size by this factor if solve fails

adapt - adaptive controller context

-ts_adapt_scale_solve_failed scale - to set scale step by this factor if solve fails

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt, TSAdaptChoose(), TSAdaptGetScaleSolveFailed(), TSAdaptGetClip()

src/ts/adapt/interface/tsadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptSetScaleSolveFailed(TSAdapt adapt, PetscReal scale)
```

Example 2 (unknown):
```unknown
TSAdaptChoose()
```

Example 3 (unknown):
```unknown
TSAdaptGetScaleSolveFailed()
```

Example 4 (unknown):
```unknown
TSAdaptGetClip()
```

---

## TSAdaptSetStepLimits#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptSetStepLimits/

**Contents:**
- TSAdaptSetStepLimits#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Note#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Set the minimum and maximum step sizes to be considered by the time step controller

adapt - time step adaptivity context, usually gotten with TSGetAdapt()

hmin - minimum time step

hmax - maximum time step

-ts_adapt_dt_min min - to set minimum time step

-ts_adapt_dt_max max - to set maximum time step

Use PETSC_CURRENT to keep the current value for either parameter

Use PETSC_CURRENT_REAL

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt, TSAdaptGetStepLimits(), TSAdaptChoose()

src/ts/adapt/interface/tsadapt.c

src/ts/tutorials/extchem.c src/ts/tutorials/ex44.c src/ts/tutorials/ex40.c src/ts/tutorials/ex41.c src/ts/tutorials/extchemfield.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptSetStepLimits(TSAdapt adapt, PetscReal hmin, PetscReal hmax)
```

Example 2 (unknown):
```unknown
TSGetAdapt()
```

Example 3 (unknown):
```unknown
PETSC_CURRENT
```

Example 4 (unknown):
```unknown
PETSC_CURRENT_REAL
```

---

## TSAdaptSetTimeStepIncreaseDelay#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptSetTimeStepIncreaseDelay/

**Contents:**
- TSAdaptSetTimeStepIncreaseDelay#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#

The number of timesteps to wait after a decrease in the timestep due to failed solver before increasing the time step.

Logicially Collective

adapt - adaptive controller context

cnt - the number of timesteps

-ts_adapt_time_step_increase_delay cnt - number of steps to delay the increase

This is to prevent an adaptor from bouncing back and forth between two nearby timesteps. The default is 0.

The successful use of this option is problem dependent

There is no theory to support this option

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt

src/ts/adapt/interface/tsadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptSetTimeStepIncreaseDelay(TSAdapt adapt, PetscInt cnt)
```

---

## TSAdaptSetType#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptSetType/

**Contents:**
- TSAdaptSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

sets the approach used for the error adapter

Logicially Collective

adapt - the TS adapter, most likely obtained with TSGetAdapt()

type - one of the TSAdaptType

-ts_adapt_type (basic|dsp|none|cfl|glee|history) - to set the adapter type

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSGetAdapt(), TSAdaptDestroy(), TSAdaptType, TSAdaptGetType()

src/ts/adapt/interface/tsadapt.c

src/ts/tutorials/ex51.c src/ts/tutorials/ex41.c src/ts/tutorials/ex40.c src/ts/utils/dmplexlandau/tutorials/ex1.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptSetType(TSAdapt adapt, TSAdaptType type)
```

Example 2 (unknown):
```unknown
TSGetAdapt()
```

Example 3 (unknown):
```unknown
TSAdaptType
```

Example 4 (unknown):
```unknown
TSGetAdapt()
```

---

## TSADAPTTSPSEUDO#

**URL:** https://petsc.org/release/manualpages/TS/TSADAPTTSPSEUDO/

**Contents:**
- TSADAPTTSPSEUDO#
- Note#
- See Also#
- Level#
- Location#

TSPseudo adaptive controller for time stepping

This is only meant to be used with TSPSEUDO time integrator.

TS: Scalable ODE and DAE Solvers, TS, TSAdapt, TSGetAdapt(), TSAdaptType, TSPSEUDO

src/ts/impls/pseudo/posindep.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGetAdapt()
```

Example 2 (unknown):
```unknown
TSAdaptType
```

---

## TSAdaptType#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptType/

**Contents:**
- TSAdaptType#
- Synopsis#
- See Also#
- Level#
- Location#

String with the name of TSAdapt scheme.

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSGetAdapt(), TSAdaptSetType(), TS, TSAdapt

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h> 
typedef const char *TSAdaptType;
#define TSADAPTNONE    "none"
#define TSADAPTBASIC   "basic"
#define TSADAPTDSP     "dsp"
#define TSADAPTCFL     "cfl"
#define TSADAPTGLEE    "glee"
#define TSADAPTHISTORY "history"
```

Example 2 (unknown):
```unknown
TSGetAdapt()
```

Example 3 (unknown):
```unknown
TSAdaptSetType()
```

---

## TSAdaptView#

**URL:** https://petsc.org/release/manualpages/TS/TSAdaptView/

**Contents:**
- TSAdaptView#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Prints the TSAdapt data structure.

adapt - the TSAdapt context obtained from TSGetAdapt()

viewer - visualization context

-ts_view - calls TSView() at end of TSStep()

This is called by TSView() so rarely called directly.

The available visualization contexts include

PETSC_VIEWER_STDOUT_SELF - standard output (default)

PETSC_VIEWER_STDOUT_WORLD - synchronized standard output where only the first processor opens the file. All other processes send their data to the first process to print.

The user can open an alternative visualization context with PetscViewerASCIIOpen() - output to a specified file.

In the debugger you can do call TSAdaptView(adapt,0) to display the TSAdapt. (The same holds for any PETSc object viewer).

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TSAdapt, TSView(), PetscViewer, PetscViewerASCIIOpen()

src/ts/adapt/interface/tsadapt.c

TSAdaptView_DSP() in src/ts/adapt/impls/dsp/adaptdsp.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSAdaptView(TSAdapt adapt, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
TSGetAdapt()
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

## TSAdapt#

**URL:** https://petsc.org/release/manualpages/TS/TSAdapt/

**Contents:**
- TSAdapt#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Abstract object that manages time-step adaptivity

TS: Scalable ODE and DAE Solvers, Error control via variable time-stepping, TS, TSGetAdapt(), TSAdaptCreate(), TSAdaptType

src/ts/tutorials/extchem.c src/ts/tutorials/ex51.c src/ts/tutorials/ex40.c src/ts/tutorials/ex44.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/tutorials/ex53.c src/ts/tutorials/ex41.c src/ts/tutorials/extchemfield.c

_p_TSAdapt in include/petsc/private/tsimpl.h TSAdapt_DSP in src/ts/adapt/impls/dsp/adaptdsp.c TSAdapt_GLEE in src/ts/adapt/impls/glee/adaptglee.c TSAdapt_History in src/ts/adapt/impls/history/adapthist.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (c):
```c
#include <petscts.h> 
typedef struct _p_TSAdapt *TSAdapt;
```

Example 2 (unknown):
```unknown
TSGetAdapt()
```

Example 3 (unknown):
```unknown
TSAdaptCreate()
```

Example 4 (unknown):
```unknown
TSAdaptType
```

---

## TSAdjointComputeDRDPFunction#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSAdjointComputeDRDPFunction/

**Contents:**
- TSAdjointComputeDRDPFunction#
- Synopsis#
- Level#
- Location#

Deprecated, use TSGetQuadratureTS() then TSComputeRHSJacobianP()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGetQuadratureTS()
```

Example 2 (unknown):
```unknown
TSComputeRHSJacobianP()
```

Example 3 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSAdjointComputeDRDPFunction(TS ts, PetscReal t, Vec U, Vec *DRDP)
```

---

## TSAdjointComputeDRDYFunction#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSAdjointComputeDRDYFunction/

**Contents:**
- TSAdjointComputeDRDYFunction#
- Synopsis#
- Level#
- Location#

Deprecated, use TSGetQuadratureTS() then TSComputeRHSJacobian()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGetQuadratureTS()
```

Example 2 (unknown):
```unknown
TSComputeRHSJacobian()
```

Example 3 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSAdjointComputeDRDYFunction(TS ts, PetscReal t, Vec U, Vec *DRDU)
```

---

## TSAdjointComputeRHSJacobian#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSAdjointComputeRHSJacobian/

**Contents:**
- TSAdjointComputeRHSJacobian#
- Synopsis#
- Level#
- Location#

Deprecated, use TSComputeRHSJacobianP()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSComputeRHSJacobianP()
```

Example 2 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSAdjointComputeRHSJacobian(TS ts, PetscReal t, Vec U, Mat Amat)
```

---

## TSAdjointCostIntegral#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSAdjointCostIntegral/

**Contents:**
- TSAdjointCostIntegral#
- Synopsis#
- Input Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Evaluate the cost integral in the adjoint run.

ts - time stepping context

This function cannot be called until TSAdjointStep() has been completed.

TS: Scalable ODE and DAE Solvers, TSAdjointSolve(), TSAdjointStep()

src/ts/interface/sensitivity/tssen.c

TSAdjointCostIntegral_RK() in src/ts/impls/explicit/rk/rk.c TSAdjointCostIntegral_Theta() in src/ts/impls/implicit/theta/theta.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSAdjointCostIntegral(TS ts)
```

Example 2 (unknown):
```unknown
TSAdjointStep()
```

Example 3 (unknown):
```unknown
TSAdjointSolve()
```

Example 4 (unknown):
```unknown
TSAdjointStep()
```

---

## TSAdjointMonitorCancel#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSAdjointMonitorCancel/

**Contents:**
- TSAdjointMonitorCancel#
- Synopsis#
- Input Parameter#
- Notes#
- See Also#
- Level#
- Location#

Clears all the adjoint monitors that have been set on a time-step object.

ts - the TS context obtained from TSCreate()

There is no way to remove a single, specific monitor.

TS: Scalable ODE and DAE Solvers, TS, TSAdjointSolve(), TSAdjointMonitorSet()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSAdjointMonitorCancel(TS ts)
```

Example 2 (unknown):
```unknown
TSAdjointSolve()
```

Example 3 (unknown):
```unknown
TSAdjointMonitorSet()
```

---

## TSAdjointMonitorDefault#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSAdjointMonitorDefault/

**Contents:**
- TSAdjointMonitorDefault#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

the default monitor of adjoint computations

step - iteration number (after the final time step the monitor routine is called with a step of -1, this is at the final time which may have been interpolated to)

numcost - number of cost functions

lambda - sensitivities to initial conditions

mu - sensitivities to parameters

vf - the viewer and format

TS: Scalable ODE and DAE Solvers, TS, TSAdjointSolve(), TSAdjointMonitorSet()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSAdjointMonitorDefault(TS ts, PetscInt step, PetscReal time, Vec v, PetscInt numcost, Vec lambda[], Vec mu[], PetscViewerAndFormat *vf)
```

Example 2 (unknown):
```unknown
TSAdjointSolve()
```

Example 3 (unknown):
```unknown
TSAdjointMonitorSet()
```

---

## TSAdjointMonitorDrawSensi#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSAdjointMonitorDrawSensi/

**Contents:**
- TSAdjointMonitorDrawSensi#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Monitors progress of the adjoint TS solvers by calling VecView() for the sensitivities to initial states at each timestep

step - current time-step

numcost - number of cost functions

lambda - sensitivities to initial conditions

mu - sensitivities to parameters

dummy - either a viewer or NULL

TS: Scalable ODE and DAE Solvers, TSAdjointSolve(), TSAdjointMonitorSet(), TSAdjointMonitorDefault(), VecView()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSAdjointMonitorDrawSensi(TS ts, PetscInt step, PetscReal ptime, Vec u, PetscInt numcost, Vec lambda[], Vec mu[], void *dummy)
```

Example 2 (unknown):
```unknown
TSAdjointSolve()
```

Example 3 (unknown):
```unknown
TSAdjointMonitorSet()
```

Example 4 (unknown):
```unknown
TSAdjointMonitorDefault()
```

---

## TSAdjointMonitorSensi#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSAdjointMonitorSensi/

**Contents:**
- TSAdjointMonitorSensi#
- Synopsis#
- See Also#
- Level#
- Location#

monitors the first lambda sensitivity

TS: Scalable ODE and DAE Solvers, TSAdjointMonitorSet()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
static PetscErrorCode TSAdjointMonitorSensi(TS ts, PetscInt step, PetscReal ptime, Vec v, PetscInt numcost, Vec *lambda, Vec *mu, PetscViewerAndFormat *vf)
```

Example 2 (unknown):
```unknown
TSAdjointMonitorSet()
```

---

## TSAdjointMonitorSetFromOptions#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSAdjointMonitorSetFromOptions/

**Contents:**
- TSAdjointMonitorSetFromOptions#
- Synopsis#
- Input Parameters#
- Calling sequence of monitor#
- Calling sequence of monitorsetup#
- See Also#
- Level#
- Location#

Sets a monitor function and viewer appropriate for the type indicated by the user

ts - TS object you wish to monitor

name - the monitor type one is seeking

help - message indicating what monitoring is done

manual - manual page for the monitor

monitor - the monitor function, its context must be a PetscViewerAndFormat

monitorsetup - a function that is called once ONLY if the user selected this monitor that may set additional features of the TS or PetscViewer objects

step - iteration number (after the final time step the monitor routine is called with a step of -1, this is at the final time which may have been interpolated to)

numcost - number of cost functions

lambda - sensitivities to initial conditions

mu - sensitivities to parameters

vf - the PetscViewer and format the monitor is using

ts - the TS object being monitored

vf - the PetscViewer and format the monitor is using

TS: Scalable ODE and DAE Solvers, PetscOptionsCreateViewer(), PetscOptionsGetReal(), PetscOptionsHasName(), PetscOptionsGetString(), PetscOptionsGetIntArray(), PetscOptionsGetRealArray(), PetscOptionsBool(), PetscOptionsInt(), PetscOptionsString(), PetscOptionsReal(), PetscOptionsName(), PetscOptionsBegin(), PetscOptionsEnd(), PetscOptionsHeadBegin(), PetscOptionsStringArray(), PetscOptionsRealArray(), PetscOptionsScalar(), PetscOptionsBoolGroupBegin(), PetscOptionsBoolGroup(), PetscOptionsBoolGroupEnd(), PetscOptionsFList(), PetscOptionsEList(), PetscViewerAndFormat

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSAdjointMonitorSetFromOptions(TS ts, const char name[], const char help[], const char manual[], PetscErrorCode (*monitor)(TS ts, PetscInt step, PetscReal time, Vec u, PetscInt numcost, Vec *lambda, Vec *mu, PetscViewerAndFormat *vf), PetscErrorCode (*monitorsetup)(TS ts, PetscViewerAndFormat *vf))
```

Example 2 (unknown):
```unknown
PetscViewerAndFormat
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## TSAdjointMonitorSet#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSAdjointMonitorSet/

**Contents:**
- TSAdjointMonitorSet#
- Synopsis#
- Input Parameters#
- Calling sequence of adjointmonitor#
- Note#
- Fortran Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets an ADDITIONAL function that is to be used at every timestep to display the iteration’s progress.

ts - the TS context obtained from TSCreate()

adjointmonitor - monitoring routine

adjointmctx - [optional] context for private data for the monitor routine (use NULL if no context is desired)

adjointmdestroy - [optional] routine that frees monitor context (may be NULL), see PetscCtxDestroyFn for its calling sequence

steps - iteration number (after the final time step the monitor routine is called with a step of -1, this is at the final time which may have been interpolated to)

numcost - number of cost functions

lambda - sensitivities to initial conditions

mu - sensitivities to parameters

adjointmctx - [optional] adjoint monitoring context

This routine adds an additional monitor to the list of monitors that already has been loaded.

Only a single monitor function can be set for each TS object

TS: Scalable ODE and DAE Solvers, TS, TSAdjointSolve(), TSAdjointMonitorCancel(), PetscCtxDestroyFn

src/ts/interface/sensitivity/tssen.c

src/ts/tutorials/ex20td.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSAdjointMonitorSet(TS ts, PetscErrorCode (*adjointmonitor)(TS ts, PetscInt steps, PetscReal time, Vec u, PetscInt numcost, Vec *lambda, Vec *mu, PetscCtx adjointmctx), PetscCtx adjointmctx, PetscCtxDestroyFn *adjointmdestroy)
```

Example 2 (unknown):
```unknown
PetscCtxDestroyFn
```

Example 3 (unknown):
```unknown
adjointmonitor
```

Example 4 (unknown):
```unknown
TSAdjointSolve()
```

---

## TSAdjointMonitor#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSAdjointMonitor/

**Contents:**
- TSAdjointMonitor#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Runs all user-provided adjoint monitor routines set using TSAdjointMonitorSet()

ts - time stepping context obtained from TSCreate()

step - step number that has just completed

ptime - model time of the state

u - state at the current model time

numcost - number of cost functions (dimension of lambda or mu)

lambda - vectors containing the gradients of the cost functions with respect to the ODE/DAE solution variables

mu - vectors containing the gradients of the cost functions with respect to the problem parameters

TSAdjointMonitor() is typically used automatically within the time stepping implementations. Users would almost never call this routine directly.

TSAdjointMonitorSet(), TSAdjointSolve()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSAdjointMonitorSet()
```

Example 2 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSAdjointMonitor(TS ts, PetscInt step, PetscReal ptime, Vec u, PetscInt numcost, Vec lambda[], Vec mu[])
```

Example 3 (unknown):
```unknown
TSAdjointMonitor()
```

Example 4 (unknown):
```unknown
TSAdjointMonitorSet()
```

---

## TSAdjointResetForward#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSAdjointResetForward/

**Contents:**
- TSAdjointResetForward#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#

Reset the tangent linear solver and destroy the tangent linear context

ts - the TS context obtained from TSCreate()

TS: Scalable ODE and DAE Solvers, TSAdjointSetForward()

src/ts/interface/sensitivity/tssen.c

src/ts/tutorials/ex20opt_p.c src/ts/tutorials/ex20opt_ic.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSAdjointResetForward(TS ts)
```

Example 2 (unknown):
```unknown
TSAdjointSetForward()
```

---

## TSAdjointReset#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSAdjointReset/

**Contents:**
- TSAdjointReset#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Resets a TS adjoint context and removes any allocated Vecs and Mats.

ts - the TS context obtained from TSCreate()

TS: Scalable ODE and DAE Solvers, TSCreate(), TSAdjointSetUp(), TSDestroy()

src/ts/interface/sensitivity/tssen.c

src/ts/tutorials/ex20opt_p.c src/ts/tutorials/ex20opt_ic.c

TSAdjointReset_ARKIMEX() in src/ts/impls/arkimex/arkimex.c TSAdjointReset_RK() in src/ts/impls/explicit/rk/rk.c TSAdjointReset_Theta() in src/ts/impls/implicit/theta/theta.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSAdjointReset(TS ts)
```

Example 2 (unknown):
```unknown
TSAdjointSetUp()
```

Example 3 (unknown):
```unknown
TSDestroy()
```

---

## TSAdjointSetForward#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSAdjointSetForward/

**Contents:**
- TSAdjointSetForward#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Trigger the tangent linear solver and initialize the forward sensitivities

ts - the TS context obtained from TSCreate()

didp - the derivative of initial values w.r.t. parameters

When computing sensitivities w.r.t. initial condition, set didp to NULL so that the solver will take it as an identity matrix mathematically. TSAdjoint does not reset the tangent linear solver automatically, TSAdjointResetForward() should be called to reset the tangent linear solver.

TS: Scalable ODE and DAE Solvers, TSAdjointSolve(), TSSetCostHessianProducts(), TSAdjointResetForward()

src/ts/interface/sensitivity/tssen.c

src/ts/tutorials/ex20opt_p.c src/ts/tutorials/ex20opt_ic.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSAdjointSetForward(TS ts, Mat didp)
```

Example 2 (unknown):
```unknown
TSAdjointResetForward()
```

Example 3 (unknown):
```unknown
TSAdjointSolve()
```

Example 4 (unknown):
```unknown
TSSetCostHessianProducts()
```

---

## TSAdjointSetFromOptions#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSAdjointSetFromOptions/

**Contents:**
- TSAdjointSetFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#

Sets various TS adjoint parameters from options database.

PetscOptionsObject - the options context

-ts_adjoint_solve (yes|no) - After solving the ODE/DAE solve the adjoint problem (requires -ts_save_trajectory)

-ts_adjoint_monitor - print information at each adjoint time step

-ts_adjoint_monitor_draw_sensi - monitor the sensitivity of the first cost function wrt initial conditions (lambda[0]) graphically

This is not normally called directly by users

TS: Scalable ODE and DAE Solvers, TSSetSaveTrajectory(), TSTrajectorySetUp()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSAdjointSetFromOptions(TS ts, PetscOptionItems PetscOptionsObject)
```

Example 2 (unknown):
```unknown
-ts_save_trajectory
```

Example 3 (unknown):
```unknown
TSSetSaveTrajectory()
```

Example 4 (unknown):
```unknown
TSTrajectorySetUp()
```

---

## TSAdjointSetRHSJacobian#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSAdjointSetRHSJacobian/

**Contents:**
- TSAdjointSetRHSJacobian#
- Synopsis#
- Level#
- Location#

Deprecated, use TSSetRHSJacobianP()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetRHSJacobianP()
```

Example 2 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSAdjointSetRHSJacobian(TS ts, Mat Amat, PetscErrorCode (*func)(TS, PetscReal, Vec, Mat, void *), PetscCtx ctx)
```

---

## TSAdjointSetSteps#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSAdjointSetSteps/

**Contents:**
- TSAdjointSetSteps#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the number of steps the adjoint solver should take backward in time

ts - the TS context obtained from TSCreate()

steps - number of steps to use

Normally one does not call this and TSAdjointSolve() integrates back to the original timestep. One can call this so as to integrate back to less than the original timestep

TS: Scalable ODE and DAE Solvers, TSAdjointSolve(), TS, TSSetExactFinalTime()

src/ts/interface/sensitivity/tssen.c

src/ts/tutorials/ex20td.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSAdjointSetSteps(TS ts, PetscInt steps)
```

Example 2 (unknown):
```unknown
TSAdjointSolve()
```

Example 3 (unknown):
```unknown
TSAdjointSolve()
```

Example 4 (unknown):
```unknown
TSSetExactFinalTime()
```

---

## TSAdjointSetUp#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSAdjointSetUp/

**Contents:**
- TSAdjointSetUp#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Sets up the internal data structures for the later use of an adjoint solver

ts - the TS context obtained from TSCreate()

TS: Scalable ODE and DAE Solvers, TSCreate(), TSAdjointStep(), TSSetCostGradients()

src/ts/interface/sensitivity/tssen.c

TSAdjointSetUp_ARKIMEX() in src/ts/impls/arkimex/arkimex.c TSAdjointSetUp_RK() in src/ts/impls/explicit/rk/rk.c TSAdjointSetUp_Theta() in src/ts/impls/implicit/theta/theta.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSAdjointSetUp(TS ts)
```

Example 2 (unknown):
```unknown
TSAdjointStep()
```

Example 3 (unknown):
```unknown
TSSetCostGradients()
```

---

## TSAdjointSolve#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSAdjointSolve/

**Contents:**
- TSAdjointSolve#
- Synopsis#
- Input Parameter#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Solves the discrete ajoint problem for an ODE/DAE

ts - the TS context obtained from TSCreate()

-ts_adjoint_view_solution viewerinfo - views the first gradient with respect to the initial values

This must be called after a call to TSSolve() that solves the forward problem

By default this will integrate back to the initial time, one can use TSAdjointSetSteps() to step back to a later time

TS: Scalable ODE and DAE Solvers, TSCreate(), TSSetCostGradients(), TSSetSolution(), TSAdjointStep()

src/ts/interface/sensitivity/tssen.c

src/ts/tutorials/ex20opt_p.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/tutorials/ex20opt_ic.c src/ts/tutorials/ex20adj.c src/ts/tutorials/ex23fwdadj.c src/ts/tutorials/ex20td.c src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSAdjointSolve(TS ts)
```

Example 2 (unknown):
```unknown
TSAdjointSetSteps()
```

Example 3 (unknown):
```unknown
TSSetCostGradients()
```

Example 4 (unknown):
```unknown
TSSetSolution()
```

---

## TSAdjointStep#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSAdjointStep/

**Contents:**
- TSAdjointStep#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Steps one time step backward in the adjoint run

ts - the TS context obtained from TSCreate()

TS: Scalable ODE and DAE Solvers, TSAdjointSetUp(), TSAdjointSolve()

src/ts/interface/sensitivity/tssen.c

TSAdjointStep_ARKIMEX() in src/ts/impls/arkimex/arkimex.c TSAdjointStep_RK() in src/ts/impls/explicit/rk/rk.c TSAdjointStep_Theta() in src/ts/impls/implicit/theta/theta.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSAdjointStep(TS ts)
```

Example 2 (unknown):
```unknown
TSAdjointSetUp()
```

Example 3 (unknown):
```unknown
TSAdjointSolve()
```

---

## TSAlpha2GetParams#

**URL:** https://petsc.org/release/manualpages/TS/TSAlpha2GetParams/

**Contents:**
- TSAlpha2GetParams#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

gets the algorithmic parameters for TSALPHA2

ts - timestepping context

alpha_m - algorithmic parameter

alpha_f - algorithmic parameter

gamma - algorithmic parameter

beta - algorithmic parameter

Use of this function is normally only required to hack TSALPHA2 to use a modified integration scheme. Users should call TSAlpha2SetRadius() to set the high-frequency damping (i.e. spectral radius of the method) in order so select optimal values for these parameters.

TS: Scalable ODE and DAE Solvers, TS, TSALPHA2, TSAlpha2SetRadius(), TSAlpha2SetParams()

src/ts/impls/implicit/alpha/alpha2.c

TSAlpha2GetParams_Alpha() in src/ts/impls/implicit/alpha/alpha2.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSAlpha2GetParams(TS ts, PetscReal *alpha_m, PetscReal *alpha_f, PetscReal *gamma, PetscReal *beta)
```

Example 2 (unknown):
```unknown
TSAlpha2SetRadius()
```

Example 3 (unknown):
```unknown
TSAlpha2SetRadius()
```

Example 4 (unknown):
```unknown
TSAlpha2SetParams()
```

---

## TSAlpha2PredictorFn#

**URL:** https://petsc.org/release/manualpages/TS/TSAlpha2PredictorFn/

**Contents:**
- TSAlpha2PredictorFn#
- Synopsis#
- Calling Sequence#
- Note#
- See Also#
- Level#
- Location#

A callback to set the predictor (i.e., the initial guess for the nonlinear solver) in a second-order generalized-alpha time integrator.

ts - the TS context obtained from TSCreate()

X0 - the previous time step’s state vector

V0 - the previous time step’s first derivative of the state vector

A0 - the previous time step’s second derivative of the state vector

X1 - the vector into which the initial guess for the current time step will be written

ctx - [optional] user-defined context for the predictor evaluation routine (may be NULL)

The deprecated TSAlpha2Predictor still works as a replacement for TSAlpha2PredictorFn *.

TS: Scalable ODE and DAE Solvers, TS, TSAlpha2SetPredictor()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h> 
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode TSAlpha2PredictorFn(TS ts, Vec X0, Vec V0, Vec A0, Vec X1, PetscCtx ctx);
```

Example 2 (unknown):
```unknown
TSAlpha2Predictor
```

Example 3 (unknown):
```unknown
TSAlpha2PredictorFn
```

Example 4 (unknown):
```unknown
TSAlpha2SetPredictor()
```

---

## TSAlpha2SetParams#

**URL:** https://petsc.org/release/manualpages/TS/TSAlpha2SetParams/

**Contents:**
- TSAlpha2SetParams#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

sets the algorithmic parameters for TSALPHA2

ts - timestepping context

alpha_m - algorithmic parameter

alpha_f - algorithmic parameter

gamma - algorithmic parameter

beta - algorithmic parameter

-ts_alpha_alpha_m alpha_m - set alpha_m

-ts_alpha_alpha_f alpha_f - set alpha_f

-ts_alpha_gamma gamma - set gamma

-ts_alpha_beta beta - set beta

Second-order accuracy can be obtained so long as:

Unconditional stability requires: $\( \alpha_m >= \alpha_f >= 1/2. \)$

Use of this function is normally only required to hack TSALPHA2 to use a modified integration scheme. Users should call TSAlpha2SetRadius() to set the desired spectral radius of the methods (i.e. high-frequency damping) in order so select optimal values for these parameters.

TS: Scalable ODE and DAE Solvers, TS, TSALPHA2, TSAlpha2SetRadius(), TSAlpha2GetParams()

src/ts/impls/implicit/alpha/alpha2.c

TSAlpha2SetParams_Alpha() in src/ts/impls/implicit/alpha/alpha2.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSAlpha2SetParams(TS ts, PetscReal alpha_m, PetscReal alpha_f, PetscReal gamma, PetscReal beta)
```

Example 2 (unknown):
```unknown
TSAlpha2SetRadius()
```

Example 3 (unknown):
```unknown
TSAlpha2SetRadius()
```

Example 4 (unknown):
```unknown
TSAlpha2GetParams()
```

---

## TSAlpha2SetPredictor#

**URL:** https://petsc.org/release/manualpages/TS/TSAlpha2SetPredictor/

**Contents:**
- TSAlpha2SetPredictor#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

sets the callback for computing a predictor (i.e., initial guess for the nonlinear solver).

ts - timestepping context

predictor - callback to set the predictor in each step

ctx - the application context, which may be set to NULL if not used

If this function is never called, a same-state-vector predictor will be used, i.e., the initial guess will be the converged solution from the previous time step, without regard for the previous velocity or acceleration.

TS: Scalable ODE and DAE Solvers, TS, TSALPHA2, TSAlpha2PredictorFn

src/ts/impls/implicit/alpha/alpha2.c

src/ts/tutorials/ex43.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSAlpha2SetPredictor(TS ts, TSAlpha2PredictorFn *predictor, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSAlpha2PredictorFn
```

---

## TSAlpha2SetRadius#

**URL:** https://petsc.org/release/manualpages/TS/TSAlpha2SetRadius/

**Contents:**
- TSAlpha2SetRadius#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

sets the desired spectral radius of the method for TSALPHA2 (i.e. high-frequency numerical damping)

ts - timestepping context

radius - the desired spectral radius

-ts_alpha_radius radius - set the desired spectral radius

The algorithmic parameters \(\alpha_m\) and \(\alpha_f\) of the generalized-\(\alpha\) method can be computed in terms of a specified spectral radius \(\rho\) in [0, 1] for infinite time step in order to control high-frequency numerical damping:

TS: Scalable ODE and DAE Solvers, TS, TSALPHA2, TSAlpha2SetParams(), TSAlpha2GetParams()

src/ts/impls/implicit/alpha/alpha2.c

TSAlpha2SetRadius_Alpha() in src/ts/impls/implicit/alpha/alpha2.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSAlpha2SetRadius(TS ts, PetscReal radius)
```

Example 2 (unknown):
```unknown
TSAlpha2SetParams()
```

Example 3 (unknown):
```unknown
TSAlpha2GetParams()
```

---

## TSALPHA2#

**URL:** https://petsc.org/release/manualpages/TS/TSALPHA2/

**Contents:**
- TSALPHA2#
- References#
- See Also#
- Level#
- Location#
- Examples#

ODE/DAE solver using the implicit Generalized-Alpha method for second-order systems [CH93]

J. Chung and G. M. Hulbert. A time integration algorithm for structural dynamics with improved numerical dissipation: the generalized-alpha method. Journal of Applied Mechanics, 60(2):371–375, 06 1993. URL: https://doi.org/10.1115/1.2900803, arXiv:https://asmedigitalcollection.asme.org/appliedmechanics/article-pdf/60/2/371/5463014/371\_1.pdf, doi:10.1115/1.2900803.

TS: Scalable ODE and DAE Solvers, TS, TSCreate(), TSSetType(), TSAlpha2SetRadius(), TSAlpha2SetParams()

src/ts/impls/implicit/alpha/alpha2.c

src/ts/tutorials/ex44.c src/ts/tutorials/ex43.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetType()
```

Example 2 (unknown):
```unknown
TSAlpha2SetRadius()
```

Example 3 (unknown):
```unknown
TSAlpha2SetParams()
```

---

## TSAlphaGetParams#

**URL:** https://petsc.org/release/manualpages/TS/TSAlphaGetParams/

**Contents:**
- TSAlphaGetParams#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

gets the algorithmic parameters for TSALPHA

ts - timestepping context

alpha_m - algorithmic parameter

alpha_f - algorithmic parameter

gamma - algorithmic parameter

Use of this function is normally only required to hack TSALPHA to use a modified integration scheme. Users should call TSAlphaSetRadius() to set the high-frequency damping (i.e. spectral radius of the method) in order so select optimal values for these parameters.

TS: Scalable ODE and DAE Solvers, TS, TSALPHA, TSAlphaSetRadius(), TSAlphaSetParams()

src/ts/impls/implicit/alpha/alpha1.c

TSAlphaGetParams_Alpha() in src/ts/impls/implicit/alpha/alpha1.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSAlphaGetParams(TS ts, PetscReal *alpha_m, PetscReal *alpha_f, PetscReal *gamma)
```

Example 2 (unknown):
```unknown
TSAlphaSetRadius()
```

Example 3 (unknown):
```unknown
TSAlphaSetRadius()
```

Example 4 (unknown):
```unknown
TSAlphaSetParams()
```

---

## TSAlphaSetParams#

**URL:** https://petsc.org/release/manualpages/TS/TSAlphaSetParams/

**Contents:**
- TSAlphaSetParams#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

sets the algorithmic parameters for TSALPHA

ts - timestepping context

alpha_m - algorithmic parameter

alpha_f - algorithmic parameter

gamma - algorithmic parameter

-ts_alpha_alpha_m alpha_m - set alpha_m

-ts_alpha_alpha_f alpha_f - set alpha_f

-ts_alpha_gamma gamma - set gamma

Second-order accuracy can be obtained so long as: \(\gamma = 0.5 + \alpha_m - \alpha_f\)

Unconditional stability requires: \(\alpha_m >= \alpha_f >= 0.5\)

Backward Euler method is recovered with: \(\alpha_m = \alpha_f = \gamma = 1\)

Use of this function is normally only required to hack TSALPHA to use a modified integration scheme. Users should call TSAlphaSetRadius() to set the desired spectral radius of the methods (i.e. high-frequency damping) in order so select optimal values for these parameters.

TS: Scalable ODE and DAE Solvers, TS, TSALPHA, TSAlphaSetRadius(), TSAlphaGetParams()

src/ts/impls/implicit/alpha/alpha1.c

TSAlphaSetParams_Alpha() in src/ts/impls/implicit/alpha/alpha1.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSAlphaSetParams(TS ts, PetscReal alpha_m, PetscReal alpha_f, PetscReal gamma)
```

Example 2 (unknown):
```unknown
TSAlphaSetRadius()
```

Example 3 (unknown):
```unknown
TSAlphaSetRadius()
```

Example 4 (unknown):
```unknown
TSAlphaGetParams()
```

---

## TSAlphaSetRadius#

**URL:** https://petsc.org/release/manualpages/TS/TSAlphaSetRadius/

**Contents:**
- TSAlphaSetRadius#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

sets the desired spectral radius of the method for TSALPHA (i.e. high-frequency numerical damping)

ts - timestepping context

radius - the desired spectral radius

-ts_alpha_radius radius - set alpha radius

The algorithmic parameters \(\alpha_m\) and \(\alpha_f\) of the generalized-\(\alpha\) method can be computed in terms of a specified spectral radius \(\rho\) in [0, 1] for infinite time step in order to control high-frequency numerical damping:

TS: Scalable ODE and DAE Solvers, TS, TSALPHA, TSAlphaSetParams(), TSAlphaGetParams()

src/ts/impls/implicit/alpha/alpha1.c

TSAlphaSetRadius_Alpha() in src/ts/impls/implicit/alpha/alpha1.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSAlphaSetRadius(TS ts, PetscReal radius)
```

Example 2 (unknown):
```unknown
TSAlphaSetParams()
```

Example 3 (unknown):
```unknown
TSAlphaGetParams()
```

---

## TSALPHA#

**URL:** https://petsc.org/release/manualpages/TS/TSALPHA/

**Contents:**
- TSALPHA#
- References#
- See Also#
- Level#
- Location#
- Examples#

ODE/DAE solver using the implicit Generalized-Alpha method [JWH00] [CH93] for first-order systems

J. Chung and G. M. Hulbert. A time integration algorithm for structural dynamics with improved numerical dissipation: the generalized-alpha method. Journal of Applied Mechanics, 60(2):371–375, 06 1993. URL: https://doi.org/10.1115/1.2900803, arXiv:https://asmedigitalcollection.asme.org/appliedmechanics/article-pdf/60/2/371/5463014/371\_1.pdf, doi:10.1115/1.2900803.

K.E. Jansen, C.H. Whiting, and G.M. Hulbert. A generalized-alpha method for integrating the filtered Navier–Stokes equations with a stabilized finite element method. Computer Methods in Applied Mechanics and Engineering, 190(3):305–319, 2000.

TS: Scalable ODE and DAE Solvers, TS, TSCreate(), TSSetType(), TSAlphaSetRadius(), TSAlphaSetParams()

src/ts/impls/implicit/alpha/alpha1.c

src/ts/tutorials/ex31.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetType()
```

Example 2 (unknown):
```unknown
TSAlphaSetRadius()
```

Example 3 (unknown):
```unknown
TSAlphaSetParams()
```

---

## TSAppendOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/TS/TSAppendOptionsPrefix/

**Contents:**
- TSAppendOptionsPrefix#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Appends to the prefix used for searching for all TS options in the database.

prefix - The prefix to prepend to all option names

A hyphen (-) must NOT be given at the beginning of the prefix name. The first character of all runtime options is AUTOMATICALLY the hyphen.

TS: Scalable ODE and DAE Solvers, TS, TSGetOptionsPrefix(), TSSetOptionsPrefix(), TSSetFromOptions()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSAppendOptionsPrefix(TS ts, const char prefix[])
```

Example 2 (unknown):
```unknown
TSGetOptionsPrefix()
```

Example 3 (unknown):
```unknown
TSSetOptionsPrefix()
```

Example 4 (unknown):
```unknown
TSSetFromOptions()
```

---

## TSARKIMEX1BEE#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEX1BEE/

**Contents:**
- TSARKIMEX1BEE#
- Options Database Key#
- See Also#
- Level#
- Location#

First order backward Euler represented as an ARK IMEX scheme with extrapolation as error estimator. This is a 3-stage method. This method is aimed at starting the integration of implicit DAEs when explicit first-stage ARK methods are used.

-ts_arkimex_type 1bee - set arkimex type to 1bee

TS: Scalable ODE and DAE Solvers, TSARKIMEX, TSARKIMEXType, TSARKIMEXSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSARKIMEXType
```

Example 2 (unknown):
```unknown
TSARKIMEXSetType()
```

---

## TSARKIMEX2C#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEX2C/

**Contents:**
- TSARKIMEX2C#
- Options Database Key#
- See Also#
- Level#
- Location#

Second order ARK IMEX scheme with L-stable implicit part. This method has one explicit stage and two implicit stages. The implicit part is the same as in TSARKIMEX2D and TSARKIMEX2E, but the explicit part has a larger stability region on the negative real axis. This method was provided by Emil Constantinescu.

-ts_arkimex_type 2c - set arkimex type to 2c

TS: Scalable ODE and DAE Solvers, TSARKIMEX, TSARKIMEXType, TSARKIMEXSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSARKIMEXType
```

Example 2 (unknown):
```unknown
TSARKIMEXSetType()
```

---

## TSARKIMEX2D#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEX2D/

**Contents:**
- TSARKIMEX2D#
- Options Database Key#
- See Also#
- Level#
- Location#

Second order ARK IMEX scheme with L-stable implicit part. This method has one explicit stage and two implicit stages. The stability function is independent of the explicit part in the infinity limit of the implicit component. This method was provided by Emil Constantinescu.

-ts_arkimex_type 2d - set arkimex type to 2d

TS: Scalable ODE and DAE Solvers, TSARKIMEX, TSARKIMEXType, TSARKIMEXSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSARKIMEXType
```

Example 2 (unknown):
```unknown
TSARKIMEXSetType()
```

---

## TSARKIMEX2E#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEX2E/

**Contents:**
- TSARKIMEX2E#
- Options Database Key#
- See Also#
- Level#
- Location#

Second order ARK IMEX scheme with L-stable implicit part. This method has one explicit stage and two implicit stages. It is an optimal method developed by Emil Constantinescu.

-ts_arkimex_type 2e - set arkimex type to 2e

TS: Scalable ODE and DAE Solvers, TSARKIMEX, TSARKIMEXType, TSARKIMEXSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSARKIMEXType
```

Example 2 (unknown):
```unknown
TSARKIMEXSetType()
```

---

## TSARKIMEX3#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEX3/

**Contents:**
- TSARKIMEX3#
- Options Database Key#
- References#
- See Also#
- Level#
- Location#

Third order ARK IMEX scheme with L-stable implicit part, [KC03] This method has one explicit stage and three implicit stages.

-ts_arkimex_type 3 - set arkimex type to 3

C.A. Kennedy and M.H. Carpenter. Additive Runge-Kutta schemes for convection-diffusion-reaction equations. Appl. Numer. Math., 44(1-2):139–181, 2003. doi:10.1016/S0168-9274(02)00138-1.

TS: Scalable ODE and DAE Solvers, TSARKIMEX, TSARKIMEXType, TSARKIMEXSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSARKIMEXType
```

Example 2 (unknown):
```unknown
TSARKIMEXSetType()
```

---

## TSARKIMEX4#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEX4/

**Contents:**
- TSARKIMEX4#
- Options Database Key#
- References#
- See Also#
- Level#
- Location#
- Examples#

Fourth order ARK IMEX scheme with L-stable implicit part, [KC03]. This method has one explicit stage and four implicit stages.

-ts_arkimex_type 4 - set arkimex type to4

C.A. Kennedy and M.H. Carpenter. Additive Runge-Kutta schemes for convection-diffusion-reaction equations. Appl. Numer. Math., 44(1-2):139–181, 2003. doi:10.1016/S0168-9274(02)00138-1.

TS: Scalable ODE and DAE Solvers, TSARKIMEX, TSARKIMEXType, TSARKIMEXSetType()

src/ts/impls/arkimex/arkimex.c

src/ts/tutorials/extchem.c src/ts/tutorials/extchemfield.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSARKIMEXType
```

Example 2 (unknown):
```unknown
TSARKIMEXSetType()
```

---

## TSARKIMEX5#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEX5/

**Contents:**
- TSARKIMEX5#
- Options Database Key#
- References#
- See Also#
- Level#
- Location#

Fifth order ARK IMEX scheme with L-stable implicit part, [KC03]. This method has one explicit stage and five implicit stages.

-ts_arkimex_type 5 - set arkimex type to 5

C.A. Kennedy and M.H. Carpenter. Additive Runge-Kutta schemes for convection-diffusion-reaction equations. Appl. Numer. Math., 44(1-2):139–181, 2003. doi:10.1016/S0168-9274(02)00138-1.

TS: Scalable ODE and DAE Solvers, TSARKIMEX, TSARKIMEXType, TSARKIMEXSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSARKIMEXType
```

Example 2 (unknown):
```unknown
TSARKIMEXSetType()
```

---

## TSARKIMEXA2#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEXA2/

**Contents:**
- TSARKIMEXA2#
- Options Database Key#
- See Also#
- Level#
- Location#

Second order ARK IMEX scheme with A-stable implicit part. This method has an explicit stage and one implicit stage, and has an A-stable implicit scheme. This method was provided by Emil Constantinescu.

-ts_arkimex_type a2 - set arkimex type to a2

TS: Scalable ODE and DAE Solvers, TSARKIMEX, TSARKIMEXType, TSARKIMEXSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSARKIMEXType
```

Example 2 (unknown):
```unknown
TSARKIMEXSetType()
```

---

## TSARKIMEXARS122#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEXARS122/

**Contents:**
- TSARKIMEXARS122#
- Options Database Key#
- References#
- See Also#
- Level#
- Location#

Second order ARK IMEX scheme, [ARS97] This method has one explicit stage and one implicit stage.

-ts_arkimex_type ars122 - set arkimex type to ars122

U.M. Ascher, S.J. Ruuth, and R.J. Spiteri. Implicit-explicit Runge-Kutta methods for time-dependent partial differential equations. Applied Numerical Mathematics, 25:151–167, 1997.

TS: Scalable ODE and DAE Solvers, TSARKIMEX, TSARKIMEXType, TSARKIMEXSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSARKIMEXType
```

Example 2 (unknown):
```unknown
TSARKIMEXSetType()
```

---

## TSARKIMEXARS443#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEXARS443/

**Contents:**
- TSARKIMEXARS443#
- Options Database Key#
- Notes#
- References#
- See Also#
- Level#
- Location#

Third order ARK IMEX scheme, [ARS97] This method has one explicit stage and four implicit stages.

-ts_arkimex_type ars443 - set arkimex type to ars443

This method is referred to as ARS(4,4,3) in https://arxiv.org/abs/1110.4375

U.M. Ascher, S.J. Ruuth, and R.J. Spiteri. Implicit-explicit Runge-Kutta methods for time-dependent partial differential equations. Applied Numerical Mathematics, 25:151–167, 1997.

TS: Scalable ODE and DAE Solvers, TSARKIMEX, TSARKIMEXType, TSARKIMEXSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSARKIMEXType
```

Example 2 (unknown):
```unknown
TSARKIMEXSetType()
```

---

## TSARKIMEXBPR3#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEXBPR3/

**Contents:**
- TSARKIMEXBPR3#
- Options Database Key#
- See Also#
- Level#
- Location#

Third order ARK IMEX scheme. Referred to as ARK3 in https://arxiv.org/abs/1110.4375 This method has one explicit stage and four implicit stages.

-ts_arkimex_type bpr3 - set arkimex type to bpr3

TS: Scalable ODE and DAE Solvers, TSARKIMEX, TSARKIMEXType, TSARKIMEXSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSARKIMEXType
```

Example 2 (unknown):
```unknown
TSARKIMEXSetType()
```

---

## TSARKIMEXFinalizePackage#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEXFinalizePackage/

**Contents:**
- TSARKIMEXFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys everything in the TSARKIMEX package. It is called from PetscFinalize().

TS: Scalable ODE and DAE Solvers, PetscFinalize(), TSARKIMEXInitializePackage()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSARKIMEXFinalizePackage(void)
```

Example 3 (unknown):
```unknown
PetscFinalize()
```

Example 4 (unknown):
```unknown
TSARKIMEXInitializePackage()
```

---

## TSARKIMEXGetFastSlowSplit#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEXGetFastSlowSplit/

**Contents:**
- TSARKIMEXGetFastSlowSplit#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Gets whether to use TSARKIMEX for a fast-slow system

ts - timestepping context

fastslow - PETSC_TRUE if TSARKIMEX will be used for solving a fast-slow system, PETSC_FALSE otherwise

TS: Scalable ODE and DAE Solvers, TSARKIMEX, TSARKIMEXSetFastSlowSplit()

src/ts/impls/arkimex/arkimex.c

TSARKIMEXGetFastSlowSplit_ARKIMEX() in src/ts/impls/arkimex/fsarkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSARKIMEXGetFastSlowSplit(TS ts, PetscBool *fastslow)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
TSARKIMEXSetFastSlowSplit()
```

---

## TSARKIMEXGetFullyImplicit#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEXGetFullyImplicit/

**Contents:**
- TSARKIMEXGetFullyImplicit#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Inquires if both parts of the equation are solved implicitly

ts - timestepping context

flg - PETSC_TRUE for fully implicit

TS: Scalable ODE and DAE Solvers, TSARKIMEXGetType(), TSARKIMEXSetFullyImplicit()

src/ts/impls/arkimex/arkimex.c

TSARKIMEXGetFullyImplicit_ARKIMEX() in src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSARKIMEXGetFullyImplicit(TS ts, PetscBool *flg)
```

Example 2 (unknown):
```unknown
TSARKIMEXGetType()
```

Example 3 (unknown):
```unknown
TSARKIMEXSetFullyImplicit()
```

---

## TSARKIMEXGetType#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEXGetType/

**Contents:**
- TSARKIMEXGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get the type of TSARKIMEX scheme

ts - timestepping context

arktype - type of TSARKIMEX scheme

TS: Scalable ODE and DAE Solvers, TSARKIMEX

src/ts/impls/arkimex/arkimex.c

TSARKIMEXGetType_ARKIMEX() in src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSARKIMEXGetType(TS ts, TSARKIMEXType *arktype)
```

---

## TSARKIMEXInitializePackage#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEXInitializePackage/

**Contents:**
- TSARKIMEXInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function initializes everything in the TSARKIMEX package. It is called from TSInitializePackage().

TS: Scalable ODE and DAE Solvers, PetscInitialize(), TSARKIMEXFinalizePackage()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSInitializePackage()
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSARKIMEXInitializePackage(void)
```

Example 3 (unknown):
```unknown
PetscInitialize()
```

Example 4 (unknown):
```unknown
TSARKIMEXFinalizePackage()
```

---

## TSARKIMEXL2#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEXL2/

**Contents:**
- TSARKIMEXL2#
- Options Database Key#
- References#
- See Also#
- Level#
- Location#

Second order ARK IMEX scheme with L-stable implicit part, [PR05] This method has two implicit stages, and L-stable implicit scheme.

-ts_arkimex_type l2 - set arkimex type to l2

L. Pareschi and G. Russo. Implicit-explicit Runge-Kutta schemes and applications to hyperbolic systems with relaxation. Journal of Scientific Computing, 25(1):129–155, 2005.

TS: Scalable ODE and DAE Solvers, TSARKIMEX, TSARKIMEXType, TSARKIMEXSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSARKIMEXType
```

Example 2 (unknown):
```unknown
TSARKIMEXSetType()
```

---

## TSARKIMEXPRSSP2#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEXPRSSP2/

**Contents:**
- TSARKIMEXPRSSP2#
- Options Database Key#
- References#
- See Also#
- Level#
- Location#
- Examples#

Second order SSP ARK IMEX scheme, [PR05] This method has three implicit stages.

This method is referred to as SSP2-(3,3,2) in https://arxiv.org/abs/1110.4375

-ts_arkimex_type prssp2 - set arkimex type to prssp2

L. Pareschi and G. Russo. Implicit-explicit Runge-Kutta schemes and applications to hyperbolic systems with relaxation. Journal of Scientific Computing, 25(1):129–155, 2005.

TS: Scalable ODE and DAE Solvers, TSARKIMEX, TSARKIMEXType, TSARKIMEXSetType()

src/ts/impls/arkimex/arkimex.c

src/ts/tutorials/ex36.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSARKIMEXType
```

Example 2 (unknown):
```unknown
TSARKIMEXSetType()
```

---

## TSARKIMEXRegisterAll#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEXRegisterAll/

**Contents:**
- TSARKIMEXRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the additive Runge-Kutta implicit-explicit methods in TSARKIMEX

Not Collective, but should be called by all processes which will need the schemes to be registered

TS: Scalable ODE and DAE Solvers, TS, TSARKIMEX, TSARKIMEXRegisterDestroy()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSARKIMEXRegisterAll(void)
```

Example 2 (unknown):
```unknown
TSARKIMEXRegisterDestroy()
```

---

## TSARKIMEXRegisterDestroy#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEXRegisterDestroy/

**Contents:**
- TSARKIMEXRegisterDestroy#
- Synopsis#
- See Also#
- Level#
- Location#

Frees the list of schemes that were registered by TSARKIMEXRegister().

TS: Scalable ODE and DAE Solvers, TSARKIMEX, TSARKIMEXRegister(), TSARKIMEXRegisterAll()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSARKIMEXRegister()
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSARKIMEXRegisterDestroy(void)
```

Example 3 (unknown):
```unknown
TSARKIMEXRegister()
```

Example 4 (unknown):
```unknown
TSARKIMEXRegisterAll()
```

---

## TSARKIMEXRegister#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEXRegister/

**Contents:**
- TSARKIMEXRegister#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

register a TSARKIMEX scheme by providing the entries in the Butcher tableau and optionally embedded approximations and interpolation

name - identifier for method

order - approximation order of method

s - number of stages, this is the dimension of the matrices below

At - Butcher table of stage coefficients for stiff part (dimension s*s, row-major)

bt - Butcher table for completing the stiff part of the step (dimension s; NULL to use the last row of At)

ct - Abscissa of each stiff stage (dimension s, NULL to use row sums of At)

A - Non-stiff stage coefficients (dimension s*s, row-major)

b - Non-stiff step completion table (dimension s; NULL to use last row of At)

c - Non-stiff abscissa (dimension s; NULL to use row sums of A)

bembedt - Stiff part of completion table for embedded method (dimension s; NULL if not available)

bembed - Non-stiff part of completion table for embedded method (dimension s; NULL to use bembedt if provided)

pinterp - Order of the interpolation scheme, equal to the number of columns of binterpt and binterp

binterpt - Coefficients of the interpolation formula for the stiff part (dimension s*pinterp)

binterp - Coefficients of the interpolation formula for the non-stiff part (dimension s*pinterp; NULL to reuse binterpt)

Several TSARKIMEX methods are provided, this function is only needed to create new methods.

TS: Scalable ODE and DAE Solvers, TSARKIMEX, TSType, TS

src/ts/impls/arkimex/arkimex.c

src/ts/tutorials/ex16.c src/ts/tutorials/ex19.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSARKIMEXRegister(TSARKIMEXType name, PetscInt order, PetscInt s, const PetscReal At[], const PetscReal bt[], const PetscReal ct[], const PetscReal A[], const PetscReal b[], const PetscReal c[], const PetscReal bembedt[], const PetscReal bembed[], PetscInt pinterp, const PetscReal binterpt[], const PetscReal binterp[])
```

---

## TSARKIMEXSetFastSlowSplit#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEXSetFastSlowSplit/

**Contents:**
- TSARKIMEXSetFastSlowSplit#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

Use TSARKIMEX for solving a fast-slow system

ts - timestepping context

fastslow - PETSC_TRUE enables the TSARKIMEX solver for a fast-slow system where the RHS is split component-wise.

-ts_arkimex_fastslowsplit (true|false) - enables the TSARKIMEX solver for a fast-slow system where the RHS is split component-wise

TS: Scalable ODE and DAE Solvers, TSARKIMEX, TSARKIMEXGetFastSlowSplit(), TSRHSSplitSetIS()

src/ts/impls/arkimex/arkimex.c

TSARKIMEXSetFastSlowSplit_ARKIMEX() in src/ts/impls/arkimex/fsarkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSARKIMEXSetFastSlowSplit(TS ts, PetscBool fastslow)
```

Example 2 (unknown):
```unknown
TSARKIMEXGetFastSlowSplit()
```

Example 3 (unknown):
```unknown
TSRHSSplitSetIS()
```

---

## TSARKIMEXSetFullyImplicit#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEXSetFullyImplicit/

**Contents:**
- TSARKIMEXSetFullyImplicit#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Solve both parts of the equation implicitly, including the part that is normally solved explicitly

ts - timestepping context

flg - PETSC_TRUE for fully implicit

-ts_arkimex_fully_implicit (true|false) - Solve both parts of the equation implicitly

TS: Scalable ODE and DAE Solvers, TSARKIMEX, TSARKIMEXGetType(), TSARKIMEXGetFullyImplicit()

src/ts/impls/arkimex/arkimex.c

src/ts/tutorials/extchem.c src/ts/tutorials/extchemfield.c

TSARKIMEXSetFullyImplicit_ARKIMEX() in src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSARKIMEXSetFullyImplicit(TS ts, PetscBool flg)
```

Example 2 (unknown):
```unknown
TSARKIMEXGetType()
```

Example 3 (unknown):
```unknown
TSARKIMEXGetFullyImplicit()
```

---

## TSARKIMEXSetType#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEXSetType/

**Contents:**
- TSARKIMEXSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Set the type of TSARKIMEX scheme

ts - timestepping context

arktype - type of TSARKIMEX scheme

-ts_arkimex_type (1bee|a2|l2|ars122|2c|2d|2e|prssp2|3|bpr3|ars443|4|5) - set TSARKIMEX scheme type, see TSARKIMEXType

TS: Scalable ODE and DAE Solvers, TSARKIMEXGetType(), TSARKIMEX, TSARKIMEXType, TSARKIMEX1BEE, TSARKIMEXA2, TSARKIMEXL2, TSARKIMEXARS122, TSARKIMEX2C, TSARKIMEX2D, TSARKIMEX2E, TSARKIMEXPRSSP2, TSARKIMEX3, TSARKIMEXBPR3, TSARKIMEXARS443, TSARKIMEX4, TSARKIMEX5

src/ts/impls/arkimex/arkimex.c

src/ts/tutorials/ex36.c src/ts/tutorials/extchem.c src/ts/tutorials/extchemfield.c

TSARKIMEXSetType_ARKIMEX() in src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSARKIMEXSetType(TS ts, TSARKIMEXType arktype)
```

Example 2 (unknown):
```unknown
TSARKIMEXType
```

Example 3 (unknown):
```unknown
TSARKIMEXGetType()
```

Example 4 (unknown):
```unknown
TSARKIMEXType
```

---

## TSARKIMEXType#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEXType/

**Contents:**
- TSARKIMEXType#
- Synopsis#
- Options Database Key#
- See Also#
- Level#
- Location#

String with the name of an Additive Runge-Kutta IMEX TSARKIMEX type

-ts_arkimex_type (1bee|a2|l2|ars122|2c|2d|2e|prssp2|3|bpr3|ars443|4|5) - set TSARKIMEX scheme type, see TSARKIMEXType

TS: Scalable ODE and DAE Solvers, TSARKIMEXSetType(), TS, TSARKIMEX, TSARKIMEXRegister()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h> 
typedef const char *TSARKIMEXType;
#define TSARKIMEX1BEE   "1bee"
#define TSARKIMEXA2     "a2"
#define TSARKIMEXL2     "l2"
#define TSARKIMEXARS122 "ars122"
#define TSARKIMEX2C     "2c"
#define TSARKIMEX2D     "2d"
#define TSARKIMEX2E     "2e"
#define TSARKIMEXPRSSP2 "prssp2"
#define TSARKIMEX3      "3"
#define TSARKIMEXBPR3   "bpr3"
#define TSARKIMEXARS443 "ars443"
#define TSARKIMEX4      "4"
#define TSARKIMEX5      "5"
```

Example 2 (unknown):
```unknown
TSARKIMEXType
```

Example 3 (unknown):
```unknown
TSARKIMEXSetType()
```

Example 4 (unknown):
```unknown
TSARKIMEXRegister()
```

---

## TSARKIMEX#

**URL:** https://petsc.org/release/manualpages/TS/TSARKIMEX/

**Contents:**
- TSARKIMEX#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

ODE and DAE solver using additive Runge-Kutta IMEX schemes These methods are intended for problems with well-separated time scales, especially when a slow scale is strongly nonlinear such that it is expensive to solve with a fully implicit method. The user should provide the stiff part of the equation using TSSetIFunction() and the non-stiff part with TSSetRHSFunction().

-ts_arkimex_type (1bee|a2|l2|ars122|2c|2d|2e|prssp2|3|bpr3|ars443|4|5) - Set TSARKIMEX scheme type

-ts_dirk_type type - Set TSDIRK scheme type

-ts_arkimex_fully_implicit (true|false) - Solve both parts of the equation implicitly

-ts_arkimex_fastslowsplit (true|false) - Enables the TSARKIMEX solver for a fast-slow system where the RHS is split component-wise, see TSRHSSplitSetIS()

-ts_arkimex_initial_guess_extrapolate - Extrapolate the initial guess for the stage solution from stage values of the previous time step

The default is TSARKIMEX3, it can be changed with TSARKIMEXSetType() or -ts_arkimex_type

If the equation is implicit or a DAE, then TSSetEquationType() needs to be set accordingly. Refer to the manual for further information.

Methods with an explicit stage can only be used with ODE in which the stiff part \( G(t,X,\dot{X}) \) has the form \( \dot{X} + \hat{G}(t,X)\).

Consider trying TSROSW if the stiff part is linear or weakly nonlinear.

TS: Scalable ODE and DAE Solvers, TSCreate(), TS, TSSetType(), TSARKIMEXSetType(), TSARKIMEXGetType(), TSARKIMEXSetFullyImplicit(), TSARKIMEXGetFullyImplicit(), TSARKIMEX1BEE, TSARKIMEX2C, TSARKIMEX2D, TSARKIMEX2E, TSARKIMEX3, TSARKIMEXL2, TSARKIMEXA2, TSARKIMEXARS122, TSARKIMEX4, TSARKIMEX5, TSARKIMEXPRSSP2, TSARKIMEXARS443, TSARKIMEXBPR3, TSARKIMEXType, TSARKIMEXRegister(), TSType

src/ts/impls/arkimex/arkimex.c

src/ts/tutorials/ex36.c src/ts/tutorials/ex29.c src/ts/tutorials/extchem.c src/ts/tutorials/ex35.cxx src/ts/tutorials/ex20adj.c src/ts/tutorials/ex22f_mf.F90 src/ts/tutorials/ex22.c src/ts/tutorials/ex31.c src/ts/tutorials/ex22f.F90 src/ts/tutorials/extchemfield.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetIFunction()
```

Example 2 (unknown):
```unknown
TSSetRHSFunction()
```

Example 3 (unknown):
```unknown
TSRHSSplitSetIS()
```

Example 4 (unknown):
```unknown
TSARKIMEXSetType()
```

---

## TSBasicSymplecticFinalizePackage#

**URL:** https://petsc.org/release/manualpages/TS/TSBasicSymplecticFinalizePackage/

**Contents:**
- TSBasicSymplecticFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys everything in the TSBASICSYMPLECTIC package. It is called from PetscFinalize().

TS: Scalable ODE and DAE Solvers, PetscFinalize(), TSBASICSYMPLECTIC

src/ts/impls/symplectic/basicsymplectic/basicsymplectic.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSBASICSYMPLECTIC
```

Example 2 (unknown):
```unknown
PetscFinalize()
```

Example 3 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSBasicSymplecticFinalizePackage(void)
```

Example 4 (unknown):
```unknown
PetscFinalize()
```

---

## TSBasicSymplecticGetType#

**URL:** https://petsc.org/release/manualpages/TS/TSBasicSymplecticGetType/

**Contents:**
- TSBasicSymplecticGetType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Get the type of the basic symplectic method

ts - timestepping context

bsymptype - type of the basic symplectic scheme

TS: Scalable ODE and DAE Solvers, TSBASICSYMPLECTIC, TSBasicSymplecticType, TSBasicSymplecticSetType()

src/ts/impls/symplectic/basicsymplectic/basicsymplectic.c

TSBasicSymplecticGetType_BasicSymplectic() in src/ts/impls/symplectic/basicsymplectic/basicsymplectic.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSBasicSymplecticGetType(TS ts, TSBasicSymplecticType *bsymptype)
```

Example 2 (unknown):
```unknown
TSBASICSYMPLECTIC
```

Example 3 (unknown):
```unknown
TSBasicSymplecticType
```

Example 4 (unknown):
```unknown
TSBasicSymplecticSetType()
```

---

## TSBasicSymplecticInitializePackage#

**URL:** https://petsc.org/release/manualpages/TS/TSBasicSymplecticInitializePackage/

**Contents:**
- TSBasicSymplecticInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function initializes everything in the TSBASICSYMPLECTIC package. It is called from TSInitializePackage().

TS: Scalable ODE and DAE Solvers, PetscInitialize(), TSBASICSYMPLECTIC

src/ts/impls/symplectic/basicsymplectic/basicsymplectic.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSBASICSYMPLECTIC
```

Example 2 (unknown):
```unknown
TSInitializePackage()
```

Example 3 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSBasicSymplecticInitializePackage(void)
```

Example 4 (unknown):
```unknown
PetscInitialize()
```

---

## TSBasicSymplecticRegisterAll#

**URL:** https://petsc.org/release/manualpages/TS/TSBasicSymplecticRegisterAll/

**Contents:**
- TSBasicSymplecticRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the basic symplectic integration methods in TSBASICSYMPLECTIC

Not Collective, but should be called by all processes which will need the schemes to be registered

TS: Scalable ODE and DAE Solvers, TSBASICSYMPLECTIC, TSBasicSymplecticRegisterDestroy()

src/ts/impls/symplectic/basicsymplectic/basicsymplectic.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSBASICSYMPLECTIC
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSBasicSymplecticRegisterAll(void)
```

Example 3 (unknown):
```unknown
TSBASICSYMPLECTIC
```

Example 4 (unknown):
```unknown
TSBasicSymplecticRegisterDestroy()
```

---

## TSBasicSymplecticRegisterDestroy#

**URL:** https://petsc.org/release/manualpages/TS/TSBasicSymplecticRegisterDestroy/

**Contents:**
- TSBasicSymplecticRegisterDestroy#
- Synopsis#
- See Also#
- Level#
- Location#

Frees the list of schemes that were registered by TSBasicSymplecticRegister().

TS: Scalable ODE and DAE Solvers, TSBasicSymplecticRegister(), TSBasicSymplecticRegisterAll(), TSBASICSYMPLECTIC

src/ts/impls/symplectic/basicsymplectic/basicsymplectic.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSBasicSymplecticRegister()
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSBasicSymplecticRegisterDestroy(void)
```

Example 3 (unknown):
```unknown
TSBasicSymplecticRegister()
```

Example 4 (unknown):
```unknown
TSBasicSymplecticRegisterAll()
```

---

## TSBasicSymplecticRegister#

**URL:** https://petsc.org/release/manualpages/TS/TSBasicSymplecticRegister/

**Contents:**
- TSBasicSymplecticRegister#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

register a basic symplectic integration scheme by providing the coefficients.

Not Collective, but the same schemes should be registered on all processes on which they will be used

name - identifier for method

order - approximation order of method

s - number of stages, this is the dimension of the matrices below

c - coefficients for updating generalized position (dimension s)

d - coefficients for updating generalized momentum (dimension s)

Several symplectic methods are provided, this function is only needed to create new methods.

TS: Scalable ODE and DAE Solvers, TSBASICSYMPLECTIC

src/ts/impls/symplectic/basicsymplectic/basicsymplectic.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSBasicSymplecticRegister(TSRosWType name, PetscInt order, PetscInt s, PetscReal c[], PetscReal d[])
```

Example 2 (unknown):
```unknown
TSBASICSYMPLECTIC
```

---

## TSBasicSymplecticSetType#

**URL:** https://petsc.org/release/manualpages/TS/TSBasicSymplecticSetType/

**Contents:**
- TSBasicSymplecticSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Set the type of the basic symplectic method

ts - timestepping context

bsymptype - type of the symplectic scheme

-ts_basicsymplectic_type scheme - select the scheme

The symplectic solver always expects a two-way splitting with the split names being “position” and “momentum”. Each split is associated with an IS object and a sub-TS that is intended to store the user-provided RHS function.

TS: Scalable ODE and DAE Solvers, TSBASICSYMPLECTIC, TSBasicSymplecticType

src/ts/impls/symplectic/basicsymplectic/basicsymplectic.c

TSBasicSymplecticSetType_BasicSymplectic() in src/ts/impls/symplectic/basicsymplectic/basicsymplectic.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSBasicSymplecticSetType(TS ts, TSBasicSymplecticType bsymptype)
```

Example 2 (unknown):
```unknown
TSBASICSYMPLECTIC
```

Example 3 (unknown):
```unknown
TSBasicSymplecticType
```

---

## TSBASICSYMPLECTICSIEULER#

**URL:** https://petsc.org/release/manualpages/TS/TSBASICSYMPLECTICSIEULER/

**Contents:**
- TSBASICSYMPLECTICSIEULER#
- See Also#
- Level#
- Location#

first order semi-implicit Euler method

TS: Scalable ODE and DAE Solvers, TSBASICSYMPLECTIC

src/ts/impls/symplectic/basicsymplectic/basicsymplectic.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSBASICSYMPLECTIC
```

---

## TSBasicSymplecticType#

**URL:** https://petsc.org/release/manualpages/TS/TSBasicSymplecticType/

**Contents:**
- TSBasicSymplecticType#
- Synopsis#
- See Also#
- Level#
- Location#

String with the name of a basic symplectic integration TSBASICSYMPLECTIC type

TS: Scalable ODE and DAE Solvers, TSBasicSymplecticSetType(), TS, TSBASICSYMPLECTIC, TSBasicSymplecticRegister()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSBASICSYMPLECTIC
```

Example 2 (cpp):
```cpp
#include <petscts.h> 
typedef const char *TSBasicSymplecticType;
#define TSBASICSYMPLECTICSIEULER   "1"
#define TSBASICSYMPLECTICVELVERLET "2"
#define TSBASICSYMPLECTIC3         "3"
#define TSBASICSYMPLECTIC4         "4"
```

Example 3 (unknown):
```unknown
TSBasicSymplecticSetType()
```

Example 4 (unknown):
```unknown
TSBASICSYMPLECTIC
```

---

## TSBASICSYMPLECTICVELVERLET#

**URL:** https://petsc.org/release/manualpages/TS/TSBASICSYMPLECTICVELVERLET/

**Contents:**
- TSBASICSYMPLECTICVELVERLET#
- See Also#
- Level#
- Location#

second order Velocity Verlet method (leapfrog method with starting process and determining velocity and position at the same time)

TS: Scalable ODE and DAE Solvers, TSBASICSYMPLECTIC

src/ts/impls/symplectic/basicsymplectic/basicsymplectic.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSBASICSYMPLECTIC
```

---

## TSBASICSYMPLECTIC#

**URL:** https://petsc.org/release/manualpages/TS/TSBASICSYMPLECTIC/

**Contents:**
- TSBASICSYMPLECTIC#
- See Also#
- Level#
- Location#

ODE solver using basic symplectic integration schemes https://en.wikipedia.org/wiki/Symplectic_integrator These methods are intended for separable Hamiltonian systems

where the Hamiltonian can be split into the sum of kinetic energy and potential energy

As a result, the system can be generally represented by

and solved iteratively with \(i \in [0, n]\)

The solution vector should contain both q and p, which correspond to (generalized) position and momentum respectively. Note that the momentum component could simply be velocity in some representations. The symplectic solver always expects a two-way splitting with the split names being “position” and “momentum”. Each split is associated with an IS object and a sub-TS that is intended to store the user-provided RHS function.

TS: Scalable ODE and DAE Solvers, TSCreate(), TSSetType(), TSRHSSplitSetIS(), TSRHSSplitSetRHSFunction(), TSType

src/ts/impls/symplectic/basicsymplectic/basicsymplectic.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetType()
```

Example 2 (unknown):
```unknown
TSRHSSplitSetIS()
```

Example 3 (unknown):
```unknown
TSRHSSplitSetRHSFunction()
```

---

## TSBDFGetOrder#

**URL:** https://petsc.org/release/manualpages/TS/TSBDFGetOrder/

**Contents:**
- TSBDFGetOrder#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get the order of the TSBDF method

ts - timestepping context

order - order of the method

TSBDFSetOrder(), TS, TSBDF

src/ts/impls/bdf/bdf.c

TSBDFGetOrder_BDF() in src/ts/impls/bdf/bdf.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSBDFGetOrder(TS ts, PetscInt *order)
```

Example 2 (unknown):
```unknown
TSBDFSetOrder()
```

---

## TSBDFSetOrder#

**URL:** https://petsc.org/release/manualpages/TS/TSBDFSetOrder/

**Contents:**
- TSBDFSetOrder#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

Set the order of the TSBDF method

ts - timestepping context

order - order of the method

-ts_bdf_order order - select the order

TSBDFGetOrder(), TS, TSBDF

src/ts/impls/bdf/bdf.c

TSBDFSetOrder_BDF() in src/ts/impls/bdf/bdf.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSBDFSetOrder(TS ts, PetscInt order)
```

Example 2 (unknown):
```unknown
TSBDFGetOrder()
```

---

## TSBDF#

**URL:** https://petsc.org/release/manualpages/TS/TSBDF/

**Contents:**
- TSBDF#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Implementations#

DAE solver using implicit backward differentiation formula (BDF) methods suitable for stiff ODEs.

-ts_bdf_order n - Order of the BDF method

-ts_bdf_initial_guess_extrapolate (true|false) - Extrapolate the initial guess of the nonlinear solve from previous time steps, defaults to true

TS: Scalable ODE and DAE Solvers, TS, TSCreate(), TSSetType(), TSType, TSBDFSetOrder()

src/ts/impls/bdf/bdf.c

TSBDF_GetVecs() in src/ts/impls/bdf/bdf.c TSBDF_RestoreVecs() in src/ts/impls/bdf/bdf.c TSBDF_Advance() in src/ts/impls/bdf/bdf.c TSBDF_VecLTE() in src/ts/impls/bdf/bdf.c TSBDF_Extrapolate() in src/ts/impls/bdf/bdf.c TSBDF_Interpolate() in src/ts/impls/bdf/bdf.c TSBDF_PreSolve() in src/ts/impls/bdf/bdf.c TSBDF_SNESSolve() in src/ts/impls/bdf/bdf.c TSBDF_Restart() in src/ts/impls/bdf/bdf.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetType()
```

Example 2 (unknown):
```unknown
TSBDFSetOrder()
```

---

## TSBEULER#

**URL:** https://petsc.org/release/manualpages/TS/TSBEULER/

**Contents:**
- TSBEULER#
- Note#
- See Also#
- Level#
- Location#
- Examples#

ODE solver using the implicit backward Euler method

TSBEULER is equivalent to TSTHETA with Theta=1.0 or -ts_type theta -ts_theta_theta 1.0

TS: Scalable ODE and DAE Solvers, TSCreate(), TS, TSSetType(), TSEULER, TSCN, TSTHETA

src/ts/impls/implicit/theta/theta.c

src/ts/tutorials/ex20.c src/ts/tutorials/ex49.c src/ts/tutorials/ex18.c src/ts/tutorials/ex7.c src/ts/tutorials/ex15.c src/ts/tutorials/ex21.c src/ts/tutorials/ex31.c src/ts/tutorials/ex2.c src/ts/tutorials/ex13.c src/ts/tutorials/ex12.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
-ts_type theta -ts_theta_theta 1.0
```

Example 2 (unknown):
```unknown
TSSetType()
```

---

## TSClone#

**URL:** https://petsc.org/release/manualpages/TS/TSClone/

**Contents:**
- TSClone#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

This function clones a time step TS object.

tsout - The output TS (cloned)

This function is used to create a clone of a TS object. It is used in TSARKIMEX for initializing the slope for first stage explicit methods. It will likely be replaced in the future with a mechanism of switching methods on the fly.

When using TSDestroy() on a clone the user has to first reset the correct TS reference in the embedded SNES object: e.g., by running

TS: Scalable ODE and DAE Solvers, TS, SNES, TSCreate(), TSSetType(), TSSetUp(), TSDestroy(), TSSetProblemType()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSClone(TS tsin, TS *tsout)
```

Example 2 (unknown):
```unknown
TSDestroy()
```

Example 3 (unknown):
```unknown
SNES snes_dup = NULL;
 TSGetSNES(ts,&snes_dup);
 TSSetSNES(ts,snes_dup);
```

Example 4 (unknown):
```unknown
TSSetType()
```

---

## TSCN#

**URL:** https://petsc.org/release/manualpages/TS/TSCN/

**Contents:**
- TSCN#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

ODE solver using the implicit Crank-Nicolson method.

TSCN is equivalent to TSTHETA with Theta=0.5 and the “endpoint” option set. I.e.

TS: Scalable ODE and DAE Solvers, TSCreate(), TS, TSSetType(), TSBEULER, TSTHETA, TSType

src/ts/impls/implicit/theta/theta.c

src/ts/tutorials/ex20opt_p.c src/ts/tutorials/ex20opt_ic.c src/ts/tutorials/ex20adj.c src/ts/tutorials/ex27.c src/ts/tutorials/ex31.c src/ts/tutorials/ex20td.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
-ts_type theta
  -ts_theta_theta 0.5
  -ts_theta_endpoint
```

Example 2 (unknown):
```unknown
TSSetType()
```

---

## TSComputeCostIntegrand#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSComputeCostIntegrand/

**Contents:**
- TSComputeCostIntegrand#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Evaluates the integral function in the cost functions.

U - state vector, i.e. current solution

Q - vector of size numcost to hold the outputs

Most users should not need to explicitly call this routine, as it is used internally within the sensitivity analysis context.

TS: Scalable ODE and DAE Solvers, TS, TSAdjointSolve(), TSSetCostIntegrand()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSComputeCostIntegrand(TS ts, PetscReal t, Vec U, Vec Q)
```

Example 2 (unknown):
```unknown
TSAdjointSolve()
```

Example 3 (unknown):
```unknown
TSSetCostIntegrand()
```

---

## TSComputeDRDPFunction#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSComputeDRDPFunction/

**Contents:**
- TSComputeDRDPFunction#
- Synopsis#
- Level#
- Location#

Deprecated, use TSGetQuadratureTS() then TSComputeRHSJacobianP()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGetQuadratureTS()
```

Example 2 (unknown):
```unknown
TSComputeRHSJacobianP()
```

Example 3 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSComputeDRDPFunction(TS ts, PetscReal t, Vec U, Vec *DRDP)
```

---

## TSComputeDRDUFunction#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSComputeDRDUFunction/

**Contents:**
- TSComputeDRDUFunction#
- Synopsis#
- Level#
- Location#

Deprecated, use TSGetQuadratureTS() then TSComputeRHSJacobian()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGetQuadratureTS()
```

Example 2 (unknown):
```unknown
TSComputeRHSJacobian()
```

Example 3 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSComputeDRDUFunction(TS ts, PetscReal t, Vec U, Vec *DRDU)
```

---

## TSComputeExactError#

**URL:** https://petsc.org/release/manualpages/TS/TSComputeExactError/

**Contents:**
- TSComputeExactError#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Compute the solution error for the timestepping using the function previously set with TSSetComputeExactError()

ts - time stepping context

u - The approximate solution

e - The Vec used to store the error

TS: Scalable ODE and DAE Solvers, TS, TSGetComputeInitialCondition(), TSSetComputeInitialCondition(), TSSolve()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetComputeExactError()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSComputeExactError(TS ts, Vec u, Vec e)
```

Example 3 (unknown):
```unknown
TSGetComputeInitialCondition()
```

Example 4 (unknown):
```unknown
TSSetComputeInitialCondition()
```

---

## TSComputeForcingFunction#

**URL:** https://petsc.org/release/manualpages/TS/TSComputeForcingFunction/

**Contents:**
- TSComputeForcingFunction#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Evaluates the forcing function.

U - the function value

TS: Scalable ODE and DAE Solvers, TS, TSSetSolutionFunction(), TSSetRHSFunction(), TSComputeIFunction()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSComputeForcingFunction(TS ts, PetscReal t, Vec U)
```

Example 2 (unknown):
```unknown
TSSetSolutionFunction()
```

Example 3 (unknown):
```unknown
TSSetRHSFunction()
```

Example 4 (unknown):
```unknown
TSComputeIFunction()
```

---

## TSComputeI2Function#

**URL:** https://petsc.org/release/manualpages/TS/TSComputeI2Function/

**Contents:**
- TSComputeI2Function#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Evaluates the DAE residual written in implicit form F(t,U,U_t,U_tt) = 0

V - time derivative of state vector (U_t)

A - second time derivative of state vector (U_tt)

F - the residual vector

Most users should not need to explicitly call this routine, as it is used internally within the nonlinear solvers.

TS: Scalable ODE and DAE Solvers, TS, TSSetI2Function(), TSGetI2Function()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSComputeI2Function(TS ts, PetscReal t, Vec U, Vec V, Vec A, Vec F)
```

Example 2 (unknown):
```unknown
TSSetI2Function()
```

Example 3 (unknown):
```unknown
TSGetI2Function()
```

---

## TSComputeI2Jacobian#

**URL:** https://petsc.org/release/manualpages/TS/TSComputeI2Jacobian/

**Contents:**
- TSComputeI2Jacobian#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Evaluates the Jacobian of the DAE

V - time derivative of state vector

A - second time derivative of state vector

shiftV - shift to apply, see note below

shiftA - shift to apply, see note below

P - optional matrix used to construct the preconditioner

If \(F(t,U,V,A) = 0\) is the DAE, the required Jacobian is

is used internally within the ODE integrators.

TS: Scalable ODE and DAE Solvers, TS, TSSetI2Jacobian()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSComputeI2Jacobian(TS ts, PetscReal t, Vec U, Vec V, Vec A, PetscReal shiftV, PetscReal shiftA, Mat J, Mat P)
```

Example 2 (bash):
```bash
$dF/dU + shiftV*dF/dV + shiftA*dF/dA
```

Example 3 (typescript):
```typescript
$Most users should not need to explicitly call this routine, as it
```

Example 4 (unknown):
```unknown
TSSetI2Jacobian()
```

---

## TSComputeIFunctionLinear#

**URL:** https://petsc.org/release/manualpages/TS/TSComputeIFunctionLinear/

**Contents:**
- TSComputeIFunctionLinear#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Evaluate the left hand side via the user-provided Jacobian, for linear problems only

ts - time stepping context

t - time at which to evaluate

U - state at which to evaluate

Udot - time derivative of state vector

The assumption here is that the left hand side is of the form AUdot (and not AUdot + B*U). For other cases, the user is required to write their own TSComputeIFunction(). This function is intended to be passed to TSSetIFunction() to evaluate the left hand side for linear problems. The matrix (and optionally the evaluation context) should be passed to TSSetIJacobian().

Note that using this function is NOT equivalent to using TSComputeRHSFunctionLinear() since that solves Udot = A U

TS: Scalable ODE and DAE Solvers, TS, TSSetIFunction(), TSSetIJacobian(), TSComputeIJacobianConstant(), TSComputeRHSFunctionLinear()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSComputeIFunctionLinear(TS ts, PetscReal t, Vec U, Vec Udot, Vec F, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSComputeIFunction()
```

Example 3 (unknown):
```unknown
TSSetIFunction()
```

Example 4 (unknown):
```unknown
TSSetIJacobian()
```

---

## TSComputeIFunction#

**URL:** https://petsc.org/release/manualpages/TS/TSComputeIFunction/

**Contents:**
- TSComputeIFunction#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Evaluates the DAE residual written in the implicit form F(t,U,Udot)=0

Udot - time derivative of state vector

imex - flag indicates if the method is TSARKIMEX so that the RHSFunction should be kept separate

Most users should not need to explicitly call this routine, as it is used internally within the nonlinear solvers.

If the user did not write their equations in implicit form, this function recasts them in implicit form.

TS: Scalable ODE and DAE Solvers, TS, TSSetIFunction(), TSComputeRHSFunction()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSComputeIFunction(TS ts, PetscReal t, Vec U, Vec Udot, Vec Y, PetscBool imex)
```

Example 2 (unknown):
```unknown
TSSetIFunction()
```

Example 3 (unknown):
```unknown
TSComputeRHSFunction()
```

---

## TSComputeIHessianProductFunctionPP#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSComputeIHessianProductFunctionPP/

**Contents:**
- TSComputeIHessianProductFunctionPP#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Runs the user-defined vector-Hessian-vector product function for Fpp.

ts - The TS context obtained from TSCreate()

U - the solution at which to compute the Hessian product

Vl - the array of input vectors to be multiplied with the Hessian from the left

Vr - the input vector to be multiplied with the Hessian from the right

VHV - the array of output vectors that store the Hessian product

TSComputeIHessianProductFunctionPP() is typically used for sensitivity implementation, so most users would not generally call this routine themselves.

TS: Scalable ODE and DAE Solvers, TSSetIHessianProduct()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSComputeIHessianProductFunctionPP(TS ts, PetscReal t, Vec U, Vec Vl[], Vec Vr, Vec VHV[])
```

Example 2 (unknown):
```unknown
TSComputeIHessianProductFunctionPP()
```

Example 3 (unknown):
```unknown
TSSetIHessianProduct()
```

---

## TSComputeIHessianProductFunctionPU#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSComputeIHessianProductFunctionPU/

**Contents:**
- TSComputeIHessianProductFunctionPU#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Runs the user-defined vector-Hessian-vector product function for Fpu.

ts - The TS context obtained from TSCreate()

U - the solution at which to compute the Hessian product

Vl - the array of input vectors to be multiplied with the Hessian from the left

Vr - the input vector to be multiplied with the Hessian from the right

VHV - the array of output vectors that store the Hessian product

TSComputeIHessianProductFunctionPU() is typically used for sensitivity implementation, so most users would not generally call this routine themselves.

TS: Scalable ODE and DAE Solvers, TSSetIHessianProduct()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSComputeIHessianProductFunctionPU(TS ts, PetscReal t, Vec U, Vec Vl[], Vec Vr, Vec VHV[])
```

Example 2 (unknown):
```unknown
TSComputeIHessianProductFunctionPU()
```

Example 3 (unknown):
```unknown
TSSetIHessianProduct()
```

---

## TSComputeIHessianProductFunctionUP#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSComputeIHessianProductFunctionUP/

**Contents:**
- TSComputeIHessianProductFunctionUP#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Runs the user-defined vector-Hessian-vector product function for Fup.

ts - The TS context obtained from TSCreate()

U - the solution at which to compute the Hessian product

Vl - the array of input vectors to be multiplied with the Hessian from the left

Vr - the input vector to be multiplied with the Hessian from the right

VHV - the array of output vectors that store the Hessian product

TSComputeIHessianProductFunctionUP() is typically used for sensitivity implementation, so most users would not generally call this routine themselves.

TS: Scalable ODE and DAE Solvers, TSSetIHessianProduct()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSComputeIHessianProductFunctionUP(TS ts, PetscReal t, Vec U, Vec Vl[], Vec Vr, Vec VHV[])
```

Example 2 (unknown):
```unknown
TSComputeIHessianProductFunctionUP()
```

Example 3 (unknown):
```unknown
TSSetIHessianProduct()
```

---

## TSComputeIHessianProductFunctionUU#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSComputeIHessianProductFunctionUU/

**Contents:**
- TSComputeIHessianProductFunctionUU#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Runs the user-defined vector-Hessian-vector product function for Fuu.

ts - The TS context obtained from TSCreate()

U - the solution at which to compute the Hessian product

Vl - the array of input vectors to be multiplied with the Hessian from the left

Vr - the input vector to be multiplied with the Hessian from the right

VHV - the array of output vectors that store the Hessian product

TSComputeIHessianProductFunctionUU() is typically used for sensitivity implementation, so most users would not generally call this routine themselves.

TS: Scalable ODE and DAE Solvers, TSSetIHessianProduct()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSComputeIHessianProductFunctionUU(TS ts, PetscReal t, Vec U, Vec Vl[], Vec Vr, Vec VHV[])
```

Example 2 (unknown):
```unknown
TSComputeIHessianProductFunctionUU()
```

Example 3 (unknown):
```unknown
TSSetIHessianProduct()
```

---

## TSComputeIJacobianConstant#

**URL:** https://petsc.org/release/manualpages/TS/TSComputeIJacobianConstant/

**Contents:**
- TSComputeIJacobianConstant#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Reuses the matrix previously computed with the provided TSIJacobianFn for a semi-implicit DAE or ODE

ts - time stepping context

t - time at which to evaluate

U - state at which to evaluate

Udot - time derivative of state vector

shift - shift to apply

A - pointer to operator

B - pointer to matrix from which the preconditioner is built (often A)

This function is intended to be passed to TSSetIJacobian() to evaluate the Jacobian for linear time-independent problems.

It is only appropriate for problems of the form

where M is constant and F is non-stiff. The user must pass M to TSSetIJacobian(). The current implementation only works with IMEX time integration methods such as TSROSW and TSARKIMEX, since there is no support for de-constructing an implicit operator of the form

where J is the Jacobian of -F(U). Support may be added in a future version of PETSc, but for now, the user must store a copy of M or reassemble it when requested.

TS: Scalable ODE and DAE Solvers, TS, TSROSW, TSARKIMEX, TSSetIFunction(), TSSetIJacobian(), TSComputeIFunctionLinear()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSIJacobianFn
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSComputeIJacobianConstant(TS ts, PetscReal t, Vec U, Vec Udot, PetscReal shift, Mat A, Mat B, PetscCtx ctx)
```

Example 3 (unknown):
```unknown
TSSetIJacobian()
```

Example 4 (unknown):
```unknown
TSSetIJacobian()
```

---

## TSComputeIJacobianDefaultColor#

**URL:** https://petsc.org/release/manualpages/TS/TSComputeIJacobianDefaultColor/

**Contents:**
- TSComputeIJacobianDefaultColor#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Computes the Jacobian using finite differences and coloring to exploit matrix sparsity.

Udot - time derivative of state vector

shift - shift to apply, see note below

ctx - an optional application context

J - Jacobian matrix (not altered in this routine)

B - newly computed Jacobian matrix to use with preconditioner (generally the same as J)

If F(t,U,Udot)=0 is the DAE, the required Jacobian is

dF/dU + shift*dF/dUdot

Most users should not need to explicitly call this routine, as it is used internally within the nonlinear solvers.

This will first try to get the coloring from the DM. If the DM type has no coloring routine, then it will try to get the coloring from the matrix. This requires that the matrix have nonzero entries precomputed.

TS: Scalable ODE and DAE Solvers, TS, TSSetIJacobian(), MatFDColoringCreate(), MatFDColoringSetFunction()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSComputeIJacobianDefaultColor(TS ts, PetscReal t, Vec U, Vec Udot, PetscReal shift, Mat J, Mat B, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSSetIJacobian()
```

Example 3 (unknown):
```unknown
MatFDColoringCreate()
```

Example 4 (unknown):
```unknown
MatFDColoringSetFunction()
```

---

## TSComputeIJacobianP#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSComputeIJacobianP/

**Contents:**
- TSComputeIJacobianP#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Runs the user-defined IJacobianP function.

Udot - time derivative of state vector

shift - shift to apply, see note below

imex - flag indicates if the method is IMEX so that the RHSJacobianP should be kept separate

Amat - Jacobian matrix

TS: Scalable ODE and DAE Solvers, TS, TSSetIJacobianP()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSComputeIJacobianP(TS ts, PetscReal t, Vec U, Vec Udot, PetscReal shift, Mat Amat, PetscBool imex)
```

Example 2 (unknown):
```unknown
RHSJacobianP
```

Example 3 (unknown):
```unknown
TSSetIJacobianP()
```

---

## TSComputeIJacobian#

**URL:** https://petsc.org/release/manualpages/TS/TSComputeIJacobian/

**Contents:**
- TSComputeIJacobian#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Evaluates the Jacobian of the DAE

Udot - time derivative of state vector

shift - shift to apply, see note below

imex - flag indicates if the method is TSARKIMEX so that the RHSJacobian should be kept separate

B - matrix from which the preconditioner is constructed; often the same as A

If \( F(t,U,\dot{U})=0 \) is the DAE, the required Jacobian is

Most users should not need to explicitly call this routine, as it is used internally within the nonlinear solvers.

TS: Scalable ODE and DAE Solvers, TS, TSSetIJacobian()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSComputeIJacobian(TS ts, PetscReal t, Vec U, Vec Udot, PetscReal shift, Mat A, Mat B, PetscBool imex)
```

Example 2 (unknown):
```unknown
dF/dU + shift*dF/dUdot
```

Example 3 (unknown):
```unknown
TSSetIJacobian()
```

---

## TSComputeInitialCondition#

**URL:** https://petsc.org/release/manualpages/TS/TSComputeInitialCondition/

**Contents:**
- TSComputeInitialCondition#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Compute an initial condition for the timestepping using the function previously set with TSSetComputeInitialCondition()

ts - time stepping context

u - The Vec to store the condition in which will be used in TSSolve()

TS: Scalable ODE and DAE Solvers, TS, TSGetComputeInitialCondition(), TSSetComputeInitialCondition(), TSSolve()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetComputeInitialCondition()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSComputeInitialCondition(TS ts, Vec u)
```

Example 3 (unknown):
```unknown
TSGetComputeInitialCondition()
```

Example 4 (unknown):
```unknown
TSSetComputeInitialCondition()
```

---

## TSComputeLinearStability#

**URL:** https://petsc.org/release/manualpages/TS/TSComputeLinearStability/

**Contents:**
- TSComputeLinearStability#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Implementations#

computes the linear stability function at a point

xr - real part of input argument

xi - imaginary part of input argument

yr - real part of function value

yi - imaginary part of function value

TS: Scalable ODE and DAE Solvers, TS, TSSetRHSFunction(), TSComputeIFunction()

src/ts/interface/ts.c

TSComputeLinearStability_Euler() in src/ts/impls/explicit/euler/euler.c TSComputeLinearStability_Theta() in src/ts/impls/implicit/theta/theta.c TSComputeLinearStability_Mimex() in src/ts/impls/mimex/mimex.c TSComputeLinearStability_BasicSymplectic() in src/ts/impls/symplectic/basicsymplectic/basicsymplectic.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSComputeLinearStability(TS ts, PetscReal xr, PetscReal xi, PetscReal *yr, PetscReal *yi)
```

Example 2 (unknown):
```unknown
TSSetRHSFunction()
```

Example 3 (unknown):
```unknown
TSComputeIFunction()
```

---

## TSComputeRHSFunctionLinear#

**URL:** https://petsc.org/release/manualpages/TS/TSComputeRHSFunctionLinear/

**Contents:**
- TSComputeRHSFunctionLinear#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Evaluate the right-hand side via the user-provided Jacobian, for linear problems Udot = A U only

ts - time stepping context

t - time at which to evaluate

U - state at which to evaluate

This function is intended to be passed to TSSetRHSFunction() to evaluate the right-hand side for linear problems. The matrix (and optionally the evaluation context) should be passed to TSSetRHSJacobian().

TS: Scalable ODE and DAE Solvers, TS, TSSetRHSFunction(), TSSetRHSJacobian(), TSComputeRHSJacobianConstant()

src/ts/interface/ts.c

src/ts/tutorials/ex74.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/tutorials/ex5.c src/ts/tutorials/ex4.c src/ts/tutorials/ex3.c src/ts/tutorials/ex6.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSComputeRHSFunctionLinear(TS ts, PetscReal t, Vec U, Vec F, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSSetRHSFunction()
```

Example 3 (unknown):
```unknown
TSSetRHSJacobian()
```

Example 4 (unknown):
```unknown
TSSetRHSFunction()
```

---

## TSComputeRHSFunction#

**URL:** https://petsc.org/release/manualpages/TS/TSComputeRHSFunction/

**Contents:**
- TSComputeRHSFunction#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Evaluates the right-hand-side function for a TS

Most users should not need to explicitly call this routine, as it is used internally within the nonlinear solvers.

TS: Scalable ODE and DAE Solvers, TS, TSSetRHSFunction(), TSComputeIFunction()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSComputeRHSFunction(TS ts, PetscReal t, Vec U, Vec y)
```

Example 2 (unknown):
```unknown
TSSetRHSFunction()
```

Example 3 (unknown):
```unknown
TSComputeIFunction()
```

---

## TSComputeRHSHessianProductFunctionPP#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSComputeRHSHessianProductFunctionPP/

**Contents:**
- TSComputeRHSHessianProductFunctionPP#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Runs the user-defined vector-Hessian-vector product function for \(G_{pp}\).

ts - The TS context obtained from TSCreate()

U - the solution at which to compute the Hessian product

Vl - the array of input vectors to be multiplied with the Hessian from the left

Vr - the input vector to be multiplied with the Hessian from the right

VHV - the array of output vectors that store the Hessian product

TSComputeRHSHessianProductFunctionPP() is typically used for sensitivity implementation, so most users would not generally call this routine themselves.

TS: Scalable ODE and DAE Solvers, TSSetRHSHessianProduct()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSComputeRHSHessianProductFunctionPP(TS ts, PetscReal t, Vec U, Vec Vl[], Vec Vr, Vec VHV[])
```

Example 2 (unknown):
```unknown
TSComputeRHSHessianProductFunctionPP()
```

Example 3 (unknown):
```unknown
TSSetRHSHessianProduct()
```

---

## TSComputeRHSHessianProductFunctionPU#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSComputeRHSHessianProductFunctionPU/

**Contents:**
- TSComputeRHSHessianProductFunctionPU#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Runs the user-defined vector-Hessian-vector product function for \(G_{pu}.\)

ts - The TS context obtained from TSCreate()

U - the solution at which to compute the Hessian product

Vl - the array of input vectors to be multiplied with the Hessian from the left

Vr - the input vector to be multiplied with the Hessian from the right

VHV - the array of output vectors that store the Hessian product

TSComputeRHSHessianProductFunctionPU() is typically used for sensitivity implementation, so most users would not generally call this routine themselves.

TS: Scalable ODE and DAE Solvers, TSSetRHSHessianProduct()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSComputeRHSHessianProductFunctionPU(TS ts, PetscReal t, Vec U, Vec Vl[], Vec Vr, Vec VHV[])
```

Example 2 (unknown):
```unknown
TSComputeRHSHessianProductFunctionPU()
```

Example 3 (unknown):
```unknown
TSSetRHSHessianProduct()
```

---

## TSComputeRHSHessianProductFunctionUP#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSComputeRHSHessianProductFunctionUP/

**Contents:**
- TSComputeRHSHessianProductFunctionUP#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Runs the user-defined vector-Hessian-vector product function for \(G_{up}\).

ts - The TS context obtained from TSCreate()

U - the solution at which to compute the Hessian product

Vl - the array of input vectors to be multiplied with the Hessian from the left

Vr - the input vector to be multiplied with the Hessian from the right

VHV - the array of output vectors that store the Hessian product

TSComputeRHSHessianProductFunctionUP() is typically used for sensitivity implementation, so most users would not generally call this routine themselves.

TS: Scalable ODE and DAE Solvers, TS, TSSetRHSHessianProduct()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSComputeRHSHessianProductFunctionUP(TS ts, PetscReal t, Vec U, Vec Vl[], Vec Vr, Vec VHV[])
```

Example 2 (unknown):
```unknown
TSComputeRHSHessianProductFunctionUP()
```

Example 3 (unknown):
```unknown
TSSetRHSHessianProduct()
```

---

## TSComputeRHSHessianProductFunctionUU#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSComputeRHSHessianProductFunctionUU/

**Contents:**
- TSComputeRHSHessianProductFunctionUU#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Runs the user-defined vector-Hessian-vector product function for \(G_{uu}\).

ts - The TS context obtained from TSCreate()

U - the solution at which to compute the Hessian product

Vl - the array of input vectors to be multiplied with the Hessian from the left

Vr - the input vector to be multiplied with the Hessian from the right

VHV - the array of output vectors that store the Hessian product

TSComputeRHSHessianProductFunctionUU() is typically used for sensitivity implementation, so most users would not generally call this routine themselves.

TS: Scalable ODE and DAE Solvers, TS, TSSetRHSHessianProduct()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSComputeRHSHessianProductFunctionUU(TS ts, PetscReal t, Vec U, Vec Vl[], Vec Vr, Vec VHV[])
```

Example 2 (unknown):
```unknown
TSComputeRHSHessianProductFunctionUU()
```

Example 3 (unknown):
```unknown
TSSetRHSHessianProduct()
```

---

## TSComputeRHSJacobianConstant#

**URL:** https://petsc.org/release/manualpages/TS/TSComputeRHSJacobianConstant/

**Contents:**
- TSComputeRHSJacobianConstant#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Reuses a Jacobian that is time-independent.

ts - time stepping context

t - time at which to evaluate

U - state at which to evaluate

B - matrix used to construct the preconditioner, often the same as A

This function is intended to be passed to TSSetRHSJacobian() to evaluate the Jacobian for linear time-independent problems.

TS: Scalable ODE and DAE Solvers, TS, TSSetRHSFunction(), TSSetRHSJacobian(), TSComputeRHSFunctionLinear()

src/ts/interface/ts.c

src/ts/tutorials/ex74.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/tutorials/ex5.c src/ts/tutorials/ex4.c src/ts/tutorials/ex3.c src/ts/tutorials/ex6.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSComputeRHSJacobianConstant(TS ts, PetscReal t, Vec U, Mat A, Mat B, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSSetRHSJacobian()
```

Example 3 (unknown):
```unknown
TSSetRHSFunction()
```

Example 4 (unknown):
```unknown
TSSetRHSJacobian()
```

---

## TSComputeRHSJacobianP#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSComputeRHSJacobianP/

**Contents:**
- TSComputeRHSJacobianP#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Runs the user-defined JacobianP function.

ts - The TS context obtained from TSCreate()

U - the solution at which to compute the Jacobian

Amat - the computed Jacobian

TS: Scalable ODE and DAE Solvers, TSSetRHSJacobianP(), TS

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSComputeRHSJacobianP(TS ts, PetscReal t, Vec U, Mat Amat)
```

Example 2 (unknown):
```unknown
TSSetRHSJacobianP()
```

---

## TSComputeRHSJacobian#

**URL:** https://petsc.org/release/manualpages/TS/TSComputeRHSJacobian/

**Contents:**
- TSComputeRHSJacobian#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Computes the Jacobian matrix that has been set with TSSetRHSJacobian().

B - optional matrix used to compute the preconditioner, often the same as A

Most users should not need to explicitly call this routine, as it is used internally within the ODE integrators.

TS: Scalable ODE and DAE Solvers, TS, TSSetRHSJacobian(), KSPSetOperators()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetRHSJacobian()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSComputeRHSJacobian(TS ts, PetscReal t, Vec U, Mat A, Mat B)
```

Example 3 (unknown):
```unknown
TSSetRHSJacobian()
```

Example 4 (unknown):
```unknown
KSPSetOperators()
```

---

## TSComputeSNESJacobian#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSComputeSNESJacobian/

**Contents:**
- TSComputeSNESJacobian#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Compute the Jacobian needed for the SNESSolve() in TS

ts - the TS context obtained from TSCreate()

Jpre - matrix used to compute the preconditioner for J (may be same as J)

Uses finite differencing when TS Jacobian is not available.

SNES, TS, SNESSetJacobian(), TSSetRHSJacobian(), TSSetIJacobian()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
SNESSolve()
```

Example 2 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSComputeSNESJacobian(TS ts, Vec x, Mat J, Mat Jpre)
```

Example 3 (unknown):
```unknown
SNESSetJacobian()
```

Example 4 (unknown):
```unknown
TSSetRHSJacobian()
```

---

## TSComputeSolutionFunction#

**URL:** https://petsc.org/release/manualpages/TS/TSComputeSolutionFunction/

**Contents:**
- TSComputeSolutionFunction#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Evaluates the solution function.

TS: Scalable ODE and DAE Solvers, TS, TSSetSolutionFunction(), TSSetRHSFunction(), TSComputeIFunction()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSComputeSolutionFunction(TS ts, PetscReal t, Vec U)
```

Example 2 (unknown):
```unknown
TSSetSolutionFunction()
```

Example 3 (unknown):
```unknown
TSSetRHSFunction()
```

Example 4 (unknown):
```unknown
TSComputeIFunction()
```

---

## TSComputeTransientVariable#

**URL:** https://petsc.org/release/manualpages/TS/TSComputeTransientVariable/

**Contents:**
- TSComputeTransientVariable#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Developer Notes#
- See Also#
- Level#
- Location#

transforms state (primitive) variables to transient (conservative) variables

ts - TS on which to compute

U - state vector to be transformed to transient variables

C - transient (conservative) variable

If DMTSSetTransientVariable() has not been called, then C is not modified in this routine and C = NULL is allowed. This makes it safe to call without a guard. One can use TSHasTransientVariable() to check if transient variables are being used.

TS: Scalable ODE and DAE Solvers, TS, TSBDF, DMTSSetTransientVariable(), TSComputeIFunction(), TSComputeIJacobian()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSComputeTransientVariable(TS ts, Vec U, Vec C)
```

Example 2 (unknown):
```unknown
DMTSSetTransientVariable()
```

Example 3 (unknown):
```unknown
TSHasTransientVariable()
```

Example 4 (unknown):
```unknown
DMTSSetTransientVariable()
```

---

## TSConvergedReason#

**URL:** https://petsc.org/release/manualpages/TS/TSConvergedReason/

**Contents:**
- TSConvergedReason#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#
- Examples#

reason a TS method has converged (integrated to the requested time) or not

TS_CONVERGED_ITERATING - this only occurs if TSGetConvergedReason() is called during the TSSolve()

TS_CONVERGED_TIME - the final time was reached

TS_CONVERGED_ITS - the maximum number of iterations (time-steps) was reached prior to the final time

TS_CONVERGED_USER - user requested termination

TS_CONVERGED_EVENT - user requested termination on event detection

TS_CONVERGED_PSEUDO_FATOL - stops when function norm decreased by a set amount, used only for TSPSEUDO

TS_CONVERGED_PSEUDO_FRTOL - stops when function norm decreases below a set amount, used only for TSPSEUDO

TS_DIVERGED_NONLINEAR_SOLVE - too many nonlinear solve failures have occurred

TS_DIVERGED_STEP_REJECTED - too many steps were rejected

TSFORWARD_DIVERGED_LINEAR_SOLVE - tangent linear solve failed

TSADJOINT_DIVERGED_LINEAR_SOLVE - transposed linear solve failed

TS: Scalable ODE and DAE Solvers, TS, TSGetConvergedReason()

src/ts/tutorials/extchem.c src/ts/tutorials/ex35.cxx src/ts/tutorials/ex18.c src/ts/tutorials/ex25.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/tutorials/ex48.c src/ts/utils/dmplexlandau/tutorials/ex2.c src/ts/tutorials/ex22.c src/ts/tutorials/ex26.c src/ts/tutorials/extchemfield.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h> 
typedef enum {
  TS_CONVERGED_ITERATING          = 0,
  TS_CONVERGED_TIME               = 1,
  TS_CONVERGED_ITS                = 2,
  TS_CONVERGED_USER               = 3,
  TS_CONVERGED_EVENT              = 4,
  TS_CONVERGED_PSEUDO_FATOL       = 5,
  TS_CONVERGED_PSEUDO_FRTOL       = 6,
  TS_DIVERGED_NONLINEAR_SOLVE     = -1,
  TS_DIVERGED_STEP_REJECTED       = -2,
  TSFORWARD_DIVERGED_LINEAR_SOLVE = -3,
  TSADJOINT_DIVERGED_LINEAR_SOLVE = -4
} TSConvergedReason;
```

Example 2 (unknown):
```unknown
TS_CONVERGED_ITERATING
```

Example 3 (unknown):
```unknown
TSGetConvergedReason()
```

Example 4 (unknown):
```unknown
TS_CONVERGED_TIME
```

---

## TSCreate#

**URL:** https://petsc.org/release/manualpages/TS/TSCreate/

**Contents:**
- TSCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

This function creates an empty timestepper. The problem type can then be set with TSSetProblemType() and the type of solver can then be set with TSSetType().

comm - The communicator

TS essentially always creates a SNES object even though explicit methods do not use it. This is unfortunate and should be fixed at some point. The flag snes->usessnes indicates if the particular method does use SNES and regulates if the information about the SNES is printed in TSView(). TSSetFromOptions() does call SNESSetFromOptions() which can lead to users being confused by help messages about meaningless SNES options.

TS: Scalable ODE and DAE Solvers, TS, SNES, TSSetType(), TSSetUp(), TSDestroy(), TSSetProblemType(), TSSetTimeStep()

src/ts/interface/tscreate.c

src/ml/da/tutorials/ex3.c src/ts/tutorials/ex1.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ml/da/tutorials/ex1.c src/ml/da/tutorials/ex2.c src/ts/utils/dmplexlandau/tutorials/ex2.c src/ml/da/tutorials/ex4.c src/tao/unconstrained/tutorials/burgers_spectral.c src/ts/utils/dmplexlandau/tutorials/ex1f90.F90

TSCreate_ARKIMEX() in src/ts/impls/arkimex/arkimex.c TSCreate_DIRK() in src/ts/impls/arkimex/arkimex.c TSCreate_BDF() in src/ts/impls/bdf/bdf.c TSCreate_EIMEX() in src/ts/impls/eimex/eimex.c TSCreate_Euler() in src/ts/impls/explicit/euler/euler.c TSCreate_RK() in src/ts/impls/explicit/rk/rk.c TSCreate_SSP() in src/ts/impls/explicit/ssp/ssp.c TSCreate_GLEE() in src/ts/impls/glee/glee.c TSCreate_Alpha() in src/ts/impls/implicit/alpha/alpha1.c TSCreate_Alpha2() in src/ts/impls/implicit/alpha/alpha2.c TSCreate_DiscGrad() in src/ts/impls/implicit/discgrad/tsdiscgrad.c TSCreate_GLLE() in src/ts/impls/implicit/glle/glle.c TSCreate_IRK() in src/ts/impls/implicit/irk/irk.c TSCreate_Radau5() in src/ts/impls/implicit/radau5/radau5.c TSCreate_Sundials() in src/ts/impls/implicit/sundials/sundials.c TSCreate_Theta() in src/ts/impls/implicit/theta/theta.c TSCreate_BEuler() in src/ts/impls/implicit/theta/theta.c TSCreate_CN() in src/ts/impls/implicit/theta/theta.c TSCreate_Mimex() in src/ts/impls/mimex/mimex.c TSCreate_MPRK() in src/ts/impls/multirate/mprk.c TSCreate_Pseudo() in src/ts/impls/pseudo/posindep.c TSCreate_RosW() in src/ts/impls/rosw/rosw.c TSCreate_BasicSymplectic() in src/ts/impls/symplectic/basicsymplectic/basicsymplectic.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetProblemType()
```

Example 2 (unknown):
```unknown
TSSetType()
```

Example 3 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSCreate(MPI_Comm comm, TS *ts)
```

Example 4 (unknown):
```unknown
TSSetFromOptions(
```

---

## TSDestroy#

**URL:** https://petsc.org/release/manualpages/TS/TSDestroy/

**Contents:**
- TSDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Destroys the timestepper context that was created with TSCreate().

ts - the TS context obtained from TSCreate()

TS: Scalable ODE and DAE Solvers, TS, TSCreate(), TSSetUp(), TSSolve()

src/ts/interface/ts.c

src/ml/da/tutorials/ex3.c src/ts/tutorials/ex1.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ml/da/tutorials/ex1.c src/ml/da/tutorials/ex2.c src/ts/utils/dmplexlandau/tutorials/ex2.c src/ml/da/tutorials/ex4.c src/tao/unconstrained/tutorials/burgers_spectral.c src/ts/utils/dmplexlandau/tutorials/ex1f90.F90

TSDestroy_ARKIMEX() in src/ts/impls/arkimex/arkimex.c TSDestroy_BDF() in src/ts/impls/bdf/bdf.c TSDestroy_EIMEX() in src/ts/impls/eimex/eimex.c TSDestroy_Euler() in src/ts/impls/explicit/euler/euler.c TSDestroy_RK() in src/ts/impls/explicit/rk/rk.c TSDestroy_SSP() in src/ts/impls/explicit/ssp/ssp.c TSDestroy_GLEE() in src/ts/impls/glee/glee.c TSDestroy_Alpha() in src/ts/impls/implicit/alpha/alpha1.c TSDestroy_Alpha() in src/ts/impls/implicit/alpha/alpha2.c TSDestroy_DiscGrad() in src/ts/impls/implicit/discgrad/tsdiscgrad.c TSDestroy_GLLE() in src/ts/impls/implicit/glle/glle.c TSDestroy_IRK() in src/ts/impls/implicit/irk/irk.c TSDestroy_Radau5() in src/ts/impls/implicit/radau5/radau5.c TSDestroy_Sundials() in src/ts/impls/implicit/sundials/sundials.c TSDestroy_Theta() in src/ts/impls/implicit/theta/theta.c TSDestroy_Mimex() in src/ts/impls/mimex/mimex.c TSDestroy_MPRK() in src/ts/impls/multirate/mprk.c TSDestroy_Pseudo() in src/ts/impls/pseudo/posindep.c TSDestroy_RosW() in src/ts/impls/rosw/rosw.c TSDestroy_BasicSymplectic() in src/ts/impls/symplectic/basicsymplectic/basicsymplectic.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSDestroy(TS *ts)
```

---

## TSDGType#

**URL:** https://petsc.org/release/manualpages/TS/TSDGType/

**Contents:**
- TSDGType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Selects the discrete-gradient flavor used by TSDISCGRAD when integrating gradient-system ODEs

TS_DG_GONZALEZ - Gonzalez’s mid-point-style discrete gradient

TS_DG_AVERAGE - average vector field (AVF) discrete gradient

TS_DG_NONE - do not apply a discrete gradient correction; the integrator falls back to a standard mid-point rule

TS, TSDISCGRAD, TSDiscGradSetType(), TSDiscGradGetType(), TSDiscGradSetFormulation()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h> 
typedef enum {
  TS_DG_GONZALEZ,
  TS_DG_AVERAGE,
  TS_DG_NONE
} TSDGType;
```

Example 2 (unknown):
```unknown
TS_DG_GONZALEZ
```

Example 3 (unknown):
```unknown
TS_DG_AVERAGE
```

Example 4 (unknown):
```unknown
TSDiscGradSetType()
```

---

## TSDIRK657A#

**URL:** https://petsc.org/release/manualpages/TS/TSDIRK657A/

**Contents:**
- TSDIRK657A#
- Options Database Key#
- See Also#
- Level#
- Location#

Sixth order DIRK scheme yousefalamri55/High_Order_DIRK_Methods_Coeffs See TSDIRK for additional details.

-ts_dirk_type 657a - select this method.

TS: Scalable ODE and DAE Solvers, TSDIRK, TSDIRKType, TSDIRKSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSDIRKSetType()
```

---

## TSDIRK658A#

**URL:** https://petsc.org/release/manualpages/TS/TSDIRK658A/

**Contents:**
- TSDIRK658A#
- Options Database Key#
- See Also#
- Level#
- Location#

Sixth order DIRK scheme yousefalamri55/High_Order_DIRK_Methods_Coeffs See TSDIRK for additional details.

-ts_dirk_type 658a - select this method.

TS: Scalable ODE and DAE Solvers, TSDIRK, TSDIRKType, TSDIRKSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSDIRKSetType()
```

---

## TSDIRK7510SAL#

**URL:** https://petsc.org/release/manualpages/TS/TSDIRK7510SAL/

**Contents:**
- TSDIRK7510SAL#
- Options Database Key#
- See Also#
- Level#
- Location#

Seventh order DIRK scheme yousefalamri55/High_Order_DIRK_Methods_Coeffs See TSDIRK for additional details.

-ts_dirk_type 7510sal - select this method.

TS: Scalable ODE and DAE Solvers, TSDIRK, TSDIRKType, TSDIRKSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSDIRKSetType()
```

---

## TSDIRK759A#

**URL:** https://petsc.org/release/manualpages/TS/TSDIRK759A/

**Contents:**
- TSDIRK759A#
- Options Database Key#
- See Also#
- Level#
- Location#

Seventh order DIRK scheme yousefalamri55/High_Order_DIRK_Methods_Coeffs See TSDIRK for additional details.

-ts_dirk_type 759a - select this method.

TS: Scalable ODE and DAE Solvers, TSDIRK, TSDIRKType, TSDIRKSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSDIRKSetType()
```

---

## TSDIRK8614A#

**URL:** https://petsc.org/release/manualpages/TS/TSDIRK8614A/

**Contents:**
- TSDIRK8614A#
- Options Database Key#
- See Also#
- Level#
- Location#

Eighth order DIRK scheme yousefalamri55/High_Order_DIRK_Methods_Coeffs See TSDIRK for additional details.

-ts_dirk_type 8614a - select this method.

TS: Scalable ODE and DAE Solvers, TSDIRK, TSDIRKType, TSDIRKSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSDIRKSetType()
```

---

## TSDIRK8616SAL#

**URL:** https://petsc.org/release/manualpages/TS/TSDIRK8616SAL/

**Contents:**
- TSDIRK8616SAL#
- Options Database Key#
- See Also#
- Level#
- Location#

Eighth order DIRK scheme yousefalamri55/High_Order_DIRK_Methods_Coeffs See TSDIRK for additional details.

-ts_dirk_type 8616sal - select this method.

TS: Scalable ODE and DAE Solvers, TSDIRK, TSDIRKType, TSDIRKSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSDIRKSetType()
```

---

## TSDIRKES122SAL#

**URL:** https://petsc.org/release/manualpages/TS/TSDIRKES122SAL/

**Contents:**
- TSDIRKES122SAL#
- Options Database Key#
- See Also#
- Level#
- Location#

First order DIRK scheme https://arxiv.org/abs/1803.01613 Uses backward Euler as advancing method and trapezoidal rule as embedded method. See TSDIRK for additional details.

-ts_dirk_type es122sal - select this method.

TS: Scalable ODE and DAE Solvers, TSDIRK, TSDIRKType, TSDIRKSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSDIRKSetType()
```

---

## TSDIRKES213SAL#

**URL:** https://petsc.org/release/manualpages/TS/TSDIRKES213SAL/

**Contents:**
- TSDIRKES213SAL#
- Options Database Key#
- Note#
- References#
- See Also#
- Level#
- Location#

Second order DIRK scheme [KC19]. Also known as TR-BDF2, see[HS96] See TSDIRK for additional details.

-ts_dirk_type es213sal - select this method.

This is the default DIRK scheme used in PETSc.

ME Hosea and LF Shampine. Analysis and implementation of TR-BDF2. Applied Numerical Mathematics, 20(1-2):21–37, 1996.

Christopher A Kennedy and Mark H Carpenter. Diagonally implicit Runge–Kutta methods for stiff ODEs. Applied Numerical Mathematics, 146:221–244, 2019.

TS: Scalable ODE and DAE Solvers, TSDIRK, TSDIRKType, TSDIRKSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSDIRKSetType()
```

---

## TSDIRKES324SAL#

**URL:** https://petsc.org/release/manualpages/TS/TSDIRKES324SAL/

**Contents:**
- TSDIRKES324SAL#
- Options Database Key#
- References#
- See Also#
- Level#
- Location#

Third order DIRK scheme, [KC19] See TSDIRK for additional details.

-ts_dirk_type es324sal - select this method.

Christopher A Kennedy and Mark H Carpenter. Diagonally implicit Runge–Kutta methods for stiff ODEs. Applied Numerical Mathematics, 146:221–244, 2019.

TS: Scalable ODE and DAE Solvers, TSDIRK, TSDIRKType, TSDIRKSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSDIRKSetType()
```

---

## TSDIRKES325SAL#

**URL:** https://petsc.org/release/manualpages/TS/TSDIRKES325SAL/

**Contents:**
- TSDIRKES325SAL#
- Options Database Key#
- References#
- See Also#
- Level#
- Location#

Third order DIRK scheme [KC19]. See TSDIRK for additional details.

-ts_dirk_type es325sal - select this method.

Christopher A Kennedy and Mark H Carpenter. Diagonally implicit Runge–Kutta methods for stiff ODEs. Applied Numerical Mathematics, 146:221–244, 2019.

TS: Scalable ODE and DAE Solvers, TSDIRK, TSDIRKType, TSDIRKSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSDIRKSetType()
```

---

## TSDIRKES648SA#

**URL:** https://petsc.org/release/manualpages/TS/TSDIRKES648SA/

**Contents:**
- TSDIRKES648SA#
- Options Database Key#
- See Also#
- Level#
- Location#

Sixth order DIRK scheme yousefalamri55/High_Order_DIRK_Methods_Coeffs See TSDIRK for additional details.

-ts_dirk_type es648sa - select this method.

TS: Scalable ODE and DAE Solvers, TSDIRK, TSDIRKType, TSDIRKSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSDIRKSetType()
```

---

## TSDIRKES7510SA#

**URL:** https://petsc.org/release/manualpages/TS/TSDIRKES7510SA/

**Contents:**
- TSDIRKES7510SA#
- Options Database Key#
- See Also#
- Level#
- Location#

Seventh order DIRK scheme yousefalamri55/High_Order_DIRK_Methods_Coeffs See TSDIRK for additional details.

-ts_dirk_type es7510sa - select this method.

TS: Scalable ODE and DAE Solvers, TSDIRK, TSDIRKType, TSDIRKSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSDIRKSetType()
```

---

## TSDIRKES8516SAL#

**URL:** https://petsc.org/release/manualpages/TS/TSDIRKES8516SAL/

**Contents:**
- TSDIRKES8516SAL#
- Options Database Key#
- See Also#
- Level#
- Location#

Eighth order DIRK scheme yousefalamri55/High_Order_DIRK_Methods_Coeffs See TSDIRK for additional details.

-ts_dirk_type es8516sal - select this method.

TS: Scalable ODE and DAE Solvers, TSDIRK, TSDIRKType, TSDIRKSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSDIRKSetType()
```

---

## TSDIRKGetType#

**URL:** https://petsc.org/release/manualpages/TS/TSDIRKGetType/

**Contents:**
- TSDIRKGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the type of TSDIRK scheme

ts - timestepping context

dirktype - type of TSDIRK scheme

TS: Scalable ODE and DAE Solvers, TSDIRKSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSDIRKGetType(TS ts, TSDIRKType *dirktype)
```

Example 2 (unknown):
```unknown
TSDIRKSetType()
```

---

## TSDIRKRegister#

**URL:** https://petsc.org/release/manualpages/TS/TSDIRKRegister/

**Contents:**
- TSDIRKRegister#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

register a TSDIRK scheme by providing the entries in its Butcher tableau and, optionally, embedded approximations and interpolation

Logically Collective.

name - identifier for method

order - approximation order of method

s - number of stages, this is the dimension of the matrices below

At - Butcher table of stage coefficients (dimension s*s, row-major order)

bt - Butcher table for completing the step (dimension s; pass NULL to use the last row of At)

ct - Abscissa of each stage (dimension s, NULL to use row sums of At)

bembedt - Stiff part of completion table for embedded method (dimension s; NULL if not available)

pinterp - Order of the interpolation scheme, equal to the number of columns of binterpt and binterp

binterpt - Coefficients of the interpolation formula (dimension s*pinterp)

Several TSDIRK methods are provided, the use of this function is only needed to create new methods.

TS: Scalable ODE and DAE Solvers, TSDIRK, TSType, TS

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSDIRKRegister(TSDIRKType name, PetscInt order, PetscInt s, const PetscReal At[], const PetscReal bt[], const PetscReal ct[], const PetscReal bembedt[], PetscInt pinterp, const PetscReal binterpt[])
```

---

## TSDIRKS212#

**URL:** https://petsc.org/release/manualpages/TS/TSDIRKS212/

**Contents:**
- TSDIRKS212#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Second order DIRK scheme. This method has two implicit stages with an embedded method of other 1. See TSDIRK for additional details.

-ts_dirk_type s212 - select this method.

This is the default DIRK scheme in SUNDIALS.

TS: Scalable ODE and DAE Solvers, TSDIRK, TSDIRKType, TSDIRKSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSDIRKSetType()
```

---

## TSDIRKS659A#

**URL:** https://petsc.org/release/manualpages/TS/TSDIRKS659A/

**Contents:**
- TSDIRKS659A#
- Options Database Key#
- See Also#
- Level#
- Location#

Sixth order DIRK scheme yousefalamri55/High_Order_DIRK_Methods_Coeffs See TSDIRK for additional details.

-ts_dirk_type s659a - select this method.

TS: Scalable ODE and DAE Solvers, TSDIRK, TSDIRKType, TSDIRKSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSDIRKSetType()
```

---

## TSDIRKS7511SAL#

**URL:** https://petsc.org/release/manualpages/TS/TSDIRKS7511SAL/

**Contents:**
- TSDIRKS7511SAL#
- Options Database Key#
- See Also#
- Level#
- Location#

Seventh order DIRK scheme yousefalamri55/High_Order_DIRK_Methods_Coeffs See TSDIRK for additional details.

-ts_dirk_type s7511sal - select this method.

TS: Scalable ODE and DAE Solvers, TSDIRK, TSDIRKType, TSDIRKSetType()

src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSDIRKSetType()
```

---

## TSDIRKSetType#

**URL:** https://petsc.org/release/manualpages/TS/TSDIRKSetType/

**Contents:**
- TSDIRKSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

Set the type of TSDIRK scheme

ts - timestepping context

dirktype - type of TSDIRK scheme

-ts_dirkimex_type - set TSDIRK scheme type

TS: Scalable ODE and DAE Solvers, TSDIRKGetType(), TSDIRK, TSDIRKType

src/ts/impls/arkimex/arkimex.c

TSDIRKSetType_DIRK() in src/ts/impls/arkimex/arkimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSDIRKSetType(TS ts, TSDIRKType dirktype)
```

Example 2 (unknown):
```unknown
TSDIRKGetType()
```

---

## TSDIRKType#

**URL:** https://petsc.org/release/manualpages/TS/TSDIRKType/

**Contents:**
- TSDIRKType#
- Synopsis#
- See Also#
- Level#
- Location#

String with the name of a Diagonally Implicit Runge-Kutta TSDIRK type

TS: Scalable ODE and DAE Solvers, TSDIRKSetType(), TS, TSDIRK, TSDIRKRegister()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h> 
typedef const char *TSDIRKType;
#define TSDIRKS212      "s212"
#define TSDIRKES122SAL  "es122sal"
#define TSDIRKES213SAL  "es213sal"
#define TSDIRKES324SAL  "es324sal"
#define TSDIRKES325SAL  "es325sal"
#define TSDIRK657A      "657a"
#define TSDIRKES648SA   "es648sa"
#define TSDIRK658A      "658a"
#define TSDIRKS659A     "s659a"
#define TSDIRK7510SAL   "7510sal"
#define TSDIRKES7510SA  "es7510sa"
#define TSDIRK759A      "759a"
#define TSDIRKS7511SAL  "s7511sal"
#define TSDIRK8614A     "8614a"
#define TSDIRK8616SAL   "8616sal"
#define TSDIRKES8516SAL "es8516sal"
```

Example 2 (unknown):
```unknown
TSDIRKSetType()
```

Example 3 (unknown):
```unknown
TSDIRKRegister()
```

---

## TSDIRK#

**URL:** https://petsc.org/release/manualpages/TS/TSDIRK/

**Contents:**
- TSDIRK#
- Notes#
- The convention used in PETSc to name the DIRK methods is TSDIRK[E][S]PQS[SA][L][A] with#
- See Also#
- Level#
- Location#
- Examples#

ODE and DAE solver using Diagonally implicit Runge-Kutta schemes.

The default is TSDIRKES213SAL, it can be changed with TSDIRKSetType() or -ts_dirk_type.

E - whether the method has an explicit first stage

S - whether the method is single diagonal

P - order of the advancing method

Q - order of the embedded method

SA - whether the method is stiffly accurate

L - whether the method is L-stable

A - whether the method is A-stable

TS: Scalable ODE and DAE Solvers, TSCreate(), TS, TSSetType(), TSDIRKSetType(), TSDIRKGetType(), TSDIRKRegister()

src/ts/impls/arkimex/arkimex.c

src/ts/tutorials/ex30.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSDIRKES213SAL
```

Example 2 (unknown):
```unknown
TSDIRKSetType()
```

Example 3 (unknown):
```unknown
-ts_dirk_type
```

Example 4 (unknown):
```unknown
TSSetType()
```

---

## TSDiscGradGetFormulation#

**URL:** https://petsc.org/release/manualpages/TS/TSDiscGradGetFormulation/

**Contents:**
- TSDiscGradGetFormulation#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Calling sequence of Sfunc#
- Calling sequence of Ffunc#
- Calling sequence of Gfunc#
- See Also#
- Level#
- Location#

Get the construction method for S, F, and grad F from the formulation \(u_t = S \nabla F\) for TSDISCGRAD

ts - timestepping context

Sfunc - constructor for the S matrix from the formulation

Ffunc - functional F from the formulation

Gfunc - constructor for the gradient of F from the formulation

ctx - the application context

time - the current time

S - the S-matrix from the formulation

ctx - the application context

time - the current time

F - the computed function from the formulation

ctx - the application context

time - the current time

G - the gradient of the computed function from the formulation

ctx - the application context

TS: Scalable ODE and DAE Solvers, TS, TSDISCGRAD, TSDiscGradSetFormulation()

src/ts/impls/implicit/discgrad/tsdiscgrad.c

TSDiscGradGetFormulation_DiscGrad(TS ts, PetscErrorCode (**Sfunc)(TS, PetscReal, Vec, Mat, void *), PetscErrorCode (**Ffunc)(TS, PetscReal, Vec, PetscScalar *, void *), PetscErrorCode (**Gfunc)() in src/ts/impls/implicit/discgrad/tsdiscgrad.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSDiscGradGetFormulation(TS ts, PetscErrorCode (**Sfunc)(TS ts, PetscReal time, Vec u, Mat S, PetscCtx ctx), PetscErrorCode (**Ffunc)(TS ts, PetscReal time, Vec u, PetscScalar *F, PetscCtx ctx), PetscErrorCode (**Gfunc)(TS ts, PetscReal time, Vec u, Vec G, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSDiscGradSetFormulation()
```

---

## TSDiscGradGetType#

**URL:** https://petsc.org/release/manualpages/TS/TSDiscGradGetType/

**Contents:**
- TSDiscGradGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Checks for which discrete gradient to use in formulation for TSDISCGRAD

ts - timestepping context

dgtype - Discrete gradient type <none, gonzalez, average>

TS: Scalable ODE and DAE Solvers, TSDISCGRAD, TSDiscGradSetType()

src/ts/impls/implicit/discgrad/tsdiscgrad.c

TSDiscGradGetType_DiscGrad() in src/ts/impls/implicit/discgrad/tsdiscgrad.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSDiscGradGetType(TS ts, TSDGType *dgtype)
```

Example 2 (unknown):
```unknown
TSDiscGradSetType()
```

---

## TSDiscGradSetFormulation#

**URL:** https://petsc.org/release/manualpages/TS/TSDiscGradSetFormulation/

**Contents:**
- TSDiscGradSetFormulation#
- Synopsis#
- Input Parameters#
- Calling sequence of Sfunc#
- Calling sequence of Ffunc#
- Calling sequence of Gfunc#
- See Also#
- Level#
- Location#
- Implementations#

Set the construction method for S, F, and grad F from the formulation \(u_t = S(u) \nabla F(u)\) for TSDISCGRAD

ts - timestepping context

Sfunc - constructor for the S matrix from the formulation

Ffunc - functional F from the formulation

Gfunc - constructor for the gradient of F from the formulation

ctx - optional context for the functions

time - the current time

S - the S-matrix from the formulation

ctx - the application context

time - the current time

F - the computed function from the formulation

ctx - the application context

time - the current time

G - the gradient of the computed function from the formulation

ctx - the application context

TS: Scalable ODE and DAE Solvers, TSDISCGRAD, TSDiscGradGetFormulation()

src/ts/impls/implicit/discgrad/tsdiscgrad.c

TSDiscGradSetFormulation_DiscGrad(TS ts, PetscErrorCode (*Sfunc)(TS, PetscReal, Vec, Mat, void *), PetscErrorCode (*Ffunc)(TS, PetscReal, Vec, PetscScalar *, void *), PetscErrorCode (*Gfunc)() in src/ts/impls/implicit/discgrad/tsdiscgrad.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSDiscGradSetFormulation(TS ts, PetscErrorCode (*Sfunc)(TS ts, PetscReal time, Vec u, Mat S, PetscCtx ctx), PetscErrorCode (*Ffunc)(TS ts, PetscReal time, Vec u, PetscScalar *F, PetscCtx ctx), PetscErrorCode (*Gfunc)(TS ts, PetscReal time, Vec u, Vec G, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSDiscGradGetFormulation()
```

---

## TSDiscGradSetType#

**URL:** https://petsc.org/release/manualpages/TS/TSDiscGradSetType/

**Contents:**
- TSDiscGradSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Sets discrete gradient formulation.

ts - timestepping context

dgtype - Discrete gradient type <none, gonzalez, average>

-ts_discgrad_type (gonzalez|average|none) - flag to choose discrete gradient type

Without dgtype or with type none, the discrete gradients timestepper is just implicit midpoint.

TS: Scalable ODE and DAE Solvers, TSDISCGRAD, TSDGType

src/ts/impls/implicit/discgrad/tsdiscgrad.c

TSDiscGradSetType_DiscGrad() in src/ts/impls/implicit/discgrad/tsdiscgrad.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSDiscGradSetType(TS ts, TSDGType dgtype)
```

---

## TSDISCGRAD#

**URL:** https://petsc.org/release/manualpages/TS/TSDISCGRAD/

**Contents:**
- TSDISCGRAD#
- Notes#
- See Also#
- Level#
- Location#

ODE solver using the discrete gradients version of the implicit midpoint method

This is the implicit midpoint rule, with an optional term that guarantees the discrete gradient property. This timestepper applies to systems of the form \(u_t = S(u) \nabla F(u)\) where \(S(u)\) is a linear operator, and \(F\) is a functional of \(u\).

For Hamiltonian systems designed to conserve the first integral (energy), but also has the property for some systems of monotonicity in a functional.

TS: Scalable ODE and DAE Solvers, TSCreate(), TSSetType(), TS, TSType, TSDiscGradSetFormulation(), TSDiscGradGetFormulation(), TSDiscGradSetType(), TSDiscGradGetType(), TSDGType

src/ts/impls/implicit/discgrad/tsdiscgrad.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetType()
```

Example 2 (unknown):
```unknown
TSDiscGradSetFormulation()
```

Example 3 (unknown):
```unknown
TSDiscGradGetFormulation()
```

Example 4 (unknown):
```unknown
TSDiscGradSetType()
```

---

## TSDMSwarmMonitorMoments#

**URL:** https://petsc.org/release/manualpages/TS/TSDMSwarmMonitorMoments/

**Contents:**
- TSDMSwarmMonitorMoments#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Monitors the first three moments of a DMSWARM being evolved by the TS

step - current timestep

-ts_dmswarm_monitor_moments - Monitor moments of particle distribution

-ts_dmswarm_monitor_moments_interval - Interval of timesteps between monitor outputs

This requires a DMSWARM be attached to the TS.

This is not called directly by users, rather one calls TSMonitorSet(), with this function as an argument, to cause the monitor to be used during the TS integration.

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet(), TSMonitorDefault(), DMSWARM

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSDMSwarmMonitorMoments(TS ts, PetscInt step, PetscReal t, Vec U, PetscViewerAndFormat *vf)
```

Example 2 (unknown):
```unknown
TSMonitorSet()
```

Example 3 (unknown):
```unknown
TSMonitorSet()
```

Example 4 (unknown):
```unknown
TSMonitorDefault()
```

---

## TSEIMEXSetMaxRows#

**URL:** https://petsc.org/release/manualpages/TS/TSEIMEXSetMaxRows/

**Contents:**
- TSEIMEXSetMaxRows#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set the maximum number of rows for TSEIMEX schemes

ts - timestepping context

nrows - maximum number of rows

TS: Scalable ODE and DAE Solvers, TSEIMEXSetRowCol(), TSEIMEXSetOrdAdapt(), TSEIMEX

src/ts/impls/eimex/eimex.c

TSEIMEXSetMaxRows_EIMEX() in src/ts/impls/eimex/eimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSEIMEXSetMaxRows(TS ts, PetscInt nrows)
```

Example 2 (unknown):
```unknown
TSEIMEXSetRowCol()
```

Example 3 (unknown):
```unknown
TSEIMEXSetOrdAdapt()
```

---

## TSEIMEXSetOrdAdapt#

**URL:** https://petsc.org/release/manualpages/TS/TSEIMEXSetOrdAdapt/

**Contents:**
- TSEIMEXSetOrdAdapt#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set the order adaptativity for the TSEIMEX schemes

ts - timestepping context

flg - index in the T table

TS: Scalable ODE and DAE Solvers, TSEIMEXSetRowCol(), TSEIMEX

src/ts/impls/eimex/eimex.c

TSEIMEXSetOrdAdapt_EIMEX() in src/ts/impls/eimex/eimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSEIMEXSetOrdAdapt(TS ts, PetscBool flg)
```

Example 2 (unknown):
```unknown
TSEIMEXSetRowCol()
```

---

## TSEIMEXSetRowCol#

**URL:** https://petsc.org/release/manualpages/TS/TSEIMEXSetRowCol/

**Contents:**
- TSEIMEXSetRowCol#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set the number of rows and the number of columns for the tableau that represents the T solution in the TSEIMEX scheme

ts - timestepping context

TS: Scalable ODE and DAE Solvers, TSEIMEXSetMaxRows(), TSEIMEXSetOrdAdapt(), TSEIMEX

src/ts/impls/eimex/eimex.c

TSEIMEXSetRowCol_EIMEX() in src/ts/impls/eimex/eimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSEIMEXSetRowCol(TS ts, PetscInt row, PetscInt col)
```

Example 2 (unknown):
```unknown
TSEIMEXSetMaxRows()
```

Example 3 (unknown):
```unknown
TSEIMEXSetOrdAdapt()
```

---

## TSEIMEXType#

**URL:** https://petsc.org/release/manualpages/TS/TSEIMEXType/

**Contents:**
- TSEIMEXType#
- Synopsis#
- See Also#
- Level#
- Location#

String with the name of an Extrapolated IMEX TSEIMEX type

TS: Scalable ODE and DAE Solvers, TSEIMEXSetType(), TS, TSEIMEX, TSEIMEXRegister()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h> 
#define TSEIMEXType char *
```

Example 2 (unknown):
```unknown
TSEIMEXSetType()
```

Example 3 (unknown):
```unknown
TSEIMEXRegister()
```

---

## TSEIMEX#

**URL:** https://petsc.org/release/manualpages/TS/TSEIMEX/

**Contents:**
- TSEIMEX#
- Notes#
- References#
- See Also#
- Level#
- Location#

Time stepping with Extrapolated W-IMEX methods [CS10]. These methods are intended for problems with well-separated time scales, especially when a slow scale is strongly nonlinear such that it is expensive to solve with a fully implicit method. The user should provide the stiff part of the equation using TSSetIFunction() and the non-stiff part with TSSetRHSFunction().

The default is a 3-stage scheme, it can be changed with TSEIMEXSetMaxRows() or -ts_eimex_max_rows

This method currently only works with ODEs, for which the stiff part \( F(t,X,Xdot) \) has the form \( Xdot + Fhat(t,X)\).

The general system is written as

where F represents the stiff part and G represents the non-stiff part. The user should provide the stiff part of the equation using TSSetIFunction() and the non-stiff part with TSSetRHSFunction(). This method is designed to be linearly implicit on G and can use an approximate and lagged Jacobian.

Another common form for the system is

The relationship between F,G and f,g is

E.M. Constantinescu and A. Sandu. Extrapolated implicit-explicit time stepping. SIAM Journal on Scientific Computing, 31(6):4452–4477, 2010. doi:10.1137/080732833.

TS: Scalable ODE and DAE Solvers, TSCreate(), TS, TSSetType(), TSEIMEXSetMaxRows(), TSEIMEXSetRowCol(), TSEIMEXSetOrdAdapt(), TSType

src/ts/impls/eimex/eimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetIFunction()
```

Example 2 (unknown):
```unknown
TSSetRHSFunction()
```

Example 3 (unknown):
```unknown
TSEIMEXSetMaxRows()
```

Example 4 (unknown):
```unknown
TSSetRHSFunction()
```

---

## TSEquationType#

**URL:** https://petsc.org/release/manualpages/TS/TSEquationType/

**Contents:**
- TSEquationType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#
- Examples#
- Examples#

type of TS problem that is solved

TS_EQ_UNSPECIFIED - (default)

TS_EQ_EXPLICIT - {ODE and DAE index 1, 2, 3, HI} F(t,U,U_t) := M(t) U_t - G(U,t) = 0

TS_EQ_IMPLICIT - {ODE and DAE index 1, 2, 3, HI} F(t,U,U_t) = 0

TS: Scalable ODE and DAE Solvers, TS, TSGetEquationType(), TSSetEquationType()

src/ts/tutorials/ex36.c src/ts/tutorials/ex35.cxx src/ts/tutorials/ex25.c

src/ts/tutorials/ex20opt_p.c src/ts/tutorials/ex20opt_ic.c src/ts/tutorials/ex20adj.c src/ts/tutorials/ex20td.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h> 
typedef enum {
  TS_EQ_UNSPECIFIED               = -1,
  TS_EQ_EXPLICIT                  = 0,
  TS_EQ_ODE_EXPLICIT              = 1,
  TS_EQ_DAE_SEMI_EXPLICIT_INDEX1  = 100,
  TS_EQ_DAE_SEMI_EXPLICIT_INDEX2  = 200,
  TS_EQ_DAE_SEMI_EXPLICIT_INDEX3  = 300,
  TS_EQ_DAE_SEMI_EXPLICIT_INDEXHI = 500,
  TS_EQ_IMPLICIT                  = 1000,
  TS_EQ_ODE_IMPLICIT              = 1001,
  TS_EQ_DAE_IMPLICIT_INDEX1       = 1100,
  TS_EQ_DAE_IMPLICIT_INDEX2       = 1200,
  TS_EQ_DAE_IMPLICIT_INDEX3       = 1300,
  TS_EQ_DAE_IMPLICIT_INDEXHI      = 1500
} TSEquationType;
```

Example 2 (unknown):
```unknown
TS_EQ_UNSPECIFIED
```

Example 3 (unknown):
```unknown
TS_EQ_EXPLICIT
```

Example 4 (unknown):
```unknown
TS_EQ_IMPLICIT
```

---

## TSErrorWeightedENorm#

**URL:** https://petsc.org/release/manualpages/TS/TSErrorWeightedENorm/

**Contents:**
- TSErrorWeightedENorm#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

compute a weighted error norm based on supplied absolute and relative tolerances

ts - time stepping context

U - state vector, usually ts->vec_sol

Y - state vector, previous time step

wnormtype - norm type, either NORM_2 or NORM_INFINITY

norm - weighted norm, a value of 1.0 achieves a balance between absolute and relative tolerances

norma - weighted norm, a value of 1.0 means that the error meets the absolute tolerance set by the user

normr - weighted norm, a value of 1.0 means that the error meets the relative tolerance set by the user

-ts_adapt_wnormtype wnormtype - 2, INFINITY

TS: Scalable ODE and DAE Solvers, TS, VecErrorWeightedNorms(), TSErrorWeightedNorm()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSErrorWeightedENorm(TS ts, Vec E, Vec U, Vec Y, NormType wnormtype, PetscReal *norm, PetscReal *norma, PetscReal *normr)
```

Example 2 (unknown):
```unknown
NORM_INFINITY
```

Example 3 (unknown):
```unknown
VecErrorWeightedNorms()
```

Example 4 (unknown):
```unknown
TSErrorWeightedNorm()
```

---

## TSErrorWeightedNorm#

**URL:** https://petsc.org/release/manualpages/TS/TSErrorWeightedNorm/

**Contents:**
- TSErrorWeightedNorm#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

compute a weighted norm of the difference between two state vectors based on supplied absolute and relative tolerances

ts - time stepping context

U - state vector, usually ts->vec_sol

Y - state vector to be compared to U

wnormtype - norm type, either NORM_2 or NORM_INFINITY

norm - weighted norm, a value of 1.0 achieves a balance between absolute and relative tolerances

norma - weighted norm, a value of 1.0 means that the error meets the absolute tolerance set by the user

normr - weighted norm, a value of 1.0 means that the error meets the relative tolerance set by the user

-ts_adapt_wnormtype wnormtype - 2, INFINITY

TS: Scalable ODE and DAE Solvers, TS, VecErrorWeightedNorms(), TSErrorWeightedENorm()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSErrorWeightedNorm(TS ts, Vec U, Vec Y, NormType wnormtype, PetscReal *norm, PetscReal *norma, PetscReal *normr)
```

Example 2 (unknown):
```unknown
NORM_INFINITY
```

Example 3 (unknown):
```unknown
VecErrorWeightedNorms()
```

Example 4 (unknown):
```unknown
TSErrorWeightedENorm()
```

---

## TSEULER#

**URL:** https://petsc.org/release/manualpages/TS/TSEULER/

**Contents:**
- TSEULER#
- See Also#
- Level#
- Location#
- Examples#

ODE solver using the explicit forward Euler method

TS: Scalable ODE and DAE Solvers, TSCreate(), TS, TSSetType(), TSBEULER, TSType

src/ts/impls/explicit/euler/euler.c

src/ts/tutorials/ex52.c src/ts/tutorials/ex31.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetType()
```

---

## TSEvaluateStep#

**URL:** https://petsc.org/release/manualpages/TS/TSEvaluateStep/

**Contents:**
- TSEvaluateStep#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Evaluate the solution at the end of a time step with a given order of accuracy.

ts - time stepping context

order - desired order of accuracy

done - whether the step was evaluated at this order (pass NULL to generate an error if not available)

U - state at the end of the current step

This function cannot be called until all stages have been evaluated.

It is normally called by adaptive controllers before a step has been accepted and may also be called by the user after TSStep() has returned.

TS: Scalable ODE and DAE Solvers, TS, TSStep(), TSAdapt

src/ts/interface/ts.c

TSEvaluateStep_ARKIMEX() in src/ts/impls/arkimex/arkimex.c TSEvaluateStep_EIMEX() in src/ts/impls/eimex/eimex.c TSEvaluateStep_RK() in src/ts/impls/explicit/rk/rk.c TSEvaluateStep_GLEE() in src/ts/impls/glee/glee.c TSEvaluateStep_IRK() in src/ts/impls/implicit/irk/irk.c TSEvaluateStep_MPRK() in src/ts/impls/multirate/mprk.c TSEvaluateStep_MPRKSPLIT() in src/ts/impls/multirate/mprk.c TSEvaluateStep_RosW() in src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSEvaluateStep(TS ts, PetscInt order, Vec U, PetscBool *done)
```

---

## TSEvaluateWLTE#

**URL:** https://petsc.org/release/manualpages/TS/TSEvaluateWLTE/

**Contents:**
- TSEvaluateWLTE#
- Synopsis#
- Input Parameters#
- Input/Output Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Evaluate the weighted local truncation error norm at the end of a time step with a given order of accuracy.

ts - time stepping context

wnormtype - norm type, either NORM_2 or NORM_INFINITY

order - optional, desired order for the error evaluation or PETSC_DECIDE; on output, the actual order of the error evaluation

wlte - the weighted local truncation error norm

If the timestepper cannot evaluate the error in a particular step (eg. in the first step or restart steps after event handling), this routine returns wlte=-1.0 .

TS: Scalable ODE and DAE Solvers, TS, TSStep(), TSAdapt, TSErrorWeightedNorm()

src/ts/interface/ts.c

TSEvaluateWLTE_BDF() in src/ts/impls/bdf/bdf.c TSEvaluateWLTE_Alpha() in src/ts/impls/implicit/alpha/alpha1.c TSEvaluateWLTE_Alpha() in src/ts/impls/implicit/alpha/alpha2.c TSEvaluateWLTE_Theta() in src/ts/impls/implicit/theta/theta.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSEvaluateWLTE(TS ts, NormType wnormtype, PetscInt *order, PetscReal *wlte)
```

Example 2 (unknown):
```unknown
NORM_INFINITY
```

Example 3 (unknown):
```unknown
PETSC_DECIDE
```

Example 4 (unknown):
```unknown
TSErrorWeightedNorm()
```

---

## TSEventHandler#

**URL:** https://petsc.org/release/manualpages/TS/TSEventHandler/

**Contents:**
- TSEventHandler#
- Synopsis#
- Developer notes#
- a few tricky aspects of the algorithm (and the underlying reasoning) are discussed in detail below#
- of events#
- To handle such (-=unlikely=-, but possible) situations, two strategies can be considered#
- See Also#
- Level#
- Location#

the main function to perform a single iteration of event detection.

A) The ‘event->iterctr > 0’ is used as an indicator that Anderson-Bjorck refinement has started. B) If event->iterctr == 0, then justrefined_AB[i] is always false. C) The right-end quantities: ptime_right, fvalue_right[i] and fsign_right[i] are only guaranteed to be valid for event->iterctr > 0. D) If event->iterctr > 0, then event->processing is PETSC_TRUE; the opposite may not hold. E) When event->processing == PETSC_TRUE and event->iterctr == 0, the event handler iterations are complete, but the event handler continues managing the 1st and 2nd post-event steps. In this case the 1st post-event step proposed by the event handler is not checked by TSAdapt, and is always accepted (beware!). However, if the 2nd post-event step is not managed by the event handler (e.g. 1st = numerical, 2nd = PETSC_DECIDE), condition “E” does not hold, and TSAdapt may reject/adjust the 1st post-event step. F) event->side[i] may take values: 0 <=> point t is a zero-crossing for indicator function i (via vtol/dt_min criterion); -1/+1 <=> detected a bracket to the left/right of t for indicator function i; +2 <=> no brackets/zero-crossings. G) The signs event->fsign[i] (with values 0/-1/+1) are calculated for each new point. Zero sign is set if the function value is smaller than the tolerance. Besides, zero sign is enforced after marking a zero-crossing due to small bracket size criterion.

The intervals with the indicator function sign change (i.e. containing the potential zero-crossings) are called ‘brackets’. To find a zero-crossing, the algorithm first locates a bracket, and then sequentially subdivides it, generating a sequence of brackets whose length tends to zero. The bracket subdivision involves the (modified) Anderson-Bjorck method.

Apart from the comments scattered throughout the code to clarify different lines and blocks,

=Sign tracking= When a zero-crossing is found, the sign variable (event->fsign[i]) is set to zero for the current point t. This happens both for zero-crossings triggered via the vtol criterion, and those triggered via the dt_min criterion. After the event, as the TS steps forward, the current sign values are handed over to event->fsign_prev[i]. The recalculation of signs is avoided if possible: e.g. if a ‘vtol’ criterion resulted in a zero-crossing at point t, but the subsequent call to postevent() handler decreased ‘vtol’, making the indicator function no longer “close to zero” at point t, the fsign[i] will still consistently keep the zero value. This allows avoiding the erroneous duplication

E.g. consider a bracket [t0, t2], where f0 < 0, f2 > 0, which resulted in a zero-crossing t1 with f1 < 0, abs(f1) < vtol. Suppose the postevent() handler changes vtol to vtol*, such that abs(f1) > vtol*. The TS makes a step t1 -> t3, where again f1 < 0, f3 > 0, and the event handler will find a new event near t1, which is actually a duplication of the original event at t1. The duplications are avoided by NOT counting the sign progressions 0 -> +1, or 0 -> -1 as brackets. Tracking (instead of recalculating) the sign values makes this procedure work more consistently.

The sign values are however recalculated if the postevent() callback has changed the current solution vector U (such a change resets everything). The sign value is also set to zero if the dt_min criterion has triggered the event. This allows the algorithm to work consistently, irrespective of the type of criterion involved (vtol/dt_min).

=Event from min bracket= When the event handler ends up with a bracket [t0, t1] with size <= dt_min, a zero crossing is reported at t1, and never at t0. If such a bracket is discovered when TS is staying at t0, one more step forward (to t1) is necessary to mark the found event. This is the situation of revisiting t1, which is described below (see Revisiting).

Why t0 is not reported as event location? Suppose it is, and let f0 < 0, f1 > 0. Also suppose that the postevent() handler has slightly changed the solution U, so the sign at t0 is recalculated: it equals -1. As the TS steps further: t0 -> t2, with sign0 == -1, and sign2 == +1, the event handler will locate the bracket [t0, t2], eventually resolving a new event near t1, i.e. finding a duplicate event. This situation is avoided by reporting the event at t1 in the first place.

=Revisiting= When handling the situation with small bracket size, the TS solver may happen to visit the same point twice, but with different results.

E.g. originally it discovered a bracket with sign change [t0, t10], and started resolving the zero-crossing, visiting the points t1,…,t9 : t0 < t1 < … < t9 < t10. Suppose that at t9 the algorithm discovers that [t9, t10] is a bracket with the sign change it was looking for, and that |t10 - t9| is too small. So point t10 should be revisited and marked as the zero crossing (by the minimum bracket size criterion). On re-visiting t10, via the refined sequence of steps t0,…,t10, the TS solver may arrive at a solution U* different from the solution U it found at t10 originally. Hence, the indicator functions at t10 may become different, and the condition of the sign change, which existed originally, may disappear, breaking the logic of the algorithm.

[not used here] Allow the brackets with sign change to disappear during iterations. The algorithm should be able to cleanly exit the iteration and leave all the objects/variables/caches involved in a valid state.

[ADOPTED HERE!] On revisiting t10, the event handler reuses the indicator functions previously calculated for the original solution U. This U may be less precise than U*, but this trick does not allow the algorithm logic to break down. HOWEVER, the original U is not stored anywhere, it is essentially lost since the TS performed the rollback from it. On revisiting t10, the updated solution U* will inevitably be found and used everywhere EXCEPT the current indicator functions calculation, e.g. U* will be used in the postevent() handler call. Since t10 is the event location, the appropriate indicator-function-signs will be enforced to be 0 (regardless if the solution was U or U*). If the solution is then changed by the postevent(), the indicator-function-signs will be recalculated.

Whether the algorithm is revisiting a point in the current TSEventHandler() call is flagged by ‘event->revisit_right’.

Handling of discontinuities, TS, TSEvent, TSSetEventHandler()

src/ts/event/tsevent.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSEventHandler(TS ts)
```

Example 2 (unknown):
```unknown
TSSetEventHandler()
```

---

## TSEvent#

**URL:** https://petsc.org/release/manualpages/TS/TSEvent/

**Contents:**
- TSEvent#
- Note#
- See Also#
- Level#
- Location#

Abstract object to handle event detection in TS time integrator

See TSSetEventHandler() for the management of events.

Handling of discontinuities, TS, TSSetEventHandler(), TSSetPostEventStep(), TSSetPostEventSecondStep(), TSSetEventTolerances(), TSGetNumEvents()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetEventHandler()
```

Example 2 (unknown):
```unknown
TSSetEventHandler()
```

Example 3 (unknown):
```unknown
TSSetPostEventStep()
```

Example 4 (unknown):
```unknown
TSSetPostEventSecondStep()
```

---

## TSExactFinalTimeOption#

**URL:** https://petsc.org/release/manualpages/TS/TSExactFinalTimeOption/

**Contents:**
- TSExactFinalTimeOption#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#
- Examples#
- Examples#

option for handling of final time step

TS_EXACTFINALTIME_STEPOVER - Don’t do anything if requested final time is exceeded

TS_EXACTFINALTIME_INTERPOLATE - Interpolate back to final time

TS_EXACTFINALTIME_MATCHSTEP - Adapt final time step to match the final time requested

TS: Scalable ODE and DAE Solvers, TS, TSGetConvergedReason(), TSSetExactFinalTime(), TSGetExactFinalTime()

src/ml/da/tutorials/ex3.c src/ts/tutorials/ex45.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/tutorials/ex20opt_ic.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ml/da/tutorials/ex1.c src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex4.c src/ts/tutorials/ex41.c src/tao/unconstrained/tutorials/burgers_spectral.c

src/ts/tutorials/ex1.c src/ts/tutorials/ex14.c src/ts/tutorials/ex17.c src/ts/tutorials/ex51.c src/ts/tutorials/ex49.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/tutorials/ex21.c src/ts/tutorials/ex41.c src/ts/tutorials/ex22f.F90 src/ts/utils/dmplexlandau/tutorials/ex1f90.F90

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h> 
typedef enum {
  TS_EXACTFINALTIME_UNSPECIFIED = 0,
  TS_EXACTFINALTIME_STEPOVER    = 1,
  TS_EXACTFINALTIME_INTERPOLATE = 2,
  TS_EXACTFINALTIME_MATCHSTEP   = 3
} TSExactFinalTimeOption;
```

Example 2 (unknown):
```unknown
TS_EXACTFINALTIME_STEPOVER
```

Example 3 (unknown):
```unknown
TS_EXACTFINALTIME_INTERPOLATE
```

Example 4 (unknown):
```unknown
TS_EXACTFINALTIME_MATCHSTEP
```

---

## TSFinalizePackage#

**URL:** https://petsc.org/release/manualpages/TS/TSFinalizePackage/

**Contents:**
- TSFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys everything in the PETSc interface to TS. It is called from PetscFinalize().

TS: Scalable ODE and DAE Solvers, TS, PetscFinalize(), TSInitializePackage()

src/ts/interface/dlregists.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
PetscErrorCode TSFinalizePackage(void)
```

Example 3 (unknown):
```unknown
PetscFinalize()
```

Example 4 (unknown):
```unknown
TSInitializePackage()
```

---

## TSForcingFn#

**URL:** https://petsc.org/release/manualpages/TS/TSForcingFn/

**Contents:**
- TSForcingFn#
- Synopsis#
- Calling Sequence#
- Note#
- See Also#
- Level#
- Location#

A prototype of a TS forcing function evaluation function that would be passed to TSSetForcingFunction()

ts - timestep context

ctx - [optional] user-defined function context

The deprecated TSForcingFunction still works as a replacement for TSForcingFn *.

TS: Scalable ODE and DAE Solvers, TS, TSSetForcingFunction(), DMTSSetForcingFunction()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetForcingFunction()
```

Example 2 (cpp):
```cpp
#include <petscts.h> 
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode TSForcingFn(TS ts, PetscReal t, Vec f, PetscCtx ctx);
```

Example 3 (unknown):
```unknown
TSForcingFunction
```

Example 4 (unknown):
```unknown
TSForcingFn
```

---

## TSForwardCostIntegral#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSForwardCostIntegral/

**Contents:**
- TSForwardCostIntegral#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Evaluate the cost integral in the forward run.

ts - time stepping context

This function cannot be called until TSStep() has been completed.

TS: Scalable ODE and DAE Solvers, TS, TSSolve(), TSAdjointCostIntegral()

src/ts/interface/sensitivity/tssen.c

TSForwardCostIntegral_RK() in src/ts/impls/explicit/rk/rk.c TSForwardCostIntegral_Theta() in src/ts/impls/implicit/theta/theta.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSForwardCostIntegral(TS ts)
```

Example 2 (unknown):
```unknown
TSAdjointCostIntegral()
```

---

## TSForwardGetIntegralGradients#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSForwardGetIntegralGradients/

**Contents:**
- TSForwardGetIntegralGradients#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Returns the forward sensitivities of the integral term.

ts - the TS context obtained from TSCreate()

numfwdint - number of integrals

vp - the vectors containing the gradients for each integral w.r.t. parameters

TS: Scalable ODE and DAE Solvers, TSForwardSetSensitivities(), TSForwardSetIntegralGradients(), TSForwardStep()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSForwardGetIntegralGradients(TS ts, PetscInt *numfwdint, Vec *vp[])
```

Example 2 (unknown):
```unknown
TSForwardSetSensitivities()
```

Example 3 (unknown):
```unknown
TSForwardSetIntegralGradients()
```

Example 4 (unknown):
```unknown
TSForwardStep()
```

---

## TSForwardGetSensitivities#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSForwardGetSensitivities/

**Contents:**
- TSForwardGetSensitivities#
- Synopsis#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#

Returns the trajectory sensitivities

Not Collective, but Smat returned is parallel if ts is parallel

ts - the TS context obtained from TSCreate()

nump - number of parameters

Smat - sensitivities with respect to the parameters, the number of entries in these vectors is the same as the number of parameters

TS: Scalable ODE and DAE Solvers, TSForwardSetSensitivities(), TSForwardSetIntegralGradients(), TSForwardGetIntegralGradients(), TSForwardStep()

src/ts/interface/sensitivity/tssen.c

src/ts/tutorials/ex20opt_p.c src/ts/tutorials/ex20opt_ic.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSForwardGetSensitivities(TS ts, PetscInt *nump, Mat *Smat)
```

Example 2 (unknown):
```unknown
TSForwardSetSensitivities()
```

Example 3 (unknown):
```unknown
TSForwardSetIntegralGradients()
```

Example 4 (unknown):
```unknown
TSForwardGetIntegralGradients()
```

---

## TSForwardGetStages#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSForwardGetStages/

**Contents:**
- TSForwardGetStages#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Get the number of stages and the tangent linear sensitivities at the intermediate stages

ts - the TS context obtained from TSCreate()

ns - number of stages

S - tangent linear sensitivities at the intermediate stages

src/ts/interface/sensitivity/tssen.c

TSForwardGetStages_RK() in src/ts/impls/explicit/rk/rk.c TSForwardGetStages_Theta() in src/ts/impls/implicit/theta/theta.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSForwardGetStages(TS ts, PetscInt *ns, Mat **S)
```

---

## TSForwardReset#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSForwardReset/

**Contents:**
- TSForwardReset#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Reset the internal data structures used by forward sensitivity analysis

ts - the TS context obtained from TSCreate()

TS: Scalable ODE and DAE Solvers, TSCreate(), TSDestroy(), TSForwardSetUp()

src/ts/interface/sensitivity/tssen.c

TSForwardReset_RK() in src/ts/impls/explicit/rk/rk.c TSForwardReset_Theta() in src/ts/impls/implicit/theta/theta.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSForwardReset(TS ts)
```

Example 2 (unknown):
```unknown
TSDestroy()
```

Example 3 (unknown):
```unknown
TSForwardSetUp()
```

---

## TSForwardSetInitialSensitivities#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSForwardSetInitialSensitivities/

**Contents:**
- TSForwardSetInitialSensitivities#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Set initial values for tangent linear sensitivities

ts - the TS context obtained from TSCreate()

didp - parametric sensitivities of the initial condition

TSSolve() allows users to pass the initial solution directly to TS. But the tangent linear variables cannot be initialized in this way. This function is used to set initial values for tangent linear variables.

TS: Scalable ODE and DAE Solvers, TS, TSForwardSetSensitivities()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSForwardSetInitialSensitivities(TS ts, Mat didp)
```

Example 2 (unknown):
```unknown
TSForwardSetSensitivities()
```

---

## TSForwardSetIntegralGradients#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSForwardSetIntegralGradients/

**Contents:**
- TSForwardSetIntegralGradients#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the vectors holding forward sensitivities of the integral term.

ts - the TS context obtained from TSCreate()

numfwdint - number of integrals

vp - the vectors containing the gradients for each integral w.r.t. parameters

TS: Scalable ODE and DAE Solvers, TSForwardGetSensitivities(), TSForwardGetIntegralGradients(), TSForwardStep()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSForwardSetIntegralGradients(TS ts, PetscInt numfwdint, Vec vp[])
```

Example 2 (unknown):
```unknown
TSForwardGetSensitivities()
```

Example 3 (unknown):
```unknown
TSForwardGetIntegralGradients()
```

Example 4 (unknown):
```unknown
TSForwardStep()
```

---

## TSForwardSetSensitivities#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSForwardSetSensitivities/

**Contents:**
- TSForwardSetSensitivities#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the initial value of the trajectory sensitivities of solution w.r.t. the problem parameters and initial values.

ts - the TS context obtained from TSCreate()

nump - number of parameters

Smat - sensitivities with respect to the parameters, the number of entries in these vectors is the same as the number of parameters

Use PETSC_DETERMINE to use the number of columns of Smat for nump

Forward sensitivity is also called ‘trajectory sensitivity’ in some fields such as power systems. This function turns on a flag to trigger TSSolve() to compute forward sensitivities automatically. You must call this function before TSSolve(). The entries in the sensitivity matrix must be correctly initialized with the values S = dy/dp|startingtime.

TS: Scalable ODE and DAE Solvers, TSForwardGetSensitivities(), TSForwardSetIntegralGradients(), TSForwardGetIntegralGradients(), TSForwardStep()

src/ts/interface/sensitivity/tssen.c

src/ts/tutorials/ex20fwd.c src/ts/tutorials/ex23fwdadj.c src/ts/tutorials/ex16fwd.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSForwardSetSensitivities(TS ts, PetscInt nump, Mat Smat)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
TSForwardGetSensitivities()
```

Example 4 (unknown):
```unknown
TSForwardSetIntegralGradients()
```

---

## TSForwardSetUp#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSForwardSetUp/

**Contents:**
- TSForwardSetUp#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Sets up the internal data structures for the later use of forward sensitivity analysis

ts - the TS context obtained from TSCreate()

TS: Scalable ODE and DAE Solvers, TS, TSCreate(), TSDestroy(), TSSetUp()

src/ts/interface/sensitivity/tssen.c

TSForwardSetUp_RK() in src/ts/impls/explicit/rk/rk.c TSForwardSetUp_Theta() in src/ts/impls/implicit/theta/theta.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSForwardSetUp(TS ts)
```

Example 2 (unknown):
```unknown
TSDestroy()
```

---

## TSForwardStep#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSForwardStep/

**Contents:**
- TSForwardStep#
- Synopsis#
- Input Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Compute the forward sensitivity for one time step.

ts - time stepping context

This function cannot be called until TSStep() has been completed.

TS: Scalable ODE and DAE Solvers, TSForwardSetSensitivities(), TSForwardGetSensitivities(), TSForwardSetIntegralGradients(), TSForwardGetIntegralGradients(), TSForwardSetUp()

src/ts/interface/sensitivity/tssen.c

TSForwardStep_RK() in src/ts/impls/explicit/rk/rk.c TSForwardStep_Theta() in src/ts/impls/implicit/theta/theta.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSForwardStep(TS ts)
```

Example 2 (unknown):
```unknown
TSForwardSetSensitivities()
```

Example 3 (unknown):
```unknown
TSForwardGetSensitivities()
```

Example 4 (unknown):
```unknown
TSForwardSetIntegralGradients()
```

---

## TSFunctionDomainError#

**URL:** https://petsc.org/release/manualpages/TS/TSFunctionDomainError/

**Contents:**
- TSFunctionDomainError#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Checks if the current state is valid

stagetime - time of the simulation

Y - state vector to check.

accept - Set to PETSC_FALSE if the current state vector is valid.

This function is called by the TS integration routines and calls the user provided function (set with TSSetFunctionDomainError()) to check if the current state is valid.

TS: Scalable ODE and DAE Solvers, TS, TSSetFunctionDomainError()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSFunctionDomainError(TS ts, PetscReal stagetime, Vec Y, PetscBool *accept)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
TSSetFunctionDomainError()
```

Example 4 (unknown):
```unknown
TSSetFunctionDomainError()
```

---

## TSGetAdapt#

**URL:** https://petsc.org/release/manualpages/TS/TSGetAdapt/

**Contents:**
- TSGetAdapt#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Get the adaptive controller context for the current method

Collective if controller has not yet been created

ts - time stepping context

adapt - adaptive controller

TS: Scalable ODE and DAE Solvers, TS, TSAdapt, TSAdaptSetType(), TSAdaptChoose()

src/ts/interface/ts.c

src/ts/tutorials/extchem.c src/ts/tutorials/ex51.c src/ts/tutorials/ex40.c src/ts/tutorials/ex44.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/tutorials/ex53.c src/ts/tutorials/ex41.c src/ts/tutorials/extchemfield.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetAdapt(TS ts, TSAdapt *adapt)
```

Example 2 (unknown):
```unknown
TSAdaptSetType()
```

Example 3 (unknown):
```unknown
TSAdaptChoose()
```

---

## TSGetApplicationContext#

**URL:** https://petsc.org/release/manualpages/TS/TSGetApplicationContext/

**Contents:**
- TSGetApplicationContext#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Fortran Notes#
- See Also#
- Level#
- Location#
- Examples#

Gets the user-defined context for the timestepper that was set with TSSetApplicationContext()

ts - the TS context obtained from TSCreate()

ctx - a pointer to the application context

This only works when the context is a Fortran derived type or a PetscObject. Declare ctx with

TS: Scalable ODE and DAE Solvers, TS, TSSetApplicationContext()

src/ts/interface/ts.c

src/ts/tutorials/ex77.c src/ts/tutorials/ex30.c src/ts/tutorials/ex42.c src/ts/tutorials/ex48.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetApplicationContext()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetApplicationContext(TS ts, PetscCtxRt ctx)
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

## TSGetAuxSolution#

**URL:** https://petsc.org/release/manualpages/TS/TSGetAuxSolution/

**Contents:**
- TSGetAuxSolution#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Returns an auxiliary solution at the present timestep, if available for the time integration method being used.

Not Collective, but v returned is parallel if ts is parallel

ts - the TS context obtained from TSCreate() (input parameter).

v - the vector containing the auxiliary solution

TS: Scalable ODE and DAE Solvers, TS, TSGetSolution()

src/ts/interface/ts.c

TSGetAuxSolution_GLEE() in src/ts/impls/glee/glee.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetAuxSolution(TS ts, Vec *v)
```

Example 2 (unknown):
```unknown
TSGetSolution()
```

---

## TSGetCFLTime#

**URL:** https://petsc.org/release/manualpages/TS/TSGetCFLTime/

**Contents:**
- TSGetCFLTime#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the maximum stable time step according to CFL criteria applied to forward Euler

ts - time stepping context

cfltime - maximum stable time step for forward Euler

TS: Scalable ODE and DAE Solvers, TSSetCFLTimeLocal()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetCFLTime(TS ts, PetscReal *cfltime)
```

Example 2 (unknown):
```unknown
TSSetCFLTimeLocal()
```

---

## TSGetComputeExactError#

**URL:** https://petsc.org/release/manualpages/TS/TSGetComputeExactError/

**Contents:**
- TSGetComputeExactError#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Calling sequence of exactError#
- See Also#
- Level#
- Location#

Get the function used to automatically compute the exact error for the timestepping.

ts - time stepping context

exactError - The function which computes the solution error

ts - The timestepping context

u - The approximate solution vector

e - The vector in which the error is stored

TS: Scalable ODE and DAE Solvers, TS, TSComputeExactError()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetComputeExactError(TS ts, PetscErrorCode (**exactError)(TS ts, Vec u, Vec e))
```

Example 2 (unknown):
```unknown
TSComputeExactError()
```

---

## TSGetComputeInitialCondition#

**URL:** https://petsc.org/release/manualpages/TS/TSGetComputeInitialCondition/

**Contents:**
- TSGetComputeInitialCondition#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Calling sequence of initCondition#
- See Also#
- Level#
- Location#

Get the function used to automatically compute an initial condition for the timestepping.

ts - time stepping context

initCondition - The function which computes an initial condition

ts - The timestepping context

u - The input vector in which the initial condition is stored

TS: Scalable ODE and DAE Solvers, TS, TSSetComputeInitialCondition(), TSComputeInitialCondition()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetComputeInitialCondition(TS ts, PetscErrorCode (**initCondition)(TS ts, Vec u))
```

Example 2 (unknown):
```unknown
initCondition
```

Example 3 (unknown):
```unknown
TSSetComputeInitialCondition()
```

Example 4 (unknown):
```unknown
TSComputeInitialCondition()
```

---

## TSGetConvergedReason#

**URL:** https://petsc.org/release/manualpages/TS/TSGetConvergedReason/

**Contents:**
- TSGetConvergedReason#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets the reason the TS iteration was stopped.

reason - negative value indicates diverged, positive value converged, see TSConvergedReason or the manual pages for the individual convergence tests for complete lists

Can only be called after the call to TSSolve() is complete.

TS: Scalable ODE and DAE Solvers, TS, TSSolve(), TSConvergedReason

src/ts/interface/ts.c

src/ts/tutorials/extchem.c src/ts/tutorials/ex35.cxx src/ts/tutorials/ex18.c src/ts/tutorials/ex25.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/tutorials/ex48.c src/ts/utils/dmplexlandau/tutorials/ex2.c src/ts/tutorials/ex22.c src/ts/tutorials/ex26.c src/ts/tutorials/extchemfield.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetConvergedReason(TS ts, TSConvergedReason *reason)
```

Example 2 (unknown):
```unknown
TSConvergedReason
```

Example 3 (unknown):
```unknown
TSConvergedReason
```

---

## TSGetCostGradients#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSGetCostGradients/

**Contents:**
- TSGetCostGradients#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Returns the gradients from the TSAdjointSolve()

Not Collective, but the vectors returned are parallel if TS is parallel

ts - the TS context obtained from TSCreate()

numcost - size of returned arrays

lambda - vectors containing the gradients of the cost functions with respect to the ODE/DAE solution variables

mu - vectors containing the gradients of the cost functions with respect to the problem parameters

TS: Scalable ODE and DAE Solvers, TS, TSAdjointSolve(), TSSetCostGradients()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSAdjointSolve()
```

Example 2 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSGetCostGradients(TS ts, PetscInt *numcost, Vec *lambda[], Vec *mu[])
```

Example 3 (unknown):
```unknown
TSAdjointSolve()
```

Example 4 (unknown):
```unknown
TSSetCostGradients()
```

---

## TSGetCostHessianProducts#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSGetCostHessianProducts/

**Contents:**
- TSGetCostHessianProducts#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Returns the gradients from the TSAdjointSolve()

Not Collective, but vectors returned are parallel if TS is parallel

ts - the TS context obtained from TSCreate()

numcost - number of cost functions

lambda2 - Hessian-vector product with respect to the initial condition variables, the dimension and parallel layout of these vectors is the same as the ODE solution vector

mu2 - Hessian-vector product with respect to the parameters, the number of entries in these vectors is the same as the number of parameters

dir - the direction vector that are multiplied with the Hessian of the cost functions

TS: Scalable ODE and DAE Solvers, TSAdjointSolve(), TSSetCostHessianProducts()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSAdjointSolve()
```

Example 2 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSGetCostHessianProducts(TS ts, PetscInt *numcost, Vec *lambda2[], Vec *mu2[], Vec *dir)
```

Example 3 (unknown):
```unknown
TSAdjointSolve()
```

Example 4 (unknown):
```unknown
TSSetCostHessianProducts()
```

---

## TSGetCostIntegral#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSGetCostIntegral/

**Contents:**
- TSGetCostIntegral#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the values of the integral term in the cost functions. It is valid to call the routine after a backward run.

ts - the TS context obtained from TSCreate()

v - the vector containing the integrals for each cost function

TS: Scalable ODE and DAE Solvers, TS, TSAdjointSolve(), TSSetCostIntegrand()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSGetCostIntegral(TS ts, Vec *v)
```

Example 2 (unknown):
```unknown
TSAdjointSolve()
```

Example 3 (unknown):
```unknown
TSSetCostIntegrand()
```

---

## TSGetDM#

**URL:** https://petsc.org/release/manualpages/TS/TSGetDM/

**Contents:**
- TSGetDM#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Gets the DM that may be used by some preconditioners

TS: Scalable ODE and DAE Solvers, TS, DM, TSSetDM(), SNESSetDM(), SNESGetDM()

src/ts/interface/ts.c

src/ts/tutorials/ex14.c src/ts/tutorials/ex45.c src/ts/tutorials/ex9.c src/ts/tutorials/ex17.c src/ts/tutorials/ex46.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/tutorials/ex22f_mf.F90 src/ts/utils/dmplexlandau/tutorials/ex2.c src/ts/tutorials/ex47.c src/ts/tutorials/ex22f.F90

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetDM(TS ts, DM *dm)
```

Example 2 (unknown):
```unknown
SNESSetDM()
```

Example 3 (unknown):
```unknown
SNESGetDM()
```

---

## TSGetDuration#

**URL:** https://petsc.org/release/manualpages/TS/TSGetDuration/

**Contents:**
- TSGetDuration#
- Synopsis#
- Level#
- Location#

Deprecated, use TSGetMaxSteps() and TSGetMaxTime().

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGetMaxSteps()
```

Example 2 (unknown):
```unknown
TSGetMaxTime()
```

Example 3 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetDuration(TS ts, PetscInt *maxsteps, PetscReal *maxtime)
```

---

## TSGetEquationType#

**URL:** https://petsc.org/release/manualpages/TS/TSGetEquationType/

**Contents:**
- TSGetEquationType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the type of the equation that TS is solving.

equation_type - see TSEquationType

TS: Scalable ODE and DAE Solvers, TS, TSSetEquationType(), TSEquationType

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetEquationType(TS ts, TSEquationType *equation_type)
```

Example 2 (unknown):
```unknown
TSEquationType
```

Example 3 (unknown):
```unknown
TSSetEquationType()
```

Example 4 (unknown):
```unknown
TSEquationType
```

---

## TSGetEvaluationSolutions#

**URL:** https://petsc.org/release/manualpages/TS/TSGetEvaluationSolutions/

**Contents:**
- TSGetEvaluationSolutions#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Get the number of solutions and the solutions at the evaluation time points specified

ts - the TS context obtained from TSCreate()

nsol - the number of solutions

sol_times - array of solution times corresponding to the solution vectors. See note below

Sols - the solution vectors

Both nsol and Sols can be NULL.

Some time points in the evaluation points may be skipped by TS so that nsol is less than the number of points specified by TSSetEvaluationTimes(). For example, manipulating the step size, especially with a reduced precision, may cause TS to step over certain evaluation times.

Also used to see view solutions requested by TSSetTimeSpan().

TS: Scalable ODE and DAE Solvers, TS, TSSetEvaluationTimes(), TSGetEvaluationTimes()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetEvaluationSolutions(TS ts, PetscInt *nsol, const PetscReal *sol_times[], Vec *Sols[])
```

Example 2 (unknown):
```unknown
TSSetEvaluationTimes()
```

Example 3 (unknown):
```unknown
TSSetTimeSpan()
```

Example 4 (unknown):
```unknown
TSSetEvaluationTimes()
```

---

## TSGetEvaluationTimes#

**URL:** https://petsc.org/release/manualpages/TS/TSGetEvaluationTimes/

**Contents:**
- TSGetEvaluationTimes#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

gets the evaluation times set with TSSetEvaluationTimes()

ts - the time-stepper

n - number of the time points

time_points - array of the time points

The values obtained are valid until the TS object is destroyed.

Both n and time_points can be NULL.

Also used to see time points set by TSSetTimeSpan().

TS: Scalable ODE and DAE Solvers, TS, TSSetEvaluationTimes(), TSGetEvaluationSolutions()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetEvaluationTimes()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetEvaluationTimes(TS ts, PetscInt *n, const PetscReal *time_points[])
```

Example 3 (unknown):
```unknown
time_points
```

Example 4 (unknown):
```unknown
TSSetTimeSpan()
```

---

## TSGetExactFinalTime#

**URL:** https://petsc.org/release/manualpages/TS/TSGetExactFinalTime/

**Contents:**
- TSGetExactFinalTime#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the exact final time option set with TSSetExactFinalTime()

eftopt - exact final time option

TS: Scalable ODE and DAE Solvers, TS, TSExactFinalTimeOption, TSSetExactFinalTime()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetExactFinalTime()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetExactFinalTime(TS ts, TSExactFinalTimeOption *eftopt)
```

Example 3 (unknown):
```unknown
TSExactFinalTimeOption
```

Example 4 (unknown):
```unknown
TSSetExactFinalTime()
```

---

## TSGetI2Function#

**URL:** https://petsc.org/release/manualpages/TS/TSGetI2Function/

**Contents:**
- TSGetI2Function#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Returns the vector where the implicit residual is stored and the function/context to compute it.

r - vector to hold residual (or NULL)

fun - the function to compute residual (or NULL)

ctx - the function context (or NULL)

TS: Scalable ODE and DAE Solvers, TS, TSSetIFunction(), SNESGetFunction(), TSCreate()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetI2Function(TS ts, Vec *r, TSI2FunctionFn **fun, PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
TSSetIFunction()
```

Example 3 (unknown):
```unknown
SNESGetFunction()
```

---

## TSGetI2Jacobian#

**URL:** https://petsc.org/release/manualpages/TS/TSGetI2Jacobian/

**Contents:**
- TSGetI2Jacobian#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Returns the implicit Jacobian at the present timestep.

Not Collective, but parallel objects are returned if TS is parallel

ts - The TS context obtained from TSCreate()

J - The (approximate) Jacobian of F(t,U,U_t,U_tt)

P - The matrix from which the preconditioner is constructed, often the same as J

jac - The function to compute the Jacobian matrices

ctx - User-defined context for Jacobian evaluation routine

You can pass in NULL for any return argument you do not need.

TS: Scalable ODE and DAE Solvers, TS, TSGetTimeStep(), TSGetMatrices(), TSGetTime(), TSGetStepNumber(), TSSetI2Jacobian(), TSGetI2Function(), TSCreate()

src/ts/interface/ts.c

src/ts/tutorials/ex44.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetI2Jacobian(TS ts, Mat *J, Mat *P, TSI2JacobianFn **jac, PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
TSGetTimeStep()
```

Example 3 (unknown):
```unknown
TSGetMatrices()
```

Example 4 (unknown):
```unknown
TSGetTime()
```

---

## TSGetIFunction#

**URL:** https://petsc.org/release/manualpages/TS/TSGetIFunction/

**Contents:**
- TSGetIFunction#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Returns the vector where the implicit residual is stored and the function/context to compute it.

r - vector to hold residual (or NULL)

func - the function to compute residual (or NULL)

ctx - the function context (or NULL)

TS: Scalable ODE and DAE Solvers, TS, TSSetIFunction(), SNESGetFunction()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetIFunction(TS ts, Vec *r, TSIFunctionFn **func, PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
TSSetIFunction()
```

Example 3 (unknown):
```unknown
SNESGetFunction()
```

---

## TSGetIJacobianP#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSGetIJacobianP/

**Contents:**
- TSGetIJacobianP#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Calling sequence of func#
- Note#
- See Also#
- Level#
- Location#

Gets the function that computes the Jacobian of \( F\) w.r.t. the parameters \(p\) where \(F(Udot,U,p,t) = G(U,p,t) \), as well as the location to store the matrix.

ts - TS context obtained from TSCreate()

Amat - JacobianP matrix

func - the function that computes the JacobianP

ctx - [optional] function context

U - input vector (current ODE solution)

Udot - time derivative of state vector

shift - shift to apply, see the note in TSSetIJacobian()

ctx - [optional] function context

Amat has the same number of rows and the same row parallel layout as u, Amat has the same number of columns and parallel layout as p

TS: Scalable ODE and DAE Solvers, TSSetRHSJacobianP(), TS, TSSetIJacobianP(), TSGetRHSJacobianP()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSGetIJacobianP(TS ts, Mat *Amat, PetscErrorCode (**func)(TS ts, PetscReal t, Vec U, Vec Udot, PetscReal shift, Mat A, PetscCtx ctx), PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
TSSetIJacobian()
```

Example 3 (unknown):
```unknown
TSSetRHSJacobianP()
```

Example 4 (unknown):
```unknown
TSSetIJacobianP()
```

---

## TSGetIJacobian#

**URL:** https://petsc.org/release/manualpages/TS/TSGetIJacobian/

**Contents:**
- TSGetIJacobian#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Returns the implicit Jacobian at the present timestep.

Not Collective, but parallel objects are returned if ts is parallel

ts - The TS context obtained from TSCreate()

Amat - The (approximate) Jacobian of F(t,U,U_t)

Pmat - The matrix from which the preconditioner is constructed, often the same as Amat

f - The function to compute the matrices

ctx - User-defined context for Jacobian evaluation routine

You can pass in NULL for any return argument you do not need.

TS: Scalable ODE and DAE Solvers, TS, TSGetTimeStep(), TSGetRHSJacobian(), TSGetMatrices(), TSGetTime(), TSGetStepNumber()

src/ts/interface/ts.c

src/ts/tutorials/ex30.c src/ts/tutorials/ex53.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetIJacobian(TS ts, Mat *Amat, Mat *Pmat, TSIJacobianFn **f, PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
TSGetTimeStep()
```

Example 3 (unknown):
```unknown
TSGetRHSJacobian()
```

Example 4 (unknown):
```unknown
TSGetMatrices()
```

---

## TSGetKSPIterations#

**URL:** https://petsc.org/release/manualpages/TS/TSGetKSPIterations/

**Contents:**
- TSGetKSPIterations#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets the total number of linear iterations used by the time integrator.

lits - number of linear iterations

This counter is reset to zero for each successive call to TSSolve().

TS: Scalable ODE and DAE Solvers, TS, TSSolve(), TSGetSNESIterations()

src/ts/interface/ts.c

src/ts/tutorials/ex24.c src/ts/tutorials/ex8.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetKSPIterations(TS ts, PetscInt *lits)
```

Example 2 (unknown):
```unknown
TSGetSNESIterations()
```

---

## TSGetKSP#

**URL:** https://petsc.org/release/manualpages/TS/TSGetKSP/

**Contents:**
- TSGetKSP#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Returns the KSP (linear solver) associated with a TS (timestepper) context.

Not Collective, but ksp is parallel if ts is parallel

ts - the TS context obtained from TSCreate()

ksp - the nonlinear solver context

The user can then directly manipulate the KSP context to set various options, etc. Likewise, the user can then extract and manipulate the PC context as well.

TSGetKSP() does not work for integrators that do not use KSP; in this case TSGetKSP() returns NULL in ksp.

TS: Scalable ODE and DAE Solvers, TS, SNES, KSP, TSCreate(), TSSetUp(), TSSolve(), TSGetSNES()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetKSP(TS ts, KSP *ksp)
```

Example 2 (unknown):
```unknown
TSGetSNES()
```

---

## TSGetMaxSteps#

**URL:** https://petsc.org/release/manualpages/TS/TSGetMaxSteps/

**Contents:**
- TSGetMaxSteps#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Gets the maximum number of steps to use.

ts - the TS context obtained from TSCreate()

maxsteps - maximum number of steps to use

TS: Scalable ODE and DAE Solvers, TS, TSSetMaxSteps(), TSGetMaxTime(), TSSetMaxTime()

src/ts/interface/ts.c

src/ts/utils/dmplexlandau/tutorials/ex2.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetMaxSteps(TS ts, PetscInt *maxsteps)
```

Example 2 (unknown):
```unknown
TSSetMaxSteps()
```

Example 3 (unknown):
```unknown
TSGetMaxTime()
```

Example 4 (unknown):
```unknown
TSSetMaxTime()
```

---

## TSGetMaxTime#

**URL:** https://petsc.org/release/manualpages/TS/TSGetMaxTime/

**Contents:**
- TSGetMaxTime#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Gets the maximum (or final) time for timestepping.

ts - the TS context obtained from TSCreate()

maxtime - final time to step to

TS: Scalable ODE and DAE Solvers, TS, TSSetMaxTime(), TSGetMaxSteps(), TSSetMaxSteps()

src/ts/interface/ts.c

src/ts/tutorials/ex20opt_p.c src/ts/tutorials/ex19.c src/ts/tutorials/ex20.c src/ts/tutorials/ex20opt_ic.c src/ts/tutorials/ex20adj.c src/ts/tutorials/ex20fwd.c src/ts/tutorials/ex16fwd.c src/ts/tutorials/ex16.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetMaxTime(TS ts, PetscReal *maxtime)
```

Example 2 (unknown):
```unknown
TSSetMaxTime()
```

Example 3 (unknown):
```unknown
TSGetMaxSteps()
```

Example 4 (unknown):
```unknown
TSSetMaxSteps()
```

---

## TSGetNumEvents#

**URL:** https://petsc.org/release/manualpages/TS/TSGetNumEvents/

**Contents:**
- TSGetNumEvents#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the number of events defined on the given MPI process

nevents - the number of local events on each MPI process

TS: Scalable ODE and DAE Solvers, Handling of discontinuities, TSEvent, TSSetEventHandler()

src/ts/event/tsevent.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSGetNumEvents(TS ts, PetscInt *nevents)
```

Example 2 (unknown):
```unknown
TSSetEventHandler()
```

---

## TSGetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/TS/TSGetOptionsPrefix/

**Contents:**
- TSGetOptionsPrefix#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Sets the prefix used for searching for all TS options in the database.

prefix - A pointer to the prefix string used

TS: Scalable ODE and DAE Solvers, TS, TSAppendOptionsPrefix(), TSSetFromOptions()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetOptionsPrefix(TS ts, const char *prefix[])
```

Example 2 (unknown):
```unknown
TSAppendOptionsPrefix()
```

Example 3 (unknown):
```unknown
TSSetFromOptions()
```

---

## TSGetPrevTime#

**URL:** https://petsc.org/release/manualpages/TS/TSGetPrevTime/

**Contents:**
- TSGetPrevTime#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Gets the starting time of the previously completed step.

ts - the TS context obtained from TSCreate()

t - the previous time

TS: Scalable ODE and DAE Solvers, TS, TSGetTime(), TSGetSolveTime(), TSGetTimeStep()

src/ts/interface/ts.c

src/ts/tutorials/ex16fwd.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetPrevTime(TS ts, PetscReal *t)
```

Example 2 (unknown):
```unknown
TSGetTime()
```

Example 3 (unknown):
```unknown
TSGetSolveTime()
```

Example 4 (unknown):
```unknown
TSGetTimeStep()
```

---

## TSGetProblemType#

**URL:** https://petsc.org/release/manualpages/TS/TSGetProblemType/

**Contents:**
- TSGetProblemType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the type of problem to be solved.

type - One of TS_LINEAR, TS_NONLINEAR where these types refer to problems of the forms

TS: Scalable ODE and DAE Solvers, TSSetUp(), TSProblemType, TS

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetProblemType(TS ts, TSProblemType *type)
```

Example 2 (unknown):
```unknown
TS_NONLINEAR
```

Example 3 (unknown):
```unknown
M U_t = A U
         M(t) U_t = A(t) U
         F(t,U,U_t)
```

Example 4 (unknown):
```unknown
TSProblemType
```

---

## TSGetRHSFunction#

**URL:** https://petsc.org/release/manualpages/TS/TSGetRHSFunction/

**Contents:**
- TSGetRHSFunction#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#

Returns the vector where the right-hand side is stored and the function/context to compute it.

r - vector to hold computed right-hand side (or NULL)

func - the function to compute right-hand side (or NULL)

ctx - the function context (or NULL)

TS: Scalable ODE and DAE Solvers, TS, TSSetRHSFunction(), SNESGetFunction()

src/ts/interface/ts.c

src/ts/tutorials/ex77.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetRHSFunction(TS ts, Vec *r, TSRHSFunctionFn **func, PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
TSSetRHSFunction()
```

Example 3 (unknown):
```unknown
SNESGetFunction()
```

---

## TSGetRHSJacobianP#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSGetRHSJacobianP/

**Contents:**
- TSGetRHSJacobianP#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Gets the function that computes the Jacobian of \(G \) w.r.t. the parameters \(p\) where \( U_t = G(U,p,t)\), as well as the location to store the matrix.

ts - TS context obtained from TSCreate()

Amat - JacobianP matrix

ctx - [optional] function context

Amat has the same number of rows and the same row parallel layout as u, Amat has the same number of columns and parallel layout as p

TS: Scalable ODE and DAE Solvers, TSSetRHSJacobianP(), TS, TSRHSJacobianPFn

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSGetRHSJacobianP(TS ts, Mat *Amat, TSRHSJacobianPFn **func, PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
TSSetRHSJacobianP()
```

Example 3 (unknown):
```unknown
TSRHSJacobianPFn
```

---

## TSGetRHSJacobian#

**URL:** https://petsc.org/release/manualpages/TS/TSGetRHSJacobian/

**Contents:**
- TSGetRHSJacobian#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Returns the Jacobian J at the present timestep.

Not Collective, but parallel objects are returned if ts is parallel

ts - The TS context obtained from TSCreate()

Amat - The (approximate) Jacobian J of G, where U_t = G(U,t) (or NULL)

Pmat - The matrix from which the preconditioner is constructed, usually the same as Amat (or NULL)

func - Function to compute the Jacobian of the RHS (or NULL)

ctx - User-defined context for Jacobian evaluation routine (or NULL)

You can pass in NULL for any return argument you do not need.

TS: Scalable ODE and DAE Solvers, TS, TSGetTimeStep(), TSGetMatrices(), TSGetTime(), TSGetStepNumber()

src/ts/interface/ts.c

src/ts/tutorials/ex4.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetRHSJacobian(TS ts, Mat *Amat, Mat *Pmat, TSRHSJacobianFn **func, PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
TSGetTimeStep()
```

Example 3 (unknown):
```unknown
TSGetMatrices()
```

Example 4 (unknown):
```unknown
TSGetTime()
```

---

## TSGetRunSteps#

**URL:** https://petsc.org/release/manualpages/TS/TSGetRunSteps/

**Contents:**
- TSGetRunSteps#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the maximum number of steps to take in each call to TSSolve().

ts - the TS context obtained from TSCreate()

runsteps - maximum number of steps to take in each call to TSSolve.

TS: Scalable ODE and DAE Solvers, TS, TSSetRunSteps(), TSGetMaxTime(), TSSetMaxTime(), TSGetMaxSteps()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetRunSteps(TS ts, PetscInt *runsteps)
```

Example 2 (unknown):
```unknown
TSSetRunSteps()
```

Example 3 (unknown):
```unknown
TSGetMaxTime()
```

Example 4 (unknown):
```unknown
TSSetMaxTime()
```

---

## TSGetSNESFailures#

**URL:** https://petsc.org/release/manualpages/TS/TSGetSNESFailures/

**Contents:**
- TSGetSNESFailures#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets the total number of failed SNES solves in a TS

fails - number of failed nonlinear solves

This counter is reset to zero for each successive call to TSSolve().

TS: Scalable ODE and DAE Solvers, TS, TSSolve(), TSGetSNESIterations(), TSGetKSPIterations(), TSSetMaxStepRejections(), TSGetStepRejections(), TSSetMaxSNESFailures()

src/ts/interface/ts.c

src/ts/tutorials/ex8.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetSNESFailures(TS ts, PetscInt *fails)
```

Example 2 (unknown):
```unknown
TSGetSNESIterations()
```

Example 3 (unknown):
```unknown
TSGetKSPIterations()
```

Example 4 (unknown):
```unknown
TSSetMaxStepRejections()
```

---

## TSGetSNESIterations#

**URL:** https://petsc.org/release/manualpages/TS/TSGetSNESIterations/

**Contents:**
- TSGetSNESIterations#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets the total number of nonlinear iterations used by the time integrator.

nits - number of nonlinear iterations

This counter is reset to zero for each successive call to TSSolve().

TS: Scalable ODE and DAE Solvers, TS, TSSolve(), TSGetKSPIterations()

src/ts/interface/ts.c

src/ts/tutorials/ex24.c src/ts/tutorials/ex8.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetSNESIterations(TS ts, PetscInt *nits)
```

Example 2 (unknown):
```unknown
TSGetKSPIterations()
```

---

## TSGetSNES#

**URL:** https://petsc.org/release/manualpages/TS/TSGetSNES/

**Contents:**
- TSGetSNES#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Returns the SNES (nonlinear solver) associated with a TS (timestepper) context. Valid only for nonlinear problems.

Not Collective, but snes is parallel if ts is parallel

ts - the TS context obtained from TSCreate()

snes - the nonlinear solver context

The user can then directly manipulate the SNES context to set various options, etc. Likewise, the user can then extract and manipulate the KSP, and PC contexts as well.

TSGetSNES() does not work for integrators that do not use SNES; in this case TSGetSNES() returns NULL in snes.

TS: Scalable ODE and DAE Solvers, TS, SNES, TSCreate(), TSSetUp(), TSSolve()

src/ts/interface/ts.c

src/ts/tutorials/ex14.c src/ts/tutorials/ex17.c src/ts/tutorials/ex4.c src/ts/tutorials/ex15.c src/ts/tutorials/ex22.c src/ts/tutorials/ex12.c src/ts/tutorials/ex10.c src/ts/tutorials/ex47.c src/ts/tutorials/ex22f.F90 src/ts/utils/dmplexlandau/tutorials/ex1f90.F90

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetSNES(TS ts, SNES *snes)
```

Example 2 (unknown):
```unknown
TSGetSNES()
```

Example 3 (unknown):
```unknown
TSGetSNES()
```

---

## TSGetSolutionComponents#

**URL:** https://petsc.org/release/manualpages/TS/TSGetSolutionComponents/

**Contents:**
- TSGetSolutionComponents#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Returns any solution components at the present timestep, if available for the time integration method being used. Solution components are quantities that share the same size and structure as the solution vector.

Not Collective, but v returned is parallel if ts is parallel

ts - the TS context obtained from TSCreate() (input parameter).

n - If v is NULL, then the number of solution components is returned through n, else the n-th solution component is returned in v.

v - the vector containing the n-th solution component (may be NULL to use this function to find out the number of solutions components).

TS: Scalable ODE and DAE Solvers, TS, TSGetSolution()

src/ts/interface/ts.c

TSGetSolutionComponents_GLEE() in src/ts/impls/glee/glee.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetSolutionComponents(TS ts, PetscInt *n, Vec *v)
```

Example 2 (unknown):
```unknown
TSGetSolution()
```

---

## TSGetSolution#

**URL:** https://petsc.org/release/manualpages/TS/TSGetSolution/

**Contents:**
- TSGetSolution#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Returns the solution at the present timestep. It is valid to call this routine inside the function that you are evaluating in order to move to the new timestep. This vector not changed until the solution at the next timestep has been calculated.

Not Collective, but v returned is parallel if ts is parallel

ts - the TS context obtained from TSCreate()

v - the vector containing the solution

If you used TSSetExactFinalTime(ts,TS_EXACTFINALTIME_MATCHSTEP); this does not return the solution at the requested final time. It returns the solution at the next timestep.

TS: Scalable ODE and DAE Solvers, TS, TSGetTimeStep(), TSGetTime(), TSGetSolveTime(), TSGetSolutionComponents(), TSSetSolutionFunction()

src/ts/interface/ts.c

src/ts/tutorials/ex14.c src/ts/tutorials/ex45.c src/ts/tutorials/ex30.c src/ts/tutorials/ex76.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/tutorials/ex48.c src/ts/tutorials/ex77.c src/ts/tutorials/ex53.c src/ts/utils/dmplexlandau/tutorials/ex2.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetSolution(TS ts, Vec *v)
```

Example 2 (unknown):
```unknown
TSSetExactFinalTime
```

Example 3 (unknown):
```unknown
TS_EXACTFINALTIME_MATCHSTEP
```

Example 4 (unknown):
```unknown
TSGetTimeStep()
```

---

## TSGetSolveTime#

**URL:** https://petsc.org/release/manualpages/TS/TSGetSolveTime/

**Contents:**
- TSGetSolveTime#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets the time after a call to TSSolve()

ftime - the final time. This time corresponds to the final time set with TSSetMaxTime()

Can only be called after the call to TSSolve() is complete.

TS: Scalable ODE and DAE Solvers, TS, TSSolve(), TSConvergedReason

src/ts/interface/ts.c

src/ts/tutorials/ex1.c src/ts/tutorials/ex14.c src/ts/tutorials/ex74.c src/ts/tutorials/extchem.c src/ts/tutorials/ex49.c src/ts/tutorials/ex18.c src/ts/tutorials/ex4.c src/ts/tutorials/ex8.c src/ts/tutorials/ex16fwd.c src/ts/tutorials/ex12.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetSolveTime(TS ts, PetscReal *ftime)
```

Example 2 (unknown):
```unknown
TSSetMaxTime()
```

Example 3 (unknown):
```unknown
TSConvergedReason
```

---

## TSGetStages#

**URL:** https://petsc.org/release/manualpages/TS/TSGetStages/

**Contents:**
- TSGetStages#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Get the number of stages and stage values

ts - the TS context obtained from TSCreate()

ns - the number of stages

Y - the current stage vectors

Both ns and Y can be NULL.

TS: Scalable ODE and DAE Solvers, TS, TSCreate()

src/ts/interface/ts.c

TSGetStages_ARKIMEX() in src/ts/impls/arkimex/arkimex.c TSGetStages_RK() in src/ts/impls/explicit/rk/rk.c TSGetStages_GLEE() in src/ts/impls/glee/glee.c TSGetStages_DiscGrad() in src/ts/impls/implicit/discgrad/tsdiscgrad.c TSGetStages_Theta() in src/ts/impls/implicit/theta/theta.c TSGetStages_MPRK() in src/ts/impls/multirate/mprk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetStages(TS ts, PetscInt *ns, Vec **Y)
```

---

## TSGetStepNumber#

**URL:** https://petsc.org/release/manualpages/TS/TSGetStepNumber/

**Contents:**
- TSGetStepNumber#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Gets the number of time steps completed.

ts - the TS context obtained from TSCreate()

steps - number of steps completed so far

TS: Scalable ODE and DAE Solvers, TS, TSGetTime(), TSGetTimeStep(), TSSetPreStep(), TSSetPreStage(), TSSetPostStage(), TSSetPostStep()

src/ts/interface/ts.c

src/ts/tutorials/ex1.c src/ts/tutorials/ex14.c src/ts/tutorials/ex17.c src/ts/tutorials/extchem.c src/ts/tutorials/ex49.c src/ts/tutorials/ex18.c src/ts/tutorials/ex8.c src/ts/utils/dmplexlandau/tutorials/ex2.c src/ts/tutorials/ex16fwd.c src/ts/tutorials/ex12.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetStepNumber(TS ts, PetscInt *steps)
```

Example 2 (unknown):
```unknown
TSGetTime()
```

Example 3 (unknown):
```unknown
TSGetTimeStep()
```

Example 4 (unknown):
```unknown
TSSetPreStep()
```

---

## TSGetStepRejections#

**URL:** https://petsc.org/release/manualpages/TS/TSGetStepRejections/

**Contents:**
- TSGetStepRejections#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets the total number of rejected steps.

rejects - number of steps rejected

This counter is reset to zero for each successive call to TSSolve().

TS: Scalable ODE and DAE Solvers, TS, TSSolve(), TSGetSNESIterations(), TSGetKSPIterations(), TSSetMaxStepRejections(), TSGetSNESFailures(), TSSetMaxSNESFailures(), TSSetErrorIfStepFails()

src/ts/interface/ts.c

src/ts/tutorials/ex8.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetStepRejections(TS ts, PetscInt *rejects)
```

Example 2 (unknown):
```unknown
TSGetSNESIterations()
```

Example 3 (unknown):
```unknown
TSGetKSPIterations()
```

Example 4 (unknown):
```unknown
TSSetMaxStepRejections()
```

---

## TSGetStepResize#

**URL:** https://petsc.org/release/manualpages/TS/TSGetStepResize/

**Contents:**
- TSGetStepResize#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the internal flag indicating if the current step is after a resize.

ts - the TS context obtained from TSCreate()

flg - the resize flag

TS: Scalable ODE and DAE Solvers, TS, TSCreate(), TSSetResize()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetStepResize(TS ts, PetscBool *flg)
```

Example 2 (unknown):
```unknown
TSSetResize()
```

---

## TSGetStepRollBack#

**URL:** https://petsc.org/release/manualpages/TS/TSGetStepRollBack/

**Contents:**
- TSGetStepRollBack#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Get the internal flag indicating if you are rolling back a step

ts - the TS context obtained from TSCreate()

flg - the rollback flag

TS: Scalable ODE and DAE Solvers, TS, TSCreate(), TSRollBack()

src/ts/interface/ts.c

src/ts/tutorials/ex11.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetStepRollBack(TS ts, PetscBool *flg)
```

Example 2 (unknown):
```unknown
TSRollBack()
```

---

## TSGetTimeError#

**URL:** https://petsc.org/release/manualpages/TS/TSGetTimeError/

**Contents:**
- TSGetTimeError#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Returns the estimated error vector, if the chosen TSType has an error estimation functionality and TSSetTimeError() was called

Not Collective, but v returned is parallel if ts is parallel

ts - the TS context obtained from TSCreate() (input parameter).

n - current estimate (n=0) or previous one (n=-1)

v - the vector containing the error (same size as the solution).

MUST call after TSSetUp()

TS: Scalable ODE and DAE Solvers, TSGetSolution(), TSSetTimeError()

src/ts/interface/ts.c

src/ts/tutorials/ex31.c

TSGetTimeError_GLEE() in src/ts/impls/glee/glee.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetTimeError()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetTimeError(TS ts, PetscInt n, Vec *v)
```

Example 3 (unknown):
```unknown
TSGetSolution()
```

Example 4 (unknown):
```unknown
TSSetTimeError()
```

---

## TSGetTimeSpanSolutions#

**URL:** https://petsc.org/release/manualpages/TS/TSGetTimeSpanSolutions/

**Contents:**
- TSGetTimeSpanSolutions#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Get the number of solutions and the solutions at the time points specified by the time span.

ts - the TS context obtained from TSCreate()

nsol - the number of solutions

Sols - the solution vectors

Deprecated, use TSGetEvaluationSolutions().

Both nsol and Sols can be NULL.

Some time points in the time span may be skipped by TS so that nsol is less than the number of points specified by TSSetTimeSpan(). For example, manipulating the step size, especially with a reduced precision, may cause TS to step over certain points in the span. This issue is alleviated in TSGetEvaluationSolutions() by returning the solution times that Sols were recorded at.

TS: Scalable ODE and DAE Solvers, TS, TSGetEvaluationSolutions(), TSSetTimeSpan(), TSGetEvaluationTimes(), TSSetEvaluationTimes()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h> 
PETSC_DEPRECATED_FUNCTION(3, 23, 0, "TSGetEvaluationSolutions()", ) static inline PetscErrorCode TSGetTimeSpanSolutions(TS ts, PetscInt *nsol, Vec **Sols)
```

Example 2 (unknown):
```unknown
TSGetEvaluationSolutions()
```

Example 3 (unknown):
```unknown
TSSetTimeSpan()
```

Example 4 (unknown):
```unknown
TSGetEvaluationSolutions()
```

---

## TSGetTimeSpan#

**URL:** https://petsc.org/release/manualpages/TS/TSGetTimeSpan/

**Contents:**
- TSGetTimeSpan#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

gets the time span set with TSSetTimeSpan()

ts - the time-stepper

n - number of the time points (>=2)

span_times - array of the time points. The first element and the last element are the initial time and the final time respectively.

Deprecated, use TSGetEvaluationTimes().

The values obtained are valid until the TS object is destroyed.

Both n and span_times can be NULL.

TS: Scalable ODE and DAE Solvers, TS, TSGetEvaluationTimes(), TSSetTimeSpan(), TSSetEvaluationTimes(), TSGetEvaluationSolutions()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetTimeSpan()
```

Example 2 (cpp):
```cpp
#include <petscts.h> 
PETSC_DEPRECATED_FUNCTION(3, 23, 0, "TSGetEvaluationTimes()", ) static inline PetscErrorCode TSGetTimeSpan(TS ts, PetscInt *n, const PetscReal *span_times[])
```

Example 3 (unknown):
```unknown
TSGetEvaluationTimes()
```

Example 4 (unknown):
```unknown
TSGetEvaluationTimes()
```

---

## TSGetTimeStepNumber#

**URL:** https://petsc.org/release/manualpages/TS/TSGetTimeStepNumber/

**Contents:**
- TSGetTimeStepNumber#
- Synopsis#
- Level#
- Location#

Deprecated, use TSGetStepNumber().

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGetStepNumber()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetTimeStepNumber(TS ts, PetscInt *steps)
```

---

## TSGetTimeStep#

**URL:** https://petsc.org/release/manualpages/TS/TSGetTimeStep/

**Contents:**
- TSGetTimeStep#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Gets the current timestep size.

ts - the TS context obtained from TSCreate()

dt - the current timestep size

TS: Scalable ODE and DAE Solvers, TS, TSSetTimeStep(), TSGetTime()

src/ts/interface/ts.c

src/ts/tutorials/ex9.c src/ts/tutorials/ex20opt_p.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/tutorials/ex20opt_ic.c src/ts/tutorials/ex8.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/tutorials/ex6.c src/ts/utils/dmplexlandau/tutorials/ex2.c src/ts/tutorials/ex16fwd.c src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetTimeStep(TS ts, PetscReal *dt)
```

Example 2 (unknown):
```unknown
TSSetTimeStep()
```

Example 3 (unknown):
```unknown
TSGetTime()
```

---

## TSGetTime#

**URL:** https://petsc.org/release/manualpages/TS/TSGetTime/

**Contents:**
- TSGetTime#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets the time of the most recently completed step.

ts - the TS context obtained from TSCreate()

t - the current time. This time may not corresponds to the final time set with TSSetMaxTime(), use TSGetSolveTime().

When called during time step evaluation (e.g. during residual evaluation or via hooks set using TSSetPreStep(), TSSetPreStage(), TSSetPostStage(), or TSSetPostStep()), the time is the time at the start of the step being evaluated.

TS: Scalable ODE and DAE Solvers, TS, TSGetSolveTime(), TSSetTime(), TSGetTimeStep(), TSGetStepNumber()

src/ts/interface/ts.c

src/ts/tutorials/ex45.c src/ts/tutorials/ex9.c src/ts/tutorials/ex17.c src/ts/tutorials/ex51.c src/ts/tutorials/ex18.c src/ts/tutorials/ex40.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/utils/dmplexlandau/tutorials/ex2.c src/ts/tutorials/ex41.c src/ts/utils/dmplexlandau/tutorials/ex1f90.F90

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetTime(TS ts, PetscReal *t)
```

Example 2 (unknown):
```unknown
TSSetMaxTime()
```

Example 3 (unknown):
```unknown
TSGetSolveTime()
```

Example 4 (unknown):
```unknown
TSSetPreStep()
```

---

## TSGetTolerances#

**URL:** https://petsc.org/release/manualpages/TS/TSGetTolerances/

**Contents:**
- TSGetTolerances#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#

Get tolerances for local truncation error when using adaptive controller

ts - time integration context

atol - scalar absolute tolerances, NULL to ignore

vatol - vector of absolute tolerances, NULL to ignore

rtol - scalar relative tolerances, NULL to ignore

vrtol - vector of relative tolerances, NULL to ignore

TS: Scalable ODE and DAE Solvers, TS, TSAdapt, TSErrorWeightedNorm(), TSSetTolerances()

src/ts/interface/ts.c

src/ts/tutorials/ex30.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetTolerances(TS ts, PetscReal *atol, Vec *vatol, PetscReal *rtol, Vec *vrtol)
```

Example 2 (unknown):
```unknown
TSErrorWeightedNorm()
```

Example 3 (unknown):
```unknown
TSSetTolerances()
```

---

## TSGetTotalSteps#

**URL:** https://petsc.org/release/manualpages/TS/TSGetTotalSteps/

**Contents:**
- TSGetTotalSteps#
- Synopsis#
- Level#
- Location#

Deprecated, use TSGetStepNumber().

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGetStepNumber()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetTotalSteps(TS ts, PetscInt *steps)
```

---

## TSGetTrajectory#

**URL:** https://petsc.org/release/manualpages/TS/TSGetTrajectory/

**Contents:**
- TSGetTrajectory#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets the trajectory from a TS if it exists

ts - the TS context obtained from TSCreate()

tr - the TSTrajectory object, if it exists

This routine should be called after all TS options have been set

TS: Scalable ODE and DAE Solvers, TS, TSTrajectory, TSAdjointSolve(), TSTrajectoryCreate()

src/ts/interface/ts.c

src/ts/tutorials/ex41.c src/ts/tutorials/extchem.c src/ts/tutorials/ex40.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetTrajectory(TS ts, TSTrajectory *tr)
```

Example 2 (unknown):
```unknown
TSTrajectory
```

Example 3 (unknown):
```unknown
TSTrajectory
```

Example 4 (unknown):
```unknown
TSAdjointSolve()
```

---

## TSGetType#

**URL:** https://petsc.org/release/manualpages/TS/TSGetType/

**Contents:**
- TSGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets the TS method type (as a string) that is being used to solve the ODE with the given TS

type should not be retained for later use as it will be an invalid pointer if the TSType of ts is changed.

TS: Scalable ODE and DAE Solvers, TS, TSType, TSSetType(), PetscObjectTypeCompare(), PetscObjectTypeCompareAny()

src/ts/interface/tsreg.c

src/ts/tutorials/ex31.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetType(TS ts, TSType *type)
```

Example 2 (unknown):
```unknown
TSSetType()
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

## TSGetUseSplitRHSFunction#

**URL:** https://petsc.org/release/manualpages/TS/TSGetUseSplitRHSFunction/

**Contents:**
- TSGetUseSplitRHSFunction#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets whether to use the split RHSFunction when a multirate method is used.

ts - timestepping context

use_splitrhsfunction - PETSC_TRUE indicates that the split RHSFunction will be used

TS: Scalable ODE and DAE Solvers, TS, TSSetUseSplitRHSFunction()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSGetUseSplitRHSFunction(TS ts, PetscBool *use_splitrhsfunction)
```

Example 2 (unknown):
```unknown
TSSetUseSplitRHSFunction()
```

---

## TSGLEE23#

**URL:** https://petsc.org/release/manualpages/TS/TSGLEE23/

**Contents:**
- TSGLEE23#
- See Also#
- Level#
- Location#

Second order three stage explicit GLEE method This method has three stages. s = 3, r = 2

TS: Scalable ODE and DAE Solvers, TSGLEE

src/ts/impls/glee/glee.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

---

## TSGLEE24#

**URL:** https://petsc.org/release/manualpages/TS/TSGLEE24/

**Contents:**
- TSGLEE24#
- See Also#
- Level#
- Location#

Second order four stage explicit GLEE method This method has four stages. s = 4, r = 2

TS: Scalable ODE and DAE Solvers, TSGLEE

src/ts/impls/glee/glee.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

---

## TSGLEE25i#

**URL:** https://petsc.org/release/manualpages/TS/TSGLEE25i/

**Contents:**
- TSGLEE25i#
- See Also#
- Level#
- Location#

Second order five stage explicit GLEE method This method has five stages. s = 5, r = 2

TS: Scalable ODE and DAE Solvers, TSGLEE

src/ts/impls/glee/glee.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

---

## TSGLEE35#

**URL:** https://petsc.org/release/manualpages/TS/TSGLEE35/

**Contents:**
- TSGLEE35#
- See Also#
- Level#
- Location#

Third order five stage explicit GLEE method This method has five stages. s = 5, r = 2

TS: Scalable ODE and DAE Solvers, TSGLEE

src/ts/impls/glee/glee.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

---

## TSGLEEEXRK2A#

**URL:** https://petsc.org/release/manualpages/TS/TSGLEEEXRK2A/

**Contents:**
- TSGLEEEXRK2A#
- See Also#
- Level#
- Location#

Second order six stage explicit GLEE method This method has six stages. s = 6, r = 2

TS: Scalable ODE and DAE Solvers, TSGLEE

src/ts/impls/glee/glee.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

---

## TSGLEEFinalizePackage#

**URL:** https://petsc.org/release/manualpages/TS/TSGLEEFinalizePackage/

**Contents:**
- TSGLEEFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys everything in the TSGLEE package. It is called from PetscFinalize().

TS: Scalable ODE and DAE Solvers, PetscFinalize()

src/ts/impls/glee/glee.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSGLEEFinalizePackage(void)
```

Example 3 (unknown):
```unknown
PetscFinalize()
```

---

## TSGLEEGetType#

**URL:** https://petsc.org/release/manualpages/TS/TSGLEEGetType/

**Contents:**
- TSGLEEGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get the type of TSGLEE scheme

ts - timestepping context

gleetype - type of TSGLEE scheme

TS: Scalable ODE and DAE Solvers, TSGLEE, TSGLEESetType()

src/ts/impls/glee/glee.c

TSGLEEGetType_GLEE() in src/ts/impls/glee/glee.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSGLEEGetType(TS ts, TSGLEEType *gleetype)
```

Example 2 (unknown):
```unknown
TSGLEESetType()
```

---

## TSGLEEi1#

**URL:** https://petsc.org/release/manualpages/TS/TSGLEEi1/

**Contents:**
- TSGLEEi1#
- See Also#
- Level#
- Location#

Second order three stage implicit GLEE method This method has two stages. s = 3, r = 2

TS: Scalable ODE and DAE Solvers, TSGLEE

src/ts/impls/glee/glee.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

---

## TSGLEEInitializePackage#

**URL:** https://petsc.org/release/manualpages/TS/TSGLEEInitializePackage/

**Contents:**
- TSGLEEInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function initializes everything in the TSGLEE package. It is called from TSInitializePackage().

TS: Scalable ODE and DAE Solvers, PetscInitialize()

src/ts/impls/glee/glee.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSInitializePackage()
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSGLEEInitializePackage(void)
```

Example 3 (unknown):
```unknown
PetscInitialize()
```

---

## TSGLEEMode#

**URL:** https://petsc.org/release/manualpages/TS/TSGLEEMode/

**Contents:**
- TSGLEEMode#
- Synopsis#
- See Also#
- Level#
- Location#

String with the mode of error estimation for a General Linear with Error Estimation TSGLEE type

TS: Scalable ODE and DAE Solvers, TSGLEESetMode(), TS, TSGLEE, TSGLEERegister()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h> 
PETSC_EXTERN PetscErrorCode TSGLEEGetType(TS, TSGLEEType *);
PETSC_EXTERN PetscErrorCode TSGLEESetType(TS, TSGLEEType);
PETSC_EXTERN PetscErrorCode TSGLEERegister(TSGLEEType, PetscInt, PetscInt, PetscInt, PetscReal, const PetscReal[], const PetscReal[], const PetscReal[], const PetscReal[], const PetscReal[], const PetscReal[], const PetscReal[], const PetscReal[], const PetscReal[], const PetscReal[], PetscInt, const PetscReal[]);
PETSC_EXTERN PetscErrorCode TSGLEERegisterAll(void);
PETSC_EXTERN PetscErrorCode TSGLEEFinalizePackage(void);
PETSC_EXTERN PetscErrorCode TSGLEEInitializePackage(void);
PETSC_EXTERN PetscErrorCode TSGLEERegisterDestroy(void);
```

Example 2 (unknown):
```unknown
TSGLEESetMode()
```

Example 3 (unknown):
```unknown
TSGLEERegister()
```

---

## TSGLEERegisterAll#

**URL:** https://petsc.org/release/manualpages/TS/TSGLEERegisterAll/

**Contents:**
- TSGLEERegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the General Linear with Error Estimation methods in TSGLEE

Not Collective, but should be called by all processes which will need the schemes to be registered

TS: Scalable ODE and DAE Solvers, TSGLEERegisterDestroy()

src/ts/impls/glee/glee.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSGLEERegisterAll(void)
```

Example 2 (unknown):
```unknown
TSGLEERegisterDestroy()
```

---

## TSGLEERegisterDestroy#

**URL:** https://petsc.org/release/manualpages/TS/TSGLEERegisterDestroy/

**Contents:**
- TSGLEERegisterDestroy#
- Synopsis#
- See Also#
- Level#
- Location#

Frees the list of schemes that were registered by TSGLEERegister().

TS: Scalable ODE and DAE Solvers, TSGLEERegister(), TSGLEERegisterAll()

src/ts/impls/glee/glee.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGLEERegister()
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSGLEERegisterDestroy(void)
```

Example 3 (unknown):
```unknown
TSGLEERegister()
```

Example 4 (unknown):
```unknown
TSGLEERegisterAll()
```

---

## TSGLEERegister#

**URL:** https://petsc.org/release/manualpages/TS/TSGLEERegister/

**Contents:**
- TSGLEERegister#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

register a new TSGLEE scheme by providing the entries in the Butcher tableau

Not Collective, but the same schemes should be registered on all processes on which they will be used, No Fortran Support

name - identifier for method

order - order of method

A - stage coefficients (dimension s*s, row-major)

B - step completion coefficients (dimension r*s, row-major)

U - method coefficients (dimension s*r, row-major)

V - method coefficients (dimension r*r, row-major)

S - starting coefficients

F - finishing coefficients

c - abscissa (dimension s; NULL to use row sums of A)

Fembed - step completion coefficients for embedded method

Ferror - error computation coefficients

Serror - error initialization coefficients

pinterp - order of interpolation (0 if unavailable)

binterp - array of interpolation coefficients (NULL if unavailable)

Several TSGLEE methods are provided, this function is only needed to create new methods.

TS: Scalable ODE and DAE Solvers, TSGLEE

src/ts/impls/glee/glee.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSGLEERegister(TSGLEEType name, PetscInt order, PetscInt s, PetscInt r, PetscReal gamma, const PetscReal A[], const PetscReal B[], const PetscReal U[], const PetscReal V[], const PetscReal S[], const PetscReal F[], const PetscReal c[], const PetscReal Fembed[], const PetscReal Ferror[], const PetscReal Serror[], PetscInt pinterp, const PetscReal binterp[])
```

---

## TSGLEERK285EX#

**URL:** https://petsc.org/release/manualpages/TS/TSGLEERK285EX/

**Contents:**
- TSGLEERK285EX#
- See Also#
- Level#
- Location#

Second order nine stage explicit GLEE method This method has nine stages. s = 9, r = 2

TS: Scalable ODE and DAE Solvers, TSGLEE

src/ts/impls/glee/glee.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

---

## TSGLEERK32G1#

**URL:** https://petsc.org/release/manualpages/TS/TSGLEERK32G1/

**Contents:**
- TSGLEERK32G1#
- See Also#
- Level#
- Location#

Third order eight stage explicit GLEE method This method has eight stages. s = 8, r = 2

TS: Scalable ODE and DAE Solvers, TSGLEE

src/ts/impls/glee/glee.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

---

## TSGLEESetType#

**URL:** https://petsc.org/release/manualpages/TS/TSGLEESetType/

**Contents:**
- TSGLEESetType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set the type of TSGLEE scheme

ts - timestepping context

gleetype - type of TSGLEE scheme

TS: Scalable ODE and DAE Solvers, TSGLEEGetType(), TSGLEE

src/ts/impls/glee/glee.c

TSGLEESetType_GLEE() in src/ts/impls/glee/glee.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSGLEESetType(TS ts, TSGLEEType gleetype)
```

Example 2 (unknown):
```unknown
TSGLEEGetType()
```

---

## TSGLEEType#

**URL:** https://petsc.org/release/manualpages/TS/TSGLEEType/

**Contents:**
- TSGLEEType#
- Synopsis#
- See Also#
- Level#
- Location#

String with the name of a General Linear with Error Estimation TSGLEE type

TS: Scalable ODE and DAE Solvers, TSGLEESetType(), TS, TSGLEE, TSGLEERegister()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h> 
typedef const char *TSGLEEType;
#define TSGLEEi1      "BE1"
#define TSGLEE23      "23"
#define TSGLEE24      "24"
#define TSGLEE25I     "25i"
#define TSGLEE35      "35"
#define TSGLEEEXRK2A  "exrk2a"
#define TSGLEERK32G1  "rk32g1"
#define TSGLEERK285EX "rk285ex"
```

Example 2 (unknown):
```unknown
TSGLEESetType()
```

Example 3 (unknown):
```unknown
TSGLEERegister()
```

---

## TSGLEE#

**URL:** https://petsc.org/release/manualpages/TS/TSGLEE/

**Contents:**
- TSGLEE#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

ODE and DAE solver using General Linear with Error Estimation schemes The user should provide the right-hand side of the equation using TSSetRHSFunction() and for TSGLEEi1 the Jacobian of the right-hand side using TSSetRHSJacobian()

The default is TSGLEE35, it can be changed with TSGLEESetType() or -ts_glee_type type

The only implicit scheme is TSGLEEi1

TS: Scalable ODE and DAE Solvers, GLEE methods, TSCreate(), TS, TSSetType(), TSGLEESetType(), TSGLEEGetType(), TSGLEE23, TSGLEE24, TSGLEE35, TSGLEE25I, TSGLEEEXRK2A, TSGLEERK32G1, TSGLEERK285EX, TSGLEEType, TSGLEERegister(), TSType

src/ts/impls/glee/glee.c

src/ts/tutorials/ex31.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetRHSFunction()
```

Example 2 (unknown):
```unknown
TSSetRHSJacobian()
```

Example 3 (unknown):
```unknown
TSGLEESetType()
```

Example 4 (unknown):
```unknown
-ts_glee_type type
```

---

## TSGLLEAcceptFn#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLEAcceptFn/

**Contents:**
- TSGLLEAcceptFn#
- Synopsis#
- Calling Sequence#
- Note#
- See Also#
- Level#
- Location#

A prototype of a TS accept function that would be passed to TSGLLEAcceptRegister()

ts - timestep context

nt - time to end of solution time

h - the proposed step-size

accept - output, if the proposal is accepted

The deprecated TSGLLEAcceptFunction still works as a replacement for TSGLLEAcceptFn *

TS: Scalable ODE and DAE Solvers, TS, TSSetRHSFunction(), DMTSSetRHSFunction(), TSIFunctionFn, TSIJacobianFn, TSRHSJacobianFn, TSGLLEAcceptRegister()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGLLEAcceptRegister()
```

Example 2 (cpp):
```cpp
#include <petscts.h> 
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode TSGLLEAcceptFn(TS ts, PetscReal nt, PetscReal h, const PetscReal enorm[], PetscBool *accept);
```

Example 3 (unknown):
```unknown
TSGLLEAcceptFunction
```

Example 4 (unknown):
```unknown
TSGLLEAcceptFn
```

---

## TSGLLEAcceptRegister#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLEAcceptRegister/

**Contents:**
- TSGLLEAcceptRegister#
- Synopsis#
- Input Parameters#
- Note#
- Example Usage#
- See Also#
- Level#
- Location#

adds a TSGLLE acceptance scheme

sname - name of user-defined acceptance scheme

function - routine to create method context, see TSGLLEAcceptFn for the calling sequence

TSGLLEAcceptRegister() may be called multiple times to add several user-defined families.

Then, your scheme can be chosen with the procedural interface via

or at runtime via the option -ts_gl_accept_type my_scheme

TS: Scalable ODE and DAE Solvers, TSGLLE, TSGLLEType, TSGLLERegisterAll(), TSGLLEAcceptFn

src/ts/impls/implicit/glle/glle.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSGLLEAcceptRegister(const char sname[], TSGLLEAcceptFn *function)
```

Example 2 (unknown):
```unknown
TSGLLEAcceptFn
```

Example 3 (unknown):
```unknown
TSGLLEAcceptRegister()
```

Example 4 (unknown):
```unknown
TSGLLEAcceptRegister("my_scheme", MySchemeCreate);
```

---

## TSGLLEAcceptType#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLEAcceptType/

**Contents:**
- TSGLLEAcceptType#
- Synopsis#
- See Also#
- Level#
- Location#

String with the name of TSGLLEAccept scheme

TS: Scalable ODE and DAE Solvers, TSGLLESetAcceptType(), TS, TSGLLEAccept

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGLLEAccept
```

Example 2 (cpp):
```cpp
#include <petscts.h> 
typedef const char *TSGLLEAcceptType;
#define TSGLLEACCEPT_ALWAYS "always"
```

Example 3 (unknown):
```unknown
TSGLLESetAcceptType()
```

Example 4 (unknown):
```unknown
TSGLLEAccept
```

---

## TSGLLEAdaptChoose#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLEAdaptChoose/

**Contents:**
- TSGLLEAdaptChoose#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Choose the next scheme and step size using a TSGLLEAdapt step-size and order controller

adapt - the TSGLLEAdapt context

n - the number of candidate schemes

orders - the orders of accuracy of the candidate schemes

errors - the error estimates for each candidate scheme

cost - the relative cost of each candidate scheme

cur - the index of the currently active scheme

h - the last step size that was taken

tleft - the amount of remaining integration time

next_sc - the index of the scheme to use next

next_h - the step size to take next

finish - PETSC_TRUE if next_h was truncated to tleft because the end of the interval has been reached

TS: Scalable ODE and DAE Solvers, TSGLLE, TSGLLEAdapt, TSGLLEAdaptCreate(), TSGLLEAdaptSetType()

src/ts/impls/implicit/glle/glleadapt.c

TSGLLEAdaptChoose_None() in src/ts/impls/implicit/glle/glleadapt.c TSGLLEAdaptChoose_Size() in src/ts/impls/implicit/glle/glleadapt.c TSGLLEAdaptChoose_Both() in src/ts/impls/implicit/glle/glleadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGLLEAdapt
```

Example 2 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSGLLEAdaptChoose(TSGLLEAdapt adapt, PetscInt n, const PetscInt orders[], const PetscReal errors[], const PetscReal cost[], PetscInt cur, PetscReal h, PetscReal tleft, PetscInt *next_sc, PetscReal *next_h, PetscBool *finish)
```

Example 3 (unknown):
```unknown
TSGLLEAdapt
```

Example 4 (unknown):
```unknown
TSGLLEAdapt
```

---

## TSGLLEAdaptCreate#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLEAdaptCreate/

**Contents:**
- TSGLLEAdaptCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Create a TSGLLEAdapt step-size and order adaptivity object

comm - the MPI communicator

inadapt - the newly created TSGLLEAdapt context

Typically this is not called by users; use TSGetAdapt() on the enclosing TS instead.

TS: Scalable ODE and DAE Solvers, TSGLLE, TSGLLEAdapt, TSGLLEAdaptSetType(), TSGLLEAdaptDestroy()

src/ts/impls/implicit/glle/glleadapt.c

TSGLLEAdaptCreate_None() in src/ts/impls/implicit/glle/glleadapt.c TSGLLEAdaptCreate_Size() in src/ts/impls/implicit/glle/glleadapt.c TSGLLEAdaptCreate_Both() in src/ts/impls/implicit/glle/glleadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGLLEAdapt
```

Example 2 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSGLLEAdaptCreate(MPI_Comm comm, TSGLLEAdapt *inadapt)
```

Example 3 (unknown):
```unknown
TSGLLEAdapt
```

Example 4 (unknown):
```unknown
TSGetAdapt()
```

---

## TSGLLEAdaptDestroy#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLEAdaptDestroy/

**Contents:**
- TSGLLEAdaptDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Destroys a TSGLLEAdapt context

adapt - the TSGLLEAdapt context

TS: Scalable ODE and DAE Solvers, TSGLLE, TSGLLEAdapt, TSGLLEAdaptCreate()

src/ts/impls/implicit/glle/glleadapt.c

TSGLLEAdaptDestroy_JustFree() in src/ts/impls/implicit/glle/glleadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGLLEAdapt
```

Example 2 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSGLLEAdaptDestroy(TSGLLEAdapt *adapt)
```

Example 3 (unknown):
```unknown
TSGLLEAdapt
```

Example 4 (unknown):
```unknown
TSGLLEAdapt
```

---

## TSGLLEAdaptFinalizePackage#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLEAdaptFinalizePackage/

**Contents:**
- TSGLLEAdaptFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys everything in the TSGLLE package. It is called from PetscFinalize().

TS: Scalable ODE and DAE Solvers, PetscFinalize(), TSGLLEAdapt, TSGLLEAdaptInitializePackage()

src/ts/impls/implicit/glle/glleadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSGLLEAdaptFinalizePackage(void)
```

Example 3 (unknown):
```unknown
PetscFinalize()
```

Example 4 (unknown):
```unknown
TSGLLEAdapt
```

---

## TSGLLEAdaptInitializePackage#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLEAdaptInitializePackage/

**Contents:**
- TSGLLEAdaptInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function initializes everything in the TSGLLEAdapt package. It is called from TSInitializePackage().

TS: Scalable ODE and DAE Solvers, PetscInitialize(), TSGLLEAdapt, TSGLLEAdaptFinalizePackage()

src/ts/impls/implicit/glle/glleadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGLLEAdapt
```

Example 2 (unknown):
```unknown
TSInitializePackage()
```

Example 3 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSGLLEAdaptInitializePackage(void)
```

Example 4 (unknown):
```unknown
PetscInitialize()
```

---

## TSGLLEAdaptRegisterAll#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLEAdaptRegisterAll/

**Contents:**
- TSGLLEAdaptRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the adaptivity schemes in TSGLLEAdapt

TS: Scalable ODE and DAE Solvers, TSGLLEAdapt, TSGLLE, TSGLLEAdaptRegisterDestroy()

src/ts/impls/implicit/glle/glleadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGLLEAdapt
```

Example 2 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSGLLEAdaptRegisterAll(void)
```

Example 3 (unknown):
```unknown
TSGLLEAdapt
```

Example 4 (unknown):
```unknown
TSGLLEAdaptRegisterDestroy()
```

---

## TSGLLEAdaptRegister#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLEAdaptRegister/

**Contents:**
- TSGLLEAdaptRegister#
- Synopsis#
- Input Parameters#
- Note#
- Example Usage#
- See Also#
- Level#
- Location#

adds a TSGLLEAdapt implementation

Not Collective, No Fortran Support

sname - name of user-defined adaptivity scheme

function - routine to create method context

TSGLLEAdaptRegister() may be called multiple times to add several user-defined families.

Then, your scheme can be chosen with the procedural interface via

or at runtime via the option

TS: Scalable ODE and DAE Solvers, TSGLLE, TSGLLEAdapt, TSGLLEAdaptRegisterAll()

src/ts/impls/implicit/glle/glleadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGLLEAdapt
```

Example 2 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSGLLEAdaptRegister(const char sname[], PetscErrorCode (*function)(TSGLLEAdapt))
```

Example 3 (unknown):
```unknown
TSGLLEAdaptRegister()
```

Example 4 (unknown):
```unknown
TSGLLEAdaptRegister("my_scheme", MySchemeCreate);
```

---

## TSGLLEAdaptSetFromOptions#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLEAdaptSetFromOptions/

**Contents:**
- TSGLLEAdaptSetFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Sets options from the options database for a TSGLLEAdapt context

adapt - the TSGLLEAdapt context

PetscOptionsObject - the PetscOptionItems used to process options

-ts_adapt_type (none|size|both) - algorithm to use for adaptivity

This function is currently intended for internal use from inside TSSetFromOptions_GLLE().

TS: Scalable ODE and DAE Solvers, TSGLLE, TSGLLEAdapt, TSGLLEAdaptSetType()

src/ts/impls/implicit/glle/glleadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGLLEAdapt
```

Example 2 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSGLLEAdaptSetFromOptions(TSGLLEAdapt adapt, PetscOptionItems PetscOptionsObject)
```

Example 3 (unknown):
```unknown
TSGLLEAdapt
```

Example 4 (unknown):
```unknown
PetscOptionItems
```

---

## TSGLLEAdaptSetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLEAdaptSetOptionsPrefix/

**Contents:**
- TSGLLEAdaptSetOptionsPrefix#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the prefix used for searching for TSGLLEAdapt options in the options database

adapt - the TSGLLEAdapt context

prefix - the prefix to prepend to all option names

TS: Scalable ODE and DAE Solvers, TSGLLE, TSGLLEAdapt, TSGLLEAdaptSetFromOptions()

src/ts/impls/implicit/glle/glleadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGLLEAdapt
```

Example 2 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSGLLEAdaptSetOptionsPrefix(TSGLLEAdapt adapt, const char prefix[])
```

Example 3 (unknown):
```unknown
TSGLLEAdapt
```

Example 4 (unknown):
```unknown
TSGLLEAdapt
```

---

## TSGLLEAdaptSetType#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLEAdaptSetType/

**Contents:**
- TSGLLEAdaptSetType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the type of a TSGLLEAdapt step-size and order adaptivity object

adapt - the TSGLLEAdapt context

type - the name of the adaptivity scheme, e.g. TSGLLEADAPT_NONE, TSGLLEADAPT_SIZE, TSGLLEADAPT_BOTH

TS: Scalable ODE and DAE Solvers, TSGLLE, TSGLLEAdapt, TSGLLEAdaptCreate(), TSGLLEAdaptType, TSGLLEAdaptRegister()

src/ts/impls/implicit/glle/glleadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGLLEAdapt
```

Example 2 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSGLLEAdaptSetType(TSGLLEAdapt adapt, TSGLLEAdaptType type)
```

Example 3 (unknown):
```unknown
TSGLLEAdapt
```

Example 4 (unknown):
```unknown
TSGLLEADAPT_NONE
```

---

## TSGLLEAdaptType#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLEAdaptType/

**Contents:**
- TSGLLEAdaptType#
- Synopsis#
- Developer Note#
- See Also#
- Level#
- Location#

String with the name of TSGLLEAdapt scheme

This functionality should be replaced by the TSAdaptType.

TS: Scalable ODE and DAE Solvers, TSGLLEAdaptSetType(), TS

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGLLEAdapt
```

Example 2 (cpp):
```cpp
#include <petscts.h> 
typedef const char *TSGLLEAdaptType;
#define TSGLLEADAPT_NONE "none"
#define TSGLLEADAPT_SIZE "size"
#define TSGLLEADAPT_BOTH "both"
```

Example 3 (unknown):
```unknown
TSAdaptType
```

Example 4 (unknown):
```unknown
TSGLLEAdaptSetType()
```

---

## TSGLLEAdaptView#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLEAdaptView/

**Contents:**
- TSGLLEAdaptView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Views a TSGLLEAdapt step-size and order adaptivity object

adapt - the TSGLLEAdapt context

viewer - the PetscViewer used to view the object

TS: Scalable ODE and DAE Solvers, TSGLLE, TSGLLEAdapt, TSGLLEAdaptCreate(), PetscViewer

src/ts/impls/implicit/glle/glleadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGLLEAdapt
```

Example 2 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSGLLEAdaptView(TSGLLEAdapt adapt, PetscViewer viewer)
```

Example 3 (unknown):
```unknown
TSGLLEAdapt
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## TSGLLEAdapt#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLEAdapt/

**Contents:**
- TSGLLEAdapt#
- Synopsis#
- Developer Note#
- See Also#
- Level#
- Location#
- Implementations#

Abstract object that manages time-step adaptivity for TSGLLE

This functionality should be replaced by the TSAdapt.

TS: Scalable ODE and DAE Solvers, TS, TSGLLE, TSGLLEAdaptCreate(), TSGLLEAdaptType

_p_TSGLLEAdapt in src/ts/impls/implicit/glle/glleadapt.c TSGLLEAdapt_None in src/ts/impls/implicit/glle/glleadapt.c TSGLLEAdapt_Size in src/ts/impls/implicit/glle/glleadapt.c TSGLLEAdapt_Both in src/ts/impls/implicit/glle/glleadapt.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (c):
```c
#include <petscts.h> 
typedef struct _p_TSGLLEAdapt *TSGLLEAdapt;
```

Example 2 (unknown):
```unknown
TSGLLEAdaptCreate()
```

Example 3 (unknown):
```unknown
TSGLLEAdaptType
```

---

## TSGLLEFinalizePackage#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLEFinalizePackage/

**Contents:**
- TSGLLEFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys everything in the TSGLLE package. It is called from PetscFinalize().

TS: Scalable ODE and DAE Solvers, PetscFinalize(), TSGLLEInitializePackage(), TSInitializePackage()

src/ts/impls/implicit/glle/glle.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSGLLEFinalizePackage(void)
```

Example 3 (unknown):
```unknown
PetscFinalize()
```

Example 4 (unknown):
```unknown
TSGLLEInitializePackage()
```

---

## TSGLLEGetAdapt#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLEGetAdapt/

**Contents:**
- TSGLLEGetAdapt#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

gets the TSGLLEAdapt object from the TS

adapt - the TSGLLEAdapt context

This allows the user set options on the TSGLLEAdapt object. Usually it is better to do this using the options database, so this function is rarely needed.

TS: Scalable ODE and DAE Solvers, TS, TSGLLE, TSGLLEAdapt, TSGLLEAdaptRegister()

src/ts/impls/implicit/glle/glle.c

TSGLLEGetAdapt_GLLE() in src/ts/impls/implicit/glle/glle.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGLLEAdapt
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSGLLEGetAdapt(TS ts, TSGLLEAdapt *adapt)
```

Example 3 (unknown):
```unknown
TSGLLEAdapt
```

Example 4 (unknown):
```unknown
TSGLLEAdapt
```

---

## TSGLLEInitializePackage#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLEInitializePackage/

**Contents:**
- TSGLLEInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function initializes everything in the TSGLLE package. It is called from TSInitializePackage().

TS: Scalable ODE and DAE Solvers, PetscInitialize(), TSInitializePackage(), TSGLLEFinalizePackage()

src/ts/impls/implicit/glle/glle.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSInitializePackage()
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSGLLEInitializePackage(void)
```

Example 3 (unknown):
```unknown
PetscInitialize()
```

Example 4 (unknown):
```unknown
TSInitializePackage()
```

---

## TSGLLERegisterAll#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLERegisterAll/

**Contents:**
- TSGLLERegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the general linear methods in TSGLLE

TS: Scalable ODE and DAE Solvers, TSGLLE, TSGLLERegisterDestroy()

src/ts/impls/implicit/glle/glle.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSGLLERegisterAll(void)
```

Example 2 (unknown):
```unknown
TSGLLERegisterDestroy()
```

---

## TSGLLERegister#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLERegister/

**Contents:**
- TSGLLERegister#
- Synopsis#
- Input Parameters#
- Note#
- Example Usage#
- See Also#
- Level#
- Location#

adds a TSGLLE implementation

Not Collective, No Fortran Support

sname - name of user-defined general linear scheme

function - routine to create method context

TSGLLERegister() may be called multiple times to add several user-defined families.

Then, your scheme can be chosen with the procedural interface via

or at runtime via the option

TS: Scalable ODE and DAE Solvers, TSGLLE, TSGLLEType, TSGLLERegisterAll(), TSGLLESetType()

src/ts/impls/implicit/glle/glle.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSGLLERegister(const char sname[], PetscErrorCode (*function)(TS))
```

Example 2 (unknown):
```unknown
TSGLLERegister()
```

Example 3 (unknown):
```unknown
TSGLLERegister("my_scheme", MySchemeCreate);
```

Example 4 (unknown):
```unknown
TSGLLESetType(ts, "my_scheme")
```

---

## TSGLLESetAcceptType#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLESetAcceptType/

**Contents:**
- TSGLLESetAcceptType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

sets the acceptance test for TSGLLE

-ts_gl_accept_type (always) - sets the method used to determine whether to accept or reject a step

Time integrators that need to control error must have the option to reject a time step based on local error estimates. This function allows different schemes to be set.

TS: Scalable ODE and DAE Solvers, TS, TSGLLE, TSGLLEAcceptRegister(), TSGLLEAdapt

src/ts/impls/implicit/glle/glle.c

TSGLLESetAcceptType_GLLE() in src/ts/impls/implicit/glle/glle.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSGLLESetAcceptType(TS ts, TSGLLEAcceptType type)
```

Example 2 (unknown):
```unknown
TSGLLEAcceptRegister()
```

Example 3 (unknown):
```unknown
TSGLLEAdapt
```

---

## TSGLLESetType#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLESetType/

**Contents:**
- TSGLLESetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

sets the class of general linear method, TSGLLE to use for time-stepping

type - a method, currently only TSGLLE_IRKS is available

-ts_gl_type (irks) - sets the method

TS: Scalable ODE and DAE Solvers, TS, TSGLLEType, TSGLLE, TSGLLERegister(), TSGLLE_IRKS, TSGLLEGetAcceptType(), TSGLLESetAcceptType(), TSGLLEAcceptType()

src/ts/impls/implicit/glle/glle.c

TSGLLESetType_GLLE() in src/ts/impls/implicit/glle/glle.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSGLLESetType(TS ts, TSGLLEType type)
```

Example 2 (unknown):
```unknown
TSGLLE_IRKS
```

Example 3 (unknown):
```unknown
TSGLLERegister()
```

Example 4 (unknown):
```unknown
TSGLLE_IRKS
```

---

## TSGLLEType#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLEType/

**Contents:**
- TSGLLEType#
- Synopsis#
- See Also#
- Level#
- Location#

string with the name of a General Linear TSGLLE type

TS: Scalable ODE and DAE Solvers, TS, TSGLLE, TSGLLESetType(), TSGLLERegister(), TSGLLEAccept

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h> 
typedef const char *TSGLLEType;
#define TSGLLE_IRKS "irks"
```

Example 2 (unknown):
```unknown
TSGLLESetType()
```

Example 3 (unknown):
```unknown
TSGLLERegister()
```

Example 4 (unknown):
```unknown
TSGLLEAccept
```

---

## TSGLLE#

**URL:** https://petsc.org/release/manualpages/TS/TSGLLE/

**Contents:**
- TSGLLE#
- Options Database Keys#
- Notes#
- References#
- See Also#
- Level#
- Location#

DAE solver using implicit General Linear methods [BJW07] [But16]

-ts_gl_type (irks) - the class of general linear method

-ts_gl_rtol tol - relative error

-ts_gl_atol tol - absolute error

-ts_gl_min_order p - minimum order method to consider (default=1)

-ts_gl_max_order p - maximum order method to consider (default=3)

-ts_gl_start_order p - order of starting method (default=1)

-ts_gl_complete (rescale|rescale- and-modify) - method to use for completing the step (rescale-and-modify or rescale)

-ts_adapt_type (basic|dsp|none|cfl|glee|history) - adaptive controller to use (none step both)

These methods contain Runge-Kutta and multistep schemes as special cases. These special cases have some fundamental limitations. For example, diagonally implicit Runge-Kutta cannot have stage order greater than 1 which limits their applicability to very stiff systems. Meanwhile, multistep methods cannot be A-stable for order greater than 2 and BDF are not 0-stable for order greater than 6. GL methods can be A- and L-stable with arbitrarily high stage order and reliable error estimates for both 1 and 2 orders higher to facilitate adaptive step sizes and adaptive order schemes. All this is possible while preserving a singly diagonally implicit structure.

This integrator can be applied to DAE.

Diagonally implicit general linear (DIGL) methods are a generalization of diagonally implicit Runge-Kutta (DIRK). They are represented by the tableau

combined with a vector c of abscissa. “Diagonally implicit” means that \(A\) is lower triangular. A step of the general method reads

where Y is the multivector of stage values, \(Y'\) is the multivector of stage derivatives, \(X^k\) is the Nordsieck vector of the solution at step \(k\). The Nordsieck vector consists of the first \(r\) moments of the solution, given by

If \(A\) is lower triangular, we can solve the stages \((Y, Y')\) sequentially

and then construct the pieces to carry to the next step

Note that when the equations are cast in implicit form, we are using the stage equation to define \(y'_i\) in terms of \(y_i\) and known stuff (\(y_j\) for \(j<i\) and \(x_j\) for all \(j\)).

At present, the most attractive GL methods for stiff problems are singly diagonally implicit schemes which posses Inherent Runge-Kutta Stability (TSIRKS). These methods have \(r=s\), the number of items passed between steps is equal to the number of stages. The order and stage-order are one less than the number of stages. We use the error estimates in the 2007 paper which provide the following estimates

These estimates are accurate to \( O(h^{p+3})\).

Changing the step size

Uses the generalized “rescale and modify” scheme, see equation (4.5) of [BJW07].

J.C. Butcher, Z. Jackiewicz, and W.M. Wright. Error propagation of general linear methods for ordinary differential equations. Journal of Complexity, 23(4-6):560–580, 2007. doi:10.1016/j.jco.2007.01.009.

John Charles Butcher. Numerical methods for ordinary differential equations. John Wiley & Sons, 2016.

TS: Scalable ODE and DAE Solvers, TSCreate(), TS, TSSetType(), TSType, TSGLLEType, TSGLLESetType(), TSGLLESetAcceptType(), TSGLLEGetAdapt()

src/ts/impls/implicit/glle/glle.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (yaml):
```yaml
A  |  U
  -------
  B  |  V
```

Example 2 (unknown):
```unknown
TSSetType()
```

Example 3 (unknown):
```unknown
TSGLLESetType()
```

Example 4 (unknown):
```unknown
TSGLLESetAcceptType()
```

---

## TSHasTransientVariable#

**URL:** https://petsc.org/release/manualpages/TS/TSHasTransientVariable/

**Contents:**
- TSHasTransientVariable#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

determine whether transient variables have been set

ts - TS on which to compute

has - PETSC_TRUE if transient variables have been set

TS: Scalable ODE and DAE Solvers, TS, TSBDF, DMTSSetTransientVariable(), TSComputeTransientVariable()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSHasTransientVariable(TS ts, PetscBool *has)
```

Example 2 (unknown):
```unknown
DMTSSetTransientVariable()
```

Example 3 (unknown):
```unknown
TSComputeTransientVariable()
```

---

## TSI2FunctionFn#

**URL:** https://petsc.org/release/manualpages/TS/TSI2FunctionFn/

**Contents:**
- TSI2FunctionFn#
- Synopsis#
- Calling Sequence#
- Note#
- See Also#
- Level#
- Location#

A prototype of a TS implicit function evaluation function for 2nd order systems that would be passed to TSSetI2Function()

ts - the TS context obtained from TSCreate()

t - time at step/stage being solved

U_t - time derivative of state vector

U_tt - second time derivative of state vector

ctx - [optional] user-defined context for matrix evaluation routine (may be NULL)

The deprecated TSI2Function still works as a replacement for TSI2FunctionFn *.

TS: Scalable ODE and DAE Solvers, TS, TSSetI2Function(), DMTSSetI2Function(), TSIFunctionFn

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetI2Function()
```

Example 2 (cpp):
```cpp
#include <petscts.h> 
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode TSI2FunctionFn(TS ts, PetscReal t, Vec U, Vec U_t, Vec U_tt, Vec F, PetscCtx ctx);
```

Example 3 (unknown):
```unknown
TSI2Function
```

Example 4 (unknown):
```unknown
TSI2FunctionFn
```

---

## TSI2JacobianFn#

**URL:** https://petsc.org/release/manualpages/TS/TSI2JacobianFn/

**Contents:**
- TSI2JacobianFn#
- Synopsis#
- Calling Sequence#
- Note#
- See Also#
- Level#
- Location#

A prototype of a TS implicit Jacobian evaluation function for 2nd order systems that would be passed to TSSetI2Jacobian()

ts - the TS context obtained from TSCreate()

t - time at step/stage being solved

U_t - time derivative of state vector

U_tt - second time derivative of state vector

J - Jacobian of G(U) = F(t,U,W+vU,W’+aU), equivalent to dF/dU + vdF/dU_t + adF/dU_tt

jac - matrix from which to construct the preconditioner, may be same as J

ctx - [optional] user-defined context for matrix evaluation routine

The deprecated TSI2Jacobian still works as a replacement for TSI2JacobianFn *.

TS: Scalable ODE and DAE Solvers, TS, TSSetI2Jacobian(), DMTSSetI2Jacobian(), TSIFunctionFn, TSIJacobianFn, TSRHSFunctionFn, TSRHSJacobianFn

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetI2Jacobian()
```

Example 2 (cpp):
```cpp
#include <petscts.h> 
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode TSI2JacobianFn(TS ts, PetscReal t, Vec U, Vec U_t, Vec U_tt, PetscReal v, PetscReal a, Mat J, Mat Jac, PetscCtx ctx);
```

Example 3 (unknown):
```unknown
TSI2Jacobian
```

Example 4 (unknown):
```unknown
TSI2JacobianFn
```

---

## TSIFunctionFn#

**URL:** https://petsc.org/release/manualpages/TS/TSIFunctionFn/

**Contents:**
- TSIFunctionFn#
- Synopsis#
- Calling Sequence#
- Note#
- See Also#
- Level#
- Location#
- Examples#

A prototype of a TS implicit function evaluation function that would be passed to `TSSetIFunction()

ts - the TS context obtained from TSCreate()

t - time at step/stage being solved

U_t - time derivative of state vector

ctx - [optional] user-defined context for function

The deprecated TSIFunction still works as a replacement for TSIFunctionFn *.

TS: Scalable ODE and DAE Solvers, TS, TSSetIFunction(), DMTSSetIFunction(), TSIJacobianFn, TSRHSFunctionFn, TSRHSJacobianFn

src/ts/tutorials/ex8.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h> 
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode TSIFunctionFn(TS ts, PetscReal t, Vec U, Vec U_t, Vec F, PetscCtx ctx);
```

Example 2 (unknown):
```unknown
TSIFunction
```

Example 3 (unknown):
```unknown
TSIFunctionFn
```

Example 4 (unknown):
```unknown
TSSetIFunction()
```

---

## TSIJacobianFn#

**URL:** https://petsc.org/release/manualpages/TS/TSIJacobianFn/

**Contents:**
- TSIJacobianFn#
- Synopsis#
- Calling Sequence#
- Note#
- See Also#
- Level#
- Location#
- Examples#

A prototype of a TS Jacobian evaluation function that would be passed to TSSetIJacobian()

ts - the TS context obtained from TSCreate()

t - time at step/stage being solved

U_t - time derivative of state vector

Amat - (approximate) Jacobian of F(t,U,W+aU), equivalent to dF/dU + adF/dU_t

Pmat - matrix used for constructing preconditioner, usually the same as Amat

ctx - [optional] user-defined context for Jacobian evaluation routine

The deprecated TSIJacobian still works as a replacement for TSIJacobianFn *.

TS: Scalable ODE and DAE Solvers, TSSetIJacobian(), DMTSSetIJacobian(), TSIFunctionFn, TSRHSFunctionFn, TSRHSJacobianFn

src/ts/tutorials/ex8.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetIJacobian()
```

Example 2 (cpp):
```cpp
#include <petscts.h> 
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode TSIJacobianFn(TS ts, PetscReal t, Vec U, Vec U_t, PetscReal a, Mat Amat, Mat Pmat, PetscCtx ctx);
```

Example 3 (unknown):
```unknown
TSIJacobian
```

Example 4 (unknown):
```unknown
TSIJacobianFn
```

---

## TSInitializePackage#

**URL:** https://petsc.org/release/manualpages/TS/TSInitializePackage/

**Contents:**
- TSInitializePackage#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#

This function initializes everything in the TS package. It is called from PetscDLLibraryRegister_petscts() when using dynamic libraries, and on the first call to TSCreate() when using shared or static libraries.

This function never needs to be called by PETSc users.

TS: Scalable ODE and DAE Solvers, TS, PetscInitialize(), TSFinalizePackage()

src/ts/interface/dlregists.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDLLibraryRegister_petscts()
```

Example 2 (unknown):
```unknown
PetscErrorCode TSInitializePackage(void)
```

Example 3 (unknown):
```unknown
PetscInitialize()
```

Example 4 (unknown):
```unknown
TSFinalizePackage()
```

---

## TSInterpolate#

**URL:** https://petsc.org/release/manualpages/TS/TSInterpolate/

**Contents:**
- TSInterpolate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Interpolate the solution computed during the previous step to an arbitrary location in the interval

ts - time stepping context

t - time to interpolate to

U - state at given time

TSInterpolate() and the storing of previous steps/stages should be generalized to support delay differential equations and continuous adjoints.

TS: Scalable ODE and DAE Solvers, TS, TSSetExactFinalTime(), TSSolve()

src/ts/interface/ts.c

src/ts/tutorials/ex20opt_p.c src/ts/tutorials/ex19.c src/ts/tutorials/ex20.c src/ts/tutorials/ex20opt_ic.c src/ts/tutorials/ex20adj.c src/ts/tutorials/ex20fwd.c src/ts/tutorials/ex16.c

TSInterpolate_ARKIMEX() in src/ts/impls/arkimex/arkimex.c TSInterpolate_BDF() in src/ts/impls/bdf/bdf.c TSInterpolate_EIMEX() in src/ts/impls/eimex/eimex.c TSInterpolate_Euler() in src/ts/impls/explicit/euler/euler.c TSInterpolate_RK() in src/ts/impls/explicit/rk/rk.c TSInterpolate_GLEE() in src/ts/impls/glee/glee.c TSInterpolate_Alpha() in src/ts/impls/implicit/alpha/alpha1.c TSInterpolate_Alpha() in src/ts/impls/implicit/alpha/alpha2.c TSInterpolate_DiscGrad() in src/ts/impls/implicit/discgrad/tsdiscgrad.c TSInterpolate_IRK() in src/ts/impls/implicit/irk/irk.c TSInterpolate_Sundials() in src/ts/impls/implicit/sundials/sundials.c TSInterpolate_Theta() in src/ts/impls/implicit/theta/theta.c TSInterpolate_Mimex() in src/ts/impls/mimex/mimex.c TSInterpolate_RosW() in src/ts/impls/rosw/rosw.c TSInterpolate_BasicSymplectic() in src/ts/impls/symplectic/basicsymplectic/basicsymplectic.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSInterpolate(TS ts, PetscReal t, Vec U)
```

Example 2 (unknown):
```unknown
TSInterpolate()
```

Example 3 (unknown):
```unknown
TSSetExactFinalTime()
```

---

## TSIRKFinalizePackage#

**URL:** https://petsc.org/release/manualpages/TS/TSIRKFinalizePackage/

**Contents:**
- TSIRKFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys everything in the TSIRK package. It is called from PetscFinalize().

TS: Scalable ODE and DAE Solvers, TSIRK, PetscFinalize(), TSInitializePackage()

src/ts/impls/implicit/irk/irk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSIRKFinalizePackage(void)
```

Example 3 (unknown):
```unknown
PetscFinalize()
```

Example 4 (unknown):
```unknown
TSInitializePackage()
```

---

## TSIRKGetNumStages#

**URL:** https://petsc.org/release/manualpages/TS/TSIRKGetNumStages/

**Contents:**
- TSIRKGetNumStages#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Get the number of stages of TSIRK scheme

ts - timestepping context

nstages - number of stages of TSIRK scheme

TS: Scalable ODE and DAE Solvers, TSIRKSetNumStages(), TSIRK

src/ts/impls/implicit/irk/irk.c

TSIRKGetNumStages_IRK() in src/ts/impls/implicit/irk/irk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSIRKGetNumStages(TS ts, PetscInt *nstages)
```

Example 2 (unknown):
```unknown
TSIRKSetNumStages()
```

---

## TSIRKGetType#

**URL:** https://petsc.org/release/manualpages/TS/TSIRKGetType/

**Contents:**
- TSIRKGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get the type of TSIRK IMEX scheme being used

ts - timestepping context

irktype - type of TSIRK IMEX scheme

TS: Scalable ODE and DAE Solvers, TSIRK, TSIRKType, TSIRKGAUSS

src/ts/impls/implicit/irk/irk.c

TSIRKGetType_IRK() in src/ts/impls/implicit/irk/irk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSIRKGetType(TS ts, TSIRKType *irktype)
```

---

## TSIRKInitializePackage#

**URL:** https://petsc.org/release/manualpages/TS/TSIRKInitializePackage/

**Contents:**
- TSIRKInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function initializes everything in the TSIRK package. It is called from TSInitializePackage().

TS: Scalable ODE and DAE Solvers, TSIRK, PetscInitialize(), TSIRKFinalizePackage(), TSInitializePackage()

src/ts/impls/implicit/irk/irk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSInitializePackage()
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSIRKInitializePackage(void)
```

Example 3 (unknown):
```unknown
PetscInitialize()
```

Example 4 (unknown):
```unknown
TSIRKFinalizePackage()
```

---

## TSIRKRegisterAll#

**URL:** https://petsc.org/release/manualpages/TS/TSIRKRegisterAll/

**Contents:**
- TSIRKRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the implicit Runge-Kutta methods in TSIRK

Not Collective, but should be called by all processes which will need the schemes to be registered

TS: Scalable ODE and DAE Solvers, TSIRK, TSIRKRegisterDestroy()

src/ts/impls/implicit/irk/irk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSIRKRegisterAll(void)
```

Example 2 (unknown):
```unknown
TSIRKRegisterDestroy()
```

---

## TSIRKRegisterDestroy#

**URL:** https://petsc.org/release/manualpages/TS/TSIRKRegisterDestroy/

**Contents:**
- TSIRKRegisterDestroy#
- Synopsis#
- See Also#
- Level#
- Location#

Frees the list of schemes that were registered by TSIRKRegister().

TS: Scalable ODE and DAE Solvers, TSIRK, TSIRKRegister(), TSIRKRegisterAll()

src/ts/impls/implicit/irk/irk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSIRKRegister()
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSIRKRegisterDestroy(void)
```

Example 3 (unknown):
```unknown
TSIRKRegister()
```

Example 4 (unknown):
```unknown
TSIRKRegisterAll()
```

---

## TSIRKRegister#

**URL:** https://petsc.org/release/manualpages/TS/TSIRKRegister/

**Contents:**
- TSIRKRegister#
- Synopsis#
- Input Parameters#
- Note#
- Example Usage#
- See Also#
- Level#
- Location#

adds a TSIRK implementation

Not Collective, No Fortran Support

sname - name of user-defined IRK scheme

function - function to create method context

TSIRKRegister() may be called multiple times to add several user-defined families.

Then, your scheme can be chosen with the procedural interface via

or at runtime via the option

TS: Scalable ODE and DAE Solvers, TSIRK, TSIRKRegisterAll()

src/ts/impls/implicit/irk/irk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSIRKRegister(const char sname[], PetscErrorCode (*function)(TS))
```

Example 2 (unknown):
```unknown
TSIRKRegister()
```

Example 3 (unknown):
```unknown
TSIRKRegister("my_scheme", MySchemeCreate);
```

Example 4 (unknown):
```unknown
TSIRKSetType(ts, "my_scheme")
```

---

## TSIRKSetNumStages#

**URL:** https://petsc.org/release/manualpages/TS/TSIRKSetNumStages/

**Contents:**
- TSIRKSetNumStages#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

Set the number of stages of TSIRK scheme to use

ts - timestepping context

nstages - number of stages of TSIRK scheme

-ts_irk_nstages int - set number of stages

TS: Scalable ODE and DAE Solvers, TSIRKGetNumStages(), TSIRK

src/ts/impls/implicit/irk/irk.c

TSIRKSetNumStages_IRK() in src/ts/impls/implicit/irk/irk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSIRKSetNumStages(TS ts, PetscInt nstages)
```

Example 2 (unknown):
```unknown
TSIRKGetNumStages()
```

---

## TSIRKSetType#

**URL:** https://petsc.org/release/manualpages/TS/TSIRKSetType/

**Contents:**
- TSIRKSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

Set the type of TSIRK scheme to use

ts - timestepping context

irktype - type of TSIRK scheme

-ts_irk_type gauss - set irk type

TS: Scalable ODE and DAE Solvers, TSIRKGetType(), TSIRK, TSIRKType, TSIRKGAUSS

src/ts/impls/implicit/irk/irk.c

TSIRKSetType_IRK() in src/ts/impls/implicit/irk/irk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSIRKSetType(TS ts, TSIRKType irktype)
```

Example 2 (unknown):
```unknown
TSIRKGetType()
```

---

## TSIRKTableauCreate#

**URL:** https://petsc.org/release/manualpages/TS/TSIRKTableauCreate/

**Contents:**
- TSIRKTableauCreate#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

create the tableau for TSIRK and provide the entries

ts - timestepping context

nstages - number of stages, this is the dimension of the matrices below

A - stage coefficients (dimension nstages * nstages, row-major)

b - step completion table (dimension nstages)

c - abscissa (dimension nstages)

binterp - coefficients of the interpolation formula (dimension nstages), optional (use NULL to skip)

A_inv - inverse of A (dimension nstages * nstages, row-major), optional (use NULL to skip)

A_inv_rowsum - row sum of the inverse of A (dimension nstages), optional (use NULL to skip)

I_s - identity matrix (dimension nstages * nstages), optional (use NULL to skip)

TS: Scalable ODE and DAE Solvers, TSIRK, TSIRKRegister()

src/ts/impls/implicit/irk/irk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSIRKTableauCreate(TS ts, PetscInt nstages, const PetscReal *A, const PetscReal *b, const PetscReal *c, const PetscReal *binterp, const PetscScalar *A_inv, const PetscScalar *A_inv_rowsum, const PetscScalar *I_s)
```

Example 2 (unknown):
```unknown
TSIRKRegister()
```

---

## TSIRKType#

**URL:** https://petsc.org/release/manualpages/TS/TSIRKType/

**Contents:**
- TSIRKType#
- Synopsis#
- See Also#
- Level#
- Location#

String with the name of an implicit Runge-Kutta TSIRK type

TS: Scalable ODE and DAE Solvers, TSIRKSetType(), TS, TSIRK, TSIRKRegister()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h> 
typedef const char *TSIRKType;
#define TSIRKGAUSS "gauss"
```

Example 2 (unknown):
```unknown
TSIRKSetType()
```

Example 3 (unknown):
```unknown
TSIRKRegister()
```

---

## TSIRK#

**URL:** https://petsc.org/release/manualpages/TS/TSIRK/

**Contents:**
- TSIRK#
- Notes#
- See Also#
- Level#
- Location#

ODE and DAE solver using Implicit Runge-Kutta schemes

TSIRK uses the sparse Kronecker product matrix implementation of MATKAIJ to achieve good arithmetic intensity.

Gauss-Legrendre methods are currently supported. These are A-stable symplectic methods with an arbitrary number of stages. The order of accuracy is 2s when using s stages. The default method uses three stages and thus has an order of six. The number of stages (thus order) can be set with -ts_irk_nstages or TSIRKSetNumStages().

TS: Scalable ODE and DAE Solvers, TSCreate(), TS, TSSetType(), TSIRKSetType(), TSIRKGetType(), TSIRKGAUSS, TSIRKRegister(), TSIRKSetNumStages(), TSType

src/ts/impls/implicit/irk/irk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
-ts_irk_nstages
```

Example 2 (unknown):
```unknown
TSIRKSetNumStages()
```

Example 3 (unknown):
```unknown
TSSetType()
```

Example 4 (unknown):
```unknown
TSIRKSetType()
```

---

## TSLoad#

**URL:** https://petsc.org/release/manualpages/TS/TSLoad/

**Contents:**
- TSLoad#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Loads a TS that has been stored in binary with TSView().

ts - the newly loaded TS, this needs to have been created with TSCreate() or some related function before a call to TSLoad().

viewer - binary file viewer, obtained from PetscViewerBinaryOpen()

The type is determined by the data in the file, any type set into the TS before this call is ignored.

TS: Scalable ODE and DAE Solvers, TS, PetscViewer, PetscViewerBinaryOpen(), TSView(), MatLoad(), VecLoad()

src/ts/interface/ts.c

src/ts/tutorials/ex28.c

TSLoad_ARKIMEX() in src/ts/impls/arkimex/arkimex.c TSLoad_RK() in src/ts/impls/explicit/rk/rk.c TSLoad_GLEE() in src/ts/impls/glee/glee.c TSLoad_IRK() in src/ts/impls/implicit/irk/irk.c TSLoad_MPRK() in src/ts/impls/multirate/mprk.c TSLoad_RosW() in src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSLoad(TS ts, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscViewerBinaryOpen()
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscViewerBinaryOpen()
```

---

## TSMIMEX#

**URL:** https://petsc.org/release/manualpages/TS/TSMIMEX/

**Contents:**
- TSMIMEX#
- See Also#
- Level#
- Location#

ODE solver using the explicit forward Mimex method

TS: Scalable ODE and DAE Solvers, TSCreate(), TS, TSSetType(), TSBEULER

src/ts/impls/mimex/mimex.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetType()
```

---

## TSMonitorCancel#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorCancel/

**Contents:**
- TSMonitorCancel#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#

Clears all the monitors that have been set on a time-step object.

ts - the TS context obtained from TSCreate()

There is no way to remove a single, specific monitor.

TS: Scalable ODE and DAE Solvers, TS, TSMonitorDefault(), TSMonitorSet()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorCancel(TS ts)
```

Example 2 (unknown):
```unknown
TSMonitorDefault()
```

Example 3 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorDefault#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorDefault/

**Contents:**
- TSMonitorDefault#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

The default monitor, prints the timestep and time for each step

step - iteration number (after the final time step the monitor routine may be called with a step of -1, this indicates the solution has been interpolated to this time)

vf - the viewer and format

-ts_monitor - monitors the time integration

This is not called directly by users, rather one calls TSMonitorSet(), with this function as an argument, to cause the monitor to be used during the TS integration.

TS: Scalable ODE and DAE Solvers, TSMonitorSet(), TSDMSwarmMonitorMoments(), TSMonitorWallClockTime(), TSMonitorExtreme(), TSMonitorDrawSolution(), TSMonitorDrawSolutionPhase(), TSMonitorDrawSolutionFunction(), TSMonitorDrawError(), TSMonitorSolution(), TSMonitorSolutionVTK(), TSMonitorLGSolution(), TSMonitorLGError(), TSMonitorSPSwarmSolution(), TSMonitorError(), TSMonitorEnvelope()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorDefault(TS ts, PetscInt step, PetscReal ptime, Vec v, PetscViewerAndFormat *vf)
```

Example 2 (unknown):
```unknown
TSMonitorSet()
```

Example 3 (unknown):
```unknown
TSMonitorSet()
```

Example 4 (unknown):
```unknown
TSDMSwarmMonitorMoments()
```

---

## TSMonitorDMDARayCtx#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorDMDARayCtx/

**Contents:**
- TSMonitorDMDARayCtx#
- Synopsis#
- See Also#
- Level#
- Location#

Context object for TSMonitorDMDARay()

TS, TSSetMonitor(), TSMonitorDMDARay(), TSMonitorDMDARayDestroy()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorDMDARay()
```

Example 2 (cpp):
```cpp
#include <petscts.h> 
typedef struct {
  Vec            ray;
  VecScatter     scatter;
  PetscViewer    viewer;
  TSMonitorLGCtx lgctx;
} TSMonitorDMDARayCtx;
```

Example 3 (unknown):
```unknown
TSSetMonitor()
```

Example 4 (unknown):
```unknown
TSMonitorDMDARay()
```

---

## TSMonitorDMDARayDestroy#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorDMDARayDestroy/

**Contents:**
- TSMonitorDMDARayDestroy#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#

Destroys the context created for the -ts_monitor_dmda_ray and -ts_monitor_lg_dmda_ray monitors

mctx - pointer to the TSMonitorDMDARayCtx context

This is normally passed to TSMonitorSet() alongside TSMonitorDMDARay() or TSMonitorLGDMDARay(); it is not called directly by users.

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet(), TSMonitorDMDARay(), TSMonitorLGDMDARay()

src/ts/utils/dmdats.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
-ts_monitor_dmda_ray
```

Example 2 (unknown):
```unknown
-ts_monitor_lg_dmda_ray
```

Example 3 (unknown):
```unknown
#include "petscdmda.h" 
#include "petscts.h" 
PetscErrorCode TSMonitorDMDARayDestroy(PetscCtxRt mctx)
```

Example 4 (unknown):
```unknown
TSMonitorDMDARayCtx
```

---

## TSMonitorDMDARay#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorDMDARay/

**Contents:**
- TSMonitorDMDARay#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Monitors the solution of a DMDA-based TS by scattering values along a ray to a viewer

steps - the current time-step number

time - the current time

u - the current solution (unused; the current TS solution is fetched)

mctx - the TSMonitorDMDARayCtx context

This is not called directly by users; pass this function to TSMonitorSet() along with a context that has been populated with the scatter and viewer describing the ray.

TS: Scalable ODE and DAE Solvers, TS, DMDA, TSMonitorSet(), TSMonitorLGDMDARay(), TSMonitorDMDARayDestroy()

src/ts/utils/dmdats.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h" 
#include "petscts.h" 
PetscErrorCode TSMonitorDMDARay(TS ts, PetscInt steps, PetscReal time, Vec u, void *mctx)
```

Example 2 (unknown):
```unknown
TSMonitorDMDARayCtx
```

Example 3 (unknown):
```unknown
TSMonitorSet()
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorDrawCtxCreate#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorDrawCtxCreate/

**Contents:**
- TSMonitorDrawCtxCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#

Creates the monitor context for TSMonitorDrawCtx

comm - the MPI communicator to use

host - the X display to open, or NULL for the local machine

label - the title to put in the title bar

x - the x screen coordinates of the upper left coordinate of the window

y - the y screen coordinates of the upper left coordinate of the window

m - the screen width in pixels

n - the screen height in pixels

howoften - if positive then determines the frequency of the plotting, if -1 then only at the final time

ctx - the monitor context

-ts_monitor_draw_solution - draw the solution at each time-step

-ts_monitor_draw_solution_initial - show initial solution as well as current solution

The context created by this function, PetscMonitorDrawSolution(), and TSMonitorDrawCtxDestroy() should be passed together to TSMonitorSet().

TS: Scalable ODE and DAE Solvers, TS, TSMonitorDrawCtxDestroy(), TSMonitorSet(), TSMonitorDefault(), VecView(), TSMonitorDrawCtx, PetscMonitorDrawSolution()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorDrawCtx
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorDrawCtxCreate(MPI_Comm comm, const char host[], const char label[], int x, int y, int m, int n, PetscInt howoften, TSMonitorDrawCtx *ctx)
```

Example 3 (unknown):
```unknown
PetscMonitorDrawSolution()
```

Example 4 (unknown):
```unknown
TSMonitorDrawCtxDestroy()
```

---

## TSMonitorDrawCtxDestroy#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorDrawCtxDestroy/

**Contents:**
- TSMonitorDrawCtxDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Destroys the monitor context for TSMonitorDrawSolution()

ictx - the monitor context

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet(), TSMonitorDefault(), VecView(), TSMonitorDrawSolution(), TSMonitorDrawError(), TSMonitorDrawCtx

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorDrawSolution()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorDrawCtxDestroy(TSMonitorDrawCtx *ictx)
```

Example 3 (unknown):
```unknown
TSMonitorSet()
```

Example 4 (unknown):
```unknown
TSMonitorDefault()
```

---

## TSMonitorDrawCtx#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorDrawCtx/

**Contents:**
- TSMonitorDrawCtx#
- Synopsis#
- See Also#
- Level#
- Location#

Context object for the TS graphical monitor routines that draw the solution, phase plot or error using a PetscDraw

TS, TSMonitorDrawCtxCreate(), TSMonitorDrawCtxDestroy(), TSMonitorDrawSolution(), TSMonitorDrawSolutionPhase(), TSMonitorDrawError(), TSMonitorDrawSolutionFunction()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (c):
```c
#include <petscts.h> 
typedef struct _n_TSMonitorDrawCtx *TSMonitorDrawCtx;
```

Example 2 (unknown):
```unknown
TSMonitorDrawCtxCreate()
```

Example 3 (unknown):
```unknown
TSMonitorDrawCtxDestroy()
```

Example 4 (unknown):
```unknown
TSMonitorDrawSolution()
```

---

## TSMonitorDrawError#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorDrawError/

**Contents:**
- TSMonitorDrawError#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Monitors progress of the TS solvers by calling VecView() for the error at each timestep

step - current time-step

u - solution at current time

Ctx - either a viewer or NULL

-ts_monitor_draw_error - Monitor error graphically, requires user to have provided TSSetSolutionFunction()

This is not called directly by users, rather one calls TSMonitorSet(), with this function as an argument, to cause the monitor to be used during the TS integration.

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet(), TSMonitorDefault(), VecView(), TSSetSolutionFunction()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorDrawError(TS ts, PetscInt step, PetscReal ptime, Vec u, PetscCtx Ctx)
```

Example 2 (unknown):
```unknown
TSSetSolutionFunction()
```

Example 3 (unknown):
```unknown
TSMonitorSet()
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorDrawSolutionFunction#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorDrawSolutionFunction/

**Contents:**
- TSMonitorDrawSolutionFunction#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Monitors progress of the TS solvers by calling VecView() for the solution provided by TSSetSolutionFunction() at each timestep

step - current time-step

u - solution at current time

Ctx - either a viewer or NULL

-ts_monitor_draw_solution_function - Monitor error graphically, requires user to have provided TSSetSolutionFunction()

This is not called directly by users, rather one calls TSMonitorSet(), with this function as an argument, to cause the monitor to be used during the TS integration.

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet(), TSMonitorDefault(), VecView(), TSSetSolutionFunction()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetSolutionFunction()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorDrawSolutionFunction(TS ts, PetscInt step, PetscReal ptime, Vec u, PetscCtx Ctx)
```

Example 3 (unknown):
```unknown
TSSetSolutionFunction()
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorDrawSolutionPhase#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorDrawSolutionPhase/

**Contents:**
- TSMonitorDrawSolutionPhase#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Monitors progress of the TS solvers by plotting the solution as a phase diagram

step - current time-step

u - the solution at the current time

ctx - either a viewer or NULL

This is not called directly by users, rather one calls TSMonitorSet(), with this function as an argument, to cause the monitor to be used during the TS integration.

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet(), TSMonitorDefault(), VecView()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorDrawSolutionPhase(TS ts, PetscInt step, PetscReal ptime, Vec u, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSMonitorSet()
```

Example 3 (unknown):
```unknown
TSMonitorSet()
```

Example 4 (unknown):
```unknown
TSMonitorDefault()
```

---

## TSMonitorDrawSolution#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorDrawSolution/

**Contents:**
- TSMonitorDrawSolution#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#

Monitors progress of the TS solvers by calling VecView() for the solution at each timestep

step - current time-step

u - the solution at the current time

ctx - either a viewer or NULL

-ts_monitor_draw_solution - draw the solution at each time-step

-ts_monitor_draw_solution_initial - show initial solution as well as current solution

The initial solution and current solution are not displayed with a common axis scaling so generally the option -ts_monitor_draw_solution_initial will look bad

This is not called directly by users, rather one calls TSMonitorSet(), with this function as an argument, as well as the context created with TSMonitorDrawCtxCreate() and the function TSMonitorDrawCtxDestroy() to cause the monitor to be used during the TS integration.

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet(), TSMonitorDefault(), VecView(), TSMonitorDrawCtxCreate(), TSMonitorDrawCtxDestroy()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorDrawSolution(TS ts, PetscInt step, PetscReal ptime, Vec u, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
-ts_monitor_draw_solution_initial
```

Example 3 (unknown):
```unknown
TSMonitorSet()
```

Example 4 (unknown):
```unknown
TSMonitorDrawCtxCreate()
```

---

## TSMonitorEnvelopeCtxCreate#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorEnvelopeCtxCreate/

**Contents:**
- TSMonitorEnvelopeCtxCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Creates a context for use with TSMonitorEnvelope()

ts - the TS solver object

TS: Scalable ODE and DAE Solvers, TS, TSMonitorLGTimeStep(), TSMonitorSet(), TSMonitorLGSolution(), TSMonitorLGError()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorEnvelope()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorEnvelopeCtxCreate(TS ts, TSMonitorEnvelopeCtx *ctx)
```

Example 3 (unknown):
```unknown
TSMonitorLGTimeStep()
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorEnvelopeCtxDestroy#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorEnvelopeCtxDestroy/

**Contents:**
- TSMonitorEnvelopeCtxDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Destroys a context that was created with TSMonitorEnvelopeCtxCreate().

ctx - the monitor context

TS: Scalable ODE and DAE Solvers, TS, TSMonitorLGCtxCreate(), TSMonitorSet(), TSMonitorLGTimeStep()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorEnvelopeCtxCreate()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorEnvelopeCtxDestroy(TSMonitorEnvelopeCtx *ctx)
```

Example 3 (unknown):
```unknown
TSMonitorLGCtxCreate()
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorEnvelopeCtx#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorEnvelopeCtx/

**Contents:**
- TSMonitorEnvelopeCtx#
- Synopsis#
- See Also#
- Level#
- Location#

Context object for the TSMonitorEnvelope() monitor that tracks the per-component min/max envelope of the solution over a time integration

TS, TSMonitorEnvelopeCtxCreate(), TSMonitorEnvelopeCtxDestroy(), TSMonitorEnvelope(), TSMonitorEnvelopeGetBounds()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorEnvelope()
```

Example 2 (c):
```c
#include <petscts.h> 
typedef struct _n_TSMonitorEnvelopeCtx *TSMonitorEnvelopeCtx;
```

Example 3 (unknown):
```unknown
TSMonitorEnvelopeCtxCreate()
```

Example 4 (unknown):
```unknown
TSMonitorEnvelopeCtxDestroy()
```

---

## TSMonitorEnvelopeGetBounds#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorEnvelopeGetBounds/

**Contents:**
- TSMonitorEnvelopeGetBounds#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Gets the bounds for the components of the solution

max - the maximum values

min - the minimum values

If the TS does not have a TSMonitorEnvelopeCtx associated with it then this function is ignored

TS: Scalable ODE and DAE Solvers, TSMonitorEnvelopeCtx, TS, TSMonitorSet(), TSMonitorDefault(), VecView(), TSMonitorLGSetDisplayVariables()

src/ts/interface/tsmon.c

src/ts/tutorials/extchem.c src/ts/tutorials/extchemfield.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorEnvelopeGetBounds(TS ts, Vec *max, Vec *min)
```

Example 2 (unknown):
```unknown
TSMonitorEnvelopeCtx
```

Example 3 (unknown):
```unknown
TSMonitorEnvelopeCtx
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorEnvelope#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorEnvelope/

**Contents:**
- TSMonitorEnvelope#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Monitors the maximum and minimum value of each component of the solution

step - current time-step

dctx - the envelope context

-ts_monitor_envelope - determine maximum and minimum value of each component of the solution over the solution time

After a solve you can use TSMonitorEnvelopeGetBounds() to access the envelope

This is not called directly by users, rather one calls TSMonitorSet(), with this function as an argument, to cause the monitor to be used during the TS integration.

TS: Scalable ODE and DAE Solvers, TSMonitorSet(), TSMonitorDefault(), VecView(), TSMonitorEnvelopeGetBounds(), TSMonitorEnvelopeCtxCreate()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorEnvelope(TS ts, PetscInt step, PetscReal ptime, Vec u, PetscCtx dctx)
```

Example 2 (unknown):
```unknown
TSMonitorEnvelopeGetBounds()
```

Example 3 (unknown):
```unknown
TSMonitorSet()
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorError#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorError/

**Contents:**
- TSMonitorError#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Monitors progress of the TS solvers by printing the 2 norm of the error at each timestep

step - current time-step

-ts_monitor_error - create a graphical monitor of error history

This is not called directly by users, rather one calls TSMonitorSet(), with this function as an argument, to cause the monitor to be used during the TS integration.

The user must provide the solution using TSSetSolutionFunction() to use this monitor.

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet(), TSMonitorDefault(), VecView(), TSSetSolutionFunction()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorError(TS ts, PetscInt step, PetscReal ptime, Vec u, PetscViewerAndFormat *vf)
```

Example 2 (unknown):
```unknown
TSMonitorSet()
```

Example 3 (unknown):
```unknown
TSSetSolutionFunction()
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorExtreme#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorExtreme/

**Contents:**
- TSMonitorExtreme#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Prints the extreme values of the solution at each timestep

step - iteration number (after the final time step the monitor routine may be called with a step of -1, this indicates the solution has been interpolated to this time)

vf - the viewer and format

This is not called directly by users, rather one calls TSMonitorSet(), with this function as an argument, to cause the monitor to be used during the TS integration.

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorExtreme(TS ts, PetscInt step, PetscReal ptime, Vec v, PetscViewerAndFormat *vf)
```

Example 2 (unknown):
```unknown
TSMonitorSet()
```

Example 3 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorHGCtxCreate#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorHGCtxCreate/

**Contents:**
- TSMonitorHGCtxCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Creates a TSMonitorHGCtx histogram monitor context for use with DMSWARM particle visualizations

comm - the MPI communicator to use

host - the X display to open, or NULL for the local machine

label - the title to put in the title bar

x - the x screen coordinates of the upper left coordinate of the window

y - the y screen coordinates of the upper left coordinate of the window

m - the screen width in pixels

n - the screen height in pixels

howoften - if positive then determines the frequency of the plotting, if -1 then only at the final time

Ns - the number of species to histogram

Nb - the number of histogram bins

velocity - PETSC_TRUE to plot histograms in velocity space, PETSC_FALSE for coordinate space

ctx - the newly created histogram monitor context

Pass this context and TSMonitorHGCtxDestroy() to TSMonitorSet() with TSMonitorHGSwarmSolution() to display particle histograms during integration.

TS: Scalable ODE and DAE Solvers, TS, DMSWARM, TSMonitorSet(), TSMonitorHGSwarmSolution(), TSMonitorHGCtxDestroy()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorHGCtx
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorHGCtxCreate(MPI_Comm comm, const char host[], const char label[], int x, int y, int m, int n, PetscInt howoften, PetscInt Ns, PetscInt Nb, PetscBool velocity, TSMonitorHGCtx *ctx)
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (unknown):
```unknown
TSMonitorHGCtxDestroy()
```

---

## TSMonitorHGCtxDestroy#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorHGCtxDestroy/

**Contents:**
- TSMonitorHGCtxDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Destroys a TSMonitorHGCtx that was created with TSMonitorHGCtxCreate()

ctx - the histogram monitor context

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet(), TSMonitorHGCtxCreate(), TSMonitorHGSwarmSolution()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorHGCtx
```

Example 2 (unknown):
```unknown
TSMonitorHGCtxCreate()
```

Example 3 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorHGCtxDestroy(TSMonitorHGCtx *ctx)
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorHGCtx#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorHGCtx/

**Contents:**
- TSMonitorHGCtx#
- Synopsis#
- See Also#
- Level#
- Location#

Context object for the TSMonitorHGSwarmSolution() histogram monitor that displays a histogram of DMSWARM particle quantities at each time step

TS, DMSWARM, TSMonitorHGCtxCreate(), TSMonitorHGCtxDestroy(), TSMonitorHGSwarmSolution()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorHGSwarmSolution()
```

Example 2 (c):
```c
#include <petscts.h> 
typedef struct _n_TSMonitorHGCtx *TSMonitorHGCtx;
```

Example 3 (unknown):
```unknown
TSMonitorHGCtxCreate()
```

Example 4 (unknown):
```unknown
TSMonitorHGCtxDestroy()
```

---

## TSMonitorHGSwarmSolution#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorHGSwarmSolution/

**Contents:**
- TSMonitorHGSwarmSolution#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#

Graphically displays histograms of DMSWARM particles

step - current time-step

dctx - the TSMonitorSPCtx object that contains all the options for the monitoring, this is created with TSMonitorHGCtxCreate()

-ts_monitor_hg_swarm n - Monitor the solution every n steps, or -1 for plotting only the final solution

-ts_monitor_hg_swarm_species num - Number of species to histogram

-ts_monitor_hg_swarm_bins num - Number of histogram bins

-ts_monitor_hg_swarm_velocity (true|false) - Plot in velocity space, as opposed to coordinate space

This is not called directly by users, rather one calls TSMonitorSet(), with this function as an argument, to cause the monitor to be used during the TS integration.

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorHGSwarmSolution(TS ts, PetscInt step, PetscReal ptime, Vec u, PetscCtx dctx)
```

Example 2 (unknown):
```unknown
TSMonitorSPCtx
```

Example 3 (unknown):
```unknown
TSMonitorHGCtxCreate()
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorLGCtxCreate#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorLGCtxCreate/

**Contents:**
- TSMonitorLGCtxCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates a TSMonitorLGCtx context for use with TS to monitor the solution process graphically in various ways

comm - the MPI communicator to use

host - the X display to open, or NULL for the local machine

label - the title to put in the title bar

x - the x screen coordinates of the upper left coordinate of the window

y - the y screen coordinates of the upper left coordinate of the window

m - the screen width in pixels

n - the screen height in pixels

howoften - if positive then determines the frequency of the plotting, if -1 then only at the final time

-ts_monitor_lg_timestep - automatically sets line graph monitor

-ts_monitor_lg_timestep_log - automatically sets line graph monitor

-ts_monitor_lg_solution - monitor the solution (or certain values of the solution by calling TSMonitorLGSetDisplayVariables() or TSMonitorLGCtxSetDisplayVariables())

-ts_monitor_lg_error - monitor the error

-ts_monitor_lg_ksp_iterations - monitor the number of KSP iterations needed for each timestep

-ts_monitor_lg_snes_iterations - monitor the number of SNES iterations needed for each timestep

-lg_use_markers (true|false) - mark the data points (at each time step) on the plot; default is true

Pass the context and TSMonitorLGCtxDestroy() to TSMonitorSet() to have the context destroyed when no longer needed.

One can provide a function that transforms the solution before plotting it with TSMonitorLGCtxSetTransform() or TSMonitorLGSetTransform()

Many of the functions that control the monitoring have two forms: TSMonitorLGSet/GetXXXX() and TSMonitorLGCtxSet/GetXXXX() the first take a TS object as the first argument (if that TS object does not have a TSMonitorLGCtx associated with it the function call is ignored) and the second takes a TSMonitorLGCtx object as the first argument.

One can control the names displayed for each solution or error variable with TSMonitorLGCtxSetVariableNames() or TSMonitorLGSetVariableNames()

TS: Scalable ODE and DAE Solvers, TSMonitorLGTimeStep(), TSMonitorSet(), TSMonitorLGSolution(), TSMonitorLGError(), TSMonitorDefault(), VecView(), TSMonitorLGCtxSetVariableNames(), TSMonitorLGCtxGetVariableNames(), TSMonitorLGSetVariableNames(), TSMonitorLGGetVariableNames(), TSMonitorLGSetDisplayVariables(), TSMonitorLGCtxSetDisplayVariables(), TSMonitorLGCtxSetTransform(), TSMonitorLGSetTransform(), TSMonitorLGSNESIterations(), TSMonitorLGKSPIterations(), TSMonitorEnvelopeCtxCreate(), TSMonitorEnvelopeGetBounds(), TSMonitorEnvelopeCtxDestroy(), TSMonitorEnvelop()

src/ts/interface/tsmon.c

src/ts/tutorials/extchemfield.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorLGCtx
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorLGCtxCreate(MPI_Comm comm, const char host[], const char label[], int x, int y, int m, int n, PetscInt howoften, TSMonitorLGCtx *ctx)
```

Example 3 (unknown):
```unknown
TSMonitorLGSetDisplayVariables()
```

Example 4 (unknown):
```unknown
TSMonitorLGCtxSetDisplayVariables()
```

---

## TSMonitorLGCtxDestroy#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorLGCtxDestroy/

**Contents:**
- TSMonitorLGCtxDestroy#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#

Destroys a line graph context that was created with TSMonitorLGCtxCreate().

ctx - the monitor context

Pass to TSMonitorSet() along with the context and TSMonitorLGTimeStep()

TS: Scalable ODE and DAE Solvers, TS, TSMonitorLGCtxCreate(), TSMonitorSet(), TSMonitorLGTimeStep()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorLGCtxCreate()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorLGCtxDestroy(TSMonitorLGCtx *ctx)
```

Example 3 (unknown):
```unknown
TSMonitorSet()
```

Example 4 (unknown):
```unknown
TSMonitorLGTimeStep()
```

---

## TSMonitorLGCtxNetworkCreate#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorLGCtxNetworkCreate/

**Contents:**
- TSMonitorLGCtxNetworkCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Creates a TSMonitorLGCtxNetwork context with one line-graph window for each edge and each vertex of a DMNETWORK

ts - the TS context whose DM is a DMNETWORK

host - the X display to open, or NULL for the local machine

label - the title to put in the title bar

x - the x screen coordinates of the upper left coordinate of the window

y - the y screen coordinates of the upper left coordinate of the window

m - the screen width in pixels

n - the screen height in pixels

howoften - if positive then determines the frequency of the plotting, if -1 then only at the final time

ctx - the newly created network line-graph monitor context

Pass this context and TSMonitorLGCtxNetworkDestroy() to TSMonitorSet() with TSMonitorLGCtxNetworkSolution() to display the solution on the network during integration.

TS: Scalable ODE and DAE Solvers, TS, DMNETWORK, TSMonitorSet(), TSMonitorLGCtxNetworkSolution(), TSMonitorLGCtxNetworkDestroy()

src/ts/utils/dmnetworkts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorLGCtxNetwork
```

Example 2 (unknown):
```unknown
#include "petscdmplex.h" 
PetscErrorCode TSMonitorLGCtxNetworkCreate(TS ts, const char host[], const char label[], int x, int y, int m, int n, PetscInt howoften, TSMonitorLGCtxNetwork *ctx)
```

Example 3 (unknown):
```unknown
TSMonitorLGCtxNetworkDestroy()
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorLGCtxNetworkDestroy#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorLGCtxNetworkDestroy/

**Contents:**
- TSMonitorLGCtxNetworkDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Destroys line graph contexts that where created with TSMonitorLGCtxNetworkCreate().

ctx - the monitor context

TS: Scalable ODE and DAE Solvers, TS, TSMonitorLGCtxNetworkSolution()

src/ts/utils/dmnetworkts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorLGCtxNetworkCreate()
```

Example 2 (unknown):
```unknown
#include "petscdmplex.h" 
PetscErrorCode TSMonitorLGCtxNetworkDestroy(TSMonitorLGCtxNetwork *ctx)
```

Example 3 (unknown):
```unknown
TSMonitorLGCtxNetworkSolution()
```

---

## TSMonitorLGCtxNetworkSolution#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorLGCtxNetworkSolution/

**Contents:**
- TSMonitorLGCtxNetworkSolution#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Monitors progress of the TS solvers for a DMNETWORK solution with one window for each vertex and each edge

step - current time-step

dctx - the TSMonitorLGCtxNetwork object that contains all the options for the monitoring, this is created with TSMonitorLGCtxCreateNetwork()

-ts_monitor_lg_solution_variables - monitor solution variables

Each process in a parallel run displays its component solutions in a separate graphics window

TS: Scalable ODE and DAE Solvers, TS, TSMonitorLGCtxNetworkDestroy()

src/ts/utils/dmnetworkts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
PetscErrorCode TSMonitorLGCtxNetworkSolution(TS ts, PetscInt step, PetscReal ptime, Vec u, void *dctx)
```

Example 2 (unknown):
```unknown
TSMonitorLGCtxNetwork
```

Example 3 (unknown):
```unknown
TSMonitorLGCtxCreateNetwork()
```

Example 4 (unknown):
```unknown
TSMonitorLGCtxNetworkDestroy()
```

---

## TSMonitorLGCtxNetwork#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorLGCtxNetwork/

**Contents:**
- TSMonitorLGCtxNetwork#
- Synopsis#
- See Also#
- Level#
- Location#

Context object for the TSMonitorLGCtxNetworkSolution() line-graph monitor that plots solution components on each subnetwork of a DMNETWORK

TS, DMNETWORK, TSMonitorLGCtxNetworkCreate(), TSMonitorLGCtxNetworkDestroy(), TSMonitorLGCtxNetworkSolution()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorLGCtxNetworkSolution()
```

Example 2 (c):
```c
#include <petscts.h> 
typedef struct _n_TSMonitorLGCtxNetwork *TSMonitorLGCtxNetwork;
```

Example 3 (unknown):
```unknown
TSMonitorLGCtxNetworkCreate()
```

Example 4 (unknown):
```unknown
TSMonitorLGCtxNetworkDestroy()
```

---

## TSMonitorLGCtxSetDisplayVariables#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorLGCtxSetDisplayVariables/

**Contents:**
- TSMonitorLGCtxSetDisplayVariables#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the variables that are to be display in the monitor

ctx - the TSMonitorLG context

displaynames - the names of the components, final string must be NULL

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet(), TSMonitorDefault(), VecView(), TSMonitorLGSetVariableNames()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorLGCtxSetDisplayVariables(TSMonitorLGCtx ctx, const char *const *displaynames)
```

Example 2 (unknown):
```unknown
TSMonitorLG
```

Example 3 (unknown):
```unknown
TSMonitorSet()
```

Example 4 (unknown):
```unknown
TSMonitorDefault()
```

---

## TSMonitorLGCtxSetTransform#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorLGCtxSetTransform/

**Contents:**
- TSMonitorLGCtxSetTransform#
- Synopsis#
- Input Parameters#
- Calling sequence of transform#
- See Also#
- Level#
- Location#
- Examples#

Solution vector will be transformed by provided function before being displayed

tctx - the TS context

transform - the transform function

destroy - function to destroy the optional context, see PetscCtxDestroyFn for its calling sequence

ctx - optional context used by transform function

tctx - context used by the transform function

u - the input solution vector

w - the output transformed vector

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet(), TSMonitorDefault(), VecView(), TSMonitorLGSetVariableNames(), TSMonitorLGSetTransform(), PetscCtxDestroyFn

src/ts/interface/tsmon.c

src/ts/tutorials/extchemfield.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (csharp):
```csharp
#include "petscts.h"  
PetscErrorCode TSMonitorLGCtxSetTransform(TSMonitorLGCtx ctx, PetscErrorCode (*transform)(PetscCtx tctx, Vec u, Vec *w), PetscCtxDestroyFn *destroy, PetscCtx tctx)
```

Example 2 (unknown):
```unknown
PetscCtxDestroyFn
```

Example 3 (unknown):
```unknown
TSMonitorSet()
```

Example 4 (unknown):
```unknown
TSMonitorDefault()
```

---

## TSMonitorLGCtxSetVariableNames#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorLGCtxSetVariableNames/

**Contents:**
- TSMonitorLGCtxSetVariableNames#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the name of each component in the solution vector so that it may be displayed in the plot

names - the names of the components, final string must be NULL

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet(), TSMonitorDefault(), VecView(), TSMonitorLGSetDisplayVariables(), TSMonitorLGSetVariableNames()

src/ts/interface/tsmon.c

src/ts/tutorials/extchemfield.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorLGCtxSetVariableNames(TSMonitorLGCtx ctx, const char *const *names)
```

Example 2 (unknown):
```unknown
TSMonitorSet()
```

Example 3 (unknown):
```unknown
TSMonitorDefault()
```

Example 4 (unknown):
```unknown
TSMonitorLGSetDisplayVariables()
```

---

## TSMonitorLGCtx#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorLGCtx/

**Contents:**
- TSMonitorLGCtx#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#

Context object for TS line-graph monitor routines that plot residuals, iteration counts or solution components at each time step on a PetscDrawLG

TS, TSMonitorLGCtxCreate(), TSMonitorLGCtxDestroy(), TSMonitorLGSolution(), TSMonitorLGTimeStep(), TSMonitorLGError()

src/ts/tutorials/extchemfield.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDrawLG
```

Example 2 (c):
```c
#include <petscts.h> 
typedef struct _n_TSMonitorLGCtx *TSMonitorLGCtx;
```

Example 3 (unknown):
```unknown
TSMonitorLGCtxCreate()
```

Example 4 (unknown):
```unknown
TSMonitorLGCtxDestroy()
```

---

## TSMonitorLGDMDARay#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorLGDMDARay/

**Contents:**
- TSMonitorLGDMDARay#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Monitors the solution of a DMDA-based TS by plotting values along a ray in a line graph

step - the current time-step number

ptime - the current time

u - the current solution

ctx - the TSMonitorDMDARayCtx context, which contains the ray scatter and an embedded TSMonitorLGCtx

This is not called directly by users; pass this function to TSMonitorSet() together with the context and TSMonitorDMDARayDestroy().

TS: Scalable ODE and DAE Solvers, TS, DMDA, TSMonitorSet(), TSMonitorDMDARay(), TSMonitorDMDARayDestroy()

src/ts/utils/dmdats.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmda.h" 
#include "petscts.h" 
PetscErrorCode TSMonitorLGDMDARay(TS ts, PetscInt step, PetscReal ptime, Vec u, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSMonitorDMDARayCtx
```

Example 3 (unknown):
```unknown
TSMonitorLGCtx
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorLGError#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorLGError/

**Contents:**
- TSMonitorLGError#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Monitors progress of the TS solvers by plotting each component of the error in a time based line graph

step - current time-step

Ctx - TSMonitorLGCtx object created with TSMonitorLGCtxCreate()

-ts_monitor_lg_error - create a graphical monitor of error history

Each process in a parallel run displays its component errors in a separate window

The user must provide the solution using TSSetSolutionFunction() to use this monitor.

This is not called directly by users, rather one calls TSMonitorSet(), with this function as an argument, to cause the monitor to be used during the TS integration.

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet(), TSMonitorDefault(), VecView(), TSSetSolutionFunction()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorLGError(TS ts, PetscInt step, PetscReal ptime, Vec u, PetscCtx Ctx)
```

Example 2 (unknown):
```unknown
TSMonitorLGCtx
```

Example 3 (unknown):
```unknown
TSMonitorLGCtxCreate()
```

Example 4 (unknown):
```unknown
TSSetSolutionFunction()
```

---

## TSMonitorLGGetVariableNames#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorLGGetVariableNames/

**Contents:**
- TSMonitorLGGetVariableNames#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets the name of each component in the solution vector so that it may be displayed in the plot

names - the names of the components, final string must be NULL

If the TS object does not have a TSMonitorLGCtx associated with it then this function is ignored

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet(), TSMonitorDefault(), VecView(), TSMonitorLGSetDisplayVariables()

src/ts/interface/tsmon.c

src/ts/tutorials/extchemfield.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorLGGetVariableNames(TS ts, const char *const **names)
```

Example 2 (unknown):
```unknown
TSMonitorLGCtx
```

Example 3 (unknown):
```unknown
TSMonitorSet()
```

Example 4 (unknown):
```unknown
TSMonitorDefault()
```

---

## TSMonitorLGKSPIterations#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorLGKSPIterations/

**Contents:**
- TSMonitorLGKSPIterations#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Monitors the number of linear (KSP) iterations used per time step in a line-graph plot

n - iteration number (a negative value indicates an interpolated solution and is ignored)

monctx - the TSMonitorLGCtx object that contains all the options for the monitoring, created with TSMonitorLGCtxCreate()

This is not called directly by users; pass this function to TSMonitorSet() along with the context created by TSMonitorLGCtxCreate() and TSMonitorLGCtxDestroy().

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet(), TSMonitorLGCtxCreate(), TSMonitorLGSNESIterations()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorLGKSPIterations(TS ts, PetscInt n, PetscReal ptime, Vec v, PetscCtx monctx)
```

Example 2 (unknown):
```unknown
TSMonitorLGCtx
```

Example 3 (unknown):
```unknown
TSMonitorLGCtxCreate()
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorLGSetDisplayVariables#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorLGSetDisplayVariables/

**Contents:**
- TSMonitorLGSetDisplayVariables#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the variables that are to be display in the monitor

displaynames - the names of the components, final string must be NULL

If the TS object does not have a TSMonitorLGCtx associated with it then this function is ignored

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet(), TSMonitorDefault(), VecView(), TSMonitorLGSetVariableNames()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorLGSetDisplayVariables(TS ts, const char *const *displaynames)
```

Example 2 (unknown):
```unknown
TSMonitorLGCtx
```

Example 3 (unknown):
```unknown
TSMonitorSet()
```

Example 4 (unknown):
```unknown
TSMonitorDefault()
```

---

## TSMonitorLGSetTransform#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorLGSetTransform/

**Contents:**
- TSMonitorLGSetTransform#
- Synopsis#
- Input Parameters#
- Calling sequence of transform#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Solution vector will be transformed by provided function before being displayed

transform - the transform function

destroy - function to destroy the optional context, see PetscCtxDestroyFn for its calling sequence

tctx - optional context used by transform function

tctx - context used by the transform function

u - the input solution vector

w - the output transformed vector

If the TS object does not have a TSMonitorLGCtx associated with it then this function is ignored

TS: Scalable ODE and DAE Solvers, TSMonitorSet(), TSMonitorLGCtxSetTransform(), TSMonitorDefault(), VecView(), TSMonitorLGSetVariableNames(), PetscCtxDestroyFn

src/ts/interface/tsmon.c

src/ts/tutorials/extchem.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (csharp):
```csharp
#include "petscts.h"  
PetscErrorCode TSMonitorLGSetTransform(TS ts, PetscErrorCode (*transform)(PetscCtx tctx, Vec u, Vec *w), PetscCtxDestroyFn *destroy, PetscCtx tctx)
```

Example 2 (unknown):
```unknown
PetscCtxDestroyFn
```

Example 3 (unknown):
```unknown
TSMonitorLGCtx
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorLGSetVariableNames#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorLGSetVariableNames/

**Contents:**
- TSMonitorLGSetVariableNames#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the name of each component in the solution vector so that it may be displayed in the plot

names - the names of the components, final string must be NULL

If the TS object does not have a TSMonitorLGCtx associated with it then this function is ignored

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet(), TSMonitorDefault(), VecView(), TSMonitorLGSetDisplayVariables(), TSMonitorLGCtxSetVariableNames()

src/ts/interface/tsmon.c

src/ts/tutorials/extchem.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorLGSetVariableNames(TS ts, const char *const *names)
```

Example 2 (unknown):
```unknown
TSMonitorLGCtx
```

Example 3 (unknown):
```unknown
TSMonitorSet()
```

Example 4 (unknown):
```unknown
TSMonitorDefault()
```

---

## TSMonitorLGSNESIterations#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorLGSNESIterations/

**Contents:**
- TSMonitorLGSNESIterations#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Monitors the number of nonlinear (SNES) iterations used per time step in a line-graph plot

n - iteration number (a negative value indicates an interpolated solution and is ignored)

monctx - the TSMonitorLGCtx object that contains all the options for the monitoring, created with TSMonitorLGCtxCreate()

This is not called directly by users; pass this function to TSMonitorSet() along with the context created by TSMonitorLGCtxCreate() and TSMonitorLGCtxDestroy().

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet(), TSMonitorLGCtxCreate(), TSMonitorLGKSPIterations()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorLGSNESIterations(TS ts, PetscInt n, PetscReal ptime, Vec v, PetscCtx monctx)
```

Example 2 (unknown):
```unknown
TSMonitorLGCtx
```

Example 3 (unknown):
```unknown
TSMonitorLGCtxCreate()
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorLGSolution#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorLGSolution/

**Contents:**
- TSMonitorLGSolution#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Monitors progress of the TS solvers by plotting each component of the solution vector in a time based line graph

step - current time-step

dctx - the TSMonitorLGCtx object that contains all the options for the monitoring, this is created with TSMonitorLGCtxCreate()

-ts_monitor_lg_solution_variables - enable monitor of lg solution variables

Each process in a parallel run displays its component solutions in a separate window

This is not called directly by users, rather one calls TSMonitorSet(), with this function as an argument, to cause the monitor to be used during the TS integration.

TS: Scalable ODE and DAE Solvers, TSMonitorSet(), TSMonitorDefault(), VecView(), TSMonitorLGCtxCreate(), TSMonitorLGCtxSetVariableNames(), TSMonitorLGCtxGetVariableNames(), TSMonitorLGSetVariableNames(), TSMonitorLGGetVariableNames(), TSMonitorLGSetDisplayVariables(), TSMonitorLGCtxSetDisplayVariables(), TSMonitorLGCtxSetTransform(), TSMonitorLGSetTransform(), TSMonitorLGError(), TSMonitorLGSNESIterations(), TSMonitorLGKSPIterations(), TSMonitorEnvelopeCtxCreate(), TSMonitorEnvelopeGetBounds(), TSMonitorEnvelopeCtxDestroy(), TSMonitorEnvelop()

src/ts/interface/tsmon.c

src/ts/tutorials/extchemfield.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorLGSolution(TS ts, PetscInt step, PetscReal ptime, Vec u, void *dctx)
```

Example 2 (unknown):
```unknown
TSMonitorLGCtx
```

Example 3 (unknown):
```unknown
TSMonitorLGCtxCreate()
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorLGTimeStep#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorLGTimeStep/

**Contents:**
- TSMonitorLGTimeStep#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Monitors a TS by printing the time-steps

ts - the time integrator

step - the current time step

ptime - the current time

v - the current state

monctx - the monitor context obtained with TSMonitorLGCtxCreate()

This is not called directly by users, rather one calls TSMonitorSet() along the ctx created by TSMonitorLGCtxCreate() and TSMonitorLGCtxDestroy()

TS: Scalable ODE and DAE Solvers, TS, TSMonitorLGCtxCreate(), TSMonitorSet(), TSMonitorLGCtxDestroy()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorLGTimeStep(TS ts, PetscInt step, PetscReal ptime, Vec v, PetscCtx monctx)
```

Example 2 (unknown):
```unknown
TSMonitorLGCtxCreate()
```

Example 3 (unknown):
```unknown
TSMonitorSet()
```

Example 4 (unknown):
```unknown
TSMonitorLGCtxCreate()
```

---

## TSMonitorSetFromOptions#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorSetFromOptions/

**Contents:**
- TSMonitorSetFromOptions#
- Synopsis#
- Input Parameters#
- Calling sequence of monitor#
- Calling sequence of monitorsetup#
- See Also#
- Level#
- Location#

Sets a monitor function and viewer appropriate for the type indicated by the user

ts - TS object you wish to monitor

name - the monitor type one is seeking

help - message indicating what monitoring is done

manual - manual page for the monitor

monitor - the monitor function, this must use a PetscViewerFormat as its context

monitorsetup - a function that is called once ONLY if the user selected this monitor that may set additional features of the TS or PetscViewer objects

ts - the TS to monitor

step - the current time-step

time - the current time

u - the current solution

vf - the PetscViewer and format to monitor with

ts - the TS to monitor

vf - the PetscViewer and format to monitor with

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet(), PetscOptionsCreateViewer(), PetscOptionsGetReal(), PetscOptionsHasName(), PetscOptionsGetString(), PetscOptionsGetIntArray(), PetscOptionsGetRealArray(), PetscOptionsBool(), PetscOptionsInt(), PetscOptionsString(), PetscOptionsReal(), PetscOptionsName(), PetscOptionsBegin(), PetscOptionsEnd(), PetscOptionsHeadBegin(), PetscOptionsStringArray(), PetscOptionsRealArray(), PetscOptionsScalar(), PetscOptionsBoolGroupBegin(), PetscOptionsBoolGroup(), PetscOptionsBoolGroupEnd(), PetscOptionsFList(), PetscOptionsEList()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorSetFromOptions(TS ts, const char name[], const char help[], const char manual[], PetscErrorCode (*monitor)(TS ts, PetscInt step, PetscReal time, Vec u, PetscViewerAndFormat *vf), PetscErrorCode (*monitorsetup)(TS ts, PetscViewerAndFormat *vf))
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
PetscViewer
```

---

## TSMonitorSet#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorSet/

**Contents:**
- TSMonitorSet#
- Synopsis#
- Input Parameters#
- Calling sequence of monitor#
- Note#
- Fortran Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets an ADDITIONAL function that is to be used at every timestep to display the iteration’s progress.

ts - the TS context obtained from TSCreate()

monitor - monitoring routine

mctx - [optional] user-defined context for private data for the monitor routine (use NULL if no context is desired)

mdestroy - [optional] routine that frees monitor context (may be NULL), see PetscCtxDestroyFn for the calling sequence

steps - iteration number (after the final time step the monitor routine may be called with a step of -1, this indicates the solution has been interpolated to this time)

ctx - [optional] monitoring context

This routine adds an additional monitor to the list of monitors that already has been loaded.

Only a single monitor function can be set for each TS object

TS: Scalable ODE and DAE Solvers, TSMonitorDefault(), TSMonitorCancel(), TSDMSwarmMonitorMoments(), TSMonitorExtreme(), TSMonitorDrawSolution(), TSMonitorDrawSolutionPhase(), TSMonitorDrawSolutionFunction(), TSMonitorDrawError(), TSMonitorSolution(), TSMonitorSolutionVTK(), TSMonitorLGSolution(), TSMonitorLGError(), TSMonitorSPSwarmSolution(), TSMonitorError(), TSMonitorEnvelope(), PetscCtxDestroyFn

src/ts/interface/tsmon.c

src/ts/tutorials/ex14.c src/ts/tutorials/extchem.c src/ts/tutorials/ex20opt_ic.c src/ts/tutorials/ex18.c src/ts/tutorials/ex21.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/utils/dmplexlandau/tutorials/ex2.c src/ts/tutorials/ex12.c src/ts/tutorials/ex16fwd.c src/ts/tutorials/ex47.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorSet(TS ts, PetscErrorCode (*monitor)(TS ts, PetscInt steps, PetscReal time, Vec u, PetscCtx ctx), PetscCtx mctx, PetscCtxDestroyFn *mdestroy)
```

Example 2 (unknown):
```unknown
PetscCtxDestroyFn
```

Example 3 (unknown):
```unknown
TSMonitorDefault()
```

Example 4 (unknown):
```unknown
TSMonitorCancel()
```

---

## TSMonitorSolutionCtx#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorSolutionCtx/

**Contents:**
- TSMonitorSolutionCtx#
- Synopsis#
- See Also#
- Level#
- Location#

Context object for the TS TSMonitorSolution() monitor that views the solution at each time step using a PetscViewer

TS, TSMonitorSet(), TSMonitorSolution(), TSMonitorSolutionSetup()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorSolution()
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (c):
```c
#include <petscts.h> 
typedef struct _n_TSMonitorSolutionCtx *TSMonitorSolutionCtx;
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorSolutionSetup#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorSolutionSetup/

**Contents:**
- TSMonitorSolutionSetup#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Setups the context for TSMonitorSolution()

vf - viewer and its format

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSolution(), TSMonitorSet(), TSMonitorDefault(), VecView(), TSMonitorSetFromOptions()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorSolution()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorSolutionSetup(TS ts, PetscViewerAndFormat *vf)
```

Example 3 (unknown):
```unknown
TSMonitorSolution()
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorSolutionVTKCtxCreate#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorSolutionVTKCtxCreate/

**Contents:**
- TSMonitorSolutionVTKCtxCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Create the monitor context to be used in TSMonitorSolutionVTK()

filenametemplate - the template file name, e.g. foo-%03d.vts

ctx - the monitor context

This function is normally used inside TSSetFromOptions() to pass the context created to TSMonitorSet() along with TSMonitorSolutionVTK().

TS: Scalable ODE and DAE Solvers, TSMonitorSet(), TSMonitorSolutionVTK(), TSMonitorSolutionVTKDestroy()

src/ts/interface/tsmon.c

src/ts/tutorials/ex30.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorSolutionVTK()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorSolutionVTKCtxCreate(const char *filenametemplate, TSMonitorVTKCtx *ctx)
```

Example 3 (unknown):
```unknown
TSSetFromOptions()
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorSolutionVTKDestroy#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorSolutionVTKDestroy/

**Contents:**
- TSMonitorSolutionVTKDestroy#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Destroy the monitor context created with TSMonitorSolutionVTKCtxCreate()

ctx - the monitor context

This function is normally passed to TSMonitorSet() along with TSMonitorSolutionVTK().

TS: Scalable ODE and DAE Solvers, TSMonitorSet(), TSMonitorSolutionVTK()

src/ts/interface/tsmon.c

src/ts/tutorials/ex30.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorSolutionVTKCtxCreate()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorSolutionVTKDestroy(TSMonitorVTKCtx *ctx)
```

Example 3 (unknown):
```unknown
TSMonitorSet()
```

Example 4 (unknown):
```unknown
TSMonitorSolutionVTK()
```

---

## TSMonitorSolutionVTK#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorSolutionVTK/

**Contents:**
- TSMonitorSolutionVTK#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Monitors progress of the TS solvers by VecView() for the solution at selected timesteps.

step - current time-step

ctx - monitor context obtained with TSMonitorSolutionVTKCtxCreate()

The VTK format does not allow writing multiple time steps in the same file, therefore a different file will be written for each time step. These are named according to the file name template.

This is not called directly by users, rather one calls TSMonitorSet(), with this function as an argument, to cause the monitor to be used during the TS integration.

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet(), TSMonitorDefault(), VecView()

src/ts/interface/tsmon.c

src/ts/tutorials/ex30.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorSolutionVTK(TS ts, PetscInt step, PetscReal ptime, Vec u, TSMonitorVTKCtx ctx)
```

Example 2 (unknown):
```unknown
TSMonitorSolutionVTKCtxCreate()
```

Example 3 (unknown):
```unknown
TSMonitorSet()
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorSolution#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorSolution/

**Contents:**
- TSMonitorSolution#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Monitors progress of the TS solvers by VecView() for the solution at each timestep. Normally the viewer is a binary file or a PetscDraw object

step - current time-step

vf - viewer and its format

This is not called directly by users, rather one calls TSMonitorSet(), with this function as an argument, to cause the monitor to be used during the TS integration.

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet(), TSMonitorDefault(), VecView(), TSMonitorSolutionSetup()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorSolution(TS ts, PetscInt step, PetscReal ptime, Vec u, PetscViewerAndFormat *vf)
```

Example 2 (unknown):
```unknown
TSMonitorSet()
```

Example 3 (unknown):
```unknown
TSMonitorSet()
```

Example 4 (unknown):
```unknown
TSMonitorDefault()
```

---

## TSMonitorSPCtxCreate#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorSPCtxCreate/

**Contents:**
- TSMonitorSPCtxCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Creates a TSMonitorSPCtx scatter-plot monitor context for use with DMSWARM particle visualizations

comm - the MPI communicator to use

host - the X display to open, or NULL for the local machine

label - the title to put in the title bar

x - the x screen coordinates of the upper left coordinate of the window

y - the y screen coordinates of the upper left coordinate of the window

m - the screen width in pixels

n - the screen height in pixels

howoften - if positive then determines the frequency of the plotting, if -1 then only at the final time

retain - the number of old points to retain in the plot, or 0 to clear, or -1 to retain all

phase - PETSC_TRUE to plot in phase space rather than coordinate space

multispecies - PETSC_TRUE to color particles by species

ctx - the newly created scatter plot monitor context

Pass this context and TSMonitorSPCtxDestroy() to TSMonitorSet() with TSMonitorSPSwarmSolution() to display particles during the integration.

TS: Scalable ODE and DAE Solvers, TS, DMSWARM, TSMonitorSet(), TSMonitorSPSwarmSolution(), TSMonitorSPCtxDestroy()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorSPCtx
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorSPCtxCreate(MPI_Comm comm, const char host[], const char label[], int x, int y, int m, int n, PetscInt howoften, PetscInt retain, PetscBool phase, PetscBool multispecies, TSMonitorSPCtx *ctx)
```

Example 3 (unknown):
```unknown
TSMonitorSPCtxDestroy()
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorSPCtxDestroy#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorSPCtxDestroy/

**Contents:**
- TSMonitorSPCtxDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Destroys a TSMonitorSPCtx that was created with TSMonitorSPCtxCreate()

ctx - the scatter plot monitor context

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet(), TSMonitorSPCtxCreate(), TSMonitorSPSwarmSolution()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorSPCtx
```

Example 2 (unknown):
```unknown
TSMonitorSPCtxCreate()
```

Example 3 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorSPCtxDestroy(TSMonitorSPCtx *ctx)
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorSPCtx#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorSPCtx/

**Contents:**
- TSMonitorSPCtx#
- Synopsis#
- See Also#
- Level#
- Location#

Context object for the TSMonitorSPSwarmSolution() scatter-plot monitor that draws the swarm particle positions at each time step on a PetscDrawSP

TS, DMSWARM, TSMonitorSPCtxCreate(), TSMonitorSPCtxDestroy(), TSMonitorSPSwarmSolution()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorSPSwarmSolution()
```

Example 2 (unknown):
```unknown
PetscDrawSP
```

Example 3 (c):
```c
#include <petscts.h> 
typedef struct _n_TSMonitorSPCtx *TSMonitorSPCtx;
```

Example 4 (unknown):
```unknown
TSMonitorSPCtxCreate()
```

---

## TSMonitorSPEigCtxCreate#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorSPEigCtxCreate/

**Contents:**
- TSMonitorSPEigCtxCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Creates a context for use with TS to monitor the eigenvalues of the linearized operator

comm - the communicator to share the monitor

host - the X display to open, or NULL for the local machine

label - the title to put in the title bar

x - the horizontal screen coordinates of the upper left coordinate of the window

y - the vertical coordinates of the upper left coordinate of the window

m - the screen width in pixels

n - the screen height in pixels

howoften - if positive then determines the frequency of the plotting, if -1 then only at the final time

-ts_monitor_sp_eig - plot egienvalues of linearized right-hand side

Use TSMonitorSPEigCtxDestroy() to destroy the context

Currently only works if the Jacobian is provided explicitly.

Currently only works for ODEs u_t - F(t,u) = 0; that is with no mass matrix.

TS: Scalable ODE and DAE Solvers, TSMonitorSPEigTimeStep(), TSMonitorSet(), TSMonitorLGSolution(), TSMonitorLGError()

src/ts/interface/tseig.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorSPEigCtxCreate(MPI_Comm comm, const char host[], const char label[], int x, int y, int m, int n, PetscInt howoften, TSMonitorSPEigCtx *ctx)
```

Example 2 (unknown):
```unknown
TSMonitorSPEigCtxDestroy()
```

Example 3 (unknown):
```unknown
TSMonitorSPEigTimeStep()
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorSPEigCtxDestroy#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorSPEigCtxDestroy/

**Contents:**
- TSMonitorSPEigCtxDestroy#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#

Destroys a scatter plot context that was created with TSMonitorSPEigCtxCreate().

ctx - the monitor context

Should be passed to TSMonitorSet() along with TSMonitorSPEig() an the context created with TSMonitorSPEigCtxCreate()

TS: Scalable ODE and DAE Solvers, TSMonitorSPEigCtxCreate(), TSMonitorSet(), TSMonitorSPEig()

src/ts/interface/tseig.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorSPEigCtxCreate()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorSPEigCtxDestroy(TSMonitorSPEigCtx *ctx)
```

Example 3 (unknown):
```unknown
TSMonitorSet()
```

Example 4 (unknown):
```unknown
TSMonitorSPEig()
```

---

## TSMonitorSPEigCtx#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorSPEigCtx/

**Contents:**
- TSMonitorSPEigCtx#
- Synopsis#
- See Also#
- Level#
- Location#

Context object for the TSMonitorSPEig() monitor that displays an estimate of the spectrum of the operator using a PetscDrawSP scatter plot

TS, TSMonitorSPEigCtxCreate(), TSMonitorSPEigCtxDestroy(), TSMonitorSPEig()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorSPEig()
```

Example 2 (unknown):
```unknown
PetscDrawSP
```

Example 3 (c):
```c
#include <petscts.h> 
typedef struct _n_TSMonitorSPEigCtx *TSMonitorSPEigCtx;
```

Example 4 (unknown):
```unknown
TSMonitorSPEigCtxCreate()
```

---

## TSMonitorSPEig#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorSPEig/

**Contents:**
- TSMonitorSPEig#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Monitors the eigenvalues of the linearized right-hand-side operator on a scatter plot at each time step

step - the current time-step number (a negative value indicates an interpolated solution and is ignored)

ptime - the current time

v - the current solution

monctx - the TSMonitorSPEigCtx context, created with TSMonitorSPEigCtxCreate()

-ts_monitor_sp_eig - plot eigenvalues of linearized right-hand side

This is not called directly by users; pass this function to TSMonitorSet() along with the context created by TSMonitorSPEigCtxCreate() and TSMonitorSPEigCtxDestroy().

Currently only works when the Jacobian is provided explicitly and the ODE has no mass matrix.

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet(), TSMonitorSPEigCtxCreate(), TSMonitorSPEigCtxDestroy()

src/ts/interface/tseig.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorSPEig(TS ts, PetscInt step, PetscReal ptime, Vec v, void *monctx)
```

Example 2 (unknown):
```unknown
TSMonitorSPEigCtx
```

Example 3 (unknown):
```unknown
TSMonitorSPEigCtxCreate()
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorSPSwarmSolution#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorSPSwarmSolution/

**Contents:**
- TSMonitorSPSwarmSolution#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#

Graphically displays phase plots of DMSWARM particles on a scatter plot

step - current time-step

dctx - the TSMonitorSPCtx object that contains all the options for the monitoring, this is created with TSMonitorSPCtxCreate()

-ts_monitor_sp_swarm n - Monitor the solution every n steps, or -1 for plotting only the final solution

-ts_monitor_sp_swarm_retain n - Retain n old points so we can see the history, or -1 for all points

-ts_monitor_sp_swarm_multi_species (true|false) - Color each species differently

-ts_monitor_sp_swarm_phase (true|false) - Plot in phase space, as opposed to coordinate space

This is not called directly by users, rather one calls TSMonitorSet(), with this function as an argument, to cause the monitor to be used during the TS integration.

TS: Scalable ODE and DAE Solvers, TS, TSMonitorSet(), DMSWARM, TSMonitorSPCtxCreate()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorSPSwarmSolution(TS ts, PetscInt step, PetscReal ptime, Vec u, PetscCtx dctx)
```

Example 2 (unknown):
```unknown
TSMonitorSPCtx
```

Example 3 (unknown):
```unknown
TSMonitorSPCtxCreate()
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitorVTKCtx#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorVTKCtx/

**Contents:**
- TSMonitorVTKCtx#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#

Context object for the TS TSMonitorSolutionVTK() monitor that dumps the solution to VTK files at each time step

TS, TSMonitorSet(), TSMonitorSolutionVTK(), TSMonitorSolutionVTKCtxCreate(), TSMonitorSolutionVTKDestroy()

src/ts/tutorials/ex30.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorSolutionVTK()
```

Example 2 (c):
```c
#include <petscts.h> 
typedef struct _n_TSMonitorVTKCtx *TSMonitorVTKCtx;
```

Example 3 (unknown):
```unknown
TSMonitorSet()
```

Example 4 (unknown):
```unknown
TSMonitorSolutionVTK()
```

---

## TSMonitorWallClockTimeSetUp#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorWallClockTimeSetUp/

**Contents:**
- TSMonitorWallClockTimeSetUp#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Setup routine passed to TSMonitorSetFromOptions() when using -ts_monitor_wall_clock_time

vf - the viewer and format

This is not called directly by users, rather one calls TSMonitorSetFromOptions(), with TSMonitorWallClockTime() and this function as arguments, to cause the monitor to be used during the TS integration.

TS: Scalable ODE and DAE Solvers, TSMonitorSet()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorSetFromOptions()
```

Example 2 (unknown):
```unknown
-ts_monitor_wall_clock_time
```

Example 3 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorWallClockTimeSetUp(TS ts, PetscViewerAndFormat *vf)
```

Example 4 (unknown):
```unknown
TSMonitorSetFromOptions()
```

---

## TSMonitorWallClockTime#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitorWallClockTime/

**Contents:**
- TSMonitorWallClockTime#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Monitor wall-clock time, KSP iterations, and SNES iterations per step.

step - iteration number (after the final time step the monitor routine may be called with a step of -1, this indicates the solution has been interpolated to this time)

vf - the viewer and format

-ts_monitor_wall_clock_time - Monitor wall-clock time, KSP iterations, and SNES iterations per step.

This is not called directly by users, rather one calls TSMonitorSetFromOptions(), with this function and TSMonitorWallClockTimeSetUp() as arguments, to cause the monitor to be used during the TS integration.

TS: Scalable ODE and DAE Solvers, TSMonitorSet(), TSMonitorDefault(), TSMonitorExtreme(), TSMonitorDrawSolution(), TSMonitorDrawSolutionPhase(), TSMonitorDrawSolutionFunction(), TSMonitorDrawError(), TSMonitorSolution(), TSMonitorSolutionVTK(), TSMonitorLGSolution(), TSMonitorLGError(), TSMonitorSPSwarmSolution(), TSMonitorError(), TSMonitorEnvelope(), TSDMSwarmMonitorMoments()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitorWallClockTime(TS ts, PetscInt step, PetscReal ptime, Vec v, PetscViewerAndFormat *vf)
```

Example 2 (unknown):
```unknown
TSMonitorSetFromOptions()
```

Example 3 (unknown):
```unknown
TSMonitorWallClockTimeSetUp()
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMonitor#

**URL:** https://petsc.org/release/manualpages/TS/TSMonitor/

**Contents:**
- TSMonitor#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Runs all user-provided monitor routines set using TSMonitorSet()

ts - time stepping context obtained from TSCreate()

step - step number that has just completed

ptime - model time of the state

u - state at the current model time

TSMonitor() is typically used automatically within the time stepping implementations. Users would almost never call this routine directly.

A step of -1 indicates that the monitor is being called on a solution obtained by interpolating from computed solutions

TS, TSMonitorSet(), TSMonitorSetFromOptions()

src/ts/interface/tsmon.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMonitorSet()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSMonitor(TS ts, PetscInt step, PetscReal ptime, Vec u)
```

Example 3 (unknown):
```unknown
TSMonitor()
```

Example 4 (unknown):
```unknown
TSMonitorSet()
```

---

## TSMPRK2A22#

**URL:** https://petsc.org/release/manualpages/TS/TSMPRK2A22/

**Contents:**
- TSMPRK2A22#
- Options Database Key#
- See Also#
- Level#
- Location#

Second Order Multirate Partitioned Runge Kutta scheme based on RK2A. This method has four stages for slow and fast parts. The refinement factor of the stepsize is 2. r = 2, np = 2

-ts_mprk_type 2a22 - select this scheme

TS: Scalable ODE and DAE Solvers, TSMPRK, TSMPRKType, TSMPRKSetType()

src/ts/impls/multirate/mprk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMPRKSetType()
```

---

## TSMPRK2A23#

**URL:** https://petsc.org/release/manualpages/TS/TSMPRK2A23/

**Contents:**
- TSMPRK2A23#
- Options Database Key#
- See Also#
- Level#
- Location#

Second Order Multirate Partitioned Runge-Kutta scheme based on RK2A. This method has eight stages for slow and medium and fast parts. The refinement factor of the stepsize is 2. r = 2, np = 3

-ts_mprk_type 2a23 - select this scheme

TS: Scalable ODE and DAE Solvers, TSMPRK, TSMPRKType, TSMPRKSetType()

src/ts/impls/multirate/mprk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMPRKSetType()
```

---

## TSMPRK2A32#

**URL:** https://petsc.org/release/manualpages/TS/TSMPRK2A32/

**Contents:**
- TSMPRK2A32#
- Options Database Key#
- See Also#
- Level#
- Location#

Second Order Multirate Partitioned Runge-Kutta scheme based on RK2A. This method has four stages for slow and fast parts. The refinement factor of the stepsize is 3. r = 3, np = 2

-ts_mprk_type 2a32 - select this scheme

TS: Scalable ODE and DAE Solvers, TSMPRK, TSMPRKType, TSMPRKSetType()

src/ts/impls/multirate/mprk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMPRKSetType()
```

---

## TSMPRK2A33#

**URL:** https://petsc.org/release/manualpages/TS/TSMPRK2A33/

**Contents:**
- TSMPRK2A33#
- Options Database Key#
- See Also#
- Level#
- Location#

Second Order Multirate Partitioned Runge-Kutta scheme based on RK2A. This method has eight stages for slow and medium and fast parts. The refinement factor of the stepsize is 3. r = 3, np = 3

-ts_mprk_type 2a33- select this scheme

TS: Scalable ODE and DAE Solvers, TSMPRK, TSMPRKType, TSMPRKSetType()

src/ts/impls/multirate/mprk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMPRKSetType()
```

---

## TSMPRK3P2M#

**URL:** https://petsc.org/release/manualpages/TS/TSMPRK3P2M/

**Contents:**
- TSMPRK3P2M#
- Options Database Key#
- See Also#
- Level#
- Location#

Third Order Multirate Partitioned Runge-Kutta scheme. This method has eight stages for both slow and fast parts.

-ts_mprk_type pm3 - select this scheme

TS: Scalable ODE and DAE Solvers, TSMPRK, TSMPRKType, TSMPRKSetType()

src/ts/impls/multirate/mprk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMPRKSetType()
```

---

## TSMPRKFinalizePackage#

**URL:** https://petsc.org/release/manualpages/TS/TSMPRKFinalizePackage/

**Contents:**
- TSMPRKFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys everything in the TSMPRK package. It is called from PetscFinalize().

TS: Scalable ODE and DAE Solvers, TSMPRK, PetscFinalize()

src/ts/impls/multirate/mprk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSMPRKFinalizePackage(void)
```

Example 3 (unknown):
```unknown
PetscFinalize()
```

---

## TSMPRKGetType#

**URL:** https://petsc.org/release/manualpages/TS/TSMPRKGetType/

**Contents:**
- TSMPRKGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get the type of TSMPRK scheme

ts - timestepping context

mprktype - type of TSMPRK scheme

TS: Scalable ODE and DAE Solvers, TSMPRK

src/ts/impls/multirate/mprk.c

TSMPRKGetType_MPRK() in src/ts/impls/multirate/mprk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSMPRKGetType(TS ts, TSMPRKType *mprktype)
```

---

## TSMPRKInitializePackage#

**URL:** https://petsc.org/release/manualpages/TS/TSMPRKInitializePackage/

**Contents:**
- TSMPRKInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function initializes everything in the TSMPRK package. It is called from PetscDLLibraryRegister() when using dynamic libraries, and on the first call to TSCreate_MPRK() when using static libraries.

TS: Scalable ODE and DAE Solvers, TSMPRK, PetscInitialize()

src/ts/impls/multirate/mprk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDLLibraryRegister()
```

Example 2 (unknown):
```unknown
TSCreate_MPRK()
```

Example 3 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSMPRKInitializePackage(void)
```

Example 4 (unknown):
```unknown
PetscInitialize()
```

---

## TSMPRKP2#

**URL:** https://petsc.org/release/manualpages/TS/TSMPRKP2/

**Contents:**
- TSMPRKP2#
- Options Database Key#
- See Also#
- Level#
- Location#

Second Order Multirate Partitioned Runge-Kutta scheme. This method has five stages for both slow and fast parts.

-ts_mprk_type p2 - select this scheme

TS: Scalable ODE and DAE Solvers, TSMPRK, TSMPRKType, TSMPRKSetType()

src/ts/impls/multirate/mprk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMPRKSetType()
```

---

## TSMPRKP3#

**URL:** https://petsc.org/release/manualpages/TS/TSMPRKP3/

**Contents:**
- TSMPRKP3#
- Options Database Key#
- See Also#
- Level#
- Location#

Third Order Multirate Partitioned Runge-Kutta scheme. This method has ten stages for both slow and fast parts.

-ts_mprk_type p3 - select this scheme

TS: Scalable ODE and DAE Solvers, TSMPRK, TSMPRKType, TSMPRKSetType()

src/ts/impls/multirate/mprk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMPRKSetType()
```

---

## TSMPRKRegisterAll#

**URL:** https://petsc.org/release/manualpages/TS/TSMPRKRegisterAll/

**Contents:**
- TSMPRKRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the Partitioned Runge-Kutta explicit methods in TSMPRK

Not Collective, but should be called by all processes which will need the schemes to be registered

TS: Scalable ODE and DAE Solvers, TSMPRK, TSMPRKRegisterDestroy()

src/ts/impls/multirate/mprk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSMPRKRegisterAll(void)
```

Example 2 (unknown):
```unknown
TSMPRKRegisterDestroy()
```

---

## TSMPRKRegisterDestroy#

**URL:** https://petsc.org/release/manualpages/TS/TSMPRKRegisterDestroy/

**Contents:**
- TSMPRKRegisterDestroy#
- Synopsis#
- See Also#
- Level#
- Location#

Frees the list of schemes that were registered by TSMPRKRegister().

TS: Scalable ODE and DAE Solvers, TSMPRK, TSMPRKRegister(), TSMPRKRegisterAll()

src/ts/impls/multirate/mprk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMPRKRegister()
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSMPRKRegisterDestroy(void)
```

Example 3 (unknown):
```unknown
TSMPRKRegister()
```

Example 4 (unknown):
```unknown
TSMPRKRegisterAll()
```

---

## TSMPRKRegister#

**URL:** https://petsc.org/release/manualpages/TS/TSMPRKRegister/

**Contents:**
- TSMPRKRegister#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

register a TSMPRK scheme by providing the entries in the Butcher tableau

Not Collective, but the same schemes should be registered on all processes on which they will be used, No Fortran Support

name - identifier for method

order - approximation order of method

sbase - number of stages in the base methods

ratio1 - stepsize ratio at 1st level (e.g. slow/medium)

ratio2 - stepsize ratio at 2nd level (e.g. medium/fast)

Asb - stage coefficients for slow components(dimension s*s, row-major)

bsb - step completion table for slow components(dimension s)

csb - abscissa for slow components(dimension s)

rsb - array of flags for repeated stages for slow components (dimension s)

Amb - stage coefficients for medium components(dimension s*s, row-major)

bmb - step completion table for medium components(dimension s)

cmb - abscissa for medium components(dimension s)

rmb - array of flags for repeated stages for medium components (dimension s)

Af - stage coefficients for fast components(dimension s*s, row-major)

bf - step completion table for fast components(dimension s)

cf - abscissa for fast components(dimension s)

Several TSMPRK methods are provided, this function is only needed to create new methods.

TS: Scalable ODE and DAE Solvers, TSMPRK

src/ts/impls/multirate/mprk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSMPRKRegister(TSMPRKType name, PetscInt order, PetscInt sbase, PetscInt ratio1, PetscInt ratio2, const PetscReal Asb[], const PetscReal bsb[], const PetscReal csb[], const PetscInt rsb[], const PetscReal Amb[], const PetscReal bmb[], const PetscReal cmb[], const PetscInt rmb[], const PetscReal Af[], const PetscReal bf[], const PetscReal cf[])
```

---

## TSMPRKSetType#

**URL:** https://petsc.org/release/manualpages/TS/TSMPRKSetType/

**Contents:**
- TSMPRKSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

Set the type of TSMPRK scheme

ts - timestepping context

mprktype - type of TSMPRK scheme

-ts_mprk_type (pm2|p2|p3) - select the specific scheme

TS: Scalable ODE and DAE Solvers, TSMPRKGetType(), TSMPRK, TSMPRKType

src/ts/impls/multirate/mprk.c

TSMPRKSetType_MPRK() in src/ts/impls/multirate/mprk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSMPRKSetType(TS ts, TSMPRKType mprktype)
```

Example 2 (unknown):
```unknown
TSMPRKGetType()
```

---

## TSMPRKType#

**URL:** https://petsc.org/release/manualpages/TS/TSMPRKType/

**Contents:**
- TSMPRKType#
- Synopsis#
- See Also#
- Level#
- Location#

String with the name of a partitioned Runge-Kutta TSMPRK type

TS: Scalable ODE and DAE Solvers, TSMPRKSetType(), TS, TSMPRK, TSMPRKRegister()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h> 
typedef const char *TSMPRKType;
#define TSMPRK2A22 "2a22"
#define TSMPRK2A23 "2a23"
#define TSMPRK2A32 "2a32"
#define TSMPRK2A33 "2a33"
#define TSMPRKP2   "p2"
#define TSMPRKP3   "p3"
```

Example 2 (unknown):
```unknown
TSMPRKSetType()
```

Example 3 (unknown):
```unknown
TSMPRKRegister()
```

---

## TSMPRK#

**URL:** https://petsc.org/release/manualpages/TS/TSMPRK/

**Contents:**
- TSMPRK#
- Note#
- See Also#
- Level#
- Location#

ODE solver using Multirate Partitioned Runge-Kutta schemes

The default is TSMPRKPM2, it can be changed with TSMPRKSetType() or -ts_mprk_type

The user should provide the right-hand side of the equation using TSSetRHSFunction().

TS: Scalable ODE and DAE Solvers, TSCreate(), TS, TSSetType(), TSMPRKSetType(), TSMPRKGetType(), TSMPRKType, TSMPRKRegister(), TSMPRKSetMultirateType(), TSMPRKM2, TSMPRKM3, TSMPRKRFSMR3, TSMPRKRFSMR2, TSType

src/ts/impls/multirate/mprk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSMPRKSetType()
```

Example 2 (unknown):
```unknown
-ts_mprk_type
```

Example 3 (unknown):
```unknown
TSSetRHSFunction()
```

Example 4 (unknown):
```unknown
TSSetType()
```

---

## TSPostEvaluate#

**URL:** https://petsc.org/release/manualpages/TS/TSPostEvaluate/

**Contents:**
- TSPostEvaluate#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#

Runs the user-defined post-evaluate function set using TSSetPostEvaluate()

ts - The TS context obtained from TSCreate()

TSPostEvaluate() is typically used within time stepping implementations, most users would not generally call this routine themselves.

TS: Scalable ODE and DAE Solvers, TS, TSSetPostEvaluate(), TSSetPreStep(), TSPreStep(), TSPostStep()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetPostEvaluate()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSPostEvaluate(TS ts)
```

Example 3 (unknown):
```unknown
TSPostEvaluate()
```

Example 4 (unknown):
```unknown
TSSetPostEvaluate()
```

---

## TSPostStage#

**URL:** https://petsc.org/release/manualpages/TS/TSPostStage/

**Contents:**
- TSPostStage#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Runs the user-defined post-stage function set using TSSetPostStage()

ts - The TS context obtained from TSCreate()

stagetime - The absolute time of the current stage

stageindex - Stage number

Y - Array of vectors (of size = total number of stages) with the stage solutions

TSPostStage() is typically used within time stepping implementations, most users would not generally call this routine themselves.

TS: Scalable ODE and DAE Solvers, TS, TSPreStage(), TSSetPreStep(), TSPreStep(), TSPostStep()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetPostStage()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSPostStage(TS ts, PetscReal stagetime, PetscInt stageindex, Vec Y[])
```

Example 3 (unknown):
```unknown
TSPostStage()
```

Example 4 (unknown):
```unknown
TSPreStage()
```

---

## TSPostStep#

**URL:** https://petsc.org/release/manualpages/TS/TSPostStep/

**Contents:**
- TSPostStep#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#

Runs the user-defined post-step function that was set with TSSetPostStep()

ts - The TS context obtained from TSCreate()

TSPostStep() is typically used within time stepping implementations, so most users would not generally call this routine themselves.

TS: Scalable ODE and DAE Solvers, TS, TSSetPreStep(), TSSetPreStage(), TSSetPostEvaluate(), TSGetTimeStep(), TSGetStepNumber(), TSGetTime(), TSSetPostStep()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetPostStep()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSPostStep(TS ts)
```

Example 3 (unknown):
```unknown
TSPostStep()
```

Example 4 (unknown):
```unknown
TSSetPreStep()
```

---

## TSPreStage#

**URL:** https://petsc.org/release/manualpages/TS/TSPreStage/

**Contents:**
- TSPreStage#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Runs the user-defined pre-stage function set using TSSetPreStage()

ts - The TS context obtained from TSCreate()

stagetime - The absolute time of the current stage

TSPreStage() is typically used within time stepping implementations, most users would not generally call this routine themselves.

TS: Scalable ODE and DAE Solvers, TS, TSPostStage(), TSSetPreStep(), TSPreStep(), TSPostStep()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetPreStage()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSPreStage(TS ts, PetscReal stagetime)
```

Example 3 (unknown):
```unknown
TSPreStage()
```

Example 4 (unknown):
```unknown
TSPostStage()
```

---

## TSPreStep#

**URL:** https://petsc.org/release/manualpages/TS/TSPreStep/

**Contents:**
- TSPreStep#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#

Runs the user-defined pre-step function provided with TSSetPreStep()

ts - The TS context obtained from TSCreate()

TSPreStep() is typically used within time stepping implementations, so most users would not generally call this routine themselves.

TS: Scalable ODE and DAE Solvers, TS, TSSetPreStep(), TSPreStage(), TSPostStage(), TSPostStep()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetPreStep()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSPreStep(TS ts)
```

Example 3 (unknown):
```unknown
TSPreStep()
```

Example 4 (unknown):
```unknown
TSSetPreStep()
```

---

## TSProblemType#

**URL:** https://petsc.org/release/manualpages/TS/TSProblemType/

**Contents:**
- TSProblemType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#
- Examples#
- Examples#
- Examples#

Determines the type of problem this TS object is to be used to solve

TS_LINEAR - a linear ODE or DAE

TS_NONLINEAR - a nonlinear ODE or DAE

TS: Scalable ODE and DAE Solvers, TS, TSCreate()

src/ts/tutorials/ex4.c

src/ml/da/tutorials/ex3.c src/ts/tutorials/ex1.c src/ts/tutorials/ex14.c src/ts/tutorials/ex51.c src/ts/tutorials/ex21.c src/ml/da/tutorials/ex1.c src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex4.c src/ts/tutorials/ex41.c src/tao/unconstrained/tutorials/burgers_spectral.c

src/ts/tutorials/ex74.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/tutorials/ex5.c src/ts/tutorials/ex4.c src/ts/tutorials/ex3.c src/ts/tutorials/ex6.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h> 
typedef enum {
  TS_LINEAR,
  TS_NONLINEAR
} TSProblemType;
```

Example 2 (unknown):
```unknown
TS_NONLINEAR
```

---

## TSPruneIJacobianColor#

**URL:** https://petsc.org/release/manualpages/TS/TSPruneIJacobianColor/

**Contents:**
- TSPruneIJacobianColor#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Remove nondiagonal zeros in the Jacobian matrix and update the MatMFFD coloring information.

J - Jacobian matrix (not altered in this routine)

B - newly computed Jacobian matrix to use with preconditioner

This function improves the MatFDColoring performance when the Jacobian matrix was over-allocated or contains many constant zeros entries, which is typically the case when the matrix is generated by a DM and multiple fields are involved.

Users need to make sure that the Jacobian matrix is properly filled to reflect the sparsity structure. For MatFDColoring, the values of nonzero entries are not important. So one can usually call TSComputeIJacobian() with randomized input vectors to generate a dummy Jacobian. TSComputeIJacobian() should be called before TSSolve() but after TSSetUp().

TS: Scalable ODE and DAE Solvers, TS, MatFDColoring, TSComputeIJacobianDefaultColor(), MatEliminateZeros(), MatFDColoringCreate(), MatFDColoringSetFunction()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSPruneIJacobianColor(TS ts, Mat J, Mat B)
```

Example 2 (unknown):
```unknown
MatFDColoring
```

Example 3 (unknown):
```unknown
MatFDColoring
```

Example 4 (unknown):
```unknown
TSComputeIJacobian()
```

---

## TSPseudoComputeFunction#

**URL:** https://petsc.org/release/manualpages/TS/TSPseudoComputeFunction/

**Contents:**
- TSPseudoComputeFunction#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Compute nonlinear residual for pseudo-timestepping

This computes the residual for \(\dot U = 0\), i.e. \(F(U, 0)\) for the IFunction.

ts - the timestep context

solution - the solution vector

residual - the nonlinear residual

fnorm - the norm of the nonlinear residual

TSPSEUDO records the nonlinear residual and the solution vector used to generate it. If given the same solution vector (as determined by the vector’s PetscObjectState), this function will return those recorded values.

This can be used in a custom adaptive timestepping implementation that needs access to the residual, but can reuse the calculation already done by TSPSEUDO.

To correctly get the residual reuse behavior, solution must be the same Vec that was returned by TSGetSolution() or the Vec given by TSAdaptCheckStage().

TS: Scalable ODE and DAE Solvers, TSPSEUDO

src/ts/impls/pseudo/posindep.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSPseudoComputeFunction(TS ts, Vec solution, Vec *residual, PetscReal *fnorm)
```

Example 2 (unknown):
```unknown
PetscObjectState
```

Example 3 (unknown):
```unknown
TSGetSolution()
```

Example 4 (unknown):
```unknown
TSAdaptCheckStage()
```

---

## TSPseudoIncrementDtFromInitialDt#

**URL:** https://petsc.org/release/manualpages/TS/TSPseudoIncrementDtFromInitialDt/

**Contents:**
- TSPseudoIncrementDtFromInitialDt#
- Synopsis#
- Input Parameter#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

Indicates that a new timestep is computed via the formula \( dt = initial\_dt*initial\_fnorm/current\_fnorm \) rather than the default update, \( dt = current\_dt*previous\_fnorm/current\_fnorm.\)

ts - the timestep context

-ts_pseudo_increment_dt_from_initial_dt (true|false) - use the initial \(dt\) to determine increment

TS: Scalable ODE and DAE Solvers, TSPSEUDO, TSPseudoSetTimeStep(), TSPseudoTimeStepDefault()

src/ts/impls/pseudo/posindep.c

TSPseudoIncrementDtFromInitialDt_Pseudo() in src/ts/impls/pseudo/posindep.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSPseudoIncrementDtFromInitialDt(TS ts)
```

Example 2 (unknown):
```unknown
TSPseudoSetTimeStep()
```

Example 3 (unknown):
```unknown
TSPseudoTimeStepDefault()
```

---

## TSPseudoSetMaxTimeStep#

**URL:** https://petsc.org/release/manualpages/TS/TSPseudoSetMaxTimeStep/

**Contents:**
- TSPseudoSetMaxTimeStep#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

Sets the maximum time step when using the TSPseudoTimeStepDefault() routine.

ts - the timestep context

maxdt - the maximum time step, use a non-positive value to deactivate

-ts_pseudo_max_dt increment - set pseudo max dt

TS: Scalable ODE and DAE Solvers, TSPSEUDO, TSPseudoSetTimeStep(), TSPseudoTimeStepDefault()

src/ts/impls/pseudo/posindep.c

TSPseudoSetMaxTimeStep_Pseudo() in src/ts/impls/pseudo/posindep.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSPseudoSetMaxTimeStep(TS ts, PetscReal maxdt)
```

Example 2 (unknown):
```unknown
TSPseudoSetTimeStep()
```

Example 3 (unknown):
```unknown
TSPseudoTimeStepDefault()
```

---

## TSPseudoSetTimeStepIncrement#

**URL:** https://petsc.org/release/manualpages/TS/TSPseudoSetTimeStepIncrement/

**Contents:**
- TSPseudoSetTimeStepIncrement#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets the scaling increment applied to dt when using the TSPseudoTimeStepDefault() routine.

ts - the timestep context

inc - the scaling factor >= 1.0

-ts_pseudo_increment increment - set pseudo increment

TS: Scalable ODE and DAE Solvers, TSPSEUDO, TSPseudoSetTimeStep(), TSPseudoTimeStepDefault()

src/ts/impls/pseudo/posindep.c

src/ts/tutorials/ex42.c

TSPseudoSetTimeStepIncrement_Pseudo() in src/ts/impls/pseudo/posindep.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSPseudoSetTimeStepIncrement(TS ts, PetscReal inc)
```

Example 2 (unknown):
```unknown
TSPseudoSetTimeStep()
```

Example 3 (unknown):
```unknown
TSPseudoTimeStepDefault()
```

---

## TSPseudoSetTimeStep#

**URL:** https://petsc.org/release/manualpages/TS/TSPseudoSetTimeStep/

**Contents:**
- TSPseudoSetTimeStep#
- Synopsis#
- Input Parameters#
- Calling sequence of dt#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets the user-defined routine to be called at each pseudo-timestep to update the timestep.

ts - timestep context

dt - function to compute timestep

ctx - [optional] user-defined context for private data required by the function (may be NULL)

newdt - the newly computed timestep

ctx - [optional] user-defined context

The routine set here will be called by TSPseudoComputeTimeStep() during the timestepping process.

If not set then TSPseudoTimeStepDefault() is automatically used

TS: Scalable ODE and DAE Solvers, TSPSEUDO, TSPseudoTimeStepDefault(), TSPseudoComputeTimeStep()

src/ts/impls/pseudo/posindep.c

src/ts/tutorials/ex1.c

TSPseudoSetTimeStep_Pseudo() in src/ts/impls/pseudo/posindep.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSPseudoSetTimeStep(TS ts, PetscErrorCode (*dt)(TS ts, PetscReal *newdt, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSPseudoComputeTimeStep()
```

Example 3 (unknown):
```unknown
TSPseudoTimeStepDefault()
```

Example 4 (unknown):
```unknown
TSPseudoTimeStepDefault()
```

---

## TSPseudoSetVerifyTimeStep#

**URL:** https://petsc.org/release/manualpages/TS/TSPseudoSetVerifyTimeStep/

**Contents:**
- TSPseudoSetVerifyTimeStep#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Sets a user-defined routine to verify the quality of the last timestep.

ts - timestep context

dt - user-defined function to verify timestep

ctx - [optional] user-defined context for private data for the timestep verification routine (may be NULL)

ts - the time-step context

update - latest solution vector

ctx - [optional] user-defined timestep context

newdt - the timestep to use for the next step

flag - flag indicating whether the last time step was acceptable

The routine set here will be called by TSPseudoVerifyTimeStep() during the timestepping process.

TS: Scalable ODE and DAE Solvers, TSPSEUDO, TSPseudoVerifyTimeStepDefault(), TSPseudoVerifyTimeStep()

src/ts/impls/pseudo/posindep.c

TSPseudoSetVerifyTimeStep_Pseudo() in src/ts/impls/pseudo/posindep.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSPseudoSetVerifyTimeStep(TS ts, PetscErrorCode (*dt)(TS ts, Vec update, PetscCtx ctx, PetscReal *newdt, PetscBool *flag), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSPseudoVerifyTimeStep()
```

Example 3 (unknown):
```unknown
TSPseudoVerifyTimeStepDefault()
```

Example 4 (unknown):
```unknown
TSPseudoVerifyTimeStep()
```

---

## TSPseudoTimeStepDefault#

**URL:** https://petsc.org/release/manualpages/TS/TSPseudoTimeStepDefault/

**Contents:**
- TSPseudoTimeStepDefault#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Default code to compute pseudo-timestepping. Use with TSPseudoSetTimeStep().

Collective, No Fortran Support

ts - the timestep context

dtctx - unused timestep context

newdt - the timestep to use for the next step

TS: Scalable ODE and DAE Solvers, TSPseudoSetTimeStep(), TSPseudoComputeTimeStep(), TSPSEUDO

src/ts/impls/pseudo/posindep.c

src/ts/tutorials/ex1.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSPseudoSetTimeStep()
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSPseudoTimeStepDefault(TS ts, PetscReal *newdt, void *dtctx)
```

Example 3 (unknown):
```unknown
TSPseudoSetTimeStep()
```

Example 4 (unknown):
```unknown
TSPseudoComputeTimeStep()
```

---

## TSPSEUDO#

**URL:** https://petsc.org/release/manualpages/TS/TSPSEUDO/

**Contents:**
- TSPSEUDO#
- Options Database Keys#
- Notes#
- References#
- See Also#
- Level#
- Location#
- Examples#

Solve steady state ODE and DAE problems with pseudo time stepping [CKK02] [KK98] This method solves equations of the form

for steady state using the iteration

This is linearly-implicit Euler with the residual always evaluated “at steady state”. See note below.

In addition to the modified solve, a dedicated adaptive timestepping scheme is implemented, mimicking the switched evolution relaxation in [CKK02]. It determines the next timestep via

where \(r\) is an additional growth factor (set by -ts_pseudo_increment). An alternative formulation is also available that uses the initial timestep and function norm.

This is chosen by setting -ts_pseudo_increment_dt_from_initial_dt. For either method, an upper limit on the timestep can be set by -ts_pseudo_max_dt.

-ts_pseudo_increment real - ratio of increase dt

-ts_pseudo_increment_dt_from_initial_dt (true|false) - Increase dt as a ratio from original dt

-ts_pseudo_max_dt - Maximum dt for adaptive timestepping algorithm

-ts_pseudo_monitor - Monitor convergence of the function norm

-ts_pseudo_fatol atol - stop iterating when the function norm is less than atol

-ts_pseudo_frtol rtol - stop iterating when the function norm divided by the initial function norm is less than rtol

The residual computed by this method includes the transient term (Xdot is computed instead of always being zero), but since the prediction from the last step is always the solution from the last step, on the first Newton iteration we have

The Jacobian \( dF/dX + shift*dF/dXdot \) contains a non-zero \( dF/dXdot\) term. In the \( X' = F(X) \) case it is \( dF/dX + shift*1/dt \). Hence still contains the \( 1/dt \) term so the Jacobian is not simply the Jacobian of \( F \) and thus this pseudo-transient continuation is not just Newton on \(F(x)=0\).

Therefore, the linear system solved by the first Newton iteration is equivalent to the one described above and in the papers. If the user chooses to perform multiple Newton iterations, the algorithm is no longer the one described in the referenced papers. By default, the SNESType is set to SNESKSPONLY to match the algorithm from the referenced papers. Setting the SNESType via -snes_type will override this default setting.

Todd S. Coffey, C. T. Kelley, and David E. Keyes. Pseudo-transient continuation and differential-algebraic equations. Technical Report, ODU, 2002. Submitted to the special issue of the SIAM Journal of Scientific Computing dedicated to papers from the 2002 Copper Mountain Conference on Iterative Methods. URL: http://www.math.odu.edu/\~{ }keyes.

Carl T. Kelley and David E. Keyes. Convergence analysis of pseudo-transient continuation. SIAM J. Numerical Analysis, 35:508–523, 1998.

TS: Scalable ODE and DAE Solvers, TSCreate(), TS, TSSetType()

src/ts/impls/pseudo/posindep.c

src/ts/tutorials/ex1.c src/ts/tutorials/ex1f.F90 src/ts/tutorials/ex24.c src/ts/tutorials/ex42.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
-ts_pseudo_increment
```

Example 2 (unknown):
```unknown
-ts_pseudo_increment_dt_from_initial_dt
```

Example 3 (unknown):
```unknown
-ts_pseudo_max_dt
```

Example 4 (unknown):
```unknown
SNESKSPONLY
```

---

## TSPythonGetType#

**URL:** https://petsc.org/release/manualpages/TS/TSPythonGetType/

**Contents:**
- TSPythonGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the type of a TS object implemented in Python.

pyname - full dotted Python name [package].module[.{class|function}]

TS: Scalable ODE and DAE Solvers, TSCreate(), TSSetType(), TSPYTHON, PetscPythonInitialize(), TSPythonSetType()

src/ts/impls/python/pythonts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSPythonGetType(TS ts, const char *pyname[])
```

Example 2 (unknown):
```unknown
TSSetType()
```

Example 3 (unknown):
```unknown
PetscPythonInitialize()
```

Example 4 (unknown):
```unknown
TSPythonSetType()
```

---

## TSPythonSetType#

**URL:** https://petsc.org/release/manualpages/TS/TSPythonSetType/

**Contents:**
- TSPythonSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Initialize a TS object implemented in Python.

pyname - full dotted Python name [package].module[.{class|function}]

-ts_python_type pyname - python class

TS: Scalable ODE and DAE Solvers, TSCreate(), TSSetType(), TSPYTHON, PetscPythonInitialize()

src/ts/impls/python/pythonts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSPythonSetType(TS ts, const char pyname[])
```

Example 2 (unknown):
```unknown
TSSetType()
```

Example 3 (unknown):
```unknown
PetscPythonInitialize()
```

---

## TSPYTHON#

**URL:** https://petsc.org/release/manualpages/TS/TSPYTHON/

**Contents:**
- TSPYTHON#
- See Also#
- Level#
- Location#

a TSType that is implemented as a Python class using TSPythonSetType()

SNES: Nonlinear Solvers, TS, TSCreate(), TSSetType(), SNESPYTHON, PetscPythonInitialize(), TSPythonSetType(), TSPythonGetType(), TAOPYTHON

src/ts/impls/python/pythonts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSPythonSetType()
```

Example 2 (unknown):
```unknown
TSSetType()
```

Example 3 (unknown):
```unknown
PetscPythonInitialize()
```

Example 4 (unknown):
```unknown
TSPythonSetType()
```

---

## TSRADAU5#

**URL:** https://petsc.org/release/manualpages/TS/TSRADAU5/

**Contents:**
- TSRADAU5#
- Notes#
- See Also#
- Level#
- Location#

ODE solver using the external RADAU5 package, requires ./configure –download-radau5

This uses its own nonlinear solver and dense matrix direct solver so PETSc SNES and KSP options do not apply.

Uses its own time-step adaptivity (but uses the TS rtol and atol, and initial timestep)

Uses its own memory for the dense matrix storage and factorization

Can only handle ODEs of the form \( \dot{u} = -F(t,u) + G(t,u) \)

TS: Scalable ODE and DAE Solvers, TSCreate(), TS, TSSetType(), TSType

src/ts/impls/implicit/radau5/radau5.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetType()
```

---

## TSRegisterAll#

**URL:** https://petsc.org/release/manualpages/TS/TSRegisterAll/

**Contents:**
- TSRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the timesteppers in the TS package.

TS: Scalable ODE and DAE Solvers, TS, TSCreate(), TSRegister(), TSRegisterDestroy()

src/ts/interface/tsregall.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSRegisterAll(void)
```

Example 2 (unknown):
```unknown
TSRegister()
```

Example 3 (unknown):
```unknown
TSRegisterDestroy()
```

---

## TSRegister#

**URL:** https://petsc.org/release/manualpages/TS/TSRegister/

**Contents:**
- TSRegister#
- Synopsis#
- Input Parameters#
- Calling sequence of function#
- Notes#
- Example Usage#
- See Also#
- Level#
- Location#

Adds a creation method to the TS package.

Not Collective, No Fortran Support

sname - The name of a new user-defined creation routine

function - The creation routine itself

ts - the TS being setup for the new TSType being registered

TSRegister() may be called multiple times to add several user-defined tses.

Then, your ts type can be chosen with the procedural interface via

or at runtime via the option

TS: Scalable ODE and DAE Solvers, TSSetType(), TSType, TSRegisterAll(), TSRegisterDestroy()

src/ts/interface/tsreg.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSRegister(const char sname[], PetscErrorCode (*function)(TS ts))
```

Example 2 (unknown):
```unknown
TSRegister()
```

Example 3 (unknown):
```unknown
TSRegister("my_ts",  MyTSCreate);
```

Example 4 (unknown):
```unknown
TS ts;
    TSCreate(MPI_Comm, &ts);
    TSSetType(ts, "my_ts")
```

---

## TSRemoveTrajectory#

**URL:** https://petsc.org/release/manualpages/TS/TSRemoveTrajectory/

**Contents:**
- TSRemoveTrajectory#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Destroys and removes the internal TSTrajectory object from a TS

ts - the TS context obtained from TSCreate()

TS: Scalable ODE and DAE Solvers, TSTrajectory, TSResetTrajectory(), TSAdjointSolve()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSTrajectory
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSRemoveTrajectory(TS ts)
```

Example 3 (unknown):
```unknown
TSTrajectory
```

Example 4 (unknown):
```unknown
TSResetTrajectory()
```

---

## TSResetTrajectory#

**URL:** https://petsc.org/release/manualpages/TS/TSResetTrajectory/

**Contents:**
- TSResetTrajectory#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#

Destroys and recreates the internal TSTrajectory object

ts - the TS context obtained from TSCreate()

TS: Scalable ODE and DAE Solvers, TSTrajectory, TSGetTrajectory(), TSAdjointSolve(), TSRemoveTrajectory()

src/ts/interface/ts.c

src/ts/tutorials/ex41.c src/ts/tutorials/ex40.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSTrajectory
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSResetTrajectory(TS ts)
```

Example 3 (unknown):
```unknown
TSTrajectory
```

Example 4 (unknown):
```unknown
TSGetTrajectory()
```

---

## TSReset#

**URL:** https://petsc.org/release/manualpages/TS/TSReset/

**Contents:**
- TSReset#
- Synopsis#
- Input Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Resets a TS context to the state it was in before TSSetUp() was called and removes any allocated Vec and Mat from its data structures

ts - the TS context obtained from TSCreate()

Any options set on the TS object, including those set with TSSetFromOptions() remain.

See also TSSetResize() to change the size of the system being integrated (for example by adaptive mesh refinement) during the time integration.

TS: Scalable ODE and DAE Solvers, TS, TSCreate(), TSSetUp(), TSDestroy(), TSSetResize()

src/ts/interface/ts.c

src/ts/tutorials/ex77.c

TSReset_ARKIMEX() in src/ts/impls/arkimex/arkimex.c TSReset_BDF() in src/ts/impls/bdf/bdf.c TSReset_EIMEX() in src/ts/impls/eimex/eimex.c TSReset_Euler() in src/ts/impls/explicit/euler/euler.c TSReset_RK() in src/ts/impls/explicit/rk/rk.c TSReset_SSP() in src/ts/impls/explicit/ssp/ssp.c TSReset_GLEE() in src/ts/impls/glee/glee.c TSReset_Alpha() in src/ts/impls/implicit/alpha/alpha1.c TSReset_Alpha() in src/ts/impls/implicit/alpha/alpha2.c TSReset_DiscGrad() in src/ts/impls/implicit/discgrad/tsdiscgrad.c TSReset_GLLE() in src/ts/impls/implicit/glle/glle.c TSReset_IRK() in src/ts/impls/implicit/irk/irk.c TSReset_Sundials() in src/ts/impls/implicit/sundials/sundials.c TSReset_Theta() in src/ts/impls/implicit/theta/theta.c TSReset_Mimex() in src/ts/impls/mimex/mimex.c TSReset_MPRK() in src/ts/impls/multirate/mprk.c TSReset_Pseudo() in src/ts/impls/pseudo/posindep.c TSReset_RosW() in src/ts/impls/rosw/rosw.c TSReset_BasicSymplectic() in src/ts/impls/symplectic/basicsymplectic/basicsymplectic.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSReset(TS ts)
```

Example 2 (unknown):
```unknown
TSSetFromOptions()
```

Example 3 (unknown):
```unknown
TSSetResize()
```

Example 4 (unknown):
```unknown
TSDestroy()
```

---

## TSResizeRegisterVec#

**URL:** https://petsc.org/release/manualpages/TS/TSResizeRegisterVec/

**Contents:**
- TSResizeRegisterVec#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Register a vector to be transferred with TSResize().

ts - The TS context obtained from TSCreate()

name - A string identifying the vector

TSResizeRegisterVec() is typically used within time stepping implementations, so most users would not generally call this routine themselves.

TS: Scalable ODE and DAE Solvers, TS, TSSetResize(), TSResize(), TSResizeRetrieveVec()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSResizeRegisterVec(TS ts, const char name[], Vec vec)
```

Example 2 (unknown):
```unknown
TSResizeRegisterVec()
```

Example 3 (unknown):
```unknown
TSSetResize()
```

Example 4 (unknown):
```unknown
TSResizeRetrieveVec()
```

---

## TSResizeRetrieveVec#

**URL:** https://petsc.org/release/manualpages/TS/TSResizeRetrieveVec/

**Contents:**
- TSResizeRetrieveVec#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Retrieve a vector registered with TSResizeRegisterVec().

ts - The TS context obtained from TSCreate()

name - A string identifying the vector

TSResizeRetrieveVec() is typically used within time stepping implementations, so most users would not generally call this routine themselves.

TS: Scalable ODE and DAE Solvers, TS, TSSetResize(), TSResize(), TSResizeRegisterVec()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSResizeRegisterVec()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSResizeRetrieveVec(TS ts, const char name[], Vec *vec)
```

Example 3 (unknown):
```unknown
TSResizeRetrieveVec()
```

Example 4 (unknown):
```unknown
TSSetResize()
```

---

## TSResize#

**URL:** https://petsc.org/release/manualpages/TS/TSResize/

**Contents:**
- TSResize#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#

Runs the user-defined transfer functions provided with TSSetResize()

ts - The TS context obtained from TSCreate()

TSResize() is typically used within time stepping implementations, so most users would not generally call this routine themselves.

TS: Scalable ODE and DAE Solvers, TS, TSSetResize()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetResize()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSResize(TS ts)
```

Example 3 (unknown):
```unknown
TSSetResize()
```

---

## TSRestartStep#

**URL:** https://petsc.org/release/manualpages/TS/TSRestartStep/

**Contents:**
- TSRestartStep#
- Synopsis#
- Input Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Flags the solver to restart the next step

ts - the TS context obtained from TSCreate()

Multistep methods like TSBDF or Runge-Kutta methods with FSAL property require restarting the solver in the event of discontinuities. These discontinuities may be introduced as a consequence of explicitly modifications to the solution vector (which PETSc attempts to detect and handle) or problem coefficients (which PETSc is not able to detect). For the sake of correctness and maximum safety, users are expected to call TSRestart() whenever they introduce discontinuities in callback routines (e.g. prestep and poststep routines, or implicit/rhs function routines with discontinuous source terms).

TS: Scalable ODE and DAE Solvers, TS, TSBDF, TSSolve(), TSSetPreStep(), TSSetPostStep()

src/ts/interface/ts.c

src/ts/tutorials/ex41.c src/ts/tutorials/ex40.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSRestartStep(TS ts)
```

Example 2 (unknown):
```unknown
TSRestart()
```

Example 3 (unknown):
```unknown
TSSetPreStep()
```

Example 4 (unknown):
```unknown
TSSetPostStep()
```

---

## TSRHSFunctionFn#

**URL:** https://petsc.org/release/manualpages/TS/TSRHSFunctionFn/

**Contents:**
- TSRHSFunctionFn#
- Synopsis#
- Calling Sequence#
- Note#
- See Also#
- Level#
- Location#

A prototype of a TS right-hand-side evaluation function that would be passed to TSSetRHSFunction()

ts - timestep context

ctx - [optional] user-defined function context

The deprecated TSRHSFunction still works as a replacement for TSRHSFunctionFn *.

TS: Scalable ODE and DAE Solvers, TS, TSSetRHSFunction(), DMTSSetRHSFunction(), TSIFunctionFn, TSIJacobianFn, TSRHSJacobianFn

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetRHSFunction()
```

Example 2 (cpp):
```cpp
#include <petscts.h> 
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode TSRHSFunctionFn(TS ts, PetscReal t, Vec u, Vec F, PetscCtx ctx);
```

Example 3 (unknown):
```unknown
TSRHSFunction
```

Example 4 (unknown):
```unknown
TSRHSFunctionFn
```

---

## TSRHSJacobianFn#

**URL:** https://petsc.org/release/manualpages/TS/TSRHSJacobianFn/

**Contents:**
- TSRHSJacobianFn#
- Synopsis#
- Calling Sequence#
- Note#
- See Also#
- Level#
- Location#

A prototype of a TS right-hand-side Jacobian evaluation function that would be passed to TSSetRHSJacobian()

ts - the TS context obtained from TSCreate()

Amat - (approximate) Jacobian matrix

Pmat - matrix from which preconditioner is to be constructed (usually the same as Amat)

ctx - [optional] user-defined context for matrix evaluation routine

The deprecated TSRHSJacobian still works as a replacement for TSRHSJacobianFn *.

TS: Scalable ODE and DAE Solvers, TS, TSSetRHSJacobian(), DMTSSetRHSJacobian(), TSRHSFunctionFn, TSIFunctionFn, TSIJacobianFn

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetRHSJacobian()
```

Example 2 (cpp):
```cpp
#include <petscts.h> 
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode TSRHSJacobianFn(TS ts, PetscReal t, Vec u, Mat Amat, Mat Pmat, PetscCtx ctx);
```

Example 3 (unknown):
```unknown
TSRHSJacobian
```

Example 4 (unknown):
```unknown
TSRHSJacobianFn
```

---

## TSRHSJacobianPFn#

**URL:** https://petsc.org/release/manualpages/TS/TSRHSJacobianPFn/

**Contents:**
- TSRHSJacobianPFn#
- Synopsis#
- Calling Sequence#
- Note#
- See Also#
- Level#
- Location#

A prototype of a function that computes the Jacobian of G w.r.t. the parameters P where U_t = G(U,P,t), as well as the location to store the matrix that would be passed to TSSetRHSJacobianP()

U - input vector (current ODE solution)

ctx - [optional] user-defined function context

The deprecated TSRHSJacobianP still works as a replacement for TSRHSJacobianPFn *.

TS: Scalable ODE and DAE Solvers, TS, TSSetRHSJacobianP(), TSGetRHSJacobianP()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetRHSJacobianP()
```

Example 2 (cpp):
```cpp
#include <petscts.h> 
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode TSRHSJacobianPFn(TS ts, PetscReal t, Vec U, Mat A, PetscCtx ctx);
```

Example 3 (unknown):
```unknown
TSRHSJacobianP
```

Example 4 (unknown):
```unknown
TSRHSJacobianPFn
```

---

## TSRHSJacobianSetReuse#

**URL:** https://petsc.org/release/manualpages/TS/TSRHSJacobianSetReuse/

**Contents:**
- TSRHSJacobianSetReuse#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

restore the RHS Jacobian before calling the user-provided TSRHSJacobianFn function again

ts - TS context obtained from TSCreate()

reuse - PETSC_TRUE if the RHS Jacobian

Without this flag, TS will change the sign and shift the RHS Jacobian for a finite-time-step implicit solve, in which case the user function will need to recompute the entire Jacobian. The reuse flag must be set if the evaluation function assumes that the matrix entries have not been changed by the TS.

TS: Scalable ODE and DAE Solvers, TS, TSSetRHSJacobian(), TSComputeRHSJacobianConstant()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSRHSJacobianFn
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSRHSJacobianSetReuse(TS ts, PetscBool reuse)
```

Example 3 (unknown):
```unknown
TSSetRHSJacobian()
```

Example 4 (unknown):
```unknown
TSComputeRHSJacobianConstant()
```

---

## TSRHSJacobianTestTranspose#

**URL:** https://petsc.org/release/manualpages/TS/TSRHSJacobianTestTranspose/

**Contents:**
- TSRHSJacobianTestTranspose#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Compares the multiply transpose routine provided to the MATSHELL with differencing on the TS given RHS function.

ts - the time stepping routine

flg - PETSC_TRUE if the multiply is likely correct

-ts_rhs_jacobian_test_mult_transpose - mat_shell_test_mult_transpose_view - run the test at each timestep of the integrator

This only works for problems defined using TSSetRHSFunction() and Jacobian NOT TSSetIFunction() and Jacobian

TS: Scalable ODE and DAE Solvers, TS, Mat, MatCreateShell(), MatShellGetContext(), MatShellGetOperation(), MatShellTestMultTranspose(), TSRHSJacobianTest()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSRHSJacobianTestTranspose(TS ts, PetscBool *flg)
```

Example 2 (unknown):
```unknown
TSSetRHSFunction()
```

Example 3 (unknown):
```unknown
TSSetIFunction()
```

Example 4 (unknown):
```unknown
MatCreateShell()
```

---

## TSRHSJacobianTest#

**URL:** https://petsc.org/release/manualpages/TS/TSRHSJacobianTest/

**Contents:**
- TSRHSJacobianTest#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Compares the multiply routine provided to the MATSHELL with differencing on the TS given RHS function.

ts - the time stepping routine

flg - PETSC_TRUE if the multiply is likely correct

-ts_rhs_jacobian_test_mult - mat_shell_test_mult_view - run the test at each timestep of the integrator

This only works for problems defined using TSSetRHSFunction() and Jacobian NOT TSSetIFunction() and Jacobian

TS: Scalable ODE and DAE Solvers, TS, Mat, MATSHELL, MatCreateShell(), MatShellGetContext(), MatShellGetOperation(), MatShellTestMultTranspose(), TSRHSJacobianTestTranspose()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSRHSJacobianTest(TS ts, PetscBool *flg)
```

Example 2 (unknown):
```unknown
TSSetRHSFunction()
```

Example 3 (unknown):
```unknown
TSSetIFunction()
```

Example 4 (unknown):
```unknown
MatCreateShell()
```

---

## TSRHSSplitGetIS#

**URL:** https://petsc.org/release/manualpages/TS/TSRHSSplitGetIS/

**Contents:**
- TSRHSSplitGetIS#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Retrieves the elements for a split as an IS

ts - the TS context obtained from TSCreate()

splitname - name of this split

is - the index set for part of the solution vector

TS: Scalable ODE and DAE Solvers, TS, IS, TSRHSSplitSetIS()

src/ts/interface/tsrhssplit.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSRHSSplitGetIS(TS ts, const char splitname[], IS *is)
```

Example 2 (unknown):
```unknown
TSRHSSplitSetIS()
```

---

## TSRHSSplitGetSNES#

**URL:** https://petsc.org/release/manualpages/TS/TSRHSSplitGetSNES/

**Contents:**
- TSRHSSplitGetSNES#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Returns the SNES (nonlinear solver) associated with a TS (timestepper) context when RHS splits are used.

Not Collective, but snes is parallel if ts is parallel

ts - the TS context obtained from TSCreate()

snes - the nonlinear solver context

The returned SNES may have a different DM with the TS DM.

TS: Scalable ODE and DAE Solvers, TS, SNES, TSCreate(), TSRHSSplitSetSNES()

src/ts/interface/tsrhssplit.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSRHSSplitGetSNES(TS ts, SNES *snes)
```

Example 2 (unknown):
```unknown
TSRHSSplitSetSNES()
```

---

## TSRHSSplitGetSubTSs#

**URL:** https://petsc.org/release/manualpages/TS/TSRHSSplitGetSubTSs/

**Contents:**
- TSRHSSplitGetSubTSs#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Get an array of all sub-TS contexts.

ts - the TS context obtained from TSCreate()

n - the number of splits

subts - the array of TS contexts

After TSRHSSplitGetSubTS() the array of TSs is to be freed by the user with PetscFree() (not the TS in the array just the array that contains them).

TS: Scalable ODE and DAE Solvers, TS, IS, TSGetRHSSplitFunction()

src/ts/interface/tsrhssplit.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSRHSSplitGetSubTSs(TS ts, PetscInt *n, TS *subts[])
```

Example 2 (unknown):
```unknown
TSRHSSplitGetSubTS()
```

Example 3 (unknown):
```unknown
PetscFree()
```

Example 4 (unknown):
```unknown
TSGetRHSSplitFunction()
```

---

## TSRHSSplitGetSubTS#

**URL:** https://petsc.org/release/manualpages/TS/TSRHSSplitGetSubTS/

**Contents:**
- TSRHSSplitGetSubTS#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Get the sub-TS by split name.

ts - the TS context obtained from TSCreate()

splitname - the number of the split

TS: Scalable ODE and DAE Solvers, TS, IS, TSGetRHSSplitFunction()

src/ts/interface/tsrhssplit.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSRHSSplitGetSubTS(TS ts, const char splitname[], TS *subts)
```

Example 2 (unknown):
```unknown
TSGetRHSSplitFunction()
```

---

## TSRHSSplitSetIFunction#

**URL:** https://petsc.org/release/manualpages/TS/TSRHSSplitSetIFunction/

**Contents:**
- TSRHSSplitSetIFunction#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the split implicit function for TSARKIMEX

ts - the TS context obtained from TSCreate()

splitname - name of this split

r - vector to hold the residual (or NULL to have it created internally)

ifunc - the implicit function evaluation routine

ctx - user-defined context for private data for the split function evaluation routine (may be NULL)

TS: Scalable ODE and DAE Solvers, TS, TSIFunctionFn, IS, TSRHSSplitSetIS(), TSARKIMEX, TSARKIMEXSetFastSlowSplit()

src/ts/interface/tsrhssplit.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSRHSSplitSetIFunction(TS ts, const char splitname[], Vec r, TSIFunctionFn *ifunc, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSIFunctionFn
```

Example 3 (unknown):
```unknown
TSRHSSplitSetIS()
```

Example 4 (unknown):
```unknown
TSARKIMEXSetFastSlowSplit()
```

---

## TSRHSSplitSetIJacobian#

**URL:** https://petsc.org/release/manualpages/TS/TSRHSSplitSetIJacobian/

**Contents:**
- TSRHSSplitSetIJacobian#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the Jacobian for the split implicit function with TSARKIMEX

ts - the TS context obtained from TSCreate()

splitname - name of this split

Amat - (approximate) matrix to store Jacobian entries computed by f

Pmat - matrix used to compute preconditioner (usually the same as Amat)

ijac - the Jacobian evaluation routine

ctx - user-defined context for private data for the split function evaluation routine (may be NULL)

TS: Scalable ODE and DAE Solvers, TS, TSRHSSplitSetIFunction, TSIJacobianFn, IS, TSRHSSplitSetIS(), TSARKIMEXSetFastSlowSplit()

src/ts/interface/tsrhssplit.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSRHSSplitSetIJacobian(TS ts, const char splitname[], Mat Amat, Mat Pmat, TSIJacobianFn *ijac, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSRHSSplitSetIFunction
```

Example 3 (unknown):
```unknown
TSIJacobianFn
```

Example 4 (unknown):
```unknown
TSRHSSplitSetIS()
```

---

## TSRHSSplitSetIS#

**URL:** https://petsc.org/release/manualpages/TS/TSRHSSplitSetIS/

**Contents:**
- TSRHSSplitSetIS#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the index set for the specified split

ts - the TS context obtained from TSCreate()

splitname - name of this split, if NULL the number of the split is used

is - the index set for part of the solution vector

TS: Scalable ODE and DAE Solvers, TS, IS, TSRHSSplitGetIS(), TSARKIMEXSetFastSlowSplit()

src/ts/interface/tsrhssplit.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSRHSSplitSetIS(TS ts, const char splitname[], IS is)
```

Example 2 (unknown):
```unknown
TSRHSSplitGetIS()
```

Example 3 (unknown):
```unknown
TSARKIMEXSetFastSlowSplit()
```

---

## TSRHSSplitSetRHSFunction#

**URL:** https://petsc.org/release/manualpages/TS/TSRHSSplitSetRHSFunction/

**Contents:**
- TSRHSSplitSetRHSFunction#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the split right-hand-side functions.

ts - the TS context obtained from TSCreate()

splitname - name of this split

r - vector to hold the residual (or NULL to have it created internally)

rhsfunc - the RHS function evaluation routine

ctx - user-defined context for private data for the split function evaluation routine (may be NULL)

TS: Scalable ODE and DAE Solvers, TS, TSRHSFunctionFn, IS, TSRHSSplitSetIS()

src/ts/interface/tsrhssplit.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSRHSSplitSetRHSFunction(TS ts, const char splitname[], Vec r, TSRHSFunctionFn *rhsfunc, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSRHSFunctionFn
```

Example 3 (unknown):
```unknown
TSRHSSplitSetIS()
```

---

## TSRHSSplitSetSNES#

**URL:** https://petsc.org/release/manualpages/TS/TSRHSSplitSetSNES/

**Contents:**
- TSRHSSplitSetSNES#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Set the SNES (nonlinear solver) to be used by the timestepping context when RHS splits are used.

ts - the TS context obtained from TSCreate()

snes - the nonlinear solver context

Most users should have the TS created by calling TSRHSSplitGetSNES()

TS: Scalable ODE and DAE Solvers, TS, SNES, TSCreate(), TSRHSSplitGetSNES()

src/ts/interface/tsrhssplit.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSRHSSplitSetSNES(TS ts, SNES snes)
```

Example 2 (unknown):
```unknown
TSRHSSplitGetSNES()
```

Example 3 (unknown):
```unknown
TSRHSSplitGetSNES()
```

---

## TSRK1FE#

**URL:** https://petsc.org/release/manualpages/TS/TSRK1FE/

**Contents:**
- TSRK1FE#
- Options Database Key#
- See Also#
- Level#
- Location#

First order forward Euler scheme. This method has one stage.

-ts_rk_type 1fe - use type 1fe

TS: Scalable ODE and DAE Solvers, TSRK, TSRKType, TSRKSetType()

src/ts/impls/explicit/rk/rk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSRKSetType()
```

---

## TSRK2A#

**URL:** https://petsc.org/release/manualpages/TS/TSRK2A/

**Contents:**
- TSRK2A#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

Second order RK scheme (Heun’s method). This method has two stages.

-ts_rk_type 2a - use type 2a

TS: Scalable ODE and DAE Solvers, TSRK, TSRKType, TSRKSetType()

src/ts/impls/explicit/rk/rk.c

src/ts/utils/dmplexlandau/tutorials/ex1.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSRKSetType()
```

---

## TSRK2B#

**URL:** https://petsc.org/release/manualpages/TS/TSRK2B/

**Contents:**
- TSRK2B#
- Options Database Key#
- See Also#
- Level#
- Location#

Second order RK scheme (the midpoint method). This method has two stages.

-ts_rk_type 2b - use type 2b

TS: Scalable ODE and DAE Solvers, TSRK, TSRKType, TSRKSetType()

src/ts/impls/explicit/rk/rk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSRKSetType()
```

---

## TSRK3BS#

**URL:** https://petsc.org/release/manualpages/TS/TSRK3BS/

**Contents:**
- TSRK3BS#
- Options Database Key#
- See Also#
- Level#
- Location#

Third order RK scheme of Bogacki-Shampine with 2nd order embedded method https://doi.org/10.1016/0893-9659(89)90079-7 This method has four stages with the First Same As Last (FSAL) property.

-ts_rk_type 3bs - use type 3bs

TS: Scalable ODE and DAE Solvers, TSRK, TSRKType, TSRKSetType()

src/ts/impls/explicit/rk/rk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSRKSetType()
```

---

## TSRK3#

**URL:** https://petsc.org/release/manualpages/TS/TSRK3/

**Contents:**
- TSRK3#
- Options Database Key#
- See Also#
- Level#
- Location#

Third order RK scheme. This method has three stages.

-ts_rk_type 3 - use type 3

TS: Scalable ODE and DAE Solvers, TSRK, TSRKType, TSRKSetType()

src/ts/impls/explicit/rk/rk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSRKSetType()
```

---

## TSRK4#

**URL:** https://petsc.org/release/manualpages/TS/TSRK4/

**Contents:**
- TSRK4#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

Fourth order RK scheme. This is the classical Runge-Kutta method with four stages.

-ts_rk_type 4 - use type 4

TS: Scalable ODE and DAE Solvers, TSRK, TSRKType, TSRKSetType()

src/ts/impls/explicit/rk/rk.c

src/ml/da/tutorials/ex3.c src/ml/da/tutorials/ex4.c src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex1.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSRKSetType()
```

---

## TSRK5BS#

**URL:** https://petsc.org/release/manualpages/TS/TSRK5BS/

**Contents:**
- TSRK5BS#
- Options Database Key#
- See Also#
- Level#
- Location#

Fifth order Bogacki-Shampine RK scheme with 4th order embedded method https://doi.org/10.1016/0898-1221(96)00141-1 This method has eight stages with the First Same As Last (FSAL) property.

-ts_rk_type 5bs - use type 5bs

TS: Scalable ODE and DAE Solvers, TSRK, TSRKType, TSRKSetType()

src/ts/impls/explicit/rk/rk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSRKSetType()
```

---

## TSRK5DP#

**URL:** https://petsc.org/release/manualpages/TS/TSRK5DP/

**Contents:**
- TSRK5DP#
- Options Database Key#
- See Also#
- Level#
- Location#

Fifth order Dormand-Prince RK scheme with the 4th order embedded method https://doi.org/10.1016/0771-050X(80)90013-3 This method has seven stages with the First Same As Last (FSAL) property.

-ts_rk_type 5dp - use type 5dp

TS: Scalable ODE and DAE Solvers, TSRK, TSRKType, TSRKSetType()

src/ts/impls/explicit/rk/rk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSRKSetType()
```

---

## TSRK5F#

**URL:** https://petsc.org/release/manualpages/TS/TSRK5F/

**Contents:**
- TSRK5F#
- Options Database Key#
- See Also#
- Level#
- Location#

Fifth order Fehlberg RK scheme with a 4th order embedded method. This method has six stages.

-ts_rk_type 5f - use type 5f

TS: Scalable ODE and DAE Solvers, TSRK, TSRKType, TSRKSetType()

src/ts/impls/explicit/rk/rk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSRKSetType()
```

---

## TSRK6VR#

**URL:** https://petsc.org/release/manualpages/TS/TSRK6VR/

**Contents:**
- TSRK6VR#
- Options Database Key#
- See Also#
- Level#
- Location#

Sixth order robust Verner RK scheme with fifth order embedded method. http://people.math.sfu.ca/~jverner/RKV65.IIIXb.Robust.00010102836.081204.CoeffsOnlyRAT This method has nine stages with the First Same As Last (FSAL) property.

-ts_rk_type 6vr - use type 6vr

TS: Scalable ODE and DAE Solvers, TSRK, TSRKType, TSRKSetType()

src/ts/impls/explicit/rk/rk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSRKSetType()
```

---

## TSRK7VR#

**URL:** https://petsc.org/release/manualpages/TS/TSRK7VR/

**Contents:**
- TSRK7VR#
- Options Database Key#
- See Also#
- Level#
- Location#

Seventh order robust Verner RK scheme with sixth order embedded method. http://people.math.sfu.ca/~jverner/RKV65.IIIXb.Robust.00010102836.081204.CoeffsOnlyRAT This method has ten stages.

-ts_rk_type 7vr - use type 7vr

TS: Scalable ODE and DAE Solvers, TSRK, TSRKType, TSRKSetType()

src/ts/impls/explicit/rk/rk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSRKSetType()
```

---

## TSRK8VR#

**URL:** https://petsc.org/release/manualpages/TS/TSRK8VR/

**Contents:**
- TSRK8VR#
- Options Database Key#
- See Also#
- Level#
- Location#

Eighth order robust Verner RK scheme with seventh order embedded method. http://people.math.sfu.ca/~jverner/RKV87.IIa.Robust.00000754677.081208.CoeffsOnlyRATandFLOAT This method has thirteen stages.

-ts_rk_type 8vr - use type 8vr

TS: Scalable ODE and DAE Solvers, TSRK, TSRKType, TSRKSetType()

src/ts/impls/explicit/rk/rk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSRKSetType()
```

---

## TSRKFinalizePackage#

**URL:** https://petsc.org/release/manualpages/TS/TSRKFinalizePackage/

**Contents:**
- TSRKFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys everything in the TSRK package. It is called from PetscFinalize().

TS: Scalable ODE and DAE Solvers, PetscFinalize(), TSRKInitializePackage()

src/ts/impls/explicit/rk/rk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSRKFinalizePackage(void)
```

Example 3 (unknown):
```unknown
PetscFinalize()
```

Example 4 (unknown):
```unknown
TSRKInitializePackage()
```

---

## TSRKGetMultirate#

**URL:** https://petsc.org/release/manualpages/TS/TSRKGetMultirate/

**Contents:**
- TSRKGetMultirate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Gets whether to use the interpolation-based multirate TSRK method

ts - timestepping context

use_multirate - PETSC_TRUE if the multirate RK method is enabled, PETSC_FALSE otherwise

TS: Scalable ODE and DAE Solvers, TSRK, TSRKSetMultirate()

src/ts/impls/explicit/rk/rk.c

TSRKGetMultirate_RK() in src/ts/impls/explicit/rk/mrk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSRKGetMultirate(TS ts, PetscBool *use_multirate)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
TSRKSetMultirate()
```

---

## TSRKGetOrder#

**URL:** https://petsc.org/release/manualpages/TS/TSRKGetOrder/

**Contents:**
- TSRKGetOrder#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get the order of the TSRK scheme

ts - timestepping context

order - order of TSRK scheme

TS: Scalable ODE and DAE Solvers, TSRK, TSRKGetType()

src/ts/impls/explicit/rk/rk.c

TSRKGetOrder_RK() in src/ts/impls/explicit/rk/rk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSRKGetOrder(TS ts, PetscInt *order)
```

Example 2 (unknown):
```unknown
TSRKGetType()
```

---

## TSRKGetTableau#

**URL:** https://petsc.org/release/manualpages/TS/TSRKGetTableau/

**Contents:**
- TSRKGetTableau#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Fortran Note#
- See Also#
- Level#
- Location#
- Implementations#

Get info on the TSRK tableau

ts - timestepping context

s - number of stages, this is the dimension of the matrices below

A - stage coefficients (dimension s*s, row-major)

b - step completion table (dimension s)

c - abscissa (dimension s)

bembed - completion table for embedded method (dimension s; NULL if not available)

p - Order of the interpolation scheme, equal to the number of columns of binterp

binterp - Coefficients of the interpolation formula (dimension s*p)

FSAL - whether or not the scheme has the First Same As Last property

Call TSRKRestoreTableau() when you no longer need access to the tableau values.

TS: Scalable ODE and DAE Solvers, TSRK, TSRKRegister(), TSRKSetType()

src/ts/impls/explicit/rk/rk.c

TSRKGetTableau_RK() in src/ts/impls/explicit/rk/rk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSRKGetTableau(TS ts, PetscInt *s, const PetscReal *A[], const PetscReal *b[], const PetscReal *c[], const PetscReal *bembed[], PetscInt *p, const PetscReal *binterp[], PetscBool *FSAL)
```

Example 2 (unknown):
```unknown
TSRKRestoreTableau()
```

Example 3 (unknown):
```unknown
TSRKRegister()
```

Example 4 (unknown):
```unknown
TSRKSetType()
```

---

## TSRKGetType#

**URL:** https://petsc.org/release/manualpages/TS/TSRKGetType/

**Contents:**
- TSRKGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get the type of TSRK scheme

ts - timestepping context

rktype - type of TSRK-scheme

TS: Scalable ODE and DAE Solvers, TSRKSetType()

src/ts/impls/explicit/rk/rk.c

TSRKGetType_RK() in src/ts/impls/explicit/rk/rk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSRKGetType(TS ts, TSRKType *rktype)
```

Example 2 (unknown):
```unknown
TSRKSetType()
```

---

## TSRKInitializePackage#

**URL:** https://petsc.org/release/manualpages/TS/TSRKInitializePackage/

**Contents:**
- TSRKInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function initializes everything in the TSRK package. It is called from TSInitializePackage().

TS: Scalable ODE and DAE Solvers, TSInitializePackage(), PetscInitialize(), TSRKFinalizePackage()

src/ts/impls/explicit/rk/rk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSInitializePackage()
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSRKInitializePackage(void)
```

Example 3 (unknown):
```unknown
TSInitializePackage()
```

Example 4 (unknown):
```unknown
PetscInitialize()
```

---

## TSRKRegisterAll#

**URL:** https://petsc.org/release/manualpages/TS/TSRKRegisterAll/

**Contents:**
- TSRKRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the Runge-Kutta explicit methods in TSRK

Not Collective, but should be called by all processes which will need the schemes to be registered

TS: Scalable ODE and DAE Solvers, TSRKRegisterDestroy(), TSRKRegister()

src/ts/impls/explicit/rk/rk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSRKRegisterAll(void)
```

Example 2 (unknown):
```unknown
TSRKRegisterDestroy()
```

Example 3 (unknown):
```unknown
TSRKRegister()
```

---

## TSRKRegisterDestroy#

**URL:** https://petsc.org/release/manualpages/TS/TSRKRegisterDestroy/

**Contents:**
- TSRKRegisterDestroy#
- Synopsis#
- See Also#
- Level#
- Location#

Frees the list of schemes that were registered by TSRKRegister().

TS: Scalable ODE and DAE Solvers, TSRK, TSRKRegister(), TSRKRegisterAll()

src/ts/impls/explicit/rk/rk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSRKRegister()
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSRKRegisterDestroy(void)
```

Example 3 (unknown):
```unknown
TSRKRegister()
```

Example 4 (unknown):
```unknown
TSRKRegisterAll()
```

---

## TSRKRegister#

**URL:** https://petsc.org/release/manualpages/TS/TSRKRegister/

**Contents:**
- TSRKRegister#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Register an TSRK scheme by providing the entries in the Butcher tableau and optionally embedded approximations and interpolation

Not Collective, but the same schemes should be registered on all processes on which they will be used, No Fortran Support

name - identifier for method

order - approximation order of method

s - number of stages, this is the dimension of the matrices below

A - stage coefficients (dimension s*s, row-major)

b - step completion table (dimension s; NULL to use last row of A)

c - abscissa (dimension s; NULL to use row sums of A)

bembed - completion table for embedded method (dimension s; NULL if not available)

p - order of the interpolation scheme, equal to the number of columns of binterp

binterp - coefficients of the interpolation formula (dimension s*p; NULL to reuse b with \(p=1\))

Several TSRK methods are provided, this function is only needed to create new methods.

TS: Scalable ODE and DAE Solvers, TSRK

src/ts/impls/explicit/rk/rk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSRKRegister(TSRKType name, PetscInt order, PetscInt s, const PetscReal A[], const PetscReal b[], const PetscReal c[], const PetscReal bembed[], PetscInt p, const PetscReal binterp[])
```

---

## TSRKSetMultirate#

**URL:** https://petsc.org/release/manualpages/TS/TSRKSetMultirate/

**Contents:**
- TSRKSetMultirate#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Use the interpolation-based multirate TSRK method

ts - timestepping context

use_multirate - PETSC_TRUE enables the multirate TSRK method, sets the basic method to be TSRK2A and sets the ratio between slow stepsize and fast stepsize to be 2

-ts_rk_multirate (true|false) - enable the multirate RK method

The multirate method requires interpolation. The default interpolation works for 1st- and 2nd- order RK, but not for high-order RKs except TSRK5DP which comes with the interpolation coefficients (binterp).

TS: Scalable ODE and DAE Solvers, TSRK, TSRKGetMultirate()

src/ts/impls/explicit/rk/rk.c

TSRKSetMultirate_RK() in src/ts/impls/explicit/rk/mrk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSRKSetMultirate(TS ts, PetscBool use_multirate)
```

Example 2 (unknown):
```unknown
TSRKGetMultirate()
```

---

## TSRKSetType#

**URL:** https://petsc.org/release/manualpages/TS/TSRKSetType/

**Contents:**
- TSRKSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Set the type of the TSRK scheme

ts - timestepping context

rktype - type of TSRK scheme

-ts_rk_type (1fe|2a|2b|3|3bs|4|5f|5dp|5bs|6vr|7vr|8vr) - the type

TS: Scalable ODE and DAE Solvers, TSRKGetType(), TSRK, TSRKType, TSRK1FE, TSRK2A, TSRK2B, TSRK3, TSRK3BS, TSRK4, TSRK5F, TSRK5DP, TSRK5BS, TSRK6VR, TSRK7VR, TSRK8VR

src/ts/impls/explicit/rk/rk.c

src/ml/da/tutorials/ex3.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ml/da/tutorials/ex1.c src/ml/da/tutorials/ex4.c src/ml/da/tutorials/ex2.c

TSRKSetType_RK() in src/ts/impls/explicit/rk/rk.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSRKSetType(TS ts, TSRKType rktype)
```

Example 2 (unknown):
```unknown
TSRKGetType()
```

---

## TSRKType#

**URL:** https://petsc.org/release/manualpages/TS/TSRKType/

**Contents:**
- TSRKType#
- Synopsis#
- See Also#
- Level#
- Location#

String with the name of a Runge-Kutta TSRK type

TS: Scalable ODE and DAE Solvers, TS, TSRKSetType(), TSRK, TSRKRegister()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h> 
typedef const char *TSRKType;
#define TSRK1FE "1fe"
#define TSRK2A  "2a"
#define TSRK2B  "2b"
#define TSRK3   "3"
#define TSRK3BS "3bs"
#define TSRK4   "4"
#define TSRK5F  "5f"
#define TSRK5DP "5dp"
#define TSRK5BS "5bs"
#define TSRK6VR "6vr"
#define TSRK7VR "7vr"
#define TSRK8VR "8vr"
```

Example 2 (unknown):
```unknown
TSRKSetType()
```

Example 3 (unknown):
```unknown
TSRKRegister()
```

---

## TSRK#

**URL:** https://petsc.org/release/manualpages/TS/TSRK/

**Contents:**
- TSRK#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

ODE and DAE solver using Runge-Kutta schemes The user should provide the right-hand side of the equation using TSSetRHSFunction().

The default is TSRK3BS, it can be changed with TSRKSetType() or -ts_rk_type

TS: Scalable ODE and DAE Solvers, TSCreate(), TS, TSRK, TSSetType(), TSRKSetType(), TSRKGetType(), TSRK1FE, TSRK2A, TSRK2B, TSRK3, TSRK3BS, TSRK4, TSRK5F, TSRK5DP, TSRK5BS, TSRK6VR, TSRK7VR, TSRK8VR, TSRKType, TSRKRegister(), TSRKSetMultirate(), TSRKGetMultirate(), TSType

src/ts/impls/explicit/rk/rk.c

src/ml/da/tutorials/ex3.c src/ts/tutorials/ex20opt_p.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/tutorials/ex20opt_ic.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ml/da/tutorials/ex1.c src/ml/da/tutorials/ex2.c src/ts/tutorials/ex16fwd.c src/ml/da/tutorials/ex4.c src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetRHSFunction()
```

Example 2 (unknown):
```unknown
TSRKSetType()
```

Example 3 (unknown):
```unknown
-ts_rk_type
```

Example 4 (unknown):
```unknown
TSSetType()
```

---

## TSRollBack#

**URL:** https://petsc.org/release/manualpages/TS/TSRollBack/

**Contents:**
- TSRollBack#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Rolls back one time step

ts - the TS context obtained from TSCreate()

TS: Scalable ODE and DAE Solvers, TS, TSGetStepRollBack(), TSCreate(), TSSetUp(), TSDestroy(), TSSolve(), TSSetPreStep(), TSSetPreStage(), TSInterpolate()

src/ts/interface/ts.c

TSRollBack_RK() in src/ts/impls/explicit/rk/rk.c TSRollBack_Alpha() in src/ts/impls/implicit/alpha/alpha2.c TSRollBack_IRK() in src/ts/impls/implicit/irk/irk.c TSRollBack_Theta() in src/ts/impls/implicit/theta/theta.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSRollBack(TS ts)
```

Example 2 (unknown):
```unknown
TSGetStepRollBack()
```

Example 3 (unknown):
```unknown
TSDestroy()
```

Example 4 (unknown):
```unknown
TSSetPreStep()
```

---

## TSROSW2M#

**URL:** https://petsc.org/release/manualpages/TS/TSROSW2M/

**Contents:**
- TSROSW2M#
- See Also#
- Level#
- Location#

Two stage second order L-stable Rosenbrock-W scheme. Only an approximate Jacobian is needed. By default, it is only recomputed once per step. This method is a reflection of TSROSW2P.

TS: Scalable ODE and DAE Solvers, TSROSW

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

---

## TSROSW2P#

**URL:** https://petsc.org/release/manualpages/TS/TSROSW2P/

**Contents:**
- TSROSW2P#
- See Also#
- Level#
- Location#

Two stage second order L-stable Rosenbrock-W scheme. Only an approximate Jacobian is needed. By default, it is only recomputed once per step. This method is a reflection of TSROSW2M.

TS: Scalable ODE and DAE Solvers, TSROSW

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

---

## TSROSW4L#

**URL:** https://petsc.org/release/manualpages/TS/TSROSW4L/

**Contents:**
- TSROSW4L#
- Note#
- References#
- See Also#
- Level#
- Location#

four stage, fourth order Rosenbrock (not W) method By default, the Jacobian is only recomputed once per step.

A-stable and L-stable

This method does not provide a dense output formula.

See Section 4 Table 7.2 in [WH96]

Gerhard Wanner and Ernst Hairer. Solving ordinary differential equations II. Volume 375. Springer Berlin Heidelberg New York, 1996.

TS: Scalable ODE and DAE Solvers, TSROSW, TSROSWGRK4T, TSROSWSHAMP4, TSROSW4L

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSROSWGRK4T
```

Example 2 (unknown):
```unknown
TSROSWSHAMP4
```

---

## TSROSWASSP3P3S1C#

**URL:** https://petsc.org/release/manualpages/TS/TSROSWASSP3P3S1C/

**Contents:**
- TSROSWASSP3P3S1C#
- See Also#
- Level#
- Location#

A-stable Rosenbrock-W method with SSP explicit part, third order, three stages By default, the Jacobian is only recomputed once per step.

A-stable SPP explicit order 3, 3 stages, CFL 1 (eff = 1/3)

TS: Scalable ODE and DAE Solvers, TSROSW, TSROSWLASSP3P4S2C, TSROSWLLSSP3P4S2C, SSP

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSROSWLASSP3P4S2C
```

Example 2 (unknown):
```unknown
TSROSWLLSSP3P4S2C
```

---

## TSRosWFinalizePackage#

**URL:** https://petsc.org/release/manualpages/TS/TSRosWFinalizePackage/

**Contents:**
- TSRosWFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys everything in the TSROSW package. It is called from PetscFinalize().

TS: Scalable ODE and DAE Solvers, TSROSW, PetscFinalize(), TSRosWInitializePackage()

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSRosWFinalizePackage(void)
```

Example 3 (unknown):
```unknown
PetscFinalize()
```

Example 4 (unknown):
```unknown
TSRosWInitializePackage()
```

---

## TSRosWGetType#

**URL:** https://petsc.org/release/manualpages/TS/TSRosWGetType/

**Contents:**
- TSRosWGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get the type of Rosenbrock-W scheme

ts - timestepping context

rostype - type of Rosenbrock-W scheme

TS: Scalable ODE and DAE Solvers, TSRosWType, TSRosWSetType()

src/ts/impls/rosw/rosw.c

TSRosWGetType_RosW() in src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSRosWGetType(TS ts, TSRosWType *rostype)
```

Example 2 (unknown):
```unknown
TSRosWSetType()
```

---

## TSROSWGRK4T#

**URL:** https://petsc.org/release/manualpages/TS/TSROSWGRK4T/

**Contents:**
- TSROSWGRK4T#
- Note#
- References#
- See Also#
- Level#
- Location#

four stage, fourth order Rosenbrock (not W) method from Kaps and Rentrop [KR79] By default, the Jacobian is only recomputed once per step.

A(89.3 degrees)-stable, |R(infty)| = 0.454.

This method does not provide a dense output formula.

See Section 4 Table 7.2 in [WH96]

Peter Kaps and Peter Rentrop. Generalized Runge–Kutta methods of order four with stepsize control for stiff ordinary differential equations. Numerische Mathematik, 33:55–68, 1979.

Gerhard Wanner and Ernst Hairer. Solving ordinary differential equations II. Volume 375. Springer Berlin Heidelberg New York, 1996.

TS: Scalable ODE and DAE Solvers, TSROSW, TSROSWSHAMP4, TSROSWVELDD4, TSROSW4L

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSROSWSHAMP4
```

Example 2 (unknown):
```unknown
TSROSWVELDD4
```

---

## TSRosWInitializePackage#

**URL:** https://petsc.org/release/manualpages/TS/TSRosWInitializePackage/

**Contents:**
- TSRosWInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function initializes everything in the TSROSW package. It is called from TSInitializePackage().

TS: Scalable ODE and DAE Solvers, TSROSW, PetscInitialize(), TSRosWFinalizePackage()

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSInitializePackage()
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSRosWInitializePackage(void)
```

Example 3 (unknown):
```unknown
PetscInitialize()
```

Example 4 (unknown):
```unknown
TSRosWFinalizePackage()
```

---

## TSROSWLASSP3P4S2C#

**URL:** https://petsc.org/release/manualpages/TS/TSROSWLASSP3P4S2C/

**Contents:**
- TSROSWLASSP3P4S2C#
- See Also#
- Level#
- Location#

L-stable Rosenbrock-W method with SSP explicit part, third order, four stages By default, the Jacobian is only recomputed once per step.

L-stable (A-stable embedded) SPP explicit order 3, 4 stages, CFL 2 (eff = 1/2)

TS: Scalable ODE and DAE Solvers, TSROSW, TSROSWASSP3P3S1C, TSROSWLLSSP3P4S2C, TSSSP

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSROSWASSP3P3S1C
```

Example 2 (unknown):
```unknown
TSROSWLLSSP3P4S2C
```

---

## TSROSWLLSSP3P4S2C#

**URL:** https://petsc.org/release/manualpages/TS/TSROSWLLSSP3P4S2C/

**Contents:**
- TSROSWLLSSP3P4S2C#
- See Also#
- Level#
- Location#

L-stable Rosenbrock-W method with SSP explicit part, third order, four stages By default, the Jacobian is only recomputed once per step.

L-stable (L-stable embedded) SPP explicit order 3, 4 stages, CFL 2 (eff = 1/2)

TS: Scalable ODE and DAE Solvers, TSROSW, TSROSWASSP3P3S1C, TSROSWLASSP3P4S2C, TSSSP

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSROSWASSP3P3S1C
```

Example 2 (unknown):
```unknown
TSROSWLASSP3P4S2C
```

---

## TSROSWR34PRW#

**URL:** https://petsc.org/release/manualpages/TS/TSROSWR34PRW/

**Contents:**
- TSROSWR34PRW#
- References#
- See Also#
- Level#
- Location#

Four stage third order L-stable Rosenbrock-W scheme for PDAE of index 1 [Ran15]. Only an approximate Jacobian is needed. By default, it is only recomputed once per step.

This is strongly A-stable with R(infty) = 0. The embedded method of order 2 is strongly A-stable with R(infty) = 0.25. This method is B_{PR} consistent of order 3. This method is spelled “ROS34PRw” in the paper, an improvement to an earlier “ROS34PRW” method from the same author with B_{PR} order 2.

Joachim Rang. Improved traditional Rosenbrock–Wanner methods for stiff ODEs and DAEs. Journal of Computational and Applied Mathematics, 286:128–144, 2015. doi:10.1016/j.cam.2015.03.010.

TS: Scalable ODE and DAE Solvers, TSROSW

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

---

## TSROSWR3PRL2#

**URL:** https://petsc.org/release/manualpages/TS/TSROSWR3PRL2/

**Contents:**
- TSROSWR3PRL2#
- References#
- See Also#
- Level#
- Location#

Four stage third order L-stable Rosenbrock-W scheme for PDAE of index 1 [Ran15]. Only an approximate Jacobian is needed. By default, it is only recomputed once per step.

This is strongly A-stable with R(infty) = 0. The embedded method of order 2 is strongly A-stable with R(infty) = 0.25. This method is B_{PR} consistent of order 3.

Joachim Rang. Improved traditional Rosenbrock–Wanner methods for stiff ODEs and DAEs. Journal of Computational and Applied Mathematics, 286:128–144, 2015. doi:10.1016/j.cam.2015.03.010.

TS: Scalable ODE and DAE Solvers, TSROSW

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

---

## TSROSWRA34PW2#

**URL:** https://petsc.org/release/manualpages/TS/TSROSWRA34PW2/

**Contents:**
- TSROSWRA34PW2#
- References#
- See Also#
- Level#
- Location#

Four stage third order L-stable Rosenbrock-W scheme for PDAE of index 1 [RA05]. Only an approximate Jacobian is needed. By default, it is only recomputed once per step.

This is strongly A-stable with R(infty) = 0. The embedded method of order 2 is strongly A-stable with R(infty) = 0.48.

J. Rang and L. Angermann. New Rosenbrock W-methods of order 3 for partial differential algebraic equations of index 1. BIT Numerical Mathematics, 45(4):761–787, 2005. doi:10.1007/s10543-005-0035-y.

TS: Scalable ODE and DAE Solvers, TSROSW

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

---

## TSROSWRA3PW#

**URL:** https://petsc.org/release/manualpages/TS/TSROSWRA3PW/

**Contents:**
- TSROSWRA3PW#
- References#
- See Also#
- Level#
- Location#

Three stage third order Rosenbrock-W scheme for PDAE of index 1 [RA05] Only an approximate Jacobian is needed. By default, it is only recomputed once per step.

This is strongly A-stable with R(infty) = 0.73. The embedded method of order 2 is strongly A-stable with R(infty) = 0.73.

J. Rang and L. Angermann. New Rosenbrock W-methods of order 3 for partial differential algebraic equations of index 1. BIT Numerical Mathematics, 45(4):761–787, 2005. doi:10.1007/s10543-005-0035-y.

TS: Scalable ODE and DAE Solvers, TSROSW

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

---

## TSRosWRegisterAll#

**URL:** https://petsc.org/release/manualpages/TS/TSRosWRegisterAll/

**Contents:**
- TSRosWRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the Rosenbrock-W methods in TSROSW

Not Collective, but should be called by all MPI processes which will need the schemes to be registered

TS: Scalable ODE and DAE Solvers, TSROSW, TSRosWRegisterDestroy()

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSRosWRegisterAll(void)
```

Example 2 (unknown):
```unknown
TSRosWRegisterDestroy()
```

---

## TSRosWRegisterDestroy#

**URL:** https://petsc.org/release/manualpages/TS/TSRosWRegisterDestroy/

**Contents:**
- TSRosWRegisterDestroy#
- Synopsis#
- See Also#
- Level#
- Location#

Frees the list of schemes that were registered by TSRosWRegister().

TS: Scalable ODE and DAE Solvers, TSRosWRegister(), TSRosWRegisterAll()

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSRosWRegister()
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSRosWRegisterDestroy(void)
```

Example 3 (unknown):
```unknown
TSRosWRegister()
```

Example 4 (unknown):
```unknown
TSRosWRegisterAll()
```

---

## TSRosWRegisterRos4#

**URL:** https://petsc.org/release/manualpages/TS/TSRosWRegisterRos4/

**Contents:**
- TSRosWRegisterRos4#
- Synopsis#
- Input Parameters#
- Notes#
- References#
- See Also#
- Level#
- Location#

register a fourth order Rosenbrock scheme by providing parameter choices

Not Collective, but the same schemes should be registered on all processes on which they will be used

name - identifier for method

gamma - leading coefficient (diagonal entry)

a2 - design parameter, see Table 7.2 of [WH96]

a3 - design parameter or PETSC_DETERMINE to satisfy one of the order five conditions (Eq 7.22)

b3 - design parameter, see Table 7.2 of [WH96]

e4 - design parameter for embedded method, see coefficient E4 in ros4.f code from Hairer

This routine encodes the design of fourth order Rosenbrock methods as described in [WH96] It is used here to implement several methods from the book and can be used to experiment with new methods. It was written this way instead of by copying coefficients in order to provide better than double precision satisfaction of the order conditions.

Gerhard Wanner and Ernst Hairer. Solving ordinary differential equations II. Volume 375. Springer Berlin Heidelberg New York, 1996.

TS: Scalable ODE and DAE Solvers, TSROSW, TSRosWRegister()

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSRosWRegisterRos4(TSRosWType name, PetscReal gamma, PetscReal a2, PetscReal a3, PetscReal b3, PetscReal e4)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
TSRosWRegister()
```

---

## TSRosWRegister#

**URL:** https://petsc.org/release/manualpages/TS/TSRosWRegister/

**Contents:**
- TSRosWRegister#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

register a TSROSW, Rosenbrock W scheme by providing the entries in the Butcher tableau and optionally embedded approximations and interpolation

Not Collective, but the same schemes should be registered on all processes on which they will be used

name - identifier for method

order - approximation order of method

s - number of stages, this is the dimension of the matrices below

A - Table of propagated stage coefficients (dimension s*s, row-major), strictly lower triangular

Gamma - Table of coefficients in implicit stage equations (dimension s*s, row-major), lower triangular with nonzero diagonal

b - Step completion table (dimension s)

bembed - Step completion table for a scheme of order one less (dimension s, NULL if no embedded scheme is available)

pinterp - Order of the interpolation scheme, equal to the number of columns of binterpt

binterpt - Coefficients of the interpolation formula (dimension s*pinterp)

Several Rosenbrock W methods are provided, this function is only needed to create new methods.

TS: Scalable ODE and DAE Solvers, TSROSW

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSRosWRegister(TSRosWType name, PetscInt order, PetscInt s, const PetscReal A[], const PetscReal Gamma[], const PetscReal b[], const PetscReal bembed[], PetscInt pinterp, const PetscReal binterpt[])
```

---

## TSROSWRODAS3#

**URL:** https://petsc.org/release/manualpages/TS/TSROSWRODAS3/

**Contents:**
- TSROSWRODAS3#
- References#
- See Also#
- Level#
- Location#

Four stage third order L-stable Rosenbrock scheme [SVB+97] By default, the Jacobian is only recomputed once per step.

Both the third order and embedded second order methods are stiffly accurate and L-stable.

A. Sandu, J.G. Verwer, J.G. Blom, E.J. Spee, G.R. Carmichael, and F.A. Potra. Benchmarking stiff ODE solvers for atmospheric chemistry problems II: Rosenbrock solvers. Atmospheric Environment, 31(20):3459–3472, 1997.

TS: Scalable ODE and DAE Solvers, TSROSW, TSROSWSANDU3

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSROSWSANDU3
```

---

## TSROSWRODASPR2#

**URL:** https://petsc.org/release/manualpages/TS/TSROSWRODASPR2/

**Contents:**
- TSROSWRODASPR2#
- Developer Note#
- References#
- See Also#
- Level#
- Location#

Six stage fourth order L-stable Rosenbrock scheme [Ran15] By default, the Jacobian is only recomputed once per step.

Both the fourth order and embedded third order methods are stiffly accurate and L-stable. The method is B_{PR} consistent of order 3, which ensures convergence order for non-stiff, medium stiff, and stiff problems. This method is similar to TSROSWRODASPR, but satisfies one extra B_{PR} order condition.

In numerical experiments with ts/tutorials/ex22.c, I (Jed) find this to produce surprisingly poor results. Although the coefficients pass basic smoke tests, I’m not confident it was tabulated correctly in the paper. It would be informative if someone could reproduce tests from the paper and/or reach out to the author to understand why it fails on this test problem. If the method is implemented correctly, doing so might shed light on an additional analysis lens (or further conditions) for robustness on such problems.

Joachim Rang. Improved traditional Rosenbrock–Wanner methods for stiff ODEs and DAEs. Journal of Computational and Applied Mathematics, 286:128–144, 2015. doi:10.1016/j.cam.2015.03.010.

TS: Scalable ODE and DAE Solvers, TSROSW, TSROSWRODASPR

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSROSWRODASPR
```

Example 2 (unknown):
```unknown
TSROSWRODASPR
```

---

## TSROSWRODASPR#

**URL:** https://petsc.org/release/manualpages/TS/TSROSWRODASPR/

**Contents:**
- TSROSWRODASPR#
- References#
- See Also#
- Level#
- Location#

Six stage fourth order L-stable Rosenbrock scheme [Ran15] By default, the Jacobian is only recomputed once per step.

Both the fourth order and embedded third order methods are stiffly accurate and L-stable. The method is B_{PR} consistent of order 3, which ensures convergence order for non-stiff, medium stiff, and stiff problems.

Joachim Rang. Improved traditional Rosenbrock–Wanner methods for stiff ODEs and DAEs. Journal of Computational and Applied Mathematics, 286:128–144, 2015. doi:10.1016/j.cam.2015.03.010.

TS: Scalable ODE and DAE Solvers, TSROSW, TSROSWR34PRW, TSROSWR3PRL2

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSROSWR34PRW
```

Example 2 (unknown):
```unknown
TSROSWR3PRL2
```

---

## TSROSWSANDU3#

**URL:** https://petsc.org/release/manualpages/TS/TSROSWSANDU3/

**Contents:**
- TSROSWSANDU3#
- References#
- See Also#
- Level#
- Location#

Three stage third order L-stable Rosenbrock scheme [SVB+97] By default, the Jacobian is only recomputed once per step.

The third order method is L-stable, but not stiffly accurate. The second order embedded method is strongly A-stable with R(infty) = 0.5. The internal stages are L-stable. This method is called ROS3 in [SVB+97].

A. Sandu, J.G. Verwer, J.G. Blom, E.J. Spee, G.R. Carmichael, and F.A. Potra. Benchmarking stiff ODE solvers for atmospheric chemistry problems II: Rosenbrock solvers. Atmospheric Environment, 31(20):3459–3472, 1997.

TS: Scalable ODE and DAE Solvers, TSROSW, TSROSWRODAS3

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSROSWRODAS3
```

---

## TSRosWSetRecomputeJacobian#

**URL:** https://petsc.org/release/manualpages/TS/TSRosWSetRecomputeJacobian/

**Contents:**
- TSRosWSetRecomputeJacobian#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set whether to recompute the Jacobian at each stage. The default is to update the Jacobian once per step.

ts - timestepping context

flg - PETSC_TRUE to recompute the Jacobian at each stage

TS: Scalable ODE and DAE Solvers, TSRosWType, TSRosWGetType()

src/ts/impls/rosw/rosw.c

TSRosWSetRecomputeJacobian_RosW() in src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSRosWSetRecomputeJacobian(TS ts, PetscBool flg)
```

Example 2 (unknown):
```unknown
TSRosWGetType()
```

---

## TSRosWSetType#

**URL:** https://petsc.org/release/manualpages/TS/TSRosWSetType/

**Contents:**
- TSRosWSetType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set the type of Rosenbrock-W, TSROSW, scheme

ts - timestepping context

roswtype - type of Rosenbrock-W scheme

TS: Scalable ODE and DAE Solvers, TSRosWGetType(), TSROSW, TSROSW2M, TSROSW2P, TSROSWRA3PW, TSROSWRA34PW2, TSROSWRODAS3, TSROSWSANDU3, TSROSWASSP3P3S1C, TSROSWLASSP3P4S2C, TSROSWLLSSP3P4S2C, TSROSWARK3

src/ts/impls/rosw/rosw.c

TSRosWSetType_RosW() in src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSRosWSetType(TS ts, TSRosWType roswtype)
```

Example 2 (unknown):
```unknown
TSRosWGetType()
```

Example 3 (unknown):
```unknown
TSROSWRA3PW
```

Example 4 (unknown):
```unknown
TSROSWRA34PW2
```

---

## TSROSWSHAMP4#

**URL:** https://petsc.org/release/manualpages/TS/TSROSWSHAMP4/

**Contents:**
- TSROSWSHAMP4#
- Note#
- References#
- See Also#
- Level#
- Location#

four stage, fourth order Rosenbrock (not W) method from Shampine [Sha82] By default, the Jacobian is only recomputed once per step.

A-stable, |R(infty)| = 1/3.

This method does not provide a dense output formula.

See Section 4 Table 7.2 in [WH96]

Lawrence F Shampine. Implementation of Rosenbrock methods. ACM Transactions on Mathematical Software (TOMS), 8(2):93–113, 1982.

Gerhard Wanner and Ernst Hairer. Solving ordinary differential equations II. Volume 375. Springer Berlin Heidelberg New York, 1996.

TS: Scalable ODE and DAE Solvers, TSROSW, TSROSWGRK4T, TSROSWVELDD4, TSROSW4L

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSROSWGRK4T
```

Example 2 (unknown):
```unknown
TSROSWVELDD4
```

---

## TSROSWTHETA1#

**URL:** https://petsc.org/release/manualpages/TS/TSROSWTHETA1/

**Contents:**
- TSROSWTHETA1#
- See Also#
- Level#
- Location#

One stage first order L-stable Rosenbrock-W scheme (aka theta method). Only an approximate Jacobian is needed.

TS: Scalable ODE and DAE Solvers, TSROSW

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

---

## TSROSWTHETA2#

**URL:** https://petsc.org/release/manualpages/TS/TSROSWTHETA2/

**Contents:**
- TSROSWTHETA2#
- See Also#
- Level#
- Location#

One stage second order A-stable Rosenbrock-W scheme (aka theta method). Only an approximate Jacobian is needed.

TS: Scalable ODE and DAE Solvers, TSROSW

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

---

## TSRosWType#

**URL:** https://petsc.org/release/manualpages/TS/TSRosWType/

**Contents:**
- TSRosWType#
- Synopsis#
- See Also#
- Level#
- Location#

String with the name of a Rosenbrock-W TSROSW type

TS: Scalable ODE and DAE Solvers, TSRosWSetType(), TS, TSROSW, TSRosWRegister()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h> 
typedef const char *TSRosWType;
#define TSROSW2M          "2m"
#define TSROSW2P          "2p"
#define TSROSWRA3PW       "ra3pw"
#define TSROSWRA34PW2     "ra34pw2"
#define TSROSWR34PRW      "r34prw"
#define TSROSWR3PRL2      "r3prl2"
#define TSROSWRODAS3      "rodas3"
#define TSROSWRODASPR     "rodaspr"
#define TSROSWRODASPR2    "rodaspr2"
#define TSROSWSANDU3      "sandu3"
#define TSROSWASSP3P3S1C  "assp3p3s1c"
#define TSROSWLASSP3P4S2C "lassp3p4s2c"
#define TSROSWLLSSP3P4S2C "llssp3p4s2c"
#define TSROSWARK3        "ark3"
#define TSROSWTHETA1      "theta1"
#define TSROSWTHETA2      "theta2"
#define TSROSWGRK4T       "grk4t"
#define TSROSWSHAMP4      "shamp4"
#define TSROSWVELDD4      "veldd4"
#define TSROSW4L          "4l"
```

Example 2 (unknown):
```unknown
TSRosWSetType()
```

Example 3 (unknown):
```unknown
TSRosWRegister()
```

---

## TSROSWVELDD4#

**URL:** https://petsc.org/release/manualpages/TS/TSROSWVELDD4/

**Contents:**
- TSROSWVELDD4#
- Note#
- References#
- See Also#
- Level#
- Location#

four stage, fourth order Rosenbrock (not W) method from van Veldhuizen [Vel84] By default, the Jacobian is only recomputed once per step.

A(89.5 degrees)-stable, |R(infty)| = 0.24.

This method does not provide a dense output formula.

See Section 4 Table 7.2 in [WH96]

M van Veldhuizen. D-stability and Kaps-Rentrop-methods. Computing, 32(3):229–237, 1984.

Gerhard Wanner and Ernst Hairer. Solving ordinary differential equations II. Volume 375. Springer Berlin Heidelberg New York, 1996.

TS: Scalable ODE and DAE Solvers, TSROSW, TSROSWGRK4T, TSROSWSHAMP4, TSROSW4L

src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSROSWGRK4T
```

Example 2 (unknown):
```unknown
TSROSWSHAMP4
```

---

## TSROSW#

**URL:** https://petsc.org/release/manualpages/TS/TSROSW/

**Contents:**
- TSROSW#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#

ODE solver using Rosenbrock-W schemes These methods are intended for problems with well-separated time scales, especially when a slow scale is strongly nonlinear such that it is expensive to solve with a fully implicit method. The user should provide the stiff part of the equation using TSSetIFunction() and the non-stiff part with TSSetRHSFunction().

This is an IMEX method.

This method currently only works with autonomous ODE and DAE.

Consider trying TSARKIMEX if the stiff part is strongly nonlinear.

Since this uses a single linear solve per time-step if you wish to lag the Jacobian or preconditioner computation you must use also -snes_lag_jacobian_persists true.

Rosenbrock-W methods are typically specified for autonomous ODE

by the stage equations

and step completion formula

with step size \(h\) and coefficients \(\alpha_{ij}\), \(\gamma_{ij}\), and \(b_i\). Implementing the method in this form would require \(f(u)\) and the Jacobian \(J\) to be available, in addition to the shifted matrix \(I - h \gamma_{ii} J\). Following Hairer and Wanner, we define new variables for the stage equations

The \(k_j\) can be recovered because \(\Gamma\) is invertible. Let \(C\) be the strictly lower triangular part of \(\Gamma^{-1}\) and define

to rewrite the method as

where we have introduced the mass matrix \(M\). Continue by defining

or, more compactly in tensor notation

Note that \(\Gamma^{-1}\) is lower triangular. With this definition of \(\dot{Y}\) in terms of known quantities and the current stage \(y_i\), the stage equations reduce to performing one Newton step (typically with a lagged Jacobian) on the equation

with initial guess \(y_i = 0\).

TS: Scalable ODE and DAE Solvers, TSCreate(), TS, TSSetType(), TSRosWSetType(), TSRosWRegister(), TSROSWTHETA1, TSROSWTHETA2, TSROSW2M, TSROSW2P, TSROSWRA3PW, TSROSWRA34PW2, TSROSWRODAS3, TSROSWSANDU3, TSROSWASSP3P3S1C, TSROSWLASSP3P4S2C, TSROSWLLSSP3P4S2C, TSROSWGRK4T, TSROSWSHAMP4, TSROSWVELDD4, TSROSW4L, TSType

src/ts/impls/rosw/rosw.c

src/ts/tutorials/ex51.c src/ts/tutorials/ex40.c src/ts/tutorials/ex8.c src/ts/tutorials/ex41.c src/ts/tutorials/ex32.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetIFunction()
```

Example 2 (unknown):
```unknown
TSSetRHSFunction()
```

Example 3 (unknown):
```unknown
-snes_lag_jacobian_persists true
```

Example 4 (unknown):
```unknown
TSSetType()
```

---

## TSSetApplicationContext#

**URL:** https://petsc.org/release/manualpages/TS/TSSetApplicationContext/

**Contents:**
- TSSetApplicationContext#
- Synopsis#
- Input Parameters#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Sets an optional user-defined context for the timesteppers that may be accessed, for example inside the user provided TS callbacks with TSGetApplicationContext()

ts - the TS context obtained from TSCreate()

ctx - application context

This only works when ctx is a Fortran derived type (it cannot be a PetscObject), we recommend writing a Fortran interface definition for this function that tells the Fortran compiler the derived data type that is passed in as the ctx argument. See TSGetApplicationContext() for an example.

TS: Scalable ODE and DAE Solvers, TS, TSGetApplicationContext()

src/ts/interface/ts.c

src/ts/tutorials/ex30.c src/ts/tutorials/ex42.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/tutorials/ex77.c src/ts/tutorials/ex48.c src/ts/utils/dmplexlandau/tutorials/ex2.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGetApplicationContext()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetApplicationContext(TS ts, PetscCtx ctx)
```

Example 3 (unknown):
```unknown
PetscObject
```

Example 4 (unknown):
```unknown
TSGetApplicationContext()
```

---

## TSSetCFLTimeLocal#

**URL:** https://petsc.org/release/manualpages/TS/TSSetCFLTimeLocal/

**Contents:**
- TSSetCFLTimeLocal#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Set the local CFL constraint relative to forward Euler

ts - time stepping context

cfltime - maximum stable time step if using forward Euler (value can be different on each process)

After calling this function, the global CFL time can be obtained by calling TSGetCFLTime()

TS: Scalable ODE and DAE Solvers, TSGetCFLTime(), TSADAPTCFL

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetCFLTimeLocal(TS ts, PetscReal cfltime)
```

Example 2 (unknown):
```unknown
TSGetCFLTime()
```

---

## TSSetComputeExactError#

**URL:** https://petsc.org/release/manualpages/TS/TSSetComputeExactError/

**Contents:**
- TSSetComputeExactError#
- Synopsis#
- Input Parameters#
- Calling sequence of exactError#
- See Also#
- Level#
- Location#
- Examples#

Set the function used to automatically compute the exact error for the timestepping.

ts - time stepping context

exactError - The function which computes the solution error

ts - The timestepping context

u - The approximate solution vector

e - The vector in which the error is stored

TS: Scalable ODE and DAE Solvers, TS, TSGetComputeExactError(), TSComputeExactError()

src/ts/interface/ts.c

src/ts/tutorials/ex77.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetComputeExactError(TS ts, PetscErrorCode (*exactError)(TS ts, Vec u, Vec e))
```

Example 2 (unknown):
```unknown
TSGetComputeExactError()
```

Example 3 (unknown):
```unknown
TSComputeExactError()
```

---

## TSSetComputeInitialCondition#

**URL:** https://petsc.org/release/manualpages/TS/TSSetComputeInitialCondition/

**Contents:**
- TSSetComputeInitialCondition#
- Synopsis#
- Input Parameters#
- Calling sequence of initCondition#
- See Also#
- Level#
- Location#
- Examples#

Set the function used to automatically compute an initial condition for the timestepping.

ts - time stepping context

initCondition - The function which computes an initial condition

ts - The timestepping context

e - The input vector in which the initial condition is to be stored

TS: Scalable ODE and DAE Solvers, TS, TSGetComputeInitialCondition(), TSComputeInitialCondition()

src/ts/interface/ts.c

src/ts/tutorials/ex77.c src/ts/tutorials/ex45.c src/ts/tutorials/ex53.c src/ts/tutorials/ex76.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetComputeInitialCondition(TS ts, PetscErrorCode (*initCondition)(TS ts, Vec e))
```

Example 2 (unknown):
```unknown
initCondition
```

Example 3 (unknown):
```unknown
TSGetComputeInitialCondition()
```

Example 4 (unknown):
```unknown
TSComputeInitialCondition()
```

---

## TSSetConvergedReason#

**URL:** https://petsc.org/release/manualpages/TS/TSSetConvergedReason/

**Contents:**
- TSSetConvergedReason#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the reason for handling the convergence of TSSolve().

Logically Collective; reason must contain common value

reason - negative value indicates diverged, positive value converged, see TSConvergedReason or the manual pages for the individual convergence tests for complete lists

Can only be called while TSSolve() is active.

TS: Scalable ODE and DAE Solvers, TS, TSSolve(), TSConvergedReason

src/ts/interface/ts.c

src/ts/tutorials/ex44.c src/ts/tutorials/ex40.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetConvergedReason(TS ts, TSConvergedReason reason)
```

Example 2 (unknown):
```unknown
TSConvergedReason
```

Example 3 (unknown):
```unknown
TSConvergedReason
```

---

## TSSetCostGradients#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSSetCostGradients/

**Contents:**
- TSSetCostGradients#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the initial value of the gradients of the cost function w.r.t. initial values and w.r.t. the problem parameters for use by the TS adjoint routines.

ts - the TS context obtained from TSCreate()

numcost - number of gradients to be computed, this is the number of cost functions

lambda - gradients with respect to the initial condition variables, the dimension and parallel layout of these vectors is the same as the ODE solution vector

mu - gradients with respect to the parameters, the number of entries in these vectors is the same as the number of parameters

the entries in these vectors must be correctly initialized with the values lambda_i = df/dy|finaltime mu_i = df/dp|finaltime

After TSAdjointSolve() is called the lambda and the mu contain the computed sensitivities

TS, TSAdjointSolve(), TSGetCostGradients()

src/ts/interface/sensitivity/tssen.c

src/ts/tutorials/extchemfield.c src/ts/tutorials/ex20opt_p.c src/ts/tutorials/extchem.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/tutorials/ex20opt_ic.c src/ts/tutorials/ex20adj.c src/ts/tutorials/ex23fwdadj.c src/ts/tutorials/ex20td.c src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSSetCostGradients(TS ts, PetscInt numcost, Vec lambda[], Vec mu[])
```

Example 2 (unknown):
```unknown
TSAdjointSolve()
```

Example 3 (unknown):
```unknown
TSAdjointSolve()
```

Example 4 (unknown):
```unknown
TSGetCostGradients()
```

---

## TSSetCostHessianProducts#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSSetCostHessianProducts/

**Contents:**
- TSSetCostHessianProducts#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the initial value of the Hessian-vector products of the cost function w.r.t. initial values and w.r.t. the problem parameters for use by the TS adjoint routines.

ts - the TS context obtained from TSCreate()

numcost - number of cost functions

lambda2 - Hessian-vector product with respect to the initial condition variables, the dimension and parallel layout of these vectors is the same as the ODE solution vector

mu2 - Hessian-vector product with respect to the parameters, the number of entries in these vectors is the same as the number of parameters

dir - the direction vector that are multiplied with the Hessian of the cost functions

Hessian of the cost function is completely different from Hessian of the ODE/DAE system

For second-order adjoint, one needs to call this function and then TSAdjointSetForward() before TSSolve().

After TSAdjointSolve() is called, the lambda2 and the mu2 will contain the computed second-order adjoint sensitivities, and can be used to produce Hessian-vector product (not the full Hessian matrix). Users must provide a direction vector; it is usually generated by an optimization solver.

Passing NULL for lambda2 disables the second-order calculation.

TS: Scalable ODE and DAE Solvers, TS, TSAdjointSolve(), TSAdjointSetForward()

src/ts/interface/sensitivity/tssen.c

src/ts/tutorials/ex20opt_p.c src/ts/tutorials/ex20opt_ic.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSSetCostHessianProducts(TS ts, PetscInt numcost, Vec lambda2[], Vec mu2[], Vec dir)
```

Example 2 (unknown):
```unknown
TSAdjointSetForward()
```

Example 3 (unknown):
```unknown
TSAdjointSolve()
```

Example 4 (unknown):
```unknown
TSAdjointSolve()
```

---

## TSSetCostIntegrand#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSSetCostIntegrand/

**Contents:**
- TSSetCostIntegrand#
- Synopsis#
- Input Parameters#
- Calling sequence of rf#
- Calling sequence of drduf#
- Calling sequence of drdpf#
- Notes#
- See Also#
- Level#
- Location#

Sets the routine for evaluating the integral term in one or more cost functions

ts - the TS context obtained from TSCreate()

numcost - number of gradients to be computed, this is the number of cost functions

costintegral - vector that stores the integral values

rf - routine for evaluating the integrand function

drduf - function that computes the gradients of the r with respect to u

drdpf - function that computes the gradients of the r with respect to p, can be NULL if parametric sensitivity is not desired (mu = NULL)

fwd - flag indicating whether to evaluate cost integral in the forward run or the adjoint run

ctx - [optional] application context for private data for the function evaluation routine (may be NULL)

F - the computed value of the function

ctx - the application context

dRdU - the computed gradients of the r with respect to u

ctx - the application context

dRdP - the computed gradients of the r with respect to p

ctx - the application context

For optimization there is usually a single cost function (numcost = 1). For sensitivities there may be multiple cost functions

Use TSCreateQuadratureTS() and TSForwardSetSensitivities() instead

TS: Scalable ODE and DAE Solvers, TS, TSSetRHSJacobianP(), TSGetCostGradients(), TSSetCostGradients(), TSCreateQuadratureTS(), TSForwardSetSensitivities()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSSetCostIntegrand(TS ts, PetscInt numcost, Vec costintegral, PetscErrorCode (*rf)(TS ts, PetscReal t, Vec U, Vec F, PetscCtx ctx), PetscErrorCode (*drduf)(TS ts, PetscReal t, Vec U, Vec *dRdU, PetscCtx ctx), PetscErrorCode (*drdpf)(TS ts, PetscReal t, Vec U, Vec *dRdP, PetscCtx ctx), PetscBool fwd, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSCreateQuadratureTS()
```

Example 3 (unknown):
```unknown
TSForwardSetSensitivities()
```

Example 4 (unknown):
```unknown
TSSetRHSJacobianP()
```

---

## TSSetDM#

**URL:** https://petsc.org/release/manualpages/TS/TSSetDM/

**Contents:**
- TSSetDM#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the DM that may be used by some nonlinear solvers or preconditioners under the TS

ts - the TS integrator object

dm - the dm, cannot be NULL

A DM can only be used for solving one problem at a time because information about the problem is stored on the DM, even when not using interfaces like DMTSSetIFunction(). Use DMClone() to get a distinct DM when solving different problems using the same function space.

TS: Scalable ODE and DAE Solvers, TS, DM, TSGetDM(), SNESSetDM(), SNESGetDM()

src/ts/interface/ts.c

src/ts/tutorials/ex14.c src/ts/tutorials/ex45.c src/ts/tutorials/ex17.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/utils/dmplexlandau/tutorials/ex2.c src/ts/tutorials/ex47.c src/ts/tutorials/ex22f.F90 src/tao/unconstrained/tutorials/burgers_spectral.c src/ts/utils/dmplexlandau/tutorials/ex1f90.F90

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetDM(TS ts, DM dm)
```

Example 2 (unknown):
```unknown
DMTSSetIFunction()
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

## TSSetDuration#

**URL:** https://petsc.org/release/manualpages/TS/TSSetDuration/

**Contents:**
- TSSetDuration#
- Synopsis#
- Level#
- Location#

Deprecated, use TSSetMaxSteps() and TSSetMaxTime().

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetMaxSteps()
```

Example 2 (unknown):
```unknown
TSSetMaxTime()
```

Example 3 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetDuration(TS ts, PetscInt maxsteps, PetscReal maxtime)
```

---

## TSSetEquationType#

**URL:** https://petsc.org/release/manualpages/TS/TSSetEquationType/

**Contents:**
- TSSetEquationType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the type of the equation that TS is solving.

equation_type - see TSEquationType

TS: Scalable ODE and DAE Solvers, TS, TSGetEquationType(), TSEquationType

src/ts/interface/ts.c

src/ts/tutorials/ex36.c src/ts/tutorials/ex20opt_p.c src/ts/tutorials/ex35.cxx src/ts/tutorials/ex20opt_ic.c src/ts/tutorials/ex20adj.c src/ts/tutorials/ex25.c src/ts/tutorials/ex20td.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetEquationType(TS ts, TSEquationType equation_type)
```

Example 2 (unknown):
```unknown
TSEquationType
```

Example 3 (unknown):
```unknown
TSGetEquationType()
```

Example 4 (unknown):
```unknown
TSEquationType
```

---

## TSSetErrorIfStepFails#

**URL:** https://petsc.org/release/manualpages/TS/TSSetErrorIfStepFails/

**Contents:**
- TSSetErrorIfStepFails#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Immediately error if no step succeeds during TSSolve()

err - PETSC_TRUE to error if no step succeeds, PETSC_FALSE to return without failure

-ts_error_if_step_fails - Error if no step succeeds

TS: Scalable ODE and DAE Solvers, TS, TSGetSNESIterations(), TSGetKSPIterations(), TSSetMaxStepRejections(), TSGetStepRejections(), TSGetSNESFailures(), TSGetConvergedReason()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetErrorIfStepFails(TS ts, PetscBool err)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
TSGetSNESIterations()
```

Example 4 (unknown):
```unknown
TSGetKSPIterations()
```

---

## TSSetEvaluationTimes#

**URL:** https://petsc.org/release/manualpages/TS/TSSetEvaluationTimes/

**Contents:**
- TSSetEvaluationTimes#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

sets the evaluation points. The solution will be computed and stored for each time requested

ts - the time-stepper

n - number of the time points

time_points - array of the time points, must be increasing

-ts_eval_times t0,…,tn - Sets the evaluation times

The elements in time_points must be all increasing. They correspond to the intermediate points to be saved.

TS_EXACTFINALTIME_MATCHSTEP must be used to make the last time step in each sub-interval match the intermediate points specified.

The intermediate solutions are saved in a vector array that can be accessed with TSGetEvaluationSolutions(). Thus using evaluation times may pressure the memory system when using a large number of time points.

TS: Scalable ODE and DAE Solvers, TS, TSGetEvaluationTimes(), TSGetEvaluationSolutions(), TSSetTimeSpan()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetEvaluationTimes(TS ts, PetscInt n, PetscReal time_points[])
```

Example 2 (unknown):
```unknown
time_points
```

Example 3 (unknown):
```unknown
TS_EXACTFINALTIME_MATCHSTEP
```

Example 4 (unknown):
```unknown
TSGetEvaluationSolutions()
```

---

## TSSetEventHandler#

**URL:** https://petsc.org/release/manualpages/TS/TSSetEventHandler/

**Contents:**
- TSSetEventHandler#
- Synopsis#
- Input Parameters#
- Calling sequence of indicator#
- Calling sequence of postevent#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#

Sets functions and parameters used for indicating events and handling them

ts - the TS context obtained from TSCreate()

nevents - number of local events (i.e. managed by the given MPI process)

direction - direction of zero crossing to be detected (one for each local event). -1 => zero crossing in negative direction, +1 => zero crossing in positive direction, 0 => both ways

terminate - flag to indicate whether time stepping should be terminated after an event is detected (one for each local event)

indicator - callback defininig the user indicator functions whose sign changes (see direction) mark presence of the events

postevent - [optional] user post-event callback; it can change the solution, ODE etc at the time of the event

ctx - [optional] user-defined context for private data for the indicator() and postevent() routines (use NULL if no context is desired)

fvalue - output array with values of local indicator functions (length == nevents) for time t and state-vector U

ctx - the context passed as the final argument to TSSetEventHandler()

nevents_zero - number of triggered local events (whose indicator function is marked as crossing zero, and direction is appropriate)

events_zero - indices of the triggered local events

forwardsolve - flag to indicate whether TS is doing a forward solve (PETSC_TRUE) or adjoint solve (PETSC_FALSE)

ctx - the context passed as the final argument to TSSetEventHandler()

-ts_event_tol tol - tolerance for zero crossing check of indicator functions

-ts_event_monitor - print choices made by event handler

-ts_event_recorder_initial_size recsize - initial size of event recorder

-ts_event_post_event_step dt1 - first time step after event

-ts_event_post_event_second_step dt2 - second time step after event

-ts_event_dt_min dt - minimum time step considered for TSEvent

The indicator functions should be defined in the indicator callback using the components of solution U and/or time t. Note that U is PetscScalar-valued, and the indicator functions are PetscReal-valued. It is the user’s responsibility to properly handle this difference, e.g. by applying PetscRealPart() or other appropriate conversion means.

The full set of events is distributed (by the user design) across MPI processes, with each process defining its own local sub-set of events. However, the postevent() callback invocation is performed synchronously on all processes, including those processes which have not currently triggered any events.

TS: Scalable ODE and DAE Solvers, Handling of discontinuities, TSEvent, TSCreate(), TSSetTimeStep(), TSSetConvergedReason()

src/ts/event/tsevent.c

src/ts/tutorials/ex32.c src/ts/tutorials/ex44.c src/ts/tutorials/ex41.c src/ts/tutorials/ex40.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSSetEventHandler(TS ts, PetscInt nevents, PetscInt direction[], PetscBool terminate[], PetscErrorCode (*indicator)(TS ts, PetscReal t, Vec U, PetscReal fvalue[], PetscCtx ctx), PetscErrorCode (*postevent)(TS ts, PetscInt nevents_zero, PetscInt events_zero[], PetscReal t, Vec U, PetscBool forwardsolve, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
indicator()
```

Example 3 (unknown):
```unknown
postevent()
```

Example 4 (unknown):
```unknown
TSSetEventHandler()
```

---

## TSSetEventTolerances#

**URL:** https://petsc.org/release/manualpages/TS/TSSetEventTolerances/

**Contents:**
- TSSetEventTolerances#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Set tolerances for event (indicator function) zero crossings

ts - time integration context

tol - tolerance, PETSC_CURRENT to leave the current value

vtol - array of tolerances or NULL, used in preference to tol if present

-ts_event_tol tol - tolerance for event (indicator function) zero crossing

One must call TSSetEventHandler() before setting the tolerances.

The size of vtol should be equal to the number of events on the given process.

This function can be also called from the postevent() callback set with TSSetEventHandler(), to adjust the tolerances on the fly.

TS: Scalable ODE and DAE Solvers, Handling of discontinuities, TS, TSEvent, TSSetEventHandler()

src/ts/event/tsevent.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSSetEventTolerances(TS ts, PetscReal tol, PetscReal vtol[])
```

Example 2 (unknown):
```unknown
PETSC_CURRENT
```

Example 3 (unknown):
```unknown
TSSetEventHandler()
```

Example 4 (unknown):
```unknown
postevent()
```

---

## TSSetExactFinalTime#

**URL:** https://petsc.org/release/manualpages/TS/TSSetExactFinalTime/

**Contents:**
- TSSetExactFinalTime#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Determines whether to adapt the final time step to match the exact final time, to interpolate the solution to the exact final time, or to just return at the final time TS computed (which may be slightly larger than the requested final time).

ts - the time-step context

eftopt - exact final time option

-ts_exact_final_time stepover,interpolate,matchstep - select the final step approach at runtime

If you use the option TS_EXACTFINALTIME_STEPOVER the solution may be at a very different time then the final time you selected.

TS: Scalable ODE and DAE Solvers, TS, TSExactFinalTimeOption, TSGetExactFinalTime()

src/ts/interface/ts.c

src/ml/da/tutorials/ex3.c src/ts/tutorials/ex1.c src/ts/tutorials/ex45.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ml/da/tutorials/ex1.c src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex4.c src/tao/unconstrained/tutorials/burgers_spectral.c src/ts/utils/dmplexlandau/tutorials/ex1f90.F90

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetExactFinalTime(TS ts, TSExactFinalTimeOption eftopt)
```

Example 2 (elixir):
```elixir
TS_EXACTFINALTIME_STEPOVER    - Don't do anything if final time is exceeded, just use it
  TS_EXACTFINALTIME_INTERPOLATE - Interpolate back to final time if the final time is exceeded
  TS_EXACTFINALTIME_MATCHSTEP   - Adapt final time step to ensure the computed final time exactly equals the requested final time
```

Example 3 (unknown):
```unknown
TS_EXACTFINALTIME_STEPOVER
```

Example 4 (unknown):
```unknown
TSExactFinalTimeOption
```

---

## TSSetForcingFunction#

**URL:** https://petsc.org/release/manualpages/TS/TSSetForcingFunction/

**Contents:**
- TSSetForcingFunction#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Provide a function that computes a forcing term for a ODE or PDE

ts - the TS context obtained from TSCreate()

func - routine for evaluating the forcing function

ctx - [optional] user-defined context for private data for the function evaluation routine (may be NULL)

This routine is useful for testing accuracy of time integration schemes when using the Method of Manufactured Solutions to create closed-form solutions with a non-physical forcing term. It allows you to use the Method of Manufactored Solution without directly editing the definition of the problem you are solving and hence possibly introducing bugs.

This replaces the ODE F(u,u_t,t) = 0 the TS is solving with F(u,u_t,t) - func(t) = 0

This forcing function does not depend on the solution to the equations, it can only depend on spatial location, time, and possibly parameters, the parameters can be passed in the ctx variable.

For low-dimensional problems solved in serial, such as small discrete systems, TSMonitorLGError() can be used to monitor the error history.

TS: Scalable ODE and DAE Solvers, TS, TSForcingFn, TSSetRHSJacobian(), TSSetIJacobian(), TSComputeSolutionFunction(), TSSetSolutionFunction()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetForcingFunction(TS ts, TSForcingFn *func, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSMonitorLGError()
```

Example 3 (unknown):
```unknown
TSForcingFn
```

Example 4 (unknown):
```unknown
TSSetRHSJacobian()
```

---

## TSSetFromOptions#

**URL:** https://petsc.org/release/manualpages/TS/TSSetFromOptions/

**Contents:**
- TSSetFromOptions#
- Synopsis#
- Input Parameter#
- Options Database Keys#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets various TS parameters from the options database

ts - the TS context obtained from TSCreate()

-ts_type type - see TSType

-ts_save_trajectory - checkpoint the solution at each time-step

-ts_max_time time - maximum time to compute to

-ts_time_span t0,…,tf - sets the time span, solutions are computed and stored for each indicated time, init_time and max_time are set

-ts_eval_times t0,…,tn - time points where solutions are computed and stored for each indicated time

-ts_max_steps steps - maximum time-step number to execute until (possibly with nonzero starting value)

-ts_run_steps steps - maximum number of time steps for TSSolve() to take on each call

-ts_init_time time - initial time to start computation

-ts_final_time time - final time to compute to (deprecated: use -ts_max_time)

-ts_time_step dt - initial time step (only a suggestion, the actual initial time step used differ)

-ts_exact_final_time (stepover,interpolate,matchstep) - whether to stop at the exact given final time and how to compute the solution at that time

-ts_max_snes_failures maxfailures - Maximum number of nonlinear solve failures allowed

-ts_max_step_rejections maxrejects - Maximum number of step rejections before step fails

-ts_error_if_step_fails (true|false) - Error if no step succeeds

-ts_rtol rtol - relative tolerance for local truncation error

-ts_atol atol - Absolute tolerance for local truncation error

-ts_rhs_jacobian_test_mult - mat_shell_test_mult_view - test the Jacobian at each iteration against finite difference with RHS function

-ts_rhs_jacobian_test_mult_transpose - test the Jacobian at each iteration against finite difference with RHS function

-ts_adjoint_solve (true|false) - After solving the ODE/DAE solve the adjoint problem (requires -ts_save_trajectory)

-ts_fd_color - Use finite differences with coloring to compute IJacobian

-ts_monitor - print information at each timestep

-ts_monitor_cancel - Cancel all monitors

-ts_monitor_wall_clock_time - Monitor wall-clock time, KSP iterations, and SNES iterations per step

-ts_monitor_lg_solution - Monitor solution graphically

-ts_monitor_lg_error - Monitor error graphically

-ts_monitor_error - Monitors norm of error

-ts_monitor_lg_timestep - Monitor timestep size graphically

-ts_monitor_lg_timestep_log - Monitor log timestep size graphically

-ts_monitor_lg_snes_iterations - Monitor number nonlinear iterations for each timestep graphically

-ts_monitor_lg_ksp_iterations - Monitor number nonlinear iterations for each timestep graphically

-ts_monitor_sp_eig - Monitor eigenvalues of linearized operator graphically

-ts_monitor_draw_solution - Monitor solution graphically

-ts_monitor_draw_solution_phase xleft,yleft,xright,yright - Monitor solution graphically with phase diagram, requires problem with exactly 2 degrees of freedom

-ts_monitor_draw_error - Monitor error graphically, requires use to have provided TSSetSolutionFunction()

-ts_monitor_solution [ascii binary draw][:filename][:viewerformat] - monitors the solution at each timestep

-ts_monitor_solution_interval interval - output once every interval (default=1) time steps. Use -1 to only output at the end of the simulation

-ts_monitor_solution_skip_initial - skip writing of initial condition

-ts_monitor_solution_vtk filename.vts,filename.vtu - Save each time step to a binary file, use filename-%%03” PetscInt_FMT “.vts (filename-%%03” PetscInt_FMT “.vtu)

-ts_monitor_solution_vtk_interval interval - output once every interval (default=1) time steps. Use -1 to only output at the end of the simulation

-ts_monitor_envelope - determine maximum and minimum value of each component of the solution over the solution time

See SNESSetFromOptions() and KSPSetFromOptions() for how to control the nonlinear and linear solves used by the time-stepper.

Certain SNES options get reset for each new nonlinear solver, for example -snes_lag_jacobian its and -snes_lag_preconditioner its, in order to retain them over the multiple nonlinear solves that TS uses you must also provide -snes_lag_jacobian_persists true and -snes_lag_preconditioner_persists true

We should unify all the -ts_monitor options in the way that -xxx_view has been unified

TS: Scalable ODE and DAE Solvers, TS, TSGetType()

src/ts/interface/ts.c

src/ml/da/tutorials/ex3.c src/ts/tutorials/ex1.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ml/da/tutorials/ex1.c src/ml/da/tutorials/ex2.c src/ts/utils/dmplexlandau/tutorials/ex2.c src/ml/da/tutorials/ex4.c src/tao/unconstrained/tutorials/burgers_spectral.c src/ts/utils/dmplexlandau/tutorials/ex1f90.F90

TSSetFromOptions_ARKIMEX() in src/ts/impls/arkimex/arkimex.c TSSetFromOptions_BDF() in src/ts/impls/bdf/bdf.c TSSetFromOptions_EIMEX() in src/ts/impls/eimex/eimex.c TSSetFromOptions_Euler() in src/ts/impls/explicit/euler/euler.c TSSetFromOptions_RK() in src/ts/impls/explicit/rk/rk.c TSSetFromOptions_SSP() in src/ts/impls/explicit/ssp/ssp.c TSSetFromOptions_GLEE() in src/ts/impls/glee/glee.c TSSetFromOptions_Alpha() in src/ts/impls/implicit/alpha/alpha1.c TSSetFromOptions_Alpha() in src/ts/impls/implicit/alpha/alpha2.c TSSetFromOptions_DiscGrad() in src/ts/impls/implicit/discgrad/tsdiscgrad.c TSSetFromOptions_GLLE() in src/ts/impls/implicit/glle/glle.c TSSetFromOptions_IRK() in src/ts/impls/implicit/irk/irk.c TSSetFromOptions_Sundials() in src/ts/impls/implicit/sundials/sundials.c TSSetFromOptions_Theta() in src/ts/impls/implicit/theta/theta.c TSSetFromOptions_Mimex() in src/ts/impls/mimex/mimex.c TSSetFromOptions_MPRK() in src/ts/impls/multirate/mprk.c TSSetFromOptions_Pseudo() in src/ts/impls/pseudo/posindep.c TSSetFromOptions_RosW() in src/ts/impls/rosw/rosw.c TSSetFromOptions_BasicSymplectic() in src/ts/impls/symplectic/basicsymplectic/basicsymplectic.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetFromOptions(TS ts)
```

Example 2 (unknown):
```unknown
-ts_max_time
```

Example 3 (unknown):
```unknown
-ts_save_trajectory
```

Example 4 (unknown):
```unknown
SNESSetFromOptions()
```

---

## TSSetFunctionDomainError#

**URL:** https://petsc.org/release/manualpages/TS/TSSetFunctionDomainError/

**Contents:**
- TSSetFunctionDomainError#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#

Set a function that tests if the current state vector is valid

func - function called within TSFunctionDomainError()

time - the current time (of the stage)

state - the state to check if it is valid

accept - (output parameter) PETSC_FALSE if the state is not acceptable, PETSC_TRUE if acceptable

accept must be collectively specified. If an implicit ODE solver is being used then, in addition to providing this routine, the user’s code should call SNESSetFunctionDomainError() when domain errors occur during function evaluations where the functions are provided by TSSetIFunction() or TSSetRHSFunction(). Use TSGetSNES() to obtain the SNES object

The naming of this function is inconsistent with the SNESSetFunctionDomainError() since one takes a function pointer and the other does not.

TS: Scalable ODE and DAE Solvers, TSAdaptCheckStage(), TSFunctionDomainError(), SNESSetFunctionDomainError(), TSGetSNES()

src/ts/interface/ts.c

src/ts/tutorials/ex30.c src/ts/tutorials/ex42.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetFunctionDomainError(TS ts, PetscErrorCode (*func)(TS ts, PetscReal time, Vec state, PetscBool *accept))
```

Example 2 (unknown):
```unknown
TSFunctionDomainError()
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (unknown):
```unknown
SNESSetFunctionDomainError()
```

---

## TSSetI2Function#

**URL:** https://petsc.org/release/manualpages/TS/TSSetI2Function/

**Contents:**
- TSSetI2Function#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the function to compute F(t,U,U_t,U_tt) where F = 0 is the DAE to be solved.

ts - the TS context obtained from TSCreate()

F - vector to hold the residual (or NULL to have it created internally)

fun - the function evaluation routine

ctx - user-defined context for private data for the function evaluation routine (may be NULL)

TS: Scalable ODE and DAE Solvers, TS, TSI2FunctionFn, TSSetI2Jacobian(), TSSetIFunction(), TSCreate(), TSSetRHSFunction()

src/ts/interface/ts.c

src/ts/tutorials/ex44.c src/ts/tutorials/ex43.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetI2Function(TS ts, Vec F, TSI2FunctionFn *fun, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSI2FunctionFn
```

Example 3 (unknown):
```unknown
TSSetI2Jacobian()
```

Example 4 (unknown):
```unknown
TSSetIFunction()
```

---

## TSSetI2Jacobian#

**URL:** https://petsc.org/release/manualpages/TS/TSSetI2Jacobian/

**Contents:**
- TSSetI2Jacobian#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Set the function to compute the matrix dF/dU + vdF/dU_t + adF/dU_tt where F(t,U,U_t,U_tt) is the function you provided with TSSetI2Function().

ts - the TS context obtained from TSCreate()

J - matrix to hold the Jacobian values

P - matrix for constructing the preconditioner (may be same as J)

jac - the Jacobian evaluation routine, see TSI2JacobianFn for the calling sequence

ctx - user-defined context for private data for the Jacobian evaluation routine (may be NULL)

The matrices J and P are exactly the matrices that are used by SNES for the nonlinear solve.

The matrix dF/dU + vdF/dU_t + adF/dU_tt you provide turns out to be the Jacobian of G(U) = F(t,U,W+vU,W’+aU) where F(t,U,U_t,U_tt) = 0 is the DAE to be solved. The time integrator internally approximates U_t by W+vU and U_tt by W’+aU where the positive “shift” parameters ‘v’ and ‘a’ and vectors W, W’ depend on the integration method, step size, and past states.

TS: Scalable ODE and DAE Solvers, TS, TSI2JacobianFn, TSSetI2Function(), TSGetI2Jacobian()

src/ts/interface/ts.c

src/ts/tutorials/ex44.c src/ts/tutorials/ex43.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetI2Function()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetI2Jacobian(TS ts, Mat J, Mat P, TSI2JacobianFn *jac, PetscCtx ctx)
```

Example 3 (unknown):
```unknown
TSI2JacobianFn
```

Example 4 (unknown):
```unknown
TSI2JacobianFn
```

---

## TSSetIFunction#

**URL:** https://petsc.org/release/manualpages/TS/TSSetIFunction/

**Contents:**
- TSSetIFunction#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Set the function to compute F(t,U,U_t) where F() = 0 is the DAE to be solved.

ts - the TS context obtained from TSCreate()

r - vector to hold the residual (or NULL to have it created internally)

f - the function evaluation routine

ctx - user-defined context for private data for the function evaluation routine (may be NULL)

The user MUST call either this routine or TSSetRHSFunction() to define the ODE. When solving DAEs you must use this function.

TS: Scalable ODE and DAE Solvers, TS, TSIFunctionFn, TSSetRHSJacobian(), TSSetRHSFunction(), TSSetIJacobian()

src/ts/interface/ts.c

src/ts/tutorials/ex14.c src/ts/tutorials/ex17.c src/ts/tutorials/ex20opt_ic.c src/ts/tutorials/ex49.c src/ts/tutorials/ex15.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/utils/dmplexlandau/tutorials/ex2.c src/ts/tutorials/ex41.c src/ts/tutorials/ex22f.F90 src/ts/utils/dmplexlandau/tutorials/ex1f90.F90

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetIFunction(TS ts, Vec r, TSIFunctionFn *f, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSSetRHSFunction()
```

Example 3 (unknown):
```unknown
TSIFunctionFn
```

Example 4 (unknown):
```unknown
TSSetRHSJacobian()
```

---

## TSSetIHessianProduct#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSSetIHessianProduct/

**Contents:**
- TSSetIHessianProduct#
- Synopsis#
- Input Parameters#
- Calling sequence of ihessianproductfunc1#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the function that computes the vector-Hessian-vector product. The Hessian is the second-order derivative of F (IFunction) w.r.t. the state variable.

ts - TS context obtained from TSCreate()

ihp1 - an array of vectors storing the result of vector-Hessian-vector product for \(F_{UU}\)

ihessianproductfunc1 - vector-Hessian-vector product function for \(F_{UU}\)

ihp2 - an array of vectors storing the result of vector-Hessian-vector product for \(F_{UP}\)

ihessianproductfunc2 - vector-Hessian-vector product function for \(F_{UP}\)

ihp3 - an array of vectors storing the result of vector-Hessian-vector product for \(F_{PU}\)

ihessianproductfunc3 - vector-Hessian-vector product function for \(F_{PU}\)

ihp4 - an array of vectors storing the result of vector-Hessian-vector product for \(F_{PP}\)

ihessianproductfunc4 - vector-Hessian-vector product function for \(F_{PP}\)

ctx - [optional] function context

U - input vector (current ODE solution)

Vl - an array of input vectors to be left-multiplied with the Hessian

Vr - input vector to be right-multiplied with the Hessian

VHV - an array of output vectors for vector-Hessian-vector product

ctx - [optional] function context

All other functions have the same calling sequence as ihessianproductfunc1, so their descriptions are omitted for brevity.

The first Hessian function and the working array are required. As an example to implement the callback functions, the second callback function calculates the vector-Hessian-vector product \(Vl_n^T*F_UP*Vr\) where the vector \(Vl_n\) (n-th element in the array Vl) and Vr are of size N and M respectively, and the Hessian \(F_{UP}\) is of size \(N x N x M.\) Each entry of \(F_{UP}\) corresponds to the derivative \( F_UP[i][j][k] = \frac{\partial^2 F[i]}{\partial U[j] \partial P[k]}.\) The result of the vector-Hessian-vector product for \(Vl_n\) needs to be stored in vector \(VHV_n\) with the j-th entry being \( VHV_n[j] = \sum_i \sum_k {Vl_n[i] * F_UP[i][j][k] * Vr[k]}\) If the cost function is a scalar, there will be only one vector in Vl and VHV.

TS: Scalable ODE and DAE Solvers, TS

src/ts/interface/sensitivity/tssen.c

src/ts/tutorials/ex20opt_p.c src/ts/tutorials/ex20opt_ic.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSSetIHessianProduct(TS ts, Vec ihp1[], PetscErrorCode (*ihessianproductfunc1)(TS ts, PetscReal t, Vec U, Vec Vl[], Vec Vr, Vec VHV[], PetscCtx ctx), Vec ihp2[], PetscErrorCode (*ihessianproductfunc2)(TS ts, PetscReal t, Vec U, Vec Vl[], Vec Vr, Vec VHV[], PetscCtx ctx), Vec ihp3[], PetscErrorCode (*ihessianproductfunc3)(TS ts, PetscReal t, Vec U, Vec Vl[], Vec Vr, Vec VHV[], PetscCtx ctx), Vec ihp4[], PetscErrorCode (*ihessianproductfunc4)(TS ts, PetscReal t, Vec U, Vec Vl[], Vec Vr, Vec VHV[], PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
ihessianproductfunc1
```

Example 3 (unknown):
```unknown
ihessianproductfunc1
```

Example 4 (unknown):
```unknown
ihessianproductfunc1
```

---

## TSSetIJacobianP#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSSetIJacobianP/

**Contents:**
- TSSetIJacobianP#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the function that computes the Jacobian of \(F\) w.r.t. the parameters \(p\) where \(F(Udot,U,p,t) = G(U,p,t)\), as well as the location to store the matrix.

ts - TS context obtained from TSCreate()

Amat - JacobianP matrix

ctx - [optional] function context

U - input vector (current ODE solution)

Udot - time derivative of state vector

shift - shift to apply, see the note in TSSetIJacobian()

ctx - [optional] function context

Amat has the same number of rows and the same row parallel layout as u, Amat has the same number of columns and parallel layout as p

TS: Scalable ODE and DAE Solvers, TSSetRHSJacobianP(), TS

src/ts/interface/sensitivity/tssen.c

src/ts/tutorials/ex23fwdadj.c src/ts/tutorials/ex20adj.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSSetIJacobianP(TS ts, Mat Amat, PetscErrorCode (*func)(TS ts, PetscReal t, Vec U, Vec Udot, PetscReal shift, Mat A, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSSetIJacobian()
```

Example 3 (unknown):
```unknown
TSSetRHSJacobianP()
```

---

## TSSetIJacobian#

**URL:** https://petsc.org/release/manualpages/TS/TSSetIJacobian/

**Contents:**
- TSSetIJacobian#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Set the function to compute the matrix dF/dU + a*dF/dU_t where F(t,U,U_t) is the function provided with TSSetIFunction().

ts - the TS context obtained from TSCreate()

Amat - (approximate) matrix to store Jacobian entries computed by f

Pmat - matrix used to compute preconditioner (usually the same as Amat)

f - the Jacobian evaluation routine

ctx - user-defined context for private data for the Jacobian evaluation routine (may be NULL)

The matrices Amat and Pmat are exactly the matrices that are used by SNES for the nonlinear solve.

If you know the operator Amat has a null space you can use MatSetNullSpace() and MatSetTransposeNullSpace() to supply the null space to Amat and the KSP solvers will automatically use that null space as needed during the solution process.

The matrix dF/dU + adF/dU_t you provide turns out to be the Jacobian of F(t,U,W+aU) where F(t,U,U_t) = 0 is the DAE to be solved. The time integrator internally approximates U_t by W+aU where the positive “shift” a and vector W depend on the integration method, step size, and past states. For example with the backward Euler method a = 1/dt and W = -aU(previous timestep) so W + aU = a(U - U(previous timestep)) = (U - U(previous timestep))/dt

You must set all the diagonal entries of the matrices, if they are zero you must still set them with a zero value

The TS solver may modify the nonzero structure and the entries of the matrices Amat and Pmat between the calls to f You should not assume the values are the same in the next call to f as you set them in the previous call.

In case TSSetRHSJacobian() is also used in conjunction with a fully-implicit solver, multilevel linear solvers, e.g. PCMG, will likely not work due to the way TS handles rhs matrices.

TS: Scalable ODE and DAE Solvers, TS, TSIJacobianFn, TSSetIFunction(), TSSetRHSJacobian(), SNESComputeJacobianDefaultColor(), SNESComputeJacobianDefault(), TSSetRHSFunction()

src/ts/interface/ts.c

src/ts/tutorials/ex14.c src/ts/tutorials/ex17.c src/ts/tutorials/ex20opt_ic.c src/ts/tutorials/ex49.c src/ts/tutorials/ex15.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/utils/dmplexlandau/tutorials/ex2.c src/ts/tutorials/ex41.c src/ts/tutorials/ex22f.F90 src/ts/utils/dmplexlandau/tutorials/ex1f90.F90

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetIFunction()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetIJacobian(TS ts, Mat Amat, Mat Pmat, TSIJacobianFn *f, PetscCtx ctx)
```

Example 3 (unknown):
```unknown
MatSetNullSpace()
```

Example 4 (unknown):
```unknown
MatSetTransposeNullSpace()
```

---

## TSSetInitialTimeStep#

**URL:** https://petsc.org/release/manualpages/TS/TSSetInitialTimeStep/

**Contents:**
- TSSetInitialTimeStep#
- Synopsis#
- Level#
- Location#

Deprecated, use TSSetTime() and TSSetTimeStep().

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetTime()
```

Example 2 (unknown):
```unknown
TSSetTimeStep()
```

Example 3 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetInitialTimeStep(TS ts, PetscReal initial_time, PetscReal time_step)
```

---

## TSSetMatStructure#

**URL:** https://petsc.org/release/manualpages/TS/TSSetMatStructure/

**Contents:**
- TSSetMatStructure#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

sets the relationship between the nonzero structure of the RHS Jacobian matrix to the IJacobian matrix.

ts - the time-stepper

str - the structure (the default is UNKNOWN_NONZERO_PATTERN)

When the relationship between the nonzero structures is known and supplied the solution process can be much faster

TS: Scalable ODE and DAE Solvers, TS, MatAXPY(), MatStructure

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetMatStructure(TS ts, MatStructure str)
```

Example 2 (unknown):
```unknown
UNKNOWN_NONZERO_PATTERN
```

Example 3 (unknown):
```unknown
MatStructure
```

---

## TSSetMaxSNESFailures#

**URL:** https://petsc.org/release/manualpages/TS/TSSetMaxSNESFailures/

**Contents:**
- TSSetMaxSNESFailures#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

Sets the maximum number of failed SNES solves allowed before TSSolve() is ended with a TSConvergedReason of TS_DIVERGED_NONLINEAR_SOLVE

fails - maximum number of failed nonlinear solves, pass PETSC_UNLIMITED to allow any number of failures.

-ts_max_snes_failures - Maximum number of nonlinear solve failures

TS: Scalable ODE and DAE Solvers, TS, SNES, TSGetSNESIterations(), TSGetKSPIterations(), TSSetMaxStepRejections(), TSGetStepRejections(), TSGetSNESFailures(), SNESGetConvergedReason(), TSGetConvergedReason(), TS_DIVERGED_NONLINEAR_SOLVE, TSConvergedReason

src/ts/interface/ts.c

src/ts/tutorials/ex30.c src/ts/tutorials/extchem.c src/ts/tutorials/ex8.c src/ts/tutorials/extchemfield.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSConvergedReason
```

Example 2 (unknown):
```unknown
TS_DIVERGED_NONLINEAR_SOLVE
```

Example 3 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetMaxSNESFailures(TS ts, PetscInt fails)
```

Example 4 (unknown):
```unknown
PETSC_UNLIMITED
```

---

## TSSetMaxStepRejections#

**URL:** https://petsc.org/release/manualpages/TS/TSSetMaxStepRejections/

**Contents:**
- TSSetMaxStepRejections#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the maximum number of step rejections allowed in a single time-step attempt before a time step fails in TSSolve() with TS_DIVERGED_STEP_REJECTED

rejects - maximum number of rejected steps, pass PETSC_UNLIMITED for unlimited

-ts_max_step_rejections - Maximum number of step rejections before a step fails

The options database name is incorrect.

TS: Scalable ODE and DAE Solvers, TS, SNES, TSGetSNESIterations(), TSGetKSPIterations(), TSSetMaxSNESFailures(), TSGetStepRejections(), TSGetSNESFailures(), TSSetErrorIfStepFails(), TSGetConvergedReason(), TSSolve(), TS_DIVERGED_STEP_REJECTED

src/ts/interface/ts.c

src/ts/tutorials/ex8.c src/ts/tutorials/ex42.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TS_DIVERGED_STEP_REJECTED
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetMaxStepRejections(TS ts, PetscInt rejects)
```

Example 3 (unknown):
```unknown
PETSC_UNLIMITED
```

Example 4 (unknown):
```unknown
TSGetSNESIterations()
```

---

## TSSetMaxSteps#

**URL:** https://petsc.org/release/manualpages/TS/TSSetMaxSteps/

**Contents:**
- TSSetMaxSteps#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the maximum number of steps to use.

ts - the TS context obtained from TSCreate()

maxsteps - maximum number of steps to use

-ts_max_steps maxsteps - Sets maxsteps

Use PETSC_DETERMINE to reset the maximum number of steps to the default from when the object’s type was set

The default maximum number of steps is 5,000

Use PETSC_DETERMINE_INTEGER

TS: Scalable ODE and DAE Solvers, TS, TSGetMaxSteps(), TSSetMaxTime(), TSSetExactFinalTime()

src/ts/interface/ts.c

src/ml/da/tutorials/ex3.c src/ts/tutorials/ex1.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/tao/unconstrained/tutorials/burgers_spectral.c src/ts/tutorials/ex18.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/tutorials/ex21.c src/ts/utils/dmplexlandau/tutorials/ex2.c src/ml/da/tutorials/ex4.c src/ml/da/tutorials/ex2.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetMaxSteps(TS ts, PetscInt maxsteps)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
PETSC_DETERMINE_INTEGER
```

Example 4 (unknown):
```unknown
TSGetMaxSteps()
```

---

## TSSetMaxTime#

**URL:** https://petsc.org/release/manualpages/TS/TSSetMaxTime/

**Contents:**
- TSSetMaxTime#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the maximum (or final) time for timestepping.

ts - the TS context obtained from TSCreate()

maxtime - final time to step to

-ts_max_time maxtime - Sets maxtime

Use PETSC_DETERMINE to reset the maximum time to the default from when the object’s type was set

The default maximum time is 5.0

Use PETSC_DETERMINE_REAL

TS: Scalable ODE and DAE Solvers, TS, TSGetMaxTime(), TSSetMaxSteps(), TSSetExactFinalTime()

src/ts/interface/ts.c

src/ml/da/tutorials/ex3.c src/ts/tutorials/ex1.c src/ts/tutorials/ex45.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ml/da/tutorials/ex1.c src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex4.c src/ts/tutorials/ex41.c src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetMaxTime(TS ts, PetscReal maxtime)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
PETSC_DETERMINE_REAL
```

Example 4 (unknown):
```unknown
TSGetMaxTime()
```

---

## TSSetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/TS/TSSetOptionsPrefix/

**Contents:**
- TSSetOptionsPrefix#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the prefix used for searching for all TS options in the database.

prefix - The prefix to prepend to all option names

A hyphen (-) must NOT be given at the beginning of the prefix name. The first character of all runtime options is AUTOMATICALLY the hyphen.

TS: Scalable ODE and DAE Solvers, TS, TSSetFromOptions(), TSAppendOptionsPrefix()

src/ts/interface/ts.c

src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/utils/dmplexlandau/tutorials/ex1f90.F90

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetOptionsPrefix(TS ts, const char prefix[])
```

Example 2 (unknown):
```unknown
TSSetFromOptions()
```

Example 3 (unknown):
```unknown
TSAppendOptionsPrefix()
```

---

## TSSetPostEvaluate#

**URL:** https://petsc.org/release/manualpages/TS/TSSetPostEvaluate/

**Contents:**
- TSSetPostEvaluate#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Note#
- See Also#
- Level#
- Location#

Sets the general-purpose function called at the end of each step evaluation.

ts - The TS context obtained from TSCreate()

The function set by TSSetPostEvaluate() is called after the solution is evaluated, or after the step rollback. Inside the func callback, the solution vector can be obtained with TSGetSolution(), and modified, if need be. The time step can be obtained with TSGetTimeStep(), and the time at the start of the step - via TSGetTime(). The potential changes to the solution vector introduced by event handling (postevent()) are not relevant for TSSetPostEvaluate(), but are relevant for TSSetPostStep(), according to the function call scheme in TSSolve(), as shown below

where EventHandling() may result in one of the following three outcomes

TS: Scalable ODE and DAE Solvers, TS, TSSetPreStage(), TSSetPreStep(), TSSetPostStep(), TSGetApplicationContext()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetPostEvaluate(TS ts, PetscErrorCode (*func)(TS ts))
```

Example 2 (unknown):
```unknown
TSSetPostEvaluate()
```

Example 3 (unknown):
```unknown
TSGetSolution()
```

Example 4 (unknown):
```unknown
TSGetTimeStep()
```

---

## TSSetPostEventSecondStep#

**URL:** https://petsc.org/release/manualpages/TS/TSSetPostEventSecondStep/

**Contents:**
- TSSetPostEventSecondStep#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Set the second time step to use after the event

ts - time integration context

dt2 - second post event step

-ts_event_post_event_second_step dt2 - second time step after the event

TSSetPostEventSecondStep() allows one to set the second time step after the event.

The post-event time steps should be selected based on the post-event dynamics. If the dynamics are stiff, or a significant jump in the equations or the state vector has taken place at the event, conservative (small) steps should be employed. If not, then larger time steps may be appropriate.

This function accepts either a numerical value for dt2, or PETSC_DECIDE (default).

To describe the way PETSC_DECIDE affects the post-event steps, consider a trajectory of time points t1 -> t2 -> t3 -> t4. Suppose the TS has reached and calculated the solution at point t3, and has planned the next move: t3 -> t4. At this moment, an event between t2 and t3 is detected, and after a few iterations it is resolved at point te, t2 < te < t3. After event te, two post-event steps can be specified: the first one dt1 (TSSetPostEventStep()), and the second one dt2 (TSSetPostEventSecondStep()). Both post-event steps can be either PETSC_DECIDE, or a number. Four different combinations are possible:

dt1 = PETSC_DECIDE, dt2 = PETSC_DECIDE. Then, after te TS goes to t3, and then to t4. This is the all-default behaviour.

dt1 = PETSC_DECIDE, dt2 = x2 (numerical). Then, after te TS goes to t3, and then to t3+x2.

dt1 = x1 (numerical), dt2 = x2 (numerical). Then, after te TS goes to te+x1, and then to te+x1+x2.

dt1 = x1 (numerical), dt2 = PETSC_DECIDE. Then, after te TS goes to te+x1, and event handler does not interfere to the subsequent steps.

In the special case when te == t3 with a good precision, the post-event step te -> t3 is not performed, so behaviour of (1) and (2) becomes:

1a. After te TS goes to t4, and event handler does not interfere to the subsequent steps.

2a. After te TS goes to t4, and then to t4+x2.

Warning! When the second post-event step (either PETSC_DECIDE or a numerical value) is managed by the event handler, i.e. in cases 1, 2, 3 and 2a, TSAdapt will never analyse (and never do a reasonable rejection of) the first post-event step. The first post-event step will always be accepted. In this situation, it is the user’s responsibility to make sure the step size is appropriate! In cases 4 and 1a, however, TSAdapt will analyse the first post-event step, and is allowed to reject it.

This function can be called not only in the initial setup, but also inside the postevent() callback set with TSSetEventHandler(), affecting the post-event steps for the current event, and the subsequent ones.

The default value is PETSC_DECIDE.

TS: Scalable ODE and DAE Solvers, Handling of discontinuities, TS, TSEvent, TSSetEventHandler(), TSSetPostEventStep()

src/ts/event/tsevent.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSSetPostEventSecondStep(TS ts, PetscReal dt2)
```

Example 2 (unknown):
```unknown
TSSetPostEventSecondStep()
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

## TSSetPostEventStep#

**URL:** https://petsc.org/release/manualpages/TS/TSSetPostEventStep/

**Contents:**
- TSSetPostEventStep#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#

Set the first time step to use after the event

ts - time integration context

dt1 - first post event step

-ts_event_post_event_step dt1 - first time step after the event

TSSetPostEventStep() allows one to set a time step to use immediately following an event. Note, if TSAdapt is allowed to interfere and reject steps, a large ‘dt1’ set by TSSetPostEventStep() may get truncated, resulting in a smaller actual post-event step. See also the warning below regarding the TSAdapt.

The post-event time steps should be selected based on the post-event dynamics. If the dynamics are stiff, or a significant jump in the equations or the state vector has taken place at the event, conservative (small) steps should be employed. If not, then larger time steps may be appropriate.

This function accepts either a numerical value for dt1, or PETSC_DECIDE. The special value PETSC_DECIDE signals the event handler to follow the originally planned trajectory, and is assumed by default.

To describe the way PETSC_DECIDE affects the post-event steps, consider a trajectory of time points t1 -> t2 -> t3 -> t4. Suppose the TS has reached and calculated the solution at point t3, and has planned the next move: t3 -> t4. At this moment, an event between t2 and t3 is detected, and after a few iterations it is resolved at point te, t2 < te < t3. After event te, two post-event steps can be specified: the first one dt1 (TSSetPostEventStep()), and the second one dt2 (TSSetPostEventSecondStep()). Both post-event steps can be either PETSC_DECIDE, or a number. Four different combinations are possible:

dt1 = PETSC_DECIDE, dt2 = PETSC_DECIDE. Then, after te TS goes to t3, and then to t4. This is the all-default behaviour.

dt1 = PETSC_DECIDE, dt2 = x2 (numerical). Then, after te TS goes to t3, and then to t3+x2.

dt1 = x1 (numerical), dt2 = x2 (numerical). Then, after te TS goes to te+x1, and then to te+x1+x2.

dt1 = x1 (numerical), dt2 = PETSC_DECIDE. Then, after te TS goes to te+x1, and event handler does not interfere to the subsequent steps.

In the special case when te == t3 with a good precision, the post-event step te -> t3 is not performed, so behaviour of (1) and (2) becomes:

1a. After te TS goes to t4, and event handler does not interfere to the subsequent steps.

2a. After te TS goes to t4, and then to t4+x2.

Warning! When the second post-event step (either PETSC_DECIDE or a numerical value) is managed by the event handler, i.e. in cases 1, 2, 3 and 2a, TSAdapt will never analyse (and never do a reasonable rejection of) the first post-event step. The first post-event step will always be accepted. In this situation, it is the user’s responsibility to make sure the step size is appropriate! In cases 4 and 1a, however, TSAdapt will analyse the first post-event step, and is allowed to reject it.

This function can be called not only in the initial setup, but also inside the postevent() callback set with TSSetEventHandler(), affecting the post-event steps for the current event, and the subsequent ones. Thus, the strategy of the post-event time step definition can be adjusted on the fly. In case several events are triggered in the given time point, only a single postevent handler is invoked, and the user is to determine what post-event time step is more appropriate in this situation.

The default value is PETSC_DECIDE.

Event processing starts after visiting point t3, which means ts->adapt->dt_span_cached has been set to whatever value is required when planning the step t3 -> t4.

TS: Scalable ODE and DAE Solvers, Handling of discontinuities, TS, TSEvent, TSSetEventHandler(), TSSetPostEventSecondStep()

src/ts/event/tsevent.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSSetPostEventStep(TS ts, PetscReal dt1)
```

Example 2 (unknown):
```unknown
TSSetPostEventStep()
```

Example 3 (unknown):
```unknown
TSSetPostEventStep()
```

Example 4 (unknown):
```unknown
PETSC_DECIDE
```

---

## TSSetPostStage#

**URL:** https://petsc.org/release/manualpages/TS/TSSetPostStage/

**Contents:**
- TSSetPostStage#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the general-purpose function called once at the end of each stage.

ts - The TS context obtained from TSCreate()

stagetime - the stage time

stageindex - the stage index

Y - Array of vectors (of size = total number of stages) with the stage solutions

There may be several stages per time step. If the solve for a given stage fails, the step may be rejected and retried. The time step number being computed can be queried using TSGetStepNumber() and the total size of the step being attempted can be obtained using TSGetTimeStep(). The time at the start of the step is available via TSGetTime().

TS: Scalable ODE and DAE Solvers, TS, TSSetPreStage(), TSSetPreStep(), TSSetPostStep(), TSGetApplicationContext()

src/ts/interface/ts.c

src/ts/tutorials/ex30.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetPostStage(TS ts, PetscErrorCode (*func)(TS ts, PetscReal stagetime, PetscInt stageindex, Vec *Y))
```

Example 2 (unknown):
```unknown
TSGetStepNumber()
```

Example 3 (unknown):
```unknown
TSGetTimeStep()
```

Example 4 (unknown):
```unknown
TSGetTime()
```

---

## TSSetPostStep#

**URL:** https://petsc.org/release/manualpages/TS/TSSetPostStep/

**Contents:**
- TSSetPostStep#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the general-purpose function called once at the end of each successful time step.

ts - The TS context obtained from TSCreate()

The function set by TSSetPostStep() is called after each successful step. If the event handler locates an event at the given step, and postevent() modifies the solution vector, the solution vector obtained by TSGetSolution() inside func will contain the changes. To get the solution without these changes, use TSSetPostEvaluate() to set the appropriate callback. The scheme of the relevant function calls in TSSolve() is shown below

where EventHandling() may result in one of the following three outcomes

TS: Scalable ODE and DAE Solvers, TS, TSSetPreStep(), TSSetPreStage(), TSSetPostEvaluate(), TSGetTimeStep(), TSGetStepNumber(), TSGetTime(), TSRestartStep()

src/ts/interface/ts.c

src/ts/tutorials/ex77.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetPostStep(TS ts, PetscErrorCode (*func)(TS ts))
```

Example 2 (unknown):
```unknown
TSSetPostStep()
```

Example 3 (unknown):
```unknown
postevent()
```

Example 4 (unknown):
```unknown
TSGetSolution()
```

---

## TSSetPreStage#

**URL:** https://petsc.org/release/manualpages/TS/TSSetPreStage/

**Contents:**
- TSSetPreStage#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the general-purpose function called once at the beginning of each stage.

ts - The TS context obtained from TSCreate()

stagetime - the stage time

There may be several stages per time step. If the solve for a given stage fails, the step may be rejected and retried. The time step number being computed can be queried using TSGetStepNumber() and the total size of the step being attempted can be obtained using TSGetTimeStep(). The time at the start of the step is available via TSGetTime().

TS: Scalable ODE and DAE Solvers, TS, TSSetPostStage(), TSSetPreStep(), TSSetPostStep(), TSGetApplicationContext()

src/ts/interface/ts.c

src/ts/tutorials/ex30.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetPreStage(TS ts, PetscErrorCode (*func)(TS ts, PetscReal stagetime))
```

Example 2 (unknown):
```unknown
TSGetStepNumber()
```

Example 3 (unknown):
```unknown
TSGetTimeStep()
```

Example 4 (unknown):
```unknown
TSGetTime()
```

---

## TSSetPreStep#

**URL:** https://petsc.org/release/manualpages/TS/TSSetPreStep/

**Contents:**
- TSSetPreStep#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

Sets the general-purpose function called once at the beginning of each time step.

ts - The TS context obtained from TSCreate()

TS: Scalable ODE and DAE Solvers, TS, TSSetPreStage(), TSSetPostStage(), TSSetPostStep(), TSStep(), TSRestartStep()

src/ts/interface/ts.c

src/ts/tutorials/ex77.c src/ts/tutorials/ex76.c src/ts/utils/dmplexlandau/tutorials/ex2.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetPreStep(TS ts, PetscErrorCode (*func)(TS ts))
```

Example 2 (unknown):
```unknown
TSSetPreStage()
```

Example 3 (unknown):
```unknown
TSSetPostStage()
```

Example 4 (unknown):
```unknown
TSSetPostStep()
```

---

## TSSetProblemType#

**URL:** https://petsc.org/release/manualpages/TS/TSSetProblemType/

**Contents:**
- TSSetProblemType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the type of problem to be solved.

type - One of TS_LINEAR, TS_NONLINEAR where these types refer to problems of the forms

TS: Scalable ODE and DAE Solvers, TSSetUp(), TSProblemType, TS

src/ts/interface/ts.c

src/ml/da/tutorials/ex3.c src/ts/tutorials/ex1.c src/ts/tutorials/ex14.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/tutorials/ex21.c src/ml/da/tutorials/ex1.c src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex4.c src/ts/tutorials/ex41.c src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetProblemType(TS ts, TSProblemType type)
```

Example 2 (unknown):
```unknown
TS_NONLINEAR
```

Example 3 (unknown):
```unknown
U_t - A U = 0      (linear)
         U_t - A(t) U = 0   (linear)
         F(t,U,U_t) = 0     (nonlinear)
```

Example 4 (unknown):
```unknown
TSProblemType
```

---

## TSSetResize#

**URL:** https://petsc.org/release/manualpages/TS/TSSetResize/

**Contents:**
- TSSetResize#
- Synopsis#
- Input Parameters#
- Calling sequence of setup#
- Calling sequence of transfer#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the resize callbacks.

ts - The TS context obtained from TSCreate()

rollback - Whether a resize will restart the step

setup - The setup function

transfer - The transfer function

ctx - [optional] The user-defined context

step - the current step

time - the current time

state - the current vector of state

resize - (output parameter) PETSC_TRUE if need resizing, PETSC_FALSE otherwise

ctx - user defined context

nv - the number of vectors to be transferred

vecsin - array of vectors to be transferred

vecsout - array of transferred vectors

ctx - user defined context

The setup function is called inside TSSolve() after TSEventHandler() or after TSPostStep() depending on the rollback value: if rollback is true, then these callbacks behave as error indicators and will flag the need to remesh and restart the current step. Otherwise, they will simply flag the solver that the size of the discrete problem has changed. In both cases, the solver will collect the needed vectors that will be transferred from the old to the new sizes using the transfer callback. These vectors will include the current solution vector, and other vectors needed by the specific solver used. For example, TSBDF uses previous solutions vectors to solve for the next time step. Other application specific objects associated with the solver, i.e. Jacobian matrices and DM, will be automatically reset if the sizes are changed and they must be specified again by the user inside the transfer function. The input and output arrays passed to transfer are allocated by PETSc. Vectors in vecsout must be created by the user. Ownership of vectors in vecsout is transferred to PETSc.

TS: Scalable ODE and DAE Solvers, TS, TSSetDM(), TSSetIJacobian(), TSSetRHSJacobian()

src/ts/interface/ts.c

src/ts/tutorials/ex30.c src/ts/tutorials/ex45.c src/ts/tutorials/ex11.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetResize(TS ts, PetscBool rollback, PetscErrorCode (*setup)(TS ts, PetscInt step, PetscReal time, Vec state, PetscBool *resize, PetscCtx ctx), PetscErrorCode (*transfer)(TS ts, PetscInt nv, Vec vecsin[], Vec vecsout[], PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
TSEventHandler()
```

Example 4 (unknown):
```unknown
TSPostStep()
```

---

## TSSetRHSFunction#

**URL:** https://petsc.org/release/manualpages/TS/TSSetRHSFunction/

**Contents:**
- TSSetRHSFunction#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the routine for evaluating the function, where U_t = G(t,u).

ts - the TS context obtained from TSCreate()

r - vector to put the computed right-hand side (or NULL to have it created)

f - routine for evaluating the right-hand-side function

ctx - [optional] user-defined context for private data for the function evaluation routine (may be NULL)

You must call this function or TSSetIFunction() to define your ODE. You cannot use this function when solving a DAE.

TS: Scalable ODE and DAE Solvers, TS, TSRHSFunctionFn, TSSetRHSJacobian(), TSSetIJacobian(), TSSetIFunction()

src/ts/interface/ts.c

src/ml/da/tutorials/ex3.c src/ts/tutorials/ex1.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ml/da/tutorials/ex1.c src/ml/da/tutorials/ex2.c src/ts/utils/dmplexlandau/tutorials/ex2.c src/ml/da/tutorials/ex4.c src/ts/tutorials/ex41.c src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetRHSFunction(TS ts, Vec r, TSRHSFunctionFn *f, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSSetIFunction()
```

Example 3 (unknown):
```unknown
TSRHSFunctionFn
```

Example 4 (unknown):
```unknown
TSSetRHSJacobian()
```

---

## TSSetRHSHessianProduct#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSSetRHSHessianProduct/

**Contents:**
- TSSetRHSHessianProduct#
- Synopsis#
- Input Parameters#
- Calling sequence of rhshessianproductfunc1#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the function that computes the vector-Hessian-vector product. The Hessian is the second-order derivative of G (RHSFunction) w.r.t. the state variable.

ts - TS context obtained from TSCreate()

rhshp1 - an array of vectors storing the result of vector-Hessian-vector product for \(G_{UU}\)

rhshessianproductfunc1 - vector-Hessian-vector product function for \(G_{UU}\)

rhshp2 - an array of vectors storing the result of vector-Hessian-vector product for \(G_{UP}\)

rhshessianproductfunc2 - vector-Hessian-vector product function for \(G_{UP}\)

rhshp3 - an array of vectors storing the result of vector-Hessian-vector product for \(G_{PU}\)

rhshessianproductfunc3 - vector-Hessian-vector product function for \(G_{PU}\)

rhshp4 - an array of vectors storing the result of vector-Hessian-vector product for \(G_{PP}\)

rhshessianproductfunc4 - vector-Hessian-vector product function for \(G_{PP}\)

ctx - [optional] function context

U - input vector (current ODE solution)

Vl - an array of input vectors to be left-multiplied with the Hessian

Vr - input vector to be right-multiplied with the Hessian

VHV - an array of output vectors for vector-Hessian-vector product

ctx - [optional] function context

All other functions have the same calling sequence as rhshessianproductfunc1, so their descriptions are omitted for brevity.

The first Hessian function and the working array are required.

As an example to implement the callback functions, the second callback function calculates the vector-Hessian-vector product \( Vl_n^T*G_UP*Vr\) where the vector \(Vl_n\) (n-th element in the array \(Vl\)) and \(Vr\) are of size \(N\) and \(M\) respectively, and the Hessian \(G_{UP}\) is of size \(N x N x M\). Each entry of \(G_{UP}\) corresponds to the derivative \( G_UP[i][j][k] = \frac{\partial^2 G[i]}{\partial U[j] \partial P[k]}.\) The result of the vector-Hessian-vector product for \(Vl_n\) needs to be stored in vector \(VHV_n\) with j-th entry being \( VHV_n[j] = \sum_i \sum_k {Vl_n[i] * G_UP[i][j][k] * Vr[k]}\) If the cost function is a scalar, there will be only one vector in \(Vl\) and \(VHV\).

src/ts/interface/sensitivity/tssen.c

src/ts/tutorials/ex20opt_p.c src/ts/tutorials/ex20opt_ic.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSSetRHSHessianProduct(TS ts, Vec rhshp1[], PetscErrorCode (*rhshessianproductfunc1)(TS ts, PetscReal t, Vec U, Vec Vl[], Vec Vr, Vec VHV[], PetscCtx ctx), Vec rhshp2[], PetscErrorCode (*rhshessianproductfunc2)(TS ts, PetscReal t, Vec U, Vec Vl[], Vec Vr, Vec VHV[], PetscCtx ctx), Vec rhshp3[], PetscErrorCode (*rhshessianproductfunc3)(TS ts, PetscReal t, Vec U, Vec Vl[], Vec Vr, Vec VHV[], PetscCtx ctx), Vec rhshp4[], PetscErrorCode (*rhshessianproductfunc4)(TS ts, PetscReal t, Vec U, Vec Vl[], Vec Vr, Vec VHV[], PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
rhshessianproductfunc1
```

Example 3 (unknown):
```unknown
rhshessianproductfunc1
```

Example 4 (unknown):
```unknown
rhshessianproductfunc1
```

---

## TSSetRHSJacobianP#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSSetRHSJacobianP/

**Contents:**
- TSSetRHSJacobianP#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the function that computes the Jacobian of \(G\) w.r.t. the parameters \(p\) where \(U_t = G(U,p,t)\), as well as the location to store the matrix.

ts - TS context obtained from TSCreate()

Amat - JacobianP matrix

ctx - [optional] function context

Amat has the same number of rows and the same row parallel layout as u, Amat has the same number of columns and parallel layout as p

TS: Scalable ODE and DAE Solvers, TS, TSRHSJacobianPFn, TSGetRHSJacobianP()

src/ts/interface/sensitivity/tssen.c

src/ts/tutorials/ex20opt_p.c src/ts/tutorials/ex20adj.c src/ts/tutorials/ex20fwd.c src/ts/tutorials/ex16fwd.c src/ts/tutorials/ex20td.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSSetRHSJacobianP(TS ts, Mat Amat, TSRHSJacobianPFn *func, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSRHSJacobianPFn
```

Example 3 (unknown):
```unknown
TSGetRHSJacobianP()
```

---

## TSSetRHSJacobian#

**URL:** https://petsc.org/release/manualpages/TS/TSSetRHSJacobian/

**Contents:**
- TSSetRHSJacobian#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the function to compute the Jacobian of G, where U_t = G(U,t), as well as the location to store the matrix.

ts - the TS context obtained from TSCreate()

Amat - (approximate) location to store Jacobian matrix entries computed by f

Pmat - matrix from which preconditioner is to be constructed (usually the same as Amat)

f - the Jacobian evaluation routine

ctx - [optional] user-defined context for private data for the Jacobian evaluation routine (may be NULL)

You must set all the diagonal entries of the matrices, if they are zero you must still set them with a zero value

The TS solver may modify the nonzero structure and the entries of the matrices Amat and Pmat between the calls to f() You should not assume the values are the same in the next call to f() as you set them in the previous call.

TS: Scalable ODE and DAE Solvers, TS, TSRHSJacobianFn, SNESComputeJacobianDefaultColor(), TSSetRHSFunction(), TSRHSJacobianSetReuse(), TSSetIJacobian(), TSRHSFunctionFn, TSIFunctionFn

src/ts/interface/ts.c

src/ts/tutorials/ex1.c src/ts/tutorials/ex74.c src/ts/tutorials/extchem.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/tutorials/ex20opt_ic.c src/ts/tutorials/ex4.c src/ts/tutorials/ex21.c src/ts/tutorials/ex16fwd.c src/ts/tutorials/ex41.c src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetRHSJacobian(TS ts, Mat Amat, Mat Pmat, TSRHSJacobianFn *f, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSRHSJacobianFn
```

Example 3 (unknown):
```unknown
SNESComputeJacobianDefaultColor()
```

Example 4 (unknown):
```unknown
TSSetRHSFunction()
```

---

## TSSetRunSteps#

**URL:** https://petsc.org/release/manualpages/TS/TSSetRunSteps/

**Contents:**
- TSSetRunSteps#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Sets the maximum number of steps to take in each call to TSSolve().

If the step count when TSSolve() is start_step, this will stop the simulation once current_step - start_step >= run_steps. Comparatively, TSSetMaxSteps() will stop if current_step >= max_steps. The simulation will stop when either condition is reached.

ts - the TS context obtained from TSCreate()

runsteps - maximum number of steps to take in each call to TSSolve();

-ts_run_steps runsteps - Sets runsteps

The default is PETSC_UNLIMITED

TS: Scalable ODE and DAE Solvers, TS, TSGetRunSteps(), TSSetMaxTime(), TSSetExactFinalTime(), TSSetMaxSteps()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetRunSteps(TS ts, PetscInt runsteps)
```

Example 2 (unknown):
```unknown
current_step - start_step >= run_steps
```

Example 3 (unknown):
```unknown
TSSetMaxSteps()
```

Example 4 (unknown):
```unknown
current_step >= max_steps
```

---

## TSSetSaveTrajectory#

**URL:** https://petsc.org/release/manualpages/TS/TSSetSaveTrajectory/

**Contents:**
- TSSetSaveTrajectory#
- Synopsis#
- Input Parameter#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Causes the TS to save its solutions as it iterates forward in time in a TSTrajectory object

ts - the TS context obtained from TSCreate()

-ts_save_trajectory - saves the trajectory to a file

-ts_trajectory_type (basic|singlefile|memory|visualization) - set trajectory type

This routine should be called after all TS options have been set

The TSTRAJECTORYVISUALIZATION files can be loaded into Python with \(PETSC_DIR/lib/petsc/bin/PetscBinaryIOTrajectory.py and MATLAB with \)PETSC_DIR/share/petsc/matlab/PetscReadBinaryTrajectory.m

TS: Scalable ODE and DAE Solvers, TS, TSTrajectoryType, TSTrajectory, TSGetTrajectory(), TSAdjointSolve()

src/ts/interface/ts.c

src/ts/tutorials/ex20opt_p.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/tutorials/ex51.c src/ts/tutorials/ex50.c src/ts/tutorials/ex20opt_ic.c src/ts/tutorials/ex40.c src/ts/tutorials/ex20adj.c src/ts/tutorials/ex44.c src/ts/tutorials/ex41.c src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSTrajectory
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetSaveTrajectory(TS ts)
```

Example 3 (unknown):
```unknown
TSTRAJECTORYVISUALIZATION
```

Example 4 (unknown):
```unknown
TSTrajectoryType
```

---

## TSSetSNES#

**URL:** https://petsc.org/release/manualpages/TS/TSSetSNES/

**Contents:**
- TSSetSNES#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Set the SNES (nonlinear solver) to be used by the TS timestepping context

ts - the TS context obtained from TSCreate()

snes - the nonlinear solver context

Most users should have the TS created by calling TSGetSNES()

TS: Scalable ODE and DAE Solvers, TS, SNES, TSCreate(), TSSetUp(), TSSolve(), TSGetSNES()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetSNES(TS ts, SNES snes)
```

Example 2 (unknown):
```unknown
TSGetSNES()
```

Example 3 (unknown):
```unknown
TSGetSNES()
```

---

## TSSetSolutionFunction#

**URL:** https://petsc.org/release/manualpages/TS/TSSetSolutionFunction/

**Contents:**
- TSSetSolutionFunction#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Provide a function that computes the solution of the ODE or DAE

ts - the TS context obtained from TSCreate()

f - routine for evaluating the solution

ctx - [optional] user-defined context for private data for the function evaluation routine (may be NULL)

-ts_monitor_lg_error - create a graphical monitor of error history, requires user to have provided TSSetSolutionFunction()

-ts_monitor_draw_error - Monitor error graphically, requires user to have provided TSSetSolutionFunction()

This routine is used for testing accuracy of time integration schemes when you already know the solution. If analytic solutions are not known for your system, consider using the Method of Manufactured Solutions to create closed-form solutions with non-physical forcing terms.

For low-dimensional problems solved in serial, such as small discrete systems, TSMonitorLGError() can be used to monitor the error history.

TS: Scalable ODE and DAE Solvers, TS, TSSolutionFn, TSSetRHSJacobian(), TSSetIJacobian(), TSComputeSolutionFunction(), TSSetForcingFunction(), TSSetSolution(), TSGetSolution(), TSMonitorLGError(), TSMonitorDrawError()

src/ts/interface/ts.c

src/ts/tutorials/ex50.c src/ts/tutorials/ex43.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetSolutionFunction(TS ts, TSSolutionFn *f, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSSetSolutionFunction()
```

Example 3 (unknown):
```unknown
TSSetSolutionFunction()
```

Example 4 (unknown):
```unknown
TSMonitorLGError()
```

---

## TSSetSolution#

**URL:** https://petsc.org/release/manualpages/TS/TSSetSolution/

**Contents:**
- TSSetSolution#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the initial solution vector for use by the TS routines.

ts - the TS context obtained from TSCreate()

u - the solution vector

TS: Scalable ODE and DAE Solvers, TS, TSSetSolutionFunction(), TSGetSolution(), TSCreate()

src/ts/interface/ts.c

src/ts/tutorials/ex1.c src/ts/tutorials/ex45.c src/ts/tutorials/ex14.c src/ts/tutorials/ex17.c src/ts/tutorials/ex51.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/utils/dmplexlandau/tutorials/ex2.c src/ts/tutorials/ex41.c src/ts/tutorials/ex22f.F90 src/ts/utils/dmplexlandau/tutorials/ex1f90.F90

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetSolution(TS ts, Vec u)
```

Example 2 (unknown):
```unknown
TSSetSolutionFunction()
```

Example 3 (unknown):
```unknown
TSGetSolution()
```

---

## TSSetStepNumber#

**URL:** https://petsc.org/release/manualpages/TS/TSSetStepNumber/

**Contents:**
- TSSetStepNumber#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the number of steps completed.

steps - number of steps completed so far

For most uses of the TS solvers the user need not explicitly call TSSetStepNumber(), as the step counter is appropriately updated in TSSolve()/TSStep()/TSRollBack(). Power users may call this routine to reinitialize timestepping by setting the step counter to zero (and time to the initial time) to solve a similar problem with different initial conditions or parameters. Other possible use case is to continue timestepping from a previously interrupted run in such a way that TS monitors will be called with a initial nonzero step counter.

TS: Scalable ODE and DAE Solvers, TS, TSGetStepNumber(), TSSetTime(), TSSetTimeStep(), TSSetSolution()

src/ts/interface/ts.c

src/ml/da/tutorials/ex3.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/tao/unconstrained/tutorials/burgers_spectral.c src/ts/tutorials/ex20opt_ic.c src/ts/tutorials/ex40.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/utils/dmplexlandau/tutorials/ex2.c src/ml/da/tutorials/ex4.c src/ts/tutorials/ex41.c src/ml/da/tutorials/ex2.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetStepNumber(TS ts, PetscInt steps)
```

Example 2 (unknown):
```unknown
TSSetStepNumber()
```

Example 3 (unknown):
```unknown
TSRollBack()
```

Example 4 (unknown):
```unknown
TSGetStepNumber()
```

---

## TSSetTimeError#

**URL:** https://petsc.org/release/manualpages/TS/TSSetTimeError/

**Contents:**
- TSSetTimeError#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Sets the estimated error vector, if the chosen TSType has an error estimation functionality. This can be used to restart such a time integrator with a given error vector.

Not Collective, but v returned is parallel if ts is parallel

ts - the TS context obtained from TSCreate() (input parameter).

v - the vector containing the error (same size as the solution).

TS: Scalable ODE and DAE Solvers, TS, TSSetSolution(), TSGetTimeError()

src/ts/interface/ts.c

TSSetTimeError_GLEE() in src/ts/impls/glee/glee.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetTimeError(TS ts, Vec v)
```

Example 2 (unknown):
```unknown
TSSetSolution()
```

Example 3 (unknown):
```unknown
TSGetTimeError()
```

---

## TSSetTimeSpan#

**URL:** https://petsc.org/release/manualpages/TS/TSSetTimeSpan/

**Contents:**
- TSSetTimeSpan#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

sets the time span. The solution will be computed and stored for each time requested in the span

ts - the time-stepper

n - number of the time points (>=2)

span_times - array of the time points, must be increasing. The first element and the last element are the initial time and the final time respectively.

-ts_time_span t0,…,tf - Sets the time span

This function is identical to TSSetEvaluationTimes(), except that it also sets the initial time and final time for the ts to the first and last span_times entries.

The elements in span_times must be all increasing. They correspond to the intermediate points to be saved.

TS_EXACTFINALTIME_MATCHSTEP must be used to make the last time step in each sub-interval match the intermediate points specified.

The intermediate solutions are saved in a vector array that can be accessed with TSGetEvaluationSolutions(). Thus using time span may pressure the memory system when using a large number of span points.

TS: Scalable ODE and DAE Solvers, TS, TSSetEvaluationTimes(), TSGetEvaluationTimes(), TSGetEvaluationSolutions()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetTimeSpan(TS ts, PetscInt n, PetscReal span_times[])
```

Example 2 (unknown):
```unknown
TSSetEvaluationTimes()
```

Example 3 (unknown):
```unknown
TS_EXACTFINALTIME_MATCHSTEP
```

Example 4 (unknown):
```unknown
TSGetEvaluationSolutions()
```

---

## TSSetTimeStep#

**URL:** https://petsc.org/release/manualpages/TS/TSSetTimeStep/

**Contents:**
- TSSetTimeStep#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Allows one to reset the timestep at any time.

ts - the TS context obtained from TSCreate()

time_step - the size of the timestep

-ts_time_step dt - provide the initial time step

This is only a suggestion, the actual initial time step used may differ

If this is called after TSSetUp(), it will not change the initial time step value printed by TSView()

TS: Scalable ODE and DAE Solvers, TS, TSPSEUDO, TSGetTimeStep(), TSSetTime()

src/ts/interface/ts.c

src/ml/da/tutorials/ex3.c src/ts/tutorials/ex1.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ml/da/tutorials/ex1.c src/ml/da/tutorials/ex2.c src/ts/utils/dmplexlandau/tutorials/ex2.c src/ml/da/tutorials/ex4.c src/ts/tutorials/ex41.c src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetTimeStep(TS ts, PetscReal time_step)
```

Example 2 (unknown):
```unknown
TSGetTimeStep()
```

Example 3 (unknown):
```unknown
TSSetTime()
```

---

## TSSetTime#

**URL:** https://petsc.org/release/manualpages/TS/TSSetTime/

**Contents:**
- TSSetTime#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Allows one to reset the time.

ts - the TS context obtained from TSCreate()

TS: Scalable ODE and DAE Solvers, TS, TSGetTime(), TSSetMaxSteps()

src/ts/interface/ts.c

src/ml/da/tutorials/ex3.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/tutorials/ex20opt_ic.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ml/da/tutorials/ex1.c src/ml/da/tutorials/ex2.c src/ts/utils/dmplexlandau/tutorials/ex2.c src/ml/da/tutorials/ex4.c src/ts/tutorials/ex41.c src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetTime(TS ts, PetscReal t)
```

Example 2 (unknown):
```unknown
TSGetTime()
```

Example 3 (unknown):
```unknown
TSSetMaxSteps()
```

---

## TSSetTolerances#

**URL:** https://petsc.org/release/manualpages/TS/TSSetTolerances/

**Contents:**
- TSSetTolerances#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Notes#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Set tolerances for local truncation error when using an adaptive controller

ts - time integration context

atol - scalar absolute tolerances

vatol - vector of absolute tolerances or NULL, used in preference to atol if present

rtol - scalar relative tolerances

vrtol - vector of relative tolerances or NULL, used in preference to rtol if present

-ts_rtol rtol - relative tolerance for local truncation error

-ts_atol atol - Absolute tolerance for local truncation error

PETSC_CURRENT or PETSC_DETERMINE may be used for atol or rtol to indicate the current value or the default value from when the object’s type was set.

With PETSc’s implicit schemes for DAE problems, the calculation of the local truncation error (LTE) includes both the differential and the algebraic variables. If one wants the LTE to be computed only for the differential or the algebraic part then this can be done using the vector of tolerances vatol. For example, by setting the tolerance vector with the desired tolerance for the differential part and infinity for the algebraic part, the LTE calculation will include only the differential variables.

Use PETSC_CURRENT_INTEGER or PETSC_DETERMINE_INTEGER.

TS: Scalable ODE and DAE Solvers, TS, TSAdapt, TSErrorWeightedNorm(), TSGetTolerances()

src/ts/interface/ts.c

src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/tutorials/ex30.c src/ts/tutorials/ex50.c src/ts/tutorials/ex49.c src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetTolerances(TS ts, PetscReal atol, Vec vatol, PetscReal rtol, Vec vrtol)
```

Example 2 (unknown):
```unknown
PETSC_CURRENT
```

Example 3 (unknown):
```unknown
PETSC_DETERMINE
```

Example 4 (unknown):
```unknown
PETSC_CURRENT_INTEGER
```

---

## TSSetTransientVariable#

**URL:** https://petsc.org/release/manualpages/TS/TSSetTransientVariable/

**Contents:**
- TSSetTransientVariable#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

sets function to transform from state to transient variables

ts - time stepping context on which to change the transient variable

tvar - a function that transforms to transient variables, see TSTransientVariableFn for the calling sequence

ctx - a context for tvar

This is typically used to transform from primitive to conservative variables so that a time integrator (e.g., TSBDF) can be conservative. In this context, primitive variables P are used to model the state (e.g., because they lead to well-conditioned formulations even in limiting cases such as low-Mach or zero porosity). The transient variable is C(P), specified by calling this function. An IFunction thus receives arguments (P, Cdot) and the IJacobian must be evaluated via the chain rule, as in

TS: Scalable ODE and DAE Solvers, TS, TSBDF, TSTransientVariableFn, DMTSSetTransientVariable(), DMTSGetTransientVariable(), TSSetIFunction(), TSSetIJacobian()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetTransientVariable(TS ts, TSTransientVariableFn *tvar, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TSTransientVariableFn
```

Example 3 (unknown):
```unknown
dF/dP + shift * dF/dCdot dC/dP.
```

Example 4 (unknown):
```unknown
TSTransientVariableFn
```

---

## TSSetType#

**URL:** https://petsc.org/release/manualpages/TS/TSSetType/

**Contents:**
- TSSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the algorithm/method to be used for integrating the ODE with the given TS.

type - A known method

-ts_type type - Sets the method; see TSType

See TSType for available methods (for instance)

TSBEULER - Backward Euler

TSPSEUDO - Pseudo-timestepping

Normally, it is best to use the TSSetFromOptions() command and then set the TS type from the options database rather than by using this routine. Using the options database provides the user with maximum flexibility in evaluating the many different solvers. The TSSetType() routine is provided for those situations where it is necessary to set the timestepping solver independently of the command line or options database. This might be the case, for example, when the choice of solver changes during the execution of the program, and the user’s application is taking responsibility for choosing the appropriate method. In other words, this routine is not for beginners.

TS: Scalable ODE and DAE Solvers, TS, TSSolve(), TSCreate(), TSSetFromOptions(), TSDestroy(), TSType

src/ts/interface/tsreg.c

src/ml/da/tutorials/ex3.c src/ts/tutorials/ex1.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/tutorials/ex20opt_ic.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ml/da/tutorials/ex1.c src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex4.c src/ts/tutorials/ex41.c src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetType(TS ts, TSType type)
```

Example 2 (unknown):
```unknown
TSSetFromOptions()
```

Example 3 (unknown):
```unknown
TSSetFromOptions()
```

Example 4 (unknown):
```unknown
TSDestroy()
```

---

## TSSetUp#

**URL:** https://petsc.org/release/manualpages/TS/TSSetUp/

**Contents:**
- TSSetUp#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets up the internal data structures for the later use of a timestepper.

ts - the TS context obtained from TSCreate()

For basic use of the TS solvers the user need not explicitly call TSSetUp(), since these actions will automatically occur during the call to TSStep() or TSSolve(). However, if one wishes to control this phase separately, TSSetUp() should be called after TSCreate() and optional routines of the form TSSetXXX(), but before TSStep() and TSSolve().

TS: Scalable ODE and DAE Solvers, TSCreate(), TS, TSStep(), TSDestroy(), TSSolve()

src/ts/interface/ts.c

src/ts/tutorials/ex1.c src/ts/tutorials/ex1f.F90 src/ts/tutorials/ex42.c src/ts/tutorials/ex28.c src/ts/tutorials/ex53.c

TSSetUp_ARKIMEX() in src/ts/impls/arkimex/arkimex.c TSSetUp_BDF() in src/ts/impls/bdf/bdf.c TSSetUp_EIMEX() in src/ts/impls/eimex/eimex.c TSSetUp_Euler() in src/ts/impls/explicit/euler/euler.c TSSetUp_RK() in src/ts/impls/explicit/rk/rk.c TSSetUp_SSP() in src/ts/impls/explicit/ssp/ssp.c TSSetUp_GLEE() in src/ts/impls/glee/glee.c TSSetUp_Alpha() in src/ts/impls/implicit/alpha/alpha1.c TSSetUp_Alpha() in src/ts/impls/implicit/alpha/alpha2.c TSSetUp_DiscGrad() in src/ts/impls/implicit/discgrad/tsdiscgrad.c TSSetUp_GLLE() in src/ts/impls/implicit/glle/glle.c TSSetUp_IRK() in src/ts/impls/implicit/irk/irk.c TSSetUp_Sundials() in src/ts/impls/implicit/sundials/sundials.c TSSetUp_Theta() in src/ts/impls/implicit/theta/theta.c TSSetUp_BEuler() in src/ts/impls/implicit/theta/theta.c TSSetUp_CN() in src/ts/impls/implicit/theta/theta.c TSSetUp_Mimex() in src/ts/impls/mimex/mimex.c TSSetUp_MPRK() in src/ts/impls/multirate/mprk.c TSSetUp_Pseudo() in src/ts/impls/pseudo/posindep.c TSSetUp_RosW() in src/ts/impls/rosw/rosw.c TSSetUp_BasicSymplectic() in src/ts/impls/symplectic/basicsymplectic/basicsymplectic.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetUp(TS ts)
```

Example 2 (unknown):
```unknown
TSDestroy()
```

---

## TSSetUseSplitRHSFunction#

**URL:** https://petsc.org/release/manualpages/TS/TSSetUseSplitRHSFunction/

**Contents:**
- TSSetUseSplitRHSFunction#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Use the split RHSFunction when a multirate method is used.

ts - timestepping context

use_splitrhsfunction - PETSC_TRUE indicates that the split RHSFunction will be used

-ts_use_splitrhsfunction (true|false) - use the split RHS function for multirate solvers

This is only for multirate methods

TS: Scalable ODE and DAE Solvers, TS, TSGetUseSplitRHSFunction()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSetUseSplitRHSFunction(TS ts, PetscBool use_splitrhsfunction)
```

Example 2 (unknown):
```unknown
TSGetUseSplitRHSFunction()
```

---

## TSSolutionFn#

**URL:** https://petsc.org/release/manualpages/TS/TSSolutionFn/

**Contents:**
- TSSolutionFn#
- Synopsis#
- Calling Sequence#
- Note#
- See Also#
- Level#
- Location#

A prototype of a TS solution evaluation function that would be passed to TSSetSolutionFunction()

ts - timestep context

ctx - [optional] user-defined function context

The deprecated TSSolutionFunction still works as a replacement for TSSolutionFn *.

TS: Scalable ODE and DAE Solvers, TS, TSSetSolutionFunction(), DMTSSetSolutionFunction()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetSolutionFunction()
```

Example 2 (cpp):
```cpp
#include <petscts.h> 
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode TSSolutionFn(TS ts, PetscReal t, Vec u, PetscCtx ctx);
```

Example 3 (unknown):
```unknown
TSSolutionFunction
```

Example 4 (unknown):
```unknown
TSSolutionFn
```

---

## TSSolve#

**URL:** https://petsc.org/release/manualpages/TS/TSSolve/

**Contents:**
- TSSolve#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Steps the requested number of timesteps.

ts - the TS context obtained from TSCreate()

u - the solution vector (can be NULL if TSSetSolution() was used and TSSetExactFinalTime(ts,TS_EXACTFINALTIME_MATCHSTEP) was not used, otherwise it must contain the initial conditions and will contain the solution at the final requested time

The final time returned by this function may be different from the time of the internally held state accessible by TSGetSolution() and TSGetTime() because the method may have stepped over the final time.

TS: Scalable ODE and DAE Solvers, TS, TSCreate(), TSSetSolution(), TSStep(), TSGetTime(), TSGetSolveTime()

src/ts/interface/ts.c

src/ml/da/tutorials/ex3.c src/ts/tutorials/ex1.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ml/da/tutorials/ex1.c src/ml/da/tutorials/ex2.c src/ts/utils/dmplexlandau/tutorials/ex2.c src/ml/da/tutorials/ex4.c src/tao/unconstrained/tutorials/burgers_spectral.c src/ts/utils/dmplexlandau/tutorials/ex1f90.F90

TSSolve_GLLE() in src/ts/impls/implicit/glle/glle.c TSSolve_Radau5() in src/ts/impls/implicit/radau5/radau5.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSSolve(TS ts, Vec u)
```

Example 2 (unknown):
```unknown
TSSetSolution()
```

Example 3 (unknown):
```unknown
TSSetExactFinalTime
```

Example 4 (unknown):
```unknown
TS_EXACTFINALTIME_MATCHSTEP
```

---

## TSSSPFinalizePackage#

**URL:** https://petsc.org/release/manualpages/TS/TSSSPFinalizePackage/

**Contents:**
- TSSSPFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys everything in the TSSSP package. It is called from PetscFinalize().

TS: Scalable ODE and DAE Solvers, PetscFinalize(), TSSSPInitiallizePackage(), TSInitializePackage()

src/ts/impls/explicit/ssp/ssp.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSSSPFinalizePackage(void)
```

Example 3 (unknown):
```unknown
PetscFinalize()
```

Example 4 (unknown):
```unknown
TSSSPInitiallizePackage()
```

---

## TSSSPGetNumStages#

**URL:** https://petsc.org/release/manualpages/TS/TSSSPGetNumStages/

**Contents:**
- TSSSPGetNumStages#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

get the number of stages in the TSSSP time integration scheme

ts - time stepping object

nstages - number of stages

TS: Scalable ODE and DAE Solvers, TSSSP, TSSSPGetType(), TSSSPSetNumStages(), TSSSPRKS2, TSSSPRKS3, TSSSPRK104

src/ts/impls/explicit/ssp/ssp.c

TSSSPGetNumStages_SSP() in src/ts/impls/explicit/ssp/ssp.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSSSPGetNumStages(TS ts, PetscInt *nstages)
```

Example 2 (unknown):
```unknown
TSSSPGetType()
```

Example 3 (unknown):
```unknown
TSSSPSetNumStages()
```

---

## TSSSPGetType#

**URL:** https://petsc.org/release/manualpages/TS/TSSSPGetType/

**Contents:**
- TSSSPGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

get the TSSSP time integration scheme

ts - time stepping object

type - type of scheme being used

TS: Scalable ODE and DAE Solvers, TSSSP, TSSSPSetType(), TSSSPSetNumStages(), TSSSPRKS2, TSSSPRKS3, TSSSPRK104

src/ts/impls/explicit/ssp/ssp.c

TSSSPGetType_SSP() in src/ts/impls/explicit/ssp/ssp.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSSSPGetType(TS ts, TSSSPType *type)
```

Example 2 (unknown):
```unknown
TSSSPSetType()
```

Example 3 (unknown):
```unknown
TSSSPSetNumStages()
```

---

## TSSSPInitializePackage#

**URL:** https://petsc.org/release/manualpages/TS/TSSSPInitializePackage/

**Contents:**
- TSSSPInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function initializes everything in the TSSSP package. It is called from TSInitializePackage().

TS: Scalable ODE and DAE Solvers, PetscInitialize(), TSSSPFinalizePackage(), TSInitializePackage()

src/ts/impls/explicit/ssp/ssp.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSInitializePackage()
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSSSPInitializePackage(void)
```

Example 3 (unknown):
```unknown
PetscInitialize()
```

Example 4 (unknown):
```unknown
TSSSPFinalizePackage()
```

---

## TSSSPRKS104#

**URL:** https://petsc.org/release/manualpages/TS/TSSSPRKS104/

**Contents:**
- TSSSPRKS104#
- References#
- See Also#
- Level#
- Location#

Optimal fourth order SSP Runge-Kutta, low-storage (2N), c_eff=0.6 SSPRK(10,4), Pseudocode 3 of [Ket08]

D.I. Ketcheson. Highly efficient strong stability-preserving Runge–Kutta methods with low-storage implementations. SIAM Journal on Scientific Computing, 30(4):2113–2136, 2008. doi:10.1137/07070485X.

TS: Scalable ODE and DAE Solvers, TSSSP, TSSSPSetType()

src/ts/impls/explicit/ssp/ssp.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSSPSetType()
```

---

## TSSSPRKS2#

**URL:** https://petsc.org/release/manualpages/TS/TSSSPRKS2/

**Contents:**
- TSSSPRKS2#
- References#
- See Also#
- Level#
- Location#

Optimal second order SSP Runge-Kutta method, low-storage, c_eff=(s-1)/s. Pseudocode 2 of [Ket08]

D.I. Ketcheson. Highly efficient strong stability-preserving Runge–Kutta methods with low-storage implementations. SIAM Journal on Scientific Computing, 30(4):2113–2136, 2008. doi:10.1137/07070485X.

TS: Scalable ODE and DAE Solvers, TSSSP, TSSSPSetType(), TSSSPSetNumStages()

src/ts/impls/explicit/ssp/ssp.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSSPSetType()
```

Example 2 (unknown):
```unknown
TSSSPSetNumStages()
```

---

## TSSSPRKS3#

**URL:** https://petsc.org/release/manualpages/TS/TSSSPRKS3/

**Contents:**
- TSSSPRKS3#
- References#
- See Also#
- Level#
- Location#

Optimal third order SSP Runge-Kutta, low-storage, \(c_eff=(PetscSqrtReal(s)-1)/PetscSqrtReal(s)\), where PetscSqrtReal(s) is an integer Pseudocode 2 of [Ket08]

D.I. Ketcheson. Highly efficient strong stability-preserving Runge–Kutta methods with low-storage implementations. SIAM Journal on Scientific Computing, 30(4):2113–2136, 2008. doi:10.1137/07070485X.

TS: Scalable ODE and DAE Solvers, TSSSP, TSSSPSetType(), TSSSPSetNumStages()

src/ts/impls/explicit/ssp/ssp.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSqrtReal
```

Example 2 (unknown):
```unknown
TSSSPSetType()
```

Example 3 (unknown):
```unknown
TSSSPSetNumStages()
```

---

## TSSSPSetNumStages#

**URL:** https://petsc.org/release/manualpages/TS/TSSSPSetNumStages/

**Contents:**
- TSSSPSetNumStages#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Implementations#

set the number of stages to use with the TSSSP method. Must be called after TSSSPSetType().

ts - time stepping object

nstages - number of stages

-ts_ssp_type (rks2|rks3|rk104) - Type of TSSSP method, see TSSSPType

-ts_ssp_num_stages nstages - number of stages

TS: Scalable ODE and DAE Solvers, TSSSP, TSSSPGetNumStages(), TSSSPRKS2, TSSSPRKS3, TSSSPRK104

src/ts/impls/explicit/ssp/ssp.c

TSSSPSetNumStages_SSP() in src/ts/impls/explicit/ssp/ssp.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSSPSetType()
```

Example 2 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSSSPSetNumStages(TS ts, PetscInt nstages)
```

Example 3 (unknown):
```unknown
TSSSPGetNumStages()
```

---

## TSSSPSetType#

**URL:** https://petsc.org/release/manualpages/TS/TSSSPSetType/

**Contents:**
- TSSSPSetType#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Implementations#

set the TSSSP time integration scheme to use

ts - time stepping object

ssptype - type of scheme to use

-ts_ssp_type (rks2|rks3|rk104) - Type of TSSSP method, see TSSSPType

-ts_ssp_num_stages nstages - Number of stages

TS: Scalable ODE and DAE Solvers, TSSSP, TSSSPGetType(), TSSSPSetNumStages(), TSSSPRKS2, TSSSPRKS3, TSSSPRK104

src/ts/impls/explicit/ssp/ssp.c

TSSSPSetType_SSP() in src/ts/impls/explicit/ssp/ssp.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSSSPSetType(TS ts, TSSSPType ssptype)
```

Example 2 (unknown):
```unknown
TSSSPGetType()
```

Example 3 (unknown):
```unknown
TSSSPSetNumStages()
```

---

## TSSSPType#

**URL:** https://petsc.org/release/manualpages/TS/TSSSPType/

**Contents:**
- TSSSPType#
- Synopsis#
- See Also#
- Level#
- Location#

string with the name of a TSSSP scheme.

TS: Scalable ODE and DAE Solvers, TSSSPSetType(), TS, TSSSP

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h> 
typedef const char *TSSSPType;
#define TSSSPRKS2  "rks2"
#define TSSSPRKS3  "rks3"
#define TSSSPRK104 "rk104"
```

Example 2 (unknown):
```unknown
TSSSPSetType()
```

---

## TSSSP#

**URL:** https://petsc.org/release/manualpages/TS/TSSSP/

**Contents:**
- TSSSP#
- References#
- See Also#
- Level#
- Location#
- Examples#

Explicit strong stability preserving ODE solver [Ket08] [GKS09] Most hyperbolic conservation laws have exact solutions that are total variation diminishing (TVD) or total variation bounded (TVB) although these solutions often contain discontinuities. Spatial discretizations such as Godunov’s scheme and high-resolution finite volume methods (TVD limiters, ENO/WENO) are designed to preserve these properties, but they are usually formulated using a forward Euler time discretization or by coupling the space and time discretization as in the classical Lax-Wendroff scheme. When the space and time discretization is coupled, it is very difficult to produce schemes with high temporal accuracy while preserving TVD properties. An alternative is the semidiscrete formulation where we choose a spatial discretization that is TVD with forward Euler and then choose a time discretization that preserves the TVD property. Such integrators are called strong stability preserving (SSP).

Let c_eff be the minimum number of function evaluations required to step as far as one step of forward Euler while still being SSP. Some theoretical bounds

There are no explicit methods with c_eff > 1.

There are no explicit methods beyond order 4 (for nonlinear problems) and c_eff > 0.

There are no implicit methods with order greater than 1 and c_eff > 2.

This integrator provides Runge-Kutta methods of order 2, 3, and 4 with maximal values of c_eff. More stages allows for larger values of c_eff which improves efficiency. These implementations are low-memory and only use 2 or 3 work vectors regardless of the total number of stages, so e.g. 25-stage 3rd order methods may be an excellent choice.

Methods can be chosen with -ts_ssp_type {rks2,rks3,rk104}

rks2: Second order methods with any number s>1 of stages. c_eff = (s-1)/s

rks3: Third order methods with s=n^2 stages, n>1. c_eff = (s-n)/s

rk104: A 10-stage fourth order method. c_eff = 0.6

Sigal Gottlieb, David I. Ketcheson, and Chi Wang Shu. High order strong stability preserving time discretizations. Journal of Scientific Computing, 38(3):251–289, 2009. doi:10.1007/s10915-008-9239-z.

D.I. Ketcheson. Highly efficient strong stability-preserving Runge–Kutta methods with low-storage implementations. SIAM Journal on Scientific Computing, 30(4):2113–2136, 2008. doi:10.1137/07070485X.

TS: Scalable ODE and DAE Solvers, TSCreate(), TS, TSSetType()

src/ts/impls/explicit/ssp/ssp.c

src/ts/tutorials/ex9.c src/ts/tutorials/ex11.c src/ts/tutorials/ex31.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetType()
```

---

## TSStep#

**URL:** https://petsc.org/release/manualpages/TS/TSStep/

**Contents:**
- TSStep#
- Synopsis#
- Input Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

ts - the TS context obtained from TSCreate()

The public interface for the ODE/DAE solvers is TSSolve(), you should almost for sure be using that routine and not this routine.

The hook set using TSSetPreStep() is called before each attempt to take the step. In general, the time step size may be changed due to adaptive error controller or solve failures. Note that steps may contain multiple stages.

This may over-step the final time provided in TSSetMaxTime() depending on the time-step used. TSSolve() interpolates to exactly the time provided in TSSetMaxTime(). One can use TSInterpolate() to determine an interpolated solution within the final timestep.

TS: Scalable ODE and DAE Solvers, TS, TSCreate(), TSSetUp(), TSDestroy(), TSSolve(), TSSetPreStep(), TSSetPreStage(), TSSetPostStage(), TSInterpolate()

src/ts/interface/ts.c

TSStep_ARKIMEX() in src/ts/impls/arkimex/arkimex.c TSStep_BDF() in src/ts/impls/bdf/bdf.c TSStep_EIMEX() in src/ts/impls/eimex/eimex.c TSStep_Euler() in src/ts/impls/explicit/euler/euler.c TSStep_RK() in src/ts/impls/explicit/rk/rk.c TSStep_SSP() in src/ts/impls/explicit/ssp/ssp.c TSStep_GLEE() in src/ts/impls/glee/glee.c TSStep_Alpha() in src/ts/impls/implicit/alpha/alpha1.c TSStep_Alpha() in src/ts/impls/implicit/alpha/alpha2.c TSStep_DiscGrad() in src/ts/impls/implicit/discgrad/tsdiscgrad.c TSStep_IRK() in src/ts/impls/implicit/irk/irk.c TSStep_Sundials() in src/ts/impls/implicit/sundials/sundials.c TSStep_Theta() in src/ts/impls/implicit/theta/theta.c TSStep_Mimex() in src/ts/impls/mimex/mimex.c TSStep_MPRK() in src/ts/impls/multirate/mprk.c TSStep_MPRKSPLIT() in src/ts/impls/multirate/mprk.c TSStep_Pseudo() in src/ts/impls/pseudo/posindep.c TSStep_RosW() in src/ts/impls/rosw/rosw.c TSStep_BasicSymplectic() in src/ts/impls/symplectic/basicsymplectic/basicsymplectic.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSStep(TS ts)
```

Example 2 (unknown):
```unknown
TSSetPreStep()
```

Example 3 (unknown):
```unknown
TSSetMaxTime()
```

Example 4 (unknown):
```unknown
TSSetMaxTime()
```

---

## TSSundialsGetIterations#

**URL:** https://petsc.org/release/manualpages/TS/TSSundialsGetIterations/

**Contents:**
- TSSundialsGetIterations#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Gets the number of nonlinear and linear iterations used so far by TSSUNDIALS.

ts - the time-step context

nonlin - number of nonlinear iterations

lin - number of linear iterations

These return the number since the creation of the TS object

TS: Scalable ODE and DAE Solvers, TSSundialsSetType(), TSSundialsSetMaxl(), TSSundialsSetLinearTolerance(), TSSundialsSetGramSchmidtType(), TSSundialsSetTolerance(), TSSundialsGetPC(), TSSetExactFinalTime()

src/ts/impls/implicit/sundials/sundials.c

TSSundialsGetIterations_Sundials() in src/ts/impls/implicit/sundials/sundials.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSSundialsGetIterations(TS ts, int *nonlin, int *lin)
```

Example 2 (unknown):
```unknown
TSSundialsSetType()
```

Example 3 (unknown):
```unknown
TSSundialsSetMaxl()
```

Example 4 (unknown):
```unknown
TSSundialsSetLinearTolerance()
```

---

## TSSundialsGetPC#

**URL:** https://petsc.org/release/manualpages/TS/TSSundialsGetPC/

**Contents:**
- TSSundialsGetPC#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Extract the PC context from a time-step context for TSSUNDIALS.

ts - the time-step context

pc - the preconditioner context

TS: Scalable ODE and DAE Solvers, TSSundialsGetIterations(), TSSundialsSetType(), TSSundialsSetMaxl(), TSSundialsSetLinearTolerance(), TSSundialsSetGramSchmidtType(), TSSundialsSetTolerance()

src/ts/impls/implicit/sundials/sundials.c

TSSundialsGetPC_Sundials() in src/ts/impls/implicit/sundials/sundials.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSSundialsGetPC(TS ts, PC *pc)
```

Example 2 (unknown):
```unknown
TSSundialsGetIterations()
```

Example 3 (unknown):
```unknown
TSSundialsSetType()
```

Example 4 (unknown):
```unknown
TSSundialsSetMaxl()
```

---

## TSSundialsGramSchmidtType#

**URL:** https://petsc.org/release/manualpages/TS/TSSundialsGramSchmidtType/

**Contents:**
- TSSundialsGramSchmidtType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Selects the Gram–Schmidt orthogonalization variant used by SUNDIALS’ internal GMRES inside TSSUNDIALS

SUNDIALS_MODIFIED_GS - modified Gram–Schmidt (more stable)

SUNDIALS_CLASSICAL_GS - classical Gram–Schmidt (cheaper, less stable)

TS, TSSUNDIALS, TSSundialsSetGramSchmidtType(), TSSundialsLmmType

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h> 
typedef enum {
  SUNDIALS_MODIFIED_GS  = 1,
  SUNDIALS_CLASSICAL_GS = 2
} TSSundialsGramSchmidtType;
```

Example 2 (unknown):
```unknown
SUNDIALS_MODIFIED_GS
```

Example 3 (unknown):
```unknown
SUNDIALS_CLASSICAL_GS
```

Example 4 (unknown):
```unknown
TSSundialsSetGramSchmidtType()
```

---

## TSSundialsLmmType#

**URL:** https://petsc.org/release/manualpages/TS/TSSundialsLmmType/

**Contents:**
- TSSundialsLmmType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Selects which linear multistep method is used by the TSSUNDIALS interface to SUNDIALS’ CVODE integrator

SUNDIALS_ADAMS - variable-order Adams methods (non-stiff problems)

SUNDIALS_BDF - variable-order backward differentiation formulas (stiff problems)

TS, TSSUNDIALS, TSSundialsSetType(), TSSundialsGramSchmidtType

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h> 
typedef enum {
  SUNDIALS_ADAMS = 1,
  SUNDIALS_BDF   = 2
} TSSundialsLmmType;
```

Example 2 (unknown):
```unknown
SUNDIALS_ADAMS
```

Example 3 (unknown):
```unknown
SUNDIALS_BDF
```

Example 4 (unknown):
```unknown
TSSundialsSetType()
```

---

## TSSundialsMonitorInternalSteps#

**URL:** https://petsc.org/release/manualpages/TS/TSSundialsMonitorInternalSteps/

**Contents:**
- TSSundialsMonitorInternalSteps#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Monitor TSSUNDIALS internal steps (Defaults to false).

ts - the time-step context

ft - PETSC_TRUE if monitor, else PETSC_FALSE

TS: Scalable ODE and DAE Solvers, TSSundialsGetIterations(), TSSundialsSetType(), TSSundialsSetMaxl(), TSSundialsSetLinearTolerance(), TSSundialsSetGramSchmidtType(), TSSundialsSetTolerance(), TSSundialsGetPC()

src/ts/impls/implicit/sundials/sundials.c

TSSundialsMonitorInternalSteps_Sundials() in src/ts/impls/implicit/sundials/sundials.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSSundialsMonitorInternalSteps(TS ts, PetscBool ft)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
TSSundialsGetIterations()
```

Example 4 (unknown):
```unknown
TSSundialsSetType()
```

---

## TSSundialsSetGramSchmidtType#

**URL:** https://petsc.org/release/manualpages/TS/TSSundialsSetGramSchmidtType/

**Contents:**
- TSSundialsSetGramSchmidtType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Sets type of orthogonalization used in GMRES method by TSSUNDIALS linear solver.

ts - the time-step context

type - either SUNDIALS_MODIFIED_GS or SUNDIALS_CLASSICAL_GS

TS: Scalable ODE and DAE Solvers, TSSundialsGetIterations(), TSSundialsSetType(), TSSundialsSetMaxl(), TSSundialsSetLinearTolerance(), TSSundialsSetTolerance(), TSSundialsGetPC(), TSSetExactFinalTime()

src/ts/impls/implicit/sundials/sundials.c

TSSundialsSetGramSchmidtType_Sundials() in src/ts/impls/implicit/sundials/sundials.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSSundialsSetGramSchmidtType(TS ts, TSSundialsGramSchmidtType type)
```

Example 2 (unknown):
```unknown
SUNDIALS_MODIFIED_GS
```

Example 3 (unknown):
```unknown
SUNDIALS_CLASSICAL_GS
```

Example 4 (unknown):
```unknown
TSSundialsGetIterations()
```

---

## TSSundialsSetLinearTolerance#

**URL:** https://petsc.org/release/manualpages/TS/TSSundialsSetLinearTolerance/

**Contents:**
- TSSundialsSetLinearTolerance#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Sets the tolerance used to solve the linear system by TSSUNDIALS.

ts - the time-step context

tol - the factor by which the tolerance on the nonlinear solver is multiplied to get the tolerance on the linear solver, .05 by default.

TS: Scalable ODE and DAE Solvers, TSSundialsGetIterations(), TSSundialsSetType(), TSSundialsSetMaxl(), TSSundialsSetGramSchmidtType(), TSSundialsSetTolerance(), TSSundialsGetPC(), TSSetExactFinalTime()

src/ts/impls/implicit/sundials/sundials.c

TSSundialsSetLinearTolerance_Sundials() in src/ts/impls/implicit/sundials/sundials.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSSundialsSetLinearTolerance(TS ts, PetscReal tol)
```

Example 2 (unknown):
```unknown
TSSundialsGetIterations()
```

Example 3 (unknown):
```unknown
TSSundialsSetType()
```

Example 4 (unknown):
```unknown
TSSundialsSetMaxl()
```

---

## TSSundialsSetMaxl#

**URL:** https://petsc.org/release/manualpages/TS/TSSundialsSetMaxl/

**Contents:**
- TSSundialsSetMaxl#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Sets the dimension of the Krylov space used by GMRES in the linear solver in TSSUNDIALS. TSSUNDIALS DOES NOT use restarted GMRES so this is the maximum number of GMRES steps that will be used.

ts - the time-step context

maxl - number of direction vectors (the dimension of Krylov subspace).

TS: Scalable ODE and DAE Solvers, TSSundialsGetIterations(), TSSundialsSetType(), TSSundialsSetLinearTolerance(), TSSundialsSetGramSchmidtType(), TSSundialsSetTolerance(), TSSundialsGetPC(), TSSetExactFinalTime()

src/ts/impls/implicit/sundials/sundials.c

TSSundialsSetMaxl_Sundials() in src/ts/impls/implicit/sundials/sundials.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSSundialsSetMaxl(TS ts, PetscInt maxl)
```

Example 2 (unknown):
```unknown
TSSundialsGetIterations()
```

Example 3 (unknown):
```unknown
TSSundialsSetType()
```

Example 4 (unknown):
```unknown
TSSundialsSetLinearTolerance()
```

---

## TSSundialsSetMaxord#

**URL:** https://petsc.org/release/manualpages/TS/TSSundialsSetMaxord/

**Contents:**
- TSSundialsSetMaxord#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the maximum order for BDF/Adams method used by TSSUNDIALS.

ts - the time-step context

maxord - maximum order of BDF / Adams method

TS: Scalable ODE and DAE Solvers, TSSundialsGetIterations(), TSSundialsSetType(), TSSundialsSetLinearTolerance(), TSSundialsSetGramSchmidtType(), TSSundialsSetTolerance(), TSSundialsGetPC(), TSSetExactFinalTime()

src/ts/impls/implicit/sundials/sundials.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSSundialsSetMaxord(TS ts, PetscInt maxord)
```

Example 2 (unknown):
```unknown
TSSundialsGetIterations()
```

Example 3 (unknown):
```unknown
TSSundialsSetType()
```

Example 4 (unknown):
```unknown
TSSundialsSetLinearTolerance()
```

---

## TSSundialsSetMaxTimeStep#

**URL:** https://petsc.org/release/manualpages/TS/TSSundialsSetMaxTimeStep/

**Contents:**
- TSSundialsSetMaxTimeStep#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Largest time step to be chosen by the adaptive controller.

ts - the time-step context

maxdt - lowest time step if positive, negative to deactivate

TS: Scalable ODE and DAE Solvers, TSSundialsSetType(), TSSundialsSetTolerance()

src/ts/impls/implicit/sundials/sundials.c

TSSundialsSetMaxTimeStep_Sundials() in src/ts/impls/implicit/sundials/sundials.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSSundialsSetMaxTimeStep(TS ts, PetscReal maxdt)
```

Example 2 (unknown):
```unknown
TSSundialsSetType()
```

Example 3 (unknown):
```unknown
TSSundialsSetTolerance()
```

---

## TSSundialsSetMinTimeStep#

**URL:** https://petsc.org/release/manualpages/TS/TSSundialsSetMinTimeStep/

**Contents:**
- TSSundialsSetMinTimeStep#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Smallest time step to be chosen by the adaptive controller.

ts - the time-step context

mindt - lowest time step if positive, negative to deactivate

TSSUNDIALS will error if it is not possible to keep the estimated truncation error below the tolerance set with TSSundialsSetTolerance() without going below this step size.

TS: Scalable ODE and DAE Solvers, TSSundialsSetType(), TSSundialsSetTolerance()

src/ts/impls/implicit/sundials/sundials.c

TSSundialsSetMinTimeStep_Sundials() in src/ts/impls/implicit/sundials/sundials.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSSundialsSetMinTimeStep(TS ts, PetscReal mindt)
```

Example 2 (unknown):
```unknown
TSSundialsSetTolerance()
```

Example 3 (unknown):
```unknown
TSSundialsSetType()
```

Example 4 (unknown):
```unknown
TSSundialsSetTolerance()
```

---

## TSSundialsSetTolerance#

**URL:** https://petsc.org/release/manualpages/TS/TSSundialsSetTolerance/

**Contents:**
- TSSundialsSetTolerance#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Sets the absolute and relative tolerance used by TSSUNDIALS for error control.

ts - the time-step context

aabs - the absolute tolerance

rel - the relative tolerance

See the CVODE/SUNDIALS users manual for exact details on these parameters. Essentially these regulate the size of the error for a SINGLE timestep.

TS: Scalable ODE and DAE Solvers, TSSundialsGetIterations(), TSSundialsSetType(), TSSundialsSetGMRESMaxl(), TSSundialsSetLinearTolerance(), TSSundialsSetGramSchmidtType(), TSSundialsGetPC(), TSSetExactFinalTime()

src/ts/impls/implicit/sundials/sundials.c

TSSundialsSetTolerance_Sundials() in src/ts/impls/implicit/sundials/sundials.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSSundialsSetTolerance(TS ts, PetscReal aabs, PetscReal rel)
```

Example 2 (unknown):
```unknown
TSSundialsGetIterations()
```

Example 3 (unknown):
```unknown
TSSundialsSetType()
```

Example 4 (unknown):
```unknown
TSSundialsSetGMRESMaxl()
```

---

## TSSundialsSetType#

**URL:** https://petsc.org/release/manualpages/TS/TSSundialsSetType/

**Contents:**
- TSSundialsSetType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Sets the method that TSSUNDIALS will use for integration.

ts - the time-step context

type - one of SUNDIALS_ADAMS or SUNDIALS_BDF

TS: Scalable ODE and DAE Solvers, TSSundialsGetIterations(), TSSundialsSetMaxl(), TSSundialsSetLinearTolerance(), TSSundialsSetGramSchmidtType(), TSSundialsSetTolerance(), TSSundialsGetPC(), TSSetExactFinalTime()

src/ts/impls/implicit/sundials/sundials.c

TSSundialsSetType_Sundials() in src/ts/impls/implicit/sundials/sundials.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSSundialsSetType(TS ts, TSSundialsLmmType type)
```

Example 2 (unknown):
```unknown
SUNDIALS_ADAMS
```

Example 3 (unknown):
```unknown
SUNDIALS_BDF
```

Example 4 (unknown):
```unknown
TSSundialsGetIterations()
```

---

## TSSundialsSetUseDense#

**URL:** https://petsc.org/release/manualpages/TS/TSSundialsSetUseDense/

**Contents:**
- TSSundialsSetUseDense#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set a flag to use a dense linear solver in TSSUNDIALS (serial only)

ts - the time-step context

use_dense - PETSC_TRUE to use the dense solver

TS: Scalable ODE and DAE Solvers, TSSUNDIALS

src/ts/impls/implicit/sundials/sundials.c

TSSundialsSetUseDense_Sundials() in src/ts/impls/implicit/sundials/sundials.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h" 
PetscErrorCode TSSundialsSetUseDense(TS ts, PetscBool use_dense)
```

---

## TSSUNDIALS#

**URL:** https://petsc.org/release/manualpages/TS/TSSUNDIALS/

**Contents:**
- TSSUNDIALS#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#

ODE solver using a very old version of the LLNL CVODE/SUNDIALS package, version 2.5 (now called SUNDIALS). Requires ./configure –download-sundials

-ts_sundials_type (bdf|adams) - integrator type

-ts_sundials_gramschmidt_type (modified|classical) - type of orthogonalization inside GMRES

-ts_sundials_atol atol - Absolute tolerance for convergence

-ts_sundials_rtol rtol - Relative tolerance for convergence

-ts_sundials_linear_tolerance ltol - convergence tolerance for linear solver

-ts_sundials_maxl maxl - Max dimension of the Krylov subspace

-ts_sundials_monitor_steps - Monitor SUNDIALS internal steps

-ts_sundials_use_dense - Use a dense linear solver within CVODE (serial only)

This uses its own nonlinear solver and Krylov method so PETSc SNES and KSP options do not apply, only PETSc PC options.

TS: Scalable ODE and DAE Solvers, TSCreate(), TS, TSSetType(), TSSundialsSetType(), TSSundialsSetMaxl(), TSSundialsSetLinearTolerance(), TSType, TSSundialsSetGramSchmidtType(), TSSundialsSetTolerance(), TSSundialsGetPC(), TSSundialsGetIterations(), TSSetExactFinalTime()

src/ts/impls/implicit/sundials/sundials.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetType()
```

Example 2 (unknown):
```unknown
TSSundialsSetType()
```

Example 3 (unknown):
```unknown
TSSundialsSetMaxl()
```

Example 4 (unknown):
```unknown
TSSundialsSetLinearTolerance()
```

---

## TSThetaGetEndpoint#

**URL:** https://petsc.org/release/manualpages/TS/TSThetaGetEndpoint/

**Contents:**
- TSThetaGetEndpoint#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Gets whether to use the endpoint variant of the method (e.g. trapezoid/Crank-Nicolson instead of midpoint rule) for TSTHETA

ts - timestepping context

endpoint - PETSC_TRUE when using the endpoint variant

TS: Scalable ODE and DAE Solvers, TSThetaSetEndpoint(), TSTHETA, TSCN

src/ts/impls/implicit/theta/theta.c

TSThetaGetEndpoint_Theta() in src/ts/impls/implicit/theta/theta.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSThetaGetEndpoint(TS ts, PetscBool *endpoint)
```

Example 2 (unknown):
```unknown
TSThetaSetEndpoint()
```

---

## TSThetaGetTheta#

**URL:** https://petsc.org/release/manualpages/TS/TSThetaGetTheta/

**Contents:**
- TSThetaGetTheta#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Get the abscissa of the stage in (0,1] for TSTHETA

ts - timestepping context

theta - stage abscissa

Use of this function is normally only required to hack TSTHETA to use a modified integration scheme.

TS: Scalable ODE and DAE Solvers, TSThetaSetTheta(), TSTHETA

src/ts/impls/implicit/theta/theta.c

src/ts/tutorials/ex10.c

TSThetaGetTheta_Theta() in src/ts/impls/implicit/theta/theta.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSThetaGetTheta(TS ts, PetscReal *theta)
```

Example 2 (unknown):
```unknown
TSThetaSetTheta()
```

---

## TSThetaSetEndpoint#

**URL:** https://petsc.org/release/manualpages/TS/TSThetaSetEndpoint/

**Contents:**
- TSThetaSetEndpoint#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

Sets whether to use the endpoint variant of the method (e.g. trapezoid/Crank-Nicolson instead of midpoint rule) for TSTHETA

ts - timestepping context

flg - PETSC_TRUE to use the endpoint variant

-ts_theta_endpoint flg - use the endpoint variant

TS: Scalable ODE and DAE Solvers, TSTHETA, TSCN

src/ts/impls/implicit/theta/theta.c

TSThetaSetEndpoint_Theta() in src/ts/impls/implicit/theta/theta.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSThetaSetEndpoint(TS ts, PetscBool flg)
```

---

## TSThetaSetTheta#

**URL:** https://petsc.org/release/manualpages/TS/TSThetaSetTheta/

**Contents:**
- TSThetaSetTheta#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Set the abscissa of the stage in (0,1] for TSTHETA

ts - timestepping context

theta - stage abscissa

-ts_theta_theta theta - set theta

TS: Scalable ODE and DAE Solvers, TSThetaGetTheta(), TSTHETA, TSCN

src/ts/impls/implicit/theta/theta.c

src/ts/tutorials/ex17.c

TSThetaSetTheta_Theta() in src/ts/impls/implicit/theta/theta.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"   
PetscErrorCode TSThetaSetTheta(TS ts, PetscReal theta)
```

Example 2 (unknown):
```unknown
TSThetaGetTheta()
```

---

## TSTHETA#

**URL:** https://petsc.org/release/manualpages/TS/TSTHETA/

**Contents:**
- TSTHETA#
- Options Database Keys#
- Notes#
- When the endpoint variant is chosen, the method becomes a 2-stage method with first stage explicit#
- See Also#
- Level#
- Location#
- Examples#

DAE solver using the implicit Theta method

-ts_theta_theta Theta - Location of stage (0<Theta<=1)

-ts_theta_endpoint flag - Use the endpoint (like Crank-Nicholson) instead of midpoint form of the Theta method

-ts_theta_initial_guess_extrapolate flg - Extrapolate stage initial guess from previous solution (sometimes unstable)

The endpoint variant of the Theta method and backward Euler can be applied to DAE. The midpoint variant is not suitable for DAEs because it is not stiffly accurate.

The midpoint variant is cast as a 1-stage implicit Runge-Kutta method.

For the default Theta=0.5, this is also known as the implicit midpoint rule.

For the default Theta=0.5, this is the trapezoid rule (also known as Crank-Nicolson, see TSCN).

To apply a diagonally implicit RK method to DAE, the stage formula

is interpreted as a formula for Y’_i in terms of Y_i and known values (Y’_j, j<i)

TS: Scalable ODE and DAE Solvers, TSCreate(), TS, TSSetType(), TSCN, TSBEULER, TSThetaSetTheta(), TSThetaSetEndpoint()

src/ts/impls/implicit/theta/theta.c

src/ts/tutorials/ex14.c src/ts/tutorials/ex31.c src/ts/tutorials/ex17.c src/ts/tutorials/ex10.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
-ts_type theta -ts_theta_theta 1.0 corresponds to backward Euler (TSBEULER)
  -ts_type theta -ts_theta_theta 0.5 corresponds to the implicit midpoint rule
  -ts_type theta -ts_theta_theta 0.5 -ts_theta_endpoint corresponds to Crank-Nicholson (TSCN)
```

Example 2 (yaml):
```yaml
Theta | Theta
  -------------
        |  1
```

Example 3 (yaml):
```yaml
0 | 0         0
  1 | 1-Theta   Theta
  -------------------
    | 1-Theta   Theta
```

Example 4 (unknown):
```unknown
Y_i = X + h sum_j a_ij Y'_j
```

---

## TSTRAJECTORYBASIC#

**URL:** https://petsc.org/release/manualpages/TS/TSTRAJECTORYBASIC/

**Contents:**
- TSTRAJECTORYBASIC#
- See Also#
- Level#
- Location#

Stores each solution of the ODE/DAE in a file Saves each timestep into a separate file named TS-data-XXXXXX/TS-%06d.bin. The file name can be changed.

This version saves the solutions at all the stages

$PETSC_DIR/share/petsc/matlab/PetscReadBinaryTrajectory.m can read in files created with this format

TS: Scalable ODE and DAE Solvers, TSTrajectoryCreate(), TS, TSTrajectory, TSTrajectorySetType(), TSTrajectorySetDirname(), TSTrajectorySetFile(), TSTrajectoryType

src/ts/trajectory/impls/basic/trajbasic.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSTrajectoryCreate()
```

Example 2 (unknown):
```unknown
TSTrajectory
```

Example 3 (unknown):
```unknown
TSTrajectorySetType()
```

Example 4 (unknown):
```unknown
TSTrajectorySetDirname()
```

---

## TSTrajectoryCreate#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectoryCreate/

**Contents:**
- TSTrajectoryCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

This function creates an empty trajectory object used to store the time dependent solution of an ODE/DAE

comm - the communicator

tj - the trajectory object

Usually one does not call this routine, it is called automatically when one calls TSSetSaveTrajectory().

TS: Scalable ODE and DAE Solvers, TS, TSTrajectory, TSTrajectorySetUp(), TSTrajectoryDestroy(), TSTrajectorySetType(), TSTrajectorySetVariableNames(), TSGetTrajectory(), TSTrajectorySetKeepFiles()

src/ts/trajectory/interface/traj.c

TSTrajectoryCreate_Basic() in src/ts/trajectory/impls/basic/trajbasic.c TSTrajectoryCreate_Memory() in src/ts/trajectory/impls/memory/trajmemory.c TSTrajectoryCreate_Singlefile() in src/ts/trajectory/impls/singlefile/singlefile.c TSTrajectoryCreate_Visualization() in src/ts/trajectory/impls/visualization/trajvisualization.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectoryCreate(MPI_Comm comm, TSTrajectory *tj)
```

Example 2 (unknown):
```unknown
TSSetSaveTrajectory()
```

Example 3 (unknown):
```unknown
TSTrajectory
```

Example 4 (unknown):
```unknown
TSTrajectorySetUp()
```

---

## TSTrajectoryDestroy#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectoryDestroy/

**Contents:**
- TSTrajectoryDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Destroys a trajectory context

tj - the TSTrajectory context obtained from TSTrajectoryCreate()

TS: Scalable ODE and DAE Solvers, TSTrajectory, TSTrajectoryCreate(), TSTrajectorySetUp()

src/ts/trajectory/interface/traj.c

TSTrajectoryDestroy_Basic() in src/ts/trajectory/impls/basic/trajbasic.c TSTrajectoryDestroy_Memory() in src/ts/trajectory/impls/memory/trajmemory.c TSTrajectoryDestroy_Singlefile() in src/ts/trajectory/impls/singlefile/singlefile.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectoryDestroy(TSTrajectory *tj)
```

Example 2 (unknown):
```unknown
TSTrajectory
```

Example 3 (unknown):
```unknown
TSTrajectoryCreate()
```

Example 4 (unknown):
```unknown
TSTrajectory
```

---

## TSTrajectoryGetNumSteps#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectoryGetNumSteps/

**Contents:**
- TSTrajectoryGetNumSteps#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Return the number of steps registered in the TSTrajectory via TSTrajectorySet().

tj - the trajectory object

steps - the number of steps

TS: Scalable ODE and DAE Solvers, TS, TSTrajectorySet()

src/ts/trajectory/interface/traj.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSTrajectory
```

Example 2 (unknown):
```unknown
TSTrajectorySet()
```

Example 3 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectoryGetNumSteps(TSTrajectory tj, PetscInt *steps)
```

Example 4 (unknown):
```unknown
TSTrajectorySet()
```

---

## TSTrajectoryGetSolutionOnly#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectoryGetSolutionOnly/

**Contents:**
- TSTrajectoryGetSolutionOnly#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the value set with TSTrajectorySetSolutionOnly().

tj - the TSTrajectory context

solution_only - the boolean flag

TS: Scalable ODE and DAE Solvers, TSTrajectory, TSSetSaveTrajectory(), TSTrajectoryCreate(), TSTrajectoryDestroy(), TSTrajectorySetSolutionOnly()

src/ts/trajectory/interface/traj.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSTrajectorySetSolutionOnly()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectoryGetSolutionOnly(TSTrajectory tj, PetscBool *solution_only)
```

Example 3 (unknown):
```unknown
TSTrajectory
```

Example 4 (unknown):
```unknown
TSTrajectory
```

---

## TSTrajectoryGetType#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectoryGetType/

**Contents:**
- TSTrajectoryGetType#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the trajectory type

tj - the TSTrajectory context

type - a known method

TS: Scalable ODE and DAE Solvers, TS, TSTrajectory, TSTrajectoryCreate(), TSTrajectorySetFromOptions(), TSTrajectoryDestroy(), TSTrajectorySetType()

src/ts/trajectory/interface/traj.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectoryGetType(TSTrajectory tj, TS ts, TSTrajectoryType *type)
```

Example 2 (unknown):
```unknown
TSTrajectory
```

Example 3 (unknown):
```unknown
TSTrajectory
```

Example 4 (unknown):
```unknown
TSTrajectoryCreate()
```

---

## TSTrajectoryGetUpdatedHistoryVecs#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectoryGetUpdatedHistoryVecs/

**Contents:**
- TSTrajectoryGetUpdatedHistoryVecs#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Get updated state and time-derivative history vectors.

tj - the TSTrajectory context

ts - the TS solver context

time - the requested time

U - state vector at given time (can be interpolated)

Udot - time-derivative vector at given time (can be interpolated)

The vectors are interpolated if time does not match any time step stored in the TSTrajectory(). Pass NULL to not request a vector.

This function differs from TSTrajectoryGetVecs() since the vectors obtained cannot be modified, and they need to be returned by calling TSTrajectoryRestoreUpdatedHistoryVecs().

TS: Scalable ODE and DAE Solvers, TSTrajectory, TSSetSaveTrajectory(), TSTrajectoryCreate(), TSTrajectoryDestroy(), TSTrajectoryRestoreUpdatedHistoryVecs(), TSTrajectoryGetVecs()

src/ts/trajectory/interface/traj.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectoryGetUpdatedHistoryVecs(TSTrajectory tj, TS ts, PetscReal time, Vec *U, Vec *Udot)
```

Example 2 (unknown):
```unknown
TSTrajectory
```

Example 3 (unknown):
```unknown
TSTrajectory()
```

Example 4 (unknown):
```unknown
TSTrajectoryGetVecs()
```

---

## TSTrajectoryGetVecs#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectoryGetVecs/

**Contents:**
- TSTrajectoryGetVecs#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Reconstructs the vector of state and its time derivative using information from the TSTrajectory and, possibly, from the TS

tj - the trajectory object

ts - the time stepper object (optional)

stepnum - the requested step number

time - On input time for the step if step number is PETSC_DECIDE, on output the time associated with the step number

U - state vector (can be NULL)

Udot - time derivative of state vector (can be NULL)

If the step number is PETSC_DECIDE, the time argument is used to inquire the trajectory. If the requested time does not match any in the trajectory, Lagrangian interpolations are returned.

TS: Scalable ODE and DAE Solvers, TS, TSTrajectory, TSTrajectorySetUp(), TSTrajectoryDestroy(), TSTrajectorySetType(), TSTrajectorySetVariableNames(), TSGetTrajectory(), TSTrajectorySet(), TSTrajectoryGet()

src/ts/trajectory/interface/traj.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSTrajectory
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectoryGetVecs(TSTrajectory tj, TS ts, PetscInt stepnum, PetscReal *time, Vec U, Vec Udot)
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

## TSTrajectoryGet#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectoryGet/

**Contents:**
- TSTrajectoryGet#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Updates the solution vector of a time stepper object by querying the TSTrajectory

tj - the trajectory object

ts - the time stepper object

stepnum - the step number

time - the time associated with the step number

Usually one does not call this routine, it is called automatically during TSSolve()

TS: Scalable ODE and DAE Solvers, TS, TSSolve(), TSTrajectorySetUp(), TSTrajectoryDestroy(), TSTrajectorySetType(), TSTrajectorySetVariableNames(), TSGetTrajectory(), TSTrajectorySet(), TSTrajectoryGetVecs(), TSGetSolution()

src/ts/trajectory/interface/traj.c

TSTrajectoryGet_Basic() in src/ts/trajectory/impls/basic/trajbasic.c TSTrajectoryGet_Memory() in src/ts/trajectory/impls/memory/trajmemory.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSTrajectory
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectoryGet(TSTrajectory tj, TS ts, PetscInt stepnum, PetscReal *time)
```

Example 3 (unknown):
```unknown
TSTrajectorySetUp()
```

Example 4 (unknown):
```unknown
TSTrajectoryDestroy()
```

---

## TSTrajectoryMemorySetType#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectoryMemorySetType/

**Contents:**
- TSTrajectoryMemorySetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

sets the software that is used to generate the checkpointing schedule.

tj - the TSTrajectory context

tj_memory_type - Revolve or CAMS

-ts_trajectory_memory_type tj_memory_type - petsc, revolve, cams

TS: Scalable ODE and DAE Solvers, TSTrajectory, TSTrajectorySetMaxUnitsRAM(), TSTrajectoryMemoryType

src/ts/trajectory/impls/memory/trajmemory.c

TSTrajectoryMemorySetType_Memory() in src/ts/trajectory/impls/memory/trajmemory.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectoryMemorySetType(TSTrajectory tj, TSTrajectoryMemoryType tj_memory_type)
```

Example 2 (unknown):
```unknown
TSTrajectory
```

Example 3 (unknown):
```unknown
TSTrajectory
```

Example 4 (unknown):
```unknown
TSTrajectorySetMaxUnitsRAM()
```

---

## TSTrajectoryMemoryType#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectoryMemoryType/

**Contents:**
- TSTrajectoryMemoryType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Selects the in-memory checkpointing scheme used by TSTRAJECTORYMEMORY to store the forward states needed for an adjoint or sensitivity computation

TJ_REVOLVE - the Revolve binomial checkpointing schedule of Griewank & Walther

TJ_CAMS - the CAMS (cache-aware multistage) checkpointing schedule

TJ_PETSC - PETSc’s own in-memory checkpointing implementation

TSTrajectory, TSTRAJECTORYMEMORY, TSTrajectoryMemorySetType(), TSSetSaveTrajectory()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSTRAJECTORYMEMORY
```

Example 2 (cpp):
```cpp
#include <petscts.h> 
typedef enum {
  TJ_REVOLVE,
  TJ_CAMS,
  TJ_PETSC
} TSTrajectoryMemoryType;
```

Example 3 (unknown):
```unknown
TSTrajectory
```

Example 4 (unknown):
```unknown
TSTRAJECTORYMEMORY
```

---

## TSTRAJECTORYMEMORY#

**URL:** https://petsc.org/release/manualpages/TS/TSTRAJECTORYMEMORY/

**Contents:**
- TSTRAJECTORYMEMORY#
- See Also#
- Level#
- Location#

Stores each solution of the ODE/ADE in memory

TS: Scalable ODE and DAE Solvers, TSTrajectoryCreate(), TS, TSTrajectorySetType(), TSTrajectoryType, TSTrajectory

src/ts/trajectory/impls/memory/trajmemory.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSTrajectoryCreate()
```

Example 2 (unknown):
```unknown
TSTrajectorySetType()
```

Example 3 (unknown):
```unknown
TSTrajectoryType
```

Example 4 (unknown):
```unknown
TSTrajectory
```

---

## TSTrajectoryRegisterAll#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectoryRegisterAll/

**Contents:**
- TSTrajectoryRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the TSTrajectory storage schecmes in the TS package.

TS: Scalable ODE and DAE Solvers, TSTrajectory, TSTrajectoryRegister()

src/ts/trajectory/interface/traj.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSTrajectory
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectoryRegisterAll(void)
```

Example 3 (unknown):
```unknown
TSTrajectory
```

Example 4 (unknown):
```unknown
TSTrajectoryRegister()
```

---

## TSTrajectoryRegister#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectoryRegister/

**Contents:**
- TSTrajectoryRegister#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Adds a way of storing trajectories to the TS package

Not Collective, No Fortran Support

sname - the name of a new user-defined creation routine

function - the creation routine itself

TSTrajectoryRegister() may be called multiple times to add several user-defined tses.

TS: Scalable ODE and DAE Solvers, TSTrajectoryRegisterAll()

src/ts/trajectory/interface/traj.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectoryRegister(const char sname[], PetscErrorCode (*function)(TSTrajectory, TS))
```

Example 2 (unknown):
```unknown
TSTrajectoryRegister()
```

Example 3 (unknown):
```unknown
TSTrajectoryRegisterAll()
```

---

## TSTrajectoryReset#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectoryReset/

**Contents:**
- TSTrajectoryReset#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Resets a trajectory context

tj - the TSTrajectory context obtained from TSGetTrajectory()

TS: Scalable ODE and DAE Solvers, TS, TSTrajectory, TSTrajectoryCreate(), TSTrajectorySetUp()

src/ts/trajectory/interface/traj.c

TSTrajectoryReset_Memory() in src/ts/trajectory/impls/memory/trajmemory.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectoryReset(TSTrajectory tj)
```

Example 2 (unknown):
```unknown
TSTrajectory
```

Example 3 (unknown):
```unknown
TSGetTrajectory()
```

Example 4 (unknown):
```unknown
TSTrajectory
```

---

## TSTrajectoryRestoreUpdatedHistoryVecs#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectoryRestoreUpdatedHistoryVecs/

**Contents:**
- TSTrajectoryRestoreUpdatedHistoryVecs#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Restores updated state and time-derivative history vectors obtained with TSTrajectoryGetUpdatedHistoryVecs().

tj - the TSTrajectory context

U - state vector at given time (can be interpolated)

Udot - time-derivative vector at given time (can be interpolated)

TS: Scalable ODE and DAE Solvers, TSTrajectory, TSTrajectoryGetUpdatedHistoryVecs()

src/ts/trajectory/interface/traj.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSTrajectoryGetUpdatedHistoryVecs()
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectoryRestoreUpdatedHistoryVecs(TSTrajectory tj, Vec *U, Vec *Udot)
```

Example 3 (unknown):
```unknown
TSTrajectory
```

Example 4 (unknown):
```unknown
TSTrajectory
```

---

## TSTrajectorySetDirname#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectorySetDirname/

**Contents:**
- TSTrajectorySetDirname#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Specify the name of the directory where TSTrajectory disk checkpoints are stored.

tj - the TSTrajectory context

dirname - the directory name

-ts_trajectory_dirname - set the directory name

The final location of the files is determined by dirname/filetemplate where filetemplate was provided by TSTrajectorySetFiletemplate()

If this is not called TSTrajectory selects a unique new name for the directory

TS: Scalable ODE and DAE Solvers, TSTrajectory, TSTrajectorySetFiletemplate(), TSTrajectorySetUp()

src/ts/trajectory/interface/traj.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSTrajectory
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectorySetDirname(TSTrajectory tj, const char dirname[])
```

Example 3 (unknown):
```unknown
TSTrajectory
```

Example 4 (unknown):
```unknown
TSTrajectorySetFiletemplate()
```

---

## TSTrajectorySetFiletemplate#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectorySetFiletemplate/

**Contents:**
- TSTrajectorySetFiletemplate#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Specify the name template for the files storing TSTrajectory checkpoints.

tj - the TSTrajectory context

filetemplate - the template

-ts_trajectory_file_template - set the file name template

The name template should be of the form, for example filename-%06” PetscInt_FMT “.bin It should not begin with a leading /

The final location of the files is determined by dirname/filetemplate where dirname was provided by TSTrajectorySetDirname(). The %06” PetscInt_FMT “ is replaced by the timestep counter

TS: Scalable ODE and DAE Solvers, TSTrajectory, TSTrajectorySetDirname(), TSTrajectorySetUp()

src/ts/trajectory/interface/traj.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSTrajectory
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectorySetFiletemplate(TSTrajectory tj, const char filetemplate[])
```

Example 3 (unknown):
```unknown
TSTrajectory
```

Example 4 (unknown):
```unknown
TSTrajectorySetDirname()
```

---

## TSTrajectorySetFromOptions#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectorySetFromOptions/

**Contents:**
- TSTrajectorySetFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Sets various TSTrajectory parameters from user options.

tj - the TSTrajectory context obtained from TSGetTrajectory()

-ts_trajectory_type (basic|singlefile|memory|visualization) - how to manage the trajectory

-ts_trajectory_keep_files (true|false) - keep the files generated by the code after the program ends. This is true by default for singlefile and visualization

-ts_trajectory_monitor - print TSTrajectory information

This is not normally called directly by users

TS: Scalable ODE and DAE Solvers, TSTrajectory, TSSetSaveTrajectory(), TSTrajectorySetUp()

src/ts/trajectory/interface/traj.c

TSTrajectorySetFromOptions_Basic() in src/ts/trajectory/impls/basic/trajbasic.c TSTrajectorySetFromOptions_Memory() in src/ts/trajectory/impls/memory/trajmemory.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSTrajectory
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectorySetFromOptions(TSTrajectory tj, TS ts)
```

Example 3 (unknown):
```unknown
TSTrajectory
```

Example 4 (unknown):
```unknown
TSGetTrajectory()
```

---

## TSTrajectorySetKeepFiles#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectorySetKeepFiles/

**Contents:**
- TSTrajectorySetKeepFiles#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Keep the files generated by the TSTrajectory once the program is done

tj - the TSTrajectory context

flg - PETSC_TRUE to save, PETSC_FALSE to disable

-ts_trajectory_keep_files - have it keep the files

By default the TSTrajectory used for adjoint computations, TSTRAJECTORYBASIC, removes the files it generates at the end of the run. This causes the files to be kept.

TS: Scalable ODE and DAE Solvers, TSTrajectoryCreate(), TSTrajectoryDestroy(), TSTrajectorySetUp(), TSTrajectorySetMonitor()

src/ts/trajectory/interface/traj.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSTrajectory
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectorySetKeepFiles(TSTrajectory tj, PetscBool flg)
```

Example 3 (unknown):
```unknown
TSTrajectory
```

Example 4 (unknown):
```unknown
PETSC_FALSE
```

---

## TSTrajectorySetMaxCpsDisk#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectorySetMaxCpsDisk/

**Contents:**
- TSTrajectorySetMaxCpsDisk#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Set maximum number of checkpoints on disk

tj - tstrajectory context

max_cps_disk - maximum number of checkpoints on disk

TS: Scalable ODE and DAE Solvers, TSTrajectory, TSTrajectorySetMaxUnitsDisk(), TSTrajectorySetMaxUnitsRAM()

src/ts/trajectory/impls/memory/trajmemory.c

TSTrajectorySetMaxCpsDisk_Memory() in src/ts/trajectory/impls/memory/trajmemory.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectorySetMaxCpsDisk(TSTrajectory tj, PetscInt max_cps_disk)
```

Example 2 (unknown):
```unknown
TSTrajectory
```

Example 3 (unknown):
```unknown
TSTrajectorySetMaxUnitsDisk()
```

Example 4 (unknown):
```unknown
TSTrajectorySetMaxUnitsRAM()
```

---

## TSTrajectorySetMaxCpsRAM#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectorySetMaxCpsRAM/

**Contents:**
- TSTrajectorySetMaxCpsRAM#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Set maximum number of checkpoints in RAM

tj - tstrajectory context

max_cps_ram - maximum number of checkpoints in RAM

TS: Scalable ODE and DAE Solvers, TSTrajectory, TSTrajectorySetMaxUnitsRAM()

src/ts/trajectory/impls/memory/trajmemory.c

TSTrajectorySetMaxCpsRAM_Memory() in src/ts/trajectory/impls/memory/trajmemory.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectorySetMaxCpsRAM(TSTrajectory tj, PetscInt max_cps_ram)
```

Example 2 (unknown):
```unknown
TSTrajectory
```

Example 3 (unknown):
```unknown
TSTrajectorySetMaxUnitsRAM()
```

---

## TSTrajectorySetMaxUnitsDisk#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectorySetMaxUnitsDisk/

**Contents:**
- TSTrajectorySetMaxUnitsDisk#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Set maximum number of checkpointing units on disk

tj - tstrajectory context

max_units_disk - maximum number of checkpointing units on disk

TS: Scalable ODE and DAE Solvers, TSTrajectory, TSTrajectorySetMaxCpsDisk()

src/ts/trajectory/impls/memory/trajmemory.c

TSTrajectorySetMaxUnitsDisk_Memory() in src/ts/trajectory/impls/memory/trajmemory.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectorySetMaxUnitsDisk(TSTrajectory tj, PetscInt max_units_disk)
```

Example 2 (unknown):
```unknown
TSTrajectory
```

Example 3 (unknown):
```unknown
TSTrajectorySetMaxCpsDisk()
```

---

## TSTrajectorySetMaxUnitsRAM#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectorySetMaxUnitsRAM/

**Contents:**
- TSTrajectorySetMaxUnitsRAM#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Set maximum number of checkpointing units in RAM

tj - tstrajectory context

max_units_ram - maximum number of checkpointing units in RAM

TS: Scalable ODE and DAE Solvers, TSTrajectory, TSTrajectorySetMaxCpsRAM()

src/ts/trajectory/impls/memory/trajmemory.c

TSTrajectorySetMaxUnitsRAM_Memory() in src/ts/trajectory/impls/memory/trajmemory.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectorySetMaxUnitsRAM(TSTrajectory tj, PetscInt max_units_ram)
```

Example 2 (unknown):
```unknown
TSTrajectory
```

Example 3 (unknown):
```unknown
TSTrajectorySetMaxCpsRAM()
```

---

## TSTrajectorySetMonitor#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectorySetMonitor/

**Contents:**
- TSTrajectorySetMonitor#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Monitor the schedules generated by the TSTrajectory checkpointing controller

tj - the TSTrajectory context

flg - PETSC_TRUE to active a monitor, PETSC_FALSE to disable

-ts_trajectory_monitor - print TSTrajectory information

TS: Scalable ODE and DAE Solvers, TSTrajectory, TSTrajectoryCreate(), TSTrajectoryDestroy(), TSTrajectorySetUp()

src/ts/trajectory/interface/traj.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSTrajectory
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectorySetMonitor(TSTrajectory tj, PetscBool flg)
```

Example 3 (unknown):
```unknown
TSTrajectory
```

Example 4 (unknown):
```unknown
PETSC_FALSE
```

---

## TSTrajectorySetSolutionOnly#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectorySetSolutionOnly/

**Contents:**
- TSTrajectorySetSolutionOnly#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Tells the trajectory to store just the solution, and not any intermediate stage information

tj - the TSTrajectory context obtained with TSGetTrajectory()

solution_only - the boolean flag

TS: Scalable ODE and DAE Solvers, TSTrajectory, TSSetSaveTrajectory(), TSTrajectoryCreate(), TSTrajectoryDestroy(), TSTrajectoryGetSolutionOnly()

src/ts/trajectory/interface/traj.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectorySetSolutionOnly(TSTrajectory tj, PetscBool solution_only)
```

Example 2 (unknown):
```unknown
TSTrajectory
```

Example 3 (unknown):
```unknown
TSGetTrajectory()
```

Example 4 (unknown):
```unknown
TSTrajectory
```

---

## TSTrajectorySetTransform#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectorySetTransform/

**Contents:**
- TSTrajectorySetTransform#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Solution vector will be transformed by provided function before being saved to disk

tj - the TSTrajectory context

transform - the transform function

destroy - function to destroy the optional context

tctx - optional context used by transform function

TS: Scalable ODE and DAE Solvers, TSTrajectorySetVariableNames(), TSTrajectory, TSMonitorLGSetTransform()

src/ts/trajectory/interface/traj.c

src/ts/tutorials/extchem.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (csharp):
```csharp
#include "petscts.h"  
PetscErrorCode TSTrajectorySetTransform(TSTrajectory tj, PetscErrorCode (*transform)(void *, Vec, Vec *), PetscCtxDestroyFn *destroy, void *tctx)
```

Example 2 (unknown):
```unknown
TSTrajectory
```

Example 3 (unknown):
```unknown
TSTrajectorySetVariableNames()
```

Example 4 (unknown):
```unknown
TSTrajectory
```

---

## TSTrajectorySetType#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectorySetType/

**Contents:**
- TSTrajectorySetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Developer Notes#
- See Also#
- Level#
- Location#

Sets the storage method to be used as in a trajectory

tj - the TSTrajectory context

type - a known method

-ts_trajectory_type (basic|singlefile|memory|visualization) - Sets the trajectory type

Why does this option require access to the TS

TS: Scalable ODE and DAE Solvers, TSTrajectory, TSTrajectoryType, TS, TSTrajectoryCreate(), TSTrajectorySetFromOptions(), TSTrajectoryDestroy(), TSTrajectoryGetType()

src/ts/trajectory/interface/traj.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectorySetType(TSTrajectory tj, TS ts, TSTrajectoryType type)
```

Example 2 (unknown):
```unknown
TSTrajectory
```

Example 3 (unknown):
```unknown
TSTrajectory
```

Example 4 (unknown):
```unknown
TSTrajectoryType
```

---

## TSTrajectorySetUp#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectorySetUp/

**Contents:**
- TSTrajectorySetUp#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Sets up the internal data structures, e.g. stacks, for the later use of a TS TSTrajectory.

tj - the TSTrajectory context

ts - the TS context obtained from TSCreate()

TS: Scalable ODE and DAE Solvers, TSTrajectory, TSSetSaveTrajectory(), TSTrajectoryCreate(), TSTrajectoryDestroy()

src/ts/trajectory/interface/traj.c

TSTrajectorySetUp_Basic() in src/ts/trajectory/impls/basic/trajbasic.c TSTrajectorySetUp_Memory() in src/ts/trajectory/impls/memory/trajmemory.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSTrajectory
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectorySetUp(TSTrajectory tj, TS ts)
```

Example 3 (unknown):
```unknown
TSTrajectory
```

Example 4 (unknown):
```unknown
TSTrajectory
```

---

## TSTrajectorySetUseHistory#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectorySetUseHistory/

**Contents:**
- TSTrajectorySetUseHistory#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Use TSHistory in TSTrajectory

tj - the TSTrajectory context

flg - PETSC_TRUE to save, PETSC_FALSE to disable

-ts_trajectory_use_history - have it use TSHistory

TS: Scalable ODE and DAE Solvers, TSTrajectory, TSTrajectoryCreate(), TSTrajectoryDestroy(), TSTrajectorySetUp()

src/ts/trajectory/interface/traj.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSTrajectory
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectorySetUseHistory(TSTrajectory tj, PetscBool flg)
```

Example 3 (unknown):
```unknown
TSTrajectory
```

Example 4 (unknown):
```unknown
PETSC_FALSE
```

---

## TSTrajectorySetVariableNames#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectorySetVariableNames/

**Contents:**
- TSTrajectorySetVariableNames#
- Synopsis#
- Input Parameters#
- Fortran Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the name of each component in the solution vector so that it may be saved with the trajectory

ctx - the trajectory context

names - the names of the components, final string must be NULL

Fortran interface is not possible because of the string array argument

TS: Scalable ODE and DAE Solvers, TSTrajectory, TSGetTrajectory()

src/ts/trajectory/interface/traj.c

src/ts/tutorials/extchem.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectorySetVariableNames(TSTrajectory ctx, const char *const *names)
```

Example 2 (unknown):
```unknown
TSTrajectory
```

Example 3 (unknown):
```unknown
TSGetTrajectory()
```

---

## TSTrajectorySet#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectorySet/

**Contents:**
- TSTrajectorySet#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Sets a vector of state in the trajectory object

tj - the trajectory object

ts - the time stepper object (optional)

stepnum - the step number

time - the current time

X - the current solution

Usually one does not call this routine, it is called automatically during TSSolve()

TS: Scalable ODE and DAE Solvers, TSTrajectorySetUp(), TSTrajectoryDestroy(), TSTrajectorySetType(), TSTrajectorySetVariableNames(), TSGetTrajectory(), TSTrajectoryGet(), TSTrajectoryGetVecs()

src/ts/trajectory/interface/traj.c

TSTrajectorySet_Basic() in src/ts/trajectory/impls/basic/trajbasic.c TSTrajectorySet_Memory() in src/ts/trajectory/impls/memory/trajmemory.c TSTrajectorySet_Singlefile() in src/ts/trajectory/impls/singlefile/singlefile.c TSTrajectorySet_Visualization() in src/ts/trajectory/impls/visualization/trajvisualization.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectorySet(TSTrajectory tj, TS ts, PetscInt stepnum, PetscReal time, Vec X)
```

Example 2 (unknown):
```unknown
TSTrajectorySetUp()
```

Example 3 (unknown):
```unknown
TSTrajectoryDestroy()
```

Example 4 (unknown):
```unknown
TSTrajectorySetType()
```

---

## TSTRAJECTORYSINGLEFILE#

**URL:** https://petsc.org/release/manualpages/TS/TSTRAJECTORYSINGLEFILE/

**Contents:**
- TSTRAJECTORYSINGLEFILE#
- See Also#
- Level#
- Location#

Stores all solutions of the ODE/ADE into a single file followed by each timestep. Does not save the intermediate stages in a multistage method

TS: Scalable ODE and DAE Solvers, TSTrajectoryCreate(), TS, TSTrajectorySetType(), TSTrajectoryType, TSTrajectory

src/ts/trajectory/impls/singlefile/singlefile.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSTrajectoryCreate()
```

Example 2 (unknown):
```unknown
TSTrajectorySetType()
```

Example 3 (unknown):
```unknown
TSTrajectoryType
```

Example 4 (unknown):
```unknown
TSTrajectory
```

---

## TSTrajectoryType#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectoryType/

**Contents:**
- TSTrajectoryType#
- Synopsis#
- See Also#
- Level#
- Location#

String with the name of a PETSc TS trajectory storage method

TS: Scalable ODE and DAE Solvers, TS, TSSetSaveTrajectory(), TSTrajectoryCreate(), TSTrajectoryDestroy()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h> 
typedef const char *TSTrajectoryType;
#define TSTRAJECTORYBASIC         "basic"
#define TSTRAJECTORYSINGLEFILE    "singlefile"
#define TSTRAJECTORYMEMORY        "memory"
#define TSTRAJECTORYVISUALIZATION "visualization"
```

Example 2 (unknown):
```unknown
TSSetSaveTrajectory()
```

Example 3 (unknown):
```unknown
TSTrajectoryCreate()
```

Example 4 (unknown):
```unknown
TSTrajectoryDestroy()
```

---

## TSTrajectoryViewFromOptions#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectoryViewFromOptions/

**Contents:**
- TSTrajectoryViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

View a TSTrajectory based on values in the options database

A - the TSTrajectory context

obj - Optional object that provides prefix used for option name

name - command line option

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

TS: Scalable ODE and DAE Solvers, TSTrajectory, TSTrajectoryView, PetscObjectViewFromOptions(), TSTrajectoryCreate()

src/ts/trajectory/interface/traj.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSTrajectory
```

Example 2 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectoryViewFromOptions(TSTrajectory A, PetscObject obj, const char name[])
```

Example 3 (unknown):
```unknown
TSTrajectory
```

Example 4 (unknown):
```unknown
PetscObjectViewFromOptions()
```

---

## TSTrajectoryView#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectoryView/

**Contents:**
- TSTrajectoryView#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Prints information about the trajectory object

tj - the TSTrajectory context obtained from TSTrajectoryCreate()

viewer - visualization context

-ts_trajectory_view - calls TSTrajectoryView() at end of TSAdjointStep()

The available visualization contexts include

PETSC_VIEWER_STDOUT_SELF - standard output (default)

PETSC_VIEWER_STDOUT_WORLD - synchronized standard output where only the first processor opens the file. All other processors send their data to the first processor to print.

The user can open an alternative visualization context with PetscViewerASCIIOpen() - output to a specified file.

TS: Scalable ODE and DAE Solvers, TS, TSTrajectory, PetscViewer, PetscViewerASCIIOpen()

src/ts/trajectory/interface/traj.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSTrajectoryView(TSTrajectory tj, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
TSTrajectory
```

Example 3 (unknown):
```unknown
TSTrajectoryCreate()
```

Example 4 (unknown):
```unknown
TSTrajectoryView()
```

---

## TSTrajectory#

**URL:** https://petsc.org/release/manualpages/TS/TSTrajectory/

**Contents:**
- TSTrajectory#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Abstract PETSc object that stores the trajectory (solution of ODE/DAE at each time step)

TS: Scalable ODE and DAE Solvers, TS, TSSetSaveTrajectory(), TSTrajectoryCreate(), TSTrajectorySetType(), TSTrajectoryDestroy(), TSTrajectoryReset()

src/ts/tutorials/ex41.c src/ts/tutorials/extchem.c src/ts/tutorials/ex40.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c

_p_TSTrajectory in include/petsc/private/tsimpl.h TSTrajectory_Basic in src/ts/trajectory/impls/basic/trajbasic.c TSTrajectory_Singlefile in src/ts/trajectory/impls/singlefile/singlefile.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (c):
```c
#include <petscts.h> 
typedef struct _p_TSTrajectory *TSTrajectory;
```

Example 2 (unknown):
```unknown
TSSetSaveTrajectory()
```

Example 3 (unknown):
```unknown
TSTrajectoryCreate()
```

Example 4 (unknown):
```unknown
TSTrajectorySetType()
```

---

## TSTransientVariableFn#

**URL:** https://petsc.org/release/manualpages/TS/TSTransientVariableFn/

**Contents:**
- TSTransientVariableFn#
- Synopsis#
- Calling Sequence#
- Note#
- See Also#
- Level#
- Location#

A prototype of a function to transform from state to transient variables that would be passed to TSSetTransientVariable()

ts - timestep context

p - input vector (primitive form)

c - output vector, transient variables (conservative form)

ctx - [optional] user-defined function context

The deprecated TSTransientVariable still works as a replacement for TSTransientVariableFn *.

TS: Scalable ODE and DAE Solvers, TS, TSSetTransientVariable(), DMTSSetTransientVariable()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetTransientVariable()
```

Example 2 (cpp):
```cpp
#include <petscts.h> 
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode TSTransientVariableFn(TS ts, Vec p, Vec c, PetscCtx ctx);
```

Example 3 (unknown):
```unknown
TSTransientVariable
```

Example 4 (unknown):
```unknown
TSTransientVariableFn
```

---

## TSType#

**URL:** https://petsc.org/release/manualpages/TS/TSType/

**Contents:**
- TSType#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#
- Examples#

String with the name of a PETSc TS method. These are all the time/ODE integrators that PETSc provides.

Use TSSetType() or the options database key -ts_type to set the ODE integrator method to use with a given TS object

Summary of Time Integrators Available In PETSc, TS: Scalable ODE and DAE Solvers, TSSetType(), TS, TSRegister()

src/ts/tutorials/ex31.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h> 
typedef const char *TSType;
#define TSEULER           "euler"
#define TSBEULER          "beuler"
#define TSBASICSYMPLECTIC "basicsymplectic"
#define TSPSEUDO          "pseudo"
#define TSCN              "cn"
#define TSSUNDIALS        "sundials"
#define TSRK              "rk"
#define TSPYTHON          "python"
#define TSTHETA           "theta"
#define TSALPHA           "alpha"
#define TSALPHA2          "alpha2"
#define TSGLLE            "glle"
#define TSGLEE            "glee"
#define TSSSP             "ssp"
#define TSARKIMEX         "arkimex"
#define TSROSW            "rosw"
#define TSEIMEX           "eimex"
#define TSMIMEX           "mimex"
#define TSBDF             "bdf"
#define TSRADAU5          "radau5"
#define TSMPRK            "mprk"
#define TSDISCGRAD        "discgrad"
#define TSIRK             "irk"
#define TSDIRK            "dirk"
```

Example 2 (unknown):
```unknown
TSSetType()
```

Example 3 (unknown):
```unknown
TSSetType()
```

Example 4 (unknown):
```unknown
TSRegister()
```

---

## TSViewFromOptions#

**URL:** https://petsc.org/release/manualpages/TS/TSViewFromOptions/

**Contents:**
- TSViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

View a TS based on values in the options database

obj - Optional object that provides the prefix for the options database keys

name - command line option string to be passed by user

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

TS: Scalable ODE and DAE Solvers, TS, TSView, PetscObjectViewFromOptions(), TSCreate()

src/ts/interface/ts.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSViewFromOptions(TS ts, PetscObject obj, const char name[])
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

## TSView#

**URL:** https://petsc.org/release/manualpages/TS/TSView/

**Contents:**
- TSView#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Prints the TS data structure.

ts - the TS context obtained from TSCreate()

viewer - visualization context

-ts_view - calls TSView() at end of TSStep()

The available visualization contexts include

PETSC_VIEWER_STDOUT_SELF - standard output (default)

PETSC_VIEWER_STDOUT_WORLD - synchronized standard output where only the first processor opens the file. All other processors send their data to the first processor to print.

The user can open an alternative visualization context with PetscViewerASCIIOpen() - output to a specified file.

In the debugger you can do call TSView(ts,0) to display the TS solver. (The same holds for any PETSc object viewer).

The “initial time step” displayed is the default time step from TSCreate() or that set with TSSetTimeStep() or -ts_time_step

TS: Scalable ODE and DAE Solvers, TS, PetscViewer, PetscViewerASCIIOpen()

src/ts/interface/ts.c

src/ts/tutorials/ex3.c src/ts/tutorials/ex28.c src/ts/tutorials/ex6.c src/ts/tutorials/ex5.c

TSView_ARKIMEX() in src/ts/impls/arkimex/arkimex.c TSView_BDF() in src/ts/impls/bdf/bdf.c TSView_EIMEX() in src/ts/impls/eimex/eimex.c TSView_Euler() in src/ts/impls/explicit/euler/euler.c TSView_RK() in src/ts/impls/explicit/rk/rk.c TSView_SSP() in src/ts/impls/explicit/ssp/ssp.c TSView_GLEE() in src/ts/impls/glee/glee.c TSView_Alpha() in src/ts/impls/implicit/alpha/alpha1.c TSView_Alpha() in src/ts/impls/implicit/alpha/alpha2.c TSView_DiscGrad() in src/ts/impls/implicit/discgrad/tsdiscgrad.c TSView_GLLE() in src/ts/impls/implicit/glle/glle.c TSView_IRK() in src/ts/impls/implicit/irk/irk.c TSView_Sundials() in src/ts/impls/implicit/sundials/sundials.c TSView_Theta() in src/ts/impls/implicit/theta/theta.c TSView_BEuler() in src/ts/impls/implicit/theta/theta.c TSView_CN() in src/ts/impls/implicit/theta/theta.c TSView_Mimex() in src/ts/impls/mimex/mimex.c TSView_MPRK() in src/ts/impls/multirate/mprk.c TSView_Pseudo() in src/ts/impls/pseudo/posindep.c TSView_RosW() in src/ts/impls/rosw/rosw.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSView(TS ts, PetscViewer viewer)
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

## TSVISetVariableBounds#

**URL:** https://petsc.org/release/manualpages/TS/TSVISetVariableBounds/

**Contents:**
- TSVISetVariableBounds#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the lower and upper bounds for the solution vector. xl <= x <= xu

If this routine is not called then the lower and upper bounds are set to PETSC_NINFINITY and PETSC_INFINITY respectively during SNESSetUp().

TS: Scalable ODE and DAE Solvers, TS

src/ts/interface/ts.c

src/ts/tutorials/ex21.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscts.h"  
PetscErrorCode TSVISetVariableBounds(TS ts, Vec xl, Vec xu)
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

## TS_CONVERGED_EVENT#

**URL:** https://petsc.org/release/manualpages/TS/TS_CONVERGED_EVENT/

**Contents:**
- TS_CONVERGED_EVENT#
- See Also#
- Level#
- Location#

user requested termination on event detection

TS: Scalable ODE and DAE Solvers, TS, TSSolve(), TSGetConvergedReason(), TSSetConvergedReason()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGetConvergedReason()
```

Example 2 (unknown):
```unknown
TSSetConvergedReason()
```

---

## TS_CONVERGED_ITERATING#

**URL:** https://petsc.org/release/manualpages/TS/TS_CONVERGED_ITERATING/

**Contents:**
- TS_CONVERGED_ITERATING#
- See Also#
- Level#
- Location#

this only occurs if TSGetConvergedReason() is called during the TSSolve()

TS: Scalable ODE and DAE Solvers, TS, TSSolve(), TSGetConvergedReason(), TSGetAdapt()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGetConvergedReason()
```

Example 2 (unknown):
```unknown
TSGetConvergedReason()
```

Example 3 (unknown):
```unknown
TSGetAdapt()
```

---

## TS_CONVERGED_ITS#

**URL:** https://petsc.org/release/manualpages/TS/TS_CONVERGED_ITS/

**Contents:**
- TS_CONVERGED_ITS#
- See Also#
- Level#
- Location#
- Examples#

the maximum number of iterations (time-steps) was reached prior to the final time

TS: Scalable ODE and DAE Solvers, TS, TSSolve(), TSGetConvergedReason(), TSGetAdapt(), TSSetMaxSteps(), TSGetMaxSteps()

src/ts/tutorials/ex48.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGetConvergedReason()
```

Example 2 (unknown):
```unknown
TSGetAdapt()
```

Example 3 (unknown):
```unknown
TSSetMaxSteps()
```

Example 4 (unknown):
```unknown
TSGetMaxSteps()
```

---

## TS_CONVERGED_PSEUDO_FATOL#

**URL:** https://petsc.org/release/manualpages/TS/TS_CONVERGED_PSEUDO_FATOL/

**Contents:**
- TS_CONVERGED_PSEUDO_FATOL#
- Options Database Key#
- See Also#
- Level#
- Location#

stops when function norm decreases below a set amount, used only for TSPSEUDO

-ts_pseudo_fatol atol - use specified atol

TS: Scalable ODE and DAE Solvers, TS, TSSolve(), TSGetConvergedReason(), TSSetConvergedReason(), TS_CONVERGED_PSEUDO_FRTOL

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGetConvergedReason()
```

Example 2 (unknown):
```unknown
TSSetConvergedReason()
```

Example 3 (unknown):
```unknown
TS_CONVERGED_PSEUDO_FRTOL
```

---

## TS_CONVERGED_PSEUDO_FRTOL#

**URL:** https://petsc.org/release/manualpages/TS/TS_CONVERGED_PSEUDO_FRTOL/

**Contents:**
- TS_CONVERGED_PSEUDO_FRTOL#
- Options Database Key#
- See Also#
- Level#
- Location#

stops when function norm decreased by a set amount, used only for TSPSEUDO

-ts_pseudo_frtol rtol - use specified rtol

TS: Scalable ODE and DAE Solvers, TS, TSSolve(), TSGetConvergedReason(), TSSetConvergedReason(), TS_CONVERGED_PSEUDO_FATOL

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGetConvergedReason()
```

Example 2 (unknown):
```unknown
TSSetConvergedReason()
```

Example 3 (unknown):
```unknown
TS_CONVERGED_PSEUDO_FATOL
```

---

## TS_CONVERGED_TIME#

**URL:** https://petsc.org/release/manualpages/TS/TS_CONVERGED_TIME/

**Contents:**
- TS_CONVERGED_TIME#
- See Also#
- Level#
- Location#
- Examples#

the final time was reached

TS: Scalable ODE and DAE Solvers, TS, TSSolve(), TSGetConvergedReason(), TSGetAdapt(), TSSetMaxTime(), TSGetMaxTime(), TSGetSolveTime()

src/ts/tutorials/ex48.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGetConvergedReason()
```

Example 2 (unknown):
```unknown
TSGetAdapt()
```

Example 3 (unknown):
```unknown
TSSetMaxTime()
```

Example 4 (unknown):
```unknown
TSGetMaxTime()
```

---

## TS_CONVERGED_USER#

**URL:** https://petsc.org/release/manualpages/TS/TS_CONVERGED_USER/

**Contents:**
- TS_CONVERGED_USER#
- See Also#
- Level#
- Location#
- Examples#

user requested termination

TS: Scalable ODE and DAE Solvers, TS, TSSolve(), TSGetConvergedReason(), TSSetConvergedReason()

src/ts/tutorials/ex44.c src/ts/tutorials/ex40.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSGetConvergedReason()
```

Example 2 (unknown):
```unknown
TSSetConvergedReason()
```

---

## TS_DIVERGED_NONLINEAR_SOLVE#

**URL:** https://petsc.org/release/manualpages/TS/TS_DIVERGED_NONLINEAR_SOLVE/

**Contents:**
- TS_DIVERGED_NONLINEAR_SOLVE#
- Note#
- See Also#
- Level#
- Location#

too many nonlinear solves failed

See TSSetMaxSNESFailures() for how to allow more nonlinear solver failures.

TS: Scalable ODE and DAE Solvers, TS, TSSolve(), TSGetConvergedReason(), TSGetAdapt(), TSGetSNES(), SNESGetConvergedReason(), TSSetMaxSNESFailures()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetMaxSNESFailures()
```

Example 2 (unknown):
```unknown
TSGetConvergedReason()
```

Example 3 (unknown):
```unknown
TSGetAdapt()
```

Example 4 (unknown):
```unknown
TSGetSNES()
```

---

## TS_DIVERGED_STEP_REJECTED#

**URL:** https://petsc.org/release/manualpages/TS/TS_DIVERGED_STEP_REJECTED/

**Contents:**
- TS_DIVERGED_STEP_REJECTED#
- Notes#
- See Also#
- Level#
- Location#

too many steps were rejected

See TSSetMaxStepRejections() for how to allow more step rejections.

TS: Scalable ODE and DAE Solvers, TS, TSSolve(), TSGetConvergedReason(), TSGetAdapt(), TSSetMaxStepRejections()

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TSSetMaxStepRejections()
```

Example 2 (unknown):
```unknown
TSGetConvergedReason()
```

Example 3 (unknown):
```unknown
TSGetAdapt()
```

Example 4 (unknown):
```unknown
TSSetMaxStepRejections()
```

---

## TS#

**URL:** https://petsc.org/release/manualpages/TS/TS/

**Contents:**
- TS#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Abstract PETSc object that manages integrating an ODE.

Summary of Time Integrators Available In PETSc, TS: Scalable ODE and DAE Solvers, TSCreate(), TSSetType(), TSType, SNES, KSP, PC, TSDestroy()

src/ml/da/tutorials/ex3.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/tao/unconstrained/tutorials/burgers_spectral.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ml/da/tutorials/ex1.c src/snes/tutorials/ex30.c src/ml/da/tutorials/ex4.c src/ml/da/tutorials/ex2.c

_p_TS in include/petsc/private/tsimpl.h TS_ARKIMEX in src/ts/impls/arkimex/arkimex.h TS_BDF in src/ts/impls/bdf/bdf.c TS_EIMEX in src/ts/impls/eimex/eimex.c TS_Euler in src/ts/impls/explicit/euler/euler.c TS_RK in src/ts/impls/explicit/rk/rk.h TS_SSP in src/ts/impls/explicit/ssp/ssp.c TS_GLEE in src/ts/impls/glee/glee.c TS_Alpha in src/ts/impls/implicit/alpha/alpha1.c TS_Alpha in src/ts/impls/implicit/alpha/alpha2.c TS_DiscGrad in src/ts/impls/implicit/discgrad/tsdiscgrad.c TS_GLLE in src/ts/impls/implicit/glle/glle.h TS_IRK in src/ts/impls/implicit/irk/irk.c TS_Sundials in src/ts/impls/implicit/sundials/sundials.h TS_Theta in src/ts/impls/implicit/theta/theta.c TS_Mimex in src/ts/impls/mimex/mimex.c TS_MPRK in src/ts/impls/multirate/mprk.c TS_Pseudo in src/ts/impls/pseudo/posindep.c TS_RosW in src/ts/impls/rosw/rosw.c TS_BasicSymplectic in src/ts/impls/symplectic/basicsymplectic/basicsymplectic.c

Index of all TS routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (c):
```c
#include <petscts.h> 
typedef struct _p_TS *TS;
```

Example 2 (unknown):
```unknown
TSSetType()
```

Example 3 (unknown):
```unknown
TSDestroy()
```

---

## TS: Scalable ODE and DAE Solvers#

**URL:** https://petsc.org/release/manual/ts/

**Contents:**
- TS: Scalable ODE and DAE Solvers#
- Basic TS Options#
- DAE Formulations#
  - Hessenberg Index-1 DAE#
  - Hessenberg Index-2 DAE#
- Using Implicit-Explicit (IMEX) Methods#
- IMEX Methods for fast-slow systems#
- GLEE methods#
- Using fully implicit methods#
- Using the Explicit Runge-Kutta timestepper with variable timesteps#

The TS library provides a framework for the scalable solution of ODEs and DAEs arising from the discretization of time-dependent PDEs.

Simple Example: Consider the PDE

discretized with centered finite differences in space yielding the semi-discrete equation

or with piecewise linear finite elements approximation in space \(u(x,t) \doteq \sum_i \xi_i(t) \phi_i(x)\) yielding the semi-discrete equation

Now applying the backward Euler method results in

\(A\) is the stiffness matrix, and \(B\) is the identity for finite differences or the mass matrix for the finite element method.

The PETSc interface for solving time dependent problems assumes the problem is written in the form

In general, this is a differential algebraic equation (DAE) [1]. For ODE with nontrivial mass matrices such as arise in FEM, the implicit/DAE interface significantly reduces overhead to prepare the system for algebraic solvers (SNES/KSP) by having the user assemble the correctly shifted matrix. Therefore this interface is also useful for ODE systems.

To solve an ODE or DAE one uses:

Function \(F(t,u,\dot{u})\)

The vector R is an optional location to store the residual. The arguments to the function f() are the timestep context, current time, input state \(u\), input time derivative \(\dot{u}\), and the (optional) user-provided context funP. If \(F(t,u,\dot{u}) = \dot{u}\) then one need not call this function.

Function \(G(t,u)\), if it is nonzero, is provided with the function

\(\sigma F_{\dot{u}}(t^n,u^n,\dot{u}^n) + F_u(t^n,u^n,\dot{u}^n)\)

If using a fully implicit or semi-implicit (IMEX) method one also can provide an appropriate (approximate) Jacobian matrix of

The arguments for the function fjac() are the timestep context, current time, input state \(u\), input derivative \(\dot{u}\), input shift \(\sigma\), matrix \(A\), matrix used to construct the preconditioner \(B\), and the (optional) user-provided context jacP.

The Jacobian needed for the nonlinear system is, by the chain rule,

For any ODE integration method the approximation of \(\dot{u}\) is linear in \(u^n\) hence \(\frac{\partial \dot{u}}{\partial u}|_{u^n} = \sigma\), where the shift \(\sigma\) depends on the ODE integrator and time step but not on the function being integrated. Thus

This explains why the user provide Jacobian is in the given form for all integration methods. An equivalent way to derive the formula is to note that

where \(w\) is some linear combination of previous time solutions of \(u\) so that

again by the chain rule.

For example, consider backward Euler’s method applied to the ODE \(F(t, u, \dot{u}) = \dot{u} - f(t, u)\) with \(\dot{u} = (u^n - u^{n-1})/\delta t\) and \(\frac{\partial \dot{u}}{\partial u}|_{u^n} = 1/\delta t\) resulting in

But \(F_{\dot{u}} = 1\), in this special case, resulting in the expected Jacobian \(I/\delta t - f_u(t,u^n)\).

If using a fully implicit method and the function

is provided, one also can provide an appropriate (approximate) Jacobian matrix of

The arguments for the function fjac() are the timestep context, current time, input state \(u\), matrix \(A\), matrix used to construct the preconditioner \(B\), and the (optional) user-provided context jacP.

Providing appropriate \(F()\) and \(G()\) for your problem allows for the easy runtime switching between explicit, semi-implicit (IMEX), and fully implicit methods.

The user first creates a TS object with the command

The TSProblemType is one of TS_LINEAR or TS_NONLINEAR.

To set up TS for solving an ODE, one must set the “initial conditions” for the ODE with

One can set the solution method with the routine

Some of the currently supported types are TSEULER, TSRK (Runge-Kutta), TSBEULER, TSCN (Crank-Nicolson), TSTHETA, TSGLLE (generalized linear), and TSPSEUDO. They can also be set with the options database option -ts_type euler, rk, beuler, cn, theta, gl, pseudo, sundials, eimex, arkimex, rosw. A list of available methods is given in Summary of Time Integrators Available In PETSc.

Set the initial time with the command

One can change the timestep with the command

can determine the current timestep with the routine

Here, “current” refers to the timestep being used to attempt to promote the solution form \(u^n\) to \(u^{n+1}.\)

One sets the total number of timesteps to run or the total time to run (whatever is first) with the commands

and determines the behavior near the final time with

where eftopt is one of TS_EXACTFINALTIME_STEPOVER,TS_EXACTFINALTIME_INTERPOLATE, or TS_EXACTFINALTIME_MATCHSTEP. One performs the requested number of time steps with

The solve call implicitly sets up the timestep context; this can be done explicitly with

One destroys the context with

In place of TSSolve(), a single step can be taken using

You can find a discussion of DAEs in [AP98] or Scholarpedia. In PETSc, TS deals with the semi-discrete form of the equations, so that space has already been discretized. If the DAE depends explicitly on the coordinate \(x\), then this will just appear as any other data for the equation, not as an explicit argument. Thus we have

In this form, only fully implicit solvers are appropriate. However, specialized solvers for restricted forms of DAE are supported by PETSc. Below we consider an ODE which is augmented with algebraic constraints on the variables.

This is a Semi-Explicit Index-1 DAE which has the form

where \(z\) is a new constraint variable, and the Jacobian \(\frac{dh}{dz}\) is non-singular everywhere. We have suppressed the \(x\) dependence since it plays no role here. Using the non-singularity of the Jacobian and the Implicit Function Theorem, we can solve for \(z\) in terms of \(u\). This means we could, in principle, plug \(z(u)\) into the first equation to obtain a simple ODE, even if this is not the numerical process we use. Below we show that this type of DAE can be used with IMEX schemes.

This DAE has the form

Notice that the constraint equation \(h\) is not a function of the constraint variable \(z\). This means that we cannot naively invert as we did in the index-1 case. Our strategy will be to convert this into an index-1 DAE using a time derivative, which loosely corresponds to the idea of an index being the number of derivatives necessary to get back to an ODE. If we differentiate the constraint equation with respect to time, we can use the ODE to simplify it,

If the Jacobian \(\frac{dh}{du} \frac{df}{dz}\) is non-singular, then we have precisely a semi-explicit index-1 DAE, and we can once again use the PETSc IMEX tools to solve it. A common example of an index-2 DAE is the incompressible Navier-Stokes equations, since the continuity equation \(\nabla\cdot u = 0\) does not involve the pressure. Using PETSc IMEX with the above conversion then corresponds to the Segregated Runge-Kutta method applied to this equation [ColomesB16].

For “stiff” problems or those with multiple time scales \(F()\) will be treated implicitly using a method suitable for stiff problems and \(G()\) will be treated explicitly when using an IMEX method like TSARKIMEX. \(F()\) is typically linear or weakly nonlinear while \(G()\) may have very strong nonlinearities such as arise in non-oscillatory methods for hyperbolic PDE. The user provides three pieces of information, the APIs for which have been described above.

“Slow” part \(G(t,u)\) using TSSetRHSFunction().

“Stiff” part \(F(t,u,\dot u)\) using TSSetIFunction().

Jacobian \(F_u + \sigma F_{\dot u}\) using TSSetIJacobian().

The user needs to set TSSetEquationType() to TS_EQ_IMPLICIT or higher if the problem is implicit; e.g., \(F(t,u,\dot u) = M \dot u - f(t,u)\), where \(M\) is not the identity matrix:

the problem is an implicit ODE (defined implicitly through TSSetIFunction()) or

a DAE is being solved.

An IMEX problem representation can be made implicit by setting TSARKIMEXSetFullyImplicit(). Note that multilevel preconditioners (e.g. PCMG), won’t work in the fully implicit case; the same holds true for any other TS type requiring a fully implicit formulation in case both Jacobians are specified.

In PETSc, DAEs and ODEs are formulated as \(F(t,u,\dot{u})=G(t,u)\), where \(F()\) is meant to be integrated implicitly and \(G()\) explicitly. An IMEX formulation such as \(M\dot{u}=f(t,u)+g(t,u)\) requires the user to provide \(M^{-1} g(t,u)\) or solve \(g(t,u) - M x=0\) in place of \(G(t,u)\). General cases such as \(F(t,u,\dot{u})=G(t,u)\) are not amenable to IMEX Runge-Kutta, but can be solved by using fully implicit methods. Some use-case examples for TSARKIMEX are listed in Table 13 and a list of methods with a summary of their properties is given in IMEX Runge-Kutta schemes.

\(\begin{aligned}F(t,u,\dot{u}) &= \dot{u} \\ G(t,u) &= g(t,u)\end{aligned}\)

\(M \dot{u} = g(t,u)\)

nonstiff ODE with mass matrix

\(\begin{aligned}F(t,u,\dot{u}) &= \dot{u} \\ G(t,u) &= M^{-1} g(t,u)\end{aligned}\)

\(\begin{aligned}F(t,u,\dot{u}) &= \dot{u} - f(t,u) \\ G(t,u) &= 0\end{aligned}\)

\(M \dot{u} = f(t,u)\)

stiff ODE with mass matrix

\(\begin{aligned}F(t,u,\dot{u}) &= M \dot{u} - f(t,u) \\ G(t,u) &= 0\end{aligned}\)

\(\dot{u} = f(t,u) + g(t,u)\)

\(\begin{aligned}F(t,u,\dot{u}) &= \dot{u} - f(t,u) \\ G(t,u) &= g(t,u)\end{aligned}\)

\(M \dot{u} = f(t,u) + g(t,u)\)

stiff-nonstiff ODE with mass matrix

\(\begin{aligned}F(t,u,\dot{u}) &= M\dot{u} - f(t,u) \\ G(t,u) &= M^{-1} g(t,u)\end{aligned}\)

\(\begin{aligned}\dot{u} &= f(t,u,z) + g(t,u,z)\\0 &= h(t,y,z)\end{aligned}\)

semi-explicit index-1 DAE

\(\begin{aligned}F(t,u,\dot{u}) &= \begin{pmatrix}\dot{u} - f(t,u,z)\\h(t, u, z)\end{pmatrix}\\G(t,u) &= g(t,u)\end{aligned}\)

fully implicit ODE/DAE

\(\begin{aligned}F(t,u,\dot{u}) &= f(t,u,\dot{u})\\G(t,u) &= 0\end{aligned}\); the user needs to set TSSetEquationType() to TS_EQ_IMPLICIT or higher

Table 14 lists of the currently available IMEX Runge-Kutta schemes. For each method, it gives the -ts_arkimex_type name, the reference, the total number of stages/implicit stages, the order/stage-order, the implicit stability properties (IM), stiff accuracy (SA), the existence of an embedded scheme, and dense output (DO).

ROSW are linearized implicit Runge-Kutta methods known as Rosenbrock W-methods. They can accommodate inexact Jacobian matrices in their formulation. A series of methods are available in PETSc are listed in Table 15 below. For each method, it gives the reference, the total number of stages and implicit stages, the scheme order and stage order, the implicit stability properties (IM), stiff accuracy (SA), the existence of an embedded scheme, dense output (DO), the capacity to use inexact Jacobian matrices (-W), and high order integration of differential algebraic equations (PDAE).

Consider a fast-slow ODE system

where \(u^{slow}\) is the slow component and \(u^{fast}\) is the fast component. The fast component can be partitioned additively as described above. Thus we want to treat \(f^{slow}()\) and \(f^{fast}()\) explicitly and the other terms implicitly when using TSARKIMEX. This is achieved by using the following APIs:

TSARKIMEXSetFastSlowSplit() informs PETSc to use ARKIMEX to solve a fast-slow system.

TSRHSSplitSetIS() specifies the index set for the slow/fast components.

TSRHSSplitSetRHSFunction() specifies the parts to be handled explicitly \(f^{slow}()\) and \(f^{fast}()\).

TSRHSSplitSetIFunction() and TSRHSSplitSetIJacobian() specify the implicit part and its Jacobian.

Note that this ODE system can also be solved by padding zeros in the implicit part and using the standard IMEX methods. However, one needs to provide the full-dimensional Jacobian whereas only a partial Jacobian is needed for the fast-slow split which is more efficient in storage and speed.

In this section, we describe explicit and implicit time stepping methods with global error estimation that are introduced in [Con16]. The solution vector for a GLEE method is either [\(y\), \(\tilde{y}\)] or [\(y\),\(\varepsilon\)], where \(y\) is the solution, \(\tilde{y}\) is the “auxiliary solution,” and \(\varepsilon\) is the error. The working vector that TSGLEE uses is \(Y\) = [\(y\),\(\tilde{y}\)], or [\(y\),\(\varepsilon\)]. A GLEE method is defined by

\((p,r,s)\): (order, steps, and stages),

\(\gamma\): factor representing the global error ratio,

\(A, U, B, V\): method coefficients,

\(S\): starting method to compute the working vector from the solution (say at the beginning of time integration) so that \(Y = Sy\),

\(F\): finalizing method to compute the solution from the working vector,\(y = FY\).

\(F_\text{embed}\): coefficients for computing the auxiliary solution \(\tilde{y}\) from the working vector (\(\tilde{y} = F_\text{embed} Y\)),

\(F_\text{error}\): coefficients to compute the estimated error vector from the working vector (\(\varepsilon = F_\text{error} Y\)).

\(S_\text{error}\): coefficients to initialize the auxiliary solution (\(\tilde{y}\) or \(\varepsilon\)) from a specified error vector (\(\varepsilon\)). It is currently implemented only for \(r = 2\). We have \(y_\text{aux} = S_{error}[0]*\varepsilon + S_\text{error}[1]*y\), where \(y_\text{aux}\) is the 2nd component of the working vector \(Y\).

The methods can be described in two mathematically equivalent forms: propagate two components (“\(y\tilde{y}\) form”) and propagating the solution and its estimated error (“\(y\varepsilon\) form”). The two forms are not explicitly specified in TSGLEE; rather, the specific values of \(B, U, S, F, F_{embed}\), and \(F_{error}\) characterize whether the method is in \(y\tilde{y}\) or \(y\varepsilon\) form.

The API used by this TS method includes:

TSGetSolutionComponents: Get all the solution components of the working vector

Call with NULL as the last argument to get the total number of components in the working vector \(Y\) (this is \(r\) (not \(r-1\))), then call to get the \(i\)-th solution component.

TSGetAuxSolution: Returns the auxiliary solution \(\tilde{y}\) (computed as \(F_\text{embed} Y\))

TSGetTimeError: Returns the estimated error vector \(\varepsilon\) (computed as \(F_\text{error} Y\) if \(n=0\) or restores the error estimate at the end of the previous step if \(n=-1\))

TSSetTimeError: Initializes the auxiliary solution (\(\tilde{y}\) or \(\varepsilon\)) for a specified initial error.

The local error is estimated as \(\varepsilon(n+1)-\varepsilon(n)\). This is to be used in the error control. The error in \(y\tilde{y}\) GLEE is \(\varepsilon(n) = \frac{1}{1-\gamma} * (\tilde{y}(n) - y(n))\).

Note that \(y\) and \(\tilde{y}\) are reported to TSAdapt basic (TSADAPTBASIC), and thus it computes the local error as \(\varepsilon_{loc} = (\tilde{y} - y)\). However, the actual local error is \(\varepsilon_{loc} = \varepsilon_{n+1} - \varepsilon_n = \frac{1}{1-\gamma} * [(\tilde{y} - y)_{n+1} - (\tilde{y} - y)_n]\).

Table 16 lists currently available GL schemes with global error estimation [Con16].

Based on backward Euler

To use a fully implicit method like TSTHETA, TSBDF or TSDIRK, either provide the Jacobian of \(F()\) (and \(G()\) if \(G()\) is provided) or use a DM that provides a coloring so the Jacobian can be computed efficiently via finite differences.

The explicit Euler and Runge-Kutta methods require the ODE be in the form

The user can either call TSSetRHSFunction() and/or they can call TSSetIFunction() (so long as the function provided to TSSetIFunction() is equivalent to \(\dot{u} + \tilde{F}(t,u)\)) but the Jacobians need not be provided. [2]

The Explicit Runge-Kutta timestepper with variable timesteps is an implementation of the standard Runge-Kutta with an embedded method. The error in each timestep is calculated using the solutions from the Runge-Kutta method and its embedded method (the 2-norm of the difference is used). The default method is the \(3\)rd-order Bogacki-Shampine method with a \(2\)nd-order embedded method (TSRK3BS). Other available methods are the \(5\)th-order Fehlberg RK scheme with a \(4\)th-order embedded method (TSRK5F), the \(5\)th-order Dormand-Prince RK scheme with a \(4\)th-order embedded method (TSRK5DP), the \(5\)th-order Bogacki-Shampine RK scheme with a \(4\)th-order embedded method (TSRK5BS, and the \(6\)th-, \(7\)th, and \(8\)th-order robust Verner RK schemes with a \(5\)th-, \(6\)th, and \(7\)th-order embedded method, respectively (TSRK6VR, TSRK7VR, TSRK8VR). Variable timesteps cannot be used with RK schemes that do not have an embedded method (TSRK1FE - \(1\)st-order, \(1\)-stage forward Euler, TSRK2A - \(2\)nd-order, \(2\)-stage RK scheme, TSRK3 - \(3\)rd-order, \(3\)-stage RK scheme, TSRK4 - \(4\)-th order, \(4\)-stage RK scheme).

\(\dot{u} = A u.\) First compute the matrix \(A\) then call

\(\dot{u} = A(t) u.\) Use

where YourComputeRHSJacobian() is a function you provide that computes \(A\) as a function of time. Or use

-ts_monitor - prints the time and timestep at each iteration.

-ts_adapt_monitor - prints information about the timestep adaption calculation at each iteration.

-ts_monitor_lg_timestep - plots the size of each timestep, TSMonitorLGTimeStep().

-ts_monitor_lg_solution - for ODEs with only a few components (not arising from the discretization of a PDE) plots the solution as a function of time, TSMonitorLGSolution().

-ts_monitor_lg_error - for ODEs with only a few components plots the error as a function of time, only if TSSetSolutionFunction() is provided, TSMonitorLGError().

-ts_monitor_draw_solution - plots the solution at each iteration, TSMonitorDrawSolution().

-ts_monitor_draw_error - plots the error at each iteration only if TSSetSolutionFunction() is provided, TSMonitorDrawSolution().

-ts_monitor_solution binary[:filename] - saves the solution at each iteration to a binary file, TSMonitorSolution(). Solution viewers work with other time-aware formats, e.g., -ts_monitor_solution cgns:sol.cgns, and can output one solution every 10 time steps by adding -ts_monitor_solution_interval 10. Use -ts_monitor_solution_interval -1 to output data only at then end of a time loop.

-ts_monitor_solution_vtk <filename-%03D.vts> - saves the solution at each iteration to a file in vtk format, TSMonitorSolutionVTK().

Most of the time stepping methods available in PETSc have an error estimation and error control mechanism. This mechanism is implemented by changing the step size in order to maintain user specified absolute and relative tolerances. The PETSc object responsible with error control is TSAdapt. The available TSAdapt types are listed in the following table.

extension of the basic adaptor to treat \({\rm Tol}_{\rm A}\) and \({\rm Tol}_{\rm R}\) as separate criteria. It can also control global errors if the integrator (e.g., TSGLEE) provides this information

adaptive controller for time-stepping based on digital signal processing

When using TSADAPTBASIC (the default), the user typically provides a desired absolute \({\rm Tol}_{\rm A}\) or a relative \({\rm Tol}_{\rm R}\) error tolerance by invoking TSSetTolerances() or at the command line with options -ts_atol and -ts_rtol. The error estimate is based on the local truncation error, so for every step the algorithm verifies that the estimated local truncation error satisfies the tolerances provided by the user and computes a new step size to be taken. For multistage methods, the local truncation is obtained by comparing the solution \(y\) to a lower order \(\widehat{p}=p-1\) approximation, \(\widehat{y}\), where \(p\) is the order of the method and \(\widehat{p}\) the order of \(\widehat{y}\).

The adaptive controller at step \(n\) computes a tolerance level

and forms the acceptable error level

where the errors are computed componentwise, \(m\) is the dimension of \(y\) and -ts_adapt_wnormtype is 2 (default). If -ts_adapt_wnormtype is infinity (max norm), then

The error tolerances are satisfied when \(\rm wlte\le 1.0\).

The next step size is based on this error estimate, and determined by

where \(\alpha_{\min}=\)-ts_adapt_clip[0] and \(\alpha_{\max}\)=-ts_adapt_clip[1] keep the change in \(\Delta t\) to within a certain factor, and \(\beta<1\) is chosen through -ts_adapt_safety so that there is some margin to which the tolerances are satisfied and so that the probability of rejection is decreased.

This adaptive controller works in the following way. After completing step \(k\), if \(\rm wlte_{k+1} \le 1.0\), then the step is accepted and the next step is modified according to (5); otherwise, the step is rejected and retaken with the step length computed in (5).

For problems that involve discontinuous right-hand sides, one can set an “event” function \(g(t,u)\) for PETSc to detect and locate the times of discontinuities (zeros of \(g(t,u)\)). Events can be defined through the event monitoring routine

Here, nevents denotes the number of events, direction sets the type of zero crossing to be detected for an event (+1 for positive zero-crossing, -1 for negative zero-crossing, and 0 for both), terminate conveys whether the time-stepping should continue or halt when an event is located, eventmonitor is a user- defined routine that specifies the event description, postevent is an optional user-defined routine to take specific actions following an event.

The arguments to indicator() are the timestep context, current time, input state \(u\), array of event function value, and the (optional) user-provided context eventP.

The arguments to postevent() routine are the timestep context, number of events occurred, indices of events occurred, current time, input state \(u\), a boolean flag indicating forward solve (1) or adjoint solve (0), and the (optional) user-provided context eventP.

Discretized finite element problems often have the form \(M \dot u = G(t, u)\) where \(M\) is the mass matrix. Such problems can be solved using DMTSSetIFunction() with implicit integrators. When \(M\) is nonsingular (i.e., the problem is an ODE, not a DAE), explicit integrators can be applied to \(\dot u = M^{-1} G(t, u)\) or \(\dot u = \hat M^{-1} G(t, u)\), where \(\hat M\) is the lumped mass matrix. While the true mass matrix generally has a dense inverse and thus must be solved iteratively, the lumped mass matrix is diagonal (e.g., computed via collocated quadrature or row sums of \(M\)). To have PETSc create and apply a (lumped) mass matrix automatically, first use DMTSSetRHSFunction() to specify \(G\) and set a PetscFE using DMAddField() and DMCreateDS(), then call either DMTSCreateRHSMassMatrix() or DMTSCreateRHSMassMatrixLumped() to automatically create the mass matrix and a KSP that will be used to apply \(M^{-1}\). This KSP can be customized using the "mass_" prefix.

The TS library provides a framework based on discrete adjoint models for sensitivity analysis for ODEs and DAEs. The ODE/DAE solution process (henceforth called the forward run) can be obtained by using either explicit or implicit solvers in TS, depending on the problem properties. Currently supported method types are TSRK (Runge-Kutta) explicit methods and TSTHETA implicit methods, which include TSBEULER and TSCN.

and the cost function(s)

The TSAdjoint routines of PETSc provide

To perform the discrete adjoint sensitivity analysis one first sets up the TS object for a regular forward run but with one extra function call

then calls TSSolve() in the usual manner.

One must create two arrays of \(n_\text{cost}\) vectors \(\lambda\) and \(\mu\) (if there are no parameters \(p\) then one can use NULL for the \(\mu\) array.) The \(\lambda\) vectors are the same dimension and parallel layout as the solution vector for the ODE, the \(\mu\) vectors are of dimension \(p\); when \(p\) is small usually all its elements are on the first MPI process, while the vectors have no entries on the other processes. \(\lambda_i\) and \(\mu_i\) should be initialized with the values \(d\Phi_i/dy|_{t=t_F}\) and \(d\Phi_i/dp|_{t=t_F}\) respectively. Then one calls

where numcost denotes \(n_\text{cost}\). If \(F()\) is a function of \(p\) one needs to also provide the Jacobian \(-F_p\) with

or both, depending on which form is used to define the ODE.

The arguments for the function fp() are the timestep context, current time, \(y\), and the (optional) user-provided context.

If there is an integral term in the cost function, i.e. \(r\) is nonzero, it can be transformed into another ODE that is augmented to the original ODE. To evaluate the integral, one needs to create a child TS objective by calling

and provide the ODE RHS function (which evaluates the integrand \(r\)) with

Similar to the settings for the original ODE, Jacobians of the integrand can be provided with

where \(\mathrm{drdyf}= dr /dy\), \(\mathrm{drdpf} = dr /dp\). Since the integral term is additive to the cost function, its gradient information will be included in \(\lambda\) and \(\mu\).

Lastly, one starts the backward run by calling

One can obtain the value of the integral term by calling

or accessing directly the solution vector used by quadts.

The second argument of TSCreateQuadratureTS() allows one to choose if the integral term is evaluated in the forward run (inside TSSolve()) or in the backward run (inside TSAdjointSolve()) when TSSetCostGradients() and TSSetCostIntegrand() are called before TSSolve(). Note that this also allows for evaluating the integral without having to use the adjoint solvers.

To provide a better understanding of the use of the adjoint solvers, we introduce a simple example, corresponding to TS Power Grid Tutorial ex3sa. The problem is to study dynamic security of power system when there are credible contingencies such as short-circuits or loss of generators, transmission lines, or loads. The dynamic security constraints are incorporated as equality constraints in the form of discretized differential equations and inequality constraints for bounds on the trajectory. The governing ODE system is

where \(\phi\) is the phase angle and \(\omega\) is the frequency.

The initial conditions at time \(t_0\) are

\(p_{max}\) is a positive number when the system operates normally. At an event such as fault incidence/removal, \(p_{max}\) will change to \(0\) temporarily and back to the original value after the fault is fixed. The objective is to maximize \(p_m\) subject to the above ODE constraints and \(\phi<\phi_S\) during all times. To accommodate the inequality constraint, we want to compute the sensitivity of the cost function

with respect to the parameter \(p_m\). \(numcost\) is \(1\) since it is a scalar function.

For ODE solution, PETSc requires user-provided functions to evaluate the system \(F(t,y,\dot{y},p)\) (set by TSSetIFunction() ) and its corresponding Jacobian \(F_y + \sigma F_{\dot y}\) (set by TSSetIJacobian()). Note that the solution state \(y\) is \([ \phi \; \omega ]^T\) here. For sensitivity analysis, we need to provide a routine to compute \(\mathrm{f}_p=[0 \; 1]^T\) using TSASetRHSJacobianP(), and three routines corresponding to the integrand \(r=c \left( \max(0, \phi - \phi_S ) \right)^2\), \(r_p = [0 \; 0]^T\) and \(r_y= [ 2 c \left( \max(0, \phi - \phi_S ) \right) \; 0]^T\) using TSSetCostIntegrand().

In the adjoint run, \(\lambda\) and \(\mu\) are initialized as \([ 0 \; 0 ]^T\) and \([-1]\) at the final time \(t_F\). After TSAdjointSolve(), the sensitivity of the cost function w.r.t. initial conditions is given by the sensitivity variable \(\lambda\) (at time \(t_0\)) directly. And the sensitivity of the cost function w.r.t. the parameter \(p_m\) can be computed (by users) as

For explicit methods where one does not need to provide the Jacobian \(F_u\) for the forward solve one still does need it for the backward solve and thus must call

discrete adjoint sensitivity using explicit and implicit time stepping methods for an ODE problem TS Tutorial ex20adj,

an optimization problem using the discrete adjoint models of the ERK (for nonstiff ODEs) and the Theta methods (for stiff DAEs) TS Tutorial ex20opt_ic and TS Tutorial ex20opt_p,

an ODE-constrained optimization using the discrete adjoint models of the Theta methods for cost function with an integral term TS Power Grid Tutorial ex3opt,

discrete adjoint sensitivity using the Crank-Nicolson methods for DAEs with discontinuities TS Power Grid Stability Tutorial ex9busadj,

a DAE-constrained optimization problem using the discrete adjoint models of the Crank-Nicolson methods for cost function with an integral term TS Power Grid Tutorial ex9busopt,

discrete adjoint sensitivity using the Crank-Nicolson methods for a PDE problem TS Advection-Diffusion-Reaction Tutorial ex5adj.

The discrete adjoint model requires the states (and stage values in the context of multistage timestepping methods) to evaluate the Jacobian matrices during the adjoint (backward) run. By default, PETSc stores the whole trajectory to disk as binary files, each of which contains the information for a single time step including state, time, and stage values (optional). One can also make PETSc store the trajectory to memory with the option -ts_trajectory_type memory. However, there might not be sufficient memory capacity especially for large-scale problems and long-time integration.

A so-called checkpointing scheme is needed to solve this problem. The scheme stores checkpoints at selective time steps and recomputes the missing information. The revolve library is used by PETSc TSTrajectory to generate an optimal checkpointing schedule that minimizes the recomputations given a limited number of available checkpoints. One can specify the number of available checkpoints with the option -ts_trajectory_max_cps_ram [maximum number of checkpoints in RAM]. Note that one checkpoint corresponds to one time step.

The revolve library also provides an optimal multistage checkpointing scheme that uses both RAM and disk for storage. This scheme is automatically chosen if one uses both the option -ts_trajectory_max_cps_ram [maximum number of checkpoints in RAM] and the option -ts_trajectory_max_cps_disk [maximum number of checkpoints on disk].

Some other useful options are listed below.

-ts_trajectory_view prints the total number of recomputations,

-ts_monitor and -ts_adjoint_monitor allow users to monitor the progress of the adjoint work flow,

-ts_trajectory_type visualization may be used to save the whole trajectory for visualization. It stores the solution and the time, but no stage values. The binary files generated can be read into MATLAB via the script $PETSC_DIR/share/petsc/matlab/PetscReadBinaryTrajectory.m.

Sundials is a parallel ODE solver developed by Hindmarsh et al. at LLNL. The TS library provides an interface to use the CVODE component of Sundials directly from PETSc. (To configure PETSc to use Sundials, see the installation guide, installation/index.htm.)

To use the Sundials integrators, call

or use the command line option -ts_type sundials.

Sundials’ CVODE solver comes with two main integrator families, Adams and BDF (backward differentiation formula). One can select these with

or the command line option -ts_sundials_type <adams,bdf>. BDF is the default.

Sundials does not use the SNES library within PETSc for its nonlinear solvers, so one cannot change the nonlinear solver options via SNES. Rather, Sundials uses the preconditioners within the PC package of PETSc, which can be accessed via

The user can then directly set preconditioner options; alternatively, the usual runtime options can be employed via -pc_xxx.

Finally, one can set the Sundials tolerances via

where abs denotes the absolute tolerance and rel the relative tolerance.

Other PETSc-Sundials options include

where type is either SUNDIALS_MODIFIED_GS or SUNDIALS_UNMODIFIED_GS. This may be set via the options data base with -ts_sundials_gramschmidt_type <modifed,unmodified>.

sets the number of vectors in the Krylov subpspace used by GMRES. This may be set in the options database with -ts_sundials_maxl maxl.

TChem [3] is a package originally developed at Sandia National Laboratory that can read in CHEMKIN [4] data files and compute the right-hand side function and its Jacobian for a reaction ODE system. To utilize PETSc’s ODE solvers for these systems, first install PETSc with the additional configure option --download-tchem. We currently provide two examples of its use; one for single cell reaction and one for an “artificial” one dimensional problem with periodic boundary conditions and diffusion of all species. The self-explanatory examples are the The TS tutorial extchem and The TS tutorial extchemfield.

Simple Example: TS provides a general code for performing pseudo timestepping with a variable timestep at each physical node point. For example, instead of directly attacking the steady-state problem

we can use pseudo-transient continuation by solving

Using time differencing

with the backward Euler method, we obtain nonlinear equations at a series of pseudo-timesteps

For this problem the user must provide \(G(u)\), the time steps \(dt^{n}\) and the left-hand-side matrix \(B\) (or optionally, if the timestep is position independent and \(B\) is the identity matrix, a scalar timestep), as well as optionally the Jacobian of \(G(u)\).

More generally, this can be applied to implicit ODE and DAE for which the transient form is

For solving steady-state problems with pseudo-timestepping one proceeds as follows.

Provide the function G(u) with the routine

The arguments to the function f() are the timestep context, the current time, the input for the function, the output for the function and the (optional) user-provided context variable fP.

Provide the (approximate) Jacobian matrix of G(u) and a function to compute it at each Newton iteration. This is done with the command

The arguments for the function f() are the timestep context, the current time, the location where the Jacobian is to be computed, the (approximate) Jacobian matrix, an alternative approximate Jacobian matrix used to construct the preconditioner, and the optional user-provided context, passed in as fP. The user must provide the Jacobian as a matrix; thus, if using a matrix-free approach, one must create a MATSHELL matrix.

In addition, the user must provide a routine that computes the pseudo-timestep. This is slightly different depending on if one is using a constant timestep over the entire grid, or it varies with location.

For location-independent pseudo-timestepping, one uses the routine

The function dt is a user-provided function that computes the next pseudo-timestep. As a default one can use TSPseudoTimeStepDefault(TS,PetscReal*,PetscCtx) for dt. This routine updates the pseudo-timestep with one of two strategies: the default

which can be set with the call

or the option -ts_pseudo_increment_dt_from_initial_dt. The value \(dt_{\mathrm{increment}}\) is by default \(1.1\), but can be reset with the call

or the option -ts_pseudo_increment <inc>.

For location-dependent pseudo-timestepping, the interface function has not yet been created.

U.M. Ascher, S.J. Ruuth, and R.J. Spiteri. Implicit-explicit Runge-Kutta methods for time-dependent partial differential equations. Applied Numerical Mathematics, 25:151–167, 1997.

Uri M Ascher and Linda R Petzold. Computer methods for ordinary differential equations and differential-algebraic equations. Volume 61. SIAM, 1998.

S. Boscarino, L. Pareschi, and G. Russo. Implicit-explicit Runge-Kutta schemes for hyperbolic systems and kinetic equations in the diffusion limit. Arxiv preprint arXiv:1110.4375, 2011.

Oriol Colomés and Santiago Badia. Segregated Runge–Kutta methods for the incompressible Navier–Stokes equations. International Journal for Numerical Methods in Engineering, 105(5):372–400, 2016.

E.M. Constantinescu. Estimating global errors in time stepping. ArXiv e-prints, March 2016. arXiv:1503.05166.

F.X. Giraldo, J.F. Kelly, and E.M. Constantinescu. Implicit-explicit formulations of a three-dimensional nonhydrostatic unified model of the atmosphere (NUMA). SIAM Journal on Scientific Computing, 35(5):B1162–B1194, 2013. doi:10.1137/120876034.

C.A. Kennedy and M.H. Carpenter. Additive Runge-Kutta schemes for convection-diffusion-reaction equations. Appl. Numer. Math., 44(1-2):139–181, 2003. doi:10.1016/S0168-9274(02)00138-1.

L. Pareschi and G. Russo. Implicit-explicit Runge-Kutta schemes and applications to hyperbolic systems with relaxation. Journal of Scientific Computing, 25(1):129–155, 2005.

J. Rang and L. Angermann. New Rosenbrock W-methods of order 3 for partial differential algebraic equations of index 1. BIT Numerical Mathematics, 45(4):761–787, 2005. doi:10.1007/s10543-005-0035-y.

A. Sandu, J.G. Verwer, J.G. Blom, E.J. Spee, G.R. Carmichael, and F.A. Potra. Benchmarking stiff ODE solvers for atmospheric chemistry problems II: Rosenbrock solvers. Atmospheric Environment, 31(20):3459–3472, 1997.

If the matrix \(F_{\dot{u}}(t) = \partial F / \partial \dot{u}\) is nonsingular then it is an ODE and can be transformed to the standard explicit form, although this transformation may not lead to efficient algorithms.

PETSc will automatically translate the function provided to the appropriate form.

bitbucket.org/jedbrown/tchem

en.wikipedia.org/wiki/CHEMKIN

SNES: Nonlinear Solvers

TAO: Optimization Solvers

**Examples:**

Example 1 (unknown):
```unknown
TSSetIFunction(TS ts, Vec R, PetscErrorCode (*f)(TS, PetscReal, Vec, Vec, Vec, PetscCtx), PetscCtxfunP);
```

Example 2 (unknown):
```unknown
TSSetRHSFunction(TS ts, Vec R, PetscErrorCode (*f)(TS, PetscReal, Vec, Vec, PetscCtx), PetscCtxfunP);
```

Example 3 (unknown):
```unknown
TSSetIJacobian(TS ts, Mat A, Mat B, PetscErrorCode (*fjac)(TS, PetscReal, Vec, Vec, PetscReal, Mat, Mat, PetscCtx), PetscCtx jacP);
```

Example 4 (unknown):
```unknown
TSSetRHSJacobian(TS ts, Mat A, Mat B, 
PetscErrorCode (*fjac)(TS, PetscReal, Vec, Mat, Mat, PetscCtx), PetscCtx jacP);
```

---
