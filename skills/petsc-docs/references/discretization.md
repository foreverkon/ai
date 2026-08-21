# Petsc-Docs-Full-Raw - Discretization

**Pages:** 574

---

## Defining your own mathematical functions (PF)#

**URL:** https://petsc.org/release/manualpages/PF/

**Contents:**
- Defining your own mathematical functions (PF)#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Single list of manual pages#

PETSc functions (PF objects) are used to compute grid functions, element functions, etc.

PFAppendOptionsPrefix

PFAppendOptionsPrefix

Finite Volumes (PetscFV)

Landau Collision Operator

---

## Discretization Technology and Quadrature (DT)#

**URL:** https://petsc.org/release/manualpages/DT/

**Contents:**
- Discretization Technology and Quadrature (DT)#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Single list of manual pages#

DT provides discretization technology, for instance quadrature, finite element, or finite volume support.

PetscCDFMaxwellBoltzmann1D

PetscCDFMaxwellBoltzmann2D

PetscCDFMaxwellBoltzmann3D

PetscDSAddDiscretization

PetscDSGetComponentDerivativeOffsets

PetscDSGetComponentDerivativeOffsetsCohesive

PetscDSGetComponentOffset

PetscDSGetComponentOffsets

PetscDSGetComponentOffsetsCohesive

PetscDSGetCoordinateDimension

PetscDSGetDiscretization

PetscDSGetFieldOffset

PetscDSGetFieldOffsetCohesive

PetscDSGetSpatialDimension

PetscDSGetTotalComponents

PetscDSGetTotalDimension

PetscDSSetCoordinateDimension

PetscDSSetDiscretization

PetscDTGradedOrderToIndex

PetscDTIndexToGradedOrder

PetscGaussLobattoLegendreElementAdvectionCreate

PetscGaussLobattoLegendreElementAdvectionDestroy

PetscGaussLobattoLegendreElementGradientCreate

PetscGaussLobattoLegendreElementGradientDestroy

PetscGaussLobattoLegendreElementLaplacianCreate

PetscGaussLobattoLegendreElementLaplacianDestroy

PetscGaussLobattoLegendreElementMassCreate

PetscGaussLobattoLegendreElementMassDestroy

PetscGaussLobattoLegendreIntegrate

PetscPDFMaxwellBoltzmann1D

PetscPDFMaxwellBoltzmann2D

PetscPDFMaxwellBoltzmann3D

PetscPDFSampleConstant1D

PetscPDFSampleConstant2D

PetscPDFSampleConstant3D

PetscPDFSampleGaussian1D

PetscPDFSampleGaussian2D

PetscPDFSampleGaussian3D

PetscPointExactSolutionFn

PetscQuadratureCreate

PetscQuadratureDestroy

PetscQuadratureDuplicate

PetscWeakFormGetNumFields

PetscWeakFormSetNumFields

PetscDSCopyExactSolutions

PetscDSDestroyBoundary

PetscDSGetBdJacobianPreconditioner

PetscDSGetDynamicJacobian

PetscDSGetExactSolution

PetscDSGetExactSolutionTimeDerivative

PetscDSGetFaceTabulation

PetscDSGetJacobianPreconditioner

PetscDSGetNumBoundary

PetscDSGetRHSResidual

PetscDSGetRiemannSolver

PetscDSHasBdJacobianPreconditioner

PetscDSHasDynamicJacobian

PetscDSHasJacobianPreconditioner

PetscDSSelectDiscretizations

PetscDSSelectEquations

PetscDSSetBdJacobianPreconditioner

PetscDSSetCellParameters

PetscDSSetDynamicJacobian

PetscDSSetExactSolution

PetscDSSetExactSolutionTimeDerivative

PetscDSSetFromOptions

PetscDSSetIntegrationParameters

PetscDSSetJacobianPreconditioner

PetscDSSetRHSResidual

PetscDSSetRiemannSolver

PetscDSUpdateBoundaryLabels

PetscDSUseJacobianPreconditioner

PetscDSViewFromOptions

PetscDTAltVInteriorMatrix

PetscDTAltVInteriorPattern

PetscDTAltVPullbackMatrix

PetscDTAltVWedgeMatrix

PetscDTGaussJacobiQuadrature

PetscDTGaussLobattoJacobiQuadrature

PetscDTGaussLobattoLegendreQuadrature

PetscDTGaussQuadrature

PetscDTGaussTensorQuadrature

PetscDTSimplexQuadrature

PetscDTSimplexQuadratureType

PetscDTStroudConicalQuadrature

PetscDTTanhSinhTensorQuadrature

PetscDTTensorQuadratureCreate

PetscGaussLobattoLegendreCreateType

PetscProbCreateFromOptions

PetscQuadratureExpandComposite

PetscQuadratureGetCellType

PetscQuadratureGetData

PetscQuadratureGetNumComponents

PetscQuadratureGetOrder

PetscQuadraturePushForward

PetscQuadratureSetCellType

PetscQuadratureSetData

PetscQuadratureSetNumComponents

PetscQuadratureSetOrder

PetscWeakFormAddBdJacobian

PetscWeakFormAddBdJacobianPreconditioner

PetscWeakFormAddBdResidual

PetscWeakFormAddDynamicJacobian

PetscWeakFormAddJacobian

PetscWeakFormAddJacobianPreconditioner

PetscWeakFormAddObjective

PetscWeakFormAddResidual

PetscWeakFormClearIndex

PetscWeakFormGetBdJacobian

PetscWeakFormGetBdJacobianPreconditioner

PetscWeakFormGetBdResidual

PetscWeakFormGetDynamicJacobian

PetscWeakFormGetIndexObjective

PetscWeakFormGetJacobian

PetscWeakFormGetJacobianPreconditioner

PetscWeakFormGetObjective

PetscWeakFormGetResidual

PetscWeakFormGetRiemannSolver

PetscWeakFormHasBdJacobian

PetscWeakFormHasBdJacobianPreconditioner

PetscWeakFormHasDynamicJacobian

PetscWeakFormHasJacobian

PetscWeakFormHasJacobianPreconditioner

PetscWeakFormReplaceLabel

PetscWeakFormRewriteKeys

PetscWeakFormSetBdJacobian

PetscWeakFormSetBdJacobianPreconditioner

PetscWeakFormSetBdResidual

PetscWeakFormSetDynamicJacobian

PetscWeakFormSetIndexBdJacobian

PetscWeakFormSetIndexBdJacobianPreconditioner

PetscWeakFormSetIndexBdResidual

PetscWeakFormSetIndexDynamicJacobian

PetscWeakFormSetIndexJacobian

PetscWeakFormSetIndexJacobianPreconditioner

PetscWeakFormSetIndexObjective

PetscWeakFormSetIndexResidual

PetscWeakFormSetIndexRiemannSolver

PetscWeakFormSetJacobian

PetscWeakFormSetJacobianPreconditioner

PetscWeakFormSetObjective

PetscWeakFormSetResidual

PetscWeakFormSetRiemannSolver

PETSC_FORM_DEGREE_UNDEFINED

PetscDTPTrimmedEvalJet

PetscDTReconstructPoly

PetscProbComputeKSStatistic

PetscProbComputeKSStatisticMagnitude

PetscProbComputeKSStatisticWeighted

PetscDSAddBoundaryByName

PetscDSGetEvaluationArrays

PetscDSGetHeightSubspace

PetscDSGetNumCohesive

PetscDSPermuteQuadPoint

PetscDSUpdateBoundary

PetscDTCreateDefaultQuadrature

PetscDTCreateQuadratureByCell

PetscDTTanhSinhIntegrate

PetscDTTanhSinhIntegrateMPFR

PetscQuadratureComputePermutations

PETSC_FORM_DEGREE_UNDEFINED

PetscCDFMaxwellBoltzmann1D

PetscCDFMaxwellBoltzmann2D

PetscCDFMaxwellBoltzmann3D

PetscDSAddBoundaryByName

PetscDSAddDiscretization

PetscDSCopyExactSolutions

PetscDSDestroyBoundary

PetscDSGetBdJacobianPreconditioner

PetscDSGetComponentDerivativeOffsets

PetscDSGetComponentDerivativeOffsetsCohesive

PetscDSGetComponentOffset

PetscDSGetComponentOffsets

PetscDSGetComponentOffsetsCohesive

PetscDSGetCoordinateDimension

PetscDSGetDiscretization

PetscDSGetDynamicJacobian

PetscDSGetEvaluationArrays

PetscDSGetExactSolution

PetscDSGetExactSolutionTimeDerivative

PetscDSGetFaceTabulation

PetscDSGetFieldOffset

PetscDSGetFieldOffsetCohesive

PetscDSGetHeightSubspace

PetscDSGetJacobianPreconditioner

PetscDSGetNumBoundary

PetscDSGetNumCohesive

PetscDSGetRHSResidual

PetscDSGetRiemannSolver

PetscDSGetSpatialDimension

PetscDSGetTotalComponents

PetscDSGetTotalDimension

PetscDSHasBdJacobianPreconditioner

PetscDSHasDynamicJacobian

PetscDSHasJacobianPreconditioner

PetscDSPermuteQuadPoint

PetscDSSelectDiscretizations

PetscDSSelectEquations

PetscDSSetBdJacobianPreconditioner

PetscDSSetCellParameters

PetscDSSetCoordinateDimension

PetscDSSetDiscretization

PetscDSSetDynamicJacobian

PetscDSSetExactSolution

PetscDSSetExactSolutionTimeDerivative

PetscDSSetFromOptions

PetscDSSetIntegrationParameters

PetscDSSetJacobianPreconditioner

PetscDSSetRHSResidual

PetscDSSetRiemannSolver

PetscDSUpdateBoundary

PetscDSUpdateBoundaryLabels

PetscDSUseJacobianPreconditioner

PetscDSViewFromOptions

PetscDTAltVInteriorMatrix

PetscDTAltVInteriorPattern

PetscDTAltVPullbackMatrix

PetscDTAltVWedgeMatrix

PetscDTCreateDefaultQuadrature

PetscDTCreateQuadratureByCell

PetscDTGaussJacobiQuadrature

PetscDTGaussLobattoJacobiQuadrature

PetscDTGaussLobattoLegendreQuadrature

PetscDTGaussQuadrature

PetscDTGaussTensorQuadrature

PetscDTGradedOrderToIndex

PetscDTIndexToGradedOrder

PetscDTPTrimmedEvalJet

PetscDTReconstructPoly

PetscDTSimplexQuadrature

PetscDTSimplexQuadratureType

PetscDTStroudConicalQuadrature

PetscDTTanhSinhIntegrate

PetscDTTanhSinhIntegrateMPFR

PetscDTTanhSinhTensorQuadrature

PetscDTTensorQuadratureCreate

PetscGaussLobattoLegendreCreateType

PetscGaussLobattoLegendreElementAdvectionCreate

PetscGaussLobattoLegendreElementAdvectionDestroy

PetscGaussLobattoLegendreElementGradientCreate

PetscGaussLobattoLegendreElementGradientDestroy

PetscGaussLobattoLegendreElementLaplacianCreate

PetscGaussLobattoLegendreElementLaplacianDestroy

PetscGaussLobattoLegendreElementMassCreate

PetscGaussLobattoLegendreElementMassDestroy

PetscGaussLobattoLegendreIntegrate

PetscPDFMaxwellBoltzmann1D

PetscPDFMaxwellBoltzmann2D

PetscPDFMaxwellBoltzmann3D

PetscPDFSampleConstant1D

PetscPDFSampleConstant2D

PetscPDFSampleConstant3D

PetscPDFSampleGaussian1D

PetscPDFSampleGaussian2D

PetscPDFSampleGaussian3D

PetscPointExactSolutionFn

PetscProbComputeKSStatistic

PetscProbComputeKSStatisticMagnitude

PetscProbComputeKSStatisticWeighted

PetscProbCreateFromOptions

PetscQuadratureComputePermutations

PetscQuadratureCreate

PetscQuadratureDestroy

PetscQuadratureDuplicate

PetscQuadratureExpandComposite

PetscQuadratureGetCellType

PetscQuadratureGetData

PetscQuadratureGetNumComponents

PetscQuadratureGetOrder

PetscQuadraturePushForward

PetscQuadratureSetCellType

PetscQuadratureSetData

PetscQuadratureSetNumComponents

PetscQuadratureSetOrder

PetscWeakFormAddBdJacobian

PetscWeakFormAddBdJacobianPreconditioner

PetscWeakFormAddBdResidual

PetscWeakFormAddDynamicJacobian

PetscWeakFormAddJacobian

PetscWeakFormAddJacobianPreconditioner

PetscWeakFormAddObjective

PetscWeakFormAddResidual

PetscWeakFormClearIndex

PetscWeakFormGetBdJacobian

PetscWeakFormGetBdJacobianPreconditioner

PetscWeakFormGetBdResidual

PetscWeakFormGetDynamicJacobian

PetscWeakFormGetIndexObjective

PetscWeakFormGetJacobian

PetscWeakFormGetJacobianPreconditioner

PetscWeakFormGetNumFields

PetscWeakFormGetObjective

PetscWeakFormGetResidual

PetscWeakFormGetRiemannSolver

PetscWeakFormHasBdJacobian

PetscWeakFormHasBdJacobianPreconditioner

PetscWeakFormHasDynamicJacobian

PetscWeakFormHasJacobian

PetscWeakFormHasJacobianPreconditioner

PetscWeakFormReplaceLabel

PetscWeakFormRewriteKeys

PetscWeakFormSetBdJacobian

PetscWeakFormSetBdJacobianPreconditioner

PetscWeakFormSetBdResidual

PetscWeakFormSetDynamicJacobian

PetscWeakFormSetIndexBdJacobian

PetscWeakFormSetIndexBdJacobianPreconditioner

PetscWeakFormSetIndexBdResidual

PetscWeakFormSetIndexDynamicJacobian

PetscWeakFormSetIndexJacobian

PetscWeakFormSetIndexJacobianPreconditioner

PetscWeakFormSetIndexObjective

PetscWeakFormSetIndexResidual

PetscWeakFormSetIndexRiemannSolver

PetscWeakFormSetJacobian

PetscWeakFormSetJacobianPreconditioner

PetscWeakFormSetNumFields

PetscWeakFormSetObjective

PetscWeakFormSetResidual

PetscWeakFormSetRiemannSolver

Discretization and Function Spaces

Function Spaces (PetscSpace)

---

## DMFieldCreateDefaultFaceQuadrature#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldCreateDefaultFaceQuadrature/

**Contents:**
- DMFieldCreateDefaultFaceQuadrature#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Creates a quadrature sufficient to integrate the field on all faces of the selected cells via pullback onto the reference element

field - the DMField object

pointIS - the index set of points over which we wish to integrate the field over faces

quad - a PetscQuadrature object

DMFieldCreateDefaultQuadrature(), DMField, PetscQuadrature, IS, DMFieldEvaluteFE(), DMFieldGetDegree()

src/dm/field/interface/dmfield.c

DMFieldCreateDefaultFaceQuadrature_DS() in src/dm/field/impls/ds/dmfieldds.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmfield.h" 
#include "petscdmfield.h" 
PetscErrorCode DMFieldCreateDefaultFaceQuadrature(DMField field, IS pointIS, PetscQuadrature *quad)
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
DMFieldCreateDefaultQuadrature()
```

Example 4 (unknown):
```unknown
PetscQuadrature
```

---

## DMFieldCreateDefaultQuadrature#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldCreateDefaultQuadrature/

**Contents:**
- DMFieldCreateDefaultQuadrature#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Creates a quadrature sufficient to integrate the field on the selected points via pullback onto the reference element

field - the DMField object

pointIS - the index set of points over which we wish to integrate the field

quad - a PetscQuadrature object

DMFieldCreateDefaultFaceQuadrature(), DMField, PetscQuadrature, IS, DMFieldEvaluteFE(), DMFieldGetDegree()

src/dm/field/interface/dmfield.c

DMFieldCreateDefaultQuadrature_DA() in src/dm/field/impls/da/dmfieldda.c DMFieldCreateDefaultQuadrature_DS() in src/dm/field/impls/ds/dmfieldds.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmfield.h" 
#include "petscdmfield.h" 
PetscErrorCode DMFieldCreateDefaultQuadrature(DMField field, IS pointIS, PetscQuadrature *quad)
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
DMFieldCreateDefaultFaceQuadrature()
```

Example 4 (unknown):
```unknown
PetscQuadrature
```

---

## DMFieldShellSetCreateDefaultQuadrature#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldShellSetCreateDefaultQuadrature/

**Contents:**
- DMFieldShellSetCreateDefaultQuadrature#
- Synopsis#
- Input Parameters#
- Calling sequence of create#
- See Also#
- Level#
- Location#

Register the routine that supplies a default PetscQuadrature sufficient to integrate a DMFIELDSHELL exactly over a set of mesh points.

field - the DMField of type DMFIELDSHELL

create - callback that returns a newly created PetscQuadrature for the given point IS

f - the DMField of type DMFIELDSHELL

is - the IS of mesh points over which the field will be integrated

quad - the newly created PetscQuadrature

DMField, DMFIELDSHELL, DMFieldCreateShell(), DMFieldCreateDefaultQuadrature()

src/dm/field/impls/shell/dmfieldshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscQuadrature
```

Example 2 (unknown):
```unknown
DMFIELDSHELL
```

Example 3 (unknown):
```unknown
#include "petscdmfield.h" 
PetscErrorCode DMFieldShellSetCreateDefaultQuadrature(DMField field, PetscErrorCode (*create)(DMField f, IS is, PetscQuadrature *quad))
```

Example 4 (unknown):
```unknown
DMFIELDSHELL
```

---

## DMMoabFEMCreateQuadratureDefault#

**URL:** https://petsc.org/release/manualpages/DMMOAB/DMMoabFEMCreateQuadratureDefault/

**Contents:**
- DMMoabFEMCreateQuadratureDefault#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Create default quadrature rules for integration over an element with a given dimension and polynomial order (deciphered from number of element vertices).

dim - the element dimension (1=EDGE, 2=QUAD/TRI, 3=HEX/TET)

nverts - the number of vertices in the physical element

quadrature - the quadrature object with default settings to integrate polynomials defined over the element

src/dm/impls/moab/dmmbfem.cxx

src/ksp/ksp/tutorials/ex35.cxx src/ksp/ksp/tutorials/ex36.cxx

Index of all DMMOAB routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
#include "petscdmmoab.h"   
PetscErrorCode DMMoabFEMCreateQuadratureDefault(const PetscInt dim, const PetscInt nverts, PetscQuadrature *quadrature)
```

Example 2 (unknown):
```unknown
DMMoabCreate()
```

---

## DMPlexLandauAccess#

**URL:** https://petsc.org/release/manualpages/LANDAU/DMPlexLandauAccess/

**Contents:**
- DMPlexLandauAccess#
- Synopsis#
- Input Parameters#
- Input/Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Access to the distribution function with user callback

pack - the DMCOMPOSITE

func - call back function

user_ctx - application context

X - Vector to data to

DMPlexLandauCreateVelocitySpace()

src/ts/utils/dmplexlandau/plexland.c

src/ts/utils/dmplexlandau/tutorials/ex1.c

Index of all LANDAU routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petsclandau.h"   
PetscErrorCode DMPlexLandauAccess(DM pack, Vec X, PetscErrorCode (*func)(DM, Vec, PetscInt, PetscInt, PetscInt, void *), void *user_ctx)
```

Example 2 (unknown):
```unknown
DMCOMPOSITE
```

Example 3 (unknown):
```unknown
DMPlexLandauCreateVelocitySpace()
```

---

## DMPlexLandauAddMaxwellians#

**URL:** https://petsc.org/release/manualpages/LANDAU/DMPlexLandauAddMaxwellians/

**Contents:**
- DMPlexLandauAddMaxwellians#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Add a Maxwellian distribution to a state

dm - The mesh (local)

temps - Temperatures of each species (global)

ns - Number density of each species (global)

grid - index into current grid - just used for offset into temp and ns

n_batch - number of batches

actx - Landau context

X - The state (local to this grid)

DMPlexLandauCreateVelocitySpace()

src/ts/utils/dmplexlandau/plexland.c

src/ts/utils/dmplexlandau/tutorials/ex2.c

Index of all LANDAU routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petsclandau.h"   
PetscErrorCode DMPlexLandauAddMaxwellians(DM dm, Vec X, PetscReal time, PetscReal temps[], PetscReal ns[], PetscInt grid, PetscInt b_id, PetscInt n_batch, void *actx)
```

Example 2 (unknown):
```unknown
DMPlexLandauCreateVelocitySpace()
```

---

## DMPlexLandauCreateMassMatrix#

**URL:** https://petsc.org/release/manualpages/LANDAU/DMPlexLandauCreateMassMatrix/

**Contents:**
- DMPlexLandauCreateMassMatrix#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Create mass matrix for Landau in Plex space (not field major order of Jacobian) - puts mass matrix into ctx->M

pack - the DM object. Puts matrix in Landau context M field

Amat - The mass matrix (optional), mass matrix is added to the DM context

DMPlexLandauCreateVelocitySpace()

src/ts/utils/dmplexlandau/plexland.c

Index of all LANDAU routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petsclandau.h"   
PetscErrorCode DMPlexLandauCreateMassMatrix(DM pack, Mat *Amat)
```

Example 2 (unknown):
```unknown
DMPlexLandauCreateVelocitySpace()
```

---

## DMPlexLandauCreateVelocitySpace#

**URL:** https://petsc.org/release/manualpages/LANDAU/DMPlexLandauCreateVelocitySpace/

**Contents:**
- DMPlexLandauCreateVelocitySpace#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#

Create a DMPLEX velocity space mesh

comm - The MPI communicator

dim - velocity space dimension (2 for axisymmetric, 3 for full 3X + 3V solver)

prefix - prefix for options (not tested)

pack - The DM object representing the mesh

X - A vector (user destroys)

J - Optional matrix (object destroys)

DMPlexCreate(), DMPlexLandauDestroyVelocitySpace()

src/ts/utils/dmplexlandau/plexland.c

src/ts/utils/dmplexlandau/tutorials/ex2.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/utils/dmplexlandau/tutorials/ex1f90.F90

Index of all LANDAU routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petsclandau.h"   
PetscErrorCode DMPlexLandauCreateVelocitySpace(MPI_Comm comm, PetscInt dim, const char prefix[], Vec *X, Mat *J, DM *pack)
```

Example 2 (unknown):
```unknown
DMPlexCreate()
```

Example 3 (unknown):
```unknown
DMPlexLandauDestroyVelocitySpace()
```

---

## DMPlexLandauDestroyVelocitySpace#

**URL:** https://petsc.org/release/manualpages/LANDAU/DMPlexLandauDestroyVelocitySpace/

**Contents:**
- DMPlexLandauDestroyVelocitySpace#
- Synopsis#
- Input/Output Parameters#
- See Also#
- Level#
- Location#
- Examples#

Destroy a DMPLEX velocity space mesh

dm - the DM to destroy

DMPlexLandauCreateVelocitySpace()

src/ts/utils/dmplexlandau/plexland.c

src/ts/utils/dmplexlandau/tutorials/ex2.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/utils/dmplexlandau/tutorials/ex1f90.F90

Index of all LANDAU routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petsclandau.h"   
PetscErrorCode DMPlexLandauDestroyVelocitySpace(DM *dm)
```

Example 2 (unknown):
```unknown
DMPlexLandauCreateVelocitySpace()
```

---

## DMPlexLandauIFunction#

**URL:** https://petsc.org/release/manualpages/LANDAU/DMPlexLandauIFunction/

**Contents:**
- DMPlexLandauIFunction#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

TS residual calculation, confusingly this computes the Jacobian w/o mass

ts - The time stepping context

time_dummy - current time (not used)

X_t - Time derivative of current state

actx - Landau context

DMPlexLandauCreateVelocitySpace(), DMPlexLandauIJacobian()

src/ts/utils/dmplexlandau/plexland.c

src/ts/utils/dmplexlandau/tutorials/ex2.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/utils/dmplexlandau/tutorials/ex1f90.F90

Index of all LANDAU routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petsclandau.h"   
PetscErrorCode DMPlexLandauIFunction(TS ts, PetscReal time_dummy, Vec X, Vec X_t, Vec F, void *actx)
```

Example 2 (unknown):
```unknown
DMPlexLandauCreateVelocitySpace()
```

Example 3 (unknown):
```unknown
DMPlexLandauIJacobian()
```

---

## DMPlexLandauIJacobian#

**URL:** https://petsc.org/release/manualpages/LANDAU/DMPlexLandauIJacobian/

**Contents:**
- DMPlexLandauIJacobian#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#

TS Jacobian construction, confusingly this adds mass

ts - The time stepping context

time_dummy - current time (not used)

U_tdummy - Time derivative of current state (not used)

shift - shift for du/dt term

actx - Landau context

DMPlexLandauCreateVelocitySpace(), DMPlexLandauIFunction()

src/ts/utils/dmplexlandau/plexland.c

src/ts/utils/dmplexlandau/tutorials/ex2.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/utils/dmplexlandau/tutorials/ex1f90.F90

Index of all LANDAU routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petsclandau.h"   
PetscErrorCode DMPlexLandauIJacobian(TS ts, PetscReal time_dummy, Vec X, Vec U_tdummy, PetscReal shift, Mat Amat, Mat Pmat, void *actx)
```

Example 2 (unknown):
```unknown
DMPlexLandauCreateVelocitySpace()
```

Example 3 (unknown):
```unknown
DMPlexLandauIFunction()
```

---

## DMPlexLandauPrintNorms#

**URL:** https://petsc.org/release/manualpages/LANDAU/DMPlexLandauPrintNorms/

**Contents:**
- DMPlexLandauPrintNorms#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

collects moments and prints them

stepi - current step to print

DMPlexLandauCreateVelocitySpace()

src/ts/utils/dmplexlandau/plexland.c

src/ts/utils/dmplexlandau/tutorials/ex2.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/utils/dmplexlandau/tutorials/ex1f90.F90

Index of all LANDAU routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petsclandau.h"   
PetscErrorCode DMPlexLandauPrintNorms(Vec X, PetscInt stepi)
```

Example 2 (unknown):
```unknown
DMPlexLandauCreateVelocitySpace()
```

---

## DTProbDensityType#

**URL:** https://petsc.org/release/manualpages/DT/DTProbDensityType/

**Contents:**
- DTProbDensityType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Names of the built-in probability density functions that PETSc can sample, evaluate, or use to test a Kolmogorov–Smirnov statistic

DTPROB_DENSITY_CONSTANT - uniform density

DTPROB_DENSITY_GAUSSIAN - Gaussian (normal) density

DTPROB_DENSITY_MAXWELL_BOLTZMANN - Maxwell–Boltzmann density (1D/2D/3D variants are provided)

DTPROB_NUM_DENSITY - sentinel; equals the number of meaningful entries in this enumeration

PetscPDFMaxwellBoltzmann1D(), PetscProbComputeKSStatistic(), PetscProbComputeKSStatisticWeighted(), DTProbDensityTypes

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  DTPROB_DENSITY_CONSTANT,
  DTPROB_DENSITY_GAUSSIAN,
  DTPROB_DENSITY_MAXWELL_BOLTZMANN,
  DTPROB_NUM_DENSITY
} DTProbDensityType;
```

Example 2 (unknown):
```unknown
DTPROB_DENSITY_CONSTANT
```

Example 3 (unknown):
```unknown
DTPROB_DENSITY_GAUSSIAN
```

Example 4 (unknown):
```unknown
DTPROB_DENSITY_MAXWELL_BOLTZMANN
```

---

## Dual Spaces (PetscDualSpace)#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/

**Contents:**
- Dual Spaces (PetscDualSpace)#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Single list of manual pages#

The PetscDualSpace class encapsulates a function space that is the dual (https://en.wikipedia.org/wiki/Dual_space) of a PetscSpace class.

PetscDualSpaceDestroy

PetscDualSpaceDuplicate

PetscDualSpaceReferenceCell

PETSCDUALSPACELAGRANGE

PETSCDUALSPACEREFINED

PetscDualSpaceGetDimension

PetscDualSpaceGetFunctional

PetscDualSpaceGetInteriorDimension

PetscDualSpaceGetNumComponents

PetscDualSpaceGetNumDof

PetscDualSpaceGetOrder

PetscDualSpaceGetType

PetscDualSpaceLagrangeGetContinuity

PetscDualSpaceLagrangeGetTensor

PetscDualSpaceLagrangeGetTrimmed

PetscDualSpaceLagrangeSetContinuity

PetscDualSpaceLagrangeSetTensor

PetscDualSpaceLagrangeSetTrimmed

PetscDualSpaceRefinedSetCellSpaces

PetscDualSpaceSetFromOptions

PetscDualSpaceSetNumComponents

PetscDualSpaceSetOrder

PetscDualSpaceSetType

PetscDualSpaceSimpleSetDimension

PetscDualSpaceSimpleSetFunctional

PetscDualSpaceSumGetConcatenate

PetscDualSpaceSumGetNumSubspaces

PetscDualSpaceSumGetSubspace

PetscDualSpaceSumSetConcatenate

PetscDualSpaceSumSetNumSubspaces

PetscDualSpaceSumSetSubspace

PetscDualSpaceTransform

PetscDualSpaceTransformGradient

PetscDualSpaceTransformHessian

PetscDualSpaceTransformType

PetscDualSpaceViewFromOptions

PetscDualSpaceApplyAll

PetscDualSpaceApplyAllDefault

PetscDualSpaceApplyDefault

PetscDualSpaceApplyFVM

PetscDualSpaceApplyInterior

PetscDualSpaceApplyInteriorDefault

PetscDualSpaceCreateAllDataDefault

PetscDualSpaceCreateInteriorDataDefault

PetscDualSpaceCreateSum

PetscDualSpaceGetAllData

PetscDualSpaceGetHeightSubspace

PetscDualSpaceGetInteriorData

PetscDualSpaceGetInteriorSection

PetscDualSpaceGetPointSubspace

PetscDualSpaceGetSection

PetscDualSpaceGetUniform

PetscDualSpaceLagrangeGetMomentOrder

PetscDualSpaceLagrangeGetNodeType

PetscDualSpaceLagrangeGetUseMoments

PetscDualSpaceLagrangeSetMomentOrder

PetscDualSpaceLagrangeSetNodeType

PetscDualSpaceLagrangeSetUseMoments

PetscDualSpacePullback

PetscDualSpacePushforward

PetscDualSpacePushforwardGradient

PetscDualSpacePushforwardHessian

PetscDualSpaceRegister

PetscDualSpaceGetDeRahm

PetscDualSpaceGetFormDegree

PetscDualSpaceGetSymmetries

PetscDualSpaceSetFormDegree

PetscDualSpaceSumGetInterleave

PetscDualSpaceSumSetInterleave

PETSCDUALSPACELAGRANGE

PETSCDUALSPACEREFINED

PetscDualSpaceApplyAll

PetscDualSpaceApplyAllDefault

PetscDualSpaceApplyDefault

PetscDualSpaceApplyFVM

PetscDualSpaceApplyInterior

PetscDualSpaceApplyInteriorDefault

PetscDualSpaceCreateAllDataDefault

PetscDualSpaceCreateInteriorDataDefault

PetscDualSpaceCreateSum

PetscDualSpaceDestroy

PetscDualSpaceDuplicate

PetscDualSpaceGetAllData

PetscDualSpaceGetDeRahm

PetscDualSpaceGetDimension

PetscDualSpaceGetFormDegree

PetscDualSpaceGetFunctional

PetscDualSpaceGetHeightSubspace

PetscDualSpaceGetInteriorData

PetscDualSpaceGetInteriorDimension

PetscDualSpaceGetInteriorSection

PetscDualSpaceGetNumComponents

PetscDualSpaceGetNumDof

PetscDualSpaceGetOrder

PetscDualSpaceGetPointSubspace

PetscDualSpaceGetSection

PetscDualSpaceGetSymmetries

PetscDualSpaceGetType

PetscDualSpaceGetUniform

PetscDualSpaceLagrangeGetContinuity

PetscDualSpaceLagrangeGetMomentOrder

PetscDualSpaceLagrangeGetNodeType

PetscDualSpaceLagrangeGetTensor

PetscDualSpaceLagrangeGetTrimmed

PetscDualSpaceLagrangeGetUseMoments

PetscDualSpaceLagrangeSetContinuity

PetscDualSpaceLagrangeSetMomentOrder

PetscDualSpaceLagrangeSetNodeType

PetscDualSpaceLagrangeSetTensor

PetscDualSpaceLagrangeSetTrimmed

PetscDualSpaceLagrangeSetUseMoments

PetscDualSpacePullback

PetscDualSpacePushforward

PetscDualSpacePushforwardGradient

PetscDualSpacePushforwardHessian

PetscDualSpaceReferenceCell

PetscDualSpaceRefinedSetCellSpaces

PetscDualSpaceRegister

PetscDualSpaceSetFormDegree

PetscDualSpaceSetFromOptions

PetscDualSpaceSetNumComponents

PetscDualSpaceSetOrder

PetscDualSpaceSetType

PetscDualSpaceSimpleSetDimension

PetscDualSpaceSimpleSetFunctional

PetscDualSpaceSumGetConcatenate

PetscDualSpaceSumGetInterleave

PetscDualSpaceSumGetNumSubspaces

PetscDualSpaceSumGetSubspace

PetscDualSpaceSumSetConcatenate

PetscDualSpaceSumSetInterleave

PetscDualSpaceSumSetNumSubspaces

PetscDualSpaceSumSetSubspace

PetscDualSpaceTransform

PetscDualSpaceTransformGradient

PetscDualSpaceTransformHessian

PetscDualSpaceTransformType

PetscDualSpaceViewFromOptions

Function Spaces (PetscSpace)

Finite Elements (PetscFE)

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpace
```

---

## Finite Elements (PetscFE)#

**URL:** https://petsc.org/release/manualpages/FE/

**Contents:**
- Finite Elements (PetscFE)#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Single list of manual pages#

The PetscFE class encapsulates a finite element discretization. Each PetscFE object contains a PetscSpace, its dual PetscDualSpace, and a DMPLEX in the classic Ciarlet triple representation (https://finite-element.github.io/2_finite_elements.html).

There are many SNES Examples using PetscFE, such ex12, ex17, and ex62.

Developer Note: Using an entire DMPLEX object to provide the cell information seems unnecessary and complicated. Why not have a simple PetscCell object that could encapsulate this information. It could then be used by a variety of DM etc.

PetscFECreateFromSpaces

PetscFECreateLagrange

PetscFECreateLagrangeByCell

PetscFECompositeGetMapping

PetscFEComputeTabulation

PetscFECopyQuadrature

PetscFECreateTabulation

PetscFEGeomGetCellPoint

PetscFEGeomRestoreChunk

PetscFEGetCellTabulation

PetscFEGetFaceCentroidTabulation

PetscFEGetFaceQuadrature

PetscFEGetFaceTabulation

PetscFEGetNumComponents

PetscFEGetSpatialDimension

PetscFEIntegrateBdJacobian

PetscFEIntegrateBdResidual

PetscFEIntegrateJacobian

PetscFEIntegrateResidual

PetscFESetFaceQuadrature

PetscFESetFromOptions

PetscFESetNumComponents

PetscFEViewFromOptions

PetscTabulationDestroy

PetscFECreateBrokenElement

PetscFEGetHeightSubspace

PetscFEPushforwardGradient

PetscFEPushforwardHessian

PetscFECreateCellGeometry

PetscFECreateHeightTrace

PetscFEDestroyCellGeometry

PetscFEExpandFaceQuadrature

PetscFEIntegrateHybridJacobian

PetscFEIntegrateHybridResidual

PetscFEOpenCLGetRealType

PetscFEOpenCLSetRealType

PetscFECompositeGetMapping

PetscFEComputeTabulation

PetscFECopyQuadrature

PetscFECreateBrokenElement

PetscFECreateCellGeometry

PetscFECreateFromSpaces

PetscFECreateHeightTrace

PetscFECreateLagrange

PetscFECreateLagrangeByCell

PetscFECreateTabulation

PetscFEDestroyCellGeometry

PetscFEExpandFaceQuadrature

PetscFEGeomGetCellPoint

PetscFEGeomRestoreChunk

PetscFEGetCellTabulation

PetscFEGetFaceCentroidTabulation

PetscFEGetFaceQuadrature

PetscFEGetFaceTabulation

PetscFEGetHeightSubspace

PetscFEGetNumComponents

PetscFEGetSpatialDimension

PetscFEIntegrateBdJacobian

PetscFEIntegrateBdResidual

PetscFEIntegrateHybridJacobian

PetscFEIntegrateHybridResidual

PetscFEIntegrateJacobian

PetscFEIntegrateResidual

PetscFEOpenCLGetRealType

PetscFEOpenCLSetRealType

PetscFEPushforwardGradient

PetscFEPushforwardHessian

PetscFESetFaceQuadrature

PetscFESetFromOptions

PetscFESetNumComponents

PetscFEViewFromOptions

PetscTabulationDestroy

Dual Spaces (PetscDualSpace)

Finite Volumes (PetscFV)

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpace
```

---

## Finite Volumes (PetscFV)#

**URL:** https://petsc.org/release/manualpages/FV/

**Contents:**
- Finite Volumes (PetscFV)#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Single list of manual pages#

The PetscFV class encapsulates a finite volume space.

TS ex11 demonstrates some hyperbolic solvers using PetscFV

PETSCLIMITERVANALBADA

PetscFVCreateDualSpace

PetscFVCreateTabulation

PetscFVGetCellTabulation

PetscFVGetComponentName

PetscFVGetComputeGradients

PetscFVGetNumComponents

PetscFVGetSpatialDimension

PetscFVLeastSquaresSetMaxFaces

PetscFVSetComponentName

PetscFVSetComputeGradients

PetscFVSetFromOptions

PetscFVSetNumComponents

PetscFVSetSpatialDimension

PetscFVViewFromOptions

PetscLimiterSetFromOptions

PetscLimiterViewFromOptions

PetscFVComputeGradient

PetscFVIntegrateRHSFunction

PETSCLIMITERVANALBADA

PetscFVComputeGradient

PetscFVCreateDualSpace

PetscFVCreateTabulation

PetscFVGetCellTabulation

PetscFVGetComponentName

PetscFVGetComputeGradients

PetscFVGetNumComponents

PetscFVGetSpatialDimension

PetscFVIntegrateRHSFunction

PetscFVLeastSquaresSetMaxFaces

PetscFVSetComponentName

PetscFVSetComputeGradients

PetscFVSetFromOptions

PetscFVSetNumComponents

PetscFVSetSpatialDimension

PetscFVViewFromOptions

PetscLimiterSetFromOptions

PetscLimiterViewFromOptions

Finite Elements (PetscFE)

Defining your own mathematical functions (PF)

---

## Function Spaces (PetscSpace)#

**URL:** https://petsc.org/release/manualpages/SPACE/

**Contents:**
- Function Spaces (PetscSpace)#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Single list of manual pages#

The PetscSpace class encapsulates a function space useful for finite element computations with PetscFE. The dual spaces are managed with PetscDualSpace.

PetscSpaceGetDimension

PetscSpaceGetNumComponents

PetscSpaceGetNumVariables

PetscSpacePTrimmedGetFormDegree

PetscSpacePTrimmedSetFormDegree

PetscSpacePointGetPoints

PetscSpacePointSetPoints

PetscSpacePolynomialGetTensor

PetscSpacePolynomialSetTensor

PetscSpaceSetFromOptions

PetscSpaceSetNumComponents

PetscSpaceSetNumVariables

PetscSpaceSumGetConcatenate

PetscSpaceSumGetNumSubspaces

PetscSpaceSumGetSubspace

PetscSpaceSumSetConcatenate

PetscSpaceSumSetNumSubspaces

PetscSpaceSumSetSubspace

PetscSpaceTensorGetNumSubspaces

PetscSpaceTensorGetSubspace

PetscSpaceTensorSetNumSubspaces

PetscSpaceTensorSetSubspace

PetscSpaceViewFromOptions

PetscSpaceCreateSubspace

PetscSpaceGetHeightSubspace

PetscSpaceSumGetInterleave

PetscSpaceSumSetInterleave

PetscSpaceCreateSubspace

PetscSpaceGetDimension

PetscSpaceGetHeightSubspace

PetscSpaceGetNumComponents

PetscSpaceGetNumVariables

PetscSpacePTrimmedGetFormDegree

PetscSpacePTrimmedSetFormDegree

PetscSpacePointGetPoints

PetscSpacePointSetPoints

PetscSpacePolynomialGetTensor

PetscSpacePolynomialSetTensor

PetscSpaceSetFromOptions

PetscSpaceSetNumComponents

PetscSpaceSetNumVariables

PetscSpaceSumGetConcatenate

PetscSpaceSumGetInterleave

PetscSpaceSumGetNumSubspaces

PetscSpaceSumGetSubspace

PetscSpaceSumSetConcatenate

PetscSpaceSumSetInterleave

PetscSpaceSumSetNumSubspaces

PetscSpaceSumSetSubspace

PetscSpaceTensorGetNumSubspaces

PetscSpaceTensorGetSubspace

PetscSpaceTensorSetNumSubspaces

PetscSpaceTensorSetSubspace

PetscSpaceViewFromOptions

Discretization Technology and Quadrature (DT)

Dual Spaces (PetscDualSpace)

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpace
```

---

## LandauCtx#

**URL:** https://petsc.org/release/manualpages/LANDAU/LandauCtx/

**Contents:**
- LandauCtx#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Application context for the DMPLEX Landau collision operator that records the species data, mesh configuration, AMR settings, batching parameters, and pre-computed static data needed to evaluate the operator

The context is created and managed by DMPlexLandauCreateVelocitySpace() and is attached to the returned DM as its application context. User code normally obtains it with DMGetApplicationContext() rather than constructing it directly.

DMPlexLandauCreateVelocitySpace(), DMPlexLandauDestroyVelocitySpace(), DMPlexLandauIFunction(), DMPlexLandauIJacobian(), LandauStaticData, LandauDeviceType, LandauOMPTimers

include/petsclandau.h

src/ts/utils/dmplexlandau/tutorials/ex2.c src/ts/utils/dmplexlandau/tutorials/ex1.c

Index of all LANDAU routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (sass):
```sass
#include "petscdmplex.h"    
typedef struct {
  PetscBool interpolate; /* Generate intermediate mesh elements */
  PetscBool gpu_assembly;
  MPI_Comm  comm; /* global communicator to use for errors and diagnostics */
  double    times[LANDAU_NUM_TIMERS];
  PetscBool use_matrix_mass;
  /* FE */
  PetscFE fe[LANDAU_MAX_SPECIES];
  /* geometry  */
  PetscReal radius[LANDAU_MAX_GRIDS];
  PetscReal radius_par[LANDAU_MAX_GRIDS];
  PetscReal radius_perp[LANDAU_MAX_GRIDS];
  PetscReal re_radius;      /* RE: radius of refinement along v_perp=0, z>0 */
  PetscReal vperp0_radius1; /* RE: radius of refinement along v_perp=0 */
  PetscReal vperp0_radius2; /* RE: radius of refinement along v_perp=0 after origin AMR refinement */
  PetscBool sphere;
  PetscBool map_sphere;
  PetscReal sphere_inner_radius_90degree[LANDAU_MAX_GRIDS];
  PetscReal sphere_inner_radius_45degree[LANDAU_MAX_GRIDS];
  PetscInt  cells0[3];
  /* AMR */
  PetscBool use_p4est;
  PetscInt  numRERefine;                     /* RE: refinement along v_perp=0, z > 0 */
  PetscInt  nZRefine1;                       /* RE: origin refinement after v_perp=0 refinement */
  PetscInt  nZRefine2;                       /* RE: origin refinement after origin AMR refinement */
  PetscInt  numAMRRefine[LANDAU_MAX_GRIDS];  /* normal AMR - refine from origin */
  PetscInt  postAMRRefine[LANDAU_MAX_GRIDS]; /* uniform refinement of AMR */
  PetscBool simplex;
  char      filename[PETSC_MAX_PATH_LEN];
  PetscReal thermal_speed[LANDAU_MAX_GRIDS];
  PetscBool sphere_uniform_normal;
  /* relativistic */
  PetscBool use_energy_tensor_trick;
  PetscBool use_relativistic_corrections;
  /* physics */
  PetscReal thermal_temps[LANDAU_MAX_SPECIES];
  PetscReal masses[LANDAU_MAX_SPECIES];  /* mass of each species  */
  PetscReal charges[LANDAU_MAX_SPECIES]; /* charge of each species  */
  PetscReal n[LANDAU_MAX_SPECIES];       /* number density of each species  */
  PetscReal m_0;                         /* reference mass */
  PetscReal v_0;                         /* reference velocity */
  PetscReal n_0;                         /* reference number density */
  PetscReal t_0;                         /* reference time */
  PetscReal Ez;
  PetscReal epsilon0;
  PetscReal k;
  PetscReal lambdas[LANDAU_MAX_GRIDS][LANDAU_MAX_GRIDS];
  PetscReal electronShift;
  PetscInt  num_species;
  PetscInt  num_grids;
  PetscInt  species_offset[LANDAU_MAX_GRIDS + 1]; // for each grid, but same for all batched vertices
  PetscInt  mat_offset[LANDAU_MAX_GRIDS + 1];     // for each grid, but same for all batched vertices
  // batching
  PetscBool  jacobian_field_major_order; // this could be a type but lets not get pedantic
  VecScatter plex_batch;
  Vec        work_vec;
  IS         batch_is;
  PetscErrorCode (*seqaij_mult)(Mat, Vec, Vec);
  PetscErrorCode (*seqaij_multtranspose)(Mat, Vec, Vec);
  PetscErrorCode (*seqaij_solve)(Mat, Vec, Vec);
  PetscErrorCode (*seqaij_getdiagonal)(Mat, Vec);
  /* COO */
  Mat J;
  Mat M;
  Vec X;
  /* derived type */
  void *data;
  /* computing */
  LandauDeviceType deviceType;
  DM               pack;
  DM               plex[LANDAU_MAX_GRIDS];
  LandauStaticData SData_d; /* static geometric data on device */
  /* diagnostics */
  PetscInt         verbose;
  PetscLogEvent    events[20];
  PetscLogStage    stage;
  PetscObjectState norm_state;
  PetscInt         batch_sz;
  PetscInt         batch_view_idx;
} LandauCtx;
```

Example 2 (unknown):
```unknown
DMPlexLandauCreateVelocitySpace()
```

Example 3 (unknown):
```unknown
DMGetApplicationContext()
```

Example 4 (unknown):
```unknown
DMPlexLandauCreateVelocitySpace()
```

---

## LandauDeviceType#

**URL:** https://petsc.org/release/manualpages/LANDAU/LandauDeviceType/

**Contents:**
- LandauDeviceType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Selects the backend used to evaluate the Landau collision-operator Jacobian and to hold its workspace data

LANDAU_KOKKOS - run on the device with the Kokkos backend (requires PETSc configured --with-kokkos)

LANDAU_CPU - run on the host (default when Kokkos is not enabled)

DMPlexLandauCreateVelocitySpace(), LandauCtx, LandauStaticData

include/petsclandau.h

Index of all LANDAU routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h"    
typedef enum {
  LANDAU_KOKKOS,
  LANDAU_CPU
} LandauDeviceType;
```

Example 2 (unknown):
```unknown
LANDAU_KOKKOS
```

Example 3 (unknown):
```unknown
--with-kokkos
```

Example 4 (unknown):
```unknown
DMPlexLandauCreateVelocitySpace()
```

---

## LandauIdx#

**URL:** https://petsc.org/release/manualpages/LANDAU/LandauIdx/

**Contents:**
- LandauIdx#
- Note#
- See Also#
- Level#
- Location#

Integer type used to index entries in the DMPLEX Landau collision-operator data structures, such as the COO matrix workspaces and the P4estVertexMaps reduced-quadrature maps

LandauIdx is a PetscInt; it is named separately so the device-side data structures used by the Landau collision operator can be sized independently from the rest of PETSc if needed.

DMPlexLandauCreateVelocitySpace(), LandauStaticData, LandauCtx, P4estVertexMaps

include/petsclandau.h

Index of all LANDAU routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
P4estVertexMaps
```

Example 2 (unknown):
```unknown
DMPlexLandauCreateVelocitySpace()
```

Example 3 (unknown):
```unknown
LandauStaticData
```

Example 4 (unknown):
```unknown
P4estVertexMaps
```

---

## LandauKokkosCreateMatMaps#

**URL:** https://petsc.org/release/manualpages/LANDAU/LandauKokkosCreateMatMaps/

**Contents:**
- LandauKokkosCreateMatMaps#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Build the Kokkos device-side P4estVertexMaps used by the DMPLEX Landau collision operator from its host-side reduced quadrature-point map

Not Collective; No Fortran Support

maps - array of vertex-map structs, one per grid, whose device-side representation is to be created

pointMaps - host-side reduced quadrature-point maps, indexed by element and face quadrature point

Nf - number of fields (species) per grid

grid - index of the grid for which to build the device-side map

This is called by DMPlexLandauCreateVelocitySpace() when the Kokkos backend is selected; it is not intended to be called directly by user code.

LandauKokkosDestroyMatMaps(), LandauCtx, LandauDeviceType, LandauStaticData, pointInterpolationP4est

src/ts/utils/dmplexlandau/kokkos/landau.kokkos.cxx

Index of all LANDAU routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
P4estVertexMaps
```

Example 2 (unknown):
```unknown
#include "petscdmplex.h"   
PetscErrorCode LandauKokkosCreateMatMaps(P4estVertexMaps maps[], pointInterpolationP4est (*pointMaps)[LANDAU_MAX_Q_FACE], PetscInt Nf[], PetscInt grid)
```

Example 3 (unknown):
```unknown
DMPlexLandauCreateVelocitySpace()
```

Example 4 (unknown):
```unknown
LandauKokkosDestroyMatMaps()
```

---

## LandauKokkosDestroyMatMaps#

**URL:** https://petsc.org/release/manualpages/LANDAU/LandauKokkosDestroyMatMaps/

**Contents:**
- LandauKokkosDestroyMatMaps#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Free the Kokkos-backed vertex maps created with LandauKokkosCreateMatMaps()

Not Collective; No Fortran Support

maps - array of vertex-map structs, one per grid, whose device-side resources are to be freed

num_grids - number of grids (length of maps)

LandauKokkosCreateMatMaps(), LandauCtx, LandauStaticData, P4estVertexMaps

src/ts/utils/dmplexlandau/kokkos/landau.kokkos.cxx

Index of all LANDAU routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
LandauKokkosCreateMatMaps()
```

Example 2 (unknown):
```unknown
#include "petscdmplex.h"   
PetscErrorCode LandauKokkosDestroyMatMaps(P4estVertexMaps maps[], PetscInt num_grids)
```

Example 3 (unknown):
```unknown
LandauKokkosCreateMatMaps()
```

Example 4 (unknown):
```unknown
LandauStaticData
```

---

## LandauKokkosJacobian#

**URL:** https://petsc.org/release/manualpages/LANDAU/LandauKokkosJacobian/

**Contents:**
- LandauKokkosJacobian#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Kokkos backend for assembling the Landau collision-operator Jacobian for the DMPlex Landau time integrator

Collective; No Fortran Support

plex - per-grid DMPLEX array (length num_grids)

Nq - number of quadrature points per element

Nb - number of basis functions per element

batch_sz - number of batched vertices

num_grids - number of grids

a_numCells - per-grid cell counts (length num_grids)

a_Eq_m - per-species external-force coefficients (length equal to the total number of species)

a_elem_closure - host element-closure data used as input when the input vector is not on the device, otherwise NULL

a_xarray - device input-vector data used when a_elem_closure is NULL

SData_d - precomputed static device data created with LandauKokkosStaticDataSet()

shift - time-integrator shift applied to the mass term of the Jacobian

events - array of PetscLogEvent identifiers used to time the operator phases

a_mat_offset - per-grid offset into the flattened matrix-block arrays (length num_grids + 1)

a_species_offset - per-grid offset into the flattened species arrays (length num_grids + 1)

subJ - per-grid sub-Jacobian matrices, one entry per (grid, batch) pair (used when assembling the matrix from a global ordering)

JacP - the assembled full Jacobian matrix

Called internally by the Landau operator setup; users go through DMPlexLandauIJacobian().

DMPlexLandauCreateVelocitySpace(), DMPlexLandauIJacobian(), LandauKokkosStaticDataSet(), LandauStaticData, LandauCtx

src/ts/utils/dmplexlandau/kokkos/landau.kokkos.cxx

Index of all LANDAU routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h"   
PetscErrorCode LandauKokkosJacobian(DM plex[], const PetscInt Nq, const PetscInt Nb, const PetscInt batch_sz, const PetscInt num_grids, const PetscInt a_numCells[], PetscReal a_Eq_m[], PetscScalar a_elem_closure[], const PetscScalar a_xarray[], const LandauStaticData *SData_d, const PetscReal shift, const PetscLogEvent events[], const PetscInt a_mat_offset[], const PetscInt a_species_offset[], Mat subJ[], Mat JacP)
```

Example 2 (unknown):
```unknown
a_elem_closure
```

Example 3 (unknown):
```unknown
LandauKokkosStaticDataSet()
```

Example 4 (unknown):
```unknown
PetscLogEvent
```

---

## LandauKokkosStaticDataClear#

**URL:** https://petsc.org/release/manualpages/LANDAU/LandauKokkosStaticDataClear/

**Contents:**
- LandauKokkosStaticDataClear#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Clears precomputed Landau quadrature and species data from device-resident Kokkos views

Collective; No Fortran Support

SData_d - the LandauStaticData workspace whose device-resident Kokkos views are to be freed

LandauKokkosStaticDataSet(), LandauKokkosJacobian(), LandauStaticData, LandauCtx

src/ts/utils/dmplexlandau/kokkos/landau.kokkos.cxx

Index of all LANDAU routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h"   
PetscErrorCode LandauKokkosStaticDataClear(LandauStaticData *SData_d)
```

Example 2 (unknown):
```unknown
LandauStaticData
```

Example 3 (unknown):
```unknown
LandauKokkosStaticDataSet()
```

Example 4 (unknown):
```unknown
LandauKokkosJacobian()
```

---

## LandauKokkosStaticDataSet#

**URL:** https://petsc.org/release/manualpages/LANDAU/LandauKokkosStaticDataSet/

**Contents:**
- LandauKokkosStaticDataSet#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Copy precomputed Landau quadrature and species data to device-resident Kokkos views for use by LandauKokkosJacobian()

Collective; No Fortran Support

plex - the DMPLEX used to obtain the spatial dimension and discretization tabulation

Nq - number of quadrature points per element

Nb - number of basis functions per element

batch_sz - number of batched vertices

num_grids - number of grids

a_numCells - per-grid cell counts (length num_grids)

a_species_offset - per-grid offset into the flattened species arrays (length num_grids + 1)

a_mat_offset - per-grid offset into the flattened matrix-block arrays (length num_grids + 1)

a_nu_alpha - flattened per-species nu alpha collision coefficients

a_nu_beta - flattened per-species nu beta collision coefficients

a_invMass - flattened per-species inverse mass

a_lambdas - flattened grid-pair lambda array of length LANDAU_MAX_GRIDS * LANDAU_MAX_GRIDS

a_invJ - inverse Jacobians at every quadrature point (length nip * dim * dim)

a_x - quadrature-point x coordinates (length nip)

a_y - quadrature-point y coordinates (length nip)

a_z - quadrature-point z coordinates (length nip, used only when dim == 3)

a_w - quadrature weights at every quadrature point (length nip)

SData_d - the LandauStaticData workspace whose device-resident Kokkos views are allocated and populated

Called by DMPlexLandauCreateVelocitySpace() when the Kokkos backend is selected; not intended for direct user calls.

LandauKokkosStaticDataClear(), LandauKokkosJacobian(), LandauStaticData, LandauCtx, DMPlexLandauCreateVelocitySpace()

src/ts/utils/dmplexlandau/kokkos/landau.kokkos.cxx

Index of all LANDAU routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
LandauKokkosJacobian()
```

Example 2 (unknown):
```unknown
#include "petscdmplex.h"   
PetscErrorCode LandauKokkosStaticDataSet(DM plex, const PetscInt Nq, const PetscInt Nb, const PetscInt batch_sz, const PetscInt num_grids, PetscInt a_numCells[], PetscInt a_species_offset[], PetscInt a_mat_offset[], PetscReal a_nu_alpha[], PetscReal a_nu_beta[], PetscReal a_invMass[], PetscReal a_lambdas[], PetscReal a_invJ[], PetscReal a_x[], PetscReal a_y[], PetscReal a_z[], PetscReal a_w[], LandauStaticData *SData_d)
```

Example 3 (unknown):
```unknown
num_grids + 1
```

Example 4 (unknown):
```unknown
num_grids + 1
```

---

## LandauOMPTimers#

**URL:** https://petsc.org/release/manualpages/LANDAU/LandauOMPTimers/

**Contents:**
- LandauOMPTimers#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Identifiers for the timing slots kept in LandauCtx.times[] for the DMPLEX Landau collision operator

LANDAU_EX2_TSSOLVE - total TSSolve() time of the Landau example

LANDAU_MATRIX_TOTAL - total time spent constructing the Jacobian and mass matrices

LANDAU_OPERATOR - time inside the Landau operator evaluation

LANDAU_JACOBIAN_COUNT - number of Jacobian evaluations (stored as a count, reused as a timer slot)

LANDAU_JACOBIAN - time inside Jacobian construction

LANDAU_MASS - time inside mass-matrix construction

LANDAU_F_DF - time evaluating the distribution function and its derivatives

LANDAU_KERNEL - time inside the Landau collision kernel

KSP_FACTOR - time inside the KSP factor stage when using a direct solver

KSP_SOLVE - time inside KSPSolve()

LANDAU_NUM_TIMERS - sentinel; equals the number of timer slots allocated in LandauCtx

LandauCtx, DMPlexLandauCreateVelocitySpace()

include/petsclandau.h

Index of all LANDAU routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
LandauCtx.times[]
```

Example 2 (unknown):
```unknown
#include "petscdmplex.h"    
typedef enum {
  LANDAU_EX2_TSSOLVE,
  LANDAU_MATRIX_TOTAL,
  LANDAU_OPERATOR,
  LANDAU_JACOBIAN_COUNT,
  LANDAU_JACOBIAN,
  LANDAU_MASS,
  LANDAU_F_DF,
  LANDAU_KERNEL,
  KSP_FACTOR,
  KSP_SOLVE,
  LANDAU_NUM_TIMERS
} LandauOMPTimers;
```

Example 3 (unknown):
```unknown
LANDAU_EX2_TSSOLVE
```

Example 4 (unknown):
```unknown
LANDAU_MATRIX_TOTAL
```

---

## LandauStaticData#

**URL:** https://petsc.org/release/manualpages/LANDAU/LandauStaticData/

**Contents:**
- LandauStaticData#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#

Workspace of pre-computed quadrature, geometry, and physics data that is shared by every Jacobian assembly of the DMPLEX Landau collision operator

The fields are typed as void * so that the same struct can hold either host arrays or device (Kokkos/CUDA/HIP) arrays depending on LandauDeviceType. The contents are managed by DMPlexLandauCreateVelocitySpace() and friends and are not intended to be inspected by user code.

DMPlexLandauCreateVelocitySpace(), LandauCtx, LandauDeviceType, LandauIdx

include/petsclandau.h

Index of all LANDAU routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (elixir):
```elixir
#include "petscdmplex.h"    
typedef struct {
  void *invJ;    // nip*dim*dim
  void *D;       // nq*nb*dim
  void *B;       // nq*nb
  void *alpha;   // ns
  void *beta;    // ns
  void *invMass; // ns
  void *w;       // nip
  void *x;       // nip
  void *y;       // nip
  void *z;       // nip
  void *Eq_m;    // ns - dynamic
  void *f;       //  nip*Nf - dynamic (IP)
  void *dfdx;    // nip*Nf - dynamic (IP)
  void *dfdy;    // nip*Nf - dynamic (IP)
  void *dfdz;    // nip*Nf - dynamic (IP)
  int   dim_, ns_, nip_, nq_, nb_;
  void *NCells;         // remove and use elem_offset - TODO
  void *species_offset; // for each grid, but same for all batched vertices
  void *mat_offset;     // for each grid, but same for all batched vertices
  void *elem_offset;    // for each grid, but same for all batched vertices
  void *ip_offset;      // for each grid, but same for all batched vertices
  void *ipf_offset;     // for each grid, but same for all batched vertices
  void *ipfdf_data;     // for each grid, but same for all batched vertices
  void *maps;           // for each grid, but same for all batched vertices
  // COO
  void     *coo_elem_offsets;
  void     *coo_elem_point_offsets;
  void     *coo_elem_fullNb;
  void     *coo_vals;
  void     *lambdas;
  LandauIdx coo_n_cellsTot;
  LandauIdx coo_size;
  LandauIdx coo_max_fullnb;
} LandauStaticData;
```

Example 2 (unknown):
```unknown
LandauDeviceType
```

Example 3 (unknown):
```unknown
DMPlexLandauCreateVelocitySpace()
```

Example 4 (unknown):
```unknown
DMPlexLandauCreateVelocitySpace()
```

---

## Landau Collision Operator#

**URL:** https://petsc.org/release/manualpages/LANDAU/

**Contents:**
- Landau Collision Operator#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Single list of manual pages#

The LANDAU class implements an AMR discretization of the Fokker-Planck collision operator in Landau form using DMPlex and DMForest, within TS function and Jacobian methods.

DMPlexLandauAddMaxwellians

DMPlexLandauCreateMassMatrix

DMPlexLandauCreateVelocitySpace

DMPlexLandauDestroyVelocitySpace

DMPlexLandauIFunction

DMPlexLandauIJacobian

DMPlexLandauPrintNorms

LandauKokkosCreateMatMaps

LandauKokkosDestroyMatMaps

LandauKokkosStaticDataClear

LandauKokkosStaticDataSet

pointInterpolationP4est

DMPlexLandauAddMaxwellians

DMPlexLandauCreateMassMatrix

DMPlexLandauCreateVelocitySpace

DMPlexLandauDestroyVelocitySpace

DMPlexLandauIFunction

DMPlexLandauIJacobian

DMPlexLandauPrintNorms

LandauKokkosCreateMatMaps

LandauKokkosDestroyMatMaps

LandauKokkosStaticDataClear

LandauKokkosStaticDataSet

pointInterpolationP4est

Defining your own mathematical functions (PF)

Linear Solvers and Preconditioners

---

## PetscBdPointFn#

**URL:** https://petsc.org/release/manualpages/DT/PetscBdPointFn/

**Contents:**
- PetscBdPointFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#
- Examples#

A prototype of a pointwise boundary function that can be passed to, for example, PetscDSSetBdResidual()

dim - the coordinate dimension

Nf - the number of fields

NfAux - the number of auxiliary fields

uOff - the offset into u[] and u_t[] for each field

uOff_x - the offset into u_x[] for each field

u - each field evaluated at the current point

u_t - the time derivative of each field evaluated at the current point

u_x - the gradient of each field evaluated at the current point

aOff - the offset into a[] and a_t[] for each auxiliary field

aOff_x - the offset into a_x[] for each auxiliary field

a - each auxiliary field evaluated at the current point

a_t - the time derivative of each auxiliary field evaluated at the current point

a_x - the gradient of auxiliary each field evaluated at the current point

x - coordinates of the current point

n - unit normal at the current point

numConstants - number of constant parameters

constants - constant parameters

f - output values at the current point

PetscPointFn, PetscDSSetBdResidual(), PetscDSGetBdResidual(), PetscDSSetObjective(), PetscDSGetObjective(), PetscDSGetResidual(), PetscDSGetRHSResidual(), PetscDSSetUpdate(), PetscDSGetUpdate(), DMPlexSetCoordinateMap(), PetscDSSetResidual(), PetscPointJacFn

include/petscdstypes.h

src/snes/tutorials/ex12.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDSSetBdResidual()
```

Example 2 (cpp):
```cpp
PETSC_EXTERN_TYPEDEF typedef void PetscBdPointFn(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f[]);
```

Example 3 (unknown):
```unknown
PetscPointFn
```

Example 4 (unknown):
```unknown
PetscDSSetBdResidual()
```

---

## PetscBdPointJacFn#

**URL:** https://petsc.org/release/manualpages/DT/PetscBdPointJacFn/

**Contents:**
- PetscBdPointJacFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

A prototype of a pointwise boundary function that can be passed to, for example, PetscDSSetBdJacobian()

dim - the coordinate dimension

Nf - the number of fields

NfAux - the number of auxiliary fields

uOff - the offset into u[] and u_t[] for each field

uOff_x - the offset into u_x[] for each field

u - each field evaluated at the current point

u_t - the time derivative of each field evaluated at the current point

u_x - the gradient of each field evaluated at the current point

aOff - the offset into a[] and a_t[] for each auxiliary field

aOff_x - the offset into a_x[] for each auxiliary field

a - each auxiliary field evaluated at the current point

a_t - the time derivative of each auxiliary field evaluated at the current point

a_x - the gradient of auxiliary each field evaluated at the current point

u_tShift - the multiplier a for \(dF/dU_t\)

x - coordinates of the current point

n - normal at the current point

numConstants - number of constant parameters

constants - constant parameters

g - output values at the current point

PetscPointFn, PetscDSSetBdJacobian(), PetscDSGetBdJacobian(), PetscDSSetBdJacobianPreconditioner(), PetscDSGetBdJacobianPreconditioner(), PetscDSSetBdResidual(), PetscDSGetBdResidual(), PetscDSSetObjective(), PetscDSGetObjective(), PetscDSGetResidual(), PetscDSGetRHSResidual(), PetscDSSetUpdate(), PetscDSGetUpdate(), DMPlexSetCoordinateMap(), PetscDSSetResidual(), PetscPointJacFn

include/petscdstypes.h

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDSSetBdJacobian()
```

Example 2 (cpp):
```cpp
PETSC_EXTERN_TYPEDEF typedef void PetscBdPointJacFn(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g0[]);
```

Example 3 (unknown):
```unknown
PetscPointFn
```

Example 4 (unknown):
```unknown
PetscDSSetBdJacobian()
```

---

## PetscCDFConstant1D#

**URL:** https://petsc.org/release/manualpages/DT/PetscCDFConstant1D/

**Contents:**
- PetscCDFConstant1D#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

CDF for the uniform distribution in 1D

x - Coordinate in \([-1, 1]\)

p - The cumulative probability at x

PetscPDFConstant1D(), PetscPDFSampleConstant1D(), PetscCDFConstant2D(), PetscCDFConstant3D()

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscCDFConstant1D(const PetscReal x[], const PetscReal unused[], PetscReal p[])
```

Example 2 (unknown):
```unknown
PetscPDFConstant1D()
```

Example 3 (unknown):
```unknown
PetscPDFSampleConstant1D()
```

Example 4 (unknown):
```unknown
PetscCDFConstant2D()
```

---

## PetscCDFConstant2D#

**URL:** https://petsc.org/release/manualpages/DT/PetscCDFConstant2D/

**Contents:**
- PetscCDFConstant2D#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

CDF for the uniform distribution in 2D

x - Coordinate in \([-1, 1]^2\)

p - The cumulative probability at x

PetscPDFConstant2D(), PetscPDFSampleConstant2D(), PetscCDFConstant1D(), PetscCDFConstant3D()

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscCDFConstant2D(const PetscReal x[], const PetscReal unused[], PetscReal p[])
```

Example 2 (unknown):
```unknown
PetscPDFConstant2D()
```

Example 3 (unknown):
```unknown
PetscPDFSampleConstant2D()
```

Example 4 (unknown):
```unknown
PetscCDFConstant1D()
```

---

## PetscCDFConstant3D#

**URL:** https://petsc.org/release/manualpages/DT/PetscCDFConstant3D/

**Contents:**
- PetscCDFConstant3D#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

CDF for the uniform distribution in 3D

x - Coordinate in \([-1, 1]^3\)

p - The cumulative probability at x

PetscPDFConstant3D(), PetscPDFSampleConstant3D(), PetscCDFConstant1D(), PetscCDFConstant2D()

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscCDFConstant3D(const PetscReal x[], const PetscReal unused[], PetscReal p[])
```

Example 2 (unknown):
```unknown
PetscPDFConstant3D()
```

Example 3 (unknown):
```unknown
PetscPDFSampleConstant3D()
```

Example 4 (unknown):
```unknown
PetscCDFConstant1D()
```

---

## PetscCDFMaxwellBoltzmann1D#

**URL:** https://petsc.org/release/manualpages/DT/PetscCDFMaxwellBoltzmann1D/

**Contents:**
- PetscCDFMaxwellBoltzmann1D#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

CDF for the Maxwell-Boltzmann distribution in 1D

x - Speed in \([0, \infty]\)

p - The probability density at x

PetscPDFMaxwellBoltzmann1D()

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscCDFMaxwellBoltzmann1D(const PetscReal x[], const PetscReal unused[], PetscReal p[])
```

Example 2 (unknown):
```unknown
PetscPDFMaxwellBoltzmann1D()
```

---

## PetscCDFMaxwellBoltzmann2D#

**URL:** https://petsc.org/release/manualpages/DT/PetscCDFMaxwellBoltzmann2D/

**Contents:**
- PetscCDFMaxwellBoltzmann2D#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

CDF for the Maxwell-Boltzmann distribution in 2D

x - Speed in \([0, \infty]\)

p - The probability density at x

PetscPDFMaxwellBoltzmann2D()

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscCDFMaxwellBoltzmann2D(const PetscReal x[], const PetscReal unused[], PetscReal p[])
```

Example 2 (unknown):
```unknown
PetscPDFMaxwellBoltzmann2D()
```

---

## PetscCDFMaxwellBoltzmann3D#

**URL:** https://petsc.org/release/manualpages/DT/PetscCDFMaxwellBoltzmann3D/

**Contents:**
- PetscCDFMaxwellBoltzmann3D#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

CDF for the Maxwell-Boltzmann distribution in 3D

x - Speed in \([0, \infty]\)

p - The probability density at x

PetscPDFMaxwellBoltzmann3D()

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscCDFMaxwellBoltzmann3D(const PetscReal x[], const PetscReal unused[], PetscReal p[])
```

Example 2 (unknown):
```unknown
PetscPDFMaxwellBoltzmann3D()
```

---

## PetscDiscType#

**URL:** https://petsc.org/release/manualpages/DT/PetscDiscType/

**Contents:**
- PetscDiscType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Identifies the discretization family attached to a PetscDS field

PETSC_DISC_NONE - no discretization (or one not known to PETSc) is attached

PETSC_DISC_FE - a PetscFE finite-element discretization is attached

PETSC_DISC_FV - a PetscFV finite-volume discretization is attached

PetscDS, PetscFE, PetscFV, PetscDSGetDiscretization()

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  PETSC_DISC_NONE,
  PETSC_DISC_FE,
  PETSC_DISC_FV
} PetscDiscType;
```

Example 2 (unknown):
```unknown
PETSC_DISC_NONE
```

Example 3 (unknown):
```unknown
PETSC_DISC_FE
```

Example 4 (unknown):
```unknown
PETSC_DISC_FV
```

---

## PetscDSAddBoundaryByName#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSAddBoundaryByName/

**Contents:**
- PetscDSAddBoundaryByName#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Calling Sequence of bcFunc and bcFunc_t#
- Notes#
- See Also#
- Level#
- Location#

Add a boundary condition to the model.

ds - The PetscDS object

type - The type of condition, e.g. DM_BC_ESSENTIAL/DM_BC_ESSENTIAL_FIELD (Dirichlet), or DM_BC_NATURAL (Neumann)

name - The boundary condition name

lname - The name of the label defining constrained points

Nv - The number of DMLabel values for constrained points

values - An array of label values for constrained points

field - The field to constrain

Nc - The number of constrained field components (0 will constrain all fields)

comps - An array of constrained component numbers

bcFunc - A pointwise function giving boundary values

bcFunc_t - A pointwise function giving the time derivative of the boundary values, or NULL

ctx - An optional application context for bcFunc

bd - The boundary number

-bc_NAME values - comma separated list of values for the boundary condition NAME

-bc_NAME_comp comps - comma separated list of components for the boundary condition NAME

If the type is DM_BC_ESSENTIAL

If the type is DM_BC_ESSENTIAL_FIELD or other _FIELD value,

dim - the coordinate dimension

Nf - the number of fields

uOff - the offset into u[] and u_t[] for each field

uOff_x - the offset into u_x[] for each field

u - each field evaluated at the current point

u_t - the time derivative of each field evaluated at the current point

u_x - the gradient of each field evaluated at the current point

aOff - the offset into a[] and a_t[] for each auxiliary field

aOff_x - the offset into a_x[] for each auxiliary field

a - each auxiliary field evaluated at the current point

a_t - the time derivative of each auxiliary field evaluated at the current point

a_x - the gradient of auxiliary each field evaluated at the current point

x - coordinates of the current point

numConstants - number of constant parameters

constants - constant parameters

bcval - output values at the current point

The pointwise functions are used to provide boundary values for essential boundary conditions. In FEM, they are acting upon by dual basis functionals to generate FEM coefficients which are fixed. Natural boundary conditions signal to PETSc that boundary integrals should be performed, using the kernels from PetscDSSetBdResidual().

This function should only be used with DMFOREST currently, since labels cannot be defined before the underlying DMPLEX is built.

PetscDS, PetscWeakForm, DMLabel, DMBoundaryConditionType, PetscDSAddBoundary(), PetscDSGetBoundary(), PetscDSSetResidual(), PetscDSSetBdResidual()

src/dm/dt/interface/dtds.c

src/snes/tutorials/ex12.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSAddBoundaryByName(PetscDS ds, DMBoundaryConditionType type, const char name[], const char lname[], PetscInt Nv, const PetscInt values[], PetscInt field, PetscInt Nc, const PetscInt comps[], PetscVoidFn *bcFunc, PetscVoidFn *bcFunc_t, PetscCtx ctx, PetscInt *bd)
```

Example 2 (unknown):
```unknown
DM_BC_ESSENTIAL
```

Example 3 (unknown):
```unknown
DM_BC_ESSENTIAL_FIELD
```

Example 4 (unknown):
```unknown
DM_BC_NATURAL
```

---

## PetscDSAddBoundary#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSAddBoundary/

**Contents:**
- PetscDSAddBoundary#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Note#
- Notes#
- See Also#
- Level#
- Location#

Add a boundary condition to the model.

ds - The PetscDS object

type - The type of condition, e.g. DM_BC_ESSENTIAL/DM_BC_ESSENTIAL_FIELD (Dirichlet), or DM_BC_NATURAL (Neumann)

name - The name for the boundary condition

label - The label defining constrained points

Nv - The number of DMLabel values for constrained points

values - An array of label values for constrained points

field - The field to constrain

Nc - The number of constrained field components (0 will constrain all fields)

comps - An array of constrained component numbers

bcFunc - A pointwise function giving boundary values

bcFunc_t - A pointwise function giving the time derivative of the boundary values, or NULL

ctx - An optional application context for bcFunc

bd - The boundary number

-bc_NAME values - comma separated list of values for the boundary condition NAME

-bc_NAME_comp comps - comma separated list of components for the boundary condition NAME

Both bcFunc and bcFunc_t will depend on the boundary condition type. If the type if DM_BC_ESSENTIAL, then the calling sequence is:

If the type is DM_BC_ESSENTIAL_FIELD or other _FIELD value, then the calling sequence is:

dim - the coordinate dimension

Nf - the number of fields

uOff - the offset into u[] and u_t[] for each field

uOff_x - the offset into u_x[] for each field

u - each field evaluated at the current point

u_t - the time derivative of each field evaluated at the current point

u_x - the gradient of each field evaluated at the current point

aOff - the offset into a[] and a_t[] for each auxiliary field

aOff_x - the offset into a_x[] for each auxiliary field

a - each auxiliary field evaluated at the current point

a_t - the time derivative of each auxiliary field evaluated at the current point

a_x - the gradient of auxiliary each field evaluated at the current point

x - coordinates of the current point

numConstants - number of constant parameters

constants - constant parameters

bcval - output values at the current point

The pointwise functions are used to provide boundary values for essential boundary conditions. In FEM, they are acting upon by dual basis functionals to generate FEM coefficients which are fixed. Natural boundary conditions signal to PETSc that boundary integrals should be performed, using the kernels from PetscDSSetBdResidual().

PetscDS, PetscWeakForm, DMLabel, DMBoundaryConditionType, PetscDSAddBoundaryByName(), PetscDSGetBoundary(), PetscDSSetResidual(), PetscDSSetBdResidual()

src/dm/dt/interface/dtds.c

src/ts/tutorials/ex11.c src/snes/tutorials/ex76.c src/ts/tutorials/ex76.c src/ts/tutorials/ex48.c src/ts/tutorials/ex77.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSAddBoundary(PetscDS ds, DMBoundaryConditionType type, const char name[], DMLabel label, PetscInt Nv, const PetscInt values[], PetscInt field, PetscInt Nc, const PetscInt comps[], PetscVoidFn *bcFunc, PetscVoidFn *bcFunc_t, PetscCtx ctx, PetscInt *bd)
```

Example 2 (unknown):
```unknown
DM_BC_ESSENTIAL
```

Example 3 (unknown):
```unknown
DM_BC_ESSENTIAL_FIELD
```

Example 4 (unknown):
```unknown
DM_BC_NATURAL
```

---

## PetscDSAddDiscretization#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSAddDiscretization/

**Contents:**
- PetscDSAddDiscretization#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Adds a discretization object

prob - The PetscDS object

disc - The discretization object, this can be a PetscFE or PetscFV

PetscWeakForm, PetscFE, PetscFV, PetscDSGetDiscretization(), PetscDSSetDiscretization(), PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSAddDiscretization(PetscDS prob, PetscObject disc)
```

Example 2 (unknown):
```unknown
PetscWeakForm
```

Example 3 (unknown):
```unknown
PetscDSGetDiscretization()
```

Example 4 (unknown):
```unknown
PetscDSSetDiscretization()
```

---

## PETSCDSBASIC#

**URL:** https://petsc.org/release/manualpages/DT/PETSCDSBASIC/

**Contents:**
- PETSCDSBASIC#
- See Also#
- Level#
- Location#

“basic” - A discrete system with pointwise residual and boundary residual functions

PetscDSType, PetscDSCreate(), PetscDSSetType()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDSType
```

Example 2 (unknown):
```unknown
PetscDSCreate()
```

Example 3 (unknown):
```unknown
PetscDSSetType()
```

---

## PetscDSCopyBoundary#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSCopyBoundary/

**Contents:**
- PetscDSCopyBoundary#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Copy all boundary condition objects to the new PetscDS

ds - The source PetscDS object

numFields - The number of selected fields, or PETSC_DEFAULT for all fields

fields - The selected fields, or NULL for all fields

newds - The target PetscDS, now with a copy of the boundary conditions

PetscDS, DMBoundary, PetscDSCopyEquations(), PetscDSSetResidual(), PetscDSSetJacobian(), PetscDSSetRiemannSolver(), PetscDSSetBdResidual(), PetscDSSetBdJacobian(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSCopyBoundary(PetscDS ds, PetscInt numFields, const PetscInt fields[], PetscDS newds)
```

Example 2 (unknown):
```unknown
PETSC_DEFAULT
```

Example 3 (unknown):
```unknown
PetscDSCopyEquations()
```

Example 4 (unknown):
```unknown
PetscDSSetResidual()
```

---

## PetscDSCopyBounds#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSCopyBounds/

**Contents:**
- PetscDSCopyBounds#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Copy lower and upper solution bounds set with PetscDSSetLowerBound() and PetscDSSetLowerBound() to another PetscDS

ds - The PetscDS object

newds - The PetscDS copy

PetscDS, PetscDSCopyBoundary(), PetscDSCopyEquations(), PetscDSCopyExactSolutions(), PetscDSSetResidual(), PetscDSSetJacobian(), PetscDSSetRiemannSolver(), PetscDSSetBdResidual(), PetscDSSetBdJacobian(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDSSetLowerBound()
```

Example 2 (unknown):
```unknown
PetscDSSetLowerBound()
```

Example 3 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSCopyBounds(PetscDS ds, PetscDS newds)
```

Example 4 (unknown):
```unknown
PetscDSCopyBoundary()
```

---

## PetscDSCopyConstants#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSCopyConstants/

**Contents:**
- PetscDSCopyConstants#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Copy all constants set with PetscDSSetConstants() to another PetscDS

prob - The PetscDS object

newprob - The PetscDS copy

PetscDS, PetscDSCopyBoundary(), PetscDSCopyEquations(), PetscDSSetResidual(), PetscDSSetJacobian(), PetscDSSetRiemannSolver(), PetscDSSetBdResidual(), PetscDSSetBdJacobian(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDSSetConstants()
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSCopyConstants(PetscDS prob, PetscDS newprob)
```

Example 3 (unknown):
```unknown
PetscDSCopyBoundary()
```

Example 4 (unknown):
```unknown
PetscDSCopyEquations()
```

---

## PetscDSCopyEquations#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSCopyEquations/

**Contents:**
- PetscDSCopyEquations#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Copy all pointwise function pointers to another PetscDS

prob - The PetscDS object

newprob - The PetscDS copy

PetscDS, PetscDSCopyBoundary(), PetscDSSetResidual(), PetscDSSetJacobian(), PetscDSSetRiemannSolver(), PetscDSSetBdResidual(), PetscDSSetBdJacobian(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSCopyEquations(PetscDS prob, PetscDS newprob)
```

Example 2 (unknown):
```unknown
PetscDSCopyBoundary()
```

Example 3 (unknown):
```unknown
PetscDSSetResidual()
```

Example 4 (unknown):
```unknown
PetscDSSetJacobian()
```

---

## PetscDSCopyExactSolutions#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSCopyExactSolutions/

**Contents:**
- PetscDSCopyExactSolutions#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Copy all exact solutions set with PetscDSSetExactSolution() and PetscDSSetExactSolutionTimeDerivative() to another PetscDS

ds - The PetscDS object

newds - The PetscDS copy

PetscDS, PetscDSCopyBoundary(), PetscDSCopyEquations(), PetscDSCopyBounds(), PetscDSSetResidual(), PetscDSSetJacobian(), PetscDSSetRiemannSolver(), PetscDSSetBdResidual(), PetscDSSetBdJacobian(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDSSetExactSolution()
```

Example 2 (unknown):
```unknown
PetscDSSetExactSolutionTimeDerivative()
```

Example 3 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSCopyExactSolutions(PetscDS ds, PetscDS newds)
```

Example 4 (unknown):
```unknown
PetscDSCopyBoundary()
```

---

## PetscDSCopy#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSCopy/

**Contents:**
- PetscDSCopy#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Copy the contents of a PetscDS into another PetscDS on a new DM.

ds - the source PetscDS

minDegree - the minimum polynomial degree to consider when selecting discretizations, or PETSC_DETERMINE

maxDegree - the maximum polynomial degree to consider when selecting discretizations, or PETSC_DETERMINE

dmNew - the target DM used to resolve boundary condition labels for the copied boundaries

dsNew - the destination PetscDS

This copies constants, exact solutions, bounds, discretizations, equations, field contexts, cohesive flags, jet degrees, and boundary conditions.

PetscDS, PetscDSCopyEquations(), PetscDSCopyConstants(), PetscDSCopyExactSolutions(), PetscDSCopyBounds(), PetscDSCopyBoundary()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSCopy(PetscDS ds, PetscInt minDegree, PetscInt maxDegree, DM dmNew, PetscDS dsNew)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
PETSC_DETERMINE
```

Example 4 (unknown):
```unknown
PetscDSCopyEquations()
```

---

## PetscDSCreate#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSCreate/

**Contents:**
- PetscDSCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Creates an empty PetscDS object. The type can then be set with PetscDSSetType().

comm - The communicator for the PetscDS object

ds - The PetscDS object

PetscDS, PetscDSSetType(), PETSCDSBASIC, PetscDSType, PetscDSDestroy()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDSSetType()
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSCreate(MPI_Comm comm, PetscDS *ds)
```

Example 3 (unknown):
```unknown
PetscDSSetType()
```

Example 4 (unknown):
```unknown
PETSCDSBASIC
```

---

## PetscDSDestroyBoundary#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSDestroyBoundary/

**Contents:**
- PetscDSDestroyBoundary#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Remove all DMBoundary objects from the PetscDS

ds - The PetscDS object

PetscDS, DMBoundary, PetscDSCopyBoundary(), PetscDSCopyEquations()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSDestroyBoundary(PetscDS ds)
```

Example 2 (unknown):
```unknown
PetscDSCopyBoundary()
```

Example 3 (unknown):
```unknown
PetscDSCopyEquations()
```

---

## PetscDSDestroy#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSDestroy/

**Contents:**
- PetscDSDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Destroys a PetscDS object

ds - the PetscDS object to destroy

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSDestroy(PetscDS *ds)
```

Example 2 (unknown):
```unknown
PetscDSView()
```

---

## PetscDSGetBdJacobian#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetBdJacobian/

**Contents:**
- PetscDSGetBdJacobian#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Get the pointwise boundary Jacobian function for given test and basis field

f - The test field number

g0 - integrand for the test and basis function term, see PetscBdPointJacFn

g1 - integrand for the test function and basis function gradient term, see PetscBdPointJacFn

g2 - integrand for the test function gradient and basis function term, see PetscBdPointJacFn

g3 - integrand for the test function gradient and basis function gradient term, see PetscBdPointJacFn

We are using a first order FEM model for the weak form:

PetscDS, PetscBdPointJacFn, PetscDSSetBdJacobian()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetBdJacobian(PetscDS ds, PetscInt f, PetscInt g, PetscBdPointJacFn **g0, PetscBdPointJacFn **g1, PetscBdPointJacFn **g2, PetscBdPointJacFn **g3)
```

Example 2 (unknown):
```unknown
PetscBdPointJacFn
```

Example 3 (unknown):
```unknown
PetscBdPointJacFn
```

Example 4 (unknown):
```unknown
PetscBdPointJacFn
```

---

## PetscDSGetBdResidual#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetBdResidual/

**Contents:**
- PetscDSGetBdResidual#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Get the pointwise boundary residual function for a given test field

f - The test field number

f0 - boundary integrand for the test function term, see PetscBdPointFn

f1 - boundary integrand for the test function gradient term, see PetscBdPointFn

We are using a first order FEM model for the weak form:

PetscDS, PetscBdPointFn, PetscDSSetBdResidual()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetBdResidual(PetscDS ds, PetscInt f, PetscBdPointFn **f0, PetscBdPointFn **f1)
```

Example 2 (unknown):
```unknown
PetscBdPointFn
```

Example 3 (unknown):
```unknown
PetscBdPointFn
```

Example 4 (unknown):
```unknown
PetscBdPointFn
```

---

## PetscDSGetBoundary#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetBoundary/

**Contents:**
- PetscDSGetBoundary#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#

Gets a boundary condition from the model

ds - The PetscDS object

bd - The boundary condition number

wf - The PetscWeakForm holding the pointwise functions

type - The type of condition, e.g. DM_BC_ESSENTIAL/DM_BC_ESSENTIAL_FIELD (Dirichlet), or DM_BC_NATURAL (Neumann)

name - The boundary condition name

label - The label defining constrained points

Nv - The number of DMLabel ids for constrained points

values - An array of ids for constrained points

field - The field to constrain

Nc - The number of constrained field components

comps - An array of constrained component numbers

func - A pointwise function giving boundary values

func_t - A pointwise function giving the time derivative of the boundary values

ctx - An optional application context for func

PetscDS, PetscWeakForm, DMBoundaryConditionType, PetscDSAddBoundary(), DMLabel

src/dm/dt/interface/dtds.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex62.c src/snes/tutorials/ex12.c src/ts/tutorials/ex76.c src/snes/tutorials/ex56.c src/snes/tutorials/ex17.c src/ts/tutorials/ex53.c src/snes/tutorials/ex24.c src/snes/tutorials/ex27.c src/snes/tutorials/ex77.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetBoundary(PetscDS ds, PetscInt bd, PetscWeakForm *wf, DMBoundaryConditionType *type, const char *name[], DMLabel *label, PetscInt *Nv, const PetscInt *values[], PetscInt *field, PetscInt *Nc, const PetscInt *comps[], PetscVoidFn **func, PetscVoidFn **func_t, PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
PetscWeakForm
```

Example 3 (unknown):
```unknown
DM_BC_ESSENTIAL
```

Example 4 (unknown):
```unknown
DM_BC_ESSENTIAL_FIELD
```

---

## PetscDSGetCohesive#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetCohesive/

**Contents:**
- PetscDSGetCohesive#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the flag indicating that a field is cohesive, meaning it is defined on the interior of a cohesive cell

ds - The PetscDS object

isCohesive - The flag

PetscDS, PetscDSSetCohesive(), PetscDSIsCohesive(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetCohesive(PetscDS ds, PetscInt f, PetscBool *isCohesive)
```

Example 2 (unknown):
```unknown
PetscDSSetCohesive()
```

Example 3 (unknown):
```unknown
PetscDSIsCohesive()
```

Example 4 (unknown):
```unknown
PetscDSCreate()
```

---

## PetscDSGetComponentDerivativeOffsetsCohesive#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetComponentDerivativeOffsetsCohesive/

**Contents:**
- PetscDSGetComponentDerivativeOffsetsCohesive#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the offset of each field derivative on an evaluation point

ds - The PetscDS object

s - The cohesive side, 0 for negative, 1 for positive, 2 for cohesive

offsets - The offsets

PetscDS, PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetComponentDerivativeOffsetsCohesive(PetscDS ds, PetscInt s, PetscInt *offsets[])
```

Example 2 (unknown):
```unknown
PetscDSGetNumFields()
```

Example 3 (unknown):
```unknown
PetscDSCreate()
```

---

## PetscDSGetComponentDerivativeOffsets#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetComponentDerivativeOffsets/

**Contents:**
- PetscDSGetComponentDerivativeOffsets#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the offset of each field derivative on an evaluation point

prob - The PetscDS object

offsets - The offsets

PetscDS, PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetComponentDerivativeOffsets(PetscDS prob, PetscInt *offsets[])
```

Example 2 (unknown):
```unknown
PetscDSGetNumFields()
```

Example 3 (unknown):
```unknown
PetscDSCreate()
```

---

## PetscDSGetComponentOffsetsCohesive#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetComponentOffsetsCohesive/

**Contents:**
- PetscDSGetComponentOffsetsCohesive#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the offset of each field on an evaluation point

ds - The PetscDS object

s - The cohesive side, 0 for negative, 1 for positive, 2 for cohesive

offsets - The offsets

PetscDS, PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetComponentOffsetsCohesive(PetscDS ds, PetscInt s, PetscInt *offsets[])
```

Example 2 (unknown):
```unknown
PetscDSGetNumFields()
```

Example 3 (unknown):
```unknown
PetscDSCreate()
```

---

## PetscDSGetComponentOffsets#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetComponentOffsets/

**Contents:**
- PetscDSGetComponentOffsets#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the offset of each field on an evaluation point

prob - The PetscDS object

offsets - The offsets

PetscDS, PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetComponentOffsets(PetscDS prob, PetscInt *offsets[])
```

Example 2 (unknown):
```unknown
PetscDSGetNumFields()
```

Example 3 (unknown):
```unknown
PetscDSCreate()
```

---

## PetscDSGetComponentOffset#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetComponentOffset/

**Contents:**
- PetscDSGetComponentOffset#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the offset of the given field on an evaluation point

prob - The PetscDS object

PetscDS, PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetComponentOffset(PetscDS prob, PetscInt f, PetscInt *off)
```

Example 2 (unknown):
```unknown
PetscDSGetNumFields()
```

Example 3 (unknown):
```unknown
PetscDSCreate()
```

---

## PetscDSGetComponents#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetComponents/

**Contents:**
- PetscDSGetComponents#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the number of components for each field on an evaluation point

prob - The PetscDS object

components - The number of components

PetscDS, PetscDSGetComponentOffsets(), PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetComponents(PetscDS prob, PetscInt *components[])
```

Example 2 (unknown):
```unknown
PetscDSGetComponentOffsets()
```

Example 3 (unknown):
```unknown
PetscDSGetNumFields()
```

Example 4 (unknown):
```unknown
PetscDSCreate()
```

---

## PetscDSGetConstants#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetConstants/

**Contents:**
- PetscDSGetConstants#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Returns the array of constants passed to point functions from a PetscDS object

ds - The PetscDS object

numConstants - The number of constants, or pass in NULL if not required

constants - The array of constants, NULL if there are none

PetscDS, PetscDSSetConstants(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetConstants(PetscDS ds, PeOp PetscInt *numConstants, PeOp const PetscScalar *constants[])
```

Example 2 (unknown):
```unknown
PetscDSSetConstants()
```

Example 3 (unknown):
```unknown
PetscDSCreate()
```

---

## PetscDSGetContext#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetContext/

**Contents:**
- PetscDSGetContext#
- Synopsis#
- Input Parameters#
- Fortran Notes#
- See Also#
- Level#
- Location#

Returns the context that was passed by PetscDSSetContext()

This only works when the context is a Fortran derived type or a PetscObject. Define ctx with

PetscDS, PetscPointFn, PetscDSSetContext()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDSSetContext()
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetContext(PetscDS ds, PetscInt f, PetscCtxRt ctx)
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

## PetscDSGetCoordinateDimension#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetCoordinateDimension/

**Contents:**
- PetscDSGetCoordinateDimension#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the coordinate dimension of the PetscDS, meaning the dimension of the space into which the discretiaztions are embedded

prob - The PetscDS object

dimEmbed - The coordinate dimension

PetscDS, PetscDSSetCoordinateDimension(), PetscDSGetSpatialDimension(), PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetCoordinateDimension(PetscDS prob, PetscInt *dimEmbed)
```

Example 2 (unknown):
```unknown
PetscDSSetCoordinateDimension()
```

Example 3 (unknown):
```unknown
PetscDSGetSpatialDimension()
```

Example 4 (unknown):
```unknown
PetscDSGetNumFields()
```

---

## PetscDSGetDimensions#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetDimensions/

**Contents:**
- PetscDSGetDimensions#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the size of the approximation space for each field on an evaluation point

prob - The PetscDS object

dimensions - The number of dimensions

PetscDS, PetscDSGetComponentOffsets(), PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetDimensions(PetscDS prob, PetscInt *dimensions[])
```

Example 2 (unknown):
```unknown
PetscDSGetComponentOffsets()
```

Example 3 (unknown):
```unknown
PetscDSGetNumFields()
```

Example 4 (unknown):
```unknown
PetscDSCreate()
```

---

## PetscDSGetDiscretization#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetDiscretization/

**Contents:**
- PetscDSGetDiscretization#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Returns the discretization object for the given field

prob - The PetscDS object

disc - The discretization object, this can be a PetscFE or a PetscFV

PetscDS, PetscFE, PetscFV, PetscDSSetDiscretization(), PetscDSAddDiscretization(), PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

src/dm/impls/plex/tutorials/ex8.c src/dm/impls/plex/tutorials/ex4f90.F90

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetDiscretization(PetscDS prob, PetscInt f, PetscObject *disc)
```

Example 2 (unknown):
```unknown
PetscDSSetDiscretization()
```

Example 3 (unknown):
```unknown
PetscDSAddDiscretization()
```

Example 4 (unknown):
```unknown
PetscDSGetNumFields()
```

---

## PetscDSGetDynamicJacobian#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetDynamicJacobian/

**Contents:**
- PetscDSGetDynamicJacobian#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Get the pointwise dynamic Jacobian, \(dF/du_t\), function for given test and basis field

f - The test field number

g0 - integrand for the test and basis function term, see PetscPointJacFn

g1 - integrand for the test function and basis function gradient term, see PetscPointJacFn

g2 - integrand for the test function gradient and basis function term, see PetscPointJacFn

g3 - integrand for the test function gradient and basis function gradient term, see PetscPointJacFn

We are using a first order FEM model for the weak form:

PetscDS, PetscDSSetJacobian(), PetscDSSetDynamicJacobian(), PetscPointJacFn

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetDynamicJacobian(PetscDS ds, PetscInt f, PetscInt g, PetscPointJacFn **g0, PetscPointJacFn **g1, PetscPointJacFn **g2, PetscPointJacFn **g3)
```

Example 2 (unknown):
```unknown
PetscPointJacFn
```

Example 3 (unknown):
```unknown
PetscPointJacFn
```

Example 4 (unknown):
```unknown
PetscPointJacFn
```

---

## PetscDSGetEvaluationArrays#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetEvaluationArrays/

**Contents:**
- PetscDSGetEvaluationArrays#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Get scratch arrays used to evaluate fields, time derivatives, and field gradients at quadrature points.

u - array for the field values, or NULL if not needed

u_t - array for the field time derivatives, or NULL if not needed

u_x - array for the field gradients, or NULL if not needed

The returned arrays are owned by the PetscDS and must not be freed by the caller.

PetscDS, PetscDSGetWeakFormArrays(), PetscDSGetWorkspace()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetEvaluationArrays(PetscDS prob, PetscScalar *u[], PetscScalar *u_t[], PetscScalar *u_x[])
```

Example 2 (unknown):
```unknown
PetscDSGetWeakFormArrays()
```

Example 3 (unknown):
```unknown
PetscDSGetWorkspace()
```

---

## PetscDSGetExactSolutionTimeDerivative#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetExactSolutionTimeDerivative/

**Contents:**
- PetscDSGetExactSolutionTimeDerivative#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Get the pointwise time derivative of the exact solution function for a given test field

f - The test field number

sol - time derivative of the exact solution for the test field, see PetscPointExactSolutionFn

ctx - the exact solution context

PetscDS, PetscPointExactSolutionFn, PetscDSSetExactSolutionTimeDerivative(), PetscDSGetExactSolution()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetExactSolutionTimeDerivative(PetscDS prob, PetscInt f, PetscPointExactSolutionFn **sol, void **ctx)
```

Example 2 (unknown):
```unknown
PetscPointExactSolutionFn
```

Example 3 (unknown):
```unknown
PetscPointExactSolutionFn
```

Example 4 (unknown):
```unknown
PetscDSSetExactSolutionTimeDerivative()
```

---

## PetscDSGetExactSolution#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetExactSolution/

**Contents:**
- PetscDSGetExactSolution#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#

Get the pointwise exact solution function for a given test field

f - The test field number

sol - exact solution function for the test field, see PetscPointExactSolutionFn

ctx - exact solution context

PetscDS, PetscPointExactSolutionFn, PetscDSSetExactSolution(), PetscDSGetExactSolutionTimeDerivative()

src/dm/dt/interface/dtds.c

src/snes/tutorials/ex71.c src/ts/tutorials/ex46.c src/snes/tutorials/ex76.c src/tao/tutorials/ex2.c src/snes/tutorials/ex13.c src/ts/tutorials/ex53.c src/snes/tutorials/ex27.c src/snes/tutorials/ex69.c src/tao/tutorials/ex1.c src/ts/tutorials/ex47.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetExactSolution(PetscDS prob, PetscInt f, PetscPointExactSolutionFn **sol, void **ctx)
```

Example 2 (unknown):
```unknown
PetscPointExactSolutionFn
```

Example 3 (unknown):
```unknown
PetscPointExactSolutionFn
```

Example 4 (unknown):
```unknown
PetscDSSetExactSolution()
```

---

## PetscDSGetFaceTabulation#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetFaceTabulation/

**Contents:**
- PetscDSGetFaceTabulation#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Return the basis tabulation at quadrature points on the faces

prob - The PetscDS object

Tf - The basis function and derivative tabulation on each local face at quadrature points for each field

The tabulation is only valid so long as the PetscDS has not be destroyed. There is no PetscDSRestoreFaceTabulation() in C.

PetscTabulation, PetscDS, PetscDSGetTabulation(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetFaceTabulation(PetscDS prob, PetscTabulation *Tf[])
```

Example 2 (unknown):
```unknown
PetscDSRestoreFaceTabulation()
```

Example 3 (unknown):
```unknown
PetscTabulation
```

Example 4 (unknown):
```unknown
PetscDSGetTabulation()
```

---

## PetscDSGetFieldIndex#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetFieldIndex/

**Contents:**
- PetscDSGetFieldIndex#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the index of the given field

prob - The PetscDS object

disc - The discretization object

PetscDS, PetscGetDiscretization(), PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetFieldIndex(PetscDS prob, PetscObject disc, PetscInt *f)
```

Example 2 (unknown):
```unknown
PetscGetDiscretization()
```

Example 3 (unknown):
```unknown
PetscDSGetNumFields()
```

Example 4 (unknown):
```unknown
PetscDSCreate()
```

---

## PetscDSGetFieldOffsetCohesive#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetFieldOffsetCohesive/

**Contents:**
- PetscDSGetFieldOffsetCohesive#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the offset of the given field in the full space basis on a cohesive cell

ds - The PetscDS object

PetscDS, PetscDSGetFieldSize(), PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetFieldOffsetCohesive(PetscDS ds, PetscInt f, PetscInt *off)
```

Example 2 (unknown):
```unknown
PetscDSGetFieldSize()
```

Example 3 (unknown):
```unknown
PetscDSGetNumFields()
```

Example 4 (unknown):
```unknown
PetscDSCreate()
```

---

## PetscDSGetFieldOffset#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetFieldOffset/

**Contents:**
- PetscDSGetFieldOffset#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the offset of the given field in the full space basis

prob - The PetscDS object

PetscDS, PetscDSGetFieldSize(), PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetFieldOffset(PetscDS prob, PetscInt f, PetscInt *off)
```

Example 2 (unknown):
```unknown
PetscDSGetFieldSize()
```

Example 3 (unknown):
```unknown
PetscDSGetNumFields()
```

Example 4 (unknown):
```unknown
PetscDSCreate()
```

---

## PetscDSGetFieldSize#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetFieldSize/

**Contents:**
- PetscDSGetFieldSize#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the size of the given field in the full space basis

prob - The PetscDS object

PetscDS, PetscDSGetFieldOffset(), PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetFieldSize(PetscDS prob, PetscInt f, PetscInt *size)
```

Example 2 (unknown):
```unknown
PetscDSGetFieldOffset()
```

Example 3 (unknown):
```unknown
PetscDSGetNumFields()
```

Example 4 (unknown):
```unknown
PetscDSCreate()
```

---

## PetscDSGetForceQuad#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetForceQuad/

**Contents:**
- PetscDSGetForceQuad#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the flag to force matching quadratures among the field discretizations

ds - The PetscDS object

PetscDS, PetscDSSetForceQuad(), PetscDSGetDiscretization(), PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetForceQuad(PetscDS ds, PetscBool *forceQuad)
```

Example 2 (unknown):
```unknown
PetscDSSetForceQuad()
```

Example 3 (unknown):
```unknown
PetscDSGetDiscretization()
```

Example 4 (unknown):
```unknown
PetscDSGetNumFields()
```

---

## PetscDSGetHeightSubspace#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetHeightSubspace/

**Contents:**
- PetscDSGetHeightSubspace#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Get the PetscDS for the trace subspace at a given height in the mesh.

height - the height (0 for the ambient cell, 1 for faces, etc.)

subprob - the PetscDS for the trace subspace; prob itself is returned when height is 0

Only PetscFE discretizations are currently supported.

PetscDS, PetscFE, PetscFEGetHeightSubspace(), PetscDSGetSpatialDimension()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetHeightSubspace(PetscDS prob, PetscInt height, PetscDS *subprob)
```

Example 2 (unknown):
```unknown
PetscFEGetHeightSubspace()
```

Example 3 (unknown):
```unknown
PetscDSGetSpatialDimension()
```

---

## PetscDSGetImplicit#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetImplicit/

**Contents:**
- PetscDSGetImplicit#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the flag for implicit solve for this field. This is just a guide for TSARKIMEX

prob - The PetscDS object

implicit - The flag indicating what kind of solve to use for this field

TSARKIMEX, PetscDS, PetscDSSetImplicit(), PetscDSSetDiscretization(), PetscDSAddDiscretization(), PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetImplicit(PetscDS prob, PetscInt f, PetscBool *implicit)
```

Example 2 (unknown):
```unknown
PetscDSSetImplicit()
```

Example 3 (unknown):
```unknown
PetscDSSetDiscretization()
```

Example 4 (unknown):
```unknown
PetscDSAddDiscretization()
```

---

## PetscDSGetJacobian#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetJacobian/

**Contents:**
- PetscDSGetJacobian#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Get the pointwise Jacobian function for given test and basis field

f - The test field number

g0 - integrand for the test and basis function term, see PetscPointJacFn

g1 - integrand for the test function and basis function gradient term, see PetscPointJacFn

g2 - integrand for the test function gradient and basis function term, see PetscPointJacFn

g3 - integrand for the test function gradient and basis function gradient term, see PetscPointJacFn

We are using a first order FEM model for the weak form:

PetscDS, PetscDSSetJacobian(), PetscPointJacFn

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetJacobian(PetscDS ds, PetscInt f, PetscInt g, PetscPointJacFn **g0, PetscPointJacFn **g1, PetscPointJacFn **g2, PetscPointJacFn **g3)
```

Example 2 (unknown):
```unknown
PetscPointJacFn
```

Example 3 (unknown):
```unknown
PetscPointJacFn
```

Example 4 (unknown):
```unknown
PetscPointJacFn
```

---

## PetscDSGetJetDegree#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetJetDegree/

**Contents:**
- PetscDSGetJetDegree#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the highest derivative for this field equation, or the k-jet that the discretization needs to tabulate.

ds - The PetscDS object

k - The highest derivative we need to tabulate

PetscDS, PetscDSSetJetDegree(), PetscDSSetDiscretization(), PetscDSAddDiscretization(), PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetJetDegree(PetscDS ds, PetscInt f, PetscInt *k)
```

Example 2 (unknown):
```unknown
PetscDSSetJetDegree()
```

Example 3 (unknown):
```unknown
PetscDSSetDiscretization()
```

Example 4 (unknown):
```unknown
PetscDSAddDiscretization()
```

---

## PetscDSGetLowerBound#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetLowerBound/

**Contents:**
- PetscDSGetLowerBound#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Get the pointwise lower bound function for a given field

lb - lower bound function for the field, see PetscPointBoundFn

ctx - lower bound context that was set with PetscDSSetLowerBound()

PetscDS, PetscPointBoundFn, PetscDSSetLowerBound(), PetscDSGetUpperBound(), PetscDSGetExactSolution()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetLowerBound(PetscDS ds, PetscInt f, PetscPointBoundFn **lb, void **ctx)
```

Example 2 (unknown):
```unknown
PetscPointBoundFn
```

Example 3 (unknown):
```unknown
PetscDSSetLowerBound()
```

Example 4 (unknown):
```unknown
PetscPointBoundFn
```

---

## PetscDSGetNumBoundary#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetNumBoundary/

**Contents:**
- PetscDSGetNumBoundary#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the number of registered boundary conditions

ds - The PetscDS object

numBd - The number of boundary conditions

PetscDS, PetscDSAddBoundary(), PetscDSGetBoundary()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetNumBoundary(PetscDS ds, PetscInt *numBd)
```

Example 2 (unknown):
```unknown
PetscDSAddBoundary()
```

Example 3 (unknown):
```unknown
PetscDSGetBoundary()
```

---

## PetscDSGetNumCohesive#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetNumCohesive/

**Contents:**
- PetscDSGetNumCohesive#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the number of cohesive fields, meaning those defined on the interior of a cohesive cell

ds - The PetscDS object

numCohesive - The number of cohesive fields

PetscDS, PetscDSSetCohesive(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetNumCohesive(PetscDS ds, PetscInt *numCohesive)
```

Example 2 (unknown):
```unknown
PetscDSSetCohesive()
```

Example 3 (unknown):
```unknown
PetscDSCreate()
```

---

## PetscDSGetNumFields#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetNumFields/

**Contents:**
- PetscDSGetNumFields#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Returns the number of fields in the PetscDS

prob - The PetscDS object

Nf - The number of fields

PetscDS, PetscDSGetSpatialDimension(), PetscDSCreate()

src/dm/dt/interface/dtds.c

src/snes/tutorials/ex26.c src/ts/tutorials/ex18.c src/ts/tutorials/ex53.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetNumFields(PetscDS prob, PetscInt *Nf)
```

Example 2 (unknown):
```unknown
PetscDSGetSpatialDimension()
```

Example 3 (unknown):
```unknown
PetscDSCreate()
```

---

## PetscDSGetObjective#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetObjective/

**Contents:**
- PetscDSGetObjective#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Get the pointwise objective function for a given test field that was provided with PetscDSSetObjective()

f - The test field number

obj - integrand for the test function term, see PetscPointFn

We are using a first order FEM model for the weak form: \( \int_\Omega \phi\,\mathrm{obj}(u, u_t, \nabla u, x, t)\)

PetscPointFn, PetscDS, PetscDSSetObjective(), PetscDSGetResidual()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDSSetObjective()
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetObjective(PetscDS ds, PetscInt f, PetscPointFn **obj)
```

Example 3 (unknown):
```unknown
PetscPointFn
```

Example 4 (unknown):
```unknown
PetscPointFn
```

---

## PetscDSGetQuadrature#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetQuadrature/

**Contents:**
- PetscDSGetQuadrature#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the quadrature, which must agree for all fields in the PetscDS

prob - The PetscDS object

q - The quadrature object

PetscDS, PetscQuadrature, PetscDSSetImplicit(), PetscDSSetDiscretization(), PetscDSAddDiscretization(), PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetQuadrature(PetscDS prob, PetscQuadrature *q)
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
PetscDSSetImplicit()
```

Example 4 (unknown):
```unknown
PetscDSSetDiscretization()
```

---

## PetscDSGetResidual#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetResidual/

**Contents:**
- PetscDSGetResidual#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Get the pointwise residual function for a given test field

f - The test field number

f0 - integrand for the test function term, see PetscPointFn

f1 - integrand for the test function gradient term, see PetscPointFn

We are using a first order FEM model for the weak form: \( \int_\Omega \phi f_0(u, u_t, \nabla u, x, t) + \nabla\phi \cdot {\vec f}_1(u, u_t, \nabla u, x, t)\)

PetscPointFn, PetscDS, PetscDSSetResidual()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetResidual(PetscDS ds, PetscInt f, PetscPointFn **f0, PetscPointFn **f1)
```

Example 2 (unknown):
```unknown
PetscPointFn
```

Example 3 (unknown):
```unknown
PetscPointFn
```

Example 4 (unknown):
```unknown
PetscPointFn
```

---

## PetscDSGetRHSResidual#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetRHSResidual/

**Contents:**
- PetscDSGetRHSResidual#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Get the pointwise RHS residual function for explicit timestepping for a given test field

f - The test field number

f0 - integrand for the test function term, see PetscPointFn

f1 - integrand for the test function gradient term, see PetscPointFn

We are using a first order FEM model for the weak form: \( \int_\Omega \phi f_0(u, u_t, \nabla u, x, t) + \nabla\phi \cdot {\vec f}_1(u, u_t, \nabla u, x, t)\)

PetscPointFn, PetscDS, PetscDSSetRHSResidual()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetRHSResidual(PetscDS ds, PetscInt f, PetscPointFn **f0, PetscPointFn **f1)
```

Example 2 (unknown):
```unknown
PetscPointFn
```

Example 3 (unknown):
```unknown
PetscPointFn
```

Example 4 (unknown):
```unknown
PetscPointFn
```

---

## PetscDSGetRiemannSolver#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetRiemannSolver/

**Contents:**
- PetscDSGetRiemannSolver#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the Riemann solver for the given field

ds - The PetscDS object

r - Riemann solver, see PetscRiemannFn

PetscDS, PetscRiemannFn, PetscDSSetRiemannSolver()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetRiemannSolver(PetscDS ds, PetscInt f, PetscRiemannFn **r)
```

Example 2 (unknown):
```unknown
PetscRiemannFn
```

Example 3 (unknown):
```unknown
PetscRiemannFn
```

Example 4 (unknown):
```unknown
PetscDSSetRiemannSolver()
```

---

## PetscDSGetSpatialDimension#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetSpatialDimension/

**Contents:**
- PetscDSGetSpatialDimension#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Returns the spatial dimension of the PetscDS, meaning the topological dimension of the discretizations

prob - The PetscDS object

dim - The spatial dimension

PetscDS, PetscDSGetCoordinateDimension(), PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

src/snes/tutorials/ex34.c src/snes/tutorials/ex17.c src/ts/tutorials/ex53.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetSpatialDimension(PetscDS prob, PetscInt *dim)
```

Example 2 (unknown):
```unknown
PetscDSGetCoordinateDimension()
```

Example 3 (unknown):
```unknown
PetscDSGetNumFields()
```

Example 4 (unknown):
```unknown
PetscDSCreate()
```

---

## PetscDSGetTabulation#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetTabulation/

**Contents:**
- PetscDSGetTabulation#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- Fortran Note#
- Developer Note#
- See Also#
- Level#
- Location#

Return the basis tabulation at quadrature points for the volume discretization

prob - The PetscDS object

T - The basis function and derivatives tabulation at quadrature points for each field, see PetscTabulation for its details

The tabulation is only valid so long as the PetscDS has not be destroyed. There is no PetscDSRestoreTabulation() in C.

and access the values using, for example,

where \( i = 1, 2, ..., Nf \) and \( j = 1, 2, ..., tab(i)%ptr%K+1 \).

Use PetscDSRestoreTabulation() to restore the array

The Fortran language syntax does not directly support arrays of pointers, the ‘%ptr’ notation allows mimicking their use in Fortran.

PetscDS, PetscTabulation, PetscDSCreate()

src/dm/dt/interface/dtds.c

src/dm/impls/plex/tutorials/ex4f90.F90

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetTabulation(PetscDS prob, PetscTabulation *T[]) PeNS
```

Example 2 (unknown):
```unknown
PetscTabulation
```

Example 3 (unknown):
```unknown
PetscDSRestoreTabulation()
```

Example 4 (julia):
```julia
PetscTabulation, pointer :: tab(:)
```

---

## PetscDSGetTotalComponents#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetTotalComponents/

**Contents:**
- PetscDSGetTotalComponents#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the total number of components in this system

prob - The PetscDS object

Nc - The total number of components

PetscDS, PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetTotalComponents(PetscDS prob, PetscInt *Nc)
```

Example 2 (unknown):
```unknown
PetscDSGetNumFields()
```

Example 3 (unknown):
```unknown
PetscDSCreate()
```

---

## PetscDSGetTotalDimension#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetTotalDimension/

**Contents:**
- PetscDSGetTotalDimension#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the total size of the approximation space for this system

prob - The PetscDS object

dim - The total problem dimension

PetscDS, PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetTotalDimension(PetscDS prob, PetscInt *dim)
```

Example 2 (unknown):
```unknown
PetscDSGetNumFields()
```

Example 3 (unknown):
```unknown
PetscDSCreate()
```

---

## PetscDSGetType#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetType/

**Contents:**
- PetscDSGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the PetscDSType name (as a string) from the PetscDS

Not Collective; No Fortran Support

name - The PetscDSType name

PetscDSType, PetscDS, PetscDSSetType(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDSType
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetType(PetscDS prob, PetscDSType *name)
```

Example 3 (unknown):
```unknown
PetscDSType
```

Example 4 (unknown):
```unknown
PetscDSType
```

---

## PetscDSGetUpdate#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetUpdate/

**Contents:**
- PetscDSGetUpdate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the pointwise update function for a given field

update - update function, see PetscPointFn

PetscDS, PetscPointFn, PetscDSSetUpdate(), PetscDSSetResidual()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetUpdate(PetscDS ds, PetscInt f, PetscPointFn **update)
```

Example 2 (unknown):
```unknown
PetscPointFn
```

Example 3 (unknown):
```unknown
PetscPointFn
```

Example 4 (unknown):
```unknown
PetscDSSetUpdate()
```

---

## PetscDSGetUpperBound#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetUpperBound/

**Contents:**
- PetscDSGetUpperBound#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Get the pointwise upper bound function for a given field

ub - upper bound function for the field, see PetscPointBoundFn

ctx - upper bound context that was set with PetscDSSetUpperBound()

PetscDS, PetscPointBoundFn, PetscDSSetUpperBound(), PetscDSGetLowerBound(), PetscDSGetExactSolution()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetUpperBound(PetscDS ds, PetscInt f, PetscPointBoundFn **ub, void **ctx)
```

Example 2 (unknown):
```unknown
PetscPointBoundFn
```

Example 3 (unknown):
```unknown
PetscDSSetUpperBound()
```

Example 4 (unknown):
```unknown
PetscPointBoundFn
```

---

## PetscDSGetWeakForm#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetWeakForm/

**Contents:**
- PetscDSGetWeakForm#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Returns the weak form object from within the PetscDS

ds - The PetscDS object

wf - The weak form object

PetscWeakForm, PetscDSSetWeakForm(), PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

src/snes/tutorials/ex23.c src/snes/tutorials/ex34.c src/snes/tutorials/ex17.c src/ts/tutorials/ex76.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetWeakForm(PetscDS ds, PetscWeakForm *wf)
```

Example 2 (unknown):
```unknown
PetscWeakForm
```

Example 3 (unknown):
```unknown
PetscDSSetWeakForm()
```

Example 4 (unknown):
```unknown
PetscDSGetNumFields()
```

---

## PetscDSGetWorkspace#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSGetWorkspace/

**Contents:**
- PetscDSGetWorkspace#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Get scratch storage used during discretization computations.

x - array for real-valued quadrature point coordinates, or NULL if not needed

basisReal - array for the real-valued basis function values, or NULL if not needed

basisDerReal - array for the real-valued basis function derivatives, or NULL if not needed

testReal - array for the real-valued test function values, or NULL if not needed

testDerReal - array for the real-valued test function derivatives, or NULL if not needed

The returned arrays are owned by the PetscDS and must not be freed by the caller.

PetscDS, PetscDSGetEvaluationArrays(), PetscDSGetWeakFormArrays()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSGetWorkspace(PetscDS prob, PetscReal **x, PetscScalar **basisReal, PetscScalar **basisDerReal, PetscScalar **testReal, PetscScalar **testDerReal)
```

Example 2 (unknown):
```unknown
PetscDSGetEvaluationArrays()
```

Example 3 (unknown):
```unknown
PetscDSGetWeakFormArrays()
```

---

## PetscDSHasBdJacobian#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSHasBdJacobian/

**Contents:**
- PetscDSHasBdJacobian#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Indicates that boundary Jacobian functions have been set

hasBdJac - flag that pointwise function for the boundary Jacobian has been set

PetscDS, PetscDSHasJacobian(), PetscDSSetBdJacobian(), PetscDSGetBdJacobian()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSHasBdJacobian(PetscDS ds, PetscBool *hasBdJac)
```

Example 2 (unknown):
```unknown
PetscDSHasJacobian()
```

Example 3 (unknown):
```unknown
PetscDSSetBdJacobian()
```

Example 4 (unknown):
```unknown
PetscDSGetBdJacobian()
```

---

## PetscDSHasDynamicJacobian#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSHasDynamicJacobian/

**Contents:**
- PetscDSHasDynamicJacobian#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Signals that a dynamic Jacobian, \(dF/du_t\), has been set

hasDynJac - flag that pointwise function for dynamic Jacobian has been set

PetscDS, PetscDSGetDynamicJacobian(), PetscDSSetDynamicJacobian(), PetscDSGetJacobian()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSHasDynamicJacobian(PetscDS ds, PetscBool *hasDynJac)
```

Example 2 (unknown):
```unknown
PetscDSGetDynamicJacobian()
```

Example 3 (unknown):
```unknown
PetscDSSetDynamicJacobian()
```

Example 4 (unknown):
```unknown
PetscDSGetJacobian()
```

---

## PetscDSHasJacobian#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSHasJacobian/

**Contents:**
- PetscDSHasJacobian#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Checks that the Jacobian functions have been set

hasJac - flag that indicates the pointwise function for the Jacobian has been set

PetscDS, PetscDSGetJacobianPreconditioner(), PetscDSSetJacobianPreconditioner(), PetscDSGetJacobian()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSHasJacobian(PetscDS ds, PetscBool *hasJac)
```

Example 2 (unknown):
```unknown
PetscDSGetJacobianPreconditioner()
```

Example 3 (unknown):
```unknown
PetscDSSetJacobianPreconditioner()
```

Example 4 (unknown):
```unknown
PetscDSGetJacobian()
```

---

## PetscDSIsCohesive#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSIsCohesive/

**Contents:**
- PetscDSIsCohesive#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the flag indicating that this PetscDS is for a cohesive cell

ds - The PetscDS object

isCohesive - The flag

PetscDS, PetscDSGetNumCohesive(), PetscDSGetCohesive(), PetscDSSetCohesive(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSIsCohesive(PetscDS ds, PetscBool *isCohesive)
```

Example 2 (unknown):
```unknown
PetscDSGetNumCohesive()
```

Example 3 (unknown):
```unknown
PetscDSGetCohesive()
```

Example 4 (unknown):
```unknown
PetscDSSetCohesive()
```

---

## PetscDSPermuteQuadPoint#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSPermuteQuadPoint/

**Contents:**
- PetscDSPermuteQuadPoint#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Permute a quadrature point index according to a cell orientation.

ornt - the cell orientation, in [-Na, Na) where Na is half the number of arrangements for the cell type

field - the field number whose quadrature is used

q - the input quadrature point index in [0, Nq)

qperm - the permuted quadrature point index

PetscDS, PetscQuadrature, PetscQuadratureComputePermutations(), DMPolytopeTypeGetNumArrangements()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSPermuteQuadPoint(PetscDS ds, PetscInt ornt, PetscInt field, PetscInt q, PetscInt *qperm)
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
PetscQuadratureComputePermutations()
```

Example 4 (unknown):
```unknown
DMPolytopeTypeGetNumArrangements()
```

---

## PetscDSRegister#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSRegister/

**Contents:**
- PetscDSRegister#
- Synopsis#
- Input Parameters#
- Example Usage#
- Note#
- See Also#
- Level#
- Location#

Adds a new PetscDS implementation

Not Collective; No Fortran Support

sname - The name of a new user-defined creation routine

function - The creation routine itself

Then, your PetscDS type can be chosen with the procedural interface via

or at runtime via the option

PetscDSRegister() may be called multiple times to add several user-defined PetscDSs

PetscDSType, PetscDS, PetscDSRegisterAll(), PetscDSRegisterDestroy()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSRegister(const char sname[], PetscErrorCode (*function)(PetscDS))
```

Example 2 (unknown):
```unknown
PetscDSRegister("my_ds", MyPetscDSCreate);
```

Example 3 (unknown):
```unknown
PetscDSCreate(MPI_Comm, PetscDS *);
    PetscDSSetType(PetscDS, "my_ds");
```

Example 4 (unknown):
```unknown
-petscds_type my_ds
```

---

## PetscDSSelectDiscretizations#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSelectDiscretizations/

**Contents:**
- PetscDSSelectDiscretizations#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Copy discretizations to the new PetscDS with different field layout

prob - The PetscDS object

numFields - Number of new fields

fields - Old field number for each new field

minDegree - Minimum degree for a discretization, or PETSC_DETERMINE for no limit

maxDegree - Maximum degree for a discretization, or PETSC_DETERMINE for no limit

newprob - The PetscDS copy

PetscDS, PetscDSSelectEquations(), PetscDSCopyBoundary(), PetscDSSetResidual(), PetscDSSetJacobian(), PetscDSSetRiemannSolver(), PetscDSSetBdResidual(), PetscDSSetBdJacobian(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSelectDiscretizations(PetscDS prob, PetscInt numFields, const PetscInt fields[], PetscInt minDegree, PetscInt maxDegree, PetscDS newprob)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
PETSC_DETERMINE
```

Example 4 (unknown):
```unknown
PetscDSSelectEquations()
```

---

## PetscDSSelectEquations#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSelectEquations/

**Contents:**
- PetscDSSelectEquations#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Copy pointwise function pointers to the new PetscDS with different field layout

prob - The PetscDS object

numFields - Number of new fields

fields - Old field number for each new field

newprob - The PetscDS copy

PetscDS, PetscDSSelectDiscretizations(), PetscDSCopyBoundary(), PetscDSSetResidual(), PetscDSSetJacobian(), PetscDSSetRiemannSolver(), PetscDSSetBdResidual(), PetscDSSetBdJacobian(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSelectEquations(PetscDS prob, PetscInt numFields, const PetscInt fields[], PetscDS newprob)
```

Example 2 (unknown):
```unknown
PetscDSSelectDiscretizations()
```

Example 3 (unknown):
```unknown
PetscDSCopyBoundary()
```

Example 4 (unknown):
```unknown
PetscDSSetResidual()
```

---

## PetscDSSetBdJacobian#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetBdJacobian/

**Contents:**
- PetscDSSetBdJacobian#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Set the pointwise boundary Jacobian function for given test and basis field

f - The test field number

g0 - integrand for the test and basis function term, see PetscBdPointJacFn

g1 - integrand for the test function and basis function gradient term, see PetscBdPointJacFn

g2 - integrand for the test function gradient and basis function term, see PetscBdPointJacFn

g3 - integrand for the test function gradient and basis function gradient term, see PetscBdPointJacFn

We are using a first order FEM model for the weak form:

PetscDS, PetscBdPointJacFn, PetscDSGetBdJacobian()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetBdJacobian(PetscDS ds, PetscInt f, PetscInt g, PetscBdPointJacFn *g0, PetscBdPointJacFn *g1, PetscBdPointJacFn *g2, PetscBdPointJacFn *g3)
```

Example 2 (unknown):
```unknown
PetscBdPointJacFn
```

Example 3 (unknown):
```unknown
PetscBdPointJacFn
```

Example 4 (unknown):
```unknown
PetscBdPointJacFn
```

---

## PetscDSSetBdResidual#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetBdResidual/

**Contents:**
- PetscDSSetBdResidual#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Get the pointwise boundary residual function for a given test field

f - The test field number

f0 - boundary integrand for the test function term, see PetscBdPointFn

f1 - boundary integrand for the test function gradient term, see PetscBdPointFn

We are using a first order FEM model for the weak form:

PetscDS, PetscBdPointFn, PetscDSGetBdResidual()

src/dm/dt/interface/dtds.c

src/ts/tutorials/ex53.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetBdResidual(PetscDS ds, PetscInt f, PetscBdPointFn *f0, PetscBdPointFn *f1)
```

Example 2 (unknown):
```unknown
PetscBdPointFn
```

Example 3 (unknown):
```unknown
PetscBdPointFn
```

Example 4 (unknown):
```unknown
PetscBdPointFn
```

---

## PetscDSSetCellParameters#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetCellParameters/

**Contents:**
- PetscDSSetCellParameters#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the parameters for a particular cell

ds - The PetscDS object

volume - The cell volume

PetscDS, PetscDSSetConstants(), PetscDSGetConstants(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetCellParameters(PetscDS ds, PetscReal volume)
```

Example 2 (unknown):
```unknown
PetscDSSetConstants()
```

Example 3 (unknown):
```unknown
PetscDSGetConstants()
```

Example 4 (unknown):
```unknown
PetscDSCreate()
```

---

## PetscDSSetCohesive#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetCohesive/

**Contents:**
- PetscDSSetCohesive#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the flag indicating that a field is cohesive, meaning it is defined on the interior of a cohesive cell

ds - The PetscDS object

isCohesive - The flag for a cohesive field

PetscDS, PetscDSGetCohesive(), PetscDSIsCohesive(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetCohesive(PetscDS ds, PetscInt f, PetscBool isCohesive)
```

Example 2 (unknown):
```unknown
PetscDSGetCohesive()
```

Example 3 (unknown):
```unknown
PetscDSIsCohesive()
```

Example 4 (unknown):
```unknown
PetscDSCreate()
```

---

## PetscDSSetConstants#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetConstants/

**Contents:**
- PetscDSSetConstants#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the array of constants passed to point functions from a PetscDS

ds - The PetscDS object

numConstants - The number of constants

constants - The array of constants, NULL if there are none

PetscDS, PetscDSGetConstants(), PetscDSCreate()

src/dm/dt/interface/dtds.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex76.c src/snes/tutorials/ex12.c src/snes/tutorials/ex36.c src/snes/tutorials/ex17.c src/snes/tutorials/ex27.c src/snes/tutorials/ex69.c src/snes/tutorials/ex64.c src/snes/tutorials/ex62.c src/snes/tutorials/ex34.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetConstants(PetscDS ds, PetscInt numConstants, PetscScalar constants[])
```

Example 2 (unknown):
```unknown
PetscDSGetConstants()
```

Example 3 (unknown):
```unknown
PetscDSCreate()
```

---

## PetscDSSetContext#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetContext/

**Contents:**
- PetscDSSetContext#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the context that is passed back to some of the pointwise function callbacks used by this PetscDS

PetscDS, PetscPointFn, PetscDSGetContext()

src/dm/dt/interface/dtds.c

src/ts/tutorials/ex11.c src/ts/tutorials/ex48.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetContext(PetscDS ds, PetscInt f, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
PetscPointFn
```

Example 3 (unknown):
```unknown
PetscDSGetContext()
```

---

## PetscDSSetCoordinateDimension#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetCoordinateDimension/

**Contents:**
- PetscDSSetCoordinateDimension#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the coordinate dimension of the PetscDS, meaning the dimension of the space into which the discretiaztions are embedded

prob - The PetscDS object

dimEmbed - The coordinate dimension

PetscDS, PetscDSGetCoordinateDimension(), PetscDSGetSpatialDimension(), PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetCoordinateDimension(PetscDS prob, PetscInt dimEmbed)
```

Example 2 (unknown):
```unknown
PetscDSGetCoordinateDimension()
```

Example 3 (unknown):
```unknown
PetscDSGetSpatialDimension()
```

Example 4 (unknown):
```unknown
PetscDSGetNumFields()
```

---

## PetscDSSetDiscretization#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetDiscretization/

**Contents:**
- PetscDSSetDiscretization#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the discretization object for the given field

prob - The PetscDS object

disc - The discretization object, this can be a PetscFE or a PetscFV

PetscDS, PetscFE, PetscFV, PetscDSGetDiscretization(), PetscDSAddDiscretization(), PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

src/tao/tutorials/ex3.c src/ts/tutorials/ex48.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetDiscretization(PetscDS prob, PetscInt f, PetscObject disc)
```

Example 2 (unknown):
```unknown
PetscDSGetDiscretization()
```

Example 3 (unknown):
```unknown
PetscDSAddDiscretization()
```

Example 4 (unknown):
```unknown
PetscDSGetNumFields()
```

---

## PetscDSSetDynamicJacobian#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetDynamicJacobian/

**Contents:**
- PetscDSSetDynamicJacobian#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Set the pointwise dynamic Jacobian, \(dF/du_t\), function for given test and basis fields

f - The test field number

g0 - integrand for the test and basis function term, see PetscPointJacFn

g1 - integrand for the test function and basis function gradient term, see PetscPointJacFn

g2 - integrand for the test function gradient and basis function term, see PetscPointJacFn

g3 - integrand for the test function gradient and basis function gradient term, see PetscPointJacFn

We are using a first order FEM model for the weak form:

PetscDS, PetscDSGetDynamicJacobian(), PetscDSGetJacobian(), PetscPointJacFn

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetDynamicJacobian(PetscDS ds, PetscInt f, PetscInt g, PetscPointJacFn *g0, PetscPointJacFn *g1, PetscPointJacFn *g2, PetscPointJacFn *g3)
```

Example 2 (unknown):
```unknown
PetscPointJacFn
```

Example 3 (unknown):
```unknown
PetscPointJacFn
```

Example 4 (unknown):
```unknown
PetscPointJacFn
```

---

## PetscDSSetExactSolutionTimeDerivative#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetExactSolutionTimeDerivative/

**Contents:**
- PetscDSSetExactSolutionTimeDerivative#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the pointwise time derivative of the exact solution function for a given test field

f - The test field number

sol - time derivative of the solution function for the test fields, see PetscPointExactSolutionFn

ctx - the solution context or NULL

PetscDS, PetscPointExactSolutionFn, PetscDSGetExactSolutionTimeDerivative(), PetscDSSetExactSolution()

src/dm/dt/interface/dtds.c

src/ts/tutorials/ex77.c src/ts/tutorials/ex45.c src/ts/tutorials/ex53.c src/ts/tutorials/ex76.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetExactSolutionTimeDerivative(PetscDS prob, PetscInt f, PetscPointExactSolutionFn *sol, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
PetscPointExactSolutionFn
```

Example 3 (unknown):
```unknown
PetscPointExactSolutionFn
```

Example 4 (unknown):
```unknown
PetscDSGetExactSolutionTimeDerivative()
```

---

## PetscDSSetExactSolution#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetExactSolution/

**Contents:**
- PetscDSSetExactSolution#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the pointwise exact solution function for a given test field

f - The test field number

sol - solution function for the test fields, see PetscPointExactSolutionFn

ctx - solution context or NULL

PetscDS, PetscPointExactSolutionFn, PetscDSGetExactSolution()

src/dm/dt/interface/dtds.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex76.c src/snes/tutorials/ex69.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex26.c src/snes/tutorials/ex17.c src/snes/tutorials/ex23.c src/snes/tutorials/ex62.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetExactSolution(PetscDS prob, PetscInt f, PetscPointExactSolutionFn *sol, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
PetscPointExactSolutionFn
```

Example 3 (unknown):
```unknown
PetscPointExactSolutionFn
```

Example 4 (unknown):
```unknown
PetscDSGetExactSolution()
```

---

## PetscDSSetForceQuad#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetForceQuad/

**Contents:**
- PetscDSSetForceQuad#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the flag to force matching quadratures among the field discretizations

Logically collective on ds

ds - The PetscDS object

PetscDS, PetscDSGetForceQuad(), PetscDSGetDiscretization(), PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetForceQuad(PetscDS ds, PetscBool forceQuad)
```

Example 2 (unknown):
```unknown
PetscDSGetForceQuad()
```

Example 3 (unknown):
```unknown
PetscDSGetDiscretization()
```

Example 4 (unknown):
```unknown
PetscDSGetNumFields()
```

---

## PetscDSSetFromOptions#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetFromOptions/

**Contents:**
- PetscDSSetFromOptions#
- Synopsis#
- Input Parameter#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#

sets parameters in a PetscDS from the options database

prob - the PetscDS object to set options for

-petscds_type type - Set the PetscDS type

-petscds_view - View the PetscDS

-petscds_jac_pre (true|false) - Turn formation of a separate Jacobian preconditioner on or off

-bc_NAME ids - comma separated list of label ids for the boundary condition NAME

-bc_NAME_comp comps - comma separated list of field components to constrain for the boundary condition NAME

PetscDS, PetscDSView()

src/dm/dt/interface/dtds.c

src/ts/tutorials/ex11.c src/ts/tutorials/ex48.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetFromOptions(PetscDS prob)
```

Example 2 (unknown):
```unknown
PetscDSView()
```

---

## PetscDSSetImplicit#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetImplicit/

**Contents:**
- PetscDSSetImplicit#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the flag for implicit solve for this field. This is just a guide for TSARKIMEX

prob - The PetscDS object

implicit - The flag indicating what kind of solve to use for this field

TSARKIMEX, PetscDSGetImplicit(), PetscDSSetDiscretization(), PetscDSAddDiscretization(), PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

src/ts/tutorials/ex30.c src/ts/tutorials/ex45.c src/ts/tutorials/ex48.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetImplicit(PetscDS prob, PetscInt f, PetscBool implicit)
```

Example 2 (unknown):
```unknown
PetscDSGetImplicit()
```

Example 3 (unknown):
```unknown
PetscDSSetDiscretization()
```

Example 4 (unknown):
```unknown
PetscDSAddDiscretization()
```

---

## PetscDSSetIntegrationParameters#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetIntegrationParameters/

**Contents:**
- PetscDSSetIntegrationParameters#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the parameters for a particular integration

ds - The PetscDS object

fieldI - The test field for a given point function, or PETSC_DETERMINE

fieldJ - The basis field for a given point function, or PETSC_DETERMINE

PetscDS, PetscDSSetConstants(), PetscDSGetConstants(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetIntegrationParameters(PetscDS ds, PetscInt fieldI, PetscInt fieldJ)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
PETSC_DETERMINE
```

Example 4 (unknown):
```unknown
PetscDSSetConstants()
```

---

## PetscDSSetJacobian#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetJacobian/

**Contents:**
- PetscDSSetJacobian#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Set the pointwise Jacobian function for given test and basis fields

f - The test field number

g0 - integrand for the test and basis function term, see PetscPointJacFn

g1 - integrand for the test function and basis function gradient term, see PetscPointJacFn

g2 - integrand for the test function gradient and basis function term, see PetscPointJacFn

g3 - integrand for the test function gradient and basis function gradient term, see PetscPointJacFn

We are using a first order FEM model for the weak form:

PetscDS, PetscDSGetJacobian(), PetscPointJacFn

src/dm/dt/interface/dtds.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex77.c src/snes/tutorials/ex26.c src/snes/tutorials/ex17.c src/snes/tutorials/ex8.c src/snes/tutorials/ex64.c src/snes/tutorials/ex62.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetJacobian(PetscDS ds, PetscInt f, PetscInt g, PetscPointJacFn *g0, PetscPointJacFn *g1, PetscPointJacFn *g2, PetscPointJacFn *g3)
```

Example 2 (unknown):
```unknown
PetscPointJacFn
```

Example 3 (unknown):
```unknown
PetscPointJacFn
```

Example 4 (unknown):
```unknown
PetscPointJacFn
```

---

## PetscDSSetJetDegree#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetJetDegree/

**Contents:**
- PetscDSSetJetDegree#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the highest derivative for this field equation, or the k-jet that the discretization needs to tabulate.

ds - The PetscDS object

k - The highest derivative we need to tabulate

PetscDS, PetscDSGetJetDegree(), PetscDSSetDiscretization(), PetscDSAddDiscretization(), PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetJetDegree(PetscDS ds, PetscInt f, PetscInt k)
```

Example 2 (unknown):
```unknown
PetscDSGetJetDegree()
```

Example 3 (unknown):
```unknown
PetscDSSetDiscretization()
```

Example 4 (unknown):
```unknown
PetscDSAddDiscretization()
```

---

## PetscDSSetLowerBound#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetLowerBound/

**Contents:**
- PetscDSSetLowerBound#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the pointwise lower bound function for a given field

lb - lower bound function for the test fields, see PetscPointBoundFn

ctx - lower bound context or NULL which will be passed to lb

PetscDS, PetscPointBoundFn, PetscDSGetLowerBound(), PetscDSGetUpperBound(), PetscDSGetExactSolution()

src/dm/dt/interface/dtds.c

src/snes/tutorials/ex34.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetLowerBound(PetscDS ds, PetscInt f, PetscPointBoundFn *lb, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
PetscPointBoundFn
```

Example 3 (unknown):
```unknown
PetscPointBoundFn
```

Example 4 (unknown):
```unknown
PetscDSGetLowerBound()
```

---

## PetscDSSetObjective#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetObjective/

**Contents:**
- PetscDSSetObjective#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Set the pointwise objective function for a given test field

f - The test field number

obj - integrand for the test function term, see PetscPointFn

We are using a first order FEM model for the weak form: \( \int_\Omega \phi\,\mathrm{obj}(u, u_t, \nabla u, x, t)\)

PetscPointFn, PetscDS, PetscDSGetObjective(), PetscDSSetResidual()

src/dm/dt/interface/dtds.c

src/snes/tutorials/ex11.c src/ts/tutorials/ex30.c src/snes/tutorials/ex13.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/tutorials/ex48.c src/snes/tutorials/ex8.c src/ts/utils/dmplexlandau/tutorials/ex2.c src/snes/tutorials/ex69.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetObjective(PetscDS ds, PetscInt f, PetscPointFn *obj)
```

Example 2 (unknown):
```unknown
PetscPointFn
```

Example 3 (unknown):
```unknown
PetscPointFn
```

Example 4 (unknown):
```unknown
PetscDSGetObjective()
```

---

## PetscDSSetResidual#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetResidual/

**Contents:**
- PetscDSSetResidual#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Set the pointwise residual function for a given test field

f - The test field number

f0 - integrand for the test function term, see PetscPointFn

f1 - integrand for the test function gradient term, see PetscPointFn

We are using a first order FEM model for the weak form: \( \int_\Omega \phi f_0(u, u_t, \nabla u, x, t) + \nabla\phi \cdot {\vec f}_1(u, u_t, \nabla u, x, t)\)

PetscPointFn, PetscDS, PetscDSGetResidual()

src/dm/dt/interface/dtds.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex77.c src/snes/tutorials/ex26.c src/snes/tutorials/ex17.c src/snes/tutorials/ex8.c src/snes/tutorials/ex64.c src/snes/tutorials/ex62.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetResidual(PetscDS ds, PetscInt f, PetscPointFn *f0, PetscPointFn *f1)
```

Example 2 (unknown):
```unknown
PetscPointFn
```

Example 3 (unknown):
```unknown
PetscPointFn
```

Example 4 (unknown):
```unknown
PetscPointFn
```

---

## PetscDSSetRHSResidual#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetRHSResidual/

**Contents:**
- PetscDSSetRHSResidual#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Set the pointwise residual function for explicit timestepping for a given test field

f - The test field number

f0 - integrand for the test function term, see PetscPointFn

f1 - integrand for the test function gradient term, see PetscPointFn

We are using a first order FEM model for the weak form: \( \int_\Omega \phi f_0(u, u_t, \nabla u, x, t) + \nabla\phi \cdot {\vec f}_1(u, u_t, \nabla u, x, t)\)

PetscDS, PetscDSGetResidual()

src/dm/dt/interface/dtds.c

src/ts/tutorials/ex45.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetRHSResidual(PetscDS ds, PetscInt f, PetscPointFn *f0, PetscPointFn *f1)
```

Example 2 (unknown):
```unknown
PetscPointFn
```

Example 3 (unknown):
```unknown
PetscPointFn
```

Example 4 (unknown):
```unknown
PetscDSGetResidual()
```

---

## PetscDSSetRiemannSolver#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetRiemannSolver/

**Contents:**
- PetscDSSetRiemannSolver#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the Riemann solver for the given field

ds - The PetscDS object

r - Riemann solver, see PetscRiemannFn

PetscDS, PetscRiemannFn, PetscDSGetRiemannSolver()

src/dm/dt/interface/dtds.c

src/ts/tutorials/ex11.c src/ts/tutorials/ex18.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetRiemannSolver(PetscDS ds, PetscInt f, PetscRiemannFn *r)
```

Example 2 (unknown):
```unknown
PetscRiemannFn
```

Example 3 (unknown):
```unknown
PetscRiemannFn
```

Example 4 (unknown):
```unknown
PetscDSGetRiemannSolver()
```

---

## PetscDSSetType#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetType/

**Contents:**
- PetscDSSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Builds a particular PetscDS

Collective; No Fortran Support

prob - The PetscDS object

name - The PetscDSType

-petscds_type type - Sets the PetscDS type; use -help for a list of available types

PetscDSType, PetscDS, PetscDSGetType(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetType(PetscDS prob, PetscDSType name)
```

Example 2 (unknown):
```unknown
PetscDSType
```

Example 3 (unknown):
```unknown
PetscDSType
```

Example 4 (unknown):
```unknown
PetscDSGetType()
```

---

## PetscDSSetUpdate#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetUpdate/

**Contents:**
- PetscDSSetUpdate#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the pointwise update function for a given field

update - update function, see PetscPointFn

PetscDS, PetscPointFn, PetscDSGetResidual()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetUpdate(PetscDS ds, PetscInt f, PetscPointFn *update)
```

Example 2 (unknown):
```unknown
PetscPointFn
```

Example 3 (unknown):
```unknown
PetscPointFn
```

Example 4 (unknown):
```unknown
PetscDSGetResidual()
```

---

## PetscDSSetUpperBound#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetUpperBound/

**Contents:**
- PetscDSSetUpperBound#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the pointwise upper bound function for a given field

ub - upper bound function for the test fields, see PetscPointBoundFn

ctx - context or NULL that will be passed to ub

PetscDS, PetscPointBoundFn, PetscDSGetUpperBound(), PetscDSGetLowerBound(), PetscDSGetExactSolution()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetUpperBound(PetscDS ds, PetscInt f, PetscPointBoundFn *ub, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
PetscPointBoundFn
```

Example 3 (unknown):
```unknown
PetscPointBoundFn
```

Example 4 (unknown):
```unknown
PetscDSGetUpperBound()
```

---

## PetscDSSetUp#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetUp/

**Contents:**
- PetscDSSetUp#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Construct data structures for the PetscDS

prob - the PetscDS object to setup

PetscDS, PetscDSView(), PetscDSDestroy()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetUp(PetscDS prob)
```

Example 2 (unknown):
```unknown
PetscDSView()
```

Example 3 (unknown):
```unknown
PetscDSDestroy()
```

---

## PetscDSSetWeakForm#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSSetWeakForm/

**Contents:**
- PetscDSSetWeakForm#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the weak form object to be used by the PetscDS

ds - The PetscDS object

wf - The weak form object

PetscWeakForm, PetscDSGetWeakForm(), PetscDSGetNumFields(), PetscDSCreate()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSSetWeakForm(PetscDS ds, PetscWeakForm wf)
```

Example 2 (unknown):
```unknown
PetscWeakForm
```

Example 3 (unknown):
```unknown
PetscDSGetWeakForm()
```

Example 4 (unknown):
```unknown
PetscDSGetNumFields()
```

---

## PetscDSType#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSType/

**Contents:**
- PetscDSType#
- Synopsis#
- See Also#
- Level#
- Location#

String with the name of a PETSc discrete system

PetscDSSetType(), PetscDS

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef const char *PetscDSType;
#define PETSCDSBASIC "basic"
```

Example 2 (unknown):
```unknown
PetscDSSetType()
```

---

## PetscDSUpdateBoundaryLabels#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSUpdateBoundaryLabels/

**Contents:**
- PetscDSUpdateBoundaryLabels#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Update DMLabel in each boundary condition using the label name and the input DM

ds - The source PetscDS object

dm - The DM holding labels

PetscDS, DMBoundary, DM, PetscDSCopyBoundary(), PetscDSCreate(), DMGetLabel()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSUpdateBoundaryLabels(PetscDS ds, DM dm)
```

Example 2 (unknown):
```unknown
PetscDSCopyBoundary()
```

Example 3 (unknown):
```unknown
PetscDSCreate()
```

Example 4 (unknown):
```unknown
DMGetLabel()
```

---

## PetscDSUpdateBoundary#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSUpdateBoundary/

**Contents:**
- PetscDSUpdateBoundary#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Change a boundary condition for the model.

ds - The PetscDS object

bd - The boundary condition number

type - The type of condition, e.g. DM_BC_ESSENTIAL/DM_BC_ESSENTIAL_FIELD (Dirichlet), or DM_BC_NATURAL (Neumann)

name - The boundary condition name

label - The label defining constrained points

Nv - The number of DMLabel ids for constrained points

values - An array of ids for constrained points

field - The field to constrain

Nc - The number of constrained field components

comps - An array of constrained component numbers

bcFunc - A pointwise function giving boundary values

bcFunc_t - A pointwise function giving the time derivative of the boundary values, or NULL

ctx - An optional application context for bcFunc

The pointwise functions are used to provide boundary values for essential boundary conditions. In FEM, they are acting upon by dual basis functionals to generate FEM coefficients which are fixed. Natural boundary conditions signal to PETSc that boundary integrals should be performed, using the kernels from PetscDSSetBdResidual().

The boundary condition number is the order in which it was registered. The user can get the number of boundary conditions from PetscDSGetNumBoundary(). See PetscDSAddBoundary() for a description of the calling sequences for the callbacks.

PetscDS, PetscWeakForm, DMBoundaryConditionType, PetscDSAddBoundary(), PetscDSGetBoundary(), PetscDSGetNumBoundary(), DMLabel

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSUpdateBoundary(PetscDS ds, PetscInt bd, DMBoundaryConditionType type, const char name[], DMLabel label, PetscInt Nv, const PetscInt values[], PetscInt field, PetscInt Nc, const PetscInt comps[], PetscVoidFn *bcFunc, PetscVoidFn *bcFunc_t, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DM_BC_ESSENTIAL
```

Example 3 (unknown):
```unknown
DM_BC_ESSENTIAL_FIELD
```

Example 4 (unknown):
```unknown
DM_BC_NATURAL
```

---

## PetscDSViewFromOptions#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSViewFromOptions/

**Contents:**
- PetscDSViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

View a PetscDS based on values in the options database

A - the PetscDS object

obj - Optional object that provides the options prefix used in the search of the options database

name - command line option

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

PetscDSType, PetscDS, PetscDSView(), PetscObjectViewFromOptions(), PetscDSCreate()

src/dm/dt/interface/dtds.c

src/snes/tutorials/ex56.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSViewFromOptions(PetscDS A, PetscObject obj, const char name[])
```

Example 2 (unknown):
```unknown
PetscObjectViewFromOptions()
```

Example 3 (unknown):
```unknown
PetscDSType
```

Example 4 (unknown):
```unknown
PetscDSView()
```

---

## PetscDSView#

**URL:** https://petsc.org/release/manualpages/DT/PetscDSView/

**Contents:**
- PetscDSView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

prob - the PetscDS object to view

PetscDSType, PetscDS, PetscViewer, PetscDSDestroy(), PetscDSViewFromOptions()

src/dm/dt/interface/dtds.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscDSView(PetscDS prob, PetscViewer v)
```

Example 2 (unknown):
```unknown
PetscDSType
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PetscDSDestroy()
```

---

## PetscDS#

**URL:** https://petsc.org/release/manualpages/DT/PetscDS/

**Contents:**
- PetscDS#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

PETSc object that manages a discrete system, which is a set of discretizations + continuum equations from a PetscWeakForm

PetscDSCreate(), PetscDSSetType(), PetscDSType, PetscWeakForm, PetscFECreate(), PetscFVCreate()

include/petscdstypes.h

src/snes/tutorials/ex71.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex26.c src/snes/tutorials/ex17.c src/snes/tutorials/ex8.c src/snes/tutorials/ex23.c src/snes/tutorials/ex64.c src/snes/tutorials/ex62.c

_p_PetscDS in include/petsc/private/petscdsimpl.h PetscDS_Basic in include/petsc/private/petscdsimpl.h

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (julia):
```julia
typedef struct _p_PetscDS *PetscDS;
```

Example 3 (unknown):
```unknown
PetscDSCreate()
```

Example 4 (unknown):
```unknown
PetscDSSetType()
```

---

## PetscDTAltVApply#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTAltVApply/

**Contents:**
- PetscDTAltVApply#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Apply an a k-form (an alternating k-linear map) to a set of k N-dimensional vectors

N - the dimension of the vector space, N >= 0

k - the degree k of the k-form w, 0 <= k <= N

w - a k-form, size [N choose k] (each degree of freedom of a k-form is associated with a subset of k coordinates of the N-dimensional vectors. The degrees of freedom are ordered lexicographically by their associated subsets)

v - a set of k vectors of size N, size [k x N], each vector stored contiguously

wv - w(v_1,…,v_k) = \sum_i w_i * det(V_i): the degree of freedom w_i is associated with coordinates [s_{i,1},…,s_{i,k}], and the square matrix V_i has entry (j,k) given by the s_{i,k}’th coordinate of v_j

PetscDTAltV, PetscDTAltVPullback(), PetscDTAltVPullbackMatrix()

src/dm/dt/interface/dtaltv.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTAltVApply(PetscInt N, PetscInt k, const PetscReal *w, const PetscReal *v, PetscReal *wv)
```

Example 2 (unknown):
```unknown
PetscDTAltV
```

Example 3 (unknown):
```unknown
PetscDTAltVPullback()
```

Example 4 (unknown):
```unknown
PetscDTAltVPullbackMatrix()
```

---

## PetscDTAltVInteriorMatrix#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTAltVInteriorMatrix/

**Contents:**
- PetscDTAltVInteriorMatrix#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Compute the matrix of the linear transformation induced on a k-form by the interior product with a vector

N - the dimension of the vector space, N >= 0

k - the degree k of the k-forms on which intvMat acts, 0 <= k <= N

v - an N dimensional vector

intvMat - an [(N choose (k-1)) x (N choose k)] matrix, row-major: (intvMat) * w = (w int v)

PetscDTAltV, PetscDTAltVInterior(), PetscDTAltVInteriorPattern(), PetscDTAltVPullback(), PetscDTAltVPullbackMatrix()

src/dm/dt/interface/dtaltv.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTAltVInteriorMatrix(PetscInt N, PetscInt k, const PetscReal *v, PetscReal *intvMat)
```

Example 2 (unknown):
```unknown
PetscDTAltV
```

Example 3 (unknown):
```unknown
PetscDTAltVInterior()
```

Example 4 (unknown):
```unknown
PetscDTAltVInteriorPattern()
```

---

## PetscDTAltVInteriorPattern#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTAltVInteriorPattern/

**Contents:**
- PetscDTAltVInteriorPattern#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

compute the sparsity and sign pattern of the interior product matrix computed in PetscDTAltVInteriorMatrix()

N - the dimension of the vector space, \(N \ge 0\)

k - the degree of the k-forms on which intvMat from PetscDTAltVInteriorMatrix() acts, \( 0 le k le N \).

indices - The interior product matrix intvMat has dimensions [(N choose (k-1)) x (N choose k)] and has (N choose k) * k non-zeros. indices[i][0] and indices[i][1] are the row and column of a non-zero, and its value is equal to the vector coordinate v[j] if indices[i][2] = j, or -v[j] if indices[i][2] = -(j+1)

This function is useful when the interior product needs to be computed at multiple locations, as when computing the Koszul differential

PetscDTAltV, PetscDTAltVInterior(), PetscDTAltVInteriorMatrix(), PetscDTAltVPullback(), PetscDTAltVPullbackMatrix()

src/dm/dt/interface/dtaltv.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDTAltVInteriorMatrix()
```

Example 2 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTAltVInteriorPattern(PetscInt N, PetscInt k, PetscInt (*indices)[3])
```

Example 3 (unknown):
```unknown
PetscDTAltVInteriorMatrix()
```

Example 4 (unknown):
```unknown
PetscDTAltV
```

---

## PetscDTAltVInterior#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTAltVInterior/

**Contents:**
- PetscDTAltVInterior#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Compute the interior product of a k-form with a vector

N - the dimension of the vector space, N >= 0

k - the degree k of the k-form w, 0 <= k <= N

w - a k-form, size [N choose k]

v - an N dimensional vector

wIntv - the (k-1)-form (w int v), size [N choose (k-1)]: (w int v) is defined by its action on (k-1) vectors {v_1, …, v_{k-1}} as (w inv v)(v_1, …, v_{k-1}) = w(v, v_1, …, v_{k-1}).

PetscDTAltV, PetscDTAltVInteriorMatrix(), PetscDTAltVInteriorPattern(), PetscDTAltVPullback(), PetscDTAltVPullbackMatrix()

src/dm/dt/interface/dtaltv.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTAltVInterior(PetscInt N, PetscInt k, const PetscReal *w, const PetscReal *v, PetscReal *wIntv)
```

Example 2 (unknown):
```unknown
PetscDTAltV
```

Example 3 (unknown):
```unknown
PetscDTAltVInteriorMatrix()
```

Example 4 (unknown):
```unknown
PetscDTAltVInteriorPattern()
```

---

## PetscDTAltVPullbackMatrix#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTAltVPullbackMatrix/

**Contents:**
- PetscDTAltVPullbackMatrix#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Compute the pullback matrix for k-forms under a linear transformation

N - the dimension of the origin vector space of the linear transformation, N >= 0

M - the dimension of the image vector space of the linear transformation, M >= 0

L - a linear transformation, an [M x N] matrix in row-major format

k - the signed degree k of the |k|-forms on which Lstar acts, -(min(M,N)) <= k <= min(M,N). A negative form degree indicates that the pullback should be conjugated by the Hodge star operator (see note in PetscDTAltvPullback())

Lstar - the pullback matrix, an [(N choose |k|) x (M choose |k|)] matrix in row-major format such that Lstar * w = L^* w

PetscDTAltV, PetscDTAltVPullback(), PetscDTAltVStar()

src/dm/dt/interface/dtaltv.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTAltVPullbackMatrix(PetscInt N, PetscInt M, const PetscReal *L, PetscInt k, PetscReal *Lstar)
```

Example 2 (unknown):
```unknown
PetscDTAltvPullback()
```

Example 3 (unknown):
```unknown
PetscDTAltV
```

Example 4 (unknown):
```unknown
PetscDTAltVPullback()
```

---

## PetscDTAltVPullback#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTAltVPullback/

**Contents:**
- PetscDTAltVPullback#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Compute the pullback of a k-form under a linear transformation of the coordinate space

N - the dimension of the origin vector space of the linear transformation, M >= 0

M - the dimension of the image vector space of the linear transformation, N >= 0

L - a linear transformation, an [M x N] matrix in row-major format

k - the signed degree k of the |k|-form w, -(min(M,N)) <= k <= min(M,N). A negative form degree indicates that the pullback should be conjugated by the Hodge star operator (see note).

w - a |k|-form in the image space, size [M choose |k|]

Lstarw - the pullback of w to a |k|-form in the origin space, size [N choose |k|]: (Lstarw)(v_1,…v_k) = w(Lv_1,…,Lv_k).

Negative form degrees accommodate, e.g., H-div conforming vector fields. An H-div conforming vector field stores its degrees of freedom as (dx, dy, dz), like a 1-form, but its normal trace is integrated on faces, like a 2-form. The correct pullback then is to apply the Hodge star transformation from (M-2)-form to 2-form, pullback as a 2-form, then invert the Hodge star transformation.

PetscDTAltV, PetscDTAltVPullbackMatrix(), PetscDTAltVStar()

src/dm/dt/interface/dtaltv.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTAltVPullback(PetscInt N, PetscInt M, const PetscReal *L, PetscInt k, const PetscReal *w, PetscReal *Lstarw)
```

Example 2 (unknown):
```unknown
PetscDTAltV
```

Example 3 (unknown):
```unknown
PetscDTAltVPullbackMatrix()
```

Example 4 (unknown):
```unknown
PetscDTAltVStar()
```

---

## PetscDTAltVStar#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTAltVStar/

**Contents:**
- PetscDTAltVStar#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Apply a power of the Hodge star operator, which maps k-forms to (N-k) forms, to a k-form

N - the dimension of the vector space, N >= 0

k - the degree k of the k-form w, 0 <= k <= N

pow - the number of times to apply the Hodge star operator: pow < 0 indicates that the inverse of the Hodge star operator should be applied |pow| times.

w - a k-form, size [N choose k]

Each degree of freedom of a k-form is associated with a subset S of k coordinates of the N dimensional vector space: the Hodge start operator (star) maps that degree of freedom to the degree of freedom associated with S’, the complement of S, with a sign change if the permutation of coordinates {S[0], … S[k-1], S’[0], starw- 1]} is an odd permutation. This implies (star)^2 w = (-1)^{k(N-k)} w, and (star)^4 w = w.

PetscDTAltV, PetscDTAltVPullback(), PetscDTAltVPullbackMatrix()

src/dm/dt/interface/dtaltv.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTAltVStar(PetscInt N, PetscInt k, PetscInt pow, const PetscReal *w, PetscReal *starw)
```

Example 2 (unknown):
```unknown
PetscDTAltV
```

Example 3 (unknown):
```unknown
PetscDTAltVPullback()
```

Example 4 (unknown):
```unknown
PetscDTAltVPullbackMatrix()
```

---

## PetscDTAltVWedgeMatrix#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTAltVWedgeMatrix/

**Contents:**
- PetscDTAltVWedgeMatrix#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Compute the matrix defined by the wedge product with a given j-form that maps k-forms to (j+k)-forms

N - the dimension of the vector space, N >= 0

j - the degree j of the j-form a, 0 <= j <= N

k - the degree k of the k-forms that (a wedge) will be applied to, 0 <= k <= N and 0 <= j+k <= N

a - a j-form, size [N choose j]

awedgeMat - (a wedge), an [(N choose j+k) x (N choose k)] matrix in row-major order, such that (a wedge) * b = a wedge b

PetscDTAltV, PetscDTAltVPullback(), PetscDTAltVPullbackMatrix()

src/dm/dt/interface/dtaltv.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTAltVWedgeMatrix(PetscInt N, PetscInt j, PetscInt k, const PetscReal *a, PetscReal *awedgeMat)
```

Example 2 (unknown):
```unknown
PetscDTAltV
```

Example 3 (unknown):
```unknown
PetscDTAltVPullback()
```

Example 4 (unknown):
```unknown
PetscDTAltVPullbackMatrix()
```

---

## PetscDTAltVWedge#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTAltVWedge/

**Contents:**
- PetscDTAltVWedge#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Compute the wedge product of a j-form and a k-form, giving a (j+k) form

N - the dimension of the vector space, N >= 0

j - the degree j of the j-form a, 0 <= j <= N

k - the degree k of the k-form b, 0 <= k <= N and 0 <= j+k <= N

a - a j-form, size [N choose j]

b - a k-form, size [N choose k]

awedgeb - the (j+k)-form a wedge b, size [N choose (j+k)]: (a wedge b)(v_1,…,v_{j+k}) = \sum_{s} sign(s) a(v_{s_1},…,v_{s_j}) b(v_{s_{j+1}},…,v_{s_{j+k}}), where the sum is over permutations s such that s_1 < s_2 < … < s_j and s_{j+1} < s_{j+2} < … < s_{j+k}.

PetscDTAltV, PetscDTAltVWedgeMatrix(), PetscDTAltVPullback(), PetscDTAltVPullbackMatrix()

src/dm/dt/interface/dtaltv.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTAltVWedge(PetscInt N, PetscInt j, PetscInt k, const PetscReal *a, const PetscReal *b, PetscReal *awedgeb)
```

Example 2 (unknown):
```unknown
PetscDTAltV
```

Example 3 (unknown):
```unknown
PetscDTAltVWedgeMatrix()
```

Example 4 (unknown):
```unknown
PetscDTAltVPullback()
```

---

## PetscDTAltV#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTAltV/

**Contents:**
- PetscDTAltV#
- vectors from a vector space V and producing a real number#
- The standard basis for Alt^k V, used in PetscDTAltV, has one basis k-form for each ordered subset of k coordinates of the N dimensional space#
- Let f be the basis j-form associated with coordinates (f_1,…,f_j) and g be the basis k-form associated with coordinates (g_1,…,g_k)#
- See Also#
- Level#
- Location#

An interface for common operations on k-forms, also known as alternating algebraic forms or alternating k-linear maps. The name of the interface comes from the notation “Alt V” for the algebra of all k-forms acting vectors in the space V, also known as the exterior algebra of V*. A recommended reference for this material is Section 2 “Exterior algebra and exterior calculus” in “Finite element exterior calculus, homological techniques, and applications”, by Arnold, Falk, & Winther (2006, doi:10.1017/S0962492906210018).

A k-form w (k is called the “form degree” of w) is an alternating k-linear map acting on tuples (v_1, …, v_k) of

alternating: swapping any two vectors in a tuple reverses the sign of the result, e.g. w(v_1, v_2, …, v_k) = -w(v_2, v_1, …, v_k)

k-linear: w acts linear in each vector separately, e.g. w(av + by, v_2, …, v_k) = aw(v,v_2,…,v_k) + bw(y,v_2,…,v_k) This action is implemented as PetscDTAltVApply().

The k-forms on a vector space form a vector space themselves, Alt^k V. The dimension of Alt^k V, if V is N dimensional, is N choose k. (This shows that for an N dimensional space, only 0 <= k <= N are valid form degrees.)

For example, if the coordinate directions of a four dimensional space are (t, x, y, z), then there are 4 choose 2 = 6 ordered subsets of two coordinates. They are, in lexicographic order, (t, x), (t, y), (t, z), (x, y), (x, z) and (y, z). PetscDTAltV also orders the basis of Alt^k V lexicographically by the associated subsets.

The unit basis k-form associated with coordinates (c_1, …, c_k) acts on a set of k vectors (v_1, …, v_k) by creating a square matrix V where V[i,j] = v_i[c_j] and taking the determinant of V.

If j + k <= N, then a j-form f and a k-form g can be multiplied to create a (j+k)-form using the wedge or exterior product, (f wedge g). This is an anticommutative product, (f wedge g) = -(g wedge f). It is sufficient to describe the wedge product of two basis forms.

If there is any coordinate in both sets, then (f wedge g) = 0.

Otherwise, (f wedge g) is a multiple of the basis (j+k)-form h associated with (f_1,…,f_j,g_1,…,g_k).

In fact it is equal to either h or -h depending on how (f_1,…,f_j,g_1,…,g_k) compares to the same list of coordinates given in ascending order: if it is an even permutation of that list, then (f wedge g) = h, otherwise (f wedge g) = -h. The wedge product is implemented for either two inputs (f and g) in PetscDTAltVWedge(), or for one (just f, giving a matrix to multiply against multiple choices of g) in PetscDTAltVWedgeMatrix().

If k > 0, a k-form w and a vector v can combine to make a (k-1)-form through the interior product, (w int v), defined by (w int v)(v_1,…,v_{k-1}) = w(v,v_1,…,v_{k-1}).

The interior product is implemented for either two inputs (w and v) in PetscDTAltVInterior, for one (just v, giving a matrix to multiply against multiple choices of w) in PetscDTAltVInteriorMatrix(), or for no inputs (giving the sparsity pattern of PetscDTAltVInteriorMatrix()) in PetscDTAltVInteriorPattern().

When there is a linear map L: V -> W from an N dimensional vector space to an M dimensional vector space, it induces the linear pullback map L^* : Alt^k W -> Alt^k V, defined by L^* w(v_1,…,v_k) = w(L v_1, …, L v_k). The pullback is implemented as PetscDTAltVPullback() (acting on a known w) and PetscDTAltVPullbackMatrix() (creating a matrix that computes the actin of L^*).

Alt^k V and Alt^(N-k) V have the same dimension, and the Hodge star operator maps between them. We note that Alt^N V is a one dimensional space, and its basis vector is sometime called vol. The Hodge star operator has the property that (f wedge (star g)) = (f,g) vol, where (f,g) is the simple inner product of the basis coefficients of f and g. Powers of the Hodge star operator can be applied with PetscDTAltVStar

PetscDTAltVApply(), PetscDTAltVWedge(), PetscDTAltVInterior(), PetscDTAltVPullback(), PetscDTAltVStar()

src/dm/dt/interface/dtaltv.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDTAltVApply()
```

Example 2 (unknown):
```unknown
PetscDTAltVWedge()
```

Example 3 (unknown):
```unknown
PetscDTAltVWedgeMatrix()
```

Example 4 (unknown):
```unknown
PetscDTAltVInteriorMatrix()
```

---

## PetscDTBaryToIndex#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTBaryToIndex/

**Contents:**
- PetscDTBaryToIndex#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

convert a barycentric coordinate to an index

len - the desired length of the barycentric tuple (usually 1 more than the dimension it represents, so a barycentric coordinate in a triangle has length 3)

sum - the value that the sum of the barycentric coordinates (which will be non-negative integers) should sum to

coord - a barycentric coordinate with the given length len and sum

index - the unique index for the coordinate, >= 0 and < Binomial(len - 1 + sum, sum)

The indices map to barycentric coordinates in lexicographic order, where the first index is the least significant and the last index is the most significant.

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTBaryToIndex(PetscInt len, PetscInt sum, const PetscInt coord[], PetscInt *index)
```

Example 2 (unknown):
```unknown
PetscDTIndexToBary
```

---

## PetscDTBinomialInt#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTBinomialInt/

**Contents:**
- PetscDTBinomialInt#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Compute the binomial coefficient n choose k

n - a non-negative integer

k - an integer between 0 and n, inclusive

binomial - the binomial coefficient n choose k

This is limited by integers that can be represented by PetscInt.

Use PetscDTBinomial() for real number approximations of larger values

PetscDTFactorial(), PetscDTFactorialInt(), PetscDTBinomial(), PetscDTEnumPerm()

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDTBinomial()
```

Example 2 (unknown):
```unknown
PetscDTFactorial()
```

Example 3 (unknown):
```unknown
PetscDTFactorialInt()
```

Example 4 (unknown):
```unknown
PetscDTBinomial()
```

---

## PetscDTBinomial#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTBinomial/

**Contents:**
- PetscDTBinomial#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Approximate the binomial coefficient n choose k

n - a non-negative integer

k - an integer between 0 and n, inclusive

binomial - approximation of the binomial coefficient n choose k

PetscDTFactorial(), PetscDTFactorialInt(), PetscDTBinomialInt(), PetscDTEnumPerm()

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDTFactorial()
```

Example 2 (unknown):
```unknown
PetscDTFactorialInt()
```

Example 3 (unknown):
```unknown
PetscDTBinomialInt()
```

Example 4 (unknown):
```unknown
PetscDTEnumPerm()
```

---

## PetscDTCreateDefaultQuadrature#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTCreateDefaultQuadrature/

**Contents:**
- PetscDTCreateDefaultQuadrature#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Create default quadrature for a given cell

ct - The integration domain

qorder - The desired quadrature order

q - The cell quadrature

fq - The face quadrature

PetscDTCreateQuadratureByCell(), PetscFECreateDefault(), PetscDTGaussTensorQuadrature(), PetscDTSimplexQuadrature(), PetscDTTensorQuadratureCreate()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTCreateDefaultQuadrature(DMPolytopeType ct, PetscInt qorder, PetscQuadrature *q, PetscQuadrature *fq)
```

Example 2 (unknown):
```unknown
PetscDTCreateQuadratureByCell()
```

Example 3 (unknown):
```unknown
PetscFECreateDefault()
```

Example 4 (unknown):
```unknown
PetscDTGaussTensorQuadrature()
```

---

## PetscDTCreateQuadratureByCell#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTCreateQuadratureByCell/

**Contents:**
- PetscDTCreateQuadratureByCell#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Create default quadrature for a given cell

ct - The integration domain

qorder - The desired quadrature order

qtype - The type of simplex quadrature, or PETSCDTSIMPLEXQUAD_DEFAULT

q - The cell quadrature

fq - The face quadrature

PetscDTCreateDefaultQuadrature(), PetscFECreateDefault(), PetscDTGaussTensorQuadrature(), PetscDTSimplexQuadrature(), PetscDTTensorQuadratureCreate()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTCreateQuadratureByCell(DMPolytopeType ct, PetscInt qorder, PetscDTSimplexQuadratureType qtype, PetscQuadrature *q, PetscQuadrature *fq)
```

Example 2 (unknown):
```unknown
PetscDTCreateDefaultQuadrature()
```

Example 3 (unknown):
```unknown
PetscFECreateDefault()
```

Example 4 (unknown):
```unknown
PetscDTGaussTensorQuadrature()
```

---

## PetscDTEnumPerm#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTEnumPerm/

**Contents:**
- PetscDTEnumPerm#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Get a permutation of n integers from its encoding into the integers [0, n!) as a sequence of swaps.

n - a non-negative integer (see note about limits below)

k - an integer in [0, n!)

perm - the permuted list of the integers [0, …, n-1]

isOdd - if not NULL, returns whether the permutation used an even or odd number of swaps.

A permutation can be described by the operations that convert the lists [0, 1, …, n-1] into the permutation, by a sequence of swaps, where the ith step swaps whatever number is in ith position with a number that is in some position j >= i. This swap is encoded as the difference (j - i). The difference d_i at step i is less than (n - i). This sequence of n-1 differences [d_0, …, d_{n-2}] is encoded as the number (n-1)! * d_0 + (n-2)! * d_1 + … + 1! * d_{n-2}.

Limited to n such that n! can be represented by PetscInt, which is 12 if PetscInt is a signed 32-bit integer and 20 if PetscInt is a signed 64-bit integer.

PetscDTFactorial(), PetscDTFactorialInt(), PetscDTBinomial(), PetscDTBinomialInt(), PetscDTPermIndex()

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDTFactorial()
```

Example 2 (unknown):
```unknown
PetscDTFactorialInt()
```

Example 3 (unknown):
```unknown
PetscDTBinomial()
```

Example 4 (unknown):
```unknown
PetscDTBinomialInt()
```

---

## PetscDTEnumSplit#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTEnumSplit/

**Contents:**
- PetscDTEnumSplit#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Split the integers [0, …, n - 1] into two complementary ordered subsets, the first subset of size k and being the jth subset of that size in lexicographic order.

n - a non-negative integer (see note about limits below)

k - an integer in [0, n]

j - an index in [0, n choose k)

perm - the jth subset of size k of the integers [0, …, n - 1], followed by its complementary set.

isOdd - if not NULL, return whether perm is an even or odd permutation.

Limited by arguments such that n choose k can be represented by PetscInt

PetscDTEnumSubset(), PetscDTSubsetIndex(), PetscDTFactorial(), PetscDTFactorialInt(), PetscDTBinomial(), PetscDTBinomialInt(), PetscDTEnumPerm(), PetscDTPermIndex()

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDTEnumSubset()
```

Example 2 (unknown):
```unknown
PetscDTSubsetIndex()
```

Example 3 (unknown):
```unknown
PetscDTFactorial()
```

Example 4 (unknown):
```unknown
PetscDTFactorialInt()
```

---

## PetscDTEnumSubset#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTEnumSubset/

**Contents:**
- PetscDTEnumSubset#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Get an ordered subset of the integers [0, …, n - 1] from its encoding as an integers in [0, n choose k). The encoding is in lexicographic order.

n - a non-negative integer (see note about limits below)

k - an integer in [0, n]

j - an index in [0, n choose k)

subset - the jth subset of size k of the integers [0, …, n - 1]

Limited by arguments such that n choose k can be represented by PetscInt

PetscDTSubsetIndex(), PetscDTFactorial(), PetscDTFactorialInt(), PetscDTBinomial(), PetscDTBinomialInt(), PetscDTEnumPerm(), PetscDTPermIndex()

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDTSubsetIndex()
```

Example 2 (unknown):
```unknown
PetscDTFactorial()
```

Example 3 (unknown):
```unknown
PetscDTFactorialInt()
```

Example 4 (unknown):
```unknown
PetscDTBinomial()
```

---

## PetscDTFactorialInt#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTFactorialInt/

**Contents:**
- PetscDTFactorialInt#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Compute n! as an integer

n - a non-negative integer

This is limited to n such that n! can be represented by PetscInt, which is 12 if PetscInt is a signed 32-bit integer and 20 if PetscInt is a signed 64-bit integer.

PetscDTFactorial(), PetscDTBinomialInt(), PetscDTBinomial()

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDTFactorial()
```

Example 2 (unknown):
```unknown
PetscDTBinomialInt()
```

Example 3 (unknown):
```unknown
PetscDTBinomial()
```

---

## PetscDTFactorial#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTFactorial/

**Contents:**
- PetscDTFactorial#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Approximate n! as a real number

n - a non-negative integer

PetscDTFactorialInt(), PetscDTBinomialInt(), PetscDTBinomial()

src/dm/tutorials/ex26.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDTFactorialInt()
```

Example 2 (unknown):
```unknown
PetscDTBinomialInt()
```

Example 3 (unknown):
```unknown
PetscDTBinomial()
```

---

## PetscDTGaussJacobiQuadrature#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTGaussJacobiQuadrature/

**Contents:**
- PetscDTGaussJacobiQuadrature#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

quadrature for the interval \([a, b]\) with the weight function \((x-a)^\alpha (x-b)^\beta\).

npoints - the number of points in the quadrature rule

a - the left endpoint of the interval

b - the right endpoint of the interval

alpha - the left exponent

beta - the right exponent

x - array of length npoints, the locations of the quadrature points

w - array of length npoints, the weights of the quadrature points

This quadrature rule is exact for polynomials up to degree 2*npoints - 1.

PetscDTGaussQuadrature()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTGaussJacobiQuadrature(PetscInt npoints, PetscReal a, PetscReal b, PetscReal alpha, PetscReal beta, PetscReal x[], PetscReal w[])
```

Example 2 (unknown):
```unknown
PetscDTGaussQuadrature()
```

---

## PetscDTGaussLobattoJacobiQuadrature#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTGaussLobattoJacobiQuadrature/

**Contents:**
- PetscDTGaussLobattoJacobiQuadrature#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

quadrature for the interval \([a, b]\) with the weight function \((x-a)^\alpha (x-b)^\beta\), with endpoints a and b included as quadrature points.

npoints - the number of points in the quadrature rule

a - the left endpoint of the interval

b - the right endpoint of the interval

alpha - the left exponent

beta - the right exponent

x - array of length npoints, the locations of the quadrature points

w - array of length npoints, the weights of the quadrature points

This quadrature rule is exact for polynomials up to degree 2*npoints - 3.

PetscDTGaussJacobiQuadrature()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTGaussLobattoJacobiQuadrature(PetscInt npoints, PetscReal a, PetscReal b, PetscReal alpha, PetscReal beta, PetscReal x[], PetscReal w[])
```

Example 2 (unknown):
```unknown
PetscDTGaussJacobiQuadrature()
```

---

## PetscDTGaussLobattoLegendreQuadrature#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTGaussLobattoLegendreQuadrature/

**Contents:**
- PetscDTGaussLobattoLegendreQuadrature#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

creates a set of the locations and weights of the Gauss-Lobatto-Legendre nodes of a given size on the domain \([-1,1]\)

npoints - number of grid nodes

type - PETSCGAUSSLOBATTOLEGENDRE_VIA_LINEAR_ALGEBRA or PETSCGAUSSLOBATTOLEGENDRE_VIA_NEWTON

x - quadrature points, pass in an array of length npoints

w - quadrature weights, pass in an array of length npoints

For n > 30 the Newton approach computes duplicate (incorrect) values for some nodes because the initial guess is apparently not close enough to the desired solution

These are useful for implementing spectral methods based on Gauss-Lobatto-Legendre (GLL) nodes

See https://epubs.siam.org/doi/abs/10.1137/110855442 https://epubs.siam.org/doi/abs/10.1137/120889873 for better ways to compute GLL nodes

PetscDTGaussQuadrature(), PetscGaussLobattoLegendreCreateType

src/dm/dt/interface/dt.c

src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/tutorials/ex50.c src/ksp/ksp/tutorials/ex68.c src/ksp/ksp/tutorials/ex69.c src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTGaussLobattoLegendreQuadrature(PetscInt npoints, PetscGaussLobattoLegendreCreateType type, PetscReal x[], PetscReal w[])
```

Example 2 (unknown):
```unknown
PETSCGAUSSLOBATTOLEGENDRE_VIA_LINEAR_ALGEBRA
```

Example 3 (unknown):
```unknown
PETSCGAUSSLOBATTOLEGENDRE_VIA_NEWTON
```

Example 4 (unknown):
```unknown
PetscDTGaussQuadrature()
```

---

## PetscDTGaussQuadrature#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTGaussQuadrature/

**Contents:**
- PetscDTGaussQuadrature#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- References#
- See Also#
- Level#
- Location#
- Examples#

create Gauss-Legendre quadrature

npoints - number of points

a - left end of interval (often-1)

b - right end of interval (often +1)

x - quadrature points

w - quadrature weights

Gene H Golub and John H Welsch. Calculation of Gauss quadrature rules. Mathematics of computation, 23(106):221–230, 1969.

PetscDTLegendreEval(), PetscDTGaussJacobiQuadrature()

src/dm/dt/interface/dt.c

src/snes/tutorials/ex31.c src/ksp/ksp/tutorials/ex74.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTGaussQuadrature(PetscInt npoints, PetscReal a, PetscReal b, PetscReal x[], PetscReal w[])
```

Example 2 (unknown):
```unknown
PetscDTLegendreEval()
```

Example 3 (unknown):
```unknown
PetscDTGaussJacobiQuadrature()
```

---

## PetscDTGaussTensorQuadrature#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTGaussTensorQuadrature/

**Contents:**
- PetscDTGaussTensorQuadrature#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

creates a tensor-product Gauss quadrature

dim - The spatial dimension

Nc - The number of components

npoints - number of points in one dimension

a - left end of interval (often-1)

b - right end of interval (often +1)

q - A PetscQuadrature object

PetscDTGaussQuadrature(), PetscDTLegendreEval()

src/dm/dt/interface/dt.c

src/dm/field/tutorials/ex1.c src/ksp/ksp/tutorials/ex70.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTGaussTensorQuadrature(PetscInt dim, PetscInt Nc, PetscInt npoints, PetscReal a, PetscReal b, PetscQuadrature *q)
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
PetscDTGaussQuadrature()
```

Example 4 (unknown):
```unknown
PetscDTLegendreEval()
```

---

## PetscDTGradedOrderToIndex#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTGradedOrderToIndex/

**Contents:**
- PetscDTGradedOrderToIndex#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

convert a tuple into an index in a graded order, the inverse of PetscDTIndexToGradedOrder().

len - the length of the degree tuple

degtup - tuple with this length

index - index in graded order: >= 0

For two tuples x and y with the same degree sum, partial degree sums over the final elements of the tuples acts as a tiebreaker. For example, (2, 1, 1) and (1, 2, 1) have the same degree sum, but the degree sum over the last two elements is smaller for the former, so (2, 1, 1) < (1, 2, 1).

PetscDTIndexToGradedOrder()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDTIndexToGradedOrder()
```

Example 2 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTGradedOrderToIndex(PetscInt len, const PetscInt degtup[], PetscInt *index)
```

Example 3 (unknown):
```unknown
PetscDTIndexToGradedOrder()
```

---

## PetscDTIndexToBary#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTIndexToBary/

**Contents:**
- PetscDTIndexToBary#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

convert an index into a barycentric coordinate.

len - the desired length of the barycentric tuple (usually 1 more than the dimension it represents, so a barycentric coordinate in a triangle has length 3)

sum - the value that the sum of the barycentric coordinates (which will be non-negative integers) should sum to

index - the index to convert: should be >= 0 and < Binomial(len - 1 + sum, sum)

coord - will be filled with the barycentric coordinate, of length n

The indices map to barycentric coordinates in lexicographic order, where the first index is the least significant and the last index is the most significant.

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTIndexToBary(PetscInt len, PetscInt sum, PetscInt index, PetscInt coord[])
```

Example 2 (unknown):
```unknown
PetscDTBaryToIndex()
```

---

## PetscDTIndexToGradedOrder#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTIndexToGradedOrder/

**Contents:**
- PetscDTIndexToGradedOrder#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

convert an index into a tuple of monomial degrees in a graded order (that is, if the degree sum of tuple x is less than the degree sum of tuple y, then the index of x is smaller than the index of y)

len - the desired length of the degree tuple

index - the index to convert: should be >= 0

degtup - filled with a tuple of degrees

For two tuples x and y with the same degree sum, partial degree sums over the final elements of the tuples acts as a tiebreaker. For example, (2, 1, 1) and (1, 2, 1) have the same degree sum, but the degree sum over the last two elements is smaller for the former, so (2, 1, 1) < (1, 2, 1).

PetscDTGradedOrderToIndex()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTIndexToGradedOrder(PetscInt len, PetscInt index, PetscInt degtup[])
```

Example 2 (unknown):
```unknown
PetscDTGradedOrderToIndex()
```

---

## PetscDTJacobiEvalJet#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTJacobiEvalJet/

**Contents:**
- PetscDTJacobiEvalJet#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Evaluate the jet (function and derivatives) of the Jacobi polynomials basis up to a given degree.

alpha - the left exponent of the weight

beta - the right exponetn of the weight

npoints - the number of points to evaluate the polynomials at

points - [npoints] array of point coordinates

degree - the maximm degree polynomial space to evaluate, (degree + 1) will be evaluated total.

k - the maximum derivative to evaluate in the jet, (k + 1) will be evaluated total.

p - an array containing the evaluations of the Jacobi polynomials’s jets on the points. the size is (degree + 1) x (k + 1) x npoints, which also describes the order of the dimensions of this three-dimensional array: the first (slowest varying) dimension is polynomial degree; the second dimension is derivative order; the third (fastest varying) dimension is the index of the evaluation point.

The Jacobi polynomials with indices \(\alpha\) and \(\beta\) are orthogonal with respect to the weighted inner product \(\langle f, g \rangle = \int_{-1}^1 (1+x)^{\alpha} (1-x)^{\beta} f(x) g(x) dx\).

PetscDTJacobiEval(), PetscDTPKDEvalJet()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTJacobiEvalJet(PetscReal alpha, PetscReal beta, PetscInt npoints, const PetscReal points[], PetscInt degree, PetscInt k, PetscReal p[])
```

Example 2 (unknown):
```unknown
PetscDTJacobiEval()
```

Example 3 (unknown):
```unknown
PetscDTPKDEvalJet()
```

---

## PetscDTJacobiEval#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTJacobiEval/

**Contents:**
- PetscDTJacobiEval#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

evaluate Jacobi polynomials for the weight function \((1.+x)^{\alpha} (1.-x)^{\beta}\) at a set of points at points

npoints - number of spatial points to evaluate at

alpha - the left exponent > -1

beta - the right exponent > -1

points - array of locations to evaluate at

ndegree - number of basis degrees to evaluate

degrees - sorted array of degrees to evaluate

B - row-oriented basis evaluation matrix B[pointndegree + degree] (dimension npointsndegrees, allocated by caller) (or NULL)

D - row-oriented derivative evaluation matrix (or NULL)

D2 - row-oriented second derivative evaluation matrix (or NULL)

PetscDTGaussQuadrature(), PetscDTLegendreEval()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTJacobiEval(PetscInt npoints, PetscReal alpha, PetscReal beta, const PetscReal *points, PetscInt ndegree, const PetscInt *degrees, PeOp PetscReal B[], PeOp PetscReal D[], PeOp PetscReal D2[])
```

Example 2 (unknown):
```unknown
PetscDTGaussQuadrature()
```

Example 3 (unknown):
```unknown
PetscDTLegendreEval()
```

---

## PetscDTJacobiNorm#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTJacobiNorm/

**Contents:**
- PetscDTJacobiNorm#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Compute the weighted L2 norm of a Jacobi polynomial.

\(\| P^{\alpha,\beta}_n \|_{\alpha,\beta}^2 = \int_{-1}^1 (1 + x)^{\alpha} (1 - x)^{\beta} P^{\alpha,\beta}_n (x)^2 dx.\)

alpha - the left exponent > -1

beta - the right exponent > -1

n - the polynomial degree

norm - the weighted L2 norm

PetscQuadrature, PetscDTJacobiEval()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTJacobiNorm(PetscReal alpha, PetscReal beta, PetscInt n, PetscReal *norm)
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
PetscDTJacobiEval()
```

---

## PetscDTLegendreEval#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTLegendreEval/

**Contents:**
- PetscDTLegendreEval#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

evaluate Legendre polynomials at points

npoints - number of spatial points to evaluate at

points - array of locations to evaluate at

ndegree - number of basis degrees to evaluate

degrees - sorted array of degrees to evaluate

B - row-oriented basis evaluation matrix B[pointndegree + degree] (dimension npointsndegrees, allocated by caller) (or NULL)

D - row-oriented derivative evaluation matrix (or NULL)

D2 - row-oriented second derivative evaluation matrix (or NULL)

PetscDTGaussQuadrature()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTLegendreEval(PetscInt npoints, const PetscReal *points, PetscInt ndegree, const PetscInt *degrees, PeOp PetscReal B[], PeOp PetscReal D[], PeOp PetscReal D2[])
```

Example 2 (unknown):
```unknown
PetscDTGaussQuadrature()
```

---

## PetscDTNodeType#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTNodeType/

**Contents:**
- PetscDTNodeType#
- Synopsis#
- Values#
- Note#
- See Also#
- Level#
- Location#

A description of strategies for generating nodes (both quadrature nodes and nodes for Lagrange polynomials)

PETSCDTNODES_DEFAULT - Nodes chosen by PETSc

PETSCDTNODES_GAUSSJACOBI - Nodes at either Gauss-Jacobi or Gauss-Lobatto-Jacobi quadrature points

PETSCDTNODES_EQUISPACED - Nodes equispaced either including the endpoints or excluding them

PETSCDTNODES_TANHSINH - Nodes at Tanh-Sinh quadrature points

A PetscDTNodeType can be paired with a PetscBool to indicate whether the nodes include endpoints or not, and in the case of PETSCDT_GAUSSJACOBI with exponents for the weight function.

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  PETSCDTNODES_DEFAULT     = -1,
  PETSCDTNODES_GAUSSJACOBI = 0,
  PETSCDTNODES_EQUISPACED  = 1,
  PETSCDTNODES_TANHSINH    = 2
} PetscDTNodeType;
```

Example 2 (unknown):
```unknown
PETSCDTNODES_DEFAULT
```

Example 3 (unknown):
```unknown
PETSCDTNODES_GAUSSJACOBI
```

Example 4 (unknown):
```unknown
PETSCDTNODES_EQUISPACED
```

---

## PetscDTPermIndex#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTPermIndex/

**Contents:**
- PetscDTPermIndex#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Encode a permutation of n into an integer in [0, n!). This inverts PetscDTEnumPerm().

n - a non-negative integer (see note about limits below)

perm - the permuted list of the integers [0, …, n-1]

k - an integer in [0, n!)

isOdd - if not NULL, returns whether the permutation used an even or odd number of swaps.

Limited to n such that n! can be represented by PetscInt, which is 12 if PetscInt is a signed 32-bit integer and 20 if PetscInt is a signed 64-bit integer.

PetscDTFactorial(), PetscDTFactorialInt(), PetscDTBinomial(), PetscDTBinomialInt(), PetscDTEnumPerm()

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDTEnumPerm()
```

Example 2 (unknown):
```unknown
PetscDTFactorial()
```

Example 3 (unknown):
```unknown
PetscDTFactorialInt()
```

Example 4 (unknown):
```unknown
PetscDTBinomial()
```

---

## PetscDTPKDEvalJet#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTPKDEvalJet/

**Contents:**
- PetscDTPKDEvalJet#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Evaluate the jet (function and derivatives) of the Proriol-Koornwinder-Dubiner (PKD) basis for the space of polynomials up to a given degree.

dim - the number of variables in the multivariate polynomials

npoints - the number of points to evaluate the polynomials at

points - [npoints x dim] array of point coordinates

degree - the degree (sum of degrees on the variables in a monomial) of the polynomial space to evaluate. There are ((dim + degree) choose dim) polynomials in this space.

k - the maximum order partial derivative to evaluate in the jet. There are (dim + k choose dim) partial derivatives in the jet. Choosing k = 0 means to evaluate just the function and no derivatives

p - an array containing the evaluations of the PKD polynomials’ jets on the points. The size is ((dim + degree) choose dim) x ((dim + k) choose dim) x npoints, which also describes the order of the dimensions of this three-dimensional array: the first (slowest varying) dimension is basis function index; the second dimension is jet index; the third (fastest varying) dimension is the index of the evaluation point.

The PKD basis is L2-orthonormal on the biunit simplex (which is used as the reference element for finite elements in PETSc), which makes it a stable basis to use for evaluating polynomials in that domain.

The ordering of the basis functions, and the ordering of the derivatives in the jet, both follow the graded ordering of PetscDTIndexToGradedOrder() and PetscDTGradedOrderToIndex(). For example, in 3D, the polynomial with leading monomial x^2,y^0,z^1, which has degree tuple (2,0,1), which by PetscDTGradedOrderToIndex() has index 12 (it is the 13th basis function in the space); the partial derivative \(\partial_x \partial_z\) has order tuple (1,0,1), appears at index 6 in the jet (it is the 7th partial derivative in the jet).

The implementation uses Kirby’s singularity-free evaluation algorithm, https://doi.org/10.1145/1644001.1644006.

PetscDTGradedOrderToIndex(), PetscDTIndexToGradedOrder(), PetscDTJacobiEvalJet()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTPKDEvalJet(PetscInt dim, PetscInt npoints, const PetscReal points[], PetscInt degree, PetscInt k, PetscReal p[])
```

Example 2 (unknown):
```unknown
PetscDTIndexToGradedOrder()
```

Example 3 (unknown):
```unknown
PetscDTGradedOrderToIndex()
```

Example 4 (unknown):
```unknown
PetscDTGradedOrderToIndex()
```

---

## PetscDTPTrimmedEvalJet#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTPTrimmedEvalJet/

**Contents:**
- PetscDTPTrimmedEvalJet#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Evaluate the jet (function and derivatives) of a basis of the trimmed polynomial k-forms up to a given degree.

dim - the number of variables in the multivariate polynomials

npoints - the number of points to evaluate the polynomials at

points - [npoints x dim] array of point coordinates

degree - the degree (sum of degrees on the variables in a monomial) of the trimmed polynomial space to evaluate. There are ((dim + degree) choose (dim + formDegree)) x ((degree + formDegree - 1) choose (formDegree)) polynomials in this space. (You can use PetscDTPTrimmedSize() to compute this size.)

formDegree - the degree of the form

jetDegree - the maximum order partial derivative to evaluate in the jet. There are ((dim + jetDegree) choose dim) partial derivatives in the jet. Choosing jetDegree = 0 means to evaluate just the function and no derivatives

p - an array containing the evaluations of the PKD polynomials’ jets on the points.

The size of p is PetscDTPTrimmedSize() x ((dim + formDegree) choose dim) x ((dim + k) choose dim) x npoints,which also describes the order of the dimensions of this four-dimensional array:

the first (slowest varying) dimension is basis function index; the second dimension is component of the form; the third dimension is jet index; the fourth (fastest varying) dimension is the index of the evaluation point.

The ordering of the basis functions is not graded, so the basis functions are not nested by degree like PetscDTPKDEvalJet(). The basis functions are not an L2-orthonormal basis on any particular domain.

The implementation is based on the description of the trimmed polynomials up to degree r as the direct sum of polynomials up to degree (r-1) and the Koszul differential applied to homogeneous polynomials of degree (r-1).

PetscDTPKDEvalJet(), PetscDTPTrimmedSize()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTPTrimmedEvalJet(PetscInt dim, PetscInt npoints, const PetscReal points[], PetscInt degree, PetscInt formDegree, PetscInt jetDegree, PetscReal p[])
```

Example 2 (unknown):
```unknown
PetscDTPTrimmedSize()
```

Example 3 (unknown):
```unknown
PetscDTPTrimmedSize()
```

Example 4 (unknown):
```unknown
PetscDTPKDEvalJet()
```

---

## PetscDTPTrimmedSize#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTPTrimmedSize/

**Contents:**
- PetscDTPTrimmedSize#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

The size of the trimmed polynomial space of k-forms with a given degree and form degree, which can be evaluated in PetscDTPTrimmedEvalJet().

dim - the number of variables in the multivariate polynomials

degree - the degree (sum of degrees on the variables in a monomial) of the trimmed polynomial space.

formDegree - the degree of the form

size - The number ((dim + degree) choose (dim + formDegree)) x ((degree + formDegree - 1) choose (formDegree))

PetscDTPTrimmedEvalJet()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDTPTrimmedEvalJet()
```

Example 2 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTPTrimmedSize(PetscInt dim, PetscInt degree, PetscInt formDegree, PetscInt *size)
```

Example 3 (unknown):
```unknown
PetscDTPTrimmedEvalJet()
```

---

## PetscDTReconstructPoly#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTReconstructPoly/

**Contents:**
- PetscDTReconstructPoly#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

create matrix representing polynomial reconstruction using cell intervals and evaluation at target intervals

degree - degree of reconstruction polynomial

nsource - number of source intervals

sourcex - sorted coordinates of source cell boundaries (length nsource+1)

ntarget - number of target intervals

targetx - sorted coordinates of target cell boundaries (length ntarget+1)

R - reconstruction matrix, utarget = sum_s R[t*nsource+s] * usource[s]

PetscDTLegendreEval()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTReconstructPoly(PetscInt degree, PetscInt nsource, const PetscReal sourcex[], PetscInt ntarget, const PetscReal targetx[], PetscReal R[])
```

Example 2 (unknown):
```unknown
PetscDTLegendreEval()
```

---

## PetscDTSimplexQuadratureType#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTSimplexQuadratureType/

**Contents:**
- PetscDTSimplexQuadratureType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

A description of classes of quadrature rules for simplices

PETSCDTSIMPLEXQUAD_DEFAULT - Quadrature rule chosen by PETSc

PETSCDTSIMPLEXQUAD_CONIC - Quadrature rules constructed as conically-warped tensor products of 1D Gauss-Jacobi quadrature rules. These are explicitly computable in any dimension for any degree, and the tensor-product structure can be exploited by sum-factorization methods, but they are not efficient in terms of nodes per polynomial degree.

PETSCDTSIMPLEXQUAD_MINSYM - Quadrature rules that are fully symmetric (symmetries of the simplex preserve the nodes and weights) with minimal (or near minimal) number of nodes. In dimensions higher than 1 these are not simple to compute, so lookup tables are used.

PetscQuadrature, PetscDTSimplexQuadrature()

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  PETSCDTSIMPLEXQUAD_DEFAULT = -1,
  PETSCDTSIMPLEXQUAD_CONIC   = 0,
  PETSCDTSIMPLEXQUAD_MINSYM  = 1
} PetscDTSimplexQuadratureType;
```

Example 2 (unknown):
```unknown
PETSCDTSIMPLEXQUAD_DEFAULT
```

Example 3 (unknown):
```unknown
PETSCDTSIMPLEXQUAD_CONIC
```

Example 4 (unknown):
```unknown
PETSCDTSIMPLEXQUAD_MINSYM
```

---

## PetscDTSimplexQuadrature#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTSimplexQuadrature/

**Contents:**
- PetscDTSimplexQuadrature#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Create a quadrature rule for a simplex that exactly integrates polynomials up to a given degree.

dim - The spatial dimension of the simplex (1 = segment, 2 = triangle, 3 = tetrahedron)

degree - The largest polynomial degree that is required to be integrated exactly

type - PetscDTSimplexQuadratureType indicating the type of quadrature rule

quad - A PetscQuadrature object for integration over the biunit simplex (defined by the bounds \(x_i >= -1\) and \(\sum_i x_i <= 2 - d\)) that is exact for polynomials up to the given degree

PetscDTSimplexQuadratureType, PetscDTGaussQuadrature(), PetscDTStroudCononicalQuadrature(), PetscQuadrature

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTSimplexQuadrature(PetscInt dim, PetscInt degree, PetscDTSimplexQuadratureType type, PetscQuadrature *quad)
```

Example 2 (unknown):
```unknown
PetscDTSimplexQuadratureType
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscDTSimplexQuadratureType
```

---

## PetscDTStroudConicalQuadrature#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTStroudConicalQuadrature/

**Contents:**
- PetscDTStroudConicalQuadrature#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- References#
- See Also#
- Level#
- Location#
- Examples#

create Stroud conical quadrature for a simplex [KS05]

dim - The simplex dimension

Nc - The number of components

npoints - The number of points in one dimension

a - left end of interval (often-1)

b - right end of interval (often +1)

q - A PetscQuadrature object

For dim == 1, this is Gauss-Legendre quadrature

George Karniadakis and Spencer J Sherwin. Spectral/hp element methods for computational fluid dynamics. Oxford University Press, USA, 2005.

PetscDTGaussTensorQuadrature(), PetscDTGaussQuadrature()

src/dm/dt/interface/dt.c

src/dm/field/tutorials/ex1.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTStroudConicalQuadrature(PetscInt dim, PetscInt Nc, PetscInt npoints, PetscReal a, PetscReal b, PetscQuadrature *q)
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
PetscDTGaussTensorQuadrature()
```

Example 4 (unknown):
```unknown
PetscDTGaussQuadrature()
```

---

## PetscDTSubsetIndex#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTSubsetIndex/

**Contents:**
- PetscDTSubsetIndex#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Convert an ordered subset of k integers from the set [0, …, n - 1] to its encoding as an integers in [0, n choose k) in lexicographic order. This is the inverse of PetscDTEnumSubset.

n - a non-negative integer (see note about limits below)

k - an integer in [0, n]

subset - an ordered subset of the integers [0, …, n - 1]

index - the rank of the subset in lexicographic order

Limited by arguments such that n choose k can be represented by PetscInt

PetscDTEnumSubset(), PetscDTFactorial(), PetscDTFactorialInt(), PetscDTBinomial(), PetscDTBinomialInt(), PetscDTEnumPerm(), PetscDTPermIndex()

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDTEnumSubset
```

Example 2 (unknown):
```unknown
PetscDTEnumSubset()
```

Example 3 (unknown):
```unknown
PetscDTFactorial()
```

Example 4 (unknown):
```unknown
PetscDTFactorialInt()
```

---

## PetscDTTanhSinhIntegrateMPFR#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTTanhSinhIntegrateMPFR/

**Contents:**
- PetscDTTanhSinhIntegrateMPFR#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

High-precision version of PetscDTTanhSinhIntegrate() that uses the MPFR arbitrary-precision library to evaluate the quadrature

Not Collective; No Fortran Support

func - the integrand callback (func(x, ctx, &value) evaluates the integrand at point x)

a - lower limit of integration

b - upper limit of integration

digits - target number of correct decimal digits (also drives the working MPFR precision)

ctx - optional application context passed to func

sol - the approximate value of the integral

Requires PETSc to be configured with --with-mpfr; otherwise an error is raised.

PetscDTTanhSinhIntegrate(), PetscDTGaussQuadrature()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDTTanhSinhIntegrate()
```

Example 2 (unknown):
```unknown
#include "petscdt.h" 
#if defined(PETSC_HAVE_MPFR)
PetscErrorCode PetscDTTanhSinhIntegrateMPFR(void (*func)(const PetscReal[], PetscCtx, PetscReal *), PetscReal a, PetscReal b, PetscInt digits, PetscCtx ctx, PetscReal *sol)
```

Example 3 (unknown):
```unknown
func(x, ctx, &value)
```

Example 4 (unknown):
```unknown
--with-mpfr
```

---

## PetscDTTanhSinhIntegrate#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTTanhSinhIntegrate/

**Contents:**
- PetscDTTanhSinhIntegrate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Approximate \(\int_a^b f(x)\,dx\) to a requested precision using adaptive tanh-sinh (double-exponential) quadrature

Not Collective; No Fortran Support

func - the integrand callback (func(x, ctx, &value) evaluates the integrand at point x)

a - lower limit of integration

b - upper limit of integration

digits - target number of correct decimal digits

ctx - optional application context passed to func

sol - the approximate value of the integral

Doubles the number of quadrature points at each refinement level until the change in the integral falls below the requested tolerance. Suitable for smooth integrands and integrands with endpoint singularities.

For arbitrary-precision arithmetic via MPFR, see PetscDTTanhSinhIntegrateMPFR().

PetscDTTanhSinhIntegrateMPFR(), PetscDTGaussQuadrature()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTTanhSinhIntegrate(void (*func)(const PetscReal[], PetscCtx, PetscReal *), PetscReal a, PetscReal b, PetscInt digits, PetscCtx ctx, PetscReal *sol)
```

Example 2 (unknown):
```unknown
func(x, ctx, &value)
```

Example 3 (unknown):
```unknown
PetscDTTanhSinhIntegrateMPFR()
```

Example 4 (unknown):
```unknown
PetscDTTanhSinhIntegrateMPFR()
```

---

## PetscDTTanhSinhTensorQuadrature#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTTanhSinhTensorQuadrature/

**Contents:**
- PetscDTTanhSinhTensorQuadrature#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

create tanh-sinh quadrature for a tensor product cell

dim - The cell dimension

level - The number of points in one dimension, \(2^l\)

a - left end of interval (often-1)

b - right end of interval (often +1)

q - A PetscQuadrature object

PetscDTGaussTensorQuadrature(), PetscQuadrature

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTTanhSinhTensorQuadrature(PetscInt dim, PetscInt level, PetscReal a, PetscReal b, PetscQuadrature *q)
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
PetscDTGaussTensorQuadrature()
```

Example 4 (unknown):
```unknown
PetscQuadrature
```

---

## PetscDTTensorQuadratureCreate#

**URL:** https://petsc.org/release/manualpages/DT/PetscDTTensorQuadratureCreate/

**Contents:**
- PetscDTTensorQuadratureCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

create the tensor product quadrature from two lower-dimensional quadratures

q1 - The first quadrature

q2 - The second quadrature

q - A PetscQuadrature object

PetscQuadrature, PetscDTGaussTensorQuadrature()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscDTTensorQuadratureCreate(PetscQuadrature q1, PetscQuadrature q2, PetscQuadrature *q)
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscDTGaussTensorQuadrature()
```

---

## PetscDT: Discretization Technology in PETSc#

**URL:** https://petsc.org/release/manual/dt/

**Contents:**
- PetscDT: Discretization Technology in PETSc#
- Quadrature#
- Probability Distributions#

This chapter discusses the low-level infrastructure which supports higher-level discretizations in PETSc, which includes things such as quadrature and probability distributions.

A probability distribution function (PDF) returns the probability density at a given location \(P(x)\), so that the probability for an event at location in \([x, x+dx]\) is \(P(x) dx\). This means that we must have the normalization condition,

where :math:Omega is the domain for \(x\). This requires that the PDF must have units which are the inverse of the volume form \(dx\), meaning that it is homogeneous of order \(d\) under scaling

We can check this using the normalization condition,

The cumulative distribution function (CDF) is the incomplete integral of the PDF,

where \(x_-\) is the lower limit of our domain. We can work out the effect of scaling on the CDF using this definition,

so the CDF itself is scale invariant and unitless.

We do not add a scale argument to the PDF in PETSc, since all variables are assuming to be dimensionless. This means that inputs to the PDF and CDF should be scaled by the appropriate factor for the units of \(x\), and the output can be rescaled if it is used outside the library.

PetscFE: Finite Element Infrastructure in PETSc

---

## PetscDualSpaceApplyAllDefault#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceApplyAllDefault/

**Contents:**
- PetscDualSpaceApplyAllDefault#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Apply all functionals from the dual space basis to the result of an evaluation at the points returned by PetscDualSpaceGetAllData()

sp - The PetscDualSpace object

pointEval - Evaluation at the points returned by PetscDualSpaceGetAllData()

spValue - The values of all dual space functionals

PetscDualSpace, PetscDualSpaceCreate()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpaceGetAllData()
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceApplyAllDefault(PetscDualSpace sp, const PetscScalar *pointEval, PetscScalar *spValue)
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpaceGetAllData()
```

---

## PetscDualSpaceApplyAll#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceApplyAll/

**Contents:**
- PetscDualSpaceApplyAll#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Apply all functionals from the dual space basis to the result of an evaluation at the points returned by PetscDualSpaceGetAllData()

sp - The PetscDualSpace object

pointEval - Evaluation at the points returned by PetscDualSpaceGetAllData()

spValue - The values of all dual space functionals

PetscDualSpace, PetscDualSpaceCreate()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpaceGetAllData()
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceApplyAll(PetscDualSpace sp, const PetscScalar *pointEval, PetscScalar *spValue)
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpaceGetAllData()
```

---

## PetscDualSpaceApplyDefault#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceApplyDefault/

**Contents:**
- PetscDualSpaceApplyDefault#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Calling sequence#
- Note#
- See Also#
- Level#
- Location#

Apply a functional from the dual space basis to an input function by assuming a point evaluation functional.

sp - The PetscDualSpace object

f - The basis functional index

cgeom - A context with geometric information for this cell, we use v0 (the initial vertex) and J (the Jacobian)

Nc - The number of components for the function

func - The input function

ctx - A context for the function

value - The output value

The idea is to evaluate the functional as an integral \( n(f) = \int dx n(x) . f(x) \) where both n and f have Nc components.

PetscDualSpace, PetscDualSpaceCreate()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceApplyDefault(PetscDualSpace sp, PetscInt f, PetscReal time, PetscFEGeom *cgeom, PetscInt Nc, PetscErrorCode (*func)(PetscInt, PetscReal, const PetscReal[], PetscInt, PetscScalar *, void *), PetscCtx ctx, PetscScalar *value)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscErrorCode func(PetscInt dim, PetscReal time, const PetscReal x[],PetscInt numComponents, PetscScalar values[], PetscCtx ctx)
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceApplyFVM#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceApplyFVM/

**Contents:**
- PetscDualSpaceApplyFVM#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Calling sequence#
- Note#
- See Also#
- Level#
- Location#

Apply a functional from the dual space basis to an input function by assuming a point evaluation functional at the cell centroid.

sp - The PetscDualSpace object

f - The basis functional index

cgeom - A context with geometric information for this cell, we currently just use the centroid

Nc - The number of components for the function

func - The input function

ctx - A context for the function

value - The output value (scalar)

The idea is to evaluate the functional as an integral \( n(f) = \int dx n(x) . f(x)\) where both n and f have Nc components.

PetscDualSpace, PetscDualSpaceCreate()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceApplyFVM(PetscDualSpace sp, PetscInt f, PetscReal time, PetscFVCellGeom *cgeom, PetscInt Nc, PetscErrorCode (*func)(PetscInt, PetscReal, const PetscReal[], PetscInt, PetscScalar *, void *), PetscCtx ctx, PetscScalar *value)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscErrorCode func(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt numComponents, PetscScalar values[], PetscCtx ctx)
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceApplyInteriorDefault#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceApplyInteriorDefault/

**Contents:**
- PetscDualSpaceApplyInteriorDefault#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Apply interior functionals from the dual space basis to the result of an evaluation at the points returned by PetscDualSpaceGetInteriorData()

sp - The PetscDualSpace object

pointEval - Evaluation at the points returned by PetscDualSpaceGetInteriorData()

spValue - The values of interior dual space functionals

PetscDualSpace, PetscDualSpaceCreate()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpaceGetInteriorData()
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceApplyInteriorDefault(PetscDualSpace sp, const PetscScalar *pointEval, PetscScalar *spValue)
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpaceGetInteriorData()
```

---

## PetscDualSpaceApplyInterior#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceApplyInterior/

**Contents:**
- PetscDualSpaceApplyInterior#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Apply interior functionals from the dual space basis to the result of an evaluation at the points returned by PetscDualSpaceGetInteriorData()

sp - The PetscDualSpace object

pointEval - Evaluation at the points returned by PetscDualSpaceGetInteriorData()

spValue - The values of interior dual space functionals

PetscDualSpace, PetscDualSpaceCreate()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpaceGetInteriorData()
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceApplyInterior(PetscDualSpace sp, const PetscScalar *pointEval, PetscScalar *spValue)
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpaceGetInteriorData()
```

---

## PetscDualSpaceApply#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceApply/

**Contents:**
- PetscDualSpaceApply#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Calling sequence#
- See Also#
- Level#
- Location#

Apply a functional from the dual space basis to an input function

sp - The PetscDualSpace object

f - The basis functional index

cgeom - A context with geometric information for this cell, we use v0 (the initial vertex) and J (the Jacobian) (or evaluated at the coordinates of the functional)

numComp - The number of components for the function

func - The input function

ctx - A context for the function

value - numComp output values

PetscDualSpace, PetscDualSpaceCreate()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceApply(PetscDualSpace sp, PetscInt f, PetscReal time, PetscFEGeom *cgeom, PetscInt numComp, PetscErrorCode (*func)(PetscInt, PetscReal, const PetscReal[], PetscInt, PetscScalar *, void *), PetscCtx ctx, PetscScalar *value)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscErrorCode func(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt numComponents, PetscScalar values[], PetscCtx ctx)
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PETSCDUALSPACEBDM#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PETSCDUALSPACEBDM/

**Contents:**
- PETSCDUALSPACEBDM#
- Note#
- See Also#
- Level#
- Location#

“bdm” - A PetscDualSpace object that encapsulates a dual space for Brezzi-Douglas-Marini elements

This type is a constructor alias of PETSCDUALSPACELAGRANGE. During PetscDualSpaceSetUp(), the correct value of PetscDualSpaceSetFormDegree() is set for H-div conforming spaces. The type of the dual space is then changed to to PETSCDUALSPACELAGRANGE.

PetscDualSpaceType, PetscDualSpaceCreate(), PetscDualSpaceSetType(), PETSCDUALSPACELAGRANGE, PetscDualSpaceSetFormDegree()

include/petscdualspace.h

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpace
```

Example 2 (unknown):
```unknown
PETSCDUALSPACELAGRANGE
```

Example 3 (unknown):
```unknown
PetscDualSpaceSetUp()
```

Example 4 (unknown):
```unknown
PetscDualSpaceSetFormDegree()
```

---

## PetscDualSpaceCreateAllDataDefault#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceCreateAllDataDefault/

**Contents:**
- PetscDualSpaceCreateAllDataDefault#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Create all evaluation nodes and the node-to-dof matrix by examining functionals

allNodes - A PetscQuadrature object containing all evaluation nodes

allMat - A Mat for the node-to-dof transformation

PetscDualSpace, PetscDualSpaceCreate(), Mat, PetscQuadrature

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceCreateAllDataDefault(PetscDualSpace sp, PetscQuadrature *allNodes, Mat *allMat)
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpaceCreate()
```

---

## PetscDualSpaceCreateInteriorDataDefault#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceCreateInteriorDataDefault/

**Contents:**
- PetscDualSpaceCreateInteriorDataDefault#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Create quadrature points by examining interior functionals and create the matrix mapping quadrature point values to interior dual space values

intNodes - A PetscQuadrature object containing all evaluation points needed to evaluate interior degrees of freedom

intMat - A matrix that computes dual space values from point values: size [spdim0 x (npoints * nc)], where spdim0 is the size of the constrained layout (PetscSectionGetConstrainStorageSize()) of the dual space section, npoints is the number of points in allNodes and nc is PetscDualSpaceGetNumComponents().

PetscDualSpace, PetscQuadrature, Mat, PetscDualSpaceCreate(), PetscDualSpaceGetInteriorData()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceCreateInteriorDataDefault(PetscDualSpace sp, PetscQuadrature *intNodes, Mat *intMat)
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
PetscSectionGetConstrainStorageSize()
```

Example 4 (unknown):
```unknown
PetscDualSpaceGetNumComponents()
```

---

## PetscDualSpaceCreateSum#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceCreateSum/

**Contents:**
- PetscDualSpaceCreateSum#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Create a finite element dual basis that is the sum of other dual bases

numSubspaces - the number of spaces that will be added together

subspaces - an array of length numSubspaces of spaces

concatenate - if PETSC_FALSE, the sum-space has the same components as the individual dual spaces (PetscDualSpaceGetNumComponents()); if PETSC_TRUE, the individual components are concatenated to create a dual space with more components

sumSpace - a PetscDualSpace of type PETSCDUALSPACESUM

PetscDualSpace, PETSCDUALSPACESUM, PETSCSPACESUM

src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceCreateSum(PetscInt numSubspaces, const PetscDualSpace subspaces[], PetscBool concatenate, PetscDualSpace *sumSpace)
```

Example 2 (unknown):
```unknown
numSubspaces
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (unknown):
```unknown
PetscDualSpaceGetNumComponents()
```

---

## PetscDualSpaceCreate#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceCreate/

**Contents:**
- PetscDualSpaceCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Creates an empty PetscDualSpace object. The type can then be set with PetscDualSpaceSetType().

comm - The communicator for the PetscDualSpace object

sp - The PetscDualSpace object

PetscDualSpace, PetscDualSpaceSetType(), PETSCDUALSPACELAGRANGE

src/dm/dt/dualspace/interface/dualspace.c

src/dm/dt/dualspace/impls/lagrange/tutorials/ex1.c

PetscDualSpaceCreate_Lagrange() in src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c PetscDualSpaceCreate_Refined() in src/dm/dt/dualspace/impls/refined/dualspacerefined.c PetscDualSpaceCreate_Simple() in src/dm/dt/dualspace/impls/simple/dspacesimple.c PetscDualSpaceCreate_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpace
```

Example 2 (unknown):
```unknown
PetscDualSpaceSetType()
```

Example 3 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceCreate(MPI_Comm comm, PetscDualSpace *sp)
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceDestroy#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceDestroy/

**Contents:**
- PetscDualSpaceDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Destroys a PetscDualSpace object

sp - the PetscDualSpace object to destroy

PetscDualSpace, PetscDualSpaceView(), PetscDualSpace(), PetscDualSpaceCreate()

src/dm/dt/dualspace/interface/dualspace.c

src/dm/dt/dualspace/impls/lagrange/tutorials/ex1.c

PetscDualSpaceDestroy_Lagrange() in src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c PetscDualSpaceDestroy_Refined() in src/dm/dt/dualspace/impls/refined/dualspacerefined.c PetscDualSpaceDestroy_Simple() in src/dm/dt/dualspace/impls/simple/dspacesimple.c PetscDualSpaceDestroy_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpace
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceDestroy(PetscDualSpace *sp)
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceDuplicate#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceDuplicate/

**Contents:**
- PetscDualSpaceDuplicate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Creates a duplicate PetscDualSpace object that is not setup.

sp - The original PetscDualSpace

spNew - The duplicate PetscDualSpace

PetscDualSpace, PetscDualSpaceCreate(), PetscDualSpaceSetType()

src/dm/dt/dualspace/interface/dualspace.c

PetscDualSpaceDuplicate_Lagrange() in src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c PetscDualSpaceDuplicate_Simple() in src/dm/dt/dualspace/impls/simple/dspacesimple.c PetscDualSpaceDuplicate_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpace
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceDuplicate(PetscDualSpace sp, PetscDualSpace *spNew)
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceEqual#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceEqual/

**Contents:**
- PetscDualSpaceEqual#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Determine if two dual spaces are equivalent

A - A PetscDualSpace object

B - Another PetscDualSpace object

equal - PETSC_TRUE if the dual spaces are equivalent

PetscDualSpace, PetscDualSpaceCreate()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceEqual(PetscDualSpace A, PetscDualSpace B, PetscBool *equal)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceGetAllData#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetAllData/

**Contents:**
- PetscDualSpaceGetAllData#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Get all quadrature nodes from this space, and the matrix that sends quadrature node values to degree-of-freedom values

allNodes - A PetscQuadrature object containing all evaluation nodes, pass NULL if not needed

allMat - A Mat for the node-to-dof transformation, pass NULL if not needed

PetscQuadrature, PetscDualSpace, PetscDualSpaceCreate(), Mat

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceGetAllData(PetscDualSpace sp, PeOp PetscQuadrature *allNodes, PeOp Mat *allMat)
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceGetDeRahm#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetDeRahm/

**Contents:**
- PetscDualSpaceGetDeRahm#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Get the k-simplex associated with the functionals in this dual space

dsp - The PetscDualSpace

k - The simplex dimension

Currently supported values are

PetscDualSpace, PetscDualSpacePullback(), PetscDualSpacePushforward(), PetscDualSpaceTransform(), PetscDualSpaceTransformType

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceGetDeRahm(PetscDualSpace dsp, PetscInt *k)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (csharp):
```csharp
0: These are H_1 methods that only transform coordinates
  1: These are Hcurl methods that transform functions using the covariant Piola transform (COVARIANT_PIOLA_TRANSFORM)
  2: These are the same as 1
  3: These are Hdiv methods that transform functions using the contravariant Piola transform (CONTRAVARIANT_PIOLA_TRANSFORM)
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceGetDimension#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetDimension/

**Contents:**
- PetscDualSpaceGetDimension#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the dimension of the dual space, i.e. the number of basis functionals

sp - The PetscDualSpace

PetscDualSpace, PetscDualSpaceGetFunctional(), PetscDualSpaceCreate()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceGetDimension(PetscDualSpace sp, PetscInt *dim)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpaceGetFunctional()
```

---

## PetscDualSpaceGetDM#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetDM/

**Contents:**
- PetscDualSpaceGetDM#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the DM representing the reference cell of a PetscDualSpace

sp - The PetscDualSpace

dm - The reference cell, that is a DM that consists of a single cell

PetscDualSpace, PetscDualSpaceSetDM(), PetscDualSpaceCreate()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpace
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceGetDM(PetscDualSpace sp, DM *dm)
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceGetFormDegree#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetFormDegree/

**Contents:**
- PetscDualSpaceGetFormDegree#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the form degree k for the k-form the describes the pushforwards/pullbacks of this dual space’s functionals.

dsp - The PetscDualSpace

k - The signed degree k of the k. If k >= 0, this means that the degrees of freedom are k-forms, and are stored in lexicographic order according to the basis of k-forms constructed from the wedge product of 1-forms. So for example, the 1-form basis in 3-D is (dx, dy, dz), and the 2-form basis in 3-D is (dx wedge dy, dx wedge dz, dy wedge dz). If k < 0, this means that the degrees transform as k-forms, but are stored as (N-k) forms according to the Hodge star map. So for example if k = -2 and N = 3, this means that the degrees of freedom transform as 2-forms but are stored as 1-forms.

PetscDualSpace, PetscDTAltV, PetscDualSpacePullback(), PetscDualSpacePushforward(), PetscDualSpaceTransform(), PetscDualSpaceTransformType

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceGetFormDegree(PetscDualSpace dsp, PetscInt *k)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDTAltV
```

---

## PetscDualSpaceGetFunctional#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetFunctional/

**Contents:**
- PetscDualSpaceGetFunctional#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the i-th basis functional in the dual space

sp - The PetscDualSpace

functional - The basis functional

PetscDualSpace, PetscQuadrature, PetscDualSpaceGetDimension(), PetscDualSpaceCreate()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceGetFunctional(PetscDualSpace sp, PetscInt i, PetscQuadrature *functional)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscQuadrature
```

---

## PetscDualSpaceGetHeightSubspace#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetHeightSubspace/

**Contents:**
- PetscDualSpaceGetHeightSubspace#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Get the subset of the dual space basis that is supported on a mesh point of a given height. This assumes that the reference cell is symmetric over points of this height.

sp - the PetscDualSpace object

height - the height of the mesh point for which the subspace is desired

subsp - the subspace. Note that the functionals in the subspace are with respect to the intrinsic geometry of the point, which will be of lesser dimension if height > 0.

If the dual space is not defined on mesh points of the given height (e.g. if the space is discontinuous and pointwise values are not defined on the element boundaries), or if the implementation of PetscDualSpace does not support extracting subspaces, then NULL is returned.

This does not increment the reference count on the returned dual space, and the user should not destroy it.

PetscDualSpace, PetscSpaceGetHeightSubspace(), PetscDualSpaceGetPointSubspace()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceGetHeightSubspace(PetscDualSpace sp, PetscInt height, PetscDualSpace *subsp)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceGetInteriorData#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetInteriorData/

**Contents:**
- PetscDualSpaceGetInteriorData#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Get all quadrature points necessary to compute the interior degrees of freedom from this space, as well as the matrix that computes the degrees of freedom from the quadrature values.

intNodes - A PetscQuadrature object containing all evaluation points needed to evaluate interior degrees of freedom, pass NULL if not needed

intMat - A matrix that computes dual space values from point values: size [spdim0 x (npoints * nc)], where spdim0 is the size of the constrained layout (PetscSectionGetConstrainStorageSize()) of the dual space section, npoints is the number of points in intNodes and nc is PetscDualSpaceGetNumComponents(). Pass NULL if not needed

Degrees of freedom are interior degrees of freedom if they belong (by PetscDualSpaceGetSection()) to interior points in the references, complementary boundary degrees of freedom are marked as constrained in the section returned by PetscDualSpaceGetSection()).

PetscDualSpace, PetscQuadrature, Mat, PetscDualSpaceCreate(), PetscDualSpaceGetDimension(), PetscDualSpaceGetNumComponents(), PetscQuadratureGetData()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceGetInteriorData(PetscDualSpace sp, PeOp PetscQuadrature *intNodes, PeOp Mat *intMat)
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
PetscSectionGetConstrainStorageSize()
```

Example 4 (unknown):
```unknown
PetscDualSpaceGetNumComponents()
```

---

## PetscDualSpaceGetInteriorDimension#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetInteriorDimension/

**Contents:**
- PetscDualSpaceGetInteriorDimension#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the interior dimension of the dual space, i.e. the number of basis functionals assigned to the interior of the reference domain

sp - The PetscDualSpace

intdim - The dimension

PetscDualSpace, PetscDualSpaceGetFunctional(), PetscDualSpaceCreate()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceGetInteriorDimension(PetscDualSpace sp, PetscInt *intdim)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpaceGetFunctional()
```

---

## PetscDualSpaceGetInteriorSection#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetInteriorSection/

**Contents:**
- PetscDualSpaceGetInteriorSection#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Create a PetscSection over the reference cell with the layout from this space for interior degrees of freedom

sp - The PetscDualSpace

section - The interior section

Most reference domains have one cell, in which case the only cell will have all of the interior degrees of freedom in the interior section. But for PETSCDUALSPACEREFINED there may be other mesh points in the interior, and this section describes their layout.

PetscDualSpace, PetscSection, PetscDualSpaceCreate(), DMPLEX

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceGetInteriorSection(PetscDualSpace sp, PetscSection *section)
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PETSCDUALSPACEREFINED
```

---

## PetscDualSpaceGetNumComponents#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetNumComponents/

**Contents:**
- PetscDualSpaceGetNumComponents#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Return the number of components for this space

sp - The PetscDualSpace

Nc - The number of components

A vector space, for example, will have d components, where d is the spatial dimension

PetscDualSpaceSetNumComponents(), PetscDualSpaceGetDimension(), PetscDualSpaceCreate(), PetscDualSpace

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceGetNumComponents(PetscDualSpace sp, PetscInt *Nc)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscDualSpaceSetNumComponents()
```

Example 4 (unknown):
```unknown
PetscDualSpaceGetDimension()
```

---

## PetscDualSpaceGetNumDof#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetNumDof/

**Contents:**
- PetscDualSpaceGetNumDof#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Get the number of degrees of freedom for each spatial (topological) dimension

sp - The PetscDualSpace

numDof - An array of length dim+1 which holds the number of dofs for each dimension

PetscDualSpace, PetscDualSpaceGetFunctional(), PetscDualSpaceCreate()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceGetNumDof(PetscDualSpace sp, const PetscInt *numDof[])
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpaceGetFunctional()
```

---

## PetscDualSpaceGetOrder#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetOrder/

**Contents:**
- PetscDualSpaceGetOrder#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Get the order of the dual space

sp - The PetscDualSpace

PetscDualSpace, PetscDualSpaceSetOrder(), PetscDualSpaceCreate()

src/dm/dt/dualspace/interface/dualspace.c

src/dm/impls/plex/tutorials/ex15.c src/dm/impls/plex/tutorials/ex16.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceGetOrder(PetscDualSpace sp, PetscInt *order)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpaceSetOrder()
```

---

## PetscDualSpaceGetPointSubspace#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetPointSubspace/

**Contents:**
- PetscDualSpaceGetPointSubspace#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Get the subset of the dual space basis that is supported on a particular mesh point.

sp - the PetscDualSpace object

point - the point (in the dual space’s DM) for which the subspace is desired

The functionals in the subspace are with respect to the intrinsic geometry of the point, which will be of lesser dimension if height > 0.

If the dual space is not defined on the mesh point (e.g. if the space is discontinuous and pointwise values are not defined on the element boundaries), or if the implementation of PetscDualSpace does not support extracting subspaces, then NULL is returned.

This does not increment the reference count on the returned dual space, and the user should not destroy it.

PetscDualSpace, PetscDualSpaceGetHeightSubspace()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceGetPointSubspace(PetscDualSpace sp, PetscInt point, PetscDualSpace *bdsp)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceGetSection#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetSection/

**Contents:**
- PetscDualSpaceGetSection#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Create a PetscSection over the reference cell with the layout from this space

sp - The PetscDualSpace

section - The section

PetscDualSpace, PetscSection, PetscDualSpaceCreate(), DMPLEX

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceGetSection(PetscDualSpace sp, PetscSection *section)
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceGetSymmetries#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetSymmetries/

**Contents:**
- PetscDualSpaceGetSymmetries#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Returns a description of the symmetries of this basis

sp - the PetscDualSpace object

perms - Permutations of the interior degrees of freedom, parameterized by the point orientation

flips - Sign reversal of the interior degrees of freedom, parameterized by the point orientation

The permutation and flip arrays are organized in the following way

src/dm/dt/dualspace/interface/dualspace.c

PetscDualSpaceGetSymmetries_Lagrange() in src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c PetscDualSpaceGetSymmetries_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceGetSymmetries(PetscDualSpace sp, const PetscInt ****perms, const PetscScalar ****flips)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
perms[p][ornt][dof # on point] = new local dof #
  flips[p][ornt][dof # on point] = reversal or not
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceGetType#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetType/

**Contents:**
- PetscDualSpaceGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the PetscDualSpaceType name (as a string) from the object.

sp - The PetscDualSpace

name - The PetscDualSpaceType name

PetscDualSpace, PetscDualSpaceType, PetscDualSpaceSetType(), PetscDualSpaceCreate()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpaceType
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceGetType(PetscDualSpace sp, PetscDualSpaceType *name)
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpaceType
```

---

## PetscDualSpaceGetUniform#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceGetUniform/

**Contents:**
- PetscDualSpaceGetUniform#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Whether this dual space is uniform

uniform - PETSC_TRUE if (a) the dual space is the same for each point in a stratum of the reference DMPLEX, and (b) every symmetry of each point in the reference DMPLEX is also a symmetry of the point’s dual space.

All of the usual spaces on simplex or tensor-product elements will be uniform, only reference cells with non-uniform strata (like trianguar-prisms) or anisotropic hp dual spaces will not be uniform.

PetscDualSpace, PetscDualSpaceGetPointSubspace(), PetscDualSpaceGetSymmetries()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceGetUniform(PetscDualSpace sp, PetscBool *uniform)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscDualSpaceGetPointSubspace()
```

Example 4 (unknown):
```unknown
PetscDualSpaceGetSymmetries()
```

---

## PetscDualSpaceLagrangeGetContinuity#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceLagrangeGetContinuity/

**Contents:**
- PetscDualSpaceLagrangeGetContinuity#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Retrieves the flag for element continuity

sp - the PetscDualSpace

continuous - flag for element continuity

PETSCDUALSPACELAGRANGE, PetscDualSpace, PetscDualSpaceLagrangeSetContinuity()

src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c

PetscDualSpaceLagrangeGetContinuity_Lagrange() in src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c PetscDualSpaceLagrangeGetContinuity_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceLagrangeGetContinuity(PetscDualSpace sp, PetscBool *continuous)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PETSCDUALSPACELAGRANGE
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceLagrangeGetMomentOrder#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceLagrangeGetMomentOrder/

**Contents:**
- PetscDualSpaceLagrangeGetMomentOrder#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get the order for moment integration

sp - The PetscDualSpace

order - Moment integration order

PETSCDUALSPACELAGRANGE, PetscDualSpace, PetscDualSpaceLagrangeSetMomentOrder()

src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c

PetscDualSpaceLagrangeGetMomentOrder_Lagrange() in src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c PetscDualSpaceLagrangeGetMomentOrder_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceLagrangeGetMomentOrder(PetscDualSpace sp, PetscInt *order)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PETSCDUALSPACELAGRANGE
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceLagrangeGetNodeType#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceLagrangeGetNodeType/

**Contents:**
- PetscDualSpaceLagrangeGetNodeType#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Get a description of how nodes are laid out for Lagrange polynomials in this dual space

sp - The PetscDualSpace

nodeType - The type of nodes

boundary - Whether the node type is one that includes endpoints (if nodeType is PETSCDTNODES_GAUSSJACOBI, nodes that include the boundary are Gauss-Lobatto-Jacobi nodes)

exponent - If nodeType is PETSCDTNODES_GAUSSJACOBI, indicates the exponent used for both ends of the 1D Jacobi weight function ‘0’ is Gauss-Legendre, ‘-0.5’ is Gauss-Chebyshev of the first type, ‘0.5’ is Gauss-Chebyshev of the second type

PETSCDUALSPACELAGRANGE, PetscDualSpace, PetscDTNodeType, PetscDualSpaceLagrangeSetNodeType()

src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c

PetscDualSpaceLagrangeGetNodeType_Lagrange() in src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c PetscDualSpaceLagrangeGetNodeType_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceLagrangeGetNodeType(PetscDualSpace sp, PeOp PetscDTNodeType *nodeType, PeOp PetscBool *boundary, PeOp PetscReal *exponent)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PETSCDTNODES_GAUSSJACOBI
```

Example 4 (unknown):
```unknown
PETSCDTNODES_GAUSSJACOBI
```

---

## PetscDualSpaceLagrangeGetTensor#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceLagrangeGetTensor/

**Contents:**
- PetscDualSpaceLagrangeGetTensor#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get the tensor nature of the dual space

sp - The PetscDualSpace

tensor - Whether the dual space has tensor layout (vs. simplicial)

PETSCDUALSPACELAGRANGE, PetscDualSpace, PetscDualSpaceLagrangeSetTensor(), PetscDualSpaceCreate()

src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c

PetscDualSpaceLagrangeGetTensor_Lagrange() in src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c PetscDualSpaceLagrangeGetTensor_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceLagrangeGetTensor(PetscDualSpace sp, PetscBool *tensor)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PETSCDUALSPACELAGRANGE
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceLagrangeGetTrimmed#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceLagrangeGetTrimmed/

**Contents:**
- PetscDualSpaceLagrangeGetTrimmed#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get the trimmed nature of the dual space

sp - The PetscDualSpace

trimmed - Whether the dual space represents to dual basis of a trimmed polynomial space (e.g. Raviart-Thomas and higher order / other form degree variants)

PETSCDUALSPACELAGRANGE, PetscDualSpace, PetscDualSpaceLagrangeSetTrimmed(), PetscDualSpaceCreate()

src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c

PetscDualSpaceLagrangeGetTrimmed_Lagrange() in src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c PetscDualSpaceLagrangeGetTrimmed_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceLagrangeGetTrimmed(PetscDualSpace sp, PetscBool *trimmed)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PETSCDUALSPACELAGRANGE
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceLagrangeGetUseMoments#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceLagrangeGetUseMoments/

**Contents:**
- PetscDualSpaceLagrangeGetUseMoments#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get the flag for using moment functionals

sp - The PetscDualSpace

useMoments - Moment flag

PETSCDUALSPACELAGRANGE, PetscDualSpace, PetscDualSpaceLagrangeSetUseMoments()

src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c

PetscDualSpaceLagrangeGetUseMoments_Lagrange() in src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c PetscDualSpaceLagrangeGetUseMoments_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceLagrangeGetUseMoments(PetscDualSpace sp, PetscBool *useMoments)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PETSCDUALSPACELAGRANGE
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceLagrangeSetContinuity#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceLagrangeSetContinuity/

**Contents:**
- PetscDualSpaceLagrangeSetContinuity#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

Indicate whether the element is continuous

sp - the PetscDualSpace

continuous - flag for element continuity

-petscdualspace_lagrange_continuity (true|false) - use a continuous element

PETSCDUALSPACELAGRANGE, PetscDualSpace, PetscDualSpaceLagrangeGetContinuity()

src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c

PetscDualSpaceLagrangeSetContinuity_Lagrange() in src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c PetscDualSpaceLagrangeSetContinuity_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceLagrangeSetContinuity(PetscDualSpace sp, PetscBool continuous)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PETSCDUALSPACELAGRANGE
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceLagrangeSetMomentOrder#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceLagrangeSetMomentOrder/

**Contents:**
- PetscDualSpaceLagrangeSetMomentOrder#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set the order for moment integration

sp - The PetscDualSpace

order - The order for moment integration

PETSCDUALSPACELAGRANGE, PetscDualSpace, PetscDualSpaceLagrangeGetMomentOrder()

src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c

PetscDualSpaceLagrangeSetMomentOrder_Lagrange() in src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c PetscDualSpaceLagrangeSetMomentOrder_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceLagrangeSetMomentOrder(PetscDualSpace sp, PetscInt order)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PETSCDUALSPACELAGRANGE
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceLagrangeSetNodeType#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceLagrangeSetNodeType/

**Contents:**
- PetscDualSpaceLagrangeSetNodeType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set a description of how nodes are laid out for Lagrange polynomials in this dual space

sp - The PetscDualSpace

nodeType - The type of nodes

boundary - Whether the node type is one that includes endpoints (if nodeType is PETSCDTNODES_GAUSSJACOBI, nodes that include the boundary are Gauss-Lobatto-Jacobi nodes)

exponent - If nodeType is PETSCDTNODES_GAUSSJACOBI, indicates the exponent used for both ends of the 1D Jacobi weight function ‘0’ is Gauss-Legendre, ‘-0.5’ is Gauss-Chebyshev of the first type, ‘0.5’ is Gauss-Chebyshev of the second type

PETSCDUALSPACELAGRANGE, PetscDualSpace, PetscDTNodeType, PetscDualSpaceLagrangeGetNodeType()

src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c

PetscDualSpaceLagrangeSetNodeType_Lagrange() in src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c PetscDualSpaceLagrangeSetNodeType_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceLagrangeSetNodeType(PetscDualSpace sp, PetscDTNodeType nodeType, PetscBool boundary, PetscReal exponent)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PETSCDTNODES_GAUSSJACOBI
```

Example 4 (unknown):
```unknown
PETSCDTNODES_GAUSSJACOBI
```

---

## PetscDualSpaceLagrangeSetTensor#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceLagrangeSetTensor/

**Contents:**
- PetscDualSpaceLagrangeSetTensor#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set the tensor nature of the dual space

sp - The PetscDualSpace

tensor - Whether the dual space has tensor layout (vs. simplicial)

PETSCDUALSPACELAGRANGE, PetscDualSpace, PetscDualSpaceLagrangeGetTensor(), PetscDualSpaceCreate()

src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c

PetscDualSpaceLagrangeSetTensor_Lagrange() in src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c PetscDualSpaceLagrangeSetTensor_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceLagrangeSetTensor(PetscDualSpace sp, PetscBool tensor)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PETSCDUALSPACELAGRANGE
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceLagrangeSetTrimmed#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceLagrangeSetTrimmed/

**Contents:**
- PetscDualSpaceLagrangeSetTrimmed#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set the trimmed nature of the dual space

sp - The PetscDualSpace

trimmed - Whether the dual space represents to dual basis of a trimmed polynomial space (e.g. Raviart-Thomas and higher order / other form degree variants)

PETSCDUALSPACELAGRANGE, PetscDualSpace, PetscDualSpaceLagrangeGetTrimmed(), PetscDualSpaceCreate()

src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c

PetscDualSpaceLagrangeSetTrimmed_Lagrange() in src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c PetscDualSpaceLagrangeSetTrimmed_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceLagrangeSetTrimmed(PetscDualSpace sp, PetscBool trimmed)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PETSCDUALSPACELAGRANGE
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceLagrangeSetUseMoments#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceLagrangeSetUseMoments/

**Contents:**
- PetscDualSpaceLagrangeSetUseMoments#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set the flag for moment functionals

sp - The PetscDualSpace

useMoments - The flag for moment functionals

PETSCDUALSPACELAGRANGE, PetscDualSpace, PetscDualSpaceLagrangeGetUseMoments()

src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c

PetscDualSpaceLagrangeSetUseMoments_Lagrange() in src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c PetscDualSpaceLagrangeSetUseMoments_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceLagrangeSetUseMoments(PetscDualSpace sp, PetscBool useMoments)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PETSCDUALSPACELAGRANGE
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PETSCDUALSPACELAGRANGE#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PETSCDUALSPACELAGRANGE/

**Contents:**
- PETSCDUALSPACELAGRANGE#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

“lagrange” - A PetscDualSpaceType that encapsulates a dual space of pointwise evaluation functionals

This PetscDualSpace seems to manage directly trimmed and untrimmed polynomials as well as tensor and non-tensor polynomials while for PetscSpace there seems to be different PetscSpaceType for them.

PetscDualSpace, PetscDualSpaceType, PetscDualSpaceCreate(), PetscDualSpaceSetType(), PetscDualSpaceLagrangeSetMomentOrder(), PetscDualSpaceLagrangeGetMomentOrder(), PetscDualSpaceLagrangeSetUseMoments(), PetscDualSpaceLagrangeGetUseMoments(), PetscDualSpaceLagrangeSetNodeType(), PetscDualSpaceLagrangeGetNodeType(), PetscDualSpaceLagrangeGetContinuity(), PetscDualSpaceLagrangeSetContinuity(), PetscDualSpaceLagrangeGetTensor(), PetscDualSpaceLagrangeSetTensor(), PetscDualSpaceLagrangeGetTrimmed(), PetscDualSpaceLagrangeSetTrimmed()

src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c

src/dm/dt/dualspace/impls/lagrange/tutorials/ex2.c src/dm/dt/dualspace/impls/lagrange/tutorials/ex1.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpaceType
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscSpaceType
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpacePullback#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpacePullback/

**Contents:**
- PetscDualSpacePullback#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Transform the given functional so that it operates on real space, rather than the reference element. Operationally, this means that we map the function evaluations depending on continuity requirements of our finite element method.

dsp - The PetscDualSpace

fegeom - The geometry for this cell

Nq - The number of function samples

Nc - The number of function components

pointEval - The function values

pointEval - The transformed function values

Functions transform in a complementary way (pushforward) to functionals, so that the scalar product is invariant. The type of transform is dependent on the associated k-simplex from the DeRahm complex.

This only handles transformations when the embedding dimension of the geometry in fegeom is the same as the reference dimension.

PetscDualSpace, PetscDualSpacePushforward(), PetscDualSpaceTransform(), PetscDualSpaceGetDeRahm()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpacePullback(PetscDualSpace dsp, PetscFEGeom *fegeom, PetscInt Nq, PetscInt Nc, PetscScalar pointEval[])
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpacePushforward()
```

---

## PetscDualSpacePushforwardGradient#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpacePushforwardGradient/

**Contents:**
- PetscDualSpacePushforwardGradient#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Transform the given function gradient so that it operates on real space, rather than the reference element. Operationally, this means that we map the function evaluations depending on continuity requirements of our finite element method.

dsp - The PetscDualSpace

fegeom - The geometry for this cell

Nq - The number of function gradient samples

Nc - The number of function components

pointEval - The function gradient values

pointEval - The transformed function gradient values

Functionals transform in a complementary way (pullback) to functions, so that the scalar product is invariant. The type of transform is dependent on the associated k-simplex from the DeRahm complex.

This only handles transformations when the embedding dimension of the geometry in fegeom is the same as the reference dimension.

PetscDualSpace, PetscDualSpacePushforward(), PetscDualSpacePullback(), PetscDualSpaceTransform(), PetscDualSpaceGetDeRahm()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpacePushforwardGradient(PetscDualSpace dsp, PetscFEGeom *fegeom, PetscInt Nq, PetscInt Nc, PetscScalar pointEval[])
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpacePushforward()
```

---

## PetscDualSpacePushforwardHessian#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpacePushforwardHessian/

**Contents:**
- PetscDualSpacePushforwardHessian#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Transform the given function Hessian so that it operates on real space, rather than the reference element. Operationally, this means that we map the function evaluations depending on continuity requirements of our finite element method.

dsp - The PetscDualSpace

fegeom - The geometry for this cell

Nq - The number of function Hessian samples

Nc - The number of function components

pointEval - The function gradient values

pointEval - The transformed function Hessian values

Functionals transform in a complementary way (pullback) to functions, so that the scalar product is invariant. The type of transform is dependent on the associated k-simplex from the DeRahm complex.

This only handles transformations when the embedding dimension of the geometry in fegeom is the same as the reference dimension.

PetscDualSpace, PetscDualSpacePushforward(), PetscDualSpacePullback(), PetscDualSpaceTransform(), PetscDualSpaceGetDeRahm()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpacePushforwardHessian(PetscDualSpace dsp, PetscFEGeom *fegeom, PetscInt Nq, PetscInt Nc, PetscScalar pointEval[])
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpacePushforward()
```

---

## PetscDualSpacePushforward#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpacePushforward/

**Contents:**
- PetscDualSpacePushforward#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Transform the given function so that it operates on real space, rather than the reference element. Operationally, this means that we map the function evaluations depending on continuity requirements of our finite element method.

dsp - The PetscDualSpace

fegeom - The geometry for this cell

Nq - The number of function samples

Nc - The number of function components

pointEval - The function values

pointEval - The transformed function values

Functionals transform in a complementary way (pullback) to functions, so that the scalar product is invariant. The type of transform is dependent on the associated k-simplex from the DeRahm complex.

This only handles transformations when the embedding dimension of the geometry in fegeom is the same as the reference dimension.

PetscDualSpace, PetscDualSpacePullback(), PetscDualSpaceTransform(), PetscDualSpaceGetDeRahm()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpacePushforward(PetscDualSpace dsp, PetscFEGeom *fegeom, PetscInt Nq, PetscInt Nc, PetscScalar pointEval[])
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpacePullback()
```

---

## PetscDualSpaceReferenceCell#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceReferenceCell/

**Contents:**
- PetscDualSpaceReferenceCell#
- Note#
- See Also#
- Level#
- Location#

The type of reference cell

This is used only for automatic creation of reference cells. A PetscDualSpace can accept an arbitrary DM for a reference cell.

PetscSpace, PetscDualSpaceCreate(), PetscDualSpaceType

include/petscdualspace.h

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpace
```

Example 2 (unknown):
```unknown
PetscDualSpaceCreate()
```

Example 3 (unknown):
```unknown
PetscDualSpaceType
```

---

## PetscDualSpaceRefinedSetCellSpaces#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceRefinedSetCellSpaces/

**Contents:**
- PetscDualSpaceRefinedSetCellSpaces#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set the dual spaces for the closures of each of the cells in the multicell DM of a PetscDualSpace

sp - a PetscDualSpace

cellSpaces - one PetscDualSpace for each of the cells. The reference count of each cell space will be incremented, so the user is still responsible for these spaces afterwards

PETSCDUALSPACEREFINED, PetscDualSpace, PetscFERefine()

src/dm/dt/dualspace/impls/refined/dualspacerefined.c

PetscDualSpaceRefinedSetCellSpaces_Refined() in src/dm/dt/dualspace/impls/refined/dualspacerefined.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpace
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceRefinedSetCellSpaces(PetscDualSpace sp, const PetscDualSpace cellSpaces[])
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PETSCDUALSPACEREFINED#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PETSCDUALSPACEREFINED/

**Contents:**
- PETSCDUALSPACEREFINED#
- See Also#
- Level#
- Location#

“refined” - A PetscDualSpaceType that defines the joint dual space of a group of cells, usually refined from one larger cell

PetscDualSpace, PetscDualSpaceType, PetscDualSpaceRefinedSetCellSpaces, PetscDualSpaceCreate(), PetscDualSpaceSetType()

src/dm/dt/dualspace/impls/refined/dualspacerefined.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpaceType
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscDualSpaceType
```

Example 4 (unknown):
```unknown
PetscDualSpaceRefinedSetCellSpaces
```

---

## PetscDualSpaceRegister#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceRegister/

**Contents:**
- PetscDualSpaceRegister#
- Synopsis#
- Input Parameters#
- Example Usage#
- Note#
- See Also#
- Level#
- Location#

Adds a new PetscDualSpaceType

Not Collective, No Fortran Support

sname - The name of a new user-defined creation routine

function - The creation routine

Then, your PetscDualSpace type can be chosen with the procedural interface via

or at runtime via the option

PetscDualSpaceRegister() may be called multiple times to add several user-defined PetscDualSpace

PetscDualSpace, PetscDualSpaceType, PetscDualSpaceRegisterAll(), PetscDualSpaceRegisterDestroy()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpaceType
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceRegister(const char sname[], PetscErrorCode (*function)(PetscDualSpace))
```

Example 3 (unknown):
```unknown
PetscDualSpaceRegister("my_space", MyPetscDualSpaceCreate);
```

Example 4 (unknown):
```unknown
PetscDualSpaceCreate(MPI_Comm, PetscDualSpace *);
    PetscDualSpaceSetType(PetscDualSpace, "my_dual_space");
```

---

## PetscDualSpaceSetDM#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSetDM/

**Contents:**
- PetscDualSpaceSetDM#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Get the DM representing the reference cell

sp - The PetscDualSpace

dm - The reference cell

PetscDualSpace, DM, PetscDualSpaceGetDM(), PetscDualSpaceCreate()

src/dm/dt/dualspace/interface/dualspace.c

src/dm/dt/dualspace/impls/lagrange/tutorials/ex1.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceSetDM(PetscDualSpace sp, DM dm)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscDualSpaceGetDM()
```

Example 4 (unknown):
```unknown
PetscDualSpaceCreate()
```

---

## PetscDualSpaceSetFormDegree#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSetFormDegree/

**Contents:**
- PetscDualSpaceSetFormDegree#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the form degree k for the k-form the describes the pushforwards/pullbacks of this dual space’s functionals.

dsp - The PetscDualSpace

k - The signed degree k of the k. If k >= 0, this means that the degrees of freedom are k-forms, and are stored in lexicographic order according to the basis of k-forms constructed from the wedge product of 1-forms. So for example, the 1-form basis in 3-D is (dx, dy, dz), and the 2-form basis in 3-D is (dx wedge dy, dx wedge dz, dy wedge dz). If k < 0, this means that the degrees transform as k-forms, but are stored as (N-k) forms according to the Hodge star map. So for example if k = -2 and N = 3, this means that the degrees of freedom transform as 2-forms but are stored as 1-forms.

PetscDualSpace, PetscDTAltV, PetscDualSpacePullback(), PetscDualSpacePushforward(), PetscDualSpaceTransform(), PetscDualSpaceTransformType

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceSetFormDegree(PetscDualSpace dsp, PetscInt k)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDTAltV
```

---

## PetscDualSpaceSetFromOptions#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSetFromOptions/

**Contents:**
- PetscDualSpaceSetFromOptions#
- Synopsis#
- Input Parameter#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

sets parameters in a PetscDualSpace from the options database

sp - the PetscDualSpace object to set options for

-petscdualspace_order order - the approximation order of the space

-petscdualspace_form_degree deg - the form degree, say 0 for point evaluations, or 2 for area integrals

-petscdualspace_components c - the number of components, say d for a vector field

-petscdualspace_refcell celltype - Reference cell type name

-petscdualspace_lagrange_continuity (true|false) - Flag for continuous element

-petscdualspace_lagrange_tensor (true|false) - Flag for tensor dual space

-petscdualspace_lagrange_trimmed (true|false) - Flag for trimmed dual space

-petscdualspace_lagrange_node_type nodetype - Lagrange node location type

-petscdualspace_lagrange_node_endpoints (true|false) - Flag for nodes that include endpoints

-petscdualspace_lagrange_node_exponent exponent - Gauss-Jacobi weight function exponent

-petscdualspace_lagrange_use_moments (true|false) - Use moments (where appropriate) for functionals

-petscdualspace_lagrange_moment_order order - Quadrature order for moment functionals

PetscDualSpaceView(), PetscDualSpace, PetscObjectSetFromOptions()

src/dm/dt/dualspace/interface/dualspace.c

src/dm/dt/dualspace/impls/lagrange/tutorials/ex1.c

PetscDualSpaceSetFromOptions_Lagrange() in src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpace
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceSetFromOptions(PetscDualSpace sp)
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpaceView()
```

---

## PetscDualSpaceSetNumComponents#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSetNumComponents/

**Contents:**
- PetscDualSpaceSetNumComponents#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the number of components for this space

sp - The PetscDualSpace

Nc - The number of components

PetscDualSpaceGetNumComponents(), PetscDualSpaceCreate(), PetscDualSpace

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceSetNumComponents(PetscDualSpace sp, PetscInt Nc)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscDualSpaceGetNumComponents()
```

Example 4 (unknown):
```unknown
PetscDualSpaceCreate()
```

---

## PetscDualSpaceSetOrder#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSetOrder/

**Contents:**
- PetscDualSpaceSetOrder#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the order of the dual space

sp - The PetscDualSpace

PetscDualSpace, PetscDualSpaceGetOrder(), PetscDualSpaceCreate()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceSetOrder(PetscDualSpace sp, PetscInt order)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpaceGetOrder()
```

---

## PetscDualSpaceSetType#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSetType/

**Contents:**
- PetscDualSpaceSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

Builds a particular PetscDualSpace based on its PetscDualSpaceType

sp - The PetscDualSpace object

name - The kind of space

-petscdualspace_type type - Sets the PetscDualSpace type; see PetscDualSpaceType for the choices

PetscDualSpace, PetscDualSpaceType, PetscDualSpaceGetType(), PetscDualSpaceCreate()

src/dm/dt/dualspace/interface/dualspace.c

src/dm/dt/dualspace/impls/lagrange/tutorials/ex1.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpace
```

Example 2 (unknown):
```unknown
PetscDualSpaceType
```

Example 3 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceSetType(PetscDualSpace sp, PetscDualSpaceType name)
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceSetUp#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSetUp/

**Contents:**
- PetscDualSpaceSetUp#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Construct a basis for a PetscDualSpace

sp - the PetscDualSpace object to setup

PetscDualSpaceView(), PetscDualSpaceDestroy(), PetscDualSpace

src/dm/dt/dualspace/interface/dualspace.c

src/dm/dt/dualspace/impls/lagrange/tutorials/ex1.c

PetscDualSpaceSetUp_Lagrange() in src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c PetscDualSpaceSetUp_Refined() in src/dm/dt/dualspace/impls/refined/dualspacerefined.c PetscDualSpaceSetUp_Simple() in src/dm/dt/dualspace/impls/simple/dspacesimple.c PetscDualSpaceSetUp_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpace
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceSetUp(PetscDualSpace sp)
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpaceView()
```

---

## PetscDualSpaceSimpleSetDimension#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSimpleSetDimension/

**Contents:**
- PetscDualSpaceSimpleSetDimension#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set the number of functionals in the dual space basis

sp - the PetscDualSpace

dim - the basis dimension

PETSCDUALSPACESIMPLE, PetscDualSpace, PetscDualSpaceSimpleSetFunctional()

src/dm/dt/dualspace/impls/simple/dspacesimple.c

PetscDualSpaceSimpleSetDimension_Simple() in src/dm/dt/dualspace/impls/simple/dspacesimple.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceSimpleSetDimension(PetscDualSpace sp, PetscInt dim)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PETSCDUALSPACESIMPLE
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceSimpleSetFunctional#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSimpleSetFunctional/

**Contents:**
- PetscDualSpaceSimpleSetFunctional#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Set the given basis functional for this dual space

sp - the PetscDualSpace

func - the basis index

q - the basis functional

The quadrature will be reweighted so that it has unit volume.

PETSCDUALSPACESIMPLE, PetscDualSpace, PetscDualSpaceSimpleSetDimension()

src/dm/dt/dualspace/impls/simple/dspacesimple.c

PetscDualSpaceSimpleSetFunctional_Simple() in src/dm/dt/dualspace/impls/simple/dspacesimple.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceSimpleSetFunctional(PetscDualSpace sp, PetscInt func, PetscQuadrature q)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PETSCDUALSPACESIMPLE
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PETSCDUALSPACESIMPLE#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PETSCDUALSPACESIMPLE/

**Contents:**
- PETSCDUALSPACESIMPLE#
- Developer Note#
- See Also#
- Level#
- Location#

“simple” - A PetscDualSpaceType that encapsulates a dual space of functionals provided with PetscDualSpaceSimpleSetFunctional()

It is not clear this has a good name

PetscDualSpace, PetscDualSpaceSimpleSetFunctional(), PetscDualSpaceType, PetscDualSpaceCreate(), PetscDualSpaceSetType()

src/dm/dt/dualspace/impls/simple/dspacesimple.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpaceType
```

Example 2 (unknown):
```unknown
PetscDualSpaceSimpleSetFunctional()
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpaceSimpleSetFunctional()
```

---

## PetscDualSpaceSumGetConcatenate#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSumGetConcatenate/

**Contents:**
- PetscDualSpaceSumGetConcatenate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Get the concatenate flag for this space.

sp - the dual space object

concatenate - flag indicating whether subspaces are concatenated.

A concatenated sum space will have the number of components equal to the sum of the number of components of all subspaces. A non-concatenated, or direct sum space will have the same number of components as its subspaces.

PETSCDUALSPACESUM, PetscDualSpace, PetscDualSpaceSumSetConcatenate()

src/dm/dt/dualspace/impls/sum/dualspacesum.c

PetscDualSpaceSumGetConcatenate_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceSumGetConcatenate(PetscDualSpace sp, PetscBool *concatenate)
```

Example 2 (unknown):
```unknown
PETSCDUALSPACESUM
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpaceSumSetConcatenate()
```

---

## PetscDualSpaceSumGetInterleave#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSumGetInterleave/

**Contents:**
- PetscDualSpaceSumGetInterleave#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Get whether the basis functions and components of a uniform sum are interleaved

sp - a PetscDualSpace of type PETSCDUALSPACESUM

interleave_basis - if PETSC_TRUE, the basis vectors of the subspaces are interleaved

interleave_components - if PETSC_TRUE and the space concatenates components (PetscDualSpaceSumGetConcatenate()), interleave the concatenated components

PetscDualSpace, PETSCDUALSPACESUM, PETSCFEVECTOR, PetscDualSpaceSumSetInterleave()

src/dm/dt/dualspace/impls/sum/dualspacesum.c

PetscDualSpaceSumGetInterleave_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceSumGetInterleave(PetscDualSpace sp, PeOp PetscBool *interleave_basis, PeOp PetscBool *interleave_components)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PETSCDUALSPACESUM
```

Example 4 (unknown):
```unknown
PetscDualSpaceSumGetConcatenate()
```

---

## PetscDualSpaceSumGetNumSubspaces#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSumGetNumSubspaces/

**Contents:**
- PetscDualSpaceSumGetNumSubspaces#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Get the number of spaces in the sum space

sp - the dual space object

numSumSpaces - the number of spaces

The name NumSubspaces is slightly misleading because it is actually getting the number of defining spaces of the sum, not a number of Subspaces of it

PETSCDUALSPACESUM, PetscDualSpace, PetscDualSpaceSumSetNumSubspaces()

src/dm/dt/dualspace/impls/sum/dualspacesum.c

PetscDualSpaceSumGetNumSubspaces_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceSumGetNumSubspaces(PetscDualSpace sp, PetscInt *numSumSpaces)
```

Example 2 (unknown):
```unknown
PETSCDUALSPACESUM
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpaceSumSetNumSubspaces()
```

---

## PetscDualSpaceSumGetSubspace#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSumGetSubspace/

**Contents:**
- PetscDualSpaceSumGetSubspace#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Get a space in the sum space

sp - the dual space object

subsp - the PetscDualSpace

The name GetSubspace is slightly misleading because it is actually getting one of the defining spaces of the sum, not a Subspace of it

PETSCDUALSPACESUM, PetscDualSpace, PetscDualSpaceSumSetSubspace()

src/dm/dt/dualspace/impls/sum/dualspacesum.c

PetscDualSpaceSumGetSubspace_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceSumGetSubspace(PetscDualSpace sp, PetscInt s, PetscDualSpace *subsp)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PETSCDUALSPACESUM
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceSumSetConcatenate#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSumSetConcatenate/

**Contents:**
- PetscDualSpaceSumSetConcatenate#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Sets the concatenate flag for this space.

sp - the dual space object

concatenate - are subspaces concatenated components (true) or direct summands (false)

A concatenated sum space will have the number of components equal to the sum of the number of components of all subspaces. A non-concatenated, or direct sum space will have the same number of components as its subspaces .

PETSCDUALSPACESUM, PetscDualSpace, PetscDualSpaceSumGetConcatenate()

src/dm/dt/dualspace/impls/sum/dualspacesum.c

PetscDualSpaceSumSetConcatenate_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceSumSetConcatenate(PetscDualSpace sp, PetscBool concatenate)
```

Example 2 (unknown):
```unknown
PETSCDUALSPACESUM
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpaceSumGetConcatenate()
```

---

## PetscDualSpaceSumSetInterleave#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSumSetInterleave/

**Contents:**
- PetscDualSpaceSumSetInterleave#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set whether the basis functions and components of a uniform sum are interleaved

sp - a PetscDualSpace of type PETSCDUALSPACESUM

interleave_basis - if PETSC_TRUE, the basis vectors of the subspaces are interleaved

interleave_components - if PETSC_TRUE and the space concatenates components (PetscDualSpaceSumGetConcatenate()), interleave the concatenated components

PetscDualSpace, PETSCDUALSPACESUM, PETSCFEVECTOR, PetscDualSpaceSumGetInterleave()

src/dm/dt/dualspace/impls/sum/dualspacesum.c

PetscDualSpaceSumSetInterleave_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceSumSetInterleave(PetscDualSpace sp, PetscBool interleave_basis, PetscBool interleave_components)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PETSCDUALSPACESUM
```

Example 4 (unknown):
```unknown
PetscDualSpaceSumGetConcatenate()
```

---

## PetscDualSpaceSumSetNumSubspaces#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSumSetNumSubspaces/

**Contents:**
- PetscDualSpaceSumSetNumSubspaces#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Set the number of spaces in the sum space

sp - the dual space object

numSumSpaces - the number of spaces

The name NumSubspaces is slightly misleading because it is actually setting the number of defining spaces of the sum, not a number of Subspaces of it

PETSCDUALSPACESUM, PetscDualSpace, PetscDualSpaceSumGetNumSubspaces()

src/dm/dt/dualspace/impls/sum/dualspacesum.c

PetscDualSpaceSumSetNumSubspaces_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceSumSetNumSubspaces(PetscDualSpace sp, PetscInt numSumSpaces)
```

Example 2 (unknown):
```unknown
PETSCDUALSPACESUM
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpaceSumGetNumSubspaces()
```

---

## PetscDualSpaceSumSetSubspace#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceSumSetSubspace/

**Contents:**
- PetscDualSpaceSumSetSubspace#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Set a space in the sum space

sp - the dual space object

subsp - the number of spaces

The name SetSubspace is slightly misleading because it is actually setting one of the defining spaces of the sum, not a Subspace of it

PETSCDUALSPACESUM, PetscDualSpace, PetscDualSpaceSumGetSubspace()

src/dm/dt/dualspace/impls/sum/dualspacesum.c

PetscDualSpaceSumSetSubspace_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceSumSetSubspace(PetscDualSpace sp, PetscInt s, PetscDualSpace subsp)
```

Example 2 (unknown):
```unknown
PETSCDUALSPACESUM
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpaceSumGetSubspace()
```

---

## PETSCDUALSPACESUM#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PETSCDUALSPACESUM/

**Contents:**
- PETSCDUALSPACESUM#
- Note#
- See Also#
- Level#
- Location#

“sum” - A PetscDualSpace object that encapsulates a sum of subspaces.

That sum can either be direct or a concatenation. For example if A and B are spaces each with 2 components, the direct sum of A and B will also have 2 components while the concatenated sum will have 4 components. In both cases A and B must be defined over the same reference element.

PetscDualSpace, PetscDualSpaceType, PetscDualSpaceCreate(), PetscDualSpaceSetType(), PetscDualSpaceSumGetNumSubspaces(), PetscDualSpaceSumSetNumSubspaces(), PetscDualSpaceSumGetConcatenate(), PetscDualSpaceSumSetConcatenate(), PetscDualSpaceSumSetInterleave(), PetscDualSpaceSumGetInterleave()

src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpace
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscDualSpaceType
```

Example 4 (unknown):
```unknown
PetscDualSpaceCreate()
```

---

## PetscDualSpaceTransformGradient#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceTransformGradient/

**Contents:**
- PetscDualSpaceTransformGradient#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Transform the function gradient values

dsp - The PetscDualSpace

trans - The type of transform

isInverse - Flag to invert the transform

fegeom - The cell geometry

Nv - The number of function gradient samples

Nc - The number of function components

vals - The function gradient values

vals - The transformed function gradient values

This only handles transformations when the embedding dimension of the geometry in fegeom is the same as the reference dimension.

PetscDualSpace, PetscDualSpaceTransform(), PetscDualSpacePullback(), PetscDualSpacePushforward(), PetscDualSpaceTransformType

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceTransformGradient(PetscDualSpace dsp, PetscDualSpaceTransformType trans, PetscBool isInverse, PetscFEGeom *fegeom, PetscInt Nv, PetscInt Nc, PetscScalar vals[])
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpaceTransform()
```

---

## PetscDualSpaceTransformHessian#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceTransformHessian/

**Contents:**
- PetscDualSpaceTransformHessian#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Transform the function Hessian values

dsp - The PetscDualSpace

trans - The type of transform

isInverse - Flag to invert the transform

fegeom - The cell geometry

Nv - The number of function Hessian samples

Nc - The number of function components

vals - The function gradient values

vals - The transformed function Hessian values

This only handles transformations when the embedding dimension of the geometry in fegeom is the same as the reference dimension.

PetscDualSpace, PetscDualSpaceTransform(), PetscDualSpacePullback(), PetscDualSpacePushforward(), PetscDualSpaceTransformType

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceTransformHessian(PetscDualSpace dsp, PetscDualSpaceTransformType trans, PetscBool isInverse, PetscFEGeom *fegeom, PetscInt Nv, PetscInt Nc, PetscScalar vals[])
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpaceTransform()
```

---

## PetscDualSpaceTransformType#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceTransformType/

**Contents:**
- PetscDualSpaceTransformType#
- Values#
- Note#
- References#
- See Also#
- Level#
- Location#

The type of function transform

IDENTITY_TRANSFORM - make no changes in the function

COVARIANT_PIOLA_TRANSFORM - Covariant Piola: \(\sigma^*(F) = J^{-T} F \circ \phi^{-1)\)

CONTRAVARIANT_PIOLA_TRANSFORM - Contravariant Piola: \(\sigma^*(F) = 1/|J| J F \circ \phi^{-1)\)

These transforms, and their inverses, are used to move functions and functionals between the reference element and real space. Suppose that we have a mapping \(\phi\) which maps the reference cell to real space, and its Jacobian \(J\). If we want to transform function \(F\) on the reference element, so that it acts on real space, we use the pushforward transform \(\sigma^*\). The pullback \(\sigma_*\) is the inverse transform. [RKL09]

Marie E Rognes, Robert C Kirby, and Anders Logg. Efficient assembly of H(div) and H(curl) conforming finite elements. SIAM Journal on Scientific Computing, 31(6):4130–4151, 2009.

PetscDualSpaceGetDeRahm()

include/petscdualspace.h

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
IDENTITY_TRANSFORM
```

Example 2 (unknown):
```unknown
COVARIANT_PIOLA_TRANSFORM
```

Example 3 (unknown):
```unknown
CONTRAVARIANT_PIOLA_TRANSFORM
```

Example 4 (unknown):
```unknown
PetscDualSpaceGetDeRahm()
```

---

## PetscDualSpaceTransform#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceTransform/

**Contents:**
- PetscDualSpaceTransform#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Transform the function values

dsp - The PetscDualSpace

trans - The type of transform

isInverse - Flag to invert the transform

fegeom - The cell geometry

Nv - The number of function samples

Nc - The number of function components

vals - The function values

vals - The transformed function values

This only handles transformations when the embedding dimension of the geometry in fegeom is the same as the reference dimension.

PetscDualSpace, PetscDualSpaceTransformGradient(), PetscDualSpaceTransformHessian(), PetscDualSpacePullback(), PetscDualSpacePushforward(), PetscDualSpaceTransformType

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceTransform(PetscDualSpace dsp, PetscDualSpaceTransformType trans, PetscBool isInverse, PetscFEGeom *fegeom, PetscInt Nv, PetscInt Nc, PetscScalar vals[])
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpaceTransformGradient()
```

---

## PetscDualSpaceType#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceType/

**Contents:**
- PetscDualSpaceType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

String with the name of a PETSc dual space

PETSCDUALSPACELAGRANGE - a dual space of pointwise evaluation functionals

PETSCDUALSPACESIMPLE - a dual space defined by functionals provided with PetscDualSpaceSimpleSetFunctional()

PETSCDUALSPACEREFINED - the joint dual space defined by a group of cells, usually refined from one larger cell

PETSCDUALSPACEBDM - a dual space for Brezzi-Douglas-Marini elements

PETSCDUALSPACESUM - a dual space that is a sum of other dual spaces

PetscDualSpaceSetType(), PetscDualSpace, PetscSpace

include/petscdualspace.h

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef const char *PetscDualSpaceType;
#define PETSCDUALSPACELAGRANGE "lagrange"
#define PETSCDUALSPACESIMPLE   "simple"
#define PETSCDUALSPACEREFINED  "refined"
#define PETSCDUALSPACEBDM      "bdm"
#define PETSCDUALSPACESUM      "sum"
```

Example 2 (unknown):
```unknown
PetscDualSpaceSimpleSetFunctional()
```

Example 3 (unknown):
```unknown
PetscDualSpaceSetType()
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscDualSpaceViewFromOptions#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceViewFromOptions/

**Contents:**
- PetscDualSpaceViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

View a PetscDualSpace based on values in the options database

A - the PetscDualSpace object

obj - Optional object, provides the options prefix

name - command line option name

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

PetscDualSpace, PetscDualSpaceView(), PetscObjectViewFromOptions(), PetscDualSpaceCreate()

src/dm/dt/dualspace/interface/dualspace.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpace
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceViewFromOptions(PetscDualSpace A, PeOp PetscObject obj, const char name[])
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscObjectViewFromOptions()
```

---

## PetscDualSpaceView#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpaceView/

**Contents:**
- PetscDualSpaceView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Views a PetscDualSpace

sp - the PetscDualSpace object to view

PetscViewer, PetscDualSpaceDestroy(), PetscDualSpace

src/dm/dt/dualspace/interface/dualspace.c

PetscDualSpaceView_Lagrange() in src/dm/dt/dualspace/impls/lagrange/dspacelagrange.c PetscDualSpaceView_Refined() in src/dm/dt/dualspace/impls/refined/dualspacerefined.c PetscDualSpaceView_Sum() in src/dm/dt/dualspace/impls/sum/dualspacesum.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpace
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscDualSpaceView(PetscDualSpace sp, PetscViewer v)
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscDualSpace#

**URL:** https://petsc.org/release/manualpages/DUALSPACE/PetscDualSpace/

**Contents:**
- PetscDualSpace#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

PETSc object that manages a dual space PetscSpace, e.g. the space of evaluation functionals at the vertices of a triangle

PetscDualSpaceCreate(), PetscSpace, PetscSpaceCreate(), PetscDualSpaceSetType(), PetscDualSpaceType

include/petscdualspace.h

src/dm/impls/plex/tutorials/ex15.c src/dm/dt/dualspace/impls/lagrange/tutorials/ex1.c src/dm/impls/plex/tutorials/ex16.c

_p_PetscDualSpace in include/petsc/private/petscfeimpl.h PetscDualSpace_Lag in include/petsc/private/petscfeimpl.h PetscDualSpace_Sum in include/petsc/private/petscfeimpl.h PetscDualSpace_Simple in include/petsc/private/petscfeimpl.h PetscDualSpace_Refined in src/dm/dt/dualspace/impls/refined/dualspacerefined.c

Index of all DUALSPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_PetscDualSpace *PetscDualSpace;
```

Example 2 (unknown):
```unknown
PetscDualSpaceCreate()
```

Example 3 (unknown):
```unknown
PetscSpaceCreate()
```

Example 4 (unknown):
```unknown
PetscDualSpaceSetType()
```

---

## PETSCFEBASIC#

**URL:** https://petsc.org/release/manualpages/FE/PETSCFEBASIC/

**Contents:**
- PETSCFEBASIC#
- See Also#
- Level#
- Location#

“basic” - A PetscFE object that integrates with basic tiling and no vectorization

PetscFE, PetscFEType, PetscFECreate(), PetscFESetType()

src/dm/dt/fe/impls/basic/febasic.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFEType
```

Example 2 (unknown):
```unknown
PetscFECreate()
```

Example 3 (unknown):
```unknown
PetscFESetType()
```

---

## PetscFECompositeGetMapping#

**URL:** https://petsc.org/release/manualpages/FE/PetscFECompositeGetMapping/

**Contents:**
- PetscFECompositeGetMapping#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Returns the mappings from the reference element to each subelement

fem - The PetscFE object

numSubelements - The number of sub elements

v0 - The affine transformation for each element, an array of length \(dim * Nc\). Pass NULL to ignore.

jac - The Jacobian for each element, an array of length \(dim^2 * Nc\). Pass NULL to ignore.

invjac - The inverse of the Jacobian, an array of length \(dim^2 * Nc\). Pass NULL to ignore.

Do not free the output arrays.

PetscFE, PetscFECreate()

src/dm/dt/fe/impls/composite/fecomposite.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
#include "petscdt.h" 
PetscErrorCode PetscFECompositeGetMapping(PetscFE fem, PeOp PetscInt *numSubelements, PeOp const PetscReal *v0[], PeOp const PetscReal *jac[], PeOp const PetscReal *invjac[])
```

Example 2 (unknown):
```unknown
PetscFECreate()
```

---

## PETSCFECOMPOSITE#

**URL:** https://petsc.org/release/manualpages/FE/PETSCFECOMPOSITE/

**Contents:**
- PETSCFECOMPOSITE#
- See Also#
- Level#
- Location#

“composite” - A PetscFEType that represents a composite element

PetscFEType, PetscFECreate(), PetscFESetType()

src/dm/dt/fe/impls/composite/fecomposite.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFEType
```

Example 2 (unknown):
```unknown
PetscFEType
```

Example 3 (unknown):
```unknown
PetscFECreate()
```

Example 4 (unknown):
```unknown
PetscFESetType()
```

---

## PetscFEComputeTabulation#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEComputeTabulation/

**Contents:**
- PetscFEComputeTabulation#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Tabulates the basis functions, and perhaps derivatives, at the points provided.

fem - The PetscFE object

npoints - The number of tabulation points

points - The tabulation point coordinates

K - The number of derivatives calculated

T - An existing tabulation object with enough allocated space, created with PetscFECreateTabulation()

T - The basis function values and derivatives at tabulation points

PetscTabulation, PetscFEGetCellTabulation(), PetscTabulationDestroy(), PetscFECreateTabulation()

src/dm/dt/fe/interface/fe.c

PetscFEComputeTabulation_Basic() in src/dm/dt/fe/impls/basic/febasic.c PetscFEComputeTabulation_Composite() in src/dm/dt/fe/impls/composite/fecomposite.c PetscFEComputeTabulation_Vector() in src/dm/dt/fe/impls/vector/fevector.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEComputeTabulation(PetscFE fem, PetscInt npoints, const PetscReal points[], PetscInt K, PetscTabulation T)
```

Example 2 (unknown):
```unknown
PetscFECreateTabulation()
```

Example 3 (perl):
```perl
T->T[0] = B[(p*pdim + i)*Nc + c] is the value at point p for basis function i and component c
  T->T[1] = D[((p*pdim + i)*Nc + c)*dim + d] is the derivative value at point p for basis function i, component c, in direction d
  T->T[2] = H[(((p*pdim + i)*Nc + c)*dim + d)*dim + e] is the Hessian value at point p for basis function i, component c, in directions d and e
```

Example 4 (unknown):
```unknown
PetscTabulation
```

---

## PetscFECopyQuadrature#

**URL:** https://petsc.org/release/manualpages/FE/PetscFECopyQuadrature/

**Contents:**
- PetscFECopyQuadrature#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Copy both volumetric and surface quadrature to a new PetscFE

sfe - The PetscFE source for the quadratures

tfe - The PetscFE target for the quadratures

PetscFE, PetscSpace, PetscDualSpace, PetscQuadrature, PetscFECreate(), PetscFESetQuadrature(), PetscFESetFaceQuadrature()

src/dm/dt/fe/interface/fe.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex11.c src/snes/tutorials/ex76.c src/tao/tutorials/ex2.c src/snes/tutorials/ex12.c src/snes/tutorials/ex24.c src/snes/tutorials/ex27.c src/snes/tutorials/ex69.c src/tao/tutorials/ex1.c src/snes/tutorials/ex77.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFECopyQuadrature(PetscFE sfe, PetscFE tfe)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscFECreate()
```

---

## PetscFECreateBrokenElement#

**URL:** https://petsc.org/release/manualpages/FE/PetscFECreateBrokenElement/

**Contents:**
- PetscFECreateBrokenElement#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Create a discontinuous version of the input PetscFE

cgfe - The continuous PetscFE object

dgfe - The discontinuous PetscFE object

This only works for Lagrange elements.

PetscFECreate(), PetscSpaceCreate(), PetscDualSpaceCreate(), PetscFECreateLagrange(), PetscFECreateLagrangeByCell(), PetscDualSpaceLagrangeSetContinuity()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFECreateBrokenElement(PetscFE cgfe, PetscFE *dgfe)
```

Example 2 (unknown):
```unknown
PetscFECreate()
```

Example 3 (unknown):
```unknown
PetscSpaceCreate()
```

Example 4 (unknown):
```unknown
PetscDualSpaceCreate()
```

---

## PetscFECreateByCell#

**URL:** https://petsc.org/release/manualpages/FE/PetscFECreateByCell/

**Contents:**
- PetscFECreateByCell#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#

Create a PetscFE for basic FEM computation

dim - The spatial dimension

Nc - The number of components

ct - The celltype of the reference cell

prefix - The options prefix, or NULL

qorder - The quadrature order or PETSC_DETERMINE to use PetscSpace polynomial degree

fem - The PetscFE object

Each subobject is SetFromOption() during creation, so that the object may be customized from the command line, using the prefix specified above. See the links below for the particular options available.

This should be called PetscFECreateDefaultByCell() since it is the extension/replacement for PetscFECreateDefault()

Since this generalizes/replaces PetscFECreateDefault() for different DMPolytopeType its name should be PetscFECreateDefaultByPolytopeType()

PetscFE, PetscFECreateDefault(), PetscFECreateLagrange(), PetscSpaceSetFromOptions(), PetscDualSpaceSetFromOptions(), PetscFESetFromOptions(), PetscFECreate(), PetscSpaceCreate(), PetscDualSpaceCreate(), DMPolytopeType

src/dm/dt/fe/interface/fe.c

src/snes/tutorials/ex36.c src/snes/tutorials/ex17.c src/snes/tutorials/ex27.c src/snes/tutorials/ex34.c src/dm/impls/swarm/tutorials/ex1.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFECreateByCell(MPI_Comm comm, PetscInt dim, PetscInt Nc, DMPolytopeType ct, const char prefix[], PetscInt qorder, PetscFE *fem)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
PetscFECreateDefaultByCell()
```

Example 4 (unknown):
```unknown
PetscFECreateDefault()
```

---

## PetscFECreateCellGeometry#

**URL:** https://petsc.org/release/manualpages/FE/PetscFECreateCellGeometry/

**Contents:**
- PetscFECreateCellGeometry#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Populates the arrays in a PetscFEGeom for a single reference cell of a PetscFE.

fe - the PetscFE whose dual-space DM provides the reference cell

quad - the quadrature at which to evaluate the geometry, or NULL to use the PetscFE’s own quadrature

cgeom - the PetscFEGeom populated with reference-cell coordinates, Jacobians, inverse Jacobians, and their determinants

This does not create cgeom, it allocates the arrays within one

Free the storage with PetscFEDestroyCellGeometry().

PetscFE, PetscFEGeom, PetscFEDestroyCellGeometry(), PetscFEGetQuadrature(), DMPlexComputeCellGeometryFEM()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFEGeom
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFECreateCellGeometry(PetscFE fe, PetscQuadrature quad, PetscFEGeom *cgeom)
```

Example 3 (unknown):
```unknown
PetscFEGeom
```

Example 4 (unknown):
```unknown
PetscFEDestroyCellGeometry()
```

---

## PetscFECreateDefault#

**URL:** https://petsc.org/release/manualpages/FE/PetscFECreateDefault/

**Contents:**
- PetscFECreateDefault#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Create a PetscFE for basic FEM computation

dim - The spatial dimension

Nc - The number of components

isSimplex - Flag for simplex reference cell, otherwise its a tensor product

prefix - The options prefix, or NULL

qorder - The quadrature order or PETSC_DETERMINE to use PetscSpace polynomial degree

fem - The PetscFE object

Preferred usage is PetscFECreateByCell()

Each subobject is SetFromOption() during creation, so that the object may be customized from the command line, using the prefix specified above. See the links below for the particular options available.

PetscFE, PetscFECreateLagrange(), PetscFECreateByCell(), PetscSpaceSetFromOptions(), PetscDualSpaceSetFromOptions(), PetscFESetFromOptions(), PetscFECreate(), PetscSpaceCreate(), PetscDualSpaceCreate()

src/dm/dt/fe/interface/fe.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex77.c src/snes/tutorials/ex26.c src/snes/tutorials/ex8.c src/snes/tutorials/ex23.c src/snes/tutorials/ex64.c src/snes/tutorials/ex62.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFECreateDefault(MPI_Comm comm, PetscInt dim, PetscInt Nc, PetscBool isSimplex, const char prefix[], PetscInt qorder, PetscFE *fem)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
PetscFECreateByCell()
```

Example 4 (unknown):
```unknown
PetscFECreateLagrange()
```

---

## PetscFECreateFromSpaces#

**URL:** https://petsc.org/release/manualpages/FE/PetscFECreateFromSpaces/

**Contents:**
- PetscFECreateFromSpaces#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Create a PetscFE from the basis and dual spaces

q - The cell quadrature

fq - The face quadrature

fem - The PetscFE object

The PetscFE takes ownership of these spaces by calling destroy on each. They should not be used after this call, and for borrowed references from PetscFEGetSpace() and the like, the caller must use PetscObjectReference() before this call.

PetscFE, PetscSpace, PetscDualSpace, PetscQuadrature, PetscFECreateLagrangeByCell(), PetscFECreateDefault(), PetscFECreateByCell(), PetscFECreate(), PetscSpaceCreate(), PetscDualSpaceCreate()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFECreateFromSpaces(PetscSpace P, PetscDualSpace Q, PetscQuadrature q, PetscQuadrature fq, PetscFE *fem)
```

Example 2 (unknown):
```unknown
PetscFEGetSpace()
```

Example 3 (unknown):
```unknown
PetscObjectReference()
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscFECreateHeightTrace#

**URL:** https://petsc.org/release/manualpages/FE/PetscFECreateHeightTrace/

**Contents:**
- PetscFECreateHeightTrace#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Create the trace PetscFE for the first mesh point of the given height stratum.

fe - the PetscFE object

height - the height of the stratum whose first point is used to construct the trace element

trFE - the trace PetscFE, or NULL if the requested height stratum is empty

PetscFE, PetscFECreatePointTrace(), PetscFEGetHeightSubspace(), DMPlexGetHeightStratum()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFECreateHeightTrace(PetscFE fe, PetscInt height, PetscFE *trFE)
```

Example 2 (unknown):
```unknown
PetscFECreatePointTrace()
```

Example 3 (unknown):
```unknown
PetscFEGetHeightSubspace()
```

Example 4 (unknown):
```unknown
DMPlexGetHeightStratum()
```

---

## PetscFECreateLagrangeByCell#

**URL:** https://petsc.org/release/manualpages/FE/PetscFECreateLagrangeByCell/

**Contents:**
- PetscFECreateLagrangeByCell#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Create a PetscFE for the basic Lagrange space of degree k

dim - The spatial dimension

Nc - The number of components

ct - The celltype of the reference cell

k - The degree of the space

qorder - The quadrature order or PETSC_DETERMINE to use PetscSpace polynomial degree

fem - The PetscFE object

For simplices, this element is the space of maximum polynomial degree k, otherwise it is a tensor product of 1D polynomials, each with maximal degree k.

Since this generalizes/replaces PetscFECreateLagrange() for different DMPolytopeType its name should be PetscFECreateLagrangeByPolytopeType()

PetscFE, PetscFECreateLagrange(), PetscFECreateDefault(), PetscFECreateByCell(), PetscFECreate(), PetscSpaceCreate(), PetscDualSpaceCreate(), DMPolytopeType

src/dm/dt/fe/interface/fe.c

src/snes/tutorials/ex27.c src/snes/tutorials/ex11.c src/dm/impls/plex/tutorials/ex16.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFECreateLagrangeByCell(MPI_Comm comm, PetscInt dim, PetscInt Nc, DMPolytopeType ct, PetscInt k, PetscInt qorder, PetscFE *fem)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
PetscFECreateLagrange()
```

Example 4 (unknown):
```unknown
DMPolytopeType
```

---

## PetscFECreateLagrange#

**URL:** https://petsc.org/release/manualpages/FE/PetscFECreateLagrange/

**Contents:**
- PetscFECreateLagrange#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Create a PetscFE for the basic Lagrange space of degree k

dim - The spatial dimension

Nc - The number of components

isSimplex - Flag for simplex reference cell, otherwise its a tensor product

k - The degree of the space

qorder - The quadrature order or PETSC_DETERMINE to use PetscSpace polynomial degree

fem - The PetscFE object

Preferred usage is PetscFECreateLagrangeByCell()

For simplices, this element is the space of maximum polynomial degree k, otherwise it is a tensor product of 1D polynomials, each with maximal degree k.

PetscFE, PetscFECreateLagrangeByCell(), PetscFECreateDefault(), PetscFECreateByCell(), PetscFECreate(), PetscSpaceCreate(), PetscDualSpaceCreate()

src/dm/dt/fe/interface/fe.c

src/dm/impls/plex/tutorials/ex15.c src/dm/impls/plex/tutorials/ex8.c src/dm/impls/swarm/tutorials/ex1f90.F90

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFECreateLagrange(MPI_Comm comm, PetscInt dim, PetscInt Nc, PetscBool isSimplex, PetscInt k, PetscInt qorder, PetscFE *fem)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
PetscFECreateLagrangeByCell()
```

Example 4 (unknown):
```unknown
PetscFECreateLagrangeByCell()
```

---

## PetscFECreateTabulation#

**URL:** https://petsc.org/release/manualpages/FE/PetscFECreateTabulation/

**Contents:**
- PetscFECreateTabulation#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Creates a PetscTabulation object to hold the basis functions, and perhaps derivatives, at the points provided.

fem - The PetscFE object

nrepl - The number of replicas

npoints - The number of tabulation points in a replica

points - The tabulation point coordinates

K - The number of derivatives calculated

T - The PetscTabulation to hold the basis function values and derivatives at tabulation points

PetscTabulation, PetscFEGetCellTabulation(), PetscTabulationDestroy(), PetscFEComputeTabulation()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscTabulation
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFECreateTabulation(PetscFE fem, PetscInt nrepl, PetscInt npoints, const PetscReal points[], PetscInt K, PetscTabulation *T)
```

Example 3 (unknown):
```unknown
PetscTabulation
```

Example 4 (unknown):
```unknown
PetscTabulation
```

---

## PetscFECreateVector#

**URL:** https://petsc.org/release/manualpages/FE/PetscFECreateVector/

**Contents:**
- PetscFECreateVector#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Create a vector-valued PetscFE from multiple copies of an underlying PetscFE.

scalar_fe - a PetscFE finite element

num_copies - a positive integer

interleave_basis - if PETSC_TRUE, the first num_copies basis vectors of the output finite element will be copies of the first basis vector of scalar_fe, and so on for the other basis vectors; otherwise all of the first-copy basis vectors will come first, followed by all of the second-copy, and so on.

interleave_components - if PETSC_TRUE, the first num_copies components of the output finite element will be copies of the first component of scalar_fe, and so on for the other components; otherwise all of the first-copy components will come first, followed by all of the second-copy, and so on.

vector_fe - a PetscFE of type PETSCFEVECTOR that represent a discretization space with num_copies copies of scalar_fe

PetscFE, PetscFEType, PetscFECreate(), PetscFESetType(), PETSCFEBASIC, PETSCFEVECTOR

src/dm/dt/fe/impls/vector/fevector.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFECreateVector(PetscFE scalar_fe, PetscInt num_copies, PetscBool interleave_basis, PetscBool interleave_components, PetscFE *vector_fe)
```

Example 2 (unknown):
```unknown
PETSCFEVECTOR
```

Example 3 (unknown):
```unknown
PetscFEType
```

Example 4 (unknown):
```unknown
PetscFECreate()
```

---

## PetscFECreate#

**URL:** https://petsc.org/release/manualpages/FE/PetscFECreate/

**Contents:**
- PetscFECreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Creates an empty PetscFE object. The type can then be set with PetscFESetType().

comm - The communicator for the PetscFE object

fem - The PetscFE object

PetscFE, PetscFEType, PetscFESetType(), PetscFECreateDefault(), PETSCFEGALERKIN

src/dm/dt/fe/interface/fe.c

PetscFECreate_Basic() in src/dm/dt/fe/impls/basic/febasic.c PetscFECreate_Composite() in src/dm/dt/fe/impls/composite/fecomposite.c PetscFECreate_OpenCL() in src/dm/dt/fe/impls/opencl/feopencl.c PetscFECreate_Vector() in src/dm/dt/fe/impls/vector/fevector.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFESetType()
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFECreate(MPI_Comm comm, PetscFE *fem)
```

Example 3 (unknown):
```unknown
PetscFEType
```

Example 4 (unknown):
```unknown
PetscFESetType()
```

---

## PetscFEDestroyCellGeometry#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEDestroyCellGeometry/

**Contents:**
- PetscFEDestroyCellGeometry#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Free the arrays inside a PetscFEGeom allocated by PetscFECreateCellGeometry().

fe - the PetscFE (unused, kept for API symmetry with PetscFECreateCellGeometry())

cgeom - the PetscFEGeom whose owned arrays should be freed

PetscFE, PetscFEGeom, PetscFECreateCellGeometry()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFEGeom
```

Example 2 (unknown):
```unknown
PetscFECreateCellGeometry()
```

Example 3 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEDestroyCellGeometry(PetscFE fe, PetscFEGeom *cgeom)
```

Example 4 (unknown):
```unknown
PetscFECreateCellGeometry()
```

---

## PetscFEDestroy#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEDestroy/

**Contents:**
- PetscFEDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Destroys a PetscFE object

fem - the PetscFE object to destroy

PetscFE, PetscFEView()

src/dm/dt/fe/interface/fe.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex26.c src/snes/tutorials/ex17.c src/snes/tutorials/ex8.c src/snes/tutorials/ex23.c src/snes/tutorials/ex64.c src/snes/tutorials/ex62.c

PetscFEDestroy_Basic() in src/dm/dt/fe/impls/basic/febasic.c PetscFEDestroy_Composite() in src/dm/dt/fe/impls/composite/fecomposite.c PetscFEDestroy_OpenCL() in src/dm/dt/fe/impls/opencl/feopencl.c PetscFEDestroy_Vector() in src/dm/dt/fe/impls/vector/fevector.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEDestroy(PetscFE *fem)
```

Example 2 (unknown):
```unknown
PetscFEView()
```

---

## PetscFEExpandFaceQuadrature#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEExpandFaceQuadrature/

**Contents:**
- PetscFEExpandFaceQuadrature#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Expand a face quadrature into a cell quadrature by mapping the face quadrature points and weights through each face of the cell reference geometry.

fe - the PetscFE object whose cell geometry defines the faces

fq - the face quadrature to expand

efq - the expanded quadrature covering all faces of the cell

PetscFE, PetscQuadrature, PetscFECreateFaceQuadrature(), PetscFEGetQuadrature()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEExpandFaceQuadrature(PetscFE fe, PetscQuadrature fq, PetscQuadrature *efq)
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
PetscFECreateFaceQuadrature()
```

Example 4 (unknown):
```unknown
PetscFEGetQuadrature()
```

---

## PetscFEGeomComplete#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEGeomComplete/

**Contents:**
- PetscFEGeomComplete#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Calculate derived quantities from a base geometry specification

geom - PetscFEGeom object

PetscFEGeom, PetscFEGeomCreate()

src/dm/dt/fe/interface/fegeom.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEGeomComplete(PetscFEGeom *geom)
```

Example 2 (unknown):
```unknown
PetscFEGeom
```

Example 3 (unknown):
```unknown
PetscFEGeom
```

Example 4 (unknown):
```unknown
PetscFEGeomCreate()
```

---

## PetscFEGeomCreate#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEGeomCreate/

**Contents:**
- PetscFEGeomCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Create a PetscFEGeom object to manage geometry for a group of cells

quad - A PetscQuadrature determining the tabulation

numCells - The number of cells in the group

dimEmbed - The coordinate dimension

mode - Type of geometry data to store

geom - The PetscFEGeom object, which is a struct not a PetscObject

PetscFEGeom, PetscQuadrature, PetscFEGeomDestroy(), PetscFEGeomComplete()

src/dm/dt/fe/interface/fegeom.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFEGeom
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEGeomCreate(PetscQuadrature quad, PetscInt numCells, PetscInt dimEmbed, PetscFEGeomMode mode, PetscFEGeom **geom)
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscFEGeom
```

---

## PetscFEGeomDestroy#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEGeomDestroy/

**Contents:**
- PetscFEGeomDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Destroy a PetscFEGeom object

geom - PetscFEGeom object

PetscFEGeom, PetscFEGeomCreate()

src/dm/dt/fe/interface/fegeom.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFEGeom
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEGeomDestroy(PetscFEGeom **geom)
```

Example 3 (unknown):
```unknown
PetscFEGeom
```

Example 4 (unknown):
```unknown
PetscFEGeom
```

---

## PetscFEGeomGetCellPoint#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEGeomGetCellPoint/

**Contents:**
- PetscFEGeomGetCellPoint#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Get the cell geometry for cell c at point p as a PetscFEGeom

geom - PetscFEGeom object

pgeom - The cell geometry of cell c at point p

For PETSC_FEGEOM_BOUNDARY mode, this gives the geometry for supporting cell 0. For PETSC_FEGEOM_COHESIVE mode, this gives the bulk geometry for that internal face.

For affine geometries, this only copies to pgeom at point 0. Since we copy pointers into pgeom, nothing needs to be done with it afterwards.

PetscFEGeom, PetscFEGeomMode, PetscFEGeomRestoreChunk(), PetscFEGeomCreate()

src/dm/dt/fe/interface/fegeom.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFEGeom
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEGeomGetCellPoint(PetscFEGeom *geom, PetscInt c, PetscInt p, PetscFEGeom *pgeom)
```

Example 3 (unknown):
```unknown
PetscFEGeom
```

Example 4 (unknown):
```unknown
PetscFEGeom
```

---

## PetscFEGeomGetChunk#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEGeomGetChunk/

**Contents:**
- PetscFEGeomGetChunk#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Get a chunk of cells in the group as a PetscFEGeom

geom - PetscFEGeom object

cStart - The first cell in the chunk

cEnd - The first cell not in the chunk

chunkGeom - an array of cells of length cEnd - cStart

Use PetscFEGeomRestoreChunk() to return the result

PetscFEGeom, PetscFEGeomRestoreChunk(), PetscFEGeomCreate()

src/dm/dt/fe/interface/fegeom.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFEGeom
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEGeomGetChunk(PetscFEGeom *geom, PetscInt cStart, PetscInt cEnd, PetscFEGeom *chunkGeom[])
```

Example 3 (unknown):
```unknown
PetscFEGeom
```

Example 4 (unknown):
```unknown
PetscFEGeomRestoreChunk()
```

---

## PetscFEGeomGetPoint#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEGeomGetPoint/

**Contents:**
- PetscFEGeomGetPoint#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Get the geometry for cell c at point p as a PetscFEGeom

geom - PetscFEGeom object

pcoords - The reference coordinates of point p, or NULL

pgeom - The geometry of cell c at point p

For affine geometries, this only copies to pgeom at point 0. Since we copy pointers into pgeom, nothing needs to be done with it afterwards.

In the affine case, pgeom must have storage for the integration point coordinates in pgeom->v if pcoords is passed in.

PetscFEGeom, PetscFEGeomRestoreChunk(), PetscFEGeomCreate()

src/dm/dt/fe/interface/fegeom.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFEGeom
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEGeomGetPoint(PetscFEGeom *geom, PetscInt c, PetscInt p, const PetscReal pcoords[], PetscFEGeom *pgeom)
```

Example 3 (unknown):
```unknown
PetscFEGeom
```

Example 4 (unknown):
```unknown
PetscFEGeom
```

---

## PetscFEGeomMode#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEGeomMode/

**Contents:**
- PetscFEGeomMode#
- Synopsis#
- Values#
- Note#
- See Also#
- Level#
- Location#

Describes the type of geometry being encoded.

PETSC_FEGEOM_BASIC - These are normal dim-cells, with dim == dE, and only bulk data is stored.

PETSC_FEGEOM_EMBEDDED - These are dim-cells embedded in a higher dimension, as an embedded manifold, where dim < dE and only bulk data is stored.

PETSC_FEGEOM_BOUNDARY - These are dim-cells on the boundary of a dE-mesh, so that dim < dE, and both bulk and s = 1 face data are stored.

PETSC_FEGEOM_COHESIVE - These are dim-cells in the interior of a dE-mesh, so that dim < dE, and both bulk and s = 2 face data are stored.

.vb dim - The topological dimension and reference coordinate dimension dE - The real coordinate dimension s - The number of supporting cells for a face .ve

DM Basics, PetscFEGeom, DM, DMPLEX, PetscFEGeomCreate()

include/petscfetypes.h

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  PETSC_FEGEOM_BASIC,
  PETSC_FEGEOM_EMBEDDED,
  PETSC_FEGEOM_BOUNDARY,
  PETSC_FEGEOM_COHESIVE
} PetscFEGeomMode;
```

Example 2 (unknown):
```unknown
PETSC_FEGEOM_BASIC
```

Example 3 (unknown):
```unknown
PETSC_FEGEOM_EMBEDDED
```

Example 4 (unknown):
```unknown
PETSC_FEGEOM_BOUNDARY
```

---

## PetscFEGeomRestoreChunk#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEGeomRestoreChunk/

**Contents:**
- PetscFEGeomRestoreChunk#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Restore the chunk obtained with PetscFEGeomCreateChunk()

geom - PetscFEGeom object

cStart - The first cell in the chunk

cEnd - The first cell not in the chunk

chunkGeom - The chunk of cells

PetscFEGeom, PetscFEGeomGetChunk(), PetscFEGeomCreate()

src/dm/dt/fe/interface/fegeom.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFEGeomCreateChunk()
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEGeomRestoreChunk(PetscFEGeom *geom, PetscInt cStart, PetscInt cEnd, PetscFEGeom **chunkGeom)
```

Example 3 (unknown):
```unknown
PetscFEGeom
```

Example 4 (unknown):
```unknown
PetscFEGeom
```

---

## PetscFEGeom#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEGeom/

**Contents:**
- PetscFEGeom#
- Note#
- See Also#
- Level#
- Location#

Structure for geometric information for PetscFE

This is a struct, not a PetscObject

PetscFE, PetscFEGeomCreate(), PetscFEGeomDestroy(), PetscFEGeomGetChunk(), PetscFEGeomRestoreChunk(), PetscFEGeomGetPoint(), PetscFEGeomGetCellPoint(), PetscFEGeomComplete(), PetscSpace, PetscDualSpace

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscObject
```

Example 2 (unknown):
```unknown
PetscFEGeomCreate()
```

Example 3 (unknown):
```unknown
PetscFEGeomDestroy()
```

Example 4 (unknown):
```unknown
PetscFEGeomGetChunk()
```

---

## PetscFEGetBasisSpace#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEGetBasisSpace/

**Contents:**
- PetscFEGetBasisSpace#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the PetscSpace used for the approximation of the solution for the PetscFE

fem - The PetscFE object

sp - The PetscSpace object

PetscFE, PetscSpace, PetscFECreate()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEGetBasisSpace(PetscFE fem, PetscSpace *sp)
```

Example 2 (unknown):
```unknown
PetscFECreate()
```

---

## PetscFEGetCeedBasis#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEGetCeedBasis/

**Contents:**
- PetscFEGetCeedBasis#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Get the Ceed object mirroring this PetscFE

basis - The CeedBasis

This is a borrowed reference, so it is not freed.

PetscFE, PetscFESetCeed(), DMGetCeed()

src/dm/dt/fe/interface/ceed/feceed.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEGetCeedBasis(PetscFE fe, CeedBasis *basis)
```

Example 2 (unknown):
```unknown
PetscFESetCeed()
```

Example 3 (unknown):
```unknown
DMGetCeed()
```

---

## PetscFEGetCellTabulation#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEGetCellTabulation/

**Contents:**
- PetscFEGetCellTabulation#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Returns the tabulation of the basis functions at the quadrature points on the reference cell

fem - The PetscFE object

k - The highest derivative we need to tabulate, very often 1

T - The basis function values and derivatives at quadrature points

PetscFE, PetscSpace, PetscDualSpace, PetscTabulation, PetscFECreateTabulation(), PetscTabulationDestroy()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEGetCellTabulation(PetscFE fem, PetscInt k, PetscTabulation *T)
```

Example 2 (perl):
```perl
T->T[0] = B[(p*pdim + i)*Nc + c] is the value at point p for basis function i and component c
  T->T[1] = D[((p*pdim + i)*Nc + c)*dim + d] is the derivative value at point p for basis function i, component c, in direction d
  T->T[2] = H[(((p*pdim + i)*Nc + c)*dim + d)*dim + e] is the Hessian value at point p for basis function i, component c, in directions d and e
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscTabulation
```

---

## PetscFEGetDimension#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEGetDimension/

**Contents:**
- PetscFEGetDimension#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get the dimension of the finite element space on a cell

PetscFE, PetscFECreate(), PetscSpaceGetDimension(), PetscDualSpaceGetDimension()

src/dm/dt/fe/interface/fe.c

PetscFEGetDimension_Basic() in src/dm/dt/fe/impls/basic/febasic.c PetscFEGetDimension_Vector() in src/dm/dt/fe/impls/vector/fevector.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEGetDimension(PetscFE fem, PetscInt *dim)
```

Example 2 (unknown):
```unknown
PetscFECreate()
```

Example 3 (unknown):
```unknown
PetscSpaceGetDimension()
```

Example 4 (unknown):
```unknown
PetscDualSpaceGetDimension()
```

---

## PetscFEGetDualSpace#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEGetDualSpace/

**Contents:**
- PetscFEGetDualSpace#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Returns the PetscDualSpace used to define the inner product for a PetscFE

fem - The PetscFE object

sp - The PetscDualSpace object

PetscFE, PetscSpace, PetscDualSpace, PetscFECreate()

src/dm/dt/fe/interface/fe.c

src/dm/impls/plex/tutorials/ex15.c src/dm/impls/plex/tutorials/ex16.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpace
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEGetDualSpace(PetscFE fem, PetscDualSpace *sp)
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscFEGetFaceCentroidTabulation#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEGetFaceCentroidTabulation/

**Contents:**
- PetscFEGetFaceCentroidTabulation#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Returns the tabulation of the basis functions at the face centroid points

fem - The PetscFE object

Tc - The basis function values at face centroid points

PetscFE, PetscSpace, PetscDualSpace, PetscTabulation, PetscFEGetFaceTabulation(), PetscFEGetCellTabulation(), PetscFECreateTabulation(), PetscTabulationDestroy()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEGetFaceCentroidTabulation(PetscFE fem, PetscTabulation *Tc)
```

Example 2 (perl):
```perl
T->T[0] = Bf[(f*pdim + i)*Nc + c] is the value at point f for basis function i and component c
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscTabulation
```

---

## PetscFEGetFaceQuadrature#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEGetFaceQuadrature/

**Contents:**
- PetscFEGetFaceQuadrature#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#

Returns the PetscQuadrature used to calculate inner products on faces

fem - The PetscFE object

q - The PetscQuadrature object

There is a special face quadrature but not edge, likely this API would benefit from a refactorization

PetscFE, PetscSpace, PetscDualSpace, PetscQuadrature, PetscFECreate(), PetscFESetQuadrature(), PetscFESetFaceQuadrature()

src/dm/dt/fe/interface/fe.c

src/ts/tutorials/ex53.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscQuadrature
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEGetFaceQuadrature(PetscFE fem, PetscQuadrature *q)
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscFEGetFaceTabulation#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEGetFaceTabulation/

**Contents:**
- PetscFEGetFaceTabulation#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Returns the tabulation of the basis functions at the face quadrature points for each face of the reference cell

fem - The PetscFE object

k - The highest derivative we need to tabulate, very often 1

Tf - The basis function values and derivatives at face quadrature points

PetscFE, PetscSpace, PetscDualSpace, PetscTabulation, PetscFEGetCellTabulation(), PetscFECreateTabulation(), PetscTabulationDestroy()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEGetFaceTabulation(PetscFE fem, PetscInt k, PetscTabulation *Tf)
```

Example 2 (perl):
```perl
T->T[0] = Bf[((f*Nq + q)*pdim + i)*Nc + c] is the value at point f,q for basis function i and component c
  T->T[1] = Df[(((f*Nq + q)*pdim + i)*Nc + c)*dim + d] is the derivative value at point f,q for basis function i, component c, in direction d
  T->T[2] = Hf[((((f*Nq + q)*pdim + i)*Nc + c)*dim + d)*dim + e] is the Hessian value at point f,q for basis function i, component c, in directions d and e
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscTabulation
```

---

## PetscFEGetHeightSubspace#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEGetHeightSubspace/

**Contents:**
- PetscFEGetHeightSubspace#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Get the subspace of this space for a mesh point of a given height

fe - The finite element space

height - The height of the DMPLEX point

subfe - The subspace of this PetscFE space

For example, if we want the subspace of this space for a face, we would choose height = 1.

PetscFECreateDefault()

src/dm/dt/fe/interface/fe.c

src/dm/impls/plex/tutorials/ex8.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEGetHeightSubspace(PetscFE fe, PetscInt height, PetscFE *subfe)
```

Example 2 (unknown):
```unknown
PetscFECreateDefault()
```

---

## PetscFEGetNumComponents#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEGetNumComponents/

**Contents:**
- PetscFEGetNumComponents#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the number of components in the element

fem - The PetscFE object

comp - The number of field components

PetscFE, PetscFECreate(), PetscFEGetSpatialDimension()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEGetNumComponents(PetscFE fem, PetscInt *comp)
```

Example 2 (unknown):
```unknown
PetscFECreate()
```

Example 3 (unknown):
```unknown
PetscFEGetSpatialDimension()
```

---

## PetscFEGetNumDof#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEGetNumDof/

**Contents:**
- PetscFEGetNumDof#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the number of dofs (dual basis vectors) associated to mesh points on the reference cell of a given dimension

fem - The PetscFE object

numDof - Array of length dim with the number of dofs in each dimension

PetscFE, PetscSpace, PetscDualSpace, PetscFECreate()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEGetNumDof(PetscFE fem, const PetscInt *numDof[])
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscFECreate()
```

---

## PetscFEGetQuadrature#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEGetQuadrature/

**Contents:**
- PetscFEGetQuadrature#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Returns the PetscQuadrature used to calculate inner products

fem - The PetscFE object

q - The PetscQuadrature object

PetscFE, PetscSpace, PetscDualSpace, PetscQuadrature, PetscFECreate()

src/dm/dt/fe/interface/fe.c

src/ts/tutorials/ex18.c src/ts/tutorials/ex53.c src/snes/tutorials/ex23.c src/snes/tutorials/ex64.c src/snes/tutorials/ex62.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscQuadrature
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEGetQuadrature(PetscFE fem, PetscQuadrature *q)
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscFEGetSpatialDimension#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEGetSpatialDimension/

**Contents:**
- PetscFEGetSpatialDimension#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the spatial dimension of the element

fem - The PetscFE object

dim - The spatial dimension

PetscFE, PetscFECreate()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEGetSpatialDimension(PetscFE fem, PetscInt *dim)
```

Example 2 (unknown):
```unknown
PetscFECreate()
```

---

## PetscFEGetTileSizes#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEGetTileSizes/

**Contents:**
- PetscFEGetTileSizes#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Returns the tile sizes for evaluation

fem - The PetscFE object

blockSize - The number of elements in a block, pass NULL if not needed

numBlocks - The number of blocks in a batch, pass NULL if not needed

batchSize - The number of elements in a batch, pass NULL if not needed

numBatches - The number of batches in a chunk, pass NULL if not needed

PetscFE, PetscFECreate(), PetscFESetTileSizes()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEGetTileSizes(PetscFE fem, PeOp PetscInt *blockSize, PeOp PetscInt *numBlocks, PeOp PetscInt *batchSize, PeOp PetscInt *numBatches)
```

Example 2 (unknown):
```unknown
PetscFECreate()
```

Example 3 (unknown):
```unknown
PetscFESetTileSizes()
```

---

## PetscFEGetType#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEGetType/

**Contents:**
- PetscFEGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the PetscFEType (as a string) from the PetscFE object.

name - The PetscFEType name

PetscFEType, PetscFE, PetscFESetType(), PetscFECreate()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFEType
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEGetType(PetscFE fem, PetscFEType *name)
```

Example 3 (unknown):
```unknown
PetscFEType
```

Example 4 (unknown):
```unknown
PetscFEType
```

---

## PetscFEIntegrateBdJacobian#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEIntegrateBdJacobian/

**Contents:**
- PetscFEIntegrateBdJacobian#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Produce the boundary element Jacobian for a chunk of elements by quadrature integration

ds - The PetscDS specifying the discretizations and continuum functions

wf - The PetscWeakForm holding the pointwise functions

jtype - The type of matrix pointwise functions that should be used

key - The (label+value, fieldI*Nf + fieldJ) being integrated

Ne - The number of elements in the chunk

fgeom - The face geometry for each cell in the chunk

coefficients - The array of FEM basis coefficients for the elements for the Jacobian evaluation point

coefficients_t - The array of FEM basis time derivative coefficients for the elements

probAux - The PetscDS specifying the auxiliary discretizations

coefficientsAux - The array of FEM auxiliary basis coefficients for the elements

u_tshift - A multiplier for the \(dF/du_t\) term (as opposed to the \(dF/du\) term)

elemMat - the element matrices for the Jacobian from each element

PetscFEIntegrateJacobian(), PetscFEIntegrateResidual()

src/dm/dt/fe/interface/fe.c

PetscFEIntegrateBdJacobian_Basic() in src/dm/dt/fe/impls/basic/febasic.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEIntegrateBdJacobian(PetscDS ds, PetscWeakForm wf, PetscFEJacobianType jtype, PetscFormKey key, PetscInt Ne, PetscFEGeom *fgeom, const PetscScalar coefficients[], const PetscScalar coefficients_t[], PetscDS probAux, const PetscScalar coefficientsAux[], PetscReal t, PetscReal u_tshift, PetscScalar elemMat[])
```

Example 2 (perl):
```perl
Loop over batch of elements (e):
    Loop over element matrix entries (f,fc,g,gc --> i,j):
      Loop over quadrature points (q):
        Make u_q and gradU_q (loops over fields,Nb,Ncomp)
          elemMat[i,j] += \psi^{fc}_f(q) g0_{fc,gc}(u, \nabla u) \phi^{gc}_g(q)
                       + \psi^{fc}_f(q) \cdot g1_{fc,gc,dg}(u, \nabla u) \nabla\phi^{gc}_g(q)
                       + \nabla\psi^{fc}_f(q) \cdot g2_{fc,gc,df}(u, \nabla u) \phi^{gc}_g(q)
                       + \nabla\psi^{fc}_f(q) \cdot g3_{fc,gc,df,dg}(u, \nabla u) \nabla\phi^{gc}_g(q)
```

Example 3 (unknown):
```unknown
PetscFEIntegrateJacobian()
```

Example 4 (unknown):
```unknown
PetscFEIntegrateResidual()
```

---

## PetscFEIntegrateBdResidual#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEIntegrateBdResidual/

**Contents:**
- PetscFEIntegrateBdResidual#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Produce the element residual vector for a chunk of elements by quadrature integration over a boundary

ds - The PetscDS specifying the discretizations and continuum functions

wf - The PetscWeakForm object holding the pointwise functions

key - The (label+value, field) being integrated

Ne - The number of elements in the chunk

fgeom - The face geometry for each cell in the chunk

coefficients - The array of FEM basis coefficients for the elements

coefficients_t - The array of FEM basis time derivative coefficients for the elements

probAux - The PetscDS specifying the auxiliary discretizations

coefficientsAux - The array of FEM auxiliary basis coefficients for the elements

elemVec - the element residual vectors from each element

PetscFEIntegrateResidual()

src/dm/dt/fe/interface/fe.c

PetscFEIntegrateBdResidual_Basic() in src/dm/dt/fe/impls/basic/febasic.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEIntegrateBdResidual(PetscDS ds, PetscWeakForm wf, PetscFormKey key, PetscInt Ne, PetscFEGeom *fgeom, const PetscScalar coefficients[], const PetscScalar coefficients_t[], PetscDS probAux, const PetscScalar coefficientsAux[], PetscReal t, PetscScalar elemVec[])
```

Example 2 (unknown):
```unknown
PetscFEIntegrateResidual()
```

---

## PetscFEIntegrateBd#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEIntegrateBd/

**Contents:**
- PetscFEIntegrateBd#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Produce the integral for the given field for a chunk of elements by quadrature integration

prob - The PetscDS specifying the discretizations and continuum functions

field - The field being integrated

obj_func - The function to be integrated

Ne - The number of elements in the chunk

geom - The face geometry for each face in the chunk

coefficients - The array of FEM basis coefficients for the elements

probAux - The PetscDS specifying the auxiliary discretizations

coefficientsAux - The array of FEM auxiliary basis coefficients for the elements

integral - the integral for this field

PetscFE, PetscDS, PetscFEIntegrateResidual(), PetscFEIntegrate()

src/dm/dt/fe/interface/fe.c

PetscFEIntegrateBd_Basic() in src/dm/dt/fe/impls/basic/febasic.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEIntegrateBd(PetscDS prob, PetscInt field, void (*obj_func)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt Ne, PetscFEGeom *geom, const PetscScalar coefficients[], PetscDS probAux, const PetscScalar coefficientsAux[], PetscScalar integral[])
```

Example 2 (unknown):
```unknown
PetscFEIntegrateResidual()
```

Example 3 (unknown):
```unknown
PetscFEIntegrate()
```

---

## PetscFEIntegrateHybridJacobian#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEIntegrateHybridJacobian/

**Contents:**
- PetscFEIntegrateHybridJacobian#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Produce the boundary element Jacobian for a chunk of hybrid elements by quadrature integration

ds - The PetscDS specifying the discretizations and continuum functions for the output

dsIn - The PetscDS specifying the discretizations and continuum functions for the input

jtype - The type of matrix pointwise functions that should be used

key - The (label+value, fieldI*Nf + fieldJ) being integrated

s - The side of the cell being integrated, 0 for negative and 1 for positive

Ne - The number of elements in the chunk

fgeom - The face geometry for each cell in the chunk

cgeom - The cell geometry for each neighbor cell in the chunk

coefficients - The array of FEM basis coefficients for the elements for the Jacobian evaluation point

coefficients_t - The array of FEM basis time derivative coefficients for the elements

probAux - The PetscDS specifying the auxiliary discretizations

coefficientsAux - The array of FEM auxiliary basis coefficients for the elements

u_tshift - A multiplier for the \(dF/du_t\) term (as opposed to the \(dF/du\) term)

elemMat - the element matrices for the Jacobian from each element

PetscFEIntegrateJacobian(), PetscFEIntegrateResidual()

src/dm/dt/fe/interface/fe.c

PetscFEIntegrateHybridJacobian_Basic() in src/dm/dt/fe/impls/basic/febasic.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEIntegrateHybridJacobian(PetscDS ds, PetscDS dsIn, PetscFEJacobianType jtype, PetscFormKey key, PetscInt s, PetscInt Ne, PetscFEGeom *fgeom, PetscFEGeom *cgeom, const PetscScalar coefficients[], const PetscScalar coefficients_t[], PetscDS probAux, const PetscScalar coefficientsAux[], PetscReal t, PetscReal u_tshift, PetscScalar elemMat[])
```

Example 2 (perl):
```perl
Loop over batch of elements (e):
    Loop over element matrix entries (f,fc,g,gc --> i,j):
      Loop over quadrature points (q):
        Make u_q and gradU_q (loops over fields,Nb,Ncomp)
          elemMat[i,j] += \psi^{fc}_f(q) g0_{fc,gc}(u, \nabla u) \phi^{gc}_g(q)
                       + \psi^{fc}_f(q) \cdot g1_{fc,gc,dg}(u, \nabla u) \nabla\phi^{gc}_g(q)
                       + \nabla\psi^{fc}_f(q) \cdot g2_{fc,gc,df}(u, \nabla u) \phi^{gc}_g(q)
                       + \nabla\psi^{fc}_f(q) \cdot g3_{fc,gc,df,dg}(u, \nabla u) \nabla\phi^{gc}_g(q)
```

Example 3 (unknown):
```unknown
PetscFEIntegrateJacobian()
```

Example 4 (unknown):
```unknown
PetscFEIntegrateResidual()
```

---

## PetscFEIntegrateHybridResidual#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEIntegrateHybridResidual/

**Contents:**
- PetscFEIntegrateHybridResidual#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Produce the element residual vector for a chunk of hybrid element faces by quadrature integration

ds - The PetscDS specifying the discretizations and continuum functions

dsIn - The PetscDS specifying the discretizations and continuum functions for input

key - The (label+value, field) being integrated

s - The side of the cell being integrated, 0 for negative and 1 for positive

Ne - The number of elements in the chunk

fgeom - The face geometry for each cell in the chunk

cgeom - The cell geometry for each neighbor cell in the chunk

coefficients - The array of FEM basis coefficients for the elements

coefficients_t - The array of FEM basis time derivative coefficients for the elements

probAux - The PetscDS specifying the auxiliary discretizations

coefficientsAux - The array of FEM auxiliary basis coefficients for the elements

elemVec - the element residual vectors from each element

PetscFEIntegrateResidual()

src/dm/dt/fe/interface/fe.c

PetscFEIntegrateHybridResidual_Basic() in src/dm/dt/fe/impls/basic/febasic.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEIntegrateHybridResidual(PetscDS ds, PetscDS dsIn, PetscFormKey key, PetscInt s, PetscInt Ne, PetscFEGeom *fgeom, PetscFEGeom *cgeom, const PetscScalar coefficients[], const PetscScalar coefficients_t[], PetscDS probAux, const PetscScalar coefficientsAux[], PetscReal t, PetscScalar elemVec[])
```

Example 2 (unknown):
```unknown
PetscFEIntegrateResidual()
```

---

## PetscFEIntegrateJacobian#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEIntegrateJacobian/

**Contents:**
- PetscFEIntegrateJacobian#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Produce the element Jacobian for a chunk of elements by quadrature integration

rds - The PetscDS specifying the row discretizations and continuum functions

cds - The PetscDS specifying the column discretizations

jtype - The type of matrix pointwise functions that should be used

key - The (label+value, fieldI*Nf + fieldJ) being integrated

Ne - The number of elements in the chunk

cgeom - The cell geometry for each cell in the chunk

coefficients - The array of FEM basis coefficients for the elements for the Jacobian evaluation point

coefficients_t - The array of FEM basis time derivative coefficients for the elements

dsAux - The PetscDS specifying the auxiliary discretizations

coefficientsAux - The array of FEM auxiliary basis coefficients for the elements

u_tshift - A multiplier for the \(dF/du_t\) term (as opposed to the \(dF/du\) term)

elemMat - the element matrices for the Jacobian from each element

PetscFEIntegrateResidual()

src/dm/dt/fe/interface/fe.c

PetscFEIntegrateJacobian_Basic() in src/dm/dt/fe/impls/basic/febasic.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEIntegrateJacobian(PetscDS rds, PetscDS cds, PetscFEJacobianType jtype, PetscFormKey key, PetscInt Ne, PetscFEGeom *cgeom, const PetscScalar coefficients[], const PetscScalar coefficients_t[], PetscDS dsAux, const PetscScalar coefficientsAux[], PetscReal t, PetscReal u_tshift, PetscScalar elemMat[])
```

Example 2 (perl):
```perl
Loop over batch of elements (e):
    Loop over element matrix entries (f,fc,g,gc --> i,j):
      Loop over quadrature points (q):
        Make u_q and gradU_q (loops over fields,Nb,Ncomp)
          elemMat[i,j] += \psi^{fc}_f(q) g0_{fc,gc}(u, \nabla u) \phi^{gc}_g(q)
                       + \psi^{fc}_f(q) \cdot g1_{fc,gc,dg}(u, \nabla u) \nabla\phi^{gc}_g(q)
                       + \nabla\psi^{fc}_f(q) \cdot g2_{fc,gc,df}(u, \nabla u) \phi^{gc}_g(q)
                       + \nabla\psi^{fc}_f(q) \cdot g3_{fc,gc,df,dg}(u, \nabla u) \nabla\phi^{gc}_g(q)
```

Example 3 (unknown):
```unknown
PetscFEIntegrateResidual()
```

---

## PetscFEIntegrateResidual#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEIntegrateResidual/

**Contents:**
- PetscFEIntegrateResidual#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Produce the element residual vector for a chunk of elements by quadrature integration

ds - The PetscDS specifying the discretizations and continuum functions

key - The (label+value, field) being integrated

Ne - The number of elements in the chunk

cgeom - The cell geometry for each cell in the chunk

coefficients - The array of FEM basis coefficients for the elements

coefficients_t - The array of FEM basis time derivative coefficients for the elements

probAux - The PetscDS specifying the auxiliary discretizations

coefficientsAux - The array of FEM auxiliary basis coefficients for the elements

elemVec - the element residual vectors from each element

PetscFEIntegrateBdResidual()

src/dm/dt/fe/interface/fe.c

PetscFEIntegrateResidual_Basic() in src/dm/dt/fe/impls/basic/febasic.c PetscFEIntegrateResidual_OpenCL() in src/dm/dt/fe/impls/opencl/feopencl.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEIntegrateResidual(PetscDS ds, PetscFormKey key, PetscInt Ne, PetscFEGeom *cgeom, const PetscScalar coefficients[], const PetscScalar coefficients_t[], PetscDS probAux, const PetscScalar coefficientsAux[], PetscReal t, PetscScalar elemVec[])
```

Example 2 (perl):
```perl
Loop over batch of elements (e):
    Loop over quadrature points (q):
      Make u_q and gradU_q (loops over fields,Nb,Ncomp) and x_q
      Call f_0 and f_1
    Loop over element vector entries (f,fc --> i):
      elemVec[i] += \psi^{fc}_f(q) f0_{fc}(u, \nabla u) + \nabla\psi^{fc}_f(q) \cdot f1_{fc,df}(u, \nabla u)
```

Example 3 (unknown):
```unknown
PetscFEIntegrateBdResidual()
```

---

## PetscFEIntegrate#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEIntegrate/

**Contents:**
- PetscFEIntegrate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Produce the integral for the given field for a chunk of elements by quadrature integration

prob - The PetscDS specifying the discretizations and continuum functions

field - The field being integrated

Ne - The number of elements in the chunk

cgeom - The cell geometry for each cell in the chunk

coefficients - The array of FEM basis coefficients for the elements

probAux - The PetscDS specifying the auxiliary discretizations

coefficientsAux - The array of FEM auxiliary basis coefficients for the elements

integral - the integral for this field

PetscFE, PetscDS, PetscFEIntegrateResidual(), PetscFEIntegrateBd()

src/dm/dt/fe/interface/fe.c

PetscFEIntegrate_Basic() in src/dm/dt/fe/impls/basic/febasic.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEIntegrate(PetscDS prob, PetscInt field, PetscInt Ne, PetscFEGeom *cgeom, const PetscScalar coefficients[], PetscDS probAux, const PetscScalar coefficientsAux[], PetscScalar integral[])
```

Example 2 (unknown):
```unknown
PetscFEIntegrateResidual()
```

Example 3 (unknown):
```unknown
PetscFEIntegrateBd()
```

---

## PetscFEJacobianType#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEJacobianType/

**Contents:**
- PetscFEJacobianType#
- See Also#
- Level#
- Location#

indicates which pointwise functions should be used to fill the Jacobian matrix

PetscFEIntegrateJacobian()

include/petscfetypes.h

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFEIntegrateJacobian()
```

---

## PetscFELimitDegree#

**URL:** https://petsc.org/release/manualpages/FE/PetscFELimitDegree/

**Contents:**
- PetscFELimitDegree#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Copy a PetscFE but limit the degree to be in the given range

minDegree - The minimum degree, or PETSC_DETERMINE for no limit

maxDegree - The maximum degree, or PETSC_DETERMINE for no limit

newfe - The PetscFE object

This currently only works for Lagrange elements.

PetscFECreateLagrange(), PetscFECreateDefault(), PetscFECreateByCell(), PetscFECreate(), PetscSpaceCreate(), PetscDualSpaceCreate()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFELimitDegree(PetscFE fe, PetscInt minDegree, PetscInt maxDegree, PetscFE *newfe)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
PETSC_DETERMINE
```

Example 4 (unknown):
```unknown
PetscFECreateLagrange()
```

---

## PetscFEOpenCLGetRealType#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEOpenCLGetRealType/

**Contents:**
- PetscFEOpenCLGetRealType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the scalar type for running on the OpenCL accelerator

realType - The scalar type

PetscFE, PetscFEOpenCLSetRealType()

src/dm/dt/fe/impls/opencl/feopencl.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEOpenCLGetRealType(PetscFE fem, PetscDataType *realType)
```

Example 2 (unknown):
```unknown
PetscFEOpenCLSetRealType()
```

---

## PetscFEOpenCLSetRealType#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEOpenCLSetRealType/

**Contents:**
- PetscFEOpenCLSetRealType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the scalar type for running on the OpenCL accelerator

realType - The scalar type

PetscFE, PetscFEOpenCLGetRealType()

src/dm/dt/fe/impls/opencl/feopencl.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEOpenCLSetRealType(PetscFE fem, PetscDataType realType)
```

Example 2 (unknown):
```unknown
PetscFEOpenCLGetRealType()
```

---

## PETSCFEOPENCL#

**URL:** https://petsc.org/release/manualpages/FE/PETSCFEOPENCL/

**Contents:**
- PETSCFEOPENCL#
- See Also#
- Level#
- Location#

“opencl” - A PetscFEType that integrates using a vectorized OpenCL implementation

PetscFEType, PetscFECreate(), PetscFESetType()

src/dm/dt/fe/impls/opencl/feopencl.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFEType
```

Example 2 (unknown):
```unknown
PetscFEType
```

Example 3 (unknown):
```unknown
PetscFECreate()
```

Example 4 (unknown):
```unknown
PetscFESetType()
```

---

## PetscFEPushforwardGradient#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEPushforwardGradient/

**Contents:**
- PetscFEPushforwardGradient#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Map the reference element function gradient to real space

fegeom - The cell geometry

Nv - The number of function gradient values

vals - The function gradient values

vals - The transformed function gradient values

This just forwards the call onto PetscDualSpacePushforwardGradient().

It only handles transformations when the embedding dimension of the geometry in fegeom is the same as the reference dimension.

PetscFE, PetscFEGeom, PetscDualSpace, PetscFEPushforward(), PetscDualSpacePushforwardGradient(), PetscDualSpacePushforward()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEPushforwardGradient(PetscFE fe, PetscFEGeom *fegeom, PetscInt Nv, PetscScalar vals[])
```

Example 2 (unknown):
```unknown
PetscDualSpacePushforwardGradient()
```

Example 3 (unknown):
```unknown
PetscFEGeom
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscFEPushforwardHessian#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEPushforwardHessian/

**Contents:**
- PetscFEPushforwardHessian#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#

Map the reference element function Hessian to real space

fegeom - The cell geometry

Nv - The number of function Hessian values

vals - The function Hessian values

vals - The transformed function Hessian values

This just forwards the call onto PetscDualSpacePushforwardHessian().

It only handles transformations when the embedding dimension of the geometry in fegeom is the same as the reference dimension.

It is unclear why all these one line convenience routines are desirable

PetscFE, PetscFEGeom, PetscDualSpace, PetscFEPushforward(), PetscDualSpacePushforwardHessian(), PetscDualSpacePushforward()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEPushforwardHessian(PetscFE fe, PetscFEGeom *fegeom, PetscInt Nv, PetscScalar vals[])
```

Example 2 (unknown):
```unknown
PetscDualSpacePushforwardHessian()
```

Example 3 (unknown):
```unknown
PetscFEGeom
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscFEPushforward#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEPushforward/

**Contents:**
- PetscFEPushforward#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Map the reference element function to real space

fegeom - The cell geometry

Nv - The number of function values

vals - The function values

vals - The transformed function values

This just forwards the call onto PetscDualSpacePushforward().

It only handles transformations when the embedding dimension of the geometry in fegeom is the same as the reference dimension.

PetscFE, PetscFEGeom, PetscDualSpace, PetscDualSpacePushforward()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEPushforward(PetscFE fe, PetscFEGeom *fegeom, PetscInt Nv, PetscScalar vals[])
```

Example 2 (unknown):
```unknown
PetscDualSpacePushforward()
```

Example 3 (unknown):
```unknown
PetscFEGeom
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscFERefine#

**URL:** https://petsc.org/release/manualpages/FE/PetscFERefine/

**Contents:**
- PetscFERefine#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Create a “refined” PetscFE object that refines the reference cell into smaller copies.

fe - The initial PetscFE

feRef - The refined PetscFE

This is typically used to generate a preconditioner for a higher order method from a lower order method on a refined mesh having the same number of dofs (but more sparsity). It is also used to create an interpolation between regularly refined meshes.

PetscFEType, PetscFECreate(), PetscFESetType()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFERefine(PetscFE fe, PetscFE *feRef)
```

Example 2 (unknown):
```unknown
PetscFEType
```

Example 3 (unknown):
```unknown
PetscFECreate()
```

Example 4 (unknown):
```unknown
PetscFESetType()
```

---

## PetscFERegister#

**URL:** https://petsc.org/release/manualpages/FE/PetscFERegister/

**Contents:**
- PetscFERegister#
- Synopsis#
- Input Parameters#
- Example Usage#
- Note#
- See Also#
- Level#
- Location#

Adds a new PetscFEType

Not Collective, No Fortran Support

sname - The name of a new user-defined creation routine

function - The creation routine

Then, your PetscFE type can be chosen with the procedural interface via

or at runtime via the option

PetscFERegister() may be called multiple times to add several user-defined PetscFEs

PetscFE, PetscFEType, PetscFERegisterAll(), PetscFERegisterDestroy()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFEType
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFERegister(const char sname[], PetscErrorCode (*function)(PetscFE))
```

Example 3 (unknown):
```unknown
PetscFERegister("my_fe", MyPetscFECreate);
```

Example 4 (unknown):
```unknown
PetscFECreate(MPI_Comm, PetscFE *);
    PetscFESetType(PetscFE, "my_fe");
```

---

## PetscFESetBasisSpace#

**URL:** https://petsc.org/release/manualpages/FE/PetscFESetBasisSpace/

**Contents:**
- PetscFESetBasisSpace#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the PetscSpace used for the approximation of the solution

fem - The PetscFE object

sp - The PetscSpace object

PetscFE, PetscSpace, PetscDualSpace, PetscFECreate(), PetscFESetDualSpace()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFESetBasisSpace(PetscFE fem, PetscSpace sp)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
PetscFECreate()
```

Example 4 (unknown):
```unknown
PetscFESetDualSpace()
```

---

## PetscFESetCeed#

**URL:** https://petsc.org/release/manualpages/FE/PetscFESetCeed/

**Contents:**
- PetscFESetCeed#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the Ceed object to a PetscFE

ceed - The Ceed object

PetscFE, PetscFEGetCeedBasis(), DMGetCeed()

src/dm/dt/fe/interface/ceed/feceed.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFESetCeed(PetscFE fe, Ceed ceed)
```

Example 2 (unknown):
```unknown
PetscFEGetCeedBasis()
```

Example 3 (unknown):
```unknown
DMGetCeed()
```

---

## PetscFESetDualSpace#

**URL:** https://petsc.org/release/manualpages/FE/PetscFESetDualSpace/

**Contents:**
- PetscFESetDualSpace#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the PetscDualSpace used to define the inner product

fem - The PetscFE object

sp - The PetscDualSpace object

PetscFE, PetscSpace, PetscDualSpace, PetscFECreate(), PetscFESetBasisSpace()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpace
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFESetDualSpace(PetscFE fem, PetscDualSpace sp)
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscFESetFaceQuadrature#

**URL:** https://petsc.org/release/manualpages/FE/PetscFESetFaceQuadrature/

**Contents:**
- PetscFESetFaceQuadrature#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the PetscQuadrature used to calculate inner products on faces

fem - The PetscFE object

q - The PetscQuadrature object

PetscFE, PetscSpace, PetscDualSpace, PetscQuadrature, PetscFECreate(), PetscFESetQuadrature()

src/dm/dt/fe/interface/fe.c

src/ts/tutorials/ex53.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscQuadrature
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFESetFaceQuadrature(PetscFE fem, PetscQuadrature q)
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscFESetFromOptions#

**URL:** https://petsc.org/release/manualpages/FE/PetscFESetFromOptions/

**Contents:**
- PetscFESetFromOptions#
- Synopsis#
- Input Parameter#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#

sets parameters in a PetscFE from the options database

fem - the PetscFE object to set options for

-petscfe_num_blocks nblocks - the number of cell blocks to integrate concurrently

-petscfe_num_batches nbatches - the number of cell batches to integrate serially

PetscFE, PetscFEView()

src/dm/dt/fe/interface/fe.c

src/dm/impls/swarm/tutorials/ex1.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFESetFromOptions(PetscFE fem)
```

Example 2 (unknown):
```unknown
PetscFEView()
```

---

## PetscFESetName#

**URL:** https://petsc.org/release/manualpages/FE/PetscFESetName/

**Contents:**
- PetscFESetName#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Names the PetscFE and its subobjects

PetscFECreate(), PetscSpaceCreate(), PetscDualSpaceCreate()

src/dm/dt/fe/interface/fe.c

src/dm/field/tutorials/ex1.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFESetName(PetscFE fe, const char name[])
```

Example 2 (unknown):
```unknown
PetscFECreate()
```

Example 3 (unknown):
```unknown
PetscSpaceCreate()
```

Example 4 (unknown):
```unknown
PetscDualSpaceCreate()
```

---

## PetscFESetNumComponents#

**URL:** https://petsc.org/release/manualpages/FE/PetscFESetNumComponents/

**Contents:**
- PetscFESetNumComponents#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the number of field components in the element

fem - The PetscFE object

comp - The number of field components

PetscFE, PetscFECreate(), PetscFEGetSpatialDimension(), PetscFEGetNumComponents()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFESetNumComponents(PetscFE fem, PetscInt comp)
```

Example 2 (unknown):
```unknown
PetscFECreate()
```

Example 3 (unknown):
```unknown
PetscFEGetSpatialDimension()
```

Example 4 (unknown):
```unknown
PetscFEGetNumComponents()
```

---

## PetscFESetQuadrature#

**URL:** https://petsc.org/release/manualpages/FE/PetscFESetQuadrature/

**Contents:**
- PetscFESetQuadrature#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the PetscQuadrature used to calculate inner products

fem - The PetscFE object

q - The PetscQuadrature object

PetscFE, PetscSpace, PetscDualSpace, PetscQuadrature, PetscFECreate(), PetscFEGetFaceQuadrature()

src/dm/dt/fe/interface/fe.c

src/snes/tutorials/ex23.c src/snes/tutorials/ex64.c src/snes/tutorials/ex62.c src/ts/tutorials/ex53.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscQuadrature
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFESetQuadrature(PetscFE fem, PetscQuadrature q)
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscDualSpace
```

---

## PetscFESetTileSizes#

**URL:** https://petsc.org/release/manualpages/FE/PetscFESetTileSizes/

**Contents:**
- PetscFESetTileSizes#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the tile sizes for evaluation

fem - The PetscFE object

blockSize - The number of elements in a block

numBlocks - The number of blocks in a batch

batchSize - The number of elements in a batch

numBatches - The number of batches in a chunk

PetscFE, PetscFECreate(), PetscFEGetTileSizes()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFESetTileSizes(PetscFE fem, PetscInt blockSize, PetscInt numBlocks, PetscInt batchSize, PetscInt numBatches)
```

Example 2 (unknown):
```unknown
PetscFECreate()
```

Example 3 (unknown):
```unknown
PetscFEGetTileSizes()
```

---

## PetscFESetType#

**URL:** https://petsc.org/release/manualpages/FE/PetscFESetType/

**Contents:**
- PetscFESetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Builds a particular PetscFE

fem - The PetscFE object

name - The kind of FEM space

-petscfe_type (basic|opencl|composite|vector) - Sets the PetscFEType

PetscFEType, PetscFE, PetscFEGetType(), PetscFECreate()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFESetType(PetscFE fem, PetscFEType name)
```

Example 2 (unknown):
```unknown
PetscFEType
```

Example 3 (unknown):
```unknown
PetscFEType
```

Example 4 (unknown):
```unknown
PetscFEGetType()
```

---

## PetscFESetUp#

**URL:** https://petsc.org/release/manualpages/FE/PetscFESetUp/

**Contents:**
- PetscFESetUp#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Construct data structures for the PetscFE after the PetscFEType has been set

fem - the PetscFE object to setup

PetscFE, PetscFEView(), PetscFEDestroy()

src/dm/dt/fe/interface/fe.c

PetscFESetUp_Basic() in src/dm/dt/fe/impls/basic/febasic.c PetscFESetUp_Composite() in src/dm/dt/fe/impls/composite/fecomposite.c PetscFESetUp_Vector() in src/dm/dt/fe/impls/vector/fevector.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFEType
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFESetUp(PetscFE fem)
```

Example 3 (unknown):
```unknown
PetscFEView()
```

Example 4 (unknown):
```unknown
PetscFEDestroy()
```

---

## PetscFEType#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEType/

**Contents:**
- PetscFEType#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#

String with the name of a PETSc finite element space

Currently, the classes are concerned with the implementation of element integration

PetscFESetType(), PetscFE

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef const char *PetscFEType;
#define PETSCFEBASIC     "basic"
#define PETSCFEOPENCL    "opencl"
#define PETSCFECOMPOSITE "composite"
#define PETSCFEVECTOR    "vector"
```

Example 2 (unknown):
```unknown
PetscFESetType()
```

---

## PETSCFEVECTOR#

**URL:** https://petsc.org/release/manualpages/FE/PETSCFEVECTOR/

**Contents:**
- PETSCFEVECTOR#
- See Also#
- Level#
- Location#

“vector” - A vector-valued PetscFE object that is repeated copies of the same underlying finite element.

PetscFE, PetscFEType, PetscFECreate(), PetscFESetType(), PETSCFEBASIC, PetscFECreateVector()

src/dm/dt/fe/impls/vector/fevector.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFEType
```

Example 2 (unknown):
```unknown
PetscFECreate()
```

Example 3 (unknown):
```unknown
PetscFESetType()
```

Example 4 (unknown):
```unknown
PETSCFEBASIC
```

---

## PetscFEViewFromOptions#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEViewFromOptions/

**Contents:**
- PetscFEViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

View a PetscFE based on values in the options database

A - the PetscFE object

obj - Optional object that provides the options prefix, pass NULL to use the options prefix of A

name - command line option name

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

PetscFE, PetscFEView(), PetscObjectViewFromOptions(), PetscFECreate()

src/dm/dt/fe/interface/fe.c

src/ts/tutorials/ex30.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEViewFromOptions(PetscFE A, PeOp PetscObject obj, const char name[])
```

Example 2 (unknown):
```unknown
PetscObjectViewFromOptions()
```

Example 3 (unknown):
```unknown
PetscFEView()
```

Example 4 (unknown):
```unknown
PetscObjectViewFromOptions()
```

---

## PetscFEView#

**URL:** https://petsc.org/release/manualpages/FE/PetscFEView/

**Contents:**
- PetscFEView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

fem - the PetscFE object to view

PetscFE, PetscViewer, PetscFEDestroy(), PetscFEViewFromOptions()

src/dm/dt/fe/interface/fe.c

PetscFEView_Basic() in src/dm/dt/fe/impls/basic/febasic.c PetscFEView_Vector() in src/dm/dt/fe/impls/vector/fevector.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscFEView(PetscFE fem, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscFEDestroy()
```

Example 4 (unknown):
```unknown
PetscFEViewFromOptions()
```

---

## PetscFE#

**URL:** https://petsc.org/release/manualpages/FE/PetscFE/

**Contents:**
- PetscFE#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

PETSc object that manages a finite element space, e.g. the P_1 Lagrange element

PetscFECreate(), PetscSpace, PetscDualSpace, PetscSpaceCreate(), PetscDualSpaceCreate(), PetscFESetType(), PetscFEType

include/petscfetypes.h

src/snes/tutorials/ex71.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex26.c src/snes/tutorials/ex17.c src/snes/tutorials/ex8.c src/snes/tutorials/ex23.c src/snes/tutorials/ex64.c src/snes/tutorials/ex62.c

_p_PetscFE in include/petsc/private/petscfeimpl.h PetscFE_Basic in include/petsc/private/petscfeimpl.h PetscFE_OpenCL in include/petsc/private/petscfeimpl.h PetscFE_Composite in include/petsc/private/petscfeimpl.h PetscFE_Vec in src/dm/dt/fe/impls/vector/fevector.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_PetscFE *PetscFE;
```

Example 2 (unknown):
```unknown
PetscFECreate()
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscSpaceCreate()
```

---

## PetscFE: Finite Element Infrastructure in PETSc#

**URL:** https://petsc.org/release/manual/fe/

**Contents:**
- PetscFE: Finite Element Infrastructure in PETSc#
- Using Pointwise Functions to Specify Finite Element Problems#
- Describing a particular finite element problem to PETSc#
- Assembling finite element residuals and Jacobians#

This chapter introduces the PetscFE class, and related subclasses PetscSpace and PetscDualSpace, which are used to represent finite element discretizations. It details there interaction with the DMPLEX class to assemble functions and operators over computational meshes, and produce optimal solvers by constructing multilevel iterations, for example using PCPATCH. The idea behind these classes is not to encompass all of computational finite elements, but rather to establish an interface and infrastructure that will allow PETSc to leverage the excellent work done in packages such as Firedrake, FEniCS, LibMesh, and Deal.II.

See the paper about Unified Residual Evaluation, which explains the use of pointwise evaluation functions to describe weak forms.

A finite element problem is presented to PETSc in a series of steps. This is both to facilitate automation, and to allow multiple entry points for user code and external packages since so much finite element software already exists. First, we tell the DM, usually a DMPLEX or DMFOREST, that we have a set of finite element fields which we intended to solve for in our problem, using

The second argument is a DMLabel object indicating the support of the field on the mesh, with NULL indicating the entire domain. Once we have a set of fields, we calls

A PetscDS (Discrete System) encodes a set of equations posed in a discrete space, which represents a set of nonlinear continuum equations. The equations can have multiple fields, each field having a different discretization. In addition, different pieces of the domain can have different field combinations and equations.

The DS provides the user a description of the approximation space on any given cell. It also gives pointwise functions representing the equations.

Each field is associated with a DMLabel, marking the cells on which it is supported. Note that a field can be supported on the closure of a cell not in the label due to overlap of the boundary of neighboring cells. The DM then creates a PetscDS for each set of cells with identical approximation spaces. When assembling, the user asks for the space associated with a given cell. DMPLEX uses the labels associated with each PetscDS in the default integration loop.

This divides the computational domain into subdomains, called regions in PETSc, each with a unique set of fields supported on it. These subdomain are identified by labels, and each one has a PetscDS object describing the discrete system on that subdomain. There are query functions to get the set of PetscDS objects for the DM, but it is usually easiest to get the proper PetscDS for a given cell using

Each PetscDS object has a set of fields, each with a PetscFE or PetscFV discretization. This allows it to calculate the size of the local discrete approximation, as well as allocate scratch space for all the associated computations. The final thing needed is to specify the actual equations to be enforced on each region. The PetscDS contains a PetscWeakForm object that holds callback function pointers that define the equations. A simplified, top-level interface through PetscDS allows users to quickly define problems for a single region. For example, in SNES Tutorial ex13, we define the Poisson problem using

where the pointwise functions are

Notice that we set boundary conditions using DMAddBoundary, which will be described later in this chapter. Also we set an exact solution for the field. This can be used to automatically calculate mesh convergence using the PetscConvEst object described later in this chapter.

For more complex cases with multiple regions, we need to use the PetscWeakForm interface directly. The weak form object allows you to set any number of functions for a given field, and also allows functions to be associated with particular subsets of the mesh using labels and label values. We can reproduce the above problem using the SetIndex variants which only set a single function at the specified index, rather than a list of functions. We use a NULL label and value, meaning that the entire domain is used.

In SNES Tutorial ex23, we define the Poisson problem over the entire domain, but in the top half we also define a pressure. The entire problem can be specified as follows

In the PyLith software we use this capability to combine bulk elasticity with a fault constitutive model integrated over the embedded manifolds corresponding to earthquake faults.

Once the pointwise functions are set in each PetscDS, mesh traversals can be automatically determined from the DMLabel and value specifications in the keys. This default traversal strategy can be activated by attaching the DM and default callbacks to a solver

PetscDT: Discretization Technology in PETSc

Additional Information

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpace
```

Example 2 (unknown):
```unknown
DMAddField(dm, NULL, presDisc);
DMAddField(dm, channelLabel, velDisc);
```

Example 3 (unknown):
```unknown
DMCreateDS(dm);
```

Example 4 (unknown):
```unknown
DMGetCellDS(dm, cell, &ds, NULL);
```

---

## PetscFormKeySort#

**URL:** https://petsc.org/release/manualpages/DT/PetscFormKeySort/

**Contents:**
- PetscFormKeySort#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sorts an array of PetscFormKey in place in increasing order.

arr - array of PetscFormKey

PetscFormKey, PetscIntSortSemiOrdered(), PetscSortInt()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFormKey
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscFormKeySort(PetscInt n, PetscFormKey arr[])
```

Example 3 (unknown):
```unknown
PetscFormKey
```

Example 4 (unknown):
```unknown
PetscFormKey
```

---

## PetscFormKey#

**URL:** https://petsc.org/release/manualpages/DT/PetscFormKey/

**Contents:**
- PetscFormKey#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#

This key indicates how to use a set of pointwise functions defining part of a system of equations

The subdomain on which to integrate is specified by (label, value), the test function field by (field), and the piece of the equation by (part). For example, LHS = 0 and RHS = 1 in IMEX methods. More pieces can be present for operator splitting methods.

This is a struct, not a PetscObject

DMPlexSNESComputeResidualFEM(), DMPlexSNESComputeJacobianFEM(), DMPlexSNESComputeBoundaryFEM()

include/petscdstypes.h

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (sql):
```sql
typedef struct {
  DMLabel  label; /* The (label, value) select a subdomain */
  PetscInt value;
  PetscInt field; /* Selects the field for the test function */
  PetscInt part;  /* Selects the equation part. For example, LHS = 0 and RHS = 1 in IMEX methods. More pieces can be present for operator splitting methods. */
} PetscFormKey;
```

Example 2 (unknown):
```unknown
PetscObject
```

Example 3 (unknown):
```unknown
DMPlexSNESComputeResidualFEM()
```

Example 4 (unknown):
```unknown
DMPlexSNESComputeJacobianFEM()
```

---

## PetscFVCellGeom#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVCellGeom/

**Contents:**
- PetscFVCellGeom#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#

Data structure (C struct) for storing information about cell geometry for a finite volume method.

Note: The components are

PetscFVFaceGeom, DMPlexComputeGeometryFVM()

include/petscfvtypes.h

src/ts/tutorials/ex11.c src/ts/tutorials/ex18.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef struct {
  PetscReal centroid[3];
  PetscReal volume;
} PetscFVCellGeom;
```

Example 2 (unknown):
```unknown
PetscReal   centroid[3] - The cell centroid
   PetscReal   volume      - The cell volume
```

Example 3 (unknown):
```unknown
PetscFVFaceGeom
```

Example 4 (unknown):
```unknown
DMPlexComputeGeometryFVM()
```

---

## PetscFVClone#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVClone/

**Contents:**
- PetscFVClone#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Create a shallow copy of a PetscFV object that just references the internal objects.

fv - The initial PetscFV

fvNew - A clone of the PetscFV

This is typically used to change the number of components.

PetscFV, PetscFVType, PetscFVCreate(), PetscFVSetType()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVClone(PetscFV fv, PetscFV *fvNew)
```

Example 2 (unknown):
```unknown
PetscFVType
```

Example 3 (unknown):
```unknown
PetscFVCreate()
```

Example 4 (unknown):
```unknown
PetscFVSetType()
```

---

## PetscFVComputeGradient#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVComputeGradient/

**Contents:**
- PetscFVComputeGradient#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Compute the gradient reconstruction matrix for a given cell

fvm - The PetscFV object

numFaces - The number of cell faces which are not constrained

dx - The vector from the cell centroid to the neighboring cell centroid for each face

PetscFV, PetscFVCreate()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVComputeGradient(PetscFV fvm, PetscInt numFaces, PetscScalar dx[], PetscScalar grad[])
```

Example 2 (unknown):
```unknown
PetscFVCreate()
```

---

## PetscFVCreateDualSpace#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVCreateDualSpace/

**Contents:**
- PetscFVCreateDualSpace#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Creates a PetscDualSpace appropriate for the PetscFV

fvm - The PetscFV object

ct - The DMPolytopeType for the cell

PetscFVGetDualSpace(), PetscFVSetDualSpace(), PetscDualSpace, PetscFV, PetscFVCreate()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpace
```

Example 2 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVCreateDualSpace(PetscFV fvm, DMPolytopeType ct)
```

Example 3 (unknown):
```unknown
DMPolytopeType
```

Example 4 (unknown):
```unknown
PetscFVGetDualSpace()
```

---

## PetscFVCreateTabulation#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVCreateTabulation/

**Contents:**
- PetscFVCreateTabulation#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Tabulates the basis functions, and perhaps derivatives, at the points provided.

fvm - The PetscFV object

nrepl - The number of replicas

npoints - The number of tabulation points in a replica

points - The tabulation point coordinates

K - The order of derivative to tabulate

T - The basis function values and derivative at tabulation points

PetscFV, PetscTabulation, PetscFECreateTabulation(), PetscTabulationDestroy(), PetscFEGetCellTabulation()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVCreateTabulation(PetscFV fvm, PetscInt nrepl, PetscInt npoints, const PetscReal points[], PetscInt K, PetscTabulation *T)
```

Example 2 (perl):
```perl
T->T[0] = B[(p*pdim + i)*Nc + c] is the value at point p for basis function i and component c
  T->T[1] = D[((p*pdim + i)*Nc + c)*dim + d] is the derivative value at point p for basis function i, component c, in direction d
  T->T[2] = H[(((p*pdim + i)*Nc + c)*dim + d)*dim + e] is the value at point p for basis function i, component c, in directions d and e
```

Example 3 (unknown):
```unknown
PetscTabulation
```

Example 4 (unknown):
```unknown
PetscFECreateTabulation()
```

---

## PetscFVCreate#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVCreate/

**Contents:**
- PetscFVCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Creates an empty PetscFV object. The type can then be set with PetscFVSetType().

comm - The communicator for the PetscFV object

fvm - The PetscFV object

PetscFVSetUp(), PetscFVSetType(), PETSCFVUPWIND, PetscFVDestroy()

src/dm/dt/fv/interface/fv.c

src/ts/tutorials/ex52.c src/ts/tutorials/ex11.c src/ts/tutorials/ex18.c src/dm/impls/plex/tutorials/ex3f90.F90

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFVSetType()
```

Example 2 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVCreate(MPI_Comm comm, PetscFV *fvm)
```

Example 3 (unknown):
```unknown
PetscFVSetUp()
```

Example 4 (unknown):
```unknown
PetscFVSetType()
```

---

## PetscFVDestroy#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVDestroy/

**Contents:**
- PetscFVDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#

Destroys a PetscFV object

fvm - the PetscFV object to destroy

PetscFV, PetscFVCreate(), PetscFVView()

src/dm/dt/fv/interface/fv.c

src/ts/tutorials/ex52.c src/ts/tutorials/ex11.c src/ts/tutorials/ex18.c src/dm/impls/plex/tutorials/ex3f90.F90

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVDestroy(PetscFV *fvm)
```

Example 2 (unknown):
```unknown
PetscFVCreate()
```

Example 3 (unknown):
```unknown
PetscFVView()
```

---

## PetscFVFaceGeom#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVFaceGeom/

**Contents:**
- PetscFVFaceGeom#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Data structure (C struct) for storing information about face geometry for a finite volume method.

PetscFVCellGeom, DMPlexComputeGeometryFVM()

include/petscfvtypes.h

src/ts/tutorials/ex52.c src/ts/tutorials/ex11.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef struct {
  PetscReal   normal[3];   /* Area-scaled normals */
  PetscReal   centroid[3]; /* Location of centroid (quadrature point) */
  PetscScalar grad[2][3];  /* Face contribution to gradient in left and right cell */
} PetscFVFaceGeom;
```

Example 2 (unknown):
```unknown
PetscReal   normal[3]   - Area-scaled normals
  PetscReal   centroid[3] - Location of centroid (quadrature point)
  PetscScalar grad[2][3]  - Face contribution to gradient in left and right cell
```

Example 3 (unknown):
```unknown
PetscFVCellGeom
```

Example 4 (unknown):
```unknown
DMPlexComputeGeometryFVM()
```

---

## PetscFVGetCeedBasis#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVGetCeedBasis/

**Contents:**
- PetscFVGetCeedBasis#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Get the Ceed object mirroring this PetscFV

basis - The CeedBasis

This is a borrowed reference, so it is not freed.

PetscFV, PetscFVSetCeed(), DMGetCeed()

src/dm/dt/fv/interface/ceed/fvceed.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVGetCeedBasis(PetscFV fv, CeedBasis *basis)
```

Example 2 (unknown):
```unknown
PetscFVSetCeed()
```

Example 3 (unknown):
```unknown
DMGetCeed()
```

---

## PetscFVGetCellTabulation#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVGetCellTabulation/

**Contents:**
- PetscFVGetCellTabulation#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Returns the tabulation of the basis functions at the quadrature points

fvm - The PetscFV object

T - The basis function values and derivatives at quadrature points

PetscFV, PetscTabulation, PetscFEGetCellTabulation(), PetscFVCreateTabulation(), PetscFVGetQuadrature(), PetscQuadratureGetData()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVGetCellTabulation(PetscFV fvm, PetscTabulation *T)
```

Example 2 (perl):
```perl
T->T[0] = B[(p*pdim + i)*Nc + c] is the value at point p for basis function i and component c
  T->T[1] = D[((p*pdim + i)*Nc + c)*dim + d] is the derivative value at point p for basis function i, component c, in direction d
  T->T[2] = H[(((p*pdim + i)*Nc + c)*dim + d)*dim + e] is the value at point p for basis function i, component c, in directions d and e
```

Example 3 (unknown):
```unknown
PetscTabulation
```

Example 4 (unknown):
```unknown
PetscFEGetCellTabulation()
```

---

## PetscFVGetComponentName#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVGetComponentName/

**Contents:**
- PetscFVGetComponentName#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the name of a component (used in output and viewing) in a PetscFV

fvm - the PetscFV object

comp - the component number

name - the component name

PetscFV, PetscFVSetComponentName()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVGetComponentName(PetscFV fvm, PetscInt comp, const char *name[])
```

Example 2 (unknown):
```unknown
PetscFVSetComponentName()
```

---

## PetscFVGetComputeGradients#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVGetComputeGradients/

**Contents:**
- PetscFVGetComputeGradients#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Return flag for computation of cell gradients on a PetscFV

fvm - the PetscFV object

computeGradients - Flag to compute cell gradients

PetscFV, PetscFVSetComputeGradients()

src/dm/dt/fv/interface/fv.c

src/ts/tutorials/ex11.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVGetComputeGradients(PetscFV fvm, PetscBool *computeGradients)
```

Example 2 (unknown):
```unknown
PetscFVSetComputeGradients()
```

---

## PetscFVGetDualSpace#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVGetDualSpace/

**Contents:**
- PetscFVGetDualSpace#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Developer Notes#
- See Also#
- Level#
- Location#

Returns the PetscDualSpace used to define the inner product on a PetscFV

fvm - The PetscFV object

sp - The PetscDualSpace object

There is overlap between the methods of PetscFE and PetscFV, they should probably share a common parent class

PetscFVSetDualSpace(), PetscFVCreateDualSpace(), PetscDualSpace, PetscFV, PetscFVCreate()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpace
```

Example 2 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVGetDualSpace(PetscFV fvm, PetscDualSpace *sp)
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscFVSetDualSpace()
```

---

## PetscFVGetLimiter#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVGetLimiter/

**Contents:**
- PetscFVGetLimiter#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Get the PetscLimiter object from the PetscFV

fvm - the PetscFV object

lim - The PetscLimiter

PetscFV, PetscLimiter, PetscFVSetLimiter()

src/dm/dt/fv/interface/fv.c

src/ts/tutorials/ex11.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLimiter
```

Example 2 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVGetLimiter(PetscFV fvm, PetscLimiter *lim)
```

Example 3 (unknown):
```unknown
PetscLimiter
```

Example 4 (unknown):
```unknown
PetscLimiter
```

---

## PetscFVGetNumComponents#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVGetNumComponents/

**Contents:**
- PetscFVGetNumComponents#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the number of field components in a PetscFV

fvm - the PetscFV object

comp - The number of components

PetscFV, PetscFVSetNumComponents(), PetscFVSetComponentName()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVGetNumComponents(PetscFV fvm, PetscInt *comp)
```

Example 2 (unknown):
```unknown
PetscFVSetNumComponents()
```

Example 3 (unknown):
```unknown
PetscFVSetComponentName()
```

---

## PetscFVGetQuadrature#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVGetQuadrature/

**Contents:**
- PetscFVGetQuadrature#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the PetscQuadrature from a PetscFV

fvm - the PetscFV object

q - The PetscQuadrature

PetscQuadrature, PetscFV, PetscFVSetQuadrature()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscQuadrature
```

Example 2 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVGetQuadrature(PetscFV fvm, PetscQuadrature *q)
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscQuadrature
```

---

## PetscFVGetSpatialDimension#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVGetSpatialDimension/

**Contents:**
- PetscFVGetSpatialDimension#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the spatial dimension of a PetscFV

fvm - the PetscFV object

dim - The spatial dimension

PetscFV, PetscFVSetSpatialDimension()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVGetSpatialDimension(PetscFV fvm, PetscInt *dim)
```

Example 2 (unknown):
```unknown
PetscFVSetSpatialDimension()
```

---

## PetscFVGetType#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVGetType/

**Contents:**
- PetscFVGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the PetscFVType (as a string) from a PetscFV.

name - The PetscFVType name

PetscFV, PetscFVType, PetscFVSetType(), PetscFVCreate()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFVType
```

Example 2 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVGetType(PetscFV fvm, PetscFVType *name)
```

Example 3 (unknown):
```unknown
PetscFVType
```

Example 4 (unknown):
```unknown
PetscFVType
```

---

## PetscFVIntegrateRHSFunction#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVIntegrateRHSFunction/

**Contents:**
- PetscFVIntegrateRHSFunction#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Produce the cell residual vector for a chunk of elements by quadrature integration

fvm - The PetscFV object for the field being integrated

prob - The PetscDS specifying the discretizations and continuum functions

field - The field being integrated

Nf - The number of faces in the chunk

fgeom - The face geometry for each face in the chunk

neighborVol - The volume for each pair of cells in the chunk

uL - The state from the cell on the left

uR - The state from the cell on the right

fluxL - the left fluxes for each face

fluxR - the right fluxes for each face

PetscFV, PetscDS, PetscFVFaceGeom, PetscFVCreate()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVIntegrateRHSFunction(PetscFV fvm, PetscDS prob, PetscInt field, PetscInt Nf, PetscFVFaceGeom *fgeom, PetscReal *neighborVol, PetscScalar uL[], PetscScalar uR[], PetscScalar fluxL[], PetscScalar fluxR[])
```

Example 2 (unknown):
```unknown
PetscFVFaceGeom
```

Example 3 (unknown):
```unknown
PetscFVCreate()
```

---

## PetscFVLeastSquaresSetMaxFaces#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVLeastSquaresSetMaxFaces/

**Contents:**
- PetscFVLeastSquaresSetMaxFaces#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the maximum number of cell faces for gradient reconstruction

fvm - The PetscFV object

maxFaces - The maximum number of cell faces

PetscFV, PetscFVCreate(), PETSCFVLEASTSQUARES, PetscFVComputeGradient()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVLeastSquaresSetMaxFaces(PetscFV fvm, PetscInt maxFaces)
```

Example 2 (unknown):
```unknown
PetscFVCreate()
```

Example 3 (unknown):
```unknown
PETSCFVLEASTSQUARES
```

Example 4 (unknown):
```unknown
PetscFVComputeGradient()
```

---

## PETSCFVLEASTSQUARES#

**URL:** https://petsc.org/release/manualpages/FV/PETSCFVLEASTSQUARES/

**Contents:**
- PETSCFVLEASTSQUARES#
- See Also#
- Level#
- Location#

“leastsquares” - A PetscFV implementation

PetscFV, PetscFVType, PetscFVCreate(), PetscFVSetType()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFVType
```

Example 2 (unknown):
```unknown
PetscFVCreate()
```

Example 3 (unknown):
```unknown
PetscFVSetType()
```

---

## PetscFVRefine#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVRefine/

**Contents:**
- PetscFVRefine#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Create a “refined” PetscFV object that refines the reference cell into smaller copies.

fv - The initial PetscFV

fvRef - The refined PetscFV

This is typically used to generate a preconditioner for a high order method from a lower order method on a refined mesh having the same number of dofs (but more sparsity). It is also used to create an interpolation between regularly refined meshes.

PetscFV, PetscFVType, PetscFVCreate(), PetscFVSetType()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVRefine(PetscFV fv, PetscFV *fvRef)
```

Example 2 (unknown):
```unknown
PetscFVType
```

Example 3 (unknown):
```unknown
PetscFVCreate()
```

Example 4 (unknown):
```unknown
PetscFVSetType()
```

---

## PetscFVRegister#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVRegister/

**Contents:**
- PetscFVRegister#
- Synopsis#
- Input Parameters#
- Example Usage#
- Note#
- See Also#
- Level#
- Location#

Adds a new PetscFV implementation

Not Collective, No Fortran Support

sname - The name of a new user-defined creation routine

function - The creation routine itself

Then, your PetscFV type can be chosen with the procedural interface via

or at runtime via the option

PetscFVRegister() may be called multiple times to add several user-defined PetscFVs

PetscFV, PetscFVType, PetscFVRegisterAll(), PetscFVRegisterDestroy()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVRegister(const char sname[], PetscErrorCode (*function)(PetscFV))
```

Example 2 (unknown):
```unknown
PetscFVRegister("my_fv", MyPetscFVCreate);
```

Example 3 (unknown):
```unknown
PetscFVCreate(MPI_Comm, PetscFV *);
    PetscFVSetType(PetscFV, "my_fv");
```

Example 4 (unknown):
```unknown
-petscfv_type my_fv
```

---

## PetscFVSetCeed#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVSetCeed/

**Contents:**
- PetscFVSetCeed#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the Ceed object to a PetscFV

ceed - The Ceed object

PetscFV, PetscFVGetCeedBasis(), DMGetCeed()

src/dm/dt/fv/interface/ceed/fvceed.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVSetCeed(PetscFV fv, Ceed ceed)
```

Example 2 (unknown):
```unknown
PetscFVGetCeedBasis()
```

Example 3 (unknown):
```unknown
DMGetCeed()
```

---

## PetscFVSetComponentName#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVSetComponentName/

**Contents:**
- PetscFVSetComponentName#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the name of a component (used in output and viewing) in a PetscFV

fvm - the PetscFV object

comp - the component number

name - the component name

PetscFV, PetscFVGetComponentName()

src/dm/dt/fv/interface/fv.c

src/ts/tutorials/ex11.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVSetComponentName(PetscFV fvm, PetscInt comp, const char *name)
```

Example 2 (unknown):
```unknown
PetscFVGetComponentName()
```

---

## PetscFVSetComputeGradients#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVSetComputeGradients/

**Contents:**
- PetscFVSetComputeGradients#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Toggle computation of cell gradients on a PetscFV

fvm - the PetscFV object

computeGradients - Flag to compute cell gradients

PetscFV, PetscFVGetComputeGradients()

src/dm/dt/fv/interface/fv.c

src/ts/tutorials/ex11.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVSetComputeGradients(PetscFV fvm, PetscBool computeGradients)
```

Example 2 (unknown):
```unknown
PetscFVGetComputeGradients()
```

---

## PetscFVSetDualSpace#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVSetDualSpace/

**Contents:**
- PetscFVSetDualSpace#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the PetscDualSpace used to define the inner product

fvm - The PetscFV object

sp - The PetscDualSpace object

A simple dual space is provided automatically, and the user typically will not need to override it.

PetscFVGetDualSpace(), PetscFVCreateDualSpace(), PetscDualSpace, PetscFV, PetscFVCreate()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDualSpace
```

Example 2 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVSetDualSpace(PetscFV fvm, PetscDualSpace sp)
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscFVGetDualSpace()
```

---

## PetscFVSetFromOptions#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVSetFromOptions/

**Contents:**
- PetscFVSetFromOptions#
- Synopsis#
- Input Parameter#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

sets parameters in a PetscFV from the options database

fvm - the PetscFV object to set options for

-petscfv_compute_gradients (true|false) - Determines whether cell gradients are calculated

PetscFV, PetscFVView()

src/dm/dt/fv/interface/fv.c

src/ts/tutorials/ex11.c src/ts/tutorials/ex18.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVSetFromOptions(PetscFV fvm)
```

Example 2 (unknown):
```unknown
PetscFVView()
```

---

## PetscFVSetLimiter#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVSetLimiter/

**Contents:**
- PetscFVSetLimiter#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the PetscLimiter to the PetscFV

fvm - the PetscFV object

lim - The PetscLimiter

PetscFV, PetscLimiter, PetscFVGetLimiter()

src/dm/dt/fv/interface/fv.c

src/ts/tutorials/ex11.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLimiter
```

Example 2 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVSetLimiter(PetscFV fvm, PetscLimiter lim)
```

Example 3 (unknown):
```unknown
PetscLimiter
```

Example 4 (unknown):
```unknown
PetscLimiter
```

---

## PetscFVSetNumComponents#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVSetNumComponents/

**Contents:**
- PetscFVSetNumComponents#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the number of field components in a PetscFV

fvm - the PetscFV object

comp - The number of components

PetscFV, PetscFVGetNumComponents()

src/dm/dt/fv/interface/fv.c

src/ts/tutorials/ex11.c src/ts/tutorials/ex18.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVSetNumComponents(PetscFV fvm, PetscInt comp)
```

Example 2 (unknown):
```unknown
PetscFVGetNumComponents()
```

---

## PetscFVSetQuadrature#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVSetQuadrature/

**Contents:**
- PetscFVSetQuadrature#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the PetscQuadrature object for a PetscFV

fvm - the PetscFV object

q - The PetscQuadrature

PetscQuadrature, PetscFV, PetscFVGetQuadrature()

src/dm/dt/fv/interface/fv.c

src/ts/tutorials/ex18.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscQuadrature
```

Example 2 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVSetQuadrature(PetscFV fvm, PetscQuadrature q)
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscQuadrature
```

---

## PetscFVSetSpatialDimension#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVSetSpatialDimension/

**Contents:**
- PetscFVSetSpatialDimension#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the spatial dimension of a PetscFV

fvm - the PetscFV object

dim - The spatial dimension

PetscFV, PetscFVGetSpatialDimension()

src/dm/dt/fv/interface/fv.c

src/ts/tutorials/ex11.c src/ts/tutorials/ex18.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVSetSpatialDimension(PetscFV fvm, PetscInt dim)
```

Example 2 (unknown):
```unknown
PetscFVGetSpatialDimension()
```

---

## PetscFVSetType#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVSetType/

**Contents:**
- PetscFVSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

Builds a particular PetscFV

fvm - The PetscFV object

name - The type of FVM space

-petscfv_type type - Sets the PetscFVType; use -help for a list of available types

PetscFV, PetscFVType, PetscFVGetType(), PetscFVCreate()

src/dm/dt/fv/interface/fv.c

src/ts/tutorials/ex52.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVSetType(PetscFV fvm, PetscFVType name)
```

Example 2 (unknown):
```unknown
PetscFVType
```

Example 3 (unknown):
```unknown
PetscFVType
```

Example 4 (unknown):
```unknown
PetscFVGetType()
```

---

## PetscFVSetUp#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVSetUp/

**Contents:**
- PetscFVSetUp#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#

Setup the data structures for the PetscFV based on the PetscFVType provided by PetscFVSetType()

fvm - the PetscFV object to setup

PetscFV, PetscFVView(), PetscFVDestroy()

src/dm/dt/fv/interface/fv.c

src/dm/impls/plex/tutorials/ex3f90.F90

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFVType
```

Example 2 (unknown):
```unknown
PetscFVSetType()
```

Example 3 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVSetUp(PetscFV fvm)
```

Example 4 (unknown):
```unknown
PetscFVView()
```

---

## PetscFVType#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVType/

**Contents:**
- PetscFVType#
- Synopsis#
- See Also#
- Level#
- Location#

String with the name of a PETSc finite volume discretization

PetscFVSetType(), PetscFV

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef const char *PetscFVType;
#define PETSCFVUPWIND       "upwind"
#define PETSCFVLEASTSQUARES "leastsquares"
```

Example 2 (unknown):
```unknown
PetscFVSetType()
```

---

## PETSCFVUPWIND#

**URL:** https://petsc.org/release/manualpages/FV/PETSCFVUPWIND/

**Contents:**
- PETSCFVUPWIND#
- See Also#
- Level#
- Location#
- Examples#

“upwind” - A PetscFV implementation

PetscFV, PetscFVType, PetscFVCreate(), PetscFVSetType()

src/dm/dt/fv/interface/fv.c

src/ts/tutorials/ex52.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFVType
```

Example 2 (unknown):
```unknown
PetscFVCreate()
```

Example 3 (unknown):
```unknown
PetscFVSetType()
```

---

## PetscFVViewFromOptions#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVViewFromOptions/

**Contents:**
- PetscFVViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

View a PetscFV based on values in the options database

A - the PetscFV object

obj - Optional object that provides the options prefix

name - command line option name

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

PetscFV, PetscFVView(), PetscObjectViewFromOptions(), PetscFVCreate()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVViewFromOptions(PetscFV A, PetscObject obj, const char name[])
```

Example 2 (unknown):
```unknown
PetscObjectViewFromOptions()
```

Example 3 (unknown):
```unknown
PetscFVView()
```

Example 4 (unknown):
```unknown
PetscObjectViewFromOptions()
```

---

## PetscFVView#

**URL:** https://petsc.org/release/manualpages/FV/PetscFVView/

**Contents:**
- PetscFVView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

fvm - the PetscFV object to view

PetscFV, PetscViewer, PetscFVDestroy()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscFVView(PetscFV fvm, PetscViewer v)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscFVDestroy()
```

---

## PetscFV#

**URL:** https://petsc.org/release/manualpages/FV/PetscFV/

**Contents:**
- PetscFV#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

PETSc object that manages a finite volume discretization

PetscFVCreate(), PetscFVSetType(), PetscFVType

include/petscfvtypes.h

src/ts/tutorials/ex52.c src/ts/tutorials/ex11.c src/ts/tutorials/ex18.c src/dm/impls/plex/tutorials/ex3f90.F90

_p_PetscFV in include/petsc/private/petscfvimpl.h PetscFV_Upwind in include/petsc/private/petscfvimpl.h PetscFV_LeastSquares in include/petsc/private/petscfvimpl.h

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_PetscFV *PetscFV;
```

Example 2 (unknown):
```unknown
PetscFVCreate()
```

Example 3 (unknown):
```unknown
PetscFVSetType()
```

Example 4 (unknown):
```unknown
PetscFVType
```

---

## PetscGaussLobattoLegendreCreateType#

**URL:** https://petsc.org/release/manualpages/DT/PetscGaussLobattoLegendreCreateType/

**Contents:**
- PetscGaussLobattoLegendreCreateType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#
- Examples#

algorithm used to compute the Gauss-Lobatto-Legendre nodes and weights

PETSCGAUSSLOBATTOLEGENDRE_VIA_LINEAR_ALGEBRA - compute the nodes via linear algebra

PETSCGAUSSLOBATTOLEGENDRE_VIA_NEWTON - compute the nodes by solving a nonlinear equation with Newton’s method

src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/tutorials/ex50.c src/ksp/ksp/tutorials/ex68.c src/ksp/ksp/tutorials/ex69.c src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  PETSCGAUSSLOBATTOLEGENDRE_VIA_LINEAR_ALGEBRA,
  PETSCGAUSSLOBATTOLEGENDRE_VIA_NEWTON
} PetscGaussLobattoLegendreCreateType;
```

Example 2 (unknown):
```unknown
PETSCGAUSSLOBATTOLEGENDRE_VIA_LINEAR_ALGEBRA
```

Example 3 (unknown):
```unknown
PETSCGAUSSLOBATTOLEGENDRE_VIA_NEWTON
```

Example 4 (unknown):
```unknown
PetscQuadrature
```

---

## PetscGaussLobattoLegendreElementAdvectionCreate#

**URL:** https://petsc.org/release/manualpages/DT/PetscGaussLobattoLegendreElementAdvectionCreate/

**Contents:**
- PetscGaussLobattoLegendreElementAdvectionCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

computes the advection operator for a single 1d GLL element

n - the number of GLL nodes

nodes - the GLL nodes, of length n

weights - the GLL weights, of length n

AA - the stiffness element, of dimension n by n

Destroy this with PetscGaussLobattoLegendreElementAdvectionDestroy()

This is the same as the Gradient operator multiplied by the diagonal mass matrix

You can access entries in this array with AA[i][j] but in memory it is stored in contiguous memory, row-oriented

PetscDTGaussLobattoLegendreQuadrature(), PetscGaussLobattoLegendreElementLaplacianCreate(), PetscGaussLobattoLegendreElementAdvectionDestroy()

src/dm/dt/interface/dt.c

src/ts/tutorials/ex50.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscGaussLobattoLegendreElementAdvectionCreate(PetscInt n, PetscReal nodes[], PetscReal weights[], PetscReal ***AA)
```

Example 2 (unknown):
```unknown
PetscGaussLobattoLegendreElementAdvectionDestroy()
```

Example 3 (unknown):
```unknown
PetscDTGaussLobattoLegendreQuadrature()
```

Example 4 (unknown):
```unknown
PetscGaussLobattoLegendreElementLaplacianCreate()
```

---

## PetscGaussLobattoLegendreElementAdvectionDestroy#

**URL:** https://petsc.org/release/manualpages/DT/PetscGaussLobattoLegendreElementAdvectionDestroy/

**Contents:**
- PetscGaussLobattoLegendreElementAdvectionDestroy#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

frees the advection stiffness for a single 1d GLL element created with PetscGaussLobattoLegendreElementAdvectionCreate()

n - the number of GLL nodes

nodes - the GLL nodes, ignored

weights - the GLL weights, ignored

AA - advection obtained with PetscGaussLobattoLegendreElementAdvectionCreate()

PetscDTGaussLobattoLegendreQuadrature(), PetscGaussLobattoLegendreElementAdvectionCreate()

src/dm/dt/interface/dt.c

src/ts/tutorials/ex50.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscGaussLobattoLegendreElementAdvectionCreate()
```

Example 2 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscGaussLobattoLegendreElementAdvectionDestroy(PetscInt n, PetscReal nodes[], PetscReal weights[], PetscReal ***AA)
```

Example 3 (unknown):
```unknown
PetscGaussLobattoLegendreElementAdvectionCreate()
```

Example 4 (unknown):
```unknown
PetscDTGaussLobattoLegendreQuadrature()
```

---

## PetscGaussLobattoLegendreElementGradientCreate#

**URL:** https://petsc.org/release/manualpages/DT/PetscGaussLobattoLegendreElementGradientCreate/

**Contents:**
- PetscGaussLobattoLegendreElementGradientCreate#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

computes the gradient for a single 1d GLL element

n - the number of GLL nodes

nodes - the GLL nodes, of length n

weights - the GLL weights, of length n

AA - the stiffness element, of dimension n by n

AAT - the transpose of AA (pass in NULL if you do not need this array), of dimension n by n

Destroy this with PetscGaussLobattoLegendreElementGradientDestroy()

You can access entries in these arrays with AA[i][j] but in memory it is stored in contiguous memory, row-oriented

PetscDTGaussLobattoLegendreQuadrature(), PetscGaussLobattoLegendreElementLaplacianDestroy(), PetscGaussLobattoLegendreElementGradientDestroy()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscGaussLobattoLegendreElementGradientCreate(PetscInt n, PetscReal nodes[], PetscReal weights[], PetscReal ***AA, PetscReal ***AAT)
```

Example 2 (unknown):
```unknown
PetscGaussLobattoLegendreElementGradientDestroy()
```

Example 3 (unknown):
```unknown
PetscDTGaussLobattoLegendreQuadrature()
```

Example 4 (unknown):
```unknown
PetscGaussLobattoLegendreElementLaplacianDestroy()
```

---

## PetscGaussLobattoLegendreElementGradientDestroy#

**URL:** https://petsc.org/release/manualpages/DT/PetscGaussLobattoLegendreElementGradientDestroy/

**Contents:**
- PetscGaussLobattoLegendreElementGradientDestroy#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

frees the gradient for a single 1d GLL element obtained with PetscGaussLobattoLegendreElementGradientCreate()

n - the number of GLL nodes

nodes - the GLL nodes, ignored

weights - the GLL weights, ignored

AA - the stiffness element obtained with PetscGaussLobattoLegendreElementGradientCreate()

AAT - the transpose of the element obtained with PetscGaussLobattoLegendreElementGradientCreate()

PetscDTGaussLobattoLegendreQuadrature(), PetscGaussLobattoLegendreElementLaplacianCreate(), PetscGaussLobattoLegendreElementAdvectionCreate()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscGaussLobattoLegendreElementGradientCreate()
```

Example 2 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscGaussLobattoLegendreElementGradientDestroy(PetscInt n, PetscReal nodes[], PetscReal weights[], PetscReal ***AA, PetscReal ***AAT)
```

Example 3 (unknown):
```unknown
PetscGaussLobattoLegendreElementGradientCreate()
```

Example 4 (unknown):
```unknown
PetscGaussLobattoLegendreElementGradientCreate()
```

---

## PetscGaussLobattoLegendreElementLaplacianCreate#

**URL:** https://petsc.org/release/manualpages/DT/PetscGaussLobattoLegendreElementLaplacianCreate/

**Contents:**
- PetscGaussLobattoLegendreElementLaplacianCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

computes the Laplacian for a single 1d GLL element

n - the number of GLL nodes

nodes - the GLL nodes, of length n

weights - the GLL weights, of length n

AA - the stiffness element, of size n by n

Destroy this with PetscGaussLobattoLegendreElementLaplacianDestroy()

You can access entries in this array with AA[i][j] but in memory it is stored in contiguous memory, row-oriented (the array is symmetric)

PetscDTGaussLobattoLegendreQuadrature(), PetscGaussLobattoLegendreElementLaplacianDestroy()

src/dm/dt/interface/dt.c

src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/tutorials/ex50.c src/ksp/ksp/tutorials/ex68.c src/ksp/ksp/tutorials/ex69.c src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscGaussLobattoLegendreElementLaplacianCreate(PetscInt n, PetscReal nodes[], PetscReal weights[], PetscReal ***AA)
```

Example 2 (unknown):
```unknown
PetscGaussLobattoLegendreElementLaplacianDestroy()
```

Example 3 (unknown):
```unknown
PetscDTGaussLobattoLegendreQuadrature()
```

Example 4 (unknown):
```unknown
PetscGaussLobattoLegendreElementLaplacianDestroy()
```

---

## PetscGaussLobattoLegendreElementLaplacianDestroy#

**URL:** https://petsc.org/release/manualpages/DT/PetscGaussLobattoLegendreElementLaplacianDestroy/

**Contents:**
- PetscGaussLobattoLegendreElementLaplacianDestroy#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

frees the Laplacian for a single 1d GLL element created with PetscGaussLobattoLegendreElementLaplacianCreate()

n - the number of GLL nodes

nodes - the GLL nodes, ignored

weights - the GLL weightss, ignored

AA - the stiffness element from PetscGaussLobattoLegendreElementLaplacianCreate()

PetscDTGaussLobattoLegendreQuadrature(), PetscGaussLobattoLegendreElementLaplacianCreate()

src/dm/dt/interface/dt.c

src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/ts/tutorials/ex50.c src/ksp/ksp/tutorials/ex68.c src/ksp/ksp/tutorials/ex69.c src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscGaussLobattoLegendreElementLaplacianCreate()
```

Example 2 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscGaussLobattoLegendreElementLaplacianDestroy(PetscInt n, PetscReal nodes[], PetscReal weights[], PetscReal ***AA)
```

Example 3 (unknown):
```unknown
PetscGaussLobattoLegendreElementLaplacianCreate()
```

Example 4 (unknown):
```unknown
PetscDTGaussLobattoLegendreQuadrature()
```

---

## PetscGaussLobattoLegendreElementMassCreate#

**URL:** https://petsc.org/release/manualpages/DT/PetscGaussLobattoLegendreElementMassCreate/

**Contents:**
- PetscGaussLobattoLegendreElementMassCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Build the elemental mass matrix for a single 1D Gauss-Lobatto-Legendre (GLL) spectral element

Not Collective; No Fortran Support

n - number of GLL nodes

nodes - the GLL quadrature nodes

weights - the GLL quadrature weights

AA - newly allocated n x n mass matrix as PetscReal **

Free with PetscGaussLobattoLegendreElementMassDestroy().

PetscDTGaussLobattoLegendreQuadrature(), PetscGaussLobattoLegendreElementMassDestroy(), PetscGaussLobattoLegendreElementLaplacianCreate(), PetscGaussLobattoLegendreElementAdvectionCreate()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscGaussLobattoLegendreElementMassCreate(PetscInt n, PetscReal *nodes, PetscReal *weights, PetscReal ***AA)
```

Example 2 (unknown):
```unknown
PetscReal **
```

Example 3 (unknown):
```unknown
PetscGaussLobattoLegendreElementMassDestroy()
```

Example 4 (unknown):
```unknown
PetscDTGaussLobattoLegendreQuadrature()
```

---

## PetscGaussLobattoLegendreElementMassDestroy#

**URL:** https://petsc.org/release/manualpages/DT/PetscGaussLobattoLegendreElementMassDestroy/

**Contents:**
- PetscGaussLobattoLegendreElementMassDestroy#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Free a 1D GLL elemental mass matrix created with PetscGaussLobattoLegendreElementMassCreate()

Not Collective; No Fortran Support

n - number of GLL nodes (ignored)

nodes - the GLL quadrature nodes (ignored)

weights - the GLL quadrature weights (ignored)

AA - the mass matrix to free; *AA is set to NULL on return

PetscGaussLobattoLegendreElementMassCreate(), PetscDTGaussLobattoLegendreQuadrature()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscGaussLobattoLegendreElementMassCreate()
```

Example 2 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscGaussLobattoLegendreElementMassDestroy(PetscInt n, PetscReal *nodes, PetscReal *weights, PetscReal ***AA)
```

Example 3 (unknown):
```unknown
PetscGaussLobattoLegendreElementMassCreate()
```

Example 4 (unknown):
```unknown
PetscDTGaussLobattoLegendreQuadrature()
```

---

## PetscGaussLobattoLegendreIntegrate#

**URL:** https://petsc.org/release/manualpages/DT/PetscGaussLobattoLegendreIntegrate/

**Contents:**
- PetscGaussLobattoLegendreIntegrate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Compute the L2 integral of a function on the GLL points

n - the number of GLL nodes

nodes - the GLL nodes

weights - the GLL weights

f - the function values at the nodes

in - the value of the integral

PetscDTGaussLobattoLegendreQuadrature()

src/dm/dt/interface/dt.c

src/ksp/ksp/tutorials/ex69.c src/ksp/ksp/tutorials/ex68.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscGaussLobattoLegendreIntegrate(PetscInt n, PetscReal nodes[], PetscReal weights[], const PetscReal f[], PetscReal *in)
```

Example 2 (unknown):
```unknown
PetscDTGaussLobattoLegendreQuadrature()
```

---

## PetscLimiterCreate#

**URL:** https://petsc.org/release/manualpages/FV/PetscLimiterCreate/

**Contents:**
- PetscLimiterCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Creates an empty PetscLimiter object. The type can then be set with PetscLimiterSetType().

comm - The communicator for the PetscLimiter object

lim - The PetscLimiter object

PetscLimiter, PetscLimiterType, PetscLimiterSetType(), PETSCLIMITERSIN

src/dm/dt/fv/interface/fv.c

src/ts/tutorials/ex11.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLimiter
```

Example 2 (unknown):
```unknown
PetscLimiterSetType()
```

Example 3 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscLimiterCreate(MPI_Comm comm, PetscLimiter *lim)
```

Example 4 (unknown):
```unknown
PetscLimiter
```

---

## PetscLimiterDestroy#

**URL:** https://petsc.org/release/manualpages/FV/PetscLimiterDestroy/

**Contents:**
- PetscLimiterDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#

Destroys a PetscLimiter object

lim - the PetscLimiter object to destroy

PetscLimiter, PetscLimiterView()

src/dm/dt/fv/interface/fv.c

src/ts/tutorials/ex11.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLimiter
```

Example 2 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscLimiterDestroy(PetscLimiter *lim)
```

Example 3 (unknown):
```unknown
PetscLimiter
```

Example 4 (unknown):
```unknown
PetscLimiter
```

---

## PetscLimiterGetType#

**URL:** https://petsc.org/release/manualpages/FV/PetscLimiterGetType/

**Contents:**
- PetscLimiterGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the PetscLimiterType name (as a string) from the PetscLimiter.

lim - The PetscLimiter

name - The PetscLimiterType

PetscLimiter, PetscLimiterType, PetscLimiterSetType(), PetscLimiterCreate()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLimiterType
```

Example 2 (unknown):
```unknown
PetscLimiter
```

Example 3 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscLimiterGetType(PetscLimiter lim, PetscLimiterType *name)
```

Example 4 (unknown):
```unknown
PetscLimiter
```

---

## PetscLimiterLimit#

**URL:** https://petsc.org/release/manualpages/FV/PetscLimiterLimit/

**Contents:**
- PetscLimiterLimit#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

lim - The PetscLimiter

flim - The input field

phi - The limited field

Limiters given in symmetric form following Berger, Aftosmis, and Murman 2005

PetscLimiter, PetscLimiterType, PetscLimiterSetType(), PetscLimiterCreate()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscLimiterLimit(PetscLimiter lim, PetscReal flim, PetscReal *phi)
```

Example 2 (unknown):
```unknown
PetscLimiter
```

Example 3 (sql):
```sql
The classical flux-limited formulation is psi(r) where

 r = (u[0] - u[-1]) / (u[1] - u[0])

 The second order TVD region is bounded by

 psi_minmod(r) = min(r,1)      and        psi_superbee(r) = min(2, 2r, max(1,r))

 where all limiters are implicitly clipped to be non-negative. A more convenient slope-limited form is psi(r) =
 phi(r)(r+1)/2 in which the reconstructed interface values are

 u(v) = u[0] + phi(r) (grad u)[0] v

 where v is the vector from centroid to quadrature point. In these variables, the usual limiters become

 phi_minmod(r) = 2 min(1/(1+r),r/(1+r))   phi_superbee(r) = 2 min(2/(1+r), 2r/(1+r), max(1,r)/(1+r))

 For a nicer symmetric formulation, rewrite in terms of

 f = (u[0] - u[-1]) / (u[1] - u[-1])

 where r(f) = f/(1-f). Not that r(1-f) = (1-f)/f = 1/r(f) so the symmetry condition

 phi(r) = phi(1/r)

 becomes

 w(f) = w(1-f).

 The limiters below implement this final form w(f). The reference methods are

 w_minmod(f) = 2 min(f,(1-f))             w_superbee(r) = 4 min((1-f), f)
```

Example 4 (unknown):
```unknown
PetscLimiter
```

---

## PETSCLIMITERMC#

**URL:** https://petsc.org/release/manualpages/FV/PETSCLIMITERMC/

**Contents:**
- PETSCLIMITERMC#
- See Also#
- Level#
- Location#

“mc” - A PetscLimiter implementation

PetscLimiter, PetscLimiterType, PetscLimiterCreate(), PetscLimiterSetType()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLimiter
```

Example 2 (unknown):
```unknown
PetscLimiter
```

Example 3 (unknown):
```unknown
PetscLimiterType
```

Example 4 (unknown):
```unknown
PetscLimiterCreate()
```

---

## PETSCLIMITERMINMOD#

**URL:** https://petsc.org/release/manualpages/FV/PETSCLIMITERMINMOD/

**Contents:**
- PETSCLIMITERMINMOD#
- See Also#
- Level#
- Location#

“minmod” - A PetscLimiter implementation

PetscLimiter, PetscLimiterType, PetscLimiterCreate(), PetscLimiterSetType()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLimiter
```

Example 2 (unknown):
```unknown
PetscLimiter
```

Example 3 (unknown):
```unknown
PetscLimiterType
```

Example 4 (unknown):
```unknown
PetscLimiterCreate()
```

---

## PETSCLIMITERNONE#

**URL:** https://petsc.org/release/manualpages/FV/PETSCLIMITERNONE/

**Contents:**
- PETSCLIMITERNONE#
- See Also#
- Level#
- Location#
- Examples#

“none” - A trivial PetscLimiter implementation

PetscLimiter, PetscLimiterType, PetscLimiterCreate(), PetscLimiterSetType()

src/dm/dt/fv/interface/fv.c

src/ts/tutorials/ex11.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLimiter
```

Example 2 (unknown):
```unknown
PetscLimiter
```

Example 3 (unknown):
```unknown
PetscLimiterType
```

Example 4 (unknown):
```unknown
PetscLimiterCreate()
```

---

## PetscLimiterRegister#

**URL:** https://petsc.org/release/manualpages/FV/PetscLimiterRegister/

**Contents:**
- PetscLimiterRegister#
- Synopsis#
- Input Parameters#
- Example Usage#
- Note#
- See Also#
- Level#
- Location#

Adds a new PetscLimiter implementation

Not Collective, No Fortran Support

sname - The name of a new user-defined creation routine

function - The creation routine

Then, your PetscLimiter type can be chosen with the procedural interface via

or at runtime via the option

PetscLimiterRegister() may be called multiple times to add several user-defined PetscLimiters

PetscLimiter, PetscLimiterType, PetscLimiterRegisterAll(), PetscLimiterRegisterDestroy()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLimiter
```

Example 2 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscLimiterRegister(const char sname[], PetscErrorCode (*function)(PetscLimiter))
```

Example 3 (unknown):
```unknown
PetscLimiterRegister("my_lim", MyPetscLimiterCreate);
```

Example 4 (unknown):
```unknown
PetscLimiter
```

---

## PetscLimiterSetFromOptions#

**URL:** https://petsc.org/release/manualpages/FV/PetscLimiterSetFromOptions/

**Contents:**
- PetscLimiterSetFromOptions#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

sets parameters in a PetscLimiter from the options database

lim - the PetscLimiter object to set options for

PetscLimiter, PetscLimiterView()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLimiter
```

Example 2 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscLimiterSetFromOptions(PetscLimiter lim)
```

Example 3 (unknown):
```unknown
PetscLimiter
```

Example 4 (unknown):
```unknown
PetscLimiter
```

---

## PetscLimiterSetType#

**URL:** https://petsc.org/release/manualpages/FV/PetscLimiterSetType/

**Contents:**
- PetscLimiterSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

Builds a PetscLimiter for a given PetscLimiterType

lim - The PetscLimiter object

name - The kind of limiter

-petsclimiter_type type - Sets the PetscLimiter type; use -help for a list of available types

PetscLimiter, PetscLimiterType, PetscLimiterGetType(), PetscLimiterCreate()

src/dm/dt/fv/interface/fv.c

src/ts/tutorials/ex11.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLimiter
```

Example 2 (unknown):
```unknown
PetscLimiterType
```

Example 3 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscLimiterSetType(PetscLimiter lim, PetscLimiterType name)
```

Example 4 (unknown):
```unknown
PetscLimiter
```

---

## PetscLimiterSetUp#

**URL:** https://petsc.org/release/manualpages/FV/PetscLimiterSetUp/

**Contents:**
- PetscLimiterSetUp#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Construct data structures for the PetscLimiter

lim - the PetscLimiter object to setup

PetscLimiter, PetscLimiterView(), PetscLimiterDestroy()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLimiter
```

Example 2 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscLimiterSetUp(PetscLimiter lim)
```

Example 3 (unknown):
```unknown
PetscLimiter
```

Example 4 (unknown):
```unknown
PetscLimiter
```

---

## PETSCLIMITERSIN#

**URL:** https://petsc.org/release/manualpages/FV/PETSCLIMITERSIN/

**Contents:**
- PETSCLIMITERSIN#
- See Also#
- Level#
- Location#

“sin” - A PetscLimiter implementation

PetscLimiter, PetscLimiterType, PetscLimiterCreate(), PetscLimiterSetType()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLimiter
```

Example 2 (unknown):
```unknown
PetscLimiter
```

Example 3 (unknown):
```unknown
PetscLimiterType
```

Example 4 (unknown):
```unknown
PetscLimiterCreate()
```

---

## PETSCLIMITERSUPERBEE#

**URL:** https://petsc.org/release/manualpages/FV/PETSCLIMITERSUPERBEE/

**Contents:**
- PETSCLIMITERSUPERBEE#
- See Also#
- Level#
- Location#

“superbee” - A PetscLimiter implementation

PetscLimiter, PetscLimiterType, PetscLimiterCreate(), PetscLimiterSetType()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLimiter
```

Example 2 (unknown):
```unknown
PetscLimiter
```

Example 3 (unknown):
```unknown
PetscLimiterType
```

Example 4 (unknown):
```unknown
PetscLimiterCreate()
```

---

## PetscLimiterType#

**URL:** https://petsc.org/release/manualpages/FV/PetscLimiterType/

**Contents:**
- PetscLimiterType#
- Synopsis#
- See Also#
- Level#
- Location#

String with the name of a PETSc finite volume slope limiter

PetscLimiterSetType(), PetscLimiter

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (rust):
```rust
typedef const char *PetscLimiterType;
#define PETSCLIMITERSIN       "sin"
#define PETSCLIMITERZERO      "zero"
#define PETSCLIMITERNONE      "none"
#define PETSCLIMITERMINMOD    "minmod"
#define PETSCLIMITERVANLEER   "vanleer"
#define PETSCLIMITERVANALBADA "vanalbada"
#define PETSCLIMITERSUPERBEE  "superbee"
#define PETSCLIMITERMC        "mc"
```

Example 2 (unknown):
```unknown
PetscLimiterSetType()
```

Example 3 (unknown):
```unknown
PetscLimiter
```

---

## PETSCLIMITERVANALBADA#

**URL:** https://petsc.org/release/manualpages/FV/PETSCLIMITERVANALBADA/

**Contents:**
- PETSCLIMITERVANALBADA#
- See Also#
- Level#
- Location#

“vanalbada” - A PetscLimiter implementation

PetscLimiter, PetscLimiterType, PetscLimiterCreate(), PetscLimiterSetType()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLimiter
```

Example 2 (unknown):
```unknown
PetscLimiterType
```

Example 3 (unknown):
```unknown
PetscLimiterCreate()
```

Example 4 (unknown):
```unknown
PetscLimiterSetType()
```

---

## PETSCLIMITERVANLEER#

**URL:** https://petsc.org/release/manualpages/FV/PETSCLIMITERVANLEER/

**Contents:**
- PETSCLIMITERVANLEER#
- See Also#
- Level#
- Location#

“vanleer” - A PetscLimiter implementation

PetscLimiter, PetscLimiterType, PetscLimiterCreate(), PetscLimiterSetType()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLimiter
```

Example 2 (unknown):
```unknown
PetscLimiter
```

Example 3 (unknown):
```unknown
PetscLimiterType
```

Example 4 (unknown):
```unknown
PetscLimiterCreate()
```

---

## PetscLimiterViewFromOptions#

**URL:** https://petsc.org/release/manualpages/FV/PetscLimiterViewFromOptions/

**Contents:**
- PetscLimiterViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

View a PetscLimiter based on values in the options database

A - the PetscLimiter object to view

obj - Optional object that provides the options prefix to use

name - command line option name

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

PetscLimiter, PetscLimiterView(), PetscObjectViewFromOptions(), PetscLimiterCreate()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLimiter
```

Example 2 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscLimiterViewFromOptions(PetscLimiter A, PetscObject obj, const char name[])
```

Example 3 (unknown):
```unknown
PetscLimiter
```

Example 4 (unknown):
```unknown
PetscObjectViewFromOptions()
```

---

## PetscLimiterView#

**URL:** https://petsc.org/release/manualpages/FV/PetscLimiterView/

**Contents:**
- PetscLimiterView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

lim - the PetscLimiter object to view

PetscLimiter, PetscViewer, PetscLimiterDestroy(), PetscLimiterViewFromOptions()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLimiter
```

Example 2 (unknown):
```unknown
#include "petscfv.h" 
PetscErrorCode PetscLimiterView(PetscLimiter lim, PetscViewer v)
```

Example 3 (unknown):
```unknown
PetscLimiter
```

Example 4 (unknown):
```unknown
PetscLimiter
```

---

## PETSCLIMITERZERO#

**URL:** https://petsc.org/release/manualpages/FV/PETSCLIMITERZERO/

**Contents:**
- PETSCLIMITERZERO#
- See Also#
- Level#
- Location#

“zero” - A simple PetscLimiter implementation

PetscLimiter, PetscLimiterType, PetscLimiterCreate(), PetscLimiterSetType()

src/dm/dt/fv/interface/fv.c

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLimiter
```

Example 2 (unknown):
```unknown
PetscLimiter
```

Example 3 (unknown):
```unknown
PetscLimiterType
```

Example 4 (unknown):
```unknown
PetscLimiterCreate()
```

---

## PetscLimiter#

**URL:** https://petsc.org/release/manualpages/FV/PetscLimiter/

**Contents:**
- PetscLimiter#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

PETSc object that manages a finite volume slope limiter

PetscLimiterCreate(), PetscLimiterSetType(), PetscLimiterType

include/petscfvtypes.h

src/ts/tutorials/ex11.c

_p_PetscLimiter in include/petsc/private/petscfvimpl.h PetscLimiter_Sin in include/petsc/private/petscfvimpl.h PetscLimiter_Zero in include/petsc/private/petscfvimpl.h PetscLimiter_None in include/petsc/private/petscfvimpl.h PetscLimiter_Minmod in include/petsc/private/petscfvimpl.h PetscLimiter_VanLeer in include/petsc/private/petscfvimpl.h PetscLimiter_VanAlbada in include/petsc/private/petscfvimpl.h PetscLimiter_Superbee in include/petsc/private/petscfvimpl.h PetscLimiter_MC in include/petsc/private/petscfvimpl.h

Index of all FV routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_PetscLimiter *PetscLimiter;
```

Example 2 (unknown):
```unknown
PetscLimiterCreate()
```

Example 3 (unknown):
```unknown
PetscLimiterSetType()
```

Example 4 (unknown):
```unknown
PetscLimiterType
```

---

## PetscPDFConstant1D#

**URL:** https://petsc.org/release/manualpages/DT/PetscPDFConstant1D/

**Contents:**
- PetscPDFConstant1D#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

PDF for the uniform distribution in 1D

x - Coordinate in \([-1, 1]\)

p - The probability density at x

PetscCDFConstant1D(), PetscPDFSampleConstant1D(), PetscPDFConstant2D(), PetscPDFConstant3D()

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscPDFConstant1D(const PetscReal x[], const PetscReal unused[], PetscReal p[])
```

Example 2 (unknown):
```unknown
PetscCDFConstant1D()
```

Example 3 (unknown):
```unknown
PetscPDFSampleConstant1D()
```

Example 4 (unknown):
```unknown
PetscPDFConstant2D()
```

---

## PetscPDFConstant2D#

**URL:** https://petsc.org/release/manualpages/DT/PetscPDFConstant2D/

**Contents:**
- PetscPDFConstant2D#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

PDF for the uniform distribution in 2D

x - Coordinate in \([-1, 1]^2\)

p - The probability density at x

PetscCDFConstant2D(), PetscPDFSampleConstant2D(), PetscPDFConstant1D(), PetscPDFConstant3D()

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscPDFConstant2D(const PetscReal x[], const PetscReal unused[], PetscReal p[])
```

Example 2 (unknown):
```unknown
PetscCDFConstant2D()
```

Example 3 (unknown):
```unknown
PetscPDFSampleConstant2D()
```

Example 4 (unknown):
```unknown
PetscPDFConstant1D()
```

---

## PetscPDFConstant3D#

**URL:** https://petsc.org/release/manualpages/DT/PetscPDFConstant3D/

**Contents:**
- PetscPDFConstant3D#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

PDF for the uniform distribution in 3D

x - Coordinate in \([-1, 1]^3\)

p - The probability density at x

PetscCDFConstant3D(), PetscPDFSampleConstant3D(), PetscPDFSampleConstant1D(), PetscPDFSampleConstant2D()

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscPDFConstant3D(const PetscReal x[], const PetscReal unused[], PetscReal p[])
```

Example 2 (unknown):
```unknown
PetscCDFConstant3D()
```

Example 3 (unknown):
```unknown
PetscPDFSampleConstant3D()
```

Example 4 (unknown):
```unknown
PetscPDFSampleConstant1D()
```

---

## PetscPDFGaussian1D#

**URL:** https://petsc.org/release/manualpages/DT/PetscPDFGaussian1D/

**Contents:**
- PetscPDFGaussian1D#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

PDF for the Gaussian distribution in 1D

x - Coordinate in \([-\infty, \infty]\)

scale - Scaling value

p - The probability density at x

PetscPDFMaxwellBoltzmann3D()

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscPDFGaussian1D(const PetscReal x[], const PetscReal scale[], PetscReal p[])
```

Example 2 (unknown):
```unknown
PetscPDFMaxwellBoltzmann3D()
```

---

## PetscPDFGaussian2D#

**URL:** https://petsc.org/release/manualpages/DT/PetscPDFGaussian2D/

**Contents:**
- PetscPDFGaussian2D#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

PDF for the Gaussian distribution in 2D

x - Coordinate in \([-\infty, \infty]^2\)

p - The probability density at x

PetscPDFSampleGaussian2D(), PetscPDFMaxwellBoltzmann3D()

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscPDFGaussian2D(const PetscReal x[], const PetscReal unused[], PetscReal p[])
```

Example 2 (unknown):
```unknown
PetscPDFSampleGaussian2D()
```

Example 3 (unknown):
```unknown
PetscPDFMaxwellBoltzmann3D()
```

---

## PetscPDFGaussian3D#

**URL:** https://petsc.org/release/manualpages/DT/PetscPDFGaussian3D/

**Contents:**
- PetscPDFGaussian3D#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

PDF for the Gaussian distribution in 3D

x - Coordinate in \([-\infty, \infty]^3\)

p - The probability density at x

PetscPDFSampleGaussian3D(), PetscPDFMaxwellBoltzmann3D()

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscPDFGaussian3D(const PetscReal x[], const PetscReal unused[], PetscReal p[])
```

Example 2 (unknown):
```unknown
PetscPDFSampleGaussian3D()
```

Example 3 (unknown):
```unknown
PetscPDFMaxwellBoltzmann3D()
```

---

## PetscPDFMaxwellBoltzmann1D#

**URL:** https://petsc.org/release/manualpages/DT/PetscPDFMaxwellBoltzmann1D/

**Contents:**
- PetscPDFMaxwellBoltzmann1D#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

PDF for the Maxwell-Boltzmann distribution in 1D

x - Speed in \([0, \infty]\)

p - The probability density at x

PetscCDFMaxwellBoltzmann1D()

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscPDFMaxwellBoltzmann1D(const PetscReal x[], const PetscReal unused[], PetscReal p[])
```

Example 2 (unknown):
```unknown
PetscCDFMaxwellBoltzmann1D()
```

---

## PetscPDFMaxwellBoltzmann2D#

**URL:** https://petsc.org/release/manualpages/DT/PetscPDFMaxwellBoltzmann2D/

**Contents:**
- PetscPDFMaxwellBoltzmann2D#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

PDF for the Maxwell-Boltzmann distribution in 2D

x - Speed in \([0, \infty]\)

p - The probability density at x

PetscCDFMaxwellBoltzmann2D()

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscPDFMaxwellBoltzmann2D(const PetscReal x[], const PetscReal unused[], PetscReal p[])
```

Example 2 (unknown):
```unknown
PetscCDFMaxwellBoltzmann2D()
```

---

## PetscPDFMaxwellBoltzmann3D#

**URL:** https://petsc.org/release/manualpages/DT/PetscPDFMaxwellBoltzmann3D/

**Contents:**
- PetscPDFMaxwellBoltzmann3D#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

PDF for the Maxwell-Boltzmann distribution in 3D

x - Speed in \([0, \infty]\)

p - The probability density at x

PetscCDFMaxwellBoltzmann3D()

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscPDFMaxwellBoltzmann3D(const PetscReal x[], const PetscReal unused[], PetscReal p[])
```

Example 2 (unknown):
```unknown
PetscCDFMaxwellBoltzmann3D()
```

---

## PetscPDFSampleConstant1D#

**URL:** https://petsc.org/release/manualpages/DT/PetscPDFSampleConstant1D/

**Contents:**
- PetscPDFSampleConstant1D#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Sample uniformly from a uniform distribution on [-1, 1] in 1D

p - A uniform variable on \([0, 1]\)

x - Coordinate in \([-1, 1]\)

PetscPDFConstant1D(), PetscCDFConstant1D(), PetscPDFSampleConstant2D(), PetscPDFSampleConstant3D()

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscPDFSampleConstant1D(const PetscReal p[], const PetscReal unused[], PetscReal x[])
```

Example 2 (unknown):
```unknown
PetscPDFConstant1D()
```

Example 3 (unknown):
```unknown
PetscCDFConstant1D()
```

Example 4 (unknown):
```unknown
PetscPDFSampleConstant2D()
```

---

## PetscPDFSampleConstant2D#

**URL:** https://petsc.org/release/manualpages/DT/PetscPDFSampleConstant2D/

**Contents:**
- PetscPDFSampleConstant2D#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Sample uniformly from a uniform distribution on \([-1, 1]^2\) in 2D

p - Two uniform variables on \([0, 1]\)

x - Coordinate in \([-1, 1]^2\)

PetscPDFConstant2D(), PetscCDFConstant2D(), PetscPDFSampleConstant1D(), PetscPDFSampleConstant3D()

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscPDFSampleConstant2D(const PetscReal p[], const PetscReal unused[], PetscReal x[])
```

Example 2 (unknown):
```unknown
PetscPDFConstant2D()
```

Example 3 (unknown):
```unknown
PetscCDFConstant2D()
```

Example 4 (unknown):
```unknown
PetscPDFSampleConstant1D()
```

---

## PetscPDFSampleConstant3D#

**URL:** https://petsc.org/release/manualpages/DT/PetscPDFSampleConstant3D/

**Contents:**
- PetscPDFSampleConstant3D#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Sample uniformly from a uniform distribution on \([-1, 1]^3\) in 3D

p - Three uniform variables on \([0, 1]\)

x - Coordinate in \([-1, 1]^3\)

PetscPDFConstant3D(), PetscCDFConstant3D(), PetscPDFSampleConstant1D(), PetscPDFSampleConstant2D()

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscPDFSampleConstant3D(const PetscReal p[], const PetscReal unused[], PetscReal x[])
```

Example 2 (unknown):
```unknown
PetscPDFConstant3D()
```

Example 3 (unknown):
```unknown
PetscCDFConstant3D()
```

Example 4 (unknown):
```unknown
PetscPDFSampleConstant1D()
```

---

## PetscPDFSampleGaussian1D#

**URL:** https://petsc.org/release/manualpages/DT/PetscPDFSampleGaussian1D/

**Contents:**
- PetscPDFSampleGaussian1D#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Sample uniformly from a Gaussian distribution in 1D

p - A uniform variable on \([0, 1]\)

x - Coordinate in \([-\infty, \infty]\)

See http://www.mimirgames.com/articles/programming/approximations-of-the-inverse-error-function and https://stackoverflow.com/questions/27229371/inverse-error-function-in-c

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscPDFSampleGaussian1D(const PetscReal p[], const PetscReal unused[], PetscReal x[])
```

Example 2 (unknown):
```unknown
PetscPDFGaussian2D()
```

---

## PetscPDFSampleGaussian2D#

**URL:** https://petsc.org/release/manualpages/DT/PetscPDFSampleGaussian2D/

**Contents:**
- PetscPDFSampleGaussian2D#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Sample uniformly from a Gaussian distribution in 2D https://en.wikipedia.org/wiki/Box–Muller_transform

p - A uniform variable on \([0, 1]^2\)

x - Coordinate in \([-\infty, \infty]^2 \)

PetscPDFGaussian2D(), PetscPDFMaxwellBoltzmann3D()

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscPDFSampleGaussian2D(const PetscReal p[], const PetscReal unused[], PetscReal x[])
```

Example 2 (unknown):
```unknown
PetscPDFGaussian2D()
```

Example 3 (unknown):
```unknown
PetscPDFMaxwellBoltzmann3D()
```

---

## PetscPDFSampleGaussian3D#

**URL:** https://petsc.org/release/manualpages/DT/PetscPDFSampleGaussian3D/

**Contents:**
- PetscPDFSampleGaussian3D#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Sample uniformly from a Gaussian distribution in 3D https://en.wikipedia.org/wiki/Box–Muller_transform

p - A uniform variable on \([0, 1]^3\)

x - Coordinate in \([-\infty, \infty]^3\)

PetscPDFGaussian3D(), PetscPDFMaxwellBoltzmann3D()

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscPDFSampleGaussian3D(const PetscReal p[], const PetscReal unused[], PetscReal x[])
```

Example 2 (unknown):
```unknown
PetscPDFGaussian3D()
```

Example 3 (unknown):
```unknown
PetscPDFMaxwellBoltzmann3D()
```

---

## PetscPointBoundFn#

**URL:** https://petsc.org/release/manualpages/DT/PetscPointBoundFn/

**Contents:**
- PetscPointBoundFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

A prototype of a pointwise function that can be passed to, for example, PetscDSSetLowerBound()

dim - the coordinate dimension

x - coordinates of the current point

Nc - the number of field components

u - the lower bound evaluated at the current point

ctx - an application context, passed in with, for example, PetscDSSetLowerBound()

PetscPointFn, PetscDSSetLowerBound(), PetscDSSetUpperBound()

include/petscdstypes.h

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDSSetLowerBound()
```

Example 2 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode PetscPointBoundFn(PetscInt dim, PetscReal t, const PetscReal x[], PetscInt Nc, PetscScalar u[], PetscCtx ctx);
```

Example 3 (unknown):
```unknown
PetscDSSetLowerBound()
```

Example 4 (unknown):
```unknown
PetscPointFn
```

---

## PetscPointExactSolutionFn#

**URL:** https://petsc.org/release/manualpages/DT/PetscPointExactSolutionFn/

**Contents:**
- PetscPointExactSolutionFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

A prototype of a pointwise function that computes the exact solution to a PDE. Used with, for example, PetscDSSetExactSolution()

dim - the coordinate dimension

x - coordinates of the current point

Nc - the number of field components

u - the solution field evaluated at the current point

ctx - an application context, set with PetscDSSetExactSolution() or PetscDSSetExactSolutionTimeDerivative()

PetscPointFn, PetscDSSetExactSolution(), PetscDSGetExactSolution(), PetscDSSetExactSolutionTimeDerivative(), PetscDSGetExactSolutionTimeDerivative()

include/petscdstypes.h

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDSSetExactSolution()
```

Example 2 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode PetscPointExactSolutionFn(PetscInt dim, PetscReal t, const PetscReal x[], PetscInt Nc, PetscScalar u[], PetscCtx ctx);
```

Example 3 (unknown):
```unknown
PetscDSSetExactSolution()
```

Example 4 (unknown):
```unknown
PetscDSSetExactSolutionTimeDerivative()
```

---

## PetscPointFn#

**URL:** https://petsc.org/release/manualpages/DT/PetscPointFn/

**Contents:**
- PetscPointFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#
- Examples#

A prototype of a pointwise function that can be passed to, for example, PetscDSSetObjective()

dim - the coordinate dimension

Nf - the number of fields

NfAux - the number of auxiliary fields

uOff - the offset into u[] and u_t[] for each field

uOff_x - the offset into u_x[] for each field

u - each field evaluated at the current point

u_t - the time derivative of each field evaluated at the current point

u_x - the gradient of each field evaluated at the current point

aOff - the offset into a[] and a_t[] for each auxiliary field

aOff_x - the offset into a_x[] for each auxiliary field

a - each auxiliary field evaluated at the current point

a_t - the time derivative of each auxiliary field evaluated at the current point

a_x - the gradient of auxiliary each field evaluated at the current point

x - coordinates of the current point

numConstants - number of constant parameters

constants - constant parameters

obj - output values at the current point

PetscPointFn, PetscDSSetObjective(), PetscDSGetObjective(), PetscDSGetResidual(), PetscDSSetResidual(), PetscDSGetRHSResidual(), PetscDSSetUpdate(), PetscDSGetUpdate(), DMPlexSetCoordinateMap()

include/petscdstypes.h

src/ts/tutorials/ex76.c src/snes/tutorials/ex13.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDSSetObjective()
```

Example 2 (cpp):
```cpp
PETSC_EXTERN_TYPEDEF typedef void PetscPointFn(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal X[], PetscInt numConstants, const PetscScalar constants[], PetscScalar result[]);
```

Example 3 (unknown):
```unknown
PetscPointFn
```

Example 4 (unknown):
```unknown
PetscDSSetObjective()
```

---

## PetscPointJacFn#

**URL:** https://petsc.org/release/manualpages/DT/PetscPointJacFn/

**Contents:**
- PetscPointJacFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

A prototype of a pointwise function that can be passed to, for example, PetscDSSetJacobian() for computing Jacobians

dim - the coordinate dimension

Nf - the number of fields

NfAux - the number of auxiliary fields

uOff - the offset into u[] and u_t[] for each field

uOff_x - the offset into u_x[] for each field

u - each field evaluated at the current point

u_t - the time derivative of each field evaluated at the current point

u_x - the gradient of each field evaluated at the current point

aOff - the offset into a[] and a_t[] for each auxiliary field

aOff_x - the offset into a_x[] for each auxiliary field

a - each auxiliary field evaluated at the current point

a_t - the time derivative of each auxiliary field evaluated at the current point

a_x - the gradient of auxiliary each field evaluated at the current point

u_tShift - the multiplier a for \(dF/dU_t\)

x - coordinates of the current point

numConstants - number of constant parameters

constants - constant parameters

g - output values at the current point

PetscPointFn, PetscDSSetJacobian(), PetscDSGetJacobian(), PetscDSSetJacobianPreconditioner(), PetscDSGetJacobianPreconditioner(), PetscDSSetDynamicJacobian(), PetscDSGetDynamicJacobian()

include/petscdstypes.h

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDSSetJacobian()
```

Example 2 (cpp):
```cpp
PETSC_EXTERN_TYPEDEF typedef void PetscPointJacFn(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, PetscReal u_tShift, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar g[]);
```

Example 3 (unknown):
```unknown
PetscPointFn
```

Example 4 (unknown):
```unknown
PetscDSSetJacobian()
```

---

## PetscProbComputeKSStatisticMagnitude#

**URL:** https://petsc.org/release/manualpages/DT/PetscProbComputeKSStatisticMagnitude/

**Contents:**
- PetscProbComputeKSStatisticMagnitude#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Compute the Kolmogorov-Smirnov statistic for the empirical distribution for the magnitude over each block of an input vector, compared to an analytic CDF.

v - The data vector, blocksize is the sample dimension

cdf - The analytic CDF

alpha - The KS statistic

The Kolmogorov-Smirnov statistic for a given cumulative distribution function \(F(x)\) is

where \(\sup_x\) is the supremum of the set of distances, and the empirical distribution function \(F_n(x)\) is discrete, and given by

The empirical distribution function \(F_n(x)\) is discrete, and thus had a ``stairstep’’ cumulative distribution, making \(n\) the number of stairs. Intuitively, the statistic takes the largest absolute difference between the two distribution functions across all \(x\) values.

The goodness-of-fit test, or Kolmogorov-Smirnov test, is constructed using the Kolmogorov distribution. It rejects the null hypothesis at level \(\alpha\) if

where \(K_\alpha\) is found from

This means that getting a small alpha says that we have high confidence that the data did not come from the input distribution, so we say that it rejects the null hypothesis.

PetscProbComputeKSStatistic(), PetscProbComputeKSStatisticWeighted(), PetscProbFn

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscProbComputeKSStatisticMagnitude(Vec v, PetscProbFn *cdf, PetscReal *alpha)
```

Example 2 (unknown):
```unknown
PetscProbComputeKSStatistic()
```

Example 3 (unknown):
```unknown
PetscProbComputeKSStatisticWeighted()
```

Example 4 (unknown):
```unknown
PetscProbFn
```

---

## PetscProbComputeKSStatisticWeighted#

**URL:** https://petsc.org/release/manualpages/DT/PetscProbComputeKSStatisticWeighted/

**Contents:**
- PetscProbComputeKSStatisticWeighted#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Compute the Kolmogorov-Smirnov statistic for the weighted empirical distribution for an input vector, compared to an analytic CDF.

v - The data vector, blocksize is the sample dimension

w - The vector of weights for each sample, instead of the default 1/n

cdf - The analytic CDF

alpha - The KS statistic

The Kolmogorov-Smirnov statistic for a given cumulative distribution function \(F(x)\) is

where \(\sup_x\) is the supremum of the set of distances, and the empirical distribution function \(F_n(x)\) is discrete, and given by

The empirical distribution function \(F_n(x)\) is discrete, and thus had a ``stairstep’’ cumulative distribution, making \(n\) the number of stairs. Intuitively, the statistic takes the largest absolute difference between the two distribution functions across all \(x\) values.

The goodness-of-fit test, or Kolmogorov-Smirnov test, is constructed using the Kolmogorov distribution. It rejects the null hypothesis at level \(\alpha\) if

where \(K_\alpha\) is found from

This means that getting a small alpha says that we have high confidence that the data did not come from the input distribution, so we say that it rejects the null hypothesis.

PetscProbComputeKSStatistic(), PetscProbComputeKSStatisticMagnitude(), PetscProbFn

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscProbComputeKSStatisticWeighted(Vec v, Vec w, PetscProbFn *cdf, PetscReal *alpha)
```

Example 2 (unknown):
```unknown
PetscProbComputeKSStatistic()
```

Example 3 (unknown):
```unknown
PetscProbComputeKSStatisticMagnitude()
```

Example 4 (unknown):
```unknown
PetscProbFn
```

---

## PetscProbComputeKSStatistic#

**URL:** https://petsc.org/release/manualpages/DT/PetscProbComputeKSStatistic/

**Contents:**
- PetscProbComputeKSStatistic#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Compute the Kolmogorov-Smirnov statistic for the empirical distribution for an input vector, compared to an analytic CDF.

v - The data vector, blocksize is the sample dimension

cdf - The analytic CDF

alpha - The KS statistic

The Kolmogorov-Smirnov statistic for a given cumulative distribution function \(F(x)\) is

where \(\sup_x\) is the supremum of the set of distances, and the empirical distribution function \(F_n(x)\) is discrete, and given by

The empirical distribution function \(F_n(x)\) is discrete, and thus had a ``stairstep’’ cumulative distribution, making \(n\) the number of stairs. Intuitively, the statistic takes the largest absolute difference between the two distribution functions across all \(x\) values.

The goodness-of-fit test, or Kolmogorov-Smirnov test, is constructed using the Kolmogorov distribution. It rejects the null hypothesis at level \(\alpha\) if

where \(K_\alpha\) is found from

This means that getting a small alpha says that we have high confidence that the data did not come from the input distribution, so we say that it rejects the null hypothesis.

PetscProbComputeKSStatisticWeighted(), PetscProbComputeKSStatisticMagnitude(), PetscProbFn

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscProbComputeKSStatistic(Vec v, PetscProbFn *cdf, PetscReal *alpha)
```

Example 2 (unknown):
```unknown
PetscProbComputeKSStatisticWeighted()
```

Example 3 (unknown):
```unknown
PetscProbComputeKSStatisticMagnitude()
```

Example 4 (unknown):
```unknown
PetscProbFn
```

---

## PetscProbCreateFromOptions#

**URL:** https://petsc.org/release/manualpages/DT/PetscProbCreateFromOptions/

**Contents:**
- PetscProbCreateFromOptions#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Return the probability distribution specified by the arguments and options

dim - The dimension of sample points

prefix - The options prefix, or NULL

name - The options database name for the probability distribution type

pdf - The PDF of this type, or NULL

cdf - The CDF of this type, or NULL

sampler - The PDF sampler of this type, or NULL

PetscProbFn, PetscPDFMaxwellBoltzmann1D(), PetscPDFGaussian1D(), PetscPDFConstant1D()

src/dm/dt/interface/dtprob.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscProbCreateFromOptions(PetscInt dim, const char prefix[], const char name[], PetscProbFn **pdf, PetscProbFn **cdf, PetscProbFn **sampler)
```

Example 2 (unknown):
```unknown
PetscProbFn
```

Example 3 (unknown):
```unknown
PetscPDFMaxwellBoltzmann1D()
```

Example 4 (unknown):
```unknown
PetscPDFGaussian1D()
```

---

## PetscProbFn#

**URL:** https://petsc.org/release/manualpages/DT/PetscProbFn/

**Contents:**
- PetscProbFn#
- Synopsis#
- Calling Sequence#
- Developer Note#
- See Also#
- Level#
- Location#

A prototype of a PDF or CDF used with PETSc probability operations whose names begin with PetscProb such as PetscProbComputeKSStatistic().

scale - scale factor, I don’t know what this is for

result - the value of the PDF or CDF at the input value

Why does this take an array argument for result when it seems to be able to output a single value?

PetscProbComputeKSStatistic(), PetscProbComputeKSStatisticWeighted(), PetscPDFMaxwellBoltzmann1D()

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscProbComputeKSStatistic()
```

Example 2 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode PetscProbFn(const PetscReal x[], const PetscReal scale[], PetscReal result[]);
```

Example 3 (unknown):
```unknown
PetscProbComputeKSStatistic()
```

Example 4 (unknown):
```unknown
PetscProbComputeKSStatisticWeighted()
```

---

## PetscQuadratureComputePermutations#

**URL:** https://petsc.org/release/manualpages/DT/PetscQuadratureComputePermutations/

**Contents:**
- PetscQuadratureComputePermutations#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Compute permutations of quadrature points corresponding to domain orientations

quad - The PetscQuadrature

Np - The number of domain orientations

perm - An array of IS permutations, one for ech orientation,

PetscQuadratureSetCellType(), PetscQuadrature

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscQuadratureComputePermutations(PetscQuadrature quad, PeOp PetscInt *Np, IS *perm[])
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
PetscQuadratureSetCellType()
```

Example 4 (unknown):
```unknown
PetscQuadrature
```

---

## PetscQuadratureCreate#

**URL:** https://petsc.org/release/manualpages/DT/PetscQuadratureCreate/

**Contents:**
- PetscQuadratureCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Create a PetscQuadrature object

comm - The communicator for the PetscQuadrature object

q - The PetscQuadrature object

PetscQuadrature, Petscquadraturedestroy(), PetscQuadratureGetData()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscQuadrature
```

Example 2 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscQuadratureCreate(MPI_Comm comm, PetscQuadrature *q)
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscQuadrature
```

---

## PetscQuadratureDestroy#

**URL:** https://petsc.org/release/manualpages/DT/PetscQuadratureDestroy/

**Contents:**
- PetscQuadratureDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#

Destroys a PetscQuadrature object

q - The PetscQuadrature object

PetscQuadrature, PetscQuadratureCreate(), PetscQuadratureGetData()

src/dm/dt/interface/dt.c

src/dm/field/tutorials/ex1.c src/ksp/ksp/tutorials/ex35.cxx src/ksp/ksp/tutorials/ex70.c src/ksp/ksp/tutorials/ex36.cxx

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscQuadrature
```

Example 2 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscQuadratureDestroy(PetscQuadrature *q)
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscQuadrature
```

---

## PetscQuadratureDuplicate#

**URL:** https://petsc.org/release/manualpages/DT/PetscQuadratureDuplicate/

**Contents:**
- PetscQuadratureDuplicate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Create a deep copy of the PetscQuadrature object

q - The PetscQuadrature object

r - The new PetscQuadrature object

PetscQuadrature, PetscQuadratureCreate(), PetscQuadratureDestroy(), PetscQuadratureGetData()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscQuadrature
```

Example 2 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscQuadratureDuplicate(PetscQuadrature q, PetscQuadrature *r)
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscQuadrature
```

---

## PetscQuadratureEqual#

**URL:** https://petsc.org/release/manualpages/DT/PetscQuadratureEqual/

**Contents:**
- PetscQuadratureEqual#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

determine whether two quadratures are equivalent

A - A PetscQuadrature object

B - Another PetscQuadrature object

equal - PETSC_TRUE if the quadratures are the same

PetscQuadrature, PetscQuadratureCreate()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscQuadratureEqual(PetscQuadrature A, PetscQuadrature B, PetscBool *equal)
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscQuadrature
```

---

## PetscQuadratureExpandComposite#

**URL:** https://petsc.org/release/manualpages/DT/PetscQuadratureExpandComposite/

**Contents:**
- PetscQuadratureExpandComposite#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Return a quadrature over the composite element, which has the original quadrature in each subelement

Not Collective; No Fortran Support

q - The original PetscQuadrature

numSubelements - The number of subelements the original element is divided into

v0 - An array of the initial points for each subelement

jac - An array of the Jacobian mappings from the reference to each subelement

Together v0 and jac define an affine mapping from the original reference element to each subelement

PetscQuadrature, PetscFECreate(), PetscSpaceGetDimension(), PetscDualSpaceGetDimension()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscQuadratureExpandComposite(PetscQuadrature q, PetscInt numSubelements, const PetscReal v0[], const PetscReal jac[], PetscQuadrature *qref)
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscFECreate()
```

---

## PetscQuadratureGetCellType#

**URL:** https://petsc.org/release/manualpages/DT/PetscQuadratureGetCellType/

**Contents:**
- PetscQuadratureGetCellType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Return the cell type of the integration domain

q - The PetscQuadrature object

ct - The cell type of the integration domain

PetscQuadrature, PetscQuadratureSetCellType(), PetscQuadratureGetData(), PetscQuadratureSetData()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscQuadratureGetCellType(PetscQuadrature q, DMPolytopeType *ct)
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscQuadratureSetCellType()
```

---

## PetscQuadratureGetData#

**URL:** https://petsc.org/release/manualpages/DT/PetscQuadratureGetData/

**Contents:**
- PetscQuadratureGetData#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Returns the data defining the PetscQuadrature

q - The PetscQuadrature object

dim - The spatial dimension

Nc - The number of components

npoints - The number of quadrature points

points - The coordinates of each quadrature point

weights - The weight of each quadrature point

All output arguments are optional, pass NULL for any argument not required

Call PetscQuadratureRestoreData() when you are done with the data

PetscQuadrature, PetscQuadratureCreate(), PetscQuadratureSetData()

src/dm/dt/interface/dt.c

src/dm/field/tutorials/ex1.c src/ksp/ksp/tutorials/ex35.cxx src/ksp/ksp/tutorials/ex70.c src/ksp/ksp/tutorials/ex36.cxx

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscQuadrature
```

Example 2 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscQuadratureGetData(PetscQuadrature q, PeOp PetscInt *dim, PeOp PetscInt *Nc, PeOp PetscInt *npoints, PeOp const PetscReal *points[], PeOp const PetscReal *weights[])
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscQuadratureRestoreData()
```

---

## PetscQuadratureGetNumComponents#

**URL:** https://petsc.org/release/manualpages/DT/PetscQuadratureGetNumComponents/

**Contents:**
- PetscQuadratureGetNumComponents#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Return the number of components for functions to be integrated

q - The PetscQuadrature object

Nc - The number of components

We are performing an integral \(\int f(x) w(x) dx\), where both \(f\) and \(w\) (the weight) have Nc components.

PetscQuadrature, PetscQuadratureSetNumComponents(), PetscQuadratureGetData(), PetscQuadratureSetData()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscQuadratureGetNumComponents(PetscQuadrature q, PetscInt *Nc)
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscQuadratureSetNumComponents()
```

---

## PetscQuadratureGetOrder#

**URL:** https://petsc.org/release/manualpages/DT/PetscQuadratureGetOrder/

**Contents:**
- PetscQuadratureGetOrder#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Return the order of the method in the PetscQuadrature

q - The PetscQuadrature object

order - The order of the quadrature, i.e. the highest degree polynomial that is exactly integrated

PetscQuadrature, PetscQuadratureSetOrder(), PetscQuadratureGetData(), PetscQuadratureSetData()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscQuadrature
```

Example 2 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscQuadratureGetOrder(PetscQuadrature q, PetscInt *order)
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscQuadrature
```

---

## PetscQuadraturePushForward#

**URL:** https://petsc.org/release/manualpages/DT/PetscQuadraturePushForward/

**Contents:**
- PetscQuadraturePushForward#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Push forward a quadrature functional under an affine transformation.

q - the quadrature functional

imageDim - the dimension of the image of the transformation

origin - a point in the original space

originImage - the image of the origin under the transformation

J - the Jacobian of the image: an [imageDim x dim] matrix in row major order

formDegree - transform the quadrature weights as k-forms of this form degree (if the number of components is a multiple of (dim choose formDegree), it is assumed that they represent multiple k-forms) [see PetscDTAltVPullback() for interpretation of formDegree]

Jinvstarq - a quadrature rule where each point is the image of a point in the original quadrature rule, and where the k-form weights have been pulled-back by the pseudoinverse of J to the k-form weights in the image space.

The new quadrature rule will have a different number of components if spaces have different dimensions. For example, pushing a 2-form forward from a two dimensional space to a three dimensional space changes the number of components from 1 to 3.

PetscQuadrature, PetscDTAltVPullback(), PetscDTAltVPullbackMatrix()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscQuadraturePushForward(PetscQuadrature q, PetscInt imageDim, const PetscReal origin[], const PetscReal originImage[], const PetscReal J[], PetscInt formDegree, PetscQuadrature *Jinvstarq)
```

Example 2 (unknown):
```unknown
PetscDTAltVPullback()
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscDTAltVPullback()
```

---

## PetscQuadratureSetCellType#

**URL:** https://petsc.org/release/manualpages/DT/PetscQuadratureSetCellType/

**Contents:**
- PetscQuadratureSetCellType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the cell type of the integration domain

q - The PetscQuadrature object

ct - The cell type of the integration domain

PetscQuadrature, PetscQuadratureGetCellType(), PetscQuadratureGetData(), PetscQuadratureSetData()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscQuadratureSetCellType(PetscQuadrature q, DMPolytopeType ct)
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscQuadratureGetCellType()
```

---

## PetscQuadratureSetData#

**URL:** https://petsc.org/release/manualpages/DT/PetscQuadratureSetData/

**Contents:**
- PetscQuadratureSetData#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the data defining the quadrature

q - The PetscQuadrature object

dim - The spatial dimension

Nc - The number of components

npoints - The number of quadrature points

points - The coordinates of each quadrature point

weights - The weight of each quadrature point

q owns the references to points and weights, so they must be allocated using PetscMalloc() and the user should not free them.

PetscQuadrature, PetscQuadratureCreate(), PetscQuadratureGetData()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscQuadratureSetData(PetscQuadrature q, PetscInt dim, PetscInt Nc, PetscInt npoints, const PetscReal points[], const PetscReal weights[]) PeNSS
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
PetscMalloc()
```

Example 4 (unknown):
```unknown
PetscQuadrature
```

---

## PetscQuadratureSetNumComponents#

**URL:** https://petsc.org/release/manualpages/DT/PetscQuadratureSetNumComponents/

**Contents:**
- PetscQuadratureSetNumComponents#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the number of components for functions to be integrated

q - The PetscQuadrature object

Nc - The number of components

We are performing an integral \(\int f(x) w(x) dx\), where both \(f\) and \(w\) (the weight) have Nc components.

PetscQuadrature, PetscQuadratureGetNumComponents(), PetscQuadratureGetData(), PetscQuadratureSetData()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscQuadratureSetNumComponents(PetscQuadrature q, PetscInt Nc)
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscQuadratureGetNumComponents()
```

---

## PetscQuadratureSetOrder#

**URL:** https://petsc.org/release/manualpages/DT/PetscQuadratureSetOrder/

**Contents:**
- PetscQuadratureSetOrder#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the order of the method in the PetscQuadrature

q - The PetscQuadrature object

order - The order of the quadrature, i.e. the highest degree polynomial that is exactly integrated

PetscQuadrature, PetscQuadratureGetOrder(), PetscQuadratureGetData(), PetscQuadratureSetData()

src/dm/dt/interface/dt.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscQuadrature
```

Example 2 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscQuadratureSetOrder(PetscQuadrature q, PetscInt order)
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscQuadrature
```

---

## PetscQuadratureView#

**URL:** https://petsc.org/release/manualpages/DT/PetscQuadratureView/

**Contents:**
- PetscQuadratureView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

View a PetscQuadrature object

quad - The PetscQuadrature object

viewer - The PetscViewer object

PetscQuadrature, PetscViewer, PetscQuadratureCreate(), PetscQuadratureGetData()

src/dm/dt/interface/dt.c

src/dm/field/tutorials/ex1.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscQuadrature
```

Example 2 (unknown):
```unknown
#include "petscdt.h" 
PetscErrorCode PetscQuadratureView(PetscQuadrature quad, PetscViewer viewer)
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscQuadrature#

**URL:** https://petsc.org/release/manualpages/DT/PetscQuadrature/

**Contents:**
- PetscQuadrature#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Quadrature rule for numerical integration.

PetscQuadratureCreate(), PetscQuadratureDestroy()

src/ksp/ksp/tutorials/ex70.c src/ts/tutorials/ex18.c src/ksp/ksp/tutorials/ex35.cxx src/ts/tutorials/ex53.c src/ksp/ksp/tutorials/ex36.cxx src/dm/field/tutorials/ex1.c src/snes/tutorials/ex23.c src/snes/tutorials/ex64.c src/snes/tutorials/ex62.c

_p_PetscQuadrature in include/petsc/private/dtimpl.h

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_PetscQuadrature *PetscQuadrature;
```

Example 2 (unknown):
```unknown
PetscQuadratureCreate()
```

Example 3 (unknown):
```unknown
PetscQuadratureDestroy()
```

---

## PetscRiemannFn#

**URL:** https://petsc.org/release/manualpages/DT/PetscRiemannFn/

**Contents:**
- PetscRiemannFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

A prototype of a pointwise function that can be passed to, for example, PetscDSSetRiemannSolver()

dim - the coordinate dimension

Nf - The number of fields

x - The coordinates at a point on the interface

n - The normal vector to the interface

uL - The state vector to the left of the interface

uR - The state vector to the right of the interface

numConstants - number of constant parameters

constants - constant parameters

flux - output array of flux through the interface

ctx - optional application context

PetscPointFn, PetscDSSetRiemannSolver(), PetscDSGetRiemannSolver()

include/petscdstypes.h

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDSSetRiemannSolver()
```

Example 2 (cpp):
```cpp
PETSC_EXTERN_TYPEDEF typedef void PetscRiemannFn(PetscInt dim, PetscInt Nf, const PetscReal x[], const PetscReal n[], const PetscScalar uL[], const PetscScalar uR[], PetscInt numConstants, const PetscScalar constants[], PetscScalar flux[], PetscCtx ctx);
```

Example 3 (unknown):
```unknown
PetscPointFn
```

Example 4 (unknown):
```unknown
PetscDSSetRiemannSolver()
```

---

## PetscSimplePointFn#

**URL:** https://petsc.org/release/manualpages/DT/PetscSimplePointFn/

**Contents:**
- PetscSimplePointFn#
- Synopsis#
- Calling Sequence#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

A prototype of a simple pointwise function that can be passed to, for example, DMPlexTransformExtrudeSetNormalFunction()

dim - The coordinate dimension of the original mesh (usually a surface)

time - The current time, or 0.

x - The location of the current normal, in the coordinate space of the original mesh

r - The layer number of this point

u - The user provides the computed normal on output

ctx - An optional application context, this context may be obtained by the calling code with DMGetApplicationContext()

The handling of ctx in the use of such functions may not be ideal since the context is not provided when the function pointer is provided with, for example, DMSwarmSetCoordinateFunction()

PetscPointFn, DMPlexTransformExtrudeSetNormalFunction(), DMSwarmSetCoordinateFunction()

include/petscdstypes.h

src/snes/tutorials/ex71.c src/ts/tutorials/ex46.c src/ts/tutorials/ex76.c src/snes/tutorials/ex36.c src/snes/tutorials/ex27.c src/ts/tutorials/ex47.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMPlexTransformExtrudeSetNormalFunction()
```

Example 2 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode PetscSimplePointFn(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt r, PetscScalar u[], PetscCtx ctx);
```

Example 3 (unknown):
```unknown
DMGetApplicationContext()
```

Example 4 (unknown):
```unknown
DMSwarmSetCoordinateFunction()
```

---

## PetscSpaceCreateSubspace#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceCreateSubspace/

**Contents:**
- PetscSpaceCreateSubspace#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

creates a subspace from a an origSpace and its dual dualSubspace

origSpace - the original PetscSpace

dualSubspace - no idea

copymode - whether to copy, borrow, or own some of the input arrays I guess

subspace - the subspace

PetscSpace, PetscDualSpace, PetscCopyMode, PetscSpaceType

src/dm/dt/space/impls/subspace/spacesubspace.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
dualSubspace
```

Example 2 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscSpaceCreateSubspace(PetscSpace origSpace, PetscDualSpace dualSubspace, PetscReal *x, PetscReal *Jx, PetscReal *u, PetscReal *Ju, PetscCopyMode copymode, PetscSpace *subspace)
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscCopyMode
```

---

## PetscSpaceCreate#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceCreate/

**Contents:**
- PetscSpaceCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Creates an empty PetscSpace object. The type can then be set with PetscSpaceSetType().

comm - The communicator for the PetscSpace object

sp - The PetscSpace object

PetscSpace, PetscSpaceSetType(), PETSCSPACEPOLYNOMIAL

src/dm/dt/space/interface/space.c

PetscSpaceCreate_Point() in src/dm/dt/space/impls/point/spacepoint.c PetscSpaceCreate_Polynomial() in src/dm/dt/space/impls/poly/spacepoly.c PetscSpaceCreate_Ptrimmed() in src/dm/dt/space/impls/ptrimmed/spaceptrimmed.c PetscSpaceCreate_Subspace() in src/dm/dt/space/impls/subspace/spacesubspace.c PetscSpaceCreate_Sum() in src/dm/dt/space/impls/sum/spacesum.c PetscSpaceCreate_Tensor() in src/dm/dt/space/impls/tensor/spacetensor.c PetscSpaceCreate_WXY() in src/dm/dt/space/impls/wxy/spacewxy.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSpaceSetType()
```

Example 2 (unknown):
```unknown
#include "petscfe.h"  
PetscErrorCode PetscSpaceCreate(MPI_Comm comm, PetscSpace *sp)
```

Example 3 (unknown):
```unknown
PetscSpaceSetType()
```

Example 4 (unknown):
```unknown
PETSCSPACEPOLYNOMIAL
```

---

## PetscSpaceDestroy#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceDestroy/

**Contents:**
- PetscSpaceDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Destroys a PetscSpace object

sp - the PetscSpace object to destroy

PetscSpace, PetscSpaceCreate()

src/dm/dt/space/interface/space.c

PetscSpaceDestroy_Point() in src/dm/dt/space/impls/point/spacepoint.c PetscSpaceDestroy_Polynomial() in src/dm/dt/space/impls/poly/spacepoly.c PetscSpaceDestroy_Ptrimmed() in src/dm/dt/space/impls/ptrimmed/spaceptrimmed.c PetscSpaceDestroy_Subspace() in src/dm/dt/space/impls/subspace/spacesubspace.c PetscSpaceDestroy_Sum() in src/dm/dt/space/impls/sum/spacesum.c PetscSpaceDestroy_Tensor() in src/dm/dt/space/impls/tensor/spacetensor.c PetscSpaceDestroy_WXY() in src/dm/dt/space/impls/wxy/spacewxy.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h"  
PetscErrorCode PetscSpaceDestroy(PetscSpace *sp)
```

Example 2 (unknown):
```unknown
PetscSpaceCreate()
```

---

## PetscSpaceEvaluate#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceEvaluate/

**Contents:**
- PetscSpaceEvaluate#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Evaluate the basis functions and their derivatives (jet) at each point

npoints - The number of evaluation points, in reference coordinates

points - The point coordinates

B - The function evaluations in a npoints x nfuncs array

D - The derivative evaluations in a npoints x nfuncs x dim array

H - The second derivative evaluations in a npoints x nfuncs x dim x dim array

Above nfuncs is the dimension of the space, and dim is the spatial dimension. The coordinates are given on the reference cell, not in real space.

PetscSpace, PetscFECreateTabulation(), PetscFEGetCellTabulation(), PetscSpaceCreate()

src/dm/dt/space/interface/space.c

PetscSpaceEvaluate_Point() in src/dm/dt/space/impls/point/spacepoint.c PetscSpaceEvaluate_Polynomial() in src/dm/dt/space/impls/poly/spacepoly.c PetscSpaceEvaluate_Ptrimmed() in src/dm/dt/space/impls/ptrimmed/spaceptrimmed.c PetscSpaceEvaluate_Subspace() in src/dm/dt/space/impls/subspace/spacesubspace.c PetscSpaceEvaluate_Sum() in src/dm/dt/space/impls/sum/spacesum.c PetscSpaceEvaluate_Tensor() in src/dm/dt/space/impls/tensor/spacetensor.c PetscSpaceEvaluate_WXY() in src/dm/dt/space/impls/wxy/spacewxy.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h"  
PetscErrorCode PetscSpaceEvaluate(PetscSpace sp, PetscInt npoints, const PetscReal points[], PeOp PetscReal B[], PeOp PetscReal D[], PeOp PetscReal H[])
```

Example 2 (unknown):
```unknown
PetscFECreateTabulation()
```

Example 3 (unknown):
```unknown
PetscFEGetCellTabulation()
```

Example 4 (unknown):
```unknown
PetscSpaceCreate()
```

---

## PetscSpaceGetDegree#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceGetDegree/

**Contents:**
- PetscSpaceGetDegree#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Return the polynomial degrees that characterize this space

minDegree - The degree of the largest polynomial space contained in the space, pass NULL if not needed

maxDegree - The degree of the smallest polynomial space containing the space, pass NULL if not needed

PetscSpace, PetscSpaceSetDegree(), PetscSpaceGetDimension(), PetscSpaceCreate()

src/dm/dt/space/interface/space.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h"  
PetscErrorCode PetscSpaceGetDegree(PetscSpace sp, PeOp PetscInt *minDegree, PeOp PetscInt *maxDegree)
```

Example 2 (unknown):
```unknown
PetscSpaceSetDegree()
```

Example 3 (unknown):
```unknown
PetscSpaceGetDimension()
```

Example 4 (unknown):
```unknown
PetscSpaceCreate()
```

---

## PetscSpaceGetDimension#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceGetDimension/

**Contents:**
- PetscSpaceGetDimension#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Return the dimension of this space, i.e. the number of basis vectors

PetscSpace, PetscSpaceGetDegree(), PetscSpaceCreate()

src/dm/dt/space/interface/space.c

PetscSpaceGetDimension_Point() in src/dm/dt/space/impls/point/spacepoint.c PetscSpaceGetDimension_Polynomial() in src/dm/dt/space/impls/poly/spacepoly.c PetscSpaceGetDimension_Ptrimmed() in src/dm/dt/space/impls/ptrimmed/spaceptrimmed.c PetscSpaceGetDimension_Subspace() in src/dm/dt/space/impls/subspace/spacesubspace.c PetscSpaceGetDimension_Sum() in src/dm/dt/space/impls/sum/spacesum.c PetscSpaceGetDimension_Tensor() in src/dm/dt/space/impls/tensor/spacetensor.c PetscSpaceGetDimension_WXY() in src/dm/dt/space/impls/wxy/spacewxy.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h"  
PetscErrorCode PetscSpaceGetDimension(PetscSpace sp, PetscInt *dim)
```

Example 2 (unknown):
```unknown
PetscSpaceGetDegree()
```

Example 3 (unknown):
```unknown
PetscSpaceCreate()
```

---

## PetscSpaceGetHeightSubspace#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceGetHeightSubspace/

**Contents:**
- PetscSpaceGetHeightSubspace#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Get the subset of the primal space basis that is supported on a mesh point of a given height.

sp - the PetscSpace object

height - the height of the mesh point for which the subspace is desired

If the space is not defined on mesh points of the given height (e.g. if the space is discontinuous and pointwise values are not defined on the element boundaries), or if the implementation of PetscSpace does not support extracting subspaces, then NULL is returned.

This does not increment the reference count on the returned space, and the user should not destroy it.

PetscDualSpaceGetHeightSubspace(), PetscSpace

src/dm/dt/space/interface/space.c

PetscSpaceGetHeightSubspace_Polynomial() in src/dm/dt/space/impls/poly/spacepoly.c PetscSpaceGetHeightSubspace_Ptrimmed() in src/dm/dt/space/impls/ptrimmed/spaceptrimmed.c PetscSpaceGetHeightSubspace_Sum() in src/dm/dt/space/impls/sum/spacesum.c PetscSpaceGetHeightSubspace_Tensor() in src/dm/dt/space/impls/tensor/spacetensor.c PetscSpaceGetHeightSubspace_WXY() in src/dm/dt/space/impls/wxy/spacewxy.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h"  
PetscErrorCode PetscSpaceGetHeightSubspace(PetscSpace sp, PetscInt height, PetscSpace *subsp)
```

Example 2 (unknown):
```unknown
PetscDualSpaceGetHeightSubspace()
```

---

## PetscSpaceGetNumComponents#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceGetNumComponents/

**Contents:**
- PetscSpaceGetNumComponents#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Return the number of components for this space

Nc - The number of components

A vector space, for example, will have d components, where d is the spatial dimension

PetscSpace, PetscSpaceSetNumComponents(), PetscSpaceGetNumVariables(), PetscSpaceGetDimension(), PetscSpaceCreate()

src/dm/dt/space/interface/space.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h"  
PetscErrorCode PetscSpaceGetNumComponents(PetscSpace sp, PetscInt *Nc)
```

Example 2 (unknown):
```unknown
PetscSpaceSetNumComponents()
```

Example 3 (unknown):
```unknown
PetscSpaceGetNumVariables()
```

Example 4 (unknown):
```unknown
PetscSpaceGetDimension()
```

---

## PetscSpaceGetNumVariables#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceGetNumVariables/

**Contents:**
- PetscSpaceGetNumVariables#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Return the number of variables for this space

n - The number of variables, e.g. x, y, z…

PetscSpace, PetscSpaceSetNumVariables(), PetscSpaceGetNumComponents(), PetscSpaceGetDimension(), PetscSpaceCreate()

src/dm/dt/space/interface/space.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h"  
PetscErrorCode PetscSpaceGetNumVariables(PetscSpace sp, PetscInt *n)
```

Example 2 (unknown):
```unknown
PetscSpaceSetNumVariables()
```

Example 3 (unknown):
```unknown
PetscSpaceGetNumComponents()
```

Example 4 (unknown):
```unknown
PetscSpaceGetDimension()
```

---

## PetscSpaceGetType#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceGetType/

**Contents:**
- PetscSpaceGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the PetscSpaceType (as a string) from the object.

name - The PetscSpace type name

PetscSpaceType, PetscSpace, PetscSpaceSetType(), PetscSpaceCreate()

src/dm/dt/space/interface/space.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSpaceType
```

Example 2 (unknown):
```unknown
#include "petscfe.h"  
PetscErrorCode PetscSpaceGetType(PetscSpace sp, PetscSpaceType *name)
```

Example 3 (unknown):
```unknown
PetscSpaceType
```

Example 4 (unknown):
```unknown
PetscSpaceSetType()
```

---

## PetscSpacePointGetPoints#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpacePointGetPoints/

**Contents:**
- PetscSpacePointGetPoints#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the evaluation points for the space as the points of a quadrature rule

q - The PetscQuadrature defining the points

PetscSpace, PetscQuadrature, PetscSpaceCreate(), PetscSpaceSetType()

src/dm/dt/space/impls/point/spacepoint.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
#include "petscdt.h" 
PetscErrorCode PetscSpacePointGetPoints(PetscSpace sp, PetscQuadrature *q)
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscSpaceCreate()
```

---

## PetscSpacePointSetPoints#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpacePointSetPoints/

**Contents:**
- PetscSpacePointSetPoints#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the evaluation points for the space to coincide with the points of a quadrature rule

q - The PetscQuadrature defining the points

PetscSpace, PetscQuadrature, PetscSpaceCreate(), PetscSpaceSetType()

src/dm/dt/space/impls/point/spacepoint.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
#include "petscdt.h" 
PetscErrorCode PetscSpacePointSetPoints(PetscSpace sp, PetscQuadrature q)
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
PetscQuadrature
```

Example 4 (unknown):
```unknown
PetscSpaceCreate()
```

---

## PETSCSPACEPOINT#

**URL:** https://petsc.org/release/manualpages/SPACE/PETSCSPACEPOINT/

**Contents:**
- PETSCSPACEPOINT#
- See Also#
- Level#
- Location#

“point” - A PetscSpace object that encapsulates functions defined on a set of quadrature points.

PetscSpace, PetscSpaceType, PetscSpaceCreate(), PetscSpaceSetType()

src/dm/dt/space/impls/point/spacepoint.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSpaceType
```

Example 2 (unknown):
```unknown
PetscSpaceCreate()
```

Example 3 (unknown):
```unknown
PetscSpaceSetType()
```

---

## PetscSpacePolynomialGetTensor#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpacePolynomialGetTensor/

**Contents:**
- PetscSpacePolynomialGetTensor#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Get whether a function space is a space of tensor polynomials.

sp - the function space object

tensor - PETSC_TRUE for a tensor polynomial space, PETSC_FALSE for a polynomial space

The space is a tensor space if it is spanned by polynomials whose degree in each variable is bounded by the given order, as opposed to the space spanned by polynomials whose total degree—summing over all variables—is bounded by the given order.

PetscSpace, PetscSpacePolynomialSetTensor(), PetscSpaceSetDegree(), PetscSpaceSetNumVariables()

src/dm/dt/space/impls/poly/spacepoly.c

PetscSpacePolynomialGetTensor_Polynomial() in src/dm/dt/space/impls/poly/spacepoly.c PetscSpacePolynomialGetTensor_Subspace() in src/dm/dt/space/impls/subspace/spacesubspace.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscSpacePolynomialGetTensor(PetscSpace sp, PetscBool *tensor)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
PetscSpacePolynomialSetTensor()
```

Example 4 (unknown):
```unknown
PetscSpaceSetDegree()
```

---

## PetscSpacePolynomialSetTensor#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpacePolynomialSetTensor/

**Contents:**
- PetscSpacePolynomialSetTensor#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Set whether a function space is a space of tensor polynomials.

sp - the function space object

tensor - PETSC_TRUE for a tensor polynomial space, PETSC_FALSE for a polynomial space

-petscspace_poly_tensor (true|false) - Whether to use tensor product polynomials in higher dimension

It is a tensor space if it is spanned by polynomials whose degree in each variable is bounded by the given order, as opposed to the space spanned by polynomials whose total degree—summing over all variables—is bounded by the given order.

PetscSpace, PetscSpacePolynomialGetTensor(), PetscSpaceSetDegree(), PetscSpaceSetNumVariables()

src/dm/dt/space/impls/poly/spacepoly.c

PetscSpacePolynomialSetTensor_Polynomial() in src/dm/dt/space/impls/poly/spacepoly.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscSpacePolynomialSetTensor(PetscSpace sp, PetscBool tensor)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

Example 3 (unknown):
```unknown
PetscSpacePolynomialGetTensor()
```

Example 4 (unknown):
```unknown
PetscSpaceSetDegree()
```

---

## PETSCSPACEPOLYNOMIAL#

**URL:** https://petsc.org/release/manualpages/SPACE/PETSCSPACEPOLYNOMIAL/

**Contents:**
- PETSCSPACEPOLYNOMIAL#
- See Also#
- Level#
- Location#

“poly” - A PetscSpace object that encapsulates a polynomial space, e.g. P1 is the space of linear polynomials. The space is replicated for each component.

PetscSpace, PetscSpaceType, PetscSpaceCreate(), PetscSpaceSetType()

src/dm/dt/space/impls/poly/spacepoly.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSpaceType
```

Example 2 (unknown):
```unknown
PetscSpaceCreate()
```

Example 3 (unknown):
```unknown
PetscSpaceSetType()
```

---

## PetscSpacePTrimmedGetFormDegree#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpacePTrimmedGetFormDegree/

**Contents:**
- PetscSpacePTrimmedGetFormDegree#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get the form degree of the trimmed polynomials.

sp - the function space object

formDegree - the form degree

PetscSpace, PetscDTAltV, PetscDTPTrimmedEvalJet(), PetscSpacePTrimmedSetFormDegree()

src/dm/dt/space/impls/ptrimmed/spaceptrimmed.c

PetscSpacePTrimmedGetFormDegree_Ptrimmed() in src/dm/dt/space/impls/ptrimmed/spaceptrimmed.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscSpacePTrimmedGetFormDegree(PetscSpace sp, PetscInt *formDegree)
```

Example 2 (unknown):
```unknown
PetscDTAltV
```

Example 3 (unknown):
```unknown
PetscDTPTrimmedEvalJet()
```

Example 4 (unknown):
```unknown
PetscSpacePTrimmedSetFormDegree()
```

---

## PetscSpacePTrimmedSetFormDegree#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpacePTrimmedSetFormDegree/

**Contents:**
- PetscSpacePTrimmedSetFormDegree#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

Set the form degree of the trimmed polynomials.

sp - the function space object

formDegree - the form degree

-petscspace_ptrimmed_form_degree degree - The trimmed polynomial form degree

PetscSpace, PetscDTAltV, PetscDTPTrimmedEvalJet(), PetscSpacePTrimmedGetFormDegree()

src/dm/dt/space/impls/ptrimmed/spaceptrimmed.c

PetscSpacePTrimmedSetFormDegree_Ptrimmed() in src/dm/dt/space/impls/ptrimmed/spaceptrimmed.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscSpacePTrimmedSetFormDegree(PetscSpace sp, PetscInt formDegree)
```

Example 2 (unknown):
```unknown
PetscDTAltV
```

Example 3 (unknown):
```unknown
PetscDTPTrimmedEvalJet()
```

Example 4 (unknown):
```unknown
PetscSpacePTrimmedGetFormDegree()
```

---

## PETSCSPACEPTRIMMED#

**URL:** https://petsc.org/release/manualpages/SPACE/PETSCSPACEPTRIMMED/

**Contents:**
- PETSCSPACEPTRIMMED#
- Notes#
- Trimmed polynomial spaces correspond to several common conformal approximation spaces in the de Rham complex#
- See Also#
- Level#
- Location#

“ptrimmed” - A PetscSpace object that encapsulates a trimmed polynomial space. Trimmed polynomial spaces are defined for \(k\)-forms, and are defined by \( \mathcal{P}^-_r \Lambda^k(\mathbb{R}^n) = mathcal{P}_{r-1} \Lambda^k(\mathbb{R}^n) \oplus \kappa [\mathcal{H}_{r-1} \Lambda^{k+1}(\mathbb{R}^n)], \) where \(\mathcal{H}_{r-1}\) are homogeneous polynomials and \(\kappa\) is the Koszul differential. This decomposition is detailed in ``Finite element exterior calculus’’, Arnold, 2018.

In \(H^1\) (\(\sim k=0\)), trimmed polynomial spaces are identical to the standard polynomial spaces, \(\mathcal{P}_r^- \sim P_r\).

In \(H(\text{curl})\), (\(\sim k=1\)), trimmed polynomial spaces are equivalent to \(H(\text{curl})\)-Nedelec spaces of the first kind and can be written as \( \begin{cases} [P_{r-1}(\mathbb{R}^2)]^2 \oplus \mathrm{rot}(\bf{x}) H_{r-1}(\mathbb{R}^2), & n = 2, \\ [P_{r-1}(\mathbb{R}^3)]^3 \oplus \bf{x} \times [H_{r-1}(\mathbb{R}^3)]^3, & n = 3. \end{cases} \)

In \(H(\text{div})\) (\(\sim k=n-1\)), trimmed polynomial spaces are equivalent to Raviart-Thomas spaces (\(n=2\)) and \(H(\text{div})\)-Nedelec spaces of the first kind (\(n=3\)), and can be written as \( [P_{r-1}(\mathbb{R}^n)]^n \oplus \bf{x} H_{r-1}(\mathbb{R}^n). \)

In \(L_2\), (\(\sim k=n\)), trimmed polynomial spaces are identical to the standard polynomial spaces of one degree less, \(\mathcal{P}_r^- \sim P_{r-1}\).

PetscSpace, PetscSpaceType, PetscSpaceCreate(), PetscSpaceSetType(), PetscDTPTrimmedEvalJet()

src/dm/dt/space/impls/ptrimmed/spaceptrimmed.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSpaceType
```

Example 2 (unknown):
```unknown
PetscSpaceCreate()
```

Example 3 (unknown):
```unknown
PetscSpaceSetType()
```

Example 4 (unknown):
```unknown
PetscDTPTrimmedEvalJet()
```

---

## PetscSpaceRegister#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceRegister/

**Contents:**
- PetscSpaceRegister#
- Synopsis#
- Input Parameters#
- Example Usage#
- Note#
- See Also#
- Level#
- Location#

Adds a new PetscSpace implementation

Not Collective, No Fortran Support

sname - The name of a new user-defined creation routine

function - The creation routine for the implementation type

Then, your PetscSpace type can be chosen with the procedural interface via

or at runtime via the option

PetscSpaceRegister() may be called multiple times to add several user-defined types of PetscSpace. The creation function is called when the type is set to ‘name’.

PetscSpace, PetscSpaceRegisterAll(), PetscSpaceRegisterDestroy()

src/dm/dt/space/interface/space.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h"  
PetscErrorCode PetscSpaceRegister(const char sname[], PetscErrorCode (*function)(PetscSpace))
```

Example 2 (unknown):
```unknown
PetscSpaceRegister("my_space", MyPetscSpaceCreate);
```

Example 3 (unknown):
```unknown
PetscSpaceCreate(MPI_Comm, PetscSpace *);
    PetscSpaceSetType(PetscSpace, "my_space");
```

Example 4 (unknown):
```unknown
-petscspace_type my_space
```

---

## PetscSpaceSetDegree#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceSetDegree/

**Contents:**
- PetscSpaceSetDegree#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the degree of approximation for this space.

degree - The degree of the largest polynomial space contained in the space

maxDegree - The degree of the largest polynomial space containing the space. One of degree and maxDegree can be PETSC_DETERMINE.

PetscSpace, PetscSpaceGetDegree(), PetscSpaceCreate()

src/dm/dt/space/interface/space.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h"  
PetscErrorCode PetscSpaceSetDegree(PetscSpace sp, PetscInt degree, PetscInt maxDegree)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
PetscSpaceGetDegree()
```

Example 4 (unknown):
```unknown
PetscSpaceCreate()
```

---

## PetscSpaceSetFromOptions#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceSetFromOptions/

**Contents:**
- PetscSpaceSetFromOptions#
- Synopsis#
- Input Parameter#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Implementations#

sets parameters in a PetscSpace from the options database

sp - the PetscSpace object to set options for

-petscspace_degree deg - the degree of the space

-petscspace_variables n - the number of different variables, e.g. x and y

-petscspace_components c - the number of components, say d for a vector field

PetscSpace, PetscSpaceView()

src/dm/dt/space/interface/space.c

PetscSpaceSetFromOptions_Polynomial() in src/dm/dt/space/impls/poly/spacepoly.c PetscSpaceSetFromOptions_Ptrimmed() in src/dm/dt/space/impls/ptrimmed/spaceptrimmed.c PetscSpaceSetFromOptions_Sum() in src/dm/dt/space/impls/sum/spacesum.c PetscSpaceSetFromOptions_Tensor() in src/dm/dt/space/impls/tensor/spacetensor.c PetscSpaceSetFromOptions_WXY() in src/dm/dt/space/impls/wxy/spacewxy.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h"  
PetscErrorCode PetscSpaceSetFromOptions(PetscSpace sp)
```

Example 2 (unknown):
```unknown
PetscSpaceView()
```

---

## PetscSpaceSetNumComponents#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceSetNumComponents/

**Contents:**
- PetscSpaceSetNumComponents#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the number of components for this space

Nc - The number of components

PetscSpace, PetscSpaceGetNumComponents(), PetscSpaceSetNumVariables(), PetscSpaceCreate()

src/dm/dt/space/interface/space.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h"  
PetscErrorCode PetscSpaceSetNumComponents(PetscSpace sp, PetscInt Nc)
```

Example 2 (unknown):
```unknown
PetscSpaceGetNumComponents()
```

Example 3 (unknown):
```unknown
PetscSpaceSetNumVariables()
```

Example 4 (unknown):
```unknown
PetscSpaceCreate()
```

---

## PetscSpaceSetNumVariables#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceSetNumVariables/

**Contents:**
- PetscSpaceSetNumVariables#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the number of variables for this space

n - The number of variables, e.g. x, y, z…

PetscSpace, PetscSpaceGetNumVariables(), PetscSpaceSetNumComponents(), PetscSpaceCreate()

src/dm/dt/space/interface/space.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h"  
PetscErrorCode PetscSpaceSetNumVariables(PetscSpace sp, PetscInt n)
```

Example 2 (unknown):
```unknown
PetscSpaceGetNumVariables()
```

Example 3 (unknown):
```unknown
PetscSpaceSetNumComponents()
```

Example 4 (unknown):
```unknown
PetscSpaceCreate()
```

---

## PetscSpaceSetType#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceSetType/

**Contents:**
- PetscSpaceSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Builds a particular PetscSpace

sp - The PetscSpace object

name - The kind of space

-petscspace_type type - Sets the PetscSpace type; use -help for a list of available types

PetscSpace, PetscSpaceType, PetscSpaceGetType(), PetscSpaceCreate()

src/dm/dt/space/interface/space.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h"  
PetscErrorCode PetscSpaceSetType(PetscSpace sp, PetscSpaceType name)
```

Example 2 (unknown):
```unknown
PetscSpaceType
```

Example 3 (unknown):
```unknown
PetscSpaceGetType()
```

Example 4 (unknown):
```unknown
PetscSpaceCreate()
```

---

## PetscSpaceSetUp#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceSetUp/

**Contents:**
- PetscSpaceSetUp#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Construct data structures for the PetscSpace

sp - the PetscSpace object to setup

PetscSpace, PetscSpaceView(), PetscSpaceDestroy()

src/dm/dt/space/interface/space.c

PetscSpaceSetUp_Point() in src/dm/dt/space/impls/point/spacepoint.c PetscSpaceSetUp_Polynomial() in src/dm/dt/space/impls/poly/spacepoly.c PetscSpaceSetUp_Ptrimmed() in src/dm/dt/space/impls/ptrimmed/spaceptrimmed.c PetscSpaceSetUp_Subspace() in src/dm/dt/space/impls/subspace/spacesubspace.c PetscSpaceSetUp_Sum() in src/dm/dt/space/impls/sum/spacesum.c PetscSpaceSetUp_Tensor() in src/dm/dt/space/impls/tensor/spacetensor.c PetscSpaceSetUp_WXY() in src/dm/dt/space/impls/wxy/spacewxy.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h"  
PetscErrorCode PetscSpaceSetUp(PetscSpace sp)
```

Example 2 (unknown):
```unknown
PetscSpaceView()
```

Example 3 (unknown):
```unknown
PetscSpaceDestroy()
```

---

## PetscSpaceSumGetConcatenate#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceSumGetConcatenate/

**Contents:**
- PetscSpaceSumGetConcatenate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Get the concatenate flag for this space.

sp - the function space object

concatenate - flag indicating whether subspaces are concatenated.

A concatenated sum space will have the number of components equal to the sum of the number of components of all subspaces. A non-concatenated, or direct sum space will have the same number of components as its subspaces.

PETSCSPACESUM, PetscSpace, PetscSpaceSumSetConcatenate()

src/dm/dt/space/impls/sum/spacesum.c

PetscSpaceSumGetConcatenate_Sum() in src/dm/dt/space/impls/sum/spacesum.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscSpaceSumGetConcatenate(PetscSpace sp, PetscBool *concatenate)
```

Example 2 (unknown):
```unknown
PETSCSPACESUM
```

Example 3 (unknown):
```unknown
PetscSpaceSumSetConcatenate()
```

---

## PetscSpaceSumGetInterleave#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceSumGetInterleave/

**Contents:**
- PetscSpaceSumGetInterleave#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Get whether the basis functions and components of a uniform sum are interleaved

sp - a PetscSpace of type PETSCSPACESUM

interleave_basis - if PETSC_TRUE, the basis vectors of the subspaces are interleaved

interleave_components - if PETSC_TRUE and the space concatenates components (PetscSpaceSumGetConcatenate()), interleave the concatenated components

PetscSpace, PETSCSPACESUM, PETSCFEVECTOR, PetscSpaceSumSetInterleave()

src/dm/dt/space/impls/sum/spacesum.c

PetscSpaceSumGetInterleave_Sum() in src/dm/dt/space/impls/sum/spacesum.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscSpaceSumGetInterleave(PetscSpace sp, PeOp PetscBool *interleave_basis, PeOp PetscBool *interleave_components)
```

Example 2 (unknown):
```unknown
PETSCSPACESUM
```

Example 3 (unknown):
```unknown
PetscSpaceSumGetConcatenate()
```

Example 4 (unknown):
```unknown
PETSCSPACESUM
```

---

## PetscSpaceSumGetNumSubspaces#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceSumGetNumSubspaces/

**Contents:**
- PetscSpaceSumGetNumSubspaces#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Get the number of spaces in the sum space

sp - the function space object

numSumSpaces - the number of spaces

The name NumSubspaces is slightly misleading because it is actually getting the number of defining spaces of the sum, not a number of Subspaces of it

PETSCSPACESUM, PetscSpace, PetscSpaceSumSetNumSubspaces(), PetscSpaceSetDegree(), PetscSpaceSetNumVariables()

src/dm/dt/space/impls/sum/spacesum.c

PetscSpaceSumGetNumSubspaces_Sum() in src/dm/dt/space/impls/sum/spacesum.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscSpaceSumGetNumSubspaces(PetscSpace sp, PetscInt *numSumSpaces)
```

Example 2 (unknown):
```unknown
PETSCSPACESUM
```

Example 3 (unknown):
```unknown
PetscSpaceSumSetNumSubspaces()
```

Example 4 (unknown):
```unknown
PetscSpaceSetDegree()
```

---

## PetscSpaceSumGetSubspace#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceSumGetSubspace/

**Contents:**
- PetscSpaceSumGetSubspace#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Get a space in the sum space

sp - the function space object

subsp - the PetscSpace

The name GetSubspace is slightly misleading because it is actually getting one of the defining spaces of the sum, not a Subspace of it

PETSCSPACESUM, PetscSpace, PetscSpaceSumSetSubspace(), PetscSpaceSetDegree(), PetscSpaceSetNumVariables()

src/dm/dt/space/impls/sum/spacesum.c

PetscSpaceSumGetSubspace_Sum() in src/dm/dt/space/impls/sum/spacesum.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscSpaceSumGetSubspace(PetscSpace sp, PetscInt s, PetscSpace *subsp)
```

Example 2 (unknown):
```unknown
PETSCSPACESUM
```

Example 3 (unknown):
```unknown
PetscSpaceSumSetSubspace()
```

Example 4 (unknown):
```unknown
PetscSpaceSetDegree()
```

---

## PetscSpaceSumSetConcatenate#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceSumSetConcatenate/

**Contents:**
- PetscSpaceSumSetConcatenate#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Sets the concatenate flag for this space.

sp - the function space object

concatenate - are subspaces concatenated components (true) or direct summands (false)

A concatenated sum space will have the number of components equal to the sum of the number of components of all subspaces. A non-concatenated, or direct sum space will have the same number of components as its subspaces .

PETSCSPACESUM, PetscSpace, PetscSpaceSumGetConcatenate()

src/dm/dt/space/impls/sum/spacesum.c

PetscSpaceSumSetConcatenate_Sum() in src/dm/dt/space/impls/sum/spacesum.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscSpaceSumSetConcatenate(PetscSpace sp, PetscBool concatenate)
```

Example 2 (unknown):
```unknown
PETSCSPACESUM
```

Example 3 (unknown):
```unknown
PetscSpaceSumGetConcatenate()
```

---

## PetscSpaceSumSetInterleave#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceSumSetInterleave/

**Contents:**
- PetscSpaceSumSetInterleave#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set whether the basis functions and components of a uniform sum are interleaved

sp - a PetscSpace of type PETSCSPACESUM

interleave_basis - if PETSC_TRUE, the basis vectors of the subspaces are interleaved

interleave_components - if PETSC_TRUE and the space concatenates components (PetscSpaceSumGetConcatenate()), interleave the concatenated components

PetscSpace, PETSCSPACESUM, PETSCFEVECTOR, PetscSpaceSumGetInterleave()

src/dm/dt/space/impls/sum/spacesum.c

PetscSpaceSumSetInterleave_Sum() in src/dm/dt/space/impls/sum/spacesum.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscSpaceSumSetInterleave(PetscSpace sp, PetscBool interleave_basis, PetscBool interleave_components)
```

Example 2 (unknown):
```unknown
PETSCSPACESUM
```

Example 3 (unknown):
```unknown
PetscSpaceSumGetConcatenate()
```

Example 4 (unknown):
```unknown
PETSCSPACESUM
```

---

## PetscSpaceSumSetNumSubspaces#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceSumSetNumSubspaces/

**Contents:**
- PetscSpaceSumSetNumSubspaces#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Set the number of spaces in the sum space

sp - the function space object

numSumSpaces - the number of spaces

The name NumSubspaces is slightly misleading because it is actually setting the number of defining spaces of the sum, not a number of Subspaces of it

PETSCSPACESUM, PetscSpace, PetscSpaceSumGetNumSubspaces(), PetscSpaceSetDegree(), PetscSpaceSetNumVariables()

src/dm/dt/space/impls/sum/spacesum.c

PetscSpaceSumSetNumSubspaces_Sum() in src/dm/dt/space/impls/sum/spacesum.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscSpaceSumSetNumSubspaces(PetscSpace sp, PetscInt numSumSpaces)
```

Example 2 (unknown):
```unknown
PETSCSPACESUM
```

Example 3 (unknown):
```unknown
PetscSpaceSumGetNumSubspaces()
```

Example 4 (unknown):
```unknown
PetscSpaceSetDegree()
```

---

## PetscSpaceSumSetSubspace#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceSumSetSubspace/

**Contents:**
- PetscSpaceSumSetSubspace#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Set a space in the sum space

sp - the function space object

subsp - the number of spaces

The name SetSubspace is slightly misleading because it is actually setting one of the defining spaces of the sum, not a Subspace of it

PETSCSPACESUM, PetscSpace, PetscSpaceSumGetSubspace(), PetscSpaceSetDegree(), PetscSpaceSetNumVariables()

src/dm/dt/space/impls/sum/spacesum.c

PetscSpaceSumSetSubspace_Sum() in src/dm/dt/space/impls/sum/spacesum.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscSpaceSumSetSubspace(PetscSpace sp, PetscInt s, PetscSpace subsp)
```

Example 2 (unknown):
```unknown
PETSCSPACESUM
```

Example 3 (unknown):
```unknown
PetscSpaceSumGetSubspace()
```

Example 4 (unknown):
```unknown
PetscSpaceSetDegree()
```

---

## PETSCSPACESUM#

**URL:** https://petsc.org/release/manualpages/SPACE/PETSCSPACESUM/

**Contents:**
- PETSCSPACESUM#
- Note#
- See Also#
- Level#
- Location#

“sum” - A PetscSpace object that encapsulates a sum of subspaces.

That sum can either be direct or a concatenation. For example if A and B are spaces each with 2 components, the direct sum of A and B will also have 2 components while the concatenated sum will have 4 components. In both cases A and B must be defined over the same number of variables.

PetscSpace, PetscSpaceType, PetscSpaceCreate(), PetscSpaceSetType(), PetscSpaceSumGetNumSubspaces(), PetscSpaceSumSetNumSubspaces(), PetscSpaceSumGetConcatenate(), PetscSpaceSumSetConcatenate()

src/dm/dt/space/impls/sum/spacesum.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSpaceType
```

Example 2 (unknown):
```unknown
PetscSpaceCreate()
```

Example 3 (unknown):
```unknown
PetscSpaceSetType()
```

Example 4 (unknown):
```unknown
PetscSpaceSumGetNumSubspaces()
```

---

## PetscSpaceTensorGetNumSubspaces#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceTensorGetNumSubspaces/

**Contents:**
- PetscSpaceTensorGetNumSubspaces#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Get the number of spaces in the tensor product space

sp - the function space object

numTensSpaces - the number of spaces

The name NumSubspaces is misleading because it is actually getting the number of defining spaces of the tensor product space, not a number of Subspaces of it

PETSCSPACETENSOR, PetscSpace, PetscSpaceTensorSetNumSubspaces(), PetscSpaceSetDegree(), PetscSpaceSetNumVariables()

src/dm/dt/space/impls/tensor/spacetensor.c

PetscSpaceTensorGetNumSubspaces_Tensor() in src/dm/dt/space/impls/tensor/spacetensor.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscSpaceTensorGetNumSubspaces(PetscSpace sp, PetscInt *numTensSpaces)
```

Example 2 (unknown):
```unknown
PETSCSPACETENSOR
```

Example 3 (unknown):
```unknown
PetscSpaceTensorSetNumSubspaces()
```

Example 4 (unknown):
```unknown
PetscSpaceSetDegree()
```

---

## PetscSpaceTensorGetSubspace#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceTensorGetSubspace/

**Contents:**
- PetscSpaceTensorGetSubspace#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Get a space in the tensor product space

sp - the function space object

subsp - the PetscSpace

The name GetSubspace is misleading because it is actually getting one of the defining spaces of the tensor product space, not a Subspace of it

PETSCSPACETENSOR, PetscSpace, PetscSpaceTensorSetSubspace(), PetscSpaceSetDegree(), PetscSpaceSetNumVariables()

src/dm/dt/space/impls/tensor/spacetensor.c

PetscSpaceTensorGetSubspace_Tensor() in src/dm/dt/space/impls/tensor/spacetensor.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscSpaceTensorGetSubspace(PetscSpace sp, PetscInt s, PetscSpace *subsp)
```

Example 2 (unknown):
```unknown
PETSCSPACETENSOR
```

Example 3 (unknown):
```unknown
PetscSpaceTensorSetSubspace()
```

Example 4 (unknown):
```unknown
PetscSpaceSetDegree()
```

---

## PetscSpaceTensorSetNumSubspaces#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceTensorSetNumSubspaces/

**Contents:**
- PetscSpaceTensorSetNumSubspaces#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Set the number of spaces in the tensor product space

sp - the function space object

numTensSpaces - the number of spaces

The name NumSubspaces is misleading because it is actually setting the number of defining spaces of the tensor product space, not a number of Subspaces of it

PETSCSPACETENSOR, PetscSpace, PetscSpaceTensorGetNumSubspaces(), PetscSpaceSetDegree(), PetscSpaceSetNumVariables()

src/dm/dt/space/impls/tensor/spacetensor.c

PetscSpaceTensorSetNumSubspaces_Tensor() in src/dm/dt/space/impls/tensor/spacetensor.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscSpaceTensorSetNumSubspaces(PetscSpace sp, PetscInt numTensSpaces)
```

Example 2 (unknown):
```unknown
PETSCSPACETENSOR
```

Example 3 (unknown):
```unknown
PetscSpaceTensorGetNumSubspaces()
```

Example 4 (unknown):
```unknown
PetscSpaceSetDegree()
```

---

## PetscSpaceTensorSetSubspace#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceTensorSetSubspace/

**Contents:**
- PetscSpaceTensorSetSubspace#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Set a space in the tensor product space

sp - the function space object

subsp - the number of spaces

The name SetSubspace is misleading because it is actually setting one of the defining spaces of the tensor product space, not a Subspace of it

PETSCSPACETENSOR, PetscSpace, PetscSpaceTensorGetSubspace(), PetscSpaceSetDegree(), PetscSpaceSetNumVariables()

src/dm/dt/space/impls/tensor/spacetensor.c

PetscSpaceTensorSetSubspace_Tensor() in src/dm/dt/space/impls/tensor/spacetensor.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscSpaceTensorSetSubspace(PetscSpace sp, PetscInt s, PetscSpace subsp)
```

Example 2 (unknown):
```unknown
PETSCSPACETENSOR
```

Example 3 (unknown):
```unknown
PetscSpaceTensorGetSubspace()
```

Example 4 (unknown):
```unknown
PetscSpaceSetDegree()
```

---

## PETSCSPACETENSOR#

**URL:** https://petsc.org/release/manualpages/SPACE/PETSCSPACETENSOR/

**Contents:**
- PETSCSPACETENSOR#
- See Also#
- Level#
- Location#

“tensor” - A PetscSpace object that encapsulates a tensor product space. A tensor product is created of the components of the subspaces as well.

PetscSpace, PetscSpaceType, PetscSpaceCreate(), PetscSpaceSetType(), PetscSpaceTensorGetSubspace(), PetscSpaceTensorSetSubspace(), PetscSpaceTensorGetNumSubspaces(), PetscSpaceTensorSetNumSubspaces()

src/dm/dt/space/impls/tensor/spacetensor.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSpaceType
```

Example 2 (unknown):
```unknown
PetscSpaceCreate()
```

Example 3 (unknown):
```unknown
PetscSpaceSetType()
```

Example 4 (unknown):
```unknown
PetscSpaceTensorGetSubspace()
```

---

## PetscSpaceType#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceType/

**Contents:**
- PetscSpaceType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

String with the name of a PETSc linear space

PETSCSPACEPOLYNOMIAL - a polynomial space, e.g. P1 is the space of linear polynomials

PETSCSPACEPTRIMMED - a trimmed polynomial space

PETSCSPACETENSOR - a space consisting of the tensor product of two or more spaces

PETSCSPACESUM - a direct or a concatenation sum

PETSCSPACEPOINT - functions defined by values on a set of quadrature points

PETSCSPACESUBSPACE - some kind of subspace, no idea what

PETSCSPACEWXY - space that encapsulates the Wheeler-Xu-Yotov enrichments

PetscSpaceSetType(), PetscSpace, PetscSpaceType

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef const char *PetscSpaceType;
#define PETSCSPACEPOLYNOMIAL "poly"
#define PETSCSPACEPTRIMMED   "ptrimmed"
#define PETSCSPACETENSOR     "tensor"
#define PETSCSPACESUM        "sum"
#define PETSCSPACEPOINT      "point"
#define PETSCSPACESUBSPACE   "subspace"
#define PETSCSPACEWXY        "wxy"
```

Example 2 (unknown):
```unknown
PETSCSPACEPOLYNOMIAL
```

Example 3 (unknown):
```unknown
PETSCSPACEPTRIMMED
```

Example 4 (unknown):
```unknown
PETSCSPACETENSOR
```

---

## PetscSpaceViewFromOptions#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceViewFromOptions/

**Contents:**
- PetscSpaceViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

View a PetscSpace based on values in the options database

A - the PetscSpace object

obj - Optional object that provides the options name prefix

name - command line option name

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

PetscSpace, PetscSpaceView(), PetscObjectViewFromOptions(), PetscSpaceCreate()

src/dm/dt/space/interface/space.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h"  
PetscErrorCode PetscSpaceViewFromOptions(PetscSpace A, PetscObject obj, const char name[])
```

Example 2 (unknown):
```unknown
PetscObjectViewFromOptions()
```

Example 3 (unknown):
```unknown
PetscSpaceView()
```

Example 4 (unknown):
```unknown
PetscObjectViewFromOptions()
```

---

## PetscSpaceView#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpaceView/

**Contents:**
- PetscSpaceView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

sp - the PetscSpace object to view

PetscSpace, PetscViewer, PetscSpaceViewFromOptions(), PetscSpaceDestroy()

src/dm/dt/space/interface/space.c

PetscSpaceView_Point() in src/dm/dt/space/impls/point/spacepoint.c PetscSpaceView_Polynomial() in src/dm/dt/space/impls/poly/spacepoly.c PetscSpaceView_Ptrimmed() in src/dm/dt/space/impls/ptrimmed/spaceptrimmed.c PetscSpaceView_Subspace() in src/dm/dt/space/impls/subspace/spacesubspace.c PetscSpaceView_Sum() in src/dm/dt/space/impls/sum/spacesum.c PetscSpaceView_Tensor() in src/dm/dt/space/impls/tensor/spacetensor.c PetscSpaceView_WXY() in src/dm/dt/space/impls/wxy/spacewxy.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h"  
PetscErrorCode PetscSpaceView(PetscSpace sp, PetscViewer v)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscSpaceViewFromOptions()
```

Example 4 (unknown):
```unknown
PetscSpaceDestroy()
```

---

## PETSCSPACEWXY#

**URL:** https://petsc.org/release/manualpages/SPACE/PETSCSPACEWXY/

**Contents:**
- PETSCSPACEWXY#
- Note#
- See Also#
- Level#
- Location#

“wxy” - A PetscSpace object that encapsulates the Wheeler-Xu-Yotov enrichments.

PetscSpace, PetscSpaceType, PetscSpaceCreate(), PetscSpaceSetType()

src/dm/dt/space/impls/wxy/spacewxy.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
curl {{0, 0, y^2 z}, {x z^2, 0, 0}, {y z^2, 0, 0}, {0, -x z^2, 0}, {0, -3/2 x^2 z, -1/2 x^2 y}, {3/2 y^2 z, 0, 1/2 y^2 x}}
  = {{2 y z, 0, 0}, {0, 2 x z, 0}, {0, 2 y z, -z^2}, {2 x z, 0, -z^2}, {x^2, x y, -3 x z}, {x y, y^2, -3 y z}}
```

Example 2 (unknown):
```unknown
PetscSpaceType
```

Example 3 (unknown):
```unknown
PetscSpaceCreate()
```

Example 4 (unknown):
```unknown
PetscSpaceSetType()
```

---

## PetscSpace#

**URL:** https://petsc.org/release/manualpages/SPACE/PetscSpace/

**Contents:**
- PetscSpace#
- Synopsis#
- See Also#
- Level#
- Location#
- Implementations#

PETSc object that manages a linear (vector) space of multi-component d-dimensional functions. For example, polynomials of given degree.

PetscSpaceCreate(), PetscDualSpace, PetscDualSpaceCreate(), PetscSpaceSetType(), PetscSpaceType, PetscFE

_p_PetscSpace in include/petsc/private/petscfeimpl.h PetscSpace_Poly in include/petsc/private/petscfeimpl.h PetscSpace_Ptrimmed in include/petsc/private/petscfeimpl.h PetscSpace_Tensor in include/petsc/private/petscfeimpl.h PetscSpace_Sum in include/petsc/private/petscfeimpl.h PetscSpace_Point in include/petsc/private/petscfeimpl.h PetscSpace_WXY in include/petsc/private/petscfeimpl.h PetscSpace_Subspace in src/dm/dt/space/impls/subspace/spacesubspace.c

Index of all SPACE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_PetscSpace *PetscSpace;
```

Example 2 (unknown):
```unknown
PetscSpaceCreate()
```

Example 3 (unknown):
```unknown
PetscDualSpace
```

Example 4 (unknown):
```unknown
PetscDualSpaceCreate()
```

---

## PetscTabulationDestroy#

**URL:** https://petsc.org/release/manualpages/FE/PetscTabulationDestroy/

**Contents:**
- PetscTabulationDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Frees memory from the associated tabulation.

PetscTabulation, PetscFECreateTabulation(), PetscFEGetCellTabulation()

src/dm/dt/fe/interface/fe.c

Index of all FE routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscfe.h" 
PetscErrorCode PetscTabulationDestroy(PetscTabulation *T)
```

Example 2 (unknown):
```unknown
PetscTabulation
```

Example 3 (unknown):
```unknown
PetscFECreateTabulation()
```

Example 4 (unknown):
```unknown
PetscFEGetCellTabulation()
```

---

## PetscTabulation#

**URL:** https://petsc.org/release/manualpages/DT/PetscTabulation/

**Contents:**
- PetscTabulation#
- Synopsis#
- Note#
- Fortran Note#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

PETSc object that manages tabulations for finite element methods.

This is a pointer to a C struct, hence the data in it may be accessed directly.

Use PetscTabulationGetData() and PetscTabulationRestoreData() to access the arrays in the tabulation.

TODO: put the meaning of the struct fields in this manual page

PetscTabulationDestroy(), PetscFECreateTabulation(), PetscFEGetCellTabulation()

src/dm/impls/plex/tutorials/ex4f90.F90

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _n_PetscTabulation *PetscTabulation;
```

Example 2 (unknown):
```unknown
PetscTabulationGetData()
```

Example 3 (unknown):
```unknown
PetscTabulationRestoreData()
```

Example 4 (unknown):
```unknown
PetscTabulationDestroy()
```

---

## PetscWeakFormAddBdJacobian#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormAddBdJacobian/

**Contents:**
- PetscWeakFormAddBdJacobian#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Append boundary Jacobian pointwise functions g0, g1, g2, and g3 to the lists for a given key in a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the boundary region, or NULL for the entire boundary

val - The label value selecting the boundary region

f - The test field number

g - The trial field number

part - The equation part, or 0 if unused

g0 - The g0 boundary Jacobian pointwise function to append; a NULL is ignored

g1 - The g1 boundary Jacobian pointwise function to append; a NULL is ignored

g2 - The g2 boundary Jacobian pointwise function to append; a NULL is ignored

g3 - The g3 boundary Jacobian pointwise function to append; a NULL is ignored

PetscWeakForm, PetscWeakFormSetBdJacobian(), PetscWeakFormGetBdJacobian(), PetscWeakFormAddJacobian()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormAddBdJacobian(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt g, PetscInt part, void (*g0)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), void (*g1)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), void (*g2)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), void (*g3)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormAddBdResidual#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormAddBdResidual/

**Contents:**
- PetscWeakFormAddBdResidual#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Append boundary residual pointwise functions f0 and f1 to the lists for a given key in a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the boundary region, or NULL for the entire boundary

val - The label value selecting the boundary region

part - The equation part, or 0 if unused

f0 - The f0 boundary residual pointwise function to append; a NULL is ignored

f1 - The f1 boundary residual pointwise function to append; a NULL is ignored

PetscWeakForm, PetscWeakFormSetBdResidual(), PetscWeakFormGetBdResidual(), PetscWeakFormAddResidual()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormAddBdResidual(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt part, void (*f0)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), void (*f1)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormAddDynamicJacobian#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormAddDynamicJacobian/

**Contents:**
- PetscWeakFormAddDynamicJacobian#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Append dynamic Jacobian pointwise functions g0, g1, g2, and g3 to the lists for a given key in a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the mesh region, or NULL for the entire domain

val - The label value selecting the mesh region

f - The test field number

g - The trial field number

part - The equation part, or 0 if unused

g0 - The g0 dynamic Jacobian pointwise function to append; a NULL is ignored

g1 - The g1 dynamic Jacobian pointwise function to append; a NULL is ignored

g2 - The g2 dynamic Jacobian pointwise function to append; a NULL is ignored

g3 - The g3 dynamic Jacobian pointwise function to append; a NULL is ignored

PetscWeakForm, PetscWeakFormSetDynamicJacobian(), PetscWeakFormGetDynamicJacobian(), PetscWeakFormAddJacobian()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormAddDynamicJacobian(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt g, PetscInt part, void (*g0)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), void (*g1)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), void (*g2)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), void (*g3)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormAddJacobian#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormAddJacobian/

**Contents:**
- PetscWeakFormAddJacobian#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Append Jacobian pointwise functions g0, g1, g2, and g3 to the lists for a given key in a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the mesh region, or NULL for the entire domain

val - The label value selecting the mesh region

f - The test field number

g - The trial field number

part - The equation part, or 0 if unused

g0 - The g0 Jacobian pointwise function to append; a NULL is ignored

g1 - The g1 Jacobian pointwise function to append; a NULL is ignored

g2 - The g2 Jacobian pointwise function to append; a NULL is ignored

g3 - The g3 Jacobian pointwise function to append; a NULL is ignored

PetscWeakForm, PetscWeakFormSetJacobian(), PetscWeakFormGetJacobian(), PetscWeakFormSetIndexJacobian()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormAddJacobian(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt g, PetscInt part, void (*g0)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), void (*g1)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), void (*g2)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), void (*g3)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormAddObjective#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormAddObjective/

**Contents:**
- PetscWeakFormAddObjective#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Append an objective pointwise function to the list for a given key in a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the mesh region, or NULL for the entire domain

val - The label value selecting the mesh region

part - The equation part, or 0 if unused

obj - The objective pointwise function to append; a NULL is ignored

PetscWeakForm, PetscWeakFormSetObjective(), PetscWeakFormGetObjective(), PetscWeakFormSetIndexObjective()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormAddObjective(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt part, void (*obj)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormAddResidual#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormAddResidual/

**Contents:**
- PetscWeakFormAddResidual#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Append residual pointwise functions f0 and f1 to the lists for a given key in a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the mesh region, or NULL for the entire domain

val - The label value selecting the mesh region

part - The equation part, or 0 if unused

f0 - The f0 residual pointwise function to append; a NULL is ignored

f1 - The f1 residual pointwise function to append; a NULL is ignored

PetscWeakForm, PetscWeakFormSetResidual(), PetscWeakFormGetResidual(), PetscWeakFormSetIndexResidual(), PetscWeakFormAddBdResidual()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormAddResidual(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt part, void (*f0)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), void (*f1)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormClearIndex#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormClearIndex/

**Contents:**
- PetscWeakFormClearIndex#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Clear the pointwise function at a given index for the given key from a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the mesh region, or NULL for the entire domain

val - The label value selecting the mesh region

part - The equation part, or 0 if unused

kind - The kind of weak form, see PetscWeakFormKind

ind - The index of the function to clear in the function list for this key

PetscWeakForm, PetscWeakFormKind, PetscWeakFormCreate()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormClearIndex(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt part, PetscWeakFormKind kind, PetscInt ind)
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakFormKind
```

---

## PetscWeakFormClear#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormClear/

**Contents:**
- PetscWeakFormClear#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Clear all functions from the PetscWeakForm

wf - The original PetscWeakForm

PetscWeakForm, PetscWeakFormCopy(), PetscWeakFormCreate(), PetscWeakFormDestroy()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormClear(PetscWeakForm wf)
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormCopy#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormCopy/

**Contents:**
- PetscWeakFormCopy#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Copy the pointwise functions to another PetscWeakForm

wf - The original PetscWeakForm

wfNew - The copy of the PetscWeakForm

PetscWeakForm, PetscWeakFormCreate(), PetscWeakFormDestroy()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormCopy(PetscWeakForm wf, PetscWeakForm wfNew)
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormCreate#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormCreate/

**Contents:**
- PetscWeakFormCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Creates an empty PetscWeakForm object.

comm - The communicator for the PetscWeakForm object

wf - The PetscWeakForm object

PetscWeakForm, PetscDS, PetscWeakFormDestroy()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormCreate(MPI_Comm comm, PetscWeakForm *wf)
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormDestroy#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormDestroy/

**Contents:**
- PetscWeakFormDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Destroys a PetscWeakForm object

wf - the PetscWeakForm object to destroy

PetscWeakForm, PetscWeakFormCreate(), PetscWeakFormView()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormDestroy(PetscWeakForm *wf)
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormGetBdJacobian#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormGetBdJacobian/

**Contents:**
- PetscWeakFormGetBdJacobian#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Retrieve the lists of boundary Jacobian pointwise functions g0, g1, g2, and g3 for a given key from a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the boundary region, or NULL for the entire boundary

val - The label value selecting the boundary region

f - The test field number

g - The trial field number

part - The equation part, or 0 if unused

n0 - The number of g0 boundary pointwise functions registered for this key

g0 - The array of g0 boundary Jacobian pointwise functions

n1 - The number of g1 boundary pointwise functions registered for this key

g1 - The array of g1 boundary Jacobian pointwise functions

n2 - The number of g2 boundary pointwise functions registered for this key

g2 - The array of g2 boundary Jacobian pointwise functions

n3 - The number of g3 boundary pointwise functions registered for this key

g3 - The array of g3 boundary Jacobian pointwise functions

PetscWeakForm, PetscWeakFormSetBdJacobian(), PetscWeakFormAddBdJacobian(), PetscWeakFormHasBdJacobian(), PetscWeakFormGetJacobian()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormGetBdJacobian(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt g, PetscInt part, PetscInt *n0, void (***g0)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt *n1, void (***g1)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt *n2, void (***g2)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt *n3, void (***g3)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormGetBdResidual#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormGetBdResidual/

**Contents:**
- PetscWeakFormGetBdResidual#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Retrieve the lists of boundary residual pointwise functions f0 and f1 for a given key from a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the boundary region, or NULL for the entire boundary

val - The label value selecting the boundary region

part - The equation part, or 0 if unused

n0 - The number of f0 boundary pointwise functions registered for this key

f0 - The array of f0 boundary residual pointwise functions

n1 - The number of f1 boundary pointwise functions registered for this key

f1 - The array of f1 boundary residual pointwise functions

PetscWeakForm, PetscWeakFormSetBdResidual(), PetscWeakFormAddBdResidual(), PetscWeakFormGetResidual()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormGetBdResidual(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt part, PetscInt *n0, void (***f0)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt *n1, void (***f1)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormGetDynamicJacobian#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormGetDynamicJacobian/

**Contents:**
- PetscWeakFormGetDynamicJacobian#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Retrieve the lists of dynamic Jacobian pointwise functions g0, g1, g2, and g3 for a given key from a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the mesh region, or NULL for the entire domain

val - The label value selecting the mesh region

f - The test field number

g - The trial field number

part - The equation part, or 0 if unused

n0 - The number of g0 pointwise functions registered for this key

g0 - The array of g0 dynamic Jacobian pointwise functions

n1 - The number of g1 pointwise functions registered for this key

g1 - The array of g1 dynamic Jacobian pointwise functions

n2 - The number of g2 pointwise functions registered for this key

g2 - The array of g2 dynamic Jacobian pointwise functions

n3 - The number of g3 pointwise functions registered for this key

g3 - The array of g3 dynamic Jacobian pointwise functions

PetscWeakForm, PetscWeakFormSetDynamicJacobian(), PetscWeakFormAddDynamicJacobian(), PetscWeakFormHasDynamicJacobian(), PetscWeakFormGetJacobian()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormGetDynamicJacobian(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt g, PetscInt part, PetscInt *n0, void (***g0)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt *n1, void (***g1)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt *n2, void (***g2)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt *n3, void (***g3)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormGetIndexObjective#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormGetIndexObjective/

**Contents:**
- PetscWeakFormGetIndexObjective#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Retrieve a single objective pointwise function at the given index for a given key from a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the mesh region, or NULL for the entire domain

val - The label value selecting the mesh region

part - The equation part, or 0 if unused

ind - The index into the list of objective pointwise functions for this key

obj - The objective pointwise function at position ind, or NULL if no function is registered for this key

PetscWeakForm, PetscWeakFormSetIndexObjective(), PetscWeakFormGetObjective(), PetscWeakFormSetObjective(), PetscWeakFormAddObjective()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormGetIndexObjective(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt part, PetscInt ind, void (**obj)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormGetJacobian#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormGetJacobian/

**Contents:**
- PetscWeakFormGetJacobian#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Retrieve the lists of Jacobian pointwise functions g0, g1, g2, and g3 for a given key from a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the mesh region, or NULL for the entire domain

val - The label value selecting the mesh region

f - The test field number

g - The trial field number

part - The equation part, or 0 if unused

n0 - The number of g0 pointwise functions registered for this key

g0 - The array of g0 Jacobian pointwise functions

n1 - The number of g1 pointwise functions registered for this key

g1 - The array of g1 Jacobian pointwise functions

n2 - The number of g2 pointwise functions registered for this key

g2 - The array of g2 Jacobian pointwise functions

n3 - The number of g3 pointwise functions registered for this key

g3 - The array of g3 Jacobian pointwise functions

PetscWeakForm, PetscWeakFormSetJacobian(), PetscWeakFormAddJacobian(), PetscWeakFormHasJacobian(), PetscWeakFormGetJacobianPreconditioner()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormGetJacobian(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt g, PetscInt part, PetscInt *n0, void (***g0)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt *n1, void (***g1)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt *n2, void (***g2)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt *n3, void (***g3)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormGetNumFields#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormGetNumFields/

**Contents:**
- PetscWeakFormGetNumFields#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the number of fields in a PetscWeakForm

wf - The PetscWeakForm object

Nf - The number of fields

PetscWeakForm, PetscWeakFormSetNumFields(), PetscWeakFormCreate()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormGetNumFields(PetscWeakForm wf, PetscInt *Nf)
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormGetObjective#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormGetObjective/

**Contents:**
- PetscWeakFormGetObjective#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Retrieve the list of objective pointwise functions for a given key from a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the mesh region, or NULL for the entire domain

val - The label value selecting the mesh region

part - The equation part, or 0 if unused

n - The number of objective pointwise functions registered for this key

obj - The array of objective pointwise functions

PetscWeakForm, PetscWeakFormSetObjective(), PetscWeakFormAddObjective(), PetscWeakFormSetIndexObjective(), PetscWeakFormGetIndexObjective()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormGetObjective(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt part, PetscInt *n, void (***obj)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormGetResidual#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormGetResidual/

**Contents:**
- PetscWeakFormGetResidual#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Retrieve the lists of residual pointwise functions f0 and f1 for a given key from a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the mesh region, or NULL for the entire domain

val - The label value selecting the mesh region

part - The equation part, or 0 if unused

n0 - The number of f0 pointwise functions registered for this key

f0 - The array of f0 residual pointwise functions

n1 - The number of f1 pointwise functions registered for this key

f1 - The array of f1 residual pointwise functions

PetscWeakForm, PetscWeakFormSetResidual(), PetscWeakFormAddResidual(), PetscWeakFormGetBdResidual()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormGetResidual(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt part, PetscInt *n0, void (***f0)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt *n1, void (***f1)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormGetRiemannSolver#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormGetRiemannSolver/

**Contents:**
- PetscWeakFormGetRiemannSolver#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Retrieve the list of Riemann solver pointwise functions for a given key from a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the mesh region, or NULL for the entire domain

val - The label value selecting the mesh region

part - The equation part, or 0 if unused

n - The number of Riemann solver pointwise functions registered for this key

r - The array of Riemann solver pointwise functions

PetscWeakForm, PetscWeakFormSetRiemannSolver(), PetscWeakFormSetIndexRiemannSolver()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormGetRiemannSolver(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt part, PetscInt *n, void (***r)(PetscInt, PetscInt, const PetscReal[], const PetscReal[], const PetscScalar[], const PetscScalar[], PetscInt, const PetscScalar[], PetscScalar[], void *))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormHasBdJacobian#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormHasBdJacobian/

**Contents:**
- PetscWeakFormHasBdJacobian#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns whether the PetscWeakForm has any boundary Jacobian (g0, g1, g2, or g3) pointwise functions registered

wf - The PetscWeakForm

hasJac - PETSC_TRUE if any boundary Jacobian pointwise functions are registered, PETSC_FALSE otherwise

PetscWeakForm, PetscWeakFormSetBdJacobian(), PetscWeakFormGetBdJacobian(), PetscWeakFormHasJacobian(), PetscWeakFormHasBdJacobianPreconditioner()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormHasBdJacobian(PetscWeakForm wf, PetscBool *hasJac)
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PETSC_FALSE
```

---

## PetscWeakFormHasDynamicJacobian#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormHasDynamicJacobian/

**Contents:**
- PetscWeakFormHasDynamicJacobian#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Returns whether the PetscWeakForm has any dynamic Jacobian (g0, g1, g2, or g3) pointwise functions registered

wf - The PetscWeakForm

hasDynJac - PETSC_TRUE if any dynamic Jacobian pointwise functions are registered, PETSC_FALSE otherwise

The dynamic Jacobian is the Jacobian of the time-derivative term for transient problems.

PetscWeakForm, PetscWeakFormSetDynamicJacobian(), PetscWeakFormGetDynamicJacobian(), PetscWeakFormHasJacobian()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormHasDynamicJacobian(PetscWeakForm wf, PetscBool *hasDynJac)
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PETSC_FALSE
```

---

## PetscWeakFormHasJacobian#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormHasJacobian/

**Contents:**
- PetscWeakFormHasJacobian#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns whether the PetscWeakForm has any Jacobian (g0, g1, g2, or g3) pointwise functions registered

wf - The PetscWeakForm

hasJac - PETSC_TRUE if any Jacobian pointwise functions are registered, PETSC_FALSE otherwise

PetscWeakForm, PetscWeakFormSetJacobian(), PetscWeakFormGetJacobian(), PetscWeakFormHasJacobianPreconditioner(), PetscWeakFormHasBdJacobian()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormHasJacobian(PetscWeakForm wf, PetscBool *hasJac)
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PETSC_FALSE
```

---

## PetscWeakFormKind#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormKind/

**Contents:**
- PetscWeakFormKind#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

The kind of weak form. The specific forms are given in the documentation for the integraton functions.

OBJECTIVE - Objective form

F0, F1 - Residual forms

G0, G1, G2, G3 - Jacobian forms

GP0, GP1, GP2, GP3 - Jacobian forms used to construct the preconditioner

GT0, GT1, GT2, GT3 - Dynamic Jacobian matrix forms

BDF0, BDF1 - Boundary Residual forms

BDG0, BDG1, BDG2, BDG3 - Jacobian forms

BDGP0, BDGP1, BDGP2, BDGP3 - Jacobian forms used to construct the preconditioner

CEED - libCEED QFunction

PetscWeakForm, PetscFEIntegrateResidual(), PetscFEIntegrateJacobian(), PetscFEIntegrateBdResidual(), PetscFEIntegrateBdJacobian(), PetscFVIntegrateRHSFunction(), PetscWeakFormSetIndexResidual(), PetscWeakFormClearIndex()

include/petscdstypes.h

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  PETSC_WF_OBJECTIVE,
  PETSC_WF_F0,
  PETSC_WF_F1,
  PETSC_WF_G0,
  PETSC_WF_G1,
  PETSC_WF_G2,
  PETSC_WF_G3,
  PETSC_WF_GP0,
  PETSC_WF_GP1,
  PETSC_WF_GP2,
  PETSC_WF_GP3,
  PETSC_WF_GT0,
  PETSC_WF_GT1,
  PETSC_WF_GT2,
  PETSC_WF_GT3,
  PETSC_WF_BDF0,
  PETSC_WF_BDF1,
  PETSC_WF_BDG0,
  PETSC_WF_BDG1,
  PETSC_WF_BDG2,
  PETSC_WF_BDG3,
  PETSC_WF_BDGP0,
  PETSC_WF_BDGP1,
  PETSC_WF_BDGP2,
  PETSC_WF_BDGP3,
  PETSC_WF_R,
  PETSC_WF_CEED,
  PETSC_NUM_WF
} PetscWeakFormKind;
```

Example 2 (unknown):
```unknown
PetscWeakForm
```

Example 3 (unknown):
```unknown
PetscFEIntegrateResidual()
```

Example 4 (unknown):
```unknown
PetscFEIntegrateJacobian()
```

---

## PetscWeakFormReplaceLabel#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormReplaceLabel/

**Contents:**
- PetscWeakFormReplaceLabel#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Change any key on a label of the same name to use the new label

wf - The original PetscWeakForm

label - The label to change keys for

This is used internally when meshes are modified

PetscWeakForm, DMLabel, PetscWeakFormRewriteKeys(), PetscWeakFormCreate(), PetscWeakFormDestroy()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormReplaceLabel(PetscWeakForm wf, DMLabel label)
```

Example 2 (unknown):
```unknown
PetscWeakForm
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakFormRewriteKeys()
```

---

## PetscWeakFormRewriteKeys#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormRewriteKeys/

**Contents:**
- PetscWeakFormRewriteKeys#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Change any key on the given label to use the new set of label values

wf - The original PetscWeakForm

label - The label to change keys for

Nv - The number of new label values

values - The set of new values to relabel keys with

This is used internally when boundary label values are specified from the command line.

PetscWeakForm, DMLabel, PetscWeakFormReplaceLabel(), PetscWeakFormCreate(), PetscWeakFormDestroy()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormRewriteKeys(PetscWeakForm wf, DMLabel label, PetscInt Nv, const PetscInt values[])
```

Example 2 (unknown):
```unknown
PetscWeakForm
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakFormReplaceLabel()
```

---

## PetscWeakFormSetBdJacobian#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormSetBdJacobian/

**Contents:**
- PetscWeakFormSetBdJacobian#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the lists of boundary Jacobian pointwise functions g0, g1, g2, and g3 for a given key in a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the boundary region, or NULL for the entire boundary

val - The label value selecting the boundary region

f - The test field number

g - The trial field number

part - The equation part, or 0 if unused

n0 - The number of g0 boundary pointwise functions to set

g0 - The array of g0 boundary Jacobian pointwise functions, or NULL to clear the key

n1 - The number of g1 boundary pointwise functions to set

g1 - The array of g1 boundary Jacobian pointwise functions, or NULL to clear the key

n2 - The number of g2 boundary pointwise functions to set

g2 - The array of g2 boundary Jacobian pointwise functions, or NULL to clear the key

n3 - The number of g3 boundary pointwise functions to set

g3 - The array of g3 boundary Jacobian pointwise functions, or NULL to clear the key

PetscWeakForm, PetscWeakFormGetBdJacobian(), PetscWeakFormAddBdJacobian(), PetscWeakFormSetJacobian()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormSetBdJacobian(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt g, PetscInt part, PetscInt n0, void (**g0)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt n1, void (**g1)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt n2, void (**g2)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt n3, void (**g3)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormSetBdResidual#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormSetBdResidual/

**Contents:**
- PetscWeakFormSetBdResidual#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the lists of boundary residual pointwise functions f0 and f1 for a given key in a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the boundary region, or NULL for the entire boundary

val - The label value selecting the boundary region

part - The equation part, or 0 if unused

n0 - The number of f0 boundary pointwise functions to set

f0 - The array of f0 boundary residual pointwise functions, or NULL to clear the key

n1 - The number of f1 boundary pointwise functions to set

f1 - The array of f1 boundary residual pointwise functions, or NULL to clear the key

PetscWeakForm, PetscWeakFormGetBdResidual(), PetscWeakFormAddBdResidual(), PetscWeakFormSetResidual()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormSetBdResidual(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt part, PetscInt n0, void (**f0)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt n1, void (**f1)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormSetDynamicJacobian#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormSetDynamicJacobian/

**Contents:**
- PetscWeakFormSetDynamicJacobian#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the lists of dynamic Jacobian pointwise functions g0, g1, g2, and g3 for a given key in a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the mesh region, or NULL for the entire domain

val - The label value selecting the mesh region

f - The test field number

g - The trial field number

part - The equation part, or 0 if unused

n0 - The number of g0 pointwise functions to set

g0 - The array of g0 dynamic Jacobian pointwise functions, or NULL to clear the key

n1 - The number of g1 pointwise functions to set

g1 - The array of g1 dynamic Jacobian pointwise functions, or NULL to clear the key

n2 - The number of g2 pointwise functions to set

g2 - The array of g2 dynamic Jacobian pointwise functions, or NULL to clear the key

n3 - The number of g3 pointwise functions to set

g3 - The array of g3 dynamic Jacobian pointwise functions, or NULL to clear the key

PetscWeakForm, PetscWeakFormGetDynamicJacobian(), PetscWeakFormAddDynamicJacobian(), PetscWeakFormSetJacobian()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormSetDynamicJacobian(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt g, PetscInt part, PetscInt n0, void (**g0)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt n1, void (**g1)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt n2, void (**g2)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt n3, void (**g3)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormSetIndexBdJacobian#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormSetIndexBdJacobian/

**Contents:**
- PetscWeakFormSetIndexBdJacobian#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the boundary Jacobian pointwise functions g0, g1, g2, and g3 at the given indices for a given key in a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the boundary region, or NULL for the entire boundary

val - The label value selecting the boundary region

f - The test field number

g - The trial field number

part - The equation part, or 0 if unused

i0 - The index at which to store g0 in the g0 list

g0 - The g0 boundary Jacobian pointwise function; a NULL is ignored

i1 - The index at which to store g1 in the g1 list

g1 - The g1 boundary Jacobian pointwise function; a NULL is ignored

i2 - The index at which to store g2 in the g2 list

g2 - The g2 boundary Jacobian pointwise function; a NULL is ignored

i3 - The index at which to store g3 in the g3 list

g3 - The g3 boundary Jacobian pointwise function; a NULL is ignored

PetscWeakForm, PetscWeakFormSetBdJacobian(), PetscWeakFormAddBdJacobian(), PetscWeakFormGetBdJacobian(), PetscWeakFormClearIndex()

src/dm/dt/interface/dtweakform.c

src/snes/tutorials/ex77.c src/snes/tutorials/ex62.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormSetIndexBdJacobian(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt g, PetscInt part, PetscInt i0, void (*g0)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt i1, void (*g1)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt i2, void (*g2)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt i3, void (*g3)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormSetIndexBdResidual#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormSetIndexBdResidual/

**Contents:**
- PetscWeakFormSetIndexBdResidual#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the boundary residual pointwise functions f0 and f1 at the given indices for a given key in a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the boundary region, or NULL for the entire boundary

val - The label value selecting the boundary region

part - The equation part, or 0 if unused

i0 - The index at which to store f0 in the f0 list

f0 - The f0 boundary residual pointwise function; a NULL is ignored

i1 - The index at which to store f1 in the f1 list

f1 - The f1 boundary residual pointwise function; a NULL is ignored

PetscWeakForm, PetscWeakFormSetBdResidual(), PetscWeakFormAddBdResidual(), PetscWeakFormGetBdResidual(), PetscWeakFormClearIndex()

src/dm/dt/interface/dtweakform.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex62.c src/snes/tutorials/ex12.c src/ts/tutorials/ex76.c src/snes/tutorials/ex56.c src/snes/tutorials/ex17.c src/ts/tutorials/ex53.c src/snes/tutorials/ex24.c src/snes/tutorials/ex27.c src/snes/tutorials/ex77.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormSetIndexBdResidual(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt part, PetscInt i0, void (*f0)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt i1, void (*f1)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormSetIndexDynamicJacobian#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormSetIndexDynamicJacobian/

**Contents:**
- PetscWeakFormSetIndexDynamicJacobian#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the dynamic Jacobian pointwise functions g0, g1, g2, and g3 at the given indices for a given key in a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the mesh region, or NULL for the entire domain

val - The label value selecting the mesh region

f - The test field number

g - The trial field number

part - The equation part, or 0 if unused

i0 - The index at which to store g0 in the g0 list

g0 - The g0 dynamic Jacobian pointwise function; a NULL is ignored

i1 - The index at which to store g1 in the g1 list

g1 - The g1 dynamic Jacobian pointwise function; a NULL is ignored

i2 - The index at which to store g2 in the g2 list

g2 - The g2 dynamic Jacobian pointwise function; a NULL is ignored

i3 - The index at which to store g3 in the g3 list

g3 - The g3 dynamic Jacobian pointwise function; a NULL is ignored

PetscWeakForm, PetscWeakFormSetDynamicJacobian(), PetscWeakFormAddDynamicJacobian(), PetscWeakFormGetDynamicJacobian(), PetscWeakFormClearIndex()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormSetIndexDynamicJacobian(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt g, PetscInt part, PetscInt i0, void (*g0)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt i1, void (*g1)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt i2, void (*g2)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt i3, void (*g3)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormSetIndexJacobian#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormSetIndexJacobian/

**Contents:**
- PetscWeakFormSetIndexJacobian#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the Jacobian pointwise functions g0, g1, g2, and g3 at the given indices for a given key in a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the mesh region, or NULL for the entire domain

val - The label value selecting the mesh region

f - The test field number

g - The trial field number

part - The equation part, or 0 if unused

i0 - The index at which to store g0 in the g0 list

g0 - The g0 Jacobian pointwise function; a NULL is ignored

i1 - The index at which to store g1 in the g1 list

g1 - The g1 Jacobian pointwise function; a NULL is ignored

i2 - The index at which to store g2 in the g2 list

g2 - The g2 Jacobian pointwise function; a NULL is ignored

i3 - The index at which to store g3 in the g3 list

g3 - The g3 Jacobian pointwise function; a NULL is ignored

PetscWeakForm, PetscWeakFormSetJacobian(), PetscWeakFormAddJacobian(), PetscWeakFormGetJacobian(), PetscWeakFormClearIndex()

src/dm/dt/interface/dtweakform.c

src/snes/tutorials/ex23.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormSetIndexJacobian(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt g, PetscInt part, PetscInt i0, void (*g0)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt i1, void (*g1)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt i2, void (*g2)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt i3, void (*g3)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormSetIndexObjective#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormSetIndexObjective/

**Contents:**
- PetscWeakFormSetIndexObjective#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set a single objective pointwise function at the given index for a given key in a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the mesh region, or NULL for the entire domain

val - The label value selecting the mesh region

part - The equation part, or 0 if unused

ind - The index into the list of objective pointwise functions for this key

obj - The objective pointwise function to store at position ind; a NULL is ignored

PetscWeakForm, PetscWeakFormGetIndexObjective(), PetscWeakFormSetObjective(), PetscWeakFormAddObjective(), PetscWeakFormClearIndex()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormSetIndexObjective(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt part, PetscInt ind, void (*obj)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormSetIndexResidual#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormSetIndexResidual/

**Contents:**
- PetscWeakFormSetIndexResidual#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the residual pointwise functions f0 and f1 at the given indices for a given key in a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the mesh region, or NULL for the entire domain

val - The label value selecting the mesh region

part - The equation part, or 0 if unused

i0 - The index at which to store f0 in the f0 list

f0 - The f0 residual pointwise function; a NULL is ignored

i1 - The index at which to store f1 in the f1 list

f1 - The f1 residual pointwise function; a NULL is ignored

PetscWeakForm, PetscWeakFormSetResidual(), PetscWeakFormAddResidual(), PetscWeakFormGetResidual(), PetscWeakFormClearIndex()

src/dm/dt/interface/dtweakform.c

src/snes/tutorials/ex23.c src/snes/tutorials/ex17.c src/ts/tutorials/ex76.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormSetIndexResidual(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt part, PetscInt i0, void (*f0)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt i1, void (*f1)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormSetIndexRiemannSolver#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormSetIndexRiemannSolver/

**Contents:**
- PetscWeakFormSetIndexRiemannSolver#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set a single Riemann solver pointwise function at the given index for a given key in a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the mesh region, or NULL for the entire domain

val - The label value selecting the mesh region

part - The equation part, or 0 if unused

i - The index into the list of Riemann solver pointwise functions for this key

r - The Riemann solver pointwise function to store at position i; a NULL is ignored

PetscWeakForm, PetscWeakFormSetRiemannSolver(), PetscWeakFormGetRiemannSolver(), PetscWeakFormClearIndex()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormSetIndexRiemannSolver(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt part, PetscInt i, void (*r)(PetscInt, PetscInt, const PetscReal[], const PetscReal[], const PetscScalar[], const PetscScalar[], PetscInt, const PetscScalar[], PetscScalar[], void *))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormSetJacobian#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormSetJacobian/

**Contents:**
- PetscWeakFormSetJacobian#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the lists of Jacobian pointwise functions g0, g1, g2, and g3 for a given key in a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the mesh region, or NULL for the entire domain

val - The label value selecting the mesh region

f - The test field number

g - The trial field number

part - The equation part, or 0 if unused

n0 - The number of g0 pointwise functions to set

g0 - The array of g0 Jacobian pointwise functions, or NULL to clear the key

n1 - The number of g1 pointwise functions to set

g1 - The array of g1 Jacobian pointwise functions, or NULL to clear the key

n2 - The number of g2 pointwise functions to set

g2 - The array of g2 Jacobian pointwise functions, or NULL to clear the key

n3 - The number of g3 pointwise functions to set

g3 - The array of g3 Jacobian pointwise functions, or NULL to clear the key

PetscWeakForm, PetscWeakFormGetJacobian(), PetscWeakFormAddJacobian(), PetscWeakFormSetIndexJacobian(), PetscWeakFormSetJacobianPreconditioner()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormSetJacobian(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt g, PetscInt part, PetscInt n0, void (**g0)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt n1, void (**g1)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt n2, void (**g2)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt n3, void (**g3)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormSetNumFields#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormSetNumFields/

**Contents:**
- PetscWeakFormSetNumFields#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the number of fields

wf - The PetscWeakForm object

Nf - The number of fields

PetscWeakForm, PetscWeakFormGetNumFields(), PetscWeakFormCreate()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormSetNumFields(PetscWeakForm wf, PetscInt Nf)
```

Example 2 (unknown):
```unknown
PetscWeakForm
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakFormGetNumFields()
```

---

## PetscWeakFormSetObjective#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormSetObjective/

**Contents:**
- PetscWeakFormSetObjective#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the list of objective pointwise functions for a given key in a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the mesh region, or NULL for the entire domain

val - The label value selecting the mesh region

part - The equation part, or 0 if unused

n - The number of objective pointwise functions to set

obj - The array of objective pointwise functions, or NULL to clear the key

PetscWeakForm, PetscWeakFormGetObjective(), PetscWeakFormAddObjective(), PetscWeakFormSetIndexObjective()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormSetObjective(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt part, PetscInt n, void (**obj)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormSetResidual#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormSetResidual/

**Contents:**
- PetscWeakFormSetResidual#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the lists of residual pointwise functions f0 and f1 for a given key in a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the mesh region, or NULL for the entire domain

val - The label value selecting the mesh region

part - The equation part, or 0 if unused

n0 - The number of f0 pointwise functions to set

f0 - The array of f0 residual pointwise functions, or NULL to clear the key

n1 - The number of f1 pointwise functions to set

f1 - The array of f1 residual pointwise functions, or NULL to clear the key

PetscWeakForm, PetscWeakFormGetResidual(), PetscWeakFormAddResidual(), PetscWeakFormSetIndexResidual()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormSetResidual(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt part, PetscInt n0, void (**f0)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]), PetscInt n1, void (**f1)(PetscInt, PetscInt, PetscInt, const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], const PetscInt[], const PetscInt[], const PetscScalar[], const PetscScalar[], const PetscScalar[], PetscReal, const PetscReal[], PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormSetRiemannSolver#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormSetRiemannSolver/

**Contents:**
- PetscWeakFormSetRiemannSolver#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the list of Riemann solver pointwise functions for a given key in a PetscWeakForm

wf - The PetscWeakForm

label - The label selecting the mesh region, or NULL for the entire domain

val - The label value selecting the mesh region

part - The equation part, or 0 if unused

n - The number of Riemann solver pointwise functions to set

r - The array of Riemann solver pointwise functions, or NULL to clear the key

PetscWeakForm, PetscWeakFormGetRiemannSolver(), PetscWeakFormSetIndexRiemannSolver()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormSetRiemannSolver(PetscWeakForm wf, DMLabel label, PetscInt val, PetscInt f, PetscInt part, PetscInt n, void (**r)(PetscInt, PetscInt, const PetscReal[], const PetscReal[], const PetscScalar[], const PetscScalar[], PetscInt, const PetscScalar[], PetscScalar[], void *))
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscWeakForm
```

---

## PetscWeakFormView#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakFormView/

**Contents:**
- PetscWeakFormView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Views a PetscWeakForm

wf - the PetscWeakForm object to view

PetscViewer, PetscWeakForm, PetscWeakFormDestroy(), PetscWeakFormCreate()

src/dm/dt/interface/dtweakform.c

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscWeakForm
```

Example 2 (unknown):
```unknown
#include "petscds.h" 
PetscErrorCode PetscWeakFormView(PetscWeakForm wf, PetscViewer v)
```

Example 3 (unknown):
```unknown
PetscWeakForm
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscWeakForm#

**URL:** https://petsc.org/release/manualpages/DT/PetscWeakForm/

**Contents:**
- PetscWeakForm#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

PETSc object that manages a sets of pointwise functions defining a system of equations

PetscWeakFormCreate(), PetscDS, PetscFECreate(), PetscFVCreate()

include/petscdstypes.h

src/snes/tutorials/ex71.c src/snes/tutorials/ex12.c src/snes/tutorials/ex77.c src/snes/tutorials/ex56.c src/snes/tutorials/ex17.c src/snes/tutorials/ex24.c src/snes/tutorials/ex27.c src/snes/tutorials/ex23.c src/snes/tutorials/ex34.c src/snes/tutorials/ex62.c

_p_PetscWeakForm in include/petsc/private/petscdsimpl.h

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_PetscWeakForm *PetscWeakForm;
```

Example 2 (unknown):
```unknown
PetscWeakFormCreate()
```

Example 3 (unknown):
```unknown
PetscFECreate()
```

Example 4 (unknown):
```unknown
PetscFVCreate()
```

---

## PETSC_FORM_DEGREE_UNDEFINED#

**URL:** https://petsc.org/release/manualpages/DT/PETSC_FORM_DEGREE_UNDEFINED/

**Contents:**
- PETSC_FORM_DEGREE_UNDEFINED#
- See Also#
- Level#
- Location#

Indicates that a field does not have a well-defined form degree in exterior calculus.

PetscDTAltV, PetscDualSpaceGetFormDegree()

Index of all DT routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDTAltV
```

Example 2 (unknown):
```unknown
PetscDualSpaceGetFormDegree()
```

---

## PFAppendOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/PF/PFAppendOptionsPrefix/

**Contents:**
- PFAppendOptionsPrefix#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Appends to the prefix used for searching for all PF options in the database.

prefix - the prefix string to prepend to all PF option requests

A hyphen (-) must NOT be given at the beginning of the prefix name. The first character of all runtime options is AUTOMATICALLY the hyphen.

KSP: Linear System Solvers, PF, PFSetFromOptions(), PFSetOptionsPrefix(), PFGetOptionsPrefix()

src/vec/pf/interface/pf.c

Index of all PF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscpf.h" 
PetscErrorCode PFAppendOptionsPrefix(PF pf, const char prefix[])
```

Example 2 (unknown):
```unknown
PFSetFromOptions()
```

Example 3 (unknown):
```unknown
PFSetOptionsPrefix()
```

Example 4 (unknown):
```unknown
PFGetOptionsPrefix()
```

---

## PFApplyVec#

**URL:** https://petsc.org/release/manualpages/PF/PFApplyVec/

**Contents:**
- PFApplyVec#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Applies the mathematical function to a vector

pf - the function context

x - input vector (or NULL for the vector (0,1, …. N-1)

PF, PFApply(), PFCreate(), PFDestroy(), PFSetType(), PFSet()

src/vec/pf/interface/pf.c

src/snes/tutorials/ex22.c src/dm/tutorials/ex4.c

PFApplyVec_Constant() in src/vec/pf/impls/constant/const.c PFApplyVec_Identity() in src/vec/pf/impls/constant/const.c

Index of all PF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscpf.h" 
PetscErrorCode PFApplyVec(PF pf, Vec x, Vec y)
```

Example 2 (unknown):
```unknown
PFDestroy()
```

Example 3 (unknown):
```unknown
PFSetType()
```

---

## PFApply#

**URL:** https://petsc.org/release/manualpages/PF/PFApply/

**Contents:**
- PFApply#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Applies the mathematical function to an array of values.

pf - the function context

n - number of pointwise function evaluations to perform, each pointwise function evaluation is a function of dimin variables and computes dimout variables where dimin and dimout are defined in the call to PFCreate()

PF, PFApplyVec(), PFCreate(), PFDestroy(), PFSetType(), PFSet()

src/vec/pf/interface/pf.c

PFApply_Constant() in src/vec/pf/impls/constant/const.c PFApply_Identity() in src/vec/pf/impls/constant/const.c PFApply_Matlab() in src/vec/pf/impls/matlab/cmatlab.c

Index of all PF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscpf.h" 
PetscErrorCode PFApply(PF pf, PetscInt n, const PetscScalar *x, PetscScalar *y)
```

Example 2 (unknown):
```unknown
PFApplyVec()
```

Example 3 (unknown):
```unknown
PFDestroy()
```

Example 4 (unknown):
```unknown
PFSetType()
```

---

## PFCreate#

**URL:** https://petsc.org/release/manualpages/PF/PFCreate/

**Contents:**
- PFCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Creates a mathematical function context.

comm - MPI communicator

dimin - dimension of the space you are mapping from

dimout - dimension of the space you are mapping to

pf - the function context

PF, PFSet(), PFApply(), PFDestroy(), PFApplyVec()

src/vec/pf/interface/pf.c

src/snes/tutorials/ex22.c

PFCreate_Constant() in src/vec/pf/impls/constant/const.c PFCreate_Quick(PF pf, PetscErrorCode (*function)() in src/vec/pf/impls/constant/const.c PFCreate_Identity() in src/vec/pf/impls/constant/const.c PFCreate_Matlab() in src/vec/pf/impls/matlab/cmatlab.c PFCreate_String() in src/vec/pf/impls/string/cstring.c

Index of all PF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscpf.h" 
PetscErrorCode PFCreate(MPI_Comm comm, PetscInt dimin, PetscInt dimout, PF *pf)
```

Example 2 (unknown):
```unknown
PFDestroy()
```

Example 3 (unknown):
```unknown
PFApplyVec()
```

---

## PFDestroy#

**URL:** https://petsc.org/release/manualpages/PF/PFDestroy/

**Contents:**
- PFDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Destroys PF context that was created with PFCreate().

pf - the function context

PF, PFCreate(), PFSet(), PFSetType()

src/vec/pf/interface/pf.c

src/snes/tutorials/ex22.c src/dm/tutorials/ex4.c

PFDestroy_Constant() in src/vec/pf/impls/constant/const.c PFDestroy_Identity() in src/vec/pf/impls/constant/const.c PFDestroy_Matlab() in src/vec/pf/impls/matlab/cmatlab.c PFDestroy_String() in src/vec/pf/impls/string/cstring.c

Index of all PF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscpf.h" 
PetscErrorCode PFDestroy(PF *pf)
```

Example 2 (unknown):
```unknown
PFSetType()
```

---

## PFFinalizePackage#

**URL:** https://petsc.org/release/manualpages/PF/PFFinalizePackage/

**Contents:**
- PFFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys everything in the PETSc PF package. It is called from PetscFinalize().

src/vec/pf/interface/pf.c

Index of all PF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
#include "petscpf.h" 
PetscErrorCode PFFinalizePackage(void)
```

Example 3 (unknown):
```unknown
PetscFinalize()
```

---

## PFGetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/PF/PFGetOptionsPrefix/

**Contents:**
- PFGetOptionsPrefix#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the prefix used for searching for all PF options in the database.

prefix - pointer to the prefix string used, is returned

KSP: Linear System Solvers, PF, PFSetFromOptions(), PFSetOptionsPrefix(), PFAppendOptionsPrefix()

src/vec/pf/interface/pf.c

Index of all PF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscpf.h" 
PetscErrorCode PFGetOptionsPrefix(PF pf, const char *prefix[])
```

Example 2 (unknown):
```unknown
PFSetFromOptions()
```

Example 3 (unknown):
```unknown
PFSetOptionsPrefix()
```

Example 4 (unknown):
```unknown
PFAppendOptionsPrefix()
```

---

## PFGetType#

**URL:** https://petsc.org/release/manualpages/PF/PFGetType/

**Contents:**
- PFGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the PFType name (as a string) from the PF context.

pf - the function context

type - name of function

type should not be retained for later use as it will be an invalid pointer if the PFType of pf is changed.

PF, PFSetType(), PFType, PetscObjectTypeCompare(), PetscObjectTypeCompareAny()

src/vec/pf/interface/pf.c

Index of all PF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscpf.h" 
PetscErrorCode PFGetType(PF pf, PFType *type)
```

Example 2 (unknown):
```unknown
PFSetType()
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

## PFInitializePackage#

**URL:** https://petsc.org/release/manualpages/PF/PFInitializePackage/

**Contents:**
- PFInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function initializes everything in the PF package. It is called from PetscDLLibraryRegister_petscvec() when using dynamic libraries, and on the first call to PFCreate() when using shared or static libraries.

PF, PetscInitialize()

src/vec/pf/interface/pf.c

Index of all PF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscpf.h" 
PetscErrorCode PFInitializePackage(void)
```

Example 2 (unknown):
```unknown
PetscInitialize()
```

---

## PFRegisterAll#

**URL:** https://petsc.org/release/manualpages/PF/PFRegisterAll/

**Contents:**
- PFRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the preconditioners in the PF package.

PFRegister(), PFRegisterDestroy()

src/vec/pf/interface/pfall.c

Index of all PF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscpf.h"   
PetscErrorCode PFRegisterAll(void)
```

Example 2 (unknown):
```unknown
PFRegister()
```

Example 3 (unknown):
```unknown
PFRegisterDestroy()
```

---

## PFRegister#

**URL:** https://petsc.org/release/manualpages/PF/PFRegister/

**Contents:**
- PFRegister#
- Synopsis#
- Input Parameters#
- Example Usage#
- Note#
- See Also#
- Level#
- Location#

Adds a method to the mathematical function package.

sname - name of a new user-defined solver

function - routine to create method context

Then, your solver can be chosen with the procedural interface via

or at runtime via the option

PFRegister() may be called multiple times to add several user-defined functions

PF, PFRegisterAll(), PFRegisterDestroy()

src/vec/pf/interface/pf.c

Index of all PF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscpf.h" 
PetscErrorCode PFRegister(const char sname[], PetscErrorCode (*function)(PF, PetscCtx))
```

Example 2 (unknown):
```unknown
PFRegister("my_function", MyFunctionSetCreate);
```

Example 3 (unknown):
```unknown
PFSetType(pf, "my_function")
```

Example 4 (unknown):
```unknown
-pf_type my_function
```

---

## PFSetFromOptions#

**URL:** https://petsc.org/release/manualpages/PF/PFSetFromOptions/

**Contents:**
- PFSetFromOptions#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets PF options from the options database.

pf - the mathematical function context

To see all options, run your program with the -help option or consult the users manual.

src/vec/pf/interface/pf.c

src/dm/tutorials/ex4.c

PFSetFromOptions_Constant() in src/vec/pf/impls/constant/const.c PFSetFromOptions_Matlab() in src/vec/pf/impls/matlab/cmatlab.c PFSetFromOptions_String() in src/vec/pf/impls/string/cstring.c

Index of all PF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscpf.h" 
PetscErrorCode PFSetFromOptions(PF pf)
```

---

## PFSetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/PF/PFSetOptionsPrefix/

**Contents:**
- PFSetOptionsPrefix#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the prefix used for searching for all PF options in the database.

prefix - the prefix string to prepend to all PF option requests

A hyphen (-) must NOT be given at the beginning of the prefix name. The first character of all runtime options is AUTOMATICALLY the hyphen.

KSP: Linear System Solvers, PF, PFSetFromOptions(), PFAppendOptionsPrefix(), PFGetOptionsPrefix()

src/vec/pf/interface/pf.c

Index of all PF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscpf.h" 
PetscErrorCode PFSetOptionsPrefix(PF pf, const char prefix[])
```

Example 2 (unknown):
```unknown
PFSetFromOptions()
```

Example 3 (unknown):
```unknown
PFAppendOptionsPrefix()
```

Example 4 (unknown):
```unknown
PFGetOptionsPrefix()
```

---

## PFSetType#

**URL:** https://petsc.org/release/manualpages/PF/PFSetType/

**Contents:**
- PFSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

Builds PF for a particular function

pf - the function context.

type - a known type, see PFType for available methods (for instance, PFCONSTANT)

ctx - optional type dependent context

-pf_type (constant|mat|string|quick|identity|matlab) - Set the PFType

PF, PFSet(), PFRegister(), PFCreate(), DMDACreatePF(), PFType, PFGetType()

src/vec/pf/interface/pf.c

src/snes/tutorials/ex22.c

Index of all PF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscpf.h" 
PetscErrorCode PFSetType(PF pf, PFType type, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
PFRegister()
```

Example 3 (unknown):
```unknown
DMDACreatePF()
```

Example 4 (unknown):
```unknown
PFGetType()
```

---

## PFSet#

**URL:** https://petsc.org/release/manualpages/PF/PFSet/

**Contents:**
- PFSet#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the C/C++/Fortran functions to be used by the PF function

pf - the function context

apply - function to apply to an array

applyvec - function to apply to a Vec

view - function that prints information about the PF

destroy - function to free the private function context

ctx - private function context

PF, PFCreate(), PFDestroy(), PFSetType(), PFApply(), PFApplyVec()

src/vec/pf/interface/pf.c

src/dm/tutorials/ex4.c

Index of all PF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscpf.h" 
PetscErrorCode PFSet(PF pf, PetscErrorCode (*apply)(PetscCtx, PetscInt, const PetscScalar *, PetscScalar *), PetscErrorCode (*applyvec)(PetscCtx, Vec, Vec), PetscErrorCode (*view)(PetscCtx, PetscViewer), PetscErrorCode (*destroy)(PetscCtxRt), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
PFDestroy()
```

Example 3 (unknown):
```unknown
PFSetType()
```

Example 4 (unknown):
```unknown
PFApplyVec()
```

---

## PFStringSetFunction#

**URL:** https://petsc.org/release/manualpages/PF/PFStringSetFunction/

**Contents:**
- PFStringSetFunction#
- Synopsis#
- Input Parameters#
- Developer Notes#
- See Also#
- Level#
- Location#

Creates a function from a string

pf - the function object

string - the string that defines the function

Currently this can be used only ONCE in a running code. It needs to be fixed to generate a new library name for each new function added.

Requires PETSC_HAVE_POPEN PETSC_USE_SHARED_LIBRARIES PETSC_HAVE_DYNAMIC_LIBRARIES to use

src/vec/pf/impls/string/cstring.c

Index of all PF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscpf.h" 
PetscErrorCode PFStringSetFunction(PF pf, const char string[])
```

Example 2 (unknown):
```unknown
PETSC_HAVE_POPEN
```

Example 3 (unknown):
```unknown
PETSC_USE_SHARED_LIBRARIES
```

Example 4 (unknown):
```unknown
PETSC_HAVE_DYNAMIC_LIBRARIES
```

---

## PFType#

**URL:** https://petsc.org/release/manualpages/PF/PFType/

**Contents:**
- PFType#
- Synopsis#
- See Also#
- Level#
- Location#

Type of PETSc mathematical function, a string name

Index of all PF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef const char *PFType;
#define PFCONSTANT "constant"
#define PFMAT      "mat"
#define PFSTRING   "string"
#define PFQUICK    "quick"
#define PFIDENTITY "identity"
#define PFMATLAB   "matlab"
```

Example 2 (unknown):
```unknown
PFSetType()
```

---

## PFViewFromOptions#

**URL:** https://petsc.org/release/manualpages/PF/PFViewFromOptions/

**Contents:**
- PFViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

View a PF based on options set in the options database

obj - Optional object that provides the prefix used to search the options database

name - command line option

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

PF, PFView, PetscObjectViewFromOptions(), PFCreate()

src/vec/pf/interface/pf.c

Index of all PF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscpf.h" 
PetscErrorCode PFViewFromOptions(PF A, PetscObject obj, const char name[])
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

## PFView#

**URL:** https://petsc.org/release/manualpages/PF/PFView/

**Contents:**
- PFView#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Prints information about a mathematical function

Collective unless viewer is PETSC_VIEWER_STDOUT_SELF

viewer - optional visualization context

The available visualization contexts include

PETSC_VIEWER_STDOUT_SELF - standard output (default)

PETSC_VIEWER_STDOUT_WORLD - synchronized standard output where only the first processor opens the file. All other processors send their data to the first processor to print.

The user can open an alternative visualization contexts with PetscViewerASCIIOpen() (output to a specified file).

PF, PetscViewerCreate(), PetscViewerASCIIOpen()

src/vec/pf/interface/pf.c

PFView_Constant() in src/vec/pf/impls/constant/const.c PFView_Identity() in src/vec/pf/impls/constant/const.c PFView_Matlab() in src/vec/pf/impls/matlab/cmatlab.c PFView_String() in src/vec/pf/impls/string/cstring.c

Index of all PF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscpf.h" 
PetscErrorCode PFView(PF pf, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PETSC_VIEWER_STDOUT_SELF
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

## PF#

**URL:** https://petsc.org/release/manualpages/PF/PF/

**Contents:**
- PF#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Abstract PETSc mathematical function that can be evaluated with PFApply() and may be constructed at run time (see PFSTRING)

PFCreate(), PFDestroy(), PFSetType(), PFApply(), PFApplyVec(), PFSet(), PFType

src/snes/tutorials/ex22.c src/dm/tutorials/ex4.c

_p_PF in src/vec/pf/pfimpl.h PF_Matlab in src/vec/pf/impls/matlab/cmatlab.c

Index of all PF routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_PF *PF;
```

Example 2 (unknown):
```unknown
PFDestroy()
```

Example 3 (unknown):
```unknown
PFSetType()
```

Example 4 (unknown):
```unknown
PFApplyVec()
```

---

## pointInterpolationP4est#

**URL:** https://petsc.org/release/manualpages/LANDAU/pointInterpolationP4est/

**Contents:**
- pointInterpolationP4est#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#

One entry in the reduced quadrature-point map used by the DMPLEX Landau collision operator; pairs a global Landau matrix index with the weight that scales the contribution of the corresponding quadrature point

These records are arrays inside P4estVertexMaps and describe how multiple coincident quadrature points produced by the p4est-based AMR mesh are combined into a single entry of the Landau Jacobian.

LandauIdx, LandauCtx, LandauStaticData, DMPlexLandauCreateVelocitySpace()

include/petsclandau.h

Index of all LANDAU routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h"    
typedef struct {
  PetscReal scale;
  LandauIdx gid; // Landau matrix index (<10,000)
} pointInterpolationP4est;
```

Example 2 (unknown):
```unknown
P4estVertexMaps
```

Example 3 (unknown):
```unknown
LandauStaticData
```

Example 4 (unknown):
```unknown
DMPlexLandauCreateVelocitySpace()
```

---

## TSCreateQuadratureTS#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSCreateQuadratureTS/

**Contents:**
- TSCreateQuadratureTS#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Create a sub-TS that evaluates integrals over time

ts - the TS context obtained from TSCreate()

fwd - flag indicating whether to evaluate cost integral in the forward run or the adjoint run

quadts - the child TS context

TS: Scalable ODE and DAE Solvers, TSGetQuadratureTS()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSCreateQuadratureTS(TS ts, PetscBool fwd, TS *quadts)
```

Example 2 (unknown):
```unknown
TSGetQuadratureTS()
```

---

## TSGetQuadratureTS#

**URL:** https://petsc.org/release/manualpages/Sensitivity/TSGetQuadratureTS/

**Contents:**
- TSGetQuadratureTS#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Return the sub-TS that evaluates integrals over time

ts - the TS context obtained from TSCreate()

fwd - flag indicating whether to evaluate cost integral in the forward run or the adjoint run

quadts - the child TS context

TS: Scalable ODE and DAE Solvers, TSCreateQuadratureTS()

src/ts/interface/sensitivity/tssen.c

Index of all Sensitivity routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (cpp):
```cpp
#include <petscts.h>  
PetscErrorCode TSGetQuadratureTS(TS ts, PetscBool *fwd, TS *quadts)
```

Example 2 (unknown):
```unknown
TSCreateQuadratureTS()
```

---
