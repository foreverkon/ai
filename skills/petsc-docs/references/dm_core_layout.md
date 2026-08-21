# DM core and data layout

## Data Management (DM)#

**URL:** https://petsc.org/release/manualpages/DM/

**Contents:**
- Data Management (DM)#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Single list of manual pages#

DM objects are used to manage communication between the algebraic structures in PETSc (Vec and Mat) and mesh data structures in PDE-based (or other) simulations. See, for structured grids DMDA, for staggered grids DMSTAG, and for unstructured grids DMPLEX. Users guide chapter: DM: Interfacing Between Solvers and Models/Discretizations.

DMAdaptationCriterion

DMAdaptorSetFromOptions

DMBoundaryConditionType

DMGetLocalBoundingBox

DMInterpolationCreate

DMInterpolationDestroy

DMInterpolationEvaluate

DMRestoreGlobalVector

DMAdaptorGetSequenceLength

DMAdaptorMonitorCancel

DMAdaptorMonitorError

DMAdaptorMonitorErrorDraw

DMAdaptorMonitorErrorDrawLG

DMAdaptorMonitorErrorDrawLGCreate

DMAdaptorSetSequenceLength

DMCreateDomainDecomposition

DMCreateFieldDecomposition

DMCreateSectionSuperDM

DMFieldCreateDSWithDG

DMFieldGetNumComponents

DMFieldShellGetContext

DMFieldShellSetCreateDefaultQuadrature

DMFieldShellSetDestroy

DMFieldShellSetEvaluate

DMFieldShellSetEvaluateFE

DMFieldShellSetEvaluateFV

DMFieldShellSetGetDegree

DMGetApplicationContext

DMGetCellCoordinateDM

DMGetCellCoordinateSection

DMGetCellCoordinatesLocal

DMGetCoordinateSection

DMGetCoordinatesLocal

DMGetFieldAvoidTensor

DMGetNearNullSpaceConstructor

DMGetNullSpaceConstructor

DMGetOutputSequenceLength

DMGetOutputSequenceNumber

DMInterpolationAddPoints

DMInterpolationGetCoordinates

DMInterpolationGetDim

DMInterpolationGetDof

DMInterpolationGetVector

DMInterpolationRestoreVector

DMInterpolationSetDim

DMInterpolationSetDof

DMProjectBdFieldLabelLocal

DMProjectFieldLabelLocal

DMReorderSectionGetDefault

DMReorderSectionGetType

DMReorderSectionSetDefault

DMReorderSectionSetType

DMSetApplicationContext

DMSetApplicationContextDestroy

DMSetCellCoordinateDM

DMSetCellCoordinateSection

DMSetCellCoordinatesLocal

DMSetCoordinateSection

DMSetCoordinatesLocal

DMSetFieldAvoidTensor

DMSetNearNullSpaceConstructor

DMSetNullSpaceConstructor

DMSetOutputSequenceNumber

DMSwarmProjectGradientFields

DMAdaptorGetCriterion

DMAdaptorGetMixedSetupFunction

DMAdaptorMonitorRegister

DMAdaptorMonitorRegisterAll

DMAdaptorSetCriterion

DMAdaptorSetMixedSetupFunction

DMAdaptorSetOptionsPrefix

DMAppendOptionsPrefix

DMComputeVariableBounds

DMCreateInterpolationScale

DMGenerateRegisterAll

DMGenerateRegisterDestroy

DMGeomModelRegisterAll

DMGeomModelRegisterDestroy

DMGetCellCoordinatesLocalNoncollective

DMGetCellCoordinatesLocalSetUp

DMGetCoordinatesLocalNoncollective

DMGetCoordinatesLocalSetUp

DMGetCoordinatesLocalTuple

DMGetDefaultConstraints

DMGetLocalToGlobalMapping

DMGlobalToLocalBeginDefaultShell

DMGlobalToLocalEndDefaultShell

DMGlobalToLocalHookAdd

DMLocalToGlobalBeginDefaultShell

DMLocalToGlobalEndDefaultShell

DMLocalToGlobalHookAdd

DMLocalToLocalBeginDefaultShell

DMLocalToLocalEndDefaultShell

DMPolytopeGetOrientation

DMPolytopeGetVertexOrientation

DMPolytopeMatchOrientation

DMPolytopeMatchVertexOrientation

DMSetCellCoordinateField

DMSetDefaultConstraints

DMShellGetCreateInjection

DMShellGetCreateInterpolation

DMShellGetCreateRestriction

DMShellGetCreateSubDM

DMShellGetGlobalVector

DMShellSetCreateDomainDecomposition

DMShellSetCreateDomainDecompositionScatters

DMShellSetCreateFieldDecomposition

DMShellSetCreateGlobalVector

DMShellSetCreateInjection

DMShellSetCreateInterpolation

DMShellSetCreateLocalVector

DMShellSetCreateMatrix

DMShellSetCreateRestriction

DMShellSetCreateSubDM

DMShellSetDestroyContext

DMShellSetGlobalToLocal

DMShellSetGlobalToLocalVecScatter

DMShellSetGlobalVector

DMShellSetLocalToGlobal

DMShellSetLocalToGlobalVecScatter

DMShellSetLocalToLocal

DMShellSetLocalToLocalVecScatter

DMShellSetLocalVector

DMSlicedSetBlockFills

DMSlicedSetPreallocation

DMSubDomainHookRemove

PetscDualSpaceRegisterAll

PetscLimiterRegisterAll

PetscSpaceRegisterAll

DMAdaptorGetTransferFunction

DMAdaptorMonitorRegisterDestroy

DMAdaptorMonitorSetFromOptions

DMAdaptorRegisterDestroy

DMAdaptorSetTransferFunction

DMClearNamedGlobalVectors

DMClearNamedLocalVectors

DMComputeExactSolution

DMComputeL2GradientDiff

DMCreateDomainDecompositionScatters

DMCreateGradientMatrix

DMCreateInterpolation

DMCreateMassMatrixLumped

DMCreateSectionPermutation

DMFieldCreateDefaultFaceQuadrature

DMFieldCreateDefaultQuadrature

DMFieldFinalizePackage

DMFieldInitializePackage

DMFieldShellEvaluateFEDefault

DMFieldShellEvaluateFVDefault

DMGeneratorFunctionList

DMGetCoordinatesLocalized

DMGetCoordinatesLocalizedLocal

DMGetNamedGlobalVector

DMGetNamedLocalVector

DMHasCreateRestriction

DMHasNamedGlobalVector

DMHasNamedLocalVector

DMInterpolateSolution

DMLocalizeCoordinates

DMMonitorSetFromOptions

DMPrintCellVectorReal

DMProjectFunctionLabel

DMProjectFunctionLabelLocal

DMProjectFunctionLocal

DMRestoreNamedGlobalVector

DMRestoreNamedLocalVector

DMSetMatrixPreallocateOnly

DMSetMatrixPreallocateSkip

DMSetMatrixStructureOnly

PetscDSFinalizePackage

PetscDSInitializePackage

PetscFEFinalizePackage

PetscFEInitializePackage

PetscFVFinalizePackage

PetscFVInitializePackage

DMAdaptationCriterion

DMAdaptorGetCriterion

DMAdaptorGetMixedSetupFunction

DMAdaptorGetSequenceLength

DMAdaptorGetTransferFunction

DMAdaptorMonitorCancel

DMAdaptorMonitorError

DMAdaptorMonitorErrorDraw

DMAdaptorMonitorErrorDrawLG

DMAdaptorMonitorErrorDrawLGCreate

DMAdaptorMonitorRegister

DMAdaptorMonitorRegisterAll

DMAdaptorMonitorRegisterDestroy

DMAdaptorMonitorSetFromOptions

DMAdaptorRegisterDestroy

DMAdaptorSetCriterion

DMAdaptorSetFromOptions

DMAdaptorSetMixedSetupFunction

DMAdaptorSetOptionsPrefix

DMAdaptorSetSequenceLength

DMAdaptorSetTransferFunction

DMAppendOptionsPrefix

DMBoundaryConditionType

DMClearNamedGlobalVectors

DMClearNamedLocalVectors

DMComputeExactSolution

DMComputeL2GradientDiff

DMComputeVariableBounds

DMCreateDomainDecomposition

DMCreateDomainDecompositionScatters

DMCreateFieldDecomposition

DMCreateGradientMatrix

DMCreateInterpolation

DMCreateInterpolationScale

DMCreateMassMatrixLumped

DMCreateSectionPermutation

DMCreateSectionSuperDM

DMFieldCreateDSWithDG

DMFieldCreateDefaultFaceQuadrature

DMFieldCreateDefaultQuadrature

DMFieldFinalizePackage

DMFieldGetNumComponents

DMFieldInitializePackage

DMFieldShellEvaluateFEDefault

DMFieldShellEvaluateFVDefault

DMFieldShellGetContext

DMFieldShellSetCreateDefaultQuadrature

DMFieldShellSetDestroy

DMFieldShellSetEvaluate

DMFieldShellSetEvaluateFE

DMFieldShellSetEvaluateFV

DMFieldShellSetGetDegree

DMGenerateRegisterAll

DMGenerateRegisterDestroy

DMGeneratorFunctionList

DMGeomModelRegisterAll

DMGeomModelRegisterDestroy

DMGetApplicationContext

DMGetCellCoordinateDM

DMGetCellCoordinateSection

DMGetCellCoordinatesLocal

DMGetCellCoordinatesLocalNoncollective

DMGetCellCoordinatesLocalSetUp

DMGetCoordinateSection

DMGetCoordinatesLocal

DMGetCoordinatesLocalNoncollective

DMGetCoordinatesLocalSetUp

DMGetCoordinatesLocalTuple

DMGetCoordinatesLocalized

DMGetCoordinatesLocalizedLocal

DMGetDefaultConstraints

DMGetFieldAvoidTensor

DMGetLocalBoundingBox

DMGetLocalToGlobalMapping

DMGetNamedGlobalVector

DMGetNamedLocalVector

DMGetNearNullSpaceConstructor

DMGetNullSpaceConstructor

DMGetOutputSequenceLength

DMGetOutputSequenceNumber

DMGlobalToLocalBeginDefaultShell

DMGlobalToLocalEndDefaultShell

DMGlobalToLocalHookAdd

DMHasCreateRestriction

DMHasNamedGlobalVector

DMHasNamedLocalVector

DMInterpolateSolution

DMInterpolationAddPoints

DMInterpolationCreate

DMInterpolationDestroy

DMInterpolationEvaluate

DMInterpolationGetCoordinates

DMInterpolationGetDim

DMInterpolationGetDof

DMInterpolationGetVector

DMInterpolationRestoreVector

DMInterpolationSetDim

DMInterpolationSetDof

DMLocalToGlobalBeginDefaultShell

DMLocalToGlobalEndDefaultShell

DMLocalToGlobalHookAdd

DMLocalToLocalBeginDefaultShell

DMLocalToLocalEndDefaultShell

DMLocalizeCoordinates

DMMonitorSetFromOptions

DMPolytopeGetOrientation

DMPolytopeGetVertexOrientation

DMPolytopeMatchOrientation

DMPolytopeMatchVertexOrientation

DMPrintCellVectorReal

DMProjectBdFieldLabelLocal

DMProjectFieldLabelLocal

DMProjectFunctionLabel

DMProjectFunctionLabelLocal

DMProjectFunctionLocal

DMReorderSectionGetDefault

DMReorderSectionGetType

DMReorderSectionSetDefault

DMReorderSectionSetType

DMRestoreGlobalVector

DMRestoreNamedGlobalVector

DMRestoreNamedLocalVector

DMSetApplicationContext

DMSetApplicationContextDestroy

DMSetCellCoordinateDM

DMSetCellCoordinateField

DMSetCellCoordinateSection

DMSetCellCoordinatesLocal

DMSetCoordinateSection

DMSetCoordinatesLocal

DMSetDefaultConstraints

DMSetFieldAvoidTensor

DMSetMatrixPreallocateOnly

DMSetMatrixPreallocateSkip

DMSetMatrixStructureOnly

DMSetNearNullSpaceConstructor

DMSetNullSpaceConstructor

DMSetOutputSequenceNumber

DMShellGetCreateInjection

DMShellGetCreateInterpolation

DMShellGetCreateRestriction

DMShellGetCreateSubDM

DMShellGetGlobalVector

DMShellSetCreateDomainDecomposition

DMShellSetCreateDomainDecompositionScatters

DMShellSetCreateFieldDecomposition

DMShellSetCreateGlobalVector

DMShellSetCreateInjection

DMShellSetCreateInterpolation

DMShellSetCreateLocalVector

DMShellSetCreateMatrix

DMShellSetCreateRestriction

DMShellSetCreateSubDM

DMShellSetDestroyContext

DMShellSetGlobalToLocal

DMShellSetGlobalToLocalVecScatter

DMShellSetGlobalVector

DMShellSetLocalToGlobal

DMShellSetLocalToGlobalVecScatter

DMShellSetLocalToLocal

DMShellSetLocalToLocalVecScatter

DMShellSetLocalVector

DMSlicedSetBlockFills

DMSlicedSetPreallocation

DMSubDomainHookRemove

DMSwarmProjectGradientFields

PetscDSFinalizePackage

PetscDSInitializePackage

PetscDualSpaceRegisterAll

PetscFEFinalizePackage

PetscFEInitializePackage

PetscFVFinalizePackage

PetscFVInitializePackage

PetscLimiterRegisterAll

PetscSpaceRegisterAll

Data Management between Vec and Mat, and Distributed Mesh Data Structures

Structured Grids (DMDA)

---

## DMAdaptationCriterion#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptationCriterion/

**Contents:**
- DMAdaptationCriterion#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Describes the test used to decide whether to coarsen or refine parts of the mesh

DM_ADAPTATION_REFINE - uniformly refine a mesh, much like grid sequencing

DM_ADAPTATION_LABEL - adapt the mesh based upon a label of the cells filled with DMAdaptFlag markers.

DM_ADAPTATION_METRIC - try to mesh the manifold described by the input metric tensor uniformly. PETSc can also construct such a metric based upon an input primal or a gradient field.

DM_ADAPTATION_NONE - do no adaptation

DM Basics, DM, DMAdaptor, DMAdaptationStrategy, DMAdaptorSolve()

include/petscdmtypes.h

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  DM_ADAPTATION_NONE,
  DM_ADAPTATION_REFINE,
  DM_ADAPTATION_LABEL,
  DM_ADAPTATION_METRIC
} DMAdaptationCriterion;
```

Example 2 (unknown):
```unknown
DM_ADAPTATION_REFINE
```

Example 3 (unknown):
```unknown
DM_ADAPTATION_LABEL
```

Example 4 (unknown):
```unknown
DMAdaptFlag
```

---

## DMAdaptationStrategy#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptationStrategy/

**Contents:**
- DMAdaptationStrategy#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Describes the strategy used for adaptive solves

DM_ADAPTATION_INITIAL - refine a mesh based on an initial guess

DM_ADAPTATION_SEQUENTIAL - refine the mesh based on a sequence of solves, much like grid sequencing

DM_ADAPTATION_MULTILEVEL - use the sequence of constructed meshes in a multilevel solve, much like the Systematic Upscaling of Brandt

DM Basics, DM, DMAdaptor, DMAdaptationCriterion, DMAdaptorSolve()

include/petscdmtypes.h

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  DM_ADAPTATION_INITIAL,
  DM_ADAPTATION_SEQUENTIAL,
  DM_ADAPTATION_MULTILEVEL
} DMAdaptationStrategy;
```

Example 2 (unknown):
```unknown
DM_ADAPTATION_INITIAL
```

Example 3 (unknown):
```unknown
DM_ADAPTATION_SEQUENTIAL
```

Example 4 (unknown):
```unknown
DM_ADAPTATION_MULTILEVEL
```

---

## DMAdaptFlag#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptFlag/

**Contents:**
- DMAdaptFlag#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#
- Examples#
- Examples#

Marker in the label prescribing what adaptation to perform

DM_ADAPT_DETERMINE - undocumented

DM_ADAPT_KEEP - undocumented

DM_ADAPT_REFINE - undocumented

DM_ADAPT_COARSEN - undocumented

DM_ADAPT_COARSEN_LAST - undocumented

DM Basics, DM, DMAdaptor, DMAdaptationStrategy, DMAdaptationCriterion, DMAdaptorSolve(), DMAdaptLabel()

include/petscdmtypes.h

src/snes/tutorials/ex27.c src/ts/tutorials/ex11.c src/dm/impls/plex/tutorials/ex10.c

src/snes/tutorials/ex27.c src/ts/tutorials/ex11.c src/dm/impls/plex/tutorials/ex10.c src/ts/tutorials/ex30.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  DM_ADAPT_DETERMINE      = PETSC_DETERMINE,
  DM_ADAPT_KEEP           = 0,
  DM_ADAPT_REFINE         = 1,
  DM_ADAPT_COARSEN        = 2,
  DM_ADAPT_COARSEN_LAST   = 3,
  DM_ADAPT_RESERVED_COUNT = 4
} DMAdaptFlag;
```

Example 2 (unknown):
```unknown
DM_ADAPT_DETERMINE
```

Example 3 (unknown):
```unknown
DM_ADAPT_KEEP
```

Example 4 (unknown):
```unknown
DM_ADAPT_REFINE
```

---

## DMAdaptInterpolator#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptInterpolator/

**Contents:**
- DMAdaptInterpolator#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Adapts a grid interpolator so that it accurately reproduces a set of sample fine-grid vectors

In - the input (unadapted) interpolation matrix from dmc to dmf

smoother - a KSP whose operator provides the fine-grid matrix used to weight modes by their Rayleigh quotient

MF - a dense matrix whose columns are fine-grid sample vectors

MC - a dense matrix whose columns are the corresponding coarse-grid sample vectors (may be NULL, in which case \(I_n^T M_F\) is used)

user - unused application context

InAdapt - the adapted interpolation matrix (created inside the routine)

-dm_interpolator_adapt_debug flag - print diagnostic information about the least-squares systems solved for each row

For each row of In a small weighted least-squares problem is solved (using LAPACK GELSS) so that the adapted interpolation reproduces the fine-grid samples as accurately as possible; see the discussion of adaptive interpolation in manual/high_level_mg.rst.

KSP: Linear System Solvers, DM, Mat, KSP, DMCheckInterpolator(), DMCreateInterpolation(), PCMG

src/ksp/ksp/utils/dm/dmproject.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h" 
#include "petscdmda.h" 
#include "petscdmplex.h" 
#include "petscdmswarm.h" 
#include "petscksp.h" 
PetscErrorCode DMAdaptInterpolator(DM dmc, DM dmf, Mat In, KSP smoother, Mat MF, Mat MC, Mat *InAdapt, void *user)
```

Example 2 (unknown):
```unknown
manual/high_level_mg.rst
```

Example 3 (unknown):
```unknown
DMCheckInterpolator()
```

Example 4 (unknown):
```unknown
DMCreateInterpolation()
```

---

## DMAdaptLabel#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptLabel/

**Contents:**
- DMAdaptLabel#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Adapt a DM based on a DMLabel with values interpreted as coarsening and refining flags. Specific implementations of DM maybe have specialized flags, but all implementations should accept flag values DM_ADAPT_DETERMINE, DM_ADAPT_KEEP, DM_ADAPT_REFINE, and, DM_ADAPT_COARSEN.

dm - the pre-adaptation DM object

label - label with the flags

dmAdapt - the adapted DM object: may be NULL if an adapted DM could not be produced.

DM, DMAdaptMetric(), DMCoarsen(), DMRefine()

src/dm/interface/dmgenerate.c

src/snes/tutorials/ex27.c src/ts/tutorials/ex11.c src/dm/impls/plex/tutorials/ex10.c src/ts/tutorials/ex30.c

DMAdaptLabel_Forest() in src/dm/impls/forest/forest.c DMAdaptLabel_Plex() in src/dm/impls/plex/plexadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DM_ADAPT_DETERMINE
```

Example 2 (unknown):
```unknown
DM_ADAPT_KEEP
```

Example 3 (unknown):
```unknown
DM_ADAPT_REFINE
```

Example 4 (unknown):
```unknown
DM_ADAPT_COARSEN
```

---

## DMAdaptMetric#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptMetric/

**Contents:**
- DMAdaptMetric#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Generates a mesh adapted to the specified metric field.

metric - The metric to which the mesh is adapted, defined vertex-wise.

bdLabel - Label for boundary tags, which will be preserved in the output mesh. bdLabel should be NULL if there is no such label, and should be different from “boundary”.

rgLabel - Label for cell tags, which will be preserved in the output mesh. rgLabel should be NULL if there is no such label, and should be different from “regions”.

dmAdapt - Pointer to the DM object containing the adapted mesh

The label in the adapted mesh will be registered under the name of the input DMLabel object

DMAdaptLabel(), DMCoarsen(), DMRefine()

src/dm/interface/dmgenerate.c

src/ts/tutorials/ex45.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMAdaptMetric(DM dm, Vec metric, DMLabel bdLabel, DMLabel rgLabel, DM *dmAdapt)
```

Example 2 (unknown):
```unknown
DMAdaptLabel()
```

Example 3 (unknown):
```unknown
DMCoarsen()
```

---

## DMAdaptorAdapt#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorAdapt/

**Contents:**
- DMAdaptorAdapt#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Options Database Keys#
- See Also#
- Level#
- Location#

Creates a new DM that is adapted to the problem

adaptor - The DMAdaptor object

x - The global approximate solution

strategy - The adaptation strategy, see DMAdaptationStrategy

ax - The adapted solution

-snes_adapt (initial|sequential|multigrid) - adaption strategy, see DMAdaptationStrategy

-adapt_gradient_view - View the Clement interpolant of the solution gradient

-adapt_hessian_view - View the Clement interpolant of the solution Hessian

-adapt_metric_view - View the metric tensor for adaptive mesh refinement

DM Basics, DMAdaptor, DMAdaptationStrategy, DMAdaptorSetSolver(), DMAdaptorCreate()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorAdapt(DMAdaptor adaptor, Vec x, DMAdaptationStrategy strategy, DM *adm, Vec *ax)
```

Example 2 (unknown):
```unknown
DMAdaptationStrategy
```

Example 3 (unknown):
```unknown
DMAdaptationStrategy
```

Example 4 (unknown):
```unknown
DMAdaptationStrategy
```

---

## DMAdaptorCreate#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorCreate/

**Contents:**
- DMAdaptorCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Create a DMAdaptor object. Its purpose is to construct a adaptation DMLabel or metric Vec that can be used to modify the DM.

comm - The communicator for the DMAdaptor object

adaptor - The DMAdaptor object

DM Basics, DM, DMAdaptor, DMAdaptorDestroy(), DMAdaptorAdapt(), PetscConvEst, PetscConvEstCreate()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorCreate(MPI_Comm comm, DMAdaptor *adaptor)
```

Example 2 (unknown):
```unknown
DMAdaptorDestroy()
```

Example 3 (unknown):
```unknown
DMAdaptorAdapt()
```

Example 4 (unknown):
```unknown
PetscConvEst
```

---

## DMAdaptorDestroy#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorDestroy/

**Contents:**
- DMAdaptorDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Destroys a DMAdaptor object

adaptor - The DMAdaptor object

DM Basics, DM, DMAdaptor, DMAdaptorCreate(), DMAdaptorAdapt()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorDestroy(DMAdaptor *adaptor)
```

Example 2 (unknown):
```unknown
DMAdaptorCreate()
```

Example 3 (unknown):
```unknown
DMAdaptorAdapt()
```

---

## DMAdaptorGetCriterion#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorGetCriterion/

**Contents:**
- DMAdaptorGetCriterion#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the adaptation criterion

adaptor - the DMAdaptor

criterion - the criterion for adaptation

DMAdaptor, DMAdaptorSetCriterion(), DMAdaptationCriterion

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorGetCriterion(DMAdaptor adaptor, DMAdaptationCriterion *criterion)
```

Example 2 (unknown):
```unknown
DMAdaptorSetCriterion()
```

Example 3 (unknown):
```unknown
DMAdaptationCriterion
```

---

## DMAdaptorGetMixedSetupFunction#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorGetMixedSetupFunction/

**Contents:**
- DMAdaptorGetMixedSetupFunction#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the function setting up the mixed problem, if it exists

adaptor - the DMAdaptor

setupFunc - the function setting up the mixed problem, or NULL

DMAdaptor, DMAdaptorSetMixedSetupFunction(), DMAdaptorAdapt()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorGetMixedSetupFunction(DMAdaptor adaptor, PetscErrorCode (**setupFunc)(DMAdaptor, DM))
```

Example 2 (unknown):
```unknown
DMAdaptorSetMixedSetupFunction()
```

Example 3 (unknown):
```unknown
DMAdaptorAdapt()
```

---

## DMAdaptorGetSequenceLength#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorGetSequenceLength/

**Contents:**
- DMAdaptorGetSequenceLength#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the number of sequential adaptations used by an adapter

adaptor - The DMAdaptor object

num - The number of adaptations

DM Basics, DMAdaptor, DMAdaptorSetSequenceLength(), DMAdaptorCreate(), DMAdaptorAdapt()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorGetSequenceLength(DMAdaptor adaptor, PetscInt *num)
```

Example 2 (unknown):
```unknown
DMAdaptorSetSequenceLength()
```

Example 3 (unknown):
```unknown
DMAdaptorCreate()
```

Example 4 (unknown):
```unknown
DMAdaptorAdapt()
```

---

## DMAdaptorGetSolver#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorGetSolver/

**Contents:**
- DMAdaptorGetSolver#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the solver used to produce discrete solutions

adaptor - The DMAdaptor object

DM Basics, DM, DMAdaptor, DMAdaptorSetSolver(), DMAdaptorCreate(), DMAdaptorAdapt()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorGetSolver(DMAdaptor adaptor, SNES *snes)
```

Example 2 (unknown):
```unknown
DMAdaptorSetSolver()
```

Example 3 (unknown):
```unknown
DMAdaptorCreate()
```

Example 4 (unknown):
```unknown
DMAdaptorAdapt()
```

---

## DMAdaptorGetTransferFunction#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorGetTransferFunction/

**Contents:**
- DMAdaptorGetTransferFunction#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Calling sequence of tfunc#
- See Also#
- Level#
- Location#

Get the callback used by a DMAdaptor to transfer a solution vector from an old DM to the adapted DM

adaptor - the DMAdaptor object

tfunc - pointer to the transfer callback

adaptor - the DMAdaptor object

xin - the current solution

newdm - the adapted DM

xout - the transferred solution on newdm

ctx - application context, set with DMSetApplicationContext()

DMAdaptor, DMAdaptorSetTransferFunction(), DMAdaptorAdapt()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorGetTransferFunction(DMAdaptor adaptor, PetscErrorCode (**tfunc)(DMAdaptor adaptor, DM dm, Vec xin, DM newdm, Vec xout, PetscCtx ctx))
```

Example 2 (unknown):
```unknown
DMSetApplicationContext()
```

Example 3 (unknown):
```unknown
DMAdaptorSetTransferFunction()
```

Example 4 (unknown):
```unknown
DMAdaptorAdapt()
```

---

## DMAdaptorGetType#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorGetType/

**Contents:**
- DMAdaptorGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the type name (as a string) from the adaptor.

adaptor - The DMAdaptor

type - The DMAdaptorType name

DMPlex: Unstructured Grids, DM, DMPLEX, DMAdaptor, DMAdaptorType, DMAdaptorSetType(), DMAdaptorCreate()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorGetType(DMAdaptor adaptor, DMAdaptorType *type)
```

Example 2 (unknown):
```unknown
DMAdaptorType
```

Example 3 (unknown):
```unknown
DMAdaptorType
```

Example 4 (unknown):
```unknown
DMAdaptorSetType()
```

---

## DMAdaptorMonitorCancel#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorMonitorCancel/

**Contents:**
- DMAdaptorMonitorCancel#
- Synopsis#
- Input Parameter#
- Options Database Key#
- See Also#
- Level#
- Location#

Clears all monitors for a DMAdaptor object.

adaptor - the DMAdaptor

-dm_adaptor_monitor_cancel - Cancels all monitors that have been hardwired into a code by calls to DMAdaptorMonitorSet(), but does not cancel those set via the options database.

SNES: Nonlinear Solvers, DMAdaptorMonitorError(), DMAdaptorMonitorSet(), DMAdaptor

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorMonitorCancel(DMAdaptor adaptor)
```

Example 2 (unknown):
```unknown
DMAdaptorMonitorSet()
```

Example 3 (unknown):
```unknown
DMAdaptorMonitorError()
```

Example 4 (unknown):
```unknown
DMAdaptorMonitorSet()
```

---

## DMAdaptorMonitorErrorDrawLGCreate#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorMonitorErrorDrawLGCreate/

**Contents:**
- DMAdaptorMonitorErrorDrawLGCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Creates the context for the error plotter DMAdaptorMonitorErrorDrawLG()

viewer - The PetscViewer

format - The viewer format

ctx - An optional application context

vf - The viewer context

SNES: Nonlinear Solvers, PETSCVIEWERDRAW, PetscViewerMonitorGLSetUp(), DMAdaptor, DMAdaptorMonitorSet(), DMAdaptorMonitorErrorDrawLG()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMAdaptorMonitorErrorDrawLG()
```

Example 2 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorMonitorErrorDrawLGCreate(PetscViewer viewer, PetscViewerFormat format, PetscCtx ctx, PetscViewerAndFormat **vf)
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

## DMAdaptorMonitorErrorDrawLG#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorMonitorErrorDrawLG/

**Contents:**
- DMAdaptorMonitorErrorDrawLG#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Plots the error norm at each iteration of an adaptive loop.

adaptor - the DMAdaptor

odm - the original DM

Nf - number of fields

enorms - 2-norm error values for each field (may be estimated).

error - Vec of cellwise errors

vf - The viewer context, obtained via DMAdaptorMonitorErrorDrawLGCreate()

-adaptor_error draw::draw_lg - Activates DMAdaptorMonitorErrorDrawLG()

This is not called directly by users, rather one calls DMAdaptorMonitorSet(), with this function as an argument, to cause the monitor to be used during the adaptation loop.

Call DMAdaptorMonitorErrorDrawLGCreate() to create the context needed for this monitor

SNES: Nonlinear Solvers, PETSCVIEWERDRAW, DMAdaptor, DMAdaptorMonitorSet(), DMAdaptorMonitorErrorDraw(), DMAdaptorMonitorError(), DMAdaptorMonitorTrueResidualDrawLGCreate()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorMonitorErrorDrawLG(DMAdaptor adaptor, PetscInt n, DM odm, DM adm, PetscInt Nf, PetscReal enorms[], Vec error, PetscViewerAndFormat *vf)
```

Example 2 (unknown):
```unknown
DMAdaptorMonitorErrorDrawLGCreate()
```

Example 3 (unknown):
```unknown
DMAdaptorMonitorErrorDrawLG()
```

Example 4 (unknown):
```unknown
DMAdaptorMonitorSet()
```

---

## DMAdaptorMonitorErrorDraw#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorMonitorErrorDraw/

**Contents:**
- DMAdaptorMonitorErrorDraw#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Plots the error at each iteration of an iterative solver.

adaptor - the DMAdaptor

odm - the original DM

Nf - number of fields

enorms - 2-norm error values for each field (may be estimated).

error - Vec of cellwise errors

vf - The viewer context

-adaptor_monitor_error draw - Activates DMAdaptorMonitorErrorDraw()

This is not called directly by users, rather one calls DMAdaptorMonitorSet(), with this function as an argument, to cause the monitor to be used during the adaptation loop.

SNES: Nonlinear Solvers, PETSCVIEWERDRAW, DMAdaptor, DMAdaptorMonitorSet(), DMAdaptorMonitorErrorDrawLG()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorMonitorErrorDraw(DMAdaptor adaptor, PetscInt n, DM odm, DM adm, PetscInt Nf, PetscReal enorms[], Vec error, PetscViewerAndFormat *vf)
```

Example 2 (unknown):
```unknown
DMAdaptorMonitorErrorDraw()
```

Example 3 (unknown):
```unknown
DMAdaptorMonitorSet()
```

Example 4 (unknown):
```unknown
PETSCVIEWERDRAW
```

---

## DMAdaptorMonitorError#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorMonitorError/

**Contents:**
- DMAdaptorMonitorError#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Prints the error norm at each iteration of an adaptation loop.

adaptor - the DMAdaptor

odm - the original DM

Nf - number of fields

enorms - 2-norm error values for each field (may be estimated).

error - Vec of cellwise errors

vf - The viewer context

-adaptor_monitor_error - Activates DMAdaptorMonitorError()

This is not called directly by users, rather one calls DMAdaptorMonitorSet(), with this function as an argument, to cause the monitor to be used during the adaptation loop.

SNES: Nonlinear Solvers, DMAdaptor, DMAdaptorMonitorSet(), DMAdaptorMonitorErrorDraw(), DMAdaptorMonitorErrorDrawLG()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorMonitorError(DMAdaptor adaptor, PetscInt n, DM odm, DM adm, PetscInt Nf, PetscReal enorms[], Vec error, PetscViewerAndFormat *vf)
```

Example 2 (unknown):
```unknown
DMAdaptorMonitorError()
```

Example 3 (unknown):
```unknown
DMAdaptorMonitorSet()
```

Example 4 (unknown):
```unknown
DMAdaptorMonitorSet()
```

---

## DMAdaptorMonitorRegisterAll#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorMonitorRegisterAll/

**Contents:**
- DMAdaptorMonitorRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the mesh adaptation monitors in the SNES package.

SNES: Nonlinear Solvers, SNES, DM, DMAdaptorMonitorRegister(), DMAdaptorRegister()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorMonitorRegisterAll(void)
```

Example 2 (unknown):
```unknown
DMAdaptorMonitorRegister()
```

Example 3 (unknown):
```unknown
DMAdaptorRegister()
```

---

## DMAdaptorMonitorRegisterDestroy#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorMonitorRegisterDestroy/

**Contents:**
- DMAdaptorMonitorRegisterDestroy#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys the registered monitors for DMAdaptor. It is called from PetscFinalize().

DMPlex: Unstructured Grids, DM, DMPLEX, DMAdaptorMonitorRegisterAll(), DMAdaptor, PetscFinalize()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorMonitorRegisterDestroy(void)
```

Example 3 (unknown):
```unknown
DMAdaptorMonitorRegisterAll()
```

Example 4 (unknown):
```unknown
PetscFinalize()
```

---

## DMAdaptorMonitorRegister#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorMonitorRegister/

**Contents:**
- DMAdaptorMonitorRegister#
- Synopsis#
- Input Parameters#
- Note#
- Example Usage#
- See Also#
- Level#
- Location#

Registers a mesh adaptation monitor routine that may be accessed with DMAdaptorMonitorSetFromOptions()

name - name of a new monitor routine

vtype - A PetscViewerType for the output

format - A PetscViewerFormat for the output

monitor - Monitor routine

create - Creation routine, or NULL

destroy - Destruction routine, or NULL

DMAdaptorMonitorRegister() may be called multiple times to add several user-defined monitors.

Then, your monitor can be chosen with the procedural interface via

or at runtime via the option -adaptor_monitor_my_monitor

SNES: Nonlinear Solvers, DMAdaptor, DMAdaptorMonitorSet(), DMAdaptorMonitorRegisterAll(), DMAdaptorMonitorSetFromOptions()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMAdaptorMonitorSetFromOptions()
```

Example 2 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorMonitorRegister(const char name[], PetscViewerType vtype, PetscViewerFormat format, PetscErrorCode (*monitor)(DMAdaptor, PetscInt, DM, DM, PetscInt, PetscReal[], Vec, PetscViewerAndFormat *), PetscErrorCode (*create)(PetscViewer, PetscViewerFormat, void *, PetscViewerAndFormat **), PetscErrorCode (*destroy)(PetscViewerAndFormat **))
```

Example 3 (unknown):
```unknown
PetscViewerType
```

Example 4 (unknown):
```unknown
PetscViewerFormat
```

---

## DMAdaptorMonitorSetFromOptions#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorMonitorSetFromOptions/

**Contents:**
- DMAdaptorMonitorSetFromOptions#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets a monitor function and viewer appropriate for the type indicated by the user in the options database

adaptor - DMadaptor object you wish to monitor

opt - the command line option for this monitor

name - the monitor type one is seeking

ctx - An optional application context for the monitor, or NULL

SNES: Nonlinear Solvers, DMAdaptorMonitorRegister(), DMAdaptorMonitorSet(), PetscOptionsGetViewer()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorMonitorSetFromOptions(DMAdaptor adaptor, const char opt[], const char name[], PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMAdaptorMonitorRegister()
```

Example 3 (unknown):
```unknown
DMAdaptorMonitorSet()
```

Example 4 (unknown):
```unknown
PetscOptionsGetViewer()
```

---

## DMAdaptorMonitorSet#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorMonitorSet/

**Contents:**
- DMAdaptorMonitorSet#
- Synopsis#
- Input Parameters#
- Calling sequence of monitor#
- Options Database Keys#
- See Also#
- Level#
- Location#

Sets an ADDITIONAL function to be called at every iteration to monitor the error etc.

adaptor - the DMAdaptor

monitor - pointer to function (if this is NULL, it turns off monitoring

ctx - [optional] context for private data for the monitor routine (use NULL if no context is needed)

monitordestroy - [optional] routine that frees monitor context (may be NULL), see PetscCtxDestroyFn for its calling sequence

adaptor - the DMAdaptor

it - iteration number

odm - the original DM

Nf - number of fields

enorms - (estimated) 2-norm of the error for each field

error - Vec of cellwise errors

ctx - optional monitoring context, as set by DMAdaptorMonitorSet()

-adaptor_monitor_size - sets DMAdaptorMonitorSize()

-adaptor_monitor_error - sets DMAdaptorMonitorError()

-adaptor_monitor_error draw - sets DMAdaptorMonitorErrorDraw() and plots error

-adaptor_monitor_error draw::draw_lg - sets DMAdaptorMonitorErrorDrawLG() and plots error

-dm_adaptor_monitor_cancel - Cancels all monitors that have been hardwired into a code by calls to DMAdaptorMonitorSet(), but does not cancel those set via the options database.

SNES: Nonlinear Solvers, DMAdaptorMonitorError(), DMAdaptor, PetscCtxDestroyFn

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorMonitorSet(DMAdaptor adaptor, PetscErrorCode (*monitor)(DMAdaptor adaptor, PetscInt it, DM odm, DM adm, PetscInt Nf, PetscReal enorms[], Vec error, PetscCtx ctx), PetscCtx ctx, PetscCtxDestroyFn *monitordestroy)
```

Example 2 (unknown):
```unknown
PetscCtxDestroyFn
```

Example 3 (unknown):
```unknown
DMAdaptorMonitorSet()
```

Example 4 (unknown):
```unknown
DMAdaptorMonitorSize()
```

---

## DMAdaptorMonitorSize#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorMonitorSize/

**Contents:**
- DMAdaptorMonitorSize#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Prints the mesh sizes at each iteration of an adaptation loop.

adaptor - the DMAdaptor

odm - the original DM

Nf - number of fields

enorms - 2-norm error values for each field (may be estimated).

error - Vec of cellwise errors

vf - The viewer context

-adaptor_monitor_size - Activates DMAdaptorMonitorSize()

This is not called directly by users, rather one calls DMAdaptorMonitorSet(), with this function as an argument, to cause the monitor to be used during the adaptation loop.

SNES: Nonlinear Solvers, DMAdaptor, DMAdaptorMonitorSet(), DMAdaptorMonitorError(), DMAdaptorMonitorErrorDraw(), DMAdaptorMonitorErrorDrawLG()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorMonitorSize(DMAdaptor adaptor, PetscInt n, DM odm, DM adm, PetscInt Nf, PetscReal enorms[], Vec error, PetscViewerAndFormat *vf)
```

Example 2 (unknown):
```unknown
DMAdaptorMonitorSize()
```

Example 3 (unknown):
```unknown
DMAdaptorMonitorSet()
```

Example 4 (unknown):
```unknown
DMAdaptorMonitorSet()
```

---

## DMAdaptorMonitor#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorMonitor/

**Contents:**
- DMAdaptorMonitor#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

runs the user provided monitor routines, if they exist

adaptor - the DMAdaptor

it - iteration number

odm - the original DM

Nf - the number of fields

enorms - the 2-norm error values for each field

error - Vec of cellwise errors

This routine is called by the DMAdaptor implementations. It does not typically need to be called by the user.

SNES: Nonlinear Solvers, DMAdaptorMonitorSet()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorMonitor(DMAdaptor adaptor, PetscInt it, DM odm, DM adm, PetscInt Nf, PetscReal enorms[], Vec error)
```

Example 2 (unknown):
```unknown
DMAdaptorMonitorSet()
```

---

## DMAdaptorRegisterAll#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorRegisterAll/

**Contents:**
- DMAdaptorRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the adaptor components in the DM package.

DMPlex: Unstructured Grids, DM, DMPLEX, DMAdaptorType, DMRegisterAll(), DMAdaptorRegisterDestroy()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorRegisterAll(void)
```

Example 2 (unknown):
```unknown
DMAdaptorType
```

Example 3 (unknown):
```unknown
DMRegisterAll()
```

Example 4 (unknown):
```unknown
DMAdaptorRegisterDestroy()
```

---

## DMAdaptorRegisterDestroy#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorRegisterDestroy/

**Contents:**
- DMAdaptorRegisterDestroy#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys the registered DMAdaptorType. It is called from PetscFinalize().

DMPlex: Unstructured Grids, DM, DMPLEX, DMAdaptorRegisterAll(), DMAdaptorType, PetscFinalize()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMAdaptorType
```

Example 2 (unknown):
```unknown
PetscFinalize()
```

Example 3 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorRegisterDestroy(void)
```

Example 4 (unknown):
```unknown
DMAdaptorRegisterAll()
```

---

## DMAdaptorRegister#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorRegister/

**Contents:**
- DMAdaptorRegister#
- Synopsis#
- Input Parameters#
- Example Usage#
- Note#
- See Also#
- Level#
- Location#

Adds a new adaptor component implementation

name - The name of a new user-defined creation routine

create_func - The creation routine

Then, your adaptor type can be chosen with the procedural interface via

or at runtime via the option

DMAdaptorRegister() may be called multiple times to add several user-defined adaptors

DMPlex: Unstructured Grids, DM, DMPLEX, DMAdaptor, DMAdaptorRegisterAll(), DMAdaptorRegisterDestroy()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorRegister(const char name[], PetscErrorCode (*create_func)(DMAdaptor))
```

Example 2 (unknown):
```unknown
DMAdaptorRegister("my_adaptor", MyAdaptorCreate);
```

Example 3 (unknown):
```unknown
DMAdaptorCreate(MPI_Comm, DMAdaptor *);
  DMAdaptorSetType(DMAdaptor, "my_adaptor");
```

Example 4 (unknown):
```unknown
-adaptor_type my_adaptor
```

---

## DMAdaptorSetCriterion#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorSetCriterion/

**Contents:**
- DMAdaptorSetCriterion#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the adaptation criterion

adaptor - the DMAdaptor

criterion - the adaptation criterion

DMAdaptor, DMAdaptorGetCriterion(), DMAdaptationCriterion

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorSetCriterion(DMAdaptor adaptor, DMAdaptationCriterion criterion)
```

Example 2 (unknown):
```unknown
DMAdaptorGetCriterion()
```

Example 3 (unknown):
```unknown
DMAdaptationCriterion
```

---

## DMAdaptorSetFromOptions#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorSetFromOptions/

**Contents:**
- DMAdaptorSetFromOptions#
- Synopsis#
- Input Parameter#
- Options Database Keys#
- See Also#
- Level#
- Location#

Sets properties of a DMAdaptor object from values in the options database

adaptor - The DMAdaptor object

-adaptor_monitor_size - Monitor the mesh size

-adaptor_monitor_error - Monitor the solution error

-adaptor_sequence_num num - Number of adaptations to generate an optimal grid

-adaptor_target_num num - Set the target number of vertices N_adapt, -1 for automatic determination

-adaptor_refinement_factor r - Set r such that N_adapt = r^dim N_orig

-adaptor_mixed_setup_function func - Set the function func that sets up the mixed problem

DM Basics, DM, DMAdaptor, DMAdaptorCreate(), DMAdaptorAdapt()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorSetFromOptions(DMAdaptor adaptor)
```

Example 2 (unknown):
```unknown
DMAdaptorCreate()
```

Example 3 (unknown):
```unknown
DMAdaptorAdapt()
```

---

## DMAdaptorSetMixedSetupFunction#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorSetMixedSetupFunction/

**Contents:**
- DMAdaptorSetMixedSetupFunction#
- Synopsis#
- Input Parameters#
- Calling sequence of setupFunc#
- See Also#
- Level#
- Location#

Set the function setting up the mixed problem

adaptor - the DMAdaptor

setupFunc - the function setting up the mixed problem

adaptor - the DMAdaptor

DMAdaptor, DMAdaptorGetMixedSetupFunction(), DMAdaptorAdapt()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorSetMixedSetupFunction(DMAdaptor adaptor, PetscErrorCode (*setupFunc)(DMAdaptor adaptor, DM dm))
```

Example 2 (unknown):
```unknown
DMAdaptorGetMixedSetupFunction()
```

Example 3 (unknown):
```unknown
DMAdaptorAdapt()
```

---

## DMAdaptorSetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorSetOptionsPrefix/

**Contents:**
- DMAdaptorSetOptionsPrefix#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the prefix used for searching for all DMAdaptor options in the database.

adaptor - the DMAdaptor

prefix - the prefix to prepend to all option names

A hyphen (-) must NOT be given at the beginning of the prefix name. The first character of all runtime options is AUTOMATICALLY the hyphen.

SNES: Nonlinear Solvers, DMAdaptor, SNESSetOptionsPrefix(), DMAdaptorSetFromOptions()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorSetOptionsPrefix(DMAdaptor adaptor, const char prefix[])
```

Example 2 (unknown):
```unknown
SNESSetOptionsPrefix()
```

Example 3 (unknown):
```unknown
DMAdaptorSetFromOptions()
```

---

## DMAdaptorSetSequenceLength#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorSetSequenceLength/

**Contents:**
- DMAdaptorSetSequenceLength#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the number of sequential adaptations

adaptor - The DMAdaptor object

num - The number of adaptations

DM Basics, DMAdaptorGetSequenceLength(), DMAdaptorCreate(), DMAdaptorAdapt()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorSetSequenceLength(DMAdaptor adaptor, PetscInt num)
```

Example 2 (unknown):
```unknown
DMAdaptorGetSequenceLength()
```

Example 3 (unknown):
```unknown
DMAdaptorCreate()
```

Example 4 (unknown):
```unknown
DMAdaptorAdapt()
```

---

## DMAdaptorSetSolver#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorSetSolver/

**Contents:**
- DMAdaptorSetSolver#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the solver used to produce discrete solutions

adaptor - The DMAdaptor object

snes - The solver, this MUST have an attached DM/PetscDS, so that the exact solution can be computed

DM Basics, DMAdaptor, DMAdaptorGetSolver(), DMAdaptorCreate(), DMAdaptorAdapt()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorSetSolver(DMAdaptor adaptor, SNES snes)
```

Example 2 (unknown):
```unknown
DMAdaptorGetSolver()
```

Example 3 (unknown):
```unknown
DMAdaptorCreate()
```

Example 4 (unknown):
```unknown
DMAdaptorAdapt()
```

---

## DMAdaptorSetTransferFunction#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorSetTransferFunction/

**Contents:**
- DMAdaptorSetTransferFunction#
- Synopsis#
- Input Parameters#
- Calling sequence of tfunc#
- See Also#
- Level#
- Location#

Set the callback used by a DMAdaptor to transfer a solution vector from an old DM to the adapted DM

adaptor - the DMAdaptor object

tfunc - the transfer callback

adaptor - the DMAdaptor object

xin - the current solution

newdm - the adapted DM

xout - the transferred solution on newdm

ctx - application context, set with DMSetApplicationContext()

DMAdaptor, DMAdaptorGetTransferFunction(), DMAdaptorAdapt()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorSetTransferFunction(DMAdaptor adaptor, PetscErrorCode (*tfunc)(DMAdaptor adaptor, DM dm, Vec xin, DM newdm, Vec xout, PetscCtx ctx))
```

Example 2 (unknown):
```unknown
DMSetApplicationContext()
```

Example 3 (unknown):
```unknown
DMAdaptorGetTransferFunction()
```

Example 4 (unknown):
```unknown
DMAdaptorAdapt()
```

---

## DMAdaptorSetType#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorSetType/

**Contents:**
- DMAdaptorSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Sets the particular implementation for a adaptor.

adaptor - The DMAdaptor

method - The name of the adaptor type

-adaptor_type type - Sets the adaptor type; see DMAdaptorType

DMPlex: Unstructured Grids, DM, DMPLEX, DMAdaptor, DMAdaptorType, DMAdaptorGetType(), DMAdaptorCreate()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorSetType(DMAdaptor adaptor, DMAdaptorType method)
```

Example 2 (unknown):
```unknown
DMAdaptorType
```

Example 3 (unknown):
```unknown
DMAdaptorType
```

Example 4 (unknown):
```unknown
DMAdaptorGetType()
```

---

## DMAdaptorSetUp#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorSetUp/

**Contents:**
- DMAdaptorSetUp#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

After the solver is specified, creates data structures for controlling adaptivity

adaptor - The DMAdaptor object

DM Basics, DMAdaptor, DMAdaptorCreate(), DMAdaptorAdapt()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorSetUp(DMAdaptor adaptor)
```

Example 2 (unknown):
```unknown
DMAdaptorCreate()
```

Example 3 (unknown):
```unknown
DMAdaptorAdapt()
```

---

## DMAdaptorType#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorType/

**Contents:**
- DMAdaptorType#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#

String with the name of a PETSc DMAdaptor type

Metric-based mesh adaptation for a table of available matrix types

Metric-based mesh adaptation, DMPlex: Unstructured Grids, DMAdaptorCreate(), DMAdaptor, DMAdaptorRegister()

include/petscdmadaptor.h

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef const char *DMAdaptorType;
#define DMADAPTORGRADIENT "gradient"
#define DMADAPTORFLUX     "flux"
```

Example 2 (unknown):
```unknown
DMAdaptorCreate()
```

Example 3 (unknown):
```unknown
DMAdaptorRegister()
```

---

## DMAdaptorView#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptorView/

**Contents:**
- DMAdaptorView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Views a DMAdaptor object

adaptor - The DMAdaptor object

viewer - The PetscViewer object

DM Basics, DM, DMAdaptor, DMAdaptorCreate(), DMAdaptorAdapt()

src/snes/utils/dm/dmadapt.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmadaptor.h" 
PetscErrorCode DMAdaptorView(DMAdaptor adaptor, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
DMAdaptorCreate()
```

Example 4 (unknown):
```unknown
DMAdaptorAdapt()
```

---

## DMAdaptor#

**URL:** https://petsc.org/release/manualpages/DM/DMAdaptor/

**Contents:**
- DMAdaptor#
- Synopsis#
- See Also#
- Level#
- Location#
- Implementations#

An object that constructs a DMLabel or metric Vec that can be used to modify a DM based on error estimators or other criteria

DM Basics, DM, DMAdaptorCreate(), DMAdaptorSetSolver(), DMAdaptorGetSolver(), DMAdaptorSetSequenceLength(), DMAdaptorGetSequenceLength(), DMAdaptorSetFromOptions(), DMAdaptorSetUp(), DMAdaptorAdapt(), DMAdaptorDestroy(), DMAdaptorGetTransferFunction(), PetscConvEstCreate(), PetscConvEstDestroy()

include/petscdmadaptortypes.h

_p_DMAdaptor in include/petsc/private/dmadaptorimpl.h

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_DMAdaptor *DMAdaptor;
```

Example 2 (unknown):
```unknown
DMAdaptorCreate()
```

Example 3 (unknown):
```unknown
DMAdaptorSetSolver()
```

Example 4 (unknown):
```unknown
DMAdaptorGetSolver()
```

---

## DMAddBoundary#

**URL:** https://petsc.org/release/manualpages/DM/DMAddBoundary/

**Contents:**
- DMAddBoundary#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Add a boundary condition, for a single field, to a model represented by a DM

dm - The DM, with a PetscDS that matches the problem being constrained

type - The type of condition, e.g. DM_BC_ESSENTIAL_ANALYTIC, DM_BC_ESSENTIAL_FIELD (Dirichlet), or DM_BC_NATURAL (Neumann)

label - The label defining constrained points

Nv - The number of DMLabel values for constrained points

values - An array of values for constrained points

field - The field to constrain

Nc - The number of constrained field components (0 will constrain all components)

comps - An array of constrained component numbers

bcFunc - A pointwise function giving boundary values

bcFunc_t - A pointwise function giving the time derivative of the boundary values, or NULL

ctx - An optional application context for bcFunc

bd - (Optional) Boundary number

-bc_NAME values - Overrides the boundary ids for boundary named NAME

-bc_NAME_comp comps - Overrides the boundary components for boundary named NAME

If the DM is of type DMPLEX and the field is of type PetscFE, then this function completes the label using DMPlexLabelComplete().

Both bcFunc and bcFunc_t will depend on the boundary condition type. If the type if DM_BC_ESSENTIAL, then the calling sequence is:

If the type is DM_BC_ESSENTIAL_FIELD or other _FIELD value, then the calling sequence is:

dim - the spatial dimension

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

DM Basics, DM, DSGetBoundary(), PetscDSAddBoundary()

src/dm/interface/dm.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex26.c src/snes/tutorials/ex17.c src/snes/tutorials/ex8.c src/snes/tutorials/ex23.c src/snes/tutorials/ex64.c src/snes/tutorials/ex62.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMAddBoundary(DM dm, DMBoundaryConditionType type, const char name[], DMLabel label, PetscInt Nv, const PetscInt values[], PetscInt field, PetscInt Nc, const PetscInt comps[], PetscVoidFn *bcFunc, PetscVoidFn *bcFunc_t, PetscCtx ctx, PetscInt *bd)
```

Example 2 (unknown):
```unknown
DM_BC_ESSENTIAL_ANALYTIC
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

## DMAddField#

**URL:** https://petsc.org/release/manualpages/DM/DMAddField/

**Contents:**
- DMAddField#
- Synopsis#
- Input Parameters#
- Notes#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Add a field to a DM object. A field is a function space defined by of a set of discretization points (geometric entities) and a discretization object that defines the function space associated with those points.

label - The label indicating the support of the field, or NULL for the entire mesh

disc - The discretization object

The label already exists or will be added to the DM with DMSetLabel().

For example, a piecewise continuous pressure field can be defined by coefficients at the cell centers of a mesh and piecewise constant functions within each cell. Thus a specific function in the space is defined by the combination of a Vec containing the coefficients, a DM defining the geometry entities, a DMLabel indicating a subset of those geometric entities, and a discretization object, such as a PetscFE.

Use the argument PetscObjectCast(disc) as the second argument

DM Basics, DM, DMSetLabel(), DMSetField(), DMGetField(), PetscFE

src/dm/interface/dm.c

src/dm/impls/plex/tutorials/ex15.c src/ts/tutorials/ex11.c src/dm/impls/plex/tutorials/ex8.c src/dm/impls/plex/tutorials/ex16.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMAddField(DM dm, DMLabel label, PetscObject disc)
```

Example 2 (unknown):
```unknown
DMSetLabel()
```

Example 3 (unknown):
```unknown
PetscObjectCast(disc)
```

Example 4 (unknown):
```unknown
DMSetLabel()
```

---

## DMAddLabel#

**URL:** https://petsc.org/release/manualpages/DM/DMAddLabel/

**Contents:**
- DMAddLabel#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Add the label to this DM

DM Basics, DM, DMLabel, DMCreateLabel(), DMHasLabel(), DMGetLabelValue(), DMSetLabelValue(), DMGetStratumIS()

src/dm/interface/dm.c

src/dm/label/tutorials/ex1.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMAddLabel(DM dm, DMLabel label)
```

Example 2 (unknown):
```unknown
DMCreateLabel()
```

Example 3 (unknown):
```unknown
DMHasLabel()
```

Example 4 (unknown):
```unknown
DMGetLabelValue()
```

---

## DMAppendOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/DM/DMAppendOptionsPrefix/

**Contents:**
- DMAppendOptionsPrefix#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Appends an additional string to an already existing prefix used for searching for DM options in the options database.

prefix - the string to append to the current prefix

If the DM does not currently have an options prefix then this value is used alone as the prefix as if DMSetOptionsPrefix() had been called. A hyphen (-) must NOT be given at the beginning of the prefix name. The first character of all runtime options is AUTOMATICALLY the hyphen.

DM Basics, DM, DMSetOptionsPrefix(), DMGetOptionsPrefix(), PetscObjectAppendOptionsPrefix(), DMSetFromOptions()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMAppendOptionsPrefix(DM dm, const char prefix[])
```

Example 2 (unknown):
```unknown
DMSetOptionsPrefix()
```

Example 3 (unknown):
```unknown
DMSetOptionsPrefix()
```

Example 4 (unknown):
```unknown
DMGetOptionsPrefix()
```

---

## DMBlockingType#

**URL:** https://petsc.org/release/manualpages/DM/DMBlockingType/

**Contents:**
- DMBlockingType#
- Synopsis#
- Values#
- Note#
- See Also#
- Level#
- Location#

Describes how to choose variable block sizes

DM_BLOCKING_TOPOLOGICAL_POINT - select all fields at a topological point (cell center, at a face, etc)

DM_BLOCKING_FIELD_NODE - using a separate block for each field at a topological point

When using PCVPBJACOBI, one can choose to block by topological point (all fields at a cell center, at a face, etc.) or by field nodes (using number of components per field to identify “nodes”). Field nodes lead to smaller blocks, but may converge more slowly. For example, a cubic Lagrange hexahedron will have one node at vertices, two at edges, four at faces, and eight at cell centers. If using point blocking, the PCVPBJACOBI preconditioner will work with block sizes up to 8 Lagrange nodes. For 5-component CFD, this produces matrices up to 40x40, which increases memory footprint and may harm performance. With field node blocking, the maximum block size will correspond to one Lagrange node, or 5x5 blocks for the CFD example.

DM Basics, PCVPBJACOBI, MatSetVariableBlockSizes(), DMSetBlockingType()

include/petscdmtypes.h

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  DM_BLOCKING_TOPOLOGICAL_POINT,
  DM_BLOCKING_FIELD_NODE
} DMBlockingType;
```

Example 2 (unknown):
```unknown
DM_BLOCKING_TOPOLOGICAL_POINT
```

Example 3 (unknown):
```unknown
DM_BLOCKING_FIELD_NODE
```

Example 4 (unknown):
```unknown
PCVPBJACOBI
```

---

## DMBoundaryConditionType#

**URL:** https://petsc.org/release/manualpages/DM/DMBoundaryConditionType/

**Contents:**
- DMBoundaryConditionType#
- Synopsis#
- Values#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Examples#
- Examples#

indicates what type of boundary condition is to be imposed

DM_BC_ESSENTIAL - A Dirichlet condition using a function of the coordinates

DM_BC_ESSENTIAL_FIELD - A Dirichlet condition using a function of the coordinates and auxiliary field data

DM_BC_ESSENTIAL_BD_FIELD - A Dirichlet condition using a function of the coordinates, facet normal, and auxiliary field data

DM_BC_NATURAL - A Neumann condition using a function of the coordinates

DM_BC_NATURAL_FIELD - A Neumann condition using a function of the coordinates and auxiliary field data

DM_BC_NATURAL_RIEMANN - A flux condition which determines the state in ghost cells

DM_BC_LOWER_BOUND - A lower bound on the solution along a boundary

DM_BC_UPPER_BOUND - An upper bound on the solution along a boundary

The user can check whether a boundary condition is essential using (type & DM_BC_ESSENTIAL), and similarly for natural conditions (type & DM_BC_NATURAL)

DM Basics, DM, DMAddBoundary(), DSAddBoundary(), DSGetBoundary()

include/petscdmtypes.h

src/snes/tutorials/ex12.c

src/ts/tutorials/ex11.c src/ts/tutorials/ex18.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex26.c src/snes/tutorials/ex17.c src/snes/tutorials/ex8.c src/snes/tutorials/ex23.c src/snes/tutorials/ex64.c src/snes/tutorials/ex62.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex62.c src/snes/tutorials/ex12.c src/ts/tutorials/ex76.c src/snes/tutorials/ex56.c src/snes/tutorials/ex17.c src/ts/tutorials/ex53.c src/snes/tutorials/ex24.c src/snes/tutorials/ex27.c src/snes/tutorials/ex77.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  DM_BC_ESSENTIAL          = 1,
  DM_BC_ESSENTIAL_FIELD    = 5,
  DM_BC_NATURAL            = 2,
  DM_BC_NATURAL_FIELD      = 6,
  DM_BC_ESSENTIAL_BD_FIELD = 9,
  DM_BC_NATURAL_RIEMANN    = 10,
  DM_BC_LOWER_BOUND        = 4,
  DM_BC_UPPER_BOUND        = 8
} DMBoundaryConditionType;
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
DM_BC_ESSENTIAL_BD_FIELD
```

---

## DMBoundaryType#

**URL:** https://petsc.org/release/manualpages/DM/DMBoundaryType/

**Contents:**
- DMBoundaryType#
- Synopsis#
- Values#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#
- Examples#

Describes the choice for the filling of ghost cells on physical domain boundaries.

DM_BOUNDARY_NONE - no ghost nodes

DM_BOUNDARY_GHOSTED - ghost vertices/cells exist but aren’t filled; you can put values into them and then apply a stencil that uses those ghost locations

DM_BOUNDARY_MIRROR - the ghost value is the same as the value 1 grid point in; that is, the 0th grid point in the real mesh acts like a mirror to define the ghost point value; not yet implemented for 3d

DM_BOUNDARY_PERIODIC - ghost vertices/cells filled by the opposite edge of the domain

DM_BOUNDARY_TWIST - like periodic, only glued backwards like a Mobius strip

This is information for the boundary of the PHYSICAL domain. It has nothing to do with boundaries between processes. That width is always determined by the stencil width; see DMDASetStencilWidth().

If the physical grid points have values 0 1 2 3 with DM_BOUNDARY_MIRROR then the local vector with ghost points has the values 1 0 1 2 3 2.

See https://scicomp.stackexchange.com/questions/5355/writing-the-poisson-equation-finite-difference-matrix-with-neumann-boundary-cond

Should DM_BOUNDARY_MIRROR have the same meaning with DMDA_Q0, that is a staggered grid? In that case should the ghost point have the same value as the 0th grid point where the physical boundary serves as the mirror?

DM Basics, DM, DMDA, DMDASetBoundaryType(), DMDACreate1d(), DMDACreate2d(), DMDACreate3d(), DMDACreate()

include/petscdmtypes.h

src/ml/da/tutorials/ex3.c src/ksp/ksp/tutorials/ex71.c src/ml/da/tutorials/ex1.c src/ksp/ksp/tutorials/ex66.c src/snes/tutorials/ex78.c src/snes/tutorials/ex48.c src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex4.c src/ksp/ksp/tutorials/ex28.c src/ksp/ksp/tutorials/ex67.c

src/dm/impls/stag/tutorials/ex3.c src/dm/tutorials/ex19.c src/dm/tutorials/ex6.c

src/ksp/ksp/tutorials/ex66.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex14.c src/snes/tutorials/ex18.c src/snes/tutorials/ex15.c src/snes/tutorials/ex35.c src/snes/tutorials/ex40f90.F90 src/snes/tutorials/ex46.c src/snes/tutorials/ex33.c src/snes/tutorials/ex21.c src/snes/tutorials/ex4.c

src/dm/tutorials/ex1.c src/ksp/ksp/tutorials/ex59.c src/ts/tutorials/ex18.c src/dm/tutorials/ex12.c src/dm/impls/stag/tutorials/ex1.c src/snes/tutorials/ex30.c src/dm/tutorials/ex13f90.F90 src/dm/impls/plex/tutorials/ex13.c src/dm/dt/dualspace/impls/lagrange/tutorials/ex2.c src/dm/tutorials/ex13f90aux.F90

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  DM_BOUNDARY_NONE,
  DM_BOUNDARY_GHOSTED,
  DM_BOUNDARY_MIRROR,
  DM_BOUNDARY_PERIODIC,
  DM_BOUNDARY_TWIST
} DMBoundaryType;
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
DM_BOUNDARY_MIRROR
```

---

## DMCheckInterpolator#

**URL:** https://petsc.org/release/manualpages/DM/DMCheckInterpolator/

**Contents:**
- DMCheckInterpolator#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Check that an interpolation matrix accurately reproduces a set of sample fine-grid vectors

In - the interpolation matrix from a coarse DM to dmf

MC - a dense matrix whose columns are coarse-grid sample vectors

MF - a dense matrix whose columns are the corresponding fine-grid sample vectors

tol - tolerance on the maximum 2-norm of \(v_f - I v_c\) across all sample vectors

-dm_interpolator_adapt_error view - view the coarse, fine, and error vectors for each sample

For each column k, the residual \(v_f^k - I v_c^k\) is computed and its infinity and 2 norms are printed. An error is raised if the maximum 2-norm exceeds tol. Typically used with DMAdaptInterpolator() to validate the adapted operator.

KSP: Linear System Solvers, DM, Mat, DMAdaptInterpolator(), DMCreateInterpolation(), PCMG

src/ksp/ksp/utils/dm/dmproject.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h" 
#include "petscdmda.h" 
#include "petscdmplex.h" 
#include "petscdmswarm.h" 
#include "petscksp.h" 
PetscErrorCode DMCheckInterpolator(DM dmf, Mat In, Mat MC, Mat MF, PetscReal tol)
```

Example 2 (unknown):
```unknown
DMAdaptInterpolator()
```

Example 3 (unknown):
```unknown
DMAdaptInterpolator()
```

Example 4 (unknown):
```unknown
DMCreateInterpolation()
```

---

## DMClearAuxiliaryVec#

**URL:** https://petsc.org/release/manualpages/DM/DMClearAuxiliaryVec/

**Contents:**
- DMClearAuxiliaryVec#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Destroys the auxiliary vector information and creates a new empty one

DM Basics, DM, DMCopyAuxiliaryVec(), DMGetNumAuxiliaryVec(), DMGetAuxiliaryVec(), DMSetAuxiliaryVec()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMClearAuxiliaryVec(DM dm)
```

Example 2 (unknown):
```unknown
DMCopyAuxiliaryVec()
```

Example 3 (unknown):
```unknown
DMGetNumAuxiliaryVec()
```

Example 4 (unknown):
```unknown
DMGetAuxiliaryVec()
```

---

## DMClearDS#

**URL:** https://petsc.org/release/manualpages/DM/DMClearDS/

**Contents:**
- DMClearDS#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Remove all discrete systems from the DM

DM Basics, DM, DMGetNumDS(), DMGetDS(), DMSetField()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMClearDS(DM dm)
```

Example 2 (unknown):
```unknown
DMGetNumDS()
```

Example 3 (unknown):
```unknown
DMSetField()
```

---

## DMClearFields#

**URL:** https://petsc.org/release/manualpages/DM/DMClearFields/

**Contents:**
- DMClearFields#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#

Remove all fields from the DM

DM Basics, DM, DMGetNumFields(), DMSetNumFields(), DMSetField()

src/dm/interface/dm.c

src/dm/impls/plex/tutorials/ex15.c src/dm/impls/plex/tutorials/ex16.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMClearFields(DM dm)
```

Example 2 (unknown):
```unknown
DMGetNumFields()
```

Example 3 (unknown):
```unknown
DMSetNumFields()
```

Example 4 (unknown):
```unknown
DMSetField()
```

---

## DMClearGlobalVectors#

**URL:** https://petsc.org/release/manualpages/DM/DMClearGlobalVectors/

**Contents:**
- DMClearGlobalVectors#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Destroys all the global vectors that have been created for DMGetGlobalVector() calls in this DM

DM, DMCreateGlobalVector(), VecDuplicate(), VecDuplicateVecs(), DMDACreate1d(), DMDACreate2d(), DMDACreate3d(), DMGlobalToLocalBegin(), DMGlobalToLocalEnd(), DMLocalToGlobalBegin(), DMCreateLocalVector(), DMRestoreLocalVector(), VecStrideMax(), VecStrideMin(), VecStrideNorm(), DMClearLocalVectors()

src/dm/interface/dmget.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMGetGlobalVector()
```

Example 2 (unknown):
```unknown
#include "petscdm.h" 
PetscErrorCode DMClearGlobalVectors(DM dm)
```

Example 3 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 4 (unknown):
```unknown
VecDuplicate()
```

---

## DMClearLabelStratum#

**URL:** https://petsc.org/release/manualpages/DM/DMClearLabelStratum/

**Contents:**
- DMClearLabelStratum#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Remove all points from a stratum from a DMLabel

name - The label name

value - The label value for this point

DM Basics, DM, DMLabel, DMLabelClearStratum(), DMSetLabelValue(), DMGetStratumIS(), DMClearLabelValue()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMClearLabelStratum(DM dm, const char name[], PetscInt value)
```

Example 2 (unknown):
```unknown
DMLabelClearStratum()
```

Example 3 (unknown):
```unknown
DMSetLabelValue()
```

Example 4 (unknown):
```unknown
DMGetStratumIS()
```

---

## DMClearLabelValue#

**URL:** https://petsc.org/release/manualpages/DM/DMClearLabelValue/

**Contents:**
- DMClearLabelValue#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Remove a point from a DMLabel with given value

name - The label name

point - The mesh point

value - The label value for this point

DM Basics, DM, DMLabelClearValue(), DMSetLabelValue(), DMGetStratumIS()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMClearLabelValue(DM dm, const char name[], PetscInt point, PetscInt value)
```

Example 2 (unknown):
```unknown
DMLabelClearValue()
```

Example 3 (unknown):
```unknown
DMSetLabelValue()
```

Example 4 (unknown):
```unknown
DMGetStratumIS()
```

---

## DMClearLocalVectors#

**URL:** https://petsc.org/release/manualpages/DM/DMClearLocalVectors/

**Contents:**
- DMClearLocalVectors#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Destroys all the local vectors that have been created for DMGetLocalVector() calls in this DM

DM, DMCreateLocalVector(), VecDuplicate(), VecDuplicateVecs(), DMDACreate1d(), DMDACreate2d(), DMDACreate3d(), DMLocalToLocalBegin(), DMLocalToLocalEnd(), DMRestoreLocalVector(), VecStrideMax(), VecStrideMin(), VecStrideNorm(), DMClearGlobalVectors()

src/dm/interface/dmget.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMGetLocalVector()
```

Example 2 (unknown):
```unknown
#include "petscdm.h" 
PetscErrorCode DMClearLocalVectors(DM dm)
```

Example 3 (unknown):
```unknown
DMCreateLocalVector()
```

Example 4 (unknown):
```unknown
VecDuplicate()
```

---

## DMClearNamedGlobalVectors#

**URL:** https://petsc.org/release/manualpages/DM/DMClearNamedGlobalVectors/

**Contents:**
- DMClearNamedGlobalVectors#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Destroys all the named global vectors that have been created with DMGetNamedGlobalVector() in this DM

DM, DMGetNamedGlobalVector(), DMGetNamedLocalVector(), DMClearNamedLocalVectors()

src/dm/interface/dmget.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMGetNamedGlobalVector()
```

Example 2 (unknown):
```unknown
#include "petscdm.h" 
PetscErrorCode DMClearNamedGlobalVectors(DM dm)
```

Example 3 (unknown):
```unknown
DMGetNamedGlobalVector()
```

Example 4 (unknown):
```unknown
DMGetNamedLocalVector()
```

---

## DMClearNamedLocalVectors#

**URL:** https://petsc.org/release/manualpages/DM/DMClearNamedLocalVectors/

**Contents:**
- DMClearNamedLocalVectors#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Destroys all the named local vectors that have been created with DMGetNamedLocalVector() in this DM

DM, DMGetNamedGlobalVector(), DMGetNamedLocalVector(), DMClearNamedGlobalVectors()

src/dm/interface/dmget.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMGetNamedLocalVector()
```

Example 2 (unknown):
```unknown
#include "petscdm.h" 
PetscErrorCode DMClearNamedLocalVectors(DM dm)
```

Example 3 (unknown):
```unknown
DMGetNamedGlobalVector()
```

Example 4 (unknown):
```unknown
DMGetNamedLocalVector()
```

---

## DMClone#

**URL:** https://petsc.org/release/manualpages/DM/DMClone/

**Contents:**
- DMClone#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Creates a DM object with the same topology as the original.

dm - The original DM object

newdm - The new DM object

For some DM implementations this is a shallow clone, the result of which may share (reference counted) information with its parent. For example, DMClone() applied to a DMPLEX object will result in a new DMPLEX that shares the topology with the original DMPLEX. It does not share the PetscSection of the original DM.

The clone is considered set up if the original has been set up.

Use DMConvert() for a general way to create new DM from a given DM

DM Basics, DM, DMDestroy(), DMCreate(), DMSetType(), DMSetLocalSection(), DMSetGlobalSection(), DMPLEX, DMConvert()

src/dm/interface/dm.c

src/ts/tutorials/ex45.c src/snes/tutorials/ex11.c src/ts/tutorials/ex47.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/tao/tutorials/ex3.c src/snes/tutorials/ex27.c src/snes/tutorials/ex7.c src/snes/tutorials/ex77.c

DMClone_DA() in src/dm/impls/da/dacreate.c DMClone_Forest() in src/dm/impls/forest/forest.c DMClone_pforest() in src/dm/impls/forest/p4est/pforest.h DMClone_Moab() in src/dm/impls/moab/dmmoab.cxx DMClone_Network() in src/dm/impls/network/networkcreate.c DMClone_Plex() in src/dm/impls/plex/plexcreate.c DMClone_Stag() in src/dm/impls/stag/stag.c DMClone_Swarm() in src/dm/impls/swarm/swarm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMClone(DM dm, DM *newdm)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
DMConvert()
```

Example 4 (unknown):
```unknown
DMDestroy()
```

---

## DMCoarsenHierarchy#

**URL:** https://petsc.org/release/manualpages/DM/DMCoarsenHierarchy/

**Contents:**
- DMCoarsenHierarchy#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Coarsens a DM object, all levels at once

nlevels - the number of levels of coarsening

dmc - the coarsened DM hierarchy

DM Basics, DM, DMCoarsen(), DMRefineHierarchy(), DMDestroy(), DMView(), DMCreateGlobalVector(), DMCreateInterpolation()

src/dm/interface/dm.c

src/ksp/ksp/tutorials/ex42.c

DMCoarsenHierarchy_DA() in src/dm/impls/da/da.c DMCoarsenHierarchy_Moab() in src/dm/impls/moab/dmmbmg.cxx DMCoarsenHierarchy_Plex() in src/dm/impls/plex/plexcoarsen.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCoarsenHierarchy(DM dm, PetscInt nlevels, DM dmc[])
```

Example 2 (unknown):
```unknown
DMCoarsen()
```

Example 3 (unknown):
```unknown
DMRefineHierarchy()
```

Example 4 (unknown):
```unknown
DMDestroy()
```

---

## DMCoarsenHookAdd#

**URL:** https://petsc.org/release/manualpages/DM/DMCoarsenHookAdd/

**Contents:**
- DMCoarsenHookAdd#
- Synopsis#
- Input Parameters#
- Calling sequence of coarsenhook#
- Calling sequence of restricthook#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

adds a callback to be run when restricting a nonlinear problem to the coarse grid

Logically Collective; No Fortran Support

fine - DM on which to run a hook when restricting to a coarser level

coarsenhook - function to run when setting up a coarser level

restricthook - function to run to update data on coarser levels (called once per SNESSolve())

ctx - [optional] application context for provide data for the hooks (may be NULL)

coarse - coarse level DM to restrict problem to

ctx - optional application function context

mrestrict - matrix restricting a fine-level solution to the coarse grid, usually the transpose of the interpolation

rscale - scaling vector for restriction

inject - matrix restricting by injection

coarse - coarse level DM to update

ctx - optional application function context

This function is only needed if auxiliary data, attached to the DM with PetscObjectCompose(), needs to be set up or passed from the fine DM to the coarse DM.

If this function is called multiple times, the hooks will be run in the order they are added.

In order to compose with nonlinear preconditioning without duplicating storage, the hook should be implemented to extract the finest level information from its context (instead of from the SNES).

The hooks are automatically called by DMRestrict()

DM Basics, DM, DMCoarsenHookRemove(), DMRefineHookAdd(), SNESFASGetInterpolation(), SNESFASGetInjection(), PetscObjectCompose(), PetscContainerCreate()

src/dm/interface/dm.c

src/ts/tutorials/ex29.c src/snes/tutorials/ex48.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCoarsenHookAdd(DM fine, PetscErrorCode (*coarsenhook)(DM fine, DM coarse, PetscCtx ctx), PetscErrorCode (*restricthook)(DM fine, Mat mrestrict, Vec rscale, Mat inject, DM coarse, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESSolve()
```

Example 3 (unknown):
```unknown
coarsenhook
```

Example 4 (unknown):
```unknown
restricthook
```

---

## DMCoarsenHookRemove#

**URL:** https://petsc.org/release/manualpages/DM/DMCoarsenHookRemove/

**Contents:**
- DMCoarsenHookRemove#
- Synopsis#
- Input Parameters#
- Calling sequence of coarsenhook#
- Calling sequence of restricthook#
- Notes#
- See Also#
- Level#
- Location#

remove a callback set with DMCoarsenHookAdd()

Logically Collective; No Fortran Support

fine - DM on which to run a hook when restricting to a coarser level

coarsenhook - function to run when setting up a coarser level

restricthook - function to run to update data on coarser levels

ctx - [optional] application context for provide data for the hooks (may be NULL)

coarse - coarse level DM to restrict problem to

ctx - optional application function context

rstrict - matrix restricting a fine-level solution to the coarse grid, usually the transpose of the interpolation

rscale - scaling vector for restriction

inject - matrix restricting by injection

coarse - coarse level DM to update

ctx - optional application function context

This function does nothing if the coarsenhook is not in the list.

See DMCoarsenHookAdd() for the calling sequence of coarsenhook and restricthook

DM Basics, DM, DMCoarsenHookAdd(), DMRefineHookAdd(), SNESFASGetInterpolation(), SNESFASGetInjection(), PetscObjectCompose(), PetscContainerCreate()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCoarsenHookAdd()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCoarsenHookRemove(DM fine, PetscErrorCode (*coarsenhook)(DM fine, DM coarse, PetscCtx ctx), PetscErrorCode (*restricthook)(DM fine, Mat rstrict, Vec rscale, Mat inject, DM coarse, PetscCtx ctx), PetscCtx ctx)
```

Example 3 (unknown):
```unknown
coarsenhook
```

Example 4 (unknown):
```unknown
restricthook
```

---

## DMCoarsen#

**URL:** https://petsc.org/release/manualpages/DM/DMCoarsen/

**Contents:**
- DMCoarsen#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Coarsens a DM object using a standard, non-adaptive coarsening of the underlying mesh

comm - the communicator to contain the new DM object (or MPI_COMM_NULL)

dmc - the coarsened DM

DM Basics, DM, DMRefine(), DMDestroy(), DMView(), DMCreateGlobalVector(), DMCreateInterpolation(), DMCreateDomainDecomposition(), DMCoarsenHookAdd(), DMCoarsenHookRemove()

src/dm/interface/dm.c

src/ksp/ksp/tutorials/ex65.c src/dm/impls/stag/tutorials/ex4.c

DMCoarsen_Composite() in src/dm/impls/composite/pack.c DMCoarsen_DA() in src/dm/impls/da/da.c DMCoarsen_Forest() in src/dm/impls/forest/forest.c DMCoarsen_Moab() in src/dm/impls/moab/dmmbmg.cxx DMCoarsen_Plex() in src/dm/impls/plex/plexcoarsen.c DMCoarsen_Redundant() in src/dm/impls/redundant/dmredundant.c DMCoarsen_Stag() in src/dm/impls/stag/stag.c DMCoarsen_SNESVI() in src/snes/impls/vi/rs/virs.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCoarsen(DM dm, MPI_Comm comm, DM *dmc)
```

Example 2 (unknown):
```unknown
MPI_COMM_NULL
```

Example 3 (unknown):
```unknown
DMDestroy()
```

Example 4 (unknown):
```unknown
DMCreateGlobalVector()
```

---

## DMCompareLabels#

**URL:** https://petsc.org/release/manualpages/DM/DMCompareLabels/

**Contents:**
- DMCompareLabels#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Compare labels between two DM objects

Collective; No Fortran Support

dm0 - First DM object

dm1 - Second DM object

equal - (Optional) Flag whether labels of dm0 and dm1 are the same

message - (Optional) Message describing the difference, or NULL if there is no difference

The output flag equal will be the same on all processes.

If equal is passed as NULL and difference is found, an error is thrown on all processes.

Make sure to pass equal is NULL on all processes or none of them.

The output message is set independently on each rank.

message must be freed with PetscFree()

If message is passed as NULL and a difference is found, the difference description is printed to stderr in synchronized manner.

Make sure to pass message as NULL on all processes or no processes.

Labels are matched by name. If the number of labels and their names are equal, DMLabelCompare() is used to compare each pair of labels with the same name.

Cannot automatically generate the Fortran stub because message must be freed with PetscFree()

DM Basics, DM, DMLabel, DMAddLabel(), DMCopyLabelsMode, DMLabelCompare()

src/dm/interface/dm.c

src/dm/label/tutorials/ex1.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCompareLabels(DM dm0, DM dm1, PetscBool *equal, char *message[]) PeNS
```

Example 2 (unknown):
```unknown
PetscFree()
```

Example 3 (unknown):
```unknown
DMLabelCompare()
```

Example 4 (unknown):
```unknown
PetscFree()
```

---

## DMComputeError#

**URL:** https://petsc.org/release/manualpages/DM/DMComputeError/

**Contents:**
- DMComputeError#
- Synopsis#
- Input Parameters#
- Input/Output Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Computes the error assuming the user has provided the exact solution functions

sol - The solution vector

errors - An array of length Nf, the number of fields, or NULL for no output; on output contains the error in each field

errorVec - A vector to hold the cellwise error (may be NULL)

The exact solutions come from the PetscDS object, and the time comes from DMGetOutputSequenceNumber().

DM Basics, DM, DMMonitorSet(), DMGetRegionNumDS(), PetscDSGetExactSolution(), DMGetOutputSequenceNumber()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMComputeError(DM dm, Vec sol, PetscReal errors[], Vec *errorVec)
```

Example 2 (unknown):
```unknown
DMGetOutputSequenceNumber()
```

Example 3 (unknown):
```unknown
DMMonitorSet()
```

Example 4 (unknown):
```unknown
DMGetRegionNumDS()
```

---

## DMComputeExactSolution#

**URL:** https://petsc.org/release/manualpages/DM/DMComputeExactSolution/

**Contents:**
- DMComputeExactSolution#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Compute the exact solution for a given DM, using the PetscDS information.

u - The vector will be filled with exact solution values, or NULL

u_t - The vector will be filled with the time derivative of exact solution values, or NULL

The user must call PetscDSSetExactSolution() before using this routine

DM Basics, DM, PetscDSSetExactSolution()

src/dm/interface/dm.c

src/ts/tutorials/ex45.c src/ts/tutorials/ex76.c src/snes/tutorials/ex36.c src/ts/tutorials/ex77.c src/ts/tutorials/ex53.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMComputeExactSolution(DM dm, PetscReal time, Vec u, Vec u_t)
```

Example 2 (unknown):
```unknown
PetscDSSetExactSolution()
```

Example 3 (unknown):
```unknown
PetscDSSetExactSolution()
```

---

## DMComputeL2Diff#

**URL:** https://petsc.org/release/manualpages/DM/DMComputeL2Diff/

**Contents:**
- DMComputeL2Diff#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

This function computes the L_2 difference between a function u and an FEM interpolant solution u_h.

funcs - The functions to evaluate for each field component

ctxs - Optional array of contexts to pass to each function, or NULL.

X - The coefficient vector u_h, a global vector

diff - The diff ||u - u_h||_2

This API is specific to only particular usage of DM

The notes need to provide some information about what has to be provided to the DM to be able to perform the computation.

DM Basics, DM, DMProjectFunction(), DMComputeL2FieldDiff(), DMComputeL2GradientDiff()

src/dm/interface/dm.c

src/snes/tutorials/ex75.c src/tao/tutorials/ex2.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/tao/tutorials/ex1.c src/ts/tutorials/ex47.c

DMComputeL2Diff_pforest(DM dm, PetscReal time, PetscErrorCode (**funcs)() in src/dm/impls/forest/p4est/pforest.h DMComputeL2Diff_Plex(DM dm, PetscReal time, PetscErrorCode (**funcs)() in src/dm/impls/plex/plexfem.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMComputeL2Diff(DM dm, PetscReal time, PetscErrorCode (**funcs)(PetscInt, PetscReal, const PetscReal[], PetscInt, PetscScalar *, void *), void **ctxs, Vec X, PetscReal *diff)
```

Example 2 (unknown):
```unknown
DMProjectFunction()
```

Example 3 (unknown):
```unknown
DMComputeL2FieldDiff()
```

Example 4 (unknown):
```unknown
DMComputeL2GradientDiff()
```

---

## DMComputeL2FieldDiff#

**URL:** https://petsc.org/release/manualpages/DM/DMComputeL2FieldDiff/

**Contents:**
- DMComputeL2FieldDiff#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

This function computes the L_2 difference between a function u and an FEM interpolant solution u_h, separated into field components.

funcs - The functions to evaluate for each field component

ctxs - Optional array of contexts to pass to each function, or NULL.

X - The coefficient vector u_h, a global vector

diff - The array of differences, ||u^f - u^f_h||_2

This API is specific to only particular usage of DM

The notes need to provide some information about what has to be provided to the DM to be able to perform the computation.

DM Basics, DM, DMProjectFunction(), DMComputeL2GradientDiff()

src/dm/interface/dm.c

src/ts/tutorials/ex77.c src/ts/tutorials/ex46.c src/ts/tutorials/ex53.c src/ts/tutorials/ex76.c

DMComputeL2FieldDiff_pforest(DM dm, PetscReal time, PetscErrorCode (**funcs)() in src/dm/impls/forest/p4est/pforest.h DMComputeL2FieldDiff_Plex(DM dm, PetscReal time, PetscErrorCode (**funcs)() in src/dm/impls/plex/plexfem.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMComputeL2FieldDiff(DM dm, PetscReal time, PetscErrorCode (**funcs)(PetscInt, PetscReal, const PetscReal[], PetscInt, PetscScalar *, void *), void **ctxs, Vec X, PetscReal diff[])
```

Example 2 (unknown):
```unknown
DMProjectFunction()
```

Example 3 (unknown):
```unknown
DMComputeL2GradientDiff()
```

---

## DMComputeL2GradientDiff#

**URL:** https://petsc.org/release/manualpages/DM/DMComputeL2GradientDiff/

**Contents:**
- DMComputeL2GradientDiff#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Developer Notes#
- See Also#
- Level#
- Location#
- Implementations#

This function computes the L_2 difference between the gradient of a function u and an FEM interpolant solution grad u_h.

funcs - The gradient functions to evaluate for each field component

ctxs - Optional array of contexts to pass to each function, or NULL.

X - The coefficient vector u_h, a global vector

n - The vector to project along

diff - The diff ||(grad u - grad u_h) . n||_2

This API is specific to only particular usage of DM

The notes need to provide some information about what has to be provided to the DM to be able to perform the computation.

DM Basics, DM, DMProjectFunction(), DMComputeL2Diff(), DMComputeL2FieldDiff()

src/dm/interface/dm.c

DMComputeL2GradientDiff_Plex(DM dm, PetscReal time, PetscErrorCode (**funcs)() in src/dm/impls/plex/plexfem.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMComputeL2GradientDiff(DM dm, PetscReal time, PetscErrorCode (**funcs)(PetscInt, PetscReal, const PetscReal[], const PetscReal[], PetscInt, PetscScalar *, void *), void **ctxs, Vec X, const PetscReal n[], PetscReal *diff)
```

Example 2 (unknown):
```unknown
DMProjectFunction()
```

Example 3 (unknown):
```unknown
DMComputeL2Diff()
```

Example 4 (unknown):
```unknown
DMComputeL2FieldDiff()
```

---

## DMComputeVariableBounds#

**URL:** https://petsc.org/release/manualpages/DM/DMComputeVariableBounds/

**Contents:**
- DMComputeVariableBounds#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

compute variable bounds used by SNESVI.

This is generally not called by users. It calls the function provided by the user with DMSetVariableBounds()

DM Basics, DM, DMHasVariableBounds(), DMView(), DMCreateGlobalVector(), DMCreateInterpolation(), DMCreateColoring(), DMCreateMatrix(), DMCreateMassMatrix(), DMGetApplicationContext()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMComputeVariableBounds(DM dm, Vec xl, Vec xu)
```

Example 2 (unknown):
```unknown
DMHasVariableBounds()
```

Example 3 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 4 (unknown):
```unknown
DMCreateInterpolation()
```

---

## DMConvert#

**URL:** https://petsc.org/release/manualpages/DM/DMConvert/

**Contents:**
- DMConvert#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Converts a DM to another DM, either of the same or different type.

newtype - new DM type (use “same” for the same type)

M - pointer to new DM

Cannot be used to convert a sequential DM to a parallel or a parallel to sequential, the MPI communicator of the generated DM is always the same as the communicator of the input DM.

DM Basics, DM, DMSetType(), DMCreate(), DMClone()

src/dm/interface/dm.c

src/ts/tutorials/ex45.c src/ts/tutorials/ex11.c src/snes/tutorials/ex11.c src/ts/tutorials/ex30.c src/snes/tutorials/ex12.c src/dm/impls/forest/tutorials/ex1.c src/ts/tutorials/ex48.c src/ts/utils/dmplexlandau/tutorials/ex2.c src/snes/tutorials/ex8.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMConvert(DM dm, DMType newtype, DM *M)
```

Example 2 (unknown):
```unknown
DMSetType()
```

---

## DMCopyAuxiliaryVec#

**URL:** https://petsc.org/release/manualpages/DM/DMCopyAuxiliaryVec/

**Contents:**
- DMCopyAuxiliaryVec#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Copy the auxiliary vector data on a DM to a new DM

dmNew - The new DM, now with the same auxiliary data

This is a shallow copy of the auxiliary vectors

DM Basics, DM, DMClearAuxiliaryVec(), DMGetNumAuxiliaryVec(), DMGetAuxiliaryVec(), DMSetAuxiliaryVec()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCopyAuxiliaryVec(DM dm, DM dmNew)
```

Example 2 (unknown):
```unknown
DMClearAuxiliaryVec()
```

Example 3 (unknown):
```unknown
DMGetNumAuxiliaryVec()
```

Example 4 (unknown):
```unknown
DMGetAuxiliaryVec()
```

---

## DMCopyDisc#

**URL:** https://petsc.org/release/manualpages/DM/DMCopyDisc/

**Contents:**
- DMCopyDisc#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Copy the fields and discrete systems for the DM into another DM

Really ugly name, nothing in PETSc is called a Disc plus it is an ugly abbreviation

DM Basics, DM, DMCopyFields(), DMCopyDS()

src/dm/interface/dm.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex26.c src/snes/tutorials/ex17.c src/snes/tutorials/ex8.c src/snes/tutorials/ex23.c src/snes/tutorials/ex64.c src/snes/tutorials/ex62.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCopyDisc(DM dm, DM newdm)
```

Example 2 (unknown):
```unknown
DMCopyFields()
```

---

## DMCopyDS#

**URL:** https://petsc.org/release/manualpages/DM/DMCopyDS/

**Contents:**
- DMCopyDS#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Copy the discrete systems for the DM into another DM

minDegree - Minimum degree for a discretization, or PETSC_DETERMINE for no limit

maxDegree - Maximum degree for a discretization, or PETSC_DETERMINE for no limit

DM Basics, DM, DMCopyFields(), DMAddField(), DMGetDS(), DMGetCellDS(), DMGetRegionDS(), DMSetRegionDS()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCopyDS(DM dm, PetscInt minDegree, PetscInt maxDegree, DM newdm)
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
DMCopyFields()
```

---

## DMCopyFields#

**URL:** https://petsc.org/release/manualpages/DM/DMCopyFields/

**Contents:**
- DMCopyFields#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Copy the discretizations for the DM into another DM

minDegree - Minimum degree for a discretization, or PETSC_DETERMINE for no limit

maxDegree - Maximum degree for a discretization, or PETSC_DETERMINE for no limit

DM Basics, DM, DMGetField(), DMSetField(), DMAddField(), DMCopyDS(), DMGetDS(), DMGetCellDS()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCopyFields(DM dm, PetscInt minDegree, PetscInt maxDegree, DM newdm)
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
DMGetField()
```

---

## DMCopyLabelsMode#

**URL:** https://petsc.org/release/manualpages/DM/DMCopyLabelsMode/

**Contents:**
- DMCopyLabelsMode#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#
- Examples#

Determines how DMCopyLabels() behaves when there is a DMLabel in the source and destination DMs with the same name

DM_COPY_LABELS_REPLACE - replace label in destination by label from source

DM_COPY_LABELS_KEEP - keep destination label

DM_COPY_LABELS_FAIL - generate an error

DM Basics, DMLabel, DM, DMCompareLabels(), DMRemoveLabel()

src/dm/label/tutorials/ex1.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCopyLabels()
```

Example 2 (unknown):
```unknown
typedef enum {
  DM_COPY_LABELS_REPLACE,
  DM_COPY_LABELS_KEEP,
  DM_COPY_LABELS_FAIL
} DMCopyLabelsMode;
```

Example 3 (unknown):
```unknown
DM_COPY_LABELS_REPLACE
```

Example 4 (unknown):
```unknown
DM_COPY_LABELS_KEEP
```

---

## DMCopyLabels#

**URL:** https://petsc.org/release/manualpages/DM/DMCopyLabels/

**Contents:**
- DMCopyLabels#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Copy labels from one DM mesh to another DM with a superset of the points

dmA - The DM object with initial labels

dmB - The DM object to which labels are copied

mode - Copy labels by pointers (PETSC_OWN_POINTER) or duplicate them (PETSC_COPY_VALUES)

all - Copy all labels including “depth”, “dim”, and “celltype” (PETSC_TRUE) which are otherwise ignored (PETSC_FALSE)

emode - How to behave when a DMLabel in the source and destination DMs with the same name is encountered (see DMCopyLabelsMode)

This is typically used when interpolating or otherwise adding to a mesh, or testing.

DM Basics, DM, DMLabel, DMAddLabel(), DMCopyLabelsMode

src/dm/interface/dm.c

src/dm/label/tutorials/ex1.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCopyLabels(DM dmA, DM dmB, PetscCopyMode mode, PetscBool all, DMCopyLabelsMode emode)
```

Example 2 (unknown):
```unknown
PETSC_OWN_POINTER
```

Example 3 (unknown):
```unknown
PETSC_COPY_VALUES
```

Example 4 (unknown):
```unknown
PETSC_FALSE
```

---

## DMCopyTransform#

**URL:** https://petsc.org/release/manualpages/DM/DMCopyTransform/

**Contents:**
- DMCopyTransform#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Copy the basis transform context and callbacks from dm to newdm

newdm - the destination DM

If the transform requires setup, DMConstructBasisTransform_Internal() is invoked on newdm.

DM Basics, DM, DMCopyDS(), DMCopyDisc()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCopyTransform(DM dm, DM newdm)
```

Example 2 (unknown):
```unknown
DMConstructBasisTransform_Internal()
```

Example 3 (unknown):
```unknown
DMCopyDisc()
```

---

## DMCreateColoring#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateColoring/

**Contents:**
- DMCreateColoring#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Gets coloring of a graph associated with the DM. Often the graph represents the operator matrix associated with the discretization of a PDE on the DM.

ctype - IS_COLORING_LOCAL or IS_COLORING_GLOBAL

coloring - the coloring

Coloring of matrices can also be computed directly from the sparse matrix nonzero structure via the MatColoring object or from the mesh from which the matrix comes from (what this function provides). In general using the mesh produces a more optimal coloring (fewer colors).

This produces a coloring with the distance of 2, see MatSetColoringDistance() which can be used for efficiently computing Jacobians with MatFDColoringCreate() For DMDA in three dimensions with periodic boundary conditions the number of grid points in each dimension must be divisible by 2*stencil_width + 1, otherwise an error will be generated.

DM Basics, DM, ISColoring, DMDestroy(), DMView(), DMCreateGlobalVector(), DMCreateInterpolation(), DMCreateMatrix(), DMCreateMassMatrix(), DMSetMatType(), MatColoring, MatFDColoringCreate()

src/dm/interface/dm.c

src/tao/unconstrained/tutorials/minsurf2.c src/snes/tutorials/ex14.c

DMCreateColoring_Composite() in src/dm/impls/composite/pack.c DMCreateColoring_DA() in src/dm/impls/da/fdda.c DMCreateColoring_Redundant() in src/dm/impls/redundant/dmredundant.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCreateColoring(DM dm, ISColoringType ctype, ISColoring *coloring)
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
MatColoring
```

---

## DMCreateDomainDecompositionScatters#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateDomainDecompositionScatters/

**Contents:**
- DMCreateDomainDecompositionScatters#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Returns scatters to the subdomain vectors from the global vector for subdomains created with DMCreateDomainDecomposition()

n - the number of subdomains

subdms - the local subdomains

iscat - scatter from global vector to nonoverlapping global vector entries on subdomain

oscat - scatter from global vector to overlapping global vector entries on subdomain

gscat - scatter from global vector to local vector on subdomain (fills in ghosts)

This is an alternative to the iis and ois arguments in DMCreateDomainDecomposition() that allow for the solution of general nonlinear problems with overlapping subdomain methods. While merely having index sets that enable subsets of the residual equations to be created is fine for linear problems, nonlinear problems require local assembly of solution and residual data.

Can the subdms input be anything or are they exactly the DM obtained from DMCreateDomainDecomposition()?

DM Basics, DM, DMCreateDomainDecomposition(), DMDestroy(), DMView(), DMCreateInterpolation(), DMCreateColoring(), DMCreateMatrix(), DMCreateMassMatrix(), DMCreateFieldIS()

src/dm/interface/dm.c

src/ts/tutorials/ex29.c src/dm/tutorials/ex14.c

DMCreateDomainDecompositionScatters_DA() in src/dm/impls/da/dadd.c DMCreateDomainDecompositionScatters_pforest() in src/dm/impls/forest/p4est/pforest.h DMCreateDomainDecompositionScatters_Plex() in src/dm/impls/plex/plexdd.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateDomainDecomposition()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCreateDomainDecompositionScatters(DM dm, PetscInt n, DM subdms[], VecScatter *iscat[], VecScatter *oscat[], VecScatter *gscat[])
```

Example 3 (unknown):
```unknown
DMCreateDomainDecomposition()
```

Example 4 (unknown):
```unknown
DMCreateDomainDecomposition()
```

---

## DMCreateDomainDecomposition#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateDomainDecomposition/

**Contents:**
- DMCreateDomainDecomposition#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#

Returns lists of IS objects defining a decomposition of a problem into subproblems corresponding to restrictions to pairs of nested subdomains.

n - The number of subproblems in the domain decomposition (or NULL if not requested), also the length of the four arrays below

namelist - The name for each subdomain (or NULL if not requested)

innerislist - The global indices for each inner subdomain (or NULL, if not requested)

outerislist - The global indices for each outer subdomain (or NULL, if not requested)

dmlist - The DMs for each subdomain subproblem (or NULL, if not requested; if NULL is returned, no DMs are defined)

Each IS contains the global indices of the dofs of the corresponding subdomains with in the dofs of the original DM. The inner subdomains conceptually define a nonoverlapping covering, while outer subdomains can overlap.

The optional list of DMs define a DM for each subproblem.

The user is responsible for freeing all requested arrays. In particular, every entry of namelist should be freed with PetscFree(), every entry of innerislist and outerislist should be destroyed with ISDestroy(), every entry of dmlist should be destroyed with DMDestroy(), and all of the arrays should be freed with PetscFree().

The dmlist is for the inner subdomains or the outer subdomains or all subdomains?

The names are inconsistent, the hooks use DMSubDomainHook which is nothing like DMCreateDomainDecomposition() while DMRefineHook is used for DMRefine().

DM Basics, DM, DMCreateFieldDecomposition(), DMDestroy(), DMCreateDomainDecompositionScatters(), DMView(), DMCreateInterpolation(), DMSubDomainHookAdd(), DMSubDomainHookRemove(), DMCreateColoring(), DMCreateMatrix(), DMCreateMassMatrix(), DMRefine(), DMCoarsen()

src/dm/interface/dm.c

src/dm/tutorials/ex14.c

DMCreateDomainDecomposition_DA() in src/dm/impls/da/dadd.c DMCreateDomainDecomposition_pforest() in src/dm/impls/forest/p4est/pforest.h DMCreateDomainDecomposition_Plex() in src/dm/impls/plex/plexdd.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCreateDomainDecomposition(DM dm, PetscInt *n, char **namelist[], IS *innerislist[], IS *outerislist[], DM *dmlist[])
```

Example 2 (unknown):
```unknown
PetscFree()
```

Example 3 (unknown):
```unknown
innerislist
```

Example 4 (unknown):
```unknown
outerislist
```

---

## DMCreateDS#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateDS/

**Contents:**
- DMCreateDS#
- Synopsis#
- Input Parameter#
- Options Database Key#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Create the discrete systems for the DM based upon the fields added to the DM

-dm_petscds_view - View all the PetscDS objects in this DM

The name of this function is wrong. Create functions always return the created object as one of the arguments.

DM Basics, DM, DMSetField, DMAddField(), DMGetDS(), DMGetCellDS(), DMGetRegionDS(), DMSetRegionDS()

src/dm/interface/dm.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex26.c src/snes/tutorials/ex17.c src/snes/tutorials/ex8.c src/snes/tutorials/ex23.c src/snes/tutorials/ex64.c src/snes/tutorials/ex62.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCreateDS(DM dm)
```

Example 2 (unknown):
```unknown
DMAddField()
```

Example 3 (unknown):
```unknown
DMGetCellDS()
```

Example 4 (unknown):
```unknown
DMGetRegionDS()
```

---

## DMCreateFEDefault#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateFEDefault/

**Contents:**
- DMCreateFEDefault#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Create a PetscFE based on the celltype for the mesh

Nc - The number of components for the field

prefix - The options prefix for the output PetscFE, or NULL

qorder - The quadrature order or PETSC_DETERMINE to use PetscSpace polynomial degree

This is a convenience method that just calls PetscFECreateByCell() underneath.

DM Basics, DM, PetscFECreateByCell(), DMAddField(), DMCreateDS(), DMGetCellDS(), DMGetRegionDS()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCreateFEDefault(DM dm, PetscInt Nc, const char prefix[], PetscInt qorder, PetscFE *fem)
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
PetscFECreateByCell()
```

---

## DMCreateFieldDecomposition#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateFieldDecomposition/

**Contents:**
- DMCreateFieldDecomposition#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- Fortran Notes#
- Developer Notes#
- See Also#
- Level#
- Location#

Returns a list of IS objects defining a decomposition of a problem into subproblems corresponding to different fields.

Not Collective; No Fortran Support

len - The number of fields (or NULL if not requested)

namelist - The name for each field (or NULL if not requested)

islist - The global indices for each field (or NULL if not requested)

dmlist - The DMs for each field subproblem (or NULL, if not requested; if NULL is returned, no DMs are defined)

Each IS contains the global indices of the dofs of the corresponding field, defined by DMAddField(). The optional list of DMs define the DM for each subproblem.

The same as DMCreateFieldIS() but also returns a DM for each field.

The user is responsible for freeing all requested arrays. In particular, every entry of namelist should be freed with PetscFree(), every entry of islist should be destroyed with ISDestroy(), every entry of dmlist should be destroyed with DMDestroy(), and all of the arrays should be freed with PetscFree().

namelist must be provided, islist may be PETSC_NULL_IS_POINTER and dmlist may be PETSC_NULL_DM_POINTER

Use DMDestroyFieldDecomposition() to free the returned objects

It is not clear why this function and DMCreateFieldIS() exist. Having two seems redundant and confusing.

Unlike DMRefine(), DMCoarsen(), and DMCreateDomainDecomposition() this provides no mechanism to provide hooks that are called after the decomposition is computed.

DM Basics, DM, DMAddField(), DMCreateFieldIS(), DMCreateSubDM(), DMCreateDomainDecomposition(), DMDestroy(), DMView(), DMCreateInterpolation(), DMCreateColoring(), DMCreateMatrix(), DMCreateMassMatrix(), DMRefine(), DMCoarsen()

src/dm/interface/dm.c

src/ksp/ksp/tutorials/ex43.c src/dm/tutorials/ex11f90.F90

DMCreateFieldDecomposition_Composite() in src/dm/impls/composite/pack.c DMCreateFieldDecomposition_DA() in src/dm/impls/da/dacreate.c DMCreateFieldDecomposition_Stag() in src/dm/impls/stag/stag.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCreateFieldDecomposition(DM dm, PetscInt *len, char ***namelist, IS *islist[], DM *dmlist[])
```

Example 2 (unknown):
```unknown
DMAddField()
```

Example 3 (unknown):
```unknown
DMCreateFieldIS()
```

Example 4 (unknown):
```unknown
PetscFree()
```

---

## DMCreateFieldIS#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateFieldIS/

**Contents:**
- DMCreateFieldIS#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#
- Implementations#

Creates a set of IS objects with the global indices of dofs for each field defined with DMAddField()

Not Collective; No Fortran Support

numFields - The number of fields (or NULL if not requested)

fieldNames - The name of each field (or NULL if not requested)

fields - The global indices for each field (or NULL if not requested)

The user is responsible for freeing all requested arrays. In particular, every entry of fieldNames should be freed with PetscFree(), every entry of fields should be destroyed with ISDestroy(), and both arrays should be freed with PetscFree().

It is not clear why both this function and DMCreateFieldDecomposition() exist. Having two seems redundant and confusing. This function should likely be removed.

DM Basics, DM, DMAddField(), DMGetField(), DMDestroy(), DMView(), DMCreateInterpolation(), DMCreateColoring(), DMCreateMatrix(), DMCreateFieldDecomposition()

src/dm/interface/dm.c

DMCreateFieldIS_Composite() in src/dm/impls/composite/pack.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMAddField()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCreateFieldIS(DM dm, PetscInt *numFields, char ***fieldNames, IS *fields[])
```

Example 3 (unknown):
```unknown
PetscFree()
```

Example 4 (unknown):
```unknown
ISDestroy()
```

---

## DMCreateGlobalVector#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateGlobalVector/

**Contents:**
- DMCreateGlobalVector#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Creates a global vector from a DM object. A global vector is a parallel vector that has no duplicate values shared between MPI ranks, that is it has no ghost locations.

vec - the global vector

PETSc Vec always have all zero entries when created with DMCreateGlobalVector() until routines such as VecSet() or VecSetValues() are used to change the values. There is no reason to call VecZeroEntries() after creation.

DM Basics, DM, Vec, DMCreateLocalVector(), DMGetGlobalVector(), DMDestroy(), DMView(), DMCreateInterpolation(), DMCreateColoring(), DMCreateMatrix(), DMGlobalToLocalBegin(), DMGlobalToLocalEnd()

src/dm/interface/dm.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex14.c src/snes/tutorials/ex35.c src/snes/tutorials/ex40f90.F90 src/snes/tutorials/ex12.c src/snes/tutorials/ex17.c src/snes/tutorials/ex8.c src/snes/tutorials/ex15.c src/snes/tutorials/ex23.c src/snes/tutorials/ex21.c

DMCreateGlobalVector_Composite() in src/dm/impls/composite/pack.c DMCreateGlobalVector_DA() in src/dm/impls/da/dadist.c DMCreateGlobalVector_pforest() in src/dm/impls/forest/p4est/pforest.h DMCreateGlobalVector_Moab() in src/dm/impls/moab/dmmbvec.cxx DMCreateGlobalVector_Network() in src/dm/impls/network/networkcreate.c DMCreateGlobalVector_Patch() in src/dm/impls/patch/patch.c DMCreateGlobalVector_Plex() in src/dm/impls/plex/plexcreate.c DMCreateGlobalVector_Redundant() in src/dm/impls/redundant/dmredundant.c DMCreateGlobalVector_Shell() in src/dm/impls/shell/dmshell.c DMCreateGlobalVector_Sliced() in src/dm/impls/sliced/sliced.c DMCreateGlobalVector_Stag() in src/dm/impls/stag/stag.c DMCreateGlobalVector_Swarm() in src/dm/impls/swarm/swarm.c DMCreateGlobalVector_SNESVI() in src/snes/impls/vi/rs/virs.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCreateGlobalVector(DM dm, Vec *vec)
```

Example 2 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 3 (unknown):
```unknown
VecSetValues()
```

Example 4 (unknown):
```unknown
VecZeroEntries()
```

---

## DMCreateGradientMatrix#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateGradientMatrix/

**Contents:**
- DMCreateGradientMatrix#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Gets the gradient matrix between two DM objects, M_(ic)j = \int \partial_c \phi_i \psi_j where the \phi are Galerkin basis functions for a Galerkin finite element model on the DM

dmc - the target DM object

dmf - the source DM object, can be NULL

mat - the gradient matrix

For DMPLEX the finite element model for the DM must have been already provided.

DM Basics, DM, DMCreateMassMatrix(), DMCreateMassMatrixLumped(), DMCreateMatrix(), DMRefine(), DMCoarsen(), DMCreateRestriction(), DMCreateInterpolation(), DMCreateInjection()

src/dm/interface/dm.c

DMCreateGradientMatrix_Plex() in src/dm/impls/plex/plex.c DMCreateGradientMatrix_Swarm() in src/dm/impls/swarm/swarm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCreateGradientMatrix(DM dmc, DM dmf, Mat *mat)
```

Example 2 (unknown):
```unknown
DMCreateMassMatrix()
```

Example 3 (unknown):
```unknown
DMCreateMassMatrixLumped()
```

Example 4 (unknown):
```unknown
DMCreateMatrix()
```

---

## DMCreateInjection#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateInjection/

**Contents:**
- DMCreateInjection#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Gets injection matrix between two DM objects.

daf - the second, finer DM object

This is an operator that applied to a vector obtained with DMCreateGlobalVector() on the fine grid maps the values to a vector on the vector on the coarse DM by simply selecting the values on the coarse grid points. This compares to the operator obtained by DMCreateRestriction() or the transpose of the operator obtained by DMCreateInterpolation() that uses a “local weighted average” of the values around the coarse grid point as the coarse grid value.

For DMDA objects this only works for “uniform refinement”, that is the refined mesh was obtained DMRefine() or the coarse mesh was obtained by DMCoarsen(). The coordinates set into the DMDA are completely ignored in computing the injection.

DM Basics, DM, DMDestroy(), DMView(), DMCreateGlobalVector(), DMCreateColoring(), DMCreateMatrix(), DMCreateMassMatrix(), DMCreateInterpolation(), DMCreateRestriction(), MatRestrict(), MatInterpolate()

src/dm/interface/dm.c

DMCreateInjection_DA() in src/dm/impls/da/dainterp.c DMCreateInjection_pforest() in src/dm/impls/forest/p4est/pforest.h DMCreateInjection_Moab() in src/dm/impls/moab/dmmbmg.cxx DMCreateInjection_Plex() in src/dm/impls/plex/plex.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCreateInjection(DM dac, DM daf, Mat *mat)
```

Example 2 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 3 (unknown):
```unknown
DMCreateRestriction()
```

Example 4 (unknown):
```unknown
DMCreateInterpolation()
```

---

## DMCreateInterpolationScale#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateInterpolationScale/

**Contents:**
- DMCreateInterpolationScale#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

Forms L = 1/(R*1) where 1 is the vector of all ones, and R is the transpose of the interpolation between the DM.

dac - DM that defines a coarse mesh

daf - DM that defines a fine mesh

mat - the restriction (or interpolation operator) from fine to coarse

scale - the scaled vector

xcoarse = diag(L)Rxfine preserves scale and is thus suitable for state (versus residual) restriction. In other words xcoarse is the coarse representation of xfine.

If the fine-scale DMDA has the -dm_bind_below option set to true, then DMCreateInterpolationScale() calls MatSetBindingPropagates() on the restriction/interpolation operator to set the bindingpropagates flag to true.

DM Basics, DM, MatRestrict(), MatInterpolate(), DMCreateInterpolation(), DMCreateRestriction(), DMCreateGlobalVector()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCreateInterpolationScale(DM dac, DM daf, Mat mat, Vec *scale)
```

Example 2 (unknown):
```unknown
DMCreateInterpolationScale()
```

Example 3 (unknown):
```unknown
MatSetBindingPropagates()
```

Example 4 (unknown):
```unknown
MatRestrict()
```

---

## DMCreateInterpolation#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateInterpolation/

**Contents:**
- DMCreateInterpolation#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Gets the interpolation matrix between two DM objects. The resulting matrix map degrees of freedom in the vector obtained by DMCreateGlobalVector() on the coarse DM to similar vectors on the fine grid DM.

dmf - the second, finer DM object

mat - the interpolation

vec - the scaling (optional, pass NULL if not needed), see DMCreateInterpolationScale()

For DMDA objects this only works for “uniform refinement”, that is the refined mesh was obtained DMRefine() or the coarse mesh was obtained by DMCoarsen(). The coordinates set into the DMDA are completely ignored in computing the interpolation.

For DMDA objects you can use this interpolation (more precisely the interpolation from the DMGetCoordinateDM()) to interpolate the mesh coordinate vectors EXCEPT in the periodic case where it does not make sense since the coordinate vectors are not periodic.

DM Basics, DM, DMDestroy(), DMView(), DMCreateGlobalVector(), DMCreateColoring(), DMCreateMatrix(), DMCreateMassMatrix(), DMRefine(), DMCoarsen(), DMCreateRestriction(), DMCreateInterpolationScale()

src/dm/interface/dm.c

src/ts/tutorials/ex45.c src/ts/tutorials/ex29.c src/snes/tutorials/ex11.c src/ksp/ksp/tutorials/ex73.c src/snes/tutorials/ex36.c src/ksp/ksp/tutorials/ex35.cxx src/ksp/ksp/tutorials/ex42.c src/snes/tutorials/ex48.c src/ksp/ksp/tutorials/ex36.cxx src/ksp/ksp/tutorials/ex65.c

DMCreateInterpolation_Composite() in src/dm/impls/composite/pack.c DMCreateInterpolation_DA() in src/dm/impls/da/dainterp.c DMCreateInterpolation_pforest() in src/dm/impls/forest/p4est/pforest.h DMCreateInterpolation_Moab() in src/dm/impls/moab/dmmbmg.cxx DMCreateInterpolation_Plex() in src/dm/impls/plex/plex.c DMCreateInterpolation_Redundant() in src/dm/impls/redundant/dmredundant.c DMCreateInterpolation_Stag() in src/dm/impls/stag/stag.c DMCreateInterpolation_SNESVI() in src/snes/impls/vi/rs/virs.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCreateInterpolation(DM dmc, DM dmf, Mat *mat, Vec *vec)
```

Example 3 (unknown):
```unknown
DMCreateInterpolationScale()
```

Example 4 (unknown):
```unknown
DMGetCoordinateDM()
```

---

## DMCreateLabelAtIndex#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateLabelAtIndex/

**Contents:**
- DMCreateLabelAtIndex#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Create a label of the given name at the given index. If it already exists in the DM, move it to this index.

l - The index for the label

name - The label name

DM Basics, DM, DMCreateLabel(), DMLabelCreate(), DMHasLabel(), DMGetLabelValue(), DMSetLabelValue(), DMGetStratumIS()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCreateLabelAtIndex(DM dm, PetscInt l, const char name[])
```

Example 2 (unknown):
```unknown
DMCreateLabel()
```

Example 3 (unknown):
```unknown
DMLabelCreate()
```

Example 4 (unknown):
```unknown
DMHasLabel()
```

---

## DMCreateLabel#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateLabel/

**Contents:**
- DMCreateLabel#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Create a label of the given name if it does not already exist in the DM

name - The label name

DM Basics, DM, DMLabelCreate(), DMHasLabel(), DMGetLabelValue(), DMSetLabelValue(), DMGetStratumIS()

src/dm/interface/dm.c

src/snes/tutorials/ex11.c src/snes/tutorials/ex69.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/ts/tutorials/ex48.c src/snes/tutorials/ex56.c src/snes/tutorials/ex8.c src/tao/tutorials/ex3.c src/snes/tutorials/ex23.c src/snes/tutorials/ex77.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCreateLabel(DM dm, const char name[])
```

Example 2 (unknown):
```unknown
DMLabelCreate()
```

Example 3 (unknown):
```unknown
DMHasLabel()
```

Example 4 (unknown):
```unknown
DMGetLabelValue()
```

---

## DMCreateLocalVector#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateLocalVector/

**Contents:**
- DMCreateLocalVector#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Creates a local vector from a DM object.

vec - the local vector

A local vector usually has ghost locations that contain values that are owned by different MPI ranks. A global vector has no ghost locations.

PETSc Vec always have all zero entries when created with DMCreateLocalVector() until routines such as VecSet() or VecSetValues() are used to change the values. There is no reason to call VecZeroEntries() after creation.

DM Basics, DM, Vec, DMCreateGlobalVector(), DMGetLocalVector(), DMDestroy(), DMView(), DMCreateInterpolation(), DMCreateColoring(), DMCreateMatrix(), DMGlobalToLocalBegin(), DMGlobalToLocalEnd()

src/dm/interface/dm.c

src/ksp/ksp/tutorials/ex65.c src/snes/tutorials/ex11.c src/snes/tutorials/ex12.c src/ksp/ksp/tutorials/ex14f.F90 src/ksp/ksp/tutorials/ex49.c src/ksp/ksp/tutorials/ex42.c src/snes/tutorials/ex48.c src/ksp/ksp/tutorials/ex43.c src/snes/tutorials/ex7.c src/snes/tutorials/ex77.c

DMCreateLocalVector_Composite() in src/dm/impls/composite/pack.c DMCreateLocalVector_DA() in src/dm/impls/da/dalocal.c DMCreateLocalVector_pforest() in src/dm/impls/forest/p4est/pforest.h DMCreateLocalVector_Moab() in src/dm/impls/moab/dmmbvec.cxx DMCreateLocalVector_Network() in src/dm/impls/network/networkcreate.c DMCreateLocalVector_Patch() in src/dm/impls/patch/patch.c DMCreateLocalVector_Plex() in src/dm/impls/plex/plexcreate.c DMCreateLocalVector_Redundant() in src/dm/impls/redundant/dmredundant.c DMCreateLocalVector_Shell() in src/dm/impls/shell/dmshell.c DMCreateLocalVector_Stag() in src/dm/impls/stag/stag.c DMCreateLocalVector_Swarm() in src/dm/impls/swarm/swarm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCreateLocalVector(DM dm, Vec *vec)
```

Example 2 (unknown):
```unknown
DMCreateLocalVector()
```

Example 3 (unknown):
```unknown
VecSetValues()
```

Example 4 (unknown):
```unknown
VecZeroEntries()
```

---

## DMCreateMassMatrixLumped#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateMassMatrixLumped/

**Contents:**
- DMCreateMassMatrixLumped#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Gets the lumped mass matrix for a given DM

llm - the local lumped mass matrix, which is a diagonal matrix, represented as a vector

lm - the global lumped mass matrix, which is a diagonal matrix, represented as a vector

See DMCreateMassMatrix() for how to create the non-lumped version of the mass matrix.

DM Basics, DM, DMCreateMassMatrix(), DMCreateMatrix(), DMRefine(), DMCoarsen(), DMCreateRestriction(), DMCreateInterpolation(), DMCreateInjection()

src/dm/interface/dm.c

src/ts/tutorials/ex30.c

DMCreateMassMatrixLumped_Plex() in src/dm/impls/plex/plex.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCreateMassMatrixLumped(DM dm, Vec *llm, Vec *lm)
```

Example 2 (unknown):
```unknown
DMCreateMassMatrix()
```

Example 3 (unknown):
```unknown
DMCreateMassMatrix()
```

Example 4 (unknown):
```unknown
DMCreateMatrix()
```

---

## DMCreateMassMatrix#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateMassMatrix/

**Contents:**
- DMCreateMassMatrix#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Gets the mass matrix between two DM objects, M_ij = \int \phi_i \psi_j where the \phi are Galerkin basis functions for a a Galerkin finite element model on the DM

dmc - the target DM object

dmf - the source DM object, can be NULL

mat - the mass matrix

For DMPLEX the finite element model for the DM must have been already provided.

if dmc is dmf or NULL, then x^t M x is an approximation to the L2 norm of the vector x which is obtained by DMCreateGlobalVector()

DM Basics, DM, DMCreateMassMatrixLumped(), DMCreateMatrix(), DMRefine(), DMCoarsen(), DMCreateRestriction(), DMCreateInterpolation(), DMCreateInjection()

src/dm/interface/dm.c

src/snes/tutorials/ex36.c src/dm/impls/swarm/tutorials/ex1f90.F90

DMCreateMassMatrix_Plex() in src/dm/impls/plex/plex.c DMCreateMassMatrix_Swarm() in src/dm/impls/swarm/swarm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCreateMassMatrix(DM dmc, DM dmf, Mat *mat)
```

Example 2 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 3 (unknown):
```unknown
DMCreateMassMatrixLumped()
```

Example 4 (unknown):
```unknown
DMCreateMatrix()
```

---

## DMCreateMatrix#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateMatrix/

**Contents:**
- DMCreateMatrix#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates a matrix of appropriate size and nonzero structure for a DM. The matrix is most commonly used to store the Jacobian of a discrete PDE operator.

-dm_preallocate_only (true|false) - Only preallocate the matrix for DMCreateMatrix() and DMCreateMassMatrix(), but do not fill its nonzero structure

This properly preallocates the number of nonzeros in the sparse matrix so you do not need to do it yourself.

By default it also sets the nonzero structure and puts in the zero entries. To prevent setting the nonzero pattern call DMSetMatrixPreallocateOnly()

For DMDA, when you call MatView() on this matrix it is displayed using the global natural ordering, NOT in the ordering used internally by PETSc.

For DMDA, in general it is easiest to use MatSetValuesStencil() or MatSetValuesLocal() to put values into the matrix because MatSetValues() requires the indices for the global numbering for the DMDA which is complic`ated to compute

DM Basics, DM, DMDestroy(), DMView(), DMCreateGlobalVector(), DMCreateInterpolation(), DMSetMatType(), DMCreateMassMatrix()

src/dm/interface/dm.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex5f90.F90 src/snes/tutorials/ex3k.kokkos.cxx src/snes/tutorials/ex14.c src/snes/tutorials/ex12.c src/snes/tutorials/ex35.c src/snes/tutorials/ex58.c src/snes/tutorials/ex78.c src/snes/tutorials/ex5f90t.F90 src/snes/tutorials/ex77.c

DMCreateMatrix_Composite() in src/dm/impls/composite/packm.c DMCreateMatrix_DA() in src/dm/impls/da/fdda.c DMCreateMatrix_pforest() in src/dm/impls/forest/p4est/pforest.h DMCreateMatrix_Moab() in src/dm/impls/moab/dmmbmat.cxx DMCreateMatrix_Network() in src/dm/impls/network/network.c DMCreateMatrix_Plex() in src/dm/impls/plex/plex.c DMCreateMatrix_Redundant() in src/dm/impls/redundant/dmredundant.c DMCreateMatrix_Shell() in src/dm/impls/shell/dmshell.c DMCreateMatrix_Sliced() in src/dm/impls/sliced/sliced.c DMCreateMatrix_Stag() in src/dm/impls/stag/stag.c DMCreateMatrix_Swarm() in src/dm/impls/swarm/swarm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCreateMatrix(DM dm, Mat *mat)
```

Example 2 (unknown):
```unknown
DMCreateMatrix()
```

Example 3 (unknown):
```unknown
DMCreateMassMatrix()
```

Example 4 (unknown):
```unknown
DMSetMatrixPreallocateOnly()
```

---

## DMCreateRestriction#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateRestriction/

**Contents:**
- DMCreateRestriction#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Gets restriction matrix between two DM objects. The resulting matrix map degrees of freedom in the vector obtained by DMCreateGlobalVector() on the fine DM to similar vectors on the coarse grid DM.

dmf - the second, finer DM object

mat - the restriction

This only works for DMSTAG. For many situations either the transpose of the operator obtained with DMCreateInterpolation() or that matrix multiplied by the vector obtained with DMCreateInterpolationScale() provides the desired object.

DM Basics, DM, DMRestrict(), DMInterpolate(), DMDestroy(), DMView(), DMCreateGlobalVector(), DMCreateColoring(), DMCreateMatrix(), DMCreateMassMatrix(), DMRefine(), DMCoarsen(), DMCreateInterpolation()

src/dm/interface/dm.c

src/dm/impls/stag/tutorials/ex4.c

DMCreateRestriction_Stag() in src/dm/impls/stag/stag.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCreateRestriction(DM dmc, DM dmf, Mat *mat)
```

Example 3 (unknown):
```unknown
DMCreateInterpolation()
```

Example 4 (unknown):
```unknown
DMCreateInterpolationScale()
```

---

## DMCreateSectionPermutation#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateSectionPermutation/

**Contents:**
- DMCreateSectionPermutation#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Create a permutation of the PetscSection chart and optionally a block structure.

perm - A permutation of the mesh points in the chart

blockStarts - A high bit is set for the point that begins every block, or NULL for default blocking

DM Basics, DM, PetscSection, DMGetLocalSection(), DMGetGlobalSection()

src/dm/interface/dm.c

DMCreateSectionPermutation_Plex() in src/dm/impls/plex/plexreorder.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCreateSectionPermutation(DM dm, IS *perm, PetscBT *blockStarts)
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (unknown):
```unknown
DMGetLocalSection()
```

---

## DMCreateSectionSF#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateSectionSF/

**Contents:**
- DMCreateSectionSF#
- Synopsis#
- Input Parameters#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

Create the PetscSF encoding the parallel dof overlap for the DM based upon the PetscSections describing the data layout.

localSection - PetscSection describing the local data layout

globalSection - PetscSection describing the global data layout

One usually uses DMGetSectionSF() to obtain the PetscSF

Since this routine has for arguments the two sections from the DM and puts the resulting PetscSF directly into the DM, perhaps this function should not take the local and global sections as input and should just obtain them from the DM? Plus PETSc creation functions return the thing they create, this returns nothing

DM Basics, DM, DMGetSectionSF(), DMSetSectionSF(), DMGetLocalSection(), DMGetGlobalSection()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCreateSectionSF(DM dm, PetscSection localSection, PetscSection globalSection)
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

## DMCreateSectionSubDM#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateSectionSubDM/

**Contents:**
- DMCreateSectionSubDM#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Returns an IS and subDM containing a PetscSection that encapsulates a subproblem defined by a subset of the fields in a PetscSection in the DM.

numFields - The number of fields to incorporate into subdm

fields - The field numbers of the selected fields

numComps - The number of components from each field to incorporate into subdm, or PETSC_DECIDE for all components

comps - The component numbers of the selected fields (omitted for PTESC_DECIDE fields)

is - The global indices for the subproblem or NULL

subdm - The DM for the subproblem, which must already have be cloned from dm or NULL

If is and subdm are both NULL this does nothing

DMCreateSubDM(), DMGetLocalSection(), DMPlexSetMigrationSF(), DMView()

src/dm/interface/dmi.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
#include "petscdm.h"     
PetscErrorCode DMCreateSectionSubDM(DM dm, PetscInt numFields, const PetscInt fields[], const PetscInt numComps[], const PetscInt comps[], IS *is, DM *subdm)
```

Example 4 (unknown):
```unknown
DMCreateSubDM()
```

---

## DMCreateSectionSuperDM#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateSectionSuperDM/

**Contents:**
- DMCreateSectionSuperDM#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Returns an arrays of IS and a DM containing a PetscSection that encapsulates a superproblem defined by the array of DM and their PetscSection

dms - The DM objects, the must all have the same topology; for example obtained with DMClone()

len - The number of DM in dms

is - The global indices for the subproblem, or NULL

superdm - The DM for the superproblem, which must already have be cloned and contain the same topology as the dms

DMCreateSuperDM(), DMGetLocalSection(), DMPlexSetMigrationSF(), DMView()

src/dm/interface/dmi.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
#include "petscdm.h"     
PetscErrorCode DMCreateSectionSuperDM(DM dms[], PetscInt len, IS *is[], DM *superdm)
```

Example 4 (unknown):
```unknown
DMCreateSuperDM()
```

---

## DMCreateSubDM#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateSubDM/

**Contents:**
- DMCreateSubDM#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Returns an IS and DM encapsulating a subproblem defined by the fields passed in. The fields are defined by DMCreateFieldIS().

numFields - The number of fields to select

fields - The field numbers of the selected fields

is - The global indices for all the degrees of freedom in the new sub DM, use NULL if not needed

subdm - The DM for the subproblem, use NULL if not needed

You need to call DMPlexSetMigrationSF() on the original DM if you want the Global-To-Natural map to be automatically constructed

DM Basics, DM, DMCreateFieldIS(), DMCreateFieldDecomposition(), DMAddField(), DMCreateSuperDM(), IS, VecISCopy(), DMPlexSetMigrationSF(), DMDestroy(), DMView(), DMCreateInterpolation(), DMCreateColoring(), DMCreateMatrix(), DMCreateMassMatrix()

src/dm/interface/dm.c

src/snes/tutorials/ex11.c src/ts/tutorials/ex30.c src/ts/tutorials/ex77.c src/snes/tutorials/ex56.c src/snes/tutorials/ex77.c

DMCreateSubDM_DA() in src/dm/impls/da/dacreate.c DMCreateSubDM_Forest() in src/dm/impls/forest/forest.c DMCreateSubDM_Patch() in src/dm/impls/patch/patch.c DMCreateSubDM_Plex() in src/dm/impls/plex/plex.c DMCreateSubDM_Shell() in src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateFieldIS()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCreateSubDM(DM dm, PetscInt numFields, const PetscInt fields[], IS *is, DM *subdm)
```

Example 3 (unknown):
```unknown
DMPlexSetMigrationSF()
```

Example 4 (unknown):
```unknown
DMCreateFieldIS()
```

---

## DMCreateSuperDM#

**URL:** https://petsc.org/release/manualpages/DM/DMCreateSuperDM/

**Contents:**
- DMCreateSuperDM#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Returns an arrays of IS and a single DM encapsulating a superproblem defined by multiple DMs passed in.

n - The number of DMs

is - The global indices for each of subproblem within the super DM, or NULL, its length is n

superdm - The DM for the superproblem

You need to call DMPlexSetMigrationSF() on the original DM if you want the Global-To-Natural map to be automatically constructed

DM Basics, DM, DMCreateSubDM(), DMPlexSetMigrationSF(), DMDestroy(), DMView(), DMCreateInterpolation(), DMCreateColoring(), DMCreateMatrix(), DMCreateMassMatrix(), DMCreateFieldIS(), DMCreateDomainDecomposition()

src/dm/interface/dm.c

src/snes/tutorials/ex13.c

DMCreateSuperDM_Plex() in src/dm/impls/plex/plex.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCreateSuperDM(DM dms[], PetscInt n, IS *is[], DM *superdm)
```

Example 2 (unknown):
```unknown
DMPlexSetMigrationSF()
```

Example 3 (unknown):
```unknown
DMCreateSubDM()
```

Example 4 (unknown):
```unknown
DMPlexSetMigrationSF()
```

---

## DMCreate#

**URL:** https://petsc.org/release/manualpages/DM/DMCreate/

**Contents:**
- DMCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Creates an empty DM object. DMs are the abstract objects in PETSc that mediate between meshes and discretizations and the algebraic solvers, time integrators, and optimization algorithms in PETSc.

comm - The communicator for the DM object

See DMType for a brief summary of available DM.

The type must then be set with DMSetType(). If you never call DMSetType() it will generate an error when you try to use the dm.

DM is an orphan initialism or orphan acronym, the letters have no meaning and never did.

DM Basics, DM, DMSetType(), DMType, DMDACreate(), DMDA, DMSLICED, DMCOMPOSITE, DMPLEX, DMMOAB, DMNETWORK

src/dm/interface/dm.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex26.c src/snes/tutorials/ex17.c src/snes/tutorials/ex8.c src/snes/tutorials/ex23.c src/snes/tutorials/ex7.c src/snes/tutorials/ex62.c

DMCreate_Composite() in src/dm/impls/composite/pack.c DMCreate_DA() in src/dm/impls/da/dacreate.c DMCreate_Forest() in src/dm/impls/forest/forest.c DMCreate_pforest() in src/dm/impls/forest/p4est/pforest.h DMCreate_Moab() in src/dm/impls/moab/dmmoab.cxx DMCreate_Network() in src/dm/impls/network/networkcreate.c DMCreate_Patch() in src/dm/impls/patch/patchcreate.c DMCreate_Plex() in src/dm/impls/plex/plexcreate.c DMCreate_Product() in src/dm/impls/product/product.c DMCreate_Redundant() in src/dm/impls/redundant/dmredundant.c DMCreate_Shell() in src/dm/impls/shell/dmshell.c DMCreate_Sliced() in src/dm/impls/sliced/sliced.c DMCreate_Stag() in src/dm/impls/stag/stag.c DMCreate_Swarm() in src/dm/impls/swarm/swarm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMCreate(MPI_Comm comm, DM *dm)
```

Example 2 (unknown):
```unknown
DMSetType()
```

Example 3 (unknown):
```unknown
DMSetType()
```

Example 4 (unknown):
```unknown
DMSetType()
```

---

## DMDestroy#

**URL:** https://petsc.org/release/manualpages/DM/DMDestroy/

**Contents:**
- DMDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

dm - the DM object to destroy

DM Basics, DM, DMCreate(), DMType, DMSetType(), DMView(), DMCreateGlobalVector(), DMCreateInterpolation(), DMCreateColoring(), DMCreateMatrix()

src/dm/interface/dm.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex14.c src/snes/tutorials/ex18.c src/snes/tutorials/ex35.c src/snes/tutorials/ex40f90.F90 src/snes/tutorials/ex12.c src/snes/tutorials/ex17.c src/snes/tutorials/ex33.c src/snes/tutorials/ex23.c src/snes/tutorials/ex21.c

DMDestroy_Composite() in src/dm/impls/composite/pack.c DMDestroy_DA() in src/dm/impls/da/dadestroy.c DMDestroy_Forest() in src/dm/impls/forest/forest.c DMDestroy_Moab() in src/dm/impls/moab/dmmoab.cxx DMDestroy_Network() in src/dm/impls/network/network.c DMDestroy_Patch() in src/dm/impls/patch/patch.c DMDestroy_Plex() in src/dm/impls/plex/plex.c DMDestroy_Product() in src/dm/impls/product/product.c DMDestroy_Redundant() in src/dm/impls/redundant/dmredundant.c DMDestroy_Shell() in src/dm/impls/shell/dmshell.c DMDestroy_Sliced() in src/dm/impls/sliced/sliced.c DMDestroy_Stag() in src/dm/impls/stag/stag.c DMDestroy_Swarm() in src/dm/impls/swarm/swarm.c DMDestroy_SNESVI() in src/snes/impls/vi/rs/virs.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMDestroy(DM *dm)
```

Example 2 (unknown):
```unknown
DMSetType()
```

Example 3 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 4 (unknown):
```unknown
DMCreateInterpolation()
```

---

## DMDirection#

**URL:** https://petsc.org/release/manualpages/DM/DMDirection/

**Contents:**
- DMDirection#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#
- Examples#
- Examples#
- Examples#
- Examples#

Indicates a coordinate direction

DM_X - the x coordinate direction

DM_Y - the y coordinate direction

DM_Z - the z coordinate direction

DM Basics, DM, DMDA, DMDAGetRay(), DMDAGetProcessorSubset(), DMPlexShearGeometry()

include/petscdmtypes.h

src/dm/tutorials/ex22.c

src/dm/tutorials/ex51.c src/snes/tutorials/ex17.c src/dm/tutorials/ex22.c src/snes/tutorials/ex13.c

src/dm/tutorials/ex51.c src/dm/tutorials/ex22.c

src/dm/tutorials/ex22.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  DM_X,
  DM_Y,
  DM_Z
} DMDirection;
```

Example 2 (unknown):
```unknown
DMDAGetRay()
```

Example 3 (unknown):
```unknown
DMDAGetProcessorSubset()
```

Example 4 (unknown):
```unknown
DMPlexShearGeometry()
```

---

## DMEnclosureType#

**URL:** https://petsc.org/release/manualpages/DM/DMEnclosureType/

**Contents:**
- DMEnclosureType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

The type of enclosure relation between one DM and another

DM_ENC_SUBMESH - the DM is the boundary of another DM

DM_ENC_SUPERMESH - the DM has the boundary of another DM (the reverse situation to DM_ENC_SUBMESH)

DM_ENC_EQUALITY - it is unknown what this means

DM_ENC_NONE - no relationship can be determined

DM_ENC_UNKNOWN - the relationship is unknown

DM Basics, DM, DMGetEnclosureRelation()

include/petscdmtypes.h

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  DM_ENC_EQUALITY,
  DM_ENC_SUPERMESH,
  DM_ENC_SUBMESH,
  DM_ENC_NONE,
  DM_ENC_UNKNOWN
} DMEnclosureType;
```

Example 2 (unknown):
```unknown
DM_ENC_SUBMESH
```

Example 3 (unknown):
```unknown
DM_ENC_SUPERMESH
```

Example 4 (unknown):
```unknown
DM_ENC_SUBMESH
```

---

## DMExtrude#

**URL:** https://petsc.org/release/manualpages/DM/DMExtrude/

**Contents:**
- DMExtrude#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Extrude a DM object from a surface

layers - the number of extruded cell layers

dme - the extruded DM, or NULL

If no extrusion was done, the return value is NULL

DM Basics, DM, DMRefine(), DMCoarsen(), DMDestroy(), DMView(), DMCreateGlobalVector()

src/dm/interface/dm.c

DMExtrude_Plex() in src/dm/impls/plex/plexextrude.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMExtrude(DM dm, PetscInt layers, DM *dme)
```

Example 2 (unknown):
```unknown
DMCoarsen()
```

Example 3 (unknown):
```unknown
DMDestroy()
```

Example 4 (unknown):
```unknown
DMCreateGlobalVector()
```

---

## DMFieldContinuity#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldContinuity/

**Contents:**
- DMFieldContinuity#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#
- Examples#

Indicates the smallest mesh entity across which a DMField is continuous; equivalently, the largest entity at which the field may be discontinuous

DMFIELD_VERTEX - continuous across vertices (i.e., everywhere on the mesh; standard \(H^1\) finite elements)

DMFIELD_EDGE - continuous across edges, but may jump at vertices

DMFIELD_FACET - continuous across facets (faces in 3D, edges in 2D); may jump at lower-dimensional points

DMFIELD_CELL - field is defined per cell, with no continuity between adjacent cells (cell-centered finite volume)

DMField, DMFieldCreateShell(), DMFieldEvaluate(), DMFieldEvaluateFE(), DMFieldEvaluateFV()

include/petscdmfield.h

src/dm/field/tutorials/ex1.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  DMFIELD_VERTEX,
  DMFIELD_EDGE,
  DMFIELD_FACET,
  DMFIELD_CELL
} DMFieldContinuity;
```

Example 2 (unknown):
```unknown
DMFIELD_VERTEX
```

Example 3 (unknown):
```unknown
DMFIELD_EDGE
```

Example 4 (unknown):
```unknown
DMFIELD_FACET
```

---

## DMFieldCreateDA#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldCreateDA/

**Contents:**
- DMFieldCreateDA#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Create a DMField of type DMFIELDDA that represents a multilinear field on a DMDA given by its values at the corners of the reference element.

dm - the DMDA on which the field lives

nc - the number of components of the field

cornerValues - array of length nc * (1 << dim) holding the field values at each corner of the reference element, ordered by lexicographic corner index

field - the newly created DMField

Internally the corner values are converted to coefficients of a tensor-product multilinear polynomial so that evaluation at arbitrary points is inexpensive.

DMField, DMFIELDDA, DMDA, DMFieldCreate(), DMFieldCreateDS(), DMFieldCreateShell()

src/dm/field/impls/da/dmfieldda.c

src/dm/field/tutorials/ex1.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmfield.h" 
#include "petscdm.h" 
PetscErrorCode DMFieldCreateDA(DM dm, PetscInt nc, const PetscScalar *cornerValues, DMField *field)
```

Example 2 (unknown):
```unknown
nc * (1 << dim)
```

Example 3 (unknown):
```unknown
DMFieldCreate()
```

Example 4 (unknown):
```unknown
DMFieldCreateDS()
```

---

## DMFieldCreateDSWithDG#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldCreateDSWithDG/

**Contents:**
- DMFieldCreateDSWithDG#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Create a DMField of type DMFIELDDS for a PetscDS field, optionally paired with a matching discontinuous-Galerkin representation on a companion DM.

dm - the DM carrying the primary (continuous) discretization

dmDG - optional DM carrying a matching discontinuous-Galerkin discretization, or NULL

fieldNum - the field number within the DM’s PetscDS

vec - local vector holding the coefficients on dm

vecDG - local vector holding the coefficients on dmDG, or NULL if dmDG is NULL

field - the newly created DMField

When the DM has no discretization set for fieldNum, or the field is only marked with a PetscContainer, a default Lagrange PetscFE is constructed for the topmost stratum.

DMField, DMFIELDDS, DMFieldCreateDS(), DMFieldCreate(), PetscDS, PetscFE

src/dm/field/impls/ds/dmfieldds.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmfield.h" 
#include "petscdmfield.h" 
PetscErrorCode DMFieldCreateDSWithDG(DM dm, DM dmDG, PetscInt fieldNum, Vec vec, Vec vecDG, DMField *field)
```

Example 2 (unknown):
```unknown
PetscContainer
```

Example 3 (unknown):
```unknown
DMFieldCreateDS()
```

Example 4 (unknown):
```unknown
DMFieldCreate()
```

---

## DMFieldCreateDS#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldCreateDS/

**Contents:**
- DMFieldCreateDS#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Create a DMField of type DMFIELDDS for a PetscDS field on a DM.

dm - the DM carrying the discretization

fieldNum - the field number within the DM’s PetscDS

vec - local vector holding the coefficients

field - the newly created DMField

Equivalent to DMFieldCreateDSWithDG() with dmDG set to NULL.

DMField, DMFIELDDS, DMFieldCreateDSWithDG(), DMFieldCreate(), PetscDS

src/dm/field/impls/ds/dmfieldds.c

src/dm/field/tutorials/ex1.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmfield.h" 
#include "petscdmfield.h" 
PetscErrorCode DMFieldCreateDS(DM dm, PetscInt fieldNum, Vec vec, DMField *field)
```

Example 2 (unknown):
```unknown
DMFieldCreateDSWithDG()
```

Example 3 (unknown):
```unknown
DMFieldCreateDSWithDG()
```

Example 4 (unknown):
```unknown
DMFieldCreate()
```

---

## DMFieldCreateFEGeom#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldCreateFEGeom/

**Contents:**
- DMFieldCreateFEGeom#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Compute and create the geometric factors of a coordinate field

field - the DMField object

pointIS - the index set of points over which we wish to integrate the field

quad - the quadrature points at which to evaluate the geometric factors

mode - Type of geometry data to store

geom - the geometric factors

For some modes, the normal vectors and adjacent cells are calculated

DMField, PetscQuadrature, IS, PetscFEGeom, DMFieldEvaluateFE(), DMFieldCreateDefaulteQuadrature(), DMFieldGetDegree()

src/dm/field/interface/dmfield.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmfield.h" 
#include "petscdmfield.h" 
PetscErrorCode DMFieldCreateFEGeom(DMField field, IS pointIS, PetscQuadrature quad, PetscFEGeomMode mode, PetscFEGeom **geom)
```

Example 2 (unknown):
```unknown
PetscQuadrature
```

Example 3 (unknown):
```unknown
PetscFEGeom
```

Example 4 (unknown):
```unknown
DMFieldEvaluateFE()
```

---

## DMFieldCreateShell#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldCreateShell/

**Contents:**
- DMFieldCreateShell#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Create a DMFIELDSHELL, a DMField whose evaluation is implemented entirely by user-supplied callbacks.

dm - the DM on which the field lives

numComponents - the number of components of the field

continuity - the continuity of the field (e.g. DMFIELD_VERTEX)

ctx - optional application context returned by DMFieldShellGetContext()

field - the newly created DMField of type DMFIELDSHELL

After creation the user must register the desired evaluation callbacks with DMFieldShellSetEvaluate(), DMFieldShellSetEvaluateFE(), DMFieldShellSetEvaluateFV(), and optionally DMFieldShellSetDestroy(), DMFieldShellSetGetDegree(), and DMFieldShellSetCreateDefaultQuadrature().

DMField, DMFIELDSHELL, DMFieldShellGetContext(), DMFieldShellSetEvaluate(), DMFieldShellSetEvaluateFE(), DMFieldShellSetEvaluateFV(), DMFieldShellSetDestroy()

src/dm/field/impls/shell/dmfieldshell.c

src/dm/field/tutorials/ex1.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMFIELDSHELL
```

Example 2 (unknown):
```unknown
#include "petscdmfield.h" 
PetscErrorCode DMFieldCreateShell(DM dm, PetscInt numComponents, DMFieldContinuity continuity, PetscCtx ctx, DMField *field)
```

Example 3 (unknown):
```unknown
DMFIELD_VERTEX
```

Example 4 (unknown):
```unknown
DMFieldShellGetContext()
```

---

## DMFieldDestroy#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldDestroy/

**Contents:**
- DMFieldDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

field - address of DMField

DMField, DMFieldCreate()

src/dm/field/interface/dmfield.c

src/dm/field/tutorials/ex1.c

DMFieldDestroy_DA() in src/dm/field/impls/da/dmfieldda.c DMFieldDestroy_DS() in src/dm/field/impls/ds/dmfieldds.c DMFieldDestroy_Shell() in src/dm/field/impls/shell/dmfieldshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmfield.h" 
#include "petscdmfield.h" 
PetscErrorCode DMFieldDestroy(DMField *field)
```

Example 2 (unknown):
```unknown
DMFieldCreate()
```

---

## DMFieldEvaluateFE#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldEvaluateFE/

**Contents:**
- DMFieldEvaluateFE#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Evaluate the field and its derivatives on a set of points mapped from quadrature points on a reference point. The derivatives are taken with respect to the reference coordinates.

field - The DMField object

cellIS - Index set for cells on which to evaluate the field

points - The quadature containing the points in the reference cell at which to evaluate the field.

datatype - The PetscDataType of the output arrays: either PETSC_REAL or PETSC_SCALAR. If the field is complex and datatype is PETSC_REAL, the real part of the field is returned.

B - pointer to data of size c * n * sizeof(datatype), where c is the number of components in the field. If B is not NULL, the values of the field are written in this array, varying first by component, then by point.

D - pointer to data of size d * c * n * sizeof(datatype). If D is not NULL, the values of the field’s spatial derivatives are written in this array, varying first by the partial derivative component, then by field component, then by point.

H - pointer to data of size d * d * c * n * sizeof(datatype). If H is not NULL, the values of the field’s second spatial derivatives are written in this array, varying first by the second partial derivative component, then by field component, then by point.

DMField, DM, DMFieldGetNumComponents(), DMFieldEvaluate(), DMFieldEvaluateFV()

src/dm/field/interface/dmfield.c

src/dm/field/tutorials/ex1.c

DMFieldEvaluateFE_DA() in src/dm/field/impls/da/dmfieldda.c DMFieldEvaluateFE_DS() in src/dm/field/impls/ds/dmfieldds.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmfield.h" 
#include "petscdmfield.h" 
PetscErrorCode DMFieldEvaluateFE(DMField field, IS cellIS, PetscQuadrature points, PetscDataType datatype, void *B, void *D, void *H)
```

Example 2 (unknown):
```unknown
PETSC_SCALAR
```

Example 3 (unknown):
```unknown
DMFieldGetNumComponents()
```

Example 4 (unknown):
```unknown
DMFieldEvaluate()
```

---

## DMFieldEvaluateFV#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldEvaluateFV/

**Contents:**
- DMFieldEvaluateFV#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Evaluate the mean of a field and its finite volume derivatives on a set of points.

field - The DMField object

cellIS - Index set for cells on which to evaluate the field

datatype - The PetscDataType of the output arrays: either PETSC_REAL or PETSC_SCALAR. If the field is complex and datatype is PETSC_REAL, the real part of the field is returned.

B - pointer to data of size c * n * sizeof(datatype), where c is the number of components in the field. If B is not NULL, the values of the field are written in this array, varying first by component, then by point.

D - pointer to data of size d * c * n * sizeof(datatype). If D is not NULL, the values of the field’s spatial derivatives are written in this array, varying first by the partial derivative component, then by field component, then by point.

H - pointer to data of size d * d * c * n * sizeof(datatype). If H is not NULL, the values of the field’s second spatial derivatives are written in this array, varying first by the second partial derivative component, then by field component, then by point.

DMField, IS, DMFieldGetNumComponents(), DMFieldEvaluate(), DMFieldEvaluateFE(), PetscDataType

src/dm/field/interface/dmfield.c

src/dm/field/tutorials/ex1.c

DMFieldEvaluateFV_DA() in src/dm/field/impls/da/dmfieldda.c DMFieldEvaluateFV_DS() in src/dm/field/impls/ds/dmfieldds.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmfield.h" 
#include "petscdmfield.h" 
PetscErrorCode DMFieldEvaluateFV(DMField field, IS cellIS, PetscDataType datatype, void *B, void *D, void *H)
```

Example 2 (unknown):
```unknown
PETSC_SCALAR
```

Example 3 (unknown):
```unknown
DMFieldGetNumComponents()
```

Example 4 (unknown):
```unknown
DMFieldEvaluate()
```

---

## DMFieldEvaluate#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldEvaluate/

**Contents:**
- DMFieldEvaluate#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Evaluate the field and its derivatives on a set of points

field - The DMField object

points - The points at which to evaluate the field. Should have size d x n, where d is the coordinate dimension of the manifold and n is the number of points

datatype - The PetscDataType of the output arrays: either PETSC_REAL or PETSC_SCALAR. If the field is complex and datatype is PETSC_REAL, the real part of the field is returned.

B - pointer to data of size c * n * sizeof(datatype), where c is the number of components in the field. If B is not NULL, the values of the field are written in this array, varying first by component, then by point.

D - pointer to data of size d * c * n * sizeof(datatype). If D is not NULL, the values of the field’s spatial derivatives are written in this array, varying first by the partial derivative component, then by field component, then by point.

H - pointer to data of size d * d * c * n * sizeof(datatype). If H is not NULL, the values of the field’s second spatial derivatives are written in this array, varying first by the second partial derivative component, then by field component, then by point.

DMField, DMFieldGetDM(), DMFieldGetNumComponents(), DMFieldEvaluateFE(), DMFieldEvaluateFV(), PetscDataType

src/dm/field/interface/dmfield.c

src/dm/field/tutorials/ex1.c

DMFieldEvaluate_DA() in src/dm/field/impls/da/dmfieldda.c DMFieldEvaluate_DS() in src/dm/field/impls/ds/dmfieldds.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmfield.h" 
#include "petscdmfield.h" 
PetscErrorCode DMFieldEvaluate(DMField field, Vec points, PetscDataType datatype, void *B, void *D, void *H)
```

Example 2 (unknown):
```unknown
PETSC_SCALAR
```

Example 3 (unknown):
```unknown
DMFieldGetDM()
```

Example 4 (unknown):
```unknown
DMFieldGetNumComponents()
```

---

## DMFieldFinalizePackage#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldFinalizePackage/

**Contents:**
- DMFieldFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

Finalize DMField package, it is called from PetscFinalize()

DMFieldInitializePackage()

src/dm/field/interface/dlregisdmfield.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
#include "petscdmfield.h" 
PetscErrorCode DMFieldFinalizePackage(void)
```

Example 3 (unknown):
```unknown
DMFieldInitializePackage()
```

---

## DMFieldGetDegree#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldGetDegree/

**Contents:**
- DMFieldGetDegree#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Get the polynomial degree of a field when pulled back onto the reference element

field - the DMField object

cellIS - the index set of points over which we want know the invariance

minDegree - the degree of the largest polynomial space contained in the field on each element

maxDegree - the largest degree of the smallest polynomial space containing the field on any element

DMField, IS, DMFieldEvaluateFE()

src/dm/field/interface/dmfield.c

DMFieldGetDegree_DA() in src/dm/field/impls/da/dmfieldda.c DMFieldGetDegree_DS() in src/dm/field/impls/ds/dmfieldds.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmfield.h" 
#include "petscdmfield.h" 
PetscErrorCode DMFieldGetDegree(DMField field, IS cellIS, PeOp PetscInt *minDegree, PeOp PetscInt *maxDegree)
```

Example 2 (unknown):
```unknown
DMFieldEvaluateFE()
```

---

## DMFieldGetDM#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldGetDM/

**Contents:**
- DMFieldGetDM#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Returns the DM for the manifold over which the field is defined.

field - The DMField object

DMField, DM, DMFieldEvaluate()

src/dm/field/interface/dmfield.c

src/dm/field/tutorials/ex1.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmfield.h" 
#include "petscdmfield.h" 
PetscErrorCode DMFieldGetDM(DMField field, DM *dm)
```

Example 2 (unknown):
```unknown
DMFieldEvaluate()
```

---

## DMFieldGetNumComponents#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldGetNumComponents/

**Contents:**
- DMFieldGetNumComponents#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Returns the number of components in the field

field - The DMField object

nc - The number of field components

DMField, DMFieldEvaluate()

src/dm/field/interface/dmfield.c

src/dm/field/tutorials/ex1.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmfield.h" 
#include "petscdmfield.h" 
PetscErrorCode DMFieldGetNumComponents(DMField field, PetscInt *nc)
```

Example 2 (unknown):
```unknown
DMFieldEvaluate()
```

---

## DMFieldGetType#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldGetType/

**Contents:**
- DMFieldGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the DMFieldType name (as a string) from the DMField.

field - The DMField context

type - The DMFieldType name

type should not be retained for later use as it will be an invalid pointer if the DMFieldType of field is changed.

DMField, DMFieldSetType(), DMFieldType, PetscObjectTypeCompare(), PetscObjectTypeCompareAny()

src/dm/field/interface/dmfield.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMFieldType
```

Example 2 (unknown):
```unknown
#include "petscdmfield.h" 
#include "petscdmfield.h" 
PetscErrorCode DMFieldGetType(DMField field, DMFieldType *type)
```

Example 3 (unknown):
```unknown
DMFieldType
```

Example 4 (unknown):
```unknown
DMFieldType
```

---

## DMFieldInitializePackage#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldInitializePackage/

**Contents:**
- DMFieldInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

Initialize DMField package

DMFieldFinalizePackage()

src/dm/field/interface/dlregisdmfield.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmfield.h" 
PetscErrorCode DMFieldInitializePackage(void)
```

Example 2 (unknown):
```unknown
DMFieldFinalizePackage()
```

---

## DMFieldRegisterAll#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldRegisterAll/

**Contents:**
- DMFieldRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all the DMField implementations

DMField, DMFieldRegisterDestroy()

src/dm/field/interface/dmfieldregi.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmfield.h"  
PetscErrorCode DMFieldRegisterAll(void)
```

Example 2 (unknown):
```unknown
DMFieldRegisterDestroy()
```

---

## DMFieldRegister#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldRegister/

**Contents:**
- DMFieldRegister#
- Synopsis#
- Input Parameters#
- Example Usage#
- Note#
- See Also#
- Level#
- Location#

Adds an implementation of the DMField object.

Not collective, No Fortran Support

sname - name of a new user-defined implementation

function - routine to create method context

Then, this implementation can be chosen with the procedural interface via

DMFieldRegister() may be called multiple times to add several user-defined implementations.

DMField, DMFieldRegisterAll(), DMFieldRegisterDestroy()

src/dm/field/interface/dmfieldregi.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmfield.h"  
PetscErrorCode DMFieldRegister(const char sname[], PetscErrorCode (*function)(DMField))
```

Example 2 (unknown):
```unknown
DMFieldRegister("my_impl",MyImplCreate);
```

Example 3 (unknown):
```unknown
DMFieldSetType(tagger, "my_impl")
```

Example 4 (unknown):
```unknown
DMFieldRegister()
```

---

## DMFieldSetType#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldSetType/

**Contents:**
- DMFieldSetType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

set the DMField implementation

field - the DMField context

type - a known method, see DMFieldType

DMField, DMFieldGetType(), DMFieldType

src/dm/field/interface/dmfield.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmfield.h" 
#include "petscdmfield.h" 
PetscErrorCode DMFieldSetType(DMField field, DMFieldType type)
```

Example 2 (unknown):
```unknown
DMFieldType
```

Example 3 (unknown):
```unknown
DMFieldGetType()
```

Example 4 (unknown):
```unknown
DMFieldType
```

---

## DMFieldShellEvaluateFEDefault#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldShellEvaluateFEDefault/

**Contents:**
- DMFieldShellEvaluateFEDefault#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Default finite-element evaluation for a DMFIELDSHELL that maps the quadrature points to real space using the coordinate DMField and then calls DMFieldEvaluate().

field - the DMField of type DMFIELDSHELL

pointIS - the IS of mesh points at which to evaluate

quad - the reference-element quadrature

type - PETSC_SCALAR or PETSC_REAL

B - values at quadrature points, or NULL

D - derivatives at quadrature points, or NULL

H - Hessians at quadrature points, or NULL

Intended to be registered as the FE evaluation callback via DMFieldShellSetEvaluateFE() when the shell only supplies a bulk DMFieldEvaluate() implementation.

DMField, DMFIELDSHELL, DMFieldShellSetEvaluateFE(), DMFieldShellEvaluateFVDefault(), DMFieldEvaluate()

src/dm/field/impls/shell/dmfieldshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMFIELDSHELL
```

Example 2 (unknown):
```unknown
DMFieldEvaluate()
```

Example 3 (unknown):
```unknown
#include "petscdmfield.h" 
PetscErrorCode DMFieldShellEvaluateFEDefault(DMField field, IS pointIS, PetscQuadrature quad, PetscDataType type, void *B, void *D, void *H)
```

Example 4 (unknown):
```unknown
DMFIELDSHELL
```

---

## DMFieldShellEvaluateFVDefault#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldShellEvaluateFVDefault/

**Contents:**
- DMFieldShellEvaluateFVDefault#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Default finite-volume evaluation for a DMFIELDSHELL that samples at cell centroids using the coordinate DMField’s default quadrature and calls DMFieldEvaluate().

field - the DMField of type DMFIELDSHELL

pointIS - the IS of mesh cells at which to evaluate

type - PETSC_SCALAR or PETSC_REAL

B - cell-averaged values, or NULL

D - cell-averaged derivatives, or NULL

H - cell-averaged Hessians, or NULL

Intended to be registered as the FV evaluation callback via DMFieldShellSetEvaluateFV() when the shell only supplies a bulk DMFieldEvaluate() implementation.

DMField, DMFIELDSHELL, DMFieldShellSetEvaluateFV(), DMFieldShellEvaluateFEDefault(), DMFieldEvaluate()

src/dm/field/impls/shell/dmfieldshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMFIELDSHELL
```

Example 2 (unknown):
```unknown
DMFieldEvaluate()
```

Example 3 (unknown):
```unknown
#include "petscdmfield.h" 
PetscErrorCode DMFieldShellEvaluateFVDefault(DMField field, IS pointIS, PetscDataType type, void *B, void *D, void *H)
```

Example 4 (unknown):
```unknown
DMFIELDSHELL
```

---

## DMFieldShellGetContext#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldShellGetContext/

**Contents:**
- DMFieldShellGetContext#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Retrieve the user-supplied context associated with a DMFIELDSHELL.

field - the DMField of type DMFIELDSHELL

ctx - the context pointer that was passed to DMFieldCreateShell()

DMField, DMFIELDSHELL, DMFieldCreateShell()

src/dm/field/impls/shell/dmfieldshell.c

src/dm/field/tutorials/ex1.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMFIELDSHELL
```

Example 2 (unknown):
```unknown
#include "petscdmfield.h" 
PetscErrorCode DMFieldShellGetContext(DMField field, PetscCtxRt ctx)
```

Example 3 (unknown):
```unknown
DMFIELDSHELL
```

Example 4 (unknown):
```unknown
DMFieldCreateShell()
```

---

## DMFieldShellSetDestroy#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldShellSetDestroy/

**Contents:**
- DMFieldShellSetDestroy#
- Synopsis#
- Input Parameters#
- Calling sequence of destroy#
- See Also#
- Level#
- Location#
- Examples#

Register a destroy callback that will be invoked when a DMFIELDSHELL is destroyed.

field - the DMField of type DMFIELDSHELL

destroy - the destroy routine, called before the shell’s own data is freed

field - the DMField of type DMFIELDSHELL being destroyed

DMField, DMFIELDSHELL, DMFieldCreateShell(), DMFieldDestroy()

src/dm/field/impls/shell/dmfieldshell.c

src/dm/field/tutorials/ex1.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMFIELDSHELL
```

Example 2 (unknown):
```unknown
#include "petscdmfield.h" 
PetscErrorCode DMFieldShellSetDestroy(DMField field, PetscErrorCode (*destroy)(DMField field))
```

Example 3 (unknown):
```unknown
DMFIELDSHELL
```

Example 4 (unknown):
```unknown
DMFIELDSHELL
```

---

## DMFieldShellSetEvaluateFE#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldShellSetEvaluateFE/

**Contents:**
- DMFieldShellSetEvaluateFE#
- Synopsis#
- Input Parameters#
- Calling sequence of evaluateFE#
- Note#
- See Also#
- Level#
- Location#

Register the routine that evaluates a DMFIELDSHELL at finite-element quadrature points over a set of mesh points.

field - the DMField of type DMFIELDSHELL

evaluateFE - the FE evaluation callback

field - the DMField of type DMFIELDSHELL

is - the IS of mesh cells on which to evaluate the field

quad - the reference-cell PetscQuadrature supplying the evaluation points

dtype - PETSC_SCALAR or PETSC_REAL

B - array of field values at each quadrature point, or NULL

D - array of field reference derivatives at each quadrature point, or NULL

H - array of field reference Hessians at each quadrature point, or NULL

If the shell only supplies a generic DMFieldEvaluate() via DMFieldShellSetEvaluate(), pass DMFieldShellEvaluateFEDefault() here.

DMField, DMFIELDSHELL, DMFieldCreateShell(), DMFieldEvaluateFE(), DMFieldShellEvaluateFEDefault(), DMFieldShellSetEvaluateFV()

src/dm/field/impls/shell/dmfieldshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMFIELDSHELL
```

Example 2 (unknown):
```unknown
#include "petscdmfield.h" 
PetscErrorCode DMFieldShellSetEvaluateFE(DMField field, PetscErrorCode (*evaluateFE)(DMField field, IS is, PetscQuadrature quad, PetscDataType dtype, void *B, void *D, void *H))
```

Example 3 (unknown):
```unknown
DMFIELDSHELL
```

Example 4 (unknown):
```unknown
DMFIELDSHELL
```

---

## DMFieldShellSetEvaluateFV#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldShellSetEvaluateFV/

**Contents:**
- DMFieldShellSetEvaluateFV#
- Synopsis#
- Input Parameters#
- Calling sequence of evaluateFV#
- Note#
- See Also#
- Level#
- Location#

Register the routine that evaluates a DMFIELDSHELL as cell averages over a set of mesh cells.

field - the DMField of type DMFIELDSHELL

evaluateFV - the FV evaluation callback

field - the DMField of type DMFIELDSHELL

is - the IS of mesh cells on which to evaluate the field

dtype - PETSC_SCALAR or PETSC_REAL

B - array of cell-averaged field values, or NULL

D - array of cell-averaged field derivatives, or NULL

H - array of cell-averaged field Hessians, or NULL

If the shell only supplies a generic DMFieldEvaluate() via DMFieldShellSetEvaluate(), pass DMFieldShellEvaluateFVDefault() here.

DMField, DMFIELDSHELL, DMFieldCreateShell(), DMFieldEvaluateFV(), DMFieldShellEvaluateFVDefault(), DMFieldShellSetEvaluateFE()

src/dm/field/impls/shell/dmfieldshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMFIELDSHELL
```

Example 2 (unknown):
```unknown
#include "petscdmfield.h" 
PetscErrorCode DMFieldShellSetEvaluateFV(DMField field, PetscErrorCode (*evaluateFV)(DMField field, IS is, PetscDataType dtype, void *B, void *D, void *H))
```

Example 3 (unknown):
```unknown
DMFIELDSHELL
```

Example 4 (unknown):
```unknown
DMFIELDSHELL
```

---

## DMFieldShellSetEvaluate#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldShellSetEvaluate/

**Contents:**
- DMFieldShellSetEvaluate#
- Synopsis#
- Input Parameters#
- Calling sequence of evaluate#
- See Also#
- Level#
- Location#
- Examples#

Register the routine that evaluates a DMFIELDSHELL at an arbitrary set of real-space points supplied as a Vec of coordinates.

field - the DMField of type DMFIELDSHELL

evaluate - the evaluation callback

field - the DMField of type DMFIELDSHELL

u - the points at which to evaluate the field, as a Vec of coordinates of size d x n

dtype - PETSC_SCALAR or PETSC_REAL

B - array of field values at each point, or NULL

D - array of field spatial derivatives at each point, or NULL

H - array of field spatial Hessians at each point, or NULL

DMField, DMFIELDSHELL, DMFieldCreateShell(), DMFieldEvaluate(), DMFieldShellSetEvaluateFE(), DMFieldShellSetEvaluateFV()

src/dm/field/impls/shell/dmfieldshell.c

src/dm/field/tutorials/ex1.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMFIELDSHELL
```

Example 2 (unknown):
```unknown
#include "petscdmfield.h" 
PetscErrorCode DMFieldShellSetEvaluate(DMField field, PetscErrorCode (*evaluate)(DMField field, Vec u, PetscDataType dtype, void *B, void *D, void *H))
```

Example 3 (unknown):
```unknown
DMFIELDSHELL
```

Example 4 (unknown):
```unknown
DMFIELDSHELL
```

---

## DMFieldShellSetGetDegree#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldShellSetGetDegree/

**Contents:**
- DMFieldShellSetGetDegree#
- Synopsis#
- Input Parameters#
- Calling sequence of getDegree#
- See Also#
- Level#
- Location#

Register the routine that reports the polynomial degree bounds of a DMFIELDSHELL over a set of mesh points.

field - the DMField of type DMFIELDSHELL

getDegree - callback that returns the minimum and maximum polynomial degrees of the field over the given point IS

field - the DMField of type DMFIELDSHELL

is - the IS of mesh points over which the degree bounds are requested

minDegree - the degree of the largest polynomial space contained in the field on each element

maxDegree - the largest degree of the smallest polynomial space containing the field on any element

DMField, DMFIELDSHELL, DMFieldCreateShell(), DMFieldGetDegree()

src/dm/field/impls/shell/dmfieldshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMFIELDSHELL
```

Example 2 (unknown):
```unknown
#include "petscdmfield.h" 
PetscErrorCode DMFieldShellSetGetDegree(DMField field, PetscErrorCode (*getDegree)(DMField field, IS is, PetscInt *minDegree, PetscInt *maxDegree))
```

Example 3 (unknown):
```unknown
DMFIELDSHELL
```

Example 4 (unknown):
```unknown
DMFIELDSHELL
```

---

## DMFieldType#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldType/

**Contents:**
- DMFieldType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

String with the name of a DMField implementation

DMFIELDDA - a field defined only by its values at the corners of a DMDA

DMFIELDDS - a field defined by a discretization over a mesh set with DMSetField()

DMFIELDSHELL - a field defined by arbitrary callbacks

DM Basics, DMField, DMFieldSetType(), DMFieldGetType(), DMFieldRegister()

include/petscdmfield.h

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef const char *DMFieldType;
#define DMFIELDDA    "da"
#define DMFIELDDS    "ds"
#define DMFIELDSHELL "shell"
```

Example 2 (unknown):
```unknown
DMSetField()
```

Example 3 (unknown):
```unknown
DMFIELDSHELL
```

Example 4 (unknown):
```unknown
DMFieldSetType()
```

---

## DMFieldView#

**URL:** https://petsc.org/release/manualpages/DM/DMFieldView/

**Contents:**
- DMFieldView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

viewer - viewer to display field, for example PETSC_VIEWER_STDOUT_WORLD

DMField, DMFieldCreate()

src/dm/field/interface/dmfield.c

DMFieldView_DA() in src/dm/field/impls/da/dmfieldda.c DMFieldView_DS() in src/dm/field/impls/ds/dmfieldds.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmfield.h" 
#include "petscdmfield.h" 
PetscErrorCode DMFieldView(DMField field, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PETSC_VIEWER_STDOUT_WORLD
```

Example 3 (unknown):
```unknown
DMFieldCreate()
```

---

## DMField#

**URL:** https://petsc.org/release/manualpages/DM/DMField/

**Contents:**
- DMField#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

PETSc object for defining a field on a mesh topology

DM Basics, DM, DMUniversalLabel, DMLabelCreate()

include/petscdmtypes.h

src/dm/field/tutorials/ex1.c

_p_DMField in include/petsc/private/dmfieldimpl.h DMField_DA in src/dm/field/impls/da/dmfieldda.c DMField_DS in src/dm/field/impls/ds/dmfieldds.c DMField_Shell in src/dm/field/impls/shell/dmfieldshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_DMField *DMField;
```

Example 2 (unknown):
```unknown
DMUniversalLabel
```

Example 3 (unknown):
```unknown
DMLabelCreate()
```

---

## DMFinalizePackage#

**URL:** https://petsc.org/release/manualpages/DM/DMFinalizePackage/

**Contents:**
- DMFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function finalizes everything in the DM package. It is called from PetscFinalize().

src/dm/interface/dlregisdmdm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
PetscErrorCode DMFinalizePackage(void)
```

Example 3 (unknown):
```unknown
PetscInitialize()
```

---

## DMFindRegionNum#

**URL:** https://petsc.org/release/manualpages/DM/DMFindRegionNum/

**Contents:**
- DMFindRegionNum#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Find the region number for a given PetscDS, or -1 if it is not found.

ds - The PetscDS defined on the given region

num - The region number, in [0, Nds), or -1 if not found

DM Basics, DM, DMGetRegionNumDS(), DMGetRegionDS(), DMSetRegionDS(), DMGetDS(), DMGetCellDS()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMFindRegionNum(DM dm, PetscDS ds, PetscInt *num)
```

Example 2 (unknown):
```unknown
DMGetRegionNumDS()
```

Example 3 (unknown):
```unknown
DMGetRegionDS()
```

Example 4 (unknown):
```unknown
DMSetRegionDS()
```

---

## DMGenerateRegisterAll#

**URL:** https://petsc.org/release/manualpages/DM/DMGenerateRegisterAll/

**Contents:**
- DMGenerateRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the mesh generation methods in the DM package.

DM, DMGenerateRegisterDestroy()

src/dm/interface/dmgenerate.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGenerateRegisterAll(void)
```

Example 2 (unknown):
```unknown
DMGenerateRegisterDestroy()
```

---

## DMGenerateRegisterDestroy#

**URL:** https://petsc.org/release/manualpages/DM/DMGenerateRegisterDestroy/

**Contents:**
- DMGenerateRegisterDestroy#
- Synopsis#
- See Also#
- Level#
- Location#

Frees the list of DM mesh generators that were registered by DMGenerateRegister() or DMGenerateRegisterAll().

DM, DMGenerateRegister(), DMGenerateRegisterAll()

src/dm/interface/dmgenerate.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMGenerateRegister()
```

Example 2 (unknown):
```unknown
DMGenerateRegisterAll()
```

Example 3 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGenerateRegisterDestroy(void)
```

Example 4 (unknown):
```unknown
DMGenerateRegister()
```

---

## DMGenerateRegister#

**URL:** https://petsc.org/release/manualpages/DM/DMGenerateRegister/

**Contents:**
- DMGenerateRegister#
- Synopsis#
- Input Parameters#
- Example Usage#
- Note#
- See Also#
- Level#
- Location#

Adds a grid generator to DM

Not Collective, No Fortran Support

sname - name of a new user-defined grid generator

fnc - generator function

rfnc - refinement function

alfnc - adapt by label function

dim - dimension of boundary of domain

Then, your generator can be chosen with the procedural interface via

or at runtime via the option

DMGenerateRegister() may be called multiple times to add several user-defined generators

DM, DMGenerateRegisterAll(), DMPlexGenerate(), DMGenerateRegisterDestroy()

src/dm/interface/dmgenerate.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGenerateRegister(const char sname[], PetscErrorCode (*fnc)(DM, PetscBool, DM *), PetscErrorCode (*rfnc)(DM, PetscReal *, DM *), PetscErrorCode (*alfnc)(DM, Vec, DMLabel, DMLabel, DM *), PetscInt dim)
```

Example 2 (unknown):
```unknown
DMGenerateRegister("my_generator", MyGeneratorCreate, MyGeneratorRefiner, MyGeneratorAdaptor, dim);
```

Example 3 (lua):
```lua
DMGenerate(dm, "my_generator",...)
```

Example 4 (unknown):
```unknown
-dm_generator my_generator
```

---

## DMGeneratorFunctionList#

**URL:** https://petsc.org/release/manualpages/DM/DMGeneratorFunctionList/

**Contents:**
- DMGeneratorFunctionList#
- Synopsis#
- See Also#
- Level#
- Location#

Opaque linked-list node used internally to register and dispatch mesh-generator backends (Triangle, Tetgen, p4est, etc.) for DMPlexGenerate()

DM, DMPlexGenerate(), DMGenerateRegister(), DMGenerateRegisterAll()

include/petscdmtypes.h

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMPlexGenerate()
```

Example 2 (julia):
```julia
typedef struct _n_DMGeneratorFunctionList *DMGeneratorFunctionList;
```

Example 3 (unknown):
```unknown
DMPlexGenerate()
```

Example 4 (unknown):
```unknown
DMGenerateRegister()
```

---

## DMGeomModelRegisterAll#

**URL:** https://petsc.org/release/manualpages/DM/DMGeomModelRegisterAll/

**Contents:**
- DMGeomModelRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the geometry model methods in the DM package.

DM, DMGeomModelRegisterDestroy()

src/dm/interface/dmgeommodel.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h" 
PetscErrorCode DMGeomModelRegisterAll(void)
```

Example 2 (unknown):
```unknown
DMGeomModelRegisterDestroy()
```

---

## DMGeomModelRegisterDestroy#

**URL:** https://petsc.org/release/manualpages/DM/DMGeomModelRegisterDestroy/

**Contents:**
- DMGeomModelRegisterDestroy#
- Synopsis#
- See Also#
- Level#
- Location#

Frees the list of DM geometry models that were registered by DMGeomModelRegister() or DMGeomModelRegisterAll().

DM, DMGeomModelRegister(), DMGeomModelRegisterAll()

src/dm/interface/dmgeommodel.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMGeomModelRegister()
```

Example 2 (unknown):
```unknown
DMGeomModelRegisterAll()
```

Example 3 (unknown):
```unknown
#include "petscdm.h" 
PetscErrorCode DMGeomModelRegisterDestroy(void)
```

Example 4 (unknown):
```unknown
DMGeomModelRegister()
```

---

## DMGeomModelRegister#

**URL:** https://petsc.org/release/manualpages/DM/DMGeomModelRegister/

**Contents:**
- DMGeomModelRegister#
- Synopsis#
- Input Parameters#
- Example Usage#
- Note#
- See Also#
- Level#
- Location#

Adds a geometry model to DM

Not Collective, No Fortran Support

sname - name of a new user-defined geometry model

fnc - geometry model function

Then, your generator can be chosen with the procedural interface via

or at runtime via the option

DMGeomModelRegister() may be called multiple times to add several user-defined generators

DM, DMGeomModelRegisterAll(), DMPlexGeomModel(), DMGeomModelRegisterDestroy()

src/dm/interface/dmgeommodel.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h" 
PetscErrorCode DMGeomModelRegister(const char sname[], PetscErrorCode (*fnc)(DM, PetscInt, PetscInt, const PetscScalar[], PetscScalar[]))
```

Example 2 (unknown):
```unknown
DMGeomModelRegister("my_geom_model", MySnapToGeomModel);
```

Example 3 (lua):
```lua
DMSetGeomModel(dm, "my_geom_model",...)
```

Example 4 (unknown):
```unknown
-dm_geom_model my_geom_model
```

---

## DMGetAdjacency#

**URL:** https://petsc.org/release/manualpages/DM/DMGetAdjacency/

**Contents:**
- DMGetAdjacency#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Returns the flags for determining variable influence

f - The field number, or PETSC_DEFAULT for the default adjacency

useCone - Flag for variable influence starting with the cone operation

useClosure - Flag for variable influence using transitive closure

Further explanation can be found in the User’s Manual Section on the Influence of Variables on One Another.

DM Basics, DM, DMSetAdjacency(), DMGetField(), DMSetField()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetAdjacency(DM dm, PetscInt f, PetscBool *useCone, PetscBool *useClosure)
```

Example 2 (unknown):
```unknown
PETSC_DEFAULT
```

Example 3 (sass):
```sass
FEM:   Two points p and q are adjacent if q \in closure(star(p)),   useCone = PETSC_FALSE, useClosure = PETSC_TRUE
     FVM:   Two points p and q are adjacent if q \in support(p+cone(p)), useCone = PETSC_TRUE,  useClosure = PETSC_FALSE
     FVM++: Two points p and q are adjacent if q \in star(closure(p)),   useCone = PETSC_TRUE,  useClosure = PETSC_TRUE
```

Example 4 (unknown):
```unknown
DMSetAdjacency()
```

---

## DMGetApplicationContext#

**URL:** https://petsc.org/release/manualpages/DM/DMGetApplicationContext/

**Contents:**
- DMGetApplicationContext#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- Fortran Notes#
- See Also#
- Level#
- Location#
- Examples#

Gets an application context from a DM object provided with DMSetApplicationContext()

ctx - a pointer to the application context

An application context is a way to pass problem specific information that is accessible whenever the DM is available

This only works when the context is a Fortran derived type (it cannot be a PetscObject) and you must write a Fortran interface definition for this function that tells the Fortran compiler the derived data type that is returned as the ctx argument. For example,

The prototype for ctx must be

DM Basics, DM, DMView(), DMCreateGlobalVector(), DMCreateInterpolation(), DMCreateColoring(), DMCreateMatrix(), DMCreateMassMatrix()

src/dm/interface/dm.c

src/snes/tutorials/ex55.c src/snes/tutorials/ex18.c src/snes/tutorials/ex5.c src/ksp/ksp/tutorials/ex73.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/snes/tutorials/ex30.c src/snes/tutorials/ex48.c src/snes/tutorials/ex27.c src/snes/tutorials/ex22.c src/ksp/ksp/tutorials/ex28.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMSetApplicationContext()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetApplicationContext(DM dm, PetscCtxRt ctx)
```

Example 3 (unknown):
```unknown
PetscObject
```

Example 4 (julia):
```julia
Interface DMGetApplicationContext
    Subroutine DMGetApplicationContext(dm,ctx,ierr)
  #include <petsc/finclude/petscdm.h>
      use petscdm
      DM dm
      type(tUsertype), pointer :: ctx
      PetscErrorCode ierr
    End Subroutine
  End Interface DMGetApplicationContext
```

---

## DMGetAuxiliaryLabels#

**URL:** https://petsc.org/release/manualpages/DM/DMGetAuxiliaryLabels/

**Contents:**
- DMGetAuxiliaryLabels#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Get the labels, values, and parts for all auxiliary vectors in this DM

labels - The DMLabels for each Vec

values - The label values for each Vec

parts - The equation parts for each Vec

The arrays passed in must be at least as large as DMGetNumAuxiliaryVec().

DM Basics, DM, DMClearAuxiliaryVec(), DMGetNumAuxiliaryVec(), DMGetAuxiliaryVec(), DMSetAuxiliaryVec(), DMCopyAuxiliaryVec()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetAuxiliaryLabels(DM dm, DMLabel labels[], PetscInt values[], PetscInt parts[])
```

Example 2 (unknown):
```unknown
DMGetNumAuxiliaryVec()
```

Example 3 (unknown):
```unknown
DMClearAuxiliaryVec()
```

Example 4 (unknown):
```unknown
DMGetNumAuxiliaryVec()
```

---

## DMGetAuxiliaryVec#

**URL:** https://petsc.org/release/manualpages/DM/DMGetAuxiliaryVec/

**Contents:**
- DMGetAuxiliaryVec#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Get the auxiliary vector for region specified by the given label and value, and equation part

value - The label value indicating the region

part - The equation part, or 0 if unused

aux - The Vec holding auxiliary field data

If no auxiliary vector is found for this (label, value), (NULL, 0, 0) is checked as well.

DM Basics, DM, DMClearAuxiliaryVec(), DMSetAuxiliaryVec(), DMGetNumAuxiliaryVec(), DMGetAuxiliaryLabels()

src/dm/interface/dm.c

src/ts/tutorials/ex30.c src/snes/tutorials/ex7.c src/snes/tutorials/ex12.c src/snes/tutorials/ex11.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetAuxiliaryVec(DM dm, DMLabel label, PetscInt value, PetscInt part, Vec *aux)
```

Example 2 (unknown):
```unknown
DMClearAuxiliaryVec()
```

Example 3 (unknown):
```unknown
DMSetAuxiliaryVec()
```

Example 4 (unknown):
```unknown
DMGetNumAuxiliaryVec()
```

---

## DMGetBasicAdjacency#

**URL:** https://petsc.org/release/manualpages/DM/DMGetBasicAdjacency/

**Contents:**
- DMGetBasicAdjacency#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Returns the flags for determining variable influence, using either the default or field 0 if it is defined

useCone - Flag for variable influence starting with the cone operation

useClosure - Flag for variable influence using transitive closure

DM Basics, DM, DMSetBasicAdjacency(), DMGetField(), DMSetField()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetBasicAdjacency(DM dm, PetscBool *useCone, PetscBool *useClosure)
```

Example 2 (sass):
```sass
FEM:   Two points p and q are adjacent if q \in closure(star(p)),   useCone = PETSC_FALSE, useClosure = PETSC_TRUE
     FVM:   Two points p and q are adjacent if q \in support(p+cone(p)), useCone = PETSC_TRUE,  useClosure = PETSC_FALSE
     FVM++: Two points p and q are adjacent if q \in star(closure(p)),   useCone = PETSC_TRUE,  useClosure = PETSC_TRUE
```

Example 3 (unknown):
```unknown
DMSetBasicAdjacency()
```

Example 4 (unknown):
```unknown
DMGetField()
```

---

## DMGetBlockingType#

**URL:** https://petsc.org/release/manualpages/DM/DMGetBlockingType/

**Contents:**
- DMGetBlockingType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

get the blocking granularity to be used for variable block size DMCreateMatrix() is called

btype - block by topological point or field node

DM Basics, DM, DMCreateMatrix(), MatSetVariableBlockSizes()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateMatrix()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetBlockingType(DM dm, DMBlockingType *btype)
```

Example 3 (unknown):
```unknown
DMCreateMatrix()
```

Example 4 (unknown):
```unknown
MatSetVariableBlockSizes()
```

---

## DMGetBlockSize#

**URL:** https://petsc.org/release/manualpages/DM/DMGetBlockSize/

**Contents:**
- DMGetBlockSize#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Gets the inherent block size associated with a DM

dm - the DM with block structure

bs - the block size, 1 implies no exploitable block structure

This might be the number of degrees of freedom at each grid point for a structured grid.

Complex DM that represent multiphysics or staggered grids or mixed-methods do not generally have a single inherent block size, but rather different locations in the vectors may have a different block size.

DM Basics, DM, ISCreateBlock(), VecSetBlockSize(), MatSetBlockSize(), DMGetLocalToGlobalMapping()

src/dm/interface/dm.c

src/ml/da/tutorials/ex4.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetBlockSize(DM dm, PetscInt *bs)
```

Example 2 (unknown):
```unknown
ISCreateBlock()
```

Example 3 (unknown):
```unknown
VecSetBlockSize()
```

Example 4 (unknown):
```unknown
MatSetBlockSize()
```

---

## DMGetBoundingBox#

**URL:** https://petsc.org/release/manualpages/DM/DMGetBoundingBox/

**Contents:**
- DMGetBoundingBox#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#

Returns the global bounding box for the DM.

gmin - global minimum coordinates (length coord dim, optional)

gmax - global maximum coordinates (length coord dim, optional)

DM, DMGetLocalBoundingBox(), DMGetCoordinates(), DMGetCoordinatesLocal()

src/dm/interface/dmcoordinates.c

src/ts/tutorials/ex53.c src/ksp/ksp/tutorials/ex42.c src/ksp/ksp/tutorials/ex43.c src/snes/tutorials/ex23.c src/dm/impls/swarm/tutorials/ex1.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGetBoundingBox(DM dm, PetscReal gmin[], PetscReal gmax[])
```

Example 2 (unknown):
```unknown
DMGetLocalBoundingBox()
```

Example 3 (unknown):
```unknown
DMGetCoordinates()
```

Example 4 (unknown):
```unknown
DMGetCoordinatesLocal()
```

---

## DMGetCeed#

**URL:** https://petsc.org/release/manualpages/DM/DMGetCeed/

**Contents:**
- DMGetCeed#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Get the LibCEED context associated with this DM

ceed - The LibCEED context

src/dm/interface/dmceed.c

src/ts/tutorials/ex11.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGetCeed(DM dm, Ceed *ceed)
```

---

## DMGetCellCoordinateDM#

**URL:** https://petsc.org/release/manualpages/DM/DMGetCellCoordinateDM/

**Contents:**
- DMGetCellCoordinateDM#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets the DM that prescribes cellwise coordinate layout and scatters between global and local cellwise coordinates

cdm - cellwise coordinate DM, or NULL if they are not defined

Call DMLocalizeCoordinates() to automatically create cellwise coordinates for periodic geometries.

DM, DMSetCellCoordinateDM(), DMSetCellCoordinates(), DMSetCellCoordinatesLocal(), DMGetCellCoordinates(), DMGetCellCoordinatesLocal(), DMLocalizeCoordinates(), DMSetCoordinateDM(), DMGetCoordinateDM()

src/dm/interface/dmcoordinates.c

src/dm/impls/plex/tutorials/ex8.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGetCellCoordinateDM(DM dm, DM *cdm)
```

Example 2 (unknown):
```unknown
DMLocalizeCoordinates()
```

Example 3 (unknown):
```unknown
DMSetCellCoordinateDM()
```

Example 4 (unknown):
```unknown
DMSetCellCoordinates()
```

---

## DMGetCellCoordinateSection#

**URL:** https://petsc.org/release/manualpages/DM/DMGetCellCoordinateSection/

**Contents:**
- DMGetCellCoordinateSection#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Retrieve the PetscSection of cellwise coordinate values over the mesh.

section - The PetscSection object, or NULL if no cellwise coordinates are defined

This just retrieves the local section from the cell coordinate DM. In other words,

DM, DMGetCoordinateSection(), DMSetCellCoordinateSection(), DMGetCellCoordinateDM(), DMGetCoordinateDM(), DMGetLocalSection(), DMSetLocalSection()

src/dm/interface/dmcoordinates.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGetCellCoordinateSection(DM dm, PetscSection *section)
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (unknown):
```unknown
DMGetCellCoordinateDM(dm, &cdm);
  DMGetLocalSection(cdm, &section);
```

---

## DMGetCellCoordinatesLocalNoncollective#

**URL:** https://petsc.org/release/manualpages/DM/DMGetCellCoordinatesLocalNoncollective/

**Contents:**
- DMGetCellCoordinatesLocalNoncollective#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Non-collective version of DMGetCellCoordinatesLocal(). Fails if global cellwise coordinates have been set and DMGetCellCoordinatesLocalSetUp() not called.

c - cellwise coordinate vector

DM, DMGetCellCoordinatesLocalSetUp(), DMGetCellCoordinatesLocal(), DMSetCellCoordinatesLocal(), DMGetCellCoordinates(), DMSetCellCoordinates(), DMGetCellCoordinateDM()

src/dm/interface/dmcoordinates.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMGetCellCoordinatesLocal()
```

Example 2 (unknown):
```unknown
DMGetCellCoordinatesLocalSetUp()
```

Example 3 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGetCellCoordinatesLocalNoncollective(DM dm, Vec *c)
```

Example 4 (unknown):
```unknown
DMGetCellCoordinatesLocalSetUp()
```

---

## DMGetCellCoordinatesLocalSetUp#

**URL:** https://petsc.org/release/manualpages/DM/DMGetCellCoordinatesLocalSetUp/

**Contents:**
- DMGetCellCoordinatesLocalSetUp#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Prepares a local vector of cellwise coordinates, so that DMGetCellCoordinatesLocalNoncollective() can be used as non-collective afterwards.

DM, DMGetCellCoordinatesLocalNoncollective()

src/dm/interface/dmcoordinates.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMGetCellCoordinatesLocalNoncollective()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGetCellCoordinatesLocalSetUp(DM dm)
```

Example 3 (unknown):
```unknown
DMGetCellCoordinatesLocalNoncollective()
```

---

## DMGetCellCoordinatesLocal#

**URL:** https://petsc.org/release/manualpages/DM/DMGetCellCoordinatesLocal/

**Contents:**
- DMGetCellCoordinatesLocal#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Gets a local vector with the cellwise coordinates associated with the DM.

c - coordinate vector

This is a borrowed reference, so the user should NOT destroy this vector

Each process has the local and ghost coordinates

DM, DMSetCellCoordinatesLocal(), DMGetCellCoordinates(), DMSetCellCoordinates(), DMGetCellCoordinateDM(), DMGetCellCoordinatesLocalNoncollective()

src/dm/interface/dmcoordinates.c

src/dm/impls/plex/tutorials/ex8.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGetCellCoordinatesLocal(DM dm, Vec *c)
```

Example 2 (unknown):
```unknown
DMSetCellCoordinatesLocal()
```

Example 3 (unknown):
```unknown
DMGetCellCoordinates()
```

Example 4 (unknown):
```unknown
DMSetCellCoordinates()
```

---

## DMGetCellCoordinates#

**URL:** https://petsc.org/release/manualpages/DM/DMGetCellCoordinates/

**Contents:**
- DMGetCellCoordinates#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Gets a global vector with the cellwise coordinates associated with the DM.

c - global coordinate vector

This is a borrowed reference, so the user should NOT destroy this vector. When the DM is destroyed c will no longer be valid.

Each process has only the locally-owned portion of the global coordinates (does NOT have the ghost coordinates).

DM, DMGetCoordinates(), DMSetCellCoordinates(), DMGetCellCoordinatesLocal(), DMGetCellCoordinateDM()

src/dm/interface/dmcoordinates.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGetCellCoordinates(DM dm, Vec *c)
```

Example 2 (unknown):
```unknown
DMGetCoordinates()
```

Example 3 (unknown):
```unknown
DMSetCellCoordinates()
```

Example 4 (unknown):
```unknown
DMGetCellCoordinatesLocal()
```

---

## DMGetCellDS#

**URL:** https://petsc.org/release/manualpages/DM/DMGetCellDS/

**Contents:**
- DMGetCellDS#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Get the PetscDS defined on a given cell

point - Cell for the PetscDS

ds - The PetscDS defined on the given cell

dsIn - The PetscDS for input on the given cell, or NULL if the same ds

DM Basics, DM, DMGetDS(), DMSetRegionDS()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetCellDS(DM dm, PetscInt point, PetscDS *ds, PetscDS *dsIn)
```

Example 2 (unknown):
```unknown
DMSetRegionDS()
```

---

## DMGetCoarseDM#

**URL:** https://petsc.org/release/manualpages/DM/DMGetCoarseDM/

**Contents:**
- DMGetCoarseDM#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Get the coarse DMfrom which this DM was obtained by refinement

DM Basics, DM, DMSetCoarseDM(), DMCoarsen()

src/dm/interface/dm.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex26.c src/snes/tutorials/ex17.c src/snes/tutorials/ex8.c src/snes/tutorials/ex23.c src/snes/tutorials/ex64.c src/snes/tutorials/ex62.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetCoarseDM(DM dm, DM *cdm)
```

Example 2 (unknown):
```unknown
DMSetCoarseDM()
```

Example 3 (unknown):
```unknown
DMCoarsen()
```

---

## DMGetCoarsenLevel#

**URL:** https://petsc.org/release/manualpages/DM/DMGetCoarsenLevel/

**Contents:**
- DMGetCoarsenLevel#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Gets the number of coarsenings that have generated this DM.

level - number of coarsenings

DM Basics, DM, DMCoarsen(), DMSetCoarsenLevel(), DMGetRefineLevel(), DMDestroy(), DMView(), DMCreateGlobalVector(), DMCreateInterpolation()

src/dm/interface/dm.c

src/ts/tutorials/ex30.c src/snes/tutorials/ex48.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetCoarsenLevel(DM dm, PetscInt *level)
```

Example 2 (unknown):
```unknown
DMCoarsen()
```

Example 3 (unknown):
```unknown
DMSetCoarsenLevel()
```

Example 4 (unknown):
```unknown
DMGetRefineLevel()
```

---

## DMGetCompatibility#

**URL:** https://petsc.org/release/manualpages/DM/DMGetCompatibility/

**Contents:**
- DMGetCompatibility#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#
- Implementations#

determine if two DMs are compatible

compatible - whether or not the two DMs are compatible

set - whether or not the compatible value was actually determined and set

Two DMs are deemed compatible if they represent the same parallel decomposition of the same topology. This implies that the section (field data) on one “makes sense” with respect to the topology and parallel decomposition of the other. Loosely speaking, compatible DMs represent the same domain and parallel decomposition, but hold different data.

Typically, one would confirm compatibility if intending to simultaneously iterate over a pair of vectors obtained from different DMs.

For example, two DMDA objects are compatible if they have the same local and global sizes and the same stencil width. They can have different numbers of degrees of freedom per node. Thus, one could use the node numbering from either DM in bounds for a loop over vectors derived from either DM.

Consider the operation of summing data living on a 2-dof DMDA to data living on a 1-dof DMDA, which should be compatible, as in the following snippet.

Checking compatibility might be expensive for a given implementation of DM, or might be impossible to unambiguously confirm or deny. For this reason, this function may decline to determine compatibility, and hence users should always check the “set” output parameter.

A DM is always compatible with itself.

In the current implementation, DMs which live on “unequal” communicators (MPI_UNEQUAL in the terminology of MPI_Comm_compare()) are always deemed incompatible.

This function is labeled “Collective,” as information about all subdomains is required on each rank. However, in DM implementations which store all this information locally, this function may be merely “Logically Collective”.

Compatibility is assumed to be a symmetric concept; DM A is compatible with DM B iff B is compatible with A. Thus, this function checks the implementations of both dm and dmc (if they are of different types), attempting to determine compatibility. It is left to DM implementers to ensure that symmetry is preserved. The simplest way to do this is, when implementing type-specific logic for this function, is to check for existing logic in the implementation of other DM types and let *set = PETSC_FALSE if found.

DM Basics, DM, DMDACreateCompatibleDMDA(), DMStagCreateCompatibleDMStag()

src/dm/interface/dm.c

DMGetCompatibility_DA() in src/dm/impls/da/da.c DMGetCompatibility_Stag() in src/dm/impls/stag/stag.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetCompatibility(DM dm1, DM dm2, PetscBool *compatible, PetscBool *set)
```

Example 2 (sass):
```sass
...
  PetscCall(DMGetCompatibility(da1,da2,&compatible,&set));
  if (set && compatible)  {
    PetscCall(DMDAVecGetArrayDOF(da1,vec1,&arr1));
    PetscCall(DMDAVecGetArrayDOF(da2,vec2,&arr2));
    PetscCall(DMDAGetCorners(da1,&x,&y,NULL,&m,&n,NULL));
    for (j=y; j<y+n; ++j) {
      for (i=x; i<x+m, ++i) {
        arr1[j][i][0] = arr2[j][i][0] + arr2[j][i][1];
      }
    }
    PetscCall(DMDAVecRestoreArrayDOF(da1,vec1,&arr1));
    PetscCall(DMDAVecRestoreArrayDOF(da2,vec2,&arr2));
  } else {
    SETERRQ(PetscObjectComm((PetscObject)da1,PETSC_ERR_ARG_INCOMP,"DMDA objects incompatible");
  }
  ...
```

Example 3 (unknown):
```unknown
DMDACreateCompatibleDMDA()
```

Example 4 (unknown):
```unknown
DMStagCreateCompatibleDMStag()
```

---

## DMGetCoordinateDim#

**URL:** https://petsc.org/release/manualpages/DM/DMGetCoordinateDim/

**Contents:**
- DMGetCoordinateDim#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Retrieve the dimension of the embedding space for coordinate values. For example a mesh on the surface of a sphere would have a 3 dimensional embedding space

dim - The embedding dimension

DM, DMSetCoordinateDim(), DMGetCoordinateSection(), DMGetCoordinateDM(), DMGetLocalSection(), DMSetLocalSection()

src/dm/interface/dmcoordinates.c

src/snes/tutorials/ex71.c src/ts/tutorials/ex11.c src/snes/tutorials/ex76.c src/ts/tutorials/ex30.c src/snes/tutorials/ex13.c src/snes/tutorials/ex17.c src/dm/impls/plex/tutorials/dmplexgetrestoreclosureindices.F90 src/dm/impls/plex/tutorials/ex8.c src/dm/impls/plex/tutorials/ex15.c src/dm/impls/plex/tutorials/ex11.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGetCoordinateDim(DM dm, PetscInt *dim)
```

Example 2 (unknown):
```unknown
DMSetCoordinateDim()
```

Example 3 (unknown):
```unknown
DMGetCoordinateSection()
```

Example 4 (unknown):
```unknown
DMGetCoordinateDM()
```

---

## DMGetCoordinateDM#

**URL:** https://petsc.org/release/manualpages/DM/DMGetCoordinateDM/

**Contents:**
- DMGetCoordinateDM#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Gets the DM that prescribes coordinate layout and scatters between global and local coordinates

DM, DMSetCoordinateDM(), DMSetCoordinates(), DMSetCoordinatesLocal(), DMGetCoordinates(), DMGetCoordinatesLocal(), DMGSetCellCoordinateDM()

src/dm/interface/dmcoordinates.c

src/snes/tutorials/ex16.c src/snes/tutorials/ex55.c src/snes/tutorials/ex11.c src/snes/tutorials/ex46.c src/snes/tutorials/ex12.c src/snes/tutorials/ex55k.kokkos.cxx src/snes/tutorials/ex17.c src/snes/tutorials/ex33.c src/snes/tutorials/ex7.c src/snes/tutorials/ex77.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGetCoordinateDM(DM dm, DM *cdm)
```

Example 2 (unknown):
```unknown
DMSetCoordinateDM()
```

Example 3 (unknown):
```unknown
DMSetCoordinates()
```

Example 4 (unknown):
```unknown
DMSetCoordinatesLocal()
```

---

## DMGetCoordinateField#

**URL:** https://petsc.org/release/manualpages/DM/DMGetCoordinateField/

**Contents:**
- DMGetCoordinateField#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Get the DMField representation of the mesh coordinates

field - the DMField describing the coordinates

If the coordinate field does not yet exist, the DM implementation is asked to construct one.

DM, DMField, DMSetCoordinateField(), DMGetCoordinateDM(), DMGetCoordinates()

src/dm/interface/dmcoordinates.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGetCoordinateField(DM dm, DMField *field)
```

Example 2 (unknown):
```unknown
DMSetCoordinateField()
```

Example 3 (unknown):
```unknown
DMGetCoordinateDM()
```

Example 4 (unknown):
```unknown
DMGetCoordinates()
```

---

## DMGetCoordinateSection#

**URL:** https://petsc.org/release/manualpages/DM/DMGetCoordinateSection/

**Contents:**
- DMGetCoordinateSection#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Retrieve the PetscSection of coordinate values over the mesh.

section - The PetscSection object

This just retrieves the local section from the coordinate DM. In other words,

DM, DMGetCoordinateDM(), DMGetLocalSection(), DMSetLocalSection()

src/dm/interface/dmcoordinates.c

src/ts/tutorials/ex11.c src/snes/tutorials/ex13.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGetCoordinateSection(DM dm, PetscSection *section)
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (unknown):
```unknown
DMGetCoordinateDM(dm, &cdm);
  DMGetLocalSection(cdm, &section);
```

---

## DMGetCoordinatesLocalizedLocal#

**URL:** https://petsc.org/release/manualpages/DM/DMGetCoordinatesLocalizedLocal/

**Contents:**
- DMGetCoordinatesLocalizedLocal#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Check if the DM coordinates have been localized for cells on this process

areLocalized - PETSC_TRUE if localized

DM, DMLocalizeCoordinates(), DMGetCoordinatesLocalized(), DMSetPeriodicity()

src/dm/interface/dmperiodicity.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGetCoordinatesLocalizedLocal(DM dm, PetscBool *areLocalized)
```

Example 2 (unknown):
```unknown
DMLocalizeCoordinates()
```

Example 3 (unknown):
```unknown
DMGetCoordinatesLocalized()
```

Example 4 (unknown):
```unknown
DMSetPeriodicity()
```

---

## DMGetCoordinatesLocalized#

**URL:** https://petsc.org/release/manualpages/DM/DMGetCoordinatesLocalized/

**Contents:**
- DMGetCoordinatesLocalized#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Check if the DM coordinates have been localized for cells

areLocalized - PETSC_TRUE if localized

DM, DMLocalizeCoordinates(), DMSetPeriodicity(), DMGetCoordinatesLocalizedLocal()

src/dm/interface/dmperiodicity.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGetCoordinatesLocalized(DM dm, PetscBool *areLocalized)
```

Example 2 (unknown):
```unknown
DMLocalizeCoordinates()
```

Example 3 (unknown):
```unknown
DMSetPeriodicity()
```

Example 4 (unknown):
```unknown
DMGetCoordinatesLocalizedLocal()
```

---

## DMGetCoordinatesLocalNoncollective#

**URL:** https://petsc.org/release/manualpages/DM/DMGetCoordinatesLocalNoncollective/

**Contents:**
- DMGetCoordinatesLocalNoncollective#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Non-collective version of DMGetCoordinatesLocal(). Fails if global coordinates have been set and DMGetCoordinatesLocalSetUp() not called.

c - coordinate vector

A previous call to DMGetCoordinatesLocal() or DMGetCoordinatesLocalSetUp() ensures that a call to this function will not error.

DM, DMGetCoordinatesLocalSetUp(), DMGetCoordinatesLocal(), DMSetCoordinatesLocal(), DMGetCoordinates(), DMSetCoordinates(), DMGetCoordinateDM()

src/dm/interface/dmcoordinates.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMGetCoordinatesLocal()
```

Example 2 (unknown):
```unknown
DMGetCoordinatesLocalSetUp()
```

Example 3 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGetCoordinatesLocalNoncollective(DM dm, Vec *c)
```

Example 4 (unknown):
```unknown
DMGetCoordinatesLocal()
```

---

## DMGetCoordinatesLocalSetUp#

**URL:** https://petsc.org/release/manualpages/DM/DMGetCoordinatesLocalSetUp/

**Contents:**
- DMGetCoordinatesLocalSetUp#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#

Prepares a local vector of coordinates, so that DMGetCoordinatesLocalNoncollective() can be used as non-collective afterwards.

DM, DMSetCoordinates(), DMGetCoordinatesLocalNoncollective()

src/dm/interface/dmcoordinates.c

src/dm/impls/plex/tutorials/ex17.c src/ts/tutorials/ex52.c src/dm/impls/plex/tutorials/ex18.c src/dm/impls/plex/tutorials/ex9.c src/dm/impls/plex/tutorials/ex8.c src/dm/impls/plex/tutorials/ex10.c src/snes/tutorials/ex23.c src/snes/tutorials/ex34.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMGetCoordinatesLocalNoncollective()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGetCoordinatesLocalSetUp(DM dm)
```

Example 3 (unknown):
```unknown
DMSetCoordinates()
```

Example 4 (unknown):
```unknown
DMGetCoordinatesLocalNoncollective()
```

---

## DMGetCoordinatesLocalTuple#

**URL:** https://petsc.org/release/manualpages/DM/DMGetCoordinatesLocalTuple/

**Contents:**
- DMGetCoordinatesLocalTuple#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Gets a local vector with the coordinates of specified points and the section describing its layout.

p - the IS of points whose coordinates will be returned

pCoordSection - the PetscSection describing the layout of pCoord, i.e. each point corresponds to one point in p, and DOFs correspond to coordinates

pCoord - the Vec with coordinates of points in p

DMGetCoordinatesLocalSetUp() must be called first. This function employs DMGetCoordinatesLocalNoncollective() so it is not collective.

This creates a new vector, so the user SHOULD destroy this vector

Each process has the local and ghost coordinates

For DMDA, in two and three dimensions coordinates are interlaced (x_0,y_0,x_1,y_1,…) and (x_0,y_0,z_0,x_1,y_1,z_1…)

DM, DMDA, DMSetCoordinatesLocal(), DMGetCoordinatesLocal(), DMGetCoordinatesLocalNoncollective(), DMGetCoordinatesLocalSetUp(), DMGetCoordinates(), DMSetCoordinates(), DMGetCoordinateDM()

src/dm/interface/dmcoordinates.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGetCoordinatesLocalTuple(DM dm, IS p, PetscSection *pCoordSection, Vec *pCoord)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
DMGetCoordinatesLocalSetUp()
```

Example 4 (unknown):
```unknown
DMGetCoordinatesLocalNoncollective()
```

---

## DMGetCoordinatesLocal#

**URL:** https://petsc.org/release/manualpages/DM/DMGetCoordinatesLocal/

**Contents:**
- DMGetCoordinatesLocal#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Gets a local vector with the coordinates associated with the DM.

Collective the first time it is called

c - coordinate vector

This is a borrowed reference, so the user should NOT destroy c

Each process has the local and ghost coordinates

For DMDA, in two and three dimensions coordinates are interlaced (x_0,y_0,x_1,y_1,…) and (x_0,y_0,z_0,x_1,y_1,z_1…)

DM, DMSetCoordinatesLocal(), DMGetCoordinates(), DMSetCoordinates(), DMGetCoordinateDM(), DMGetCoordinatesLocalNoncollective()

src/dm/interface/dmcoordinates.c

src/snes/tutorials/ex16.c src/ksp/ksp/tutorials/ex70.c src/snes/tutorials/ex13.c src/ksp/ksp/tutorials/ex71.c src/snes/tutorials/ex56.c src/snes/tutorials/ex17.c src/ksp/ksp/tutorials/ex49.c src/ksp/ksp/tutorials/ex43.c src/ksp/ksp/tutorials/ex69.c src/snes/tutorials/ex77.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGetCoordinatesLocal(DM dm, Vec *c)
```

Example 2 (unknown):
```unknown
DMSetCoordinatesLocal()
```

Example 3 (unknown):
```unknown
DMGetCoordinates()
```

Example 4 (unknown):
```unknown
DMSetCoordinates()
```

---

## DMGetCoordinates#

**URL:** https://petsc.org/release/manualpages/DM/DMGetCoordinates/

**Contents:**
- DMGetCoordinates#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Gets a global vector with the coordinates associated with the DM.

Collective if the global vector with coordinates has not been set yet but the local vector with coordinates has been set

c - global coordinate vector

This is a borrowed reference, so the user should NOT destroy this vector. When the DM is destroyed c will no longer be valid.

Each process has only the locally-owned portion of the global coordinates (does NOT have the ghost coordinates), see DMGetCoordinatesLocal().

For DMDA, in two and three dimensions coordinates are interlaced (x_0,y_0,x_1,y_1,…) and (x_0,y_0,z_0,x_1,y_1,z_1…)

Does not work for DMSTAG

DM, DMDA, DMSetCoordinates(), DMGetCoordinatesLocal(), DMGetCoordinateDM(), DMDASetUniformCoordinates()

src/dm/interface/dmcoordinates.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex16.c src/snes/tutorials/ex55.c src/snes/tutorials/ex76.c src/snes/tutorials/ex5.c src/snes/tutorials/ex46.c src/ksp/ksp/tutorials/ex49.c src/snes/tutorials/ex33.c src/snes/tutorials/ex55k.kokkos.cxx src/snes/tutorials/ex22.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGetCoordinates(DM dm, Vec *c)
```

Example 2 (unknown):
```unknown
DMGetCoordinatesLocal()
```

Example 3 (unknown):
```unknown
DMSetCoordinates()
```

Example 4 (unknown):
```unknown
DMGetCoordinatesLocal()
```

---

## DMGetDefaultConstraints#

**URL:** https://petsc.org/release/manualpages/DM/DMGetDefaultConstraints/

**Contents:**
- DMGetDefaultConstraints#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Get the PetscSection and Mat that specify the local constraint interpolation. See DMSetDefaultConstraints() for a description of the purpose of constraint interpolation.

section - The PetscSection describing the range of the constraint matrix: relates rows of the constraint matrix to dofs of the default section. Returns NULL if there are no local constraints.

mat - The Mat that interpolates local constraints: its width should be the layout size of the default section. Returns NULL if there are no local constraints.

bias - Vector containing bias to be added to constrained dofs

This gets borrowed references, so the user should not destroy the PetscSection, Mat, or Vec.

DM Basics, DM, DMSetDefaultConstraints()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
DMSetDefaultConstraints()
```

Example 3 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetDefaultConstraints(DM dm, PetscSection *section, Mat *mat, Vec *bias)
```

Example 4 (unknown):
```unknown
PetscSection
```

---

## DMGetDimension#

**URL:** https://petsc.org/release/manualpages/DM/DMGetDimension/

**Contents:**
- DMGetDimension#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Return the topological dimension of the DM

dim - The topological dimension

DM Basics, DM, DMSetDimension(), DMCreate()

src/dm/interface/dm.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex26.c src/snes/tutorials/ex17.c src/snes/tutorials/ex8.c src/snes/tutorials/ex23.c src/snes/tutorials/ex7.c src/snes/tutorials/ex62.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetDimension(DM dm, PetscInt *dim)
```

Example 2 (unknown):
```unknown
DMSetDimension()
```

---

## DMGetDimPoints#

**URL:** https://petsc.org/release/manualpages/DM/DMGetDimPoints/

**Contents:**
- DMGetDimPoints#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Get the half-open interval for all points of a given dimension

pStart - The first point of the given dimension

pEnd - The first point following points of the given dimension

The points are vertices in the Hasse diagram encoding the topology. This is explained in https://arxiv.org/abs/0908.4427. If no points exist of this dimension in the storage scheme, then the interval is empty.

DM Basics, DM, DMPLEX, DMPlexGetDepthStratum(), DMPlexGetHeightStratum()

src/dm/interface/dm.c

DMGetDimPoints_DA() in src/dm/impls/da/dacreate.c DMGetDimPoints_pforest() in src/dm/impls/forest/p4est/pforest.h DMGetDimPoints_Plex() in src/dm/impls/plex/plexcreate.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetDimPoints(DM dm, PetscInt dim, PetscInt *pStart, PetscInt *pEnd)
```

Example 2 (unknown):
```unknown
DMPlexGetDepthStratum()
```

Example 3 (unknown):
```unknown
DMPlexGetHeightStratum()
```

---

## DMGetDS#

**URL:** https://petsc.org/release/manualpages/DM/DMGetDS/

**Contents:**
- DMGetDS#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Get the default PetscDS

ds - The default PetscDS

The ds is owned by the dm and should not be destroyed directly.

DM Basics, DM, DMGetCellDS(), DMGetRegionDS()

src/dm/interface/dm.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex77.c src/snes/tutorials/ex26.c src/snes/tutorials/ex17.c src/snes/tutorials/ex8.c src/snes/tutorials/ex64.c src/snes/tutorials/ex62.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetDS(DM dm, PetscDS *ds)
```

Example 2 (unknown):
```unknown
DMGetCellDS()
```

Example 3 (unknown):
```unknown
DMGetRegionDS()
```

---

## DMGetFieldAvoidTensor#

**URL:** https://petsc.org/release/manualpages/DM/DMGetFieldAvoidTensor/

**Contents:**
- DMGetFieldAvoidTensor#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Get flag to avoid defining the field on tensor cells

avoidTensor - The flag to avoid defining the field on tensor cells

DM Basics, DM, DMAddField(), DMSetField(), DMGetField(), DMSetFieldAvoidTensor()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetFieldAvoidTensor(DM dm, PetscInt f, PetscBool *avoidTensor)
```

Example 2 (unknown):
```unknown
DMAddField()
```

Example 3 (unknown):
```unknown
DMSetField()
```

Example 4 (unknown):
```unknown
DMGetField()
```

---

## DMGetField#

**URL:** https://petsc.org/release/manualpages/DM/DMGetField/

**Contents:**
- DMGetField#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#

Return the DMLabel and discretization object for a given DM field

label - The label indicating the support of the field, or NULL for the entire mesh (pass in NULL if not needed)

disc - The discretization object (pass in NULL if not needed)

DM Basics, DM, DMAddField(), DMSetField()

src/dm/interface/dm.c

src/ts/tutorials/ex46.c src/snes/tutorials/ex62.c src/ts/tutorials/ex30.c src/ts/tutorials/ex76.c src/ts/tutorials/ex77.c src/snes/tutorials/ex56.c src/dm/impls/plex/tutorials/ex16.c src/dm/impls/plex/tutorials/ex15.c src/snes/tutorials/ex69.c src/snes/tutorials/ex77.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetField(DM dm, PetscInt f, DMLabel *label, PetscObject *disc)
```

Example 2 (unknown):
```unknown
DMAddField()
```

Example 3 (unknown):
```unknown
DMSetField()
```

---

## DMGetFineDM#

**URL:** https://petsc.org/release/manualpages/DM/DMGetFineDM/

**Contents:**
- DMGetFineDM#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the fine mesh from which this DM was obtained by coarsening

DM Basics, DM, DMSetFineDM(), DMCoarsen(), DMRefine()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetFineDM(DM dm, DM *fdm)
```

Example 2 (unknown):
```unknown
DMSetFineDM()
```

Example 3 (unknown):
```unknown
DMCoarsen()
```

---

## DMGetGlobalSection#

**URL:** https://petsc.org/release/manualpages/DM/DMGetGlobalSection/

**Contents:**
- DMGetGlobalSection#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Get the PetscSection encoding the global data layout for the DM.

section - The PetscSection

This gets a borrowed reference, so the user should not destroy this PetscSection.

DM Basics, DM, DMSetLocalSection(), DMGetLocalSection()

src/dm/interface/dm.c

src/dm/impls/plex/tutorials/dmplexgetrestoreclosureindices.F90

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetGlobalSection(DM dm, PetscSection *section)
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

## DMGetGlobalVector#

**URL:** https://petsc.org/release/manualpages/DM/DMGetGlobalVector/

**Contents:**
- DMGetGlobalVector#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets a PETSc vector that may be used with the DM global routines.

g - the global vector

The vector values are NOT initialized and may have garbage in them, so you may need to zero them.

The output parameter, g, is a regular PETSc vector that should be returned with DMRestoreGlobalVector() DO NOT call VecDestroy() on it.

This is intended to be used for vectors you need for a short time, like within a single function call. For vectors that you intend to keep around (for example in a C struct) or pass around large parts of your code you should use DMCreateGlobalVector().

VecStride*() operations can be useful when using DM with dof > 1

DM, DMCreateGlobalVector(), VecDuplicate(), VecDuplicateVecs(), DMDACreate1d(), DMDACreate2d(), DMDACreate3d(), DMGlobalToLocalBegin(), DMGlobalToLocalEnd(), DMLocalToGlobalBegin(), DMCreateLocalVector(), DMRestoreLocalVector(), VecStrideMax(), VecStrideMin(), VecStrideNorm(), DMClearGlobalVectors(), DMGetNamedGlobalVector(), DMGetNamedLocalVector()

src/dm/interface/dmget.c

src/snes/tutorials/ex3k.kokkos.cxx src/snes/tutorials/ex76.c src/snes/tutorials/ex75.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex27.c src/snes/tutorials/ex33.c src/snes/tutorials/ex69.c src/snes/tutorials/ex7.c src/snes/tutorials/ex22.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h" 
PetscErrorCode DMGetGlobalVector(DM dm, Vec *g)
```

Example 2 (unknown):
```unknown
DMRestoreGlobalVector()
```

Example 3 (unknown):
```unknown
VecDestroy()
```

Example 4 (unknown):
```unknown
DMCreateGlobalVector()
```

---

## DMGetISColoringType#

**URL:** https://petsc.org/release/manualpages/DM/DMGetISColoringType/

**Contents:**
- DMGetISColoringType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the type of coloring, IS_COLORING_GLOBAL or IS_COLORING_LOCAL that is created by the DM

ctype - the matrix type

DM Basics, DM, DMDACreate1d(), DMDACreate2d(), DMDACreate3d(), DMCreateMatrix(), DMCreateMassMatrix(), DMSetMatrixPreallocateOnly(), MatType, DMGetMatType(), ISColoringType, IS_COLORING_GLOBAL, IS_COLORING_LOCAL

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
IS_COLORING_GLOBAL
```

Example 2 (unknown):
```unknown
IS_COLORING_LOCAL
```

Example 3 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetISColoringType(DM dm, ISColoringType *ctype)
```

Example 4 (unknown):
```unknown
DMDACreate1d()
```

---

## DMGetLabelByNum#

**URL:** https://petsc.org/release/manualpages/DM/DMGetLabelByNum/

**Contents:**
- DMGetLabelByNum#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Return the nth label on a DM

DM Basics, DM, DMLabel, DMAddLabel(), DMGetLabelValue(), DMSetLabelValue(), DMGetStratumIS()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetLabelByNum(DM dm, PetscInt n, DMLabel *label)
```

Example 2 (unknown):
```unknown
DMAddLabel()
```

Example 3 (unknown):
```unknown
DMGetLabelValue()
```

Example 4 (unknown):
```unknown
DMSetLabelValue()
```

---

## DMGetLabelIdIS#

**URL:** https://petsc.org/release/manualpages/DM/DMGetLabelIdIS/

**Contents:**
- DMGetLabelIdIS#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the DMLabelGetValueIS() from a DMLabel in the DM

name - The label name

ids - The integer ids, or NULL if the label does not exist

DM Basics, DM, DMLabelGetValueIS(), DMGetLabelSize()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMLabelGetValueIS()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetLabelIdIS(DM dm, const char name[], IS *ids)
```

Example 3 (unknown):
```unknown
DMLabelGetValueIS()
```

Example 4 (unknown):
```unknown
DMGetLabelSize()
```

---

## DMGetLabelName#

**URL:** https://petsc.org/release/manualpages/DM/DMGetLabelName/

**Contents:**
- DMGetLabelName#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Return the name of nth label

name - the label name

Some of the functions that appropriate on labels using their number have the suffix ByNum, others do not.

DM Basics, DM, DMLabel, DMGetLabelByNum(), DMGetLabel(), DMGetLabelValue(), DMSetLabelValue(), DMGetStratumIS()

src/dm/interface/dm.c

src/dm/label/tutorials/ex1f90.F90 src/dm/label/tutorials/ex1.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetLabelName(DM dm, PetscInt n, const char *name[])
```

Example 2 (unknown):
```unknown
DMGetLabelByNum()
```

Example 3 (unknown):
```unknown
DMGetLabel()
```

Example 4 (unknown):
```unknown
DMGetLabelValue()
```

---

## DMGetLabelOutput#

**URL:** https://petsc.org/release/manualpages/DM/DMGetLabelOutput/

**Contents:**
- DMGetLabelOutput#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the output flag for a given label

name - The label name

output - The flag for output

DM Basics, DM, DMLabel, DMSetLabelOutput(), DMCreateLabel(), DMHasLabel(), DMGetLabelValue(), DMSetLabelValue(), DMGetStratumIS()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetLabelOutput(DM dm, const char name[], PetscBool *output)
```

Example 2 (unknown):
```unknown
DMSetLabelOutput()
```

Example 3 (unknown):
```unknown
DMCreateLabel()
```

Example 4 (unknown):
```unknown
DMHasLabel()
```

---

## DMGetLabelSize#

**URL:** https://petsc.org/release/manualpages/DM/DMGetLabelSize/

**Contents:**
- DMGetLabelSize#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Developer Note#
- See Also#
- Level#
- Location#

Get the value of DMLabelGetNumValues() of a DMLabel in the DM

name - The label name

size - The number of different integer ids, or 0 if the label does not exist

This should be renamed to something like DMGetLabelNumValues() or removed.

DM Basics, DM, DMLabelGetNumValues(), DMSetLabelValue(), DMGetLabel()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMLabelGetNumValues()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetLabelSize(DM dm, const char name[], PetscInt *size)
```

Example 3 (unknown):
```unknown
DMGetLabelNumValues()
```

Example 4 (unknown):
```unknown
DMLabelGetNumValues()
```

---

## DMGetLabelValue#

**URL:** https://petsc.org/release/manualpages/DM/DMGetLabelValue/

**Contents:**
- DMGetLabelValue#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the value in a DMLabel for the given point, with -1 as the default

name - The label name

point - The mesh point

value - The label value for this point, or -1 if the point is not in the label

DM Basics, DM, DMLabelGetValue(), DMSetLabelValue(), DMGetStratumIS()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetLabelValue(DM dm, const char name[], PetscInt point, PetscInt *value)
```

Example 2 (unknown):
```unknown
DMLabelGetValue()
```

Example 3 (unknown):
```unknown
DMSetLabelValue()
```

Example 4 (unknown):
```unknown
DMGetStratumIS()
```

---

## DMGetLabel#

**URL:** https://petsc.org/release/manualpages/DM/DMGetLabel/

**Contents:**
- DMGetLabel#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Default labels in a DMPLEX#
- See Also#
- Level#
- Location#
- Examples#

Return the label of a given name, or NULL, from a DM

name - The label name

label - The DMLabel, or NULL if the label is absent

“depth” - Holds the depth (co-dimension) of each mesh point

“celltype” - Holds the topological type of each cell

“ghost” - If the DM is distributed with overlap, this marks the cells and faces in the overlap

“Cell Sets” - Mirrors the cell sets defined by GMsh and ExodusII

“Face Sets” - Mirrors the face sets defined by GMsh and ExodusII

“Vertex Sets” - Mirrors the vertex sets defined by GMsh

DM Basics, DM, DMLabel, DMHasLabel(), DMGetLabelByNum(), DMAddLabel(), DMCreateLabel(), DMPlexGetDepthLabel(), DMPlexGetCellType()

src/dm/interface/dm.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex26.c src/snes/tutorials/ex17.c src/snes/tutorials/ex8.c src/snes/tutorials/ex23.c src/snes/tutorials/ex64.c src/snes/tutorials/ex62.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetLabel(DM dm, const char name[], DMLabel *label)
```

Example 2 (unknown):
```unknown
DMHasLabel()
```

Example 3 (unknown):
```unknown
DMGetLabelByNum()
```

Example 4 (unknown):
```unknown
DMAddLabel()
```

---

## DMGetLocalBoundingBox#

**URL:** https://petsc.org/release/manualpages/DM/DMGetLocalBoundingBox/

**Contents:**
- DMGetLocalBoundingBox#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Returns the bounding box for the piece of the DM on this process.

lmin - local minimum coordinates (length coord dim, optional)

lmax - local maximum coordinates (length coord dim, optional)

If the DM is a DMDA and has no coordinates, the index bounds are returned instead.

DM, DMGetCoordinates(), DMGetCoordinatesLocal(), DMGetBoundingBox()

src/dm/interface/dmcoordinates.c

DMGetLocalBoundingBox_DA() in src/dm/impls/da/dageometry.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGetLocalBoundingBox(DM dm, PetscReal lmin[], PetscReal lmax[])
```

Example 2 (unknown):
```unknown
DMGetCoordinates()
```

Example 3 (unknown):
```unknown
DMGetCoordinatesLocal()
```

Example 4 (unknown):
```unknown
DMGetBoundingBox()
```

---

## DMGetLocalSection#

**URL:** https://petsc.org/release/manualpages/DM/DMGetLocalSection/

**Contents:**
- DMGetLocalSection#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Get the PetscSection encoding the local data layout for the DM.

section - The PetscSection

-dm_petscsection_view - View the section created by the DM

This gets a borrowed reference, so the user should not destroy this PetscSection.

DM Basics, DM, DMSetLocalSection(), DMGetGlobalSection()

src/dm/interface/dm.c

src/dm/impls/plex/tutorials/ex6.c src/ts/tutorials/ex18.c src/snes/tutorials/ex13.c src/snes/tutorials/ex56.c src/dm/impls/plex/tutorials/ex8.c src/dm/impls/plex/tutorials/ex16.c src/tao/tutorials/ex3.c src/dm/impls/plex/tutorials/ex15.c src/snes/tutorials/ex7.c src/snes/tutorials/ex77.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetLocalSection(DM dm, PetscSection *section)
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

## DMGetLocalToGlobalMapping#

**URL:** https://petsc.org/release/manualpages/DM/DMGetLocalToGlobalMapping/

**Contents:**
- DMGetLocalToGlobalMapping#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Accesses the local-to-global mapping in a DM.

dm - the DM that provides the mapping

The global to local mapping allows one to set values into the global vector or matrix using VecSetValuesLocal() and MatSetValuesLocal()

Vectors obtained with DMCreateGlobalVector() and matrices obtained with DMCreateMatrix() already contain the global mapping so you do need to use this function with those objects.

This mapping can then be used by VecSetLocalToGlobalMapping() or MatSetLocalToGlobalMapping().

DM Basics, DM, DMCreateLocalVector(), DMCreateGlobalVector(), VecSetLocalToGlobalMapping(), MatSetLocalToGlobalMapping(), DMCreateMatrix()

src/dm/interface/dm.c

src/tao/bound/tutorials/plate2f.F90 src/ksp/ksp/tutorials/ex70.c src/ksp/ksp/tutorials/ex71.c src/ksp/ksp/tutorials/ex14f.F90 src/ksp/ksp/tutorials/ex49.c src/tao/bound/tutorials/plate2.c src/snes/tutorials/ex48.c src/ksp/ksp/tutorials/ex43.c

DMGetLocalToGlobalMapping_Composite() in src/dm/impls/composite/pack.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetLocalToGlobalMapping(DM dm, ISLocalToGlobalMapping *ltog)
```

Example 2 (unknown):
```unknown
VecSetValuesLocal()
```

Example 3 (unknown):
```unknown
MatSetValuesLocal()
```

Example 4 (unknown):
```unknown
DMCreateGlobalVector()
```

---

## DMGetLocalVector#

**URL:** https://petsc.org/release/manualpages/DM/DMGetLocalVector/

**Contents:**
- DMGetLocalVector#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets a PETSc vector that may be used with the DM local routines. This vector has spaces for the ghost values.

The vector values are NOT initialized and may have garbage in them, so you may need to zero them.

The output parameter, g, is a regular PETSc vector that should be returned with DMRestoreLocalVector() DO NOT call VecDestroy() on it.

This is intended to be used for vectors you need for a short time, like within a single function call. For vectors that you intend to keep around (for example in a C struct) or pass around large parts of your code you should use DMCreateLocalVector().

VecStride*() operations can be useful when using DM with dof > 1

DM, DMCreateGlobalVector(), VecDuplicate(), VecDuplicateVecs(), DMDACreate1d(), DMDACreate2d(), DMDACreate3d(), DMGlobalToLocalBegin(), DMGlobalToLocalEnd(), DMLocalToGlobalBegin(), DMCreateLocalVector(), DMRestoreLocalVector(), VecStrideMax(), VecStrideMin(), VecStrideNorm(), DMClearLocalVectors(), DMGetNamedGlobalVector(), DMGetNamedLocalVector()

src/dm/interface/dmget.c

src/snes/tutorials/ex5f90.F90 src/snes/tutorials/ex14.c src/snes/tutorials/ex18.c src/snes/tutorials/ex12.c src/snes/tutorials/ex35.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex78.c src/snes/tutorials/ex15.c src/snes/tutorials/ex7.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h" 
PetscErrorCode DMGetLocalVector(DM dm, Vec *g)
```

Example 2 (unknown):
```unknown
DMRestoreLocalVector()
```

Example 3 (unknown):
```unknown
VecDestroy()
```

Example 4 (unknown):
```unknown
DMCreateLocalVector()
```

---

## DMGetMatType#

**URL:** https://petsc.org/release/manualpages/DM/DMGetMatType/

**Contents:**
- DMGetMatType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the type of matrix that would be created with DMCreateMatrix()

ctype - the matrix type

DM Basics, DM, DMDACreate1d(), DMDACreate2d(), DMDACreate3d(), DMCreateMatrix(), DMCreateMassMatrix(), DMSetMatrixPreallocateOnly(), MatType, DMSetMatType()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateMatrix()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetMatType(DM dm, MatType *ctype)
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

## DMGetNamedGlobalVector#

**URL:** https://petsc.org/release/manualpages/DM/DMGetNamedGlobalVector/

**Contents:**
- DMGetNamedGlobalVector#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

get access to a named, persistent global vector

dm - DM to hold named vectors

name - unique name for X

If a Vec with the given name does not exist, it is created.

DM, DMRestoreNamedGlobalVector(), DMHasNamedGlobalVector(), DMClearNamedGlobalVectors(), DMGetGlobalVector(), DMGetLocalVector()

src/dm/interface/dmget.c

src/ts/tutorials/ex30.c src/ts/tutorials/ex29.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h" 
PetscErrorCode DMGetNamedGlobalVector(DM dm, const char *name, Vec *X)
```

Example 2 (unknown):
```unknown
DMRestoreNamedGlobalVector()
```

Example 3 (unknown):
```unknown
DMHasNamedGlobalVector()
```

Example 4 (unknown):
```unknown
DMClearNamedGlobalVectors()
```

---

## DMGetNamedLocalVector#

**URL:** https://petsc.org/release/manualpages/DM/DMGetNamedLocalVector/

**Contents:**
- DMGetNamedLocalVector#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

get access to a named, persistent local vector

dm - DM to hold named vectors

name - unique name for X

If a Vec with the given name does not exist, it is created.

DM, DMGetNamedGlobalVector(), DMRestoreNamedLocalVector(), DMHasNamedLocalVector(), DMClearNamedLocalVectors(), DMGetGlobalVector(), DMGetLocalVector()

src/dm/interface/dmget.c

src/ts/tutorials/ex30.c src/ts/tutorials/ex29.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h" 
PetscErrorCode DMGetNamedLocalVector(DM dm, const char *name, Vec *X)
```

Example 2 (unknown):
```unknown
DMGetNamedGlobalVector()
```

Example 3 (unknown):
```unknown
DMRestoreNamedLocalVector()
```

Example 4 (unknown):
```unknown
DMHasNamedLocalVector()
```

---

## DMGetNaturalSF#

**URL:** https://petsc.org/release/manualpages/DM/DMGetNaturalSF/

**Contents:**
- DMGetNaturalSF#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Get the PetscSF encoding the map back to the original mesh ordering

This gets a borrowed reference, so the user should not destroy this PetscSF.

DM Basics, DM, DMSetNaturalSF(), DMSetUseNatural(), DMGetUseNatural(), DMPlexCreateGlobalToNaturalSF(), DMPlexDistribute()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetNaturalSF(DM dm, PetscSF *sf)
```

Example 2 (unknown):
```unknown
DMSetNaturalSF()
```

Example 3 (unknown):
```unknown
DMSetUseNatural()
```

Example 4 (unknown):
```unknown
DMGetUseNatural()
```

---

## DMGetNearNullSpaceConstructor#

**URL:** https://petsc.org/release/manualpages/DM/DMGetNearNullSpaceConstructor/

**Contents:**
- DMGetNearNullSpaceConstructor#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Calling sequence of nullsp#
- See Also#
- Level#
- Location#

Return the callback function which constructs the near-nullspace for a given field, defined with DMAddField()

Not Collective; No Fortran Support

field - The field number for the nullspace

nullsp - A callback to create the near-nullspace

origField - The field number given above, in the original DM

field - The field number in dm

nullSpace - The nullspace for the given field

DM Basics, DM, DMAddField(), DMGetField(), DMSetNearNullSpaceConstructor(), DMSetNullSpaceConstructor(), DMGetNullSpaceConstructor(), DMCreateSubDM(), MatNullSpace, DMCreateSuperDM()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMAddField()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetNearNullSpaceConstructor(DM dm, PetscInt field, PetscErrorCode (**nullsp)(DM dm, PetscInt origField, PetscInt field, MatNullSpace *nullSpace))
```

Example 3 (unknown):
```unknown
DMAddField()
```

Example 4 (unknown):
```unknown
DMGetField()
```

---

## DMGetNeighbors#

**URL:** https://petsc.org/release/manualpages/DM/DMGetNeighbors/

**Contents:**
- DMGetNeighbors#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Gets an array containing the MPI ranks of all the processes neighbors

nranks - the number of neighbours

ranks - the neighbors ranks

Do not free the array, it is freed when the DM is destroyed.

DM Basics, DM, DMDAGetNeighbors(), PetscSFGetRootRanks()

src/dm/interface/dm.c

src/dm/tutorials/swarm_ex3.c

DMGetNeighbors_DA() in src/dm/impls/da/dacreate.c DMGetNeighbors_Plex() in src/dm/impls/plex/plexcreate.c DMGetNeighbors_Stag() in src/dm/impls/stag/stag.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetNeighbors(DM dm, PetscInt *nranks, const PetscMPIInt *ranks[])
```

Example 2 (unknown):
```unknown
DMDAGetNeighbors()
```

Example 3 (unknown):
```unknown
PetscSFGetRootRanks()
```

---

## DMGetNullSpaceConstructor#

**URL:** https://petsc.org/release/manualpages/DM/DMGetNullSpaceConstructor/

**Contents:**
- DMGetNullSpaceConstructor#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Calling sequence of nullsp#
- See Also#
- Level#
- Location#

Return the callback function which constructs the nullspace for a given field, defined with DMAddField()

Not Collective; No Fortran Support

field - The field number for the nullspace

nullsp - A callback to create the nullspace

origField - The field number given above, in the original DM

field - The field number in dm

nullSpace - The nullspace for the given field

DM Basics, DM, DMAddField(), DMGetField(), DMSetNullSpaceConstructor(), DMSetNearNullSpaceConstructor(), DMGetNearNullSpaceConstructor(), DMCreateSubDM(), DMCreateSuperDM()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMAddField()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetNullSpaceConstructor(DM dm, PetscInt field, PetscErrorCode (**nullsp)(DM dm, PetscInt origField, PetscInt field, MatNullSpace *nullSpace))
```

Example 3 (unknown):
```unknown
DMAddField()
```

Example 4 (unknown):
```unknown
DMGetField()
```

---

## DMGetNumAuxiliaryVec#

**URL:** https://petsc.org/release/manualpages/DM/DMGetNumAuxiliaryVec/

**Contents:**
- DMGetNumAuxiliaryVec#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the number of auxiliary vectors associated with this DM

numAux - The number of auxiliary data vectors

DM Basics, DM, DMClearAuxiliaryVec(), DMSetAuxiliaryVec(), DMGetAuxiliaryLabels(), DMGetAuxiliaryVec()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetNumAuxiliaryVec(DM dm, PetscInt *numAux)
```

Example 2 (unknown):
```unknown
DMClearAuxiliaryVec()
```

Example 3 (unknown):
```unknown
DMSetAuxiliaryVec()
```

Example 4 (unknown):
```unknown
DMGetAuxiliaryLabels()
```

---

## DMGetNumDS#

**URL:** https://petsc.org/release/manualpages/DM/DMGetNumDS/

**Contents:**
- DMGetNumDS#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Get the number of discrete systems in the DM

Nds - The number of PetscDS objects

DM Basics, DM, DMGetDS(), DMGetCellDS()

src/dm/interface/dm.c

src/ts/tutorials/ex53.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetNumDS(DM dm, PetscInt *Nds)
```

Example 2 (unknown):
```unknown
DMGetCellDS()
```

---

## DMGetNumFields#

**URL:** https://petsc.org/release/manualpages/DM/DMGetNumFields/

**Contents:**
- DMGetNumFields#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Get the number of fields in the DM

numFields - The number of fields

DM Basics, DM, DMSetNumFields(), DMSetField()

src/dm/interface/dm.c

src/ts/tutorials/ex53.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetNumFields(DM dm, PetscInt *numFields)
```

Example 2 (unknown):
```unknown
DMSetNumFields()
```

Example 3 (unknown):
```unknown
DMSetField()
```

---

## DMGetNumLabels#

**URL:** https://petsc.org/release/manualpages/DM/DMGetNumLabels/

**Contents:**
- DMGetNumLabels#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Return the number of labels defined by on the DM

numLabels - the number of Labels

DM Basics, DM, DMLabel, DMGetLabelByNum(), DMGetLabelName(), DMGetLabelValue(), DMSetLabelValue(), DMGetStratumIS()

src/dm/interface/dm.c

src/dm/label/tutorials/ex1f90.F90 src/dm/label/tutorials/ex1.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetNumLabels(DM dm, PetscInt *numLabels)
```

Example 2 (unknown):
```unknown
DMGetLabelByNum()
```

Example 3 (unknown):
```unknown
DMGetLabelName()
```

Example 4 (unknown):
```unknown
DMGetLabelValue()
```

---

## DMGetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/DM/DMGetOptionsPrefix/

**Contents:**
- DMGetOptionsPrefix#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the prefix used for searching for all DM options in the options database.

prefix - pointer to the prefix string used is returned

DM Basics, DM, DMSetOptionsPrefix(), DMAppendOptionsPrefix(), DMSetFromOptions()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetOptionsPrefix(DM dm, const char *prefix[])
```

Example 2 (unknown):
```unknown
DMSetOptionsPrefix()
```

Example 3 (unknown):
```unknown
DMAppendOptionsPrefix()
```

Example 4 (unknown):
```unknown
DMSetFromOptions()
```

---

## DMGetOutputDM#

**URL:** https://petsc.org/release/manualpages/DM/DMGetOutputDM/

**Contents:**
- DMGetOutputDM#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Retrieve the DM associated with the layout for output

odm - The DM which provides the layout for output

In some situations the vector obtained with DMCreateGlobalVector() excludes points for degrees of freedom that are associated with fixed (Dirichelet) boundary conditions since the algebraic solver does not solve for those variables. The output DM includes these excluded points and its global vector contains the locations for those dof so that they can be output to a file or other viewer along with the unconstrained dof.

DM Basics, DM, VecView(), DMGetGlobalSection(), DMCreateGlobalVector(), PetscSectionHasConstraints(), DMSetGlobalSection()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetOutputDM(DM dm, DM *odm)
```

Example 2 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 3 (unknown):
```unknown
DMGetGlobalSection()
```

Example 4 (unknown):
```unknown
DMCreateGlobalVector()
```

---

## DMGetOutputSequenceLength#

**URL:** https://petsc.org/release/manualpages/DM/DMGetOutputSequenceLength/

**Contents:**
- DMGetOutputSequenceLength#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

Retrieve the number of sequence values from a PetscViewer

viewer - The PetscViewer to get it from

name - The sequence name

len - The length of the output sequence

This is intended for output that should appear in sequence, for instance a set of timesteps in an PETSCVIEWERHDF5 file, or a set of realizations of a stochastic system.

It is unclear at the user API level why a DM is needed as input

DM Basics, DM, DMGetOutputSequenceNumber(), DMSetOutputSequenceNumber(), VecView()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetOutputSequenceLength(DM dm, PetscViewer viewer, const char name[], PetscInt *len)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PETSCVIEWERHDF5
```

---

## DMGetOutputSequenceNumber#

**URL:** https://petsc.org/release/manualpages/DM/DMGetOutputSequenceNumber/

**Contents:**
- DMGetOutputSequenceNumber#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Retrieve the sequence number/value for output

num - The output sequence number

val - The output sequence value

This is intended for output that should appear in sequence, for instance a set of timesteps in an PETSCVIEWERHDF5 file, or a set of realizations of a stochastic system.

The DM serves as a convenient place to store the current iteration value. The iteration is not not directly related to the DM.

DM Basics, DM, VecView()

src/dm/interface/dm.c

src/dm/impls/plex/tutorials/ex19.c src/ts/tutorials/ex30.c src/ts/tutorials/ex18.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/tutorials/ex48.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetOutputSequenceNumber(DM dm, PetscInt *num, PetscReal *val)
```

Example 2 (unknown):
```unknown
PETSCVIEWERHDF5
```

---

## DMGetPeriodicity#

**URL:** https://petsc.org/release/manualpages/DM/DMGetPeriodicity/

**Contents:**
- DMGetPeriodicity#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#

Get the description of mesh periodicity

maxCell - Over distances greater than this, we can assume a point has crossed over to another sheet, when trying to localize cell coordinates

Lstart - If we assume the mesh is a torus, this is the start of each coordinate, or NULL for 0.0

L - If we assume the mesh is a torus, this is the length of each coordinate, otherwise it is < 0.0

src/dm/interface/dmperiodicity.c

src/snes/tutorials/ex12.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGetPeriodicity(DM dm, const PetscReal *maxCell[], const PetscReal *Lstart[], const PetscReal *L[])
```

---

## DMGetPointSF#

**URL:** https://petsc.org/release/manualpages/DM/DMGetPointSF/

**Contents:**
- DMGetPointSF#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Get the PetscSF encoding the parallel section point overlap for the DM.

Not collective but the resulting PetscSF is collective

This gets a borrowed reference, so the user should not destroy this PetscSF.

DM Basics, DM, DMSetPointSF(), DMGetSectionSF(), DMSetSectionSF(), DMCreateSectionSF()

src/dm/interface/dm.c

src/ts/tutorials/ex11.c src/dm/impls/plex/tutorials/ex14.c src/dm/impls/plex/tutorials/ex14f90.F90

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetPointSF(DM dm, PetscSF *sf)
```

Example 2 (unknown):
```unknown
DMSetPointSF()
```

Example 3 (unknown):
```unknown
DMGetSectionSF()
```

Example 4 (unknown):
```unknown
DMSetSectionSF()
```

---

## DMGetRefineLevel#

**URL:** https://petsc.org/release/manualpages/DM/DMGetRefineLevel/

**Contents:**
- DMGetRefineLevel#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets the number of refinements that have generated this DM from some initial DM.

level - number of refinements

This can be used, by example, to set the number of coarser levels associated with this DM for a multigrid solver.

DM Basics, DM, DMRefine(), DMCoarsen(), DMGetCoarsenLevel(), DMDestroy(), DMView(), DMCreateGlobalVector(), DMCreateInterpolation()

src/dm/interface/dm.c

src/ts/tutorials/ex30.c src/ksp/ksp/tutorials/ex65.c src/snes/tutorials/ex11.c src/snes/tutorials/ex48.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetRefineLevel(DM dm, PetscInt *level)
```

Example 2 (unknown):
```unknown
DMCoarsen()
```

Example 3 (unknown):
```unknown
DMGetCoarsenLevel()
```

Example 4 (unknown):
```unknown
DMDestroy()
```

---

## DMGetRegionDS#

**URL:** https://petsc.org/release/manualpages/DM/DMGetRegionDS/

**Contents:**
- DMGetRegionDS#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Get the PetscDS for a given mesh region, defined by a DMLabel

label - The DMLabel defining the mesh region, or NULL for the entire mesh

fields - The IS containing the DM field numbers for the fields in this PetscDS, or NULL

ds - The PetscDS defined on the given region, or NULL

dsIn - The PetscDS for input in the given region, or NULL

If a non-NULL label is given, but there is no PetscDS on that specific label, the PetscDS for the full domain (if present) is returned. Returns with fields = NULL and ds = NULL if there is no PetscDS for the full domain.

DM Basics, DM, DMGetRegionNumDS(), DMSetRegionDS(), DMGetDS(), DMGetCellDS()

src/dm/interface/dm.c

src/dm/impls/plex/tutorials/ex8.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetRegionDS(DM dm, DMLabel label, IS *fields, PetscDS *ds, PetscDS *dsIn)
```

Example 2 (unknown):
```unknown
DMGetRegionNumDS()
```

Example 3 (unknown):
```unknown
DMSetRegionDS()
```

Example 4 (unknown):
```unknown
DMGetCellDS()
```

---

## DMGetRegionNumDS#

**URL:** https://petsc.org/release/manualpages/DM/DMGetRegionNumDS/

**Contents:**
- DMGetRegionNumDS#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#

Get the PetscDS for a given mesh region, defined by the region number

num - The region number, in [0, Nds)

label - The region label, or NULL

fields - The IS containing the DM field numbers for the fields in this PetscDS, or NULL

ds - The PetscDS defined on the given region, or NULL

dsIn - The PetscDS for input in the given region, or NULL

DM Basics, DM, DMGetRegionDS(), DMSetRegionDS(), DMGetDS(), DMGetCellDS()

src/dm/interface/dm.c

src/snes/tutorials/ex23.c src/ts/tutorials/ex53.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetRegionNumDS(DM dm, PetscInt num, DMLabel *label, IS *fields, PetscDS *ds, PetscDS *dsIn)
```

Example 2 (unknown):
```unknown
DMGetRegionDS()
```

Example 3 (unknown):
```unknown
DMSetRegionDS()
```

Example 4 (unknown):
```unknown
DMGetCellDS()
```

---

## DMGetSectionSF#

**URL:** https://petsc.org/release/manualpages/DM/DMGetSectionSF/

**Contents:**
- DMGetSectionSF#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Get the PetscSF encoding the parallel dof overlap for the DM. If it has not been set, it is created from the default PetscSection layouts in the DM.

This gets a borrowed reference, so the user should not destroy this PetscSF.

DM Basics, DM, DMSetSectionSF(), DMCreateSectionSF()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetSectionSF(DM dm, PetscSF *sf)
```

Example 3 (unknown):
```unknown
DMSetSectionSF()
```

Example 4 (unknown):
```unknown
DMCreateSectionSF()
```

---

## DMGetSparseLocalize#

**URL:** https://petsc.org/release/manualpages/DM/DMGetSparseLocalize/

**Contents:**
- DMGetSparseLocalize#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Check if the DM coordinates should be localized only for cells near the periodic boundary.

sparse - PETSC_TRUE if only cells near the periodic boundary are localized

DMSetSparseLocalize(), DMLocalizeCoordinates(), DMSetPeriodicity()

src/dm/interface/dmperiodicity.c

src/dm/impls/plex/tutorials/ex8.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMGetSparseLocalize(DM dm, PetscBool *sparse)
```

Example 2 (unknown):
```unknown
DMSetSparseLocalize()
```

Example 3 (unknown):
```unknown
DMLocalizeCoordinates()
```

Example 4 (unknown):
```unknown
DMSetPeriodicity()
```

---

## DMGetStratumIS#

**URL:** https://petsc.org/release/manualpages/DM/DMGetStratumIS/

**Contents:**
- DMGetStratumIS#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Get the points in a label stratum

name - The label name

value - The stratum value

points - The stratum points, or NULL if the label does not exist or does not have that value

DM Basics, DM, DMLabelGetStratumIS(), DMGetStratumSize()

src/dm/interface/dm.c

src/dm/impls/plex/tutorials/ex1f90.F90 src/ts/tutorials/ex52.c src/dm/impls/plex/tutorials/ex1.c src/snes/tutorials/ex56.c src/snes/tutorials/ex69.c src/snes/tutorials/ex77.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetStratumIS(DM dm, const char name[], PetscInt value, IS *points)
```

Example 2 (unknown):
```unknown
DMLabelGetStratumIS()
```

Example 3 (unknown):
```unknown
DMGetStratumSize()
```

---

## DMGetStratumSize#

**URL:** https://petsc.org/release/manualpages/DM/DMGetStratumSize/

**Contents:**
- DMGetStratumSize#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the number of points in a label stratum

name - The label name of the stratum

value - The stratum value

size - The number of points, also called the stratum size

DM Basics, DM, DMLabelGetStratumSize(), DMGetLabelSize(), DMGetLabelIds()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetStratumSize(DM dm, const char name[], PetscInt value, PetscInt *size)
```

Example 2 (unknown):
```unknown
DMLabelGetStratumSize()
```

Example 3 (unknown):
```unknown
DMGetLabelSize()
```

Example 4 (unknown):
```unknown
DMGetLabelIds()
```

---

## DMGetType#

**URL:** https://petsc.org/release/manualpages/DM/DMGetType/

**Contents:**
- DMGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the DM type name (as a string) from the DM.

type - The DMType name

type should not be retained for later use as it will be an invalid pointer if the DMType of dm is changed.

DM Basics, DM, DMType, DMDA, DMPLEX, DMSetType(), DMCreate(), PetscObjectTypeCompare(), PetscObjectTypeCompareAny()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetType(DM dm, DMType *type)
```

Example 2 (unknown):
```unknown
DMSetType()
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

## DMGetUseNatural#

**URL:** https://petsc.org/release/manualpages/DM/DMGetUseNatural/

**Contents:**
- DMGetUseNatural#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the flag for creating a mapping to the natural order when a DM is (re)distributed in parallel

useNatural - PETSC_TRUE to build the mapping to a natural order during distribution

DM Basics, DM, DMSetUseNatural(), DMCreate()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetUseNatural(DM dm, PetscBool *useNatural)
```

Example 2 (unknown):
```unknown
DMSetUseNatural()
```

---

## DMGetVecType#

**URL:** https://petsc.org/release/manualpages/DM/DMGetVecType/

**Contents:**
- DMGetVecType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Gets the type of vector created with DMCreateLocalVector() and DMCreateGlobalVector()

da - initial distributed array

ctype - the vector type

DM Basics, DM, DMCreate(), DMDestroy(), DMDAInterpolationType, VecType, DMSetMatType(), DMGetMatType(), DMSetVecType()

src/dm/interface/dm.c

src/snes/tutorials/ex28.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateLocalVector()
```

Example 2 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 3 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetVecType(DM da, VecType *ctype)
```

Example 4 (unknown):
```unknown
DMDestroy()
```

---

## DMGetWorkArray#

**URL:** https://petsc.org/release/manualpages/DM/DMGetWorkArray/

**Contents:**
- DMGetWorkArray#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Gets a work array guaranteed to be at least the input size, restore with DMRestoreWorkArray()

count - The minimum size

dtype - MPI data type, often MPIU_REAL, MPIU_SCALAR, or MPIU_INT)

A DM may stash the array between instantiations so using this routine may be more efficient than calling PetscMalloc()

The array may contain nonzero values

DM Basics, DM, DMDestroy(), DMCreate(), DMRestoreWorkArray(), PetscMalloc()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMRestoreWorkArray()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGetWorkArray(DM dm, PetscInt count, MPI_Datatype dtype, void *mem)
```

Example 3 (unknown):
```unknown
MPIU_SCALAR
```

Example 4 (unknown):
```unknown
PetscMalloc()
```

---

## DMGlobalToLocalBeginDefaultShell#

**URL:** https://petsc.org/release/manualpages/DM/DMGlobalToLocalBeginDefaultShell/

**Contents:**
- DMGlobalToLocalBeginDefaultShell#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Uses the GlobalToLocal VecScatter context set by the user to begin a global to local scatter

This is not normally called directly by user code, generally user code calls DMGlobalToLocalBegin() and DMGlobalToLocalEnd(). If the user provides their own custom routines to DMShellSetLocalToGlobal() then those routines might have reason to call this function.

DM, DMSHELL, DMGlobalToLocalEndDefaultShell()

src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMGlobalToLocalBeginDefaultShell(DM dm, Vec g, InsertMode mode, Vec l)
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
DMShellSetLocalToGlobal()
```

---

## DMGlobalToLocalBegin#

**URL:** https://petsc.org/release/manualpages/DM/DMGlobalToLocalBegin/

**Contents:**
- DMGlobalToLocalBegin#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Begins updating local vectors from global vector

Neighbor-wise Collective

g - the global vector

mode - INSERT_VALUES or ADD_VALUES

The operation is completed with DMGlobalToLocalEnd()

One can perform local computations between the DMGlobalToLocalBegin() and DMGlobalToLocalEnd() to overlap communication and computation

DMGlobalToLocal() is a short form of DMGlobalToLocalBegin() and DMGlobalToLocalEnd()

DMGlobalToLocalHookAdd() may be used to provide additional operations that are performed during the update process.

DM Basics, DM, DMCoarsen(), DMDestroy(), DMView(), DMCreateGlobalVector(), DMCreateInterpolation(), DMGlobalToLocal(), DMGlobalToLocalEnd(), DMLocalToGlobalBegin(), DMLocalToGlobal(), DMLocalToGlobalEnd()

src/dm/interface/dm.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex14.c src/snes/tutorials/ex18.c src/snes/tutorials/ex12.c src/snes/tutorials/ex35.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex78.c src/snes/tutorials/ex15.c src/snes/tutorials/ex7.c

DMGlobalToLocalBegin_Composite() in src/dm/impls/composite/pack.c DMGlobalToLocalBegin_DA() in src/dm/impls/da/dagtol.c DMGlobalToLocalBegin_Moab() in src/dm/impls/moab/dmmbvec.cxx DMGlobalToLocalBegin_Network() in src/dm/impls/network/network.c DMGlobalToLocalBegin_Redundant() in src/dm/impls/redundant/dmredundant.c DMGlobalToLocalBegin_Sliced() in src/dm/impls/sliced/sliced.c DMGlobalToLocalBegin_Stag() in src/dm/impls/stag/stag.c DMGlobalToLocalBegin_Swarm() in src/dm/impls/swarm/swarm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGlobalToLocalBegin(DM dm, Vec g, InsertMode mode, Vec l)
```

Example 2 (unknown):
```unknown
INSERT_VALUES
```

Example 3 (unknown):
```unknown
DMGlobalToLocalEnd()
```

Example 4 (unknown):
```unknown
DMGlobalToLocalBegin()
```

---

## DMGlobalToLocalEndDefaultShell#

**URL:** https://petsc.org/release/manualpages/DM/DMGlobalToLocalEndDefaultShell/

**Contents:**
- DMGlobalToLocalEndDefaultShell#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Uses the GlobalToLocal VecScatter context set by the user to end a global to local scatter Collective

DM, DMSHELL, DMGlobalToLocalBeginDefaultShell()

src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMGlobalToLocalEndDefaultShell(DM dm, Vec g, InsertMode mode, Vec l)
```

Example 2 (unknown):
```unknown
DMGlobalToLocalBeginDefaultShell()
```

---

## DMGlobalToLocalEnd#

**URL:** https://petsc.org/release/manualpages/DM/DMGlobalToLocalEnd/

**Contents:**
- DMGlobalToLocalEnd#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Ends updating local vectors from global vector

Neighbor-wise Collective

g - the global vector

mode - INSERT_VALUES or ADD_VALUES

See DMGlobalToLocalBegin() for details.

DM Basics, DM, DMCoarsen(), DMDestroy(), DMView(), DMCreateGlobalVector(), DMCreateInterpolation(), DMGlobalToLocal(), DMLocalToGlobalBegin(), DMLocalToGlobal(), DMLocalToGlobalEnd()

src/dm/interface/dm.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex14.c src/snes/tutorials/ex18.c src/snes/tutorials/ex12.c src/snes/tutorials/ex35.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex78.c src/snes/tutorials/ex15.c src/snes/tutorials/ex7.c

DMGlobalToLocalEnd_Composite() in src/dm/impls/composite/pack.c DMGlobalToLocalEnd_DA() in src/dm/impls/da/dagtol.c DMGlobalToLocalEnd_Moab() in src/dm/impls/moab/dmmbvec.cxx DMGlobalToLocalEnd_Network() in src/dm/impls/network/network.c DMGlobalToLocalEnd_Redundant() in src/dm/impls/redundant/dmredundant.c DMGlobalToLocalEnd_Sliced() in src/dm/impls/sliced/sliced.c DMGlobalToLocalEnd_Stag() in src/dm/impls/stag/stag.c DMGlobalToLocalEnd_Swarm() in src/dm/impls/swarm/swarm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGlobalToLocalEnd(DM dm, Vec g, InsertMode mode, Vec l)
```

Example 2 (unknown):
```unknown
INSERT_VALUES
```

Example 3 (unknown):
```unknown
DMGlobalToLocalBegin()
```

Example 4 (unknown):
```unknown
DMCoarsen()
```

---

## DMGlobalToLocalHookAdd#

**URL:** https://petsc.org/release/manualpages/DM/DMGlobalToLocalHookAdd/

**Contents:**
- DMGlobalToLocalHookAdd#
- Synopsis#
- Input Parameters#
- Calling sequence of beginhook#
- Calling sequence of endhook#
- Note#
- See Also#
- Level#
- Location#

adds a callback to be run when DMGlobalToLocal() is called

beginhook - function to run at the beginning of DMGlobalToLocalBegin()

endhook - function to run after DMGlobalToLocalEnd() has completed

ctx - [optional] context for provide data for the hooks (may be NULL)

ctx - optional function context

ctx - optional function context

The hook may be used to provide, for example, values that represent boundary conditions in the local vectors that do not exist on the global vector.

DM Basics, DM, DMGlobalToLocal(), DMRefineHookAdd(), SNESFASGetInterpolation(), SNESFASGetInjection(), PetscObjectCompose(), PetscContainerCreate()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMGlobalToLocal()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGlobalToLocalHookAdd(DM dm, PetscErrorCode (*beginhook)(DM dm, Vec g, InsertMode mode, Vec l, PetscCtx ctx), PetscErrorCode (*endhook)(DM dm, Vec g, InsertMode mode, Vec l, PetscCtx ctx), PetscCtx ctx)
```

Example 3 (unknown):
```unknown
DMGlobalToLocalBegin()
```

Example 4 (unknown):
```unknown
DMGlobalToLocalEnd()
```

---

## DMGlobalToLocalSolve#

**URL:** https://petsc.org/release/manualpages/DM/DMGlobalToLocalSolve/

**Contents:**
- DMGlobalToLocalSolve#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Solve for the global vector that is mapped to a given local vector by DMGlobalToLocalBegin()/DMGlobalToLocalEnd() with mode INSERT_VALUES.

y - The global vector: the input value of this variable is used as an initial guess

y - The least-squares solution

It is assumed that the sum of all the local vector sizes is greater than or equal to the global vector size, so the solution is a least-squares solution. It is also assumed that DMLocalToGlobalBegin()/DMLocalToGlobalEnd() with mode ADD_VALUES is the adjoint of the global-to-local map, so that the least-squares solution may be found by the normal equations.

If the DM is of type DMPLEX, then y is the solution of \( L^T * D * L * y = L^T * D * x \), where \(D\) is a diagonal mask that is 1 for every point in the union of the closures of the local cells and 0 otherwise. This difference is only relevant if there are anchor points that are not in the closure of any local cell (see DMPlexGetAnchors()/DMPlexSetAnchors()).

If this solves for a global vector from a local vector why is not called DMLocalToGlobalSolve()?

DM Basics, DM, DMGlobalToLocalBegin(), DMGlobalToLocalEnd(), DMLocalToGlobalBegin(), DMLocalToGlobalEnd(), DMPlexGetAnchors(), DMPlexSetAnchors()

src/ksp/ksp/utils/dm/dmproject.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

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
INSERT_VALUES
```

Example 4 (unknown):
```unknown
#include "petscdm.h" 
#include "petscdmda.h" 
#include "petscdmplex.h" 
#include "petscdmswarm.h" 
#include "petscksp.h" 
PetscErrorCode DMGlobalToLocalSolve(DM dm, Vec x, Vec y)
```

---

## DMGlobalToLocal#

**URL:** https://petsc.org/release/manualpages/DM/DMGlobalToLocal/

**Contents:**
- DMGlobalToLocal#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

update local vectors from global vector

Neighbor-wise Collective

g - the global vector

mode - INSERT_VALUES or ADD_VALUES

The communication involved in this update can be overlapped with computation by instead using DMGlobalToLocalBegin() and DMGlobalToLocalEnd().

DMGlobalToLocalHookAdd() may be used to provide additional operations that are performed during the update process.

DM Basics, DM, DMGlobalToLocalHookAdd(), DMCoarsen(), DMDestroy(), DMView(), DMCreateGlobalVector(), DMCreateInterpolation(), DMLocalToGlobalBegin(), DMLocalToGlobal(), DMLocalToGlobalEnd(), DMGlobalToLocalBegin(), DMGlobalToLocalEnd()

src/dm/interface/dm.c

src/ts/tutorials/ex45.c src/snes/tutorials/ex11.c src/snes/tutorials/ex16.c src/snes/tutorials/ex3k.kokkos.cxx src/ts/tutorials/ex30.c src/dm/impls/stag/tutorials/ex4.c src/dm/impls/stag/tutorials/ex1.c src/dm/tutorials/ex2.c src/dm/impls/stag/tutorials/ex6.c src/dm/impls/stag/tutorials/ex3.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMGlobalToLocal(DM dm, Vec g, InsertMode mode, Vec l)
```

Example 2 (unknown):
```unknown
INSERT_VALUES
```

Example 3 (unknown):
```unknown
DMGlobalToLocalBegin()
```

Example 4 (unknown):
```unknown
DMGlobalToLocalEnd()
```

---

## DMHasBasisTransform#

**URL:** https://petsc.org/release/manualpages/DM/DMHasBasisTransform/

**Contents:**
- DMHasBasisTransform#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Whether the DM employs a basis transformation from functions in global vectors to functions in local vectors

flg - PETSC_TRUE if a basis transformation should be done

DM Basics, DM, DMPlexGlobalToLocalBasis(), DMPlexLocalToGlobalBasis(), DMPlexCreateBasisRotation()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMHasBasisTransform(DM dm, PetscBool *flg)
```

Example 2 (unknown):
```unknown
DMPlexGlobalToLocalBasis()
```

Example 3 (unknown):
```unknown
DMPlexLocalToGlobalBasis()
```

Example 4 (unknown):
```unknown
DMPlexCreateBasisRotation()
```

---

## DMHasBound#

**URL:** https://petsc.org/release/manualpages/DM/DMHasBound/

**Contents:**
- DMHasBound#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Determine whether a bound condition was specified

dm - The DM, with a PetscDS that matches the problem being constrained

hasBound - Flag indicating if a bound condition was specified

DM Basics, DM, DSAddBoundary(), PetscDSAddBoundary()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMHasBound(DM dm, PetscBool *hasBound)
```

Example 2 (unknown):
```unknown
DSAddBoundary()
```

Example 3 (unknown):
```unknown
PetscDSAddBoundary()
```

---

## DMHasColoring#

**URL:** https://petsc.org/release/manualpages/DM/DMHasColoring/

**Contents:**
- DMHasColoring#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

does the DM object have a method of providing a coloring?

flg - PETSC_TRUE if the DM has facilities for DMCreateColoring().

DM Basics, DM, DMCreateColoring()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMHasColoring(DM dm, PetscBool *flg)
```

Example 2 (unknown):
```unknown
DMCreateColoring()
```

Example 3 (unknown):
```unknown
DMCreateColoring()
```

---

## DMHasCreateInjection#

**URL:** https://petsc.org/release/manualpages/DM/DMHasCreateInjection/

**Contents:**
- DMHasCreateInjection#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

does the DM object have a method of providing an injection?

flg - PETSC_TRUE if the DM has facilities for DMCreateInjection().

DM Basics, DM, DMCreateInjection(), DMHasCreateRestriction(), DMHasCreateInterpolation()

src/dm/interface/dm.c

DMHasCreateInjection_DA() in src/dm/impls/da/dacreate.c DMHasCreateInjection_Stag() in src/dm/impls/stag/stag.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMHasCreateInjection(DM dm, PetscBool *flg)
```

Example 2 (unknown):
```unknown
DMCreateInjection()
```

Example 3 (unknown):
```unknown
DMCreateInjection()
```

Example 4 (unknown):
```unknown
DMHasCreateRestriction()
```

---

## DMHasCreateRestriction#

**URL:** https://petsc.org/release/manualpages/DM/DMHasCreateRestriction/

**Contents:**
- DMHasCreateRestriction#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

does the DM object have a method of providing a restriction?

flg - PETSC_TRUE if the DM has facilities for DMCreateRestriction().

DM Basics, DM, DMCreateRestriction(), DMHasCreateInterpolation(), DMHasCreateInjection()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMHasCreateRestriction(DM dm, PetscBool *flg)
```

Example 2 (unknown):
```unknown
DMCreateRestriction()
```

Example 3 (unknown):
```unknown
DMCreateRestriction()
```

Example 4 (unknown):
```unknown
DMHasCreateInterpolation()
```

---

## DMHasLabel#

**URL:** https://petsc.org/release/manualpages/DM/DMHasLabel/

**Contents:**
- DMHasLabel#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Determine whether the DM has a label of a given name

name - The label name

hasLabel - PETSC_TRUE if the label is present

DM Basics, DM, DMLabel, DMGetLabel(), DMGetLabelByNum(), DMCreateLabel(), DMGetLabelValue(), DMSetLabelValue(), DMGetStratumIS()

src/dm/interface/dm.c

src/dm/impls/plex/tutorials/ex10.c src/snes/tutorials/ex12.c src/snes/tutorials/ex8.c src/ts/tutorials/ex48.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMHasLabel(DM dm, const char name[], PetscBool *hasLabel)
```

Example 2 (unknown):
```unknown
DMGetLabel()
```

Example 3 (unknown):
```unknown
DMGetLabelByNum()
```

Example 4 (unknown):
```unknown
DMCreateLabel()
```

---

## DMHasNamedGlobalVector#

**URL:** https://petsc.org/release/manualpages/DM/DMHasNamedGlobalVector/

**Contents:**
- DMHasNamedGlobalVector#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

check for a named, persistent global vector created with DMGetNamedGlobalVector()

dm - DM to hold named vectors

name - unique name for Vec

exists - true if the vector was previously created

DM, DMGetNamedGlobalVector(), DMRestoreNamedLocalVector(), DMClearNamedGlobalVectors()

src/dm/interface/dmget.c

src/ts/tutorials/ex30.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMGetNamedGlobalVector()
```

Example 2 (unknown):
```unknown
#include "petscdm.h" 
PetscErrorCode DMHasNamedGlobalVector(DM dm, const char *name, PetscBool *exists)
```

Example 3 (unknown):
```unknown
DMGetNamedGlobalVector()
```

Example 4 (unknown):
```unknown
DMRestoreNamedLocalVector()
```

---

## DMHasNamedLocalVector#

**URL:** https://petsc.org/release/manualpages/DM/DMHasNamedLocalVector/

**Contents:**
- DMHasNamedLocalVector#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

check for a named, persistent local vector created with DMGetNamedLocalVector()

dm - DM to hold named vectors

name - unique name for Vec

exists - true if the vector was previously created

If a Vec with the given name does not exist, it is created.

DM, DMGetNamedGlobalVector(), DMRestoreNamedLocalVector(), DMClearNamedLocalVectors()

src/dm/interface/dmget.c

src/ts/tutorials/ex30.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMGetNamedLocalVector()
```

Example 2 (unknown):
```unknown
#include "petscdm.h" 
PetscErrorCode DMHasNamedLocalVector(DM dm, const char *name, PetscBool *exists)
```

Example 3 (unknown):
```unknown
DMGetNamedGlobalVector()
```

Example 4 (unknown):
```unknown
DMRestoreNamedLocalVector()
```

---

## DMHasVariableBounds#

**URL:** https://petsc.org/release/manualpages/DM/DMHasVariableBounds/

**Contents:**
- DMHasVariableBounds#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

does the DM object have a variable bounds function?

dm - the DM object to destroy

flg - PETSC_TRUE if the variable bounds function exists

DM Basics, DM, DMComputeVariableBounds(), DMView(), DMCreateGlobalVector(), DMCreateInterpolation(), DMCreateColoring(), DMCreateMatrix(), DMCreateMassMatrix(), DMGetApplicationContext()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMHasVariableBounds(DM dm, PetscBool *flg)
```

Example 2 (unknown):
```unknown
DMComputeVariableBounds()
```

Example 3 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 4 (unknown):
```unknown
DMCreateInterpolation()
```

---

## DMInitializePackage#

**URL:** https://petsc.org/release/manualpages/DM/DMInitializePackage/

**Contents:**
- DMInitializePackage#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#

This function initializes everything in the DM package. It is called from PetscDLLibraryRegister_petscdm() when using dynamic libraries, and on the first call to DMCreate() or similar routines when using shared or static libraries.

This function never needs to be called by PETSc users.

src/dm/interface/dlregisdmdm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDLLibraryRegister_petscdm()
```

Example 2 (unknown):
```unknown
PetscErrorCode DMInitializePackage(void)
```

Example 3 (unknown):
```unknown
PetscInitialize()
```

---

## DMInterpolateSolution#

**URL:** https://petsc.org/release/manualpages/DM/DMInterpolateSolution/

**Contents:**
- DMInterpolateSolution#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#
- Implementations#

Interpolates a solution from a coarse mesh to a fine mesh.

interp - (optional) the matrix computed by DMCreateInterpolation(). Implementations may not need this, but if it is available it can avoid some recomputation. If it is provided, MatInterpolate() will be used if the coarse DM does not have a specialized implementation.

coarseSol - solution on the coarse mesh

fineSol - the interpolation of coarseSol to the fine mesh

This function exists because the interpolation of a solution vector between meshes is not always a linear map. For example, if a boundary value problem has an inhomogeneous Dirichlet boundary condition that is compressed out of the solution vector. Or if interpolation is inherently a nonlinear operation, such as a method using slope-limiting reconstruction.

This doesn’t just interpolate “solutions” so its API name is questionable.

DM Basics, DM, DMInterpolate(), DMCreateInterpolation()

src/dm/interface/dm.c

DMInterpolateSolution_Plex() in src/dm/impls/plex/plex.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMInterpolateSolution(DM coarse, DM fine, Mat interp, Vec coarseSol, Vec fineSol)
```

Example 2 (unknown):
```unknown
DMCreateInterpolation()
```

Example 3 (unknown):
```unknown
MatInterpolate()
```

Example 4 (unknown):
```unknown
DMInterpolate()
```

---

## DMInterpolate#

**URL:** https://petsc.org/release/manualpages/DM/DMInterpolate/

**Contents:**
- DMInterpolate#
- Synopsis#
- Input Parameters#
- Developer Note#
- See Also#
- Level#
- Location#

interpolates user-defined problem data attached to a DM to a finer DM by running hooks registered by DMRefineHookAdd()

Collective if any hooks are

coarse - coarser DM to use as a base

interp - interpolation matrix, apply using MatInterpolate()

fine - finer DM to update

This routine is called DMInterpolate() while the hook is called DMRefineHookAdd(). It would be better to have an an API with consistent terminology.

DM Basics, DM, DMRefineHookAdd(), MatInterpolate()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMRefineHookAdd()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMInterpolate(DM coarse, Mat interp, DM fine)
```

Example 3 (unknown):
```unknown
MatInterpolate()
```

Example 4 (unknown):
```unknown
DMInterpolate()
```

---

## DMInterpolationAddPoints#

**URL:** https://petsc.org/release/manualpages/DM/DMInterpolationAddPoints/

**Contents:**
- DMInterpolationAddPoints#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Add points at which we will interpolate the fields

n - the number of points

points - the coordinates for each point, an array of size n * dim

The input coordinate information is copied into the object.

DM Basics, DM, DMInterpolationInfo, DMInterpolationSetDim(), DMInterpolationEvaluate(), DMInterpolationCreate()

src/snes/utils/dm/dminterpolatesnes.c

src/ts/tutorials/ex77.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMInterpolationAddPoints(DMInterpolationInfo ctx, PetscInt n, PetscReal points[])
```

Example 2 (unknown):
```unknown
DMInterpolationInfo
```

Example 3 (unknown):
```unknown
DMInterpolationSetDim()
```

Example 4 (unknown):
```unknown
DMInterpolationEvaluate()
```

---

## DMInterpolationCreate#

**URL:** https://petsc.org/release/manualpages/DM/DMInterpolationCreate/

**Contents:**
- DMInterpolationCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Creates a DMInterpolationInfo context

comm - the communicator

The naming is incorrect, either the object should be named DMInterpolation or all the routines should begin with DMInterpolationInfo

DM Basics, DM, DMInterpolationInfo, DMInterpolationEvaluate(), DMInterpolationAddPoints(), DMInterpolationDestroy()

src/snes/utils/dm/dminterpolatesnes.c

src/ts/tutorials/ex77.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMInterpolationInfo
```

Example 2 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMInterpolationCreate(MPI_Comm comm, DMInterpolationInfo *ctx)
```

Example 3 (unknown):
```unknown
DMInterpolation
```

Example 4 (unknown):
```unknown
DMInterpolationInfo
```

---

## DMInterpolationDestroy#

**URL:** https://petsc.org/release/manualpages/DM/DMInterpolationDestroy/

**Contents:**
- DMInterpolationDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#

Destroys a DMInterpolationInfo context

DM Basics, DM, DMInterpolationInfo, DMInterpolationEvaluate(), DMInterpolationAddPoints(), DMInterpolationCreate()

src/snes/utils/dm/dminterpolatesnes.c

src/ts/tutorials/ex77.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMInterpolationInfo
```

Example 2 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMInterpolationDestroy(DMInterpolationInfo *ctx)
```

Example 3 (unknown):
```unknown
DMInterpolationInfo
```

Example 4 (unknown):
```unknown
DMInterpolationEvaluate()
```

---

## DMInterpolationEvaluate#

**URL:** https://petsc.org/release/manualpages/DM/DMInterpolationEvaluate/

**Contents:**
- DMInterpolationEvaluate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Using the input from dm and x, calculates interpolated field values at the interpolation points.

ctx - The DMInterpolationInfo context obtained with DMInterpolationCreate()

x - The local vector containing the field to be interpolated, can be created with DMCreateGlobalVector()

v - The vector containing the interpolated values, obtained with DMInterpolationGetVector()

DM Basics, DM, DMInterpolationInfo, DMInterpolationGetVector(), DMInterpolationAddPoints(), DMInterpolationCreate(), DMInterpolationGetCoordinates()

src/snes/utils/dm/dminterpolatesnes.c

src/ts/tutorials/ex77.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMInterpolationEvaluate(DMInterpolationInfo ctx, DM dm, Vec x, Vec v)
```

Example 2 (unknown):
```unknown
DMInterpolationInfo
```

Example 3 (unknown):
```unknown
DMInterpolationCreate()
```

Example 4 (unknown):
```unknown
DMCreateGlobalVector()
```

---

## DMInterpolationGetCoordinates#

**URL:** https://petsc.org/release/manualpages/DM/DMInterpolationGetCoordinates/

**Contents:**
- DMInterpolationGetCoordinates#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets a Vec with the coordinates of each interpolation point

coordinates - the coordinates of interpolation points

The local vector entries correspond to interpolation points lying on this process, according to the associated DM. This is a borrowed vector that the user should not destroy.

DM Basics, DM, DMInterpolationInfo, DMInterpolationEvaluate(), DMInterpolationAddPoints(), DMInterpolationCreate()

src/snes/utils/dm/dminterpolatesnes.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMInterpolationGetCoordinates(DMInterpolationInfo ctx, Vec *coordinates)
```

Example 2 (unknown):
```unknown
DMInterpolationInfo
```

Example 3 (unknown):
```unknown
DMInterpolationEvaluate()
```

Example 4 (unknown):
```unknown
DMInterpolationAddPoints()
```

---

## DMInterpolationGetDim#

**URL:** https://petsc.org/release/manualpages/DM/DMInterpolationGetDim/

**Contents:**
- DMInterpolationGetDim#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the spatial dimension for the interpolation context

dim - the spatial dimension

DM Basics, DM, DMInterpolationInfo, DMInterpolationSetDim(), DMInterpolationEvaluate(), DMInterpolationAddPoints()

src/snes/utils/dm/dminterpolatesnes.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMInterpolationGetDim(DMInterpolationInfo ctx, PetscInt *dim)
```

Example 2 (unknown):
```unknown
DMInterpolationInfo
```

Example 3 (unknown):
```unknown
DMInterpolationSetDim()
```

Example 4 (unknown):
```unknown
DMInterpolationEvaluate()
```

---

## DMInterpolationGetDof#

**URL:** https://petsc.org/release/manualpages/DM/DMInterpolationGetDof/

**Contents:**
- DMInterpolationGetDof#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the number of fields interpolated at a point for the interpolation context

dof - the number of fields

DM Basics, DM, DMInterpolationInfo, DMInterpolationSetDof(), DMInterpolationEvaluate(), DMInterpolationAddPoints()

src/snes/utils/dm/dminterpolatesnes.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMInterpolationGetDof(DMInterpolationInfo ctx, PetscInt *dof)
```

Example 2 (unknown):
```unknown
DMInterpolationInfo
```

Example 3 (unknown):
```unknown
DMInterpolationSetDof()
```

Example 4 (unknown):
```unknown
DMInterpolationEvaluate()
```

---

## DMInterpolationGetVector#

**URL:** https://petsc.org/release/manualpages/DM/DMInterpolationGetVector/

**Contents:**
- DMInterpolationGetVector#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets a Vec which can hold all the interpolated field values

v - a vector capable of holding the interpolated field values

This vector should be returned using DMInterpolationRestoreVector().

DM Basics, DM, DMInterpolationInfo, DMInterpolationRestoreVector(), DMInterpolationEvaluate(), DMInterpolationAddPoints(), DMInterpolationCreate()

src/snes/utils/dm/dminterpolatesnes.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMInterpolationGetVector(DMInterpolationInfo ctx, Vec *v)
```

Example 2 (unknown):
```unknown
DMInterpolationRestoreVector()
```

Example 3 (unknown):
```unknown
DMInterpolationInfo
```

Example 4 (unknown):
```unknown
DMInterpolationRestoreVector()
```

---

## DMInterpolationInfo#

**URL:** https://petsc.org/release/manualpages/DM/DMInterpolationInfo/

**Contents:**
- DMInterpolationInfo#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#

Pointer to a structure for holding information about interpolation on a mesh

DM Basics, DM, DMInterpolationCreate(), DMInterpolationEvaluate(), DMInterpolationAddPoints()

src/ts/tutorials/ex77.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
comm     - The communicator
dim      - The spatial dimension of points
nInput   - The number of input points
points[] - The input point coordinates
cells[]  - The cell containing each point
n        - The number of local points
coords   - The point coordinates
dof      - The number of components to interpolate
```

Example 2 (unknown):
```unknown
DMInterpolationCreate()
```

Example 3 (unknown):
```unknown
DMInterpolationEvaluate()
```

Example 4 (unknown):
```unknown
DMInterpolationAddPoints()
```

---

## DMInterpolationRestoreVector#

**URL:** https://petsc.org/release/manualpages/DM/DMInterpolationRestoreVector/

**Contents:**
- DMInterpolationRestoreVector#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Returns a Vec which can hold all the interpolated field values

v - a vector capable of holding the interpolated field values

DM Basics, DM, DMInterpolationInfo, DMInterpolationGetVector(), DMInterpolationEvaluate(), DMInterpolationAddPoints(), DMInterpolationCreate()

src/snes/utils/dm/dminterpolatesnes.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMInterpolationRestoreVector(DMInterpolationInfo ctx, Vec *v)
```

Example 2 (unknown):
```unknown
DMInterpolationInfo
```

Example 3 (unknown):
```unknown
DMInterpolationGetVector()
```

Example 4 (unknown):
```unknown
DMInterpolationEvaluate()
```

---

## DMInterpolationSetDim#

**URL:** https://petsc.org/release/manualpages/DM/DMInterpolationSetDim/

**Contents:**
- DMInterpolationSetDim#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the spatial dimension for the interpolation context

dim - the spatial dimension

DM Basics, DM, DMInterpolationInfo, DMInterpolationGetDim(), DMInterpolationEvaluate(), DMInterpolationAddPoints()

src/snes/utils/dm/dminterpolatesnes.c

src/ts/tutorials/ex77.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMInterpolationSetDim(DMInterpolationInfo ctx, PetscInt dim)
```

Example 2 (unknown):
```unknown
DMInterpolationInfo
```

Example 3 (unknown):
```unknown
DMInterpolationGetDim()
```

Example 4 (unknown):
```unknown
DMInterpolationEvaluate()
```

---

## DMInterpolationSetDof#

**URL:** https://petsc.org/release/manualpages/DM/DMInterpolationSetDof/

**Contents:**
- DMInterpolationSetDof#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the number of fields interpolated at a point for the interpolation context

dof - the number of fields

DM Basics, DM, DMInterpolationInfo, DMInterpolationGetDof(), DMInterpolationEvaluate(), DMInterpolationAddPoints()

src/snes/utils/dm/dminterpolatesnes.c

src/ts/tutorials/ex77.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMInterpolationSetDof(DMInterpolationInfo ctx, PetscInt dof)
```

Example 2 (unknown):
```unknown
DMInterpolationInfo
```

Example 3 (unknown):
```unknown
DMInterpolationGetDof()
```

Example 4 (unknown):
```unknown
DMInterpolationEvaluate()
```

---

## DMInterpolationSetUp#

**URL:** https://petsc.org/release/manualpages/DM/DMInterpolationSetUp/

**Contents:**
- DMInterpolationSetUp#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Compute spatial indices for point location during interpolation

dm - the DM for the function space used for interpolation

redundantPoints - If PETSC_TRUE, all processes are passing in the same array of points. Otherwise, points need to be communicated among processes.

ignoreOutsideDomain - If PETSC_TRUE, ignore points outside the domain, otherwise return an error

DM Basics, DM, DMInterpolationInfo, DMInterpolationEvaluate(), DMInterpolationAddPoints(), DMInterpolationCreate()

src/snes/utils/dm/dminterpolatesnes.c

src/ts/tutorials/ex77.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmplex.h" 
#include "petscsnes.h"   
PetscErrorCode DMInterpolationSetUp(DMInterpolationInfo ctx, DM dm, PetscBool redundantPoints, PetscBool ignoreOutsideDomain)
```

Example 2 (unknown):
```unknown
DMInterpolationInfo
```

Example 3 (unknown):
```unknown
DMInterpolationEvaluate()
```

Example 4 (unknown):
```unknown
DMInterpolationAddPoints()
```

---

## DMIsBoundaryPoint#

**URL:** https://petsc.org/release/manualpages/DM/DMIsBoundaryPoint/

**Contents:**
- DMIsBoundaryPoint#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Determine whether a mesh point lies on a DM boundary

point - the mesh point number

isBd - PETSC_TRUE if point belongs to any boundary label registered on the DM

DM Basics, DM, DMLabel, DMAddBoundary(), PetscDSGetBoundary()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMIsBoundaryPoint(DM dm, PetscInt point, PetscBool *isBd)
```

Example 2 (unknown):
```unknown
DMAddBoundary()
```

Example 3 (unknown):
```unknown
PetscDSGetBoundary()
```

---

## DMLabelType#

**URL:** https://petsc.org/release/manualpages/DM/DMLabelType/

**Contents:**
- DMLabelType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

String name identifying a DMLabel implementation

DMLABELCONCRETE - the default in-memory DMLabel that stores point-to-value mappings explicitly

DMLABELEPHEMERAL - a DMLabel whose values are computed on demand from another DMLabel and a transformation, without storing them

DMLabel, DMLabelSetType(), DMLabelGetType(), DMLabelCreate()

include/petscdmlabeltypes.h

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef const char *DMLabelType;
#define DMLABELCONCRETE  "concrete"
#define DMLABELEPHEMERAL "ephemeral"
```

Example 2 (unknown):
```unknown
DMLABELCONCRETE
```

Example 3 (unknown):
```unknown
DMLABELEPHEMERAL
```

Example 4 (unknown):
```unknown
DMLabelSetType()
```

---

## DMLabel#

**URL:** https://petsc.org/release/manualpages/DM/DMLabel/

**Contents:**
- DMLabel#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Object which encapsulates a subset of the mesh from a DM

A label consists of a set of points on a DM

DM Basics, DM, DMPlexCreate(), DMLabelCreate(), DMLabelView(), DMLabelDestroy(), DMPlexCreateLabelField(), DMLabelGetDefaultValue(), DMLabelSetDefaultValue(), DMLabelDuplicate(), DMLabelGetValue(), DMLabelSetValue(), DMLabelAddStratum(), DMLabelAddStrata(), DMLabelInsertIS(), DMLabelGetNumValues(), DMLabelGetValueIS(), DMLabelGetStratumSize(), DMLabelComputeIndex(), DMLabelDestroyIndex(), DMLabelDistribute(), DMLabelConvertToSection()

include/petscdmlabeltypes.h

src/snes/tutorials/ex71.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex26.c src/snes/tutorials/ex17.c src/snes/tutorials/ex8.c src/snes/tutorials/ex23.c src/snes/tutorials/ex64.c src/snes/tutorials/ex62.c

_p_DMLabel in include/petsc/private/dmlabelimpl.h

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_DMLabel *DMLabel;
```

Example 2 (unknown):
```unknown
DMPlexCreate()
```

Example 3 (unknown):
```unknown
DMLabelCreate()
```

Example 4 (unknown):
```unknown
DMLabelView()
```

---

## DMLoad#

**URL:** https://petsc.org/release/manualpages/DM/DMLoad/

**Contents:**
- DMLoad#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Loads a DM that has been stored in binary with DMView().

newdm - the newly loaded DM, this needs to have been created with DMCreate() or some related function before a call to DMLoad().

viewer - binary file viewer, obtained from PetscViewerBinaryOpen() or PETSCVIEWERHDF5 file viewer, obtained from PetscViewerHDF5Open()

The type is determined by the data in the file, any type set into the DM before this call is ignored.

Using PETSCVIEWERHDF5 type with PETSC_VIEWER_HDF5_PETSC format, one can save multiple DMPLEX meshes in a single HDF5 file. This in turn requires one to name the DMPLEX object with PetscObjectSetName() before saving it with DMView() and before loading it with DMLoad() for identification of the mesh object.

DM Basics, DM, PetscViewerBinaryOpen(), DMView(), MatLoad(), VecLoad()

src/dm/interface/dm.c

src/dm/impls/plex/tutorials/ex5.c

DMLoad_DA() in src/dm/impls/da/dacreate.c DMLoad_Plex() in src/dm/impls/plex/plex.c DMLoad_Shell() in src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMLoad(DM newdm, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscViewerBinaryOpen()
```

Example 3 (unknown):
```unknown
PETSCVIEWERHDF5
```

Example 4 (unknown):
```unknown
PetscViewerHDF5Open()
```

---

## DMLocalizeCoordinates#

**URL:** https://petsc.org/release/manualpages/DM/DMLocalizeCoordinates/

**Contents:**
- DMLocalizeCoordinates#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#

If a mesh is periodic, create local coordinates for cells having periodic faces

DM, DMSetPeriodicity(), DMLocalizeCoordinate(), DMLocalizeAddCoordinate()

src/dm/interface/dmperiodicity.c

src/snes/tutorials/ex11.c src/ts/tutorials/ex30.c src/ts/tutorials/ex18.c src/dm/impls/forest/tutorials/ex1.c src/ts/tutorials/ex48.c src/dm/impls/plex/tutorials/ex8.c src/dm/impls/plex/tutorials/ex10.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMLocalizeCoordinates(DM dm)
```

Example 2 (unknown):
```unknown
DMSetPeriodicity()
```

Example 3 (unknown):
```unknown
DMLocalizeCoordinate()
```

Example 4 (unknown):
```unknown
DMLocalizeAddCoordinate()
```

---

## DMLocalizeCoordinate#

**URL:** https://petsc.org/release/manualpages/DM/DMLocalizeCoordinate/

**Contents:**
- DMLocalizeCoordinate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

If a mesh is periodic (a torus with lengths L_i, some of which can be infinite), project the coordinate onto [0, L_i) in each dimension.

in - The input coordinate point (dim numbers)

endpoint - Include the endpoint L_i

out - The localized coordinate point (dim numbers)

DM, DMLocalizeCoordinates(), DMLocalizeAddCoordinate()

src/dm/interface/dmperiodicity.c

src/ts/tutorials/ex18.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMLocalizeCoordinate(DM dm, const PetscScalar in[], PetscBool endpoint, PetscScalar out[])
```

Example 2 (unknown):
```unknown
DMLocalizeCoordinates()
```

Example 3 (unknown):
```unknown
DMLocalizeAddCoordinate()
```

---

## DMLocalToGlobalBeginDefaultShell#

**URL:** https://petsc.org/release/manualpages/DM/DMLocalToGlobalBeginDefaultShell/

**Contents:**
- DMLocalToGlobalBeginDefaultShell#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Uses the LocalToGlobal VecScatter context set by the user to begin a local to global scatter Collective

This is not normally called directly by user code, generally user code calls DMLocalToGlobalBegin() and DMLocalToGlobalEnd(). If the user provides their own custom routines to DMShellSetLocalToGlobal() then those routines might have reason to call this function.

DM, DMSHELL, DMLocalToGlobalEndDefaultShell()

src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMLocalToGlobalBeginDefaultShell(DM dm, Vec l, InsertMode mode, Vec g)
```

Example 2 (unknown):
```unknown
DMLocalToGlobalBegin()
```

Example 3 (unknown):
```unknown
DMLocalToGlobalEnd()
```

Example 4 (unknown):
```unknown
DMShellSetLocalToGlobal()
```

---

## DMLocalToGlobalBegin#

**URL:** https://petsc.org/release/manualpages/DM/DMLocalToGlobalBegin/

**Contents:**
- DMLocalToGlobalBegin#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

begins updating global vectors from local vectors

Neighbor-wise Collective

mode - if INSERT_VALUES then no parallel communication is used, if ADD_VALUES then all ghost points from the same base point accumulate into that base point.

g - the global vector

In the ADD_VALUES case you normally would zero the receiving vector before beginning this operation.

INSERT_VALUES is not supported for DMDA, in that case simply compute the values directly into a global vector instead of a local one.

Use DMLocalToGlobalEnd() to complete the communication process.

DMLocalToGlobal() is a short form of DMLocalToGlobalBegin() and DMLocalToGlobalEnd()

DMLocalToGlobalHookAdd() may be used to provide additional operations that are performed during the update process.

DM Basics, DM, DMLocalToGlobal(), DMLocalToGlobalEnd(), DMCoarsen(), DMDestroy(), DMView(), DMCreateGlobalVector(), DMCreateInterpolation(), DMGlobalToLocal(), DMGlobalToLocalEnd(), DMGlobalToLocalBegin()

src/dm/interface/dm.c

src/snes/tutorials/ex55.c src/snes/tutorials/ex5.c src/ksp/ksp/tutorials/ex70.c src/snes/tutorials/ex35.c src/snes/tutorials/ex36.c src/ksp/ksp/tutorials/ex49.c src/snes/tutorials/ex19.c src/ksp/ksp/tutorials/ex43.c src/snes/tutorials/ex15.c src/snes/tutorials/ex7.c

DMLocalToGlobalBegin_Composite() in src/dm/impls/composite/pack.c DMLocalToGlobalBegin_DA() in src/dm/impls/da/dagtol.c DMLocalToGlobalBegin_Moab() in src/dm/impls/moab/dmmbvec.cxx DMLocalToGlobalBegin_Network() in src/dm/impls/network/network.c DMLocalToGlobalBegin_Redundant() in src/dm/impls/redundant/dmredundant.c DMLocalToGlobalBegin_Stag() in src/dm/impls/stag/stag.c DMLocalToGlobalBegin_Swarm() in src/dm/impls/swarm/swarm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMLocalToGlobalBegin(DM dm, Vec l, InsertMode mode, Vec g)
```

Example 2 (unknown):
```unknown
INSERT_VALUES
```

Example 3 (unknown):
```unknown
INSERT_VALUES is
```

Example 4 (unknown):
```unknown
DMLocalToGlobalEnd()
```

---

## DMLocalToGlobalEndDefaultShell#

**URL:** https://petsc.org/release/manualpages/DM/DMLocalToGlobalEndDefaultShell/

**Contents:**
- DMLocalToGlobalEndDefaultShell#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Uses the LocalToGlobal VecScatter context set by the user to end a local to global scatter Collective

DM, DMSHELL, DMLocalToGlobalBeginDefaultShell()

src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMLocalToGlobalEndDefaultShell(DM dm, Vec l, InsertMode mode, Vec g)
```

Example 2 (unknown):
```unknown
DMLocalToGlobalBeginDefaultShell()
```

---

## DMLocalToGlobalEnd#

**URL:** https://petsc.org/release/manualpages/DM/DMLocalToGlobalEnd/

**Contents:**
- DMLocalToGlobalEnd#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

updates global vectors from local vectors

Neighbor-wise Collective

mode - INSERT_VALUES or ADD_VALUES

g - the global vector

See DMLocalToGlobalBegin() for full details

DM Basics, DM, DMLocalToGlobalBegin(), DMCoarsen(), DMDestroy(), DMView(), DMCreateGlobalVector(), DMCreateInterpolation(), DMGlobalToLocalEnd()

src/dm/interface/dm.c

src/snes/tutorials/ex55.c src/snes/tutorials/ex5.c src/ksp/ksp/tutorials/ex70.c src/snes/tutorials/ex35.c src/snes/tutorials/ex36.c src/ksp/ksp/tutorials/ex49.c src/snes/tutorials/ex19.c src/ksp/ksp/tutorials/ex43.c src/snes/tutorials/ex15.c src/snes/tutorials/ex7.c

DMLocalToGlobalEnd_Composite() in src/dm/impls/composite/pack.c DMLocalToGlobalEnd_DA() in src/dm/impls/da/dagtol.c DMLocalToGlobalEnd_Moab() in src/dm/impls/moab/dmmbvec.cxx DMLocalToGlobalEnd_Network() in src/dm/impls/network/network.c DMLocalToGlobalEnd_Redundant() in src/dm/impls/redundant/dmredundant.c DMLocalToGlobalEnd_Stag() in src/dm/impls/stag/stag.c DMLocalToGlobalEnd_Swarm() in src/dm/impls/swarm/swarm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMLocalToGlobalEnd(DM dm, Vec l, InsertMode mode, Vec g)
```

Example 2 (unknown):
```unknown
INSERT_VALUES
```

Example 3 (unknown):
```unknown
DMLocalToGlobalBegin()
```

Example 4 (unknown):
```unknown
DMLocalToGlobalBegin()
```

---

## DMLocalToGlobalHookAdd#

**URL:** https://petsc.org/release/manualpages/DM/DMLocalToGlobalHookAdd/

**Contents:**
- DMLocalToGlobalHookAdd#
- Synopsis#
- Input Parameters#
- Calling sequence of beginhook#
- Calling sequence of endhook#
- See Also#
- Level#
- Location#

adds a callback to be run when a local to global is called

beginhook - function to run at the beginning of DMLocalToGlobalBegin()

endhook - function to run after DMLocalToGlobalEnd() has completed

ctx - [optional] context for provide data for the hooks (may be NULL)

ctx - optional function context

ctx - optional function context

DM Basics, DM, DMLocalToGlobal(), DMRefineHookAdd(), DMGlobalToLocalHookAdd(), SNESFASGetInterpolation(), SNESFASGetInjection(), PetscObjectCompose(), PetscContainerCreate()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMLocalToGlobalHookAdd(DM dm, PetscErrorCode (*beginhook)(DM global, Vec l, InsertMode mode, Vec g, PetscCtx ctx), PetscErrorCode (*endhook)(DM global, Vec l, InsertMode mode, Vec g, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMLocalToGlobalBegin()
```

Example 3 (unknown):
```unknown
DMLocalToGlobalEnd()
```

Example 4 (unknown):
```unknown
DMLocalToGlobal()
```

---

## DMLocalToGlobal#

**URL:** https://petsc.org/release/manualpages/DM/DMLocalToGlobal/

**Contents:**
- DMLocalToGlobal#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

updates global vectors from local vectors

Neighbor-wise Collective

mode - if INSERT_VALUES then no parallel communication is used, if ADD_VALUES then all ghost points from the same base point accumulate into that base point.

g - the global vector

The communication involved in this update can be overlapped with computation by using DMLocalToGlobalBegin() and DMLocalToGlobalEnd().

In the ADD_VALUES case you normally would zero the receiving vector before beginning this operation.

INSERT_VALUES is not supported for DMDA; in that case simply compute the values directly into a global vector instead of a local one.

Use DMLocalToGlobalHookAdd() to add additional operations that are performed on the data during the update process

DM Basics, DM, DMLocalToGlobalBegin(), DMLocalToGlobalEnd(), DMCoarsen(), DMDestroy(), DMView(), DMCreateGlobalVector(), DMCreateInterpolation(), DMGlobalToLocal(), DMGlobalToLocalEnd(), DMGlobalToLocalBegin(), DMLocalToGlobalHookAdd(), DMGlobaToLocallHookAdd()

src/dm/interface/dm.c

src/snes/tutorials/ex11.c src/snes/tutorials/ex16.c src/dm/impls/stag/tutorials/ex4.c src/dm/impls/stag/tutorials/ex1.c src/dm/tutorials/ex2.c src/dm/impls/stag/tutorials/ex6.c src/dm/impls/stag/tutorials/ex3.c src/dm/impls/stag/tutorials/ex2.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMLocalToGlobal(DM dm, Vec l, InsertMode mode, Vec g)
```

Example 2 (unknown):
```unknown
INSERT_VALUES
```

Example 3 (unknown):
```unknown
DMLocalToGlobalBegin()
```

Example 4 (unknown):
```unknown
DMLocalToGlobalEnd()
```

---

## DMLocalToLocalBeginDefaultShell#

**URL:** https://petsc.org/release/manualpages/DM/DMLocalToLocalBeginDefaultShell/

**Contents:**
- DMLocalToLocalBeginDefaultShell#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Uses the LocalToLocal VecScatter context set by the user to begin a local to local scatter Collective

g - the original local vector

l - the local vector with correct ghost values

This is not normally called directly by user code, generally user code calls DMLocalToLocalBegin() and DMLocalToLocalEnd(). If the user provides their own custom routines to DMShellSetLocalToLocal() then those routines might have reason to call this function.

DM, DMSHELL, DMLocalToLocalEndDefaultShell()

src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMLocalToLocalBeginDefaultShell(DM dm, Vec g, InsertMode mode, Vec l)
```

Example 2 (unknown):
```unknown
DMLocalToLocalBegin()
```

Example 3 (unknown):
```unknown
DMLocalToLocalEnd()
```

Example 4 (unknown):
```unknown
DMShellSetLocalToLocal()
```

---

## DMLocalToLocalBegin#

**URL:** https://petsc.org/release/manualpages/DM/DMLocalToLocalBegin/

**Contents:**
- DMLocalToLocalBegin#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Begins the process of mapping values from a local vector (that include ghost points that contain irrelevant values) to another local vector where the ghost points in the second are set correctly from values on other MPI ranks.

Neighbor-wise Collective

g - the original local vector

mode - one of INSERT_VALUES or ADD_VALUES

l - the local vector with correct ghost values

Must be followed by DMLocalToLocalEnd().

DM Basics, DM, DMLocalToLocalEnd(), DMCoarsen(), DMDestroy(), DMView(), DMCreateLocalVector(), DMCreateGlobalVector(), DMCreateInterpolation(), DMGlobalToLocalEnd(), DMLocalToGlobalBegin()

src/dm/interface/dm.c

src/dm/tutorials/ex13f90.F90

DMLocalToLocalBegin_Composite() in src/dm/impls/composite/pack.c DMLocalToLocalBegin_DA() in src/dm/impls/da/daltol.c DMLocalToLocalBegin_Stag() in src/dm/impls/stag/stag.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMLocalToLocalBegin(DM dm, Vec g, InsertMode mode, Vec l)
```

Example 2 (unknown):
```unknown
INSERT_VALUES
```

Example 3 (unknown):
```unknown
DMLocalToLocalEnd()
```

Example 4 (unknown):
```unknown
DMLocalToLocalEnd()
```

---

## DMLocalToLocalEndDefaultShell#

**URL:** https://petsc.org/release/manualpages/DM/DMLocalToLocalEndDefaultShell/

**Contents:**
- DMLocalToLocalEndDefaultShell#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Uses the LocalToLocal VecScatter context set by the user to end a local to local scatter Collective

g - the original local vector

l - the local vector with correct ghost values

DM, DMSHELL, DMLocalToLocalBeginDefaultShell()

src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMLocalToLocalEndDefaultShell(DM dm, Vec g, InsertMode mode, Vec l)
```

Example 2 (unknown):
```unknown
DMLocalToLocalBeginDefaultShell()
```

---

## DMLocalToLocalEnd#

**URL:** https://petsc.org/release/manualpages/DM/DMLocalToLocalEnd/

**Contents:**
- DMLocalToLocalEnd#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Maps from a local vector to another local vector where the ghost points in the second are set correctly. Must be preceded by DMLocalToLocalBegin().

Neighbor-wise Collective

g - the original local vector

mode - one of INSERT_VALUES or ADD_VALUES

l - the local vector with correct ghost values

DM Basics, DM, DMLocalToLocalBegin(), DMCoarsen(), DMDestroy(), DMView(), DMCreateLocalVector(), DMCreateGlobalVector(), DMCreateInterpolation(), DMGlobalToLocalEnd(), DMLocalToGlobalBegin()

src/dm/interface/dm.c

src/dm/tutorials/ex13f90.F90

DMLocalToLocalEnd_Composite() in src/dm/impls/composite/pack.c DMLocalToLocalEnd_DA() in src/dm/impls/da/daltol.c DMLocalToLocalEnd_Stag() in src/dm/impls/stag/stag.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMLocalToLocalBegin()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMLocalToLocalEnd(DM dm, Vec g, InsertMode mode, Vec l)
```

Example 3 (unknown):
```unknown
INSERT_VALUES
```

Example 4 (unknown):
```unknown
DMLocalToLocalBegin()
```

---

## DMLocatePoints#

**URL:** https://petsc.org/release/manualpages/DM/DMLocatePoints/

**Contents:**
- DMLocatePoints#
- Synopsis#
- Input Parameters#
- Input/Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Locate the points in v in the mesh and return a PetscSF of the containing cells

ltype - The type of point location, e.g. DM_POINTLOCATION_NONE or DM_POINTLOCATION_NEAREST

v - The Vec of points, on output contains the nearest mesh points to the given points if DM_POINTLOCATION_NEAREST is used

cellSF - Points to either NULL, or a PetscSF with guesses for which cells contain each point; on output, the PetscSF containing the MPI ranks and local indices of the containing points

To do a search of the local cells of the mesh, v should have PETSC_COMM_SELF as its communicator. To do a search of all the cells in the distributed mesh, v should have the same MPI communicator as dm.

Points will only be located in owned cells, not overlap cells arising from DMPlexDistribute() or other overlapping distributions.

If *cellSF is NULL on input, a PetscSF will be created. If *cellSF is not NULL on input, it should point to an existing PetscSF, whose graph will be used as initial guesses.

An array that maps each point to its containing cell can be obtained with

Where cells[i].rank is the MPI rank of the process owning the cell containing point found[i] (or i if found == NULL), and cells[i].index is the index of the cell in its MPI process’ local numbering. This rank is in the communicator for v, so if v is on PETSC_COMM_SELF then the rank will always be 0.

DM, DMSetCoordinates(), DMSetCoordinatesLocal(), DMGetCoordinates(), DMGetCoordinatesLocal(), DMPointLocationType

src/dm/interface/dmcoordinates.c

DMLocatePoints_Plex() in src/dm/impls/plex/plexgeometry.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMLocatePoints(DM dm, Vec v, DMPointLocationType ltype, PetscSF *cellSF)
```

Example 2 (unknown):
```unknown
DM_POINTLOCATION_NONE
```

Example 3 (unknown):
```unknown
DM_POINTLOCATION_NEAREST
```

Example 4 (unknown):
```unknown
DM_POINTLOCATION_NEAREST
```

---

## DMMonitorCancel#

**URL:** https://petsc.org/release/manualpages/DM/DMMonitorCancel/

**Contents:**
- DMMonitorCancel#
- Synopsis#
- Input Parameter#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Clears all the monitor functions for a DM object.

-dm_monitor_cancel - cancels all monitors that have been hardwired into a code by calls to DMonitorSet(), but does not cancel those set via the options database

There is no way to clear one specific monitor from a DM object.

DM Basics, DM, DMMonitorSet(), DMMonitorSetFromOptions(), DMMonitor()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMMonitorCancel(DM dm)
```

Example 2 (unknown):
```unknown
DMonitorSet()
```

Example 3 (unknown):
```unknown
DMMonitorSet()
```

Example 4 (unknown):
```unknown
DMMonitorSetFromOptions()
```

---

## DMMonitorSetFromOptions#

**URL:** https://petsc.org/release/manualpages/DM/DMMonitorSetFromOptions/

**Contents:**
- DMMonitorSetFromOptions#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Calling sequence of monitor#
- Calling sequence of monitorsetup#
- See Also#
- Level#
- Location#

Sets a monitor function and viewer appropriate for the type indicated by the user

dm - DM object you wish to monitor

name - the monitor type one is seeking

help - message indicating what monitoring is done

manual - manual page for the monitor

monitor - the monitor function, this must use a PetscViewerFormat as its context

monitorsetup - a function that is called once ONLY if the user selected this monitor that may set additional features of the DM or PetscViewer objects

flg - Flag set if the monitor was created

dm - the DM to be monitored

ctx - monitor context

dm - the DM to be monitored

vf - the PetscViewer and format to be used by the monitor

DM Basics, DM, PetscOptionsCreateViewer(), PetscOptionsGetReal(), PetscOptionsHasName(), PetscOptionsGetString(), PetscOptionsGetIntArray(), PetscOptionsGetRealArray(), PetscOptionsBool(), PetscOptionsInt(), PetscOptionsString(), PetscOptionsReal(), PetscOptionsName(), PetscOptionsBegin(), PetscOptionsEnd(), PetscOptionsHeadBegin(), PetscOptionsStringArray(), PetscOptionsRealArray(), PetscOptionsScalar(), PetscOptionsBoolGroupBegin(), PetscOptionsBoolGroup(), PetscOptionsBoolGroupEnd(), PetscOptionsFList(), PetscOptionsEList(), DMMonitor(), DMMonitorSet()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMMonitorSetFromOptions(DM dm, const char name[], const char help[], const char manual[], PetscErrorCode (*monitor)(DM dm, PetscCtx ctx), PetscErrorCode (*monitorsetup)(DM dm, PetscViewerAndFormat *vf), PetscBool *flg)
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
monitorsetup
```

---

## DMMonitorSet#

**URL:** https://petsc.org/release/manualpages/DM/DMMonitorSet/

**Contents:**
- DMMonitorSet#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- Fortran Note#
- Developer Note#
- See Also#
- Level#
- Location#

Sets an additional monitor function that is to be used after a solve to monitor discretization performance.

f - the monitor function

mctx - [optional] context for private data for the monitor routine (use NULL if no context is desired)

monitordestroy - [optional] routine that frees monitor context (may be NULL), see PetscCtxDestroyFn for the calling sequence

-dm_monitor_cancel - cancels all monitors that have been hardwired into a code by calls to DMMonitorSet(), but does not cancel those set via the options database.

Several different monitoring routines may be set by calling DMMonitorSet() multiple times or with DMMonitorSetFromOptions(); all will be called in the order in which they were set.

Only a single monitor function can be set for each DM object

This API has a generic name but seems specific to a very particular aspect of the use of DM

DM Basics, DM, DMMonitorCancel(), DMMonitorSetFromOptions(), DMMonitor(), PetscCtxDestroyFn

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMMonitorSet(DM dm, PetscErrorCode (*f)(DM, void *), void *mctx, PetscCtxDestroyFn *monitordestroy)
```

Example 2 (unknown):
```unknown
PetscCtxDestroyFn
```

Example 3 (unknown):
```unknown
DMMonitorSet()
```

Example 4 (unknown):
```unknown
DMMonitorSet()
```

---

## DMMonitor#

**URL:** https://petsc.org/release/manualpages/DM/DMMonitor/

**Contents:**
- DMMonitor#
- Synopsis#
- Input Parameter#
- Developer Note#
- See Also#
- Level#
- Location#

runs the user provided monitor routines, if they exist

Note should indicate when during the life of the DM the monitor is run. It appears to be related to the discretization process seems rather specialized since some DM have no concept of discretization.

DM Basics, DM, DMMonitorSet(), DMMonitorSetFromOptions()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMMonitor(DM dm)
```

Example 2 (unknown):
```unknown
DMMonitorSet()
```

Example 3 (unknown):
```unknown
DMMonitorSetFromOptions()
```

---

## DMOutputSequenceLoad#

**URL:** https://petsc.org/release/manualpages/DM/DMOutputSequenceLoad/

**Contents:**
- DMOutputSequenceLoad#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

Retrieve the sequence value from a PetscViewer

viewer - The PetscViewer to get it from

name - The sequence name

num - The output sequence number

val - The output sequence value

This is intended for output that should appear in sequence, for instance a set of timesteps in an PETSCVIEWERHDF5 file, or a set of realizations of a stochastic system.

It is unclear at the user API level why a DM is needed as input

DM Basics, DM, DMGetOutputSequenceNumber(), DMSetOutputSequenceNumber(), VecView()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMOutputSequenceLoad(DM dm, PetscViewer viewer, const char name[], PetscInt num, PetscReal *val)
```

Example 3 (unknown):
```unknown
PetscViewer
```

Example 4 (unknown):
```unknown
PETSCVIEWERHDF5
```

---

## DMPlexTransformType#

**URL:** https://petsc.org/release/manualpages/DM/DMPlexTransformType/

**Contents:**
- DMPlexTransformType#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#

String with the name of a PETSc DMPlexTransformType

Summary of Unstructured Mesh Transformations for a table of available transformation types

Summary of Unstructured Mesh Transformations, DMPlex: Unstructured Grids, DMPlexTransformCreate(), DMPlexTransform, DMPlexTransformRegister()

include/petscdmplextransform.h

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMPlexTransformType
```

Example 2 (unknown):
```unknown
typedef const char *DMPlexTransformType;
#define DMPLEXREFINEREGULAR       "refine_regular"
#define DMPLEXREFINEALFELD        "refine_alfeld"
#define DMPLEXREFINEPOWELLSABIN   "refine_powell_sabin"
#define DMPLEXREFINEBOUNDARYLAYER "refine_boundary_layer"
#define DMPLEXREFINESBR           "refine_sbr"
#define DMPLEXREFINETOBOX         "refine_tobox"
#define DMPLEXREFINETOSIMPLEX     "refine_tosimplex"
#define DMPLEXREFINE1D            "refine_1d"
#define DMPLEXEXTRUDETYPE         "extrude"
#define DMPLEXCOHESIVEEXTRUDE     "cohesive_extrude"
#define DMPLEXTRANSFORMFILTER     "transform_filter"
```

Example 3 (unknown):
```unknown
DMPlexTransformCreate()
```

Example 4 (unknown):
```unknown
DMPlexTransform
```

---

## DMPointLocationType#

**URL:** https://petsc.org/release/manualpages/DM/DMPointLocationType/

**Contents:**
- DMPointLocationType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#
- Examples#

Describes the method to handle point location failure

DM_POINTLOCATION_NONE - return a negative cell number

DM_POINTLOCATION_NEAREST - the (approximate) nearest point in the mesh is used

DM_POINTLOCATION_REMOVE - returns values only for points which were located

DM Basics, DM, DMLocatePoints()

include/petscdmtypes.h

src/dm/tutorials/swarm_ex3.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  DM_POINTLOCATION_NONE,
  DM_POINTLOCATION_NEAREST,
  DM_POINTLOCATION_REMOVE
} DMPointLocationType;
```

Example 2 (unknown):
```unknown
DM_POINTLOCATION_NONE
```

Example 3 (unknown):
```unknown
DM_POINTLOCATION_NEAREST
```

Example 4 (unknown):
```unknown
DM_POINTLOCATION_REMOVE
```

---

## DMPolytopeGetOrientation#

**URL:** https://petsc.org/release/manualpages/DM/DMPolytopeGetOrientation/

**Contents:**
- DMPolytopeGetOrientation#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Determine an orientation (transformation) that takes the source face arrangement to the target face arrangement

ct - The DMPolytopeType

sourceCone - The source arrangement of faces

targetCone - The target arrangement of faces

ornt - The orientation (transformation) which will take the source arrangement to the target arrangement

This function is the same as DMPolytopeMatchOrientation() except it will generate an error if no suitable orientation can be found.

It is unclear why this function needs to exist since one can simply call DMPolytopeMatchOrientation() and error if none is found

DM Basics, DM, DMPolytopeType, DMPolytopeMatchOrientation(), DMPolytopeGetVertexOrientation(), DMPolytopeMatchVertexOrientation()

src/dm/interface/dm.c

src/dm/impls/plex/tutorials/ex11.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMPolytopeGetOrientation(DMPolytopeType ct, const PetscInt sourceCone[], const PetscInt targetCone[], PetscInt *ornt)
```

Example 2 (unknown):
```unknown
DMPolytopeType
```

Example 3 (unknown):
```unknown
DMPolytopeMatchOrientation()
```

Example 4 (unknown):
```unknown
DMPolytopeMatchOrientation()
```

---

## DMPolytopeGetVertexOrientation#

**URL:** https://petsc.org/release/manualpages/DM/DMPolytopeGetVertexOrientation/

**Contents:**
- DMPolytopeGetVertexOrientation#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

Determine an orientation (transformation) that takes the source vertex arrangement to the target vertex arrangement

ct - The DMPolytopeType

sourceCone - The source arrangement of vertices

targetCone - The target arrangement of vertices

ornt - The orientation (transformation) which will take the source arrangement to the target arrangement

This function is the same as DMPolytopeMatchVertexOrientation() except it errors if not orientation is possible.

It is unclear why this function needs to exist since one can simply call DMPolytopeMatchVertexOrientation() and error if none is found

DM Basics, DM, DMPolytopeType, DMPolytopeMatchVertexOrientation(), DMPolytopeGetOrientation()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMPolytopeGetVertexOrientation(DMPolytopeType ct, const PetscInt sourceCone[], const PetscInt targetCone[], PetscInt *ornt)
```

Example 2 (unknown):
```unknown
DMPolytopeType
```

Example 3 (unknown):
```unknown
DMPolytopeMatchVertexOrientation()
```

Example 4 (unknown):
```unknown
DMPolytopeMatchVertexOrientation()
```

---

## DMPolytopeInCellTest#

**URL:** https://petsc.org/release/manualpages/DM/DMPolytopeInCellTest/

**Contents:**
- DMPolytopeInCellTest#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Check whether a point lies inside the reference cell of given type

ct - The DMPolytopeType

point - Coordinates of the point

inside - Flag indicating whether the point is inside the reference cell of given type

DM Basics, DM, DMPolytopeType, DMLocatePoints()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMPolytopeInCellTest(DMPolytopeType ct, const PetscReal point[], PetscBool *inside)
```

Example 2 (unknown):
```unknown
DMPolytopeType
```

Example 3 (unknown):
```unknown
DMPolytopeType
```

Example 4 (unknown):
```unknown
DMLocatePoints()
```

---

## DMPolytopeMatchOrientation#

**URL:** https://petsc.org/release/manualpages/DM/DMPolytopeMatchOrientation/

**Contents:**
- DMPolytopeMatchOrientation#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Determine an orientation (transformation) that takes the source face arrangement to the target face arrangement

ct - The DMPolytopeType

sourceCone - The source arrangement of faces

targetCone - The target arrangement of faces

ornt - The orientation (transformation) which will take the source arrangement to the target arrangement

found - Flag indicating that a suitable orientation was found

An arrangement is a face order combined with an orientation for each face

Each orientation (transformation) is labeled with an integer from negative DMPolytopeTypeGetNumArrangements(ct)/2 to DMPolytopeTypeGetNumArrangements(ct)/2 that labels each arrangement (face ordering plus orientation for each face).

See DMPolytopeMatchVertexOrientation() to find a new vertex orientation that takes the source vertex arrangement to the target vertex arrangement

DM Basics, DM, DMPolytopeGetOrientation(), DMPolytopeMatchVertexOrientation(), DMPolytopeGetVertexOrientation()

src/dm/interface/dm.c

src/dm/impls/plex/tutorials/ex11.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMPolytopeMatchOrientation(DMPolytopeType ct, const PetscInt sourceCone[], const PetscInt targetCone[], PetscInt *ornt, PetscBool *found)
```

Example 2 (unknown):
```unknown
DMPolytopeType
```

Example 3 (unknown):
```unknown
DMPolytopeTypeGetNumArrangements(ct)
```

Example 4 (unknown):
```unknown
DMPolytopeTypeGetNumArrangements(ct)
```

---

## DMPolytopeMatchVertexOrientation#

**URL:** https://petsc.org/release/manualpages/DM/DMPolytopeMatchVertexOrientation/

**Contents:**
- DMPolytopeMatchVertexOrientation#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Determine an orientation (transformation) that takes the source vertex arrangement to the target vertex arrangement

ct - The DMPolytopeType

sourceVert - The source arrangement of vertices

targetVert - The target arrangement of vertices

ornt - The orientation (transformation) which will take the source arrangement to the target arrangement

found - Flag indicating that a suitable orientation was found

An arrangement is a vertex order

Each orientation (transformation) is labeled with an integer from negative DMPolytopeTypeGetNumArrangements(ct)/2 to DMPolytopeTypeGetNumArrangements(ct)/2 that labels each arrangement (vertex ordering).

See DMPolytopeMatchOrientation() to find a new face orientation that takes the source face arrangement to the target face arrangement

DM Basics, DM, DMPolytopeType, DMPolytopeGetOrientation(), DMPolytopeMatchOrientation(), DMPolytopeTypeGetNumVertices(), DMPolytopeTypeGetVertexArrangement()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMPolytopeMatchVertexOrientation(DMPolytopeType ct, const PetscInt sourceVert[], const PetscInt targetVert[], PetscInt *ornt, PetscBool *found)
```

Example 2 (unknown):
```unknown
DMPolytopeType
```

Example 3 (unknown):
```unknown
DMPolytopeTypeGetNumArrangements(ct)
```

Example 4 (unknown):
```unknown
DMPolytopeTypeGetNumArrangements(ct)
```

---

## DMPolytopeType#

**URL:** https://petsc.org/release/manualpages/DM/DMPolytopeType/

**Contents:**
- DMPolytopeType#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#
- Examples#
- Examples#
- Examples#

This describes the polytope represented by each cell.

While most operations only need the topology information in the DMPLEX, we must sometimes have the user specify a polytope. For instance, when interpolating from a cell-vertex mesh, the type of polytope can be ambiguous. Also, DMPLEX allows different symmetries of a prism cell with the same constituent points. Normally these types are automatically inferred and the user does not specify them.

DM Basics, DM, DMPlexComputeCellTypes()

include/petscdmtypes.h

src/dm/impls/plex/tutorials/ex11.c

src/dm/impls/plex/tutorials/ex11.c

src/dm/impls/plex/tutorials/ex11.c

src/snes/tutorials/ex11.c src/snes/tutorials/ex13.c src/snes/tutorials/ex20.c src/snes/tutorials/ex36.c src/snes/tutorials/ex26.c src/snes/tutorials/ex17.c src/snes/tutorials/ex27.c src/snes/tutorials/ex69.c src/snes/tutorials/ex34.c src/snes/tutorials/ex24.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  DM_POLYTOPE_POINT,
  DM_POLYTOPE_SEGMENT,
  DM_POLYTOPE_POINT_PRISM_TENSOR,
  DM_POLYTOPE_TRIANGLE,
  DM_POLYTOPE_QUADRILATERAL,
  DM_POLYTOPE_SEG_PRISM_TENSOR,
  DM_POLYTOPE_TETRAHEDRON,
  DM_POLYTOPE_HEXAHEDRON,
  DM_POLYTOPE_TRI_PRISM,
  DM_POLYTOPE_TRI_PRISM_TENSOR,
  DM_POLYTOPE_QUAD_PRISM_TENSOR,
  DM_POLYTOPE_PYRAMID,
  DM_POLYTOPE_FV_GHOST,
  DM_POLYTOPE_INTERIOR_GHOST,
  DM_POLYTOPE_UNKNOWN,
  DM_POLYTOPE_UNKNOWN_CELL,
  DM_POLYTOPE_UNKNOWN_FACE,
  DM_NUM_POLYTOPES
} DMPolytopeType;
```

Example 2 (unknown):
```unknown
DMPlexComputeCellTypes()
```

---

## DMPrintCellIndices#

**URL:** https://petsc.org/release/manualpages/DM/DMPrintCellIndices/

**Contents:**
- DMPrintCellIndices#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Print an integer array of per-cell indices to PETSC_COMM_SELF

name - the label to print with the cell (typically the element or field name)

len - the length of x

x - the array of integer indices

DM Basics, DM, DMPrintCellVector(), DMPrintCellVectorReal(), DMPrintCellMatrix(), DMPrintLocalVec()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_COMM_SELF
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMPrintCellIndices(PetscInt c, const char name[], PetscInt len, const PetscInt x[])
```

Example 3 (unknown):
```unknown
DMPrintCellVector()
```

Example 4 (unknown):
```unknown
DMPrintCellVectorReal()
```

---

## DMPrintCellMatrix#

**URL:** https://petsc.org/release/manualpages/DM/DMPrintCellMatrix/

**Contents:**
- DMPrintCellMatrix#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Print a scalar array representing a per-cell matrix to PETSC_COMM_SELF

name - the label to print with the cell (typically the element or field name)

rows - number of rows in the matrix

cols - number of columns in the matrix

A - the row-major array of PetscScalar matrix entries

Only the real part of each entry is printed.

DM Basics, DM, DMPrintCellIndices(), DMPrintCellVector(), DMPrintCellVectorReal(), DMPrintLocalVec()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_COMM_SELF
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMPrintCellMatrix(PetscInt c, const char name[], PetscInt rows, PetscInt cols, const PetscScalar A[])
```

Example 3 (unknown):
```unknown
PetscScalar
```

Example 4 (unknown):
```unknown
DMPrintCellIndices()
```

---

## DMPrintCellVectorReal#

**URL:** https://petsc.org/release/manualpages/DM/DMPrintCellVectorReal/

**Contents:**
- DMPrintCellVectorReal#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Print a real array representing a per-cell vector to PETSC_COMM_SELF

name - the label to print with the cell (typically the element or field name)

len - the length of x

x - the array of PetscReal values

DM Basics, DM, DMPrintCellIndices(), DMPrintCellVector(), DMPrintCellMatrix(), DMPrintLocalVec()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_COMM_SELF
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMPrintCellVectorReal(PetscInt c, const char name[], PetscInt len, const PetscReal x[])
```

Example 3 (unknown):
```unknown
DMPrintCellIndices()
```

Example 4 (unknown):
```unknown
DMPrintCellVector()
```

---

## DMPrintCellVector#

**URL:** https://petsc.org/release/manualpages/DM/DMPrintCellVector/

**Contents:**
- DMPrintCellVector#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Print a scalar array representing a per-cell vector to PETSC_COMM_SELF

name - the label to print with the cell (typically the element or field name)

len - the length of x

x - the array of PetscScalar values

Only the real part of each entry is printed.

DM Basics, DM, DMPrintCellIndices(), DMPrintCellVectorReal(), DMPrintCellMatrix(), DMPrintLocalVec()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_COMM_SELF
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMPrintCellVector(PetscInt c, const char name[], PetscInt len, const PetscScalar x[])
```

Example 3 (unknown):
```unknown
PetscScalar
```

Example 4 (unknown):
```unknown
DMPrintCellIndices()
```

---

## DMPrintLocalVec#

**URL:** https://petsc.org/release/manualpages/DM/DMPrintLocalVec/

**Contents:**
- DMPrintLocalVec#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Print a Vec associated with a DM, filtering out very small entries

dm - the DM providing the communicator

name - a label printed before the vector values

tol - tolerance below which entries are filtered to zero using VecFilter()

Runs in parallel by wrapping the local portion of the vector in an MPI vector for viewing.

DM Basics, DM, DMPrintCellIndices(), DMPrintCellVector(), DMPrintCellVectorReal(), DMPrintCellMatrix(), VecFilter()

src/dm/interface/dm.c

src/snes/tutorials/ex12.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMPrintLocalVec(DM dm, const char name[], PetscReal tol, Vec X)
```

Example 2 (unknown):
```unknown
VecFilter()
```

Example 3 (unknown):
```unknown
DMPrintCellIndices()
```

Example 4 (unknown):
```unknown
DMPrintCellVector()
```

---

## DMProjectBdFieldLabelLocal#

**URL:** https://petsc.org/release/manualpages/DM/DMProjectBdFieldLabelLocal/

**Contents:**
- DMProjectBdFieldLabelLocal#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Calling sequence of funcs#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#

This projects the given function of the input fields into the function space provided, putting the coefficients in a local vector, calculating only over the portion of the domain boundary specified by the label.

label - The DMLabel marking the portion of the domain boundary to output

numIds - The number of label ids to use

ids - The label ids to use for marking

Nc - The number of components to set in the output, or PETSC_DETERMINE for all components

comps - The components to set in the output, or NULL for all components

localU - The input field vector

funcs - The functions to evaluate, one per field

mode - The insertion mode for values

localX - The output vector

dim - The spatial dimension

Nf - The number of input fields

NfAux - The number of input auxiliary fields

uOff - The offset of each field in u[]

uOff_x - The offset of each field in u_x[]

u - The field values at this point in space

u_t - The field time derivative at this point in space (or NULL)

u_x - The field derivatives at this point in space

aOff - The offset of each auxiliary field in u[]

aOff_x - The offset of each auxiliary field in u_x[]

a - The auxiliary field values at this point in space

a_t - The auxiliary field time derivative at this point in space (or NULL)

a_x - The auxiliary field derivatives at this point in space

x - The coordinates of this point

numConstants - The number of constants

constants - The value of each constant

f - The value of the function at this point in space

There are three different DMs that potentially interact in this function. The output DM, dm, specifies the layout of the values calculates by funcs. The input DM, attached to U, may be different. For example, you can input the solution over the full domain, but output over a piece of the boundary, or a subdomain. You can also output a different number of fields than the input, with different discretizations. Last the auxiliary DM, attached to the auxiliary field vector, which is attached to dm, can also be different. It can have a different topology, number of fields, and discretizations.

This API is specific to only particular usage of DM

The notes need to provide some information about what has to be provided to the DM to be able to perform the computation.

DM Basics, DM, DMProjectField(), DMProjectFieldLabelLocal(), DMProjectFunction(), DMComputeL2Diff()

src/dm/interface/dm.c

DMProjectBdFieldLabelLocal_Plex(DM dm, PetscReal time, DMLabel label, PetscInt numIds, const PetscInt ids[], PetscInt Ncc, const PetscInt comps[], Vec localU, void (**funcs)() in src/dm/impls/plex/plexproject.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMProjectBdFieldLabelLocal(DM dm, PetscReal time, DMLabel label, PetscInt numIds, const PetscInt ids[], PetscInt Nc, const PetscInt comps[], Vec localU, void (**funcs)(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], const PetscReal n[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f[]), InsertMode mode, Vec localX)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
DMProjectField()
```

Example 4 (unknown):
```unknown
DMProjectFieldLabelLocal()
```

---

## DMProjectFieldLabelLocal#

**URL:** https://petsc.org/release/manualpages/DM/DMProjectFieldLabelLocal/

**Contents:**
- DMProjectFieldLabelLocal#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Calling sequence of funcs#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#

This projects the given function of the input fields into the function space provided, putting the coefficients in a local vector, calculating only over the portion of the domain specified by the label.

label - The DMLabel marking the portion of the domain to output

numIds - The number of label ids to use

ids - The label ids to use for marking

Nc - The number of components to set in the output, or PETSC_DETERMINE for all components

comps - The components to set in the output, or NULL for all components

localU - The input field vector

funcs - The functions to evaluate, one per field

mode - The insertion mode for values

localX - The output vector

dim - The spatial dimension

Nf - The number of input fields

NfAux - The number of input auxiliary fields

uOff - The offset of each field in u[]

uOff_x - The offset of each field in u_x[]

u - The field values at this point in space

u_t - The field time derivative at this point in space (or NULL)

u_x - The field derivatives at this point in space

aOff - The offset of each auxiliary field in u[]

aOff_x - The offset of each auxiliary field in u_x[]

a - The auxiliary field values at this point in space

a_t - The auxiliary field time derivative at this point in space (or NULL)

a_x - The auxiliary field derivatives at this point in space

x - The coordinates of this point

numConstants - The number of constants

constants - The value of each constant

f - The value of the function at this point in space

There are three different DMs that potentially interact in this function. The output DM, dm, specifies the layout of the values calculates by funcs. The input DM, attached to localU, may be different. For example, you can input the solution over the full domain, but output over a piece of the boundary, or a subdomain. You can also output a different number of fields than the input, with different discretizations. Last the auxiliary DM, attached to the auxiliary field vector, which is attached to dm, can also be different. It can have a different topology, number of fields, and discretizations.

This API is specific to only particular usage of DM

The notes need to provide some information about what has to be provided to the DM to be able to perform the computation.

DM Basics, DM, DMProjectField(), DMProjectFieldLabel(), DMProjectFunction(), DMComputeL2Diff()

src/dm/interface/dm.c

DMProjectFieldLabelLocal_Plex(DM dm, PetscReal time, DMLabel label, PetscInt numIds, const PetscInt ids[], PetscInt Ncc, const PetscInt comps[], Vec localU, void (**funcs)() in src/dm/impls/plex/plexproject.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMProjectFieldLabelLocal(DM dm, PetscReal time, DMLabel label, PetscInt numIds, const PetscInt ids[], PetscInt Nc, const PetscInt comps[], Vec localU, void (**funcs)(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f[]), InsertMode mode, Vec localX)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
DMProjectField()
```

Example 4 (unknown):
```unknown
DMProjectFieldLabel()
```

---

## DMProjectFieldLabel#

**URL:** https://petsc.org/release/manualpages/DM/DMProjectFieldLabel/

**Contents:**
- DMProjectFieldLabel#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Calling sequence of funcs#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#

This projects the given function of the input fields into the function space provided, putting the coefficients in a global vector, calculating only over the portion of the domain specified by the label.

label - The DMLabel marking the portion of the domain to output

numIds - The number of label ids to use

ids - The label ids to use for marking

Nc - The number of components to set in the output, or PETSC_DETERMINE for all components

comps - The components to set in the output, or NULL for all components

U - The input field vector

funcs - The functions to evaluate, one per field

mode - The insertion mode for values

X - The output vector

dim - The spatial dimension

Nf - The number of input fields

NfAux - The number of input auxiliary fields

uOff - The offset of each field in u[]

uOff_x - The offset of each field in u_x[]

u - The field values at this point in space

u_t - The field time derivative at this point in space (or NULL)

u_x - The field derivatives at this point in space

aOff - The offset of each auxiliary field in u[]

aOff_x - The offset of each auxiliary field in u_x[]

a - The auxiliary field values at this point in space

a_t - The auxiliary field time derivative at this point in space (or NULL)

a_x - The auxiliary field derivatives at this point in space

x - The coordinates of this point

numConstants - The number of constants

constants - The value of each constant

f - The value of the function at this point in space

There are three different DMs that potentially interact in this function. The output DM, dm, specifies the layout of the values calculates by funcs. The input DM, attached to U, may be different. For example, you can input the solution over the full domain, but output over a piece of the boundary, or a subdomain. You can also output a different number of fields than the input, with different discretizations. Last the auxiliary DM, attached to the auxiliary field vector, which is attached to dm, can also be different. It can have a different topology, number of fields, and discretizations.

This API is specific to only particular usage of DM

The notes need to provide some information about what has to be provided to the DM to be able to perform the computation.

DM Basics, DM, DMProjectField(), DMProjectFieldLabelLocal(), DMProjectFunction(), DMComputeL2Diff()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMProjectFieldLabel(DM dm, PetscReal time, DMLabel label, PetscInt numIds, const PetscInt ids[], PetscInt Nc, const PetscInt comps[], Vec U, void (**funcs)(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f[]), InsertMode mode, Vec X)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
DMProjectField()
```

Example 4 (unknown):
```unknown
DMProjectFieldLabelLocal()
```

---

## DMProjectFieldLocal#

**URL:** https://petsc.org/release/manualpages/DM/DMProjectFieldLocal/

**Contents:**
- DMProjectFieldLocal#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Calling sequence of funcs#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#

This projects the given function of the input fields into the function space provided by the DM, putting the coefficients in a local vector.

localU - The input field vector; may be NULL if projection is defined purely by coordinates

funcs - The functions to evaluate, one per field

mode - The insertion mode for values

localX - The output vector

dim - The spatial dimension

Nf - The number of input fields

NfAux - The number of input auxiliary fields

uOff - The offset of each field in u[]

uOff_x - The offset of each field in u_x[]

u - The field values at this point in space

u_t - The field time derivative at this point in space (or NULL)

u_x - The field derivatives at this point in space

aOff - The offset of each auxiliary field in u[]

aOff_x - The offset of each auxiliary field in u_x[]

a - The auxiliary field values at this point in space

a_t - The auxiliary field time derivative at this point in space (or NULL)

a_x - The auxiliary field derivatives at this point in space

x - The coordinates of this point

numConstants - The number of constants

constants - The value of each constant

f - The value of the function at this point in space

There are three different DMs that potentially interact in this function. The output DM, dm, specifies the layout of the values calculates by funcs. The input DM, attached to U, may be different. For example, you can input the solution over the full domain, but output over a piece of the boundary, or a subdomain. You can also output a different number of fields than the input, with different discretizations. Last the auxiliary DM, attached to the auxiliary field vector, which is attached to dm, can also be different. It can have a different topology, number of fields, and discretizations.

This API is specific to only particular usage of DM

The notes need to provide some information about what has to be provided to the DM to be able to perform the computation.

DM Basics, DM, DMProjectField(), DMProjectFieldLabelLocal(), DMProjectFunction(), DMComputeL2Diff()

src/dm/interface/dm.c

src/snes/tutorials/ex12.c

DMProjectFieldLocal_pforest(DM dm, PetscReal time, Vec localU, void (**funcs)() in src/dm/impls/forest/p4est/pforest.h DMProjectFieldLocal_Plex(DM dm, PetscReal time, Vec localU, void (**funcs)() in src/dm/impls/plex/plexproject.c DMProjectFieldLocal_Swarm() in src/dm/impls/swarm/swarmpic.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMProjectFieldLocal(DM dm, PetscReal time, Vec localU, void (**funcs)(PetscInt dim, PetscInt Nf, PetscInt NfAux, const PetscInt uOff[], const PetscInt uOff_x[], const PetscScalar u[], const PetscScalar u_t[], const PetscScalar u_x[], const PetscInt aOff[], const PetscInt aOff_x[], const PetscScalar a[], const PetscScalar a_t[], const PetscScalar a_x[], PetscReal t, const PetscReal x[], PetscInt numConstants, const PetscScalar constants[], PetscScalar f[]), InsertMode mode, Vec localX)
```

Example 2 (unknown):
```unknown
DMProjectField()
```

Example 3 (unknown):
```unknown
DMProjectFieldLabelLocal()
```

Example 4 (unknown):
```unknown
DMProjectFunction()
```

---

## DMProjectField#

**URL:** https://petsc.org/release/manualpages/DM/DMProjectField/

**Contents:**
- DMProjectField#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

This projects a given function of the input fields into the function space provided by a DM, putting the coefficients in a global vector.

U - The input field vector

funcs - The functions to evaluate, one per field, see PetscPointFn

mode - The insertion mode for values

X - The output vector

There are three different DMs that potentially interact in this function. The output dm, specifies the layout of the values calculates by the function. The input DM, attached to U, may be different. For example, you can input the solution over the full domain, but output over a piece of the boundary, or a subdomain. You can also output a different number of fields than the input, with different discretizations. Last the auxiliary DM, attached to the auxiliary field vector, which is attached to dm, can also be different. It can have a different topology, number of fields, and discretizations.

DM Basics, DM, PetscPointFn, DMProjectFieldLocal(), DMProjectFieldLabelLocal(), DMProjectFunction(), DMComputeL2Diff()

src/ksp/ksp/utils/dm/dmproject.c

src/ts/tutorials/ex30.c src/snes/tutorials/ex12.c src/ts/tutorials/ex76.c src/snes/tutorials/ex13.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h" 
#include "petscdmda.h" 
#include "petscdmplex.h" 
#include "petscdmswarm.h" 
#include "petscksp.h" 
PetscErrorCode DMProjectField(DM dm, PetscReal time, Vec U, PetscPointFn **funcs, InsertMode mode, Vec X)
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
DMProjectFieldLocal()
```

---

## DMProjectFunctionLabelLocal#

**URL:** https://petsc.org/release/manualpages/DM/DMProjectFunctionLabelLocal/

**Contents:**
- DMProjectFunctionLabelLocal#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Calling sequence of funcs#
- Developer Notes#
- See Also#
- Level#
- Location#
- Implementations#

This projects the given function into the function space provided by the DM, putting the coefficients in a local vector, setting values only for points in the given label.

label - The DMLabel selecting the portion of the mesh for projection

numIds - The number of ids

Nc - The number of components

comps - The components

funcs - The coordinate functions to evaluate, one per field

ctxs - Optional array of contexts to pass to each coordinate function. ctxs itself may be null.

mode - The insertion mode for values

dim - The spatial dimension

time - The current time

Nc - The number of components

u - The output field values

ctx - optional function context

This API is specific to only particular usage of DM

The notes need to provide some information about what has to be provided to the DM to be able to perform the computation.

DM Basics, DM, DMProjectFunction(), DMProjectFunctionLocal(), DMProjectFunctionLabel(), DMComputeL2Diff()

src/dm/interface/dm.c

DMProjectFunctionLabelLocal_pforest(DM dm, PetscReal time, DMLabel label, PetscInt numIds, const PetscInt ids[], PetscInt Ncc, const PetscInt comps[], PetscErrorCode (**funcs)() in src/dm/impls/forest/p4est/pforest.h DMProjectFunctionLabelLocal_Plex(DM dm, PetscReal time, DMLabel label, PetscInt numIds, const PetscInt ids[], PetscInt Ncc, const PetscInt comps[], PetscErrorCode (**funcs)() in src/dm/impls/plex/plexproject.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMProjectFunctionLabelLocal(DM dm, PetscReal time, DMLabel label, PetscInt numIds, const PetscInt ids[], PetscInt Nc, const PetscInt comps[], PetscErrorCode (**funcs)(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx), void **ctxs, InsertMode mode, Vec localX)
```

Example 2 (unknown):
```unknown
DMProjectFunction()
```

Example 3 (unknown):
```unknown
DMProjectFunctionLocal()
```

Example 4 (unknown):
```unknown
DMProjectFunctionLabel()
```

---

## DMProjectFunctionLabel#

**URL:** https://petsc.org/release/manualpages/DM/DMProjectFunctionLabel/

**Contents:**
- DMProjectFunctionLabel#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Calling sequence of funcs#
- Developer Notes#
- See Also#
- Level#
- Location#

This projects the given function into the function space provided by the DM, putting the coefficients in a global vector, setting values only for points in the given label.

numIds - The number of ids

Nc - The number of components

comps - The components

label - The DMLabel selecting the portion of the mesh for projection

funcs - The coordinate functions to evaluate, one per field

ctxs - Optional array of contexts to pass to each coordinate function. ctxs may be null.

mode - The insertion mode for values

dim - The spatial dimension

time - The current timestep

Nc - The number of components

u - The output field values

ctx - optional function context

This API is specific to only particular usage of DM

The notes need to provide some information about what has to be provided to the DM to be able to perform the computation.

DM Basics, DM, DMProjectFunction(), DMProjectFunctionLocal(), DMProjectFunctionLabelLocal(), DMComputeL2Diff()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMProjectFunctionLabel(DM dm, PetscReal time, DMLabel label, PetscInt numIds, const PetscInt ids[], PetscInt Nc, const PetscInt comps[], PetscErrorCode (**funcs)(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx), void **ctxs, InsertMode mode, Vec X)
```

Example 2 (unknown):
```unknown
DMProjectFunction()
```

Example 3 (unknown):
```unknown
DMProjectFunctionLocal()
```

Example 4 (unknown):
```unknown
DMProjectFunctionLabelLocal()
```

---

## DMProjectFunctionLocal#

**URL:** https://petsc.org/release/manualpages/DM/DMProjectFunctionLocal/

**Contents:**
- DMProjectFunctionLocal#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Calling sequence of funcs#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#

This projects the given function into the function space provided by a DM, putting the coefficients in a local vector.

funcs - The coordinate functions to evaluate, one per field

ctxs - Optional array of contexts to pass to each coordinate function. ctxs itself may be null.

mode - The insertion mode for values

dim - The spatial dimension

time - The current timestep

Nc - The number of components

u - The output field values

ctx - optional function context

This API is specific to only particular usage of DM

The notes need to provide some information about what has to be provided to the DM to be able to perform the computation.

DM Basics, DM, DMProjectFunction(), DMProjectFunctionLabel(), DMComputeL2Diff()

src/dm/interface/dm.c

src/dm/field/tutorials/ex1.c src/snes/tutorials/ex77.c src/ts/tutorials/ex47.c src/snes/tutorials/ex12.c

DMProjectFunctionLocal_pforest(DM dm, PetscReal time, PetscErrorCode (**funcs)() in src/dm/impls/forest/p4est/pforest.h DMProjectFunctionLocal_Plex(DM dm, PetscReal time, PetscErrorCode (**funcs)() in src/dm/impls/plex/plexproject.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMProjectFunctionLocal(DM dm, PetscReal time, PetscErrorCode (**funcs)(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx), void **ctxs, InsertMode mode, Vec localX)
```

Example 2 (unknown):
```unknown
DMProjectFunction()
```

Example 3 (unknown):
```unknown
DMProjectFunctionLabel()
```

Example 4 (unknown):
```unknown
DMComputeL2Diff()
```

---

## DMProjectFunction#

**URL:** https://petsc.org/release/manualpages/DM/DMProjectFunction/

**Contents:**
- DMProjectFunction#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Calling sequence of funcs#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#

This projects the given function into the function space provided by a DM, putting the coefficients in a global vector.

funcs - The coordinate functions to evaluate, one per field

ctxs - Optional array of contexts to pass to each coordinate function. ctxs itself may be null.

mode - The insertion mode for values

dim - The spatial dimension

time - The time at which to sample

Nc - The number of components

u - The output field values

ctx - optional function context

This API is specific to only particular usage of DM

The notes need to provide some information about what has to be provided to the DM to be able to perform the computation.

DM Basics, DM, DMProjectFunctionLocal(), DMProjectFunctionLabel(), DMComputeL2Diff()

src/dm/interface/dm.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex62.c src/snes/tutorials/ex11.c src/snes/tutorials/ex76.c src/snes/tutorials/ex75.c src/tao/tutorials/ex2.c src/snes/tutorials/ex12.c src/snes/tutorials/ex69.c src/tao/tutorials/ex1.c src/snes/tutorials/ex77.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMProjectFunction(DM dm, PetscReal time, PetscErrorCode (**funcs)(PetscInt dim, PetscReal time, const PetscReal x[], PetscInt Nc, PetscScalar *u, PetscCtx ctx), void **ctxs, InsertMode mode, Vec X)
```

Example 2 (unknown):
```unknown
DMProjectFunctionLocal()
```

Example 3 (unknown):
```unknown
DMProjectFunctionLabel()
```

Example 4 (unknown):
```unknown
DMComputeL2Diff()
```

---

## DMRedundantCreate#

**URL:** https://petsc.org/release/manualpages/DM/DMRedundantCreate/

**Contents:**
- DMRedundantCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Creates a DM object, used to manage data for dense globally coupled variables

comm - the processors that will share the global vector

rank - the MPI rank to own the redundant values

N - total number of degrees of freedom

dm - the DM object of type DMREDUNDANT

DM, DMREDUNDANT, DMDestroy(), DMCreateGlobalVector(), DMCreateMatrix(), DMCompositeAddDM(), DMSetType(), DMRedundantSetSize(), DMRedundantGetSize()

src/dm/impls/redundant/dmredundant.c

src/snes/tutorials/ex22.c src/snes/tutorials/ex21.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmredundant.h" 
PetscErrorCode DMRedundantCreate(MPI_Comm comm, PetscMPIInt rank, PetscInt N, DM *dm)
```

Example 2 (unknown):
```unknown
DMREDUNDANT
```

Example 3 (unknown):
```unknown
DMREDUNDANT
```

Example 4 (unknown):
```unknown
DMDestroy()
```

---

## DMRedundantGetSize#

**URL:** https://petsc.org/release/manualpages/DM/DMRedundantGetSize/

**Contents:**
- DMRedundantGetSize#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Gets the size of a densely coupled redundant object

dm - DM object of type DMREDUNDANT

rank - rank of process to own the redundant degrees of freedom (or NULL)

N - total number of redundant degrees of freedom (or NULL)

DM, DMREDUNDANT, DMDestroy(), DMCreateGlobalVector(), DMRedundantCreate(), DMRedundantSetSize()

src/dm/impls/redundant/dmredundant.c

DMRedundantGetSize_Redundant() in src/dm/impls/redundant/dmredundant.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmredundant.h" 
PetscErrorCode DMRedundantGetSize(DM dm, PetscMPIInt *rank, PetscInt *N)
```

Example 2 (unknown):
```unknown
DMREDUNDANT
```

Example 3 (unknown):
```unknown
DMREDUNDANT
```

Example 4 (unknown):
```unknown
DMDestroy()
```

---

## DMRedundantSetSize#

**URL:** https://petsc.org/release/manualpages/DM/DMRedundantSetSize/

**Contents:**
- DMRedundantSetSize#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Sets the size of a densely coupled redundant object

dm - DM object of type DMREDUNDANT

rank - rank of process to own the redundant degrees of freedom

N - total number of redundant degrees of freedom

DM, DMREDUNDANT, DMDestroy(), DMCreateGlobalVector(), DMRedundantCreate(), DMRedundantGetSize()

src/dm/impls/redundant/dmredundant.c

DMRedundantSetSize_Redundant() in src/dm/impls/redundant/dmredundant.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmredundant.h" 
PetscErrorCode DMRedundantSetSize(DM dm, PetscMPIInt rank, PetscInt N)
```

Example 2 (unknown):
```unknown
DMREDUNDANT
```

Example 3 (unknown):
```unknown
DMREDUNDANT
```

Example 4 (unknown):
```unknown
DMDestroy()
```

---

## DMREDUNDANT#

**URL:** https://petsc.org/release/manualpages/DM/DMREDUNDANT/

**Contents:**
- DMREDUNDANT#
- See Also#
- Level#
- Location#

“redundant” - A DM object that is used to manage data for a small set of dense globally coupled variables. In the global representation of the vector the variables are all stored on a single MPI process (all the other MPI processes have no variables) in the local representation all the variables are stored on ALL the MPI processes (because they are all needed for each processes local computations). This DM is generally used inside a DMCOMPOSITE object. For example, it may be used to store continuation parameters for a bifurcation problem.

DMType, DMCOMPOSITE, DMCreate(), DMRedundantSetSize(), DMRedundantGetSize()

src/dm/impls/redundant/dmredundant.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCOMPOSITE
```

Example 2 (unknown):
```unknown
DMRedundantSetSize()
```

Example 3 (unknown):
```unknown
DMRedundantGetSize()
```

---

## DMRefineHierarchy#

**URL:** https://petsc.org/release/manualpages/DM/DMRefineHierarchy/

**Contents:**
- DMRefineHierarchy#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Refines a DM object, all levels at once

nlevels - the number of levels of refinement

dmf - the refined DM hierarchy

DM Basics, DM, DMCoarsen(), DMCoarsenHierarchy(), DMDestroy(), DMView(), DMCreateGlobalVector(), DMCreateInterpolation()

src/dm/interface/dm.c

src/ts/tutorials/ex30.c src/ksp/ksp/tutorials/ex35.cxx src/ksp/ksp/tutorials/ex36.cxx src/snes/tutorials/ex48.c

DMRefineHierarchy_DA() in src/dm/impls/da/da.c DMRefineHierarchy_Moab() in src/dm/impls/moab/dmmbmg.cxx DMRefineHierarchy_Plex() in src/dm/impls/plex/plexrefine.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMRefineHierarchy(DM dm, PetscInt nlevels, DM dmf[])
```

Example 2 (unknown):
```unknown
DMCoarsen()
```

Example 3 (unknown):
```unknown
DMCoarsenHierarchy()
```

Example 4 (unknown):
```unknown
DMDestroy()
```

---

## DMRefineHookAdd#

**URL:** https://petsc.org/release/manualpages/DM/DMRefineHookAdd/

**Contents:**
- DMRefineHookAdd#
- Synopsis#
- Input Parameters#
- Calling sequence of refinehook#
- Calling sequence of interphook#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

adds a callback to be run when interpolating a nonlinear problem to a finer grid

Logically Collective; No Fortran Support

coarse - DM on which to run a hook when interpolating to a finer level

refinehook - function to run when setting up the finer level

interphook - function to run to update data on finer levels (once per SNESSolve())

ctx - [optional] context for provide data for the hooks (may be NULL)

coarse - coarse level DM

fine - fine level DM to interpolate problem to

ctx - optional function context

coarse - coarse level DM

interp - matrix interpolating a coarse-level solution to the finer grid

fine - fine level DM to update

ctx - optional function context

This function is only needed if auxiliary data that is attached to the DMs via, for example, PetscObjectCompose(), needs to be passed to fine grids while grid sequencing.

The actual interpolation is done when DMInterpolate() is called.

If this function is called multiple times, the hooks will be run in the order they are added.

DM Basics, DM, DMCoarsenHookAdd(), DMInterpolate(), SNESFASGetInterpolation(), SNESFASGetInjection(), PetscObjectCompose(), PetscContainerCreate()

src/dm/interface/dm.c

src/snes/tutorials/ex48.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMRefineHookAdd(DM coarse, PetscErrorCode (*refinehook)(DM coarse, DM fine, PetscCtx ctx), PetscErrorCode (*interphook)(DM coarse, Mat interp, DM fine, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
SNESSolve()
```

Example 3 (unknown):
```unknown
PetscObjectCompose()
```

Example 4 (unknown):
```unknown
DMInterpolate()
```

---

## DMRefineHookRemove#

**URL:** https://petsc.org/release/manualpages/DM/DMRefineHookRemove/

**Contents:**
- DMRefineHookRemove#
- Synopsis#
- Input Parameters#
- Calling sequence of refinehook#
- Calling sequence of interphook#
- Note#
- See Also#
- Level#
- Location#

remove a callback from the list of hooks, that have been set with DMRefineHookAdd(), to be run when interpolating a nonlinear problem to a finer grid

Logically Collective; No Fortran Support

coarse - the DM on which to run a hook when restricting to a coarser level

refinehook - function to run when setting up a finer level

interphook - function to run to update data on finer levels

ctx - [optional] application context for provide data for the hooks (may be NULL)

coarse - the coarse DM

ctx - context for the function

coarse - the coarse DM

interp - the interpolation Mat from coarse to fine

ctx - context for the function

This function does nothing if the hook is not in the list.

DM Basics, DM, DMRefineHookAdd(), DMCoarsenHookRemove(), DMInterpolate(), SNESFASGetInterpolation(), SNESFASGetInjection(), PetscObjectCompose(), PetscContainerCreate()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMRefineHookAdd()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMRefineHookRemove(DM coarse, PetscErrorCode (*refinehook)(DM coarse, DM fine, PetscCtx ctx), PetscErrorCode (*interphook)(DM coarse, Mat interp, DM fine, PetscCtx ctx), PetscCtx ctx)
```

Example 3 (unknown):
```unknown
DMRefineHookAdd()
```

Example 4 (unknown):
```unknown
DMCoarsenHookRemove()
```

---

## DMRefine#

**URL:** https://petsc.org/release/manualpages/DM/DMRefine/

**Contents:**
- DMRefine#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Refines a DM object using a standard nonadaptive refinement of the underlying mesh

comm - the communicator to contain the new DM object (or MPI_COMM_NULL)

dmf - the refined DM, or NULL

-dm_plex_cell_refiner strategy - chooses the refinement strategy, e.g. regular, tohex

If no refinement was done, the return value is NULL

DM Basics, DM, DMCoarsen(), DMDestroy(), DMView(), DMCreateGlobalVector(), DMCreateInterpolation(), DMCreateDomainDecomposition(), DMRefineHookAdd(), DMRefineHookRemove()

src/dm/interface/dm.c

src/ts/tutorials/ex30.c src/ksp/ksp/tutorials/ex73.c src/ksp/ksp/tutorials/ex35.cxx src/snes/tutorials/ex56.c src/dm/tutorials/ex3.c src/ksp/ksp/tutorials/ex36.cxx src/dm/impls/plex/tutorials/ex11.c src/ksp/ksp/tutorials/ex65.c

DMRefine_Composite() in src/dm/impls/composite/pack.c DMRefine_DA() in src/dm/impls/da/da.c DMRefine_Forest() in src/dm/impls/forest/forest.c DMRefine_Moab() in src/dm/impls/moab/dmmbmg.cxx DMRefine_Plex() in src/dm/impls/plex/plexrefine.c DMRefine_Redundant() in src/dm/impls/redundant/dmredundant.c DMRefine_Stag() in src/dm/impls/stag/stag.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMRefine(DM dm, MPI_Comm comm, DM *dmf)
```

Example 2 (unknown):
```unknown
MPI_COMM_NULL
```

Example 3 (unknown):
```unknown
DMCoarsen()
```

Example 4 (unknown):
```unknown
DMDestroy()
```

---

## DMRegisterAll#

**URL:** https://petsc.org/release/manualpages/DM/DMRegisterAll/

**Contents:**
- DMRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the DM components in the DM package.

DMRegister(), DMRegisterDestroy()

src/dm/interface/dmregall.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"  
#include "petscdmplex.h"  
PetscErrorCode DMRegisterAll(void)
```

Example 2 (unknown):
```unknown
DMRegister()
```

Example 3 (unknown):
```unknown
DMRegisterDestroy()
```

---

## DMRegister#

**URL:** https://petsc.org/release/manualpages/DM/DMRegister/

**Contents:**
- DMRegister#
- Synopsis#
- Input Parameters#
- Calling sequence of function#
- Note#
- Example Usage#
- See Also#
- Level#
- Location#

Adds a new DM type implementation

Not Collective, No Fortran Support

sname - The name of a new user-defined creation routine

function - The creation routine itself

dm - the new DM that is being created

DMRegister() may be called multiple times to add several user-defined DMs

Then, your DM type can be chosen with the procedural interface via

or at runtime via the option

DM Basics, DM, DMType, DMSetType(), DMRegisterAll(), DMRegisterDestroy()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMRegister(const char sname[], PetscErrorCode (*function)(DM dm))
```

Example 2 (unknown):
```unknown
DMRegister()
```

Example 3 (unknown):
```unknown
DMRegister("my_da", MyDMCreate);
```

Example 4 (unknown):
```unknown
DMCreate(MPI_Comm, DM *);
    DMSetType(DM,"my_da");
```

---

## DMRemoveLabelBySelf#

**URL:** https://petsc.org/release/manualpages/DM/DMRemoveLabelBySelf/

**Contents:**
- DMRemoveLabelBySelf#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Remove the label from this DM

label - The DMLabel to be removed from the DM

failNotFound - Should it fail if the label is not found in the DM?

Only exactly the same instance is removed if found, name match is ignored. If the DM has an exclusive reference to the label, the label gets destroyed and *label nullified.

DM Basics, DM, DMLabel, DMCreateLabel(), DMHasLabel(), DMGetLabel(), DMGetLabelValue(), DMSetLabelValue(), DMLabelDestroy(), DMRemoveLabel()

src/dm/interface/dm.c

src/dm/label/tutorials/ex1.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMRemoveLabelBySelf(DM dm, DMLabel *label, PetscBool failNotFound)
```

Example 2 (unknown):
```unknown
DMCreateLabel()
```

Example 3 (unknown):
```unknown
DMHasLabel()
```

Example 4 (unknown):
```unknown
DMGetLabel()
```

---

## DMRemoveLabel#

**URL:** https://petsc.org/release/manualpages/DM/DMRemoveLabel/

**Contents:**
- DMRemoveLabel#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Remove the label given by name from this DM

name - The label name

label - The DMLabel, or NULL if the label is absent. Pass in NULL to call DMLabelDestroy() on the label, otherwise the caller is responsible for calling DMLabelDestroy().

DM Basics, DM, DMLabel, DMCreateLabel(), DMHasLabel(), DMGetLabel(), DMGetLabelValue(), DMSetLabelValue(), DMLabelDestroy(), DMRemoveLabelBySelf()

src/dm/interface/dm.c

src/dm/label/tutorials/ex1.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMRemoveLabel(DM dm, const char name[], DMLabel *label)
```

Example 2 (unknown):
```unknown
DMLabelDestroy()
```

Example 3 (unknown):
```unknown
DMLabelDestroy()
```

Example 4 (unknown):
```unknown
DMCreateLabel()
```

---

## DMReorderDefaultFlag#

**URL:** https://petsc.org/release/manualpages/DM/DMReorderDefaultFlag/

**Contents:**
- DMReorderDefaultFlag#
- Synopsis#
- Values#
- Developer Note#
- See Also#
- Level#
- Location#

Flag indicating whether the DM should be reordered by default

DM_REORDER_DEFAULT_NOTSET - Flag not set.

DM_REORDER_DEFAULT_FALSE - Do not reorder by default.

DM_REORDER_DEFAULT_TRUE - Reorder by default.

Could be replaced with PETSC_BOOL3

DMPlexReorderSetDefault(), DMPlexReorderGetDefault(), DMPlexGetOrdering(), DMPlexPermute()

include/petscdmtypes.h

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  DM_REORDER_DEFAULT_NOTSET = -1,
  DM_REORDER_DEFAULT_FALSE  = 0,
  DM_REORDER_DEFAULT_TRUE   = 1
} DMReorderDefaultFlag;
```

Example 2 (unknown):
```unknown
DM_REORDER_DEFAULT_NOTSET
```

Example 3 (unknown):
```unknown
DM_REORDER_DEFAULT_FALSE
```

Example 4 (unknown):
```unknown
DM_REORDER_DEFAULT_TRUE
```

---

## DMReorderSectionGetDefault#

**URL:** https://petsc.org/release/manualpages/DM/DMReorderSectionGetDefault/

**Contents:**
- DMReorderSectionGetDefault#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get flag indicating whether the local section should be reordered by default

reorder - Flag for reordering

DMReorderSetDefault()

src/dm/interface/dm.c

DMReorderSectionGetDefault_Plex() in src/dm/impls/plex/plexreorder.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMReorderSectionGetDefault(DM dm, DMReorderDefaultFlag *reorder)
```

Example 2 (unknown):
```unknown
DMReorderSetDefault()
```

---

## DMReorderSectionGetType#

**URL:** https://petsc.org/release/manualpages/DM/DMReorderSectionGetType/

**Contents:**
- DMReorderSectionGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get the reordering type for the local section

reorder - The reordering method

DMReorderSetDefault(), DMReorderSectionGetDefault()

src/dm/interface/dm.c

DMReorderSectionGetType_Plex() in src/dm/impls/plex/plexreorder.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMReorderSectionGetType(DM dm, MatOrderingType *reorder)
```

Example 2 (unknown):
```unknown
DMReorderSetDefault()
```

Example 3 (unknown):
```unknown
DMReorderSectionGetDefault()
```

---

## DMReorderSectionSetDefault#

**URL:** https://petsc.org/release/manualpages/DM/DMReorderSectionSetDefault/

**Contents:**
- DMReorderSectionSetDefault#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set flag indicating whether the local section should be reordered by default

reorder - Flag for reordering

DMReorderSectionGetDefault()

src/dm/interface/dm.c

DMReorderSectionSetDefault_Plex() in src/dm/impls/plex/plexreorder.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMReorderSectionSetDefault(DM dm, DMReorderDefaultFlag reorder)
```

Example 2 (unknown):
```unknown
DMReorderSectionGetDefault()
```

---

## DMReorderSectionSetType#

**URL:** https://petsc.org/release/manualpages/DM/DMReorderSectionSetType/

**Contents:**
- DMReorderSectionSetType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set the type of local section reordering

reorder - The reordering method

DMReorderSectionGetType(), DMReorderSectionSetDefault()

src/dm/interface/dm.c

DMReorderSectionSetType_Plex() in src/dm/impls/plex/plexreorder.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMReorderSectionSetType(DM dm, MatOrderingType reorder)
```

Example 2 (unknown):
```unknown
DMReorderSectionGetType()
```

Example 3 (unknown):
```unknown
DMReorderSectionSetDefault()
```

---

## DMRestoreGlobalVector#

**URL:** https://petsc.org/release/manualpages/DM/DMRestoreGlobalVector/

**Contents:**
- DMRestoreGlobalVector#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Returns a PETSc vector that obtained from DMGetGlobalVector(). Do not use with vector obtained via DMCreateGlobalVector().

g - the global vector

DM, DMCreateGlobalVector(), VecDuplicate(), VecDuplicateVecs(), DMDACreate1d(), DMDACreate2d(), DMDACreate3d(), DMGlobalToGlobalBegin(), DMGlobalToGlobalEnd(), DMGlobalToGlobal(), DMCreateLocalVector(), DMGetGlobalVector(), DMClearGlobalVectors()

src/dm/interface/dmget.c

src/snes/tutorials/ex3k.kokkos.cxx src/snes/tutorials/ex76.c src/snes/tutorials/ex75.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex27.c src/snes/tutorials/ex33.c src/snes/tutorials/ex69.c src/snes/tutorials/ex7.c src/snes/tutorials/ex22.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMGetGlobalVector()
```

Example 2 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 3 (unknown):
```unknown
#include "petscdm.h" 
PetscErrorCode DMRestoreGlobalVector(DM dm, Vec *g)
```

Example 4 (unknown):
```unknown
DMCreateGlobalVector()
```

---

## DMRestoreLocalVector#

**URL:** https://petsc.org/release/manualpages/DM/DMRestoreLocalVector/

**Contents:**
- DMRestoreLocalVector#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Returns a PETSc vector that was obtained from DMGetLocalVector(). Do not use with vector obtained via DMCreateLocalVector().

DM, DMCreateGlobalVector(), VecDuplicate(), VecDuplicateVecs(), DMDACreate1d(), DMDACreate2d(), DMDACreate3d(), DMGlobalToLocalBegin(), DMGlobalToLocalEnd(), DMLocalToGlobalBegin(), DMCreateLocalVector(), DMGetLocalVector(), DMClearLocalVectors()

src/dm/interface/dmget.c

src/snes/tutorials/ex5f90.F90 src/snes/tutorials/ex14.c src/snes/tutorials/ex18.c src/snes/tutorials/ex12.c src/snes/tutorials/ex35.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex78.c src/snes/tutorials/ex15.c src/snes/tutorials/ex7.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMGetLocalVector()
```

Example 2 (unknown):
```unknown
DMCreateLocalVector()
```

Example 3 (unknown):
```unknown
#include "petscdm.h" 
PetscErrorCode DMRestoreLocalVector(DM dm, Vec *g)
```

Example 4 (unknown):
```unknown
DMCreateGlobalVector()
```

---

## DMRestoreNamedGlobalVector#

**URL:** https://petsc.org/release/manualpages/DM/DMRestoreNamedGlobalVector/

**Contents:**
- DMRestoreNamedGlobalVector#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

restore access to a named, persistent global vector

dm - DM on which X was gotten

name - name under which X was gotten

DM, DMGetNamedGlobalVector(), DMClearNamedGlobalVectors()

src/dm/interface/dmget.c

src/ts/tutorials/ex30.c src/ts/tutorials/ex29.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h" 
PetscErrorCode DMRestoreNamedGlobalVector(DM dm, const char *name, Vec *X)
```

Example 2 (unknown):
```unknown
DMGetNamedGlobalVector()
```

Example 3 (unknown):
```unknown
DMClearNamedGlobalVectors()
```

---

## DMRestoreNamedLocalVector#

**URL:** https://petsc.org/release/manualpages/DM/DMRestoreNamedLocalVector/

**Contents:**
- DMRestoreNamedLocalVector#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

restore access to a named, persistent local vector obtained with DMGetNamedLocalVector()

dm - DM on which X was gotten

name - name under which X was gotten

DM, DMRestoreNamedGlobalVector(), DMGetNamedLocalVector(), DMClearNamedLocalVectors()

src/dm/interface/dmget.c

src/ts/tutorials/ex30.c src/ts/tutorials/ex29.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMGetNamedLocalVector()
```

Example 2 (unknown):
```unknown
#include "petscdm.h" 
PetscErrorCode DMRestoreNamedLocalVector(DM dm, const char *name, Vec *X)
```

Example 3 (unknown):
```unknown
DMRestoreNamedGlobalVector()
```

Example 4 (unknown):
```unknown
DMGetNamedLocalVector()
```

---

## DMRestoreWorkArray#

**URL:** https://petsc.org/release/manualpages/DM/DMRestoreWorkArray/

**Contents:**
- DMRestoreWorkArray#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Developer Note#
- See Also#
- Level#
- Location#

Restores a work array obtained with DMCreateWorkArray()

count - The minimum size

dtype - MPI data type, often MPIU_REAL, MPIU_SCALAR, MPIU_INT

count and dtype are ignored, they are only needed for DMGetWorkArray()

DM Basics, DM, DMDestroy(), DMCreate(), DMGetWorkArray()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateWorkArray()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMRestoreWorkArray(DM dm, PetscInt count, MPI_Datatype dtype, void *mem)
```

Example 3 (unknown):
```unknown
MPIU_SCALAR
```

Example 4 (unknown):
```unknown
DMGetWorkArray()
```

---

## DMRestrict#

**URL:** https://petsc.org/release/manualpages/DM/DMRestrict/

**Contents:**
- DMRestrict#
- Synopsis#
- Input Parameters#
- Developer Note#
- See Also#
- Level#
- Location#

restricts user-defined problem data to a coarser DM by running hooks registered by DMCoarsenHookAdd()

Collective if any hooks are

fine - finer DM from which the data is obtained

restrct - restriction matrix, apply using MatRestrict(), usually the transpose of the interpolation

rscale - scaling vector for restriction

inject - injection matrix, also use MatRestrict()

coarse - coarser DM to update

Though this routine is called DMRestrict() the hooks are added with DMCoarsenHookAdd(), a consistent terminology would be better

DM Basics, DM, DMCoarsenHookAdd(), MatRestrict(), DMInterpolate(), DMRefineHookAdd()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCoarsenHookAdd()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMRestrict(DM fine, Mat restrct, Vec rscale, Mat inject, DM coarse)
```

Example 3 (unknown):
```unknown
MatRestrict()
```

Example 4 (unknown):
```unknown
MatRestrict()
```

---

## DMSetAdjacency#

**URL:** https://petsc.org/release/manualpages/DM/DMSetAdjacency/

**Contents:**
- DMSetAdjacency#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Set the flags for determining variable influence

useCone - Flag for variable influence starting with the cone operation

useClosure - Flag for variable influence using transitive closure

Further explanation can be found in the User’s Manual Section on the Influence of Variables on One Another.

DM Basics, DM, DMGetAdjacency(), DMGetField(), DMSetField()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetAdjacency(DM dm, PetscInt f, PetscBool useCone, PetscBool useClosure)
```

Example 2 (sass):
```sass
FEM:   Two points p and q are adjacent if q \in closure(star(p)),   useCone = PETSC_FALSE, useClosure = PETSC_TRUE
     FVM:   Two points p and q are adjacent if q \in support(p+cone(p)), useCone = PETSC_TRUE,  useClosure = PETSC_FALSE
     FVM++: Two points p and q are adjacent if q \in star(closure(p)),   useCone = PETSC_TRUE,  useClosure = PETSC_TRUE
```

Example 3 (unknown):
```unknown
DMGetAdjacency()
```

Example 4 (unknown):
```unknown
DMGetField()
```

---

## DMSetApplicationContextDestroy#

**URL:** https://petsc.org/release/manualpages/DM/DMSetApplicationContextDestroy/

**Contents:**
- DMSetApplicationContextDestroy#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets a user function that will be called to destroy the application context when the DM is destroyed

Logically Collective if the function is collective

destroy - the destroy function, see PetscCtxDestroyFn for the calling sequence

DM Basics, DM, DMSetApplicationContext(), DMView(), DMCreateGlobalVector(), DMCreateInterpolation(), DMCreateColoring(), DMCreateMatrix(), DMCreateMassMatrix(), DMGetApplicationContext(), PetscCtxDestroyFn

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetApplicationContextDestroy(DM dm, PetscCtxDestroyFn *destroy)
```

Example 2 (unknown):
```unknown
PetscCtxDestroyFn
```

Example 3 (unknown):
```unknown
DMSetApplicationContext()
```

Example 4 (unknown):
```unknown
DMCreateGlobalVector()
```

---

## DMSetApplicationContext#

**URL:** https://petsc.org/release/manualpages/DM/DMSetApplicationContext/

**Contents:**
- DMSetApplicationContext#
- Synopsis#
- Input Parameters#
- Note#
- Fortran Notes#
- See Also#
- Level#
- Location#
- Examples#

Set an application context into a DM object

ctx - the application context

An application context is a way to pass problem specific information that is accessible whenever the DM is available In a multilevel solver, the application context is shared by all the DM in the hierarchy; it is thus not advisable to store objects that represent discretized quantities inside the context.

This only works when the context is a Fortran derived type or a PetscObject. Declare ctx with

DM Basics, DM, DMGetApplicationContext(), DMView(), DMCreateGlobalVector(), DMCreateInterpolation(), DMCreateColoring(), DMCreateMatrix(), DMCreateMassMatrix()

src/dm/interface/dm.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex18.c src/snes/tutorials/ex15.c src/snes/tutorials/ex12.c src/snes/tutorials/ex46.c src/snes/tutorials/ex26.c src/snes/tutorials/ex17.c src/snes/tutorials/ex33.c src/snes/tutorials/ex23.c src/snes/tutorials/ex22.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetApplicationContext(DM dm, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
PetscObject
```

Example 3 (julia):
```julia
type(tUsertype), pointer :: ctx
```

Example 4 (unknown):
```unknown
DMGetApplicationContext()
```

---

## DMSetAuxiliaryVec#

**URL:** https://petsc.org/release/manualpages/DM/DMSetAuxiliaryVec/

**Contents:**
- DMSetAuxiliaryVec#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set an auxiliary vector for region specified by the given label and value, and equation part

Not Collective because auxiliary vectors are not parallel

value - The label value indicating the region

part - The equation part, or 0 if unused

aux - The Vec holding auxiliary field data

DM Basics, DM, DMClearAuxiliaryVec(), DMGetAuxiliaryVec(), DMGetAuxiliaryLabels(), DMCopyAuxiliaryVec()

src/dm/interface/dm.c

src/snes/tutorials/ex11.c src/ts/tutorials/ex30.c src/ts/tutorials/ex47.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex7.c src/snes/tutorials/ex77.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetAuxiliaryVec(DM dm, DMLabel label, PetscInt value, PetscInt part, Vec aux)
```

Example 2 (unknown):
```unknown
DMClearAuxiliaryVec()
```

Example 3 (unknown):
```unknown
DMGetAuxiliaryVec()
```

Example 4 (unknown):
```unknown
DMGetAuxiliaryLabels()
```

---

## DMSetBasicAdjacency#

**URL:** https://petsc.org/release/manualpages/DM/DMSetBasicAdjacency/

**Contents:**
- DMSetBasicAdjacency#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Set the flags for determining variable influence, using either the default or field 0 if it is defined

useCone - Flag for variable influence starting with the cone operation

useClosure - Flag for variable influence using transitive closure

DM Basics, DM, DMGetBasicAdjacency(), DMGetField(), DMSetField()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetBasicAdjacency(DM dm, PetscBool useCone, PetscBool useClosure)
```

Example 2 (sass):
```sass
FEM:   Two points p and q are adjacent if q \in closure(star(p)),   useCone = PETSC_FALSE, useClosure = PETSC_TRUE
     FVM:   Two points p and q are adjacent if q \in support(p+cone(p)), useCone = PETSC_TRUE,  useClosure = PETSC_FALSE
     FVM++: Two points p and q are adjacent if q \in star(closure(p)),   useCone = PETSC_TRUE,  useClosure = PETSC_TRUE
```

Example 3 (unknown):
```unknown
DMGetBasicAdjacency()
```

Example 4 (unknown):
```unknown
DMGetField()
```

---

## DMSetBlockingType#

**URL:** https://petsc.org/release/manualpages/DM/DMSetBlockingType/

**Contents:**
- DMSetBlockingType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

set the blocking granularity to be used for variable block size DMCreateMatrix() is called

btype - block by topological point or field node

-dm_blocking_type (topological_point|field_node) - use topological point blocking or field node blocking

DM Basics, DM, DMCreateMatrix(), MatSetVariableBlockSizes()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateMatrix()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetBlockingType(DM dm, DMBlockingType btype)
```

Example 3 (unknown):
```unknown
DMCreateMatrix()
```

Example 4 (unknown):
```unknown
MatSetVariableBlockSizes()
```

---

## DMSetCellCoordinateDM#

**URL:** https://petsc.org/release/manualpages/DM/DMSetCellCoordinateDM/

**Contents:**
- DMSetCellCoordinateDM#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the DM that prescribes cellwise coordinate layout and scatters between global and local cellwise coordinates

cdm - cellwise coordinate DM

As opposed to DMSetCoordinateDM() these coordinates are useful for discontinuous Galerkin methods since they support coordinate fields that are discontinuous at cell boundaries.

DMGetCellCoordinateDM(), DMSetCellCoordinates(), DMSetCellCoordinatesLocal(), DMGetCellCoordinates(), DMGetCellCoordinatesLocal(), DMSetCoordinateDM(), DMGetCoordinateDM()

src/dm/interface/dmcoordinates.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMSetCellCoordinateDM(DM dm, DM cdm)
```

Example 2 (unknown):
```unknown
DMSetCoordinateDM()
```

Example 3 (unknown):
```unknown
DMGetCellCoordinateDM()
```

Example 4 (unknown):
```unknown
DMSetCellCoordinates()
```

---

## DMSetCellCoordinateField#

**URL:** https://petsc.org/release/manualpages/DM/DMSetCellCoordinateField/

**Contents:**
- DMSetCellCoordinateField#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Set the DMField representation of the discontinuous per-cell mesh coordinates

field - the DMField describing the cell coordinates

Cell coordinates support meshes whose coordinate representation is discontinuous at cell boundaries, such as those used by discontinuous Galerkin methods.

DM, DMField, DMSetCoordinateField(), DMGetCellCoordinateDM(), DMSetCellCoordinates()

src/dm/interface/dmcoordinates.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMSetCellCoordinateField(DM dm, DMField field)
```

Example 2 (unknown):
```unknown
DMSetCoordinateField()
```

Example 3 (unknown):
```unknown
DMGetCellCoordinateDM()
```

Example 4 (unknown):
```unknown
DMSetCellCoordinates()
```

---

## DMSetCellCoordinateSection#

**URL:** https://petsc.org/release/manualpages/DM/DMSetCellCoordinateSection/

**Contents:**
- DMSetCellCoordinateSection#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the PetscSection of cellwise coordinate values over the mesh.

dim - The embedding dimension, or PETSC_DETERMINE

section - The PetscSection object for a cellwise layout

DM, DMGetCoordinateDim(), DMSetCoordinateSection(), DMGetCellCoordinateSection(), DMGetCoordinateSection(), DMGetCellCoordinateDM(), DMGetLocalSection(), DMSetLocalSection()

src/dm/interface/dmcoordinates.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMSetCellCoordinateSection(DM dm, PetscInt dim, PetscSection section)
```

Example 3 (unknown):
```unknown
PETSC_DETERMINE
```

Example 4 (unknown):
```unknown
PetscSection
```

---

## DMSetCellCoordinatesLocal#

**URL:** https://petsc.org/release/manualpages/DM/DMSetCellCoordinatesLocal/

**Contents:**
- DMSetCellCoordinatesLocal#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Sets into the DM a local vector including ghost points that holds the cellwise coordinates

c - cellwise coordinate vector

The coordinates of ghost points can be set using DMSetCoordinates() followed by DMGetCoordinatesLocal(). This is intended to enable the setting of ghost coordinates outside of the domain.

The vector c should be destroyed by the caller.

DM, DMGetCellCoordinatesLocal(), DMSetCellCoordinates(), DMGetCellCoordinates(), DMGetCellCoordinateDM()

src/dm/interface/dmcoordinates.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMSetCellCoordinatesLocal(DM dm, Vec c)
```

Example 2 (unknown):
```unknown
DMSetCoordinates()
```

Example 3 (unknown):
```unknown
DMGetCoordinatesLocal()
```

Example 4 (unknown):
```unknown
DMGetCellCoordinatesLocal()
```

---

## DMSetCellCoordinates#

**URL:** https://petsc.org/release/manualpages/DM/DMSetCellCoordinates/

**Contents:**
- DMSetCellCoordinates#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Sets into the DM a global vector that holds the cellwise coordinates

c - cellwise coordinate vector

The coordinates do not include those for ghost points, which are in the local vector.

The vector c should be destroyed by the caller.

DM, DMGetCoordinates(), DMSetCellCoordinatesLocal(), DMGetCellCoordinates(), DMGetCellCoordinatesLocal(), DMGetCellCoordinateDM()

src/dm/interface/dmcoordinates.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMSetCellCoordinates(DM dm, Vec c)
```

Example 2 (unknown):
```unknown
DMGetCoordinates()
```

Example 3 (unknown):
```unknown
DMSetCellCoordinatesLocal()
```

Example 4 (unknown):
```unknown
DMGetCellCoordinates()
```

---

## DMSetCoarseDM#

**URL:** https://petsc.org/release/manualpages/DM/DMSetCoarseDM/

**Contents:**
- DMSetCoarseDM#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Set the coarse DM from which this DM was obtained by refinement

Normally this is set automatically by DMRefine()

DM Basics, DM, DMGetCoarseDM(), DMCoarsen(), DMSetRefine(), DMSetFineDM()

src/dm/interface/dm.c

src/ts/tutorials/ex30.c src/ksp/ksp/tutorials/ex73.c src/snes/tutorials/ex11.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetCoarseDM(DM dm, DM cdm)
```

Example 2 (unknown):
```unknown
DMGetCoarseDM()
```

Example 3 (unknown):
```unknown
DMCoarsen()
```

Example 4 (unknown):
```unknown
DMSetRefine()
```

---

## DMSetCoarsenLevel#

**URL:** https://petsc.org/release/manualpages/DM/DMSetCoarsenLevel/

**Contents:**
- DMSetCoarsenLevel#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the number of coarsenings that have generated this DM.

level - number of coarsenings

This is rarely used directly, the information is automatically set when a DM is created with DMCoarsen()

DM Basics, DM, DMCoarsen(), DMGetCoarsenLevel(), DMGetRefineLevel(), DMDestroy(), DMView(), DMCreateGlobalVector(), DMCreateInterpolation()

src/dm/interface/dm.c

src/ts/tutorials/ex30.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetCoarsenLevel(DM dm, PetscInt level)
```

Example 2 (unknown):
```unknown
DMCoarsen()
```

Example 3 (unknown):
```unknown
DMCoarsen()
```

Example 4 (unknown):
```unknown
DMGetCoarsenLevel()
```

---

## DMSetCoordinateDim#

**URL:** https://petsc.org/release/manualpages/DM/DMSetCoordinateDim/

**Contents:**
- DMSetCoordinateDim#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the dimension of the embedding space for coordinate values.

dim - The embedding dimension

DM, DMGetCoordinateDim(), DMSetCoordinateSection(), DMGetCoordinateSection(), DMGetLocalSection(), DMSetLocalSection()

src/dm/interface/dmcoordinates.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMSetCoordinateDim(DM dm, PetscInt dim)
```

Example 2 (unknown):
```unknown
DMGetCoordinateDim()
```

Example 3 (unknown):
```unknown
DMSetCoordinateSection()
```

Example 4 (unknown):
```unknown
DMGetCoordinateSection()
```

---

## DMSetCoordinateDisc#

**URL:** https://petsc.org/release/manualpages/DM/DMSetCoordinateDisc/

**Contents:**
- DMSetCoordinateDisc#
- Synopsis#
- Input Parameters#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Set a coordinate space

disc - The new coordinate discretization or NULL to ensure a coordinate discretization exists

localized - Set a localized (DG) coordinate space

project - Project coordinates to new discretization

A PetscFE defines an approximation space using a PetscSpace, which represents the basis functions, and a PetscDualSpace, which defines the interpolation operation in the space.

This function takes the current mesh coordinates, which are discretized using some PetscFE space, and projects this function into a new PetscFE space. The coordinate projection is done on the continuous coordinates, but the discontinuous coordinates are not updated.

With more effort, we could directly project the discontinuous coordinates also.

DM, PetscFE, DMGetCoordinateField()

src/dm/interface/dmcoordinates.c

src/dm/impls/plex/tutorials/ex8.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMSetCoordinateDisc(DM dm, PetscFE disc, PetscBool localized, PetscBool project)
```

Example 2 (unknown):
```unknown
PetscDualSpace
```

Example 3 (unknown):
```unknown
DMGetCoordinateField()
```

---

## DMSetCoordinateDM#

**URL:** https://petsc.org/release/manualpages/DM/DMSetCoordinateDM/

**Contents:**
- DMSetCoordinateDM#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the DM that prescribes coordinate layout and scatters between global and local coordinates

DM, DMGetCoordinateDM(), DMSetCoordinates(), DMGetCellCoordinateDM(), DMSetCoordinatesLocal(), DMGetCoordinates(), DMGetCoordinatesLocal(), DMGSetCellCoordinateDM()

src/dm/interface/dmcoordinates.c

src/snes/tutorials/ex77.c src/snes/tutorials/ex7.c src/ts/tutorials/ex47.c src/snes/tutorials/ex12.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMSetCoordinateDM(DM dm, DM cdm)
```

Example 2 (unknown):
```unknown
DMGetCoordinateDM()
```

Example 3 (unknown):
```unknown
DMSetCoordinates()
```

Example 4 (unknown):
```unknown
DMGetCellCoordinateDM()
```

---

## DMSetCoordinateField#

**URL:** https://petsc.org/release/manualpages/DM/DMSetCoordinateField/

**Contents:**
- DMSetCoordinateField#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the DMField representation of the mesh coordinates

field - the DMField describing the coordinates

DM, DMField, DMGetCoordinateField(), DMSetCoordinateDM(), DMSetCoordinates()

src/dm/interface/dmcoordinates.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMSetCoordinateField(DM dm, DMField field)
```

Example 2 (unknown):
```unknown
DMGetCoordinateField()
```

Example 3 (unknown):
```unknown
DMSetCoordinateDM()
```

Example 4 (unknown):
```unknown
DMSetCoordinates()
```

---

## DMSetCoordinateSection#

**URL:** https://petsc.org/release/manualpages/DM/DMSetCoordinateSection/

**Contents:**
- DMSetCoordinateSection#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the PetscSection of coordinate values over the mesh.

dim - The embedding dimension, or PETSC_DETERMINE

section - The PetscSection object

DM, DMGetCoordinateDim(), DMGetCoordinateSection(), DMGetLocalSection(), DMSetLocalSection()

src/dm/interface/dmcoordinates.c

src/ts/tutorials/ex11.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMSetCoordinateSection(DM dm, PetscInt dim, PetscSection section)
```

Example 3 (unknown):
```unknown
PETSC_DETERMINE
```

Example 4 (unknown):
```unknown
PetscSection
```

---

## DMSetCoordinatesLocal#

**URL:** https://petsc.org/release/manualpages/DM/DMSetCoordinatesLocal/

**Contents:**
- DMSetCoordinatesLocal#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets into the DM a local vector, including ghost points, that holds the coordinates

c - coordinate vector

The coordinates of ghost points can be set using DMSetCoordinates() followed by DMGetCoordinatesLocal(). This is intended to enable the setting of ghost coordinates outside of the domain.

The vector c should be destroyed by the caller.

DM, DMGetCoordinatesLocal(), DMSetCoordinates(), DMGetCoordinates(), DMGetCoordinateDM()

src/dm/interface/dmcoordinates.c

src/ts/tutorials/ex11.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMSetCoordinatesLocal(DM dm, Vec c)
```

Example 2 (unknown):
```unknown
DMSetCoordinates()
```

Example 3 (unknown):
```unknown
DMGetCoordinatesLocal()
```

Example 4 (unknown):
```unknown
DMGetCoordinatesLocal()
```

---

## DMSetCoordinates#

**URL:** https://petsc.org/release/manualpages/DM/DMSetCoordinates/

**Contents:**
- DMSetCoordinates#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets into the DM a global vector that holds the coordinates

c - coordinate vector

The coordinates do not include those for ghost points, which are in the local vector.

The vector c can be destroyed after the call

DM, DMSetCoordinatesLocal(), DMGetCoordinates(), DMGetCoordinatesLocal(), DMGetCoordinateDM(), DMDASetUniformCoordinates()

src/dm/interface/dmcoordinates.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex16.c src/snes/tutorials/ex76.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMSetCoordinates(DM dm, Vec c)
```

Example 2 (unknown):
```unknown
DMSetCoordinatesLocal()
```

Example 3 (unknown):
```unknown
DMGetCoordinates()
```

Example 4 (unknown):
```unknown
DMGetCoordinatesLocal()
```

---

## DMSetDefaultConstraints#

**URL:** https://petsc.org/release/manualpages/DM/DMSetDefaultConstraints/

**Contents:**
- DMSetDefaultConstraints#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Set the PetscSection and Mat that specify the local constraint interpolation.

section - The PetscSection describing the range of the constraint matrix: relates rows of the constraint matrix to dofs of the default section. Must have a local communicator (PETSC_COMM_SELF or derivative).

mat - The Mat that interpolates local constraints: its width should be the layout size of the default section: NULL indicates no constraints. Must have a local communicator (PETSC_COMM_SELF or derivative).

bias - A bias vector to be added to constrained values in the local vector. NULL indicates no bias. Must have a local communicator (PETSC_COMM_SELF or derivative).

If a constraint matrix is specified, then it is applied during DMGlobalToLocalEnd() when mode is INSERT_VALUES, INSERT_BC_VALUES, or INSERT_ALL_VALUES. Without a constraint matrix, the local vector l returned by DMGlobalToLocalEnd() contains values that have been scattered from a global vector without modification; with a constraint matrix A, l is modified by computing c = A * l + bias, l[s[i]] = c[i], where the scatter s is defined by the PetscSection returned by DMGetDefaultConstraints().

If a constraint matrix is specified, then its adjoint is applied during DMLocalToGlobalBegin() when mode is ADD_VALUES, ADD_BC_VALUES, or ADD_ALL_VALUES. Without a constraint matrix, the local vector l is accumulated into a global vector without modification; with a constraint matrix A, l is first modified by computing c[i] = l[s[i]], l[s[i]] = 0, l = l + A’*c, which is the adjoint of the operation described above. Any bias, if specified, is ignored when accumulating.

This increments the references of the PetscSection, Mat, and Vec, so they user can destroy them.

DM Basics, DM, DMGetDefaultConstraints()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetDefaultConstraints(DM dm, PetscSection section, Mat mat, Vec bias)
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (unknown):
```unknown
PETSC_COMM_SELF
```

---

## DMSetDimension#

**URL:** https://petsc.org/release/manualpages/DM/DMSetDimension/

**Contents:**
- DMSetDimension#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the topological dimension of the DM

dim - The topological dimension

DM Basics, DM, DMGetDimension(), DMCreate()

src/dm/interface/dm.c

src/ksp/ksp/tutorials/ex70.c src/dm/tutorials/ex19.c src/ts/tutorials/ex77.c src/dm/impls/plex/tutorials/ex3f90.F90 src/dm/tutorials/ex21.c src/dm/tutorials/swarm_ex3.c src/dm/impls/swarm/tutorials/ex1.c src/dm/tutorials/ex20.c src/dm/impls/swarm/tutorials/ex1f90.F90

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetDimension(DM dm, PetscInt dim)
```

Example 2 (unknown):
```unknown
DMGetDimension()
```

---

## DMSetFieldAvoidTensor#

**URL:** https://petsc.org/release/manualpages/DM/DMSetFieldAvoidTensor/

**Contents:**
- DMSetFieldAvoidTensor#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set flag to avoid defining the field on tensor cells

avoidTensor - PETSC_TRUE to skip defining the field on tensor cells

DM Basics, DM, DMGetFieldAvoidTensor(), DMSetField(), DMGetField()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetFieldAvoidTensor(DM dm, PetscInt f, PetscBool avoidTensor)
```

Example 2 (unknown):
```unknown
DMGetFieldAvoidTensor()
```

Example 3 (unknown):
```unknown
DMSetField()
```

Example 4 (unknown):
```unknown
DMGetField()
```

---

## DMSetField#

**URL:** https://petsc.org/release/manualpages/DM/DMSetField/

**Contents:**
- DMSetField#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the discretization object for a given DM field. Usually one would call DMAddField() which automatically handles the field numbering.

label - The label indicating the support of the field, or NULL for the entire mesh

disc - The discretization object

DM Basics, DM, DMAddField(), DMGetField()

src/dm/interface/dm.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex26.c src/snes/tutorials/ex17.c src/snes/tutorials/ex8.c src/snes/tutorials/ex23.c src/snes/tutorials/ex64.c src/snes/tutorials/ex62.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMAddField()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetField(DM dm, PetscInt f, DMLabel label, PetscObject disc)
```

Example 3 (unknown):
```unknown
DMAddField()
```

Example 4 (unknown):
```unknown
DMGetField()
```

---

## DMSetFineDM#

**URL:** https://petsc.org/release/manualpages/DM/DMSetFineDM/

**Contents:**
- DMSetFineDM#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Set the fine mesh from which this was obtained by coarsening

Normally this is set automatically by DMCoarsen()

DM Basics, DM, DMGetFineDM(), DMCoarsen(), DMRefine()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetFineDM(DM dm, DM fdm)
```

Example 2 (unknown):
```unknown
DMCoarsen()
```

Example 3 (unknown):
```unknown
DMGetFineDM()
```

Example 4 (unknown):
```unknown
DMCoarsen()
```

---

## DMSetFromOptions#

**URL:** https://petsc.org/release/manualpages/DM/DMSetFromOptions/

**Contents:**
- DMSetFromOptions#
- Synopsis#
- Input Parameter#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

sets parameters in a DM from the options database

dm - the DM object to set options for

-dm_preallocate_only (true|false) - Only preallocate the matrix for DMCreateMatrix() and DMCreateMassMatrix(), but do not fill it with zeros

-dm_vec_type type - type of vector to create inside DM

-dm_mat_type type - type of matrix to create inside DM

-dm_is_coloring_type (global|local) - see ISColoringType

-dm_bind_below n - bind (force execution on CPU) for Vec and Mat objects with local size (number of vector entries or matrix rows) below n; currently only supported for DMDA

-dm_plex_option_phases ph0_, ph1_, … - List of prefixes for option processing phases

-dm_plex_filename str - File containing a mesh

-dm_plex_boundary_filename str - File containing a mesh boundary

-dm_plex_name str - Name of the mesh in the file

-dm_plex_shape shape - The domain shape, such as BOX, SPHERE, etc.

-dm_plex_cell ct - Cell shape

-dm_plex_reference_cell_domain (true|false) - Use a reference cell domain

-dm_plex_dim dim - Set the topological dimension

-dm_plex_simplex (true|false) - PETSC_TRUE for simplex elements, PETSC_FALSE for tensor elements

-dm_plex_interpolate (true|false) - PETSC_TRUE turns on topological interpolation (creating edges and faces)

-dm_plex_orient (true|false) - PETSC_TRUE turns on topological orientation (flipping edges and faces)

-dm_plex_scale sc - Scale factor for mesh coordinates

-dm_coord_remap (true|false) - Map coordinates using a function

-dm_plex_coordinate_dim dim - Change the coordinate dimension of a mesh (usually given with cdm_ prefix)

-dm_coord_map mapname - Select a builtin coordinate map

-dm_coord_map_params p0,p1,p2,… - Set coordinate mapping parameters

-dm_plex_box_faces m,n,p - Number of faces along each dimension

-dm_plex_box_lower x,y,z - Specify lower-left-bottom coordinates for the box

-dm_plex_box_upper x,y,z - Specify upper-right-top coordinates for the box

-dm_plex_box_bd bx,by,bz - Specify the DMBoundaryType for each direction

-dm_plex_sphere_radius r - The sphere radius

-dm_plex_ball_radius r - Radius of the ball

-dm_plex_cylinder_bd bz - Boundary type in the z direction

-dm_plex_cylinder_num_wedges n - Number of wedges around the cylinder

-dm_plex_reorder order - Reorder the mesh using the specified algorithm

-dm_refine_pre n - The number of refinements before distribution

-dm_refine_uniform_pre (true|false) - Flag for uniform refinement before distribution

-dm_refine_volume_limit_pre v - The maximum cell volume after refinement before distribution

-dm_refine n - The number of refinements after distribution

-dm_extrude l - Activate extrusion and specify the number of layers to extrude

-dm_plex_save_transform (true|false) - Save the DMPlexTransform that produced this mesh

-dm_plex_transform_extrude_thickness t - The total thickness of extruded layers

-dm_plex_transform_extrude_use_tensor (true|false) - Use tensor cells when extruding

-dm_plex_transform_extrude_symmetric (true|false) - Extrude layers symmetrically about the surface

-dm_plex_transform_extrude_normal n0,…,nd - Specify the extrusion direction

-dm_plex_transform_extrude_thicknesses t0,…,tl - Specify thickness of each layer

-dm_plex_create_fv_ghost_cells - Flag to create finite volume ghost cells on the boundary

-dm_plex_fv_ghost_cells_label name - Label name for ghost cells boundary

-dm_distribute (true|false) - Flag to redistribute a mesh among processes

-dm_distribute_overlap n - The size of the overlap halo

-dm_plex_adj_cone (true|false) - Set adjacency direction

-dm_plex_adj_closure (true|false) - Set adjacency size

-dm_plex_use_ceed (true|false) - Use LibCEED as the FEM backend

-dm_plex_check_symmetry (true|false) - Check that the adjacency information in the mesh is symmetric - DMPlexCheckSymmetry()

-dm_plex_check_skeleton (true|false) - Check that each cell has the correct number of vertices (only for homogeneous simplex or tensor meshes) - DMPlexCheckSkeleton()

-dm_plex_check_faces (true|false) - Check that the faces of each cell give a vertex order this is consistent with what we expect from the cell type - DMPlexCheckFaces()

-dm_plex_check_geometry (true|false) - Check that cells have positive volume - DMPlexCheckGeometry()

-dm_plex_check_pointsf (true|false) - Check some necessary conditions for PointSF - DMPlexCheckPointSF()

-dm_plex_check_interface_cones (true|false) - Check points on inter-partition interfaces have conforming order of cone points - DMPlexCheckInterfaceCones()

-dm_plex_check_all (true|false) - Perform all the checks above

For some DMType such as DMDA this cannot be called after DMSetUp() has been called.

DM Basics, DM, DMView(), DMCreateGlobalVector(), DMCreateInterpolation(), DMCreateColoring(), DMCreateMatrix(), DMPlexCheckSymmetry(), DMPlexCheckSkeleton(), DMPlexCheckFaces(), DMPlexCheckGeometry(), DMPlexCheckPointSF(), DMPlexCheckInterfaceCones(), DMSetOptionsPrefix(), DMType, DMPLEX, DMDA, DMSetUp()

src/dm/interface/dm.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex14.c src/snes/tutorials/ex18.c src/snes/tutorials/ex35.c src/snes/tutorials/ex40f90.F90 src/snes/tutorials/ex12.c src/snes/tutorials/ex17.c src/snes/tutorials/ex33.c src/snes/tutorials/ex23.c src/snes/tutorials/ex21.c

DMSetFromOptions_DA() in src/dm/impls/da/dacreate.c DMSetFromOptions_Forest() in src/dm/impls/forest/forest.c DMSetFromOptions_pforest() in src/dm/impls/forest/p4est/pforest.h DMSetFromOptions_Moab() in src/dm/impls/moab/dmmoab.cxx DMSetFromOptions_Network() in src/dm/impls/network/networkcreate.c DMSetFromOptions_Patch() in src/dm/impls/patch/patchcreate.c DMSetFromOptions_Plex() in src/dm/impls/plex/plexcreate.c DMSetFromOptions_Stag() in src/dm/impls/stag/stag.c DMSetFromOptions_Swarm() in src/dm/impls/swarm/swarm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetFromOptions(DM dm)
```

Example 2 (unknown):
```unknown
DMCreateMatrix()
```

Example 3 (unknown):
```unknown
DMCreateMassMatrix()
```

Example 4 (unknown):
```unknown
ISColoringType
```

---

## DMSetGlobalSection#

**URL:** https://petsc.org/release/manualpages/DM/DMSetGlobalSection/

**Contents:**
- DMSetGlobalSection#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Set the PetscSection encoding the global data layout for the DM.

section - The PetscSection, or NULL

Any existing PetscSection will be destroyed

DM Basics, DM, DMGetGlobalSection(), DMSetLocalSection()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetGlobalSection(DM dm, PetscSection section)
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (unknown):
```unknown
DMGetGlobalSection()
```

---

## DMSetISColoringType#

**URL:** https://petsc.org/release/manualpages/DM/DMSetISColoringType/

**Contents:**
- DMSetISColoringType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Sets the type of coloring, IS_COLORING_GLOBAL or IS_COLORING_LOCAL that is created by the DM

ctype - the matrix type

-dm_is_coloring_type (global|local) - see ISColoringType

DM Basics, DM, DMDACreate1d(), DMDACreate2d(), DMDACreate3d(), DMCreateMatrix(), DMCreateMassMatrix(), DMSetMatrixPreallocateOnly(), MatType, DMGetMatType(), DMGetISColoringType(), ISColoringType, IS_COLORING_GLOBAL, IS_COLORING_LOCAL

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
IS_COLORING_GLOBAL
```

Example 2 (unknown):
```unknown
IS_COLORING_LOCAL
```

Example 3 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetISColoringType(DM dm, ISColoringType ctype)
```

Example 4 (unknown):
```unknown
ISColoringType
```

---

## DMSetLabelOutput#

**URL:** https://petsc.org/release/manualpages/DM/DMSetLabelOutput/

**Contents:**
- DMSetLabelOutput#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set if a given label should be saved to a PetscViewer in calls to DMView()

name - The label name

output - PETSC_TRUE to save the label to the viewer

DM Basics, DM, DMLabel, DMGetOutputFlag(), DMGetLabelOutput(), DMCreateLabel(), DMHasLabel(), DMGetLabelValue(), DMSetLabelValue(), DMGetStratumIS()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetLabelOutput(DM dm, const char name[], PetscBool output)
```

Example 3 (unknown):
```unknown
DMGetOutputFlag()
```

Example 4 (unknown):
```unknown
DMGetLabelOutput()
```

---

## DMSetLabelValue#

**URL:** https://petsc.org/release/manualpages/DM/DMSetLabelValue/

**Contents:**
- DMSetLabelValue#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Add a point to a DMLabel with given value

name - The label name

point - The mesh point

value - The label value for this point

DM Basics, DM, DMLabelSetValue(), DMGetStratumIS(), DMClearLabelValue()

src/dm/interface/dm.c

src/snes/tutorials/ex56.c src/snes/tutorials/ex77.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetLabelValue(DM dm, const char name[], PetscInt point, PetscInt value)
```

Example 2 (unknown):
```unknown
DMLabelSetValue()
```

Example 3 (unknown):
```unknown
DMGetStratumIS()
```

Example 4 (unknown):
```unknown
DMClearLabelValue()
```

---

## DMSetLabel#

**URL:** https://petsc.org/release/manualpages/DM/DMSetLabel/

**Contents:**
- DMSetLabel#
- Synopsis#
- Input Parameters#
- Default labels in a DMPLEX#
- See Also#
- Level#
- Location#

Replaces the label of a given name, or ignores it if the name is not present

label - The DMLabel, having the same name, to substitute

“depth” - Holds the depth (co-dimension) of each mesh point

“celltype” - Holds the topological type of each cell

“ghost” - If the DM is distributed with overlap, this marks the cells and faces in the overlap

“Cell Sets” - Mirrors the cell sets defined by GMsh and ExodusII

“Face Sets” - Mirrors the face sets defined by GMsh and ExodusII

“Vertex Sets” - Mirrors the vertex sets defined by GMsh

DM Basics, DM, DMLabel, DMCreateLabel(), DMHasLabel(), DMPlexGetDepthLabel(), DMPlexGetCellType()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetLabel(DM dm, DMLabel label)
```

Example 2 (unknown):
```unknown
DMCreateLabel()
```

Example 3 (unknown):
```unknown
DMHasLabel()
```

Example 4 (unknown):
```unknown
DMPlexGetDepthLabel()
```

---

## DMSetLocalSection#

**URL:** https://petsc.org/release/manualpages/DM/DMSetLocalSection/

**Contents:**
- DMSetLocalSection#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Set the PetscSection encoding the local data layout for the DM.

section - The PetscSection

Any existing Section will be destroyed

DM Basics, DM, PetscSection, DMGetLocalSection(), DMSetGlobalSection()

src/dm/interface/dm.c

src/ts/tutorials/ex11.c src/dm/impls/plex/tutorials/ex6.c src/ts/tutorials/ex30.c src/ts/tutorials/ex52.c src/dm/impls/plex/tutorials/ex1.c src/ts/tutorials/ex18.c src/dm/impls/plex/tutorials/ex14.c src/dm/impls/plex/tutorials/ex7.c src/dm/impls/plex/tutorials/ex15.c src/snes/tutorials/ex7.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetLocalSection(DM dm, PetscSection section)
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

## DMSetMatrixPreallocateOnly#

**URL:** https://petsc.org/release/manualpages/DM/DMSetMatrixPreallocateOnly/

**Contents:**
- DMSetMatrixPreallocateOnly#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

When DMCreateMatrix() is called the matrix will be properly preallocated but the nonzero structure and zero values will not be set.

only - PETSC_TRUE if only want preallocation

-dm_preallocate_only - Only preallocate the matrix for DMCreateMatrix(), DMCreateMassMatrix(), but do not fill it with zeros

DM Basics, DM, DMCreateMatrix(), DMCreateMassMatrix(), DMSetMatrixStructureOnly(), DMSetMatrixPreallocateSkip()

src/dm/interface/dm.c

src/ts/tutorials/ex50.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/dm/impls/stag/tutorials/ex8.c src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateMatrix()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetMatrixPreallocateOnly(DM dm, PetscBool only)
```

Example 3 (unknown):
```unknown
DMCreateMatrix()
```

Example 4 (unknown):
```unknown
DMCreateMassMatrix()
```

---

## DMSetMatrixPreallocateSkip#

**URL:** https://petsc.org/release/manualpages/DM/DMSetMatrixPreallocateSkip/

**Contents:**
- DMSetMatrixPreallocateSkip#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

When DMCreateMatrix() is called the matrix sizes and ISLocalToGlobalMapping will be properly set, but the data structures to store values in the matrices will not be preallocated.

skip - PETSC_TRUE to skip preallocation

This is most useful to reduce initialization costs when MatSetPreallocationCOO() and MatSetValuesCOO() will be used.

DM Basics, DM, DMCreateMatrix(), DMSetMatrixStructureOnly(), DMSetMatrixPreallocateOnly()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateMatrix()
```

Example 2 (unknown):
```unknown
ISLocalToGlobalMapping
```

Example 3 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetMatrixPreallocateSkip(DM dm, PetscBool skip)
```

Example 4 (unknown):
```unknown
MatSetPreallocationCOO()
```

---

## DMSetMatrixStructureOnly#

**URL:** https://petsc.org/release/manualpages/DM/DMSetMatrixStructureOnly/

**Contents:**
- DMSetMatrixStructureOnly#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

When DMCreateMatrix() is called, the matrix nonzero structure will be created but the array for numerical values will not be allocated.

only - PETSC_TRUE if you only want matrix nonzero structure

DM Basics, DM, DMCreateMatrix(), DMSetMatrixPreallocateOnly(), DMSetMatrixPreallocateSkip()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateMatrix()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetMatrixStructureOnly(DM dm, PetscBool only)
```

Example 3 (unknown):
```unknown
DMCreateMatrix()
```

Example 4 (unknown):
```unknown
DMSetMatrixPreallocateOnly()
```

---

## DMSetMatType#

**URL:** https://petsc.org/release/manualpages/DM/DMSetMatType/

**Contents:**
- DMSetMatType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

Sets the type of matrix created with DMCreateMatrix()

ctype - the matrix type, for example MATMPIAIJ

-dm_mat_type ctype - the type of the matrix to create, see MatType

DM Basics, DM, MatType, DMDACreate1d(), DMDACreate2d(), DMDACreate3d(), DMCreateMatrix(), DMCreateMassMatrix(), DMSetMatrixPreallocateOnly(), DMGetMatType(), DMCreateGlobalVector(), DMCreateLocalVector()

src/dm/interface/dm.c

src/snes/tutorials/ex5f90.F90 src/snes/tutorials/ex55.c src/snes/tutorials/ex14.c src/ksp/ksp/tutorials/ex70.c src/snes/tutorials/ex35.c src/snes/tutorials/ex58.c src/ksp/ksp/tutorials/ex49.c src/snes/tutorials/ex48.c src/snes/tutorials/ex5f90t.F90 src/snes/tutorials/ex77.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateMatrix()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetMatType(DM dm, MatType ctype)
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

## DMSetNaturalSF#

**URL:** https://petsc.org/release/manualpages/DM/DMSetNaturalSF/

**Contents:**
- DMSetNaturalSF#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the PetscSF encoding the map back to the original mesh ordering

DM Basics, DM, DMGetNaturalSF(), DMSetUseNatural(), DMGetUseNatural(), DMPlexCreateGlobalToNaturalSF(), DMPlexDistribute()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetNaturalSF(DM dm, PetscSF sf)
```

Example 2 (unknown):
```unknown
DMGetNaturalSF()
```

Example 3 (unknown):
```unknown
DMSetUseNatural()
```

Example 4 (unknown):
```unknown
DMGetUseNatural()
```

---

## DMSetNearNullSpaceConstructor#

**URL:** https://petsc.org/release/manualpages/DM/DMSetNearNullSpaceConstructor/

**Contents:**
- DMSetNearNullSpaceConstructor#
- Synopsis#
- Input Parameters#
- Calling sequence of nullsp#
- See Also#
- Level#
- Location#
- Examples#

Provide a callback function which constructs the near-nullspace for a given field, defined with DMAddField()

Logically Collective; No Fortran Support

field - The field number for the nullspace

nullsp - A callback to create the near-nullspace

origField - The field number given above, in the original DM

field - The field number in dm

nullSpace - The nullspace for the given field

DM Basics, DM, DMAddField(), DMGetNearNullSpaceConstructor(), DMSetNullSpaceConstructor(), DMGetNullSpaceConstructor(), DMCreateSubDM(), DMCreateSuperDM(), MatNullSpace

src/dm/interface/dm.c

src/snes/tutorials/ex17.c src/ts/tutorials/ex53.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMAddField()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetNearNullSpaceConstructor(DM dm, PetscInt field, PetscErrorCode (*nullsp)(DM dm, PetscInt origField, PetscInt field, MatNullSpace *nullSpace))
```

Example 3 (unknown):
```unknown
DMAddField()
```

Example 4 (unknown):
```unknown
DMGetNearNullSpaceConstructor()
```

---

## DMSetNullSpaceConstructor#

**URL:** https://petsc.org/release/manualpages/DM/DMSetNullSpaceConstructor/

**Contents:**
- DMSetNullSpaceConstructor#
- Synopsis#
- Input Parameters#
- Calling sequence of nullsp#
- See Also#
- Level#
- Location#
- Examples#

Provide a callback function which constructs the nullspace for a given field, defined with DMAddField(), when function spaces are joined or split, such as in DMCreateSubDM()

Logically Collective; No Fortran Support

field - The field number for the nullspace

nullsp - A callback to create the nullspace

origField - The field number given above, in the original DM

field - The field number in dm

nullSpace - The nullspace for the given field

DM Basics, DM, DMAddField(), DMGetNullSpaceConstructor(), DMSetNearNullSpaceConstructor(), DMGetNearNullSpaceConstructor(), DMCreateSubDM(), DMCreateSuperDM()

src/dm/interface/dm.c

src/snes/tutorials/ex76.c src/ts/tutorials/ex30.c src/ts/tutorials/ex76.c src/ts/tutorials/ex77.c src/snes/tutorials/ex69.c src/snes/tutorials/ex62.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMAddField()
```

Example 2 (unknown):
```unknown
DMCreateSubDM()
```

Example 3 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetNullSpaceConstructor(DM dm, PetscInt field, PetscErrorCode (*nullsp)(DM dm, PetscInt origField, PetscInt field, MatNullSpace *nullSpace))
```

Example 4 (unknown):
```unknown
DMAddField()
```

---

## DMSetNumFields#

**URL:** https://petsc.org/release/manualpages/DM/DMSetNumFields/

**Contents:**
- DMSetNumFields#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the number of fields in the DM

numFields - The number of fields

DM Basics, DM, DMGetNumFields(), DMSetField()

src/dm/interface/dm.c

src/dm/impls/plex/tutorials/ex1f90.F90 src/dm/impls/plex/tutorials/ex6.c src/ts/tutorials/ex30.c src/ts/tutorials/ex52.c src/dm/impls/plex/tutorials/ex1.c src/dm/impls/plex/tutorials/ex14.c src/dm/impls/plex/tutorials/ex14f90.F90 src/tao/tutorials/ex3.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetNumFields(DM dm, PetscInt numFields)
```

Example 2 (unknown):
```unknown
DMGetNumFields()
```

Example 3 (unknown):
```unknown
DMSetField()
```

---

## DMSetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/DM/DMSetOptionsPrefix/

**Contents:**
- DMSetOptionsPrefix#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the prefix prepended to all option names when searching through the options database

prefix - the prefix to prepend

A hyphen (-) must NOT be given at the beginning of the prefix name. The first character of all runtime options is AUTOMATICALLY the hyphen.

DM Basics, DM, PetscObjectSetOptionsPrefix(), DMSetFromOptions()

src/dm/interface/dm.c

src/snes/tutorials/ex28.c src/ts/tutorials/ex14.c src/snes/tutorials/ex11.c src/snes/tutorials/ex73f90t.F90 src/dm/tutorials/ex19.c src/dm/impls/plex/tutorials/ex16.c src/dm/impls/plex/tutorials/ex5.c src/dm/impls/plex/tutorials/ex15.c src/snes/tutorials/ex22.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetOptionsPrefix(DM dm, const char prefix[])
```

Example 2 (unknown):
```unknown
PetscObjectSetOptionsPrefix()
```

Example 3 (unknown):
```unknown
DMSetFromOptions()
```

---

## DMSetOutputSequenceNumber#

**URL:** https://petsc.org/release/manualpages/DM/DMSetOutputSequenceNumber/

**Contents:**
- DMSetOutputSequenceNumber#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Set the sequence number/value for output

num - The output sequence number

val - The output sequence value

This is intended for output that should appear in sequence, for instance a set of timesteps in an PETSCVIEWERHDF5 file, or a set of realizations of a stochastic system.

DM Basics, DM, VecView()

src/dm/interface/dm.c

src/ts/tutorials/ex30.c src/ts/tutorials/ex18.c src/ts/tutorials/ex76.c src/ts/utils/dmplexlandau/tutorials/ex1.c src/ts/tutorials/ex48.c src/ts/tutorials/ex77.c src/ts/tutorials/ex53.c src/ts/utils/dmplexlandau/tutorials/ex2.c src/ts/tutorials/ex47.c src/ts/utils/dmplexlandau/tutorials/ex1f90.F90

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetOutputSequenceNumber(DM dm, PetscInt num, PetscReal val)
```

Example 2 (unknown):
```unknown
PETSCVIEWERHDF5
```

---

## DMSetPeriodicity#

**URL:** https://petsc.org/release/manualpages/DM/DMSetPeriodicity/

**Contents:**
- DMSetPeriodicity#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the description of mesh periodicity

maxCell - Over distances greater than this, we can assume a point has crossed over to another sheet, when trying to localize cell coordinates. Pass NULL to remove such information.

Lstart - If we assume the mesh is a torus, this is the start of each coordinate, or NULL for 0.0

L - If we assume the mesh is a torus, this is the length of each coordinate, otherwise it is < 0.0

DM, DMGetPeriodicity()

src/dm/interface/dmperiodicity.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMSetPeriodicity(DM dm, const PetscReal maxCell[], const PetscReal Lstart[], const PetscReal L[])
```

Example 2 (unknown):
```unknown
DMGetPeriodicity()
```

---

## DMSetPointSF#

**URL:** https://petsc.org/release/manualpages/DM/DMSetPointSF/

**Contents:**
- DMSetPointSF#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the PetscSF encoding the parallel section point overlap for the DM.

DM Basics, DM, DMGetPointSF(), DMGetSectionSF(), DMSetSectionSF(), DMCreateSectionSF()

src/dm/interface/dm.c

src/ts/tutorials/ex11.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetPointSF(DM dm, PetscSF sf)
```

Example 2 (unknown):
```unknown
DMGetPointSF()
```

Example 3 (unknown):
```unknown
DMGetSectionSF()
```

Example 4 (unknown):
```unknown
DMSetSectionSF()
```

---

## DMSetRefineLevel#

**URL:** https://petsc.org/release/manualpages/DM/DMSetRefineLevel/

**Contents:**
- DMSetRefineLevel#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the number of refinements that have generated this DM.

level - number of refinements

This value is used by PCMG to determine how many multigrid levels to use

The values are usually set automatically by the process that is causing the refinements of an initial DM by calling this routine.

DM Basics, DM, DMGetRefineLevel(), DMCoarsen(), DMGetCoarsenLevel(), DMDestroy(), DMView(), DMCreateGlobalVector(), DMCreateInterpolation()

src/dm/interface/dm.c

src/ts/tutorials/ex30.c src/ksp/ksp/tutorials/ex65.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetRefineLevel(DM dm, PetscInt level)
```

Example 2 (unknown):
```unknown
DMGetRefineLevel()
```

Example 3 (unknown):
```unknown
DMCoarsen()
```

Example 4 (unknown):
```unknown
DMGetCoarsenLevel()
```

---

## DMSetRegionDS#

**URL:** https://petsc.org/release/manualpages/DM/DMSetRegionDS/

**Contents:**
- DMSetRegionDS#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Set the PetscDS for a given mesh region, defined by a DMLabel

label - The DMLabel defining the mesh region, or NULL for the entire mesh

fields - The IS containing the DM field numbers for the fields in this PetscDS, or NULL for all fields

ds - The PetscDS defined on the given region

dsIn - The PetscDS for input on the given cell, or NULL if it is the same PetscDS

If the label has a PetscDS defined, it will be replaced. Otherwise, it will be added to the DM. If the PetscDS is replaced, the fields argument is ignored.

DM Basics, DM, DMGetRegionDS(), DMSetRegionNumDS(), DMGetDS(), DMGetCellDS()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetRegionDS(DM dm, DMLabel label, IS fields, PetscDS ds, PetscDS dsIn)
```

Example 2 (unknown):
```unknown
DMGetRegionDS()
```

Example 3 (unknown):
```unknown
DMSetRegionNumDS()
```

Example 4 (unknown):
```unknown
DMGetCellDS()
```

---

## DMSetRegionNumDS#

**URL:** https://petsc.org/release/manualpages/DM/DMSetRegionNumDS/

**Contents:**
- DMSetRegionNumDS#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the PetscDS for a given mesh region, defined by the region number

num - The region number, in [0, Nds)

label - The region label, or NULL

fields - The IS containing the DM field numbers for the fields in this PetscDS, or NULL to prevent setting

ds - The PetscDS defined on the given region, or NULL to prevent setting

dsIn - The PetscDS for input on the given cell, or NULL if it is the same PetscDS

DM Basics, DM, DMGetRegionDS(), DMSetRegionDS(), DMGetDS(), DMGetCellDS()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetRegionNumDS(DM dm, PetscInt num, DMLabel label, IS fields, PetscDS ds, PetscDS dsIn)
```

Example 2 (unknown):
```unknown
DMGetRegionDS()
```

Example 3 (unknown):
```unknown
DMSetRegionDS()
```

Example 4 (unknown):
```unknown
DMGetCellDS()
```

---

## DMSetSectionSF#

**URL:** https://petsc.org/release/manualpages/DM/DMSetSectionSF/

**Contents:**
- DMSetSectionSF#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Set the PetscSF encoding the parallel dof overlap for the DM

Any previous PetscSF is destroyed

DM Basics, DM, DMGetSectionSF(), DMCreateSectionSF()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetSectionSF(DM dm, PetscSF sf)
```

Example 2 (unknown):
```unknown
DMGetSectionSF()
```

Example 3 (unknown):
```unknown
DMCreateSectionSF()
```

---

## DMSetSnapToGeomModel#

**URL:** https://petsc.org/release/manualpages/DM/DMSetSnapToGeomModel/

**Contents:**
- DMSetSnapToGeomModel#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Choose a geometry model for this DM.

name - A geometry model name, or NULL for the default

DMPlex: Unstructured Grids, DM, DMPLEX, DMRefine(), DMPlexCreate(), DMSnapToGeomModel()

src/dm/interface/dmgeommodel.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h" 
PetscErrorCode DMSetSnapToGeomModel(DM dm, const char name[])
```

Example 2 (unknown):
```unknown
DMPlexCreate()
```

Example 3 (unknown):
```unknown
DMSnapToGeomModel()
```

---

## DMSetSparseLocalize#

**URL:** https://petsc.org/release/manualpages/DM/DMSetSparseLocalize/

**Contents:**
- DMSetSparseLocalize#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Set the flag indicating that DM coordinates should be localized only for cells near the periodic boundary.

sparse - PETSC_TRUE if only cells near the periodic boundary are localized

If previous cell coordinates existed with a different sparse localization then these will be destroyed.

DMGetSparseLocalize(), DMLocalizeCoordinates(), DMSetPeriodicity()

src/dm/interface/dmperiodicity.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
PetscErrorCode DMSetSparseLocalize(DM dm, PetscBool sparse)
```

Example 2 (unknown):
```unknown
DMGetSparseLocalize()
```

Example 3 (unknown):
```unknown
DMLocalizeCoordinates()
```

Example 4 (unknown):
```unknown
DMSetPeriodicity()
```

---

## DMSetStratumIS#

**URL:** https://petsc.org/release/manualpages/DM/DMSetStratumIS/

**Contents:**
- DMSetStratumIS#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the points in a label stratum

name - The label name

value - The stratum value

points - The stratum points

DM Basics, DM, DMLabel, DMClearLabelStratum(), DMLabelClearStratum(), DMLabelSetStratumIS(), DMGetStratumSize()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetStratumIS(DM dm, const char name[], PetscInt value, IS points)
```

Example 2 (unknown):
```unknown
DMClearLabelStratum()
```

Example 3 (unknown):
```unknown
DMLabelClearStratum()
```

Example 4 (unknown):
```unknown
DMLabelSetStratumIS()
```

---

## DMSetType#

**URL:** https://petsc.org/release/manualpages/DM/DMSetType/

**Contents:**
- DMSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Builds a DM, for a particular DM implementation.

method - The name of the DMType, for example DMDA, DMPLEX

-dm_type type - Sets the DM type; use -help for a list of available types

Of the DM is constructed by directly calling a function to construct a particular DM, for example, DMDACreate2d() or DMPlexCreateBoxMesh()

DM Basics, DM, DMType, DMDA, DMPLEX, DMGetType(), DMCreate(), DMDACreate2d()

src/dm/interface/dm.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex26.c src/snes/tutorials/ex17.c src/snes/tutorials/ex8.c src/snes/tutorials/ex23.c src/snes/tutorials/ex7.c src/snes/tutorials/ex62.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetType(DM dm, DMType method)
```

Example 2 (unknown):
```unknown
DMDACreate2d()
```

Example 3 (unknown):
```unknown
DMPlexCreateBoxMesh()
```

Example 4 (unknown):
```unknown
DMGetType()
```

---

## DMSetUp#

**URL:** https://petsc.org/release/manualpages/DM/DMSetUp/

**Contents:**
- DMSetUp#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

sets up the data structures inside a DM object

dm - the DM object to setup

This is usually called after various parameter setting operations and DMSetFromOptions() are called on the DM

DM Basics, DM, DMCreate(), DMSetType(), DMView(), DMCreateGlobalVector(), DMCreateInterpolation(), DMCreateColoring(), DMCreateMatrix()

src/dm/interface/dm.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex14.c src/snes/tutorials/ex18.c src/snes/tutorials/ex15.c src/snes/tutorials/ex35.c src/snes/tutorials/ex40f90.F90 src/snes/tutorials/ex12.c src/snes/tutorials/ex46.c src/snes/tutorials/ex33.c src/snes/tutorials/ex21.c

DMSetUp_Composite() in src/dm/impls/composite/pack.c DMSetUp_DA() in src/dm/impls/da/dareg.c DMSetUp_pforest() in src/dm/impls/forest/p4est/pforest.h DMSetUp_Moab() in src/dm/impls/moab/dmmoab.cxx DMSetUp_Network() in src/dm/impls/network/network.c DMSetUp_Patch() in src/dm/impls/patch/patch.c DMSetUp_Plex() in src/dm/impls/plex/plex.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetUp(DM dm)
```

Example 2 (unknown):
```unknown
DMSetFromOptions()
```

Example 3 (unknown):
```unknown
DMSetType()
```

Example 4 (unknown):
```unknown
DMCreateGlobalVector()
```

---

## DMSetUseNatural#

**URL:** https://petsc.org/release/manualpages/DM/DMSetUseNatural/

**Contents:**
- DMSetUseNatural#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Set the flag for creating a mapping to the natural order when a DM is (re)distributed in parallel

useNatural - PETSC_TRUE to build the mapping to a natural order during distribution

This also causes the map to be build after DMCreateSubDM() and DMCreateSuperDM()

DM Basics, DM, DMGetUseNatural(), DMCreate(), DMPlexDistribute(), DMCreateSubDM(), DMCreateSuperDM()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetUseNatural(DM dm, PetscBool useNatural)
```

Example 2 (unknown):
```unknown
DMCreateSubDM()
```

Example 3 (unknown):
```unknown
DMCreateSuperDM()
```

Example 4 (unknown):
```unknown
DMGetUseNatural()
```

---

## DMSetVariableBounds#

**URL:** https://petsc.org/release/manualpages/DM/DMSetVariableBounds/

**Contents:**
- DMSetVariableBounds#
- Synopsis#
- Input Parameters#
- Calling sequence of f#
- Developer Note#
- See Also#
- Level#
- Location#

sets a function to compute the lower and upper bound vectors for SNESVI.

f - the function that computes variable bounds used by SNESVI (use NULL to cancel a previous function that was set)

lower - the vector to hold the lower bounds

upper - the vector to hold the upper bounds

Should be called DMSetComputeVIBounds() or something similar

DM Basics, DM, DMComputeVariableBounds(), DMHasVariableBounds(), DMView(), DMCreateGlobalVector(), DMCreateInterpolation(), DMCreateColoring(), DMCreateMatrix(), DMCreateMassMatrix(), DMGetApplicationContext(), DMSetJacobian()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetVariableBounds(DM dm, PetscErrorCode (*f)(DM dm, Vec lower, Vec upper))
```

Example 2 (unknown):
```unknown
DMSetComputeVIBounds()
```

Example 3 (unknown):
```unknown
DMComputeVariableBounds()
```

Example 4 (unknown):
```unknown
DMHasVariableBounds()
```

---

## DMSetVecType#

**URL:** https://petsc.org/release/manualpages/DM/DMSetVecType/

**Contents:**
- DMSetVecType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

Sets the type of vector to be created with DMCreateLocalVector() and DMCreateGlobalVector()

dm - initial distributed array

ctype - the vector type, for example VECSTANDARD, VECCUDA, or VECVIENNACL

-dm_vec_type ctype - the type of vector to create

DM Basics, DM, DMCreate(), DMDestroy(), DMDAInterpolationType, VecType, DMGetVecType(), DMSetMatType(), DMGetMatType(), VECSTANDARD, VECCUDA, VECVIENNACL, DMCreateLocalVector(), DMCreateGlobalVector()

src/dm/interface/dm.c

src/snes/tutorials/ex28.c src/snes/tutorials/ex55.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateLocalVector()
```

Example 2 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 3 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSetVecType(DM dm, VecType ctype)
```

Example 4 (unknown):
```unknown
VECSTANDARD
```

---

## DMShellCreate#

**URL:** https://petsc.org/release/manualpages/DM/DMShellCreate/

**Contents:**
- DMShellCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Creates a DMSHELL object, used to manage user-defined problem data

comm - the processors that will share the global vector

DMDestroy(), DMCreateGlobalVector(), DMCreateLocalVector(), DMShellSetContext(), DMShellGetContext()

src/dm/impls/shell/dmshell.c

src/snes/tutorials/ex73f90t.F90 src/ksp/ksp/tutorials/ex65.c src/ksp/ksp/tutorials/ex73.c src/dm/tutorials/swarm_ex3.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellCreate(MPI_Comm comm, DM *dm)
```

Example 2 (unknown):
```unknown
DMDestroy()
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

## DMShellGetCoarsen#

**URL:** https://petsc.org/release/manualpages/DM/DMShellGetCoarsen/

**Contents:**
- DMShellGetCoarsen#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Calling sequence of coarsen#
- See Also#
- Level#
- Location#

Get the routine used to coarsen the DMSHELL

coarsen - the routine that coarsens the DM

fine - the DM to coarsen

comm - the MPI_Comm to share the coarser DM

coarse - the resulting coarse DM

DM, DMSHELL, DMShellSetCoarsen(), DMCoarsen(), DMShellSetRefine(), DMRefine()

src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellGetCoarsen(DM dm, PetscErrorCode (**coarsen)(DM fine, MPI_Comm comm, DM *coarse))
```

Example 2 (unknown):
```unknown
DMShellSetCoarsen()
```

Example 3 (unknown):
```unknown
DMCoarsen()
```

Example 4 (unknown):
```unknown
DMShellSetRefine()
```

---

## DMShellGetContext#

**URL:** https://petsc.org/release/manualpages/DM/DMShellGetContext/

**Contents:**
- DMShellGetContext#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Fortran Notes#
- See Also#
- Level#
- Location#
- Examples#

Returns the user-provided context associated to the DMSHELL

This only works when the context is a Fortran derived type or a PetscObject. Declare ctx with

DM, DMSHELL, DMCreateMatrix(), DMShellSetContext()

src/dm/impls/shell/dmshell.c

src/ksp/ksp/tutorials/ex65.c src/ksp/ksp/tutorials/ex73.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellGetContext(DM dm, PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
PetscObject
```

Example 3 (julia):
```julia
type(tUsertype), pointer :: ctx
```

Example 4 (unknown):
```unknown
DMCreateMatrix()
```

---

## DMShellGetCreateInjection#

**URL:** https://petsc.org/release/manualpages/DM/DMShellGetCreateInjection/

**Contents:**
- DMShellGetCreateInjection#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Calling sequence of inject#
- See Also#
- Level#
- Location#

Get the routine used to create the injection operator

inject - the routine to create the injection

coarse - the DM to inject to

inject - the output injection Mat

DM, DMSHELL, DMShellGetCreateInterpolation(), DMCreateInjection(), DMShellSetContext(), DMShellGetContext()

src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellGetCreateInjection(DM dm, PetscErrorCode (**inject)(DM fine, DM coarse, Mat *inject))
```

Example 2 (unknown):
```unknown
DMShellGetCreateInterpolation()
```

Example 3 (unknown):
```unknown
DMCreateInjection()
```

Example 4 (unknown):
```unknown
DMShellSetContext()
```

---

## DMShellGetCreateInterpolation#

**URL:** https://petsc.org/release/manualpages/DM/DMShellGetCreateInterpolation/

**Contents:**
- DMShellGetCreateInterpolation#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Calling sequence of interp#
- See Also#
- Level#
- Location#

Get the routine used to create the interpolation operator

interp - the routine to create the interpolation

coarse - the DM to refine to

interp - the output interpolation Mat

rscale - an output scaling Vec, see DMCreateInterpolationScale()

DM, DMSHELL, DMShellGetCreateInjection(), DMCreateInterpolation(), DMShellGetCreateRestriction(), DMShellSetContext(), DMShellGetContext()

src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellGetCreateInterpolation(DM dm, PetscErrorCode (**interp)(DM coarse, DM fine, Mat *interp, Vec *rscale))
```

Example 2 (unknown):
```unknown
DMCreateInterpolationScale()
```

Example 3 (unknown):
```unknown
DMShellGetCreateInjection()
```

Example 4 (unknown):
```unknown
DMCreateInterpolation()
```

---

## DMShellGetCreateRestriction#

**URL:** https://petsc.org/release/manualpages/DM/DMShellGetCreateRestriction/

**Contents:**
- DMShellGetCreateRestriction#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Calling sequence of restriction#
- See Also#
- Level#
- Location#

Get the routine used to create the restriction operator

restriction - the routine to create the restriction

coarse - the DM to restrict to

restrct - the output restriction Mat

DM, DMSHELL, DMShellSetCreateInjection(), DMCreateInterpolation(), DMShellSetContext(), DMShellGetContext()

src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellGetCreateRestriction(DM dm, PetscErrorCode (**restriction)(DM fine, DM coarse, Mat *restrct))
```

Example 2 (unknown):
```unknown
restriction
```

Example 3 (unknown):
```unknown
DMShellSetCreateInjection()
```

Example 4 (unknown):
```unknown
DMCreateInterpolation()
```

---

## DMShellGetCreateSubDM#

**URL:** https://petsc.org/release/manualpages/DM/DMShellGetCreateSubDM/

**Contents:**
- DMShellGetCreateSubDM#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Calling sequence of subdm#
- See Also#
- Level#
- Location#

Get the routine used to create a sub DM from the DMSHELL

subdm - the routine to create the decomposition

numFields - the number of fields to create

fields - the fields to create for

is - output, the IS defining the sub DM

DM, DMSHELL, DMCreateSubDM(), DMShellSetCreateSubDM(), DMShellSetContext(), DMShellGetContext()

src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellGetCreateSubDM(DM dm, PetscErrorCode (**subdm)(DM dm, PetscInt numFields, const PetscInt fields[], IS *is, DM *subdm))
```

Example 2 (unknown):
```unknown
DMCreateSubDM()
```

Example 3 (unknown):
```unknown
DMShellSetCreateSubDM()
```

Example 4 (unknown):
```unknown
DMShellSetContext()
```

---

## DMShellGetGlobalVector#

**URL:** https://petsc.org/release/manualpages/DM/DMShellGetGlobalVector/

**Contents:**
- DMShellGetGlobalVector#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Returns the template global vector associated with the DMSHELL, or NULL if it was not set

DM, DMSHELL, DMShellSetGlobalVector(), DMShellSetCreateGlobalVector(), DMCreateGlobalVector()

src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellGetGlobalVector(DM dm, Vec *X)
```

Example 2 (unknown):
```unknown
DMShellSetGlobalVector()
```

Example 3 (unknown):
```unknown
DMShellSetCreateGlobalVector()
```

Example 4 (unknown):
```unknown
DMCreateGlobalVector()
```

---

## DMShellGetRefine#

**URL:** https://petsc.org/release/manualpages/DM/DMShellGetRefine/

**Contents:**
- DMShellGetRefine#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Calling sequence of refine#
- See Also#
- Level#
- Location#

Get the routine used to refine the DMSHELL

refine - the routine that refines the DM

coarse - the DM to refine

comm - the MPI_Comm to share the finer DM

fine - the resulting fine DM

DM, DMSHELL, DMShellSetCoarsen(), DMCoarsen(), DMShellSetRefine(), DMRefine()

src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellGetRefine(DM dm, PetscErrorCode (**refine)(DM coarse, MPI_Comm comm, DM *fine))
```

Example 2 (unknown):
```unknown
DMShellSetCoarsen()
```

Example 3 (unknown):
```unknown
DMCoarsen()
```

Example 4 (unknown):
```unknown
DMShellSetRefine()
```

---

## DMShellSetCoarsen#

**URL:** https://petsc.org/release/manualpages/DM/DMShellSetCoarsen/

**Contents:**
- DMShellSetCoarsen#
- Synopsis#
- Input Parameters#
- Calling sequence of coarsen#
- See Also#
- Level#
- Location#
- Examples#

Set the routine used to coarsen the DMSHELL

coarsen - the routine that coarsens the DM

fine - the DM to coarsen

comm - the MPI_Comm to share the coarser DM

coarse - the resulting coarse DM

DM, DMSHELL, DMShellSetRefine(), DMCoarsen(), DMShellGetCoarsen(), DMShellSetContext(), DMShellGetContext()

src/dm/impls/shell/dmshell.c

src/ksp/ksp/tutorials/ex65.c src/ksp/ksp/tutorials/ex73.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellSetCoarsen(DM dm, PetscErrorCode (*coarsen)(DM fine, MPI_Comm comm, DM *coarse))
```

Example 2 (unknown):
```unknown
DMShellSetRefine()
```

Example 3 (unknown):
```unknown
DMCoarsen()
```

Example 4 (unknown):
```unknown
DMShellGetCoarsen()
```

---

## DMShellSetContext#

**URL:** https://petsc.org/release/manualpages/DM/DMShellSetContext/

**Contents:**
- DMShellSetContext#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

set some data to be usable by this DMSHELL

DM, DMSHELL, DMCreateMatrix(), DMShellGetContext()

src/dm/impls/shell/dmshell.c

src/ksp/ksp/tutorials/ex65.c src/ksp/ksp/tutorials/ex73.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellSetContext(DM dm, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
DMCreateMatrix()
```

Example 3 (unknown):
```unknown
DMShellGetContext()
```

---

## DMShellSetCreateDomainDecompositionScatters#

**URL:** https://petsc.org/release/manualpages/DM/DMShellSetCreateDomainDecompositionScatters/

**Contents:**
- DMShellSetCreateDomainDecompositionScatters#
- Synopsis#
- Input Parameters#
- Calling sequence of scatter#
- See Also#
- Level#
- Location#

Set the routine used to create the scatter contexts for domain decomposition with a DMSHELL

scatter - the routine to create the scatters

dm - the DM to decompose into domains

n - number of subdomains

iscat - output, the inner scatters for the subdomains

oscat - output, outer scatters for the subdomains

gscat - output, the global scatters for the subdomains

DM, DMSHELL, DMCreateDomainDecompositionScatters(), DMShellSetContext(), DMShellGetContext()

src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellSetCreateDomainDecompositionScatters(DM dm, PetscErrorCode (*scatter)(DM dm, PetscInt n, DM subdms[], VecScatter *iscat[], VecScatter *oscat[], VecScatter *gscat[]))
```

Example 2 (unknown):
```unknown
DMCreateDomainDecompositionScatters()
```

Example 3 (unknown):
```unknown
DMShellSetContext()
```

Example 4 (unknown):
```unknown
DMShellGetContext()
```

---

## DMShellSetCreateDomainDecomposition#

**URL:** https://petsc.org/release/manualpages/DM/DMShellSetCreateDomainDecomposition/

**Contents:**
- DMShellSetCreateDomainDecomposition#
- Synopsis#
- Input Parameters#
- Calling sequence of decomp#
- See Also#
- Level#
- Location#

Set the routine used to create a domain decomposition for the DMSHELL

decomp - the routine to create the decomposition

dm - the DM to decompose into domains

len - output, the number of domains (or NULL if not requested)

namelist - output, the name for each domain (or NULL if not requested)

innerlist - output, the global indices for each domain’s inner region (or NULL if not requested)

outerlist - output, the global indices for each domain’s outer region (or NULL if not requested)

dmlist - output, the DMs for each field subproblem (or NULL, if not requested; if NULL is returned, no DMs are defined)

DM, DMSHELL, DMCreateDomainDecomposition(), DMShellSetContext(), DMShellGetContext()

src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellSetCreateDomainDecomposition(DM dm, PetscErrorCode (*decomp)(DM dm, PetscInt *len, char **namelist[], IS *innerlist[], IS *outerlist[], DM *dmlist[]))
```

Example 2 (unknown):
```unknown
DMCreateDomainDecomposition()
```

Example 3 (unknown):
```unknown
DMShellSetContext()
```

Example 4 (unknown):
```unknown
DMShellGetContext()
```

---

## DMShellSetCreateFieldDecomposition#

**URL:** https://petsc.org/release/manualpages/DM/DMShellSetCreateFieldDecomposition/

**Contents:**
- DMShellSetCreateFieldDecomposition#
- Synopsis#
- Input Parameters#
- Calling sequence of decomp#
- See Also#
- Level#
- Location#

Set the routine used to create a decomposition of fields for the DMSHELL

decomp - the routine to create the decomposition

dm - the DM to decompose into fields

len - output, the number of fields (or NULL if not requested)

namelist - output, the name for each field (or NULL if not requested)

islist - output, the global indices for each field (or NULL if not requested)

dmlist - output, the DMs for each field subproblem (or NULL, if not requested; if NULL is returned, no DMs are defined)

DM, DMSHELL, DMCreateFieldDecomposition(), DMShellSetContext(), DMShellGetContext()

src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellSetCreateFieldDecomposition(DM dm, PetscErrorCode (*decomp)(DM dm, PetscInt *len, char **namelist[], IS *islist[], DM *dmlist[]))
```

Example 2 (unknown):
```unknown
DMCreateFieldDecomposition()
```

Example 3 (unknown):
```unknown
DMShellSetContext()
```

Example 4 (unknown):
```unknown
DMShellGetContext()
```

---

## DMShellSetCreateGlobalVector#

**URL:** https://petsc.org/release/manualpages/DM/DMShellSetCreateGlobalVector/

**Contents:**
- DMShellSetCreateGlobalVector#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

sets the routine to create a global vector associated with the DMSHELL

func - the creation routine

g - the global Vec to be created

DM, DMSHELL, DMShellSetGlobalVector(), DMShellSetCreateMatrix(), DMShellSetContext(), DMShellGetContext()

src/dm/impls/shell/dmshell.c

src/ksp/ksp/tutorials/ex65.c src/ksp/ksp/tutorials/ex73.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellSetCreateGlobalVector(DM dm, PetscErrorCode (*func)(DM dm, Vec *g))
```

Example 2 (unknown):
```unknown
DMShellSetGlobalVector()
```

Example 3 (unknown):
```unknown
DMShellSetCreateMatrix()
```

Example 4 (unknown):
```unknown
DMShellSetContext()
```

---

## DMShellSetCreateInjection#

**URL:** https://petsc.org/release/manualpages/DM/DMShellSetCreateInjection/

**Contents:**
- DMShellSetCreateInjection#
- Synopsis#
- Input Parameters#
- Calling sequence of inject#
- See Also#
- Level#
- Location#

Set the routine used to create the injection operator

inject - the routine to create the injection

coarse - the DM to inject to

inject - the output injection Mat

DM, DMSHELL, DMShellSetCreateInterpolation(), DMCreateInjection(), DMShellGetCreateInjection(), DMShellSetContext(), DMShellGetContext()

src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellSetCreateInjection(DM dm, PetscErrorCode (*inject)(DM fine, DM coarse, Mat *inject))
```

Example 2 (unknown):
```unknown
DMShellSetCreateInterpolation()
```

Example 3 (unknown):
```unknown
DMCreateInjection()
```

Example 4 (unknown):
```unknown
DMShellGetCreateInjection()
```

---

## DMShellSetCreateInterpolation#

**URL:** https://petsc.org/release/manualpages/DM/DMShellSetCreateInterpolation/

**Contents:**
- DMShellSetCreateInterpolation#
- Synopsis#
- Input Parameters#
- Calling sequence of interp#
- See Also#
- Level#
- Location#
- Examples#

Set the routine used to create the interpolation operator

interp - the routine to create the interpolation

coarse - the DM to refine to

interp - the output interpolation Mat

rscale - an output scaling Vec, see DMCreateInterpolationScale()

DM, DMSHELL, DMShellSetCreateInjection(), DMCreateInterpolation(), DMShellGetCreateInterpolation(), DMShellSetCreateRestriction(), DMShellSetContext(), DMShellGetContext()

src/dm/impls/shell/dmshell.c

src/ksp/ksp/tutorials/ex65.c src/ksp/ksp/tutorials/ex73.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellSetCreateInterpolation(DM dm, PetscErrorCode (*interp)(DM coarse, DM fine, Mat *interp, Vec *rscale))
```

Example 2 (unknown):
```unknown
DMCreateInterpolationScale()
```

Example 3 (unknown):
```unknown
DMShellSetCreateInjection()
```

Example 4 (unknown):
```unknown
DMCreateInterpolation()
```

---

## DMShellSetCreateLocalVector#

**URL:** https://petsc.org/release/manualpages/DM/DMShellSetCreateLocalVector/

**Contents:**
- DMShellSetCreateLocalVector#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

sets the routine to create a local vector associated with the DMSHELL

func - the creation routine

l - the local Vec to be created

DM, DMSHELL, DMShellSetLocalVector(), DMShellSetCreateMatrix(), DMShellSetContext(), DMShellGetContext()

src/dm/impls/shell/dmshell.c

src/ksp/ksp/tutorials/ex65.c src/ksp/ksp/tutorials/ex73.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellSetCreateLocalVector(DM dm, PetscErrorCode (*func)(DM dm, Vec *l))
```

Example 2 (unknown):
```unknown
DMShellSetLocalVector()
```

Example 3 (unknown):
```unknown
DMShellSetCreateMatrix()
```

Example 4 (unknown):
```unknown
DMShellSetContext()
```

---

## DMShellSetCreateMatrix#

**URL:** https://petsc.org/release/manualpages/DM/DMShellSetCreateMatrix/

**Contents:**
- DMShellSetCreateMatrix#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

sets the routine to create a matrix associated with the DMSHELL

func - the function to create a matrix

mat - the Mat to be created

DM, DMSHELL, DMCreateMatrix(), DMShellSetMatrix(), DMShellSetContext(), DMShellGetContext()

src/dm/impls/shell/dmshell.c

src/ksp/ksp/tutorials/ex65.c src/ksp/ksp/tutorials/ex73.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellSetCreateMatrix(DM dm, PetscErrorCode (*func)(DM dm, Mat *mat))
```

Example 2 (unknown):
```unknown
DMCreateMatrix()
```

Example 3 (unknown):
```unknown
DMShellSetMatrix()
```

Example 4 (unknown):
```unknown
DMShellSetContext()
```

---

## DMShellSetCreateRestriction#

**URL:** https://petsc.org/release/manualpages/DM/DMShellSetCreateRestriction/

**Contents:**
- DMShellSetCreateRestriction#
- Synopsis#
- Input Parameters#
- Calling sequence of restriction#
- See Also#
- Level#
- Location#
- Examples#

Set the routine used to create the restriction operator

restriction - the routine to create the restriction

coarse - the DM to restrict to

restrct - the output restriction Mat

DM, DMSHELL, DMShellSetCreateInjection(), DMCreateInterpolation(), DMShellGetCreateRestriction(), DMShellSetContext(), DMShellGetContext()

src/dm/impls/shell/dmshell.c

src/ksp/ksp/tutorials/ex65.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellSetCreateRestriction(DM dm, PetscErrorCode (*restriction)(DM fine, DM coarse, Mat *restrct))
```

Example 2 (unknown):
```unknown
restriction
```

Example 3 (unknown):
```unknown
DMShellSetCreateInjection()
```

Example 4 (unknown):
```unknown
DMCreateInterpolation()
```

---

## DMShellSetCreateSubDM#

**URL:** https://petsc.org/release/manualpages/DM/DMShellSetCreateSubDM/

**Contents:**
- DMShellSetCreateSubDM#
- Synopsis#
- Input Parameters#
- Calling sequence of subdm#
- See Also#
- Level#
- Location#

Set the routine used to create a sub DM from the DMSHELL

subdm - the routine to create the decomposition

numFields - the number of fields to create

fields - the fields to create for

is - output, the IS defining the sub DM

DM, DMSHELL, DMCreateSubDM(), DMShellGetCreateSubDM(), DMShellSetContext(), DMShellGetContext()

src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellSetCreateSubDM(DM dm, PetscErrorCode (*subdm)(DM dm, PetscInt numFields, const PetscInt fields[], IS *is, DM *subdm))
```

Example 2 (unknown):
```unknown
DMCreateSubDM()
```

Example 3 (unknown):
```unknown
DMShellGetCreateSubDM()
```

Example 4 (unknown):
```unknown
DMShellSetContext()
```

---

## DMShellSetDestroyContext#

**URL:** https://petsc.org/release/manualpages/DM/DMShellSetDestroyContext/

**Contents:**
- DMShellSetDestroyContext#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

set a function that destroys the context provided with DMShellSetContext()

dm - the DM to attach the destroyctx() function to

destroyctx - the function that destroys the context

DM, DMSHELL, DMShellSetContext(), DMShellGetContext()

src/dm/impls/shell/dmshell.c

src/ksp/ksp/tutorials/ex65.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMShellSetContext()
```

Example 2 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellSetDestroyContext(DM dm, PetscCtxDestroyFn *destroyctx)
```

Example 3 (unknown):
```unknown
destroyctx()
```

Example 4 (unknown):
```unknown
DMShellSetContext()
```

---

## DMShellSetGlobalToLocalVecScatter#

**URL:** https://petsc.org/release/manualpages/DM/DMShellSetGlobalToLocalVecScatter/

**Contents:**
- DMShellSetGlobalToLocalVecScatter#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets a VecScatter context for global to local communication

gtol - the global to local VecScatter context

DM, DMSHELL, DMShellSetGlobalToLocal(), DMGlobalToLocalBeginDefaultShell(), DMGlobalToLocalEndDefaultShell()

src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellSetGlobalToLocalVecScatter(DM dm, VecScatter gtol)
```

Example 2 (unknown):
```unknown
DMShellSetGlobalToLocal()
```

Example 3 (unknown):
```unknown
DMGlobalToLocalBeginDefaultShell()
```

Example 4 (unknown):
```unknown
DMGlobalToLocalEndDefaultShell()
```

---

## DMShellSetGlobalToLocal#

**URL:** https://petsc.org/release/manualpages/DM/DMShellSetGlobalToLocal/

**Contents:**
- DMShellSetGlobalToLocal#
- Synopsis#
- Input Parameters#
- Calling sequence of begin#
- Calling sequence of end#
- Note#
- See Also#
- Level#
- Location#

Sets the routines used to perform a global to local scatter

begin - the routine that begins the global to local scatter

end - the routine that ends the global to local scatter

global - the global Vec to be communicated

mode - insert mode of the resulting vector

local - the local Vec to receive the result

global - the global Vec to be communicated

mode - insert mode of the resulting vector

local - the local Vec to receive the result

If these functions are not provided but DMShellSetGlobalToLocalVecScatter() is called then DMGlobalToLocalBeginDefaultShell()/DMGlobalToLocalEndDefaultShell() are used to perform the transfers

DM, DMSHELL, DMShellSetLocalToGlobal(), DMGlobalToLocalBeginDefaultShell(), DMGlobalToLocalEndDefaultShell()

src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
#include "petscdmshell.h"  
PetscErrorCode DMShellSetGlobalToLocal(DM dm, PetscErrorCode (*begin)(DM dm, Vec global, InsertMode mode, Vec local), PetscErrorCode (*end)(DM dm, Vec global, InsertMode mode, Vec local))
```

Example 2 (unknown):
```unknown
DMShellSetGlobalToLocalVecScatter()
```

Example 3 (unknown):
```unknown
DMGlobalToLocalBeginDefaultShell()
```

Example 4 (unknown):
```unknown
DMGlobalToLocalEndDefaultShell()
```

---

## DMShellSetGlobalVector#

**URL:** https://petsc.org/release/manualpages/DM/DMShellSetGlobalVector/

**Contents:**
- DMShellSetGlobalVector#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

sets a template global vector associated with the DMSHELL

DM, DMSHELL, DMCreateGlobalVector(), DMShellSetMatrix(), DMShellSetCreateGlobalVector()

src/dm/impls/shell/dmshell.c

src/snes/tutorials/ex73f90t.F90

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellSetGlobalVector(DM dm, Vec X)
```

Example 2 (unknown):
```unknown
DMCreateGlobalVector()
```

Example 3 (unknown):
```unknown
DMShellSetMatrix()
```

Example 4 (unknown):
```unknown
DMShellSetCreateGlobalVector()
```

---

## DMShellSetLocalToGlobalVecScatter#

**URL:** https://petsc.org/release/manualpages/DM/DMShellSetLocalToGlobalVecScatter/

**Contents:**
- DMShellSetLocalToGlobalVecScatter#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets a VecScatter context for local to global communication

ltog - the local to global VecScatter context

DM, DMSHELL, DMShellSetLocalToGlobal(), DMLocalToGlobalBeginDefaultShell(), DMLocalToGlobalEndDefaultShell()

src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellSetLocalToGlobalVecScatter(DM dm, VecScatter ltog)
```

Example 2 (unknown):
```unknown
DMShellSetLocalToGlobal()
```

Example 3 (unknown):
```unknown
DMLocalToGlobalBeginDefaultShell()
```

Example 4 (unknown):
```unknown
DMLocalToGlobalEndDefaultShell()
```

---

## DMShellSetLocalToGlobal#

**URL:** https://petsc.org/release/manualpages/DM/DMShellSetLocalToGlobal/

**Contents:**
- DMShellSetLocalToGlobal#
- Synopsis#
- Input Parameters#
- Calling sequence of begin#
- Calling sequence of end#
- Note#
- See Also#
- Level#
- Location#

Sets the routines used to perform a local to global scatter

begin - the routine that begins the local to global scatter

end - the routine that ends the local to global scatter

local - the local Vec to be communicated

mode - insert mode of the resulting vector

global - the global Vec to receive the result

local - the local Vec to be communicated

mode - insert mode of the resulting vector

global - the global Vec to receive the result

If these functions are not provided but DMShellSetLocalToGlobalVecScatter() is called then DMLocalToGlobalBeginDefaultShell()/DMLocalToGlobalEndDefaultShell() are used to perform the transfers

DM, DMSHELL, DMShellSetGlobalToLocal(), InsertMode, VecScatter, DMLocalToGlobal(), DMGlobalToLocal()

src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
#include "petscdmshell.h"  
PetscErrorCode DMShellSetLocalToGlobal(DM dm, PetscErrorCode (*begin)(DM dm, Vec local, InsertMode mode, Vec global), PetscErrorCode (*end)(DM dm, Vec local, InsertMode mode, Vec global))
```

Example 2 (unknown):
```unknown
DMShellSetLocalToGlobalVecScatter()
```

Example 3 (unknown):
```unknown
DMLocalToGlobalBeginDefaultShell()
```

Example 4 (unknown):
```unknown
DMLocalToGlobalEndDefaultShell()
```

---

## DMShellSetLocalToLocalVecScatter#

**URL:** https://petsc.org/release/manualpages/DM/DMShellSetLocalToLocalVecScatter/

**Contents:**
- DMShellSetLocalToLocalVecScatter#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets a VecScatter context for local to local communication

ltol - the local to local VecScatter context

DM, DMSHELL, DMShellSetLocalToLocal(), DMLocalToLocalBeginDefaultShell(), DMLocalToLocalEndDefaultShell()

src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellSetLocalToLocalVecScatter(DM dm, VecScatter ltol)
```

Example 2 (unknown):
```unknown
DMShellSetLocalToLocal()
```

Example 3 (unknown):
```unknown
DMLocalToLocalBeginDefaultShell()
```

Example 4 (unknown):
```unknown
DMLocalToLocalEndDefaultShell()
```

---

## DMShellSetLocalToLocal#

**URL:** https://petsc.org/release/manualpages/DM/DMShellSetLocalToLocal/

**Contents:**
- DMShellSetLocalToLocal#
- Synopsis#
- Input Parameters#
- Calling sequence of begin#
- Calling sequence of end#
- Note#
- See Also#
- Level#
- Location#

Sets the routines used to perform a local to local scatter

begin - the routine that begins the local to local scatter

end - the routine that ends the local to local scatter

local - the local Vec to be communicated

mode - insert mode of the resulting vector

nlocal - the local Vec to receive the result

local - the local Vec to be communicated

mode - insert mode of the resulting vector

nlocal - the local Vec to receive the result

If these functions are not provided but DMShellSetLocalToLocalVecScatter() is called then DMLocalToLocalBeginDefaultShell()/DMLocalToLocalEndDefaultShell() are used to perform the transfers

DM, DMSHELL, DMShellSetGlobalToLocal(), DMLocalToLocalBeginDefaultShell(), DMLocalToLocalEndDefaultShell(), DMLocalToLocalBegin(), DMLocalToLocalEnd()

src/dm/impls/shell/dmshell.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
#include "petscdmshell.h"  
PetscErrorCode DMShellSetLocalToLocal(DM dm, PetscErrorCode (*begin)(DM dm, Vec local, InsertMode mode, Vec nlocal), PetscErrorCode (*end)(DM dm, Vec local, InsertMode mode, Vec nlocal))
```

Example 2 (unknown):
```unknown
DMShellSetLocalToLocalVecScatter()
```

Example 3 (unknown):
```unknown
DMLocalToLocalBeginDefaultShell()
```

Example 4 (unknown):
```unknown
DMLocalToLocalEndDefaultShell()
```

---

## DMShellSetLocalVector#

**URL:** https://petsc.org/release/manualpages/DM/DMShellSetLocalVector/

**Contents:**
- DMShellSetLocalVector#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

sets a template local vector associated with the DMSHELL

DM, DMSHELL, DMCreateLocalVector(), DMShellSetMatrix(), DMShellSetCreateLocalVector()

src/dm/impls/shell/dmshell.c

src/snes/tutorials/ex73f90t.F90

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellSetLocalVector(DM dm, Vec X)
```

Example 2 (unknown):
```unknown
DMCreateLocalVector()
```

Example 3 (unknown):
```unknown
DMShellSetMatrix()
```

Example 4 (unknown):
```unknown
DMShellSetCreateLocalVector()
```

---

## DMShellSetMatrix#

**URL:** https://petsc.org/release/manualpages/DM/DMShellSetMatrix/

**Contents:**
- DMShellSetMatrix#
- Synopsis#
- Input Parameters#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#

sets a template matrix associated with the DMSHELL

To avoid circular references, if J is already associated to the same DM, then MatDuplicate(SHARE_NONZERO_PATTERN) is called, followed by removing the DM reference from the private template.

DM, DMSHELL, DMCreateMatrix(), DMShellSetCreateMatrix(), DMShellSetContext(), DMShellGetContext()

src/dm/impls/shell/dmshell.c

src/snes/tutorials/ex73f90t.F90

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellSetMatrix(DM dm, Mat J)
```

Example 2 (unknown):
```unknown
MatDuplicate
```

Example 3 (unknown):
```unknown
SHARE_NONZERO_PATTERN
```

Example 4 (unknown):
```unknown
DMCreateMatrix()
```

---

## DMShellSetRefine#

**URL:** https://petsc.org/release/manualpages/DM/DMShellSetRefine/

**Contents:**
- DMShellSetRefine#
- Synopsis#
- Input Parameters#
- Calling sequence of refine#
- See Also#
- Level#
- Location#
- Examples#

Set the routine used to refine the DMSHELL

refine - the routine that refines the DM

coarse - the DM to refine

comm - the MPI_Comm to share the finer DM

fine - the resulting fine DM

DM, DMSHELL, DMShellSetCoarsen(), DMRefine(), DMShellGetRefine(), DMShellSetContext(), DMShellGetContext()

src/dm/impls/shell/dmshell.c

src/ksp/ksp/tutorials/ex65.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmshell.h"  
PetscErrorCode DMShellSetRefine(DM dm, PetscErrorCode (*refine)(DM coarse, MPI_Comm comm, DM *fine))
```

Example 2 (unknown):
```unknown
DMShellSetCoarsen()
```

Example 3 (unknown):
```unknown
DMShellGetRefine()
```

Example 4 (unknown):
```unknown
DMShellSetContext()
```

---

## DMSHELL#

**URL:** https://petsc.org/release/manualpages/DM/DMSHELL/

**Contents:**
- DMSHELL#
- See Also#
- Level#
- Location#
- Examples#

A DM object that allows users to provide the DM functionality

DMDA - Creating vectors for structured grids, DMType, DMCOMPOSITE, DMSTAG, DMDA, DMDACreate(), DMCreate(), DMSetType(), DMShellCreate(), DMShellSetContext(), DMShellGetContext(), DMShellSetDestroyContext(), DMShellSetMatrix, DMShellSetCreateMatrix(), DMShellSetCreateSubDM(), DMShellGetCreateSubDM(), DMShellSetCreateDomainDecomposition(), DMShellSetCreateDomainDecompositionScatters()

src/dm/impls/shell/dmshell.c

src/ksp/ksp/tutorials/ex65.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCOMPOSITE
```

Example 2 (unknown):
```unknown
DMDACreate()
```

Example 3 (unknown):
```unknown
DMSetType()
```

Example 4 (unknown):
```unknown
DMShellCreate()
```

---

## DMSlicedCreate#

**URL:** https://petsc.org/release/manualpages/DM/DMSlicedCreate/

**Contents:**
- DMSlicedCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Creates a DM object, used to manage data for a unstructured problem

comm - the processors that will share the global vector

nlocal - number of vector entries on this process

Nghosts - number of ghost points needed on this process

ghosts - global indices of all ghost points for this process

d_nnz - matrix preallocation information representing coupling within this process

o_nnz - matrix preallocation information representing coupling between this process and other processes

dm - the slice object

This DM does not support DMCreateLocalVector(), DMGlobalToLocalBegin(), and DMGlobalToLocalEnd() instead one directly uses VecGhostGetLocalForm() and VecGhostRestoreLocalForm() to access the local representation and VecGhostUpdateBegin() and VecGhostUpdateEnd() to update the ghost points.

One can use DMGlobalToLocalBegin(), and DMGlobalToLocalEnd() instead of VecGhostUpdateBegin() and VecGhostUpdateEnd().

DM, DMSLICED, DMDestroy(), DMCreateGlobalVector(), DMSetType(), DMSlicedSetGhosts(), DMSlicedSetPreallocation(), VecGhostUpdateBegin(), VecGhostUpdateEnd(), VecGhostGetLocalForm(), VecGhostRestoreLocalForm()

src/dm/impls/sliced/sliced.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmsliced.h" 
PetscErrorCode DMSlicedCreate(MPI_Comm comm, PetscInt bs, PetscInt nlocal, PetscInt Nghosts, const PetscInt ghosts[], const PetscInt d_nnz[], const PetscInt o_nnz[], DM *dm)
```

Example 2 (unknown):
```unknown
DMCreateLocalVector()
```

Example 3 (unknown):
```unknown
DMGlobalToLocalBegin()
```

Example 4 (unknown):
```unknown
DMGlobalToLocalEnd()
```

---

## DMSlicedSetBlockFills#

**URL:** https://petsc.org/release/manualpages/DM/DMSlicedSetBlockFills/

**Contents:**
- DMSlicedSetBlockFills#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the fill pattern in each block for a multi-component problem of the matrix returned by DMSlicedGetMatrix().

dfill - the fill pattern in the diagonal block (may be NULL, means use dense block)

ofill - the fill pattern in the off-diagonal blocks

This only makes sense for multicomponent problems using scalar matrix formats (AIJ). See DMDASetBlockFills() for example usage.

DM, DMSLICED, DMSlicedGetMatrix(), DMDASetBlockFills()

src/dm/impls/sliced/sliced.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMSlicedGetMatrix()
```

Example 2 (unknown):
```unknown
#include "petscdmsliced.h" 
PetscErrorCode DMSlicedSetBlockFills(DM dm, const PetscInt dfill[], const PetscInt ofill[])
```

Example 3 (unknown):
```unknown
DMDASetBlockFills()
```

Example 4 (unknown):
```unknown
DMSlicedGetMatrix()
```

---

## DMSlicedSetGhosts#

**URL:** https://petsc.org/release/manualpages/DM/DMSlicedSetGhosts/

**Contents:**
- DMSlicedSetGhosts#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the global indices of other processes elements that will be ghosts on this process

dm - the DMSLICED object

nlocal - number of local (owned, non-ghost) blocks

Nghosts - number of ghost blocks on this process

ghosts - global indices of each ghost block

DM, DMSLICED, DMDestroy(), DMCreateGlobalVector()

src/dm/impls/sliced/sliced.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmsliced.h" 
PetscErrorCode DMSlicedSetGhosts(DM dm, PetscInt bs, PetscInt nlocal, PetscInt Nghosts, const PetscInt ghosts[])
```

Example 2 (unknown):
```unknown
DMDestroy()
```

Example 3 (unknown):
```unknown
DMCreateGlobalVector()
```

---

## DMSlicedSetPreallocation#

**URL:** https://petsc.org/release/manualpages/DM/DMSlicedSetPreallocation/

**Contents:**
- DMSlicedSetPreallocation#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

sets the matrix memory preallocation for matrices computed by DMSLICED

d_nz - number of block nonzeros per block row in diagonal portion of local submatrix (same for all local rows)

d_nnz - array containing the number of block nonzeros in the various block rows of the in diagonal portion of the local (possibly different for each block row) or NULL.

o_nz - number of block nonzeros per block row in the off-diagonal portion of local submatrix (same for all local rows).

o_nnz - array containing the number of nonzeros in the various block rows of the off-diagonal portion of the local submatrix (possibly different for each block row) or NULL.

See MatMPIBAIJSetPreallocation() for more details on preallocation. If a scalar matrix (MATAIJ) is obtained with DMSlicedGetMatrix(), the correct preallocation will be set, respecting DMSlicedSetBlockFills().

DM, DMSLICED, DMDestroy(), DMCreateGlobalVector(), MatMPIAIJSetPreallocation(), MatMPIBAIJSetPreallocation(), DMSlicedGetMatrix(), DMSlicedSetBlockFills()

src/dm/impls/sliced/sliced.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdmsliced.h" 
PetscErrorCode DMSlicedSetPreallocation(DM dm, PetscInt d_nz, const PetscInt d_nnz[], PetscInt o_nz, const PetscInt o_nnz[])
```

Example 2 (unknown):
```unknown
MatMPIBAIJSetPreallocation()
```

Example 3 (unknown):
```unknown
DMSlicedGetMatrix()
```

Example 4 (unknown):
```unknown
DMSlicedSetBlockFills()
```

---

## DMSLICED#

**URL:** https://petsc.org/release/manualpages/DM/DMSLICED/

**Contents:**
- DMSLICED#
- See Also#
- Level#
- Location#

“sliced” - A DM object that is used to manage data for a general graph. Uses VecCreateGhost() ghosted vectors for storing the fields See DMCreateSliced() for details.

DMType, DMCOMPOSITE, DMCreateSliced(), DMCreate()

src/dm/impls/sliced/sliced.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecCreateGhost()
```

Example 2 (unknown):
```unknown
DMCreateSliced()
```

Example 3 (unknown):
```unknown
DMCOMPOSITE
```

Example 4 (unknown):
```unknown
DMCreateSliced()
```

---

## DMSnapToGeomModel#

**URL:** https://petsc.org/release/manualpages/DM/DMSnapToGeomModel/

**Contents:**
- DMSnapToGeomModel#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Given a coordinate point ‘mcoords’ on the mesh point ‘p’, return the closest coordinate point ‘gcoords’ on the geometry model associated with that point.

dm - The DMPLEX object

dE - The coordinate dimension

mcoords - A coordinate point lying on the mesh point

gcoords - The closest coordinate point on the geometry model associated with ‘p’ to the given point

Returns the original coordinates if no geometry model is found.

The coordinate dimension may be different from the coordinate dimension of the dm, for example if the transformation is extrusion.

DMPlex: Unstructured Grids, DM, DMPLEX, DMRefine(), DMPlexCreate(), DMPlexSetRefinementUniform()

src/dm/interface/dmgeommodel.c

DMSnapToGeomModel_EGADS() in src/dm/impls/plex/plexegads.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h" 
PetscErrorCode DMSnapToGeomModel(DM dm, PetscInt p, PetscInt dE, const PetscScalar mcoords[], PetscScalar gcoords[])
```

Example 2 (unknown):
```unknown
DMPlexCreate()
```

Example 3 (unknown):
```unknown
DMPlexSetRefinementUniform()
```

---

## DMSubDomainHookAdd#

**URL:** https://petsc.org/release/manualpages/DM/DMSubDomainHookAdd/

**Contents:**
- DMSubDomainHookAdd#
- Synopsis#
- Input Parameters#
- Calling sequence of ddhook#
- Calling sequence of restricthook#
- Notes#
- Developer Note#
- See Also#
- Level#
- Location#

adds a callback to be run when restricting a problem to subdomain DMs with DMCreateDomainDecomposition()

Logically Collective; No Fortran Support

ddhook - function to run to pass data to the decomposition DM upon its creation

restricthook - function to run to update data on block solve (at the beginning of the block solve)

ctx - [optional] application context for provide data for the hooks (may be NULL)

ctx - optional application function context

out - scatter to the outer (with ghost and overlap points) sub vector

in - scatter to sub vector values only owned locally

ctx - optional application function context

This function can be used if auxiliary data needs to be set up on subdomain DMs.

If this function is called multiple times, the hooks will be run in the order they are added.

In order to compose with nonlinear preconditioning without duplicating storage, the hook should be implemented to extract the global information from its context (instead of from the SNES).

It is unclear what “block solve” means within the definition of restricthook

DM Basics, DM, DMSubDomainHookRemove(), DMRefineHookAdd(), SNESFASGetInterpolation(), SNESFASGetInjection(), PetscObjectCompose(), PetscContainerCreate(), DMCreateDomainDecomposition()

src/dm/interface/dm.c

src/ts/tutorials/ex29.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateDomainDecomposition()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSubDomainHookAdd(DM global, PetscErrorCode (*ddhook)(DM global, DM block, PetscCtx ctx), PetscErrorCode (*restricthook)(DM global, VecScatter out, VecScatter in, DM block, PetscCtx ctx), PetscCtx ctx)
```

Example 3 (unknown):
```unknown
restricthook
```

Example 4 (unknown):
```unknown
restricthook
```

---

## DMSubDomainHookRemove#

**URL:** https://petsc.org/release/manualpages/DM/DMSubDomainHookRemove/

**Contents:**
- DMSubDomainHookRemove#
- Synopsis#
- Input Parameters#
- Calling sequence of ddhook#
- Calling sequence of restricthook#
- See Also#
- Level#
- Location#

remove a callback from the list to be run when restricting a problem to subdomain DMs with DMCreateDomainDecomposition()

Logically Collective; No Fortran Support

ddhook - function to run to pass data to the decomposition DM upon its creation

restricthook - function to run to update data on block solve (at the beginning of the block solve)

ctx - [optional] application context for provide data for the hooks (may be NULL)

ctx - optional application function context

oscatter - scatter to the outer (with ghost and overlap points) sub vector

gscatter - scatter to sub vector values only owned locally

ctx - optional application function context

DM Basics, DM, DMSubDomainHookAdd(), SNESFASGetInterpolation(), SNESFASGetInjection(), PetscObjectCompose(), PetscContainerCreate(), DMCreateDomainDecomposition()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMCreateDomainDecomposition()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSubDomainHookRemove(DM global, PetscErrorCode (*ddhook)(DM dm, DM block, PetscCtx ctx), PetscErrorCode (*restricthook)(DM dm, VecScatter oscatter, VecScatter gscatter, DM block, PetscCtx ctx), PetscCtx ctx)
```

Example 3 (unknown):
```unknown
restricthook
```

Example 4 (unknown):
```unknown
DMSubDomainHookAdd()
```

---

## DMSubDomainRestrict#

**URL:** https://petsc.org/release/manualpages/DM/DMSubDomainRestrict/

**Contents:**
- DMSubDomainRestrict#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

restricts user-defined problem data to a subdomain DM by running hooks registered by DMSubDomainHookAdd()

Collective if any hooks are

global - The global DM to use as a base

oscatter - The scatter from domain global vector filling subdomain global vector with overlap

gscatter - The scatter from domain global vector filling subdomain local vector with ghosts

subdm - The subdomain DM to update

DM Basics, DM, DMCoarsenHookAdd(), MatRestrict(), DMCreateDomainDecomposition()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
DMSubDomainHookAdd()
```

Example 2 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMSubDomainRestrict(DM global, VecScatter oscatter, VecScatter gscatter, DM subdm)
```

Example 3 (unknown):
```unknown
DMCoarsenHookAdd()
```

Example 4 (unknown):
```unknown
MatRestrict()
```

---

## DMSwarmProjectFields#

**URL:** https://petsc.org/release/manualpages/DM/DMSwarmProjectFields/

**Contents:**
- DMSwarmProjectFields#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Project a set of swarm fields onto another DM

dm - the DM, or NULL to use the cell DM

nfields - the number of swarm fields to project

fieldnames - the textual names of the swarm fields to project

fields - an array of Vec’s of length nfields

mode - if SCATTER_FORWARD then map particles to the continuum, and if SCATTER_REVERSE map the continuum to particles

Currently, there are two available projection methods. The first is conservative projection, used for a DMPLEX cell DM. The second is the averaging which is used for a DMDA cell DM

where \(\phi_p \) is the swarm field at point \(p\), \(N_i()\) is the cell DM basis function at vertex \(i\), \(dJ\) is the determinant of the cell Jacobian and \(\phi_i\) is the projected vertex value of the field \(\phi\).

The user is responsible for destroying both the array and the individual Vec objects.

For the DMPLEX case, there is only a single vector, so the field layout in the DMPLEX must match the requested fields from the DMSwarm.

For averaging projection, nly swarm fields registered with data type of PETSC_REAL can be projected onto the cell DM, and only swarm fields of block size = 1 can currently be projected.

DM Basics, DMSWARM, DMSwarmSetType(), DMSwarmSetCellDM(), DMSwarmType

src/ksp/ksp/utils/dm/dmproject.c

src/ksp/ksp/tutorials/ex70.c src/dm/impls/swarm/tutorials/ex1.c src/dm/tutorials/ex21.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h" 
#include "petscdmda.h" 
#include "petscdmplex.h" 
#include "petscdmswarm.h" 
#include "petscksp.h" 
PetscErrorCode DMSwarmProjectFields(DM sw, DM dm, PetscInt nfields, const char *fieldnames[], Vec fields[], ScatterMode mode)
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
DMSwarmSetType()
```

---

## DMSwarmProjectGradientFields#

**URL:** https://petsc.org/release/manualpages/DM/DMSwarmProjectGradientFields/

**Contents:**
- DMSwarmProjectGradientFields#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Project the gradient of continuum fields on a mesh onto particle fields in a DMSWARM, or the reverse

dm - the continuum DM (a DMPLEX); if NULL the swarm’s cell DM is used

nfields - the number of fields to project

fieldnames - the names of the swarm fields to receive (or supply) the gradient

fields - the corresponding mesh Vec objects

mode - SCATTER_FORWARD to project mesh field gradients to particles, SCATTER_REVERSE to project particle values back to the mesh

Only DMPLEX cell DMs and single-field projection are currently supported. The swarm field block size must equal the mesh field component count times the coordinate dimension.

DMSWARM, DMPLEX, DMSwarmProjectFields(), DMSwarmVectorDefineFields(), DMSwarmCreateGlobalVectorFromField()

src/ksp/ksp/utils/dm/dmproject.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h" 
#include "petscdmda.h" 
#include "petscdmplex.h" 
#include "petscdmswarm.h" 
#include "petscksp.h" 
PetscErrorCode DMSwarmProjectGradientFields(DM sw, DM dm, PetscInt nfields, const char *fieldnames[], Vec fields[], ScatterMode mode)
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
DMSwarmProjectFields()
```

---

## DMSwarmRemap#

**URL:** https://petsc.org/release/manualpages/DM/DMSwarmRemap/

**Contents:**
- DMSwarmRemap#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Project the swarm fields onto a new set of particles

sw - The DMSWARM object

DM Basics, DMSWARM, DMSwarmMigrate(), DMSwarmCrate()

src/ksp/ksp/utils/dm/dmproject.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h" 
#include "petscdmda.h" 
#include "petscdmplex.h" 
#include "petscdmswarm.h" 
#include "petscksp.h" 
PetscErrorCode DMSwarmRemap(DM sw)
```

Example 2 (unknown):
```unknown
DMSwarmMigrate()
```

Example 3 (unknown):
```unknown
DMSwarmCrate()
```

---

## DMType#

**URL:** https://petsc.org/release/manualpages/DM/DMType/

**Contents:**
- DMType#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#

String with the name of a PETSc DM. These are all the DM provided by PETSc.

These can be used with DMSetType() or the options database key -dm_type to set the specific data structures and algorithms to use with a specific DM. But more commonly one calls directly a constructor for a particular DMType such as DMDACreate()

DM Basics, DMSetType(), DMCreate(), DM, DMDACreate()

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef const char *DMType;
#define DMDA        "da"
#define DMCOMPOSITE "composite"
#define DMSLICED    "sliced"
#define DMSHELL     "shell"
#define DMPLEX      "plex"
#define DMREDUNDANT "redundant"
#define DMPATCH     "patch"
#define DMMOAB      "moab"
#define DMNETWORK   "network"
#define DMFOREST    "forest"
#define DMP4EST     "p4est"
#define DMP8EST     "p8est"
#define DMSWARM     "swarm"
#define DMPRODUCT   "product"
#define DMSTAG      "stag"
```

Example 2 (unknown):
```unknown
DMSetType()
```

Example 3 (unknown):
```unknown
DMDACreate()
```

Example 4 (unknown):
```unknown
DMSetType()
```

---

## DMUniversalLabel#

**URL:** https://petsc.org/release/manualpages/DM/DMUniversalLabel/

**Contents:**
- DMUniversalLabel#
- Synopsis#
- See Also#
- Level#
- Location#

A label that encodes a set of DMLabels, bijectively

DM Basics, DM, DMLabel, DMUniversalLabelCreate()

include/petscdmtypes.h

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_UniversalLabel *DMUniversalLabel;
```

Example 2 (unknown):
```unknown
DMUniversalLabelCreate()
```

---

## DMUseTensorOrder#

**URL:** https://petsc.org/release/manualpages/DM/DMUseTensorOrder/

**Contents:**
- DMUseTensorOrder#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Use a tensor product closure ordering for the default section

tensor - Flag for tensor order

DMPlexSetClosurePermutationTensor(), PetscSectionResetClosurePermutation()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMUseTensorOrder(DM dm, PetscBool tensor)
```

Example 2 (unknown):
```unknown
DMPlexSetClosurePermutationTensor()
```

Example 3 (unknown):
```unknown
PetscSectionResetClosurePermutation()
```

---

## DMViewFromOptions#

**URL:** https://petsc.org/release/manualpages/DM/DMViewFromOptions/

**Contents:**
- DMViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

View a DM in a particular way based on a request in the options database

obj - optional object that provides the prefix for the options database (if NULL then the prefix in obj is used)

name - option string that is used to activate viewing

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

DM Basics, DM, DMView(), PetscObjectViewFromOptions(), DMCreate()

src/dm/interface/dm.c

src/snes/tutorials/ex71.c src/snes/tutorials/ex12.c src/snes/tutorials/ex13.c src/snes/tutorials/ex36.c src/snes/tutorials/ex26.c src/snes/tutorials/ex17.c src/snes/tutorials/ex8.c src/snes/tutorials/ex23.c src/snes/tutorials/ex7.c src/snes/tutorials/ex62.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMViewFromOptions(DM dm, PeOp PetscObject obj, const char name[])
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

## DMView#

**URL:** https://petsc.org/release/manualpages/DM/DMView/

**Contents:**
- DMView#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Views a DM. Depending on the PetscViewer and its PetscViewerFormat it may print some ASCII information about the DM to the screen or a file or save the DM in a binary file to be loaded later or create a visualization of the DM

dm - the DM object to view

-view_pyvista_warp f - Warps the mesh by the active scalar with factor f

-view_pyvista_clip xl,xu,yl,yu,zl,zu - Defines the clipping box

-dm_view_draw_line_color color - Specify the X-window color for cell borders

-dm_view_draw_cell_color color - Specify the X-window color for cells

-dm_view_draw_affine (true|false) - Flag to ignore high-order edges

PetscViewer = PETSCVIEWERHDF5 i.e. HDF5 format can be used with PETSC_VIEWER_HDF5_PETSC as the PetscViewerFormat to save multiple DMPLEX meshes in a single HDF5 file. This in turn requires one to name the DMPLEX object with PetscObjectSetName() before saving it with DMView() and before loading it with DMLoad() for identification of the mesh object.

PetscViewer = PETSCVIEWEREXODUSII i.e. ExodusII format assumes that element blocks (mapped to “Cell sets” labels) consists of sequentially numbered cells.

If dm has been distributed, only the part of the DM on MPI rank 0 (including “ghost” cells and vertices) will be written.

Only TRI, TET, QUAD, and HEX cells are supported in ExodusII.

DMPLEX only represents geometry while most post-processing software expect that a mesh also provides information on the discretization space. This function assumes that the file represents Lagrange finite elements of order 1 or 2. The order of the mesh shall be set using PetscViewerExodusIISetOrder()

Variable names can be set and queried using PetscViewerExodusII[Set/Get][Nodal/Zonal]VariableNames[s].

DM Basics, DM, PetscViewer, PetscViewerFormat, PetscViewerSetFormat(), DMDestroy(), DMCreateGlobalVector(), DMCreateInterpolation(), DMCreateColoring(), DMCreateMatrix(), DMCreateMassMatrix(), DMLoad(), PetscObjectSetName()

src/dm/interface/dm.c

src/dm/tutorials/ex1.c src/snes/tutorials/ex5f90.F90 src/dm/impls/plex/tutorials/ex19.c src/ts/tutorials/ex30.c src/ksp/ksp/tutorials/ex70.c src/ksp/ksp/tutorials/ex73.c src/ts/tutorials/ex48.c src/dm/impls/plex/tutorials/ex5.c src/snes/tutorials/ex5f90t.F90 src/dm/impls/plex/tutorials/ex3f90.F90

DMView_Composite() in src/dm/impls/composite/pack.c DMView_pforest() in src/dm/impls/forest/p4est/pforest.h DMView_Moab() in src/dm/impls/moab/dmmoab.cxx DMView_Network() in src/dm/impls/network/networkview.c DMView_Patch() in src/dm/impls/patch/patch.c DMView_PlexCGNS() in src/dm/impls/plex/cgns/plexcgns2.c DMView_PlexExodusII() in src/dm/impls/plex/exodusii/plexexodusii2.c DMView_Plex() in src/dm/impls/plex/plex.c DMView_Product() in src/dm/impls/product/product.c DMView_Redundant() in src/dm/impls/redundant/dmredundant.c DMView_Shell() in src/dm/impls/shell/dmshell.c DMView_Stag() in src/dm/impls/stag/stag.c DMView_Swarm() in src/dm/impls/swarm/swarm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscViewer
```

Example 2 (unknown):
```unknown
PetscViewerFormat
```

Example 3 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode DMView(DM dm, PetscViewer v)
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## DM#

**URL:** https://petsc.org/release/manualpages/DM/DM/

**Contents:**
- DM#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Abstract PETSc object that manages an abstract grid-like object and its interactions with the algebraic solvers

DM is an orphan initialism or orphan acronym, the letters have no meaning and never did.

DM Basics, DMType, DMGetType(), DMCompositeCreate(), DMDACreate(), DMSetType(), DMDA, DMPLEX, DMSWARM, DMNETWORK, DMCreate()

include/petscdmtypes.h

src/snes/tutorials/ex28.c src/snes/tutorials/ex14.c src/snes/tutorials/ex18.c src/snes/tutorials/ex35.c src/snes/tutorials/ex40f90.F90 src/snes/tutorials/ex12.c src/snes/tutorials/ex17.c src/snes/tutorials/ex33.c src/snes/tutorials/ex23.c src/snes/tutorials/ex21.c

_p_DM in include/petsc/private/dmimpl.h DM_DA in include/petsc/private/dmdaimpl.h DM_Forest in include/petsc/private/dmforestimpl.h DM_Moab in include/petsc/private/dmmbimpl.h DM_Network in include/petsc/private/dmnetworkimpl.h DM_Patch in include/petsc/private/dmpatchimpl.h DM_Plex in include/petsc/private/dmpleximpl.h DM_Product in include/petsc/private/dmproductimpl.h DM_Stag in include/petsc/private/dmstagimpl.h DM_Swarm in include/petsc/private/dmswarmimpl.h DM_Composite in src/dm/impls/composite/packimpl.h DM_Redundant in src/dm/impls/redundant/dmredundant.c DM_Shell in src/dm/impls/shell/dmshell.c DM_Sliced in src/dm/impls/sliced/sliced.c DM_SNESVI in src/snes/impls/vi/rs/virs.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_DM *DM;
```

Example 2 (unknown):
```unknown
DMGetType()
```

Example 3 (unknown):
```unknown
DMCompositeCreate()
```

Example 4 (unknown):
```unknown
DMDACreate()
```

---

## DM Basics#

**URL:** https://petsc.org/release/manual/dmbase/

**Contents:**
- DM Basics#

The previous chapters have focused on the core numerical solvers in PETSc. However, numerical solvers without efficient ways (in both human and machine time) of connecting the solvers to the mathematical models and discretizations, including grids (or meshes) that people wish to build their simulations on, will not get widely used. Thus PETSc provides a set of abstractions represented by the DM object to provide a powerful, comprehensive mechanism for translating the problem specification of a model and its discretization to the language and API of solvers. DM is an orphan initialism or orphan acronym, the letters have no meaning and never did.

Some of the model classes DM currently supports are PDEs on structured and staggered grids with finite difference methods (DMDA – DMDA - Creating vectors for structured grids and DMSTAG – DMSTAG: Staggered, Structured Grid), PDEs on unstructured grids with finite element and finite volume methods (DMPLEX – DMPlex: Unstructured Grids), PDEs on quad and octree-grids (DMFOREST), models on networks (graphs) such as the power grid or river networks (DMNETWORK – Networks), and particle-in-cell simulations (DMSWARM).

In previous chapters, we have demonstrated some simple usage of DM to provide the input for the solvers. In this chapter, and those that follow, we will dive deep into the capabilities of DM.

It is possible to create a DM with

but more commonly, a DM is created with a type-specific constructor; the construction process for each type of DM is discussed in the sections on each DMType. This chapter focuses on commonalities between all the DM so we assume the DM already exists and we wish to work with it.

As discussed earlier, a DM can construct vectors and matrices appropriate for a model and discretization and provide the mapping between the global and local vector representations.

The matrices produced may support MatSetValuesLocal() allowing one to work with the local numbering on each MPI rank. For DMDA one can also use MatSetValuesStencil() and for DMSTAG with DMStagMatSetValuesStencil().

A given DM can be refined for certain DMTypes with DMRefine() or coarsened with DMCoarsen(). Mappings between DMs may be obtained with routines such as DMCreateInterpolation(), DMCreateRestriction() and DMCreateInjection().

One attaches a DM to a PETSc solver object, KSP, SNES, TS, or Tao with

Once the DM is attached, the solver can utilize it to create and process much of the data that the solver needs to set up and implement its solve. For example, with PCMG simply providing a DM can allow it to create all the data structures needed to run geometric multigrid on your problem.

SNES Tutorial ex19 demonstrates how this may be done with DMDA.

See DM Commonalities for an advanced discussion of the commonalities between the various DM. That material should be read after having read the material below for each of the DM.

DM: Interfacing Between Solvers and Models/Discretizations

PetscSection: Connecting Grids to Data

**Examples:**

Example 1 (unknown):
```unknown
DM dm;
DMCreate(MPI_Comm comm, DM *dm);
DMSetType(DM dm, DMType type);
```

Example 2 (unknown):
```unknown
DMCreateLocalVector(DM dm,Vec *l);
DMCreateGlobalVector(DM dm,Vec *g);
DMGlobalToLocal(dm,g,l,INSERT_VALUES);
DMLocalToGlobal(dm,l,g,ADD_VALUES);
DMCreateMatrix(dm,Mat *m);
```

Example 3 (unknown):
```unknown
MatSetValuesLocal()
```

Example 4 (unknown):
```unknown
MatSetValuesStencil()
```

---

## DM Commonalities#

**URL:** https://petsc.org/release/manual/dmcommonality/

**Contents:**
- DM Commonalities#
- DMDA simple structured grids#
- DMSTAG simple stagger grids#
- DMPLEX unstructured meshes#
- DMNETWORK computations on graphs of nodes and connecting edges#
- Is it a programming language issue?#

We have introduced a variety of seemingly very different DM. Here, we will try to explore the commonalities between them to emphasize that despite superficial differences they all tackle the three same basic problems:

How to map between the indices of (geometric) entities, in some physical space such as \(R^3\) or perhaps an abstract space, and the storage location (offsets) of numerical values associated with said entities in PETSc vectors or arrays. In PETSc, these geometric entities are referred to as points.

How to iterate over the entities of interest (for example, points) to produce updates to the numerical values associated with the entities in the PETSc vectors or arrays.

How to store/access the “connectivity information” that is needed at each entity (point) and provides the correct data dependencies needed to compute the numerical updates.

For several DM we will devote a short paragraph for each of the three problems.

For structured grids, DMDA - Creating vectors for structured grids, the indexing is trivial, the points are represented as tuples \((i, j, k)\), where \(l_i \le i \le u_i\), \(l_j \le j \le u_j\), and \(l_k \le k \le u_k.\) DMDAVecGetArray() returns a multidimensional array that trivially provides the mapping from said points to the numerical values. Note that when the programming language gives access to the values in a multi-dimensional array, internally it computes the offset from the beginning of the array using a formula based on the value of \(i\), \(j\), and \(k\) and the array dimensions.

To iterate over the local points, one uses DMDAGetCorners() or DMDAGetGhostCorners() and iterates over the tuples within the bounds. Specific points, for example boundary points, can be skipped or processed differently based on the index values.

For finite difference methods on structured grids using a stencil formula, the “connectivity information” is defined implicitly by the stencil needed by the given discretization and is the same for all grid points (except maybe boundaries or other special points). For example, for the standard seven point stencil computed at the \((i, j, k)\) entity one needs the numerical values at the \((i \pm 1, j, k)\), \((i, j \pm 1, k)\), and \((i, j, k \pm 1)\) entities.

A staggered grid, DMSTAG: Staggered, Structured Grid, extends the idea of a simple structured grid by allowing not only entities associated with grid vertices (or equivalently cells) as with DMDA but also with grid edges, grid faces, and grid cells (also called elements). As with DMDA each type of entity must have the same number of associated numerical values. As with simple structured grids, each cell can be represented as a \((i, j, k)\) tuple. But, in addition we need to represent what vertex, edge, or face of the cell we are referring to. This is done using DMStagStencilLocation. DMStagVecGetArray() returns a multidimensional array indexed by \((i, j, k)\) plus a slot that tells us which entity on the cell is being accessed. Since a staggered grid can have any problem-dependent number of numerical values associated with a given entity type, the function DMStagGetLocationSlot() provides the final index needed for the array access. After this the programming language than computes the offset from the beginning of the array from the provided indices using a simple formula.

To iterate over the local points, one uses DMStagGetCorners() or DMStagGetGhostCorners() and iterates over the tuples within the bounds with an inner iteration of the point entities desired for the application. For example, for a discretization with cell-centered pressures and edge-based velocity the application would process each of these entities.

For finite difference methods on staggered structured grids using a stencil formula the “connectivity information” is again defined implicitly by the stencil needed by the given discretization and is the same for all grid points (except maybe boundaries or other special points). In addition, any required cross coupling between different entities needs to be encoded for the given problem. For example, how do the velocities affect the pressure equation. This information is generally embedded directly in lines of code that implement the finite difference formula and is not represented in the data structures.

For general unstructured grids, DMPlex: Unstructured Grids, there is no formula for computing the offset into the numerical values for an entity on the grid from its point value, since each point can have any number of values which is determined at runtime based on the grid, PDE, and discretization. Hence all the offsets must be managed by DMPLEX. This is the job of PetscSection, PetscSection: Connecting Grids to Data. The process of building a PetscSection computes and stores the offsets and then using the PetscSection gives access to the needed offsets.

For unstructured grids, one does not in general iterate over all the entities on all the points. Rather it iterates over a subset of the points representing a particular entity. For example, when using the finite element method, the application iterates all the points representing elements (cells) using DMPlexGetHeightStratum() to access the chart (beginning and end indices) of the cell entities. Then one uses an associated PetscSection to determine the offsets into vectors or arrays for said points. If needed one can then have an inner iteration over the fields associated with the cell.

For DMPLEX, the connectivity information is defined by a graph (and stored explicitly in a data structure used to store graphs), and the connectivity of a point (entity) is obtained by DMPlexGetTransitiveClosure().

For networks, Networks, the entities are nodes and edges that connect two nodes, each of which can have any number of submodels. Again, in general, there is no formula that can produce the appropriate offset into the numerical values for a given point (node or edge) directly. The routines DMNetworkGetLocalVecOffset() and DMNetworkGetGlobalVecOffset() are used to obtain the needed offsets from a given point (node or edge) and submodel at that point. Internally a PetscSection is used to manage the storage of the offset information but the user-level API does not refer to PetscSection directly, rather one thinks about a collection of submodels at each node and edge of the graph.

To iterate over graph vertices (nodes) one uses DMNetworkGetVertexRange() to provide its chart (the starting and end indices) and DMNetworkGetEdgeRange() to provide the chart of the edges. One can then iterate over the models on each point To iterate over sub-networks one can call DMNetworkGetSubnetwork() for each network which returns lists of the vertex and edge points in said network.

For DMNETWORK, the connectivity information is defined by a graph, which is is query-able at each entity by DMNetworkGetSupportingEdges() and DMNetworkGetConnectedVertices().

Regarding problem 1. Does the need for these various approaches for mapping between the entities and the related array offsets and the large amount of code (in particular PetscSection come from the limitation of programming languages when working with complex multidimensional jagged arrays. Both in constructing such arrays at runtime, that is supplying all the jagged information which depends on the exact problem, and then providing simple syntax to produce the correct offset into the memory for accessing the numerical values when the simple array access methods do not work.

PetscDT: Discretization Technology in PETSc

**Examples:**

Example 1 (unknown):
```unknown
DMDAVecGetArray()
```

Example 2 (unknown):
```unknown
DMDAGetCorners()
```

Example 3 (unknown):
```unknown
DMDAGetGhostCorners()
```

Example 4 (unknown):
```unknown
DMStagStencilLocation
```

---

## MatFDColoringUseDM#

**URL:** https://petsc.org/release/manualpages/DM/MatFDColoringUseDM/

**Contents:**
- MatFDColoringUseDM#
- Synopsis#
- Input Parameters#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

allows a MatFDColoring object to use the DM associated with the matrix to compute a IS_COLORING_LOCAL coloring

coloring - The matrix to get the DM from

fdcoloring - the MatFDColoring object

This routine exists because the PETSc Mat library does not know about the DM objects

DM Basics, DM, MatFDColoring, MatFDColoringCreate(), ISColoringType

src/dm/interface/dm.c

src/snes/tutorials/ex14.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
MatFDColoring
```

Example 2 (unknown):
```unknown
IS_COLORING_LOCAL
```

Example 3 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode MatFDColoringUseDM(Mat coloring, MatFDColoring fdcoloring)
```

Example 4 (unknown):
```unknown
MatFDColoring
```

---

## MatGetDM#

**URL:** https://petsc.org/release/manualpages/DM/MatGetDM/

**Contents:**
- MatGetDM#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

Gets the DM defining the data layout of the matrix

A matrix may not have a DM associated with it

Since the Mat class doesn’t know about the DM class the DM object is associated with the Mat through a PetscObjectCompose() operation

DM Basics, DM, MatSetDM(), DMCreateMatrix(), DMSetMatType()

src/dm/interface/dm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode MatGetDM(Mat A, DM *dm)
```

Example 2 (unknown):
```unknown
PetscObjectCompose()
```

Example 3 (unknown):
```unknown
DMCreateMatrix()
```

Example 4 (unknown):
```unknown
DMSetMatType()
```

---

## MatSetDM#

**URL:** https://petsc.org/release/manualpages/DM/MatSetDM/

**Contents:**
- MatSetDM#
- Synopsis#
- Input Parameters#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the DM defining the data layout of the matrix

This is rarely used in practice, rather DMCreateMatrix() is used to create a matrix associated with a particular DM

Since the Mat class doesn’t know about the DM class the DM object is associated with the Mat through a PetscObjectCompose() operation

DM Basics, DM, MatGetDM(), DMCreateMatrix(), DMSetMatType()

src/dm/interface/dm.c

src/ksp/ksp/tutorials/ex29.c src/ksp/ksp/tutorials/ex34.c src/snes/tutorials/ex22.c src/snes/tutorials/ex35.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode MatSetDM(Mat A, DM dm)
```

Example 2 (unknown):
```unknown
DMCreateMatrix()
```

Example 3 (unknown):
```unknown
PetscObjectCompose()
```

Example 4 (unknown):
```unknown
DMCreateMatrix()
```

---

## PetscDSFinalizePackage#

**URL:** https://petsc.org/release/manualpages/DM/PetscDSFinalizePackage/

**Contents:**
- PetscDSFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function finalizes everything in the PetscDS package. It is called from PetscFinalize().

src/dm/interface/dlregisdmdm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscDSFinalizePackage(void)
```

Example 3 (unknown):
```unknown
PetscInitialize()
```

---

## PetscDSInitializePackage#

**URL:** https://petsc.org/release/manualpages/DM/PetscDSInitializePackage/

**Contents:**
- PetscDSInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function initializes everything in the PetscDS package. It is called from PetscDLLibraryRegister() when using dynamic libraries, and on the first call to PetscDSCreate() when using static libraries.

src/dm/interface/dlregisdmdm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDLLibraryRegister()
```

Example 2 (unknown):
```unknown
PetscDSCreate()
```

Example 3 (unknown):
```unknown
PetscErrorCode PetscDSInitializePackage(void)
```

Example 4 (unknown):
```unknown
PetscInitialize()
```

---

## PetscDSRegisterAll#

**URL:** https://petsc.org/release/manualpages/DM/PetscDSRegisterAll/

**Contents:**
- PetscDSRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the PetscDS components in the PetscDS package.

PetscDSRegister(), PetscDSRegisterDestroy()

src/dm/interface/dmregall.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"  
#include "petscdmplex.h"  
#include "petscfe.h"  
#include "petscfv.h"  
#include "petscds.h"  
PetscErrorCode PetscDSRegisterAll(void)
```

Example 2 (unknown):
```unknown
PetscDSRegister()
```

Example 3 (unknown):
```unknown
PetscDSRegisterDestroy()
```

---

## PetscDualSpaceRegisterAll#

**URL:** https://petsc.org/release/manualpages/DM/PetscDualSpaceRegisterAll/

**Contents:**
- PetscDualSpaceRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the PetscDualSpace components in the PetscFE package.

PetscDualSpaceRegister(), PetscDualSpaceRegisterDestroy()

src/dm/interface/dmregall.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"  
#include "petscdmplex.h"  
#include "petscfe.h"  
PetscErrorCode PetscDualSpaceRegisterAll(void)
```

Example 2 (unknown):
```unknown
PetscDualSpaceRegister()
```

Example 3 (unknown):
```unknown
PetscDualSpaceRegisterDestroy()
```

---

## PetscFEFinalizePackage#

**URL:** https://petsc.org/release/manualpages/DM/PetscFEFinalizePackage/

**Contents:**
- PetscFEFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function finalizes everything in the PetscFE package. It is called from PetscFinalize().

src/dm/interface/dlregisdmdm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscFEFinalizePackage(void)
```

Example 3 (unknown):
```unknown
PetscInitialize()
```

---

## PetscFEInitializePackage#

**URL:** https://petsc.org/release/manualpages/DM/PetscFEInitializePackage/

**Contents:**
- PetscFEInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function initializes everything in the PetscFE package. It is called from PetscDLLibraryRegister() when using dynamic libraries, and on the first call to PetscSpaceCreate() when using static libraries.

src/dm/interface/dlregisdmdm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDLLibraryRegister()
```

Example 2 (unknown):
```unknown
PetscSpaceCreate()
```

Example 3 (unknown):
```unknown
PetscErrorCode PetscFEInitializePackage(void)
```

Example 4 (unknown):
```unknown
PetscInitialize()
```

---

## PetscFERegisterAll#

**URL:** https://petsc.org/release/manualpages/DM/PetscFERegisterAll/

**Contents:**
- PetscFERegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the PetscFE components in the PetscFE package.

PetscFERegister(), PetscFERegisterDestroy()

src/dm/interface/dmregall.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"  
#include "petscdmplex.h"  
#include "petscfe.h"  
PetscErrorCode PetscFERegisterAll(void)
```

Example 2 (unknown):
```unknown
PetscFERegister()
```

Example 3 (unknown):
```unknown
PetscFERegisterDestroy()
```

---

## PetscFVFinalizePackage#

**URL:** https://petsc.org/release/manualpages/DM/PetscFVFinalizePackage/

**Contents:**
- PetscFVFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function finalizes everything in the PetscFV package. It is called from PetscFinalize().

src/dm/interface/dlregisdmdm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscFVFinalizePackage(void)
```

Example 3 (unknown):
```unknown
PetscInitialize()
```

---

## PetscFVInitializePackage#

**URL:** https://petsc.org/release/manualpages/DM/PetscFVInitializePackage/

**Contents:**
- PetscFVInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function initializes everything in the PetscFV package. It is called from PetscDLLibraryRegister() when using dynamic libraries, and on the first call to PetscFVCreate() when using static libraries.

src/dm/interface/dlregisdmdm.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDLLibraryRegister()
```

Example 2 (unknown):
```unknown
PetscFVCreate()
```

Example 3 (unknown):
```unknown
PetscErrorCode PetscFVInitializePackage(void)
```

Example 4 (unknown):
```unknown
PetscInitialize()
```

---

## PetscFVRegisterAll#

**URL:** https://petsc.org/release/manualpages/DM/PetscFVRegisterAll/

**Contents:**
- PetscFVRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the PetscFV components in the PetscFV package.

PetscFVRegister(), PetscFVRegisterDestroy()

src/dm/interface/dmregall.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"  
#include "petscdmplex.h"  
#include "petscfe.h"  
#include "petscfv.h"  
PetscErrorCode PetscFVRegisterAll(void)
```

Example 2 (unknown):
```unknown
PetscFVRegister()
```

Example 3 (unknown):
```unknown
PetscFVRegisterDestroy()
```

---

## PetscLimiterRegisterAll#

**URL:** https://petsc.org/release/manualpages/DM/PetscLimiterRegisterAll/

**Contents:**
- PetscLimiterRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the PetscLimiter components in the PetscFV package.

PetscLimiterRegister(), PetscLimiterRegisterDestroy()

src/dm/interface/dmregall.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLimiter
```

Example 2 (unknown):
```unknown
#include "petscdm.h"  
#include "petscdmplex.h"  
#include "petscfe.h"  
#include "petscfv.h"  
PetscErrorCode PetscLimiterRegisterAll(void)
```

Example 3 (unknown):
```unknown
PetscLimiterRegister()
```

Example 4 (unknown):
```unknown
PetscLimiterRegisterDestroy()
```

---

## PetscSectionAddConstraintDof#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionAddConstraintDof/

**Contents:**
- PetscSectionAddConstraintDof#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Increment the number of constrained degrees of freedom associated with a given point.

numDof - the number of additional dof which are fixed by constraints

PetscSection, PetscSection, PetscSectionAddDof(), PetscSectionGetConstraintDof(), PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionAddConstraintDof(PetscSection s, PetscInt point, PetscInt numDof)
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
PetscSectionAddDof()
```

---

## PetscSectionAddDof#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionAddDof/

**Contents:**
- PetscSectionAddDof#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Adds to the total number of degrees of freedom associated with a given point.

numDof - the number of additional dof

This number is for the unnamed default field at the given point plus all degrees of freedom associated with all fields at that point

PetscSection, PetscSection, PetscSectionGetDof(), PetscSectionSetDof(), PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionAddDof(PetscSection s, PetscInt point, PetscInt numDof)
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
PetscSectionGetDof()
```

---

## PetscSectionAddFieldConstraintDof#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionAddFieldConstraintDof/

**Contents:**
- PetscSectionAddFieldConstraintDof#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Increment the number of constrained degrees of freedom associated with a given field on a point.

numDof - the number of additional dof which are fixed by constraints

PetscSection, PetscSection, PetscSectionAddDof(), PetscSectionGetFieldConstraintDof(), PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionAddFieldConstraintDof(PetscSection s, PetscInt point, PetscInt field, PetscInt numDof)
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
PetscSectionAddDof()
```

---

## PetscSectionAddFieldDof#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionAddFieldDof/

**Contents:**
- PetscSectionAddFieldDof#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Adds a number of degrees of freedom associated with a field on a given point.

numDof - the number of dof

When adding to the number of dof for a field at a point one must also ensure the count of the total number of dof at the point (summed over the fields and the unnamed default field) is correct by also calling PetscSectionAddDof() or PetscSectionSetDof()

This is equivalent to

PetscSection, PetscSection, PetscSectionSetFieldDof(), PetscSectionGetFieldDof(), PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionAddFieldDof(PetscSection s, PetscInt point, PetscInt field, PetscInt numDof)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
PetscSectionAddDof()
```

Example 4 (unknown):
```unknown
PetscSectionSetDof()
```

---

## PetscSectionArrayView#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionArrayView/

**Contents:**
- PetscSectionArrayView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

View an array, using the section to structure the values

s - the organizing PetscSection

array - the array of values

data_type - the PetscDataType of the array

viewer - the PetscViewer

PetscSection, PetscViewer, PetscSectionCreate(), VecSetValuesSection(), PetscSectionVecView()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionArrayView(PetscSection s, void *array, PetscDataType data_type, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
PetscDataType
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscSectionClone#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionClone/

**Contents:**
- PetscSectionClone#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#

Creates a shallow (if possible) copy of the PetscSection

section - the PetscSection

newSection - the copy

With standard PETSc terminology this should be called PetscSectionDuplicate()

PetscSection, PetscSection, PetscSectionCreate(), PetscSectionDestroy(), PetscSectionCopy()

src/vec/is/section/interface/section.c

src/ts/tutorials/ex18.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionClone(PetscSection section, PetscSection *newSection)
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (unknown):
```unknown
PetscSectionDuplicate()
```

---

## PetscSectionCompare#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionCompare/

**Contents:**
- PetscSectionCompare#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Compares two sections

s1 - the first PetscSection

s2 - the second PetscSection

congruent - PETSC_TRUE if the two sections are congruent, PETSC_FALSE otherwise

Field names are disregarded.

PetscSection, PetscSection, PetscSectionCreate(), PetscSectionCopy(), PetscSectionClone()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionCompare(PetscSection s1, PetscSection s2, PetscBool *congruent)
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
PETSC_FALSE
```

---

## PetscSectionCopy#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionCopy/

**Contents:**
- PetscSectionCopy#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Developer Notes#
- See Also#
- Level#
- Location#

Creates a shallow (if possible) copy of the PetscSection

section - the PetscSection

newSection - the copy

What exactly does shallow mean in this context?

PetscSection, PetscSection, PetscSectionCreate(), PetscSectionDestroy()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionCopy(PetscSection section, PetscSection newSection)
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

## PetscSectionCreateComponentSubsection#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionCreateComponentSubsection/

**Contents:**
- PetscSectionCreateComponentSubsection#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Create a new, smaller PetscSection composed of only selected components

len - the number of components

comps - the component numbers

subs - the subsection

The chart of subs is the same as the chart of s

This will error if the section has more than one field, or if a component number is out of range

PetscSection, PetscSection, PetscSectionCreateSupersection(), PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionCreateComponentSubsection(PetscSection s, PetscInt len, const PetscInt comps[], PetscSection *subs)
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

## PetscSectionCreateGlobalSectionCensored#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionCreateGlobalSectionCensored/

**Contents:**
- PetscSectionCreateGlobalSectionCensored#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#

Create a PetscSection describing the globallayout using a local (sequential) PetscSection on each MPI process and an PetscSF describing the section point overlap.

s - The PetscSection for the local field layout

sf - The PetscSF describing parallel layout of the section points

includeConstraints - By default this is PETSC_FALSE, meaning that the global vector will not possess constrained dofs

numExcludes - The number of exclusion ranges, this must have the same value on all MPI processes

excludes - An array [start_0, end_0, start_1, end_1, …] where there are numExcludes pairs and must have the same values on all MPI processes

gsection - The PetscSection for the global field layout

On each MPI process gsection inherits the chart of the s on that process.

This sets negative sizes and offsets to points not owned by this process as defined by sf but that are within the local value of the chart of gsection. In those locations the value of size is -(size+1) and the value of the offset on the remote process is -(off+1).

This routine augments PetscSectionCreateGlobalSection() by allowing one to exclude certain ranges in the chart of the PetscSection

This is a terrible function name

PetscSection, PetscSection, PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionCreateGlobalSectionCensored(PetscSection s, PetscSF sf, PetscBool includeConstraints, PetscInt numExcludes, const PetscInt excludes[], PetscSection *gsection)
```

Example 4 (unknown):
```unknown
PetscSection
```

---

## PetscSectionCreateGlobalSection#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionCreateGlobalSection/

**Contents:**
- PetscSectionCreateGlobalSection#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Create a parallel section describing the global layout using a local (sequential) PetscSection on each MPI process and a PetscSF describing the section point overlap.

s - The PetscSection for the local field layout

sf - The PetscSF describing parallel layout of the section points (leaves are unowned local points)

usePermutation - By default this is PETSC_TRUE, meaning any permutation of the local section is transferred to the global section

includeConstraints - By default this is PETSC_FALSE, meaning that the global field vector will not possess constrained dofs

localOffsets - If PETSC_TRUE, use local rather than global offsets for the points

gsection - The PetscSection for the global field layout

On each MPI process gsection inherits the chart of the s on that process.

This sets negative sizes and offsets to points not owned by this process as defined by sf but that are within the local value of the chart of gsection. In those locations the value of size is -(size+1) and the value of the offset on the remote process is -(off+1).

PetscSection, PetscSection, PetscSectionCreate(), PetscSectionCreateGlobalSectionCensored()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionCreateGlobalSection(PetscSection s, PetscSF sf, PetscBool usePermutation, PetscBool includeConstraints, PetscBool localOffsets, PetscSection *gsection)
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (unknown):
```unknown
PETSC_FALSE
```

---

## PetscSectionCreateSubdomainSection#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionCreateSubdomainSection/

**Contents:**
- PetscSectionCreateSubdomainSection#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#

Create a new, smaller section with support on a subdomain of the mesh

subpointMap - a sorted list of points in the original mesh which are in the subdomain

subs - the subsection

The point numbers remain the same as in the larger PetscSection, but the section offsets now refer to a new, smaller vector. The chart of subs is [min(subpointMap),max(subpointMap)+1)

Compare this with PetscSectionCreateSubmeshSection() that maps the point numbers to start at zero

The use of the term Subdomain is unneeded and needs clarification, it is not specific to meshes. It appears to be just a subset of the chart of the original PetscSection

PetscSection, PetscSection, PetscSectionCreateSubmeshSection(), PetscSectionCreateSubsection(), DMPlexGetSubpointMap(), PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionCreateSubdomainSection(PetscSection s, IS subpointMap, PetscSection *subs)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (sass):
```sass
[min(subpointMap),max(subpointMap)+1)
```

---

## PetscSectionCreateSubmeshSection#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionCreateSubmeshSection/

**Contents:**
- PetscSectionCreateSubmeshSection#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#

Create a new, smaller section with support on the submesh

subpointIS - a sorted list of points in the original mesh which are in the submesh

subs - the subsection

The points are renumbered from 0, and the section offsets now refer to a new, smaller vector. That is the chart of subs is [0,sizeof(subpointmap))

Compare this with PetscSectionCreateSubdomainSection() that does not map the points numbers to start at zero but leaves them as before

The use of the term Submesh is confusing and needs clarification, it is not specific to meshes. It appears to be just a subset of the chart of the original PetscSection

PetscSection, PetscSection, PetscSectionCreateSubdomainSection(), PetscSectionCreateSubsection(), DMPlexGetSubpointMap(), PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionCreateSubmeshSection(PetscSection s, IS subpointIS, PetscSection *subs)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (json):
```json
[0,sizeof(subpointmap))
```

Example 4 (unknown):
```unknown
PetscSectionCreateSubdomainSection()
```

---

## PetscSectionCreateSubsection#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionCreateSubsection/

**Contents:**
- PetscSectionCreateSubsection#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Create a new, smaller PetscSection composed of only selected fields

len - the number of subfields

fields - the subfield numbers

subs - the subsection

The chart of subs is the same as the chart of s

This will error if a fieldnumber is out of range

PetscSection, PetscSection, PetscSectionCreateSupersection(), PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionCreateSubsection(PetscSection s, PetscInt len, const PetscInt fields[], PetscSection *subs)
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

## PetscSectionCreateSupersection#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionCreateSupersection/

**Contents:**
- PetscSectionCreateSupersection#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#

Create a new, larger section composed of multiple PetscSections

s - the input sections

len - the number of input sections

supers - the supersection

The section offsets now refer to a new, larger vector.

Needs to explain how the sections are composed

PetscSection, PetscSection, PetscSectionCreateSubsection(), PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionCreateSupersection(PetscSection s[], PetscInt len, PetscSection *supers)
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (unknown):
```unknown
PetscSectionCreateSubsection()
```

---

## PetscSectionCreate#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionCreate/

**Contents:**
- PetscSectionCreate#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Allocates a PetscSection and sets the map contents to the default.

comm - the MPI communicator

s - pointer to the section

Typical calling sequence

The PetscSection object and methods are intended to be used in the PETSc Vec and Mat implementations. The indices returned by the PetscSection are appropriate for the kind of Vec it is associated with. For example, if the vector being indexed is a local vector, we call the section a local section. If the section indexes a global vector, we call it a global section. For parallel vectors, like global vectors, we use negative indices to indicate dofs owned by other processes.

PetscSection, PetscSection, PetscSectionSetChart(), PetscSectionDestroy(), PetscSectionCreateGlobalSection()

src/vec/is/section/interface/section.c

src/ts/tutorials/ex30.c src/snes/tutorials/ex7.c src/ts/tutorials/ex11.c src/dm/impls/plex/tutorials/ex7.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionCreate(MPI_Comm comm, PetscSection *s)
```

Example 3 (unknown):
```unknown
PetscSectionCreate(MPI_Comm,PetscSection *);!
       PetscSectionSetNumFields(PetscSection, numFields);
       PetscSectionSetChart(PetscSection,low,high);
       PetscSectionSetDof(PetscSection,point,numdof);
       PetscSectionSetUp(PetscSection);
       PetscSectionGetOffset(PetscSection,point,PetscInt *);
       PetscSectionDestroy(PetscSection);
```

Example 4 (unknown):
```unknown
PetscSection
```

---

## PetscSectionDestroy#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionDestroy/

**Contents:**
- PetscSectionDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#

PetscSection, PetscSection, PetscSectionCreate(), PetscSectionReset()

src/vec/is/section/interface/section.c

src/ts/tutorials/ex11.c src/dm/impls/plex/tutorials/ex1f90.F90 src/dm/impls/plex/tutorials/ex6.c src/ts/tutorials/ex30.c src/ts/tutorials/ex52.c src/dm/impls/plex/tutorials/ex1.c src/ts/tutorials/ex18.c src/dm/impls/plex/tutorials/ex14.c src/dm/impls/plex/tutorials/ex7.c src/snes/tutorials/ex7.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionDestroy(PetscSection *s)
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

## PetscSectionExtractDofsFromArray#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionExtractDofsFromArray/

**Contents:**
- PetscSectionExtractDofsFromArray#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Extracts elements of an array corresponding to DOFs of specified points.

origSection - the PetscSection describing the layout of the array

dataType - MPI_Datatype describing the data type of the array (currently only MPIU_INT, MPIU_SCALAR, MPIU_REAL)

origArray - the array; its size must be equal to the storage size of origSection

points - IS with points to extract; its indices must lie in the chart of origSection

newSection - the new PetscSection describing the layout of the new array (with points renumbered 0,1,… but preserving numbers of DOFs)

newArray - the array of the extracted DOFs; its size is the storage size of newSection

PetscSection, PetscSectionSym, PetscSectionGetChart(), PetscSectionGetDof(), PetscSectionGetStorageSize(), PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionExtractDofsFromArray(PetscSection origSection, MPI_Datatype dataType, const void *origArray, IS points, PetscSection *newSection, void *newArray[])
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
MPI_Datatype
```

Example 4 (unknown):
```unknown
MPIU_SCALAR
```

---

## PetscSectionGetBlockStarts#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetBlockStarts/

**Contents:**
- PetscSectionGetBlockStarts#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Returns a table indicating which points start new blocks

Not Collective, No Fortran Support

blockStarts - The PetscBT with a 1 for each point that begins a block

The table is on [0, pEnd - pStart).

This information is used by DMCreateMatrix() to create a variable block size description which is set using MatSetVariableBlockSizes().

Low-level Vector Communication, IS, PetscSection, PetscSectionSetBlockStarts(), PetscSectionCreate(), DMCreateMatrix(), MatSetVariableBlockSizes()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetBlockStarts(PetscSection s, PetscBT *blockStarts)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
DMCreateMatrix()
```

Example 4 (unknown):
```unknown
MatSetVariableBlockSizes()
```

---

## PetscSectionGetChart#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetChart/

**Contents:**
- PetscSectionGetChart#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Returns the range [pStart, pEnd) in which points (indices) lie for this PetscSection on this MPI process

pStart - the first point

pEnd - one past the last point

The chart may be thought of as the bounds on the points (indices) one may use to index into numerical data that is associated with the PetscSection data layout.

PetscSection, PetscSection, PetscSectionSetChart(), PetscSectionCreate()

src/vec/is/section/interface/section.c

src/ts/tutorials/ex18.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetChart(PetscSection s, PetscInt *pStart, PetscInt *pEnd)
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

## PetscSectionGetClosureIndex#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetClosureIndex/

**Contents:**
- PetscSectionGetClosureIndex#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Get the cache of points in the closure of each point in the section set with PetscSectionSetClosureIndex()

section - The PetscSection

obj - A PetscObject which serves as the key for this index

clSection - PetscSection giving the size of the closure of each point

clPoints - IS giving the points in each closure

PetscSection, PetscSectionSetClosureIndex(), DMPlexCreateClosureIndex()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSectionSetClosureIndex()
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetClosureIndex(PetscSection section, PetscObject obj, PetscSection *clSection, IS *clPoints)
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (unknown):
```unknown
PetscObject
```

---

## PetscSectionGetClosureInversePermutation#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetClosureInversePermutation/

**Contents:**
- PetscSectionGetClosureInversePermutation#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Get the inverse dof permutation for the closure of each cell in the section, meaning clPerm[oldIndex] = newIndex.

section - The PetscSection

obj - A PetscObject which serves as the key for this index (usually a DM)

depth - Depth stratum on which to obtain closure permutation

clSize - Closure size to be permuted (e.g., may vary with element topology and degree)

perm - The dof closure permutation

The user must destroy the IS that is returned.

PetscSection, PetscSection, IS, PetscSectionSetClosurePermutation(), PetscSectionGetClosureIndex(), PetscSectionSetClosureIndex(), DMPlexCreateClosureIndex()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetClosureInversePermutation(PetscSection section, PetscObject obj, PetscInt depth, PetscInt clSize, IS *perm)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
PetscObject
```

Example 4 (unknown):
```unknown
PetscSection
```

---

## PetscSectionGetClosurePermutation#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetClosurePermutation/

**Contents:**
- PetscSectionGetClosurePermutation#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Get the dof permutation for the closure of each cell in the section, meaning clPerm[newIndex] = oldIndex.

section - The PetscSection

obj - A PetscObject which serves as the key for this index (usually a DM)

depth - Depth stratum on which to obtain closure permutation

clSize - Closure size to be permuted (e.g., may vary with element topology and degree)

perm - The dof closure permutation

The user must destroy the IS that is returned.

PetscSection, PetscSection, IS, PetscSectionSetClosurePermutation(), PetscSectionGetClosureInversePermutation(), PetscSectionGetClosureIndex(), PetscSectionSetClosureIndex(), DMPlexCreateClosureIndex()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetClosurePermutation(PetscSection section, PetscObject obj, PetscInt depth, PetscInt clSize, IS *perm)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
PetscObject
```

Example 4 (unknown):
```unknown
PetscSection
```

---

## PetscSectionGetComponentName#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetComponentName/

**Contents:**
- PetscSectionGetComponentName#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#

Gets the name of a field component in the PetscSection

field - the field number

comp - the component number

compName - the component name

Will error if the field or component number do not exist

The function name should have Field in it since they are field components.

PetscSection, PetscSection, PetscSectionGetFieldName(), PetscSectionSetNumFields(), PetscSectionGetNumFields(), PetscSectionSetComponentName(), PetscSectionSetFieldName(), PetscSectionGetFieldComponents(), PetscSectionSetFieldComponents()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetComponentName(PetscSection s, PetscInt field, PetscInt comp, const char *compName[])
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

## PetscSectionGetConstrainedStorageSize#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetConstrainedStorageSize/

**Contents:**
- PetscSectionGetConstrainedStorageSize#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Return the size of an array or local Vec capable of holding all unconstrained degrees of freedom in a PetscSection

size - the size of an array which can hold all unconstrained dofs

PetscSection, PetscSection, PetscSectionGetStorageSize(), PetscSectionGetOffset(), PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetConstrainedStorageSize(PetscSection s, PetscInt *size)
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

## PetscSectionGetConstraintDof#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetConstraintDof/

**Contents:**
- PetscSectionGetConstraintDof#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Return the number of constrained degrees of freedom associated with a given point.

numDof - the number of dof which are fixed by constraints

PetscSection, PetscSection, PetscSectionGetDof(), PetscSectionSetConstraintDof(), PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetConstraintDof(PetscSection s, PetscInt point, PetscInt *numDof)
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
PetscSectionGetDof()
```

---

## PetscSectionGetConstraintIndices#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetConstraintIndices/

**Contents:**
- PetscSectionGetConstraintIndices#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Fortran Notes#
- See Also#
- Level#
- Location#

Get the point dof numbers, in [0, dof), which are constrained for a given point

indices - The constrained dofs

Use PetscSectionRestoreConstraintIndices() when the indices are no longer needed

PetscSection, PetscSectionSetConstraintIndices(), PetscSectionGetConstraintDof(), PetscSection

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetConstraintIndices(PetscSection s, PetscInt point, const PetscInt *indices[])
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
PetscSectionRestoreConstraintIndices()
```

Example 4 (unknown):
```unknown
PetscSectionSetConstraintIndices()
```

---

## PetscSectionGetDof#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetDof/

**Contents:**
- PetscSectionGetDof#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Return the total number of degrees of freedom associated with a given point.

numDof - the number of dof

In a global section, this size will be negative for points not owned by this process.

This number is for the unnamed default field at the given point plus all degrees of freedom associated with all fields at that point

PetscSection, PetscSection, PetscSectionSetDof(), PetscSectionCreate()

src/vec/is/section/interface/section.c

src/dm/impls/plex/tutorials/ex6.c src/snes/tutorials/ex7.c src/tao/tutorials/ex3.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetDof(PetscSection s, PetscInt point, PetscInt *numDof)
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
PetscSectionSetDof()
```

---

## PetscSectionGetFieldComponents#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetFieldComponents/

**Contents:**
- PetscSectionGetFieldComponents#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Developer Notes#
- See Also#
- Level#
- Location#

Returns the number of field components for the given field.

field - the field number

numComp - the number of field components

This function is misnamed. There is a Num in PetscSectionGetNumFields() but not in this name

PetscSection, PetscSection, PetscSectionSetFieldComponents(), PetscSectionGetNumFields(), PetscSectionSetComponentName(), PetscSectionGetComponentName()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetFieldComponents(PetscSection s, PetscInt field, PetscInt *numComp)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
PetscSectionGetNumFields()
```

Example 4 (unknown):
```unknown
PetscSection
```

---

## PetscSectionGetFieldConstraintDof#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetFieldConstraintDof/

**Contents:**
- PetscSectionGetFieldConstraintDof#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Return the number of constrained degrees of freedom associated with a given field on a point.

numDof - the number of dof which are fixed by constraints

PetscSection, PetscSection, PetscSectionGetDof(), PetscSectionSetFieldConstraintDof(), PetscSectionCreate()

src/vec/is/section/interface/section.c

src/ts/tutorials/ex18.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetFieldConstraintDof(PetscSection s, PetscInt point, PetscInt field, PetscInt *numDof)
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
PetscSectionGetDof()
```

---

## PetscSectionGetFieldConstraintIndices#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetFieldConstraintIndices/

**Contents:**
- PetscSectionGetFieldConstraintIndices#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Fortran Notes#
- See Also#
- Level#
- Location#

Get the field dof numbers, in [0, fdof), which are constrained

field - The field number

indices - The constrained dofs sorted in ascending order, the length is returned by PetscSectionGetConstraintDof().

Use PetscSectionRestoreFieldConstraintIndices() to restore the indices when no longer needed

PetscSection, PetscSectionSetFieldConstraintIndices(), PetscSectionGetConstraintIndices(), PetscSectionGetConstraintDof(), PetscSection

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetFieldConstraintIndices(PetscSection s, PetscInt point, PetscInt field, const PetscInt *indices[])
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
PetscSectionGetConstraintDof()
```

Example 4 (unknown):
```unknown
PetscSectionRestoreFieldConstraintIndices()
```

---

## PetscSectionGetFieldDof#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetFieldDof/

**Contents:**
- PetscSectionGetFieldDof#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Return the number of degrees of freedom associated with a field on a given point.

numDof - the number of dof

PetscSection, PetscSection, PetscSectionSetFieldDof(), PetscSectionCreate()

src/vec/is/section/interface/section.c

src/ts/tutorials/ex18.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetFieldDof(PetscSection s, PetscInt point, PetscInt field, PetscInt *numDof)
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
PetscSectionSetFieldDof()
```

---

## PetscSectionGetFieldName#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetFieldName/

**Contents:**
- PetscSectionGetFieldName#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Returns the name of a field in the PetscSection

field - the field number

fieldName - the field name

Will error if the field number is out of range

PetscSection, PetscSection, PetscSectionSetFieldName(), PetscSectionSetNumFields(), PetscSectionGetNumFields()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetFieldName(PetscSection s, PetscInt field, const char *fieldName[])
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

## PetscSectionGetFieldOffset#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetFieldOffset/

**Contents:**
- PetscSectionGetFieldOffset#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Return the offset into an array or Vec for the field dof associated with the given point.

In a global section, offset will be negative for points not owned by this process.

The offset values are different depending on a value set with PetscSectionSetPointMajor()

PetscSection, PetscSection, PetscSectionGetOffset(), PetscSectionCreate(), PetscSectionGetFieldPointOffset()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetFieldOffset(PetscSection s, PetscInt point, PetscInt field, PetscInt *offset)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
PetscSectionSetPointMajor()
```

Example 4 (unknown):
```unknown
PetscSection
```

---

## PetscSectionGetFieldPointOffset#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetFieldPointOffset/

**Contents:**
- PetscSectionGetFieldPointOffset#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- Example#
- See Also#
- Level#
- Location#

Return the offset for the first field dof associated with the given point relative to the offset for that point for the unnamed default field’s first dof

This ignores constraints

PetscSection, PetscSection, PetscSectionGetOffset(), PetscSectionCreate(), PetscSectionGetFieldOffset()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetFieldPointOffset(PetscSection s, PetscInt point, PetscInt field, PetscInt *offset)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (lua):
```lua
if PetscSectionSetPointMajor(s,PETSC_TRUE)
  The unnamed default field has 3 dof at `point`
  Field 0 has 2 dof at `point`
  Then PetscSectionGetFieldPointOffset(s,point,1,&offset) returns and offset of 5
```

Example 4 (unknown):
```unknown
PetscSection
```

---

## PetscSectionGetFieldPointSyms#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetFieldPointSyms/

**Contents:**
- PetscSectionGetFieldPointSyms#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Get the symmetries for a set of points in a field of a PetscSection under specific orientations.

section - the section

field - the field of the section

numPoints - the number of points

points - an array of size 2 * numPoints, containing a list of (point, orientation) pairs. (An orientation is an arbitrary integer: its interpretation is up to sym. Orientations are used by DM: for their interpretation in that context, see DMPlexGetConeOrientation()).

perms - The permutations for the given orientations (or NULL if there is no symmetry or the permutation is the identity).

rots - The field rotations symmetries for the given orientations (or NULL if there is no symmetry or the rotations are all identity).

PetscSectionSetFieldSym() must have been previously called to provide the symmetries to the PetscSection

Use PetscSectionRestoreFieldPointSyms() when finished with the data

PetscSection, PetscSectionSym, PetscSectionGetPointSyms(), PetscSectionRestoreFieldPointSyms()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetFieldPointSyms(PetscSection section, PetscInt field, PetscInt numPoints, const PetscInt *points, const PetscInt ***perms, const PetscScalar ***rots)
```

Example 3 (unknown):
```unknown
DMPlexGetConeOrientation()
```

Example 4 (unknown):
```unknown
PetscSectionSetFieldSym()
```

---

## PetscSectionGetFieldSym#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetFieldSym/

**Contents:**
- PetscSectionGetFieldSym#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the symmetries for the data referred to by a field of the section

section - the section describing data layout

field - the field number

sym - the symmetry describing the affect of orientation on the access of the data

PetscSection, PetscSectionSym, PetscSectionSetFieldSym(), PetscSectionSymCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetFieldSym(PetscSection section, PetscInt field, PetscSectionSym *sym)
```

Example 2 (unknown):
```unknown
PetscSectionSym
```

Example 3 (unknown):
```unknown
PetscSectionSetFieldSym()
```

Example 4 (unknown):
```unknown
PetscSectionSymCreate()
```

---

## PetscSectionGetField#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetField/

**Contents:**
- PetscSectionGetField#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Get the PetscSection associated with a single field

field - The field number

subs - The PetscSection for the given field, note the chart of subs is not set

Does not increase the reference count of the selected sub-section. There is no matching PetscSectionRestoreField()

PetscSection, PetscSection, IS, PetscSectionSetNumFields()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetField(PetscSection s, PetscInt field, PetscSection *subs)
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

## PetscSectionGetIncludesConstraints#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetIncludesConstraints/

**Contents:**
- PetscSectionGetIncludesConstraints#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the flag indicating if constrained dofs were included when computing offsets in the PetscSection. The value is set with PetscSectionSetIncludesConstraints()

includesConstraints - the flag indicating if constrained dofs were included when computing offsets

PetscSection, PetscSection, PetscSectionSetIncludesConstraints()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
PetscSectionSetIncludesConstraints()
```

Example 3 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetIncludesConstraints(PetscSection s, PetscBool *includesConstraints)
```

Example 4 (unknown):
```unknown
PetscSection
```

---

## PetscSectionGetMaxDof#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetMaxDof/

**Contents:**
- PetscSectionGetMaxDof#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#

Return the maximum number of degrees of freedom on any point in the PetscSection

maxDof - the maximum dof

The returned number is up-to-date without need for PetscSectionSetUp().

This is the maximum over all points of the sum of the number of dof in the unnamed default field plus all named fields. This is equivalent to the maximum over all points of the value returned by PetscSectionGetDof() on this MPI process

The returned number is calculated lazily and stashed.

A call to PetscSectionInvalidateMaxDof_Internal() invalidates the stashed value.

PetscSectionInvalidateMaxDof_Internal() is called in PetscSectionSetDof(), PetscSectionAddDof() and PetscSectionReset()

It should also be called every time atlasDof is modified directly.

PetscSection, PetscSection, PetscSectionGetDof(), PetscSectionSetDof(), PetscSectionAddDof(), PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetMaxDof(PetscSection s, PetscInt *maxDof)
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (unknown):
```unknown
PetscSectionSetUp()
```

---

## PetscSectionGetNumFields#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetNumFields/

**Contents:**
- PetscSectionGetNumFields#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Returns the number of fields in a PetscSection, or 0 if no fields were defined.

numFields - the number of fields defined, or 0 if none were defined

PetscSection, PetscSection, PetscSectionSetNumFields()

src/vec/is/section/interface/section.c

src/ts/tutorials/ex18.c src/dm/impls/plex/tutorials/dmplexgetrestoreclosureindices.F90

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetNumFields(PetscSection s, PetscInt *numFields)
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

## PetscSectionGetOffsetRange#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetOffsetRange/

**Contents:**
- PetscSectionGetOffsetRange#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Return the full range of offsets [start, end) for a PetscSection

start - the minimum offset

end - one more than the maximum offset

PetscSection, PetscSection, PetscSectionGetOffset(), PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (julia):
```julia
#include "petscsection.h"   
PetscErrorCode PetscSectionGetOffsetRange(PetscSection s, PetscInt *start, PetscInt *end)
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

## PetscSectionGetOffset#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetOffset/

**Contents:**
- PetscSectionGetOffset#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Return the offset into an array or Vec for the dof associated with the given point.

In a global section, offset will be negative for points not owned by this process.

This is for the unnamed default field in the PetscSection not the named fields

The offset values are different depending on a value set with PetscSectionSetPointMajor()

PetscSection, PetscSection, PetscSectionGetFieldOffset(), PetscSectionCreate(), PetscSectionSetPointMajor()

src/vec/is/section/interface/section.c

src/snes/tutorials/ex7.c src/tao/tutorials/ex3.c src/snes/tutorials/ex13.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetOffset(PetscSection s, PetscInt point, PetscInt *offset)
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
PetscSectionSetPointMajor()
```

---

## PetscSectionGetPermutation#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetPermutation/

**Contents:**
- PetscSectionGetPermutation#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the permutation of [0, pEnd - pStart) or NULL that was set with PetscSectionSetPermutation()

perm - The permutation as an IS

Low-level Vector Communication, IS, PetscSection, PetscSectionSetPermutation(), PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSectionSetPermutation()
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetPermutation(PetscSection s, IS *perm)
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

## PetscSectionGetPointLayout#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetPointLayout/

**Contents:**
- PetscSectionGetPointLayout#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- Example#
- Developer Notes#
- See Also#
- Level#
- Location#

Get a PetscLayout for the points with nonzero dof counts of the unnamed default field within this PetscSections local chart

layout - The point layout for the data that defines the section

PetscSectionGetValueLayout() provides similar information but counting the total number of degrees of freedom on the MPI process (excluding constrained degrees of freedom).

This count includes constrained degrees of freedom

This is usually called on the default global section.

I find the names of these two functions extremely non-informative

PetscSection, PetscSection, PetscSectionGetValueLayout(), PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLayout
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetPointLayout(MPI_Comm comm, PetscSection s, PetscLayout *layout)
```

Example 4 (unknown):
```unknown
PetscSection
```

---

## PetscSectionGetPointMajor#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetPointMajor/

**Contents:**
- PetscSectionGetPointMajor#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the flag for dof ordering, PETSC_TRUE if it is point major, PETSC_FALSE if it is field major

pm - the flag for point major ordering

PetscSection, PetscSection, PetscSectionSetPointMajor()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSC_FALSE
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetPointMajor(PetscSection s, PetscBool *pm)
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

## PetscSectionGetPointSyms#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetPointSyms/

**Contents:**
- PetscSectionGetPointSyms#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Example of usage, gathering dofs into a local array (lArray) from a section array (sArray)#
- Example of usage, adding dofs into a section array (sArray) from a local array (lArray)#
- Notes#
- See Also#
- Level#
- Location#

Get the symmetries for a set of points in a PetscSection under specific orientations.

section - the section

numPoints - the number of points

points - an array of size 2 * numPoints, containing a list of (point, orientation) pairs. (An orientation is an arbitrary integer: its interpretation is up to sym. Orientations are used by DM: for their interpretation in that context, see DMPlexGetConeOrientation()).

perms - The permutations for the given orientations (or NULL if there is no symmetry or the permutation is the identity).

rots - The field rotations symmetries for the given orientations (or NULL if there is no symmetry or the rotations are all identity).

PetscSectionSetSym() must have been previously called to provide the symmetries to the PetscSection

Use PetscSectionRestorePointSyms() when finished with the data

PetscSection, PetscSectionSym, PetscSectionRestorePointSyms(), PetscSectionSymCreate(), PetscSectionSetSym(), PetscSectionGetSym()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetPointSyms(PetscSection section, PetscInt numPoints, const PetscInt *points, const PetscInt ***perms, const PetscScalar ***rots)
```

Example 3 (unknown):
```unknown
DMPlexGetConeOrientation()
```

Example 4 (unknown):
```unknown
const PetscInt    **perms;
     const PetscScalar **rots;
     PetscInt            lOffset;

     PetscSectionGetPointSyms(section,numPoints,points,&perms,&rots);
     for (i = 0, lOffset = 0; i < numPoints; i++) {
       PetscInt           point = points[2*i], dof, sOffset;
       const PetscInt    *perm  = perms ? perms[i] : NULL;
       const PetscScalar *rot   = rots  ? rots[i]  : NULL;

       PetscSectionGetDof(section,point,&dof);
       PetscSectionGetOffset(section,point,&sOffset);

       if (perm) { for (j = 0; j < dof; j++) lArray[lOffset + perm[j]]  = sArray[sOffset + j]; }
       else      { for (j = 0; j < dof; j++) lArray[lOffset +      j ]  = sArray[sOffset + j]; }
       if (rot)  { for (j = 0; j < dof; j++) lArray[lOffset +      j ] *= rot[j];              }
       lOffset += dof;
     }
     PetscSectionRestorePointSyms(section,numPoints,points,&perms,&rots);
```

---

## PetscSectionGetStorageSize#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetStorageSize/

**Contents:**
- PetscSectionGetStorageSize#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Return the size of an array or local Vec capable of holding all the degrees of freedom defined in a PetscSection

size - the size of an array which can hold all the dofs

PetscSection, PetscSection, PetscSectionGetOffset(), PetscSectionGetConstrainedStorageSize(), PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetStorageSize(PetscSection s, PetscInt *size)
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

## PetscSectionGetSym#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetSym/

**Contents:**
- PetscSectionGetSym#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the symmetries for the data referred to by the section

section - the section describing data layout

sym - the symmetry describing the affect of orientation on the access of the data, provided previously by PetscSectionSetSym()

PetscSection, PetscSectionSym, PetscSectionSetSym(), PetscSectionSymCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetSym(PetscSection section, PetscSectionSym *sym)
```

Example 2 (unknown):
```unknown
PetscSectionSetSym()
```

Example 3 (unknown):
```unknown
PetscSectionSym
```

Example 4 (unknown):
```unknown
PetscSectionSetSym()
```

---

## PetscSectionGetUseFieldOffsets#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetUseFieldOffsets/

**Contents:**
- PetscSectionGetUseFieldOffsets#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the flag indicating if field offsets are used directly in a global section, rather than just the point offset

s - the global PetscSection

PetscSection, PetscSectionSym, PetscSectionSetChart(), PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetUseFieldOffsets(PetscSection s, PetscBool *flg)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
PetscSectionSym
```

Example 4 (unknown):
```unknown
PetscSectionSetChart()
```

---

## PetscSectionGetValueLayout#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionGetValueLayout/

**Contents:**
- PetscSectionGetValueLayout#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- Example#
- See Also#
- Level#
- Location#

Get the PetscLayout associated with the section dofs of a PetscSection

layout - The dof layout for the section

PetscSectionGetPointLayout() provides similar information but only counting the number of points with nonzero degrees of freedom and including the constrained degrees of freedom

This is usually called for the default global section.

PetscSection, PetscSection, PetscSectionGetPointLayout(), PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscLayout
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionGetValueLayout(MPI_Comm comm, PetscSection s, PetscLayout *layout)
```

Example 4 (unknown):
```unknown
PetscSection
```

---

## PetscSectionHasConstraints#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionHasConstraints/

**Contents:**
- PetscSectionHasConstraints#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Determine whether a PetscSection has constrained dofs

hasConstraints - flag indicating that the section has constrained dofs

PetscSection, PetscSectionSetConstraintIndices(), PetscSectionGetConstraintDof(), PetscSection

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionHasConstraints(PetscSection s, PetscBool *hasConstraints)
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (unknown):
```unknown
PetscSectionSetConstraintIndices()
```

---

## PetscSectionLoad#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionLoad/

**Contents:**
- PetscSectionLoad#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

s - the PetscSection object to load

PetscSectionLoad(), when viewer is of type PETSCVIEWERHDF5, loads a section saved with PetscSectionView(). The number of processes used here (N) does not need to be the same as that used when saving. After calling this function, the chart of s on rank i will be set to [0, E_i), where \sum_{i=0}^{N-1}E_i equals to the total number of saved section points.

PetscSection, PetscSection, PetscSectionCreate(), PetscSectionDestroy(), PetscSectionView()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionLoad(PetscSection s, PetscViewer viewer)
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (unknown):
```unknown
PetscSectionLoad()
```

---

## PetscSectionMigrateData#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionMigrateData/

**Contents:**
- PetscSectionMigrateData#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Migrate data described by a PetscSection using a PetscSF that defines a original-to-new (root-to-leaf) point mapping

migratePointSF - defines the mapping (communication) of the root points to the leaf points

datatype - the type of data

rootSection - the PetscSection that describes the data layout on the root points (how many dof and what fields are associated with each root point)

rootData - the existing data array described by rootSection, may be NULL is storage size of rootSection is zero

leafSection - the new PetscSection that describes the data layout on the leaf points

leafData - the redistributed data array that is associated with the leaf points

migrateDataSF - defines the mapping (communication) of the rootData array to the leafData array, may be NULL if not needed

This function can best be thought of as applying PetscSFBcastBegin() to an array described by a PetscSection. While PetscSFBcastBegin() is limited to broadcasting data that is of the same size for every index, this function allows the data to be a different size for each index. The size and layout of that irregularly sized data before and after PetscSFBcastBegin() is described by the rootSection and leafSection, respectively.

This function combines PetscSFDistributeSection(), PetscSFCreateSectionSF(), and PetscSFBcastBegin()/PetscSFBcastEnd() into a single call. migrateDataSF can be used to repeat the PetscSFBcastBegin()/PetscSFBcastEnd() on a different data array described by the same rootSection.

This should not be used for global-to-local type communication patterns. For this use case, see PetscSectionCreateGlobalSection() and PetscSFSetGraphSection().

PetscSection, PetscSection, PetscSFDistributeSection(), PetscSFCreateSectionSF(), DMPlexDistributeData()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionMigrateData(PetscSF migratePointSF, MPI_Datatype datatype, PetscSection rootSection, const void *rootData, PetscSection leafSection, void *leafData[], PetscSF *migrateDataSF)
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (unknown):
```unknown
rootSection
```

---

## PetscSectionPermute#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionPermute/

**Contents:**
- PetscSectionPermute#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Reorder the section according to the input point permutation

section - The PetscSection object

permutation - The point permutation, old point p becomes new point perm[p]

sectionNew - The permuted PetscSection

The data and the access to the data via PetscSectionGetFieldOffset() and PetscSectionGetOffset() are both changed in sectionNew

Compare to PetscSectionSetPermutation()

PetscSection, IS, PetscSection, MatPermute(), PetscSectionSetPermutation()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionPermute(PetscSection section, IS permutation, PetscSection *sectionNew)
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
PetscSectionGetFieldOffset()
```

---

## PetscSectionResetClosurePermutation#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionResetClosurePermutation/

**Contents:**
- PetscSectionResetClosurePermutation#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Remove any existing closure permutation

section - The PetscSection

PetscSectionSetClosurePermutation(), PetscSectionSetClosureIndex(), PetscSectionReset()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionResetClosurePermutation(PetscSection section)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
PetscSectionSetClosurePermutation()
```

Example 4 (unknown):
```unknown
PetscSectionSetClosureIndex()
```

---

## PetscSectionReset#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionReset/

**Contents:**
- PetscSectionReset#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Frees all section data, the section is then as if PetscSectionCreate() had just been called.

PetscSection, PetscSection, PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSectionCreate()
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionReset(PetscSection s)
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

## PetscSectionRestoreFieldPointSyms#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionRestoreFieldPointSyms/

**Contents:**
- PetscSectionRestoreFieldPointSyms#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Restore the symmetries returned by PetscSectionGetFieldPointSyms()

section - the section

field - the field number

numPoints - the number of points

points - an array of size 2 * numPoints, containing a list of (point, orientation) pairs. (An orientation is an arbitrary integer: its interpretation is up to sym. Orientations are used by DM: for their interpretation in that context, see DMPlexGetConeOrientation()).

perms - The permutations for the given orientations: set to NULL at conclusion

rots - The field rotations symmetries for the given orientations: set to NULL at conclusion

PetscSection, PetscSectionSym, PetscSectionRestorePointSyms(), petscSectionGetFieldPointSyms(), PetscSectionSymCreate(), PetscSectionSetSym(), PetscSectionGetSym()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSectionGetFieldPointSyms()
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionRestoreFieldPointSyms(PetscSection section, PetscInt field, PetscInt numPoints, const PetscInt *points, const PetscInt ***perms, const PetscScalar ***rots)
```

Example 3 (unknown):
```unknown
DMPlexGetConeOrientation()
```

Example 4 (unknown):
```unknown
PetscSectionSym
```

---

## PetscSectionRestorePointSyms#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionRestorePointSyms/

**Contents:**
- PetscSectionRestorePointSyms#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Restore the symmetries returned by PetscSectionGetPointSyms()

section - the section

numPoints - the number of points

points - an array of size 2 * numPoints, containing a list of (point, orientation) pairs. (An orientation is an arbitrary integer: its interpretation is up to sym. Orientations are used by DM: for their interpretation in that context, see DMPlexGetConeOrientation()).

perms - The permutations for the given orientations: set to NULL at conclusion

rots - The field rotations symmetries for the given orientations: set to NULL at conclusion

PetscSection, PetscSectionSym, PetscSectionGetPointSyms(), PetscSectionSymCreate(), PetscSectionSetSym(), PetscSectionGetSym()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSectionGetPointSyms()
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionRestorePointSyms(PetscSection section, PetscInt numPoints, const PetscInt *points, const PetscInt ***perms, const PetscScalar ***rots)
```

Example 3 (unknown):
```unknown
DMPlexGetConeOrientation()
```

Example 4 (unknown):
```unknown
PetscSectionSym
```

---

## PetscSectionSetBlockStarts#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetBlockStarts/

**Contents:**
- PetscSectionSetBlockStarts#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Sets a table indicating which points start new blocks

Not Collective, No Fortran Support

blockStarts - The PetscBT with a 1 for each point that begins a block

The table is on [0, pEnd - pStart). PETSc takes ownership of the PetscBT when it is passed in and will destroy it. The user should not destroy it.

This information is used by DMCreateMatrix() to create a variable block size description which is set using MatSetVariableBlockSizes().

Low-level Vector Communication, IS, PetscSection, PetscSectionGetBlockStarts(), PetscSectionCreate(), DMCreateMatrix(), MatSetVariableBlockSizes()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetBlockStarts(PetscSection s, PetscBT blockStarts)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
DMCreateMatrix()
```

Example 4 (unknown):
```unknown
MatSetVariableBlockSizes()
```

---

## PetscSectionSetChart#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetChart/

**Contents:**
- PetscSectionSetChart#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the range [pStart, pEnd) in which points (indices) lie for this PetscSection on this MPI process

pStart - the first point

pEnd - one past the last point, pStart \( \le \) pEnd

The chart may be thought of as the bounds on the points (indices) one may use to index into numerical data that is associated with the PetscSection data layout.

The charts on different MPI processes may (and often do) overlap

If you intend to use PetscSectionSetNumFields() it must be called before this call.

The chart for all fields created with PetscSectionSetNumFields() is the same as this chart.

PetscSection, PetscSection, PetscSectionGetChart(), PetscSectionCreate(), PetscSectionSetNumFields()

src/vec/is/section/interface/section.c

src/ts/tutorials/ex30.c src/snes/tutorials/ex7.c src/ts/tutorials/ex11.c src/dm/impls/plex/tutorials/ex7.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetChart(PetscSection s, PetscInt pStart, PetscInt pEnd)
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

## PetscSectionSetClosureIndex#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetClosureIndex/

**Contents:**
- PetscSectionSetClosureIndex#
- Synopsis#
- Input Parameters#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#

Create an internal data structure to speed up closure queries.

section - The PetscSection

obj - A PetscObject which serves as the key for this index

clSection - PetscSection giving the size of the closure of each point

clPoints - IS giving the points in each closure

This function creates an internal map from each point to its closure. We compress out closure points with no dofs in this section.

The information provided here is completely opaque

PetscSection, PetscSection, PetscSectionGetClosureIndex(), DMPlexCreateClosureIndex()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetClosureIndex(PetscSection section, PetscObject obj, PetscSection clSection, IS clPoints)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
PetscObject
```

Example 4 (unknown):
```unknown
PetscSection
```

---

## PetscSectionSetClosurePermutation#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetClosurePermutation/

**Contents:**
- PetscSectionSetClosurePermutation#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Set the dof permutation for the closure of each cell in the section, meaning clPerm[newIndex] = oldIndex.

section - The PetscSection

obj - A PetscObject which serves as the key for this index (usually a DM)

depth - Depth of points on which to apply the given permutation

perm - Permutation of the cell dof closure

The specified permutation will only be applied to points at depth whose closure size matches the length of perm. In a mixed-topology or variable-degree finite element space, this function can be called multiple times at each depth for each topology and degree.

This approach assumes that (depth, len(perm)) uniquely identifies the desired permutation; this might not be true for exotic/enriched spaces on mixed topology meshes.

PetscSection, PetscSection, IS, PetscSectionGetClosurePermutation(), PetscSectionGetClosureIndex(), DMPlexCreateClosureIndex(), PetscCopyMode

src/vec/is/section/interface/section.c

src/dm/impls/plex/tutorials/ex6.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetClosurePermutation(PetscSection section, PetscObject obj, PetscInt depth, IS perm)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
PetscObject
```

Example 4 (unknown):
```unknown
PetscSection
```

---

## PetscSectionSetComponentName#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetComponentName/

**Contents:**
- PetscSectionSetComponentName#
- Synopsis#
- Input Parameters#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the name of a field component in the PetscSection

field - the field number

comp - the component number

compName - the component name

Will error if the field or component number do not exist

The function name should have Field in it since they are field components.

PetscSection, PetscSection, PetscSectionGetComponentName(), PetscSectionSetNumFields(), PetscSectionGetNumFields(), PetscSectionSetFieldName(), PetscSectionGetFieldComponents(), PetscSectionSetFieldComponents()

src/vec/is/section/interface/section.c

src/dm/impls/plex/tutorials/ex15.c src/dm/impls/plex/tutorials/ex16.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetComponentName(PetscSection s, PetscInt field, PetscInt comp, const char compName[])
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

## PetscSectionSetConstraintDof#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetConstraintDof/

**Contents:**
- PetscSectionSetConstraintDof#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the number of constrained degrees of freedom associated with a given point.

numDof - the number of dof which are fixed by constraints

PetscSection, PetscSection, PetscSectionSetDof(), PetscSectionGetConstraintDof(), PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetConstraintDof(PetscSection s, PetscInt point, PetscInt numDof)
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
PetscSectionSetDof()
```

---

## PetscSectionSetConstraintIndices#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetConstraintIndices/

**Contents:**
- PetscSectionSetConstraintIndices#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the point dof numbers, in [0, dof), which are constrained

indices - The constrained dofs

PetscSection, PetscSectionGetConstraintIndices(), PetscSectionGetConstraintDof(), PetscSection

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetConstraintIndices(PetscSection s, PetscInt point, const PetscInt indices[])
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
PetscSectionGetConstraintIndices()
```

Example 4 (unknown):
```unknown
PetscSectionGetConstraintDof()
```

---

## PetscSectionSetDof#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetDof/

**Contents:**
- PetscSectionSetDof#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the total number of degrees of freedom associated with a given point.

numDof - the number of dof, these values may be negative -(dof+1) to indicate they are off process

This number is for the unnamed default field at the given point plus all degrees of freedom associated with all fields at that point

PetscSection, PetscSection, PetscSectionGetDof(), PetscSectionAddDof(), PetscSectionCreate()

src/vec/is/section/interface/section.c

src/ts/tutorials/ex30.c src/snes/tutorials/ex7.c src/ts/tutorials/ex11.c src/dm/impls/plex/tutorials/ex7.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetDof(PetscSection s, PetscInt point, PetscInt numDof)
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
PetscSectionGetDof()
```

---

## PetscSectionSetFieldComponents#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetFieldComponents/

**Contents:**
- PetscSectionSetFieldComponents#
- Synopsis#
- Input Parameters#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the number of field components for the given field.

field - the field number

numComp - the number of field components

This number can be different than the values set with PetscSectionSetFieldDof(). It can be used to indicate the number of components in the field of the underlying physical model which may be different than the number of degrees of freedom needed at a point in a discretization. For example, if in three dimensions the field is velocity, it will have 3 components, u, v, and w but an face based model for velocity (where the velocity normal to the face is stored) there is only 1 dof for each face point.

The value set with this function are not needed or used in PetscSectionSetUp().

This function is misnamed. There is a Num in PetscSectionSetNumFields() but not in this name

PetscSection, PetscSection, PetscSectionGetFieldComponents(), PetscSectionSetComponentName(), PetscSectionGetComponentName(), PetscSectionGetNumFields()

src/vec/is/section/interface/section.c

src/dm/impls/plex/tutorials/ex7.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetFieldComponents(PetscSection s, PetscInt field, PetscInt numComp)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
PetscSectionSetFieldDof()
```

Example 4 (unknown):
```unknown
PetscSectionSetUp()
```

---

## PetscSectionSetFieldConstraintDof#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetFieldConstraintDof/

**Contents:**
- PetscSectionSetFieldConstraintDof#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the number of constrained degrees of freedom associated with a given field on a point.

numDof - the number of dof which are fixed by constraints

PetscSection, PetscSection, PetscSectionSetDof(), PetscSectionGetFieldConstraintDof(), PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetFieldConstraintDof(PetscSection s, PetscInt point, PetscInt field, PetscInt numDof)
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
PetscSectionSetDof()
```

---

## PetscSectionSetFieldConstraintIndices#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetFieldConstraintIndices/

**Contents:**
- PetscSectionSetFieldConstraintIndices#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the field dof numbers, in [0, fdof), which are constrained

field - The field number

indices - The constrained dofs

PetscSection, PetscSectionSetConstraintIndices(), PetscSectionGetFieldConstraintIndices(), PetscSectionGetConstraintDof(), PetscSection

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetFieldConstraintIndices(PetscSection s, PetscInt point, PetscInt field, const PetscInt indices[])
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
PetscSectionSetConstraintIndices()
```

Example 4 (unknown):
```unknown
PetscSectionGetFieldConstraintIndices()
```

---

## PetscSectionSetFieldDof#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetFieldDof/

**Contents:**
- PetscSectionSetFieldDof#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the number of degrees of freedom associated with a field on a given point.

numDof - the number of dof, these values may be negative -(dof+1) to indicate they are off process

When setting the number of dof for a field at a point one must also ensure the count of the total number of dof at the point (summed over the fields and the unnamed default field) is correct by also calling PetscSectionAddDof() or PetscSectionSetDof()

This is equivalent to

PetscSection, PetscSection, PetscSectionGetFieldDof(), PetscSectionCreate(), PetscSectionAddDof(), PetscSectionSetDof()

src/vec/is/section/interface/section.c

src/dm/impls/plex/tutorials/ex7.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetFieldDof(PetscSection s, PetscInt point, PetscInt field, PetscInt numDof)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
PetscSectionAddDof()
```

Example 4 (unknown):
```unknown
PetscSectionSetDof()
```

---

## PetscSectionSetFieldName#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetFieldName/

**Contents:**
- PetscSectionSetFieldName#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the name of a field in the PetscSection

field - the field number

fieldName - the field name

Will error if the field number is out of range

PetscSection, PetscSectionGetFieldName(), PetscSectionSetNumFields(), PetscSectionGetNumFields()

src/vec/is/section/interface/section.c

src/dm/impls/plex/tutorials/ex1f90.F90 src/ts/tutorials/ex52.c src/dm/impls/plex/tutorials/ex1.c src/ts/tutorials/ex18.c src/dm/impls/plex/tutorials/ex14.c src/dm/impls/plex/tutorials/ex14f90.F90 src/dm/impls/plex/tutorials/ex16.c src/dm/impls/plex/tutorials/ex15.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetFieldName(PetscSection s, PetscInt field, const char fieldName[])
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (unknown):
```unknown
PetscSectionGetFieldName()
```

---

## PetscSectionSetFieldOffset#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetFieldOffset/

**Contents:**
- PetscSectionSetFieldOffset#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Set the offset into an array or Vec for the dof associated with the given field at a point.

offset - the offset, these values may be negative indicating the values are off process

The user usually does not call this function, but uses PetscSectionSetUp()

PetscSection, PetscSection, PetscSectionGetFieldOffset(), PetscSectionSetOffset(), PetscSectionCreate(), PetscSectionSetUp()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetFieldOffset(PetscSection s, PetscInt point, PetscInt field, PetscInt offset)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
PetscSectionSetUp()
```

Example 4 (unknown):
```unknown
PetscSection
```

---

## PetscSectionSetFieldSym#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetFieldSym/

**Contents:**
- PetscSectionSetFieldSym#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the symmetries for the data referred to by a field of the section

section - the section describing data layout

field - the field number

sym - the symmetry describing the affect of orientation on the access of the data

PetscSection, PetscSectionSym, PetscSectionGetFieldSym(), PetscSectionSymCreate()

src/vec/is/section/interface/section.c

src/dm/impls/plex/tutorials/ex6.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetFieldSym(PetscSection section, PetscInt field, PetscSectionSym sym)
```

Example 2 (unknown):
```unknown
PetscSectionSym
```

Example 3 (unknown):
```unknown
PetscSectionGetFieldSym()
```

Example 4 (unknown):
```unknown
PetscSectionSymCreate()
```

---

## PetscSectionSetFromOptions#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetFromOptions/

**Contents:**
- PetscSectionSetFromOptions#
- Synopsis#
- Input Parameter#
- Options Database Key#
- See Also#
- Level#
- Location#

sets parameters in a PetscSection from the options database

-petscsection_point_major - PETSC_TRUE for point-major order

PetscSection, PetscSection, PetscSectionCreate(), PetscSectionDestroy()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetFromOptions(PetscSection s)
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

## PetscSectionSetIncludesConstraints#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetIncludesConstraints/

**Contents:**
- PetscSectionSetIncludesConstraints#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the flag indicating if constrained dofs are to be included when computing offsets

includesConstraints - the flag indicating if constrained dofs are to be included when computing offsets

PetscSection, PetscSection, PetscSectionGetIncludesConstraints()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetIncludesConstraints(PetscSection s, PetscBool includesConstraints)
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
PetscSectionGetIncludesConstraints()
```

---

## PetscSectionSetNumFields#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetNumFields/

**Contents:**
- PetscSectionSetNumFields#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the number of fields in a PetscSection

numFields - the number of fields

Calling this destroys all the information in the PetscSection including the chart.

You must call PetscSectionSetChart() after calling this.

PetscSection, PetscSection, PetscSectionGetNumFields(), PetscSectionSetChart(), PetscSectionReset()

src/vec/is/section/interface/section.c

src/dm/impls/plex/tutorials/ex7.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetNumFields(PetscSection s, PetscInt numFields)
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

## PetscSectionSetOffset#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetOffset/

**Contents:**
- PetscSectionSetOffset#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Set the offset into an array or Vec for the dof associated with the given point.

offset - the offset, these values may be negative indicating the values are off process

The user usually does not call this function, but uses PetscSectionSetUp()

PetscSection, PetscSection, PetscSectionGetFieldOffset(), PetscSectionCreate(), PetscSectionSetUp()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetOffset(PetscSection s, PetscInt point, PetscInt offset)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
PetscSectionSetUp()
```

Example 4 (unknown):
```unknown
PetscSection
```

---

## PetscSectionSetPermutation#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetPermutation/

**Contents:**
- PetscSectionSetPermutation#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Sets a permutation of the chart for this section, [0, pEnd - pStart), which determines the order to store the PetscSection information

perm - the permutation of points

The permutation must be provided before PetscSectionSetUp().

The data in the PetscSection are permuted but the access via PetscSectionGetFieldOffset() and PetscSectionGetOffset() is not changed

Compare to PetscSectionPermute()

Low-level Vector Communication, IS, PetscSection, PetscSectionSetUp(), PetscSectionGetPermutation(), PetscSectionPermute(), PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetPermutation(PetscSection s, IS perm)
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (unknown):
```unknown
PetscSectionSetUp()
```

---

## PetscSectionSetPointMajor#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetPointMajor/

**Contents:**
- PetscSectionSetPointMajor#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the flag for dof ordering, PETSC_TRUE for point major, otherwise it will be field major

pm - the flag for point major ordering

Field-major order is not recommended unless you are managing the entire problem yourself, since many higher-level functions in PETSc depend on point-major order.

Point major order means the degrees of freedom are stored as follows

Field major order means the degrees of freedom are stored as follows

PetscSection, PetscSection, PetscSectionGetPointMajor(), PetscSectionSetPermutation()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetPointMajor(PetscSection s, PetscBool pm)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (sql):
```sql
all the degrees of freedom for each point are stored contiguously, one point after another (respecting a permutation set with `PetscSectionSetPermutation()`)
    for each point
       the degrees of freedom for each field (starting with the unnamed default field) are listed in order by field
```

Example 4 (sql):
```sql
all degrees of freedom for each field (including the unnamed default field) are stored contiguously, one field after another
    for each field (started with unnamed default field)
      the degrees of freedom for each point are listed in order by point (respecting a permutation set with `PetscSectionSetPermutation()`)
```

---

## PetscSectionSetSym#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetSym/

**Contents:**
- PetscSectionSetSym#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the symmetries for the data referred to by the section

section - the section describing data layout

sym - the symmetry describing the affect of orientation on the access of the data

PetscSection, PetscSectionSym, PetscSectionGetSym(), PetscSectionSymCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetSym(PetscSection section, PetscSectionSym sym)
```

Example 2 (unknown):
```unknown
PetscSectionSym
```

Example 3 (unknown):
```unknown
PetscSectionGetSym()
```

Example 4 (unknown):
```unknown
PetscSectionSymCreate()
```

---

## PetscSectionSetUpBC#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetUpBC/

**Contents:**
- PetscSectionSetUpBC#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Setup the subsections describing boundary conditions.

PetscSection, PetscSection, PetscSectionSetUp(), PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetUpBC(PetscSection s)
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
PetscSectionSetUp()
```

---

## PetscSectionSetUp#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetUp/

**Contents:**
- PetscSectionSetUp#
- Synopsis#
- Input Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Calculate offsets based upon the number of degrees of freedom for each point in preparation for use of the PetscSection

If used, PetscSectionSetPermutation() must be called before this routine.

PetscSectionSetPointMajor(), cannot be called after this routine.

PetscSection, PetscSection, PetscSectionCreate(), PetscSectionSetPermutation()

src/vec/is/section/interface/section.c

src/ts/tutorials/ex30.c src/snes/tutorials/ex7.c src/ts/tutorials/ex11.c src/dm/impls/plex/tutorials/ex7.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetUp(PetscSection s)
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (unknown):
```unknown
PetscSectionSetPermutation()
```

---

## PetscSectionSetUseFieldOffsets#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSetUseFieldOffsets/

**Contents:**
- PetscSectionSetUseFieldOffsets#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the flag to use field offsets directly in a global section, rather than just the point offset

s - the global PetscSection

PetscSection, PetscSectionSym, PetscSectionGetUseFieldOffsets(), PetscSectionSetChart(), PetscSectionCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSetUseFieldOffsets(PetscSection s, PetscBool flg)
```

Example 2 (unknown):
```unknown
PetscSection
```

Example 3 (unknown):
```unknown
PetscSectionSym
```

Example 4 (unknown):
```unknown
PetscSectionGetUseFieldOffsets()
```

---

## PetscSectionSymCopy#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSymCopy/

**Contents:**
- PetscSectionSymCopy#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Copy the symmetries, assuming that the point structure is compatible

sym - the PetscSectionSym

nsym - the equivalent symmetries

PetscSection, PetscSectionSym, PetscSectionSymCreate(), PetscSectionSetSym(), PetscSectionGetSym(), PetscSectionSymLabelSetStratum(), PetscSectionGetPointSyms()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSymCopy(PetscSectionSym sym, PetscSectionSym nsym)
```

Example 2 (unknown):
```unknown
PetscSectionSym
```

Example 3 (unknown):
```unknown
PetscSectionSym
```

Example 4 (unknown):
```unknown
PetscSectionSymCreate()
```

---

## PetscSectionSymCreate#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSymCreate/

**Contents:**
- PetscSectionSymCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Creates an empty PetscSectionSym object.

comm - the MPI communicator

sym - pointer to the new set of symmetries

PetscSection, PetscSection, PetscSectionSym, PetscSectionSymDestroy()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSectionSym
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSymCreate(MPI_Comm comm, PetscSectionSym *sym)
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (unknown):
```unknown
PetscSectionSym
```

---

## PetscSectionSymDestroy#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSymDestroy/

**Contents:**
- PetscSectionSymDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#

Destroys a section symmetry.

sym - the section symmetry

PetscSection, PetscSectionSym, PetscSectionSymCreate()

src/vec/is/section/interface/section.c

src/dm/impls/plex/tutorials/ex6.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSymDestroy(PetscSectionSym *sym)
```

Example 2 (unknown):
```unknown
PetscSectionSym
```

Example 3 (unknown):
```unknown
PetscSectionSymCreate()
```

---

## PetscSectionSymDistribute#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSymDistribute/

**Contents:**
- PetscSectionSymDistribute#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Distribute the symmetries in accordance with the input PetscSF

sym - the PetscSectionSym

migrationSF - the distribution map from roots to leaves

dsym - the redistributed symmetries

PetscSection, PetscSectionSym, PetscSectionSymCreate(), PetscSectionSetSym(), PetscSectionGetSym(), PetscSectionSymLabelSetStratum(), PetscSectionGetPointSyms()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSymDistribute(PetscSectionSym sym, PetscSF migrationSF, PetscSectionSym *dsym)
```

Example 2 (unknown):
```unknown
PetscSectionSym
```

Example 3 (unknown):
```unknown
PetscSectionSym
```

Example 4 (unknown):
```unknown
PetscSectionSymCreate()
```

---

## PetscSectionSymGetType#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSymGetType/

**Contents:**
- PetscSectionSymGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the section symmetry type name (as a string) from the PetscSectionSym.

sym - The section symmetry

type - The index set type name

PetscSection, PetscSectionSym, PetscSectionSymType, PetscSectionSymSetType(), PetscSectionSymCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSectionSym
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSymGetType(PetscSectionSym sym, PetscSectionSymType *type)
```

Example 3 (unknown):
```unknown
PetscSectionSym
```

Example 4 (unknown):
```unknown
PetscSectionSymType
```

---

## PetscSectionSymRegister#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSymRegister/

**Contents:**
- PetscSectionSymRegister#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Registers a new section symmetry implementation

Not Collective, No Fortran Support

sname - The name of a new user-defined creation routine

function - The creation routine itself

PetscSectionSymRegister() may be called multiple times to add several user-defined vectors

PetscSection, PetscSectionSym, PetscSectionSymType, PetscSectionSymCreate(), PetscSectionSymSetType()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSymRegister(const char sname[], PetscErrorCode (*function)(PetscSectionSym))
```

Example 2 (unknown):
```unknown
PetscSectionSymRegister()
```

Example 3 (unknown):
```unknown
PetscSectionSym
```

Example 4 (unknown):
```unknown
PetscSectionSymType
```

---

## PetscSectionSymSetType#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSymSetType/

**Contents:**
- PetscSectionSymSetType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Builds a PetscSectionSym, for a particular implementation.

sym - The section symmetry object

method - The name of the section symmetry type

PetscSection, PetscSectionSym, PetscSectionSymType, PetscSectionSymGetType(), PetscSectionSymCreate()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSectionSym
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSymSetType(PetscSectionSym sym, PetscSectionSymType method)
```

Example 3 (unknown):
```unknown
PetscSectionSym
```

Example 4 (unknown):
```unknown
PetscSectionSymType
```

---

## PetscSectionSymType#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSymType/

**Contents:**
- PetscSectionSymType#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#

String with the name of a PetscSectionSym type.

PetscSectionSym has no default implementation, but is used by DM in PetscSectionSymCreateLabel().

PetscSection, PetscSectionSymSetType(), PetscSectionSymGetType(), PetscSectionSym, PetscSectionSymCreate(), PetscSectionSymRegister()

include/petscsectiontypes.h

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSectionSym
```

Example 2 (unknown):
```unknown
typedef const char *PetscSectionSymType;
```

Example 3 (unknown):
```unknown
PetscSectionSym
```

Example 4 (unknown):
```unknown
PetscSectionSymCreateLabel()
```

---

## PetscSectionSymView#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSymView/

**Contents:**
- PetscSectionSymView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Displays a section symmetry

viewer - viewer used to display the set, for example PETSC_VIEWER_STDOUT_SELF.

PetscSectionSym, PetscViewer, PetscViewerASCIIOpen()

src/vec/is/section/interface/section.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionSymView(PetscSectionSym sym, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PETSC_VIEWER_STDOUT_SELF
```

Example 3 (unknown):
```unknown
PetscSectionSym
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscSectionSym#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionSym/

**Contents:**
- PetscSectionSym#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Symmetries of the data referenced by a PetscSection.

Often the order of data index by a PetscSection is meaningful, and describes additional structure, such as points on a line, grid, or lattice. If the data is accessed from a different “orientation”, then the image of the data under access then undergoes a symmetry transformation. A PetscSectionSym specifies these symmetries. The types of symmetries that can be specified are of the form R * P, where R is a diagonal matrix of scalars, and P is a permutation.

PetscSection, PetscSection, PetscSectionSymCreate(), PetscSectionSymDestroy(), PetscSectionSetSym(), PetscSectionGetSym(), PetscSectionSetFieldSym(), PetscSectionGetFieldSym(), PetscSectionGetSymPoints(), PetscSectionSymType, PetscSectionSymSetType(), PetscSectionSymGetType()

include/petscsectiontypes.h

src/dm/impls/plex/tutorials/ex6.c

_p_PetscSectionSym in include/petsc/private/sectionimpl.h PetscSectionSym_Label in src/dm/label/dmlabel.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (julia):
```julia
typedef struct _p_PetscSectionSym *PetscSectionSym;
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (unknown):
```unknown
PetscSectionSym
```

---

## PetscSectionViewFromOptions#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionViewFromOptions/

**Contents:**
- PetscSectionViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

View the PetscSection based on values in the options database

A - the PetscSection object to view

obj - Optional object that provides the options prefix used for the options

name - command line option

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

PetscSection, PetscSection, PetscSectionView, PetscObjectViewFromOptions(), PetscSectionCreate(), PetscSectionView()

src/vec/is/section/interface/section.c

src/dm/impls/plex/tutorials/ex1.c src/dm/impls/plex/tutorials/ex6.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionViewFromOptions(PetscSection A, PetscObject obj, const char name[])
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (unknown):
```unknown
PetscObjectViewFromOptions()
```

---

## PetscSectionView#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSectionView/

**Contents:**
- PetscSectionView#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Examples#

s - the PetscSection object to view

PetscSectionView(), when viewer is of type PETSCVIEWERHDF5, only saves distribution independent data, such as dofs, offsets, constraint dofs, and constraint indices. Points that have negative dofs, for instance, are not saved as they represent points owned by other processes. Point numbering and rank assignment is currently not stored. The saved section can be loaded with PetscSectionLoad().

PetscSection, PetscSection, PetscSectionCreate(), PetscSectionDestroy(), PetscSectionLoad(), PetscViewer

src/vec/is/section/interface/section.c

src/dm/impls/plex/tutorials/ex1f90.F90 src/snes/tutorials/ex13.c

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (unknown):
```unknown
#include "petscsection.h"   
PetscErrorCode PetscSectionView(PetscSection s, PetscViewer viewer)
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (unknown):
```unknown
PetscSectionView()
```

---

## PetscSection: Connecting Grids to Data#

**URL:** https://petsc.org/release/manual/section/

**Contents:**
- PetscSection: Connecting Grids to Data#
- General concept#
  - Charts: Defining mesh points#
  - Defining the (ndof, offset) tuple#
  - Basic Setup Example#
- Multiple Fields#
  - Setting Up Multiple Fields#
  - Point Major or Field Major#
- Working with data#
- Global Sections: Constrained and Distributed Data#

The strongest links between solvers and discretizations are

the relationship between the layout of data over a mesh (or similar structure) and the data layout in arrays and Vec used for computation,

data partitioning, and

To enable modularity, we encode the operations above in simple data structures that can be understood by the linear algebraic and solver components of PETSc (Vec, Mat, KSP, PC, SNES, TS, Tao, PetscRegressor) without explicit reference to the mesh (topology) or discretization (analysis).

While PetscSection is currently only employed for DMPlex, DMForest, and DMNetwork mesh descriptions, much of its operation is general enough to be utilized for other types of discretizations. This section will explain the basic concepts of a PetscSection that are generalizable to other mesh descriptions.

Specific entries (or collections of entries) in a Vec (or a simple array) can be associated with a “location” on a mesh (or other types of data structure) using the PetscSection object. A point is a PetscInt that serves as an abstract “index” into arrays from iterable sets, such as k-cells in a mesh. Other iterable set examples can be as simple as the points of a finite difference grid, or cells of a finite volume grid, or as complex as the topological entities of an unstructured mesh (cells, faces, edges, and vertices).

At it’s most basic, a PetscSection is a mapping between the mesh points and a tuple (ndof, offset), where ndof is the number of values stored at that mesh point and offset is the location in the array of that data. So given the tuple for a mesh point, its data can be accessed by array[offset + d], where d in [0, ndof) is the dof to access.

The mesh points for a PetscSection must be contiguously numbered and are defined to be in some range \([\mathrm{pStart}, \mathrm{pEnd})\), which is called a chart. The chart of a PetscSection is set via PetscSectionSetChart(). Note that even though the mesh points must be contiguously numbered, the indexes into the array (defined by each (ndof, offset) tuple) associated with the PetscSection need not be. In other words, there may be elements in the array that are not associated with any mesh points, though this is not often the case.

Defining the (ndof, offset) tuple for each mesh point generally first starts with setting the ndof for each point, which is done using PetscSectionSetDof(). This associates a set of degrees of freedom (dof), (a small space \(\{e_k\}\ 0 < k < ndof\)), with every point. If ndof is not set for a mesh point, it is assumed to be 0.

The offset for each mesh point is usually set automatically by PetscSectionSetUp(). This will concatenate each mesh point’s dofs together in the order of the mesh points. This concatenation can be done in a different order by setting a permutation, which is described in Permutation: Changing the order of array data.

Alternatively, the offset for each mesh point can be set manually by PetscSectionSetOffset(), though this is not commonly needed.

Once the tuples are created, the PetscSection is ready to use.

To summarize, the sequence for constructing a basic PetscSection is the following:

Specify the range of points, or chart, with PetscSectionSetChart().

Specify the number of dofs per point with PetscSectionSetDof(). Any values not set will be zero.

Set up the PetscSection with PetscSectionSetUp().

In many discretizations, it is useful to differentiate between different kinds of dofs present on a mesh. For example, a dof attached to a cell point might represent pressure while dofs on vertices might represent velocity or displacement. A PetscSection can represent this additional structure with what are called fields. Fields are indexed contiguously from [0, num_fields). To set the number of fields for a PetscSection, call PetscSectionSetNumFields().

Internally, each field is stored in a separate PetscSection. In fact, all the concepts and functions presented in General concept were actually applied onto the default field, which is indexed as 0. The fields inherit the same chart as the “parent” PetscSection.

Setup for a PetscSection with multiple fields is nearly identical to setup for a single field.

The sequence for constructing such a PetscSection is the following:

Specify the range of points, or chart, with PetscSectionSetChart(). All fields share the same chart.

Specify the number of fields with PetscSectionSetNumFields().

Set the number of dof for each point on each field with PetscSectionSetFieldDof(). Any values not set will be zero.

Set the total number of dof for each point with PetscSectionSetDof(). Thus value must be greater than or equal to the sum of the values set with PetscSectionSetFieldDof() at that point. Again, values not set will be zero.

Set up the PetscSection with PetscSectionSetUp().

A PetscSection with one field and and offsets set in PetscSectionSetUp() may be thought of as defining a two dimensional array indexed by point in the outer dimension with a variable length inner dimension indexed by the dof at that point: \(v[\mathrm{pStart} <= point < \mathrm{pEnd}][0 <= dof < \mathrm{ndof}]\) [1].

With multiple fields, this array is now three dimensional, with the outer dimensions being both indexed by mesh points and field points. Thus, there is a choice on whether to index by points first, or by fields first. In other words, will the array be laid out in a point-major or field-major fashion.

Point-major ordering corresponds to \(v[\mathrm{pStart} <= point < \mathrm{pEnd}][0 <= field < \mathrm{num\_fields}][0 <= dof < \mathrm{ndof}]\). All the dofs for each mesh point are stored contiguously, meaning the fields are interlaced. Field-major ordering corresponds to \(v[0 <= field < \mathrm{num\_fields}][\mathrm{pStart} <= point < \mathrm{pEnd}][0 <= dof < \mathrm{ndof}]\). The all the dofs for each field are stored contiguously, meaning the points are interlaced.

Consider a PetscSection with 2 fields and 2 points (from 0 to 2). Let the 0th field have ndof=1 for each point and the 1st field have ndof=2 for each point. Denote each array entry \((p_i, f_i, d_i)\) for \(p_i\) being the ith point, \(f_i\) being the ith field, and \(d_i\) being the ith dof.

Point-major order would result in:

Conversely, field-major ordering would result in:

Note that dofs are always contiguous, regardless of the outer dimensional ordering.

Setting the which ordering is done with PetscSectionSetPointMajor(), where PETSC_TRUE sets point-major and PETSC_FALSE sets field major.

NOTE: The current default is for point-major, and many operations on DMPlex will only work with this ordering. Field-major ordering is provided mainly for compatibility with external packages, such as LibMesh.

Once a PetscSection has been created one can use PetscSectionGetStorageSize() to determine the total number of entries that can be stored in an array or Vec accessible by the PetscSection. This is most often used when creating a new Vec for a PetscSection such as:

The memory locations in the associated array are found using an offset which can be obtained with:

Single-field PetscSection:

Multi-field PetscSection:

The value in the array is then accessed with array[offset + d], where d in [0, ndof) is the dof to access.

To handle distributed data and data with constraints, we use a pair of PetscSections called the localSection and globalSection. Their use for each is described below.

PetscSection can also be applied to distributed problems as well. This is done using the same local/global system described in Local/global vectors and communicating between vectors. To do this, we introduce three new concepts; a localSection, globalSection, pointSF, and sectionSF.

Assume the mesh points of the “global” mesh are partitioned among processes and that some mesh points are shared between multiple processes (i.e there is an overlap in the partitions). The shared mesh points define the ghost/halo points needed in many PDE problems. For each shared mesh point, appoint one process to be the owner of that mesh point. To describe this parallel mesh point layout, we use a PetscSF and call it the pointSF. The pointSF describes which processes “own” which mesh points and which process is the owner of each shared mesh point.

Next, for each process define a PetscSection that describes the mapping between that process’s partition (including shared mesh points) and the data stored on it and call it the localSection. The localSection describes the layout of the local vector. To generate the globalSection we use PetscSectionCreateGlobalSection(), which takes the localSection and pointSF as inputs. The global section returns \(-(dof+1)\) for the number of dofs on an unowned (ghost) point, and traditionally \(-(off+1)\) for its offset on the owning process. This behavior of the offsets is controlled via an argument to PetscSectionCreateGlobalSection(). The globalSection can be used to create global vectors, just as the local section is used to create local vectors.

To perform the global-to-local and local-to-global communication, we define sectionSF to be the PetscSF describing the mapping between the local and global vectors. This is generated via PetscSFSetGraphSection(). Using PetscSFBcastBegin() will send data from the global vector to the local vector, while PetscSFReduceBegin() will send data from the local vector to the global vector.

If using DM, this entire process is done automatically. The localSection, globalSection, pointSF, and sectionSF on a DM can be obtained via DMGetLocalSection(), DMGetGlobalSection(), DMGetPointSF(), and DMGetSectionSF(), respectively. Additionally, communication from global to local vectors and vice versa can be done via DMGlobalToLocal() and DMLocalToGlobal() as described in Local/global vectors and communicating between vectors. Note that not all DM types use this system, such as DMDA (see DMDA - Creating vectors for structured grids).

In addition to describing parallel data, the localSection/globalSection pair can be used to describe constrained dofs These constraints usually represent essential (Dirichlet) boundary conditions, or algebraic constraints. They are dofs that have a given fixed value, so they are present in local vectors for finite element/volume assembly or finite difference stencil application purposes, but generally absent from global vectors since they are not unknowns in the algebraic solves.

Constraints should be indicated in the localSection. Use PetscSectionSetConstraintDof() to set the number of constrained dofs for a given point, and PetscSectionSetConstraintIndices() to indicate which dofs on the given point are constrained. This must be done before PetscSectionCreateGlobalSection() is called to create the globalSection.

Note that it is possible to have constraints set in a localSection, but have the globalSection be generated to include those constraints. This is useful when doing some form of post-processing of a solution where you want to access all data (see DMGetOutputDM() for example). See PetscSectionCreateGlobalSection() for more details on this.

By default, when PetscSectionSetUp() is called, the data laid out in the associated array is assumed to be in the same order of the grid points. For example, the DoFs associated with grid point 0 appear directly before grid point 1, which appears before grid point 2, etc.

It may be desired to have a different the ordering of data in the array than the order of grid points defined by a section. For example, one may want grid points associated with the boundary of a domain to appear before points associated with the interior of the domain.

This can be accomplished by either changing the indexes of the grid points themselves, or by informing the section of the change in array ordering. Either method uses an IS to define the permutation.

To change the indices of the grid points, call PetscSectionPermute() to generate a new PetscSection with the desired grid point permutation.

To just change the array layout without changing the grid point indexing, call PetscSectionSetPermutation(). This must be called before PetscSectionSetUp() and will only affect the calculation of the offsets for each grid point.

A vanilla PetscSection (what’s been described up till now) gives a relatively naive perspective on the underlying data; it doesn’t describe how DoFs attached to a single grid point are ordered or how different grid points relate to each other. A PetscSection can store and use this extra information in the form of closures, symmetries, and closure permutations. These features currently target DMPlex and other unstructured grid descriptions. A description of those features will be left to DMPlex: Unstructured Grids.

A PetscSection can be thought of as a generalization of PetscLayout, in the same way that a fiber bundle is a generalization of the normal Euclidean basis used in linear algebra. With PetscLayout, we associate a unit vector (\(e_i\)) with every point in the space, and just divide up points between processes. Conversely, PetscSection associates multiple unit vectors with every mesh point (one for each dof) and divides the mesh points between processes using a PetscSF to define the distribution.

DMPlex: Unstructured Grids

**Examples:**

Example 1 (unknown):
```unknown
PetscRegressor
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
PetscSection
```

---

## PetscSection#

**URL:** https://petsc.org/release/manualpages/PetscSection/PetscSection/

**Contents:**
- PetscSection#
- Synopsis#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Provides a mapping from integers in a designated domain (defined by bounds startp to endp) to integers which can then be used for accessing entries in arrays, other PetscSections, ISs, Vecs, and Mats.

One can think of PetscSection as a library-based tool for indexing into multi-dimensional jagged arrays which is needed since programming languages do not provide jagged array functionality baked into their syntax.

The domain, startp to endp, is called the chart of the PetscSection() and is set with PetscSectionSetChart() and accessed PetscSectionGetChart(). startp does not need to be 0, endp must be greater than or equal to startp and the bounds may be positive or negative.

The range of a PetscSection is in the space of contiguous sets of integers. These ranges are frequently interpreted as domains (charts, meaning lower and upper bounds) of other array-like objects, especially other PetscSections, ISs, and Vecs.

For each point in the chart (from startp to endp) of a PetscSection, the output set is represented through an offset and a count, which can be obtained using PetscSectionGetOffset() and PetscSectionGetDof() respectively and can be set via PetscSectionSetOffset() and PetscSectionSetDof(). Lookup is typically using accessors or routines like VecGetValuesSection()

The indices returned by the PetscSection are appropriate for the kind of Vec it is associated with. For example, if the vector being indexed is a local vector, we call the section a local section. If the section indexes a global vector, we call it a global section. For parallel vectors, like global vectors, we use negative indices to indicate dofs owned by other processes.

Typically PetscSections are first constructed via a series of calls to PetscSectionSetOffset() and PetscSectionSetDof(), finalized via a call to PetscSectionSetup() and then used to index into arrays and other PETSc objects. The construction (setup) phase corresponds to providing all the information needed to define the multi-dimensional jagged array structure.

PetscSection is used heavily by DMPLEX. Simpler DM, such as DMDA, generally do not need PetscSection since their array access patterns are simpler and can be fully expressed using standard programming language array syntax, see DM commonality.

PetscSection, PetscSectionCreate(), PetscSectionGetOffset(), PetscSectionGetDof(), PetscSectionSetChart(), PetscSectionGetChart(), PetscSectionDestroy(), PetscSectionSym, PetscSectionSetup(), DM, DMDA, DMPLEX

include/petscsectiontypes.h

src/ts/tutorials/ex11.c src/ts/tutorials/ex30.c src/ts/tutorials/ex52.c src/ts/tutorials/ex18.c src/snes/tutorials/ex13.c src/snes/tutorials/ex56.c src/tao/tutorials/ex3.c src/snes/tutorials/ex7.c src/snes/tutorials/ex77.c

_p_PetscSection in include/petsc/private/sectionimpl.h

Index of all PetscSection routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

Example 2 (julia):
```julia
typedef struct _p_PetscSection *PetscSection;
```

Example 3 (unknown):
```unknown
PetscSection
```

Example 4 (unknown):
```unknown
PetscSection()
```

---

## PetscSpaceRegisterAll#

**URL:** https://petsc.org/release/manualpages/DM/PetscSpaceRegisterAll/

**Contents:**
- PetscSpaceRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the PetscSpace components in the PetscFE package.

PetscSpaceRegister(), PetscSpaceRegisterDestroy()

src/dm/interface/dmregall.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"  
#include "petscdmplex.h"  
#include "petscfe.h"  
PetscErrorCode PetscSpaceRegisterAll(void)
```

Example 2 (unknown):
```unknown
PetscSpaceRegister()
```

Example 3 (unknown):
```unknown
PetscSpaceRegisterDestroy()
```

---

## PetscUnit#

**URL:** https://petsc.org/release/manualpages/DM/PetscUnit/

**Contents:**
- PetscUnit#
- Synopsis#
- See Also#
- Level#
- Location#

The seven fundamental SI units

DMPlexGetScale(), DMPlexSetScale()

include/petscdmtypes.h

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  PETSC_UNIT_LENGTH,
  PETSC_UNIT_MASS,
  PETSC_UNIT_TIME,
  PETSC_UNIT_CURRENT,
  PETSC_UNIT_TEMPERATURE,
  PETSC_UNIT_AMOUNT,
  PETSC_UNIT_LUMINOSITY,
  NUM_PETSC_UNITS
} PetscUnit;
```

Example 2 (unknown):
```unknown
DMPlexGetScale()
```

Example 3 (unknown):
```unknown
DMPlexSetScale()
```

---

## Section Data Layout (PetscSection)#

**URL:** https://petsc.org/release/manualpages/PetscSection/

**Contents:**
- Section Data Layout (PetscSection)#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Single list of manual pages#

PetscSection provides an interface to describe arbitrary data layouts onto entries of a Vec or array. User guide section: PetscSection: Connecting Grids to Data.

PetscSectionAddConstraintDof

PetscSectionAddFieldConstraintDof

PetscSectionAddFieldDof

PetscSectionCreateGlobalSection

PetscSectionGetBlockStarts

PetscSectionGetClosureInversePermutation

PetscSectionGetClosurePermutation

PetscSectionGetComponentName

PetscSectionGetConstrainedStorageSize

PetscSectionGetConstraintDof

PetscSectionGetConstraintIndices

PetscSectionGetFieldConstraintDof

PetscSectionGetFieldConstraintIndices

PetscSectionGetFieldDof

PetscSectionGetFieldName

PetscSectionGetFieldOffset

PetscSectionGetIncludesConstraints

PetscSectionGetMaxDof

PetscSectionGetNumFields

PetscSectionGetOffset

PetscSectionGetOffsetRange

PetscSectionGetPermutation

PetscSectionGetPointMajor

PetscSectionGetStorageSize

PetscSectionHasConstraints

PetscSectionResetClosurePermutation

PetscSectionSetBlockStarts

PetscSectionSetClosurePermutation

PetscSectionSetConstraintDof

PetscSectionSetConstraintIndices

PetscSectionSetFieldConstraintDof

PetscSectionSetFieldConstraintIndices

PetscSectionSetFieldDof

PetscSectionSetFieldName

PetscSectionSetFromOptions

PetscSectionSetIncludesConstraints

PetscSectionSetNumFields

PetscSectionSetPermutation

PetscSectionSetPointMajor

PetscSectionViewFromOptions

PetscSectionCreateComponentSubsection

PetscSectionCreateGlobalSectionCensored

PetscSectionCreateSubdomainSection

PetscSectionCreateSubmeshSection

PetscSectionCreateSubsection

PetscSectionCreateSupersection

PetscSectionGetClosureIndex

PetscSectionGetFieldComponents

PetscSectionGetFieldPointOffset

PetscSectionGetPointLayout

PetscSectionGetValueLayout

PetscSectionMigrateData

PetscSectionSetClosureIndex

PetscSectionSetComponentName

PetscSectionSetFieldComponents

PetscSectionArrayView

PetscSectionExtractDofsFromArray

PetscSectionGetFieldPointSyms

PetscSectionGetFieldSym

PetscSectionGetPointSyms

PetscSectionGetUseFieldOffsets

PetscSectionRestoreFieldPointSyms

PetscSectionRestorePointSyms

PetscSectionSetFieldOffset

PetscSectionSetFieldSym

PetscSectionSetOffset

PetscSectionSetUseFieldOffsets

PetscSectionSymCreate

PetscSectionSymDestroy

PetscSectionSymDistribute

PetscSectionSymGetType

PetscSectionSymRegister

PetscSectionSymSetType

PetscSectionAddConstraintDof

PetscSectionAddFieldConstraintDof

PetscSectionAddFieldDof

PetscSectionArrayView

PetscSectionCreateComponentSubsection

PetscSectionCreateGlobalSection

PetscSectionCreateGlobalSectionCensored

PetscSectionCreateSubdomainSection

PetscSectionCreateSubmeshSection

PetscSectionCreateSubsection

PetscSectionCreateSupersection

PetscSectionExtractDofsFromArray

PetscSectionGetBlockStarts

PetscSectionGetClosureIndex

PetscSectionGetClosureInversePermutation

PetscSectionGetClosurePermutation

PetscSectionGetComponentName

PetscSectionGetConstrainedStorageSize

PetscSectionGetConstraintDof

PetscSectionGetConstraintIndices

PetscSectionGetFieldComponents

PetscSectionGetFieldConstraintDof

PetscSectionGetFieldConstraintIndices

PetscSectionGetFieldDof

PetscSectionGetFieldName

PetscSectionGetFieldOffset

PetscSectionGetFieldPointOffset

PetscSectionGetFieldPointSyms

PetscSectionGetFieldSym

PetscSectionGetIncludesConstraints

PetscSectionGetMaxDof

PetscSectionGetNumFields

PetscSectionGetOffset

PetscSectionGetOffsetRange

PetscSectionGetPermutation

PetscSectionGetPointLayout

PetscSectionGetPointMajor

PetscSectionGetPointSyms

PetscSectionGetStorageSize

PetscSectionGetUseFieldOffsets

PetscSectionGetValueLayout

PetscSectionHasConstraints

PetscSectionMigrateData

PetscSectionResetClosurePermutation

PetscSectionRestoreFieldPointSyms

PetscSectionRestorePointSyms

PetscSectionSetBlockStarts

PetscSectionSetClosureIndex

PetscSectionSetClosurePermutation

PetscSectionSetComponentName

PetscSectionSetConstraintDof

PetscSectionSetConstraintIndices

PetscSectionSetFieldComponents

PetscSectionSetFieldConstraintDof

PetscSectionSetFieldConstraintIndices

PetscSectionSetFieldDof

PetscSectionSetFieldName

PetscSectionSetFieldOffset

PetscSectionSetFieldSym

PetscSectionSetFromOptions

PetscSectionSetIncludesConstraints

PetscSectionSetNumFields

PetscSectionSetOffset

PetscSectionSetPermutation

PetscSectionSetPointMajor

PetscSectionSetUseFieldOffsets

PetscSectionSymCreate

PetscSectionSymDestroy

PetscSectionSymDistribute

PetscSectionSymGetType

PetscSectionSymRegister

PetscSectionSymSetType

PetscSectionViewFromOptions

Star Forest Communication (PetscSF)

Application Orderings (AO)

**Examples:**

Example 1 (unknown):
```unknown
PetscSection
```

---

## VecGetDM#

**URL:** https://petsc.org/release/manualpages/DM/VecGetDM/

**Contents:**
- VecGetDM#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Gets the DM defining the data layout of the vector

A Vec may not have a DM associated with it.

DM Basics, DM, VecSetDM(), DMGetLocalVector(), DMGetGlobalVector(), DMSetVecType()

src/dm/interface/dm.c

src/snes/tutorials/ex11.c src/ts/tutorials/ex18.c src/snes/tutorials/ex13.c src/ts/tutorials/ex48.c src/snes/tutorials/ex36.c src/ksp/ksp/tutorials/ex43.c src/ts/utils/dmplexlandau/tutorials/ex2.c src/snes/tutorials/ex27.c src/snes/tutorials/ex7.c src/snes/tutorials/ex22.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode VecGetDM(Vec v, DM *dm)
```

Example 2 (unknown):
```unknown
DMGetLocalVector()
```

Example 3 (unknown):
```unknown
DMGetGlobalVector()
```

Example 4 (unknown):
```unknown
DMSetVecType()
```

---

## VecSetDM#

**URL:** https://petsc.org/release/manualpages/DM/VecSetDM/

**Contents:**
- VecSetDM#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the DM defining the data layout of the vector.

This is rarely used, generally one uses DMGetLocalVector() or DMGetGlobalVector() to create a vector associated with a given DM

This is NOT the same as DMCreateGlobalVector() since it does not change the view methods or perform other customization, but merely sets the DM member.

DM Basics, DM, VecGetDM(), DMGetLocalVector(), DMGetGlobalVector(), DMSetVecType()

src/dm/interface/dm.c

src/ksp/ksp/tutorials/ex43.c src/ksp/ksp/tutorials/ex65.c src/ksp/ksp/tutorials/ex73.c src/ts/tutorials/ex30.c

Index of all DM routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscdm.h"          
#include "petscdmlabel.h"     
#include "petscds.h"     
PetscErrorCode VecSetDM(Vec v, DM dm)
```

Example 2 (unknown):
```unknown
DMGetLocalVector()
```

Example 3 (unknown):
```unknown
DMGetGlobalVector()
```

Example 4 (unknown):
```unknown
DMCreateGlobalVector()
```

---
