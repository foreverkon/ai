# Petsc-Docs-Full-Raw - Optimization Learning

**Pages:** 477

---

## ADMM_UPDATE_ADAPTIVE_RELAXED#

**URL:** https://petsc.org/release/manualpages/Tao/ADMM_UPDATE_ADAPTIVE_RELAXED/

**Contents:**
- ADMM_UPDATE_ADAPTIVE_RELAXED#
- Note#
- See Also#
- Level#
- Location#

Adaptively update spectral penalty, and relaxes parameter update

With adaptive spectral penalty update, it also relaxes the x vector update by a factor.

TAO: Optimization Solvers, Tao, TaoADMMSetUpdateType(), TAO_ADMM_UPDATE_BASIC, TAO_ADMM_UPDATE_ADAPTIVE

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoADMMSetUpdateType()
```

Example 2 (unknown):
```unknown
TAO_ADMM_UPDATE_BASIC
```

Example 3 (unknown):
```unknown
TAO_ADMM_UPDATE_ADAPTIVE
```

---

## Data Assimilation (PetscDA)#

**URL:** https://petsc.org/release/manualpages/PetscDA/

**Contents:**
- Data Assimilation (PetscDA)#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Single list of manual pages#

The PetscDA object provides a high-level framework for data assimilation capabilities.

It currently only provides ensemble-based data assimilation capabilities for combining model forecasts with observations in dynamical systems. It centralizes ensemble storage, observational metadata, and user-defined forecast/analysis operators, enabling algorithms to run independently of MPI layout or vector/matrix backends. Users guide chapter: PetscDA: Data Assimilation

PetscDAEnsembleGetSize

PetscDAEnsembleInitialize

PetscDAEnsembleSetSize

PetscDAGetObsErrorVariance

PetscDASetObsErrorVariance

PetscDAViewFromOptions

PetscDAEnsembleAnalysis

PetscDAEnsembleComputeAnomalies

PetscDAEnsembleComputeMean

PetscDAEnsembleForecast

PetscDAEnsembleGetInflation

PetscDAEnsembleGetMember

PetscDAEnsembleRestoreMember

PetscDAEnsembleSetInflation

PetscDAEnsembleSetMember

PetscDALETKFGetLocalizationMatrix

PetscDASetFromOptions

PetscDAAppendOptionsPrefix

PetscDAEnsembleApplySqrtTInverse

PetscDAEnsembleApplyTInverse

PetscDAEnsembleGetSqrtType

PetscDAEnsembleSetSqrtType

PetscDAEnsembleTFactor

PetscDAGetOptionsPrefix

PetscDALETKFGetObsPerVertex

PetscDALETKFSetLocalization

PetscDALETKFSetObsPerVertex

PetscDASetOptionsPrefix

PetscDAEnsembleComputeNormalizedInnovationMatrix

PetscDAFinalizePackage

PetscDAInitializePackage

PetscDAAppendOptionsPrefix

PetscDAEnsembleAnalysis

PetscDAEnsembleApplySqrtTInverse

PetscDAEnsembleApplyTInverse

PetscDAEnsembleComputeAnomalies

PetscDAEnsembleComputeMean

PetscDAEnsembleComputeNormalizedInnovationMatrix

PetscDAEnsembleForecast

PetscDAEnsembleGetInflation

PetscDAEnsembleGetMember

PetscDAEnsembleGetSize

PetscDAEnsembleGetSqrtType

PetscDAEnsembleInitialize

PetscDAEnsembleRestoreMember

PetscDAEnsembleSetInflation

PetscDAEnsembleSetMember

PetscDAEnsembleSetSize

PetscDAEnsembleSetSqrtType

PetscDAEnsembleTFactor

PetscDAFinalizePackage

PetscDAGetObsErrorVariance

PetscDAGetOptionsPrefix

PetscDAInitializePackage

PetscDALETKFGetLocalizationMatrix

PetscDALETKFGetObsPerVertex

PetscDALETKFSetLocalization

PetscDALETKFSetObsPerVertex

PetscDASetFromOptions

PetscDASetObsErrorVariance

PetscDASetOptionsPrefix

PetscDAViewFromOptions

Regression Analysis and Classification (PetscRegressor)

Graphics and Visualization

---

## Machine Learning#

**URL:** https://petsc.org/release/manualpages/MachineLearning/

**Contents:**
- Machine Learning#

Objective Function Terms (TaoTerm)

Regression Analysis and Classification (PetscRegressor)

---

## MatCreateSubMatrixFree#

**URL:** https://petsc.org/release/manualpages/Tao/MatCreateSubMatrixFree/

**Contents:**
- MatCreateSubMatrixFree#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#

Creates a reduced matrix by masking a full matrix.

mat - matrix of arbitrary type

Rows - the rows that will be in the submatrix

Cols - the columns that will be in the submatrix

The caller is responsible for destroying the input objects after matrix J has been destroyed.

This should be moved/supported in Mat

src/tao/matrix/submatfree.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode MatCreateSubMatrixFree(Mat mat, IS Rows, IS Cols, Mat *J)
```

Example 2 (unknown):
```unknown
MatCreate()
```

---

## MatDFischer#

**URL:** https://petsc.org/release/manualpages/Tao/MatDFischer/

**Contents:**
- MatDFischer#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Calculates an element of the B-subdifferential of the Fischer-Burmeister function for complementarity problems.

jac - the jacobian of f at X

Con - constraints function evaluated at X

Da - diagonal perturbation component of the result

Db - row scaling component of the result

Mat, VecFischer(), VecSFischer(), MatDSFischer()

src/tao/util/tao_util.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode MatDFischer(Mat jac, Vec X, Vec Con, Vec XL, Vec XU, Vec T1, Vec T2, Vec Da, Vec Db)
```

Example 2 (unknown):
```unknown
VecFischer()
```

Example 3 (unknown):
```unknown
VecSFischer()
```

Example 4 (unknown):
```unknown
MatDSFischer()
```

---

## MatDSFischer#

**URL:** https://petsc.org/release/manualpages/Tao/MatDSFischer/

**Contents:**
- MatDSFischer#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Calculates an element of the B-subdifferential of the smoothed Fischer-Burmeister function for complementarity problems.

jac - the jacobian of f at X

Con - constraint function evaluated at X

mu - smoothing parameter

Da - diagonal perturbation component of the result

Db - row scaling component of the result

Dm - derivative with respect to scaling parameter

Mat, VecFischer(), VecSFischer(), MatDFischer()

src/tao/util/tao_util.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode MatDSFischer(Mat jac, Vec X, Vec Con, Vec XL, Vec XU, PetscReal mu, Vec T1, Vec T2, Vec Da, Vec Db, Vec Dm)
```

Example 2 (unknown):
```unknown
VecFischer()
```

Example 3 (unknown):
```unknown
VecSFischer()
```

Example 4 (unknown):
```unknown
MatDFischer()
```

---

## Objective Function Terms (TaoTerm)#

**URL:** https://petsc.org/release/manualpages/TaoTerm/

**Contents:**
- Objective Function Terms (TaoTerm)#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Single list of manual pages#

TaoTerm provides an interface to constructing and manipulating multiple separate terms in the objective function of an optimization problem solved with a Tao solver.

TaoTermCreateHalfL2Squared

TaoTermCreateQuadratic

TaoTermGetParametersSizes

TaoTermGetSolutionSizes

TaoTermSetFromOptions

TaoTermSetParametersSizes

TaoTermSetSolutionSizes

TaoTermDuplicateOption

TaoTermGetParametersLayout

TaoTermGetParametersMode

TaoTermGetSolutionLayout

TaoTermObjectiveAndGradientFn

TaoTermParametersMode

TaoTermQuadraticGetMat

TaoTermQuadraticSetMat

TaoTermSetParametersLayout

TaoTermSetParametersTemplate

TaoTermSetSolutionLayout

TaoTermSetSolutionTemplate

TaoTermShellGetContext

TaoTermShellSetContext

TaoTermShellSetContextDestroy

TaoTermShellSetCreateHessianMatrices

TaoTermShellSetCreateParametersVec

TaoTermShellSetCreateSolutionVec

TaoTermShellSetGradient

TaoTermShellSetHessian

TaoTermShellSetIsComputeHessianFDPossible

TaoTermShellSetObjective

TaoTermShellSetObjectiveAndGradient

TaoTermSumParametersUnpack

VecNestGetTaoTermSumParameters

TaoTermComputeGradientFD

TaoTermComputeGradientGetUseFD

TaoTermComputeGradientSetUseFD

TaoTermComputeHessianFD

TaoTermComputeHessianGetUseFD

TaoTermComputeHessianMFFD

TaoTermComputeHessianSetUseFD

TaoTermCreateHessianMFFD

TaoTermCreateHessianMatrices

TaoTermCreateParametersVec

TaoTermCreateSolutionVec

TaoTermGetParametersVecType

TaoTermGetSolutionVecType

TaoTermSetParametersMode

TaoTermSetParametersVecType

TaoTermSetSolutionVecType

TaoTermComputeGradient

TaoTermComputeHessian

TaoTermComputeObjective

TaoTermComputeObjectiveAndGradient

TaoTermCreateHessianMatricesDefault

TaoTermGetCreateHessianMode

TaoTermIsComputeHessianFDPossible

TaoTermIsCreateHessianMatricesDefined

TaoTermIsGradientDefined

TaoTermIsHessianDefined

TaoTermIsObjectiveAndGradientDefined

TaoTermIsObjectiveDefined

TaoTermSetCreateHessianMode

TaoTermSumGetLastTermObjectives

TaoTermSumGetNumberTerms

TaoTermSumGetTermHessianMatrices

TaoTermSumGetTermMask

TaoTermSumParametersPack

TaoTermSumSetNumberTerms

TaoTermSumSetTermHessianMatrices

TaoTermSumSetTermMask

TaoTermComputeGradient

TaoTermComputeGradientFD

TaoTermComputeGradientGetUseFD

TaoTermComputeGradientSetUseFD

TaoTermComputeHessian

TaoTermComputeHessianFD

TaoTermComputeHessianGetUseFD

TaoTermComputeHessianMFFD

TaoTermComputeHessianSetUseFD

TaoTermComputeObjective

TaoTermComputeObjectiveAndGradient

TaoTermCreateHalfL2Squared

TaoTermCreateHessianMFFD

TaoTermCreateHessianMatrices

TaoTermCreateHessianMatricesDefault

TaoTermCreateParametersVec

TaoTermCreateQuadratic

TaoTermCreateSolutionVec

TaoTermDuplicateOption

TaoTermGetCreateHessianMode

TaoTermGetParametersLayout

TaoTermGetParametersMode

TaoTermGetParametersSizes

TaoTermGetParametersVecType

TaoTermGetSolutionLayout

TaoTermGetSolutionSizes

TaoTermGetSolutionVecType

TaoTermIsComputeHessianFDPossible

TaoTermIsCreateHessianMatricesDefined

TaoTermIsGradientDefined

TaoTermIsHessianDefined

TaoTermIsObjectiveAndGradientDefined

TaoTermIsObjectiveDefined

TaoTermObjectiveAndGradientFn

TaoTermParametersMode

TaoTermQuadraticGetMat

TaoTermQuadraticSetMat

TaoTermSetCreateHessianMode

TaoTermSetFromOptions

TaoTermSetParametersLayout

TaoTermSetParametersMode

TaoTermSetParametersSizes

TaoTermSetParametersTemplate

TaoTermSetParametersVecType

TaoTermSetSolutionLayout

TaoTermSetSolutionSizes

TaoTermSetSolutionTemplate

TaoTermSetSolutionVecType

TaoTermShellGetContext

TaoTermShellSetContext

TaoTermShellSetContextDestroy

TaoTermShellSetCreateHessianMatrices

TaoTermShellSetCreateParametersVec

TaoTermShellSetCreateSolutionVec

TaoTermShellSetGradient

TaoTermShellSetHessian

TaoTermShellSetIsComputeHessianFDPossible

TaoTermShellSetObjective

TaoTermShellSetObjectiveAndGradient

TaoTermSumGetLastTermObjectives

TaoTermSumGetNumberTerms

TaoTermSumGetTermHessianMatrices

TaoTermSumGetTermMask

TaoTermSumParametersPack

TaoTermSumParametersUnpack

TaoTermSumSetNumberTerms

TaoTermSumSetTermHessianMatrices

TaoTermSumSetTermMask

VecNestGetTaoTermSumParameters

Optimization Line Search (TaoLineSearch)

---

## Optimization#

**URL:** https://petsc.org/release/manualpages/Optimization/

**Contents:**
- Optimization#

Semi-Lagrangian Solves using the Method of Characteristics

Optimization Solvers (Tao)

---

## Optimization Line Search (TaoLineSearch)#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/

**Contents:**
- Optimization Line Search (TaoLineSearch)#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Single list of manual pages#

The TaoLineSearch class manages the line searches needed by some of the Tao methods. Users guide chapter: TAO: Optimization Solvers.

TaoLineSearchSetFromOptions

TaoLineSearchSetGradientRoutine

TaoLineSearchSetObjectiveAndGradientRoutine

TaoLineSearchSetVariableBounds

TaoLineSearchGetNumberFunctionEvaluations

TaoLineSearchGetStepLength

TaoLineSearchSetInitialStepLength

TaoLineSearchViewFromOptions

TaoLineSearchAppendOptionsPrefix

TaoLineSearchGetOptionsPrefix

TaoLineSearchGetStartingVector

TaoLineSearchGetStepDirection

TaoLineSearchSetObjectiveAndGTSRoutine

TaoLineSearchSetObjectiveRoutine

TaoLineSearchSetOptionsPrefix

TAOLINESEARCHOWARMIJO

TaoLineSearchComputeGradient

TaoLineSearchComputeObjective

TaoLineSearchComputeObjectiveAndGTS

TaoLineSearchComputeObjectiveAndGradient

TaoLineSearchFinalizePackage

TaoLineSearchGetFullStepObjective

TaoLineSearchGetSolution

TaoLineSearchInitializePackage

TaoLineSearchIsUsingTaoRoutines

TaoLineSearchRegister

TaoLineSearchUseTaoRoutines

TAOLINESEARCHOWARMIJO

TaoLineSearchAppendOptionsPrefix

TaoLineSearchComputeGradient

TaoLineSearchComputeObjective

TaoLineSearchComputeObjectiveAndGTS

TaoLineSearchComputeObjectiveAndGradient

TaoLineSearchFinalizePackage

TaoLineSearchGetFullStepObjective

TaoLineSearchGetNumberFunctionEvaluations

TaoLineSearchGetOptionsPrefix

TaoLineSearchGetSolution

TaoLineSearchGetStartingVector

TaoLineSearchGetStepDirection

TaoLineSearchGetStepLength

TaoLineSearchInitializePackage

TaoLineSearchIsUsingTaoRoutines

TaoLineSearchRegister

TaoLineSearchSetFromOptions

TaoLineSearchSetGradientRoutine

TaoLineSearchSetInitialStepLength

TaoLineSearchSetObjectiveAndGTSRoutine

TaoLineSearchSetObjectiveAndGradientRoutine

TaoLineSearchSetObjectiveRoutine

TaoLineSearchSetOptionsPrefix

TaoLineSearchSetVariableBounds

TaoLineSearchUseTaoRoutines

TaoLineSearchViewFromOptions

Optimization Solvers (Tao)

Objective Function Terms (TaoTerm)

**Examples:**

Example 1 (unknown):
```unknown
TaoLineSearch
```

---

## Optimization Solvers (Tao)#

**URL:** https://petsc.org/release/manualpages/Tao/

**Contents:**
- Optimization Solvers (Tao)#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Single list of manual pages#

The Toolkit for Advance Optimization Tao, provides a large suite of optimization solvers for unconstrained and constrained problems. Users guide chapter: TAO: Optimization Solvers.

TaoBRGNSetRegularizerWeight

TaoGetInequalityBounds

TaoGetObjectiveAndGradient

TaoLineSearchConvergedReason

TaoSetInequalityBounds

TaoSetObjectiveAndGradient

TaoSetResidualRoutine

TaoSetVariableBoundsRoutine

TaoADMMGetRegularizerType

TaoADMMSetRegularizerType

TaoGetApplicationContext

TaoGetConstraintTolerances

TaoGetConvergedReason

TaoGetCurrentFunctionEvaluations

TaoGetCurrentTrustRegionRadius

TaoGetEqualityConstraintsRoutine

TaoGetFunctionLowerBound

TaoGetHessianMatrices

TaoGetInequalityConstraintsRoutine

TaoGetInitialTrustRegionRadius

TaoGetIterationNumber

TaoGetJacobianEqualityRoutine

TaoGetJacobianInequalityRoutine

TaoGetLinearSolveIterations

TaoGetMaximumFunctionEvaluations

TaoGetMaximumIterations

TaoGetTotalIterationNumber

TaoMonitorDrawCtxCreate

TaoMonitorDrawCtxDestroy

TaoSetApplicationContext

TaoSetConstraintTolerances

TaoSetConstraintsRoutine

TaoSetConvergedReason

TaoSetConvergenceHistory

TaoSetEqualityConstraintsRoutine

TaoSetFunctionLowerBound

TaoSetInequalityConstraintsRoutine

TaoSetInitialTrustRegionRadius

TaoSetJacobianDesignRoutine

TaoSetJacobianEqualityRoutine

TaoSetJacobianInequalityRoutine

TaoSetJacobianResidualRoutine

TaoSetJacobianRoutine

TaoSetJacobianStateRoutine

TaoSetMaximumFunctionEvaluations

TaoSetMaximumIterations

TaoSetResidualWeights

ADMM_UPDATE_ADAPTIVE_RELAXED

TAO_ADMM_REGULARIZER_SOFT_THRESH

TAO_ADMM_REGULARIZER_USER

TAO_ADMM_UPDATE_ADAPTIVE

TAO_ADMM_UPDATE_BASIC

TaoADMMGetMisfitSubsolver

TaoADMMGetRegularizationSubsolver

TaoADMMGetRegularizerCoefficient

TaoADMMGetSpectralPenalty

TaoADMMRegularizerType

TaoADMMSetConstraintVectorRHS

TaoADMMSetMinimumSpectralPenalty

TaoADMMSetMisfitConstraintJacobian

TaoADMMSetMisfitHessianChangeStatus

TaoADMMSetMisfitHessianRoutine

TaoADMMSetMisfitObjectiveAndGradientRoutine

TaoADMMSetRegHessianChangeStatus

TaoADMMSetRegularizerCoefficient

TaoADMMSetRegularizerConstraintJacobian

TaoADMMSetRegularizerHessianRoutine

TaoADMMSetRegularizerObjectiveAndGradientRoutine

TaoADMMSetSpectralPenalty

TaoALMMGetMultipliers

TaoALMMSetMultipliers

TaoAppendOptionsPrefix

TaoBRGNGetRegularizationType

TaoBRGNRegularizationType

TaoBRGNSetDictionaryMatrix

TaoBRGNSetL1SmoothEpsilon

TaoBRGNSetRegularizationType

TaoBRGNSetRegularizerHessianRoutine

TaoBRGNSetRegularizerObjectiveAndGradientRoutine

TaoComputeDualVariables

TaoDefaultComputeGradient

TaoDefaultComputeHessian

TaoDefaultComputeHessianColor

TaoDefaultComputeHessianMFFD

TaoGetConvergenceHistory

TaoMonitorConstraintNorm

TaoMonitorDefaultShort

TaoMonitorGlobalization

TaoMonitorGradientDraw

TaoMonitorSolutionDraw

TaoSetConvergenceTest

MatCreateSubMatrixFree

TaoAddLineSearchCounts

TaoBRGNGetDampingVector

TaoComputeConstraints

TaoComputeEqualityConstraints

TaoComputeInequalityConstraints

TaoComputeJacobianDesign

TaoComputeJacobianEquality

TaoComputeJacobianInequality

TaoComputeJacobianState

TaoComputeObjectiveAndGradient

TaoComputeResidualJacobian

TaoComputeVariableBounds

TaoDefaultConvergenceTest

TaoEstimateActiveBounds

TaoIsObjectiveAndGradientDefined

TaoIsObjectiveDefined

TaoMonitorSetFromOptions

TaoParametersInitialize

TaoSetIterationNumber

TaoSetTotalIterationNumber

ADMM_UPDATE_ADAPTIVE_RELAXED

MatCreateSubMatrixFree

TAO_ADMM_REGULARIZER_SOFT_THRESH

TAO_ADMM_REGULARIZER_USER

TAO_ADMM_UPDATE_ADAPTIVE

TAO_ADMM_UPDATE_BASIC

TaoADMMGetMisfitSubsolver

TaoADMMGetRegularizationSubsolver

TaoADMMGetRegularizerCoefficient

TaoADMMGetRegularizerType

TaoADMMGetSpectralPenalty

TaoADMMRegularizerType

TaoADMMSetConstraintVectorRHS

TaoADMMSetMinimumSpectralPenalty

TaoADMMSetMisfitConstraintJacobian

TaoADMMSetMisfitHessianChangeStatus

TaoADMMSetMisfitHessianRoutine

TaoADMMSetMisfitObjectiveAndGradientRoutine

TaoADMMSetRegHessianChangeStatus

TaoADMMSetRegularizerCoefficient

TaoADMMSetRegularizerConstraintJacobian

TaoADMMSetRegularizerHessianRoutine

TaoADMMSetRegularizerObjectiveAndGradientRoutine

TaoADMMSetRegularizerType

TaoADMMSetSpectralPenalty

TaoALMMGetMultipliers

TaoALMMSetMultipliers

TaoAddLineSearchCounts

TaoAppendOptionsPrefix

TaoBRGNGetDampingVector

TaoBRGNGetRegularizationType

TaoBRGNRegularizationType

TaoBRGNSetDictionaryMatrix

TaoBRGNSetL1SmoothEpsilon

TaoBRGNSetRegularizationType

TaoBRGNSetRegularizerHessianRoutine

TaoBRGNSetRegularizerObjectiveAndGradientRoutine

TaoBRGNSetRegularizerWeight

TaoComputeConstraints

TaoComputeDualVariables

TaoComputeEqualityConstraints

TaoComputeInequalityConstraints

TaoComputeJacobianDesign

TaoComputeJacobianEquality

TaoComputeJacobianInequality

TaoComputeJacobianState

TaoComputeObjectiveAndGradient

TaoComputeResidualJacobian

TaoComputeVariableBounds

TaoDefaultComputeGradient

TaoDefaultComputeHessian

TaoDefaultComputeHessianColor

TaoDefaultComputeHessianMFFD

TaoDefaultConvergenceTest

TaoEstimateActiveBounds

TaoGetApplicationContext

TaoGetConstraintTolerances

TaoGetConvergedReason

TaoGetConvergenceHistory

TaoGetCurrentFunctionEvaluations

TaoGetCurrentTrustRegionRadius

TaoGetEqualityConstraintsRoutine

TaoGetFunctionLowerBound

TaoGetHessianMatrices

TaoGetInequalityBounds

TaoGetInequalityConstraintsRoutine

TaoGetInitialTrustRegionRadius

TaoGetIterationNumber

TaoGetJacobianEqualityRoutine

TaoGetJacobianInequalityRoutine

TaoGetLinearSolveIterations

TaoGetMaximumFunctionEvaluations

TaoGetMaximumIterations

TaoGetObjectiveAndGradient

TaoGetTotalIterationNumber

TaoIsObjectiveAndGradientDefined

TaoIsObjectiveDefined

TaoLineSearchConvergedReason

TaoMonitorConstraintNorm

TaoMonitorDefaultShort

TaoMonitorDrawCtxCreate

TaoMonitorDrawCtxDestroy

TaoMonitorGlobalization

TaoMonitorGradientDraw

TaoMonitorSetFromOptions

TaoMonitorSolutionDraw

TaoParametersInitialize

TaoSetApplicationContext

TaoSetConstraintTolerances

TaoSetConstraintsRoutine

TaoSetConvergedReason

TaoSetConvergenceHistory

TaoSetConvergenceTest

TaoSetEqualityConstraintsRoutine

TaoSetFunctionLowerBound

TaoSetInequalityBounds

TaoSetInequalityConstraintsRoutine

TaoSetInitialTrustRegionRadius

TaoSetIterationNumber

TaoSetJacobianDesignRoutine

TaoSetJacobianEqualityRoutine

TaoSetJacobianInequalityRoutine

TaoSetJacobianResidualRoutine

TaoSetJacobianRoutine

TaoSetJacobianStateRoutine

TaoSetMaximumFunctionEvaluations

TaoSetMaximumIterations

TaoSetObjectiveAndGradient

TaoSetResidualRoutine

TaoSetResidualWeights

TaoSetTotalIterationNumber

TaoSetVariableBoundsRoutine

Optimization Line Search (TaoLineSearch)

---

## PetscDAAppendOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAAppendOptionsPrefix/

**Contents:**
- PetscDAAppendOptionsPrefix#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Appends to the prefix used for searching for all PetscDA options in the database.

das - the PetscDA context

p - the prefix string to prepend to all PetscDA option requests

PetscDA, PetscDASetFromOptions(), PetscDASetOptionsPrefix(), PetscDAGetOptionsPrefix()

src/ml/da/interface/petscda.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAAppendOptionsPrefix(PetscDA das, const char p[])
```

Example 2 (unknown):
```unknown
PetscDASetFromOptions()
```

Example 3 (unknown):
```unknown
PetscDASetOptionsPrefix()
```

Example 4 (unknown):
```unknown
PetscDAGetOptionsPrefix()
```

---

## PetscDACreate#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDACreate/

**Contents:**
- PetscDACreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Creates a new PetscDA object for data assimilation.

comm - MPI communicator used to create the object

da_out - newly created PetscDA object

PetscDA: Data Assimilation, PetscDADestroy(), PetscDASetType(), PetscDASetUp()

src/ml/da/interface/petscda.c

src/ml/da/tutorials/ex3.c src/ml/da/tutorials/ex4.c src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex1.c

PetscDACreate_Ensemble() in src/ml/da/impls/ensemble/daensemble.c PetscDACreate_ETKF() in src/ml/da/impls/ensemble/etkf/etkfilter.c PetscDACreate_LETKF() in src/ml/da/impls/ensemble/letkf/letkfilter.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDACreate(MPI_Comm comm, PetscDA *da_out)
```

Example 2 (unknown):
```unknown
PetscDADestroy()
```

Example 3 (unknown):
```unknown
PetscDASetType()
```

Example 4 (unknown):
```unknown
PetscDASetUp()
```

---

## PetscDADestroy#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDADestroy/

**Contents:**
- PetscDADestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Destroys a PetscDA object and releases its resources.

da - pointer to the PetscDA object to destroy

PetscDA: Data Assimilation, PetscDACreate()

src/ml/da/interface/petscda.c

src/ml/da/tutorials/ex3.c src/ml/da/tutorials/ex4.c src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex1.c

PetscDADestroy_Ensemble() in src/ml/da/impls/ensemble/daensemble.c PetscDADestroy_ETKF() in src/ml/da/impls/ensemble/etkf/etkfilter.c PetscDADestroy_LETKF() in src/ml/da/impls/ensemble/letkf/letkfilter.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDADestroy(PetscDA *da)
```

Example 2 (unknown):
```unknown
PetscDACreate()
```

---

## PetscDAEnsembleAnalysis#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleAnalysis/

**Contents:**
- PetscDAEnsembleAnalysis#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Executes the analysis (update) step using sparse observation matrix H

da - the PetscDA context

observation - observation vector y in R^P

H - observation operator matrix (P x N), sparse AIJ format

The observation matrix H maps from state space (N dimensions) to observation space (P dimensions): y = H*x + noise

H must be a sparse AIJ matrix

For identity observations (observe entire state), use an identity matrix for H. For partial observations, set appropriate rows and columns to observe specific state components.

PetscDA: Data Assimilation, PetscDA, PETSCDAETKF, PETSCDALETKF, PetscDAEnsembleForecast(), PetscDASetObsErrorVariance()

src/ml/da/impls/ensemble/daensemble.c

src/ml/da/tutorials/ex3.c src/ml/da/tutorials/ex4.c src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex1.c

PetscDAEnsembleAnalysis_ETKF() in src/ml/da/impls/ensemble/etkf/etkfilter.c PetscDAEnsembleAnalysis_LETKF() in src/ml/da/impls/ensemble/letkf/letkfilter.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAEnsembleAnalysis(PetscDA da, Vec observation, Mat H)
```

Example 2 (unknown):
```unknown
PETSCDAETKF
```

Example 3 (unknown):
```unknown
PETSCDALETKF
```

Example 4 (unknown):
```unknown
PetscDAEnsembleForecast()
```

---

## PetscDAEnsembleApplySqrtTInverse#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleApplySqrtTInverse/

**Contents:**
- PetscDAEnsembleApplySqrtTInverse#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Apply T^{-1/2} to a matrix U [Alg 6.4 line 9]

da - the PetscDA context

U - input matrix (usually Identity, but can be general)

Y - output matrix Y = T^{-1/2} * U

This function applies the inverse square root of T = I + S^T * S using the stored factorization.

For CHOLESKY mode: Computes Y = L^{-T} U

For EIGEN mode: Computes Y = V D^{-1/2} V^T U

Both results satisfy Y^T * T * Y = U^T * U, preserving the metric.

PetscDA: Data Assimilation, PetscDA, PETSCDAETKF, PETSCDALETKF, PetscDAEnsembleTFactor(), PetscDAEnsembleApplyTInverse()

src/ml/da/impls/ensemble/daensemble.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAEnsembleApplySqrtTInverse(PetscDA da, Mat U, Mat Y)
```

Example 2 (unknown):
```unknown
PETSCDAETKF
```

Example 3 (unknown):
```unknown
PETSCDALETKF
```

Example 4 (unknown):
```unknown
PetscDAEnsembleTFactor()
```

---

## PetscDAEnsembleApplyTInverse#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleApplyTInverse/

**Contents:**
- PetscDAEnsembleApplyTInverse#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Apply T^{-1} to a vector [Alg 6.4 line 8]

da - the PetscDA context

sdel - input vector S^T-delta

w - output vector w = T^{-1} * sdel

This function applies the inverse of T = I + S^T S using the stored factorization. For CHOLESKY mode, it uses triangular solves. For EIGEN mode, it uses the eigendecomposition (T^{-1} = V D^{-1} V^T).

PetscDA: Data Assimilation, PetscDA, PETSCDAETKF, PETSCDALETKF, PetscDAEnsembleTFactor(), PetscDAEnsembleApplySqrtTInverse()

src/ml/da/impls/ensemble/daensemble.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAEnsembleApplyTInverse(PetscDA da, Vec sdel, Vec w)
```

Example 2 (unknown):
```unknown
PETSCDAETKF
```

Example 3 (unknown):
```unknown
PETSCDALETKF
```

Example 4 (unknown):
```unknown
PetscDAEnsembleTFactor()
```

---

## PetscDAEnsembleComputeAnomalies#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleComputeAnomalies/

**Contents:**
- PetscDAEnsembleComputeAnomalies#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Forms the state-space anomalies matrix for a PetscDA.

da - the PetscDA context

mean_in - optional mean state vector (pass NULL to compute internally)

anomalies_out - location to store the newly created anomalies matrix

If mean is NULL, the function will create a temporary vector and compute the ensemble mean using PetscDAEnsembleComputeMean(). If mean is provided, it will be used directly, which can improve performance when the mean has already been computed.

PetscDA: Data Assimilation, PetscDA, PETSCDAETKF, PETSCDALETKF, PetscDAEnsembleComputeMean()

src/ml/da/impls/ensemble/daensemble.c

src/ml/da/tutorials/ex2.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAEnsembleComputeAnomalies(PetscDA da, Vec mean_in, Mat *anomalies_out)
```

Example 2 (unknown):
```unknown
PetscDAEnsembleComputeMean()
```

Example 3 (unknown):
```unknown
PETSCDAETKF
```

Example 4 (unknown):
```unknown
PETSCDALETKF
```

---

## PetscDAEnsembleComputeMean#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleComputeMean/

**Contents:**
- PetscDAEnsembleComputeMean#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Computes ensemble mean for a PetscDA

da - the PetscDA context

mean - vector that will hold the ensemble mean

PetscDA: Data Assimilation, PetscDA, PETSCDAETKF, PETSCDALETKF, PetscDAEnsembleComputeAnomalies()

src/ml/da/impls/ensemble/daensemble.c

src/ml/da/tutorials/ex3.c src/ml/da/tutorials/ex4.c src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex1.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAEnsembleComputeMean(PetscDA da, Vec mean)
```

Example 2 (unknown):
```unknown
PETSCDAETKF
```

Example 3 (unknown):
```unknown
PETSCDALETKF
```

Example 4 (unknown):
```unknown
PetscDAEnsembleComputeAnomalies()
```

---

## PetscDAEnsembleComputeNormalizedInnovationMatrix#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleComputeNormalizedInnovationMatrix/

**Contents:**
- PetscDAEnsembleComputeNormalizedInnovationMatrix#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Computes S = R^{-1/2}(Z - y_mean * 1’)/sqrt(m-1) [Alg 6.4 line 5]

Z - observation ensemble matrix

y_mean - mean of observations

r_inv_sqrt - R^{-1/2}

S - normalized innovation matrix

PetscDA: Data Assimilation, PetscDA, PETSCDAETKF, PETSCDALETKF, PetscDASetSizes(), PetscDAGetSizes()

src/ml/da/impls/ensemble/daensemble.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAEnsembleComputeNormalizedInnovationMatrix(Mat Z, Vec y_mean, Vec r_inv_sqrt, PetscInt m, PetscScalar scale, Mat S)
```

Example 2 (unknown):
```unknown
PETSCDAETKF
```

Example 3 (unknown):
```unknown
PETSCDALETKF
```

Example 4 (unknown):
```unknown
PetscDASetSizes()
```

---

## PetscDAEnsembleForecast#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleForecast/

**Contents:**
- PetscDAEnsembleForecast#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Advances every ensemble member through the user-supplied forecast model.

da - the PetscDA context

model - routine that evaluates the model map f(input, output; ctx)

ctx - optional context for model

PetscDA: Data Assimilation, PetscDA, PETSCDAETKF, PETSCDALETKF, PetscDAEnsembleAnalysis()

src/ml/da/impls/ensemble/daensemble.c

src/ml/da/tutorials/ex3.c src/ml/da/tutorials/ex4.c src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex1.c

PetscDAEnsembleForecast_Ensemble(PetscDA da, PetscErrorCode (*model)() in src/ml/da/impls/ensemble/etkf/etkfilter.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAEnsembleForecast(PetscDA da, PetscErrorCode (*model)(Vec, Vec, PetscCtx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
f(input, output; ctx)
```

Example 3 (unknown):
```unknown
PETSCDAETKF
```

Example 4 (unknown):
```unknown
PETSCDALETKF
```

---

## PetscDAEnsembleGetInflation#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleGetInflation/

**Contents:**
- PetscDAEnsembleGetInflation#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the inflation factor for the data assimilation method.

da - the PetscDA context

inflation - the inflation factor

PetscDA: Data Assimilation, PetscDA, PETSCDAETKF, PETSCDALETKF, PetscDAEnsembleSetInflation()

src/ml/da/impls/ensemble/daensemble.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAEnsembleGetInflation(PetscDA da, PetscReal *inflation)
```

Example 2 (unknown):
```unknown
PETSCDAETKF
```

Example 3 (unknown):
```unknown
PETSCDALETKF
```

Example 4 (unknown):
```unknown
PetscDAEnsembleSetInflation()
```

---

## PetscDAEnsembleGetMember#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleGetMember/

**Contents:**
- PetscDAEnsembleGetMember#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns a read-only view of an ensemble member stored in the PetscDA.

da - the PetscDA context

member_idx - index of the requested member (0 <= idx < ensemble_size)

member - read-only vector view; call PetscDAEnsembleRestoreMember() when done

PetscDA: Data Assimilation, PetscDA, PETSCDAETKF, PETSCDALETKF, PetscDAEnsembleRestoreMember(), PetscDAEnsembleSetMember()

src/ml/da/impls/ensemble/daensemble.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAEnsembleGetMember(PetscDA da, PetscInt member_idx, Vec *member)
```

Example 2 (unknown):
```unknown
PetscDAEnsembleRestoreMember()
```

Example 3 (unknown):
```unknown
PETSCDAETKF
```

Example 4 (unknown):
```unknown
PETSCDALETKF
```

---

## PetscDAEnsembleGetSize#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleGetSize/

**Contents:**
- PetscDAEnsembleGetSize#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#

Retrieves the dimension of the ensemble in a PetscDA.

da - the PetscDA context

ensemble_size - number of ensemble members

PetscDA: Data Assimilation, PetscDA, PETSCDAETKF, PETSCDALETKF, PetscDASetSizes(), PetscDAGetSizes()

src/ml/da/impls/ensemble/daensemble.c

src/ml/da/tutorials/ex3.c src/ml/da/tutorials/ex4.c src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex1.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAEnsembleGetSize(PetscDA da, PetscInt *ensemble_size)
```

Example 2 (unknown):
```unknown
PETSCDAETKF
```

Example 3 (unknown):
```unknown
PETSCDALETKF
```

Example 4 (unknown):
```unknown
PetscDASetSizes()
```

---

## PetscDAEnsembleGetSqrtType#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleGetSqrtType/

**Contents:**
- PetscDAEnsembleGetSqrtType#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Retrieves the current square-root implementation configured for analysis.

da - the PetscDA object

type - on output, the configured PetscDASqrtType

PetscDA: Data Assimilation, PetscDA, PETSCDAETKF, PETSCDALETKF, PetscDAEnsembleSetSqrtType()

src/ml/da/impls/ensemble/daensemble.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAEnsembleGetSqrtType(PetscDA da, PetscDASqrtType *type)
```

Example 2 (unknown):
```unknown
PetscDASqrtType
```

Example 3 (unknown):
```unknown
PETSCDAETKF
```

Example 4 (unknown):
```unknown
PETSCDALETKF
```

---

## PetscDAEnsembleInitialize#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleInitialize/

**Contents:**
- PetscDAEnsembleInitialize#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Initialize ensemble members with Gaussian perturbations

x0 - Background state

obs_error_std - Standard deviation for perturbations

rng - Random number generator

Each ensemble member is initialized as x0 + Gaussian(0, obs_error_std)

PetscDA: Data Assimilation, PETSCDAETKF, PETSCDALETKF, PetscDA

src/ml/da/impls/ensemble/daensemble.c

src/ml/da/tutorials/ex3.c src/ml/da/tutorials/ex4.c src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex1.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAEnsembleInitialize(PetscDA da, Vec x0, PetscReal obs_error_std, PetscRandom rng)
```

Example 2 (unknown):
```unknown
PETSCDAETKF
```

Example 3 (unknown):
```unknown
PETSCDALETKF
```

---

## PetscDAEnsembleRestoreMember#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleRestoreMember/

**Contents:**
- PetscDAEnsembleRestoreMember#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Returns a column view obtained with PetscDAEnsembleGetMember().

da - the PetscDA context

member_idx - index that was previously requested

member - location that holds the view to restore

PetscDA: Data Assimilation, PetscDA, PETSCDAETKF, PETSCDALETKF, PetscDAEnsembleGetMember()

src/ml/da/impls/ensemble/daensemble.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDAEnsembleGetMember()
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscDAEnsembleRestoreMember(PetscDA da, PetscInt member_idx, Vec *member)
```

Example 3 (unknown):
```unknown
PETSCDAETKF
```

Example 4 (unknown):
```unknown
PETSCDALETKF
```

---

## PetscDAEnsembleSetInflation#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleSetInflation/

**Contents:**
- PetscDAEnsembleSetInflation#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the inflation factor for the data assimilation method.

da - the PetscDA context

inflation - the inflation factor (must be >= 1.0)

PetscDA: Data Assimilation, PetscDA, PETSCDAETKF, PETSCDALETKF, PetscDAEnsembleGetInflation()

src/ml/da/impls/ensemble/daensemble.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAEnsembleSetInflation(PetscDA da, PetscReal inflation)
```

Example 2 (unknown):
```unknown
PETSCDAETKF
```

Example 3 (unknown):
```unknown
PETSCDALETKF
```

Example 4 (unknown):
```unknown
PetscDAEnsembleGetInflation()
```

---

## PetscDAEnsembleSetMember#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleSetMember/

**Contents:**
- PetscDAEnsembleSetMember#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Overwrites an ensemble member with user-provided state data.

da - the PetscDA context

member_idx - index of the entry to modify

member - vector containing the new state values

PetscDA: Data Assimilation, PetscDA, PETSCDAETKF, PETSCDALETKF, PetscDAEnsembleGetMember()

src/ml/da/impls/ensemble/daensemble.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAEnsembleSetMember(PetscDA da, PetscInt member_idx, Vec member)
```

Example 2 (unknown):
```unknown
PETSCDAETKF
```

Example 3 (unknown):
```unknown
PETSCDALETKF
```

Example 4 (unknown):
```unknown
PetscDAEnsembleGetMember()
```

---

## PetscDAEnsembleSetSize#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleSetSize/

**Contents:**
- PetscDAEnsembleSetSize#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the ensemble dimensions used by a PetscDA.

da - the PetscDA context

ensemble_size - number of ensemble members

-petscda_ensemble_size - number of ensemble members

The size must be greater than or equal to two. See the scale factor in PetscDAEnsembleInitialize() and PetscDALETKFLocalAnalysis()

PetscDA: Data Assimilation, PetscDA, PETSCDAETKF, PETSCDALETKF, PetscDAGetSizes(), PetscDASetSizes(), PetscDASetUp()

src/ml/da/impls/ensemble/daensemble.c

src/ml/da/tutorials/ex3.c src/ml/da/tutorials/ex4.c src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex1.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAEnsembleSetSize(PetscDA da, PetscInt ensemble_size)
```

Example 2 (unknown):
```unknown
PetscDAEnsembleInitialize()
```

Example 3 (unknown):
```unknown
PetscDALETKFLocalAnalysis()
```

Example 4 (unknown):
```unknown
PETSCDAETKF
```

---

## PetscDAEnsembleSetSqrtType#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleSetSqrtType/

**Contents:**
- PetscDAEnsembleSetSqrtType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Selects the reduced-space square-root algorithm used during analysis.

da - the PetscDA object

type - either PETSCDA_SQRT_CHOLESKY or PETSCDA_SQRT_EIGEN

-petscda_ensemble_sqrt_type - set the PetscDASqrtType

PetscDA: Data Assimilation, PetscDA, PETSCDAETKF, PETSCDALETKF, PetscDASqrtType, PetscDAEnsembleGetSqrtType()

src/ml/da/impls/ensemble/daensemble.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAEnsembleSetSqrtType(PetscDA da, PetscDASqrtType type)
```

Example 2 (unknown):
```unknown
PETSCDA_SQRT_CHOLESKY
```

Example 3 (unknown):
```unknown
PETSCDA_SQRT_EIGEN
```

Example 4 (unknown):
```unknown
PetscDASqrtType
```

---

## PetscDAEnsembleTFactor#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAEnsembleTFactor/

**Contents:**
- PetscDAEnsembleTFactor#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Compute and store factorization of T matrix

da - the PetscDA context

S - normalized innovation matrix (obs_size x m)

This function computes \(T = I + S^T * S\) and stores its factorization based on the selected PetscDASqrtType.

For CHOLESKY mode: computes the lower triangular Cholesky factor \(L\) such that \(T = L * L^T\).

For EIGEN mode: computes eigenvectors \(V\) and eigenvalues \(D\) such that \(T = V * D * V^T\).

The implementation uses matrix reuse (MAT_REUSE_MATRIX) to minimize memory allocation overhead when the ensemble size remains constant across analysis cycles.

PetscDA: Data Assimilation, PetscDA, PETSCDAETKF, PETSCDALETKF, PetscDAEnsembleApplyTInverse(), PetscDAEnsembleApplySqrtTInverse()

src/ml/da/impls/ensemble/daensemble.c

PetscDAEnsembleTFactor_Cholesky() in src/ml/da/impls/ensemble/daensemble.c PetscDAEnsembleTFactor_Eigen() in src/ml/da/impls/ensemble/daensemble.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAEnsembleTFactor(PetscDA da, Mat S)
```

Example 2 (unknown):
```unknown
PetscDASqrtType
```

Example 3 (unknown):
```unknown
MAT_REUSE_MATRIX
```

Example 4 (unknown):
```unknown
PETSCDAETKF
```

---

## PETSCDAETKF#

**URL:** https://petsc.org/release/manualpages/PetscDA/PETSCDAETKF/

**Contents:**
- PETSCDAETKF#
- Options Database Keys#
- Note#
- References#
- See Also#
- Level#
- Location#
- Examples#

Ensemble transform Kalman filter data assimilation using a deterministic square-root update that avoids stochastic perturbations.

-petscda_type etkf - set the PetscDAType to PETSCDAETKF

-petscda_ensemble_size - number of ensemble members

-petscda_ensemble_sqrt_type <cholesky, eigen> - the square root of the matrix to use

The ETKF algorithm is based on Algorithm 6.4 in [ABN16]

M. Asch, M. Bocquet, and M. Nodet. Data Assimilation: Methods, Algorithms, and Applications. SIAM, 2016. doi:10.1137/1.9781611974546.

PetscDA: Data Assimilation, PetscDA, PetscDACreate(), PETSCDALETKF, PetscDAEnsembleSetSize(), PetscDASetSizes(), PetscDAEnsembleSetSqrtType(), PetscDAEnsembleSetInflation(), PetscDAType, PetscDAEnsembleComputeMean(), PetscDAEnsembleComputeAnomalies(), PetscDAEnsembleAnalysis(), PetscDAEnsembleForecast()

src/ml/da/impls/ensemble/etkf/etkfilter.c

src/ml/da/tutorials/ex1.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDAType
```

Example 2 (unknown):
```unknown
PETSCDAETKF
```

Example 3 (unknown):
```unknown
PetscDACreate()
```

Example 4 (unknown):
```unknown
PETSCDALETKF
```

---

## PetscDAFinalizePackage#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAFinalizePackage/

**Contents:**
- PetscDAFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function finalizes everything in the PetscDA package. It is called from PetscFinalize().

PetscDAInitializePackage(), PetscInitialize()

src/ml/da/interface/petscda.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscDAFinalizePackage(void)
```

Example 3 (unknown):
```unknown
PetscDAInitializePackage()
```

Example 4 (unknown):
```unknown
PetscInitialize()
```

---

## PetscDAGetNDOF#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAGetNDOF/

**Contents:**
- PetscDAGetNDOF#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the number of degrees of freedom per grid point

da - the PetscDA context

ndof - number of degrees of freedom per grid point

PetscDA, PetscDASetNDOF()

src/ml/da/interface/petscda.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAGetNDOF(PetscDA da, PetscInt *ndof)
```

Example 2 (unknown):
```unknown
PetscDASetNDOF()
```

---

## PetscDAGetObsErrorVariance#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAGetObsErrorVariance/

**Contents:**
- PetscDAGetObsErrorVariance#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns a borrowed reference to the observation-error variance vector.

da - the PetscDA context

obs_error_var - pointer to the variance vector managed by the PetscDA

PetscDA: Data Assimilation, PetscDASetObsErrorVariance()

src/ml/da/interface/petscda.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAGetObsErrorVariance(PetscDA da, Vec *obs_error_var)
```

Example 2 (unknown):
```unknown
PetscDASetObsErrorVariance()
```

---

## PetscDAGetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAGetOptionsPrefix/

**Contents:**
- PetscDAGetOptionsPrefix#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the prefix used for searching for all PetscDA options in the database

das - the PetscDA context

p - pointer to the prefix string used

PetscDA, PetscDASetFromOptions(), PetscDASetOptionsPrefix(), PetscDAAppendOptionsPrefix()

src/ml/da/interface/petscda.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAGetOptionsPrefix(PetscDA das, const char *p[])
```

Example 2 (unknown):
```unknown
PetscDASetFromOptions()
```

Example 3 (unknown):
```unknown
PetscDASetOptionsPrefix()
```

Example 4 (unknown):
```unknown
PetscDAAppendOptionsPrefix()
```

---

## PetscDAGetSizes#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAGetSizes/

**Contents:**
- PetscDAGetSizes#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Retrieves the state size and observation size from a PetscDA.

da - the PetscDA context

state_size - number of state components (may be NULL)

obs_size - number of observation components (may be NULL)

PetscDA: Data Assimilation, PetscDASetSizes()

src/ml/da/interface/petscda.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAGetSizes(PetscDA da, PetscInt *state_size, PetscInt *obs_size)
```

Example 2 (unknown):
```unknown
PetscDASetSizes()
```

---

## PetscDAGetType#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAGetType/

**Contents:**
- PetscDAGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the name of the implementation currently associated with a PetscDA.

da - the PetscDA context

type - pointer that will receive the type name (may be NULL)

PetscDA: Data Assimilation, PetscDASetType()

src/ml/da/interface/petscda.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAGetType(PetscDA da, PetscDAType *type)
```

Example 2 (unknown):
```unknown
PetscDASetType()
```

---

## PetscDAInitializePackage#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAInitializePackage/

**Contents:**
- PetscDAInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function initializes everything in the PetscDA package. called on the first call to PetscDACreate() when using static or shared libraries.

PetscDAFinalizePackage(), PetscInitialize()

src/ml/da/interface/petscda.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDACreate()
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscDAInitializePackage(void)
```

Example 3 (unknown):
```unknown
PetscDAFinalizePackage()
```

Example 4 (unknown):
```unknown
PetscInitialize()
```

---

## PetscDALETKFGetLocalizationMatrix#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDALETKFGetLocalizationMatrix/

**Contents:**
- PetscDALETKFGetLocalizationMatrix#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Compute localization weight matrix for LETKF [move to ml/da/interface]

n_obs_vertex - Number of observations to localize to per vertex

n_dof - Number of degrees of freedom

Vecxyz - Array of vectors containing the vertex coordinates

bd - Array of boundary extents per dimension (used for periodicity)

H - Observation operator matrix

Q - Localization weight matrix (sparse, AIJ format)

The output matrix Q has dimensions (n_vert_global x n_obs_global) where n_vert_global is the number of vertices in the DMPlex. Each row contains exactly n_obs_vertex non-zero entries corresponding to the nearest observations, weighted by the Gaspari-Cohn fifth-order piecewise rational function.

The observation locations are computed as H * V where V is the vector of vertex coordinates. The localization weights ensure smooth tapering of observation influence with distance.

Kokkos is required for this routine.

PetscDA: Data Assimilation, PetscDALETKFSetLocalization()

src/ml/da/impls/ensemble/letkf/kokkos/dalocalizationletkf.kokkos.cxx

src/ml/da/tutorials/ex3.c src/ml/da/tutorials/ex4.c src/ml/da/tutorials/ex2.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDALETKFGetLocalizationMatrix(const PetscInt n_obs_vertex, const PetscInt n_dof, Vec Vecxyz[3], PetscReal bd[3], Mat H, Mat *Q)
```

Example 2 (unknown):
```unknown
PetscDALETKFSetLocalization()
```

---

## PetscDALETKFGetObsPerVertex#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDALETKFGetObsPerVertex/

**Contents:**
- PetscDALETKFGetObsPerVertex#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Gets the number of local observations per vertex for the LETKF algorithm.

da - the PetscDA context

n_obs_vertex - number of observations per vertex

PetscDA: Data Assimilation, PETSCDALETKF, PetscDA, PetscDALETKFSetObsPerVertex()

src/ml/da/impls/ensemble/letkf/letkfilter.c

src/ml/da/tutorials/ex2.c

PetscDALETKFGetObsPerVertex_LETKF() in src/ml/da/impls/ensemble/letkf/letkfilter.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDALETKFGetObsPerVertex(PetscDA da, PetscInt *n_obs_vertex)
```

Example 2 (unknown):
```unknown
PETSCDALETKF
```

Example 3 (unknown):
```unknown
PetscDALETKFSetObsPerVertex()
```

---

## PetscDALETKFSetLocalization#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDALETKFSetLocalization/

**Contents:**
- PetscDALETKFSetLocalization#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets the localization matrix for the LETKF algorithm.

da - the PetscDA context

Q - the localization matrix (N x P)

H - the observation operator matrix (P x N)

PetscDA: Data Assimilation, PETSCDALETKF, PetscDA

src/ml/da/impls/ensemble/letkf/letkfilter.c

src/ml/da/tutorials/ex3.c src/ml/da/tutorials/ex4.c src/ml/da/tutorials/ex2.c

PetscDALETKFSetLocalization_LETKF() in src/ml/da/impls/ensemble/letkf/letkfilter.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDALETKFSetLocalization(PetscDA da, Mat Q, Mat H)
```

Example 2 (unknown):
```unknown
PETSCDALETKF
```

---

## PetscDALETKFSetObsPerVertex#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDALETKFSetObsPerVertex/

**Contents:**
- PetscDALETKFSetObsPerVertex#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets the number of local observations per vertex for the LETKF algorithm.

da - the PetscDA context

n_obs_vertex - number of observations per vertex

PetscDA: Data Assimilation, PETSCDALETKF, PetscDA, PetscDALETKFSetLocalization()

src/ml/da/impls/ensemble/letkf/letkfilter.c

src/ml/da/tutorials/ex3.c src/ml/da/tutorials/ex4.c src/ml/da/tutorials/ex2.c

PetscDALETKFSetObsPerVertex_LETKF() in src/ml/da/impls/ensemble/letkf/letkfilter.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDALETKFSetObsPerVertex(PetscDA da, PetscInt n_obs_vertex)
```

Example 2 (unknown):
```unknown
PETSCDALETKF
```

Example 3 (unknown):
```unknown
PetscDALETKFSetLocalization()
```

---

## PETSCDALETKF#

**URL:** https://petsc.org/release/manualpages/PetscDA/PETSCDALETKF/

**Contents:**
- PETSCDALETKF#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#

The Local ETKF performs the analysis update locally around each grid point, enabling scalable assimilation on large domains by avoiding the global ensemble covariance matrix.

-petscda_type letkf - set the PetscDAType to PETSCDALETKF

-petscda_ensemble_size - number of ensemble members

-petscda_ensemble_sqrt_type <cholesky, eigen> - the square root of the matrix to use

-petscda_letkf_batch_size <batch_size> - set the batch size for GPU processing

-petscda_letkf_obs_per_vertex <n_obs_vertex> - number of observations per vertex

PetscDA: Data Assimilation, PetscDA, PetscDACreate(), PETSCDAETKF, PetscDALETKFSetObsPerVertex(), PetscDALETKFGetObsPerVertex(), PetscDALETKFSetLocalization(), PetscDAEnsembleSetSize(), PetscDASetSizes(), PetscDAEnsembleSetSqrtType(), PetscDAEnsembleSetInflation(), PetscDAEnsembleComputeMean(), PetscDAEnsembleComputeAnomalies(), PetscDAEnsembleAnalysis(), PetscDAEnsembleForecast()

src/ml/da/impls/ensemble/letkf/letkfilter.c

src/ml/da/tutorials/ex3.c src/ml/da/tutorials/ex4.c src/ml/da/tutorials/ex2.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscDAType
```

Example 2 (unknown):
```unknown
PETSCDALETKF
```

Example 3 (unknown):
```unknown
PetscDACreate()
```

Example 4 (unknown):
```unknown
PETSCDAETKF
```

---

## PetscDARegisterAll#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDARegisterAll/

**Contents:**
- PetscDARegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all data assimilation backends that were compiled in.

PetscDA: Data Assimilation, PetscDARegister()

src/ml/da/interface/petscda.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDARegisterAll(void)
```

Example 2 (unknown):
```unknown
PetscDARegister()
```

---

## PetscDARegister#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDARegister/

**Contents:**
- PetscDARegister#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Registers a constructor for a PetscDA implementation with the dispatcher.

sname - name associated with the implementation

function - routine that creates the implementation and installs method table

PetscDA: Data Assimilation, PetscDARegisterAll(), PetscDASetType()

src/ml/da/interface/petscda.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDARegister(const char sname[], PetscErrorCode (*function)(PetscDA))
```

Example 2 (unknown):
```unknown
PetscDARegisterAll()
```

Example 3 (unknown):
```unknown
PetscDASetType()
```

---

## PetscDASetFromOptions#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDASetFromOptions/

**Contents:**
- PetscDASetFromOptions#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Configures a PetscDA object from the options database.

da - the PetscDA context to set up

PetscDA: Data Assimilation, PetscDASetType(), PetscObjectOptionsBegin()

src/ml/da/interface/petscda.c

src/ml/da/tutorials/ex3.c src/ml/da/tutorials/ex4.c src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex1.c

PetscDASetFromOptions_Ensemble() in src/ml/da/impls/ensemble/daensemble.c PetscDASetFromOptions_LETKF() in src/ml/da/impls/ensemble/letkf/letkfilter.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDASetFromOptions(PetscDA da)
```

Example 2 (unknown):
```unknown
PetscDASetType()
```

Example 3 (unknown):
```unknown
PetscObjectOptionsBegin()
```

---

## PetscDASetLocalSizes#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDASetLocalSizes/

**Contents:**
- PetscDASetLocalSizes#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the local state and observation dimensions used by a PetscDA.

da - the PetscDA context

local_state_size - number of local state components (or PETSC_DECIDE)

local_obs_size - number of local observation components (or PETSC_DECIDE)

PetscDA: Data Assimilation, PetscDASetSizes(), PetscDASetUp()

src/ml/da/interface/petscda.c

src/ml/da/tutorials/ex3.c src/ml/da/tutorials/ex4.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDASetLocalSizes(PetscDA da, PetscInt local_state_size, PetscInt local_obs_size)
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
PetscDASetSizes()
```

---

## PetscDASetNDOF#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDASetNDOF/

**Contents:**
- PetscDASetNDOF#
- Synopsis#
- Input Parameters#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Set the number of degrees of freedom per grid point

da - the PetscDA context

ndof - number of degrees of freedom per grid point (e.g., 2 for shallow water with h and hu)

This must be called before PetscDASetUp(). The default is 1 (scalar field).

It is a limitation that each grid point needs the same number of degrees of freedom.

PetscDA, PetscDAGetNDOF(), PetscDASetUp(), PetscDASetSizes()

src/ml/da/interface/petscda.c

src/ml/da/tutorials/ex3.c src/ml/da/tutorials/ex4.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDASetNDOF(PetscDA da, PetscInt ndof)
```

Example 2 (unknown):
```unknown
PetscDASetUp()
```

Example 3 (unknown):
```unknown
PetscDAGetNDOF()
```

Example 4 (unknown):
```unknown
PetscDASetUp()
```

---

## PetscDASetObsErrorVariance#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDASetObsErrorVariance/

**Contents:**
- PetscDASetObsErrorVariance#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the observation-error variances associated with a PetscDA.

da - the PetscDA context

obs_error_var - vector containing observation error variances (assumes R is a diagonal matrix)

This function creates or updates both the observation error variance vector and the observation error covariance matrix R. The matrix R is constructed as a diagonal matrix with the variances on the diagonal.

PetscDA: Data Assimilation, PetscDAGetObsErrorVariance()

src/ml/da/interface/petscda.c

src/ml/da/tutorials/ex3.c src/ml/da/tutorials/ex4.c src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex1.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDASetObsErrorVariance(PetscDA da, Vec obs_error_var)
```

Example 2 (unknown):
```unknown
PetscDAGetObsErrorVariance()
```

---

## PetscDASetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDASetOptionsPrefix/

**Contents:**
- PetscDASetOptionsPrefix#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the prefix used for searching for all PetscDA options in the database.

das - the PetscDA context

p - the prefix string to prepend to all PetscDA option requests

PetscDA, PetscDASetFromOptions(), PetscDAAppendOptionsPrefix(), PetscDAGetOptionsPrefix()

src/ml/da/interface/petscda.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDASetOptionsPrefix(PetscDA das, const char p[])
```

Example 2 (unknown):
```unknown
PetscDASetFromOptions()
```

Example 3 (unknown):
```unknown
PetscDAAppendOptionsPrefix()
```

Example 4 (unknown):
```unknown
PetscDAGetOptionsPrefix()
```

---

## PetscDASetSizes#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDASetSizes/

**Contents:**
- PetscDASetSizes#
- Synopsis#
- Input Parameters#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the state and observation sizes for a PetscDA

da - the PetscDA context

state_size - number of state components

obs_size - number of observation components

It is not clear this is a good API, shouldn’t one provide template vectors for these?

PetscDA: Data Assimilation, PetscDAGetSizes(), PetscDASetUp(), PetscDAEnsembleSetSize()

src/ml/da/interface/petscda.c

src/ml/da/tutorials/ex3.c src/ml/da/tutorials/ex4.c src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex1.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDASetSizes(PetscDA da, PetscInt state_size, PetscInt obs_size)
```

Example 2 (unknown):
```unknown
PetscDAGetSizes()
```

Example 3 (unknown):
```unknown
PetscDASetUp()
```

Example 4 (unknown):
```unknown
PetscDAEnsembleSetSize()
```

---

## PetscDASetType#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDASetType/

**Contents:**
- PetscDASetType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the data assimilation implementation used by a PetscDA object.

da - the PetscDA context

type - name of the implementation (for example PETSCDAETKF)

PetscDA: Data Assimilation, PetscDAGetType(), PetscDARegister()

src/ml/da/interface/petscda.c

src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex1.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDASetType(PetscDA da, PetscDAType type)
```

Example 2 (unknown):
```unknown
PETSCDAETKF
```

Example 3 (unknown):
```unknown
PetscDAGetType()
```

Example 4 (unknown):
```unknown
PetscDARegister()
```

---

## PetscDASetUp#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDASetUp/

**Contents:**
- PetscDASetUp#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Allocates internal data structures for a PetscDA based on the previously provided sizes.

da - the PetscDA context to assemble

PetscDA: Data Assimilation, PetscDASetSizes(), PetscDASetType()

src/ml/da/interface/petscda.c

src/ml/da/tutorials/ex3.c src/ml/da/tutorials/ex4.c src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex1.c

PetscDASetUp_Ensemble() in src/ml/da/impls/ensemble/daensemble.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDASetUp(PetscDA da)
```

Example 2 (unknown):
```unknown
PetscDASetSizes()
```

Example 3 (unknown):
```unknown
PetscDASetType()
```

---

## PetscDASqrtType#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDASqrtType/

**Contents:**
- PetscDASqrtType#
- Synopsis#
- Values#
- Option Database Key#
- See Also#
- Level#
- Location#

Type of square root of matrices to use the data assimilation algorithms

PETSCDA_SQRT_CHOLESKY - Use the Cholesky factorization

PETSCDA_SQRT_EIGEN - Use the eigenvalue decomposition

-petscda_ensemble_sqrt_type <cholesky, eigen> - select the square root type at run time

PetscDA: Data Assimilation, PetscDA, PetscDAEnsembleSetSqrtType(), PetscDAEnsembleGetSqrtType()

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  PETSCDA_SQRT_CHOLESKY = 0,
  PETSCDA_SQRT_EIGEN    = 1
} PetscDASqrtType;
```

Example 2 (unknown):
```unknown
PETSCDA_SQRT_CHOLESKY
```

Example 3 (unknown):
```unknown
PETSCDA_SQRT_EIGEN
```

Example 4 (unknown):
```unknown
PetscDAEnsembleSetSqrtType()
```

---

## PetscDAType#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAType/

**Contents:**
- PetscDAType#
- Synopsis#
- See Also#
- Level#
- Location#

String with the name of a PETSc data assimilation method

PetscDA: Data Assimilation, PetscDA, PetscDASetType(), PETSCDAETKF, PETSCDALETKF

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef const char *PetscDAType;
#define PETSCDAETKF  "etkf"
#define PETSCDALETKF "letkf"
```

Example 2 (unknown):
```unknown
PetscDASetType()
```

Example 3 (unknown):
```unknown
PETSCDAETKF
```

Example 4 (unknown):
```unknown
PETSCDALETKF
```

---

## PetscDAViewFromOptions#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAViewFromOptions/

**Contents:**
- PetscDAViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

Processes command-line options to determine if a PetscDA should be viewed.

da - the PetscDA context

obj - optional object that provides the prefix for options

name - option name to check

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

PetscDA: Data Assimilation, PetscDAView(), PetscObjectViewFromOptions()

src/ml/da/interface/petscda.c

src/ml/da/tutorials/ex3.c src/ml/da/tutorials/ex4.c src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex1.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAViewFromOptions(PetscDA da, PetscObject obj, const char name[])
```

Example 2 (unknown):
```unknown
PetscObjectViewFromOptions()
```

Example 3 (unknown):
```unknown
PetscDAView()
```

Example 4 (unknown):
```unknown
PetscObjectViewFromOptions()
```

---

## PetscDAView#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDAView/

**Contents:**
- PetscDAView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Views a PetscDA and its implementation-specific data structure.

da - the PetscDA context

viewer - the PetscViewer to use (or NULL for standard output)

PetscDA: Data Assimilation, PetscDAViewFromOptions()

src/ml/da/interface/petscda.c

PetscDAView_Ensemble() in src/ml/da/impls/ensemble/daensemble.c PetscDAView_LETKF() in src/ml/da/impls/ensemble/letkf/letkfilter.c

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscDAView(PetscDA da, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
PetscDAViewFromOptions()
```

---

## PetscDA#

**URL:** https://petsc.org/release/manualpages/PetscDA/PetscDA/

**Contents:**
- PetscDA#
- Synopsis#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Abstract PETSc object that manages data assimilation

This is new code, please independently verify all results you obtain using it.

Some planned work for PetscDA is available as GitLab Issue #1882

Currently we supply two ensemble-based assimilators: PETSCDAETKF and PETSCDALETKF

PetscDA: Data Assimilation, PetscDAType, PETSCDAETKF, PETSCDALETKF, PetscDASqrtType, PetscDACreate(), PetscDASetType(), PetscDASetSizes(), PetscDAEnsembleSetSize(), PetscDAEnsembleAnalysis(), PetscDAEnsembleForecast(), PetscDADestroy(), PetscDAView()

src/ml/da/tutorials/ex3.c src/ml/da/tutorials/ex4.c src/ml/da/tutorials/ex2.c src/ml/da/tutorials/ex1.c

_p_PetscDA in include/petsc/private/daimpl.h PetscDA_Ensemble in include/petsc/private/daimpl.h PetscDA_ETKF in src/ml/da/impls/ensemble/etkf/etkfilter.c PetscDA_LETKF in src/ml/da/impls/ensemble/letkf/letkf.h

Index of all PetscDA routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_PetscDA *PetscDA;
```

Example 2 (unknown):
```unknown
PETSCDAETKF
```

Example 3 (unknown):
```unknown
PETSCDALETKF
```

Example 4 (unknown):
```unknown
PetscDAType
```

---

## PetscRegressorAppendOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorAppendOptionsPrefix/

**Contents:**
- PetscRegressorAppendOptionsPrefix#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Appends to the prefix used for searching for all PetscRegressor options in the database.

regressor - the PetscRegressor solver context

p - the prefix string to prepend to all PetscRegressor option requests

A hyphen (-) must NOT be given at the beginning of the prefix name. The first character of all runtime options is automatically the hyphen.

PetscRegressor: Regression Solvers, PetscRegressor, PetscRegressorSetFromOptions(), PetscRegressorSetOptionsPrefix(), PetscRegressorGetOptionsPrefix()

src/ml/regressor/interface/regressor.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscRegressorAppendOptionsPrefix(PetscRegressor regressor, const char p[])
```

Example 2 (unknown):
```unknown
PetscRegressor
```

Example 3 (unknown):
```unknown
PetscRegressor
```

Example 4 (unknown):
```unknown
PetscRegressor
```

---

## PetscRegressorCreate#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorCreate/

**Contents:**
- PetscRegressorCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Creates a PetscRegressor object.

comm - the MPI communicator that will share the PetscRegressor object

newregressor - the new PetscRegressor object

PetscRegressorFit(), PetscRegressorPredict(), PetscRegressor

src/ml/regressor/interface/regressor.c

PetscRegressorCreate_Linear() in src/ml/regressor/impls/linear/linear.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscRegressor
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscRegressorCreate(MPI_Comm comm, PetscRegressor *newregressor)
```

Example 3 (unknown):
```unknown
PetscRegressor
```

Example 4 (unknown):
```unknown
PetscRegressor
```

---

## PetscRegressorDestroy#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorDestroy/

**Contents:**
- PetscRegressorDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Destroys the regressor context that was created with PetscRegressorCreate().

regressor - the PetscRegressor context

PetscRegressorCreate(), PetscRegressorSetUp(), PetscRegressorReset(), PetscRegressor

src/ml/regressor/interface/regressor.c

PetscRegressorDestroy_Linear() in src/ml/regressor/impls/linear/linear.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscRegressorCreate()
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscRegressorDestroy(PetscRegressor *regressor)
```

Example 3 (unknown):
```unknown
PetscRegressor
```

Example 4 (unknown):
```unknown
PetscRegressorCreate()
```

---

## PetscRegressorFinalizePackage#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorFinalizePackage/

**Contents:**
- PetscRegressorFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

Finalize PetscRegressor package; it is called from PetscFinalize()

PetscRegressorInitializePackage()

src/ml/regressor/interface/dlregisregressor.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscRegressor
```

Example 2 (unknown):
```unknown
PetscFinalize()
```

Example 3 (unknown):
```unknown
PetscErrorCode PetscRegressorFinalizePackage(void)
```

Example 4 (unknown):
```unknown
PetscRegressorInitializePackage()
```

---

## PetscRegressorFit#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorFit/

**Contents:**
- PetscRegressorFit#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Fit, or train, a regressor from a training dataset

regressor - the PetscRegressor context

X - matrix of training data (of dimension [number of samples] x [number of features])

y - vector of target values from the training dataset

PetscRegressorCreate(), PetscRegressorSetUp(), PetscRegressorDestroy(), PetscRegressorPredict()

src/ml/regressor/interface/regressor.c

PetscRegressorFit_Linear() in src/ml/regressor/impls/linear/linear.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscRegressorFit(PetscRegressor regressor, Mat X, Vec y)
```

Example 2 (unknown):
```unknown
PetscRegressor
```

Example 3 (unknown):
```unknown
PetscRegressorCreate()
```

Example 4 (unknown):
```unknown
PetscRegressorSetUp()
```

---

## PetscRegressorGetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorGetOptionsPrefix/

**Contents:**
- PetscRegressorGetOptionsPrefix#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Fortran Notes#
- See Also#
- Level#
- Location#

Gets the prefix used for searching for all PetscRegressor options in the database

regressor - the PetscRegressor context

p - pointer to the prefix string used is returned

Pass in a string ‘prefix’ of sufficient length to hold the prefix.

PetscRegressor: Regression Solvers, PetscRegressor, PetscRegressorSetFromOptions(), PetscRegressorSetOptionsPrefix(), PetscRegressorAppendOptionsPrefix()

src/ml/regressor/interface/regressor.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscRegressorGetOptionsPrefix(PetscRegressor regressor, const char *p[])
```

Example 2 (unknown):
```unknown
PetscRegressor
```

Example 3 (unknown):
```unknown
PetscRegressor
```

Example 4 (unknown):
```unknown
PetscRegressorSetFromOptions()
```

---

## PetscRegressorGetTao#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorGetTao/

**Contents:**
- PetscRegressorGetTao#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Returns the Tao context for a PetscRegressor object.

Not Collective, but if the PetscRegressor is parallel, then the Tao object is parallel

regressor - the regressor context

tao - the Tao context

The Tao object will be created if it does not yet exist.

The user can directly manipulate the Tao context to set various options, etc. Likewise, the user can then extract and manipulate the child contexts such as KSP or TaoLineSearchas well.

Depending on the type of the regressor and the options that are set, the regressor may use not use a Tao object.

PetscRegressorLinearGetKSP()

src/ml/regressor/interface/regressor.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscRegressor
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscRegressorGetTao(PetscRegressor regressor, Tao *tao)
```

Example 3 (unknown):
```unknown
PetscRegressor
```

Example 4 (unknown):
```unknown
TaoLineSearch
```

---

## PetscRegressorGetType#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorGetType/

**Contents:**
- PetscRegressorGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the current PetscRegressorType being used in the PetscRegressor object

regressor - the PetscRegressor solver context

type - the PetscRegressorType

PetscRegressor: Regression Solvers, PetscRegressor, PetscRegressorType, PetscRegressorSetType()

src/ml/regressor/interface/regressor.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscRegressorType
```

Example 2 (unknown):
```unknown
PetscRegressor
```

Example 3 (unknown):
```unknown
PetscErrorCode PetscRegressorGetType(PetscRegressor regressor, PetscRegressorType *type)
```

Example 4 (unknown):
```unknown
PetscRegressor
```

---

## PetscRegressorInitializePackage#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorInitializePackage/

**Contents:**
- PetscRegressorInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

Initialize PetscRegressor package

PetscRegressorFinalizePackage()

src/ml/regressor/interface/dlregisregressor.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscRegressor
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscRegressorInitializePackage(void)
```

Example 3 (unknown):
```unknown
PetscRegressorFinalizePackage()
```

---

## PetscRegressorLinearGetCoefficients#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorLinearGetCoefficients/

**Contents:**
- PetscRegressorLinearGetCoefficients#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get a vector of the fitted coefficients from a linear regression model

Not Collective but the vector is parallel

regressor - the PetscRegressor context

coefficients - the vector of the coefficients

PetscRegressor, PetscRegressorLinearGetIntercept(), PETSCREGRESSORLINEAR, Vec

src/ml/regressor/impls/linear/linear.c

PetscRegressorLinearGetCoefficients_Linear() in src/ml/regressor/impls/linear/linear.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscregressor.h" 
PETSC_EXTERN PetscErrorCode PetscRegressorLinearGetCoefficients(PetscRegressor regressor, Vec *coefficients)
```

Example 2 (unknown):
```unknown
PetscRegressor
```

Example 3 (unknown):
```unknown
PetscRegressor
```

Example 4 (unknown):
```unknown
PetscRegressorLinearGetIntercept()
```

---

## PetscRegressorLinearGetIntercept#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorLinearGetIntercept/

**Contents:**
- PetscRegressorLinearGetIntercept#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get the intercept from a linear regression model

regressor - the PetscRegressor context

intercept - the intercept

PetscRegressor, PetscRegressorLinearSetFitIntercept(), PetscRegressorLinearGetCoefficients(), PETSCREGRESSORLINEAR

src/ml/regressor/impls/linear/linear.c

PetscRegressorLinearGetIntercept_Linear() in src/ml/regressor/impls/linear/linear.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscregressor.h" 
PETSC_EXTERN PetscErrorCode PetscRegressorLinearGetIntercept(PetscRegressor regressor, PetscScalar *intercept)
```

Example 2 (unknown):
```unknown
PetscRegressor
```

Example 3 (unknown):
```unknown
PetscRegressor
```

Example 4 (unknown):
```unknown
PetscRegressorLinearSetFitIntercept()
```

---

## PetscRegressorLinearGetKSP#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorLinearGetKSP/

**Contents:**
- PetscRegressorLinearGetKSP#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Returns the KSP context for a PETSCREGRESSORLINEAR object.

Not Collective, but if the PetscRegressor is parallel, then the KSP object is parallel

regressor - the PetscRegressor context

ksp - the KSP context

This routine will always return a KSP, but, depending on the type of the linear regressor and the options that are set, the regressor may actually use a Tao object instead of this KSP.

PetscRegressorGetTao()

src/ml/regressor/impls/linear/linear.c

PetscRegressorLinearGetKSP_Linear() in src/ml/regressor/impls/linear/linear.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCREGRESSORLINEAR
```

Example 2 (unknown):
```unknown
#include "petscregressor.h" 
PetscErrorCode PetscRegressorLinearGetKSP(PetscRegressor regressor, KSP *ksp)
```

Example 3 (unknown):
```unknown
PetscRegressor
```

Example 4 (unknown):
```unknown
PetscRegressor
```

---

## PetscRegressorLinearGetType#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorLinearGetType/

**Contents:**
- PetscRegressorLinearGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Return the type for the PETSCREGRESSORLINEAR solver

regressor - the PetscRegressor solver context

type - PETSCREGRESSORLINEAR type

PetscRegressor, PETSCREGRESSORLINEAR, PetscRegressorLinearSetType(), PetscRegressorLinearType

src/ml/regressor/impls/linear/linear.c

PetscRegressorLinearGetType_Linear() in src/ml/regressor/impls/linear/linear.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PETSCREGRESSORLINEAR
```

Example 2 (unknown):
```unknown
#include "petscregressor.h" 
PetscErrorCode PetscRegressorLinearGetType(PetscRegressor regressor, PetscRegressorLinearType *type)
```

Example 3 (unknown):
```unknown
PetscRegressor
```

Example 4 (unknown):
```unknown
PETSCREGRESSORLINEAR
```

---

## PetscRegressorLinearSetFitIntercept#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorLinearSetFitIntercept/

**Contents:**
- PetscRegressorLinearSetFitIntercept#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Set a flag to indicate that the intercept (also known as the “bias” or “offset”) should be calculated; data are assumed to be mean-centered if false.

regressor - the PetscRegressor context

flg - PETSC_TRUE to calculate the intercept, PETSC_FALSE to assume mean-centered data (default is PETSC_TRUE)

regressor_linear_fit_intercept (true|false) - fit the intercept

If the user indicates that the intercept should not be calculated, the intercept will be set to zero.

PetscRegressor, PetscRegressorFit()

src/ml/regressor/impls/linear/linear.c

PetscRegressorLinearSetFitIntercept_Linear() in src/ml/regressor/impls/linear/linear.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscregressor.h" 
PetscErrorCode PetscRegressorLinearSetFitIntercept(PetscRegressor regressor, PetscBool flg)
```

Example 2 (unknown):
```unknown
PetscRegressor
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (unknown):
```unknown
PetscRegressor
```

---

## PetscRegressorLinearSetType#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorLinearSetType/

**Contents:**
- PetscRegressorLinearSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

Sets the type of linear regression to be performed

regressor - the PetscRegressor context (should be of type PETSCREGRESSORLINEAR)

type - a known linear regression method

-regressor_linear_type - Sets the linear regression method; use -help for a list of available methods (for instance “-regressor_linear_type ols” or “-regressor_linear_type lasso”)

PetscRegressorLinearGetType(), PetscRegressorLinearType, PetscRegressorSetType(), REGRESSOR_LINEAR_OLS, REGRESSOR_LINEAR_LASSO, REGRESSOR_LINEAR_RIDGE

src/ml/regressor/impls/linear/linear.c

PetscRegressorLinearSetType_Linear() in src/ml/regressor/impls/linear/linear.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscregressor.h" 
PetscErrorCode PetscRegressorLinearSetType(PetscRegressor regressor, PetscRegressorLinearType type)
```

Example 2 (unknown):
```unknown
PetscRegressor
```

Example 3 (unknown):
```unknown
PETSCREGRESSORLINEAR
```

Example 4 (unknown):
```unknown
PetscRegressorLinearGetType()
```

---

## PetscRegressorLinearSetUseKSP#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorLinearSetUseKSP/

**Contents:**
- PetscRegressorLinearSetUseKSP#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#
- Implementations#

Set a flag to indicate that a KSP object, instead of a Tao one, should be used to fit the linear regressor

regressor - the PetscRegressor context

flg - PETSC_TRUE to use a KSP, PETSC_FALSE to use a Tao object (default is false)

regressor_linear_use_ksp (true|false) - use KSP

KSPLSQR with no preconditioner is used to solve the normal equations by default.

For sequential MATSEQAIJ sparse matrices QR factorization a PCType of PCQR can be used to solve the least-squares system with a MatSolverType of MATSOLVERSPQR, using, for example,

if centering, PetscRegressorLinearSetFitIntercept(), is not used.

It should be possible to use Cholesky (and any other preconditioners) to solve the normal equations.

It should be possible to use QR if centering is used. See ml/regressor/ex1.c and ex2.c

It should be possible to use dense SVD PCSVD and dense qr directly on the rectangular matrix to solve the least squares problem.

Adding the above support seems to require a refactorization of how least squares problems are solved with PETSc in KSPLSQR

PetscRegressor, PetscRegressorLinearGetKSP(), KSPLSQR, PCQR, MATSOLVERSPQR, MatSolverType, MATSEQDENSE, PCSVD

src/ml/regressor/impls/linear/linear.c

PetscRegressorLinearSetUseKSP_Linear() in src/ml/regressor/impls/linear/linear.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petscregressor.h" 
PetscErrorCode PetscRegressorLinearSetUseKSP(PetscRegressor regressor, PetscBool flg)
```

Example 2 (unknown):
```unknown
PetscRegressor
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (unknown):
```unknown
MatSolverType
```

---

## PetscRegressorLinearType#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorLinearType/

**Contents:**
- PetscRegressorLinearType#
- Synopsis#
- Values#
- Note#
- See Also#
- Level#
- Location#

Type of linear regression

REGRESSOR_LINEAR_OLS - ordinary least squares

REGRESSOR_LINEAR_LASSO - lasso

REGRESSOR_LINEAR_RIDGE - ridge

One can perform binary classification using the ridge regressor type by converting labels into the values -1 and +1, corresponding to the two classes, and then performing a ridge regression. Observations with a negative prediction value are then placed in the -1 class, while those with positive values are placed in the +1 class. This is the approach used in the RidgeClassifer implementation provided by the scikit-learn library.

PetscRegressor, PETSCREGRESSORLINEAR

include/petscregressor.h

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  REGRESSOR_LINEAR_OLS,
  REGRESSOR_LINEAR_LASSO,
  REGRESSOR_LINEAR_RIDGE
} PetscRegressorLinearType;
```

Example 2 (unknown):
```unknown
REGRESSOR_LINEAR_OLS
```

Example 3 (unknown):
```unknown
REGRESSOR_LINEAR_LASSO
```

Example 4 (unknown):
```unknown
REGRESSOR_LINEAR_RIDGE
```

---

## PETSCREGRESSORLINEAR#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PETSCREGRESSORLINEAR/

**Contents:**
- PETSCREGRESSORLINEAR#
- Options Database#
- Notes#
- See Also#
- Level#
- Location#

Linear regression model (ordinary least squares or regularized variants)

-regressor_linear_fit_intercept - Calculate the intercept for the linear model

-regressor_linear_use_ksp - Use KSP instead of Tao for linear model fitting (non-regularized variants only)

By “linear” we mean that the model is linear in its coefficients, but not necessarily in its input features. One can use the linear regressor to fit polynomial functions by training the model with a design matrix that is a nonlinear function of the input data.

This is the default regressor in PetscRegressor.

PetscRegressorCreate(), PetscRegressor, PetscRegressorSetType()

src/ml/regressor/impls/linear/linear.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscRegressor
```

Example 2 (unknown):
```unknown
PetscRegressorCreate()
```

Example 3 (unknown):
```unknown
PetscRegressor
```

Example 4 (unknown):
```unknown
PetscRegressorSetType()
```

---

## PetscRegressorPredict#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorPredict/

**Contents:**
- PetscRegressorPredict#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Compute predictions (that is, perform inference) using a fitted regression model.

regressor - the PetscRegressor context (for which PetscRegressorFit() must have been called)

X - data matrix of unlabeled observations

y - vector of predicted labels

PetscRegressorFit(), PetscRegressorDestroy()

src/ml/regressor/interface/regressor.c

PetscRegressorPredict_Linear() in src/ml/regressor/impls/linear/linear.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscRegressorPredict(PetscRegressor regressor, Mat X, Vec y)
```

Example 2 (unknown):
```unknown
PetscRegressor
```

Example 3 (unknown):
```unknown
PetscRegressorFit()
```

Example 4 (unknown):
```unknown
PetscRegressorFit()
```

---

## PetscRegressorRegister#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorRegister/

**Contents:**
- PetscRegressorRegister#
- Synopsis#
- Input Parameters#
- Notes#
- Example Usage#
- See Also#
- Level#
- Location#

Adds a method to the PetscRegressor package.

sname - name of a new user-defined regressor

function - routine to create method context

PetscRegressorRegister() may be called multiple times to add several user-defined regressors.

Then, your regressor can be chosen with the procedural interface via

or at runtime via the option

PetscRegressorRegisterAll()

src/ml/regressor/interface/regressor.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscRegressor
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscRegressorRegister(const char sname[], PetscErrorCode (*function)(PetscRegressor))
```

Example 3 (unknown):
```unknown
PetscRegressorRegister()
```

Example 4 (unknown):
```unknown
PetscRegressorRegister("my_regressor",MyRegressorCreate);
```

---

## PetscRegressorReset#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorReset/

**Contents:**
- PetscRegressorReset#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Resets a PetscRegressor context by removing any allocated Vec and Mat. Any options set in the object remain.

regressor - context obtained from PetscRegressorCreate()

PetscRegressorCreate(), PetscRegressorSetUp(), PetscRegressorFit(), PetscRegressorPredict(), PetscRegressorDestroy()

src/ml/regressor/interface/regressor.c

PetscRegressorReset_Linear() in src/ml/regressor/impls/linear/linear.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscRegressor
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscRegressorReset(PetscRegressor regressor)
```

Example 3 (unknown):
```unknown
PetscRegressorCreate()
```

Example 4 (unknown):
```unknown
PetscRegressorCreate()
```

---

## PetscRegressorSetFromOptions#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorSetFromOptions/

**Contents:**
- PetscRegressorSetFromOptions#
- Synopsis#
- Input Parameter#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Sets PetscRegressor options from the options database.

regressor - the PetscRegressor context

-regressor_type (linear) - the particular type of regressor to be used

This routine must be called before PetscRegressorSetUp() (or PetscRegressorFit(), which calls the former) if the user is to be allowed to set the regressor type.

PetscRegressor, PetscRegressorCreate()

src/ml/regressor/interface/regressor.c

PetscRegressorSetFromOptions_Linear() in src/ml/regressor/impls/linear/linear.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscRegressor
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscRegressorSetFromOptions(PetscRegressor regressor)
```

Example 3 (unknown):
```unknown
PetscRegressor
```

Example 4 (unknown):
```unknown
PetscRegressorSetUp()
```

---

## PetscRegressorSetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorSetOptionsPrefix/

**Contents:**
- PetscRegressorSetOptionsPrefix#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Sets the prefix used for searching for all PetscRegressor options in the database.

regressor - the PetscRegressor context

p - the prefix string to prepend to all PetscRegressor option requests

A hyphen (-) must NOT be given at the beginning of the prefix name. The first character of all runtime options is AUTOMATICALLY the hyphen.

For example, to distinguish between the runtime options for two different PetscRegressor solvers, one could call

This would enable use of different options for each system, such as

PetscRegressor: Regression Solvers, PetscRegressor, PetscRegressorSetFromOptions(), PetscRegressorAppendOptionsPrefix(), PetscRegressorGetOptionsPrefix()

src/ml/regressor/interface/regressor.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscRegressorSetOptionsPrefix(PetscRegressor regressor, const char p[])
```

Example 2 (unknown):
```unknown
PetscRegressor
```

Example 3 (unknown):
```unknown
PetscRegressorSetOptionsPrefix(regressor1,"sys1_")
      PetscRegressorSetOptionsPrefix(regressor2,"sys2_")
```

Example 4 (unknown):
```unknown
-sys1_regressor_method linear -sys1_regressor_regularizer_weight 1.2
      -sys2_regressor_method linear -sys2_regressor_regularizer_weight 1.1
```

---

## PetscRegressorSetRegularizerWeight#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorSetRegularizerWeight/

**Contents:**
- PetscRegressorSetRegularizerWeight#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Sets the weight to be used for the regularizer for a PetscRegressor context

regressor - the PetscRegressor context

weight - the regularizer weight

regressor_regularizer_weight weight - sets the regularizer’s weight

PetscRegressorSetType

src/ml/regressor/interface/regressor.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscRegressor
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscRegressorSetRegularizerWeight(PetscRegressor regressor, PetscReal weight)
```

Example 3 (unknown):
```unknown
PetscRegressor
```

Example 4 (unknown):
```unknown
PetscRegressorSetType
```

---

## PetscRegressorSetType#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorSetType/

**Contents:**
- PetscRegressorSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

Sets the type for the regressor.

regressor - the PetscRegressor context

type - a known regression method

-regressor_type type - Sets the type of regressor; use -help for a list of available types

See “include/petscregressor.h” for available methods (for instance)

PETSCREGRESSORLINEAR - Regression model that is linear in its coefficients; supports ordinary least squares as well as regularized variants

Normally, it is best to use the PetscRegressorSetFromOptions() command and then set the PetscRegressor type from the options database rather than by using this routine, as this provides maximum flexibility. The PetscRegressorSetType() routine is provided for those situations where it is necessary to set the nonlinear solver independently of the command line or options database.

src/ml/regressor/interface/regressor.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscRegressorSetType(PetscRegressor regressor, PetscRegressorType type)
```

Example 2 (unknown):
```unknown
PetscRegressor
```

Example 3 (unknown):
```unknown
PETSCREGRESSORLINEAR
```

Example 4 (unknown):
```unknown
PetscRegressorSetFromOptions()
```

---

## PetscRegressorSetUp#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorSetUp/

**Contents:**
- PetscRegressorSetUp#
- Synopsis#
- Input Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Sets up the internal data structures for the later use of a regressor.

regressor - the PetscRegressor context

For basic use of the PetscRegressor solvers the user need not to explicitly call PetscRegressorSetUp(), since these actions will automatically occur during the call to PetscRegressorFit(). However, if one wishes to control this phase separately, PetscRegressorSetUp() should be called after PetscRegressorCreate(), PetscRegressorSetUp(), and optional routines of the form PetscRegressorSetXXX(), but before PetscRegressorFit().

PetscRegressorCreate(), PetscRegressorFit(), PetscRegressorDestroy()

src/ml/regressor/interface/regressor.c

PetscRegressorSetUp_Linear() in src/ml/regressor/impls/linear/linear.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode PetscRegressorSetUp(PetscRegressor regressor)
```

Example 2 (unknown):
```unknown
PetscRegressor
```

Example 3 (unknown):
```unknown
PetscRegressor
```

Example 4 (unknown):
```unknown
PetscRegressorSetUp()
```

---

## PetscRegressorType#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorType/

**Contents:**
- PetscRegressorType#
- Synopsis#
- See Also#
- Level#
- Location#

String with the name of a PETSc regression method.

PetscRegressor: Regression Solvers, PetscRegressorSetType(), PetscRegressor, PetscRegressorRegister(), PetscRegressorCreate(), PetscRegressorSetFromOptions(), PETSCREGRESSORLINEAR

include/petscregressor.h

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef const char *PetscRegressorType;
#define PETSCREGRESSORLINEAR "linear"
```

Example 2 (unknown):
```unknown
PetscRegressorSetType()
```

Example 3 (unknown):
```unknown
PetscRegressor
```

Example 4 (unknown):
```unknown
PetscRegressorRegister()
```

---

## PetscRegressorViewFromOptions#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorViewFromOptions/

**Contents:**
- PetscRegressorViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

View a PetscRegressor object based on values in the options database

A - the PetscRegressor context

obj - Optional object that provides the prefix for the options database

name - command line option

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

PetscRegressor: Regression Solvers, PetscRegressor, PetscRegressorView, PetscObjectViewFromOptions(), PetscRegressorCreate()

src/ml/regressor/interface/regressor.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscRegressor
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscRegressorViewFromOptions(PetscRegressor A, PetscObject obj, const char name[])
```

Example 3 (unknown):
```unknown
PetscRegressor
```

Example 4 (unknown):
```unknown
PetscObjectViewFromOptions()
```

---

## PetscRegressorView#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressorView/

**Contents:**
- PetscRegressorView#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Prints information about the PetscRegressor object

regressor - the PetscRegressor context

viewer - a PetscViewer context

-regressor_view - Calls PetscRegressorView() at the end of PetscRegressorFit()

The available visualization contexts include

PETSC_VIEWER_STDOUT_SELF - standard output (default)

PETSC_VIEWER_STDOUT_WORLD - synchronized standard output where only the first processor opens the file. All other processors send their data to the first processor to print.

PetscRegressor: Regression Solvers, PetscRegressor, PetscViewerASCIIOpen()

src/ml/regressor/interface/regressor.c

PetscRegressorView_Linear() in src/ml/regressor/impls/linear/linear.c

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscRegressor
```

Example 2 (unknown):
```unknown
PetscErrorCode PetscRegressorView(PetscRegressor regressor, PetscViewer viewer)
```

Example 3 (unknown):
```unknown
PetscRegressor
```

Example 4 (unknown):
```unknown
PetscViewer
```

---

## PetscRegressor#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/PetscRegressor/

**Contents:**
- PetscRegressor#
- Synopsis#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Abstract PETSc object that manages regression and classification problems

For linear problems PetscRegressor supports ordinary least squares, lasso, and ridge regression using the PetscRegressorType of PETSCREGRESSORLINEAR and PetscRegressorLinearType of REGRESSOR_LINEAR_OLS, REGRESSOR_LINEAR_LASSO, and REGRESSOR_LINEAR_RIDGE.

We have slightly abused the term “regressor” in the naming of this component of PETSc. Statisticians would say that we are doing “regression”, and a “regressor”, in this context, strictly means an independent (or “predictor”) variable in the regression analysis. However, “regressor” has taken on an informal meaning in the machine-learning community of something along the lines of “algorithm or implementation used to fit a regression model”. Examples are MLPRegressor (multi-layer perceptron regressor) or RandomForestRegressor from the scikit-learn toolkit (which is itself not consistent about the use of the term “regressor”, since it has a LinearRegression component instead of a LinearRegressor component).

PetscRegressorCreate(), PetscRegressorLinearType, PetscRegressorSetType(), PetscRegressorType, PetscRegressorDestroy(), PETSCREGRESSORLINEAR, REGRESSOR_LINEAR_OLS, REGRESSOR_LINEAR_LASSO, REGRESSOR_LINEAR_RIDGE

include/petscregressor.h

_p_PetscRegressor in include/petsc/private/regressorimpl.h PetscRegressor_Linear in src/ml/regressor/impls/linear/linearimpl.h

Index of all PetscRegressor routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_PetscRegressor *PetscRegressor;
```

Example 2 (unknown):
```unknown
PetscRegressor
```

Example 3 (unknown):
```unknown
PetscRegressorType
```

Example 4 (unknown):
```unknown
PETSCREGRESSORLINEAR
```

---

## Regression Analysis and Classification (PetscRegressor)#

**URL:** https://petsc.org/release/manualpages/PetscRegressor/

**Contents:**
- Regression Analysis and Classification (PetscRegressor)#
- Beginner - Basic usage#
- Intermediate - Setting options for algorithms and data structures#
- Advanced - Setting more advanced options and customization#
- Developer - Interfaces rarely needed by applications programmers#
- Single list of manual pages#

The Regression Analysis and Classification (PetscRegressor) component provides a simple interface for supervised statistical (or machine) learning regression (prediction of continuous numerical values, including least squares with PETSCREGRESSORLINEAR) or classification (prediction of discrete labels or categories) tasks.

PetscRegressor internally employs Tao (or KSP for a few, specialized cases) to solve the underlying numerical optimization problems. PetscRegressor users can set Tao options or otherwise directly manipulate the underlying Tao context, which can be accessed via PetscRegressorGetTao(). User guide chapter: PetscRegressor: Regression Solvers.

PetscRegressorDestroy

PetscRegressorLinearGetCoefficients

PetscRegressorLinearGetIntercept

PetscRegressorLinearGetKSP

PetscRegressorPredict

PetscRegressorSetFromOptions

PetscRegressorSetRegularizerWeight

PetscRegressorGetType

PetscRegressorLinearSetFitIntercept

PetscRegressorLinearSetType

PetscRegressorLinearSetUseKSP

PetscRegressorSetType

PetscRegressorViewFromOptions

PetscRegressorAppendOptionsPrefix

PetscRegressorGetOptionsPrefix

PetscRegressorLinearGetType

PetscRegressorLinearType

PetscRegressorRegister

PetscRegressorSetOptionsPrefix

PetscRegressorFinalizePackage

PetscRegressorInitializePackage

PetscRegressorAppendOptionsPrefix

PetscRegressorDestroy

PetscRegressorFinalizePackage

PetscRegressorGetOptionsPrefix

PetscRegressorGetType

PetscRegressorInitializePackage

PetscRegressorLinearGetCoefficients

PetscRegressorLinearGetIntercept

PetscRegressorLinearGetKSP

PetscRegressorLinearGetType

PetscRegressorLinearSetFitIntercept

PetscRegressorLinearSetType

PetscRegressorLinearSetUseKSP

PetscRegressorLinearType

PetscRegressorPredict

PetscRegressorRegister

PetscRegressorSetFromOptions

PetscRegressorSetOptionsPrefix

PetscRegressorSetRegularizerWeight

PetscRegressorSetType

PetscRegressorViewFromOptions

Data Assimilation (PetscDA)

**Examples:**

Example 1 (unknown):
```unknown
PetscRegressor
```

Example 2 (unknown):
```unknown
PETSCREGRESSORLINEAR
```

Example 3 (unknown):
```unknown
PetscRegressor
```

Example 4 (unknown):
```unknown
PetscRegressor
```

---

## TaoAddLineSearchCounts#

**URL:** https://petsc.org/release/manualpages/Tao/TaoAddLineSearchCounts/

**Contents:**
- TaoAddLineSearchCounts#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Adds the number of function evaluations spent in the line search to the running total.

TAO: Optimization Solvers, Tao, TaoGetLineSearch(), TaoLineSearchApply()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoAddLineSearchCounts(Tao tao)
```

Example 2 (unknown):
```unknown
TaoGetLineSearch()
```

Example 3 (unknown):
```unknown
TaoLineSearchApply()
```

---

## TaoAddTerm#

**URL:** https://petsc.org/release/manualpages/Tao/TaoAddTerm/

**Contents:**
- TaoAddTerm#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Add a term to the objective function. If Tao is empty, term will be the objective of Tao.

tao - a Tao solver context

prefix - the prefix used for configuring the new term (if NULL, the index of the term will be used as a prefix, e.g. “0_”, “1_”, etc.)

scale - scaling coefficient for the new term

term - the real-valued function defining the new term

params - (optional) parameters for the new term. It is up to each implementation of TaoTerm to determine how it behaves when parameters are omitted.

map - (optional) a map from the tao solution space to the term solution space; if NULL the map is assumed to be the identity

If the objective function was \(f(x)\), after calling TaoAddTerm() it becomes \(f(x) + \alpha g(Ax; p)\), where \(\alpha\) is the scale, \(g\) is the term, \(A\) is the (optional) map, and \(p\) are the (optional) params of \(g\).

The map \(A\) transforms the Tao solution vector into the term’s solution space. For example, if the Tao solution vector is \(x \in \mathbb{R}^n\) and the mapping matrix is \(A \in \mathbb{R}^{m \times n}\), then the term evaluates \(g(Ax; p)\) with \(Ax \in \mathbb{R}^m\). The term’s solution space is therefore \(\mathbb{R}^m\). If the map is NULL, the identity is used and the term’s solution space must match the Tao solution space. Tao automatically applies the chain rule for gradients (\(A^T \nabla g\)) and Hessians (\(A^T \nabla^2 g \, A\)) with respect to \(x\).

The params \(p\) are fixed data that are not optimized over. Some TaoTermTypes require the parameter space to be related to the term’s solution space (e.g., the same size); when a mapping matrix \(A\) is used, the parameter space may depend on either the row or column space of \(A\). See the documentation for each TaoTermType.

Currently, TaoAddTerm() does not support bounded Newton solvers (TAOBNK,TAOBNLS,TAOBNTL,TAOBNTR,and TAOBQNK)

TAO: Optimization Solvers, Tao, TaoTerm, TAOTERMSUM, TaoGetTerm()

src/tao/interface/taosolver.c

src/tao/unconstrained/tutorials/rosenbrock1_taoterm.c src/tao/unconstrained/tutorials/elastic_net_regularization.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoAddTerm(Tao tao, const char prefix[], PetscReal scale, TaoTerm term, Vec params, Mat map)
```

Example 2 (unknown):
```unknown
TaoAddTerm()
```

Example 3 (unknown):
```unknown
TaoTermType
```

Example 4 (unknown):
```unknown
TaoTermType
```

---

## TaoADMMGetDualVector#

**URL:** https://petsc.org/release/manualpages/Tao/TaoADMMGetDualVector/

**Contents:**
- TaoADMMGetDualVector#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Returns the dual vector associated with the current TAOADMM state

tao - the Tao context

Y - the current solution

src/tao/constrained/impls/admm/admm.c

src/tao/constrained/tutorials/tomographyADMM.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoADMMGetDualVector(Tao tao, Vec *Y)
```

---

## TaoADMMGetMisfitSubsolver#

**URL:** https://petsc.org/release/manualpages/Tao/TaoADMMGetMisfitSubsolver/

**Contents:**
- TaoADMMGetMisfitSubsolver#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Get the pointer to the misfit subsolver inside TAOADMM

tao - the Tao solver context

misfit - the Tao subsolver context

src/tao/constrained/impls/admm/admm.c

src/tao/constrained/tutorials/tomographyADMM.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoADMMGetMisfitSubsolver(Tao tao, Tao *misfit)
```

---

## TaoADMMGetRegularizationSubsolver#

**URL:** https://petsc.org/release/manualpages/Tao/TaoADMMGetRegularizationSubsolver/

**Contents:**
- TaoADMMGetRegularizationSubsolver#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Get the pointer to the regularization subsolver inside TAOADMM

tao - the Tao solver context

reg - the Tao subsolver context

src/tao/constrained/impls/admm/admm.c

src/tao/constrained/tutorials/tomographyADMM.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoADMMGetRegularizationSubsolver(Tao tao, Tao *reg)
```

---

## TaoADMMGetRegularizerCoefficient#

**URL:** https://petsc.org/release/manualpages/Tao/TaoADMMGetRegularizerCoefficient/

**Contents:**
- TaoADMMGetRegularizerCoefficient#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Get the regularization coefficient lambda for L1 norm regularization case

tao - the Tao solver context

lambda - L1-norm regularizer coefficient

TaoADMMSetMisfitConstraintJacobian(), TaoADMMSetRegularizerConstraintJacobian(), TAOADMM

src/tao/constrained/impls/admm/admm.c

src/tao/constrained/tutorials/tomographyADMM.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoADMMGetRegularizerCoefficient(Tao tao, PetscReal *lambda)
```

Example 2 (unknown):
```unknown
TaoADMMSetMisfitConstraintJacobian()
```

Example 3 (unknown):
```unknown
TaoADMMSetRegularizerConstraintJacobian()
```

---

## TaoADMMGetRegularizerType#

**URL:** https://petsc.org/release/manualpages/Tao/TaoADMMGetRegularizerType/

**Contents:**
- TaoADMMGetRegularizerType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Gets the type of regularizer routine for TAOADMM

tao - the Tao context

type - the type of regularizer

TaoADMMSetRegularizerType(), TaoADMMRegularizerType, TAOADMM

src/tao/constrained/impls/admm/admm.c

TaoADMMGetRegularizerType_ADMM() in src/tao/constrained/impls/admm/admm.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoADMMGetRegularizerType(Tao tao, TaoADMMRegularizerType *type)
```

Example 2 (unknown):
```unknown
TaoADMMSetRegularizerType()
```

Example 3 (unknown):
```unknown
TaoADMMRegularizerType
```

---

## TaoADMMGetSpectralPenalty#

**URL:** https://petsc.org/release/manualpages/Tao/TaoADMMGetSpectralPenalty/

**Contents:**
- TaoADMMGetSpectralPenalty#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Get the spectral penalty (mu) value

tao - the Tao solver context

mu - spectral penalty

TaoADMMSetMinimumSpectralPenalty(), TaoADMMSetSpectralPenalty(), TAOADMM

src/tao/constrained/impls/admm/admm.c

src/tao/constrained/tutorials/tomographyADMM.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoADMMGetSpectralPenalty(Tao tao, PetscReal *mu)
```

Example 2 (unknown):
```unknown
TaoADMMSetMinimumSpectralPenalty()
```

Example 3 (unknown):
```unknown
TaoADMMSetSpectralPenalty()
```

---

## TaoADMMGetUpdateType#

**URL:** https://petsc.org/release/manualpages/Tao/TaoADMMGetUpdateType/

**Contents:**
- TaoADMMGetUpdateType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Gets the type of spectral penalty update routine for TAOADMM

tao - the Tao context

type - the type of spectral penalty update routine

TaoADMMSetUpdateType(), TaoADMMUpdateType, TAOADMM

src/tao/constrained/impls/admm/admm.c

TaoADMMGetUpdateType_ADMM() in src/tao/constrained/impls/admm/admm.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoADMMGetUpdateType(Tao tao, TaoADMMUpdateType *type)
```

Example 2 (unknown):
```unknown
TaoADMMSetUpdateType()
```

Example 3 (unknown):
```unknown
TaoADMMUpdateType
```

---

## TaoADMMRegularizerType#

**URL:** https://petsc.org/release/manualpages/Tao/TaoADMMRegularizerType/

**Contents:**
- TaoADMMRegularizerType#
- Synopsis#
- See Also#
- Level#
- Location#

Determine regularizer routine - either user provided or soft threshold for TAOADMM

TAO: Optimization Solvers, Tao, TAOADMM, TaoADMMSetRegularizerType()

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  TAO_ADMM_REGULARIZER_USER,
  TAO_ADMM_REGULARIZER_SOFT_THRESH
} TaoADMMRegularizerType;
```

Example 2 (unknown):
```unknown
TaoADMMSetRegularizerType()
```

---

## TaoADMMSetConstraintVectorRHS#

**URL:** https://petsc.org/release/manualpages/Tao/TaoADMMSetConstraintVectorRHS/

**Contents:**
- TaoADMMSetConstraintVectorRHS#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the RHS constraint vector for TAOADMM

tao - the Tao solver context

src/tao/constrained/impls/admm/admm.c

src/tao/constrained/tutorials/tomographyADMM.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoADMMSetConstraintVectorRHS(Tao tao, Vec c)
```

---

## TaoADMMSetMinimumSpectralPenalty#

**URL:** https://petsc.org/release/manualpages/Tao/TaoADMMSetMinimumSpectralPenalty/

**Contents:**
- TaoADMMSetMinimumSpectralPenalty#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the minimum value for the spectral penalty

tao - the Tao solver context

mu - minimum spectral penalty value

TaoADMMGetSpectralPenalty(), TAOADMM

src/tao/constrained/impls/admm/admm.c

src/tao/constrained/tutorials/tomographyADMM.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoADMMSetMinimumSpectralPenalty(Tao tao, PetscReal mu)
```

Example 2 (unknown):
```unknown
TaoADMMGetSpectralPenalty()
```

---

## TaoADMMSetMisfitConstraintJacobian#

**URL:** https://petsc.org/release/manualpages/Tao/TaoADMMSetMisfitConstraintJacobian/

**Contents:**
- TaoADMMSetMisfitConstraintJacobian#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

Set the constraint matrix B for the TAOADMM algorithm. Matrix B constrains the z variable.

tao - the Tao solver context

J - user-created misfit constraint Jacobian matrix

Jpre - user-created misfit Jacobian constraint matrix for constructing the preconditioner, often this is J

func - function pointer for the misfit constraint Jacobian update function

ctx - application context for the regularizer constraint Jacobian

tao - the Tao context

u - in current input solution

J - the contribution to the misfit constraint Jacobian

Jpre - the contribution to matrix from which to construct a preconditioner for the misfit constraint Jacobian

ctx - the optional application context

TaoADMMSetRegularizerCoefficient(), TaoADMMSetRegularizerConstraintJacobian(), TAOADMM

src/tao/constrained/impls/admm/admm.c

src/tao/constrained/tutorials/tomographyADMM.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoADMMSetMisfitConstraintJacobian(Tao tao, Mat J, Mat Jpre, PetscErrorCode (*func)(Tao tao, Vec u, Mat J, Mat Jpre, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoADMMSetRegularizerCoefficient()
```

Example 3 (unknown):
```unknown
TaoADMMSetRegularizerConstraintJacobian()
```

---

## TaoADMMSetMisfitHessianChangeStatus#

**URL:** https://petsc.org/release/manualpages/Tao/TaoADMMSetMisfitHessianChangeStatus/

**Contents:**
- TaoADMMSetMisfitHessianChangeStatus#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set boolean that determines whether Hessian matrix of misfit subsolver changes with respect to input vector.

tao - the Tao solver context.

b - the Hessian matrix change status boolean, PETSC_FALSE when the Hessian matrix does not change, PETSC_TRUE otherwise.

src/tao/constrained/impls/admm/admm.c

src/tao/constrained/tutorials/tomographyADMM.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoADMMSetMisfitHessianChangeStatus(Tao tao, PetscBool b)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

---

## TaoADMMSetMisfitHessianRoutine#

**URL:** https://petsc.org/release/manualpages/Tao/TaoADMMSetMisfitHessianRoutine/

**Contents:**
- TaoADMMSetMisfitHessianRoutine#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

Sets the user-defined misfit Hessian call-back function into the algorithm, to be used for subsolverX.

tao - the Tao context

H - user-created matrix for the Hessian of the misfit term

Hpre - user-created matrix for the preconditioner of Hessian of the misfit term

func - function pointer for the misfit Hessian evaluation

ctx - application context for the misfit Hessian

tao - the Tao context

u - in current input solution

H - output, the contribution to the Hessian matrix

Hpre - an optional contribution to an alternative matrix with which the preconditioner is to be constructed

ctx - the optional application context

src/tao/constrained/impls/admm/admm.c

src/tao/constrained/tutorials/tomographyADMM.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoADMMSetMisfitHessianRoutine(Tao tao, Mat H, Mat Hpre, PetscErrorCode (*func)(Tao tao, Vec u, Mat H, Mat Hpre, PetscCtx ctx), PetscCtx ctx)
```

---

## TaoADMMSetMisfitObjectiveAndGradientRoutine#

**URL:** https://petsc.org/release/manualpages/Tao/TaoADMMSetMisfitObjectiveAndGradientRoutine/

**Contents:**
- TaoADMMSetMisfitObjectiveAndGradientRoutine#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

Sets the user-defined misfit call-back function

tao - the Tao context

func - function pointer for the misfit value and gradient evaluation

ctx - application context for the misfit

tao - the Tao context

u - in current input solution

f - the contribution to the objective function

g - the contribution to the gradient

ctx - the optional application context

src/tao/constrained/impls/admm/admm.c

src/tao/constrained/tutorials/tomographyADMM.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoADMMSetMisfitObjectiveAndGradientRoutine(Tao tao, PetscErrorCode (*func)(Tao tao, Vec u, PetscReal *f, Vec g, PetscCtx ctx), PetscCtx ctx)
```

---

## TaoADMMSetRegHessianChangeStatus#

**URL:** https://petsc.org/release/manualpages/Tao/TaoADMMSetRegHessianChangeStatus/

**Contents:**
- TaoADMMSetRegHessianChangeStatus#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set boolean that determines whether Hessian matrix of regularization subsolver changes with respect to input vector.

tao - the Tao solver context

b - the Hessian matrix change status boolean, PETSC_FALSE when the Hessian matrix does not change, PETSC_TRUE otherwise.

src/tao/constrained/impls/admm/admm.c

src/tao/constrained/tutorials/tomographyADMM.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoADMMSetRegHessianChangeStatus(Tao tao, PetscBool b)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

---

## TaoADMMSetRegularizerCoefficient#

**URL:** https://petsc.org/release/manualpages/Tao/TaoADMMSetRegularizerCoefficient/

**Contents:**
- TaoADMMSetRegularizerCoefficient#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the regularization coefficient lambda for L1 norm regularization case

tao - the Tao solver context

lambda - L1-norm regularizer coefficient

TaoADMMSetMisfitConstraintJacobian(), TaoADMMSetRegularizerConstraintJacobian(), TAOADMM

src/tao/constrained/impls/admm/admm.c

src/tao/constrained/tutorials/tomographyADMM.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoADMMSetRegularizerCoefficient(Tao tao, PetscReal lambda)
```

Example 2 (unknown):
```unknown
TaoADMMSetMisfitConstraintJacobian()
```

Example 3 (unknown):
```unknown
TaoADMMSetRegularizerConstraintJacobian()
```

---

## TaoADMMSetRegularizerConstraintJacobian#

**URL:** https://petsc.org/release/manualpages/Tao/TaoADMMSetRegularizerConstraintJacobian/

**Contents:**
- TaoADMMSetRegularizerConstraintJacobian#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

Set the constraint matrix B for TAOADMM algorithm. Matrix B constraints z variable.

tao - the Tao solver context

J - user-created regularizer constraint Jacobian matrix

Jpre - user-created regularizer Jacobian constraint matrix for constructing the preconditioner, often this is J

func - function pointer for the regularizer constraint Jacobian update function

ctx - application context for the regularizer constraint Jacobian

tao - the Tao context

u - in current input solution

J - the contribution to the constraint Jacobian

Jpre - the contribution to matrix from which to construct a preconditioner for the constraint Jacobian

ctx - the optional application context

TaoADMMSetRegularizerCoefficient(), TaoADMMSetMisfitConstraintJacobian(), TAOADMM

src/tao/constrained/impls/admm/admm.c

src/tao/constrained/tutorials/tomographyADMM.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoADMMSetRegularizerConstraintJacobian(Tao tao, Mat J, Mat Jpre, PetscErrorCode (*func)(Tao tao, Vec u, Mat J, Mat Jpre, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoADMMSetRegularizerCoefficient()
```

Example 3 (unknown):
```unknown
TaoADMMSetMisfitConstraintJacobian()
```

---

## TaoADMMSetRegularizerHessianRoutine#

**URL:** https://petsc.org/release/manualpages/Tao/TaoADMMSetRegularizerHessianRoutine/

**Contents:**
- TaoADMMSetRegularizerHessianRoutine#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

Sets the user-defined regularizer Hessian call-back function, to be used for subsolverZ.

tao - the Tao context

H - user-created matrix for the Hessian of the regularization term

Hpre - user-created matrix for building the preconditioner of the Hessian of the regularization term

func - function pointer for the regularizer Hessian evaluation

ctx - application context for the regularizer Hessian

tao - the Tao context

u - in current input solution

H - output, the contribution to the Hessian matrix

Hpre - an optional contribution to an alternative matrix with which the preconditioner is to be constructed

ctx - the optional application context

src/tao/constrained/impls/admm/admm.c

src/tao/constrained/tutorials/tomographyADMM.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoADMMSetRegularizerHessianRoutine(Tao tao, Mat H, Mat Hpre, PetscErrorCode (*func)(Tao tao, Vec u, Mat H, Mat Hpre, PetscCtx ctx), PetscCtx ctx)
```

---

## TaoADMMSetRegularizerObjectiveAndGradientRoutine#

**URL:** https://petsc.org/release/manualpages/Tao/TaoADMMSetRegularizerObjectiveAndGradientRoutine/

**Contents:**
- TaoADMMSetRegularizerObjectiveAndGradientRoutine#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

Sets the user-defined regularizer call-back function

tao - the Tao context

func - function pointer for the regularizer value and gradient evaluation

ctx - application context for the regularizer

tao - the Tao context

u - in current input solution

f - the contribution to the objective function

g - the contribution to the gradient

ctx - the optional application context

src/tao/constrained/impls/admm/admm.c

src/tao/constrained/tutorials/tomographyADMM.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoADMMSetRegularizerObjectiveAndGradientRoutine(Tao tao, PetscErrorCode (*func)(Tao tao, Vec u, PetscReal *f, Vec g, PetscCtx ctx), PetscCtx ctx)
```

---

## TaoADMMSetRegularizerType#

**URL:** https://petsc.org/release/manualpages/Tao/TaoADMMSetRegularizerType/

**Contents:**
- TaoADMMSetRegularizerType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

Set regularizer type for TAOADMM routine

tao - the Tao context

type - regularizer type

-tao_admm_regularizer_type (regularizer_user|regularizer_soft_thresh) - select the regularizer

TaoADMMGetRegularizerType(), TaoADMMRegularizerType, TAOADMM

src/tao/constrained/impls/admm/admm.c

TaoADMMSetRegularizerType_ADMM() in src/tao/constrained/impls/admm/admm.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoADMMSetRegularizerType(Tao tao, TaoADMMRegularizerType type)
```

Example 2 (unknown):
```unknown
TaoADMMGetRegularizerType()
```

Example 3 (unknown):
```unknown
TaoADMMRegularizerType
```

---

## TaoADMMSetSpectralPenalty#

**URL:** https://petsc.org/release/manualpages/Tao/TaoADMMSetSpectralPenalty/

**Contents:**
- TaoADMMSetSpectralPenalty#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the spectral penalty (mu) value

tao - the Tao solver context

mu - spectral penalty

TaoADMMSetMinimumSpectralPenalty(), TAOADMM

src/tao/constrained/impls/admm/admm.c

src/tao/constrained/tutorials/tomographyADMM.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoADMMSetSpectralPenalty(Tao tao, PetscReal mu)
```

Example 2 (unknown):
```unknown
TaoADMMSetMinimumSpectralPenalty()
```

---

## TaoADMMSetUpdateType#

**URL:** https://petsc.org/release/manualpages/Tao/TaoADMMSetUpdateType/

**Contents:**
- TaoADMMSetUpdateType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set update routine for TAOADMM routine

tao - the Tao context

type - spectral parameter update type

TaoADMMGetUpdateType(), TaoADMMUpdateType, TAOADMM

src/tao/constrained/impls/admm/admm.c

TaoADMMSetUpdateType_ADMM() in src/tao/constrained/impls/admm/admm.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoADMMSetUpdateType(Tao tao, TaoADMMUpdateType type)
```

Example 2 (unknown):
```unknown
TaoADMMGetUpdateType()
```

Example 3 (unknown):
```unknown
TaoADMMUpdateType
```

---

## TaoADMMUpdateType#

**URL:** https://petsc.org/release/manualpages/Tao/TaoADMMUpdateType/

**Contents:**
- TaoADMMUpdateType#
- Synopsis#
- See Also#
- Level#
- Location#

Determine the spectral penalty update routine for the Lagrange augmented term for TAOADMM.

TAO: Optimization Solvers, Tao, TAOADMM, TaoADMMSetUpdateType()

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  TAO_ADMM_UPDATE_BASIC,
  TAO_ADMM_UPDATE_ADAPTIVE,
  TAO_ADMM_UPDATE_ADAPTIVE_RELAXED
} TaoADMMUpdateType;
```

Example 2 (unknown):
```unknown
TaoADMMSetUpdateType()
```

---

## TAOADMM#

**URL:** https://petsc.org/release/manualpages/Tao/TAOADMM/

**Contents:**
- TAOADMM#
- Options Database Keys#
- References#
- See Also#
- Level#
- Location#
- Examples#

Alternating direction method of multipliers method for solving linear problems with constraints. in a \( \min_x f(x) + g(z)\) s.t. \(Ax+Bz=c\). This algorithm employs two sub Tao solvers, of which type can be specified by the user. User need to provide ObjectiveAndGradient routine, and/or HessianRoutine for both subsolvers. Hessians can be given boolean flag determining whether they change with respect to a input vector. This can be set via TaoADMMSet{Misfit,Regularizer}HessianChangeStatus(). Second subsolver does support TAOSHELL. It should be noted that L1-norm is used for objective value for TAOSHELL type. There is option to set regularizer option, and currently soft-threshold is implemented. For spectral penalty update, currently there are basic option and adaptive option. Constraint is set at Ax+Bz=c, and A and B can be set with TaoADMMSet{Misfit,Regularizer}ConstraintJacobian(). c can be set with TaoADMMSetConstraintVectorRHS(). The user can also provide regularizer weight for second subsolver. [XFY+17]

-tao_admm_regularizer_coefficient - regularizer constant (default 1.e-6)

-tao_admm_spectral_penalty - Constant for Augmented Lagrangian term (default 1.)

-tao_admm_relaxation_parameter - relaxation parameter for Z update (default 1.)

-tao_admm_tolerance_update_factor - ADMM dynamic tolerance update factor (default 1.e-12)

-tao_admm_spectral_penalty_update_factor - ADMM spectral penalty update curvature safeguard value (default 0.2)

-tao_admm_minimum_spectral_penalty - Set ADMM minimum spectral penalty (default 0)

-tao_admm_dual_update - Lagrangian dual update policy (“basic”,”adaptive”,”adaptive-relaxed”) (default “basic”)

-tao_admm_regularizer_type - ADMM regularizer update rule (“user”,”soft-threshold”) (default “soft-threshold”)

Zheng Xu, Mario AT Figueiredo, Xiaoming Yuan, Christoph Studer, and Tom Goldstein. Adaptive relaxed ADMM: convergence theory and practical implementation. In Proceedings of the IEEE conference on computer vision and pattern recognition, 7389–7398. 2017.

TaoADMMSetMisfitHessianChangeStatus(), TaoADMMSetRegHessianChangeStatus(), TaoADMMGetSpectralPenalty(), TaoADMMGetMisfitSubsolver(), TaoADMMGetRegularizationSubsolver(), TaoADMMSetConstraintVectorRHS(), TaoADMMSetMinimumSpectralPenalty(), TaoADMMSetRegularizerCoefficient(), TaoADMMGetRegularizerCoefficient(), TaoADMMSetRegularizerConstraintJacobian(), TaoADMMSetMisfitConstraintJacobian(), TaoADMMSetMisfitObjectiveAndGradientRoutine(), TaoADMMSetMisfitHessianRoutine(), TaoADMMSetRegularizerObjectiveAndGradientRoutine(), TaoADMMSetRegularizerHessianRoutine(), TaoGetADMMParentTao(), TaoADMMGetDualVector(), TaoADMMSetRegularizerType(), TaoADMMGetRegularizerType(), TaoADMMSetUpdateType(), TaoADMMGetUpdateType()

src/tao/constrained/impls/admm/admm.c

src/tao/constrained/tutorials/tomographyADMM.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoADMMSet{Misfit,Regularizer}HessianChangeStatus()
```

Example 2 (unknown):
```unknown
TaoADMMSet{Misfit,Regularizer}ConstraintJacobian()
```

Example 3 (unknown):
```unknown
TaoADMMSetConstraintVectorRHS()
```

Example 4 (unknown):
```unknown
TaoADMMSetMisfitHessianChangeStatus()
```

---

## TaoALMMGetDualIS#

**URL:** https://petsc.org/release/manualpages/Tao/TaoALMMGetDualIS/

**Contents:**
- TaoALMMGetDualIS#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Retrieve the index set that identifies equality and inequality constraint components of the dual vector returned by TaoALMMGetMultipliers().

tao - the Tao context for the TAOALMM solver

eq_is - index set associated with the equality constraints (NULL if not needed)

ineq_is - index set associated with the inequality constraints (NULL if not needed)

TAOALMM, Tao, TaoALMMGetMultipliers()

src/tao/constrained/impls/almm/almmutils.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoALMMGetMultipliers()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoALMMGetDualIS(Tao tao, IS *eq_is, IS *ineq_is)
```

Example 3 (unknown):
```unknown
TaoALMMGetMultipliers()
```

---

## TaoALMMGetMultipliers#

**URL:** https://petsc.org/release/manualpages/Tao/TaoALMMGetMultipliers/

**Contents:**
- TaoALMMGetMultipliers#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Retrieve a pointer to the Lagrange multipliers.

tao - the Tao context for the TAOALMM solver

Y - vector of Lagrange multipliers

For problems with both equality and inequality constraints, the multipliers are combined together as Y = (Ye, Yi). Users can recover copies of the subcomponents using index sets provided by TaoALMMGetDualIS() and use VecGetSubVector().

TAOALMM, Tao, TaoALMMSetMultipliers(), TaoALMMGetDualIS()

src/tao/constrained/impls/almm/almmutils.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoALMMGetMultipliers(Tao tao, Vec *Y)
```

Example 2 (unknown):
```unknown
TaoALMMGetDualIS()
```

Example 3 (unknown):
```unknown
VecGetSubVector()
```

Example 4 (unknown):
```unknown
TaoALMMSetMultipliers()
```

---

## TaoALMMGetPrimalIS#

**URL:** https://petsc.org/release/manualpages/Tao/TaoALMMGetPrimalIS/

**Contents:**
- TaoALMMGetPrimalIS#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Retrieve the index set that identifies optimization and slack variable components of the subsolver’s solution vector.

tao - the Tao context for the TAOALMM solver

opt_is - index set associated with the optimization variables (NULL if not needed)

slack_is - index set associated with the slack variables (NULL if not needed)

TAOALMM, Tao, IS, TaoALMMGetPrimalVector()

src/tao/constrained/impls/almm/almmutils.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoALMMGetPrimalIS(Tao tao, IS *opt_is, IS *slack_is)
```

Example 2 (unknown):
```unknown
TaoALMMGetPrimalVector()
```

---

## TaoALMMGetSubsolver#

**URL:** https://petsc.org/release/manualpages/Tao/TaoALMMGetSubsolver/

**Contents:**
- TaoALMMGetSubsolver#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Retrieve the subsolver being used by TAOALMM.

tao - the Tao context for the TAOALMM solver

subsolver - the Tao context for the subsolver

Tao, TAOALMM, TaoALMMSetSubsolver()

src/tao/constrained/impls/almm/almmutils.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoALMMGetSubsolver(Tao tao, Tao *subsolver)
```

Example 2 (unknown):
```unknown
TaoALMMSetSubsolver()
```

---

## TaoALMMGetType#

**URL:** https://petsc.org/release/manualpages/Tao/TaoALMMGetType/

**Contents:**
- TaoALMMGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Retrieve the augmented Lagrangian formulation type for the subproblem.

tao - the Tao context for the TAOALMM solver

type - augmented Lagragrangian type

Tao, TAOALMM, TaoALMMSetType(), TaoALMMType

src/tao/constrained/impls/almm/almmutils.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoALMMGetType(Tao tao, TaoALMMType *type)
```

Example 2 (unknown):
```unknown
TaoALMMSetType()
```

Example 3 (unknown):
```unknown
TaoALMMType
```

---

## TaoALMMSetMultipliers#

**URL:** https://petsc.org/release/manualpages/Tao/TaoALMMSetMultipliers/

**Contents:**
- TaoALMMSetMultipliers#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Set user-defined Lagrange multipliers.

tao - the Tao context for the TAOALMM solver

Y - vector of Lagrange multipliers

The vector type and parallel layout must match the equality and inequality constraints.

The vector must have a local size equal to the sum of the local sizes for the constraint vectors, and a global size equal to the sum of the global sizes of the constraint vectors.

This routine is only useful if the user wants to change the parallel distribution of the combined dual vector in problems that feature both equality and inequality constraints. For other tasks, it is strongly recommended that the user retrieve the dual vector created by the solver using TaoALMMGetMultipliers().

TAOALMM, Tao, TaoALMMGetMultipliers()

src/tao/constrained/impls/almm/almmutils.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoALMMSetMultipliers(Tao tao, Vec Y)
```

Example 2 (unknown):
```unknown
TaoALMMGetMultipliers()
```

Example 3 (unknown):
```unknown
TaoALMMGetMultipliers()
```

---

## TaoALMMSetSubsolver#

**URL:** https://petsc.org/release/manualpages/Tao/TaoALMMSetSubsolver/

**Contents:**
- TaoALMMSetSubsolver#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Changes the subsolver inside TAOALMM with the user provided one.

tao - the Tao context for the TAOALMM solver

subsolver - the Tao context for the subsolver

This is not recommended, instead call TaoALMMGetSubsolver() and set the type as desired.

Tao, TAOALMM, TaoALMMGetSubsolver()

src/tao/constrained/impls/almm/almmutils.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoALMMSetSubsolver(Tao tao, Tao subsolver)
```

Example 2 (unknown):
```unknown
TaoALMMGetSubsolver()
```

Example 3 (unknown):
```unknown
TaoALMMGetSubsolver()
```

---

## TaoALMMSetType#

**URL:** https://petsc.org/release/manualpages/Tao/TaoALMMSetType/

**Contents:**
- TaoALMMSetType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Determine the augmented Lagrangian formulation type for the subproblem.

tao - the Tao context for the TAOALMM solver

type - augmented Lagragrangian type

Tao, TAOALMM, TaoALMMGetType(), TaoALMMType

src/tao/constrained/impls/almm/almmutils.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoALMMSetType(Tao tao, TaoALMMType type)
```

Example 2 (unknown):
```unknown
TaoALMMGetType()
```

Example 3 (unknown):
```unknown
TaoALMMType
```

---

## TaoALMMType#

**URL:** https://petsc.org/release/manualpages/Tao/TaoALMMType/

**Contents:**
- TaoALMMType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Determine the augmented Lagrangian formulation used in the TAOALMM subproblem.

TAO_ALMM_CLASSIC - classic augmented Lagrangian definition including slack variables for inequality constraints

TAO_ALMM_PHR - Powell-Hestenes-Rockafellar formulation without slack variables, uses pointwise min() for inequalities

TAO: Optimization Solvers, Tao, TAOALMM, TaoALMMSetType(), TaoALMMGetType()

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  TAO_ALMM_CLASSIC,
  TAO_ALMM_PHR
} TaoALMMType;
```

Example 2 (unknown):
```unknown
TAO_ALMM_CLASSIC
```

Example 3 (unknown):
```unknown
TAO_ALMM_PHR
```

Example 4 (unknown):
```unknown
TaoALMMSetType()
```

---

## TAOALMM#

**URL:** https://petsc.org/release/manualpages/Tao/TAOALMM/

**Contents:**
- TAOALMM#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Augmented Lagrangian multiplier method for solving nonlinear optimization problems with general constraints.

-tao_almm_mu_init real - initial penalty parameter (default: 10.)

-tao_almm_mu_factor real - increase factor for the penalty parameter (default: 100.)

-tao_almm_mu_max real - maximum safeguard for penalty parameter updates (default: 1.e20)

-tao_almm_mu_power_good real - exponential for penalty parameter when multiplier update is accepted (default: 0.9)

-tao_almm_mu_power_bad real - exponential for penalty parameter when multiplier update is rejected (default: 0.1)

-tao_almm_ye_min real - minimum safeguard for equality multiplier updates (default: -1.e20)

-tao_almm_ye_max real - maximum safeguard for equality multiplier updates (default: 1.e20)

-tao_almm_yi_min real - minimum safeguard for inequality multiplier updates (default: -1.e20)

-tao_almm_yi_max real - maximum safeguard for inequality multiplier updates (default: 1.e20)

-tao_almm_type (phr|classic) - change formulation of the augmented Lagrangian merit function for the subproblem (default: phr)

This method converts a constrained problem into a sequence of unconstrained problems via the augmented Lagrangian merit function. Bound constraints are pushed down to the subproblem without any modifications.

Two formulations are offered for the subproblem: canonical Hestenes-Powell augmented Lagrangian with slack variables for inequality constraints, and a slack-less Powell-Hestenes-Rockafellar (PHR) formulation utilizing a pointwise max() penalty on inequality constraints. The canonical augmented Lagrangian formulation may converge faster for smaller problems but is highly susceptible to poor step lengths in the subproblem due to the positivity constraint on slack variables. PHR avoids this issue by eliminating the slack variables entirely, and is highly desirable for problems with a large number of inequality constraints.

The subproblem is solved using a nested first-order TAO solver (default: TAOBQNLS). The user can retrieve a pointer to the subsolver via TaoALMMGetSubsolver() or pass command line arguments to it using the “-tao_almm_subsolver_” prefix. Currently, TAOALMM does not support second-order methods for the subproblem.

TAOALMM, Tao, TaoALMMGetType(), TaoALMMSetType(), TaoALMMSetSubsolver(), TaoALMMGetSubsolver(), TaoALMMGetMultipliers(), TaoALMMSetMultipliers(), TaoALMMGetPrimalIS(), TaoALMMGetDualIS()

src/tao/constrained/impls/almm/almm.c

src/tao/constrained/tutorials/ex1.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoALMMGetSubsolver()
```

Example 2 (sql):
```sql
while unconverged
    solve argmin_x L(x) s.t. l <= x <= u
    if ||c|| <= y_tol
      if ||c|| <= c_tol && ||Lgrad|| <= g_tol:
        problem converged, return solution
      else
        constraints sufficiently improved
        update multipliers and tighten tolerances
      endif
    else
      constraints did not improve
      update penalty and loosen tolerances
    endif
  endwhile
```

Example 3 (unknown):
```unknown
TaoALMMGetType()
```

Example 4 (unknown):
```unknown
TaoALMMSetType()
```

---

## TaoAppendOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/Tao/TaoAppendOptionsPrefix/

**Contents:**
- TaoAppendOptionsPrefix#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Appends to the prefix used for searching for all Tao options in the database.

tao - the Tao solver context

p - the prefix string to prepend to all Tao option requests

A hyphen (-) must NOT be given at the beginning of the prefix name. The first character of all runtime options is automatically the hyphen.

TAO: Optimization Solvers, Tao, TaoSetFromOptions(), TaoSetOptionsPrefix(), TaoGetOptionsPrefix()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoAppendOptionsPrefix(Tao tao, const char p[])
```

Example 2 (unknown):
```unknown
TaoSetFromOptions()
```

Example 3 (unknown):
```unknown
TaoSetOptionsPrefix()
```

Example 4 (unknown):
```unknown
TaoGetOptionsPrefix()
```

---

## TAOASFLS#

**URL:** https://petsc.org/release/manualpages/Tao/TAOASFLS/

**Contents:**
- TAOASFLS#
- Options Database Keys#
- Note#
- References#
- See Also#
- Level#
- Location#

Active-set feasible linesearch algorithm for solving complementarity constraints

-tao_ssls_delta - descent test fraction

-tao_ssls_rho - descent test power

See [Bil95], [DeLucaFK96], [FKM99], [Fis92], and [MFF+01].

S. C. Billups. Algorithms for Complementarity Problems and Generalized Equations. PhD thesis, University of Wisconsin–Madison, Madison, Wisconsin, August 1995.

M. C. Ferris, C. Kanzow, and T. S. Munson. Feasible descent algorithms for mixed complementarity problems. Mathematical Programming, 86:475–497, 1999. URL: ftp://ftp.cs.wisc.edu/math-prog/tech-reports/98-04.ps.

A. Fischer. A special Newton–type optimization method. Optimization, 24:269–284, 1992.

T. S. Munson, F. Facchinei, M. C. Ferris, A. Fischer, and C. Kanzow. The semismooth algorithm for large scale complementarity problems. INFORMS Journal on Computing, 2001.

T. De Luca, F. Facchinei, and C. Kanzow. A semismooth equation approach to the solution of nonlinear complementarity problems. Mathematical Programming, 75:407–439, 1996.

Tao, TaoType, TAOASILS

src/tao/complementarity/impls/asls/asfls.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

---

## TAOASILS#

**URL:** https://petsc.org/release/manualpages/Tao/TAOASILS/

**Contents:**
- TAOASILS#
- Options Database Keys#
- Note#
- References#
- See Also#
- Level#
- Location#

Active-set infeasible linesearch algorithm for solving complementarity constraints

-tao_ssls_delta - descent test fraction

-tao_ssls_rho - descent test power

See [Bil95], [DeLucaFK96], [FKM99], [Fis92], and [MFF+01].

S. C. Billups. Algorithms for Complementarity Problems and Generalized Equations. PhD thesis, University of Wisconsin–Madison, Madison, Wisconsin, August 1995.

M. C. Ferris, C. Kanzow, and T. S. Munson. Feasible descent algorithms for mixed complementarity problems. Mathematical Programming, 86:475–497, 1999. URL: ftp://ftp.cs.wisc.edu/math-prog/tech-reports/98-04.ps.

A. Fischer. A special Newton–type optimization method. Optimization, 24:269–284, 1992.

T. S. Munson, F. Facchinei, M. C. Ferris, A. Fischer, and C. Kanzow. The semismooth algorithm for large scale complementarity problems. INFORMS Journal on Computing, 2001.

T. De Luca, F. Facchinei, and C. Kanzow. A semismooth equation approach to the solution of nonlinear complementarity problems. Mathematical Programming, 75:407–439, 1996.

Tao, TaoType, TAOASFLS

src/tao/complementarity/impls/asls/asils.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

---

## TAOBLMVM#

**URL:** https://petsc.org/release/manualpages/Tao/TAOBLMVM/

**Contents:**
- TAOBLMVM#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

Bounded limited memory variable metric is a quasi-Newton method for nonlinear minimization with bound constraints. It is an extension of TAOLMVM

-tao_lmm_recycle - enable recycling of LMVM information between subsequent TaoSolve() calls

Tao, TAOLMVM, TAOBLMVM, TaoLMVMGetH0(), TaoLMVMGetH0KSP()

src/tao/bound/impls/blmvm/blmvm.c

src/tao/bound/tutorials/plate2f.F90 src/tao/bound/tutorials/jbearing2.c src/ts/tutorials/ex20opt_ic.c src/tao/tutorials/ex3.c src/tao/bound/tutorials/plate2.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoLMVMGetH0()
```

Example 2 (unknown):
```unknown
TaoLMVMGetH0KSP()
```

---

## TAOBMRM#

**URL:** https://petsc.org/release/manualpages/Tao/TAOBMRM/

**Contents:**
- TAOBMRM#
- Options Database Keys#
- See Also#
- Level#
- Location#

bundle method for regularized risk minimization

- tao_bmrm_lambda - regulariser weight

Tao, TAONTR, TAONLS, TAOCG, TaoType, TaoCreate()

src/tao/unconstrained/impls/bmrm/bmrm.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

---

## TaoBNCGGetType#

**URL:** https://petsc.org/release/manualpages/Tao/TaoBNCGGetType/

**Contents:**
- TaoBNCGGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Return the type for the TAOBNCG solver

tao - the Tao solver context

Tao, TAOBNCG, TaoBNCGSetType(), TaoBNCGType

src/tao/bound/impls/bncg/bncg.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoBNCGGetType(Tao tao, TaoBNCGType *type)
```

Example 2 (unknown):
```unknown
TaoBNCGSetType()
```

Example 3 (unknown):
```unknown
TaoBNCGType
```

---

## TaoBNCGSetType#

**URL:** https://petsc.org/release/manualpages/Tao/TaoBNCGSetType/

**Contents:**
- TaoBNCGSetType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Set the type for the TAOBNCG solver

tao - the Tao solver context

Tao, TAOBNCG, TaoBNCGGetType(), TaoBNCGType

src/tao/bound/impls/bncg/bncg.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoBNCGSetType(Tao tao, TaoBNCGType type)
```

Example 2 (unknown):
```unknown
TaoBNCGGetType()
```

Example 3 (unknown):
```unknown
TaoBNCGType
```

---

## TaoBNCGType#

**URL:** https://petsc.org/release/manualpages/Tao/TaoBNCGType/

**Contents:**
- TaoBNCGType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Determine the conjugate gradient update formula used in the TAOBNCG algorithm.

TAO_BNCG_GD - basic gradient descent, no CG update

TAO_BNCG_PCGD - preconditioned/scaled gradient descent

TAO_BNCG_HS - Hestenes-Stiefel

TAO_BNCG_FR - Fletcher-Reeves

TAO_BNCG_PRP - Polak-Ribiere-Polyak (PRP)

TAO_BNCG_PRP_PLUS - Polak-Ribiere-Polyak “plus” (PRP+)

TAO_BNCG_DY - Dai-Yuan

TAO_BNCG_HZ - Hager-Zhang (CG_DESCENT 5.3)

TAO_BNCG_DK - Dai-Kou (2013)

TAO_BNCG_KD - Kou-Dai (2015)

TAO_BNCG_SSML_BFGS - Self-Scaling Memoryless BFGS (Perry-Shanno)

TAO_BNCG_SSML_DFP - Self-Scaling Memoryless DFP

TAO_BNCG_SSML_BRDN - Self-Scaling Memoryless (Symmetric) Broyden

Tao, TAOBNCG, TaoBNCGSetType(), TaoBNCGGetType()

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  TAO_BNCG_GD,
  TAO_BNCG_PCGD,
  TAO_BNCG_HS,
  TAO_BNCG_FR,
  TAO_BNCG_PRP,
  TAO_BNCG_PRP_PLUS,
  TAO_BNCG_DY,
  TAO_BNCG_HZ,
  TAO_BNCG_DK,
  TAO_BNCG_KD,
  TAO_BNCG_SSML_BFGS,
  TAO_BNCG_SSML_DFP,
  TAO_BNCG_SSML_BRDN
} TaoBNCGType;
```

Example 2 (unknown):
```unknown
TAO_BNCG_GD
```

Example 3 (unknown):
```unknown
TAO_BNCG_PCGD
```

Example 4 (unknown):
```unknown
TAO_BNCG_HS
```

---

## TAOBNCG#

**URL:** https://petsc.org/release/manualpages/Tao/TAOBNCG/

**Contents:**
- TAOBNCG#
- Options Database Keys#
- Note#
- CG formulas are#
- See Also#
- Level#
- Location#

Bound-constrained Nonlinear Conjugate Gradient method.

-tao_bncg_recycle - enable recycling the latest calculated gradient vector in subsequent TaoSolve() calls (currently disabled)

-tao_bncg_eta r - restart tolerance

-tao_bncg_type taocg_type - cg formula

-tao_bncg_as_type (none|bertsekas) - active set estimation method

-tao_bncg_as_tol r - tolerance used in Bertsekas active-set estimation

-tao_bncg_as_step r - trial step length used in Bertsekas active-set estimation

-tao_bncg_eps r - cutoff used for determining whether or not we restart based on steplength each iteration, as well as determining whether or not we continue using the last stepdirection. Defaults to machine precision.

-tao_bncg_theta r - convex combination parameter for the Broyden method

-tao_bncg_hz_eta r - cutoff tolerance for the beta term in the hz, dk methods

-tao_bncg_dk_eta r - cutoff tolerance for the beta term in the hz, dk methods

-tao_bncg_xi r - Multiplicative constant of the gamma term in the kd method

-tao_bncg_hz_theta r - Multiplicative constant of the theta term for the hz method

-tao_bncg_bfgs_scale r - Scaling parameter of the BFGS contribution to the scalar Broyden method

-tao_bncg_dfp_scale r - Scaling parameter of the dfp contribution to the scalar Broyden method

-tao_bncg_diag_scaling b - Whether or not to use diagonal initialization/preconditioning for the CG methods. Default True.

-tao_bncg_dynamic_restart b - use dynamic restart strategy in the hz, dk, kd methods

-tao_bncg_unscaled_restart b - whether or not to scale the gradient when doing gradient descent restarts

-tao_bncg_zeta r - Scaling parameter in the kd method

-tao_bncg_delta_min r - Minimum bound for rescaling during restarted gradient descent steps

-tao_bncg_delta_max r - Maximum bound for rescaling during restarted gradient descent steps

-tao_bncg_min_quad i - Number of quadratic-like steps in a row necessary to do a dynamic restart

-tao_bncg_min_restart_num i - This number, x, makes sure there is a gradient descent step every \(x*n\) iterations, where n is the dimension of the problem

-tao_bncg_spaced_restart (true|false) - whether or not to do gradient descent steps every x*n iterations

-tao_bncg_no_scaling b - If true, eliminates all scaling, including defaults.

-tao_bncg_neg_xi b - Whether or not to use negative xi in the kd method under certain conditions

gd - Gradient Descent

pr - Polak-Ribiere-Polyak

prp - Polak-Ribiere-Plus

hs - Hestenes-Steifel

ssml_bfgs - Self-Scaling Memoryless BFGS

ssml_dfp - Self-Scaling Memoryless DFP

ssml_brdn - Self-Scaling Memoryless Broyden

hz - Hager-Zhang (CG_DESCENT 5.3)

The various algorithmic factors can only be supplied via the options database

Tao, TAONTR, TAONTL, TAONM, TAOCG, TaoType, TaoCreate()

src/tao/bound/impls/bncg/bncg.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

---

## TAOBNK#

**URL:** https://petsc.org/release/manualpages/Tao/TAOBNK/

**Contents:**
- TAOBNK#
- Options Database Keys#
- See Also#
- Level#
- Location#

Shared base-type for Bounded Newton-Krylov type algorithms. At each iteration, the BNK methods solve the symmetric system of equations to obtain the step direction \(d_k\): \( H_k d_k = -g_k \) for free variables only. The step can be globalized either through trust-region methods, or a line search, or a heuristic mixture of both.

-tao_bnk_max_cg_its - maximum number of bounded conjugate-gradient iterations taken in each Newton loop

-tao_bnk_init_type - trust radius initialization method (“constant”, “direction”, “interpolation”)

-tao_bnk_update_type - trust radius update method (“step”, “direction”, “interpolation”)

-tao_bnk_as_type - active-set estimation method (“none”, “bertsekas”)

-tao_bnk_as_tol - (developer) initial tolerance used in estimating bounded active variables (-as_type bertsekas)

-tao_bnk_as_step - (developer) trial step length used in estimating bounded active variables (-as_type bertsekas)

-tao_bnk_sval - (developer) Hessian perturbation starting value

-tao_bnk_imin - (developer) minimum initial Hessian perturbation

-tao_bnk_imax - (developer) maximum initial Hessian perturbation

-tao_bnk_pmin - (developer) minimum Hessian perturbation

-tao_bnk_pmax - (developer) aximum Hessian perturbation

-tao_bnk_pgfac - (developer) Hessian perturbation growth factor

-tao_bnk_psfac - (developer) Hessian perturbation shrink factor

-tao_bnk_imfac - (developer) initial merit factor for Hessian perturbation

-tao_bnk_pmgfac - (developer) merit growth factor for Hessian perturbation

-tao_bnk_pmsfac - (developer) merit shrink factor for Hessian perturbation

-tao_bnk_eta1 - (developer) threshold for rejecting step (-update_type reduction)

-tao_bnk_eta2 - (developer) threshold for accepting marginal step (-update_type reduction)

-tao_bnk_eta3 - (developer) threshold for accepting reasonable step (-update_type reduction)

-tao_bnk_eta4 - (developer) threshold for accepting good step (-update_type reduction)

-tao_bnk_alpha1 - (developer) radius reduction factor for rejected step (-update_type reduction)

-tao_bnk_alpha2 - (developer) radius reduction factor for marginally accepted bad step (-update_type reduction)

-tao_bnk_alpha3 - (developer) radius increase factor for reasonable accepted step (-update_type reduction)

-tao_bnk_alpha4 - (developer) radius increase factor for good accepted step (-update_type reduction)

-tao_bnk_alpha5 - (developer) radius increase factor for very good accepted step (-update_type reduction)

-tao_bnk_epsilon - (developer) tolerance for small pred/actual ratios that trigger automatic step acceptance (-update_type reduction)

-tao_bnk_mu1 - (developer) threshold for accepting very good step (-update_type interpolation)

-tao_bnk_mu2 - (developer) threshold for accepting good step (-update_type interpolation)

-tao_bnk_gamma1 - (developer) radius reduction factor for rejected very bad step (-update_type interpolation)

-tao_bnk_gamma2 - (developer) radius reduction factor for rejected bad step (-update_type interpolation)

-tao_bnk_gamma3 - (developer) radius increase factor for accepted good step (-update_type interpolation)

-tao_bnk_gamma4 - (developer) radius increase factor for accepted very good step (-update_type interpolation)

-tao_bnk_theta - (developer) trust region interpolation factor (-update_type interpolation)

-tao_bnk_nu1 - (developer) threshold for small line-search step length (-update_type step)

-tao_bnk_nu2 - (developer) threshold for reasonable line-search step length (-update_type step)

-tao_bnk_nu3 - (developer) threshold for large line-search step length (-update_type step)

-tao_bnk_nu4 - (developer) threshold for very large line-search step length (-update_type step)

-tao_bnk_omega1 - (developer) radius reduction factor for very small line-search step length (-update_type step)

-tao_bnk_omega2 - (developer) radius reduction factor for small line-search step length (-update_type step)

-tao_bnk_omega3 - (developer) radius factor for decent line-search step length (-update_type step)

-tao_bnk_omega4 - (developer) radius increase factor for large line-search step length (-update_type step)

-tao_bnk_omega5 - (developer) radius increase factor for very large line-search step length (-update_type step)

-tao_bnk_mu1_i - (developer) threshold for accepting very good step (-init_type interpolation)

-tao_bnk_mu2_i - (developer) threshold for accepting good step (-init_type interpolation)

-tao_bnk_gamma1_i - (developer) radius reduction factor for rejected very bad step (-init_type interpolation)

-tao_bnk_gamma2_i - (developer) radius reduction factor for rejected bad step (-init_type interpolation)

-tao_bnk_gamma3_i - (developer) radius increase factor for accepted good step (-init_type interpolation)

-tao_bnk_gamma4_i - (developer) radius increase factor for accepted very good step (-init_type interpolation)

-tao_bnk_theta_i - (developer) trust region interpolation factor (-init_type interpolation)

The various algorithmic factors can only be supplied via the options database

Tao, TAONLS, TAONTL, TAONM, TaoType, TaoCreate()

src/tao/bound/impls/bnk/bnk.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

---

## TAOBNLS#

**URL:** https://petsc.org/release/manualpages/Tao/TAOBNLS/

**Contents:**
- TAOBNLS#
- Options Database Keys#
- See Also#
- Level#
- Location#

Bounded Newton Line Search for nonlinear minimization with bound constraints.

-tao_bnk_max_cg_its - maximum number of bounded conjugate-gradient iterations taken in each Newton loop

-tao_bnk_init_type - trust radius initialization method (“constant”, “direction”, “interpolation”)

-tao_bnk_update_type - trust radius update method (“step”, “direction”, “interpolation”)

-tao_bnk_as_type - active-set estimation method (“none”, “bertsekas”)

Tao, TAONTR, TAONTL, TAONM, TAOCG, TaoType, TaoCreate()

src/tao/bound/impls/bnk/bnls.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

---

## TAOBNTL#

**URL:** https://petsc.org/release/manualpages/Tao/TAOBNTL/

**Contents:**
- TAOBNTL#
- Options Database Keys#
- Developer Note#
- See Also#
- Level#
- Location#

Bounded Newton Trust Region method with line-search fall-back for nonlinear minimization with bound constraints.

-tao_bnk_max_cg_its - maximum number of bounded conjugate-gradient iterations taken in each Newton loop . -tao_bnk_init_type - trust radius initialization method (“constant”, “direction”, “interpolation”) . -tao_bnk_update_type - trust radius update method (“step”, “direction”, “interpolation”)

-tao_bnk_as_type - active-set estimation method (“none”, “bertsekas”)

One should control the maximum number of cg iterations through the standard -ksp_max_it option not with a special ad hoc option

Tao, TAONTR, TAONTL, TAONM, TAOCG, TaoType, TaoCreate()

src/tao/bound/impls/bnk/bntl.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
-ksp_max_it
```

Example 2 (unknown):
```unknown
TaoCreate()
```

---

## TAOBNTR#

**URL:** https://petsc.org/release/manualpages/Tao/TAOBNTR/

**Contents:**
- TAOBNTR#
- Options Database Keys#
- See Also#
- Level#
- Location#

Bounded Newton Trust Region for nonlinear minimization with bound constraints.

-tao_bnk_max_cg_its - maximum number of bounded conjugate-gradient iterations taken in each Newton loop

-tao_bnk_init_type - trust radius initialization method (“constant”, “direction”, “interpolation”)

-tao_bnk_update_type - trust radius update method (“step”, “direction”, “interpolation”)

-tao_bnk_as_type - active-set estimation method (“none”, “bertsekas”)

Tao, TAONTR, TAONTL, TAONM, TAOCG, TaoType, TaoCreate()

src/tao/bound/impls/bnk/bntr.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

---

## TaoBoundSolution#

**URL:** https://petsc.org/release/manualpages/Tao/TaoBoundSolution/

**Contents:**
- TaoBoundSolution#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#

Ensures that the solution vector is snapped into the bounds within a given tolerance.

XL - lower bound vector

XU - upper bound vector

bound_tol - absolute tolerance in enforcing the bound

nDiff - total number of vector entries that have been bounded

Xout - modified solution vector satisfying bounds to bound_tol

TAOBNCG, TAOBNTL, TAOBNTR, TaoBoundStep()

src/tao/bound/utils/isutil.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoBoundSolution(Vec X, Vec XL, Vec XU, PetscReal bound_tol, PetscInt *nDiff, Vec Xout)
```

Example 2 (unknown):
```unknown
TaoBoundStep()
```

---

## TaoBoundStep#

**URL:** https://petsc.org/release/manualpages/Tao/TaoBoundStep/

**Contents:**
- TaoBoundStep#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Ensures the correct zero or adjusted step direction values for active variables.

XL - lower bound vector

XU - upper bound vector

active_lower - index set for lower bounded active variables

active_upper - index set for lower bounded active variables

active_fixed - index set for fixed active variables

scale - amplification factor for the step that needs to be taken on actively bounded variables

S - step direction to be modified

TAOBNCG, TAOBNTL, TAOBNTR, TaoBoundSolution()

src/tao/bound/utils/isutil.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoBoundStep(Vec X, Vec XL, Vec XU, IS active_lower, IS active_upper, IS active_fixed, PetscReal scale, Vec S)
```

Example 2 (unknown):
```unknown
TaoBoundSolution()
```

---

## TAOBQNKLS#

**URL:** https://petsc.org/release/manualpages/Tao/TAOBQNKLS/

**Contents:**
- TAOBQNKLS#
- Notes#
- See Also#
- Level#
- Location#

Bounded Quasi-Newton-Krylov Line Search method for nonlinear minimization with bound constraints. This method approximates the Hessian-vector product using a limited-memory quasi-Newton formula, and iteratively inverts the Hessian with a Krylov solver. The quasi-Newton matrix and its settings can be accessed via the prefix -tao_bqnk_. For options database, see TAOBNK

The base class for this method is TAOBNK

The various algorithmic factors can only be supplied via the options database

Tao, TaoType, TAOBNK, TAOBQNKTR, TAOBQNKTL, TaoCreate()

src/tao/bound/impls/bqnk/bqnkls.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

---

## TAOBQNKTL#

**URL:** https://petsc.org/release/manualpages/Tao/TAOBQNKTL/

**Contents:**
- TAOBQNKTL#
- Notes#
- See Also#
- Level#
- Location#

Bounded Quasi-Newton-Krylov Trust-region with Line-search fallback, for nonlinear minimization with bound constraints. This method approximates the Hessian-vector product using a limited-memory quasi-Newton formula, and iteratively inverts the Hessian with a Krylov solver. The quasi-Newton matrix and its settings can be accessed via the prefix -tao_bqnk_. For options database, see TAOBNK

The base class for this method is TAOBNK

The various algorithmic factors can only be supplied via the options database

Tao, TAOBNK, TAONLS, TAONTL, TAONM, TaoType, TaoCreate(), TAOBQNKTR, TAOBQNKLS

src/tao/bound/impls/bqnk/bqnktl.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

---

## TAOBQNKTR#

**URL:** https://petsc.org/release/manualpages/Tao/TAOBQNKTR/

**Contents:**
- TAOBQNKTR#
- Notes#
- See Also#
- Level#
- Location#

Bounded Quasi-Newton-Krylov Trust Region method for nonlinear minimization with bound constraints. This method approximates the Hessian-vector product using a limited-memory quasi-Newton formula, and iteratively inverts the Hessian with a Krylov solver. The quasi-Newton matrix and its settings can be accessed via the prefix -tao_bqnk_. For options database, see TAOBNK

The base class for this method is TAOBNK

The various algorithmic factors can only be supplied via the options database

Tao, TAOBNK, TAONLS, TAONTL, TAONM, TaoType, TaoCreate(), TAOBQNKTR, TAOBQNKLS

src/tao/bound/impls/bqnk/bqnktr.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

---

## TAOBQNLS#

**URL:** https://petsc.org/release/manualpages/Tao/TAOBQNLS/

**Contents:**
- TAOBQNLS#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Bounded Quasi-Newton Line Search method for nonlinear minimization with bound constraints. This method approximates the action of the inverse-Hessian with a limited memory quasi-Newton formula. The quasi-Newton matrix and its options are accessible via the prefix -tao_bqnls_

-tao_bnk_max_cg_its - maximum number of bounded conjugate-gradient iterations taken in each Newton loop

-tao_bnk_as_type - active-set estimation method (“none”, “bertsekas”)

-tao_bnk_epsilon - (developer) tolerance for small pred/actual ratios that trigger automatic step acceptance

-tao_bnk_as_tol - (developer) initial tolerance used in estimating bounded active variables (-as_type bertsekas)

-tao_bnk_as_step - (developer) trial step length used in estimating bounded active variables (-as_type bertsekas)

The base class for this method is TAOBNK

The various algorithmic factors can only be supplied via the options database

Tao, TAOBNK, TAONLS, TAONTL, TAONM, TaoType, TaoCreate()

src/tao/bound/impls/bqnls/bqnls.c

src/ts/tutorials/ex20opt_p.c src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/tao/unconstrained/tutorials/rosenbrock3.c src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
-tao_bqnls_
```

Example 2 (unknown):
```unknown
TaoCreate()
```

---

## TAOBQPIP#

**URL:** https://petsc.org/release/manualpages/Tao/TAOBQPIP/

**Contents:**
- TAOBQPIP#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#
- Examples#

interior-point method for quadratic programs with box constraints.

-tao_bqpip_predcorr - use a predictor/corrector method

This algorithm solves quadratic problems only, the Hessian will only be computed once.

Tao, TaoType, TAOGPCG, TAOTRON

src/tao/quadratic/impls/bqpip/bqpip.c

src/tao/bound/tutorials/jbearing2.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

---

## TaoBRGNGetDampingVector#

**URL:** https://petsc.org/release/manualpages/Tao/TaoBRGNGetDampingVector/

**Contents:**
- TaoBRGNGetDampingVector#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get the damping vector \(\mathrm{diag}(J^T J)\) from a TAOBRGN with TAOBRGN_REGULARIZATION_LM regularization

tao - a Tao of type TAOBRGN with TAOBRGN_REGULARIZATION_LM regularization

d - the damping vector

TAO: Optimization Solvers, Tao, TAOBRGN, TaoBRGNRegularzationTypes

src/tao/leastsquares/impls/brgn/brgn.c

TaoBRGNGetDampingVector_BRGN() in src/tao/leastsquares/impls/brgn/brgn.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TAOBRGN_REGULARIZATION_LM
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoBRGNGetDampingVector(Tao tao, Vec *d)
```

Example 3 (unknown):
```unknown
TAOBRGN_REGULARIZATION_LM
```

Example 4 (unknown):
```unknown
TaoBRGNRegularzationTypes
```

---

## TaoBRGNGetRegularizationType#

**URL:** https://petsc.org/release/manualpages/Tao/TaoBRGNGetRegularizationType/

**Contents:**
- TaoBRGNGetRegularizationType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Get the TaoBRGNRegularizationType of a TAOBRGN

tao - a Tao of type TAOBRGN

type - the TaoBRGNRegularizationType

TAO: Optimization Solvers, Tao, TAOBRGN, TaoBRGNRegularizationType, TaoBRGNSetRegularizationType()

src/tao/leastsquares/impls/brgn/brgn.c

src/tao/leastsquares/tutorials/cs1.c

TaoBRGNGetRegularizationType_BRGN() in src/tao/leastsquares/impls/brgn/brgn.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoBRGNRegularizationType
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoBRGNGetRegularizationType(Tao tao, TaoBRGNRegularizationType *type)
```

Example 3 (unknown):
```unknown
TaoBRGNRegularizationType
```

Example 4 (unknown):
```unknown
TaoBRGNRegularizationType
```

---

## TaoBRGNGetSubsolver#

**URL:** https://petsc.org/release/manualpages/Tao/TaoBRGNGetSubsolver/

**Contents:**
- TaoBRGNGetSubsolver#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Get the pointer to the subsolver inside a TAOBRGN

tao - the Tao solver context

subsolver - the Tao sub-solver context

src/tao/leastsquares/impls/brgn/brgn.c

TaoBRGNGetSubsolver_BRGN() in src/tao/leastsquares/impls/brgn/brgn.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoBRGNGetSubsolver(Tao tao, Tao *subsolver)
```

---

## TaoBRGNRegularizationType#

**URL:** https://petsc.org/release/manualpages/Tao/TaoBRGNRegularizationType/

**Contents:**
- TaoBRGNRegularizationType#
- Synopsis#
- Values#
- Options database Key#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Examples#

The regularization added in the TAOBRGN solver.

TAOBRGN_REGULARIZATION_USER - A user-defined regularizer

TAOBRGN_REGULARIZATION_L2PROX - \(\tfrac{1}{2}\|x - x_k\|_2^\), where \(x_k\) is the latest solution

TAOBRGN_REGULARIZATION_L2PURE - \(\tfrac{1}{2}\|x\|_2^2\)

TAOBRGN_REGULARIZATION_L1DICT - \(\|D x\|_1\), where \(D\) is a dictionary matrix

TAOBRGN_REGULARIZATION_LM - Levenberg-Marquardt, \(\tfrac{1}{2} x^T \mathrm{diag}(J^T J) x\), where \(J\) is the Jacobian of the least-squares residual

-tao_brgn_regularization_type (l2prox|l2pure|l1dict|lm|user) - select one of the regularization types

If TAOBRGN_REGULARIZATION_USER, the regularizer is set either by calling TaoBRGNSetRegularizerObjectiveAndGradientRoutine() and TaoBRGNSetRegulazerHessianRoutine()

If TAOBRGN_REGULARIZATION_L1DICT, the dictionary matrix is set with TaoBRGNSetDictionaryMatrix() and the smoothing parameter of the approximate \(\ell_1\) norm is set with TaoBRGNSetL1SmoothEpsilon().

If TAOBRGN_REGULARIZATION_LM, the diagonal damping vector \(\mathrm{diag}(J^T J)\) can be obtained with TaoBRGNGetDampingVector().

TAO: Optimization Solvers, Tao, TaoBRGNGetSubsolver(), TaoBRGNSetRegularizerWeight(), TaoBRGNSetL1SmoothEpsilon(), TaoBRGNSetDictionaryMatrix(), TaoBRGNSetRegularizerObjectiveAndGradientRoutine(), TaoBRGNSetRegularizerHessianRoutine(), TaoBRGNGetRegularizationType(), TaoBRGNSetRegularizationType()

src/tao/leastsquares/tutorials/cs1.c

src/tao/leastsquares/tutorials/cs1.c

src/tao/leastsquares/tutorials/cs1.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  TAOBRGN_REGULARIZATION_USER,
  TAOBRGN_REGULARIZATION_L2PROX,
  TAOBRGN_REGULARIZATION_L2PURE,
  TAOBRGN_REGULARIZATION_L1DICT,
  TAOBRGN_REGULARIZATION_LM,
} TaoBRGNRegularizationType;
```

Example 2 (unknown):
```unknown
TAOBRGN_REGULARIZATION_USER
```

Example 3 (unknown):
```unknown
TaoBRGNSetRegularizerObjectiveAndGradientRoutine()
```

Example 4 (unknown):
```unknown
TaoBRGNSetRegulazerHessianRoutine()
```

---

## TaoBRGNSetDictionaryMatrix#

**URL:** https://petsc.org/release/manualpages/Tao/TaoBRGNSetDictionaryMatrix/

**Contents:**
- TaoBRGNSetDictionaryMatrix#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

bind the dictionary matrix from user application context to gn->D, for compressed sensing (with least-squares problem)

tao - the Tao context

dict - the user specified dictionary matrix. We allow to set a NULL dictionary, which means identity matrix by default

src/tao/leastsquares/impls/brgn/brgn.c

src/tao/leastsquares/tutorials/tomography.c src/tao/leastsquares/tutorials/cs1.c

TaoBRGNSetDictionaryMatrix_BRGN() in src/tao/leastsquares/impls/brgn/brgn.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoBRGNSetDictionaryMatrix(Tao tao, Mat dict)
```

---

## TaoBRGNSetL1SmoothEpsilon#

**URL:** https://petsc.org/release/manualpages/Tao/TaoBRGNSetL1SmoothEpsilon/

**Contents:**
- TaoBRGNSetL1SmoothEpsilon#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Set the L1-norm smooth approximation parameter for L1-regularized least-squares algorithm

tao - the Tao solver context

epsilon - L1-norm smooth approximation parameter

src/tao/leastsquares/impls/brgn/brgn.c

src/tao/leastsquares/tutorials/cs1.c

TaoBRGNSetL1SmoothEpsilon_BRGN() in src/tao/leastsquares/impls/brgn/brgn.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoBRGNSetL1SmoothEpsilon(Tao tao, PetscReal epsilon)
```

---

## TaoBRGNSetRegularizationType#

**URL:** https://petsc.org/release/manualpages/Tao/TaoBRGNSetRegularizationType/

**Contents:**
- TaoBRGNSetRegularizationType#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Set the TaoBRGNRegularizationType of a TAOBRGN

tao - a Tao of type TAOBRGN

type - the TaoBRGNRegularizationType

TAO: Optimization Solvers, Tao, TAOBRGN, TaoBRGNRegularizationType, TaoBRGNGetRegularizationType

src/tao/leastsquares/impls/brgn/brgn.c

src/tao/leastsquares/tutorials/cs1.c

TaoBRGNSetRegularizationType_BRGN() in src/tao/leastsquares/impls/brgn/brgn.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoBRGNRegularizationType
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoBRGNSetRegularizationType(Tao tao, TaoBRGNRegularizationType type)
```

Example 3 (unknown):
```unknown
TaoBRGNRegularizationType
```

Example 4 (unknown):
```unknown
TaoBRGNRegularizationType
```

---

## TaoBRGNSetRegularizerHessianRoutine#

**URL:** https://petsc.org/release/manualpages/Tao/TaoBRGNSetRegularizerHessianRoutine/

**Contents:**
- TaoBRGNSetRegularizerHessianRoutine#
- Synopsis#
- Input Parameters#
- Calling sequence#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets the user-defined regularizer call-back function into the algorithm.

tao - the Tao context

Hreg - user-created matrix for the Hessian of the regularization term

func - function pointer for the regularizer Hessian evaluation

ctx - application context for the regularizer Hessian

tao - the Tao context

u - the location at which to compute the Hessian

Hreg - user-created matrix for the Hessian of the regularization term

ctx - application context for the regularizer Hessian

src/tao/leastsquares/impls/brgn/brgn.c

src/tao/leastsquares/tutorials/tomography.c

TaoBRGNSetRegularizerHessianRoutine_BRGN(Tao tao, Mat Hreg, PetscErrorCode (*func)() in src/tao/leastsquares/impls/brgn/brgn.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoBRGNSetRegularizerHessianRoutine(Tao tao, Mat Hreg, PetscErrorCode (*func)(Tao tao, Vec u, Mat Hreg, PetscCtx ctx), PetscCtx ctx)
```

---

## TaoBRGNSetRegularizerObjectiveAndGradientRoutine#

**URL:** https://petsc.org/release/manualpages/Tao/TaoBRGNSetRegularizerObjectiveAndGradientRoutine/

**Contents:**
- TaoBRGNSetRegularizerObjectiveAndGradientRoutine#
- Synopsis#
- Input Parameters#
- Calling sequence#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets the user-defined regularizer call-back function into the algorithm.

tao - the Tao context

func - function pointer for the regularizer value and gradient evaluation

ctx - application context for the regularizer

tao - the Tao context

u - the location at which to compute the objective and gradient

val - location to store objective function value

g - location to store gradient

ctx - application context for the regularizer Hessian

src/tao/leastsquares/impls/brgn/brgn.c

src/tao/leastsquares/tutorials/tomography.c

TaoBRGNSetRegularizerObjectiveAndGradientRoutine_BRGN(Tao tao, PetscErrorCode (*func)() in src/tao/leastsquares/impls/brgn/brgn.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoBRGNSetRegularizerObjectiveAndGradientRoutine(Tao tao, PetscErrorCode (*func)(Tao tao, Vec u, PetscReal *val, Vec g, PetscCtx ctx), PetscCtx ctx)
```

---

## TaoBRGNSetRegularizerWeight#

**URL:** https://petsc.org/release/manualpages/Tao/TaoBRGNSetRegularizerWeight/

**Contents:**
- TaoBRGNSetRegularizerWeight#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Set the regularizer weight for the Gauss-Newton least-squares algorithm

tao - the Tao solver context

lambda - L1-norm regularizer weight

src/tao/leastsquares/impls/brgn/brgn.c

src/tao/leastsquares/tutorials/cs1.c

TaoBRGNSetRegularizerWeight_BRGN() in src/tao/leastsquares/impls/brgn/brgn.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoBRGNSetRegularizerWeight(Tao tao, PetscReal lambda)
```

---

## TAOBRGN#

**URL:** https://petsc.org/release/manualpages/Tao/TAOBRGN/

**Contents:**
- TAOBRGN#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#

Bounded Regularized Gauss-Newton method for solving nonlinear least-squares problems with bound constraints. This algorithm is a thin wrapper around TAOBNTL that constructs the Gauss-Newton problem with the user-provided least-squares residual and Jacobian. The algorithm offers an L2-norm (l2pure), L2-norm proximal point (l2prox) regularizer, and L1-norm dictionary regularizer (l1dict), where we approximate the L1-norm \(\|x\|_1\) by \(\sum_i{\sqrt{x_i^2+\epsilon^2}-\epsilon}\) with a small positive number \(\epsilon\). Also offered is the lm regularizer which uses a scaled diagonal of \(J^T J\). With the lm regularizer, TAOBRGN is a Levenberg-Marquardt optimizer. The user can also provide their own regularization function.

-tao_brgn_regularization_type (user|l2prox|l2pure|l1dict|lm) - regularization type, default l2prox

-tao_brgn_regularizer_weight - regularizer weight (default 1e-4)

-tao_brgn_l1_smooth_epsilon - L1-norm smooth approximation parameter: \(\|x\|_1 = \sum_i{\sqrt{x_i^2+\epsilon^2}-\epsilon}\) (default 1e-6)

Tao, TaoBRGNGetSubsolver(), TaoBRGNSetRegularizerWeight(), TaoBRGNSetL1SmoothEpsilon(), TaoBRGNSetDictionaryMatrix(), TaoBRGNSetRegularizerObjectiveAndGradientRoutine(), TaoBRGNSetRegularizerHessianRoutine()

src/tao/leastsquares/impls/brgn/brgn.c

src/tao/leastsquares/tutorials/tomography.c src/tao/leastsquares/tutorials/cs1.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoBRGNGetSubsolver()
```

Example 2 (unknown):
```unknown
TaoBRGNSetRegularizerWeight()
```

Example 3 (unknown):
```unknown
TaoBRGNSetL1SmoothEpsilon()
```

Example 4 (unknown):
```unknown
TaoBRGNSetDictionaryMatrix()
```

---

## TAOCG#

**URL:** https://petsc.org/release/manualpages/Tao/TAOCG/

**Contents:**
- TAOCG#
- Options Database Keys#
- Note#
- The cg formulas are#
- See Also#
- Level#
- Location#
- Examples#

Nonlinear conjugate gradient method is an extension of the nonlinear conjugate gradient solver for nonlinear optimization.

-tao_cg_eta r - restart tolerance

-tao_cg_type taocg_type - cg formula, one of fr, pr, prp, hs, dy

-tao_cg_delta_min r - minimum delta value

-tao_cg_delta_max r - maximum delta value

prp - Polak-Ribiere-Plus

hs - Hestenes-Steifel

Tao, TAONTR, TAONLS, TaoType, TaoCreate()

src/tao/unconstrained/impls/cg/taocg.c

src/tao/unconstrained/tutorials/minsurf2.c src/tao/unconstrained/tutorials/eptorsion2f.F90 src/tao/unconstrained/tutorials/eptorsion2.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

---

## TaoComputeConstraints#

**URL:** https://petsc.org/release/manualpages/Tao/TaoComputeConstraints/

**Contents:**
- TaoComputeConstraints#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Compute the variable bounds using the routine set by TaoSetConstraintsRoutine().

tao - the Tao context

X - location to evaluate the constraints

TAO: Optimization Solvers, Tao, TaoSetConstraintsRoutine(), TaoComputeJacobian()

src/tao/interface/taosolver_bounds.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoSetConstraintsRoutine()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoComputeConstraints(Tao tao, Vec X, Vec C)
```

Example 3 (unknown):
```unknown
TaoSetConstraintsRoutine()
```

Example 4 (unknown):
```unknown
TaoComputeJacobian()
```

---

## TaoComputeDualVariables#

**URL:** https://petsc.org/release/manualpages/Tao/TaoComputeDualVariables/

**Contents:**
- TaoComputeDualVariables#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Computes the dual vectors corresponding to the bounds of the variables

tao - the Tao context

DL - dual variable vector for the lower bounds

DU - dual variable vector for the upper bounds

DL and DU should be created before calling this routine. If calling this routine after using an unconstrained solver, DL and DU are set to all zeros.

TAO: Optimization Solvers, Tao, TaoComputeObjective(), TaoSetVariableBounds()

src/tao/interface/taosolver_bounds.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoComputeDualVariables(Tao tao, Vec DL, Vec DU)
```

Example 2 (unknown):
```unknown
TaoComputeObjective()
```

Example 3 (unknown):
```unknown
TaoSetVariableBounds()
```

---

## TaoComputeEqualityConstraints#

**URL:** https://petsc.org/release/manualpages/Tao/TaoComputeEqualityConstraints/

**Contents:**
- TaoComputeEqualityConstraints#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Compute the variable bounds using the routine set by TaoSetEqualityConstraintsRoutine().

tao - the Tao context

X - point the equality constraints were evaluated on

CE - vector of equality constraints evaluated at X

TAO: Optimization Solvers, Tao, TaoSetEqualityConstraintsRoutine(), TaoComputeJacobianEquality(), TaoComputeInequalityConstraints()

src/tao/interface/taosolver_bounds.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoSetEqualityConstraintsRoutine()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoComputeEqualityConstraints(Tao tao, Vec X, Vec CE)
```

Example 3 (unknown):
```unknown
TaoSetEqualityConstraintsRoutine()
```

Example 4 (unknown):
```unknown
TaoComputeJacobianEquality()
```

---

## TaoComputeGradient#

**URL:** https://petsc.org/release/manualpages/Tao/TaoComputeGradient/

**Contents:**
- TaoComputeGradient#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Computes the gradient of the objective function

tao - the Tao context

-tao_test_gradient - compare the user provided gradient with one compute via finite differences to check for errors

-tao_test_gradient_view - display the user provided gradient, the finite difference gradient and the difference between them to help users detect the location of errors in the user provided gradient

TaoComputeGradient() is typically used within the implementation of the optimization method, so most users would not generally call this routine themselves.

TAO: Optimization Solvers, TaoComputeObjective(), TaoComputeObjectiveAndGradient(), TaoSetGradient()

src/tao/interface/taosolver_fg.c

src/tao/tutorials/ex4.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoComputeGradient(Tao tao, Vec X, Vec G)
```

Example 2 (unknown):
```unknown
TaoComputeGradient()
```

Example 3 (unknown):
```unknown
TaoComputeObjective()
```

Example 4 (unknown):
```unknown
TaoComputeObjectiveAndGradient()
```

---

## TaoComputeHessian#

**URL:** https://petsc.org/release/manualpages/Tao/TaoComputeHessian/

**Contents:**
- TaoComputeHessian#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Options Database Keys#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#

Computes the Hessian matrix that has been set with TaoSetHessian().

tao - the Tao solver context

Hpre - matrix used to construct the preconditioner, usually the same as H

-tao_test_hessian - compare the user provided Hessian with one compute via finite differences to check for errors

-tao_test_hessian numerical value - display entries in the difference between the user provided Hessian and finite difference Hessian that are greater than a certain value to help users detect errors

-tao_test_hessian_view - display the user provided Hessian, the finite difference Hessian and the difference between them to help users detect the location of errors in the user provided Hessian

Most users should not need to explicitly call this routine, as it is used internally within the minimization solvers.

TaoComputeHessian() is typically used within optimization algorithms, so most users would not generally call this routine themselves.

The Hessian test mechanism follows SNESTestJacobian().

If there is no separate preconditioning matrix, TaoComputeHessian(tao, X, H, NULL) and TaoComputeHessian(tao, X, H, H) are equivalent.

TAO: Optimization Solvers, Tao, TaoComputeObjective(), TaoComputeObjectiveAndGradient(), TaoSetHessian()

src/tao/interface/taosolver_hj.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoSetHessian()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoComputeHessian(Tao tao, Vec X, Mat H, Mat Hpre)
```

Example 3 (unknown):
```unknown
TaoComputeHessian()
```

Example 4 (unknown):
```unknown
SNESTestJacobian()
```

---

## TaoComputeInequalityConstraints#

**URL:** https://petsc.org/release/manualpages/Tao/TaoComputeInequalityConstraints/

**Contents:**
- TaoComputeInequalityConstraints#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Compute the variable bounds using the routine set by TaoSetInequalityConstraintsRoutine().

tao - the Tao context

X - point the inequality constraints were evaluated on

CI - vector of inequality constraints evaluated at X

TAO: Optimization Solvers, Tao, TaoSetInequalityConstraintsRoutine(), TaoComputeJacobianInequality(), TaoComputeEqualityConstraints()

src/tao/interface/taosolver_bounds.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoSetInequalityConstraintsRoutine()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoComputeInequalityConstraints(Tao tao, Vec X, Vec CI)
```

Example 3 (unknown):
```unknown
TaoSetInequalityConstraintsRoutine()
```

Example 4 (unknown):
```unknown
TaoComputeJacobianInequality()
```

---

## TaoComputeJacobianDesign#

**URL:** https://petsc.org/release/manualpages/Tao/TaoComputeJacobianDesign/

**Contents:**
- TaoComputeJacobianDesign#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Computes the Jacobian matrix that has been set with TaoSetJacobianDesignRoutine().

tao - the Tao solver context

Most users should not need to explicitly call this routine, as it is used internally within the optimization algorithms.

TAO: Optimization Solvers, Tao, TaoComputeObjective(), TaoComputeObjectiveAndGradient(), TaoSetJacobianDesignRoutine(), TaoSetStateDesignIS()

src/tao/interface/taosolver_hj.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoSetJacobianDesignRoutine()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoComputeJacobianDesign(Tao tao, Vec X, Mat J)
```

Example 3 (unknown):
```unknown
TaoComputeObjective()
```

Example 4 (unknown):
```unknown
TaoComputeObjectiveAndGradient()
```

---

## TaoComputeJacobianEquality#

**URL:** https://petsc.org/release/manualpages/Tao/TaoComputeJacobianEquality/

**Contents:**
- TaoComputeJacobianEquality#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Computes the Jacobian matrix that has been set with TaoSetJacobianEqualityRoutine().

tao - the Tao solver context

Jpre - matrix used to construct the preconditioner, often the same as J

Most users should not need to explicitly call this routine, as it is used internally within the optimization algorithms.

TAO: Optimization Solvers, TaoComputeObjective(), TaoComputeObjectiveAndGradient(), TaoSetJacobianStateRoutine(), TaoComputeJacobianDesign(), TaoSetStateDesignIS()

src/tao/interface/taosolver_hj.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoSetJacobianEqualityRoutine()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoComputeJacobianEquality(Tao tao, Vec X, Mat J, Mat Jpre)
```

Example 3 (unknown):
```unknown
TaoComputeObjective()
```

Example 4 (unknown):
```unknown
TaoComputeObjectiveAndGradient()
```

---

## TaoComputeJacobianInequality#

**URL:** https://petsc.org/release/manualpages/Tao/TaoComputeJacobianInequality/

**Contents:**
- TaoComputeJacobianInequality#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Computes the Jacobian matrix that has been set with TaoSetJacobianInequalityRoutine().

tao - the Tao solver context

Jpre - matrix used to construct the preconditioner

Most users should not need to explicitly call this routine, as it is used internally within the minimization solvers.

TAO: Optimization Solvers, Tao, TaoComputeObjective(), TaoComputeObjectiveAndGradient(), TaoSetJacobianStateRoutine(), TaoComputeJacobianDesign(), TaoSetStateDesignIS()

src/tao/interface/taosolver_hj.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoSetJacobianInequalityRoutine()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoComputeJacobianInequality(Tao tao, Vec X, Mat J, Mat Jpre)
```

Example 3 (unknown):
```unknown
TaoComputeObjective()
```

Example 4 (unknown):
```unknown
TaoComputeObjectiveAndGradient()
```

---

## TaoComputeJacobianState#

**URL:** https://petsc.org/release/manualpages/Tao/TaoComputeJacobianState/

**Contents:**
- TaoComputeJacobianState#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Computes the Jacobian matrix that has been set with TaoSetJacobianStateRoutine().

tao - the Tao solver context

Jpre - matrix used to construct the preconditioner, often the same as J

Most users should not need to explicitly call this routine, as it is used internally within the optimization algorithms.

TAO: Optimization Solvers, Tao, TaoComputeObjective(), TaoComputeObjectiveAndGradient(), TaoSetJacobianStateRoutine(), TaoComputeJacobianDesign(), TaoSetStateDesignIS()

src/tao/interface/taosolver_hj.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoSetJacobianStateRoutine()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoComputeJacobianState(Tao tao, Vec X, Mat J, Mat Jpre, Mat Jinv)
```

Example 3 (unknown):
```unknown
TaoComputeObjective()
```

Example 4 (unknown):
```unknown
TaoComputeObjectiveAndGradient()
```

---

## TaoComputeJacobian#

**URL:** https://petsc.org/release/manualpages/Tao/TaoComputeJacobian/

**Contents:**
- TaoComputeJacobian#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Computes the Jacobian matrix that has been set with TaoSetJacobianRoutine().

tao - the Tao solver context

Jpre - matrix used to compute the preconditioner, often the same as J

Most users should not need to explicitly call this routine, as it is used internally within the minimization solvers.

TaoComputeJacobian() is typically used within minimization implementations, so most users would not generally call this routine themselves.

TAO: Optimization Solvers, TaoComputeObjective(), TaoComputeObjectiveAndGradient(), TaoSetJacobianRoutine()

src/tao/interface/taosolver_hj.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoComputeJacobian(Tao tao, Vec X, Mat J, Mat Jpre)
```

Example 2 (unknown):
```unknown
TaoComputeJacobian()
```

Example 3 (unknown):
```unknown
TaoComputeObjective()
```

Example 4 (unknown):
```unknown
TaoComputeObjectiveAndGradient()
```

---

## TaoComputeObjectiveAndGradient#

**URL:** https://petsc.org/release/manualpages/Tao/TaoComputeObjectiveAndGradient/

**Contents:**
- TaoComputeObjectiveAndGradient#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Computes the objective function value at a given point

tao - the Tao context

f - Objective value at X

G - Gradient vector at X

TaoComputeObjectiveAndGradient() is typically used within the implementation of the optimization algorithm, so most users would not generally call this routine themselves.

TAO: Optimization Solvers, TaoComputeGradient(), TaoSetObjective()

src/tao/interface/taosolver_fg.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoComputeObjectiveAndGradient(Tao tao, Vec X, PetscReal *f, Vec G)
```

Example 2 (unknown):
```unknown
TaoComputeObjectiveAndGradient()
```

Example 3 (unknown):
```unknown
TaoComputeGradient()
```

Example 4 (unknown):
```unknown
TaoSetObjective()
```

---

## TaoComputeObjective#

**URL:** https://petsc.org/release/manualpages/Tao/TaoComputeObjective/

**Contents:**
- TaoComputeObjective#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Computes the objective function value at a given point

tao - the Tao context

f - Objective value at X

TaoComputeObjective() is typically used within the implementation of the optimization algorithm so most users would not generally call this routine themselves.

TAO: Optimization Solvers, Tao, TaoComputeGradient(), TaoComputeObjectiveAndGradient(), TaoSetObjective()

src/tao/interface/taosolver_fg.c

src/tao/tutorials/ex4.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoComputeObjective(Tao tao, Vec X, PetscReal *f)
```

Example 2 (unknown):
```unknown
TaoComputeObjective()
```

Example 3 (unknown):
```unknown
TaoComputeGradient()
```

Example 4 (unknown):
```unknown
TaoComputeObjectiveAndGradient()
```

---

## TaoComputeResidualJacobian#

**URL:** https://petsc.org/release/manualpages/Tao/TaoComputeResidualJacobian/

**Contents:**
- TaoComputeResidualJacobian#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Computes the least-squares residual Jacobian matrix that has been set with TaoSetJacobianResidual().

tao - the Tao solver context

Jpre - matrix used to compute the preconditioner, often the same as J

Most users should not need to explicitly call this routine, as it is used internally within the minimization solvers.

TaoComputeResidualJacobian() is typically used within least-squares implementations, so most users would not generally call this routine themselves.

TAO: Optimization Solvers, Tao, TaoComputeResidual(), TaoSetJacobianResidual()

src/tao/interface/taosolver_hj.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoSetJacobianResidual()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoComputeResidualJacobian(Tao tao, Vec X, Mat J, Mat Jpre)
```

Example 3 (unknown):
```unknown
TaoComputeResidualJacobian()
```

Example 4 (unknown):
```unknown
TaoComputeResidual()
```

---

## TaoComputeResidual#

**URL:** https://petsc.org/release/manualpages/Tao/TaoComputeResidual/

**Contents:**
- TaoComputeResidual#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Computes a least-squares residual vector at a given point

tao - the Tao context

F - Objective vector at X

TaoComputeResidual() is typically used within the implementation of the optimization algorithm, so most users would not generally call this routine themselves.

TAO: Optimization Solvers, Tao, TaoSetResidualRoutine()

src/tao/interface/taosolver_fg.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoComputeResidual(Tao tao, Vec X, Vec F)
```

Example 2 (unknown):
```unknown
TaoComputeResidual()
```

Example 3 (unknown):
```unknown
TaoSetResidualRoutine()
```

---

## TaoComputeVariableBounds#

**URL:** https://petsc.org/release/manualpages/Tao/TaoComputeVariableBounds/

**Contents:**
- TaoComputeVariableBounds#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#

Compute the variable bounds using the routine set by TaoSetVariableBoundsRoutine().

tao - the Tao context

TAO: Optimization Solvers, Tao, TaoSetVariableBoundsRoutine(), TaoSetVariableBounds()

src/tao/interface/taosolver_bounds.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoSetVariableBoundsRoutine()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoComputeVariableBounds(Tao tao)
```

Example 3 (unknown):
```unknown
TaoSetVariableBoundsRoutine()
```

Example 4 (unknown):
```unknown
TaoSetVariableBounds()
```

---

## TaoConvergedReason#

**URL:** https://petsc.org/release/manualpages/Tao/TaoConvergedReason/

**Contents:**
- TaoConvergedReason#
- Synopsis#
- Values#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#
- Examples#

reason a Tao optimizer was said to have converged or diverged

TAO_CONVERGED_GATOL - \(||g(X)|| < gatol\)

TAO_CONVERGED_GRTOL - \(||g(X)|| / f(X) < grtol\)

TAO_CONVERGED_GTTOL - \(||g(X)|| / ||g(X0)|| < gttol\)

TAO_CONVERGED_STEPTOL - step size smaller than tolerance

TAO_CONVERGED_MINF - \(F < F_min\)

TAO_CONVERGED_USER - the user indicates the optimization has succeeded

TAO_DIVERGED_MAXITS - the maximum number of iterations allowed has been achieved

TAO_DIVERGED_NAN - not a number appeared in the computations

TAO_DIVERGED_MAXFCN - the maximum number of function evaluations has been computed

TAO_DIVERGED_LS_FAILURE - a linesearch failed

TAO_DIVERGED_TR_REDUCTION - trust region failure

TAO_DIVERGED_USER - the user has indicated the optimization has failed

TAO_CONTINUE_ITERATING - the optimization is still running, TaoSolve()

f(X) - current function value

f(X) -* true solution (estimated)

g(X) - current gradient

its - current iterate number

maxits - maximum number of iterates

fevals - number of function evaluations

max_funcsals - maximum number of function evaluations

The two most common reasons for divergence are an incorrectly coded or computed gradient or Hessian failure or lack of convergence in the linear system solve (in this case we recommend testing with -pc_type lu to eliminate the linear solver as the cause of the problem).

The names in KSPConvergedReason, SNESConvergedReason, and TaoConvergedReason should be uniformized

TAO: Optimization Solvers, Tao, TaoSolve(), TaoGetConvergedReason(), KSPConvergedReason, SNESConvergedReason

src/tao/unconstrained/tutorials/rosenbrock3.c src/tao/unconstrained/tutorials/rosenbrock2.c

src/tao/bound/tutorials/jbearing2.c src/tao/unconstrained/tutorials/eptorsion2f.F90

src/tao/leastsquares/tutorials/chwirut1f.F90 src/tao/bound/tutorials/jbearing2.c src/tao/unconstrained/tutorials/rosenbrock2.c src/tao/unconstrained/tutorials/eptorsion2f.F90 src/tao/constrained/tutorials/maros.c src/tao/unconstrained/tutorials/rosenbrock3.c src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {               /* converged */
  TAO_CONVERGED_GATOL   = 3, /* ||g(X)|| < gatol */
  TAO_CONVERGED_GRTOL   = 4, /* ||g(X)|| / f(X)  < grtol */
  TAO_CONVERGED_GTTOL   = 5, /* ||g(X)|| / ||g(X0)|| < gttol */
  TAO_CONVERGED_STEPTOL = 6, /* step size small */
  TAO_CONVERGED_MINF    = 7, /* F < F_min */
  TAO_CONVERGED_USER    = 8, /* User defined */
  /* diverged */
  TAO_DIVERGED_MAXITS       = -2,
  TAO_DIVERGED_NAN          = -4,
  TAO_DIVERGED_MAXFCN       = -5,
  TAO_DIVERGED_LS_FAILURE   = -6,
  TAO_DIVERGED_TR_REDUCTION = -7,
  TAO_DIVERGED_USER         = -8, /* User defined */
  /* keep going */
  TAO_CONTINUE_ITERATING = 0
} TaoConvergedReason;
```

Example 2 (unknown):
```unknown
TAO_CONVERGED_GATOL
```

Example 3 (unknown):
```unknown
TAO_CONVERGED_GRTOL
```

Example 4 (unknown):
```unknown
TAO_CONVERGED_GTTOL
```

---

## TaoCreate#

**URL:** https://petsc.org/release/manualpages/Tao/TaoCreate/

**Contents:**
- TaoCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

comm - MPI communicator

newtao - the new Tao context

-tao_type - select which method Tao should use

TAO: Optimization Solvers, Tao, TaoSolve(), TaoDestroy(), TaoSetFromOptions(), TaoSetType()

src/tao/interface/taosolver.c

src/tao/leastsquares/tutorials/chwirut1f.F90 src/tao/leastsquares/tutorials/chwirut2f.F90 src/tao/leastsquares/tutorials/cs1.c src/tao/pde_constrained/tutorials/elliptic.c src/tao/constrained/tutorials/tomographyADMM.c src/tao/pde_constrained/tutorials/parabolic.c src/tao/constrained/tutorials/ex1.c src/tao/pde_constrained/tutorials/hyperbolic.c src/tao/constrained/tutorials/maros.c src/tao/leastsquares/tutorials/chwirut1.c

TaoCreate_BLMVM() in src/tao/bound/impls/blmvm/blmvm.c TaoCreate_BNCG() in src/tao/bound/impls/bncg/bncg.c TaoCreate_BNK() in src/tao/bound/impls/bnk/bnk.c TaoCreate_BNLS() in src/tao/bound/impls/bnk/bnls.c TaoCreate_BNTL() in src/tao/bound/impls/bnk/bntl.c TaoCreate_BNTR() in src/tao/bound/impls/bnk/bntr.c TaoCreate_BQNK() in src/tao/bound/impls/bqnk/bqnk.c TaoCreate_BQNKLS() in src/tao/bound/impls/bqnk/bqnkls.c TaoCreate_BQNKTL() in src/tao/bound/impls/bqnk/bqnktl.c TaoCreate_BQNKTR() in src/tao/bound/impls/bqnk/bqnktr.c TaoCreate_BQNLS() in src/tao/bound/impls/bqnls/bqnls.c TaoCreate_TRON() in src/tao/bound/impls/tron/tron.c TaoCreate_ASFLS() in src/tao/complementarity/impls/asls/asfls.c TaoCreate_ASILS() in src/tao/complementarity/impls/asls/asils.c TaoCreate_SSFLS() in src/tao/complementarity/impls/ssls/ssfls.c TaoCreate_SSILS() in src/tao/complementarity/impls/ssls/ssils.c TaoCreate_ADMM() in src/tao/constrained/impls/admm/admm.c TaoCreate_ALMM() in src/tao/constrained/impls/almm/almm.c TaoCreate_IPM() in src/tao/constrained/impls/ipm/ipm.c TaoCreate_PDIPM() in src/tao/constrained/impls/ipm/pdipm.c TaoCreate_BRGN() in src/tao/leastsquares/impls/brgn/brgn.c TaoCreate_POUNDERS() in src/tao/leastsquares/impls/pounders/pounders.c TaoCreate_LCL() in src/tao/pde_constrained/impls/lcl/lcl.c TaoCreate_BQPIP() in src/tao/quadratic/impls/bqpip/bqpip.c TaoCreate_GPCG() in src/tao/quadratic/impls/gpcg/gpcg.c TaoCreate_BMRM() in src/tao/unconstrained/impls/bmrm/bmrm.c TaoCreate_CG() in src/tao/unconstrained/impls/cg/taocg.c TaoCreate_LMVM() in src/tao/unconstrained/impls/lmvm/lmvm.c TaoCreate_NM() in src/tao/unconstrained/impls/neldermead/neldermead.c TaoCreate_NLS() in src/tao/unconstrained/impls/nls/nls.c TaoCreate_NTL() in src/tao/unconstrained/impls/ntl/ntl.c TaoCreate_NTR() in src/tao/unconstrained/impls/ntr/ntr.c TaoCreate_OWLQN() in src/tao/unconstrained/impls/owlqn/owlqn.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoCreate(MPI_Comm comm, Tao *newtao)
```

Example 2 (unknown):
```unknown
TaoDestroy()
```

Example 3 (unknown):
```unknown
TaoSetFromOptions()
```

Example 4 (unknown):
```unknown
TaoSetType()
```

---

## TaoDefaultComputeGradient#

**URL:** https://petsc.org/release/manualpages/Tao/TaoDefaultComputeGradient/

**Contents:**
- TaoDefaultComputeGradient#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#

computes the gradient using finite differences.

tao - the Tao context

Xin - compute gradient at this point

-tao_fd_gradient - activates TaoDefaultComputeGradient()

-tao_fd_delta delta - change in X used to calculate finite differences

This routine is slow and expensive, and is not optimized to take advantage of sparsity in the problem. Although not recommended for general use in large-scale applications, it can be useful in checking the correctness of a user-provided gradient using the command-line option -tao_test_gradient This finite difference gradient evaluation can be set using the routine TaoSetGradient() or by using the command line option -tao_fd_gradient

Tao, TaoSetGradient(), TaoTermComputeGradientFD()

src/tao/interface/fdiff.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h"  
PetscErrorCode TaoDefaultComputeGradient(Tao tao, Vec Xin, Vec G, void *dummy)
```

Example 2 (unknown):
```unknown
-tao_test_gradient
```

Example 3 (unknown):
```unknown
TaoSetGradient()
```

Example 4 (unknown):
```unknown
TaoSetGradient()
```

---

## TaoDefaultComputeHessianColor#

**URL:** https://petsc.org/release/manualpages/Tao/TaoDefaultComputeHessianColor/

**Contents:**
- TaoDefaultComputeHessianColor#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#

Computes the Hessian using colored finite differences.

tao - the Tao context

V - compute Hessian at this point

ctx - the color object of type MatFDColoring

H - Hessian matrix (not altered in this routine)

B - newly computed Hessian matrix to use with preconditioner (generally the same as H)

Tao, MatColoring, TaoSetHessian(), TaoDefaultComputeHessian(), SNESComputeJacobianDefaultColor(), TaoSetGradient()

src/tao/interface/fdiff.c

src/tao/unconstrained/tutorials/minsurf2.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h"  
PetscErrorCode TaoDefaultComputeHessianColor(Tao tao, Vec V, Mat H, Mat B, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
MatFDColoring
```

Example 3 (unknown):
```unknown
MatColoring
```

Example 4 (unknown):
```unknown
TaoSetHessian()
```

---

## TaoDefaultComputeHessianMFFD#

**URL:** https://petsc.org/release/manualpages/Tao/TaoDefaultComputeHessianMFFD/

**Contents:**
- TaoDefaultComputeHessianMFFD#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Computes the Hessian using finite differences with MATMFFD.

tao - the Tao context

X - compute Hessian at this point

H - Hessian matrix of type MATMFFD

B - should be NULL or equal to H

This can be passed to TaoSetHessian() to use MATMFFD for approximate Hessian-vector products. The matrix H can originate from MatCreateMFFD() or from TaoTermCreateHessianMFFD().

Tao, MATMFFD, MatCreateMFFD(), TaoTermCreateHessianMFFD()

src/tao/interface/fdiff.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h"  
PetscErrorCode TaoDefaultComputeHessianMFFD(Tao tao, Vec X, Mat H, Mat B, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoSetHessian()
```

Example 3 (unknown):
```unknown
MatCreateMFFD()
```

Example 4 (unknown):
```unknown
TaoTermCreateHessianMFFD()
```

---

## TaoDefaultComputeHessian#

**URL:** https://petsc.org/release/manualpages/Tao/TaoDefaultComputeHessian/

**Contents:**
- TaoDefaultComputeHessian#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Computes the Hessian using finite differences.

tao - the Tao context

V - compute Hessian at this point

H - Hessian matrix (not altered in this routine)

B - newly computed Hessian matrix to use with preconditioner (generally the same as H)

-tao_fd_hessian - activates TaoDefaultComputeHessian()

This routine is slow and expensive, and is not optimized to take advantage of sparsity in the problem. Although it is not recommended for general use in large-scale applications, It can be useful in checking the correctness of a user-provided Hessian.

Tao, TaoSetHessian(), TaoDefaultComputeHessianColor(), SNESComputeJacobianDefault(), TaoSetGradient(), TaoDefaultComputeGradient()

src/tao/interface/fdiff.c

src/tao/unconstrained/tutorials/minsurf2.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h"  
PetscErrorCode TaoDefaultComputeHessian(Tao tao, Vec V, Mat H, Mat B, void *dummy)
```

Example 2 (unknown):
```unknown
TaoSetHessian()
```

Example 3 (unknown):
```unknown
TaoDefaultComputeHessianColor()
```

Example 4 (unknown):
```unknown
SNESComputeJacobianDefault()
```

---

## TaoDefaultConvergenceTest#

**URL:** https://petsc.org/release/manualpages/Tao/TaoDefaultConvergenceTest/

**Contents:**
- TaoDefaultConvergenceTest#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Determines whether the solver should continue iterating or terminate.

tao - the Tao context

dummy - unused dummy context

This routine checks the residual in the optimality conditions, the relative residual in the optimity conditions, the number of function evaluations, and the function value to test convergence. Some solvers may use different convergence routines.

TAO: Optimization Solvers, Tao, TaoSetTolerances(), TaoGetConvergedReason(), TaoSetConvergedReason()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoDefaultConvergenceTest(Tao tao, void *dummy)
```

Example 2 (unknown):
```unknown
TaoSetTolerances()
```

Example 3 (unknown):
```unknown
TaoGetConvergedReason()
```

Example 4 (unknown):
```unknown
TaoSetConvergedReason()
```

---

## TaoDestroy#

**URL:** https://petsc.org/release/manualpages/Tao/TaoDestroy/

**Contents:**
- TaoDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Destroys the Tao context that was created with TaoCreate()

tao - the Tao context

TAO: Optimization Solvers, Tao, TaoCreate(), TaoSolve()

src/tao/interface/taosolver.c

src/tao/leastsquares/tutorials/chwirut1f.F90 src/tao/leastsquares/tutorials/chwirut2f.F90 src/tao/leastsquares/tutorials/cs1.c src/tao/pde_constrained/tutorials/elliptic.c src/tao/constrained/tutorials/tomographyADMM.c src/tao/pde_constrained/tutorials/parabolic.c src/tao/constrained/tutorials/ex1.c src/tao/pde_constrained/tutorials/hyperbolic.c src/tao/constrained/tutorials/maros.c src/tao/leastsquares/tutorials/chwirut1.c

TaoDestroy_BLMVM() in src/tao/bound/impls/blmvm/blmvm.c TaoDestroy_BNCG() in src/tao/bound/impls/bncg/bncg.c TaoDestroy_BNK() in src/tao/bound/impls/bnk/bnk.c TaoDestroy_BQNK() in src/tao/bound/impls/bqnk/bqnk.c TaoDestroy_TRON() in src/tao/bound/impls/tron/tron.c TaoDestroy_ASFLS() in src/tao/complementarity/impls/asls/asfls.c TaoDestroy_ASILS() in src/tao/complementarity/impls/asls/asils.c TaoDestroy_SSFLS() in src/tao/complementarity/impls/ssls/ssfls.c TaoDestroy_SSILS() in src/tao/complementarity/impls/ssls/ssils.c TaoDestroy_ADMM() in src/tao/constrained/impls/admm/admm.c TaoDestroy_ALMM() in src/tao/constrained/impls/almm/almm.c TaoDestroy_IPM() in src/tao/constrained/impls/ipm/ipm.c TaoDestroy_PDIPM() in src/tao/constrained/impls/ipm/pdipm.c TaoDestroy_BRGN() in src/tao/leastsquares/impls/brgn/brgn.c TaoDestroy_POUNDERS() in src/tao/leastsquares/impls/pounders/pounders.c TaoDestroy_LCL() in src/tao/pde_constrained/impls/lcl/lcl.c TaoDestroy_BQPIP() in src/tao/quadratic/impls/bqpip/bqpip.c TaoDestroy_GPCG() in src/tao/quadratic/impls/gpcg/gpcg.c TaoDestroy_BMRM() in src/tao/unconstrained/impls/bmrm/bmrm.c TaoDestroy_CG() in src/tao/unconstrained/impls/cg/taocg.c TaoDestroy_LMVM() in src/tao/unconstrained/impls/lmvm/lmvm.c TaoDestroy_NM() in src/tao/unconstrained/impls/neldermead/neldermead.c TaoDestroy_NLS() in src/tao/unconstrained/impls/nls/nls.c TaoDestroy_NTL() in src/tao/unconstrained/impls/ntl/ntl.c TaoDestroy_NTR() in src/tao/unconstrained/impls/ntr/ntr.c TaoDestroy_OWLQN() in src/tao/unconstrained/impls/owlqn/owlqn.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoDestroy(Tao *tao)
```

Example 3 (unknown):
```unknown
TaoCreate()
```

---

## TaoEstimateActiveBounds#

**URL:** https://petsc.org/release/manualpages/Tao/TaoEstimateActiveBounds/

**Contents:**
- TaoEstimateActiveBounds#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#

Generates index sets for variables at the lower and upper bounds, as well as fixed variables where lower and upper bounds equal each other.

XL - lower bound vector

XU - upper bound vector

G - unprojected gradient

S - step direction with which the active bounds will be estimated

W - work vector of type and size of X

steplen - the step length at which the active bounds will be estimated (needs to be conservative)

bound_tol - tolerance for the bound estimation

active_lower - index set for active variables at the lower bound

active_upper - index set for active variables at the upper bound

active_fixed - index set for fixed variables

active - index set for all active variables

inactive - complementary index set for inactive variables

This estimation is based on Bertsekas’ method, with a built in diagonal scaling value of 1.0e-3.

TAOBNCG, TAOBNTL, TAOBNTR, TaoBoundSolution()

src/tao/bound/utils/isutil.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoEstimateActiveBounds(Vec X, Vec XL, Vec XU, Vec G, Vec S, Vec W, PetscReal steplen, PetscReal *bound_tol, IS *active_lower, IS *active_upper, IS *active_fixed, IS *active, IS *inactive)
```

Example 2 (unknown):
```unknown
TaoBoundSolution()
```

---

## TaoFinalizePackage#

**URL:** https://petsc.org/release/manualpages/Tao/TaoFinalizePackage/

**Contents:**
- TaoFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys everything in the PETSc/Tao interface to the Tao package. It is called from PetscFinalize().

TaoInitializePackage(), PetscFinalize(), TaoRegister(), TaoRegisterAll()

src/tao/interface/dlregistao.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscFinalize()
```

Example 2 (unknown):
```unknown
PetscErrorCode TaoFinalizePackage(void)
```

Example 3 (unknown):
```unknown
TaoInitializePackage()
```

Example 4 (unknown):
```unknown
PetscFinalize()
```

---

## TaoGetADMMParentTao#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetADMMParentTao/

**Contents:**
- TaoGetADMMParentTao#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Gets pointer to parent TAOADMM, used by inner subsolver.

tao - the Tao context

admm_tao - the parent Tao context

src/tao/constrained/impls/admm/admm.c

src/tao/constrained/tutorials/tomographyADMM.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetADMMParentTao(Tao tao, Tao *admm_tao)
```

---

## TaoGetApplicationContext#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetApplicationContext/

**Contents:**
- TaoGetApplicationContext#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Fortran Note#
- See Also#
- Level#
- Location#

Gets the user-defined context for a Tao solver provided with TaoSetApplicationContext()

tao - the Tao context

ctx - a pointer to the application context

This only works when the context is a Fortran derived type or a PetscObject. Define ctx with

TAO: Optimization Solvers, Tao, TaoSetApplicationContext()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoSetApplicationContext()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetApplicationContext(Tao tao, PetscCtxRt ctx)
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

## TaoGetConstraintTolerances#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetConstraintTolerances/

**Contents:**
- TaoGetConstraintTolerances#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Gets constraint tolerance parameters used in TaoSolve() convergence tests

tao - the Tao context

catol - absolute constraint tolerance, constraint norm must be less than catol for used for gatol convergence criteria

crtol - relative constraint tolerance, constraint norm must be less than crtol for used for gatol, gttol convergence criteria

TAO: Optimization Solvers, Tao, TaoConvergedReason, TaoGetTolerances(), TaoSetTolerances(), TaoSetConstraintTolerances()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetConstraintTolerances(Tao tao, PetscReal *catol, PetscReal *crtol)
```

Example 2 (unknown):
```unknown
TaoConvergedReason
```

Example 3 (unknown):
```unknown
TaoGetTolerances()
```

Example 4 (unknown):
```unknown
TaoSetTolerances()
```

---

## TaoGetConvergedReason#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetConvergedReason/

**Contents:**
- TaoGetConvergedReason#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Gets the reason the TaoSolve() was stopped.

tao - the Tao solver context

reason - value of TaoConvergedReason

TAO: Optimization Solvers, Tao, TaoConvergedReason, TaoSetConvergenceTest(), TaoSetTolerances()

src/tao/interface/taosolver.c

src/tao/leastsquares/tutorials/chwirut1f.F90 src/tao/constrained/tutorials/maros.c src/tao/unconstrained/tutorials/rosenbrock3.c src/tao/unconstrained/tutorials/rosenbrock2.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetConvergedReason(Tao tao, TaoConvergedReason *reason)
```

Example 2 (unknown):
```unknown
TaoConvergedReason
```

Example 3 (unknown):
```unknown
TaoConvergedReason
```

Example 4 (unknown):
```unknown
TaoSetConvergenceTest()
```

---

## TaoGetConvergenceHistory#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetConvergenceHistory/

**Contents:**
- TaoGetConvergenceHistory#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- Fortran Notes#
- See Also#
- Level#
- Location#
- Examples#

Gets the arrays used that hold the convergence history.

tao - the Tao context

obj - array used to hold objective value history

resid - array used to hold residual history

cnorm - array used to hold constraint violation history

lits - integer array used to hold linear solver iteration count

nhist - size of obj, resid, cnorm, and lits

This routine must be preceded by calls to TaoSetConvergenceHistory() and TaoSolve(), otherwise it returns useless information.

This routine is useful, e.g., when running a code for purposes of accurate performance monitoring, when no I/O should be done during the section of code that is being timed.

The calling sequence is

In other words this gets the current number of entries in the history. Access the history through the array you passed to TaoSetConvergenceHistory()

TAO: Optimization Solvers, Tao, TaoSolve(), TaoSetConvergenceHistory()

src/tao/interface/taosolver.c

src/tao/leastsquares/tutorials/chwirut1f.F90

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetConvergenceHistory(Tao tao, PetscReal **obj, PetscReal **resid, PetscReal **cnorm, PetscInt **lits, PetscInt *nhist)
```

Example 2 (unknown):
```unknown
TaoSetConvergenceHistory()
```

Example 3 (unknown):
```unknown
call TaoGetConvergenceHistory(Tao tao, PetscInt nhist, PetscErrorCode ierr)
```

Example 4 (unknown):
```unknown
TaoSetConvergenceHistory()
```

---

## TaoGetCurrentFunctionEvaluations#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetCurrentFunctionEvaluations/

**Contents:**
- TaoGetCurrentFunctionEvaluations#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get current number of function evaluations used by a Tao object

tao - the Tao solver context

nfuncs - the current number of function evaluations (maximum between gradient and function evaluations)

TAO: Optimization Solvers, Tao, TaoSetMaximumFunctionEvaluations(), TaoGetMaximumFunctionEvaluations(), TaoGetMaximumIterations()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetCurrentFunctionEvaluations(Tao tao, PetscInt *nfuncs)
```

Example 2 (unknown):
```unknown
TaoSetMaximumFunctionEvaluations()
```

Example 3 (unknown):
```unknown
TaoGetMaximumFunctionEvaluations()
```

Example 4 (unknown):
```unknown
TaoGetMaximumIterations()
```

---

## TaoGetCurrentTrustRegionRadius#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetCurrentTrustRegionRadius/

**Contents:**
- TaoGetCurrentTrustRegionRadius#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the current trust region radius.

tao - a Tao optimization solver

radius - the trust region radius

TAO: Optimization Solvers, Tao, TaoSetInitialTrustRegionRadius(), TaoGetInitialTrustRegionRadius(), TAONTR

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetCurrentTrustRegionRadius(Tao tao, PetscReal *radius)
```

Example 2 (unknown):
```unknown
TaoSetInitialTrustRegionRadius()
```

Example 3 (unknown):
```unknown
TaoGetInitialTrustRegionRadius()
```

---

## TaoGetDualVariables#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetDualVariables/

**Contents:**
- TaoGetDualVariables#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#

Gets the dual vectors

tao - the Tao context

DE - dual variable vector for the lower bounds

DI - dual variable vector for the upper bounds

TAO: Optimization Solvers, Tao, TaoComputeDualVariables()

src/tao/interface/taosolver_bounds.c

src/tao/constrained/tutorials/ex1.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetDualVariables(Tao tao, Vec *DE, Vec *DI)
```

Example 2 (unknown):
```unknown
TaoComputeDualVariables()
```

---

## TaoGetEqualityConstraintsRoutine#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetEqualityConstraintsRoutine/

**Contents:**
- TaoGetEqualityConstraintsRoutine#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#

Gets the function used to compute equality constraints.

tao - the Tao context

ci - the vector to internally hold the constraint computation

func - the bounds computation routine

ctx - the (optional) user-defined context

x - point to evaluate equality constraints

ci - vector of equality constraints evaluated at x

ctx - the (optional) user-defined function context

TAO: Optimization Solvers, Tao, TaoSolve(), TaoGetObjective(), TaoGetGradient(), TaoGetHessian(), TaoGetObjectiveAndGradient(), TaoGetInequalityConstraintsRoutine()

src/tao/interface/taosolver_bounds.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetEqualityConstraintsRoutine(Tao tao, Vec *ci, PetscErrorCode (**func)(Tao tao, Vec x, Vec ci, PetscCtx ctx), PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
TaoGetObjective()
```

Example 3 (unknown):
```unknown
TaoGetGradient()
```

Example 4 (unknown):
```unknown
TaoGetHessian()
```

---

## TaoGetFunctionLowerBound#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetFunctionLowerBound/

**Contents:**
- TaoGetFunctionLowerBound#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the bound on the solution objective value. When an approximate solution with an objective value below this number has been found, the solver will terminate.

tao - the Tao solver context

fmin - the minimum function value

TAO: Optimization Solvers, Tao, TaoConvergedReason, TaoSetFunctionLowerBound()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetFunctionLowerBound(Tao tao, PetscReal *fmin)
```

Example 2 (unknown):
```unknown
TaoConvergedReason
```

Example 3 (unknown):
```unknown
TaoSetFunctionLowerBound()
```

---

## TaoGetGradientNorm#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetGradientNorm/

**Contents:**
- TaoGetGradientNorm#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the matrix used to define the norm used for measuring the size of the gradient in some of the Tao algorithms

tao - the Tao context

TAO: Optimization Solvers, Tao, TaoSetGradientNorm(), TaoGradientNorm()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetGradientNorm(Tao tao, Mat *M)
```

Example 2 (unknown):
```unknown
TaoSetGradientNorm()
```

Example 3 (unknown):
```unknown
TaoGradientNorm()
```

---

## TaoGetGradient#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetGradient/

**Contents:**
- TaoGetGradient#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Calling sequence of func#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Gets the gradient evaluation routine for the function being optimized

tao - the Tao context

g - the vector to internally hold the gradient computation

func - the gradient function

ctx - user-defined context for private data for the gradient evaluation routine

g - gradient value (output)

ctx - [optional] user-defined function context

In addition to specifying an objective function using callbacks such as TaoSetObjective() and TaoSetGradient(), users can specify objective functions with TaoAddTerm().

TaoGetGradient() will always return the callback specified with TaoSetGradient(), even if the objective function has been changed by calling TaoAddTerm().

TAO: Optimization Solvers, Tao, TaoSetObjective(), TaoSetHessian(), TaoSetObjectiveAndGradient(), TaoSetGradient()

src/tao/interface/taosolver_fg.c

src/tao/unconstrained/tutorials/spectraladjointassimilation.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetGradient(Tao tao, Vec *g, PetscErrorCode (**func)(Tao tao, Vec x, Vec g, PetscCtx ctx), PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
TaoSetObjective()
```

Example 3 (unknown):
```unknown
TaoSetGradient()
```

Example 4 (unknown):
```unknown
TaoAddTerm()
```

---

## TaoGetHessianMatrices#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetHessianMatrices/

**Contents:**
- TaoGetHessianMatrices#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Get the matrices that store the Hessian matrix and its (optional) approximation that is used to construct the preconditioner

tao - the Tao context

H - the Hessian matrix

Hpre - approximation to the Hessian matrix used to construct the preconditioner (often H)

TAO: Optimization Solvers, Tao, TaoType, TaoGetObjective(), TaoGetGradient(), TaoGetObjectiveAndGradient(), TaoSetHessian(), TaoGetHessian()

src/tao/interface/taosolver_hj.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetHessianMatrices(Tao tao, Mat *H, Mat *Hpre)
```

Example 2 (unknown):
```unknown
TaoGetObjective()
```

Example 3 (unknown):
```unknown
TaoGetGradient()
```

Example 4 (unknown):
```unknown
TaoGetObjectiveAndGradient()
```

---

## TaoGetHessian#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetHessian/

**Contents:**
- TaoGetHessian#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Calling sequence of func#
- Notes#
- See Also#
- Level#
- Location#

Gets the function to compute the Hessian as well as the location to store the matrix.

tao - the Tao context

H - Matrix used for the hessian

Hpre - Matrix that will be used to construct the preconditioner, can be the same as H

func - Hessian evaluation routine

ctx - user-defined context for private data for the Hessian evaluation routine

tao - the Tao context

Hpre - matrix used to construct the preconditioner, usually the same as H

ctx - [optional] user-defined Hessian context

In addition to specifying an objective function using callbacks such as TaoSetObjectiveAndGradient() and TaoSetHessian(), users can specify objective functions with TaoAddTerm().

TaoGetHessian() will always return the callback specified with TaoSetHessian(), even if the objective function has been changed by calling TaoAddTerm().

TAO: Optimization Solvers, Tao, TaoType, TaoGetObjective(), TaoGetGradient(), TaoGetObjectiveAndGradient(), TaoSetHessian(), TaoGetHessianMatrices()

src/tao/interface/taosolver_hj.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetHessian(Tao tao, Mat *H, Mat *Hpre, PetscErrorCode (**func)(Tao tao, Vec x, Mat H, Mat Hpre, PetscCtx ctx), PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
TaoSetObjectiveAndGradient()
```

Example 3 (unknown):
```unknown
TaoSetHessian()
```

Example 4 (unknown):
```unknown
TaoAddTerm()
```

---

## TaoGetInequalityBounds#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetInequalityBounds/

**Contents:**
- TaoGetInequalityBounds#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Gets the upper and lower bounds set via TaoSetInequalityBounds()

tao - the Tao context

IL - vector of lower bounds

IU - vector of upper bounds

TAO: Optimization Solvers, TaoSetObjective(), TaoSetHessian(), TaoSetObjectiveAndGradient(), TaoSetInequalityBounds()

src/tao/interface/taosolver_bounds.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoSetInequalityBounds()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetInequalityBounds(Tao tao, Vec *IL, Vec *IU)
```

Example 3 (unknown):
```unknown
TaoSetObjective()
```

Example 4 (unknown):
```unknown
TaoSetHessian()
```

---

## TaoGetInequalityConstraintsRoutine#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetInequalityConstraintsRoutine/

**Contents:**
- TaoGetInequalityConstraintsRoutine#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#

Gets the function used to compute inequality constraints.

tao - the Tao context

ci - the vector to internally hold the constraint computation

func - the bounds computation routine

ctx - the (optional) user-defined context

x - point to evaluate inequality constraints

ci - vector of inequality constraints evaluated at x

ctx - the (optional) user-defined function context

TAO: Optimization Solvers, Tao, TaoSolve(), TaoGetObjective(), TaoGetGradient(), TaoGetHessian(), TaoGetObjectiveAndGradient(), TaoGetEqualityConstraintsRoutine()

src/tao/interface/taosolver_bounds.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetInequalityConstraintsRoutine(Tao tao, Vec *ci, PetscErrorCode (**func)(Tao tao, Vec x, Vec ci, PetscCtx ctx), PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
TaoGetObjective()
```

Example 3 (unknown):
```unknown
TaoGetGradient()
```

Example 4 (unknown):
```unknown
TaoGetHessian()
```

---

## TaoGetInitialTrustRegionRadius#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetInitialTrustRegionRadius/

**Contents:**
- TaoGetInitialTrustRegionRadius#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the initial trust region radius.

tao - a Tao optimization solver

radius - the trust region radius

TAO: Optimization Solvers, Tao, TaoSetInitialTrustRegionRadius(), TaoGetCurrentTrustRegionRadius(), TAONTR

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetInitialTrustRegionRadius(Tao tao, PetscReal *radius)
```

Example 2 (unknown):
```unknown
TaoSetInitialTrustRegionRadius()
```

Example 3 (unknown):
```unknown
TaoGetCurrentTrustRegionRadius()
```

---

## TaoGetIterationNumber#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetIterationNumber/

**Contents:**
- TaoGetIterationNumber#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Gets the number of TaoSolve() iterations completed at this time.

tao - the Tao context

iter - iteration number

For example, during the computation of iteration 2 this would return 1.

TAO: Optimization Solvers, Tao, TaoGetLinearSolveIterations(), TaoGetResidualNorm(), TaoGetObjective()

src/tao/interface/taosolver.c

src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/tao/unconstrained/tutorials/rosenbrock3.c src/tao/unconstrained/tutorials/rosenbrock2.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetIterationNumber(Tao tao, PetscInt *iter)
```

Example 2 (unknown):
```unknown
TaoGetLinearSolveIterations()
```

Example 3 (unknown):
```unknown
TaoGetResidualNorm()
```

Example 4 (unknown):
```unknown
TaoGetObjective()
```

---

## TaoGetJacobianEqualityRoutine#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetJacobianEqualityRoutine/

**Contents:**
- TaoGetJacobianEqualityRoutine#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#

Gets the function used to compute equality constraint Jacobian.

tao - the Tao context

J - the matrix to internally hold the constraint computation

Jpre - the matrix used to construct the preconditioner

func - Jacobian evaluation routine

ctx - the (optional) user-defined context

tao - the Tao context

Jpre - matrix used to construct the preconditioner, usually the same as J

ctx - [optional] user-defined Jacobian context

TAO: Optimization Solvers, Tao, TaoComputeJacobianEquality(), TaoSetJacobianEqualityRoutine()

src/tao/interface/taosolver_hj.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetJacobianEqualityRoutine(Tao tao, Mat *J, Mat *Jpre, PetscErrorCode (**func)(Tao tao, Vec x, Mat J, Mat Jpre, PetscCtx ctx), PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
TaoComputeJacobianEquality()
```

Example 3 (unknown):
```unknown
TaoSetJacobianEqualityRoutine()
```

---

## TaoGetJacobianInequalityRoutine#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetJacobianInequalityRoutine/

**Contents:**
- TaoGetJacobianInequalityRoutine#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#

Gets the function used to compute inequality constraint Jacobian.

tao - the Tao context

J - the matrix to internally hold the constraint computation

Jpre - the matrix used to construct the preconditioner

func - Jacobian evaluation routine

ctx - the (optional) user-defined context

tao - the Tao context

Jpre - matrix used to construct the preconditioner, usually the same as J

ctx - [optional] user-defined Jacobian context

TAO: Optimization Solvers, Tao, TaoComputeJacobianInequality(), TaoSetJacobianInequalityRoutine()

src/tao/interface/taosolver_hj.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetJacobianInequalityRoutine(Tao tao, Mat *J, Mat *Jpre, PetscErrorCode (**func)(Tao tao, Vec x, Mat J, Mat Jpre, PetscCtx ctx), PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
TaoComputeJacobianInequality()
```

Example 3 (unknown):
```unknown
TaoSetJacobianInequalityRoutine()
```

---

## TaoGetKSP#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetKSP/

**Contents:**
- TaoGetKSP#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Gets the linear solver used by the optimization solver.

ksp - the KSP linear solver used in the optimization solver

TAO: Optimization Solvers, Tao, KSP

src/tao/interface/taosolver.c

src/ts/tutorials/ex20opt_p.c src/tao/bound/tutorials/jbearing2.c src/tao/unconstrained/tutorials/minsurf1.c src/ts/tutorials/ex20opt_ic.c src/tao/unconstrained/tutorials/eptorsion1.c src/tao/unconstrained/tutorials/eptorsion3.c src/tao/constrained/tutorials/ex1.c src/tao/constrained/tutorials/maros.c src/tao/unconstrained/tutorials/eptorsion2.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetKSP(Tao tao, KSP *ksp)
```

---

## TaoGetLinearSolveIterations#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetLinearSolveIterations/

**Contents:**
- TaoGetLinearSolveIterations#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the total number of linear iterations used by the Tao solver

tao - the Tao context

lits - number of linear iterations

This counter is reset to zero for each successive call to TaoSolve()

TAO: Optimization Solvers, Tao, TaoGetKSP()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetLinearSolveIterations(Tao tao, PetscInt *lits)
```

Example 2 (unknown):
```unknown
TaoGetKSP()
```

---

## TaoGetLineSearch#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetLineSearch/

**Contents:**
- TaoGetLineSearch#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the line search used by the optimization solver.

ls - the line search used in the optimization solver

TAO: Optimization Solvers, Tao, TaoLineSearch, TaoLineSearchType

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetLineSearch(Tao tao, TaoLineSearch *ls)
```

Example 2 (unknown):
```unknown
TaoLineSearch
```

Example 3 (unknown):
```unknown
TaoLineSearchType
```

---

## TaoGetLMVMMatrix#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetLMVMMatrix/

**Contents:**
- TaoGetLMVMMatrix#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns a pointer to the internal LMVM matrix. Valid only for quasi-Newton family of methods.

tao - Tao solver context

TAOBQNLS, TAOBQNKLS, TAOBQNKTL, TAOBQNKTR, MATLMVM, TaoSetLMVMMatrix()

src/tao/bound/impls/bqnk/bqnk.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetLMVMMatrix(Tao tao, Mat *B)
```

Example 2 (unknown):
```unknown
TaoSetLMVMMatrix()
```

---

## TaoGetMaximumFunctionEvaluations#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetMaximumFunctionEvaluations/

**Contents:**
- TaoGetMaximumFunctionEvaluations#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets a maximum number of function evaluations allowed for a TaoSolve()

tao - the Tao solver context

nfcn - the maximum number of function evaluations

TAO: Optimization Solvers, Tao, TaoSetMaximumFunctionEvaluations(), TaoGetMaximumIterations()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetMaximumFunctionEvaluations(Tao tao, PetscInt *nfcn)
```

Example 2 (unknown):
```unknown
TaoSetMaximumFunctionEvaluations()
```

Example 3 (unknown):
```unknown
TaoGetMaximumIterations()
```

---

## TaoGetMaximumIterations#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetMaximumIterations/

**Contents:**
- TaoGetMaximumIterations#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets a maximum number of iterates that will be used

tao - the Tao solver context

maxits - the maximum number of iterates

TAO: Optimization Solvers, Tao, TaoSetMaximumIterations(), TaoGetMaximumFunctionEvaluations()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetMaximumIterations(Tao tao, PetscInt *maxits)
```

Example 2 (unknown):
```unknown
TaoSetMaximumIterations()
```

Example 3 (unknown):
```unknown
TaoGetMaximumFunctionEvaluations()
```

---

## TaoGetObjectiveAndGradient#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetObjectiveAndGradient/

**Contents:**
- TaoGetObjectiveAndGradient#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Calling sequence of func#
- Note#
- See Also#
- Level#
- Location#

Gets the combined objective function and gradient evaluation routine for the function to be optimized

tao - the Tao context

g - the vector to internally hold the gradient computation

func - the gradient function

ctx - user-defined context for private data for the gradient evaluation routine

f - objective value (output)

g - gradient value (output)

ctx - [optional] user-defined function context

In addition to specifying an objective function using callbacks such as TaoSetObjectiveAndGradient(), users can specify objective functions with TaoAddTerm().

TaoGetObjectiveAndGradient() will always return the callback specified with TaoSetObjectiveAndGradient(), even if the objective function has been changed by calling TaoAddTerm().

TAO: Optimization Solvers, Tao, TaoSolve(), TaoSetObjective(), TaoSetGradient(), TaoSetHessian(), TaoSetObjectiveAndGradient()

src/tao/interface/taosolver_fg.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetObjectiveAndGradient(Tao tao, Vec *g, PetscErrorCode (**func)(Tao tao, Vec x, PetscReal *f, Vec g, PetscCtx ctx), PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
TaoSetObjectiveAndGradient()
```

Example 3 (unknown):
```unknown
TaoAddTerm()
```

Example 4 (unknown):
```unknown
TaoGetObjectiveAndGradient()
```

---

## TaoGetObjective#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetObjective/

**Contents:**
- TaoGetObjective#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Calling sequence of func#
- Notes#
- See Also#
- Level#
- Location#

Gets the function evaluation routine for the function to be minimized

tao - the Tao context

func - the objective function

ctx - the user-defined context for private data for the function evaluation

ctx - [optional] user-defined function context

In addition to specifying an objective function using callbacks such as TaoSetObjective() and TaoSetGradient(), users can specify objective functions with TaoAddTerm().

TaoGetObjective() will always return the callback specified with TaoSetObjective(), even if the objective function has been changed by calling TaoAddTerm().

TAO: Optimization Solvers, Tao, TaoSetGradient(), TaoSetHessian(), TaoSetObjective()

src/tao/interface/taosolver_fg.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetObjective(Tao tao, PetscErrorCode (**func)(Tao tao, Vec x, PetscReal *f, PetscCtx ctx), PetscCtxRt ctx)
```

Example 2 (unknown):
```unknown
TaoSetObjective()
```

Example 3 (unknown):
```unknown
TaoSetGradient()
```

Example 4 (unknown):
```unknown
TaoAddTerm()
```

---

## TaoGetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetOptionsPrefix/

**Contents:**
- TaoGetOptionsPrefix#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the prefix used for searching for all Tao options in the database

tao - the Tao context

p - pointer to the prefix string used is returned

TAO: Optimization Solvers, Tao, TaoSetFromOptions(), TaoSetOptionsPrefix(), TaoAppendOptionsPrefix()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetOptionsPrefix(Tao tao, const char *p[])
```

Example 2 (unknown):
```unknown
TaoSetFromOptions()
```

Example 3 (unknown):
```unknown
TaoSetOptionsPrefix()
```

Example 4 (unknown):
```unknown
TaoAppendOptionsPrefix()
```

---

## TaoGetRecycleHistory#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetRecycleHistory/

**Contents:**
- TaoGetRecycleHistory#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Retrieve the boolean flag for re-using iterate information from the previous TaoSolve(). This feature is disabled by default.

tao - the Tao context

recycle - boolean flag

TAO: Optimization Solvers, Tao, TaoSetRecycleHistory(), TAOBNCG, TAOBQNLS, TAOBQNKLS, TAOBQNKTR, TAOBQNKTL

src/tao/interface/taosolver.c

src/tao/unconstrained/tutorials/rosenbrock3.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetRecycleHistory(Tao tao, PetscBool *recycle)
```

Example 2 (unknown):
```unknown
TaoSetRecycleHistory()
```

---

## TaoGetResidualNorm#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetResidualNorm/

**Contents:**
- TaoGetResidualNorm#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Developer Notes#
- See Also#
- Level#
- Location#

Gets the current value of the norm of the residual (gradient) at this time.

tao - the Tao context

value - the current value

This is the 2-norm of the residual, we cannot use TaoGetGradientNorm() because that has a different meaning. For some reason Tao sometimes calls the gradient the residual.

TAO: Optimization Solvers, Tao, TaoGetLinearSolveIterations(), TaoGetIterationNumber(), TaoGetObjective()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetResidualNorm(Tao tao, PetscReal *value)
```

Example 2 (unknown):
```unknown
TaoGetGradientNorm()
```

Example 3 (unknown):
```unknown
TaoGetLinearSolveIterations()
```

Example 4 (unknown):
```unknown
TaoGetIterationNumber()
```

---

## TaoGetSolutionStatus#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetSolutionStatus/

**Contents:**
- TaoGetSolutionStatus#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Get the current iterate, objective value, residual, infeasibility, and termination from a Tao object

tao - the Tao context

its - the current iterate number (>=0)

f - the current function value

gnorm - the square of the gradient norm, duality gap, or other measure indicating distance from optimality.

cnorm - the infeasibility of the current solution with regard to the constraints.

xdiff - the step length or trust region radius of the most recent iterate.

reason - The termination reason, which can equal TAO_CONTINUE_ITERATING

Tao returns the values set by the solvers in the routine TaoMonitor().

If any of the output arguments are set to NULL, no corresponding value will be returned.

TAO: Optimization Solvers, TaoMonitor(), TaoGetConvergedReason()

src/tao/interface/taosolver.c

src/tao/bound/tutorials/jbearing2.c src/tao/unconstrained/tutorials/eptorsion2f.F90 src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetSolutionStatus(Tao tao, PetscInt *its, PetscReal *f, PetscReal *gnorm, PetscReal *cnorm, PetscReal *xdiff, TaoConvergedReason *reason)
```

Example 2 (unknown):
```unknown
TAO_CONTINUE_ITERATING
```

Example 3 (unknown):
```unknown
TaoMonitor()
```

Example 4 (unknown):
```unknown
TaoMonitor()
```

---

## TaoGetSolution#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetSolution/

**Contents:**
- TaoGetSolution#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Returns the vector with the current solution from the Tao object

tao - the Tao context

X - the current solution

The returned vector will be the same object that was passed into TaoSetSolution()

TAO: Optimization Solvers, Tao, TaoSetSolution(), TaoSolve()

src/tao/interface/taosolver.c

src/tao/unconstrained/tutorials/minsurf2.c src/tao/pde_constrained/tutorials/elliptic.c src/tao/constrained/tutorials/tomographyADMM.c src/tao/pde_constrained/tutorials/parabolic.c src/tao/constrained/tutorials/ex1.c src/tao/pde_constrained/tutorials/hyperbolic.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetSolution(Tao tao, Vec *X)
```

Example 2 (unknown):
```unknown
TaoSetSolution()
```

Example 3 (unknown):
```unknown
TaoSetSolution()
```

---

## TaoGetTerm#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetTerm/

**Contents:**
- TaoGetTerm#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Get the entire objective function of the Tao as a single TaoTerm in the form \(\alpha f(Ax; p)\), where \(\alpha\) is a scaling coefficient, \(f\) is a TaoTerm, \(A\) is an (optional) map and \(p\) are the parameters of \(f\).

scale - the scale of the term

term - a TaoTerm for the real-valued function defining the objective

params - the vector of parameters for term, or NULL if no parameters were specified for term

map - a map from the solution space of tao to the solution space of term, if NULL then the map is the identity

If the objective function was defined by providing function callbacks directly to Tao (for example, with TaoSetObjectiveAndGradient()), then TaoGetTerm will return a TaoTerm with the type TAOTERMCALLBACKS that encapsulates those functions.

If multiple TaoTerms were provided to Tao via, for example, TaoAddTerm(), or in combination with giving functions directly to Tao, then the type TAOTERMSUM is returned.

TAO: Optimization Solvers, Tao, TaoTerm, TAOTERMSUM, TaoAddTerm()

src/tao/interface/taosolver.c

src/tao/unconstrained/tutorials/elastic_net_regularization.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetTerm(Tao tao, PetscReal *scale, TaoTerm *term, Vec *params, Mat *map)
```

Example 2 (unknown):
```unknown
TaoSetObjectiveAndGradient()
```

Example 3 (unknown):
```unknown
TAOTERMCALLBACKS
```

Example 4 (unknown):
```unknown
TaoAddTerm()
```

---

## TaoGetTolerances#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetTolerances/

**Contents:**
- TaoGetTolerances#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

gets the current values of some tolerances used for the convergence testing of TaoSolve()

tao - the Tao context

gatol - stop if norm of gradient is less than this

grtol - stop if relative norm of gradient is less than this

gttol - stop if norm of gradient is reduced by a this factor

NULL can be used as an argument if not all tolerances values are needed

TAO: Optimization Solvers, Tao, TaoSetTolerances()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetTolerances(Tao tao, PetscReal *gatol, PetscReal *grtol, PetscReal *gttol)
```

Example 2 (unknown):
```unknown
TaoSetTolerances()
```

---

## TaoGetTotalIterationNumber#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetTotalIterationNumber/

**Contents:**
- TaoGetTotalIterationNumber#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the total number of TaoSolve() iterations completed. This number keeps accumulating if multiple solves are called with the Tao object.

tao - the Tao context

iter - number of iterations

The total iteration count is updated after each solve, if there is a current TaoSolve() in progress then those iterations are not included in the count

TAO: Optimization Solvers, Tao, TaoGetLinearSolveIterations()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetTotalIterationNumber(Tao tao, PetscInt *iter)
```

Example 2 (unknown):
```unknown
TaoGetLinearSolveIterations()
```

---

## TaoGetType#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetType/

**Contents:**
- TaoGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the current TaoType being used in the Tao object

tao - the Tao solver context

type should not be retained for later use as it will be an invalid pointer if the TaoType of tao is changed.

TAO: Optimization Solvers, Tao, TaoType, TaoSetType(), PetscObjectTypeCompare(), PetscObjectTypeCompareAny()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetType(Tao tao, TaoType *type)
```

Example 2 (unknown):
```unknown
TaoSetType()
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

## TaoGetVariableBounds#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGetVariableBounds/

**Contents:**
- TaoGetVariableBounds#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Gets the upper and lower bounds vectors set with TaoSetVariableBounds()

tao - the Tao context

XL - vector of lower bounds

XU - vector of upper bounds

TAO: Optimization Solvers, Tao, TaoSetObjective(), TaoSetHessian(), TaoSetObjectiveAndGradient(), TaoSetVariableBounds()

src/tao/interface/taosolver_bounds.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoSetVariableBounds()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGetVariableBounds(Tao tao, Vec *XL, Vec *XU)
```

Example 3 (unknown):
```unknown
TaoSetObjective()
```

Example 4 (unknown):
```unknown
TaoSetHessian()
```

---

## TAOGPCG#

**URL:** https://petsc.org/release/manualpages/Tao/TAOGPCG/

**Contents:**
- TAOGPCG#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#

gradient projected conjugate gradient algorithm is an active-set conjugate-gradient based method for bound-constrained minimization

-tao_gpcg_maxpgits - maximum number of gradient projections for GPCG iterate

-tao_subset_type - “subvec”,”mask”,”matrix-free”, strategies for handling active-sets

Tao, TaoType, TAOTRON, TAOBQPIP, TAOLINESEARCHGPCG

src/tao/quadratic/impls/gpcg/gpcg.c

src/tao/bound/tutorials/jbearing2.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TAOLINESEARCHGPCG
```

---

## TaoGradientNorm#

**URL:** https://petsc.org/release/manualpages/Tao/TaoGradientNorm/

**Contents:**
- TaoGradientNorm#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- Developer Notes#
- See Also#
- Level#
- Location#

Compute the norm using the NormType, the user has selected

tao - the Tao context

gradient - the gradient

gnorm - the gradient norm

If TaoSetGradientNorm() has been set and type is NORM_2 then the norm provided with TaoSetGradientNorm() is used.

Should be named TaoComputeGradientNorm().

The usage is a bit confusing, with TaoSetGradientNorm() plus NORM_2 resulting in the computation of the user provided norm, perhaps a refactorization is in order.

TAO: Optimization Solvers, Tao, TaoSetGradientNorm(), TaoGetGradientNorm()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoGradientNorm(Tao tao, Vec gradient, NormType type, PetscReal *gnorm)
```

Example 2 (unknown):
```unknown
TaoSetGradientNorm()
```

Example 3 (unknown):
```unknown
TaoSetGradientNorm()
```

Example 4 (unknown):
```unknown
TaoComputeGradientNorm()
```

---

## TaoInitializePackage#

**URL:** https://petsc.org/release/manualpages/Tao/TaoInitializePackage/

**Contents:**
- TaoInitializePackage#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#

This function sets up PETSc to use the Tao package. When using static or shared libraries, this function is called from the first entry to TaoCreate(); when using shared or static libraries, it is called from PetscDLLibraryRegister_tao()

This function never needs to be called by PETSc users.

TaoCreate(), TaoFinalizePackage(), TaoRegister(), TaoRegisterAll()

src/tao/interface/dlregistao.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

Example 2 (unknown):
```unknown
PetscErrorCode TaoInitializePackage(void)
```

Example 3 (unknown):
```unknown
TaoCreate()
```

Example 4 (unknown):
```unknown
TaoFinalizePackage()
```

---

## TAOIPM#

**URL:** https://petsc.org/release/manualpages/Tao/TAOIPM/

**Contents:**
- TAOIPM#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Interior point algorithm for generally constrained optimization.

-tao_ipm_pushnu - parameter to push initial dual variables away from bounds

-tao_ipm_pushs - parameter to push initial slack variables away from bounds

This algorithm is more of a place-holder for future constrained optimization algorithms and should not yet be used for large problems or production code.

Tao, TAOPDIPM, TaoType

src/tao/constrained/impls/ipm/ipm.c

src/tao/constrained/tutorials/maros.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

---

## TaoIsGradientDefined#

**URL:** https://petsc.org/release/manualpages/Tao/TaoIsGradientDefined/

**Contents:**
- TaoIsGradientDefined#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Checks to see if the user has declared a gradient-only routine. Useful for determining when it is appropriate to call TaoComputeGradient() or TaoComputeObjectiveAndGradient()

tao - the Tao context

flg - PETSC_TRUE if the objective TaoTerm has this routine, PETSC_FALSE otherwise

If the objective of Tao has been altered via TaoAddTerm(), it will return whether the summation of all terms has this routine.

TAO: Optimization Solvers, TaoSetGradient(), TaoIsObjectiveDefined(), TaoIsObjectiveAndGradientDefined()

src/tao/interface/taosolver_fg.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoComputeGradient()
```

Example 2 (unknown):
```unknown
TaoComputeObjectiveAndGradient()
```

Example 3 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoIsGradientDefined(Tao tao, PetscBool *flg)
```

Example 4 (unknown):
```unknown
PETSC_FALSE
```

---

## TaoIsObjectiveAndGradientDefined#

**URL:** https://petsc.org/release/manualpages/Tao/TaoIsObjectiveAndGradientDefined/

**Contents:**
- TaoIsObjectiveAndGradientDefined#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Checks to see if the user has declared a joint objective/gradient routine. Useful for determining when it is appropriate to call TaoComputeObjectiveAndGradient()

tao - the Tao context

flg - PETSC_TRUE if the objective TaoTerm has this routine PETSC_FALSE otherwise

If the objective of Tao has been altered via TaoAddTerm(), it will return whether the summation of all terms has this routine.

TAO: Optimization Solvers, TaoSetObjectiveAndGradient(), TaoIsObjectiveDefined(), TaoIsGradientDefined()

src/tao/interface/taosolver_fg.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoComputeObjectiveAndGradient()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoIsObjectiveAndGradientDefined(Tao tao, PetscBool *flg)
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (unknown):
```unknown
TaoAddTerm()
```

---

## TaoIsObjectiveDefined#

**URL:** https://petsc.org/release/manualpages/Tao/TaoIsObjectiveDefined/

**Contents:**
- TaoIsObjectiveDefined#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Checks to see if the user has declared an objective-only routine. Useful for determining when it is appropriate to call TaoComputeObjective() or TaoComputeObjectiveAndGradient()

tao - the Tao context

flg - PETSC_TRUE if the Tao has this routine PETSC_FALSE otherwise

If the objective of Tao has been altered via TaoAddTerm(), it will return whether the summation of all terms has this routine.

TAO: Optimization Solvers, Tao, TaoSetObjective(), TaoIsGradientDefined(), TaoIsObjectiveAndGradientDefined()

src/tao/interface/taosolver_fg.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoComputeObjective()
```

Example 2 (unknown):
```unknown
TaoComputeObjectiveAndGradient()
```

Example 3 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoIsObjectiveDefined(Tao tao, PetscBool *flg)
```

Example 4 (unknown):
```unknown
PETSC_FALSE
```

---

## TaoKSPSetUseEW#

**URL:** https://petsc.org/release/manualpages/Tao/TaoKSPSetUseEW/

**Contents:**
- TaoKSPSetUseEW#
- Synopsis#
- Input Parameters#
- Note#
- References#
- See Also#
- Level#
- Location#

Sets SNES to use Eisenstat-Walker method [EW96] for computing relative tolerance for linear solvers.

flag - PETSC_TRUE or PETSC_FALSE

See SNESKSPSetUseEW() for customization details.

S. C. Eisenstat and H. F. Walker. Choosing the forcing terms in an inexact Newton method. SIAM J. Scientific Computing, 17:16–32, 1996.

TAO: Optimization Solvers, Tao, SNESKSPSetUseEW()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoKSPSetUseEW(Tao tao, PetscBool flag)
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
SNESKSPSetUseEW()
```

---

## TAOLCL#

**URL:** https://petsc.org/release/manualpages/Tao/TAOLCL/

**Contents:**
- TAOLCL#
- Option Database Keys#
- See Also#
- Level#
- Location#
- Examples#

linearly constrained Lagrangian method for PDE-constrained optimization

-tao_lcl_eps1 - epsilon 1 tolerance

-tao_lcl_eps2 - epsilon 2 tolerance

-tao_lcl_rho0 - initial value for rho

-tao_lcl_rhomax - maximum allowed value for rho

-tao_lcl_phase2_niter - Number of phase 2 iterations in the LCL algorithm

-tao_lcl_verbose - Print verbose output if True

-tao_lcl_tola - Tolerance for first forward solve

-tao_lcl_tolb - Tolerance for first adjoint solve

-tao_lcl_tolc - Tolerance for second forward solve

-tao_lcl_told - Tolerance for second adjoint solve

Tao, TaoType, TaoSetStateDesignIS(), TaoSetJacobianStateRoutine(), TaoSetJacobianDesignRoutine()

src/tao/pde_constrained/impls/lcl/lcl.c

src/tao/pde_constrained/tutorials/elliptic.c src/tao/pde_constrained/tutorials/hyperbolic.c src/tao/pde_constrained/tutorials/parabolic.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoSetStateDesignIS()
```

Example 2 (unknown):
```unknown
TaoSetJacobianStateRoutine()
```

Example 3 (unknown):
```unknown
TaoSetJacobianDesignRoutine()
```

---

## TaoLineSearchAppendOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchAppendOptionsPrefix/

**Contents:**
- TaoLineSearchAppendOptionsPrefix#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Appends to the prefix used for searching for all TaoLineSearch options in the database.

ls - the TaoLineSearch solver context

p - the prefix string to prepend to all line search requests

A hyphen (-) must NOT be given at the beginning of the prefix name. The first character of all runtime options is AUTOMATICALLY the hyphen.

This is inherited from the Tao object so rarely needs to be set

TAO: Optimization Solvers, Tao, TaoLineSearch, TaoLineSearchSetOptionsPrefix(), TaoLineSearchGetOptionsPrefix()

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoLineSearch
```

Example 2 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchAppendOptionsPrefix(TaoLineSearch ls, const char p[])
```

Example 3 (unknown):
```unknown
TaoLineSearch
```

Example 4 (unknown):
```unknown
TaoLineSearch
```

---

## TaoLineSearchApply#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchApply/

**Contents:**
- TaoLineSearchApply#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Performs a line-search in a given step direction. Criteria for acceptable step length depends on the line-search algorithm chosen

ls - the TaoLineSearch context

x - On input the current solution, on output x contains the new solution determined by the line search

f - On input the objective function value at current solution, on output contains the objective function value at new solution

g - On input the gradient evaluated at x, on output contains the gradient at new solution

steplength - scalar multiplier of s used ( $x = x_0 + steplength * x)

reason - TaoLineSearchConvergedReason reason why the line-search stopped

The algorithm developer must set up the TaoLineSearch with calls to TaoLineSearchSetObjectiveRoutine() and TaoLineSearchSetGradientRoutine(), TaoLineSearchSetObjectiveAndGradientRoutine(), or TaoLineSearchUseTaoRoutines(). The latter is done automatically by default and thus requires no user input.

You may or may not need to follow this with a call to TaoAddLineSearchCounts(), depending on whether you want these evaluations to count toward the total function/gradient evaluations.

TAO: Optimization Solvers, Tao, TaoLineSearchConvergedReason, TaoLineSearch, TaoLineSearchCreate(), TaoLineSearchSetType(), TaoLineSearchSetInitialStepLength(), TaoAddLineSearchCounts()

src/tao/linesearch/interface/taolinesearch.c

TaoLineSearchApply_Armijo() in src/tao/linesearch/impls/armijo/armijo.c TaoLineSearchApply_GPCG() in src/tao/linesearch/impls/gpcglinesearch/gpcglinesearch.c TaoLineSearchApply_MT() in src/tao/linesearch/impls/morethuente/morethuente.c TaoLineSearchApply_OWArmijo() in src/tao/linesearch/impls/owarmijo/owarmijo.c TaoLineSearchApply_Unit() in src/tao/linesearch/impls/unit/unit.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchApply(TaoLineSearch ls, Vec x, PetscReal *f, Vec g, Vec s, PetscReal *steplength, TaoLineSearchConvergedReason *reason)
```

Example 2 (unknown):
```unknown
TaoLineSearch
```

Example 3 (unknown):
```unknown
TaoLineSearchConvergedReason
```

Example 4 (unknown):
```unknown
TaoLineSearch
```

---

## TAOLINESEARCHARMIJO#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TAOLINESEARCHARMIJO/

**Contents:**
- TAOLINESEARCHARMIJO#
- See Also#
- Level#
- Location#

Backtracking line-search that satisfies only the (nonmonotone) Armijo condition (i.e., sufficient decrease). Armijo line-search type can be selected with “-tao_ls_type armijo”.

TaoLineSearchCreate(), TaoLineSearchSetType(), TaoLineSearchApply()

src/tao/linesearch/impls/armijo/armijo.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoLineSearchCreate()
```

Example 2 (unknown):
```unknown
TaoLineSearchSetType()
```

Example 3 (unknown):
```unknown
TaoLineSearchApply()
```

---

## TaoLineSearchComputeGradient#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchComputeGradient/

**Contents:**
- TaoLineSearchComputeGradient#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Computes the gradient of the objective function

ls - the TaoLineSearch context

TaoComputeGradient() is typically used within line searches so most users would not generally call this routine themselves.

TAO: Optimization Solvers, Tao, TaoLineSearch, TaoLineSearchComputeObjective(), TaoLineSearchComputeObjectiveAndGradient(), TaoLineSearchSetGradient()

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchComputeGradient(TaoLineSearch ls, Vec x, Vec g)
```

Example 2 (unknown):
```unknown
TaoLineSearch
```

Example 3 (unknown):
```unknown
TaoComputeGradient()
```

Example 4 (unknown):
```unknown
TaoLineSearch
```

---

## TaoLineSearchComputeObjectiveAndGradient#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchComputeObjectiveAndGradient/

**Contents:**
- TaoLineSearchComputeObjectiveAndGradient#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Computes the objective function value at a given point

ls - the TaoLineSearch context

f - Objective value at x

g - Gradient vector at x

TaoLineSearchComputeObjectiveAndGradient() is typically used within line searches so most users would not generally call this routine themselves.

TAO: Optimization Solvers, Tao, TaoLineSearch, TaoLineSearchComputeGradient(), TaoLineSearchSetObjectiveRoutine()

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchComputeObjectiveAndGradient(TaoLineSearch ls, Vec x, PetscReal *f, Vec g)
```

Example 2 (unknown):
```unknown
TaoLineSearch
```

Example 3 (unknown):
```unknown
TaoLineSearchComputeObjectiveAndGradient()
```

Example 4 (unknown):
```unknown
TaoLineSearch
```

---

## TaoLineSearchComputeObjectiveAndGTS#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchComputeObjectiveAndGTS/

**Contents:**
- TaoLineSearchComputeObjectiveAndGTS#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Computes the objective function value and inner product of gradient and step direction at a given point

ls - the TaoLineSearch context

f - Objective value at x

gts - inner product of gradient and step direction at x

TaoLineSearchComputeObjectiveAndGTS() is typically used within line searches so most users would not generally call this routine themselves.

TAO: Optimization Solvers, Tao, TaoLineSearch, TaoLineSearchComputeGradient(), TaoLineSearchComputeObjectiveAndGradient(), TaoLineSearchSetObjectiveRoutine()

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchComputeObjectiveAndGTS(TaoLineSearch ls, Vec x, PetscReal *f, PetscReal *gts)
```

Example 2 (unknown):
```unknown
TaoLineSearch
```

Example 3 (unknown):
```unknown
TaoLineSearchComputeObjectiveAndGTS()
```

Example 4 (unknown):
```unknown
TaoLineSearch
```

---

## TaoLineSearchComputeObjective#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchComputeObjective/

**Contents:**
- TaoLineSearchComputeObjective#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Computes the objective function value at a given point

ls - the TaoLineSearch context

f - Objective value at x

TaoLineSearchComputeObjective() is typically used within line searches so most users would not generally call this routine themselves.

TAO: Optimization Solvers, Tao, TaoLineSearch, TaoLineSearchComputeGradient(), TaoLineSearchComputeObjectiveAndGradient(), TaoLineSearchSetObjectiveRoutine()

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchComputeObjective(TaoLineSearch ls, Vec x, PetscReal *f)
```

Example 2 (unknown):
```unknown
TaoLineSearch
```

Example 3 (unknown):
```unknown
TaoLineSearchComputeObjective()
```

Example 4 (unknown):
```unknown
TaoLineSearch
```

---

## TaoLineSearchConvergedReason#

**URL:** https://petsc.org/release/manualpages/Tao/TaoLineSearchConvergedReason/

**Contents:**
- TaoLineSearchConvergedReason#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

reason a TaoLineSearch completed

TAOLINESEARCH_FAILED_ASCENT - initial line search step * g is not descent direction

TAOLINESEARCH_FAILED_INFORNAN - function evaluation gives Inf or Nan value

TAOLINESEARCH_FAILED_BADPARAMETER - negative value set as parameter

TAOLINESEARCH_HALTED_MAXFCN - maximum number of function evaluation reached

TAOLINESEARCH_HALTED_UPPERBOUND - step is at upper bound

TAOLINESEARCH_HALTED_LOWERBOUND - step is at lower bound

TAOLINESEARCH_HALTED_RTOL - range of uncertainty is smaller than given tolerance

TAOLINESEARCH_HALTED_USER - user can set this reason to stop line search

TAOLINESEARCH_HALTED_OTHER - any other reason

TAOLINESEARCH_SUCCESS - successful line search

TAO: Optimization Solvers, Tao, TaoLineSearch, TaoSolve(), TaoGetConvergedReason(), KSPConvergedReason, SNESConvergedReason

include/petsctaolinesearch.h

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoLineSearch
```

Example 2 (unknown):
```unknown
typedef enum {
  TAOLINESEARCH_FAILED_INFORNAN     = -1,
  TAOLINESEARCH_FAILED_BADPARAMETER = -2,
  TAOLINESEARCH_FAILED_ASCENT       = -3,
  TAOLINESEARCH_CONTINUE_ITERATING  = 0,
  TAOLINESEARCH_SUCCESS             = 1,
  TAOLINESEARCH_SUCCESS_USER        = 2,
  TAOLINESEARCH_HALTED_OTHER        = 3,
  TAOLINESEARCH_HALTED_MAXFCN       = 4,
  TAOLINESEARCH_HALTED_UPPERBOUND   = 5,
  TAOLINESEARCH_HALTED_LOWERBOUND   = 6,
  TAOLINESEARCH_HALTED_RTOL         = 7,
  TAOLINESEARCH_HALTED_USER         = 8
} TaoLineSearchConvergedReason;
```

Example 3 (unknown):
```unknown
TAOLINESEARCH_FAILED_ASCENT
```

Example 4 (unknown):
```unknown
TAOLINESEARCH_FAILED_INFORNAN
```

---

## TaoLineSearchCreate#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchCreate/

**Contents:**
- TaoLineSearchCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

Creates a TaoLineSearch object. Algorithms in Tao that use line-searches will automatically create one so this all is rarely needed

comm - MPI communicator

newls - the new TaoLineSearch context

-tao_ls_type (unit|more- thuente|gpcg|armijo|owarmijo|ipm) - select which line search Tao should use

TAO: Optimization Solvers, Tao, TaoLineSearch, TaoLineSearchType, TaoLineSearchSetType(), TaoLineSearchApply(), TaoLineSearchDestroy()

src/tao/linesearch/interface/taolinesearch.c

TaoLineSearchCreate_Armijo() in src/tao/linesearch/impls/armijo/armijo.c TaoLineSearchCreate_GPCG() in src/tao/linesearch/impls/gpcglinesearch/gpcglinesearch.c TaoLineSearchCreate_MT() in src/tao/linesearch/impls/morethuente/morethuente.c TaoLineSearchCreate_OWArmijo() in src/tao/linesearch/impls/owarmijo/owarmijo.c TaoLineSearchCreate_Unit() in src/tao/linesearch/impls/unit/unit.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoLineSearch
```

Example 2 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchCreate(MPI_Comm comm, TaoLineSearch *newls)
```

Example 3 (unknown):
```unknown
TaoLineSearch
```

Example 4 (unknown):
```unknown
TaoLineSearch
```

---

## TaoLineSearchDestroy#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchDestroy/

**Contents:**
- TaoLineSearchDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Destroys the TaoLineSearch context that was created with TaoLineSearchCreate()

ls - the TaoLineSearch context

TaoLineSearch, TaoLineSearchCreate(), TaoLineSearchApple()

src/tao/linesearch/interface/taolinesearch.c

TaoLineSearchDestroy_Armijo() in src/tao/linesearch/impls/armijo/armijo.c TaoLineSearchDestroy_GPCG() in src/tao/linesearch/impls/gpcglinesearch/gpcglinesearch.c TaoLineSearchDestroy_MT() in src/tao/linesearch/impls/morethuente/morethuente.c TaoLineSearchDestroy_OWArmijo() in src/tao/linesearch/impls/owarmijo/owarmijo.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoLineSearch
```

Example 2 (unknown):
```unknown
TaoLineSearchCreate()
```

Example 3 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchDestroy(TaoLineSearch *ls)
```

Example 4 (unknown):
```unknown
TaoLineSearch
```

---

## TaoLineSearchFinalizePackage#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchFinalizePackage/

**Contents:**
- TaoLineSearchFinalizePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function destroys everything in the TaoLineSearch package. It is called from PetscFinalize().

src/tao/linesearch/interface/dlregis_taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoLineSearch
```

Example 2 (unknown):
```unknown
PetscFinalize()
```

Example 3 (unknown):
```unknown
PetscErrorCode TaoLineSearchFinalizePackage(void)
```

Example 4 (unknown):
```unknown
TaoLineSearch
```

---

## TaoLineSearchGetFullStepObjective#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchGetFullStepObjective/

**Contents:**
- TaoLineSearchGetFullStepObjective#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Returns the objective function value at the full step. Useful for some minimization algorithms.

ls - the TaoLineSearch context

f_fullstep - the objective value at the full step length

TaoLineSearchGetSolution(), TaoLineSearchGetStartingVector(), TaoLineSearchGetStepDirection()

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchGetFullStepObjective(TaoLineSearch ls, PetscReal *f_fullstep)
```

Example 2 (unknown):
```unknown
TaoLineSearch
```

Example 3 (unknown):
```unknown
TaoLineSearchGetSolution()
```

Example 4 (unknown):
```unknown
TaoLineSearchGetStartingVector()
```

---

## TaoLineSearchGetNumberFunctionEvaluations#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchGetNumberFunctionEvaluations/

**Contents:**
- TaoLineSearchGetNumberFunctionEvaluations#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Gets the number of function and gradient evaluation routines used by the line search in last application (not cumulative).

ls - the TaoLineSearch context

nfeval - number of function evaluations

ngeval - number of gradient evaluations

nfgeval - number of function/gradient evaluations

If the line search is using the Tao objective and gradient routines directly (see TaoLineSearchUseTaoRoutines()), then the Tao is already counting the number of evaluations.

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchGetNumberFunctionEvaluations(TaoLineSearch ls, PetscInt *nfeval, PetscInt *ngeval, PetscInt *nfgeval)
```

Example 2 (unknown):
```unknown
TaoLineSearch
```

Example 3 (unknown):
```unknown
TaoLineSearchUseTaoRoutines()
```

Example 4 (unknown):
```unknown
TaoLineSearch
```

---

## TaoLineSearchGetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchGetOptionsPrefix/

**Contents:**
- TaoLineSearchGetOptionsPrefix#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the prefix used for searching for all TaoLineSearch options in the database

ls - the TaoLineSearch context

p - pointer to the prefix string used is returned

TAO: Optimization Solvers, Tao, TaoLineSearch, TaoLineSearchSetOptionsPrefix(), TaoLineSearchAppendOptionsPrefix()

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoLineSearch
```

Example 2 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchGetOptionsPrefix(TaoLineSearch ls, const char *p[])
```

Example 3 (unknown):
```unknown
TaoLineSearch
```

Example 4 (unknown):
```unknown
TaoLineSearch
```

---

## TaoLineSearchGetSolution#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchGetSolution/

**Contents:**
- TaoLineSearchGetSolution#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Returns the solution to the line search

ls - the TaoLineSearch context

f - the objective function value at x

g - the gradient at x

steplength - the multiple of the step direction taken by the line search

reason - the reason why the line search terminated

TaoLineSearchGetStartingVector(), TaoLineSearchGetStepDirection()

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchGetSolution(TaoLineSearch ls, Vec x, PetscReal *f, Vec g, PetscReal *steplength, TaoLineSearchConvergedReason *reason)
```

Example 2 (unknown):
```unknown
TaoLineSearch
```

Example 3 (unknown):
```unknown
TaoLineSearchGetStartingVector()
```

Example 4 (unknown):
```unknown
TaoLineSearchGetStepDirection()
```

---

## TaoLineSearchGetStartingVector#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchGetStartingVector/

**Contents:**
- TaoLineSearchGetStartingVector#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets a the initial point of the line search.

ls - the TaoLineSearch context

x - The initial point of the line search

TaoLineSearchGetSolution(), TaoLineSearchGetStepDirection()

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchGetStartingVector(TaoLineSearch ls, Vec *x)
```

Example 2 (unknown):
```unknown
TaoLineSearch
```

Example 3 (unknown):
```unknown
TaoLineSearchGetSolution()
```

Example 4 (unknown):
```unknown
TaoLineSearchGetStepDirection()
```

---

## TaoLineSearchGetStepDirection#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchGetStepDirection/

**Contents:**
- TaoLineSearchGetStepDirection#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the step direction of the line search.

ls - the TaoLineSearch context

s - the step direction of the line search

TaoLineSearchGetSolution(), TaoLineSearchGetStartingVector()

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchGetStepDirection(TaoLineSearch ls, Vec *s)
```

Example 2 (unknown):
```unknown
TaoLineSearch
```

Example 3 (unknown):
```unknown
TaoLineSearchGetSolution()
```

Example 4 (unknown):
```unknown
TaoLineSearchGetStartingVector()
```

---

## TaoLineSearchGetStepLength#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchGetStepLength/

**Contents:**
- TaoLineSearchGetStepLength#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the current step length

ls - the TaoLineSearch context

s - the current step length

TAO: Optimization Solvers, Tao, TaoLineSearch, TaoLineSearchSetInitialStepLength(), TaoLineSearchApply()

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchGetStepLength(TaoLineSearch ls, PetscReal *s)
```

Example 2 (unknown):
```unknown
TaoLineSearch
```

Example 3 (unknown):
```unknown
TaoLineSearch
```

Example 4 (unknown):
```unknown
TaoLineSearchSetInitialStepLength()
```

---

## TaoLineSearchGetType#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchGetType/

**Contents:**
- TaoLineSearchGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Gets the current line search algorithm

ls - the TaoLineSearch context

type - the line search algorithm in effect

type should not be retained for later use as it will be an invalid pointer if the TaoLineSearchType of ls is changed.

TaoLineSearch, TaoLineSearchSetType(), TaoLineSearchType, PetscObjectTypeCompare(), PetscObjectTypeCompareAny()

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchGetType(TaoLineSearch ls, TaoLineSearchType *type)
```

Example 2 (unknown):
```unknown
TaoLineSearch
```

Example 3 (unknown):
```unknown
TaoLineSearchType
```

Example 4 (unknown):
```unknown
TaoLineSearch
```

---

## TAOLINESEARCHGPCG#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TAOLINESEARCHGPCG/

**Contents:**
- TAOLINESEARCHGPCG#
- See Also#
- Level#
- Location#

Special line-search method for the Gradient-Projected Conjugate Gradient (TAOGPCG) algorithm. Should not be used with any other algorithm.

TAOGPCG, TaoLineSearch, Tao

src/tao/linesearch/impls/gpcglinesearch/gpcglinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoLineSearch
```

---

## TaoLineSearchInitializePackage#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchInitializePackage/

**Contents:**
- TaoLineSearchInitializePackage#
- Synopsis#
- See Also#
- Level#
- Location#

This function registers the line-search algorithms in Tao. When using shared or static libraries, this function is called from the first entry to TaoCreate(); when using dynamic, it is called from PetscDLLibraryRegister_tao()

Tao, TaoLineSearch, TaoLineSearchCreate()

src/tao/linesearch/interface/dlregis_taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

Example 2 (unknown):
```unknown
PetscErrorCode TaoLineSearchInitializePackage(void)
```

Example 3 (unknown):
```unknown
TaoLineSearch
```

Example 4 (unknown):
```unknown
TaoLineSearchCreate()
```

---

## TaoLineSearchIsUsingTaoRoutines#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchIsUsingTaoRoutines/

**Contents:**
- TaoLineSearchIsUsingTaoRoutines#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Checks whether the line search is using the standard Tao evaluation routines.

ls - the TaoLineSearch context

flg - PETSC_TRUE if the line search is using Tao evaluation routines, otherwise PETSC_FALSE

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchIsUsingTaoRoutines(TaoLineSearch ls, PetscBool *flg)
```

Example 2 (unknown):
```unknown
TaoLineSearch
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (unknown):
```unknown
TaoLineSearch
```

---

## TaoLineSearchMonitor#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchMonitor/

**Contents:**
- TaoLineSearchMonitor#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Implementations#

Monitor the line search steps. This routine will output the iteration number, step length, and function value before calling the implementation specific monitor.

ls - the TaoLineSearch context

its - the current iterate number (>=0)

f - the current objective function value

step - the step length

-tao_ls_monitor - Use the default monitor, which prints statistics to standard output

src/tao/linesearch/interface/taolinesearch.c

TaoLineSearchMonitor_MT() in src/tao/linesearch/impls/morethuente/morethuente.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchMonitor(TaoLineSearch ls, PetscInt its, PetscReal f, PetscReal step)
```

Example 2 (unknown):
```unknown
TaoLineSearch
```

Example 3 (unknown):
```unknown
TaoLineSearch
```

---

## TAOLINESEARCHMT#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TAOLINESEARCHMT/

**Contents:**
- TAOLINESEARCHMT#
- Options Database Key#
- References#
- See Also#
- Level#
- Location#

More-Thuente line-search type with cubic interpolation that satisfies both the sufficient decrease and curvature conditions. This method can take step lengths greater than 1, [MoreT92]

-tao_ls_type more- thuente - use this line search type

Jorge J. Moré and David Thuente. Line search algorithms with guaranteed sufficient decrease. Technical Report MCS-P330-1092, Mathematics and Computer Science Division, Argonne National Laboratory, 1992.

TaoLineSearchCreate(), TaoLineSearchSetType(), TaoLineSearchApply()

src/tao/linesearch/impls/morethuente/morethuente.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoLineSearchCreate()
```

Example 2 (unknown):
```unknown
TaoLineSearchSetType()
```

Example 3 (unknown):
```unknown
TaoLineSearchApply()
```

---

## TAOLINESEARCHOWARMIJO#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TAOLINESEARCHOWARMIJO/

**Contents:**
- TAOLINESEARCHOWARMIJO#
- See Also#
- Level#
- Location#

Special line-search type for the Orthant-Wise Limited Quasi-Newton (TAOOWLQN) algorithm. Should not be used with any other algorithm.

TaoLineSearch, TAOOWLQN, Tao

src/tao/linesearch/impls/owarmijo/owarmijo.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoLineSearch
```

---

## TaoLineSearchRegister#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchRegister/

**Contents:**
- TaoLineSearchRegister#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Example Usage#
- Note#
- See Also#
- Level#
- Location#

Adds a line-search algorithm to the registry

Not Collective, No Fortran Support

sname - name of a new user-defined solver

func - routine to Create method context

ls - the TaoLineSearch object to set with the TaoLineSearchType specific structure

Then, your solver can be chosen with the procedural interface via

or at runtime via the option

TaoLineSearchRegister() may be called multiple times to add several user-defined solvers.

TAO: Optimization Solvers, Tao, TaoLineSearch

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchRegister(const char sname[], PetscErrorCode (*func)(TaoLineSearch ls))
```

Example 2 (unknown):
```unknown
TaoLineSearch
```

Example 3 (unknown):
```unknown
TaoLineSearchType
```

Example 4 (unknown):
```unknown
TaoLineSearchRegister("my_linesearch", MyLinesearchCreate);
```

---

## TaoLineSearchReset#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchReset/

**Contents:**
- TaoLineSearchReset#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Some line searches may carry state information from one TaoLineSearchApply() to the next. This function resets this state information.

ls - the TaoLineSearch context

TAO: Optimization Solvers, Tao, TaoLineSearch, TaoLineSearchCreate(), TaoLineSearchApply()

src/tao/linesearch/interface/taolinesearch.c

TaoLineSearchReset_Armijo() in src/tao/linesearch/impls/armijo/armijo.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoLineSearchApply()
```

Example 2 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchReset(TaoLineSearch ls)
```

Example 3 (unknown):
```unknown
TaoLineSearch
```

Example 4 (unknown):
```unknown
TaoLineSearch
```

---

## TaoLineSearchSetFromOptions#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchSetFromOptions/

**Contents:**
- TaoLineSearchSetFromOptions#
- Synopsis#
- Input Parameter#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Implementations#

Sets various TaoLineSearch parameters from user options.

ls - the TaoLineSearch context

-tao_ls_type (unit|more- thuente|gpcg|armijo|owarmijo|ipm) - select which line search Tao should use

-tao_ls_ftol tol - tolerance for sufficient decrease

-tao_ls_gtol tol - tolerance for curvature condition

-tao_ls_rtol tol - relative tolerance for acceptable step

-tao_ls_stepinit step - initial steplength allowed

-tao_ls_stepmin step - minimum steplength allowed

-tao_ls_stepmax step - maximum steplength allowed

-tao_ls_max_funcs n - maximum number of function evaluations allowed

-tao_ls_view - display line-search results

Tao, TaoLineSearch, TaoGetLineSearch()

src/tao/linesearch/interface/taolinesearch.c

TaoLineSearchSetFromOptions_Armijo() in src/tao/linesearch/impls/armijo/armijo.c TaoLineSearchSetFromOptions_OWArmijo() in src/tao/linesearch/impls/owarmijo/owarmijo.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoLineSearch
```

Example 2 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchSetFromOptions(TaoLineSearch ls)
```

Example 3 (unknown):
```unknown
TaoLineSearch
```

Example 4 (unknown):
```unknown
TaoLineSearch
```

---

## TaoLineSearchSetGradientRoutine#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchSetGradientRoutine/

**Contents:**
- TaoLineSearchSetGradientRoutine#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Note#
- See Also#
- Level#
- Location#

Sets the gradient evaluation routine for the line search

ls - the TaoLineSearch context

func - the gradient evaluation routine

ctx - the (optional) user-defined context for private data

ls - the linesearch object

ctx - (optional) user-defined context

Use this routine only if you want the line search gradient evaluation routine to be different from the Tao’s gradient evaluation routine. If you use this routine you must also set the line search function and/or function/gradient routine.

Some algorithms (lcl, gpcg) set their own gradient routine for the line search, application programmers should be wary of overriding the default gradient routine.

TAO: Optimization Solvers, Tao, TaoLineSearch, TaoLineSearchCreate(), TaoLineSearchSetObjectiveRoutine(), TaoLineSearchSetObjectiveAndGradientRoutine(), TaoLineSearchUseTaoRoutines()

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchSetGradientRoutine(TaoLineSearch ls, PetscErrorCode (*func)(TaoLineSearch ls, Vec x, Vec g, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoLineSearch
```

Example 3 (unknown):
```unknown
TaoLineSearch
```

Example 4 (unknown):
```unknown
TaoLineSearchCreate()
```

---

## TaoLineSearchSetInitialStepLength#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchSetInitialStepLength/

**Contents:**
- TaoLineSearchSetInitialStepLength#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the initial step length of a line search. If this value is not set then 1.0 is assumed.

ls - the TaoLineSearch context

s - the initial step size

TAO: Optimization Solvers, Tao, TaoLineSearch, TaoLineSearchGetStepLength(), TaoLineSearchApply()

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchSetInitialStepLength(TaoLineSearch ls, PetscReal s)
```

Example 2 (unknown):
```unknown
TaoLineSearch
```

Example 3 (unknown):
```unknown
TaoLineSearch
```

Example 4 (unknown):
```unknown
TaoLineSearchGetStepLength()
```

---

## TaoLineSearchSetObjectiveAndGradientRoutine#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchSetObjectiveAndGradientRoutine/

**Contents:**
- TaoLineSearchSetObjectiveAndGradientRoutine#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Note#
- See Also#
- Level#
- Location#

Sets the objective/gradient evaluation routine for the line search

ls - the TaoLineSearch context

func - the objective and gradient evaluation routine

ctx - the (optional) user-defined context for private data

ls - the linesearch object

ctx - (optional) user-defined context

Use this routine only if you want the line search objective and gradient evaluation routines to be different from the Tao’s objective and gradient evaluation routines.

Some algorithms (lcl, gpcg) set their own objective routine for the line search, application programmers should be wary of overriding the default objective routine.

TAO: Optimization Solvers, Tao, TaoLineSearch, TaoLineSearchCreate(), TaoLineSearchSetObjectiveRoutine(), TaoLineSearchSetGradientRoutine(), TaoLineSearchUseTaoRoutines()

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchSetObjectiveAndGradientRoutine(TaoLineSearch ls, PetscErrorCode (*func)(TaoLineSearch ls, Vec x, PetscReal *f, Vec g, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoLineSearch
```

Example 3 (unknown):
```unknown
TaoLineSearch
```

Example 4 (unknown):
```unknown
TaoLineSearchCreate()
```

---

## TaoLineSearchSetObjectiveAndGTSRoutine#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchSetObjectiveAndGTSRoutine/

**Contents:**
- TaoLineSearchSetObjectiveAndGTSRoutine#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Notes#
- See Also#
- Level#
- Location#

Sets the objective and (gradient’*stepdirection) evaluation routine for the line search.

ls - the TaoLineSearch context

func - the objective and gradient evaluation routine

ctx - the (optional) user-defined context for private data

ls - the linesearch context

gts - inner product of gradient and step direction vectors

ctx - (optional) user-defined context

Sometimes it is more efficient to compute the inner product of the gradient and the step direction than it is to compute the gradient, and this is all the line search typically needs of the gradient.

The gradient will still need to be computed at the end of the line search, so you will still need to set a line search gradient evaluation routine

Bounded line searches (those used in bounded optimization algorithms) don’t use g’s directly, but rather (g’x - g’x0)/steplength. You can get the x0 and steplength with TaoLineSearchGetStartingVector() and TaoLineSearchGetStepLength()

Some algorithms (lcl, gpcg) set their own objective routine for the line search, application programmers should be wary of overriding the default objective routine.

TAO: Optimization Solvers, Tao, TaoLineSearch, TaoLineSearchCreate(), TaoLineSearchSetObjective(), TaoLineSearchSetGradient(), TaoLineSearchUseTaoRoutines()

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchSetObjectiveAndGTSRoutine(TaoLineSearch ls, PetscErrorCode (*func)(TaoLineSearch ls, Vec x, Vec s, PetscReal *f, PetscReal *gts, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoLineSearch
```

Example 3 (unknown):
```unknown
TaoLineSearchGetStartingVector()
```

Example 4 (unknown):
```unknown
TaoLineSearchGetStepLength()
```

---

## TaoLineSearchSetObjectiveRoutine#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchSetObjectiveRoutine/

**Contents:**
- TaoLineSearchSetObjectiveRoutine#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Notes#
- See Also#
- Level#
- Location#

Sets the function evaluation routine for the line search

ls - the TaoLineSearch context

func - the objective function evaluation routine

ctx - the (optional) user-defined context for private data

ls - the line search context

ctx - (optional) user-defined context

Use this routine only if you want the line search objective evaluation routine to be different from the Tao’s objective evaluation routine. If you use this routine you must also set the line search gradient and/or function/gradient routine.

Some algorithms (lcl, gpcg) set their own objective routine for the line search, application programmers should be wary of overriding the default objective routine.

TAO: Optimization Solvers, Tao, TaoLineSearch, TaoLineSearchCreate(), TaoLineSearchSetGradientRoutine(), TaoLineSearchSetObjectiveAndGradientRoutine(), TaoLineSearchUseTaoRoutines()

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchSetObjectiveRoutine(TaoLineSearch ls, PetscErrorCode (*func)(TaoLineSearch ls, Vec x, PetscReal *f, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoLineSearch
```

Example 3 (unknown):
```unknown
TaoLineSearch
```

Example 4 (unknown):
```unknown
TaoLineSearchCreate()
```

---

## TaoLineSearchSetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchSetOptionsPrefix/

**Contents:**
- TaoLineSearchSetOptionsPrefix#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Sets the prefix used for searching for all TaoLineSearch options in the database.

ls - the TaoLineSearch context

p - the prefix string to prepend to all ls option requests

A hyphen (-) must NOT be given at the beginning of the prefix name. The first character of all runtime options is AUTOMATICALLY the hyphen.

This is inherited from the Tao object so rarely needs to be set

For example, to distinguish between the runtime options for two different line searches, one could call

This would enable use of different options for each system, such as

TAO: Optimization Solvers, Tao, TaoLineSearch, TaoLineSearchAppendOptionsPrefix(), TaoLineSearchGetOptionsPrefix()

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoLineSearch
```

Example 2 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchSetOptionsPrefix(TaoLineSearch ls, const char p[])
```

Example 3 (unknown):
```unknown
TaoLineSearch
```

Example 4 (unknown):
```unknown
TaoLineSearchSetOptionsPrefix(ls1,"sys1_")
      TaoLineSearchSetOptionsPrefix(ls2,"sys2_")
```

---

## TaoLineSearchSetType#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchSetType/

**Contents:**
- TaoLineSearchSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Sets the algorithm used in a line search

ls - the TaoLineSearch context

type - the TaoLineSearchType selection

-tao_ls_type (unit|more- thuente|gpcg|armijo|owarmijo|ipm) - select which line search Tao should use

TAO: Optimization Solvers, Tao, TaoLineSearch, TaoLineSearchType, TaoLineSearchCreate(), TaoLineSearchGetType(), TaoLineSearchApply()

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchSetType(TaoLineSearch ls, TaoLineSearchType type)
```

Example 2 (unknown):
```unknown
TaoLineSearch
```

Example 3 (unknown):
```unknown
TaoLineSearchType
```

Example 4 (unknown):
```unknown
TaoLineSearch
```

---

## TaoLineSearchSetUp#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchSetUp/

**Contents:**
- TaoLineSearchSetUp#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#

Sets up the internal data structures for the later use of a TaoLineSearch

ls - the TaoLineSearch context

The user will not need to explicitly call TaoLineSearchSetUp(), as it will automatically be called in TaoLineSearchSolve(). However, if the user desires to call it explicitly, it should come after TaoLineSearchCreate() but before TaoLineSearchApply().

TAO: Optimization Solvers, Tao, TaoLineSearch, TaoLineSearchCreate(), TaoLineSearchApply()

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoLineSearch
```

Example 2 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchSetUp(TaoLineSearch ls)
```

Example 3 (unknown):
```unknown
TaoLineSearch
```

Example 4 (unknown):
```unknown
TaoLineSearchSetUp()
```

---

## TaoLineSearchSetVariableBounds#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchSetVariableBounds/

**Contents:**
- TaoLineSearchSetVariableBounds#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#

Sets the upper and lower bounds for a bounded line search

ls - the TaoLineSearch context

xl - vector of lower bounds

xu - vector of upper bounds

If the variable bounds are not set with this routine, then PETSC_NINFINITY and PETSC_INFINITY are assumed

TAO: Optimization Solvers, Tao, TaoLineSearch, TaoSetVariableBounds(), TaoLineSearchCreate()

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchSetVariableBounds(TaoLineSearch ls, Vec xl, Vec xu)
```

Example 2 (unknown):
```unknown
TaoLineSearch
```

Example 3 (unknown):
```unknown
PETSC_NINFINITY
```

Example 4 (unknown):
```unknown
PETSC_INFINITY
```

---

## TaoLineSearchType#

**URL:** https://petsc.org/release/manualpages/Tao/TaoLineSearchType/

**Contents:**
- TaoLineSearchType#
- Synopsis#
- Values#
- Options Database Key#
- See Also#
- Level#
- Location#

String with the name of a TaoLineSearch method

TAOLINESEARCHUNIT - “unit” do not perform a line search and always accept unit step length

TAOLINESEARCHMT - “more-thuente” line search with a cubic model enforcing the strong Wolfe/curvature condition

TAOLINESEARCHGPCG - “gpcg”

TAOLINESEARCHARMIJO - “armijo” simple backtracking line search enforcing only the sufficient decrease condition

TAOLINESEARCHOWARMIJO - “owarmijo”

TAOLINESEARCHIPM - “ipm”

-tao_ls_type type - select which method Tao should use at runtime

TAO: Optimization Solvers, Tao, TaoLineSearch, TaoLineSearchSetType(), TaoCreate(), TaoSetType()

include/petsctaolinesearch.h

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoLineSearch
```

Example 2 (unknown):
```unknown
typedef const char *TaoLineSearchType;
#define TAOLINESEARCHUNIT     "unit"
#define TAOLINESEARCHMT       "more-thuente"
#define TAOLINESEARCHGPCG     "gpcg"
#define TAOLINESEARCHARMIJO   "armijo"
#define TAOLINESEARCHOWARMIJO "owarmijo"
#define TAOLINESEARCHIPM      "ipm"
```

Example 3 (unknown):
```unknown
TAOLINESEARCHUNIT
```

Example 4 (unknown):
```unknown
TAOLINESEARCHMT
```

---

## TAOLINESEARCHUNIT#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TAOLINESEARCHUNIT/

**Contents:**
- TAOLINESEARCHUNIT#
- Options Database Keys#
- See Also#
- Level#
- Location#

Line-search type that disables line search and accepts the unit step length every time

-tao_ls_stepinit step - steplength

Tao, TaoLineSearch, TaoLineSearchCreate(), TaoLineSearchSetType(), TaoLineSearchApply()

src/tao/linesearch/impls/unit/unit.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoLineSearch
```

Example 2 (unknown):
```unknown
TaoLineSearchCreate()
```

Example 3 (unknown):
```unknown
TaoLineSearchSetType()
```

Example 4 (unknown):
```unknown
TaoLineSearchApply()
```

---

## TaoLineSearchUseTaoRoutines#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchUseTaoRoutines/

**Contents:**
- TaoLineSearchUseTaoRoutines#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Informs the TaoLineSearch to use the objective and gradient evaluation routines from the given Tao object. The default.

ls - the TaoLineSearch context

ts - the Tao context with defined objective/gradient evaluation routines

TAO: Optimization Solvers, Tao, TaoLineSearch, TaoLineSearchCreate()

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoLineSearch
```

Example 2 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchUseTaoRoutines(TaoLineSearch ls, Tao ts)
```

Example 3 (unknown):
```unknown
TaoLineSearch
```

Example 4 (unknown):
```unknown
TaoLineSearch
```

---

## TaoLineSearchViewFromOptions#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchViewFromOptions/

**Contents:**
- TaoLineSearchViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

View a TaoLineSearch object based on values in the options database

obj - Optional object

name - command line option

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

TAO: Optimization Solvers, Tao, TaoLineSearch, TaoLineSearchView(), PetscObjectViewFromOptions(), TaoLineSearchCreate()

src/tao/linesearch/interface/taolinesearch.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoLineSearch
```

Example 2 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchViewFromOptions(TaoLineSearch A, PetscObject obj, const char name[])
```

Example 3 (unknown):
```unknown
PetscObjectViewFromOptions()
```

Example 4 (unknown):
```unknown
TaoLineSearch
```

---

## TaoLineSearchView#

**URL:** https://petsc.org/release/manualpages/TaoLineSearch/TaoLineSearchView/

**Contents:**
- TaoLineSearchView#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Prints information about the TaoLineSearch

ls - the TaoLineSearch context

viewer - visualization context

-tao_ls_view - Calls TaoLineSearchView() at the end of each line search

The available visualization contexts include

PETSC_VIEWER_STDOUT_SELF - standard output (default)

PETSC_VIEWER_STDOUT_WORLD - synchronized standard output where only the first processor opens the file. All other processors send their data to the first processor to print.

TAO: Optimization Solvers, Tao, TaoLineSearch, PetscViewerASCIIOpen(), TaoLineSearchViewFromOptions()

src/tao/linesearch/interface/taolinesearch.c

TaoLineSearchView_Armijo() in src/tao/linesearch/impls/armijo/armijo.c TaoLineSearchView_GPCG() in src/tao/linesearch/impls/gpcglinesearch/gpcglinesearch.c TaoLineSearchView_OWArmijo() in src/tao/linesearch/impls/owarmijo/owarmijo.c TaoLineSearchView_Unit() in src/tao/linesearch/impls/unit/unit.c

Index of all TaoLineSearch routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoLineSearch
```

Example 2 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLineSearchView(TaoLineSearch ls, PetscViewer viewer)
```

Example 3 (unknown):
```unknown
TaoLineSearch
```

Example 4 (unknown):
```unknown
TaoLineSearchView()
```

---

## TaoLineSearch#

**URL:** https://petsc.org/release/manualpages/Tao/TaoLineSearch/

**Contents:**
- TaoLineSearch#
- Synopsis#
- See Also#
- Level#
- Location#
- Implementations#

PETSc object that manages line searches for the Tao optimization solves

TAO: Optimization Solvers, TaoLineSearchType, Tao, TaoCreate(), TaoDestroy(), TaoSetType(), TaoType

include/petsctaolinesearch.h

_p_TaoLineSearch in include/petsc/private/taolinesearchimpl.h TaoLineSearch_ARMIJO in src/tao/linesearch/impls/armijo/armijo.h TaoLineSearch_GPCG in src/tao/linesearch/impls/gpcglinesearch/gpcglinesearch.h TaoLineSearch_MT in src/tao/linesearch/impls/morethuente/morethuente.h TaoLineSearch_OWARMIJO in src/tao/linesearch/impls/owarmijo/owarmijo.h

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_TaoLineSearch *TaoLineSearch;
```

Example 2 (unknown):
```unknown
TaoLineSearchType
```

Example 3 (unknown):
```unknown
TaoCreate()
```

Example 4 (unknown):
```unknown
TaoDestroy()
```

---

## TaoLMVMGetH0KSP#

**URL:** https://petsc.org/release/manualpages/Tao/TaoLMVMGetH0KSP/

**Contents:**
- TaoLMVMGetH0KSP#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the iterative solver for applying the inverse of the QN initial Hessian

tao - the Tao solver context

ksp - KSP solver context for the initial Hessian

Tao, TAOLMVM, TAOBLMVM, TaoLMVMGetH0()

src/tao/bound/impls/blmvm/blmvm.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLMVMGetH0KSP(Tao tao, KSP *ksp)
```

Example 2 (unknown):
```unknown
TaoLMVMGetH0()
```

---

## TaoLMVMGetH0#

**URL:** https://petsc.org/release/manualpages/Tao/TaoLMVMGetH0/

**Contents:**
- TaoLMVMGetH0#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the matrix object for the QN initial Hessian

tao - the Tao solver context

H0 - Mat object for the initial Hessian

Tao, TAOLMVM, TAOBLMVM, TaoLMVMSetH0(), TaoLMVMGetH0KSP()

src/tao/bound/impls/blmvm/blmvm.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLMVMGetH0(Tao tao, Mat *H0)
```

Example 2 (unknown):
```unknown
TaoLMVMSetH0()
```

Example 3 (unknown):
```unknown
TaoLMVMGetH0KSP()
```

---

## TaoLMVMRecycle#

**URL:** https://petsc.org/release/manualpages/Tao/TaoLMVMRecycle/

**Contents:**
- TaoLMVMRecycle#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Enable/disable recycling of the QN history between subsequent TaoSolve() calls.

tao - the Tao solver context

flg - Boolean flag for recycling (PETSC_TRUE or PETSC_FALSE)

Tao, TAOLMVM, TAOBLMVM

src/tao/bound/impls/blmvm/blmvm.c

src/tao/unconstrained/tutorials/rosenbrock2.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLMVMRecycle(Tao tao, PetscBool flg)
```

Example 2 (unknown):
```unknown
PETSC_FALSE
```

---

## TaoLMVMSetH0#

**URL:** https://petsc.org/release/manualpages/Tao/TaoLMVMSetH0/

**Contents:**
- TaoLMVMSetH0#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Set the initial Hessian for the QN approximation

tao - the Tao solver context

H0 - Mat object for the initial Hessian

Tao, TAOLMVM, TAOBLMVM, TaoLMVMGetH0(), TaoLMVMGetH0KSP()

src/tao/bound/impls/blmvm/blmvm.c

src/tao/tutorials/ex3.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctaolinesearch.h" 
PetscErrorCode TaoLMVMSetH0(Tao tao, Mat H0)
```

Example 2 (unknown):
```unknown
TaoLMVMGetH0()
```

Example 3 (unknown):
```unknown
TaoLMVMGetH0KSP()
```

---

## TAOLMVM#

**URL:** https://petsc.org/release/manualpages/Tao/TAOLMVM/

**Contents:**
- TAOLMVM#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#

Limited Memory Variable Metric method is a quasi-Newton optimization solver for unconstrained minimization. It solves the Newton step \( H d_k = - g \) using an approximation \(B_k\) in place of \(H\), where \(B_k\) is composed using the BFGS update formula. A More-Thuente line search is then used to compute the steplength in the \(d_k\) direction

-tao_lmvm_recycle - enable recycling LMVM updates between TaoSolve() calls

-tao_lmvm_no_scale - (developer) disables diagonal Broyden scaling on the LMVM approximation

Tao, TAONTR, TAONTL, TAONM, TaoType, TaoCreate()

src/tao/unconstrained/impls/lmvm/lmvm.c

src/tao/unconstrained/tutorials/rosenbrock1_taoterm.c src/tao/unconstrained/tutorials/minsurf1.c src/tao/unconstrained/tutorials/rosenbrock1f.F90 src/tao/unconstrained/tutorials/eptorsion1.c src/tao/unconstrained/tutorials/rosenbrock1.c src/tao/unconstrained/tutorials/rosenbrock2.c src/tao/unconstrained/tutorials/eptorsion3.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

---

## TaoMatGetSubMat#

**URL:** https://petsc.org/release/manualpages/Tao/TaoMatGetSubMat/

**Contents:**
- TaoMatGetSubMat#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets a submatrix using the IS

M - the full matrix (n x n)

is - the index set for the submatrix (both row and column index sets need to be the same)

v1 - work vector of dimension n, needed for TAO_SUBSET_MASK option

subset_type - the method Tao is using for subsetting

TaoVecGetSubVec(), TaoSubsetType

src/tao/bound/utils/isutil.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoMatGetSubMat(Mat M, IS is, Vec v1, TaoSubsetType subset_type, Mat *Msub)
```

Example 2 (unknown):
```unknown
TAO_SUBSET_MASK
```

Example 3 (unknown):
```unknown
TaoVecGetSubVec()
```

Example 4 (unknown):
```unknown
TaoSubsetType
```

---

## TaoMonitorCancel#

**URL:** https://petsc.org/release/manualpages/Tao/TaoMonitorCancel/

**Contents:**
- TaoMonitorCancel#
- Synopsis#
- Input Parameter#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Clears all the monitor functions for a Tao object.

tao - the Tao solver context

-tao_monitor_cancel - cancels all monitors that have been hardwired into a code by calls to TaoMonitorSet(), but does not cancel those set via the options database

There is no way to clear one specific monitor from a Tao object.

TAO: Optimization Solvers, Tao, TaoMonitorDefault(), TaoMonitorSet()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoMonitorCancel(Tao tao)
```

Example 2 (unknown):
```unknown
TaoMonitorSet()
```

Example 3 (unknown):
```unknown
TaoMonitorDefault()
```

Example 4 (unknown):
```unknown
TaoMonitorSet()
```

---

## TaoMonitorConstraintNorm#

**URL:** https://petsc.org/release/manualpages/Tao/TaoMonitorConstraintNorm/

**Contents:**
- TaoMonitorConstraintNorm#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

same as TaoMonitorDefault() except it prints the norm of the constraint function.

tao - the Tao context

vf - PetscViewerAndFormat context

-tao_monitor_constraint_norm - monitor the constraints

TAO: Optimization Solvers, Tao, TaoMonitorDefault(), TaoMonitorSet()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoMonitorDefault()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoMonitorConstraintNorm(Tao tao, PetscViewerAndFormat *vf)
```

Example 3 (unknown):
```unknown
PetscViewerAndFormat
```

Example 4 (unknown):
```unknown
TaoMonitorDefault()
```

---

## TaoMonitorDefaultShort#

**URL:** https://petsc.org/release/manualpages/Tao/TaoMonitorDefaultShort/

**Contents:**
- TaoMonitorDefaultShort#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Routine for monitoring progress of TaoSolve() that displays fewer digits than TaoMonitorDefault()

tao - the Tao context

vf - PetscViewerAndFormat context

-tao_monitor_short - turn on default short monitoring

Same as TaoMonitorDefault() except it prints fewer digits of the residual as the residual gets smaller. This is because the later digits are meaningless and are often different on different machines; by using this routine different machines will usually generate the same output.

TAO: Optimization Solvers, Tao, TaoMonitorDefault(), TaoMonitorSet()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoMonitorDefault()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoMonitorDefaultShort(Tao tao, PetscViewerAndFormat *vf)
```

Example 3 (unknown):
```unknown
PetscViewerAndFormat
```

Example 4 (unknown):
```unknown
TaoMonitorDefault()
```

---

## TaoMonitorDefault#

**URL:** https://petsc.org/release/manualpages/Tao/TaoMonitorDefault/

**Contents:**
- TaoMonitorDefault#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Default routine for monitoring progress of TaoSolve()

tao - the Tao context

vf - PetscViewerAndFormat context

-tao_monitor - turn on default monitoring

This monitor prints the function value and gradient norm at each iteration.

TAO: Optimization Solvers, Tao, TaoMonitorDefaultShort(), TaoMonitorSet()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoMonitorDefault(Tao tao, PetscViewerAndFormat *vf)
```

Example 2 (unknown):
```unknown
PetscViewerAndFormat
```

Example 3 (unknown):
```unknown
TaoMonitorDefaultShort()
```

Example 4 (unknown):
```unknown
TaoMonitorSet()
```

---

## TaoMonitorDrawCtxCreate#

**URL:** https://petsc.org/release/manualpages/Tao/TaoMonitorDrawCtxCreate/

**Contents:**
- TaoMonitorDrawCtxCreate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#

Creates the monitor context for TaoMonitorSolutionDraw()

comm - the communicator to share the context

host - the name of the X Windows host that will display the monitor

label - the label to put at the top of the display window

x - the horizontal coordinate of the lower left corner of the window to open

y - the vertical coordinate of the lower left corner of the window to open

m - the width of the window

n - the height of the window

howoften - how many Tao iterations between displaying the monitor information

ctx - the monitor context

-tao_monitor_solution_draw - use TaoMonitorSolutionDraw() to monitor the solution

-tao_draw_solution_initial - show initial guess as well as current solution

The context this creates, along with TaoMonitorSolutionDraw(), and TaoMonitorDrawCtxDestroy() are passed to TaoMonitorSet().

TAO: Optimization Solvers, Tao, TaoMonitorSet(), TaoMonitorDefault(), VecView(), TaoMonitorDrawCtx()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoMonitorSolutionDraw()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoMonitorDrawCtxCreate(MPI_Comm comm, const char host[], const char label[], int x, int y, int m, int n, PetscInt howoften, TaoMonitorDrawCtx *ctx)
```

Example 3 (unknown):
```unknown
TaoMonitorSolutionDraw()
```

Example 4 (unknown):
```unknown
TaoMonitorSolutionDraw()
```

---

## TaoMonitorDrawCtxDestroy#

**URL:** https://petsc.org/release/manualpages/Tao/TaoMonitorDrawCtxDestroy/

**Contents:**
- TaoMonitorDrawCtxDestroy#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#

Destroys the monitor context for TaoMonitorSolutionDraw()

ictx - the monitor context

This is passed to TaoMonitorSet() as the final argument, along with TaoMonitorSolutionDraw(), and the context obtained with TaoMonitorDrawCtxCreate().

TAO: Optimization Solvers, Tao, TaoMonitorSet(), TaoMonitorDefault(), VecView(), TaoMonitorSolutionDraw()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoMonitorSolutionDraw()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoMonitorDrawCtxDestroy(TaoMonitorDrawCtx *ictx)
```

Example 3 (unknown):
```unknown
TaoMonitorSet()
```

Example 4 (unknown):
```unknown
TaoMonitorSolutionDraw()
```

---

## TaoMonitorDrawCtx#

**URL:** https://petsc.org/release/manualpages/Tao/TaoMonitorDrawCtx/

**Contents:**
- TaoMonitorDrawCtx#
- Synopsis#
- See Also#
- Level#
- Location#

Context object for the Tao graphical monitor routines that draw convergence information on a PetscDraw

Tao, TaoMonitorDrawCtxCreate(), TaoMonitorDrawCtxDestroy(), TaoMonitorSet()

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _n_TaoMonitorDrawCtx *TaoMonitorDrawCtx;
```

Example 2 (unknown):
```unknown
TaoMonitorDrawCtxCreate()
```

Example 3 (unknown):
```unknown
TaoMonitorDrawCtxDestroy()
```

Example 4 (unknown):
```unknown
TaoMonitorSet()
```

---

## TaoMonitorGlobalization#

**URL:** https://petsc.org/release/manualpages/Tao/TaoMonitorGlobalization/

**Contents:**
- TaoMonitorGlobalization#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Default routine for monitoring progress of TaoSolve() with extra detail on the globalization method.

tao - the Tao context

vf - PetscViewerAndFormat context

-tao_monitor_globalization - turn on monitoring with globalization information

This monitor prints the function value and gradient norm at each iteration, as well as the step size and trust radius. Note that the step size and trust radius may be the same for some algorithms.

TAO: Optimization Solvers, Tao, TaoMonitorDefaultShort(), TaoMonitorSet()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoMonitorGlobalization(Tao tao, PetscViewerAndFormat *vf)
```

Example 2 (unknown):
```unknown
PetscViewerAndFormat
```

Example 3 (unknown):
```unknown
TaoMonitorDefaultShort()
```

Example 4 (unknown):
```unknown
TaoMonitorSet()
```

---

## TaoMonitorGradientDraw#

**URL:** https://petsc.org/release/manualpages/Tao/TaoMonitorGradientDraw/

**Contents:**
- TaoMonitorGradientDraw#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Plots the gradient at each iteration of TaoSolve()

tao - the Tao context

ctx - PetscViewer context

-tao_monitor_gradient_draw - draw the gradient at each iteration

TAO: Optimization Solvers, Tao, TaoMonitorGradient(), TaoMonitorSet(), TaoMonitorSolutionDraw()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoMonitorGradientDraw(Tao tao, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
TaoMonitorGradient()
```

Example 4 (unknown):
```unknown
TaoMonitorSet()
```

---

## TaoMonitorGradient#

**URL:** https://petsc.org/release/manualpages/Tao/TaoMonitorGradient/

**Contents:**
- TaoMonitorGradient#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Views the gradient at each iteration of TaoSolve()

tao - the Tao context

vf - PetscViewerAndFormat context

-tao_monitor_gradient - view the gradient at each iteration

TAO: Optimization Solvers, Tao, TaoMonitorDefaultShort(), TaoMonitorSet()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoMonitorGradient(Tao tao, PetscViewerAndFormat *vf)
```

Example 2 (unknown):
```unknown
PetscViewerAndFormat
```

Example 3 (unknown):
```unknown
TaoMonitorDefaultShort()
```

Example 4 (unknown):
```unknown
TaoMonitorSet()
```

---

## TaoMonitorResidual#

**URL:** https://petsc.org/release/manualpages/Tao/TaoMonitorResidual/

**Contents:**
- TaoMonitorResidual#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Views the least-squares residual at each iteration of TaoSolve()

tao - the Tao context

vf - PetscViewerAndFormat context

-tao_monitor_ls_residual - view the residual at each iteration

TAO: Optimization Solvers, Tao, TaoMonitorDefaultShort(), TaoMonitorSet()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoMonitorResidual(Tao tao, PetscViewerAndFormat *vf)
```

Example 2 (unknown):
```unknown
PetscViewerAndFormat
```

Example 3 (unknown):
```unknown
TaoMonitorDefaultShort()
```

Example 4 (unknown):
```unknown
TaoMonitorSet()
```

---

## TaoMonitorSetFromOptions#

**URL:** https://petsc.org/release/manualpages/Tao/TaoMonitorSetFromOptions/

**Contents:**
- TaoMonitorSetFromOptions#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets a monitor function and viewer appropriate for the type indicated by the user

tao - Tao object you wish to monitor

name - the monitor type one is seeking

help - message indicating what monitoring is done

manual - manual page for the monitor

monitor - the monitor function, this must use a PetscViewerFormat as its context

TAO: Optimization Solvers, Tao, TaoMonitorSet(), PetscOptionsCreateViewer(), PetscOptionsGetReal(), PetscOptionsHasName(), PetscOptionsGetString(), PetscOptionsGetIntArray(), PetscOptionsGetRealArray(), PetscOptionsBool(), PetscOptionsInt(), PetscOptionsString(), PetscOptionsReal(), PetscOptionsName(), PetscOptionsBegin(), PetscOptionsEnd(), PetscOptionsHeadBegin(), PetscOptionsStringArray(), PetscOptionsRealArray(), PetscOptionsScalar(), PetscOptionsBoolGroupBegin(), PetscOptionsBoolGroup(), PetscOptionsBoolGroupEnd(), PetscOptionsFList(), PetscOptionsEList()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoMonitorSetFromOptions(Tao tao, const char name[], const char help[], const char manual[], PetscErrorCode (*monitor)(Tao, PetscViewerAndFormat *))
```

Example 2 (unknown):
```unknown
PetscViewerFormat
```

Example 3 (unknown):
```unknown
TaoMonitorSet()
```

Example 4 (unknown):
```unknown
PetscOptionsCreateViewer()
```

---

## TaoMonitorSet#

**URL:** https://petsc.org/release/manualpages/Tao/TaoMonitorSet/

**Contents:**
- TaoMonitorSet#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Notes#
- Fortran Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets an additional function that is to be used at every iteration of the solver to display the iteration’s progress.

tao - the Tao solver context

func - monitoring routine

ctx - [optional] user-defined context for private data for the monitor routine (may be NULL)

dest - [optional] function to destroy the context when the Tao is destroyed, see PetscCtxDestroyFn for the calling sequence

tao - the Tao solver context

ctx - [optional] monitoring context

See TaoSetFromOptions() for a monitoring options.

Several different monitoring routines may be set by calling TaoMonitorSet() multiple times; all will be called in the order in which they were set.

Only one monitor function may be set

TAO: Optimization Solvers, Tao, TaoSolve(), TaoMonitorDefault(), TaoMonitorCancel(), TaoView(), PetscCtxDestroyFn

src/tao/interface/taosolver.c

src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/tao/bound/tutorials/jbearing2.c src/tao/unconstrained/tutorials/minsurf2.c src/tao/unconstrained/tutorials/eptorsion2f.F90 src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoMonitorSet(Tao tao, PetscErrorCode (*func)(Tao tao, PetscCtx ctx), PetscCtx ctx, PetscCtxDestroyFn *dest)
```

Example 2 (unknown):
```unknown
PetscCtxDestroyFn
```

Example 3 (unknown):
```unknown
TaoSetFromOptions()
```

Example 4 (unknown):
```unknown
TaoMonitorSet()
```

---

## TaoMonitorSolutionDraw#

**URL:** https://petsc.org/release/manualpages/Tao/TaoMonitorSolutionDraw/

**Contents:**
- TaoMonitorSolutionDraw#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Plots the solution at each iteration of TaoSolve()

tao - the Tao context

ctx - TaoMonitorDraw context

-tao_monitor_solution_draw - draw the solution at each iteration

The context created by TaoMonitorDrawCtxCreate(), along with TaoMonitorSolutionDraw(), and TaoMonitorDrawCtxDestroy() are passed to TaoMonitorSet() to monitor the solution graphically.

TAO: Optimization Solvers, Tao, TaoMonitorSolution(), TaoMonitorSet(), TaoMonitorGradientDraw(), TaoMonitorDrawCtxCreate(), TaoMonitorDrawCtxDestroy()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoMonitorSolutionDraw(Tao tao, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoMonitorDraw
```

Example 3 (unknown):
```unknown
TaoMonitorDrawCtxCreate()
```

Example 4 (unknown):
```unknown
TaoMonitorSolutionDraw()
```

---

## TaoMonitorSolution#

**URL:** https://petsc.org/release/manualpages/Tao/TaoMonitorSolution/

**Contents:**
- TaoMonitorSolution#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Views the solution at each iteration of TaoSolve()

tao - the Tao context

vf - PetscViewerAndFormat context

-tao_monitor_solution - view the solution

TAO: Optimization Solvers, Tao, TaoMonitorDefaultShort(), TaoMonitorSet()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoMonitorSolution(Tao tao, PetscViewerAndFormat *vf)
```

Example 2 (unknown):
```unknown
PetscViewerAndFormat
```

Example 3 (unknown):
```unknown
TaoMonitorDefaultShort()
```

Example 4 (unknown):
```unknown
TaoMonitorSet()
```

---

## TaoMonitorStepDraw#

**URL:** https://petsc.org/release/manualpages/Tao/TaoMonitorStepDraw/

**Contents:**
- TaoMonitorStepDraw#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Plots the step direction at each iteration of TaoSolve()

tao - the Tao context

ctx - the PetscViewer context

-tao_monitor_step_draw - draw the step direction at each iteration

TAO: Optimization Solvers, Tao, TaoMonitorSet(), TaoMonitorSolutionDraw

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoMonitorStepDraw(Tao tao, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
TaoMonitorSet()
```

Example 4 (unknown):
```unknown
TaoMonitorSolutionDraw
```

---

## TaoMonitorStep#

**URL:** https://petsc.org/release/manualpages/Tao/TaoMonitorStep/

**Contents:**
- TaoMonitorStep#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Views the step-direction at each iteration of TaoSolve()

tao - the Tao context

vf - PetscViewerAndFormat context

-tao_monitor_step - view the step vector at each iteration

TAO: Optimization Solvers, Tao, TaoMonitorDefaultShort(), TaoMonitorSet()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoMonitorStep(Tao tao, PetscViewerAndFormat *vf)
```

Example 2 (unknown):
```unknown
PetscViewerAndFormat
```

Example 3 (unknown):
```unknown
TaoMonitorDefaultShort()
```

Example 4 (unknown):
```unknown
TaoMonitorSet()
```

---

## TaoMonitor#

**URL:** https://petsc.org/release/manualpages/Tao/TaoMonitor/

**Contents:**
- TaoMonitor#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Monitor the solver and the current solution. This routine will record the iteration number and residual statistics, and call any monitors specified by the user.

tao - the Tao context

its - the current iterate number (>=0)

f - the current objective function value

res - the gradient norm, square root of the duality gap, or other measure indicating distance from optimality. This measure will be recorded and used for some termination tests.

cnorm - the infeasibility of the current solution with regard to the constraints.

steplength - multiple of the step direction added to the previous iterate.

-tao_monitor - Use the default monitor, which prints statistics to standard output

TAO: Optimization Solvers, Tao, TaoGetConvergedReason(), TaoMonitorDefault(), TaoMonitorSet()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoMonitor(Tao tao, PetscInt its, PetscReal f, PetscReal res, PetscReal cnorm, PetscReal steplength)
```

Example 2 (unknown):
```unknown
TaoGetConvergedReason()
```

Example 3 (unknown):
```unknown
TaoMonitorDefault()
```

Example 4 (unknown):
```unknown
TaoMonitorSet()
```

---

## TAONLS#

**URL:** https://petsc.org/release/manualpages/Tao/TAONLS/

**Contents:**
- TAONLS#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#

Newton’s method with linesearch for unconstrained minimization. At each iteration, the Newton line search method solves the symmetric system of equations to obtain the step direction dk: \( H_k d_k = -g_k \) a More-Thuente line search is applied on the direction dk to approximately solve \( \min_t f(x_k + t d_k)\).

-tao_nls_init_type - “constant”,”direction”,”interpolation”

-tao_nls_update_type - “step”,”direction”,”interpolation”

-tao_nls_sval - perturbation starting value

-tao_nls_imin - minimum initial perturbation

-tao_nls_imax - maximum initial perturbation

-tao_nls_pmin - minimum perturbation

-tao_nls_pmax - maximum perturbation

-tao_nls_pgfac - growth factor

-tao_nls_psfac - shrink factor

-tao_nls_imfac - initial merit factor

-tao_nls_pmgfac - merit growth factor

-tao_nls_pmsfac - merit shrink factor

-tao_nls_eta1 - poor steplength; reduce radius

-tao_nls_eta2 - reasonable steplength; leave radius

-tao_nls_eta3 - good steplength; increase radius

-tao_nls_eta4 - excellent steplength; greatly increase radius

-tao_nls_alpha1 - alpha1 reduction

-tao_nls_alpha2 - alpha2 reduction

-tao_nls_alpha3 - alpha3 reduction

-tao_nls_alpha4 - alpha4 reduction

-tao_nls_alpha - alpha5 reduction

-tao_nls_mu1 - mu1 interpolation update

-tao_nls_mu2 - mu2 interpolation update

-tao_nls_gamma1 - gamma1 interpolation update

-tao_nls_gamma2 - gamma2 interpolation update

-tao_nls_gamma3 - gamma3 interpolation update

-tao_nls_gamma4 - gamma4 interpolation update

-tao_nls_theta - theta interpolation update

-tao_nls_omega1 - omega1 step update

-tao_nls_omega2 - omega2 step update

-tao_nls_omega3 - omega3 step update

-tao_nls_omega4 - omega4 step update

-tao_nls_omega5 - omega5 step update

-tao_nls_mu1_i - mu1 interpolation init factor

-tao_nls_mu2_i - mu2 interpolation init factor

-tao_nls_gamma1_i - gamma1 interpolation init factor

-tao_nls_gamma2_i - gamma2 interpolation init factor

-tao_nls_gamma3_i - gamma3 interpolation init factor

-tao_nls_gamma4_i - gamma4 interpolation init factor

-tao_nls_theta_i - theta interpolation init factor

The various algorithmic factors can only be supplied via the options database

Tao, TAONTR, TAONTL, TAONM, TaoType, TaoCreate()

src/tao/unconstrained/impls/nls/nls.c

src/tao/constrained/tutorials/tomographyADMM.c src/tao/tutorials/ex4.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

---

## TAONM#

**URL:** https://petsc.org/release/manualpages/Tao/TAONM/

**Contents:**
- TAONM#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#

Nelder-Mead solver for derivative free, unconstrained minimization

-tao_nm_lambda - initial step length

-tao_nm_mu - expansion/contraction factor

Tao, TAONLS, TAONTL, TaoType, TaoCreate()

src/tao/unconstrained/impls/neldermead/neldermead.c

src/tao/tutorials/ex4.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

---

## TAONTL#

**URL:** https://petsc.org/release/manualpages/Tao/TAONTL/

**Contents:**
- TAONTL#
- Options Database Keys#
- See Also#
- Level#
- Location#

Newton’s method with trust region globalization and line search fallback. At each iteration, the Newton trust region method solves the system for d and performs a line search in the d direction: \(\min_d .5 d^T H_k d + g_k^T d, s.t. ||d|| < \Delta_k.\)

-tao_ntl_init_type - “constant”,”direction”,”interpolation”

-tao_ntl_update_type - “reduction”,”interpolation”

-tao_ntl_min_radius - lower bound on trust region radius

-tao_ntl_max_radius - upper bound on trust region radius

-tao_ntl_epsilon - tolerance for accepting actual / predicted reduction

-tao_ntl_mu1_i - mu1 interpolation initial factor

-tao_ntl_mu2_i - mu2 interpolation initial factor

-tao_ntl_gamma1_i - gamma1 interpolation initial factor

-tao_ntl_gamma2_i - gamma2 interpolation initial factor

-tao_ntl_gamma3_i - gamma3 interpolation initial factor

-tao_ntl_gamma4_i - gamma4 interpolation initial factor

-tao_ntl_theta_i - theta1 interpolation initial factor

-tao_ntl_eta1 - eta1 reduction update factor

-tao_ntl_eta2 - eta2 reduction update factor

-tao_ntl_eta3 - eta3 reduction update factor

-tao_ntl_eta4 - eta4 reduction update factor

-tao_ntl_alpha1 - alpha1 reduction update factor

-tao_ntl_alpha2 - alpha2 reduction update factor

-tao_ntl_alpha3 - alpha3 reduction update factor

-tao_ntl_alpha4 - alpha4 reduction update factor

-tao_ntl_mu1 - mu1 interpolation update

-tao_ntl_mu2 - mu2 interpolation update

-tao_ntl_gamma1 - gamma1 interpolation update

-tao_ntl_gamma2 - gamma2 interpolation update

-tao_ntl_gamma3 - gamma3 interpolation update

-tao_ntl_gamma4 - gamma4 interpolation update

-tao_ntl_theta - theta1 interpolation update

The various algorithmic factors can only be supplied via the options database

Tao, TAONTR, TAONLS, TAONM, TAOCG, TaoType, TaoCreate()

src/tao/unconstrained/impls/ntl/ntl.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

---

## TAONTR#

**URL:** https://petsc.org/release/manualpages/Tao/TAONTR/

**Contents:**
- TAONTR#
- Options Database Keys#
- See Also#
- Level#
- Location#

Newton’s method with trust region for unconstrained minimization. At each iteration, the Newton trust region method solves the system \(\min_d .5 d^T Hk d + gk^T d, s.t. ||d|| < \Delta_k.\)

-tao_ntr_init_type - “constant”,”direction”,”interpolation”

-tao_ntr_update_type - “reduction”,”interpolation”

-tao_ntr_min_radius - lower bound on trust region radius

-tao_ntr_max_radius - upper bound on trust region radius

-tao_ntr_epsilon - tolerance for accepting actual / predicted reduction

-tao_ntr_mu1_i - mu1 interpolation initial factor

-tao_ntr_mu2_i - mu2 interpolation initial factor

-tao_ntr_gamma1_i - gamma1 interpolation initial factor

-tao_ntr_gamma2_i - gamma2 interpolation initial factor

-tao_ntr_gamma3_i - gamma3 interpolation initial factor

-tao_ntr_gamma4_i - gamma4 interpolation initial factor

-tao_ntr_theta_i - theta1 interpolation initial factor

-tao_ntr_eta1 - eta1 reduction update factor

-tao_ntr_eta2 - eta2 reduction update factor

-tao_ntr_eta3 - eta3 reduction update factor

-tao_ntr_eta4 - eta4 reduction update factor

-tao_ntr_alpha1 - alpha1 reduction update factor

-tao_ntr_alpha2 - alpha2 reduction update factor

-tao_ntr_alpha3 - alpha3 reduction update factor

-tao_ntr_alpha4 - alpha4 reduction update factor

-tao_ntr_mu1 - mu1 interpolation update

-tao_ntr_mu2 - mu2 interpolation update

-tao_ntr_gamma1 - gamma1 interpolation update

-tao_ntr_gamma2 - gamma2 interpolation update

-tao_ntr_gamma3 - gamma3 interpolation update

-tao_ntr_gamma4 - gamma4 interpolation update

-tao_ntr_theta - theta interpolation update

The various algorithmic factors can only be supplied via the options database

Tao, TAONLS, TAONTL, TAONM, TaoType, TaoCreate()

src/tao/unconstrained/impls/ntr/ntr.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

---

## TAOOWLQN#

**URL:** https://petsc.org/release/manualpages/Tao/TAOOWLQN/

**Contents:**
- TAOOWLQN#
- See Also#
- Level#
- Location#

orthant-wise limited memory quasi-Newton algorithm

- tao_owlqn_lambda - regulariser weight

Tao, TaoType, TaoCreate()

src/tao/unconstrained/impls/owlqn/owlqn.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

---

## TaoParametersInitialize#

**URL:** https://petsc.org/release/manualpages/Tao/TaoParametersInitialize/

**Contents:**
- TaoParametersInitialize#
- Synopsis#
- Input Parameter#
- Developer Note#
- See Also#
- Level#
- Location#

Sets all the parameters in tao to their default value (when TaoCreate() was called) if they currently contain default values. Default values are the parameter values when the object’s type is set.

This is called by all the TaoCreate_XXX() routines.

SNES: Nonlinear Solvers, Tao, TaoSolve(), TaoDestroy(), PetscObjectParameterSetDefault()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoParametersInitialize(Tao tao)
```

Example 3 (unknown):
```unknown
TaoCreate_XXX()
```

Example 4 (unknown):
```unknown
TaoDestroy()
```

---

## TAOPDIPM#

**URL:** https://petsc.org/release/manualpages/Tao/TAOPDIPM/

**Contents:**
- TAOPDIPM#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#

Barrier-based primal-dual interior point algorithm for generally constrained optimization.

-tao_pdipm_push_init_lambdai - parameter to push initial dual variables away from bounds (> 0)

-tao_pdipm_push_init_slack - parameter to push initial slack variables away from bounds (> 0)

-tao_pdipm_mu_update_factor - update scalar for barrier parameter (mu) update (> 0)

-tao_pdipm_symmetric_kkt - Solve non-reduced symmetric KKT system

-tao_pdipm_kkt_shift_pd - Add shifts to make KKT matrix positive definite

TAOPDIPM, Tao, TaoType

src/tao/constrained/impls/ipm/pdipm.c

src/tao/constrained/tutorials/ex1.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

---

## TAOPOUNDERS#

**URL:** https://petsc.org/release/manualpages/Tao/TAOPOUNDERS/

**Contents:**
- TAOPOUNDERS#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#

POUNDERS derivate-free model-based algorithm for nonlinear least squares

-tao_pounders_delta - initial step length

-tao_pounders_npmax - maximum number of points in model

-tao_pounders_gqt - use gqt algorithm for subproblem instead of TRON

Tao, TAONTR, TAONTL, TAONM, TaoType, TaoCreate()

src/tao/leastsquares/impls/pounders/pounders.c

src/tao/leastsquares/tutorials/chwirut1f.F90 src/tao/leastsquares/tutorials/chwirut2.c src/tao/leastsquares/tutorials/chwirut2f.F90 src/tao/leastsquares/tutorials/chwirut1.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

---

## TaoPythonGetType#

**URL:** https://petsc.org/release/manualpages/Tao/TaoPythonGetType/

**Contents:**
- TaoPythonGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the type of a Tao object implemented in Python.

tao - the optimization solver (Tao) context.

pyname - full dotted Python name [package].module[.{class|function}]

TaoCreate(), TaoSetType(), TAOPYTHON, PetscPythonInitialize(), TaoPythonSetType()

src/tao/python/pythontao.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoPythonGetType(Tao tao, const char *pyname[])
```

Example 2 (unknown):
```unknown
TaoCreate()
```

Example 3 (unknown):
```unknown
TaoSetType()
```

Example 4 (unknown):
```unknown
PetscPythonInitialize()
```

---

## TaoPythonSetType#

**URL:** https://petsc.org/release/manualpages/Tao/TaoPythonSetType/

**Contents:**
- TaoPythonSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Initialize a Tao object implemented in Python.

tao - the optimization solver (Tao) context.

pyname - full dotted Python name [package].module[.{class|function}]

-tao_python_type pyname - python class

TaoCreate(), TaoSetType(), TAOPYTHON, PetscPythonInitialize()

src/tao/python/pythontao.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoPythonSetType(Tao tao, const char pyname[])
```

Example 2 (unknown):
```unknown
TaoCreate()
```

Example 3 (unknown):
```unknown
TaoSetType()
```

Example 4 (unknown):
```unknown
PetscPythonInitialize()
```

---

## TAOPYTHON#

**URL:** https://petsc.org/release/manualpages/Tao/TAOPYTHON/

**Contents:**
- TAOPYTHON#
- See Also#
- Level#
- Location#

a TAOType that is implemented as a Python class using TaoPythonSetType()

SNES: Nonlinear Solvers, Tao, TaoCreate(), TAOSHELL, TaoSetType(), PetscPythonInitialize(), TaoPythonSetType(), TaoPythonGetType(), TSPYTHON, SNESPYTHON

src/tao/python/pythontao.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoPythonSetType()
```

Example 2 (unknown):
```unknown
TaoCreate()
```

Example 3 (unknown):
```unknown
TaoSetType()
```

Example 4 (unknown):
```unknown
PetscPythonInitialize()
```

---

## TaoRegisterAll#

**URL:** https://petsc.org/release/manualpages/Tao/TaoRegisterAll/

**Contents:**
- TaoRegisterAll#
- Synopsis#
- See Also#
- Level#
- Location#

Registers all of the optimization methods in the Tao package.

Tao, TaoRegister(), TaoRegisterDestroy()

src/tao/interface/taosolverregi.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoRegisterAll(void)
```

Example 2 (unknown):
```unknown
TaoRegister()
```

Example 3 (unknown):
```unknown
TaoRegisterDestroy()
```

---

## TaoRegisterDestroy#

**URL:** https://petsc.org/release/manualpages/Tao/TaoRegisterDestroy/

**Contents:**
- TaoRegisterDestroy#
- Synopsis#
- See Also#
- Level#
- Location#

Frees the list of minimization solvers that were registered by TaoRegister().

TAO: Optimization Solvers, Tao, TaoRegisterAll(), TaoRegister()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoRegister()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoRegisterDestroy(void)
```

Example 3 (unknown):
```unknown
TaoRegisterAll()
```

Example 4 (unknown):
```unknown
TaoRegister()
```

---

## TaoRegister#

**URL:** https://petsc.org/release/manualpages/Tao/TaoRegister/

**Contents:**
- TaoRegister#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Example Usage#
- Note#
- See Also#
- Level#
- Location#

Adds a method to the Tao package for minimization.

Not Collective, No Fortran Support

sname - name of a new user-defined solver

func - routine to create TaoType specific method context

tao - the Tao object to be created

Then, your solver can be chosen with the procedural interface via

or at runtime via the option

TaoRegister() may be called multiple times to add several user-defined solvers.

TAO: Optimization Solvers, Tao, TaoSetType(), TaoRegisterAll(), TaoRegisterDestroy()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoRegister(const char sname[], PetscErrorCode (*func)(Tao tao))
```

Example 2 (unknown):
```unknown
TaoRegister("my_solver", MySolverCreate);
```

Example 3 (unknown):
```unknown
TaoSetType(tao, "my_solver")
```

Example 4 (unknown):
```unknown
-tao_type my_solver
```

---

## TaoResetStatistics#

**URL:** https://petsc.org/release/manualpages/Tao/TaoResetStatistics/

**Contents:**
- TaoResetStatistics#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#

Initialize the statistics collected by the Tao object. These statistics include the iteration number, residual norms, and convergence status. This routine gets called before solving each optimization problem.

tao - the Tao context

This function does not reset the statistics of internal TaoTerm

TAO: Optimization Solvers, Tao, TaoCreate(), TaoSolve()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoResetStatistics(Tao tao)
```

Example 2 (unknown):
```unknown
TaoCreate()
```

---

## TaoSetApplicationContext#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetApplicationContext/

**Contents:**
- TaoSetApplicationContext#
- Synopsis#
- Input Parameters#
- Fortran Note#
- See Also#
- Level#
- Location#

Sets the optional user-defined context for a Tao solver that can be accessed later, for example in the Tao callback functions with TaoGetApplicationContext()

tao - the Tao context

ctx - the application context

This only works when ctx is a Fortran derived type (it cannot be a PetscObject), we recommend writing a Fortran interface definition for this function that tells the Fortran compiler the derived data type that is passed in as the ctx argument. See TaoGetApplicationContext() for an example.

TAO: Optimization Solvers, Tao, TaoGetApplicationContext()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoGetApplicationContext()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetApplicationContext(Tao tao, PetscCtx ctx)
```

Example 3 (unknown):
```unknown
PetscObject
```

Example 4 (unknown):
```unknown
TaoGetApplicationContext()
```

---

## TaoSetConstraintsRoutine#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetConstraintsRoutine/

**Contents:**
- TaoSetConstraintsRoutine#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

Sets a function to be used to compute constraints. Tao only handles constraints under certain conditions, see TAO: Optimization Solvers for details

tao - the Tao context

c - A vector that will be used to store constraint evaluation

func - the bounds computation routine

ctx - [optional] user-defined context for private data for the constraints computation (may be NULL)

x - point to evaluate constraints

c - vector constraints evaluated at x

ctx - the (optional) user-defined function context

TAO: Optimization Solvers, Tao, TaoSetObjective(), TaoSetHessian(), TaoSetObjectiveAndGradient(), TaoSetVariablevBounds()

src/tao/interface/taosolver_bounds.c

src/tao/complementarity/tutorials/blackscholes.c src/tao/pde_constrained/tutorials/elliptic.c src/tao/pde_constrained/tutorials/parabolic.c src/tao/complementarity/tutorials/minsurf1.c src/tao/pde_constrained/tutorials/hyperbolic.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetConstraintsRoutine(Tao tao, Vec c, PetscErrorCode (*func)(Tao tao, Vec x, Vec c, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoSetObjective()
```

Example 3 (unknown):
```unknown
TaoSetHessian()
```

Example 4 (unknown):
```unknown
TaoSetObjectiveAndGradient()
```

---

## TaoSetConstraintTolerances#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetConstraintTolerances/

**Contents:**
- TaoSetConstraintTolerances#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Notes#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Sets constraint tolerance parameters used in TaoSolve() convergence tests

tao - the Tao context

catol - absolute constraint tolerance, constraint norm must be less than catol for used for gatol convergence criteria

crtol - relative constraint tolerance, constraint norm must be less than crtol for used for gatol, gttol convergence criteria

-tao_catol catol - Sets catol

-tao_crtol crtol - Sets crtol

Use PETSC_CURRENT to leave one or tolerance unchanged.

Use PETSC_DETERMINE to set one or more tolerances to their values when the tao object’s type was set

Use PETSC_CURRENT_REAL or PETSC_DETERMINE_REAL

TAO: Optimization Solvers, Tao, TaoConvergedReason, TaoGetTolerances(), TaoGetConstraintTolerances(), TaoSetTolerances()

src/tao/interface/taosolver.c

src/tao/constrained/tutorials/ex1.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetConstraintTolerances(Tao tao, PetscReal catol, PetscReal crtol)
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
PETSC_CURRENT_REAL
```

---

## TaoSetConvergedReason#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetConvergedReason/

**Contents:**
- TaoSetConvergedReason#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the termination flag on a Tao object

tao - the Tao context

reason - the TaoConvergedReason

TAO: Optimization Solvers, Tao, TaoConvergedReason

src/tao/interface/taosolver.c

src/tao/bound/tutorials/jbearing2.c src/tao/unconstrained/tutorials/eptorsion2f.F90

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetConvergedReason(Tao tao, TaoConvergedReason reason)
```

Example 2 (unknown):
```unknown
TaoConvergedReason
```

Example 3 (unknown):
```unknown
TaoConvergedReason
```

---

## TaoSetConvergenceHistory#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetConvergenceHistory/

**Contents:**
- TaoSetConvergenceHistory#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the array used to hold the convergence history.

tao - the Tao solver context

obj - array to hold objective value history

resid - array to hold residual history

cnorm - array to hold constraint violation history

lits - integer array holds the number of linear iterations for each Tao iteration

na - size of obj, resid, and cnorm

reset - PETSC_TRUE indicates each new minimization resets the history counter to zero, else it continues storing new values for new minimizations after the old ones

If set, Tao will fill the given arrays with the indicated information at each iteration. If ‘obj’,’resid’,’cnorm’,’lits’ are all NULL then space (using size na, or 1000 if na is PETSC_DECIDE) is allocated for the history. If not all are NULL, then only the non-NULL information categories will be stored, the others will be ignored.

Any convergence information after iteration number ‘na’ will not be stored.

This routine is useful, e.g., when running a code for purposes of accurate performance monitoring, when no I/O should be done during the section of code that is being timed.

TAO: Optimization Solvers, TaoGetConvergenceHistory()

src/tao/interface/taosolver.c

src/tao/leastsquares/tutorials/tomography.c src/tao/leastsquares/tutorials/cs1.c src/tao/leastsquares/tutorials/chwirut1f.F90 src/tao/leastsquares/tutorials/chwirut1.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetConvergenceHistory(Tao tao, PetscReal obj[], PetscReal resid[], PetscReal cnorm[], PetscInt lits[], PetscInt na, PetscBool reset)
```

Example 2 (unknown):
```unknown
PETSC_DECIDE
```

Example 3 (unknown):
```unknown
TaoGetConvergenceHistory()
```

---

## TaoSetConvergenceTest#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetConvergenceTest/

**Contents:**
- TaoSetConvergenceTest#
- Synopsis#
- Input Parameters#
- Calling sequence of conv#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the function that is to be used to test for convergence of the iterative minimization solution. The new convergence testing routine will replace Tao’s default convergence test.

conv - the routine to test for convergence

ctx - [optional] context for private data for the convergence routine (may be NULL)

ctx - [optional] convergence context

The new convergence testing routine should call TaoSetConvergedReason().

TAO: Optimization Solvers, Tao, TaoSolve(), TaoSetConvergedReason(), TaoGetSolutionStatus(), TaoGetTolerances(), TaoMonitorSet()

src/tao/interface/taosolver.c

src/tao/bound/tutorials/jbearing2.c src/tao/unconstrained/tutorials/eptorsion2f.F90

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetConvergenceTest(Tao tao, PetscErrorCode (*conv)(Tao tao, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoSetConvergedReason()
```

Example 3 (unknown):
```unknown
TaoSetConvergedReason()
```

Example 4 (unknown):
```unknown
TaoGetSolutionStatus()
```

---

## TaoSetEqualityConstraintsRoutine#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetEqualityConstraintsRoutine/

**Contents:**
- TaoSetEqualityConstraintsRoutine#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

Sets a function to be used to compute constraints. Tao only handles constraints under certain conditions, see TAO: Optimization Solvers for details

tao - the Tao context

ce - A vector that will be used to store equality constraint evaluation

func - the bounds computation routine

ctx - [optional] user-defined context for private data for the equality constraints computation (may be NULL)

x - point to evaluate equality constraints

ce - vector of equality constraints evaluated at x

ctx - the (optional) user-defined function context

TAO: Optimization Solvers, Tao, TaoSetObjective(), TaoSetHessian(), TaoSetObjectiveAndGradient(), TaoSetVariableBounds()

src/tao/interface/taosolver_bounds.c

src/tao/constrained/tutorials/ex1.c src/tao/constrained/tutorials/maros.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetEqualityConstraintsRoutine(Tao tao, Vec ce, PetscErrorCode (*func)(Tao tao, Vec x, Vec ce, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoSetObjective()
```

Example 3 (unknown):
```unknown
TaoSetHessian()
```

Example 4 (unknown):
```unknown
TaoSetObjectiveAndGradient()
```

---

## TaoSetFromOptions#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetFromOptions/

**Contents:**
- TaoSetFromOptions#
- Synopsis#
- Input Parameter#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets various Tao parameters from the options database

tao - the Tao solver context

-tao_type type - The algorithm that Tao uses (lmvm, nls, etc.). See TAOType

-tao_gatol gatol - absolute error tolerance for ||gradient||

-tao_grtol grtol - relative error tolerance for ||gradient||

-tao_gttol gttol - reduction of ||gradient|| relative to initial gradient

-tao_max_it max - sets maximum number of iterations

-tao_max_funcs max - sets maximum number of function evaluations

-tao_fmin fmin - stop if function value reaches fmin

-tao_steptol tol - stop if trust region radius less than tol

-tao_trust0 radius - initial trust region radius

-tao_view_solution - view the solution at the end of the optimization process

-tao_monitor - prints function value and residual norm at each iteration

-tao_monitor_short - same as -tao_monitor, but truncates very small values

-tao_monitor_constraint_norm - prints objective value, gradient, and constraint norm at each iteration

-tao_monitor_globalization - prints information about the globalization at each iteration

-tao_monitor_solution - prints solution vector at each iteration

-tao_monitor_ls_residual - prints least-squares residual vector at each iteration

-tao_monitor_step - prints step vector at each iteration

-tao_monitor_gradient - prints gradient vector at each iteration

-tao_monitor_solution_draw - graphically view solution vector at each iteration

-tao_monitor_step_draw - graphically view step vector at each iteration

-tao_monitor_gradient_draw - graphically view gradient at each iteration

-tao_monitor_cancel - cancels all monitors (except those set with command line)

-tao_fd_gradient - use gradient computed with finite differences

-tao_fd_hessian - use hessian computed with finite differences

-tao_mf_hessian - use matrix-free Hessian computed with finite differences. No TaoTerm support

-tao_view - prints information about the Tao after solving

-tao_converged_reason - prints the reason Tao stopped iterating

-tao_add_terms - takes a comma-separated list of up to 16 options prefixes, a TaoTerm will be created for each and added to the objective function

To see all options, run your program with the -help option or consult the user’s manual. Should be called after TaoCreate() but before TaoSolve().

The -tao_add_terms option accepts at most 16 prefixes.

TAO: Optimization Solvers, Tao, TaoCreate(), TaoSolve()

src/tao/interface/taosolver.c

src/tao/leastsquares/tutorials/chwirut1f.F90 src/tao/leastsquares/tutorials/chwirut2f.F90 src/tao/leastsquares/tutorials/cs1.c src/tao/pde_constrained/tutorials/elliptic.c src/tao/constrained/tutorials/tomographyADMM.c src/tao/pde_constrained/tutorials/parabolic.c src/tao/constrained/tutorials/ex1.c src/tao/pde_constrained/tutorials/hyperbolic.c src/tao/constrained/tutorials/maros.c src/tao/leastsquares/tutorials/chwirut1.c

TaoSetFromOptions_BLMVM() in src/tao/bound/impls/blmvm/blmvm.c TaoSetFromOptions_BNCG() in src/tao/bound/impls/bncg/bncg.c TaoSetFromOptions_BNK() in src/tao/bound/impls/bnk/bnk.c TaoSetFromOptions_BNTL() in src/tao/bound/impls/bnk/bntl.c TaoSetFromOptions_BNTR() in src/tao/bound/impls/bnk/bntr.c TaoSetFromOptions_BQNK() in src/tao/bound/impls/bqnk/bqnk.c TaoSetFromOptions_BQNLS() in src/tao/bound/impls/bqnls/bqnls.c TaoSetFromOptions_TRON() in src/tao/bound/impls/tron/tron.c TaoSetFromOptions_SSLS() in src/tao/complementarity/impls/ssls/ssls.c TaoSetFromOptions_ADMM() in src/tao/constrained/impls/admm/admm.c TaoSetFromOptions_ALMM() in src/tao/constrained/impls/almm/almm.c TaoSetFromOptions_IPM() in src/tao/constrained/impls/ipm/ipm.c TaoSetFromOptions_PDIPM() in src/tao/constrained/impls/ipm/pdipm.c TaoSetFromOptions_BRGN() in src/tao/leastsquares/impls/brgn/brgn.c TaoSetFromOptions_POUNDERS() in src/tao/leastsquares/impls/pounders/pounders.c TaoSetFromOptions_LCL() in src/tao/pde_constrained/impls/lcl/lcl.c TaoSetFromOptions_BQPIP() in src/tao/quadratic/impls/bqpip/bqpip.c TaoSetFromOptions_GPCG() in src/tao/quadratic/impls/gpcg/gpcg.c TaoSetFromOptions_BMRM() in src/tao/unconstrained/impls/bmrm/bmrm.c TaoSetFromOptions_CG() in src/tao/unconstrained/impls/cg/taocg.c TaoSetFromOptions_LMVM() in src/tao/unconstrained/impls/lmvm/lmvm.c TaoSetFromOptions_NM() in src/tao/unconstrained/impls/neldermead/neldermead.c TaoSetFromOptions_NLS() in src/tao/unconstrained/impls/nls/nls.c TaoSetFromOptions_NTL() in src/tao/unconstrained/impls/ntl/ntl.c TaoSetFromOptions_NTR() in src/tao/unconstrained/impls/ntr/ntr.c TaoSetFromOptions_OWLQN() in src/tao/unconstrained/impls/owlqn/owlqn.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetFromOptions(Tao tao)
```

Example 2 (unknown):
```unknown
-tao_monitor
```

Example 3 (unknown):
```unknown
TaoCreate()
```

Example 4 (unknown):
```unknown
-tao_add_terms
```

---

## TaoSetFunctionLowerBound#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetFunctionLowerBound/

**Contents:**
- TaoSetFunctionLowerBound#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

Sets a bound on the solution objective value. When an approximate solution with an objective value below this number has been found, the solver will terminate.

tao - the Tao solver context

-tao_fmin fmin - sets the minimum function value

TAO: Optimization Solvers, Tao, TaoConvergedReason, TaoSetTolerances()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetFunctionLowerBound(Tao tao, PetscReal fmin)
```

Example 2 (unknown):
```unknown
TaoConvergedReason
```

Example 3 (unknown):
```unknown
TaoSetTolerances()
```

---

## TaoSetGradientNorm#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetGradientNorm/

**Contents:**
- TaoSetGradientNorm#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the matrix used to define the norm that measures the size of the gradient in some of the Tao algorithms

tao - the Tao context

M - matrix that defines the norm

TAO: Optimization Solvers, Tao, TaoGetGradientNorm(), TaoGradientNorm()

src/tao/interface/taosolver.c

src/tao/tutorials/ex3.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetGradientNorm(Tao tao, Mat M)
```

Example 2 (unknown):
```unknown
TaoGetGradientNorm()
```

Example 3 (unknown):
```unknown
TaoGradientNorm()
```

---

## TaoSetGradient#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetGradient/

**Contents:**
- TaoSetGradient#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

Sets the gradient evaluation routine for the function to be optimized

tao - the Tao context

g - [optional] the vector to internally hold the gradient computation

func - the gradient function

ctx - [optional] user-defined context for private data for the gradient evaluation routine (may be NULL)

tao - the optimization solver

g - gradient value (output)

ctx - [optional] user-defined function context

TAO: Optimization Solvers, Tao, TaoSolve(), TaoSetObjective(), TaoSetHessian(), TaoSetObjectiveAndGradient(), TaoGetGradient()

src/tao/interface/taosolver_fg.c

src/tao/pde_constrained/tutorials/elliptic.c src/tao/pde_constrained/tutorials/hyperbolic.c src/tao/tutorials/ex4.c src/tao/pde_constrained/tutorials/parabolic.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetGradient(Tao tao, Vec g, PetscErrorCode (*func)(Tao tao, Vec x, Vec g, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoSetObjective()
```

Example 3 (unknown):
```unknown
TaoSetHessian()
```

Example 4 (unknown):
```unknown
TaoSetObjectiveAndGradient()
```

---

## TaoSetHessian#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetHessian/

**Contents:**
- TaoSetHessian#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

Sets the function to compute the Hessian as well as the location to store the matrix.

tao - the Tao context

H - Matrix used for the hessian

Hpre - Matrix that will be used to construct the preconditioner, can be same as H

func - Hessian evaluation routine

ctx - [optional] user-defined context for private data for the Hessian evaluation routine (may be NULL)

tao - the Tao context

Hpre - matrix used to construct the preconditioner, usually the same as H

ctx - [optional] user-defined Hessian context

TAO: Optimization Solvers, Tao, TaoType, TaoSetObjective(), TaoSetGradient(), TaoSetObjectiveAndGradient(), TaoGetHessian()

src/tao/interface/taosolver_hj.c

src/tao/bound/tutorials/plate2f.F90 src/tao/unconstrained/tutorials/minsurf2.c src/tao/bound/tutorials/jbearing2.c src/tao/unconstrained/tutorials/rosenbrock1f.F90 src/tao/constrained/tutorials/tomographyADMM.c src/tao/bound/tutorials/plate2.c src/tao/constrained/tutorials/ex1.c src/tao/unconstrained/tutorials/eptorsion2f.F90 src/tao/constrained/tutorials/maros.c src/tao/unconstrained/tutorials/rosenbrock3.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetHessian(Tao tao, Mat H, Mat Hpre, PetscErrorCode (*func)(Tao tao, Vec x, Mat H, Mat Hpre, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoSetObjective()
```

Example 3 (unknown):
```unknown
TaoSetGradient()
```

Example 4 (unknown):
```unknown
TaoSetObjectiveAndGradient()
```

---

## TaoSetInequalityBounds#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetInequalityBounds/

**Contents:**
- TaoSetInequalityBounds#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the upper and lower bounds

tao - the Tao context

IL - vector of lower bounds

IU - vector of upper bounds

TAO: Optimization Solvers, Tao, TaoSetObjective(), TaoSetHessian(), TaoSetObjectiveAndGradient(), TaoGetInequalityBounds()

src/tao/interface/taosolver_bounds.c

src/tao/constrained/tutorials/maros.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetInequalityBounds(Tao tao, Vec IL, Vec IU)
```

Example 2 (unknown):
```unknown
TaoSetObjective()
```

Example 3 (unknown):
```unknown
TaoSetHessian()
```

Example 4 (unknown):
```unknown
TaoSetObjectiveAndGradient()
```

---

## TaoSetInequalityConstraintsRoutine#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetInequalityConstraintsRoutine/

**Contents:**
- TaoSetInequalityConstraintsRoutine#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

Sets a function to be used to compute constraints. Tao only handles constraints under certain conditions, see TAO: Optimization Solvers for details

tao - the Tao context

ci - A vector that will be used to store inequality constraint evaluation

func - the bounds computation routine

ctx - [optional] user-defined context for private data for the inequality constraints computation (may be NULL)

x - point to evaluate inequality constraints

ci - vector of inequality constraints evaluated at x

ctx - the (optional) user-defined function context

TAO: Optimization Solvers, Tao, TaoSetObjective(), TaoSetHessian(), TaoSetObjectiveAndGradient(), TaoSetVariableBounds()

src/tao/interface/taosolver_bounds.c

src/tao/constrained/tutorials/ex1.c src/tao/constrained/tutorials/maros.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetInequalityConstraintsRoutine(Tao tao, Vec ci, PetscErrorCode (*func)(Tao tao, Vec x, Vec ci, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoSetObjective()
```

Example 3 (unknown):
```unknown
TaoSetHessian()
```

Example 4 (unknown):
```unknown
TaoSetObjectiveAndGradient()
```

---

## TaoSetInitialTrustRegionRadius#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetInitialTrustRegionRadius/

**Contents:**
- TaoSetInitialTrustRegionRadius#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#

Sets the initial trust region radius.

tao - a Tao optimization solver

radius - the trust region radius

-tao_trust0 radius - sets initial trust region radius

Use PETSC_DETERMINE to use the default radius that was set when the object’s type was set.

TAO: Optimization Solvers, Tao, TaoGetTrustRegionRadius(), TaoSetTrustRegionTolerance(), TAONTR

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetInitialTrustRegionRadius(Tao tao, PetscReal radius)
```

Example 2 (unknown):
```unknown
PETSC_DETERMINE
```

Example 3 (unknown):
```unknown
TaoGetTrustRegionRadius()
```

Example 4 (unknown):
```unknown
TaoSetTrustRegionTolerance()
```

---

## TaoSetIterationNumber#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetIterationNumber/

**Contents:**
- TaoSetIterationNumber#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the current iteration number.

tao - the Tao context

iter - iteration number

TAO: Optimization Solvers, Tao, TaoGetLinearSolveIterations()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetIterationNumber(Tao tao, PetscInt iter)
```

Example 2 (unknown):
```unknown
TaoGetLinearSolveIterations()
```

---

## TaoSetJacobianDesignRoutine#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetJacobianDesignRoutine/

**Contents:**
- TaoSetJacobianDesignRoutine#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

Sets the function to compute the Jacobian of the constraint function with respect to the design variables. Used only for PDE-constrained optimization.

tao - the Tao context

J - Matrix used for the Jacobian

func - Jacobian evaluation routine

ctx - [optional] user-defined context for private data for the Jacobian evaluation routine (may be NULL)

tao - the Tao context

ctx - [optional] user-defined Jacobian context

TAO: Optimization Solvers, Tao, TaoComputeJacobianDesign(), TaoSetJacobianStateRoutine(), TaoSetStateDesignIS()

src/tao/interface/taosolver_hj.c

src/tao/pde_constrained/tutorials/elliptic.c src/tao/pde_constrained/tutorials/hyperbolic.c src/tao/pde_constrained/tutorials/parabolic.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetJacobianDesignRoutine(Tao tao, Mat J, PetscErrorCode (*func)(Tao tao, Vec x, Mat J, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoComputeJacobianDesign()
```

Example 3 (unknown):
```unknown
TaoSetJacobianStateRoutine()
```

Example 4 (unknown):
```unknown
TaoSetStateDesignIS()
```

---

## TaoSetJacobianEqualityRoutine#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetJacobianEqualityRoutine/

**Contents:**
- TaoSetJacobianEqualityRoutine#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

Sets the function to compute the Jacobian (and its inverse) of the constraint function with respect to the equality variables. Used only for PDE-constrained optimization.

tao - the Tao context

J - Matrix used for the Jacobian

Jpre - Matrix that will be used to construct the preconditioner, can be same as J.

func - Jacobian evaluation routine

ctx - [optional] user-defined context for private data for the Jacobian evaluation routine (may be NULL)

tao - the Tao context

Jpre - matrix used to construct the preconditioner, usually the same as J

ctx - [optional] user-defined Jacobian context

TAO: Optimization Solvers, Tao, TaoComputeJacobianEquality(), TaoSetJacobianDesignRoutine(), TaoSetEqualityDesignIS()

src/tao/interface/taosolver_hj.c

src/tao/constrained/tutorials/ex1.c src/tao/constrained/tutorials/maros.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetJacobianEqualityRoutine(Tao tao, Mat J, Mat Jpre, PetscErrorCode (*func)(Tao tao, Vec x, Mat J, Mat Jpre, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoComputeJacobianEquality()
```

Example 3 (unknown):
```unknown
TaoSetJacobianDesignRoutine()
```

Example 4 (unknown):
```unknown
TaoSetEqualityDesignIS()
```

---

## TaoSetJacobianInequalityRoutine#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetJacobianInequalityRoutine/

**Contents:**
- TaoSetJacobianInequalityRoutine#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

Sets the function to compute the Jacobian (and its inverse) of the constraint function with respect to the inequality variables. Used only for PDE-constrained optimization.

tao - the Tao context

J - Matrix used for the Jacobian

Jpre - Matrix that will be used to construct the preconditioner, can be same as J.

func - Jacobian evaluation routine

ctx - [optional] user-defined context for private data for the Jacobian evaluation routine (may be NULL)

tao - the Tao context

Jpre - matrix used to construct the preconditioner, usually the same as J

ctx - [optional] user-defined Jacobian context

TAO: Optimization Solvers, Tao, TaoComputeJacobianInequality(), TaoSetJacobianDesignRoutine(), TaoSetInequalityDesignIS()

src/tao/interface/taosolver_hj.c

src/tao/constrained/tutorials/ex1.c src/tao/constrained/tutorials/maros.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetJacobianInequalityRoutine(Tao tao, Mat J, Mat Jpre, PetscErrorCode (*func)(Tao tao, Vec x, Mat J, Mat Jpre, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoComputeJacobianInequality()
```

Example 3 (unknown):
```unknown
TaoSetJacobianDesignRoutine()
```

Example 4 (unknown):
```unknown
TaoSetInequalityDesignIS()
```

---

## TaoSetJacobianResidualRoutine#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetJacobianResidualRoutine/

**Contents:**
- TaoSetJacobianResidualRoutine#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

Sets the function to compute the least-squares residual Jacobian as well as the location to store the matrix.

tao - the Tao context

J - Matrix used for the jacobian

Jpre - Matrix that will be used to construct the preconditioner, can be same as J

func - Jacobian evaluation routine

ctx - [optional] user-defined context for private data for the Jacobian evaluation routine (may be NULL)

tao - the Tao context

Jpre - matrix used to construct the preconditioner, usually the same as J

ctx - [optional] user-defined Jacobian context

TAO: Optimization Solvers, Tao, TaoSetGradient(), TaoSetObjective()

src/tao/interface/taosolver_hj.c

src/tao/leastsquares/tutorials/tomography.c src/tao/leastsquares/tutorials/cs1.c src/tao/leastsquares/tutorials/chwirut1.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetJacobianResidualRoutine(Tao tao, Mat J, Mat Jpre, PetscErrorCode (*func)(Tao tao, Vec x, Mat J, Mat Jpre, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoSetGradient()
```

Example 3 (unknown):
```unknown
TaoSetObjective()
```

---

## TaoSetJacobianRoutine#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetJacobianRoutine/

**Contents:**
- TaoSetJacobianRoutine#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

Sets the function to compute the Jacobian as well as the location to store the matrix.

tao - the Tao context

J - Matrix used for the Jacobian

Jpre - Matrix that will be used to construct the preconditioner, can be same as J

func - Jacobian evaluation routine

ctx - [optional] user-defined context for private data for the Jacobian evaluation routine (may be NULL)

tao - the Tao context

Jpre - matrix used to construct the preconditioner, usually the same as J

ctx - [optional] user-defined Jacobian context

TAO: Optimization Solvers, Tao, TaoSetGradient(), TaoSetObjective()

src/tao/interface/taosolver_hj.c

src/tao/complementarity/tutorials/minsurf1.c src/tao/complementarity/tutorials/blackscholes.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetJacobianRoutine(Tao tao, Mat J, Mat Jpre, PetscErrorCode (*func)(Tao tao, Vec x, Mat J, Mat Jpre, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoSetGradient()
```

Example 3 (unknown):
```unknown
TaoSetObjective()
```

---

## TaoSetJacobianStateRoutine#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetJacobianStateRoutine/

**Contents:**
- TaoSetJacobianStateRoutine#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

Sets the function to compute the Jacobian (and its inverse) of the constraint function with respect to the state variables. Used only for PDE-constrained optimization.

tao - the Tao context

J - Matrix used for the Jacobian

Jpre - Matrix that will be used to construct the preconditioner, can be same as J. Only used if Jinv is NULL

Jinv - [optional] Matrix used to apply the inverse of the state Jacobian. Use NULL to default to PETSc KSP solvers to apply the inverse.

func - Jacobian evaluation routine

ctx - [optional] user-defined context for private data for the Jacobian evaluation routine (may be NULL)

tao - the Tao context

Jpre - matrix used to construct the preconditioner, usually the same as J

ctx - [optional] user-defined Jacobian context

TAO: Optimization Solvers, Tao, TaoComputeJacobianState(), TaoSetJacobianDesignRoutine(), TaoSetStateDesignIS()

src/tao/interface/taosolver_hj.c

src/tao/pde_constrained/tutorials/elliptic.c src/tao/pde_constrained/tutorials/hyperbolic.c src/tao/pde_constrained/tutorials/parabolic.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetJacobianStateRoutine(Tao tao, Mat J, Mat Jpre, Mat Jinv, PetscErrorCode (*func)(Tao tao, Vec x, Mat J, Mat Jpre, Mat Jinv, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoComputeJacobianState()
```

Example 3 (unknown):
```unknown
TaoSetJacobianDesignRoutine()
```

Example 4 (unknown):
```unknown
TaoSetStateDesignIS()
```

---

## TaoSetLMVMMatrix#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetLMVMMatrix/

**Contents:**
- TaoSetLMVMMatrix#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets an external LMVM matrix into the Tao solver. Valid only for quasi-Newton family of methods.

QN family of methods create their own LMVM matrices and users who wish to manipulate this matrix should use TaoGetLMVMMatrix() instead.

tao - Tao solver context

TAOBQNLS, TAOBQNKLS, TAOBQNKTL, TAOBQNKTR, MATLMVM, TaoGetLMVMMatrix()

src/tao/bound/impls/bqnk/bqnk.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetLMVMMatrix(Tao tao, Mat B)
```

Example 2 (unknown):
```unknown
TaoGetLMVMMatrix()
```

---

## TaoSetMaximumFunctionEvaluations#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetMaximumFunctionEvaluations/

**Contents:**
- TaoSetMaximumFunctionEvaluations#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Sets a maximum number of function evaluations allowed for a TaoSolve().

tao - the Tao solver context

nfcn - the maximum number of function evaluations (>=0), use PETSC_UNLIMITED to have no bound

-tao_max_funcs nfcn - sets the maximum number of function evaluations

Use PETSC_DETERMINE to use the default maximum number of function evaluations that was set when the object type was set.

Deprecated support for an unlimited number of function evaluations by passing a negative value.

TAO: Optimization Solvers, Tao, TaoSetTolerances(), TaoSetMaximumIterations()

src/tao/interface/taosolver.c

src/tao/constrained/tutorials/ex1.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetMaximumFunctionEvaluations(Tao tao, PetscInt nfcn)
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
TaoSetTolerances()
```

---

## TaoSetMaximumIterations#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetMaximumIterations/

**Contents:**
- TaoSetMaximumIterations#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Sets a maximum number of iterates to be used in TaoSolve()

tao - the Tao solver context

maxits - the maximum number of iterates (>=0), use PETSC_UNLIMITED to have no bound

-tao_max_it its - sets the maximum number of iterations

Use PETSC_DETERMINE to use the default maximum number of iterations that was set when the object’s type was set.

Also accepts the deprecated negative values to indicate no limit

TAO: Optimization Solvers, Tao, TaoSetTolerances(), TaoSetMaximumFunctionEvaluations()

src/tao/interface/taosolver.c

src/tao/unconstrained/tutorials/rosenbrock3.c src/tao/unconstrained/tutorials/rosenbrock2.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetMaximumIterations(Tao tao, PetscInt maxits)
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
TaoSetTolerances()
```

---

## TaoSetObjectiveAndGradient#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetObjectiveAndGradient/

**Contents:**
- TaoSetObjectiveAndGradient#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets a combined objective function and gradient evaluation routine for the function to be optimized

tao - the Tao context

g - [optional] the vector to internally hold the gradient computation

func - the gradient function

ctx - [optional] user-defined context for private data for the gradient evaluation routine (may be NULL)

tao - the optimization object

f - objective value (output)

g - gradient value (output)

ctx - [optional] user-defined function context

For some optimization methods using a combined function can be more efficient.

TAO: Optimization Solvers, Tao, TaoSolve(), TaoSetObjective(), TaoSetHessian(), TaoSetGradient(), TaoGetObjectiveAndGradient()

src/tao/interface/taosolver_fg.c

src/tao/bound/tutorials/plate2f.F90 src/tao/unconstrained/tutorials/minsurf2.c src/tao/bound/tutorials/jbearing2.c src/tao/unconstrained/tutorials/rosenbrock1f.F90 src/tao/constrained/tutorials/tomographyADMM.c src/tao/bound/tutorials/plate2.c src/tao/constrained/tutorials/ex1.c src/tao/unconstrained/tutorials/eptorsion2f.F90 src/tao/constrained/tutorials/maros.c src/tao/unconstrained/tutorials/rosenbrock3.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetObjectiveAndGradient(Tao tao, Vec g, PetscErrorCode (*func)(Tao tao, Vec x, PetscReal *f, Vec g, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoSetObjective()
```

Example 3 (unknown):
```unknown
TaoSetHessian()
```

Example 4 (unknown):
```unknown
TaoSetGradient()
```

---

## TaoSetObjective#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetObjective/

**Contents:**
- TaoSetObjective#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

Sets the function evaluation routine for minimization

tao - the Tao context

func - the objective function

ctx - [optional] user-defined context for private data for the function evaluation routine (may be NULL)

ctx - [optional] user-defined function context

TAO: Optimization Solvers, TaoSetGradient(), TaoSetHessian(), TaoSetObjectiveAndGradient(), TaoGetObjective()

src/tao/interface/taosolver_fg.c

src/tao/tutorials/ex4.c src/tao/pde_constrained/tutorials/elliptic.c src/tao/pde_constrained/tutorials/parabolic.c src/tao/unconstrained/tutorials/minsurf2.c src/tao/pde_constrained/tutorials/hyperbolic.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetObjective(Tao tao, PetscErrorCode (*func)(Tao tao, Vec x, PetscReal *f, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoSetGradient()
```

Example 3 (unknown):
```unknown
TaoSetHessian()
```

Example 4 (unknown):
```unknown
TaoSetObjectiveAndGradient()
```

---

## TaoSetOptionsPrefix#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetOptionsPrefix/

**Contents:**
- TaoSetOptionsPrefix#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the prefix used for searching for all Tao options in the database.

tao - the Tao context

p - the prefix string to prepend to all Tao option requests

A hyphen (-) must NOT be given at the beginning of the prefix name. The first character of all runtime options is AUTOMATICALLY the hyphen.

For example, to distinguish between the runtime options for two different Tao solvers, one could call

This would enable use of different options for each system, such as

TAO: Optimization Solvers, Tao, TaoSetFromOptions(), TaoAppendOptionsPrefix(), TaoGetOptionsPrefix()

src/tao/interface/taosolver.c

src/tao/tutorials/ex4.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetOptionsPrefix(Tao tao, const char p[])
```

Example 2 (unknown):
```unknown
TaoSetOptionsPrefix(tao1,"sys1_")
      TaoSetOptionsPrefix(tao2,"sys2_")
```

Example 3 (unknown):
```unknown
-sys1_tao_method blmvm -sys1_tao_grtol 1.e-3
      -sys2_tao_method lmvm  -sys2_tao_grtol 1.e-4
```

Example 4 (unknown):
```unknown
TaoSetFromOptions()
```

---

## TaoSetRecycleHistory#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetRecycleHistory/

**Contents:**
- TaoSetRecycleHistory#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Sets the boolean flag to enable/disable re-using iterate information from the previous TaoSolve(). This feature is disabled by default.

tao - the Tao context

recycle - boolean flag

-tao_recycle_history (true|false) - reuse the history

For conjugate gradient methods (TAOBNCG), this re-uses the latest search direction from the previous TaoSolve() call when computing the first search direction in a new solution. By default, CG methods set the first search direction to the negative gradient.

For quasi-Newton family of methods (TAOBQNLS, TAOBQNKLS, TAOBQNKTR, TAOBQNKTL), this re-uses the accumulated quasi-Newton Hessian approximation from the previous TaoSolve() call. By default, QN family of methods reset the initial Hessian approximation to the identity matrix.

For any other algorithm, this setting has no effect.

TAO: Optimization Solvers, Tao, TaoGetRecycleHistory(), TAOBNCG, TAOBQNLS, TAOBQNKLS, TAOBQNKTR, TAOBQNKTL

src/tao/interface/taosolver.c

src/tao/unconstrained/tutorials/rosenbrock3.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetRecycleHistory(Tao tao, PetscBool recycle)
```

Example 2 (unknown):
```unknown
TaoGetRecycleHistory()
```

---

## TaoSetResidualRoutine#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetResidualRoutine/

**Contents:**
- TaoSetResidualRoutine#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- See Also#
- Level#
- Location#
- Examples#

Sets the residual evaluation routine for least-square applications

tao - the Tao context

res - the residual vector

func - the residual evaluation routine

ctx - [optional] user-defined context for private data for the function evaluation routine (may be NULL)

res - function value vector

ctx - [optional] user-defined function context

TAO: Optimization Solvers, Tao, TaoSetObjective(), TaoSetJacobianRoutine()

src/tao/interface/taosolver_fg.c

src/tao/leastsquares/tutorials/chwirut1f.F90 src/tao/leastsquares/tutorials/chwirut1.c src/tao/leastsquares/tutorials/chwirut2f.F90 src/tao/leastsquares/tutorials/cs1.c src/tao/leastsquares/tutorials/tomography.c src/tao/leastsquares/tutorials/chwirut2.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetResidualRoutine(Tao tao, Vec res, PetscErrorCode (*func)(Tao tao, Vec x, Vec res, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoSetObjective()
```

Example 3 (unknown):
```unknown
TaoSetJacobianRoutine()
```

---

## TaoSetResidualWeights#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetResidualWeights/

**Contents:**
- TaoSetResidualWeights#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Give weights for the residual values. A vector can be used if only diagonal terms are used, otherwise a matrix can be give.

tao - the Tao context

sigma_v - vector of weights (diagonal terms only)

n - the number of weights (if using off-diagonal)

rows - index list of rows for sigma_v

cols - index list of columns for sigma_v

vals - array of weights

If this function is not provided, or if sigma_v and vals are both NULL, then the identity matrix will be used for weights.

Either sigma_v or vals should be NULL

TAO: Optimization Solvers, Tao, TaoSetResidualRoutine()

src/tao/interface/taosolver_fg.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetResidualWeights(Tao tao, Vec sigma_v, PetscInt n, PetscInt *rows, PetscInt *cols, PetscReal *vals)
```

Example 2 (unknown):
```unknown
TaoSetResidualRoutine()
```

---

## TaoSetSolution#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetSolution/

**Contents:**
- TaoSetSolution#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the vector holding the initial guess for the solve

tao - the Tao context

x0 - the initial guess

TAO: Optimization Solvers, Tao, TaoCreate(), TaoSolve(), TaoGetSolution()

src/tao/interface/taosolver_fg.c

src/tao/leastsquares/tutorials/chwirut1f.F90 src/tao/leastsquares/tutorials/chwirut2f.F90 src/tao/leastsquares/tutorials/cs1.c src/tao/pde_constrained/tutorials/elliptic.c src/tao/constrained/tutorials/tomographyADMM.c src/tao/pde_constrained/tutorials/parabolic.c src/tao/constrained/tutorials/ex1.c src/tao/pde_constrained/tutorials/hyperbolic.c src/tao/constrained/tutorials/maros.c src/tao/leastsquares/tutorials/chwirut1.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetSolution(Tao tao, Vec x0)
```

Example 2 (unknown):
```unknown
TaoCreate()
```

Example 3 (unknown):
```unknown
TaoGetSolution()
```

---

## TaoSetStateDesignIS#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetStateDesignIS/

**Contents:**
- TaoSetStateDesignIS#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Indicate to the Tao object which variables in the solution vector are state variables and which are design. Only applies to PDE-constrained optimization.

tao - The Tao context

s_is - the index set corresponding to the state variables

d_is - the index set corresponding to the design variables

TAO: Optimization Solvers, Tao, TaoSetJacobianStateRoutine(), TaoSetJacobianDesignRoutine()

src/tao/interface/taosolver_hj.c

src/tao/pde_constrained/tutorials/elliptic.c src/tao/pde_constrained/tutorials/hyperbolic.c src/tao/pde_constrained/tutorials/parabolic.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetStateDesignIS(Tao tao, IS s_is, IS d_is)
```

Example 2 (unknown):
```unknown
TaoSetJacobianStateRoutine()
```

Example 3 (unknown):
```unknown
TaoSetJacobianDesignRoutine()
```

---

## TaoSetTolerances#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetTolerances/

**Contents:**
- TaoSetTolerances#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Notes#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Sets parameters used in TaoSolve() convergence tests

tao - the Tao context

gatol - stop if norm of gradient is less than this

grtol - stop if relative norm of gradient is less than this

gttol - stop if norm of gradient is reduced by this factor

-tao_gatol gatol - Sets gatol

-tao_grtol grtol - Sets grtol

-tao_gttol gttol - Sets gttol

Use PETSC_CURRENT to leave one or more tolerances unchanged.

Use PETSC_DETERMINE to set one or more tolerances to their values when the taoobject’s type was set

Use PETSC_CURRENT_REAL or PETSC_DETERMINE_REAL

TAO: Optimization Solvers, Tao, TaoConvergedReason, TaoGetTolerances()

src/tao/interface/taosolver.c

src/tao/unconstrained/tutorials/spectraladjointassimilation.c src/tao/unconstrained/tutorials/rosenbrock2.c src/tao/constrained/tutorials/ex1.c src/tao/constrained/tutorials/maros.c src/tao/unconstrained/tutorials/rosenbrock3.c src/tao/unconstrained/tutorials/burgers_spectral.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetTolerances(Tao tao, PetscReal gatol, PetscReal grtol, PetscReal gttol)
```

Example 2 (unknown):
```unknown
||g(X)||                            <= gatol
  ||g(X)|| / |f(X)|                   <= grtol
  ||g(X)|| / ||g(X0)||                <= gttol
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

## TaoSetTotalIterationNumber#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetTotalIterationNumber/

**Contents:**
- TaoSetTotalIterationNumber#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#

Sets the current total iteration number.

tao - the Tao context

iter - the iteration number

TAO: Optimization Solvers, Tao, TaoGetLinearSolveIterations()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetTotalIterationNumber(Tao tao, PetscInt iter)
```

Example 2 (unknown):
```unknown
TaoGetLinearSolveIterations()
```

---

## TaoSetType#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetType/

**Contents:**
- TaoSetType#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets the TaoType for the minimization solver.

tao - the Tao solver context

type - a known method

-tao_type type - Sets the method; see TaoType

Calling this function resets the convergence test to TaoDefaultConvergenceTest(). If a custom convergence test has been set with TaoSetConvergenceTest(), it must be set again after calling TaoSetType().

TAO: Optimization Solvers, Tao, TaoCreate(), TaoGetType(), TaoType

src/tao/interface/taosolver.c

src/tao/leastsquares/tutorials/chwirut1f.F90 src/tao/leastsquares/tutorials/chwirut2f.F90 src/tao/leastsquares/tutorials/cs1.c src/tao/pde_constrained/tutorials/elliptic.c src/tao/constrained/tutorials/tomographyADMM.c src/tao/pde_constrained/tutorials/parabolic.c src/tao/constrained/tutorials/ex1.c src/tao/pde_constrained/tutorials/hyperbolic.c src/tao/constrained/tutorials/maros.c src/tao/leastsquares/tutorials/chwirut1.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetType(Tao tao, TaoType type)
```

Example 2 (unknown):
```unknown
TaoDefaultConvergenceTest()
```

Example 3 (unknown):
```unknown
TaoSetConvergenceTest()
```

Example 4 (unknown):
```unknown
TaoSetType()
```

---

## TaoSetUpdate#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetUpdate/

**Contents:**
- TaoSetUpdate#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Notes#
- See Also#
- Level#
- Location#

Sets the general-purpose update function called at the beginning of every iteration of the optimization algorithm. Called after the new solution and the gradient is determined, but before the Hessian is computed (if applicable).

ctx - The update function context

tao - The optimizer context

it - The current iteration index

ctx - The update context

Users can modify the gradient direction or any other vector associated to the specific solver used. The objective function value is always recomputed after a call to the update hook.

TAO: Optimization Solvers, Tao, TaoSolve()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetUpdate(Tao tao, PetscErrorCode (*func)(Tao tao, PetscInt it, PetscCtx ctx), PetscCtx ctx)
```

---

## TaoSetUp#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetUp/

**Contents:**
- TaoSetUp#
- Synopsis#
- Input Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Sets up the internal data structures for the later use of a Tao solver

tao - the Tao context

The user will not need to explicitly call TaoSetUp(), as it will automatically be called in TaoSolve(). However, if the user desires to call it explicitly, it should come after TaoCreate() and any TaoSetSomething() routines, but before TaoSolve().

TAO: Optimization Solvers, Tao, TaoCreate(), TaoSolve()

src/tao/interface/taosolver.c

src/tao/constrained/tutorials/ex1.c

TaoSetUp_BNCG() in src/tao/bound/impls/bncg/bncg.c TaoSetUp_BNK() in src/tao/bound/impls/bnk/bnk.c TaoSetUp_BNTL() in src/tao/bound/impls/bnk/bntl.c TaoSetUp_BNTR() in src/tao/bound/impls/bnk/bntr.c TaoSetUp_BQNK() in src/tao/bound/impls/bqnk/bqnk.c TaoSetUp_BQNKTL() in src/tao/bound/impls/bqnk/bqnktl.c TaoSetUp_BQNKTR() in src/tao/bound/impls/bqnk/bqnktr.c TaoSetUp_ASFLS() in src/tao/complementarity/impls/asls/asfls.c TaoSetUp_ASILS() in src/tao/complementarity/impls/asls/asils.c TaoSetUp_SSFLS() in src/tao/complementarity/impls/ssls/ssfls.c TaoSetUp_SSILS() in src/tao/complementarity/impls/ssls/ssils.c TaoSetUp_ADMM() in src/tao/constrained/impls/admm/admm.c TaoSetUp_ALMM() in src/tao/constrained/impls/almm/almm.c TaoSetUp_BRGN() in src/tao/leastsquares/impls/brgn/brgn.c TaoSetUp_POUNDERS() in src/tao/leastsquares/impls/pounders/pounders.c TaoSetUp_CG() in src/tao/unconstrained/impls/cg/taocg.c TaoSetUp_LMVM() in src/tao/unconstrained/impls/lmvm/lmvm.c TaoSetUp_NM() in src/tao/unconstrained/impls/neldermead/neldermead.c TaoSetUp_NLS() in src/tao/unconstrained/impls/nls/nls.c TaoSetUp_NTL() in src/tao/unconstrained/impls/ntl/ntl.c TaoSetUp_NTR() in src/tao/unconstrained/impls/ntr/ntr.c TaoSetUp_OWLQN() in src/tao/unconstrained/impls/owlqn/owlqn.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetUp(Tao tao)
```

Example 2 (unknown):
```unknown
TaoCreate()
```

Example 3 (unknown):
```unknown
TaoCreate()
```

---

## TaoSetVariableBoundsRoutine#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetVariableBoundsRoutine/

**Contents:**
- TaoSetVariableBoundsRoutine#
- Synopsis#
- Input Parameters#
- Calling sequence of func#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Sets a function to be used to compute lower and upper variable bounds for the optimization

tao - the Tao context

func - the bounds computation routine

ctx - [optional] user-defined context for private data for the bounds computation (may be NULL)

xl - vector of lower bounds

xu - vector of upper bounds

ctx - the (optional) user-defined function context

The func passed to TaoSetVariableBoundsRoutine() takes precedence over any values set in TaoSetVariableBounds().

TAO: Optimization Solvers, Tao, TaoSetObjective(), TaoSetHessian(), TaoSetObjectiveAndGradient(), TaoSetVariableBounds()

src/tao/interface/taosolver_bounds.c

src/tao/bound/tutorials/plate2f.F90 src/tao/complementarity/tutorials/blackscholes.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetVariableBoundsRoutine(Tao tao, PetscErrorCode (*func)(Tao tao, Vec xl, Vec xu, PetscCtx ctx), PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoSetVariableBoundsRoutine()
```

Example 3 (unknown):
```unknown
TaoSetVariableBounds()
```

Example 4 (unknown):
```unknown
TaoSetObjective()
```

---

## TaoSetVariableBounds#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSetVariableBounds/

**Contents:**
- TaoSetVariableBounds#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

Sets the upper and lower bounds for the optimization problem

tao - the Tao context

XL - vector of lower bounds

XU - vector of upper bounds

TAO: Optimization Solvers, Tao, TaoSetObjective(), TaoSetHessian(), TaoSetObjectiveAndGradient(), TaoGetVariableBounds()

src/tao/interface/taosolver_bounds.c

src/tao/bound/tutorials/jbearing2.c src/tao/leastsquares/tutorials/tomography.c src/tao/constrained/tutorials/tomographyADMM.c src/tao/complementarity/tutorials/minsurf1.c src/tao/unconstrained/tutorials/eptorsion3.c src/tao/bound/tutorials/plate2.c src/tao/tutorials/ex3.c src/tao/constrained/tutorials/ex1.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSetVariableBounds(Tao tao, Vec XL, Vec XU)
```

Example 2 (unknown):
```unknown
TaoSetObjective()
```

Example 3 (unknown):
```unknown
TaoSetHessian()
```

Example 4 (unknown):
```unknown
TaoSetObjectiveAndGradient()
```

---

## TaoShellGetContext#

**URL:** https://petsc.org/release/manualpages/Tao/TaoShellGetContext/

**Contents:**
- TaoShellGetContext#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- Fortran Note#
- See Also#
- Level#
- Location#
- Examples#

Returns the user-provided context associated with a TAOSHELL

tao - should have been created with TaoSetType(tao,TAOSHELL);

ctx - the user provided context

This routine is intended for use within various shell routines

This only works when the context is a Fortran derived type or a PetscObject. Define ctx with

Tao, TAOSHELL, TaoShellSetContext()

src/tao/shell/taoshell.c

src/tao/constrained/tutorials/tomographyADMM.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoShellGetContext(Tao tao, PetscCtxRt ctx)
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
TaoShellSetContext()
```

---

## TaoShellSetContext#

**URL:** https://petsc.org/release/manualpages/Tao/TaoShellSetContext/

**Contents:**
- TaoShellSetContext#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#

sets the context for a TAOSHELL

Tao, TAOSHELL, TaoShellGetContext()

src/tao/shell/taoshell.c

src/tao/constrained/tutorials/tomographyADMM.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoShellSetContext(Tao tao, PetscCtx ctx)
```

Example 2 (unknown):
```unknown
TaoShellGetContext()
```

---

## TaoShellSetSolve#

**URL:** https://petsc.org/release/manualpages/Tao/TaoShellSetSolve/

**Contents:**
- TaoShellSetSolve#
- Synopsis#
- Input Parameters#
- Calling sequence of solve#
- See Also#
- Level#
- Location#
- Examples#

Sets routine to apply as solver

tao - the nonlinear solver context

solve - the application-provided solver routine

tao - the optimizer, get the application context with TaoShellGetContext()

Tao, TAOSHELL, TaoShellSetContext(), TaoShellGetContext()

src/tao/shell/taoshell.c

src/tao/constrained/tutorials/tomographyADMM.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoShellSetSolve(Tao tao, PetscErrorCode (*solve)(Tao tao))
```

Example 2 (unknown):
```unknown
TaoShellGetContext()
```

Example 3 (unknown):
```unknown
TaoShellSetContext()
```

Example 4 (unknown):
```unknown
TaoShellGetContext()
```

---

## TAOSHELL#

**URL:** https://petsc.org/release/manualpages/Tao/TAOSHELL/

**Contents:**
- TAOSHELL#
- See Also#
- Level#
- Location#
- Examples#

a user provided optimizer

TaoCreate(), Tao, TaoSetType(), TaoType

src/tao/shell/taoshell.c

src/tao/constrained/tutorials/tomographyADMM.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

Example 2 (unknown):
```unknown
TaoSetType()
```

---

## TAOSNES#

**URL:** https://petsc.org/release/manualpages/Tao/TAOSNES/

**Contents:**
- TAOSNES#
- See Also#
- Level#
- Location#

nonlinear solver using SNES

TaoCreate(), Tao, TaoSetType(), TaoType

src/tao/snes/taosnes.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

Example 2 (unknown):
```unknown
TaoSetType()
```

---

## TaoSoftThreshold#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSoftThreshold/

**Contents:**
- TaoSoftThreshold#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Calculates soft thresholding routine with input vector and given lower and upper bound and returns it to output vector.

in - input vector to be thresholded

out - Soft thresholded output vector

Soft thresholding is defined as [ S(input,lb,ub) = \begin{cases} input - ub & \text{if } input > ub \ 0 & \text{if } lb \leq input \leq ub \ input - lb & \text{if } input < lb \end{cases} ]

src/tao/util/softthreshold.c

src/tao/constrained/tutorials/tomographyADMM.c src/tao/tutorials/ex4.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
PetscErrorCode TaoSoftThreshold(Vec in, PetscReal lb, PetscReal ub, Vec out)
```

---

## TaoSolve#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSolve/

**Contents:**
- TaoSolve#
- Synopsis#
- Input Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Solves an optimization problem min F(x) s.t. l <= x <= u

tao - the Tao context

The user must set up the Tao object with calls to TaoSetSolution(), TaoSetObjective(), TaoSetGradient(), and (if using 2nd order method) TaoSetHessian().

You should call TaoGetConvergedReason() or run with -tao_converged_reason to determine if the optimization algorithm actually succeeded or why it failed.

TAO: Optimization Solvers, Tao, TaoCreate(), TaoSetObjective(), TaoSetGradient(), TaoSetHessian(), TaoGetConvergedReason(), TaoSetUp()

src/tao/interface/taosolver.c

src/tao/leastsquares/tutorials/chwirut1f.F90 src/tao/leastsquares/tutorials/chwirut2f.F90 src/tao/leastsquares/tutorials/cs1.c src/tao/pde_constrained/tutorials/elliptic.c src/tao/constrained/tutorials/tomographyADMM.c src/tao/pde_constrained/tutorials/parabolic.c src/tao/constrained/tutorials/ex1.c src/tao/pde_constrained/tutorials/hyperbolic.c src/tao/constrained/tutorials/maros.c src/tao/leastsquares/tutorials/chwirut1.c

TaoSolve_BLMVM() in src/tao/bound/impls/blmvm/blmvm.c TaoSolve_BNCG() in src/tao/bound/impls/bncg/bncg.c TaoSolve_BNLS() in src/tao/bound/impls/bnk/bnls.c TaoSolve_BNTL() in src/tao/bound/impls/bnk/bntl.c TaoSolve_BNTR() in src/tao/bound/impls/bnk/bntr.c TaoSolve_BQNK() in src/tao/bound/impls/bqnk/bqnk.c TaoSolve_TRON() in src/tao/bound/impls/tron/tron.c TaoSolve_ASFLS() in src/tao/complementarity/impls/asls/asfls.c TaoSolve_ASILS() in src/tao/complementarity/impls/asls/asils.c TaoSolve_SSFLS() in src/tao/complementarity/impls/ssls/ssfls.c TaoSolve_SSILS() in src/tao/complementarity/impls/ssls/ssils.c TaoSolve_ADMM() in src/tao/constrained/impls/admm/admm.c TaoSolve_ALMM() in src/tao/constrained/impls/almm/almm.c TaoSolve_IPM() in src/tao/constrained/impls/ipm/ipm.c TaoSolve_PDIPM() in src/tao/constrained/impls/ipm/pdipm.c TaoSolve_BRGN() in src/tao/leastsquares/impls/brgn/brgn.c TaoSolve_POUNDERS() in src/tao/leastsquares/impls/pounders/pounders.c TaoSolve_LCL() in src/tao/pde_constrained/impls/lcl/lcl.c TaoSolve_BQPIP() in src/tao/quadratic/impls/bqpip/bqpip.c TaoSolve_GPCG() in src/tao/quadratic/impls/gpcg/gpcg.c TaoSolve_BMRM() in src/tao/unconstrained/impls/bmrm/bmrm.c TaoSolve_CG() in src/tao/unconstrained/impls/cg/taocg.c TaoSolve_LMVM() in src/tao/unconstrained/impls/lmvm/lmvm.c TaoSolve_NM() in src/tao/unconstrained/impls/neldermead/neldermead.c TaoSolve_NLS() in src/tao/unconstrained/impls/nls/nls.c TaoSolve_NTL() in src/tao/unconstrained/impls/ntl/ntl.c TaoSolve_NTR() in src/tao/unconstrained/impls/ntr/ntr.c TaoSolve_OWLQN() in src/tao/unconstrained/impls/owlqn/owlqn.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoSolve(Tao tao)
```

Example 2 (unknown):
```unknown
TaoSetSolution()
```

Example 3 (unknown):
```unknown
TaoSetObjective()
```

Example 4 (unknown):
```unknown
TaoSetGradient()
```

---

## TAOSSFLS#

**URL:** https://petsc.org/release/manualpages/Tao/TAOSSFLS/

**Contents:**
- TAOSSFLS#
- Options Database Keys#
- See Also#
- Level#
- Location#

Semi-smooth feasible linesearch algorithm for solving complementarity constraints

-tao_ssls_delta - descent test fraction

-tao_ssls_rho - descent test power

Tao, TAOASILS, TAONTR, TAONTL, TAONM, TaoType, TaoCreate()

src/tao/complementarity/impls/ssls/ssfls.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

---

## TAOSSILS#

**URL:** https://petsc.org/release/manualpages/Tao/TAOSSILS/

**Contents:**
- TAOSSILS#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#

semi-smooth infeasible linesearch algorithm for solving complementarity constraints

-tao_ssls_delta - descent test fraction

-tao_ssls_rho - descent test power

Tao, TAOSSFLS, TAONTR, TAONLS, TAONM, TAOCG, TaoType, TaoCreate()

src/tao/complementarity/impls/ssls/ssils.c

src/tao/complementarity/tutorials/minsurf1.c src/tao/complementarity/tutorials/blackscholes.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

---

## TaoSubsetType#

**URL:** https://petsc.org/release/manualpages/Tao/TaoSubsetType/

**Contents:**
- TaoSubsetType#
- Synopsis#
- Values#
- Options database Key#
- See Also#
- Level#
- Location#

Type representing the way the Tao solvers handle active sets

TAO_SUBSET_SUBVEC - Tao uses MatCreateSubMatrix() and VecGetSubVector()

TAO_SUBSET_MASK - Matrices are zeroed out corresponding to active set entries

TAO_SUBSET_MATRIXFREE - Same as TAO_SUBSET_MASK but it can be applied to matrix-free operators

-different_hessian - Tao will use a copy of the Hessian operator for masking. By default Tao will directly alter the Hessian operator.

TAO: Optimization Solvers, TaoVecGetSubVec(), TaoMatGetSubMat(), Tao, TaoCreate(), TaoDestroy(), TaoSetType(), TaoType

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  TAO_SUBSET_SUBVEC,
  TAO_SUBSET_MASK,
  TAO_SUBSET_MATRIXFREE
} TaoSubsetType;
```

Example 2 (unknown):
```unknown
TAO_SUBSET_SUBVEC
```

Example 3 (unknown):
```unknown
MatCreateSubMatrix()
```

Example 4 (unknown):
```unknown
VecGetSubVector()
```

---

## TAOTERMCALLBACKS#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TAOTERMCALLBACKS/

**Contents:**
- TAOTERMCALLBACKS#
- Notes#
- Developer Notes#
- See Also#
- Level#
- Location#

A TaoTerm implementation that accesses the callback functions that have been provided with in TaoSetObjective(), TaoSetGradient(), TaoSetObjectiveAndGradient(), and TaoSetHessian().

If you are interested in creating your own term, you should not use this. Use TAOTERMSHELL or create your own implementation of TaoTerm with TaoTermRegister().

A TAOTERMCALLBACKS is always TAOTERM_PARAMETERS_NONE, so the params argument of TaoTerm evaluation routines should always be NULL.

A TAOTERMCALLBACKS cannot create Hessian matrices; the user needs to pass the Hessian matrices used in algorithms in TaoSetHessian().

Internally each Tao has a TaoTerm of type TAOTERMCALLBACKS that is updated by the Tao callback routines (TaoSetObjective(), TaoSetGradient(), TaoSetObjectiveAndGradient(), and TaoSetHessian()).

The routines that get the user-defined Tao callback functions (TaoGetObjective(), TaoGetObjectiveAndGradient(), TaoGetGradient(), TaoGetHessian()) will always return those original callbacks, even if the objective function has been changed by TaoAddTerm(), so PETSc/TAO should not assume that those callbacks are valid in any library code.

A TAOTERMCALLBACKS has a weak-reference to the Tao that created it, which may not be the Tao currently using it because the term could have been shared using TaoGetTerm() and TaoAddTerm().

TaoTerm: composable objective function terms, TaoTerm, TaoTermType

src/tao/term/impls/callbacks/taotermcallbacks.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoSetObjective()
```

Example 2 (unknown):
```unknown
TaoSetGradient()
```

Example 3 (unknown):
```unknown
TaoSetObjectiveAndGradient()
```

Example 4 (unknown):
```unknown
TaoSetHessian()
```

---

## TaoTermComputeGradientFD#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermComputeGradientFD/

**Contents:**
- TaoTermComputeGradientFD#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#

Approximate the gradient of a TaoTerm using finite differences

x - a solution vector

params - parameters vector (may be NULL, see TaoTermParametersMode)

g - the computed finite difference approximation to the gradient

-tao_term_fd_delta - change in x used to calculate finite differences

-tao_term_gradient_use_fd - Use TaoTermComputeGradientFD() in TaoTermComputeGradient()

This routine is slow and expensive, and is not optimized to take advantage of sparsity in the problem. Although not recommended for general use in large-scale applications, it can be useful in checking the correctness of a user-provided gradient. Call TaoTermComputeGradientSetUseFD() to start using this routine in TaoTermComputeGradient().

TaoTerm: composable objective function terms, TaoTerm, TaoTermGetFDDelta(), TaoTermSetFDDelta(), TaoTermComputeGradientSetUseFD(), TaoTermComputeGradientGetUseFD(), TaoTermComputeHessianFD()

src/tao/term/utils/taotermfdiff.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermComputeGradientFD(TaoTerm term, Vec x, Vec params, Vec g)
```

Example 2 (unknown):
```unknown
TaoTermParametersMode
```

Example 3 (unknown):
```unknown
TaoTermComputeGradientFD()
```

Example 4 (unknown):
```unknown
TaoTermComputeGradient()
```

---

## TaoTermComputeGradientGetUseFD#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermComputeGradientGetUseFD/

**Contents:**
- TaoTermComputeGradientGetUseFD#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get whether finite differences are used in TaoTermComputeGradient().

use_fd - PETSC_TRUE if finite differences are used

TaoTerm: composable objective function terms, TaoTerm, TaoTermGetFDDelta(), TaoTermSetFDDelta(), TaoTermComputeGradientFD(), TaoTermComputeGradientSetUseFD(), TaoTermComputeHessianFD(), TaoTermComputeHessianSetUseFD(), TaoTermComputeHessianGetUseFD()

src/tao/term/interface/taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermComputeGradient()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermComputeGradientGetUseFD(TaoTerm term, PetscBool *use_fd)
```

Example 3 (unknown):
```unknown
TaoTermGetFDDelta()
```

Example 4 (unknown):
```unknown
TaoTermSetFDDelta()
```

---

## TaoTermComputeGradientSetUseFD#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermComputeGradientSetUseFD/

**Contents:**
- TaoTermComputeGradientSetUseFD#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#

Set whether to use finite differences instead of the user-provided or built-in gradient method in TaoTermComputeGradient().

use_fd - PETSC_TRUE to use finite differences, PETSC_FALSE to use the user-provided or built-in gradient method

-tao_term_gradient_use_fd - use finite differences for gradient computation

TaoTerm: composable objective function terms, TaoTerm, TaoTermGetFDDelta(), TaoTermSetFDDelta(), TaoTermComputeGradientFD(), TaoTermComputeGradientGetUseFD(), TaoTermComputeHessianFD(), TaoTermComputeHessianSetUseFD(), TaoTermComputeHessianGetUseFD()

src/tao/term/interface/taoterm.c

src/tao/unconstrained/tutorials/rosenbrock1_taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermComputeGradient()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermComputeGradientSetUseFD(TaoTerm term, PetscBool use_fd)
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (unknown):
```unknown
TaoTermGetFDDelta()
```

---

## TaoTermComputeGradient#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermComputeGradient/

**Contents:**
- TaoTermComputeGradient#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Evaluate the gradient of a TaoTerm for a given solution vector and parameter vector

term - a TaoTerm representing a parametric function \(f(x; p)\)

x - the solution variable \(x\) in \(f(x; p)\)

params - the parameters \(p\) in \(f(x; p)\) (may be NULL if the term is not parametric)

g - the value of \(\nabla_x f(x; p)\)

TaoTerm: composable objective function terms, TaoTerm, TaoTermComputeObjective(), TaoTermComputeObjectiveAndGradient(), TaoTermComputeHessian(), TaoTermShellSetGradient()

src/tao/term/interface/taoterm.c

TaoTermComputeGradient_Callbacks() in src/tao/term/impls/callbacks/taotermcallbacks.c TaoTermComputeGradient_Halfl2squared() in src/tao/term/impls/halfl2squared/taotermhalfl2squared.c TaoTermComputeGradient_L1() in src/tao/term/impls/l1/taoterml1.c TaoTermComputeGradient_Quadratic() in src/tao/term/impls/quadratic/taotermquadratic.c TaoTermComputeGradient_Test() in src/tao/term/impls/shell/tests/ex1.c TaoTermComputeGradient_Sum() in src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermComputeGradient(TaoTerm term, Vec x, Vec params, Vec g)
```

Example 2 (unknown):
```unknown
TaoTermComputeObjective()
```

Example 3 (unknown):
```unknown
TaoTermComputeObjectiveAndGradient()
```

Example 4 (unknown):
```unknown
TaoTermComputeHessian()
```

---

## TaoTermComputeHessianFD#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermComputeHessianFD/

**Contents:**
- TaoTermComputeHessianFD#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#

Use finite difference to compute Hessian matrix.

x - a solution vector

params - parameters vector (may be NULL, see TaoTermParametersMode)

H - (optional) Hessian matrix

Hpre - (optional) Hessian preconditioning matrix

-tao_term_fd_delta - change in X used to calculate finite differences

-tao_term_hessian_use_fd - Use TaoTermComputeHessianFD() in TaoTermComputeHessian()

This routine is slow and expensive, and is not optimized to take advantage of sparsity in the problem. Although not recommended for general use in large-scale applications, it can be useful in checking the correctness of a user-provided Hessian. Call TaoTermComputeHessianSetUseFD() to start using this routine in TaoTermComputeHessian().

TaoTerm: composable objective function terms, TaoTerm, TaoTermComputeHessian(), TaoTermGetFDDelta(), TaoTermSetFDDelta(), TaoTermComputeHessianSetUseFD(), TaoTermComputeHessianGetUseFD()

src/tao/term/utils/taotermfdiff.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermComputeHessianFD(TaoTerm term, Vec x, Vec params, Mat H, Mat Hpre)
```

Example 2 (unknown):
```unknown
TaoTermParametersMode
```

Example 3 (unknown):
```unknown
TaoTermComputeHessianFD()
```

Example 4 (unknown):
```unknown
TaoTermComputeHessian()
```

---

## TaoTermComputeHessianGetUseFD#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermComputeHessianGetUseFD/

**Contents:**
- TaoTermComputeHessianGetUseFD#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get whether finite differences are used in TaoTermComputeHessian().

use_fd - PETSC_TRUE if finite differences are used

TaoTerm: composable objective function terms, TaoTerm, TaoTermGetFDDelta(), TaoTermSetFDDelta(), TaoTermComputeGradientFD(), TaoTermComputeGradientSetUseFD(), TaoTermComputeGradientGetUseFD(), TaoTermComputeHessianFD(), TaoTermComputeHessianSetUseFD()

src/tao/term/interface/taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermComputeHessian()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermComputeHessianGetUseFD(TaoTerm term, PetscBool *use_fd)
```

Example 3 (unknown):
```unknown
TaoTermGetFDDelta()
```

Example 4 (unknown):
```unknown
TaoTermSetFDDelta()
```

---

## TaoTermComputeHessianMFFD#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermComputeHessianMFFD/

**Contents:**
- TaoTermComputeHessianMFFD#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#

Update a matrix-free finite-difference MATMFFD Hessian created by TaoTermCreateHessianMFFD() to represent the Hessian of a TaoTerm at a given point and parameters.

x - the point at which the Hessian is to be applied

params - the current parameter vector for term, or NULL

H - the MATMFFD Hessian, reinitialized if needed and updated to base point x

B - the preconditioning matrix (unused; retained for API symmetry), or NULL

If H has not yet been initialized for this TaoTerm, this routine initializes it via TaoTermInitializeHessianMFFD(); passing a shell matrix from a different TaoTerm is an error.

TaoTerm, TaoTermCreateHessianMFFD(), TaoTermComputeHessian(), MATMFFD

src/tao/term/utils/taotermfdiff.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermCreateHessianMFFD()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermComputeHessianMFFD(TaoTerm term, Vec x, Vec params, Mat H, Mat B)
```

Example 3 (unknown):
```unknown
TaoTermInitializeHessianMFFD()
```

Example 4 (unknown):
```unknown
TaoTermCreateHessianMFFD()
```

---

## TaoTermComputeHessianSetUseFD#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermComputeHessianSetUseFD/

**Contents:**
- TaoTermComputeHessianSetUseFD#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#

Set whether to use finite differences instead of the user-provided or built-in methods in TaoTermComputeHessian().

use_fd - PETSC_TRUE to use finite differences, PETSC_FALSE to use the user-provided or built-in Hessian method

-tao_term_hessian_use_fd - use finite differences for Hessian computation

TaoTerm: composable objective function terms, TaoTerm, TaoTermGetFDDelta(), TaoTermSetFDDelta(), TaoTermComputeGradientFD(), TaoTermComputeGradientSetUseFD(), TaoTermComputeGradientGetUseFD(), TaoTermComputeHessianFD(), TaoTermComputeHessianGetUseFD()

src/tao/term/interface/taoterm.c

src/tao/unconstrained/tutorials/rosenbrock1_taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermComputeHessian()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermComputeHessianSetUseFD(TaoTerm term, PetscBool use_fd)
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (unknown):
```unknown
TaoTermGetFDDelta()
```

---

## TaoTermComputeHessian#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermComputeHessian/

**Contents:**
- TaoTermComputeHessian#
- Synopsis#
- Input Parameters#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Evaluate the Hessian of a TaoTerm (with respect to the solution variables) for a given solution vector and parameter vector

term - a TaoTerm representing a parametric function \(f(x; p)\)

x - the solution variable \(x\) in \(f(x; p)\)

params - the parameters \(p\) in \(f(x; p)\) (may be NULL if the term is not parametric)

H - Hessian matrix \(\nabla_x^2 f(x;p)\)

Hpre - an (approximate) Hessian from which the preconditioner will be constructed, often the same as H

If there is no separate matrix from which to construct the preconditioner, then TaoTermComputeHessian(term, x, params, H, NULL) and TaoTermComputeHessian(term, x, params, H, H) are equivalent.

TaoTerm: composable objective function terms, TaoTerm, TaoTermComputeObjective(), TaoTermComputeGradient(), TaoTermComputeObjectiveAndGradient(), TaoTermShellSetHessian()

src/tao/term/interface/taoterm.c

TaoTermComputeHessian_Callbacks() in src/tao/term/impls/callbacks/taotermcallbacks.c TaoTermComputeHessian_Halfl2squared() in src/tao/term/impls/halfl2squared/taotermhalfl2squared.c TaoTermComputeHessian_L1() in src/tao/term/impls/l1/taoterml1.c TaoTermComputeHessian_Quadratic() in src/tao/term/impls/quadratic/taotermquadratic.c TaoTermComputeHessian_Sum() in src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermComputeHessian(TaoTerm term, Vec x, Vec params, Mat H, Mat Hpre)
```

Example 2 (unknown):
```unknown
TaoTermComputeHessian(term, x, params, H, NULL)
```

Example 3 (unknown):
```unknown
TaoTermComputeHessian(term, x, params, H, H)
```

Example 4 (unknown):
```unknown
TaoTermComputeObjective()
```

---

## TaoTermComputeObjectiveAndGradient#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermComputeObjectiveAndGradient/

**Contents:**
- TaoTermComputeObjectiveAndGradient#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Evaluate both the value and gradient of a TaoTerm for a given set of solution vector and parameter vector

term - a TaoTerm representing a parametric function \(f(x; p)\)

x - the solution variable \(x\) in \(f(x; p)\)

params - the parameters \(p\) in \(f(x; p)\) (may be NULL if the term is not parametric)

value - the value of \(f(x; p)\)

g - the value of \(\nabla_x f(x; p)\)

TaoTerm: composable objective function terms, TaoTerm, TaoTermComputeObjective(), TaoTermComputeGradient(), TaoTermComputeHessian(), TaoTermShellSetObjectiveAndGradient()

src/tao/term/interface/taoterm.c

TaoTermComputeObjectiveAndGradient_Callbacks() in src/tao/term/impls/callbacks/taotermcallbacks.c TaoTermComputeObjectiveAndGradient_Halfl2squared() in src/tao/term/impls/halfl2squared/taotermhalfl2squared.c TaoTermComputeObjectiveAndGradient_L1() in src/tao/term/impls/l1/taoterml1.c TaoTermComputeObjectiveAndGradient_Quadratic() in src/tao/term/impls/quadratic/taotermquadratic.c TaoTermComputeObjectiveAndGradient_Test() in src/tao/term/impls/shell/tests/ex1.c TaoTermComputeObjectiveAndGradient_Sum() in src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermComputeObjectiveAndGradient(TaoTerm term, Vec x, Vec params, PetscReal *value, Vec g)
```

Example 2 (unknown):
```unknown
TaoTermComputeObjective()
```

Example 3 (unknown):
```unknown
TaoTermComputeGradient()
```

Example 4 (unknown):
```unknown
TaoTermComputeHessian()
```

---

## TaoTermComputeObjective#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermComputeObjective/

**Contents:**
- TaoTermComputeObjective#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Evaluate a TaoTerm for a given solution vector and parameter vector

term - a TaoTerm representing a parametric function \(f(x; p)\)

x - the solution variable \(x\) in \(f(x; p)\)

params - the parameters \(p\) in \(f(x; p)\) (may be NULL if the term is not parametric)

value - the value of \(f(x; p)\)

TaoTerm: composable objective function terms, TaoTerm, TaoTermComputeGradient(), TaoTermComputeObjectiveAndGradient(), TaoTermComputeHessian(), TaoTermShellSetObjective()

src/tao/term/interface/taoterm.c

TaoTermComputeObjective_Callbacks() in src/tao/term/impls/callbacks/taotermcallbacks.c TaoTermComputeObjective_Halfl2squared() in src/tao/term/impls/halfl2squared/taotermhalfl2squared.c TaoTermComputeObjective_L1() in src/tao/term/impls/l1/taoterml1.c TaoTermComputeObjective_Quadratic() in src/tao/term/impls/quadratic/taotermquadratic.c TaoTermComputeObjective_Test() in src/tao/term/impls/shell/tests/ex1.c TaoTermComputeObjective_Sum() in src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermComputeObjective(TaoTerm term, Vec x, Vec params, PetscReal *value)
```

Example 2 (unknown):
```unknown
TaoTermComputeGradient()
```

Example 3 (unknown):
```unknown
TaoTermComputeObjectiveAndGradient()
```

Example 4 (unknown):
```unknown
TaoTermComputeHessian()
```

---

## TaoTermCreateHalfL2Squared#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermCreateHalfL2Squared/

**Contents:**
- TaoTermCreateHalfL2Squared#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Create a TaoTerm for the objective term \(\tfrac{1}{2}\|x - p\|_2^2\), for solution \(x\) and parameters \(p\).

comm - the MPI communicator where the TaoTerm will be computed

n - the local size of the \(x\) and \(p\) vectors (or PETSC_DECIDE)

N - the global size of the \(x\) and \(p\) vectors (or PETSC_DECIDE)

If you would like to add a Tikhonov regularization term \(\alpha \tfrac{1}{2}\|x\|_2^2\) to the objective function of a Tao, do the following:

If you would like to add a biased regularization term \(\alpha \tfrac{1}{2}\|x - p \|_2^2\), do the same but pass p as the parameters of the term:

TaoTerm: composable objective function terms, TaoTerm, TAOTERMHALFL2SQUARED, TaoTermCreateL1(), TaoTermCreateQuadratic()

src/tao/term/impls/halfl2squared/taotermhalfl2squared.c

src/tao/unconstrained/tutorials/elastic_net_regularization.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermCreateHalfL2Squared(MPI_Comm comm, PetscInt n, PetscInt N, TaoTerm *term)
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
VecGetSizes(x, &n, &N);
  TaoTermCreateHalfL2Squared(PetscObjectComm((PetscObject)x), n, N, &term);
  TaoAddTerm(tao, "reg_", alpha, term, NULL, NULL);
  TaoTermDestroy(&term);
```

---

## TaoTermCreateHessianMatricesDefault#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermCreateHessianMatricesDefault/

**Contents:**
- TaoTermCreateHessianMatricesDefault#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Developer Note#
- See Also#
- Level#
- Location#
- Examples#

Default routine for creating Hessian matrices that can be used by many TaoTerm implementations

H - (optional) a matrix that can store the Hessian computed in TaoTermComputeHessian()

Hpre - (optional) a matrix from which a preconditioner can be computed in TaoTermComputeHessian()

The behavior of this routine is determined by TaoTermSetCreateHessianMode(). If Hpre_is_H, then the same matrix will be returned for H and Hpre, otherwise they will be separate matrices, with the matrix types H_mattype and Hpre_mattype. If either type is MATMFFD, then it will create a shell matrix with TaoTermCreateHessianMFFD().

TaoTerm: composable objective function terms, TaoTerm, TaoTermComputeHessian(), TaoTermCreateHessianMatrices(), TaoTermGetCreateHessianMode(), TaoTermSetCreateHessianMode()

src/tao/term/interface/taoterm.c

src/tao/unconstrained/tutorials/rosenbrock1_taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermCreateHessianMatricesDefault(TaoTerm term, Mat *H, Mat *Hpre)
```

Example 2 (unknown):
```unknown
TaoTermComputeHessian()
```

Example 3 (unknown):
```unknown
TaoTermComputeHessian()
```

Example 4 (unknown):
```unknown
TaoTermSetCreateHessianMode()
```

---

## TaoTermCreateHessianMatrices#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermCreateHessianMatrices/

**Contents:**
- TaoTermCreateHessianMatrices#
- Synopsis#
- Input Parameter#
- Output Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Create the matrices that can be inputs to TaoTermComputeHessian()

H - (optional) a matrix that can store the Hessian computed in TaoTermComputeHessian()

Hpre - (optional) a matrix from which a preconditioner can be computed in TaoTermComputeHessian()

Before Hessian matrices can be created, the size of the solution vector space must be set (see the ways this can be done in TaoTermCreateSolutionVec()). If the term is a TAOTERMSHELL, TaoTermShellSetCreateHessianMatrices() must be called. Most TaoTerms use TaoTermCreateHessianMatricesDefault() to create their Hessian matrices: the behavior of that function can be controlled by TaoTermSetCreateHessianMode().

TaoTerm: composable objective function terms, TaoTerm, TaoTermComputeHessian(), TaoTermShellSetCreateHessianMatrices(), TaoTermCreateSolutionVec(), TaoTermCreateHessianMatricesDefault(), TaoTermGetCreateHessianMode(), TaoTermSetCreateHessianMode(), TaoTermIsCreateHessianMatricesDefined()

src/tao/term/interface/taoterm.c

TaoTermCreateHessianMatrices_Callbacks() in src/tao/term/impls/callbacks/taotermcallbacks.c TaoTermCreateHessianMatrices_Halfl2squared() in src/tao/term/impls/halfl2squared/taotermhalfl2squared.c TaoTermCreateHessianMatrices_L1() in src/tao/term/impls/l1/taoterml1.c TaoTermCreateHessianMatrices_Quadratic() in src/tao/term/impls/quadratic/taotermquadratic.c TaoTermCreateHessianMatrices_Sum() in src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermComputeHessian()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermCreateHessianMatrices(TaoTerm term, Mat *H, Mat *Hpre)
```

Example 3 (unknown):
```unknown
TaoTermComputeHessian()
```

Example 4 (unknown):
```unknown
TaoTermComputeHessian()
```

---

## TaoTermCreateHessianMFFD#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermCreateHessianMFFD/

**Contents:**
- TaoTermCreateHessianMFFD#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Create a MATMFFD for a matrix-free finite-difference approximation of the Hessian of a TaoTerm

mffd - a Mat of type MATMFFD

TaoTerm: composable objective function terms, TaoTerm, TaoTermComputeHessianFD()

src/tao/term/utils/taotermfdiff.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermCreateHessianMFFD(TaoTerm term, Mat *mffd)
```

Example 2 (unknown):
```unknown
TaoTermComputeHessianFD()
```

---

## TaoTermCreateL1#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermCreateL1/

**Contents:**
- TaoTermCreateL1#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Create a TaoTerm for the objective function term \(\|x - p\|_1\).

comm - the MPI communicator where the term will be computed

n - the local size of the \(x\) and \(p\) vectors (or PETSC_DECIDE)

N - the global size of the \(x\) and \(p\) vectors (or PETSC_DECIDE)

epsilon - a non-negative smoothing parameter (see TaoTermL1SetEpsilon())

If you would like to add an L1 regularization term \(\alpha \|x\|_1\) to the objective function of a Tao, do the following:

If you would like to have a dictionary matrix term \(\alpha \|D x\|_1\), do the same but pass D as the map of the term:

TaoTerm: composable objective function terms, TaoTerm, TAOTERML1, TaoTermL1GetEpsilon(), TaoTermL1SetEpsilon(), TaoTermCreateHalfL2Squared(), TaoTermCreateQuadratic()

src/tao/term/impls/l1/taoterml1.c

src/tao/unconstrained/tutorials/elastic_net_regularization.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermCreateL1(MPI_Comm comm, PetscInt n, PetscInt N, PetscReal epsilon, TaoTerm *term)
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
TaoTermL1SetEpsilon()
```

---

## TaoTermCreateParametersVec#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermCreateParametersVec/

**Contents:**
- TaoTermCreateParametersVec#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Create a parameter vector for a TaoTerm

parameters - a compatible parameter vector for term

Before a TaoTerm can create a parameter vector, you must do one of the following:

Call TaoTermSetParametersSizes() to describe the size and parallel layout of a parameters vector.

Call TaoTermSetParametersLayout() to directly set PetscLayouts for the parameters vector.

Call TaoTermSetParametersTemplate() to set the parameters vector spaces to match existing Vec.

If the TaoTerm is a TAOTERMSHELL, you can call TaoTermShellSetCreateParametersVec() to use your own code for creating vectors.

You can also call TaoTermSetParametersVecType() to set the type of vector created (e.g. VECCUDA).

TaoTerm: composable objective function terms, TaoTerm, TaoTermShellSetCreateParametersVec(), TaoTermGetParametersSizes(), TaoTermSetParametersSizes(), TaoTermSetParametersTemplate(), TaoTermGetParametersVecType(), TaoTermSetParametersVecType(), TaoTermGetParametersLayout(), TaoTermSetParametersLayout(), TaoTermCreateHessianMatrices()

src/tao/term/interface/taoterm.c

TaoTermCreateParametersVec_Test() in src/tao/term/impls/shell/tests/ex1.c TaoTermCreateParametersVec_Sum() in src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermCreateParametersVec(TaoTerm term, Vec *parameters)
```

Example 2 (unknown):
```unknown
TaoTermSetParametersSizes()
```

Example 3 (unknown):
```unknown
TaoTermSetParametersLayout()
```

Example 4 (unknown):
```unknown
PetscLayout
```

---

## TaoTermCreateQuadratic#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermCreateQuadratic/

**Contents:**
- TaoTermCreateQuadratic#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Create a TAOTERMQUADRATIC for a given matrix

term - a TaoTerm that implements \(\tfrac{1}{2}(x - p)^T A (x - p)\)

TaoTerm: composable objective function terms, TaoTerm, TaoTermCreate(), TAOTERMQUADRATIC, TaoTermCreateHalfL2Squared(), TaoTermCreateL1(), TaoTermQuadraticSetMat()

src/tao/term/impls/quadratic/taotermquadratic.c

src/tao/unconstrained/tutorials/elastic_net_regularization.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TAOTERMQUADRATIC
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermCreateQuadratic(Mat A, TaoTerm *term)
```

Example 3 (unknown):
```unknown
TaoTermCreate()
```

Example 4 (unknown):
```unknown
TAOTERMQUADRATIC
```

---

## TaoTermCreateShell#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermCreateShell/

**Contents:**
- TaoTermCreateShell#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Create a TaoTerm of type TAOTERMSHELL that is ready to accept user-provided callback operations.

comm - the MPI communicator for computing the term

ctx - (optional) a context to be used by routines

destroy - (optional) a routine to destroy the context when term is destroyed

term - a TaoTerm of type TAOTERMSHELL

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSHELL

src/tao/term/impls/shell/taotermshell.c

src/tao/unconstrained/tutorials/rosenbrock1_taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TAOTERMSHELL
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermCreateShell(MPI_Comm comm, PetscCtx ctx, PetscCtxDestroyFn *destroy, TaoTerm *term)
```

Example 3 (unknown):
```unknown
TAOTERMSHELL
```

Example 4 (unknown):
```unknown
TAOTERMSHELL
```

---

## TaoTermCreateSolutionVec#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermCreateSolutionVec/

**Contents:**
- TaoTermCreateSolutionVec#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Create a solution vector for a TaoTerm

solution - a compatible solution vector for term

Before a TaoTerm can create a solution vector, you must do one of the following:

Call TaoTermSetSolutionSizes() to describe the size and parallel layout of a solution vector.

Call TaoTermSetSolutionLayout() to directly set PetscLayouts for the solution vector.

Call TaoTermSetSolutionTemplate() to set the solution vector spaces to match existing Vec.

If the TaoTerm is a TAOTERMSHELL, you can call TaoTermShellSetCreateSolutionVec() to use your own code for creating vectors.

You can also call TaoTermSetSolutionVecType() to set the type of vector created (e.g. VECCUDA).

TaoTerm: composable objective function terms, TaoTerm, TaoTermShellSetCreateSolutionVec(), TaoTermGetSolutionSizes(), TaoTermSetSolutionSizes(), TaoTermSetSolutionTemplate(), TaoTermGetSolutionVecType(), TaoTermSetSolutionVecType(), TaoTermGetSolutionLayout(), TaoTermSetSolutionLayout(), TaoTermCreateHessianMatrices()

src/tao/term/interface/taoterm.c

src/tao/unconstrained/tutorials/elastic_net_regularization.c

TaoTermCreateSolutionVec_Test() in src/tao/term/impls/shell/tests/ex1.c TaoTermCreateSolutionVec_Sum() in src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermCreateSolutionVec(TaoTerm term, Vec *solution)
```

Example 2 (unknown):
```unknown
TaoTermSetSolutionSizes()
```

Example 3 (unknown):
```unknown
TaoTermSetSolutionLayout()
```

Example 4 (unknown):
```unknown
PetscLayout
```

---

## TaoTermCreate#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermCreate/

**Contents:**
- TaoTermCreate#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Create a TaoTerm to use in defining the function Tao is to optimize

comm - communicator for MPI processes that compute the term

TaoTerm: composable objective function terms, TaoTerm, TaoTermSetType(), TaoAddTerm(), TaoTermSetFromOptions(), TaoTermSetUp(), TaoTermView(), TaoTermDestroy()

src/tao/term/interface/taoterm.c

src/tao/term/tutorials/ex1.c

TaoTermCreate_Callbacks() in src/tao/term/impls/callbacks/taotermcallbacks.c TaoTermCreate_Halfl2squared() in src/tao/term/impls/halfl2squared/taotermhalfl2squared.c TaoTermCreate_L1() in src/tao/term/impls/l1/taoterml1.c TaoTermCreate_Quadratic() in src/tao/term/impls/quadratic/taotermquadratic.c TaoTermCreate_Shell() in src/tao/term/impls/shell/taotermshell.c TaoTermCreate_Sum() in src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermCreate(MPI_Comm comm, TaoTerm *term)
```

Example 2 (unknown):
```unknown
TaoTermSetType()
```

Example 3 (unknown):
```unknown
TaoAddTerm()
```

Example 4 (unknown):
```unknown
TaoTermSetFromOptions()
```

---

## TaoTermDestroy#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermDestroy/

**Contents:**
- TaoTermDestroy#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

TaoTerm: composable objective function terms, TaoTerm, TaoTermCreate(), TaoTermSetType(), TaoTermSetFromOptions(), TaoTermSetUp(), TaoTermView()

src/tao/term/interface/taoterm.c

src/tao/unconstrained/tutorials/rosenbrock1_taoterm.c src/tao/term/tutorials/ex1.c src/tao/unconstrained/tutorials/elastic_net_regularization.c

TaoTermDestroy_Callbacks() in src/tao/term/impls/callbacks/taotermcallbacks.c TaoTermDestroy_Halfl2squared() in src/tao/term/impls/halfl2squared/taotermhalfl2squared.c TaoTermDestroy_L1() in src/tao/term/impls/l1/taoterml1.c TaoTermDestroy_Quadratic() in src/tao/term/impls/quadratic/taotermquadratic.c TaoTermDestroy_Shell() in src/tao/term/impls/shell/taotermshell.c TaoTermDestroy_Sum() in src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermDestroy(TaoTerm *term)
```

Example 2 (unknown):
```unknown
TaoTermCreate()
```

Example 3 (unknown):
```unknown
TaoTermSetType()
```

Example 4 (unknown):
```unknown
TaoTermSetFromOptions()
```

---

## TaoTermDuplicateOption#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermDuplicateOption/

**Contents:**
- TaoTermDuplicateOption#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#
- Examples#

Aspects to preserve when duplicating a TaoTerm

TAOTERM_DUPLICATE_SIZEONLY - duplicates size of the solution space only; user must set appropriate TaoTermType

TAOTERM_DUPLICATE_TYPE - TaoTermType preserved

TaoTerm, TaoTermDuplicate()

include/petsctaoterm.h

src/tao/term/tutorials/ex1.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  TAOTERM_DUPLICATE_SIZEONLY,
  TAOTERM_DUPLICATE_TYPE
} TaoTermDuplicateOption;
```

Example 2 (unknown):
```unknown
TAOTERM_DUPLICATE_SIZEONLY
```

Example 3 (unknown):
```unknown
TaoTermType
```

Example 4 (unknown):
```unknown
TAOTERM_DUPLICATE_TYPE
```

---

## TaoTermDuplicate#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermDuplicate/

**Contents:**
- TaoTermDuplicate#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

opt - TAOTERM_DUPLICATE_SIZEONLY or TAOTERM_DUPLICATE_TYPE

newterm - the duplicate TaoTerm

This function duplicates the solution space layout and vector type, but does not duplicate parameters-related configuration such as the parameters layout, TaoTermParametersMode, Hessian matrix types, or finite-difference settings. These must be set separately on the new TaoTerm if needed.

If TAOTERM_DUPLICATE_SIZEONLY is used, then the duplicated term must have proper TaoTermType set with TaoTermSetType().

TaoTerm: composable objective function terms, TaoTerm, TaoTermDuplicateOption

src/tao/term/interface/taoterm.c

src/tao/term/tutorials/ex1.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermDuplicate(TaoTerm term, TaoTermDuplicateOption opt, TaoTerm *newterm)
```

Example 2 (unknown):
```unknown
TAOTERM_DUPLICATE_SIZEONLY
```

Example 3 (unknown):
```unknown
TAOTERM_DUPLICATE_TYPE
```

Example 4 (unknown):
```unknown
TaoTermParametersMode
```

---

## TaoTermGetCreateHessianMode#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermGetCreateHessianMode/

**Contents:**
- TaoTermGetCreateHessianMode#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Get the behavior of TaoTermCreateHessianMatricesDefault().

Hpre_is_H - (optional) should TaoTermCreateHessianMatricesDefault() make one matrix for H and Hpre?

H_mattype - (optional) the MatType to create for H

Hpre_mattype - (optional) the MatType to create for Hpre

TaoTerm: composable objective function terms, TaoTerm, TaoTermComputeHessian(), TaoTermCreateHessianMatrices(), TaoTermCreateHessianMatricesDefault(), TaoTermSetCreateHessianMode()

src/tao/term/interface/taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermCreateHessianMatricesDefault()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermGetCreateHessianMode(TaoTerm term, PetscBool *Hpre_is_H, MatType *H_mattype, MatType *Hpre_mattype)
```

Example 3 (unknown):
```unknown
TaoTermCreateHessianMatricesDefault()
```

Example 4 (unknown):
```unknown
TaoTermComputeHessian()
```

---

## TaoTermGetFDDelta#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermGetFDDelta/

**Contents:**
- TaoTermGetFDDelta#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

Get the increment used for finite difference derivative approximations in methods like TaoTermComputeGradientFD()

delta - the finite difference increment

-tao_term_fd_delta - the above increment

TaoTerm: composable objective function terms, TaoTerm, TaoTermSetFDDelta(), TaoTermComputeGradientFD(), TaoTermComputeGradientSetUseFD(), TaoTermComputeGradientGetUseFD()

src/tao/term/interface/taoterm.c

src/tao/unconstrained/tutorials/rosenbrock1_taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermComputeGradientFD()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermGetFDDelta(TaoTerm term, PetscReal *delta)
```

Example 3 (unknown):
```unknown
TaoTermSetFDDelta()
```

Example 4 (unknown):
```unknown
TaoTermComputeGradientFD()
```

---

## TaoTermGetParametersLayout#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermGetParametersLayout/

**Contents:**
- TaoTermGetParametersLayout#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the layouts describing the parameter vectors of a TaoTerm.

parameters_layout - the PetscLayout for the parameter space

TaoTerm: composable objective function terms, TaoTerm, TaoTermGetParametersVecType(), TaoTermSetParametersVecType(), TaoTermSetParametersLayout(), TaoTermSetSolutionTemplate(), TaoTermSetParametersTemplate(), TaoTermCreateParametersVec()

src/tao/term/interface/taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermGetParametersLayout(TaoTerm term, PetscLayout *parameters_layout)
```

Example 2 (unknown):
```unknown
PetscLayout
```

Example 3 (unknown):
```unknown
TaoTermGetParametersVecType()
```

Example 4 (unknown):
```unknown
TaoTermSetParametersVecType()
```

---

## TaoTermGetParametersMode#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermGetParametersMode/

**Contents:**
- TaoTermGetParametersMode#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Gets the way a TaoTerm can accept parameters

parameters_mode - TAOTERM_PARAMETERS_OPTIONAL, TAOTERM_PARAMETERS_NONE, TAOTERM_PARAMETERS_REQUIRED

TaoTerm: composable objective function terms, TaoTerm, TaoTermParametersMode, TaoTermSetParametersMode()

src/tao/term/interface/taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermGetParametersMode(TaoTerm term, TaoTermParametersMode *parameters_mode)
```

Example 2 (unknown):
```unknown
TAOTERM_PARAMETERS_OPTIONAL
```

Example 3 (unknown):
```unknown
TAOTERM_PARAMETERS_NONE
```

Example 4 (unknown):
```unknown
TAOTERM_PARAMETERS_REQUIRED
```

---

## TaoTermGetParametersSizes#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermGetParametersSizes/

**Contents:**
- TaoTermGetParametersSizes#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Get the sizes describing the layout of the parameter vector space of a TaoTerm.

k - (optional) the size of a parameter vector on the current MPI process

K - (optional) the global size of a parameter vector

bs - (optional) the block size of a parameter vector

TaoTerm: composable objective function terms, TaoTerm, TaoTermSetParametersSizes(), TaoTermSetParametersTemplate(), TaoTermGetParametersVecType(), TaoTermSetParametersVecType(), TaoTermGetParametersLayout(), TaoTermSetParametersLayout(), TaoTermCreateParametersVec()

src/tao/term/interface/taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermGetParametersSizes(TaoTerm term, PetscInt *k, PetscInt *K, PetscInt *bs)
```

Example 2 (unknown):
```unknown
TaoTermSetParametersSizes()
```

Example 3 (unknown):
```unknown
TaoTermSetParametersTemplate()
```

Example 4 (unknown):
```unknown
TaoTermGetParametersVecType()
```

---

## TaoTermGetParametersVecType#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermGetParametersVecType/

**Contents:**
- TaoTermGetParametersVecType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the vector types of the parameter vector of a TaoTerm

parameters_type - the VecType for the parameter space

TaoTerm: composable objective function terms, TaoTerm, TaoTermSetParametersVecType(), TaoTermGetParametersLayout(), TaoTermSetParametersLayout(), TaoTermSetSolutionTemplate(), TaoTermSetParametersTemplate(), TaoTermCreateParametersVec()

src/tao/term/interface/taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermGetParametersVecType(TaoTerm term, VecType *parameters_type)
```

Example 2 (unknown):
```unknown
TaoTermSetParametersVecType()
```

Example 3 (unknown):
```unknown
TaoTermGetParametersLayout()
```

Example 4 (unknown):
```unknown
TaoTermSetParametersLayout()
```

---

## TaoTermGetSolutionLayout#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermGetSolutionLayout/

**Contents:**
- TaoTermGetSolutionLayout#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the layouts describing the solution vectors of a TaoTerm.

solution_layout - the PetscLayout for the solution space

TaoTerm: composable objective function terms, TaoTerm, TaoTermGetSolutionVecType(), TaoTermSetSolutionVecType(), TaoTermSetSolutionLayout(), TaoTermSetSolutionTemplate(), TaoTermSetParametersTemplate(), TaoTermCreateSolutionVec()

src/tao/term/interface/taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermGetSolutionLayout(TaoTerm term, PetscLayout *solution_layout)
```

Example 2 (unknown):
```unknown
PetscLayout
```

Example 3 (unknown):
```unknown
TaoTermGetSolutionVecType()
```

Example 4 (unknown):
```unknown
TaoTermSetSolutionVecType()
```

---

## TaoTermGetSolutionSizes#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermGetSolutionSizes/

**Contents:**
- TaoTermGetSolutionSizes#
- Synopsis#
- Input Parameter#
- Output Parameters#
- See Also#
- Level#
- Location#

Get the sizes describing the layout of the solution vector space of a TaoTerm.

n - (optional) the size of a solution vector on the current MPI process

N - (optional) the global size of a solution vector

bs - (optional) the block size of a solution vector

TaoTerm: composable objective function terms, TaoTerm, TaoTermSetSolutionSizes(), TaoTermSetSolutionTemplate(), TaoTermGetSolutionVecType(), TaoTermSetSolutionVecType(), TaoTermGetSolutionLayout(), TaoTermSetSolutionLayout(), TaoTermCreateSolutionVec()

src/tao/term/interface/taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermGetSolutionSizes(TaoTerm term, PetscInt *n, PetscInt *N, PetscInt *bs)
```

Example 2 (unknown):
```unknown
TaoTermSetSolutionSizes()
```

Example 3 (unknown):
```unknown
TaoTermSetSolutionTemplate()
```

Example 4 (unknown):
```unknown
TaoTermGetSolutionVecType()
```

---

## TaoTermGetSolutionVecType#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermGetSolutionVecType/

**Contents:**
- TaoTermGetSolutionVecType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Get the vector types of the solution vector of a TaoTerm

solution_type - the VecType for the solution space

TaoTerm: composable objective function terms, TaoTerm, TaoTermSetSolutionVecType(), TaoTermGetSolutionLayout(), TaoTermSetSolutionLayout(), TaoTermSetSolutionTemplate(), TaoTermSetParametersTemplate(), TaoTermCreateSolutionVec()

src/tao/term/interface/taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermGetSolutionVecType(TaoTerm term, VecType *solution_type)
```

Example 2 (unknown):
```unknown
TaoTermSetSolutionVecType()
```

Example 3 (unknown):
```unknown
TaoTermGetSolutionLayout()
```

Example 4 (unknown):
```unknown
TaoTermSetSolutionLayout()
```

---

## TaoTermGetType#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermGetType/

**Contents:**
- TaoTermGetType#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#

Get the type of a TaoTerm

type - the TaoTermType

TaoTerm: composable objective function terms, TaoTerm, TaoTermType, TaoTermCreate(), TaoTermSetType(), TaoTermSetFromOptions(), TaoTermSetUp(), TaoTermView(), TaoTermDestroy()

src/tao/term/interface/taoterm.c

src/tao/term/tutorials/ex1.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermGetType(TaoTerm term, TaoTermType *type)
```

Example 2 (unknown):
```unknown
TaoTermType
```

Example 3 (unknown):
```unknown
TaoTermType
```

Example 4 (unknown):
```unknown
TaoTermCreate()
```

---

## TaoTermGradientFn#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermGradientFn/

**Contents:**
- TaoTermGradientFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

A prototype of a TaoTerm function that would be passed to TaoTermShellSetGradient()

x - the solution vector

params - the parameters vector (for some TaoTerm this may be NULL, see TaoTermGetParametersMode())

g - output, the gradient of the term

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSHELL, TaoTermShellSetGradient(), TaoTermObjectiveFn, TaoTermObjectiveAndGradientFn, TaoTermHessianFn

include/petsctaoterm.h

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermShellSetGradient()
```

Example 2 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode(TaoTermGradientFn)(TaoTerm term, Vec x, Vec params, Vec g);
```

Example 3 (unknown):
```unknown
TaoTermGetParametersMode()
```

Example 4 (unknown):
```unknown
TAOTERMSHELL
```

---

## TAOTERMHALFL2SQUARED#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TAOTERMHALFL2SQUARED/

**Contents:**
- TAOTERMHALFL2SQUARED#
- Notes#
- See Also#
- Level#
- Location#

A TaoTerm that computes \(\tfrac{1}{2}\|x - p\|_2^2\), for solution \(x\) and parameters \(p\).

By default this term is TAOTERM_PARAMETERS_OPTIONAL. If the parameters argument is NULL in the evaluation routines (TaoTermComputeObjective(), TaoTermComputeGradient(), etc.), then it is assumed \(p = 0\) and the term computes \(\tfrac{1}{2}\|x\|_2^2\).

The default Hessian creation mode (see TaoTermGetCreateHessianMode()) is H == Hpre and TaoTermCreateHessianMatrices() will create a MATDIAGONAL for the Hessian.

TaoTerm: composable objective function terms, TaoTerm, TaoTermType, TaoTermCreateHalfL2Squared(), TAOTERML1, TAOTERMQUADRATIC

src/tao/term/impls/halfl2squared/taotermhalfl2squared.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TAOTERM_PARAMETERS_OPTIONAL
```

Example 2 (unknown):
```unknown
TaoTermComputeObjective()
```

Example 3 (unknown):
```unknown
TaoTermComputeGradient()
```

Example 4 (unknown):
```unknown
TaoTermGetCreateHessianMode()
```

---

## TaoTermHessianFn#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermHessianFn/

**Contents:**
- TaoTermHessianFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

A prototype of a TaoTerm function that would be passed to TaoTermShellSetHessian()

x - the solution vector

params - the parameters vector (for some TaoTerm this may be NULL, see TaoTermGetParametersMode())

H - (optional) output, the Hessian of term

Hpre - (optional) output, the approximation of H from which a preconditioner may be built

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSHELL, TaoTermShellSetHessian(), TaoTermObjectiveFn, TaoTermObjectiveAndGradientFn, TaoTermGradientFn

include/petsctaoterm.h

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermShellSetHessian()
```

Example 2 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode(TaoTermHessianFn)(TaoTerm term, Vec x, Vec params, Mat H, Mat Hpre);
```

Example 3 (unknown):
```unknown
TaoTermGetParametersMode()
```

Example 4 (unknown):
```unknown
TAOTERMSHELL
```

---

## TaoTermIsComputeHessianFDPossible#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermIsComputeHessianFDPossible/

**Contents:**
- TaoTermIsComputeHessianFDPossible#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Whether this term can compute Hessian with finite differences with either -tao_term_hessian_use_fd, TaoTermComputeHessianSetUseFD(), or MATMFFD.

is_fdpossible - whether Hessian computation with finite differences is possible

TaoTerm: composable objective function terms, TaoTerm, TaoTermComputeObjective(), TaoTermShellSetObjective(), TaoTermIsGradientDefined(), TaoTermIsObjectiveAndGradientDefined(), TaoTermIsHessianDefined()

src/tao/term/interface/taoterm.c

TaoTermIsComputeHessianFDPossible_Halfl2squared() in src/tao/term/impls/halfl2squared/taotermhalfl2squared.c TaoTermIsComputeHessianFDPossible_L1() in src/tao/term/impls/l1/taoterml1.c TaoTermIsComputeHessianFDPossible_Quadratic() in src/tao/term/impls/quadratic/taotermquadratic.c TaoTermIsComputeHessianFDPossible_Shell() in src/tao/term/impls/shell/taotermshell.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
-tao_term_hessian_use_fd
```

Example 2 (unknown):
```unknown
TaoTermComputeHessianSetUseFD()
```

Example 3 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermIsComputeHessianFDPossible(TaoTerm term, PetscBool3 *is_fdpossible)
```

Example 4 (unknown):
```unknown
TaoTermComputeObjective()
```

---

## TaoTermIsCreateHessianMatricesDefined#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermIsCreateHessianMatricesDefined/

**Contents:**
- TaoTermIsCreateHessianMatricesDefined#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#

Whether this term can call TaoTermCreateHessianMatrices().

is_defined - whether the term can create new Hessian matrices

TaoTerm: composable objective function terms, TaoTerm, TaoTermCreateHessianMatrices(), TaoTermShellSetCreateHessianMatrices(), TaoTermIsObjectiveDefined(), TaoTermIsGradientDefined(), TaoTermIsObjectiveAndGradientDefined(), TaoTermIsHessianDefined()

src/tao/term/interface/taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermCreateHessianMatrices()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermIsCreateHessianMatricesDefined(TaoTerm term, PetscBool *is_defined)
```

Example 3 (unknown):
```unknown
TaoTermCreateHessianMatrices()
```

Example 4 (unknown):
```unknown
TaoTermShellSetCreateHessianMatrices()
```

---

## TaoTermIsGradientDefined#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermIsGradientDefined/

**Contents:**
- TaoTermIsGradientDefined#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Whether a standalone gradient operation is defined for this TaoTerm

is_defined - whether the gradient is defined

This function strictly checks whether a dedicated gradient operation is defined. It does not check whether the gradient could be computed via other operations (e.g., an objective-and-gradient callback or finite differences). TaoTermComputeGradient() may still succeed even if this function returns PETSC_FALSE, by falling back to TaoTermComputeObjectiveAndGradient() or finite-difference approximation.

TaoTerm: composable objective function terms, TaoTerm, TaoTermComputeGradient(), TaoTermShellSetGradient(), TaoTermIsObjectiveDefined(), TaoTermIsObjectiveAndGradientDefined(), TaoTermIsHessianDefined()

src/tao/term/interface/taoterm.c

TaoTermIsGradientDefined_Callbacks() in src/tao/term/impls/callbacks/taotermcallbacks.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermIsGradientDefined(TaoTerm term, PetscBool *is_defined)
```

Example 2 (unknown):
```unknown
TaoTermComputeGradient()
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (unknown):
```unknown
TaoTermComputeObjectiveAndGradient()
```

---

## TaoTermIsHessianDefined#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermIsHessianDefined/

**Contents:**
- TaoTermIsHessianDefined#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Whether a Hessian operation is defined for this TaoTerm

is_defined - whether the Hessian is defined

This function strictly checks whether a dedicated Hessian operation is defined. It does not check whether the Hessian could be computed via finite differences. TaoTermComputeHessian() may still succeed even if this function returns PETSC_FALSE, if finite-difference Hessian computation has been enabled.

TaoTerm: composable objective function terms, TaoTerm, TaoTermComputeHessian(), TaoTermShellSetHessian(), TaoTermIsObjectiveDefined(), TaoTermIsGradientDefined(), TaoTermIsObjectiveAndGradientDefined()

src/tao/term/interface/taoterm.c

TaoTermIsHessianDefined_Callbacks() in src/tao/term/impls/callbacks/taotermcallbacks.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermIsHessianDefined(TaoTerm term, PetscBool *is_defined)
```

Example 2 (unknown):
```unknown
TaoTermComputeHessian()
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (unknown):
```unknown
TaoTermComputeHessian()
```

---

## TaoTermIsObjectiveAndGradientDefined#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermIsObjectiveAndGradientDefined/

**Contents:**
- TaoTermIsObjectiveAndGradientDefined#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Whether a combined objective-and-gradient operation is defined for this TaoTerm

is_defined - whether the objective/gradient is defined

This function strictly checks whether a dedicated combined objective-and-gradient operation is defined. It does not check whether the objective and gradient could be computed via separate objective and gradient operations. TaoTermComputeObjectiveAndGradient() may still succeed even if this function returns PETSC_FALSE, by falling back to separate TaoTermComputeObjective() and TaoTermComputeGradient() calls.

TaoTerm: composable objective function terms, TaoTerm, TaoTermComputeObjectiveAndGradient(), TaoTermShellSetObjectiveAndGradient(), TaoTermIsObjectiveDefined(), TaoTermIsGradientDefined(), TaoTermIsHessianDefined()

src/tao/term/interface/taoterm.c

TaoTermIsObjectiveAndGradientDefined_Callbacks() in src/tao/term/impls/callbacks/taotermcallbacks.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermIsObjectiveAndGradientDefined(TaoTerm term, PetscBool *is_defined)
```

Example 2 (unknown):
```unknown
TaoTermComputeObjectiveAndGradient()
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (unknown):
```unknown
TaoTermComputeObjective()
```

---

## TaoTermIsObjectiveDefined#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermIsObjectiveDefined/

**Contents:**
- TaoTermIsObjectiveDefined#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Whether a standalone objective operation is defined for this TaoTerm

is_defined - whether the objective is defined

This function strictly checks whether a dedicated objective operation is defined. It does not check whether the objective could be computed via other operations (e.g., an objective-and-gradient callback). TaoTermComputeObjective() may still succeed even if this function returns PETSC_FALSE, by falling back to TaoTermComputeObjectiveAndGradient().

TaoTerm: composable objective function terms, TaoTerm, TaoTermComputeObjective(), TaoTermShellSetObjective(), TaoTermIsGradientDefined(), TaoTermIsObjectiveAndGradientDefined(), TaoTermIsHessianDefined()

src/tao/term/interface/taoterm.c

TaoTermIsObjectiveDefined_Callbacks() in src/tao/term/impls/callbacks/taotermcallbacks.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermIsObjectiveDefined(TaoTerm term, PetscBool *is_defined)
```

Example 2 (unknown):
```unknown
TaoTermComputeObjective()
```

Example 3 (unknown):
```unknown
PETSC_FALSE
```

Example 4 (unknown):
```unknown
TaoTermComputeObjectiveAndGradient()
```

---

## TaoTermL1GetEpsilon#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermL1GetEpsilon/

**Contents:**
- TaoTermL1GetEpsilon#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Get the \(\epsilon\) smoothing parameter set by TaoTermL1SetEpsilon().

term - a TaoTerm of type TAOTERML1

epsilon - the smoothing parameter

TaoTerm: composable objective function terms, TaoTerm, TAOTERML1, TaoTermL1SetEpsilon()

src/tao/term/impls/l1/taoterml1.c

src/tao/unconstrained/tutorials/elastic_net_regularization.c

TaoTermL1GetEpsilon_L1() in src/tao/term/impls/l1/taoterml1.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermL1SetEpsilon()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermL1GetEpsilon(TaoTerm term, PetscReal *epsilon)
```

Example 3 (unknown):
```unknown
TaoTermL1SetEpsilon()
```

---

## TaoTermL1SetEpsilon#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermL1SetEpsilon/

**Contents:**
- TaoTermL1SetEpsilon#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Implementations#

Set an \(\epsilon\) smoothing parameter.

term - a TaoTerm of type TAOTERML1

epsilon - a real number \(\geq 0\)

-tao_term_l1_epsilon - \(\epsilon\)

If \(\epsilon = 0\) (the default), then term computes \(\|x - p\|_1\), but if \(\epsilon > 0\), then it computes \(\sum_{i=0}^{n-1} \left(\sqrt{(x_i-p_i)^2 + \epsilon^2} - \epsilon\right)\).

TaoTerm: composable objective function terms, TaoTerm, TAOTERML1, TaoTermL1GetEpsilon()

src/tao/term/impls/l1/taoterml1.c

TaoTermL1SetEpsilon_L1() in src/tao/term/impls/l1/taoterml1.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermL1SetEpsilon(TaoTerm term, PetscReal epsilon)
```

Example 2 (unknown):
```unknown
TaoTermL1GetEpsilon()
```

---

## TAOTERML1#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TAOTERML1/

**Contents:**
- TAOTERML1#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

A TaoTerm that computes \(\|x - p\|_1\), for solution \(x\) and parameters \(p\).

-tao_term_l1_epsilon - (default 0.0) a smoothing parameter (see TaoTermL1SetEpsilon())

This term is TAOTERM_PARAMETERS_OPTIONAL. If the parameters argument is NULL for evaluation routines the term computes \(\|x\|_1\).

This term has a smoothing parameter \(\epsilon\) that defaults to 0: if \(\epsilon > 0\), the term computes a smooth approximation of \(\|x - p\|_1\), see TaoTermL1SetEpsilon().

The default Hessian creation mode (see TaoTermGetCreateHessianMode()) is H == Hpre and TaoTermCreateHessianMatrices() will create a MATDIAGONAL for the Hessian.

TaoTerm: composable objective function terms, TaoTerm, TaoTermType, TaoTermCreateL1(), TaoTermL1GetEpsilon(), TaoTermL1SetEpsilon(), TAOTERMHALFL2SQUARED, TAOTERMQUADRATIC

src/tao/term/impls/l1/taoterml1.c

src/tao/unconstrained/tutorials/elastic_net_regularization.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermL1SetEpsilon()
```

Example 2 (unknown):
```unknown
TAOTERM_PARAMETERS_OPTIONAL
```

Example 3 (unknown):
```unknown
TaoTermL1SetEpsilon()
```

Example 4 (unknown):
```unknown
TaoTermGetCreateHessianMode()
```

---

## TaoTermMask#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermMask/

**Contents:**
- TaoTermMask#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

Determine which evaluation operations are masked; that is, skipped (not used) by Tao when computing the objective function or its derivatives for a particular TaoTerm.

TAOTERM_MASK_NONE - do not mask any evaluation routines

TAOTERM_MASK_OBJECTIVE - override the term’s objective function and return 0 instead

TAOTERM_MASK_GRADIENT - override the term’s gradient and return a zero vector instead

TAOTERM_MASK_HESSIAN - override the term’s Hessian and return a zero matrix instead

TaoTerm: composable objective function terms, TaoTerm, TaoTermSumSetTermMask(), TaoTermSumGetTermMask()

include/petsctaoterm.h

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef enum {
  TAOTERM_MASK_NONE      = 0, /* 0x0 */
  TAOTERM_MASK_OBJECTIVE = 1, /* 0x1 */
  TAOTERM_MASK_GRADIENT  = 2, /* 0x2 */
  TAOTERM_MASK_HESSIAN   = 4  /* 0x4 */
} TaoTermMask;
```

Example 2 (unknown):
```unknown
TAOTERM_MASK_NONE
```

Example 3 (unknown):
```unknown
TAOTERM_MASK_OBJECTIVE
```

Example 4 (unknown):
```unknown
TAOTERM_MASK_GRADIENT
```

---

## TaoTermObjectiveAndGradientFn#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermObjectiveAndGradientFn/

**Contents:**
- TaoTermObjectiveAndGradientFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

A prototype of a TaoTerm function that would be passed to TaoTermShellSetObjectiveAndGradient()

x - the solution vector

params - the parameters vector (for some TaoTerm this may be NULL, see TaoTermGetParametersMode())

value - output, the value of the term

g - output, the gradient of the term

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSHELL, TaoTermShellSetObjectiveAndGradient(), TaoTermObjectiveFn, TaoTermGradientFn, TaoTermHessianFn

include/petsctaoterm.h

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermShellSetObjectiveAndGradient()
```

Example 2 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode(TaoTermObjectiveAndGradientFn)(TaoTerm term, Vec x, Vec params, PetscReal *value, Vec g);
```

Example 3 (unknown):
```unknown
TaoTermGetParametersMode()
```

Example 4 (unknown):
```unknown
TAOTERMSHELL
```

---

## TaoTermObjectiveFn#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermObjectiveFn/

**Contents:**
- TaoTermObjectiveFn#
- Synopsis#
- Calling Sequence#
- See Also#
- Level#
- Location#

A prototype of a TaoTerm function that would be passed to TaoTermShellSetObjective()

x - the solution vector

params - the parameters vector (for some TaoTerm this may be NULL, see TaoTermGetParametersMode())

value - output, the value of the term

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSHELL, TaoTermShellSetObjective(), TaoTermObjectiveAndGradientFn, TaoTermGradientFn, TaoTermHessianFn

include/petsctaoterm.h

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermShellSetObjective()
```

Example 2 (unknown):
```unknown
PETSC_EXTERN_TYPEDEF typedef PetscErrorCode(TaoTermObjectiveFn)(TaoTerm term, Vec x, Vec params, PetscReal *value);
```

Example 3 (unknown):
```unknown
TaoTermGetParametersMode()
```

Example 4 (unknown):
```unknown
TAOTERMSHELL
```

---

## TaoTermParametersMode#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermParametersMode/

**Contents:**
- TaoTermParametersMode#
- Synopsis#
- Values#
- Note#
- See Also#
- Level#
- Location#
- Examples#

Ways a TaoTerm can accept parameter vectors in TaoTermComputeObjective() and related functions

TAOTERM_PARAMETERS_OPTIONAL - the term has default parameters that will be used if parameters are omitted

TAOTERM_PARAMETERS_NONE - the term is not parametric, passing parameters is an error

TAOTERM_PARAMETERS_REQUIRED - the term requires parameters, omitting parameters is an error

Each TaoTerm represents a parametric real-valued function \(f(x; p)\), where \(x\) is the solution variable (the optimization variable) and \(p\) is a parameter vector of fixed data that is not optimized over. The solution space (the vector space of \(x\)) and the parameter space (the vector space of \(p\)) are set independently; see TaoTermSetSolutionSizes() and TaoTermSetParametersSizes().

TaoTerm: composable objective function terms, TaoTerm, TaoTermGetParametersMode(), TaoTermSetParametersMode()

include/petsctaoterm.h

src/tao/unconstrained/tutorials/rosenbrock1_taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermComputeObjective()
```

Example 2 (unknown):
```unknown
typedef enum {
  TAOTERM_PARAMETERS_OPTIONAL,
  TAOTERM_PARAMETERS_NONE,
  TAOTERM_PARAMETERS_REQUIRED
} TaoTermParametersMode;
```

Example 3 (unknown):
```unknown
TAOTERM_PARAMETERS_OPTIONAL
```

Example 4 (unknown):
```unknown
TAOTERM_PARAMETERS_NONE
```

---

## TaoTermQuadraticGetMat#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermQuadraticGetMat/

**Contents:**
- TaoTermQuadraticGetMat#
- Synopsis#
- Input Parameter#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Get the matrix defining a TaoTerm of type TAOTERMQUADRATIC

term - a TaoTerm of type TAOTERMQUADRATIC

This function will return NULL if the term is not a TAOTERMQUADRATIC.

TaoTerm: composable objective function terms, TaoTerm, TAOTERMQUADRATIC, TaoTermQuadraticSetMat()

src/tao/term/impls/quadratic/taotermquadratic.c

TaoTermQuadraticGetMat_Quadratic() in src/tao/term/impls/quadratic/taotermquadratic.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TAOTERMQUADRATIC
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermQuadraticGetMat(TaoTerm term, Mat *A)
```

Example 3 (unknown):
```unknown
TAOTERMQUADRATIC
```

Example 4 (unknown):
```unknown
TAOTERMQUADRATIC
```

---

## TaoTermQuadraticSetMat#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermQuadraticSetMat/

**Contents:**
- TaoTermQuadraticSetMat#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set the matrix defining a TaoTerm of type TAOTERMQUADRATIC

term - a TaoTerm of type TAOTERMQUADRATIC

TaoTerm: composable objective function terms, TaoTerm, TAOTERMQUADRATIC, TaoTermQuadraticGetMat()

src/tao/term/impls/quadratic/taotermquadratic.c

TaoTermQuadraticSetMat_Quadratic() in src/tao/term/impls/quadratic/taotermquadratic.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TAOTERMQUADRATIC
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermQuadraticSetMat(TaoTerm term, Mat A)
```

Example 3 (unknown):
```unknown
TAOTERMQUADRATIC
```

Example 4 (unknown):
```unknown
TAOTERMQUADRATIC
```

---

## TAOTERMQUADRATIC#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TAOTERMQUADRATIC/

**Contents:**
- TAOTERMQUADRATIC#
- Notes#
- See Also#
- Level#
- Location#

A TaoTerm that computes \(\tfrac{1}{2}(x - p)^T A (x - p)\), for a fixed matrix \(A\), solution \(x\) and parameters \(p\).

This term is TAOTERM_PARAMETERS_OPTIONAL. If the parameters argument is NULL for evaluation routines the term computes \(\tfrac{1}{2}x^T A x\).

The matrix \(A\) must be symmetric.

The default Hessian creation mode (see TaoTermGetCreateHessianMode()) is H == Hpre and TaoTermCreateHessianMatrices() will create a matrix with the same type as \(A\).

TaoTerm: composable objective function terms, TaoTerm, TaoTermType, TaoTermCreateQuadratic(), TAOTERMHALFL2SQUARED, TAOTERML1, TaoTermQuadraticSetMat()

src/tao/term/impls/quadratic/taotermquadratic.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TAOTERM_PARAMETERS_OPTIONAL
```

Example 2 (unknown):
```unknown
TaoTermGetCreateHessianMode()
```

Example 3 (unknown):
```unknown
TaoTermCreateHessianMatrices()
```

Example 4 (unknown):
```unknown
TaoTermType
```

---

## TaoTermRegister#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermRegister/

**Contents:**
- TaoTermRegister#
- Synopsis#
- Input Parameters#
- Example Usage#
- Note#
- See Also#
- Level#
- Location#

Register an implementation of TaoTerm

Not Collective, No Fortran Support

sname - name of a new user-defined term

func - routine to create the context for the TaoTermType

Then, your term can be chosen with the procedural interface via

or at runtime via the option

TaoTermRegister() may be called multiple times to add multiple new TaoTermType.

TaoTerm: composable objective function terms, TaoTerm, TaoTermSetType()

src/tao/term/interface/taotermregi.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermRegister(const char sname[], PetscErrorCode (*func)(TaoTerm))
```

Example 2 (unknown):
```unknown
TaoTermType
```

Example 3 (unknown):
```unknown
TaoTermRegister("my_term", MyTermCreate);
```

Example 4 (unknown):
```unknown
TaoTermSetType(term, "my_term")
```

---

## TaoTermSetCreateHessianMode#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSetCreateHessianMode/

**Contents:**
- TaoTermSetCreateHessianMode#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#

Determine the behavior of TaoTermCreateHessianMatricesDefault().

Hpre_is_H - should TaoTermCreateHessianMatricesDefault() make one matrix for H and Hpre?

H_mattype - the MatType to create for H

Hpre_mattype - the MatType to create for Hpre

-tao_term_hessian_pre_is_hessian - Whether TaoTermCreateHessianMatrices() should make a separate matrix for constructing the preconditioner

-tao_term_hessian_mat_type - MatType for Hessian matrix created by TaoTermCreateHessianMatrices()

-tao_term_hessian_pre_mat_type - MatType for matrix from which a preconditioner can be created by TaoTermCreateHessianMatrices()

TaoTerm: composable objective function terms, TaoTerm, TaoTermComputeHessian(), TaoTermCreateHessianMatrices(), TaoTermCreateHessianMatricesDefault(), TaoTermGetCreateHessianMode()

src/tao/term/interface/taoterm.c

src/tao/unconstrained/tutorials/rosenbrock1_taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermCreateHessianMatricesDefault()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSetCreateHessianMode(TaoTerm term, PetscBool Hpre_is_H, MatType H_mattype, MatType Hpre_mattype)
```

Example 3 (unknown):
```unknown
TaoTermCreateHessianMatricesDefault()
```

Example 4 (unknown):
```unknown
TaoTermCreateHessianMatrices()
```

---

## TaoTermSetFDDelta#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSetFDDelta/

**Contents:**
- TaoTermSetFDDelta#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#
- Examples#

Set the increment used for finite difference derivative approximations in methods like TaoTermComputeGradientFD()

delta - the finite difference increment

-tao_term_fd_delta - the above increment

TaoTerm: composable objective function terms, TaoTerm, TaoTermGetFDDelta(), TaoTermComputeGradientFD(), TaoTermComputeGradientSetUseFD(), TaoTermComputeGradientGetUseFD(), TaoTermComputeHessianFD(), TaoTermComputeHessianSetUseFD(), TaoTermComputeHessianGetUseFD()

src/tao/term/interface/taoterm.c

src/tao/unconstrained/tutorials/rosenbrock1_taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermComputeGradientFD()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSetFDDelta(TaoTerm term, PetscReal delta)
```

Example 3 (unknown):
```unknown
TaoTermGetFDDelta()
```

Example 4 (unknown):
```unknown
TaoTermComputeGradientFD()
```

---

## TaoTermSetFromOptions#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSetFromOptions/

**Contents:**
- TaoTermSetFromOptions#
- Synopsis#
- Input Parameter#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Configure a TaoTerm from the PETSc options database

-tao_term_type - l1, halfl2squared; see TaoTermType for a complete list

-tao_term_solution_vec_type - the type of vector to use for the solution, see VecType for a complete list of vector types

-tao_term_parameters_vec_type - the type of vector to use for the parameters, see VecType for a complete list of vector types

-tao_term_parameters_mode <optional,none,required> - TAOTERM_PARAMETERS_OPTIONAL, TAOTERM_PARAMETERS_NONE, TAOTERM_PARAMETERS_REQUIRED

-tao_term_hessian_pre_is_hessian - Whether TaoTermCreateHessianMatricesDefault() should make a separate preconditioning matrix

-tao_term_hessian_mat_type - MatType for Hessian matrix created by TaoTermCreateHessianMatricesDefault()

-tao_term_hessian_pre_mat_type - MatType for approximate Hessian matrix used to construct the preconditioner created by TaoTermCreateHessianMatricesDefault()

-tao_term_fd_delta - Increment for finite difference derivative approximations in TaoTermComputeGradientFD()

-tao_term_gradient_use_fd - Use finite differences in TaoTermComputeGradient(), overriding other user-provided or built-in routines

-tao_term_hessian_use_fd - Use finite differences in TaoTermComputeHessian(), overriding other user-provided or built-in routines

TaoTerm: composable objective function terms, TaoTerm, TaoTermCreate(), TaoTermSetType(), TaoTermSetUp(), TaoTermView(), TaoTermDestroy()

src/tao/term/interface/taoterm.c

src/tao/term/tutorials/ex1.c

TaoTermSetFromOptions_L1() in src/tao/term/impls/l1/taoterml1.c TaoTermSetFromOptions_Sum() in src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSetFromOptions(TaoTerm term)
```

Example 2 (unknown):
```unknown
TaoTermType
```

Example 3 (unknown):
```unknown
TAOTERM_PARAMETERS_OPTIONAL
```

Example 4 (unknown):
```unknown
TAOTERM_PARAMETERS_NONE
```

---

## TaoTermSetParametersLayout#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSetParametersLayout/

**Contents:**
- TaoTermSetParametersLayout#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Set the layout describing the parameter vector of TaoTerm.

parameters_layout - the PetscLayout for the parameter space

The “parameter space” of a TaoTerm is the vector space of the fixed data \(p\) in \(f(x; p)\). Parameters are not optimized over. This is distinct from the “solution space” (set with TaoTermSetSolutionSizes()), which is the space of the optimization variable \(x\). Some TaoTermTypes require the solution and parameter spaces to be related (e.g., have the same size); see the documentation for each type.

Alternatively, one may use TaoTermSetParametersSizes() or TaoTermSetParametersTemplate() to define the vector sizes.

TaoTerm: composable objective function terms, TaoTerm, TaoTermGetParametersVecType(), TaoTermSetParametersVecType(), TaoTermGetParametersLayout(), TaoTermSetSolutionTemplate(), TaoTermSetParametersTemplate(), TaoTermCreateParametersVec()

src/tao/term/interface/taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSetParametersLayout(TaoTerm term, PetscLayout parameters_layout)
```

Example 2 (unknown):
```unknown
PetscLayout
```

Example 3 (unknown):
```unknown
TaoTermSetSolutionSizes()
```

Example 4 (unknown):
```unknown
TaoTermType
```

---

## TaoTermSetParametersMode#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSetParametersMode/

**Contents:**
- TaoTermSetParametersMode#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#

Sets the way a TaoTerm can accept parameters

parameters_mode - TAOTERM_PARAMETERS_OPTIONAL, TAOTERM_PARAMETERS_NONE, TAOTERM_PARAMETERS_REQUIRED

-tao_term_parameters_mode <optional,none,required> - TAOTERM_PARAMETERS_OPTIONAL, TAOTERM_PARAMETERS_NONE, TAOTERM_PARAMETERS_REQUIRED

TaoTerm: composable objective function terms, TaoTerm, TaoTermParametersMode, TaoTermGetParametersMode()

src/tao/term/interface/taoterm.c

src/tao/unconstrained/tutorials/rosenbrock1_taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSetParametersMode(TaoTerm term, TaoTermParametersMode parameters_mode)
```

Example 2 (unknown):
```unknown
TAOTERM_PARAMETERS_OPTIONAL
```

Example 3 (unknown):
```unknown
TAOTERM_PARAMETERS_NONE
```

Example 4 (unknown):
```unknown
TAOTERM_PARAMETERS_REQUIRED
```

---

## TaoTermSetParametersSizes#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSetParametersSizes/

**Contents:**
- TaoTermSetParametersSizes#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Set the sizes describing the layout of the parameter vector space of a TaoTerm.

k - the size of a parameter vector on the current MPI process (or PETSC_DECIDE)

K - the global size of a parameter vector (or PETSC_DECIDE)

bs - the block size of a parameter vector (must be >= 1)

The “parameter space” of a TaoTerm is the vector space of the fixed data \(p\) in \(f(x; p)\). Parameters are not optimized over. This is distinct from the “solution space” (set with TaoTermSetSolutionSizes()), which is the space of the optimization variable \(x\). Some TaoTermTypes require the solution and parameter spaces to be related (e.g., have the same size); see the documentation for each type.

Alternatively, one may use TaoTermSetParametersLayout() or TaoTermSetParametersTemplate() to define the vector sizes.

TaoTerm: composable objective function terms, TaoTerm, TaoTermGetParametersSizes(), TaoTermSetParametersTemplate(), TaoTermGetParametersVecType(), TaoTermSetParametersVecType(), TaoTermGetParametersLayout(), TaoTermSetParametersLayout(), TaoTermCreateParametersVec()

src/tao/term/interface/taoterm.c

src/tao/term/tutorials/ex1.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSetParametersSizes(TaoTerm term, PetscInt k, PetscInt K, PetscInt bs)
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
TaoTermSetSolutionSizes()
```

---

## TaoTermSetParametersTemplate#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSetParametersTemplate/

**Contents:**
- TaoTermSetParametersTemplate#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Set the parameter vector space to match a template vector

params_template - a vector with the desired size, layout, and VecType of parameter vectors for TaoTerm

The “parameter space” of a TaoTerm is the vector space of the fixed data \(p\) in \(f(x; p)\). Parameters are not optimized over. This is distinct from the “solution space” (set with TaoTermSetSolutionSizes()), which is the space of the optimization variable \(x\). Some TaoTermTypes require the solution and parameter spaces to be related (e.g., have the same size); see the documentation for each type.

Alternatively, one may use TaoTermSetParametersSizes() or TaoTermSetParametersLayout() to define the vector sizes.

TaoTerm: composable objective function terms, TaoTerm, TaoTermGetParametersVecType(), TaoTermSetParametersVecType(), TaoTermSetSolutionTemplate(), TaoTermGetParametersLayout(), TaoTermSetParametersLayout(), TaoTermCreateSolutionVec()

src/tao/term/interface/taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSetParametersTemplate(TaoTerm term, Vec params_template)
```

Example 2 (unknown):
```unknown
TaoTermSetSolutionSizes()
```

Example 3 (unknown):
```unknown
TaoTermType
```

Example 4 (unknown):
```unknown
TaoTermSetParametersSizes()
```

---

## TaoTermSetParametersVecType#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSetParametersVecType/

**Contents:**
- TaoTermSetParametersVecType#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- See Also#
- Level#
- Location#

Set the vector types of the parameters vector of a TaoTerm

parameters_type - the VecType for the parameters space

-tao_term_parameters_vec_type - VecType for complete list of vector types

TaoTerm: composable objective function terms, TaoTerm, TaoTermGetParametersVecType(), TaoTermSetParametersLayout(), TaoTermGetParametersLayout(), TaoTermSetParametersTemplate(), TaoTermCreateParametersVec()

src/tao/term/interface/taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSetParametersVecType(TaoTerm term, VecType parameters_type)
```

Example 2 (unknown):
```unknown
TaoTermGetParametersVecType()
```

Example 3 (unknown):
```unknown
TaoTermSetParametersLayout()
```

Example 4 (unknown):
```unknown
TaoTermGetParametersLayout()
```

---

## TaoTermSetSolutionLayout#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSetSolutionLayout/

**Contents:**
- TaoTermSetSolutionLayout#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Set the layout describing the solution vector of TaoTerm.

solution_layout - the PetscLayout for the solution space

The “solution space” of a TaoTerm is the vector space of the optimization variable \(x\) in \(f(x; p)\). This is distinct from the “parameter space” (the space of the fixed data \(p\), set with TaoTermSetParametersSizes()). Some TaoTermTypes require the solution and parameter spaces to be related (e.g., have the same size); see the documentation for each type.

When a mapping matrix \(A\) is used to add a term to a Tao via TaoAddTerm(), the mapping transforms the Tao solution vector into this term’s solution space. For example, if the Tao solution vector is \(x \in \mathbb{R}^n\) and the mapping matrix is \(A \in \mathbb{R}^{m \times n}\), then the term evaluates \(f(Ax; p)\) with \(Ax \in \mathbb{R}^m\). The term’s solution space is therefore \(\mathbb{R}^m\), and TaoTermView() will report \(N = m\) for this term.

Alternatively, one may use TaoTermSetSolutionSizes() or TaoTermSetSolutionTemplate() to define the vector sizes.

TaoTerm: composable objective function terms, TaoTerm, TaoTermGetSolutionVecType(), TaoTermSetSolutionVecType(), TaoTermGetSolutionLayout(), TaoTermSetSolutionTemplate(), TaoTermSetParametersTemplate(), TaoTermCreateSolutionVec()

src/tao/term/interface/taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSetSolutionLayout(TaoTerm term, PetscLayout solution_layout)
```

Example 2 (unknown):
```unknown
PetscLayout
```

Example 3 (unknown):
```unknown
TaoTermSetParametersSizes()
```

Example 4 (unknown):
```unknown
TaoTermType
```

---

## TaoTermSetSolutionSizes#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSetSolutionSizes/

**Contents:**
- TaoTermSetSolutionSizes#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Examples#

Set the sizes describing the layout of the solution vector space of a TaoTerm.

n - the size of a solution vector on the current MPI process (or PETSC_DECIDE)

N - the global size of a solution vector (or PETSC_DECIDE)

bs - the block size of a solution vector (must be >= 1)

The “solution space” of a TaoTerm is the vector space of the optimization variable \(x\) in \(f(x; p)\). This is distinct from the “parameter space” (the space of the fixed data \(p\), set with TaoTermSetParametersSizes()). Some TaoTermTypes require the solution and parameter spaces to be related (e.g., have the same size); see the documentation for each type.

When a mapping matrix \(A\) is used to add a term to a Tao via TaoAddTerm(), the mapping transforms the Tao solution vector into this term’s solution space. For example, if the Tao solution vector is \(x \in \mathbb{R}^n\) and the mapping matrix is \(A \in \mathbb{R}^{m \times n}\), then the term evaluates \(f(Ax; p)\) with \(Ax \in \mathbb{R}^m\). The term’s solution space is therefore \(\mathbb{R}^m\), and TaoTermView() will report \(N = m\) for this term.

Alternatively, one may use TaoTermSetSolutionLayout() or TaoTermSetSolutionTemplate() to define the vector sizes.

TaoTerm: composable objective function terms, TaoTerm, TaoTermGetSolutionSizes(), TaoTermSetSolutionTemplate(), TaoTermGetSolutionVecType(), TaoTermSetSolutionVecType(), TaoTermGetSolutionLayout(), TaoTermSetSolutionLayout(), TaoTermCreateSolutionVec()

src/tao/term/interface/taoterm.c

src/tao/term/tutorials/ex1.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSetSolutionSizes(TaoTerm term, PetscInt n, PetscInt N, PetscInt bs)
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
TaoTermSetParametersSizes()
```

---

## TaoTermSetSolutionTemplate#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSetSolutionTemplate/

**Contents:**
- TaoTermSetSolutionTemplate#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#

Set the solution vector space to match a template vector

sol_template - a vector with the desired size, layout, and VecType of solution vectors for TaoTerm

The “solution space” of a TaoTerm is the vector space of the optimization variable \(x\) in \(f(x; p)\). This is distinct from the “parameter space” (the space of the fixed data \(p\), set with TaoTermSetParametersSizes()). Some TaoTermTypes require the solution and parameter spaces to be related (e.g., have the same size); see the documentation for each type.

When a mapping matrix \(A\) is used to add a term to a Tao via TaoAddTerm(), the mapping transforms the Tao solution vector into this term’s solution space. For example, if the Tao solution vector is \(x \in \mathbb{R}^n\) and the mapping matrix is \(A \in \mathbb{R}^{m \times n}\), then the term evaluates \(f(Ax; p)\) with \(Ax \in \mathbb{R}^m\). The term’s solution space is therefore \(\mathbb{R}^m\), and TaoTermView() will report \(N = m\) for this term.

Alternatively, one may use TaoTermSetSolutionSizes() or TaoTermSetSolutionLayout() to define the vector sizes.

TaoTerm: composable objective function terms, TaoTerm, TaoTermGetSolutionVecType(), TaoTermSetSolutionVecType(), TaoTermSetParametersTemplate(), TaoTermGetSolutionLayout(), TaoTermSetSolutionLayout(), TaoTermCreateSolutionVec()

src/tao/term/interface/taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSetSolutionTemplate(TaoTerm term, Vec sol_template)
```

Example 2 (unknown):
```unknown
TaoTermSetParametersSizes()
```

Example 3 (unknown):
```unknown
TaoTermType
```

Example 4 (unknown):
```unknown
TaoAddTerm()
```

---

## TaoTermSetSolutionVecType#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSetSolutionVecType/

**Contents:**
- TaoTermSetSolutionVecType#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- See Also#
- Level#
- Location#

Set the vector types of the solution vector of a TaoTerm

solution_type - the VecType for the solution space

-tao_term_solution_vec_type - VecType for complete list of vector types

TaoTerm: composable objective function terms, TaoTerm, TaoTermGetSolutionVecType(), TaoTermSetSolutionLayout(), TaoTermGetSolutionLayout(), TaoTermSetSolutionTemplate(), TaoTermSetParametersTemplate(), TaoTermCreateSolutionVec()

src/tao/term/interface/taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSetSolutionVecType(TaoTerm term, VecType solution_type)
```

Example 2 (unknown):
```unknown
TaoTermGetSolutionVecType()
```

Example 3 (unknown):
```unknown
TaoTermSetSolutionLayout()
```

Example 4 (unknown):
```unknown
TaoTermGetSolutionLayout()
```

---

## TaoTermSetType#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSetType/

**Contents:**
- TaoTermSetType#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Notes#
- See Also#
- Level#
- Location#

Set the type of a TaoTerm

-tao_term_type - l1, halfl2squared, TaoTermType for complete list

Use TaoTermCreateShell() to define a custom term using your own function definition

New types of TaoTerm can be created with TaoTermRegister()

TaoTerm: composable objective function terms, TaoTerm, TaoTermType, TaoTermCreate(), TaoTermGetType(), TaoTermSetFromOptions(), TaoTermSetUp(), TaoTermView(), TaoTermDestroy()

src/tao/term/interface/taoterm.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSetType(TaoTerm term, TaoTermType type)
```

Example 2 (unknown):
```unknown
TaoTermType
```

Example 3 (unknown):
```unknown
TaoTermType
```

Example 4 (unknown):
```unknown
TaoTermCreateShell()
```

---

## TaoTermSetUp#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSetUp/

**Contents:**
- TaoTermSetUp#
- Synopsis#
- Input Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

TaoTerm: composable objective function terms, TaoTerm, TaoTermCreate(), TaoTermSetType(), TaoTermSetFromOptions(), TaoTermView(), TaoTermDestroy()

src/tao/term/interface/taoterm.c

src/tao/term/tutorials/ex1.c

TaoTermSetUp_Sum() in src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSetUp(TaoTerm term)
```

Example 2 (unknown):
```unknown
TaoTermCreate()
```

Example 3 (unknown):
```unknown
TaoTermSetType()
```

Example 4 (unknown):
```unknown
TaoTermSetFromOptions()
```

---

## TaoTermShellGetContext#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermShellGetContext/

**Contents:**
- TaoTermShellGetContext#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Get the context for a TAOTERMSHELL

term - a TaoTerm of type TAOTERMSHELL

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSHELL, TaoTermShellSetContext(), TaoTermShellSetContextDestroy()

src/tao/term/impls/shell/taotermshell.c

src/tao/unconstrained/tutorials/rosenbrock1_taoterm.c

TaoTermShellGetContext_Shell() in src/tao/term/impls/shell/taotermshell.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TAOTERMSHELL
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermShellGetContext(TaoTerm term, PetscCtxRt ctx)
```

Example 3 (unknown):
```unknown
TAOTERMSHELL
```

Example 4 (unknown):
```unknown
TAOTERMSHELL
```

---

## TaoTermShellSetContextDestroy#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermShellSetContextDestroy/

**Contents:**
- TaoTermShellSetContextDestroy#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set a method to destroy the context resources when a TAOTERMSHELL is destroyed

term - a TaoTerm of type TAOTERMSHELL

destroy - the context destroy function

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSHELL, TaoTermShellSetContext(), TaoTermShellGetContext()

src/tao/term/impls/shell/taotermshell.c

TaoTermShellSetContextDestroy_Shell() in src/tao/term/impls/shell/taotermshell.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TAOTERMSHELL
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermShellSetContextDestroy(TaoTerm term, PetscCtxDestroyFn *destroy)
```

Example 3 (unknown):
```unknown
TAOTERMSHELL
```

Example 4 (unknown):
```unknown
TAOTERMSHELL
```

---

## TaoTermShellSetContext#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermShellSetContext/

**Contents:**
- TaoTermShellSetContext#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Set a context for a TAOTERMSHELL

term - a TaoTerm of type TAOTERMSHELL

The context can be accessed in callbacks using TaoTermShellGetContext()

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSHELL, TaoTermShellGetContext(), TaoTermShellSetContextDestroy()

src/tao/term/impls/shell/taotermshell.c

TaoTermShellSetContext_Shell() in src/tao/term/impls/shell/taotermshell.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TAOTERMSHELL
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermShellSetContext(TaoTerm term, PetscCtx ctx)
```

Example 3 (unknown):
```unknown
TAOTERMSHELL
```

Example 4 (unknown):
```unknown
TaoTermShellGetContext()
```

---

## TaoTermShellSetCreateHessianMatrices#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermShellSetCreateHessianMatrices/

**Contents:**
- TaoTermShellSetCreateHessianMatrices#
- Synopsis#
- Input Parameters#
- Calling sequence of createmats#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Set the routine that creates Hessian matrices for a TaoTerm of type TAOTERMSHELL

term - a TaoTerm of type TAOTERMSHELL

createmats - a function with the same signature as TaoTermCreateHessianMatrices()

H - (optional) a matrix of the appropriate type and size for the Hessian of term

Hpre - (optional) a matrix of the appropriate type and size for constructing a preconditioner for the Hessian of term

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSHELL, TaoTermShellGetContext(), TaoTermShellSetContextDestroy(), TaoTermShellSetCreateSolutionVec(), TaoTermShellSetCreateParametersVec()

src/tao/term/impls/shell/taotermshell.c

src/tao/unconstrained/tutorials/rosenbrock1_taoterm.c

TaoTermShellSetCreateHessianMatrices_Shell(TaoTerm term, PetscErrorCode (*createhessianmatrices)() in src/tao/term/impls/shell/taotermshell.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TAOTERMSHELL
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermShellSetCreateHessianMatrices(TaoTerm term, PetscErrorCode (*createmats)(TaoTerm f, Mat *H, Mat *Hpre))
```

Example 3 (unknown):
```unknown
TAOTERMSHELL
```

Example 4 (unknown):
```unknown
TaoTermCreateHessianMatrices()
```

---

## TaoTermShellSetCreateParametersVec#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermShellSetCreateParametersVec/

**Contents:**
- TaoTermShellSetCreateParametersVec#
- Synopsis#
- Input Parameters#
- Calling sequence of createparametersvec#
- See Also#
- Level#
- Location#
- Implementations#

Set the routine that creates parameters vector for a TaoTerm of type TAOTERMSHELL

term - a TaoTerm of type TAOTERMSHELL

createparametersvec - a function with the same signature as TaoTermCreateParametersVec()

parameters - a parameters vector for term

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSHELL, TaoTermShellGetContext(), TaoTermShellSetContextDestroy(), TaoTermShellSetCreateHessianMatrices()

src/tao/term/impls/shell/taotermshell.c

TaoTermShellSetCreateParametersVec_Shell(TaoTerm term, PetscErrorCode (*createparametersvec)() in src/tao/term/impls/shell/taotermshell.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TAOTERMSHELL
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermShellSetCreateParametersVec(TaoTerm term, PetscErrorCode (*createparametersvec)(TaoTerm term, Vec *parameters))
```

Example 3 (unknown):
```unknown
TAOTERMSHELL
```

Example 4 (unknown):
```unknown
TaoTermCreateParametersVec()
```

---

## TaoTermShellSetCreateSolutionVec#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermShellSetCreateSolutionVec/

**Contents:**
- TaoTermShellSetCreateSolutionVec#
- Synopsis#
- Input Parameters#
- Calling sequence of createsolutionvec#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Set the routine that creates solution vector for a TaoTerm of type TAOTERMSHELL

term - a TaoTerm of type TAOTERMSHELL

createsolutionvec - a function with the same signature as TaoTermCreateSolutionVec()

solution - a solution vector for term

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSHELL, TaoTermShellGetContext(), TaoTermShellSetContextDestroy(), TaoTermShellSetCreateHessianMatrices()

src/tao/term/impls/shell/taotermshell.c

src/tao/unconstrained/tutorials/rosenbrock1_taoterm.c

TaoTermShellSetCreateSolutionVec_Shell(TaoTerm term, PetscErrorCode (*createsolutionvec)() in src/tao/term/impls/shell/taotermshell.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TAOTERMSHELL
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermShellSetCreateSolutionVec(TaoTerm term, PetscErrorCode (*createsolutionvec)(TaoTerm term, Vec *solution))
```

Example 3 (unknown):
```unknown
TAOTERMSHELL
```

Example 4 (unknown):
```unknown
TaoTermCreateSolutionVec()
```

---

## TaoTermShellSetGradient#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermShellSetGradient/

**Contents:**
- TaoTermShellSetGradient#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set the gradient function of a TAOTERMSHELL

term - a TaoTerm of type TAOTERMSHELL

gradient - a TaoTermGradientFn function pointer

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSHELL, TaoTermShellGetContext(), TaoTermShellSetContextDestroy(), TaoTermShellSetObjective(), TaoTermShellSetObjectiveAndGradient(), TaoTermShellSetHessian(), TaoTermShellSetView(), TaoTermGradientFn

src/tao/term/impls/shell/taotermshell.c

TaoTermShellSetGradient_Shell() in src/tao/term/impls/shell/taotermshell.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TAOTERMSHELL
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermShellSetGradient(TaoTerm term, TaoTermGradientFn *gradient)
```

Example 3 (unknown):
```unknown
TAOTERMSHELL
```

Example 4 (unknown):
```unknown
TaoTermGradientFn
```

---

## TaoTermShellSetHessian#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermShellSetHessian/

**Contents:**
- TaoTermShellSetHessian#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Set the Hessian function of a TAOTERMSHELL

term - a TaoTerm of type TAOTERMSHELL

hessian - a TaoTermHessianFn function pointer

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSHELL, TaoTermShellGetContext(), TaoTermShellSetContextDestroy(), TaoTermShellSetObjective(), TaoTermShellSetGradient(), TaoTermShellSetObjectiveAndGradient(), TaoTermShellSetView(), TaoTermHessianFn

src/tao/term/impls/shell/taotermshell.c

src/tao/unconstrained/tutorials/rosenbrock1_taoterm.c

TaoTermShellSetHessian_Shell() in src/tao/term/impls/shell/taotermshell.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TAOTERMSHELL
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermShellSetHessian(TaoTerm term, TaoTermHessianFn *hessian)
```

Example 3 (unknown):
```unknown
TAOTERMSHELL
```

Example 4 (unknown):
```unknown
TaoTermHessianFn
```

---

## TaoTermShellSetIsComputeHessianFDPossible#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermShellSetIsComputeHessianFDPossible/

**Contents:**
- TaoTermShellSetIsComputeHessianFDPossible#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set whether this term can compute Hessian with finite differences for a TAOTERMSHELL

term - a TaoTerm of type TAOTERMSHELL

ispossible - whether Hessian computation with finite differences is possible

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSHELL, TaoTermShellGetContext(), TaoTermShellSetContextDestroy(), TaoTermShellSetObjective(), TaoTermShellSetGradient(), TaoTermShellSetObjectiveAndGradient(), TaoTermShellSetHessian(), TaoTermIsComputeHessianFDPossible()

src/tao/term/impls/shell/taotermshell.c

TaoTermShellSetIsComputeHessianFDPossible_Shell() in src/tao/term/impls/shell/taotermshell.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TAOTERMSHELL
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermShellSetIsComputeHessianFDPossible(TaoTerm term, PetscBool3 ispossible)
```

Example 3 (unknown):
```unknown
TAOTERMSHELL
```

Example 4 (unknown):
```unknown
TAOTERMSHELL
```

---

## TaoTermShellSetObjectiveAndGradient#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermShellSetObjectiveAndGradient/

**Contents:**
- TaoTermShellSetObjectiveAndGradient#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Set the objective and gradient function of a TAOTERMSHELL

term - a TaoTerm of type TAOTERMSHELL

objandgrad - a TaoTermObjectiveAndGradientFn function pointer

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSHELL, TaoTermShellGetContext(), TaoTermShellSetContextDestroy(), TaoTermShellSetObjective(), TaoTermShellSetGradient(), TaoTermShellSetHessian(), TaoTermShellSetView(), TaoTermObjectiveAndGradientFn

src/tao/term/impls/shell/taotermshell.c

src/tao/unconstrained/tutorials/rosenbrock1_taoterm.c

TaoTermShellSetObjectiveAndGradient_Shell() in src/tao/term/impls/shell/taotermshell.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TAOTERMSHELL
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermShellSetObjectiveAndGradient(TaoTerm term, TaoTermObjectiveAndGradientFn *objandgrad)
```

Example 3 (unknown):
```unknown
TAOTERMSHELL
```

Example 4 (unknown):
```unknown
TaoTermObjectiveAndGradientFn
```

---

## TaoTermShellSetObjective#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermShellSetObjective/

**Contents:**
- TaoTermShellSetObjective#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set the objective function of a TAOTERMSHELL

term - a TaoTerm of type TAOTERMSHELL

objective - a TaoTermObjectiveFn function pointer

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSHELL, TaoTermShellGetContext(), TaoTermShellSetContextDestroy(), TaoTermShellSetGradient(), TaoTermShellSetObjectiveAndGradient(), TaoTermShellSetHessian(), TaoTermShellSetView(), TaoTermObjectiveFn

src/tao/term/impls/shell/taotermshell.c

TaoTermShellSetObjective_Shell() in src/tao/term/impls/shell/taotermshell.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TAOTERMSHELL
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermShellSetObjective(TaoTerm term, TaoTermObjectiveFn *objective)
```

Example 3 (unknown):
```unknown
TAOTERMSHELL
```

Example 4 (unknown):
```unknown
TaoTermObjectiveFn
```

---

## TaoTermShellSetView#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermShellSetView/

**Contents:**
- TaoTermShellSetView#
- Synopsis#
- Input Parameters#
- Calling sequence of view#
- See Also#
- Level#
- Location#
- Implementations#

Set the view function of a TAOTERMSHELL

term - a TaoTerm of type TAOTERMSHELL

view - a function with the same signature as TaoTermView()

viewer - a PetscViewer

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSHELL, TaoTermShellGetContext(), TaoTermShellSetContextDestroy(), TaoTermShellSetObjective(), TaoTermShellSetGradient(), TaoTermShellSetObjectiveAndGradient(), TaoTermShellSetHessian()

src/tao/term/impls/shell/taotermshell.c

TaoTermShellSetView_Shell(TaoTerm term, PetscErrorCode (*view)() in src/tao/term/impls/shell/taotermshell.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TAOTERMSHELL
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermShellSetView(TaoTerm term, PetscErrorCode (*view)(TaoTerm term, PetscViewer viewer))
```

Example 3 (unknown):
```unknown
TAOTERMSHELL
```

Example 4 (unknown):
```unknown
TaoTermView()
```

---

## TAOTERMSHELL#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TAOTERMSHELL/

**Contents:**
- TAOTERMSHELL#
- See Also#
- Level#
- Location#

A TaoTerm that uses user-provided function callbacks for its operations

TaoTerm: composable objective function terms, TaoTerm, TaoTermShellGetContext(), TaoTermShellSetContextDestroy(), TaoTermCreateShell(), TaoTermShellSetObjective(), TaoTermShellSetGradient(), TaoTermShellSetObjectiveAndGradient(), TaoTermShellSetHessian()

src/tao/term/impls/shell/taotermshell.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermShellGetContext()
```

Example 2 (unknown):
```unknown
TaoTermShellSetContextDestroy()
```

Example 3 (unknown):
```unknown
TaoTermCreateShell()
```

Example 4 (unknown):
```unknown
TaoTermShellSetObjective()
```

---

## TaoTermSumAddTerm#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSumAddTerm/

**Contents:**
- TaoTermSumAddTerm#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Append a term to the terms being summed

sumterm - a TaoTerm of type TAOTERMSUM

prefix - (optional) the prefix used for configuring the term (if NULL, the index of the term will be used as a prefix, e.g. term_0_, term_1_, etc.)

scale - the coefficient scaling the term in the sum

term - the TaoTerm to add

map - (optional) a map from the TAOTERMSUM solution space to the term solution space; if NULL the map is assumed to be the identity

index - (optional) the index of the newly added term

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSUM

src/tao/term/impls/sum/taotermsum.c

TaoTermSumAddTerm_Sum() in src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSumAddTerm(TaoTerm sumterm, const char prefix[], PetscReal scale, TaoTerm term, Mat map, PetscInt *index)
```

---

## TaoTermSumGetLastTermObjectives#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSumGetLastTermObjectives/

**Contents:**
- TaoTermSumGetLastTermObjectives#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get the contributions from each term to the last evaluation of TaoTermComputeObjective() or TaoTermComputeObjectiveAndGradient()

term - a TaoTerm of type TAOTERMSUM

values - an array of the contributions to the last computed objective value

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSUM

src/tao/term/impls/sum/taotermsum.c

TaoTermSumGetLastTermObjectives_Sum() in src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermComputeObjective()
```

Example 2 (unknown):
```unknown
TaoTermComputeObjectiveAndGradient()
```

Example 3 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSumGetLastTermObjectives(TaoTerm term, const PetscReal *values[])
```

---

## TaoTermSumGetNumberTerms#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSumGetNumberTerms/

**Contents:**
- TaoTermSumGetNumberTerms#
- Synopsis#
- Input Parameter#
- Output Parameter#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Get the number of terms in the sum

term - a TaoTerm of type TAOTERMSUM

n_terms - the number of terms that will be in the sum

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSUM, TaoTermSumSetNumberTerms()

src/tao/term/impls/sum/taotermsum.c

src/tao/unconstrained/tutorials/elastic_net_regularization.c

TaoTermSumGetNumberTerms_Sum() in src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSumGetNumberTerms(TaoTerm term, PetscInt *n_terms)
```

Example 2 (unknown):
```unknown
TaoTermSumSetNumberTerms()
```

---

## TaoTermSumGetTermHessianMatrices#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSumGetTermHessianMatrices/

**Contents:**
- TaoTermSumGetTermHessianMatrices#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Get Hessian matrices set with TaoTermSumSetTermHessianMatrices().

term - a TaoTerm of type TAOTERMSUM

index - the index for the term from TaoTermSumSetTerm() or TaoTermSumAddTerm()

unmapped_H - (optional) unmapped Hessian matrix

unmapped_Hpre - (optional) unmapped matrix for constructing the preconditioner for unmapped_H

mapped_H - (optional) Hessian matrix

mapped_Hpre - (optional) matrix for constructing the preconditioner for mapped_H

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSUM, TaoTermComputeHessian(), TaoTermSumSetTermHessianMatrices()

src/tao/term/impls/sum/taotermsum.c

TaoTermSumGetTermHessianMatrices_Sum() in src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermSumSetTermHessianMatrices()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSumGetTermHessianMatrices(TaoTerm term, PetscInt index, Mat *unmapped_H, Mat *unmapped_Hpre, Mat *mapped_H, Mat *mapped_Hpre)
```

Example 3 (unknown):
```unknown
TaoTermSumSetTerm()
```

Example 4 (unknown):
```unknown
TaoTermSumAddTerm()
```

---

## TaoTermSumGetTermMask#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSumGetTermMask/

**Contents:**
- TaoTermSumGetTermMask#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#
- Implementations#

Get the TaoTermMask of a term in the sum

term - a TaoTerm of type TAOTERMSUM

index - the index for the term from TaoTermSumSetTerm() or TaoTermSumAddTerm()

mask - a bitmask of TaoTermMask evaluation methods to mask (e.g. just TAOTERM_MASK_OBJECTIVE or a bitwise-or like TAOTERM_MASK_OBJECTIVE | TAOTERM_MASK_GRADIENT)

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSUM, TaoTermSumSetTermMask()

src/tao/term/impls/sum/taotermsum.c

TaoTermSumGetTermMask_Sum() in src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermMask
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSumGetTermMask(TaoTerm term, PetscInt index, TaoTermMask *mask)
```

Example 3 (unknown):
```unknown
TaoTermSumSetTerm()
```

Example 4 (unknown):
```unknown
TaoTermSumAddTerm()
```

---

## TaoTermSumGetTerm#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSumGetTerm/

**Contents:**
- TaoTermSumGetTerm#
- Synopsis#
- Input Parameters#
- Output Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Get the data for a term in a TAOTERMSUM

sumterm - a TaoTerm of type TAOTERMSUM

index - a number \(0 \leq i < n\), where \(n\) is the number of terms in TaoTermSumGetNumberTerms()

prefix - (optional) the prefix used for configuring the term

scale - (optional) the coefficient scaling the term in the sum

term - the TaoTerm at given index of TAOTERMSUM

map - (optional) a map from the TAOTERMSUM solution space to the term solution space; if NULL the map is assumed to be the identity

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSUM, TaoTermSumSetTerm(), TaoTermSumAddTerm()

src/tao/term/impls/sum/taotermsum.c

src/tao/unconstrained/tutorials/elastic_net_regularization.c

TaoTermSumGetTerm_Sum() in src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSumGetTerm(TaoTerm sumterm, PetscInt index, const char **prefix, PetscReal *scale, TaoTerm *term, Mat *map)
```

Example 2 (unknown):
```unknown
TaoTermSumGetNumberTerms()
```

Example 3 (unknown):
```unknown
TaoTermSumSetTerm()
```

Example 4 (unknown):
```unknown
TaoTermSumAddTerm()
```

---

## TaoTermSumParametersPack#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSumParametersPack/

**Contents:**
- TaoTermSumParametersPack#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#

Concatenate the parameters for terms into a VECNEST parameter vector for a TAOTERMSUM

term - a TaoTerm of type TAOTERMSUM

p_arr - an array of parameters Vecs, one for each term in the sum. An entry can be NULL for a term that doesn’t take parameters.

params - a Vec of type VECNEST that concatenates all of the parameters

This is a wrapper around VecCreateNest(), but that function does not allow NULL for any of the Vecs in the array. A 0-length vector will be created for each NULL Vec that will be internally ignored by TAOTERMSUM.

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSUM, TaoTermSumParametersUnpack(), VECNEST, VecNestGetTaoTermSumParameters(), VecCreateNest()

src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSumParametersPack(TaoTerm term, Vec p_arr[], Vec *params)
```

Example 2 (unknown):
```unknown
VecCreateNest()
```

Example 3 (unknown):
```unknown
TaoTermSumParametersUnpack()
```

Example 4 (unknown):
```unknown
VecNestGetTaoTermSumParameters()
```

---

## TaoTermSumParametersUnpack#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSumParametersUnpack/

**Contents:**
- TaoTermSumParametersUnpack#
- Synopsis#
- Input Parameters#
- Output Parameter#
- See Also#
- Level#
- Location#

Unpack the concatenated parameters created by TaoTermSumParametersPack() and destroy the VECNEST

term - a TaoTerm of type TAOTERMSUM

params - a Vec created by TaoTermSumParametersPack()

p_arr - an array of parameters Vecs, one for each term in the sum. An entry will be NULL if NULL was passed in the same position of TaoTermSumParametersPack()

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSUM, TaoTermSumParametersPack(), VecNestGetTaoTermSumParameters()

src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermSumParametersPack()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSumParametersUnpack(TaoTerm term, Vec *params, Vec p_arr[])
```

Example 3 (unknown):
```unknown
TaoTermSumParametersPack()
```

Example 4 (unknown):
```unknown
TaoTermSumParametersPack()
```

---

## TaoTermSumSetNumberTerms#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSumSetNumberTerms/

**Contents:**
- TaoTermSumSetNumberTerms#
- Synopsis#
- Input Parameters#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Set the number of terms in the sum

term - a TaoTerm of type TAOTERMSUM

n_terms - the number of terms that will be in the sum

If n_terms is smaller than the current number of terms, the trailing terms will be dropped.

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSUM, TaoTermSumGetNumberTerms()

src/tao/term/impls/sum/taotermsum.c

TaoTermSumSetNumberTerms_Sum() in src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSumSetNumberTerms(TaoTerm term, PetscInt n_terms)
```

Example 2 (unknown):
```unknown
TaoTermSumGetNumberTerms()
```

---

## TaoTermSumSetTermHessianMatrices#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSumSetTermHessianMatrices/

**Contents:**
- TaoTermSumSetTermHessianMatrices#
- Synopsis#
- Input Parameters#
- Notes#
- See Also#
- Level#
- Location#
- Implementations#

Set Hessian matrices that can be used internally by a TAOTERMSUM

term - a TaoTerm of type TAOTERMSUM

index - the index for the term from TaoTermSumSetTerm() or TaoTermSumAddTerm()

unmapped_H - (optional) unmapped Hessian matrix

unmapped_Hpre - (optional) unmapped matrix for constructing the preconditioner of unmapped_H

mapped_H - (optional) Hessian matrix

mapped_Hpre - (optional) matrix for constructing the preconditioner of mapped_H

If the inner term has the form \(g(x) = \alpha f(Ax; p)\), the “mapped” Hessians should be able to hold the Hessian \(\nabla^2 g\) and the unmapped Hessians should be able to hold the Hessian \(\nabla_x^2 f\). If the term is not mapped, just pass the unmapped Hessians (e.g. TaoTermSumSetTermHessianMatrices(term, 0, H, Hpre, NULL, NULL)).

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSUM, TaoTermComputeHessian(), TaoTermSumGetTermHessianMatrices()

src/tao/term/impls/sum/taotermsum.c

TaoTermSumSetTermHessianMatrices_Sum() in src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSumSetTermHessianMatrices(TaoTerm term, PetscInt index, Mat unmapped_H, Mat unmapped_Hpre, Mat mapped_H, Mat mapped_Hpre)
```

Example 2 (unknown):
```unknown
TaoTermSumSetTerm()
```

Example 3 (unknown):
```unknown
TaoTermSumAddTerm()
```

Example 4 (unknown):
```unknown
TaoTermSumSetTermHessianMatrices(term, 0, H, Hpre, NULL, NULL)
```

---

## TaoTermSumSetTermMask#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSumSetTermMask/

**Contents:**
- TaoTermSumSetTermMask#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#
- Implementations#

Set a TaoTermMask on a term in the sum

term - a TaoTerm of type TAOTERMSUM

index - the index for the term from TaoTermSumSetTerm() or TaoTermSumAddTerm()

mask - a bitmask of TaoTermMask evaluation methods to mask (e.g. just TAOTERM_MASK_OBJECTIVE or a bitwise-or like TAOTERM_MASK_OBJECTIVE | TAOTERM_MASK_GRADIENT)

-tao_term_sum_<prefix_>mask - a list containing any of none, objective, gradient, and hessian to indicate which evaluations to mask for a term with a given prefix (see TaoTermSumSetTerm())

Some optimization methods may add a damping term to the Hessian of an objective function without affecting the objective or gradient. If, e.g., the regularizer has index 1, then this can be accomplished with TaoTermSumSetTermMask(term, 1, TAOTERM_MASK_OBJECTIVE | TAOTERM_MASK_GRADIENT).

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSUM, TaoTermSumGetTermMask()

src/tao/term/impls/sum/taotermsum.c

TaoTermSumSetTermMask_Sum() in src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermMask
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSumSetTermMask(TaoTerm term, PetscInt index, TaoTermMask mask)
```

Example 3 (unknown):
```unknown
TaoTermSumSetTerm()
```

Example 4 (unknown):
```unknown
TaoTermSumAddTerm()
```

---

## TaoTermSumSetTerm#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermSumSetTerm/

**Contents:**
- TaoTermSumSetTerm#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Implementations#

Set a term in a sum of terms

sumterm - a TaoTerm of type TAOTERMSUM

index - a number \(0 \leq i < n\), where \(n\) is the number of terms in TaoTermSumSetNumberTerms()

prefix - (optional) the prefix used for configuring the term (if NULL, term_x_ will be the prefix, e.g. “term_0_”, “term_1_”, etc.)

scale - the coefficient scaling the term in the sum

term - the TaoTerm to be set in TAOTERMSUM

map - (optional) a map from the TAOTERMSUM solution space to the term solution space; if NULL the map is assumed to be the identity

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSUM, TaoTermSumGetTerm(), TaoTermSumAddTerm()

src/tao/term/impls/sum/taotermsum.c

TaoTermSumSetTerm_Sum() in src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermSumSetTerm(TaoTerm sumterm, PetscInt index, const char prefix[], PetscReal scale, TaoTerm term, Mat map)
```

Example 2 (unknown):
```unknown
TaoTermSumSetNumberTerms()
```

Example 3 (unknown):
```unknown
TaoTermSumGetTerm()
```

Example 4 (unknown):
```unknown
TaoTermSumAddTerm()
```

---

## TAOTERMSUM#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TAOTERMSUM/

**Contents:**
- TAOTERMSUM#
- Note#
- See Also#
- Level#
- Location#

A TaoTerm that is a sum of multiple TaoTerms.

The default Hessian creation mode (see TaoTermGetCreateHessianMode()) is H == Hpre and TaoTermCreateHessianMatrices() will create a MATAIJ.

TaoTerm: composable objective function terms, TaoTerm, TaoTermType, TaoTermSumGetNumberTerms(), TaoTermSumSetNumberTerms(), TaoTermSumGetTerm(), TaoTermSumSetTerm(), TaoTermSumAddTerm(), TaoTermSumGetTermHessianMatrices(), TaoTermSumSetTermHessianMatrices(), TaoTermSumGetTermMask(), TaoTermSumSetTermMask()

src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoTermGetCreateHessianMode()
```

Example 2 (unknown):
```unknown
TaoTermCreateHessianMatrices()
```

Example 3 (unknown):
```unknown
TaoTermType
```

Example 4 (unknown):
```unknown
TaoTermSumGetNumberTerms()
```

---

## TaoTermType#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermType/

**Contents:**
- TaoTermType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#
- Examples#

String with the name of a TaoTerm method

TAOTERMSHELL - uses user-provided callback functions, see TaoTermCreateShell()

TAOTERMSUM - a sum of multiple other TaoTerms

TAOTERMHALFL2SQUARED - \(\tfrac{1}{2}\|x - p\|_2^2\)

TAOTERML1 - \(\|x - p\|_1\)

TAOTERMQUADRATIC - a quadratic form \(\tfrac{1}{2}(x - p)^T A (x - p)\)

TAOTERMCALLBACKS - uses the callback functions set in TaoSetObjective(), TaoSetGradient(), etc.

TAO: Optimization Solvers, TaoTerm: composable objective function terms, TaoTerm, TaoTermCreate(), TaoTermSetType(), TaoTermCreateShell()

include/petsctaoterm.h

src/tao/term/tutorials/ex1.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef const char *TaoTermType;
#define TAOTERMCALLBACKS     "callbacks"
#define TAOTERMSHELL         "shell"
#define TAOTERMSUM           "sum"
#define TAOTERMHALFL2SQUARED "halfl2squared"
#define TAOTERML1            "l1"
#define TAOTERMQUADRATIC     "quadratic"
```

Example 2 (unknown):
```unknown
TAOTERMSHELL
```

Example 3 (unknown):
```unknown
TaoTermCreateShell()
```

Example 4 (unknown):
```unknown
TAOTERMHALFL2SQUARED
```

---

## TaoTermView#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTermView/

**Contents:**
- TaoTermView#
- Synopsis#
- Input Parameters#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

View a description of a TaoTerm.

viewer - a PetscViewer

TaoTerm: composable objective function terms, TaoTerm, TaoTermCreate(), TaoTermSetType(), TaoTermSetFromOptions(), TaoTermSetUp(), TaoTermDestroy(), PetscViewer

src/tao/term/interface/taoterm.c

src/tao/term/tutorials/ex1.c

TaoTermView_Callbacks() in src/tao/term/impls/callbacks/taotermcallbacks.c TaoTermView_L1() in src/tao/term/impls/l1/taoterml1.c TaoTermView_Quadratic() in src/tao/term/impls/quadratic/taotermquadratic.c TaoTermView_Shell() in src/tao/term/impls/shell/taotermshell.c TaoTermView_Test() in src/tao/term/impls/shell/tests/ex1.c TaoTermView_Sum() in src/tao/term/impls/sum/taotermsum.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTermView(TaoTerm term, PetscViewer viewer)
```

Example 2 (unknown):
```unknown
PetscViewer
```

Example 3 (unknown):
```unknown
TaoTermCreate()
```

Example 4 (unknown):
```unknown
TaoTermSetType()
```

---

## TaoTerm#

**URL:** https://petsc.org/release/manualpages/TaoTerm/TaoTerm/

**Contents:**
- TaoTerm#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Abstract PETSc object that manages individual terms whose sum forms the objective function of optimization solvers.

User can combine a user-defined TaoTerm using TaoTermCreateShell() and built-in TaoTerm to define the objective function.

TAO: Optimization Solvers, TaoTerm: composable objective function terms, TaoTermCreate(), TaoTermSetType(), TaoTermSetFromOptions(), TaoTermView(), TaoTermComputeObjective(), TaoTermComputeGradient(), TaoTermComputeObjectiveAndGradient(), TaoTermComputeHessian(), TaoTermDestroy(), TaoTermCreateShell(), Tao, TaoAddTerm()

include/petsctaoterm.h

src/tao/unconstrained/tutorials/rosenbrock1_taoterm.c src/tao/term/tutorials/ex1.c src/tao/unconstrained/tutorials/elastic_net_regularization.c

_p_TaoTerm in include/petsc/private/taoimpl.h

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_TaoTerm *TaoTerm;
```

Example 2 (unknown):
```unknown
TaoTermCreateShell()
```

Example 3 (unknown):
```unknown
TaoTermCreate()
```

Example 4 (unknown):
```unknown
TaoTermSetType()
```

---

## TaoTestGradient#

**URL:** https://petsc.org/release/manualpages/Tao/TaoTestGradient/

**Contents:**
- TaoTestGradient#
- Synopsis#
- Input Parameters#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#

Compare the user-supplied gradient with a finite-difference approximation, when requested via the options database, and print the difference.

tao - the Tao context

x - the point at which to evaluate the gradient

g1 - the user-supplied gradient at x

-tao_test_gradient - enable the comparison

-tao_test_gradient_view - display the user-supplied gradient, the finite-difference gradient, and their difference

If -tao_test_gradient is not set, this routine returns immediately without performing any work.

TAO: Optimization Solvers, Tao, TaoTestHessian(), TaoComputeGradient()

src/tao/interface/taosolver_fg.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTestGradient(Tao tao, Vec x, Vec g1)
```

Example 2 (unknown):
```unknown
-tao_test_gradient
```

Example 3 (unknown):
```unknown
TaoTestHessian()
```

Example 4 (unknown):
```unknown
TaoComputeGradient()
```

---

## TaoTestHessian#

**URL:** https://petsc.org/release/manualpages/Tao/TaoTestHessian/

**Contents:**
- TaoTestHessian#
- Synopsis#
- Input Parameter#
- Options Database Keys#
- Note#
- See Also#
- Level#
- Location#

Compare the user-supplied Hessian with a finite-difference approximation, when requested via the options database, and print the difference.

tao - the Tao context

-tao_test_hessian threshold - enable the comparison, optionally overriding the reporting threshold (default 1e-5)

-tao_test_hessian_view - display the user-supplied Hessian, the finite-difference Hessian, and their difference

If -tao_test_hessian is not set, this routine returns immediately without performing any work.

TAO: Optimization Solvers, Tao, TaoTestGradient(), TaoComputeHessian()

src/tao/interface/taosolver_hj.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoTestHessian(Tao tao)
```

Example 2 (unknown):
```unknown
-tao_test_hessian
```

Example 3 (unknown):
```unknown
TaoTestGradient()
```

Example 4 (unknown):
```unknown
TaoComputeHessian()
```

---

## TAOTRON#

**URL:** https://petsc.org/release/manualpages/Tao/TAOTRON/

**Contents:**
- TAOTRON#
- Options Database Keys#
- See Also#
- Level#
- Location#
- Examples#

The TRON algorithm is an active-set Newton trust region method for bound-constrained minimization.

-tao_tron_maxgpits - maximum number of gradient projections per TRON iterate

-tao_subset_type - “subvec”,”mask”,”matrix-free”, strategies for handling active-sets

Tao, TAONTR, TAONTL, TAONM, TAOCG, TaoType, TaoCreate()

src/tao/bound/impls/tron/tron.c

src/tao/bound/tutorials/jbearing2.c src/tao/bound/tutorials/plate2.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoCreate()
```

---

## TaoType#

**URL:** https://petsc.org/release/manualpages/Tao/TaoType/

**Contents:**
- TaoType#
- Synopsis#
- Values#
- See Also#
- Level#
- Location#

String with the name of a Tao method

TAONLS - nls Newton’s method with line search for unconstrained minimization

TAONTR - ntr Newton’s method with trust region for unconstrained minimization

TAONTL - ntl Newton’s method with trust region, line search for unconstrained minimization

TAOLMVM - lmvm Limited memory variable metric method for unconstrained minimization

TAOCG - cg Nonlinear conjugate gradient method for unconstrained minimization

TAONM - nm Nelder-Mead algorithm for derivate-free unconstrained minimization

TAOTRON - tron Newton Trust Region method for bound constrained minimization

TAOGPCG - gpcg Newton Trust Region method for quadratic bound constrained minimization

TAOBLMVM - blmvm Limited memory variable metric method for bound constrained minimization

TAOLCL - lcl Linearly constrained Lagrangian method for pde-constrained minimization

TAOPOUNDERS - Pounders Model-based algorithm for nonlinear least squares

Summary of Tao Solvers, TAO: Optimization Solvers, Tao, TaoCreate(), TaoSetType()

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
typedef const char *TaoType;
#define TAOLMVM     "lmvm"
#define TAONLS      "nls"
#define TAONTR      "ntr"
#define TAONTL      "ntl"
#define TAOCG       "cg"
#define TAOTRON     "tron"
#define TAOOWLQN    "owlqn"
#define TAOBMRM     "bmrm"
#define TAOBLMVM    "blmvm"
#define TAOBQNLS    "bqnls"
#define TAOBNCG     "bncg"
#define TAOBNLS     "bnls"
#define TAOBNTR     "bntr"
#define TAOBNTL     "bntl"
#define TAOBNK      "bnk"
#define TAOBQNKLS   "bqnkls"
#define TAOBQNKTR   "bqnktr"
#define TAOBQNKTL   "bqnktl"
#define TAOBQPIP    "bqpip"
#define TAOGPCG     "gpcg"
#define TAONM       "nm"
#define TAOPOUNDERS "pounders"
#define TAOBRGN     "brgn"
#define TAOLCL      "lcl"
#define TAOSSILS    "ssils"
#define TAOSSFLS    "ssfls"
#define TAOASILS    "asils"
#define TAOASFLS    "asfls"
#define TAOIPM      "ipm"
#define TAOPDIPM    "pdipm"
#define TAOSHELL    "shell"
#define TAOADMM     "admm"
#define TAOALMM     "almm"
#define TAOPYTHON   "python"
#define TAOSNES     "snes"
```

Example 2 (unknown):
```unknown
TAOPOUNDERS
```

Example 3 (unknown):
```unknown
TaoCreate()
```

Example 4 (unknown):
```unknown
TaoSetType()
```

---

## TaoVecGetSubVec#

**URL:** https://petsc.org/release/manualpages/Tao/TaoVecGetSubVec/

**Contents:**
- TaoVecGetSubVec#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Gets a subvector using the IS

vfull - the full matrix

is - the index set for the subvector

reduced_type - the method Tao is using for subsetting

maskvalue - the value to set the unused vector elements to (for TAO_SUBSET_MASK or TAO_SUBSET_MATRIXFREE)

vreduced - the subvector

maskvalue should usually be 0.0, unless a pointwise divide will be used.

TaoMatGetSubMat(), TaoSubsetType

src/tao/bound/utils/isutil.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoVecGetSubVec(Vec vfull, IS is, TaoSubsetType reduced_type, PetscReal maskvalue, Vec *vreduced)
```

Example 2 (unknown):
```unknown
TAO_SUBSET_MASK
```

Example 3 (unknown):
```unknown
TAO_SUBSET_MATRIXFREE
```

Example 4 (unknown):
```unknown
TaoMatGetSubMat()
```

---

## TaoViewFromOptions#

**URL:** https://petsc.org/release/manualpages/Tao/TaoViewFromOptions/

**Contents:**
- TaoViewFromOptions#
- Synopsis#
- Input Parameters#
- Options Database Key#
- See Also#
- Level#
- Location#

View a Tao object based on values in the options database

obj - Optional object that provides the prefix for the options database

name - command line option

-name [viewertype][:…] - option name and values. See PetscObjectViewFromOptions() for the possible arguments

TAO: Optimization Solvers, Tao, TaoView, PetscObjectViewFromOptions(), TaoCreate()

src/tao/interface/taosolver.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoViewFromOptions(Tao A, PetscObject obj, const char name[])
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
TaoCreate()
```

---

## TaoView#

**URL:** https://petsc.org/release/manualpages/Tao/TaoView/

**Contents:**
- TaoView#
- Synopsis#
- Input Parameters#
- Options Database Key#
- Notes#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Prints information about the Tao object

tao - the Tao context

viewer - visualization context

-tao_view - Calls TaoView() at the end of TaoSolve()

The available visualization contexts include

PETSC_VIEWER_STDOUT_SELF - standard output (default)

PETSC_VIEWER_STDOUT_WORLD - synchronized standard output where only the first processor opens the file. All other processors send their data to the first processor to print.

To view all the TaoTerm inside of Tao, use PETSC_VIEWER_ASCII_INFO_DETAIL, or pass -tao_view ::ascii_info_detail flag

TAO: Optimization Solvers, Tao, PetscViewerASCIIOpen()

src/tao/interface/taosolver.c

src/tao/unconstrained/tutorials/minsurf2.c src/tao/unconstrained/tutorials/rosenbrock1f.F90 src/tao/bound/tutorials/plate2.c

TaoView_BLMVM() in src/tao/bound/impls/blmvm/blmvm.c TaoView_BNCG() in src/tao/bound/impls/bncg/bncg.c TaoView_BNK() in src/tao/bound/impls/bnk/bnk.c TaoView_BQNK() in src/tao/bound/impls/bqnk/bqnk.c TaoView_TRON() in src/tao/bound/impls/tron/tron.c TaoView_SSLS() in src/tao/complementarity/impls/ssls/ssls.c TaoView_ADMM() in src/tao/constrained/impls/admm/admm.c TaoView_ALMM() in src/tao/constrained/impls/almm/almm.c TaoView_IPM() in src/tao/constrained/impls/ipm/ipm.c TaoView_PDIPM() in src/tao/constrained/impls/ipm/pdipm.c TaoView_BRGN() in src/tao/leastsquares/impls/brgn/brgn.c TaoView_POUNDERS() in src/tao/leastsquares/impls/pounders/pounders.c TaoView_LCL() in src/tao/pde_constrained/impls/lcl/lcl.c TaoView_BQPIP() in src/tao/quadratic/impls/bqpip/bqpip.c TaoView_GPCG() in src/tao/quadratic/impls/gpcg/gpcg.c TaoView_BMRM() in src/tao/unconstrained/impls/bmrm/bmrm.c TaoView_CG() in src/tao/unconstrained/impls/cg/taocg.c TaoView_LMVM() in src/tao/unconstrained/impls/lmvm/lmvm.c TaoView_NM() in src/tao/unconstrained/impls/neldermead/neldermead.c TaoView_NLS() in src/tao/unconstrained/impls/nls/nls.c TaoView_NTL() in src/tao/unconstrained/impls/ntl/ntl.c TaoView_OWLQN() in src/tao/unconstrained/impls/owlqn/owlqn.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode TaoView(Tao tao, PetscViewer viewer)
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
PETSC_VIEWER_ASCII_INFO_DETAIL
```

---

## Tao#

**URL:** https://petsc.org/release/manualpages/Tao/Tao/

**Contents:**
- Tao#
- Synopsis#
- Note#
- See Also#
- Level#
- Location#
- Examples#
- Implementations#

Abstract PETSc object that manages optimization solvers.

Tao is the object, while TAO, which stands for Toolkit for Advanced Optimization, is the software package.

Summary of Tao Solvers, TAO: Optimization Solvers, TaoCreate(), TaoDestroy(), TaoSetType(), TaoType

include/petsctaotypes.h

src/tao/leastsquares/tutorials/chwirut1f.F90 src/tao/leastsquares/tutorials/chwirut2f.F90 src/tao/leastsquares/tutorials/cs1.c src/tao/pde_constrained/tutorials/elliptic.c src/tao/constrained/tutorials/tomographyADMM.c src/tao/pde_constrained/tutorials/parabolic.c src/tao/constrained/tutorials/ex1.c src/tao/pde_constrained/tutorials/hyperbolic.c src/tao/constrained/tutorials/maros.c src/tao/leastsquares/tutorials/chwirut1.c

_p_Tao in include/petsc/private/taoimpl.h Tao_SNES in src/tao/snes/taosnes.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (julia):
```julia
typedef struct _p_Tao *Tao;
```

Example 2 (unknown):
```unknown
TaoCreate()
```

Example 3 (unknown):
```unknown
TaoDestroy()
```

Example 4 (unknown):
```unknown
TaoSetType()
```

---

## TAO_ADMM_REGULARIZER_SOFT_THRESH#

**URL:** https://petsc.org/release/manualpages/Tao/TAO_ADMM_REGULARIZER_SOFT_THRESH/

**Contents:**
- TAO_ADMM_REGULARIZER_SOFT_THRESH#
- Note#
- See Also#
- Level#
- Location#

Soft threshold to solve regularizer part of TAOADMM

Utilizes built-in SoftThreshold routines

TAO: Optimization Solvers, Tao, TAOADMM, TaoSoftThreshold(), TaoADMMSetRegularizerObjectiveAndGradientRoutine(), TaoADMMSetRegularizerHessianRoutine(), TaoADMMSetRegularizerType(), TAO_ADMM_REGULARIZER_USER

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoSoftThreshold()
```

Example 2 (unknown):
```unknown
TaoADMMSetRegularizerObjectiveAndGradientRoutine()
```

Example 3 (unknown):
```unknown
TaoADMMSetRegularizerHessianRoutine()
```

Example 4 (unknown):
```unknown
TaoADMMSetRegularizerType()
```

---

## TAO_ADMM_REGULARIZER_USER#

**URL:** https://petsc.org/release/manualpages/Tao/TAO_ADMM_REGULARIZER_USER/

**Contents:**
- TAO_ADMM_REGULARIZER_USER#
- Note#
- See Also#
- Level#
- Location#

User provided routines for regularizer part of TAOADMM

User needs to provided appropriate routines and type for regularizer solver

TAO: Optimization Solvers, Tao, TAOADMM, TaoADMMSetRegularizerType(), TAO_ADMM_REGULARIZER_SOFT_THRESH

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoADMMSetRegularizerType()
```

Example 2 (unknown):
```unknown
TAO_ADMM_REGULARIZER_SOFT_THRESH
```

---

## TAO_ADMM_UPDATE_ADAPTIVE#

**URL:** https://petsc.org/release/manualpages/Tao/TAO_ADMM_UPDATE_ADAPTIVE/

**Contents:**
- TAO_ADMM_UPDATE_ADAPTIVE#
- Note#
- See Also#
- Level#
- Location#

Adaptively update the spectral penalty

Adaptively updates spectral penalty of TAOADMM by using both steepest descent and minimum gradient.

TAO: Optimization Solvers, Tao, TAOADMM, TaoADMMSetUpdateType(), TAO_ADMM_UPDATE_BASIC, TAO_ADMM_UPDATE_ADAPTIVE_RELAXED

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoADMMSetUpdateType()
```

Example 2 (unknown):
```unknown
TAO_ADMM_UPDATE_BASIC
```

Example 3 (unknown):
```unknown
TAO_ADMM_UPDATE_ADAPTIVE_RELAXED
```

---

## TAO_ADMM_UPDATE_BASIC#

**URL:** https://petsc.org/release/manualpages/Tao/TAO_ADMM_UPDATE_BASIC/

**Contents:**
- TAO_ADMM_UPDATE_BASIC#
- Note#
- See Also#
- Level#
- Location#

Use same spectral penalty set at the beginning. This never performs an update to the penalty

Most basic implementation of TAOADMM. Generally slower than adaptive or adaptive relaxed version.

TAO: Optimization Solvers, Tao, TAOADMM, TaoADMMSetUpdateType(), TAO_ADMM_UPDATE_ADAPTIVE, TAO_ADMM_UPDATE_ADAPTIVE_RELAXED

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
TaoADMMSetUpdateType()
```

Example 2 (unknown):
```unknown
TAO_ADMM_UPDATE_ADAPTIVE
```

Example 3 (unknown):
```unknown
TAO_ADMM_UPDATE_ADAPTIVE_RELAXED
```

---

## TAO: Optimization Solvers#

**URL:** https://petsc.org/release/manual/tao/

**Contents:**
- TAO: Optimization Solvers#
- Getting Started: A Simple TAO Example#
- TAO Workflow#
  - Header File#
  - Creation and Destruction#
  - Command-line Options#
  - Defining Variables#
  - User Defined Callback Routines#
    - Application Context#
    - Objective Function and Gradient Routines#

The Toolkit for Advanced Optimization (TAO) focuses on algorithms for the solution of large-scale optimization problems on high-performance architectures. Methods are available for

Nonlinear Least-Squares

Unconstrained Minimization

Bound-Constrained Optimization

Generally Constrained Solvers

PDE-constrained Optimization

To help start using TAO immediately, we introduce a simple uniprocessor example. Please read TAO Algorithms for a more in-depth discussion on using the TAO solvers. The code presented below minimizes the extended Rosenbrock function \(f: \mathbb R^n \to \mathbb R\) defined by

where \(n = 2m\) is the number of variables. Note that while we use the C language to introduce the TAO software, the package is usable from C++, Fortran, and Python. PETSc for Fortran Users discusses additional issues concerning Fortran usage.

The code in the example contains many of the components needed to write most TAO programs and thus is illustrative of the features present in complex optimization problems. Note that for display purposes we have omitted some nonessential lines of code as well as the (essential) code required for the routine FormFunctionGradient, which evaluates the function and gradient, and the code for FormHessian, which evaluates the Hessian matrix for Rosenbrock’s function. The complete code is available in $TAO_DIR/src/unconstrained/tutorials/rosenbrock1.c. The following sections annotate the lines of code in the example.

Listing: src/tao/unconstrained/tutorials/rosenbrock1.c

Many TAO applications will follow an ordered set of procedures for solving an optimization problem: The user creates a Tao context and selects a default algorithm. Callback routines as well as vector (Vec) and matrix (Mat) data structures are then set. These callback routines will be used for evaluating the objective function, gradient, and perhaps the Hessian matrix. The user then invokes TAO to solve the optimization problem and finally destroys the Tao context. A list of the necessary functions for performing these steps using TAO is shown below.

TAO supports constructing an objective function by summing several distinct functions (called terms) via the TaoTerm object. With TaoTerm, the user can define one or more objective function ‘terms’. For an example, consider a data‑misfit term and a regularization term, each providing objective, gradient, and optional Hessian routines. TAO automatically composes (sums) the terms to form the overall objective and its derivatives at runtime. This approach promotes code reuse, makes it easy to modify scaling parameters, and simplifies complex problems that are naturally expressed as sums of contributions. In addition, it allows the easy implementation of efficient optimization algorithms that utilize the sum structure of the objective function. See TaoTerm: composable objective function terms for more information on the TaoTerm objects.

Note that the solver algorithm selected through the function TaoSetType() can be overridden at runtime by using an options database. Through this database, the user not only can select a minimization method (e.g., limited-memory variable metric, conjugate gradient, Newton with line search or trust region) but also can prescribe the convergence tolerance, set various monitoring routines, set iterative methods and preconditions for solving the linear systems, and so forth. See TAO Algorithms for more information on the solver methods available in TAO.

TAO applications written in C/C++ should have the statement

in each file that uses a routine in the TAO libraries.

A TAO solver can be created by calling the

routine. Much like creating PETSc vector and matrix objects, the first argument is an MPI communicator. An MPI [1] communicator indicates a collection of processors that will be used to evaluate the objective function, compute constraints, and provide derivative information. When only one processor is being used, the communicator PETSC_COMM_SELF can be used with no understanding of MPI. Even parallel users need to be familiar with only the basic concepts of message passing and distributed-memory computing. Most applications running TAO in parallel environments can employ the communicator PETSC_COMM_WORLD to indicate all processes known to PETSc in a given run.

can be used to set the algorithm TAO uses to solve the application. The various types of TAO solvers and the flags that identify them will be discussed in the following sections. The solution method should be carefully chosen depending on the problem being solved. Some solvers, for instance, are meant for problems with no constraints, whereas other solvers acknowledge constraints in the problem and handle them accordingly. The user must also be aware of the derivative information that is available. Some solvers require second-order information, while other solvers require only gradient or function information. The command line option -tao_type followed by a TAO method will override any method specified by the second argument. The command line option -tao_type bqnls, for instance, will specify the limited-memory quasi-Newton line search method for bound-constrained problems. Note that the TaoType variable is a string that requires quotation marks in an application program, but quotation marks are not required at the command line.

Each TAO solver that has been created should also be destroyed by using the

command. This routine frees the internal data structures used by the solver.

Additional options for the TAO solver can be set from the command line by using the

routine. This command also provides information about runtime options when the user includes the -help option on the command line.

In addition to common command line options shared by all TAO solvers, each TAO method also implements its own specialized options. Please refer to the documentation for individual methods for more details.

In all the optimization solvers, the application must provide a Vec object of appropriate dimension to represent the variables. This vector will be cloned by the solvers to create additional work space within the solver. If this vector is distributed over multiple processors, it should have a parallel distribution that allows for efficient scaling, inner products, and function evaluations. This vector can be passed to the application object by using the

routine. When using this routine, the application should initialize the vector with an approximate solution of the optimization problem before calling the TAO solver. This vector will be used by the TAO solver to store the solution. Elsewhere in the application, this solution vector can be retrieved from the application object by using the

routine. This routine takes the address of a Vec in the second argument and sets it to the solution vector used in the application.

A Tao must be able to evaluate a function in order to optimize it; depending on the solver chosen, it may also need to evaluate the gradient vector and Hessian matrix. TAO gives users two ways to specify this information: with callback functions for the evaluation operations (described in this section) provided directly to the Tao object, or with TaoTerm objects that encapsulate the functions and derivatives (see TaoTerm: composable objective function terms).

Writing a TAO application may require use of an application context. An application context is a structure or object defined by an application developer, passed into a routine also written by the application developer, and used within the routine to perform its stated task.

For example, a routine that evaluates an objective function may need parameters, work vectors, and other information. This information, which may be specific to an application and necessary to evaluate the objective, can be collected in a single structure and used as one of the arguments in the routine. The address of this structure will be cast as type (void*) and passed to the routine in the final argument. Many examples of these structures are included in the TAO distribution.

This technique offers several advantages. In particular, it allows for a uniform interface between TAO and the applications. The fundamental information needed by TAO appears in the arguments of the routine, while data specific to an application and its implementation is confined to an opaque pointer. The routines can access information created outside the local scope without the use of global variables. The TAO solvers and application objects will never access this structure, so the application developer has complete freedom to define it. If no such structure or needed by the application then a NULL pointer can be used.

TAO solvers that minimize an objective function require the application to evaluate the objective function. Some solvers may also require the application to evaluate derivatives of the objective function. Routines that perform these computations must be identified to the application object and must follow a strict calling sequence.

Routines should follow the form

in order to evaluate an objective function \(f: \, \mathbb R^n \to \mathbb R\). The first argument is the TAO Solver object, the second argument is the \(n\)-dimensional vector that identifies where the objective should be evaluated, and the fourth argument is an application context. This routine should use the third argument to return the objective value evaluated at the point specified by the vector in the second argument.

This routine, and the application context, should be passed to the application object by using the

routine. The first argument in this routine is the TAO solver object, the second argument is a function pointer to the routine that evaluates the objective, and the third argument is the pointer to an appropriate application context. Although the final argument may point to anything, it must be cast as a (void*) type. This pointer will be passed back to the developer in the fourth argument of the routine that evaluates the objective. In this routine, the pointer can be cast back to the appropriate type. Examples of these structures and their usage are provided in the distribution.

Many TAO solvers also require gradient information from the application The gradient of the objective function is specified in a similar manner. Routines that evaluate the gradient should have the calling sequence

where the first argument is the TAO solver object, the second argument is the variable vector, the third argument is the gradient vector, and the fourth argument is the user-defined application context. Only the third argument in this routine is different from the arguments in the routine for evaluating the objective function. The numbers in the gradient vector have no meaning when passed into this routine, but they should represent the gradient of the objective at the specified point at the end of the routine. This routine, and the user-defined pointer, can be passed to the application object by using the

routine. In this routine, the first argument is the Tao object, the second argument is the optional vector to hold the computed gradient, the third argument is the function pointer, and the fourth object is the application context, cast to (void*).

Instead of evaluating the objective and its gradient in separate routines, TAO also allows the user to evaluate the function and the gradient in the same routine. In fact, some solvers are more efficient when both function and gradient information can be computed in the same routine. These routines should follow the form

where the first argument is the TAO solver and the second argument points to the input vector for use in evaluating the function and gradient. The third argument should return the function value, while the fourth argument should return the gradient vector. The fifth argument is a pointer to a user-defined context. This context and the name of the routine should be set with the call

where the arguments are the TAO application, the optional vector to be used to hold the computed gradient, a function pointer, and a pointer to a user-defined context.

The TAO example problems demonstrate the use of these application contexts as well as specific instances of function, gradient, and Hessian evaluation routines. All these routines should return PETSC_SUCCESS after successful completion and a nonzero integer if the function is undefined at that point or an error occurred.

Some optimization algorithms also require a Hessian matrix from the user. The routine that evaluates the Hessian should have the form

where the first argument of this routine is a TAO solver object. The second argument is the point at which the Hessian should be evaluated. The third argument is the Hessian matrix, and the sixth argument is a user-defined context. Since the Hessian matrix is usually used in solving a system of linear equations, a preconditioner for the matrix is often needed. The fourth argument is the matrix that will be used for preconditioning the linear system; in most cases, this matrix will be the same as the Hessian matrix. The fifth argument is the flag used to set the Hessian matrix and linear solver in the routine KSPSetOperators().

One can set the Hessian evaluation routine by calling the

routine. The first argument is the TAO Solver object. The second and third arguments are, respectively, the Mat object where the Hessian will be stored and the Mat object that will be used for the preconditioning (they may be the same). The fourth argument is the function that evaluates the Hessian, and the fifth argument is a pointer to a user-defined context, cast to (void*).

Finite-difference approximations can be used to compute the gradient and the Hessian of an objective function. These approximations will slow the solve considerably and are recommended primarily for checking the accuracy of hand-coded gradients and Hessians. These routines are

respectively. They can be set by using TaoSetGradient() and TaoSetHessian() or through the options database with the options -tao_fdgrad and -tao_fd, respectively.

The efficiency of the finite-difference Hessian can be improved if the coloring of the matrix is known. If the application programmer creates a PETSc MatFDColoring object, it can be applied to the finite-difference approximation by setting the Hessian evaluation routine to

and using the MatFDColoring object as the last (void *) argument to TaoSetHessian().

One also can use finite-difference approximations to directly check the correctness of the gradient and/or Hessian evaluation routines. This process can be initiated from the command line by using the special TAO solver tao_fd_test together with the option -tao_test_gradient or -tao_test_hessian.

TAO also supports matrix-free methods. The matrices specified in the Hessian evaluation routine need not be conventional matrices; instead, they can point to the data required to implement a particular matrix-free method. The matrix-free variant is allowed only when the linear systems are solved by an iterative method in combination with no preconditioning (PCNONE or -pc_type none), a user-provided matrix from which to construct the preconditioner, or a user-provided preconditioner shell (PCSHELL). In other words, matrix-free methods cannot be used if a direct solver is to be employed. Details about using matrix-free methods are provided in the User-Guide.

Fig. 7 Tao use of PETSc and callbacks#

Some optimization problems also impose constraints on the variables or intermediate application states. The user defines these constraints through the appropriate TAO interface functions and callback routines where necessary.

The simplest type of constraint on an optimization problem puts lower or upper bounds on the variables. Vectors that represent lower and upper bounds for each variable can be set with the

command. The first vector and second vector should contain the lower and upper bounds, respectively. When no upper or lower bound exists for a variable, the bound may be set to PETSC_INFINITY or PETSC_NINFINITY. After the two bound vectors have been set, they may be accessed with the command TaoGetVariableBounds().

Since not all solvers recognize the presence of bound constraints on variables, the user must be careful to select a solver that acknowledges these bounds.

Some TAO algorithms also support general constraints as a linear or nonlinear function of the optimization variables. These constraints can be imposed either as equalities or inequalities. TAO currently does not make any distinctions between linear and nonlinear constraints, and implements them through the same software interfaces.

In the equality constrained case, TAO assumes that the constraints are formulated as \(c_e(x) = 0\) and requires the user to implement a callback routine for evaluating \(c_e(x)\) at a given vector of optimization variables,

As in the previous callback routines, the first argument is the TAO solver object. The second and third arguments are the vector of optimization variables (input) and vector of equality constraints (output), respectively. The final argument is a pointer to the user-defined application context, cast into (void*).

Generally constrained TAO algorithms also require a second user callback function to compute the constraint Jacobian matrix \(\nabla_x c_e(x)\),

where the first and last arguments are the TAO solver object and the application context pointer as before. The second argument is the vector of optimization variables at which the computation takes place. The third and fourth arguments are the constraint Jacobian and its pseudo-inverse (optional), respectively. The pseudoinverse is optional, and if not available, the user can simply set it to the constraint Jacobian itself.

These callback functions are then given to the TAO solver using the interface functions

Inequality constraints are assumed to be formulated as \(c_i(x) \geq 0\) and follow the same workflow as equality constraints using the TaoSetInequalityConstraintsRoutine() and TaoSetJacobianInequalityRoutine() interfaces.

Some TAO algorithms may adopt an alternative double-sided \(c_l \leq c_i(x) \leq c_u\) formulation and require the lower and upper bounds \(c_l\) and \(c_u\) to be set using the TaoSetInequalityBounds(Tao, Vec, Vec) interface. Please refer to the documentation for each TAO algorithm for further details.

The objective function optimized by Tao may be a sum of one or more terms, where each term provides various evaluation routines, such as the objective value, gradient, or Hessian for the term. Here, we define term as the basic additive unit used to form an objective function, equipped with appropriate evaluation routines (objective, gradient, and/or Hessian).

For an example, Tikhonov regularization (also known as Ridge Regression), can be formulated as \(f(x) + \beta ||x||_2^2\). This can be viewed as the summation of two terms, \(f(x) \) and \( \beta ||x||_2^2\).

Each TaoTerm encapsulates the routines needed to evaluate its own contribution; Tao automatically manages aggregating (summing) the value, gradient, and/or Hessian across all TaoTerm objects in the Tao object. This lets users modify terms without changing their base \(f(x)\) function code; for example, to add regularization.

Each TaoTerm represents a parametric real-valued function \(f(x; p)\) for solution variable \(x\) and parameters \(p\). The interface includes methods for evaluating \(f(x; p)\) (TaoTermComputeObjective()), \(\nabla_x f(x; p)\) (TaoTermComputeGradient() and TaoTermComputeObjectiveAndGradient()), and \(\nabla_x^2 f(x; p)\) (TaoTermComputeHessian()).

A TaoTerm can be added to a Tao object by calling the

routine. The first argument is the Tao object. The second argument is an optional prefix for the TaoTerm. The third argument is the scaling coefficient \(\alpha\), and the fourth argument is the TaoTerm to add to the Tao object. The fifth and sixth arguments are the optional parameters vector and optional mapping matrix, respectively.

If the current objective function of Tao is \(f(x)\), then after calling TaoAddTerm() with scale \(\alpha\), term \(g\), parameter \(p\), and map \(A\), the objective becomes

The mapping matrix \(A\) transforms the Tao solution vector \(x\) into the term’s solution space before evaluation. For example, if the Tao solution vector is \(x \in \mathbb{R}^n\) and \(A \in \mathbb{R}^{m \times n}\), then \(Ax \in \mathbb{R}^m\) and therefore the term’s solution space is \(\mathbb{R}^m\). If no mapping matrix is provided, the identity matrix is assumed and the term’s solution space must match the Tao solution space. When a mapping matrix is used, the parameter space may depend on either the row or column space of \(A\); see the documentation for each TaoTermType.

Tao automatically applies the scaling and the chain-rule transformation of gradients and Hessians:

Mapped gradients: \(\alpha A^T \nabla g(Ax; p)\)

Mapped Hessians: \(\alpha A^T \nabla^2 g(Ax; p) A\)

Every TaoTerm has two vector spaces:

Solution space — the vector space of the optimization variable \(x\) in \(f(x; p)\). Its size is set with TaoTermSetSolutionSizes(), TaoTermSetSolutionLayout(), or TaoTermSetSolutionTemplate(), and reported as \(N\) in TaoTermView().

If a mapping matrix \(A \in \mathbb{R}^{m \times n}\) is used, then \(n\) must match the dimension of the Tao solution space, and \(m\) must match the solution space of the TaoTerm.

Parameter space — the vector space of the parameter vector \(p\) in \(f(x; p)\). Parameters are fixed data that are not optimized over; they are passed to the evaluation routines (e.g., TaoTermComputeObjective()). Its size is set with TaoTermSetParametersSizes(), TaoTermSetParametersLayout(), or TaoTermSetParametersTemplate(), and reported as \(K\) in TaoTermView(). Whether a term accepts, requires, or ignores parameters is determined by TaoTermSetParametersMode(). Some TaoTermTypes require the solution and parameter spaces to be related (e.g., have the same size); see the documentation for each type. For users, setting parameter space for built-in TaoTermTypes is generally not needed, except for TAOTERMSHELL.

For an example of using mapping matrices with TaoTerm, see the elastic net regularization example, which demonstrates the use of TAOTERMHALFL2SQUARED with a mapping matrix to represent a data misfit term.

TAO comes with several built-in implementations for TaoTerm:

TAOTERMCALLBACKS: wraps the callback functions set via TaoSetObjective(), TaoSetGradient(), TaoSetObjectiveAndGradient(), and TaoSetHessian(). This type is automatically created internally when needed. It does not accept parameters and always has TAOTERM_PARAMETERS_NONE.

TAOTERMHALFL2SQUARED: \(f(x;p) = \tfrac{1}{2} \|x - p\|_2^2\) (See TaoTermCreateHalfL2Squared().)

TAOTERML1: \(f(x;p) = \|x - p\|_1\) (See TaoTermCreateL1().)

TAOTERMQUADRATIC: \(f(x;p) = \tfrac{1}{2}(x - p)^T A (x - p)\) for matrix \(A\) (See TaoTermCreateQuadratic().)

TAOTERMSUM: a sum of other terms implemented by TaoTerm, \(f(x;p) = \sum_i \alpha_i f(A_i x; p_i)\).

TAOTERMSHELL: an interface for user-defined terms, see User-defined TaoTerm implementations.

The parameters \(p\) of the parametric function \(f(x;p)\) implemented by a TaoTerm are passed as arguments in the evaluation routines. For some terms, however, omitting the parameters results in a default value of \(p\) being used. For TAOTERMHALFL2SQUARED, TAOTERML1, and TAOTERMQUADRATIC the default is \(p = 0\). In general, the parametric behavior of a TaoTerm is determined by TaoTermSetParametersMode():

TAOTERM_PARAMETERS_OPTIONAL: default parameters are used if NULL is passed for the parameters argument

TAOTERM_PARAMETERS_NONE: the term is not parametric, NULL is the only valid parameters argument

TAOTERM_PARAMETERS_REQUIRED: parameters are required, it is an error to pass NULL for the parameters argument

A TaoTerm can be set to an empty Tao object or added to an existing Tao using TaoAddTerm(). The entire objective function of a Tao object can be retrieved as a single TaoTerm using TaoGetTerm(), which returns the term along with its scale, parameters, and mapping matrix (if any).

Currently, TaoAddTerm() does not support bounded Newton solvers (TAOBNK,TAOBNLS,TAOBNTL,TAOBNTR,and TAOBQNK). For these solvers, one must use function callbacks only - TaoSetObjective(), TaoSetGradient(), TaoSetObjectiveAndGradient(), or TaoSetHessian().

For example: if you have specified an objective function \(f(x)\) using TaoSetObjectiveAndGradient(), and a regularizer \(g(x;p)\) is specified by a TaoTerm, you can create the objective function \(f(x) + \alpha g(Ax; p)\) using:

The example $TAO_DIR/src/unconstrained/tutorials/elastic_net_regularization.c uses this interface to define the optimization problem \(\min_x \tfrac{1}{2} \|Ax - b\|_W^2 + \lambda_2 \tfrac{1}{2}\|x\|_2^2 + \lambda_1 \|D x - y\|_1\):

Listing: src/tao/unconstrained/tutorials/elastic_net_regularization.c

Regularization terms can also be added to the objective function of a Tao solver from the command line. For instance, the elastic net regularizer \(\frac{0.4}{2} \|x\|_2^2 + 0.7 \|x\|_1\) can be added with the following options:

In the above, ridge_, and lasso_ are PETSc option prefixes and could be any unique strings for each term to be added.

When more than one TaoTerm object is set to Tao (or both TaoSetObjective() and TaoAddTerm() are used), a TaoTerm with type TAOTERMSUM gets created internally, and all the subsequently added TaoTerm objects get stored in it. With this structure in mind, users can gradually control each term, with the following command line options:

A user-defined TaoTerm can be defined from function callbacks using the TAOTERMSHELL type. This interface is very similar to TAOSHELL: there is a single application context that is set with TaoTermShellSetContext() and obtained with TaoTermShellGetContext(), and the evaluation routines are set by passing function callbacks with the same signature as routines they implement (see for example TaoTermShellSetObjectiveAndGradient()). As an example, $TAO_DIR/src/unconstrained/tutorials/rosenbrock1_taoterm.c in the example below demonstrates the same Rosenbrock example as the first example.

Listing: src/tao/unconstrained/tutorials/rosenbrock1_taoterm.c

In some cases, for a given TAOTERMSUM, the user may only want some evaluation of a specific TaoTerm (instead of computing all of them and summing the results). For an example, in a case where TAOTERMSUM is composed of TAOTERMHALFL2SQUARED and TAOTERML1, but the user only wants the objective function evaluation of TAOTERML1, and not its gradient and Hessian evaluations. In this case, user can mask desired evaluation operations via TaoTermSumSetTermMask(). Masking can also be done from the command line. For instance, for the elastic net regularization example above, the user can mask gradient and Hessian evaluation of TAOTERML1 with the following options:

Once the application and solver have been set up, the solve takes place with a call to the

routine. We discuss several universal options below.

Although TAO and its solvers set default parameters that are useful for many problems, the user may need to modify these parameters in order to change the behavior and convergence of various algorithms.

One convergence criterion for most algorithms concerns the number of digits of accuracy needed in the solution. In particular, the convergence test employed by TAO attempts to stop when the error in the constraints is less than \(\epsilon_{crtol}\) and either

where \(X\) is the current approximation to the true solution \(X^*\) and \(X_0\) is the initial guess. \(X^*\) is unknown, so TAO estimates \(f(X) - f(X^*)\) with either the square of the norm of the gradient or the duality gap. A relative tolerance of \(\epsilon_{frtol}=0.01\) indicates that two significant digits are desired in the objective function. Each solver sets its own convergence tolerances, but they can be changed by using the routine TaoSetTolerances(). Another set of convergence tolerances terminates the solver when the norm of the gradient function (or Lagrangian function for bound-constrained problems) is sufficiently close to zero.

Other stopping criteria include a minimum trust-region radius or a maximum number of iterations. These parameters can be set with the routines TaoSetTrustRegionTolerance() and TaoSetMaximumIterations() Similarly, a maximum number of function evaluations can be set with the command TaoSetMaximumFunctionEvaluations(). -tao_max_it, and -tao_max_funcs.

To see parameters and performance statistics for the solver, the routine

can be used. This routine will display to standard output the number of function evaluations need by the solver and other information specific to the solver. This same output can be produced by using the command line option -tao_view.

The progress of the optimization solver can be monitored with the runtime option -tao_monitor. Although monitoring routines can be customized, the default monitoring routine will print out several relevant statistics to the screen.

The user also has access to information about the current solution. The current iteration number, objective function value, gradient norm, infeasibility norm, and step length can be retrieved with the following command.

The last argument returns a code that indicates the reason that the solver terminated. Positive numbers indicate that a solution has been found, while negative numbers indicate a failure. A list of reasons can be found in the manual page for TaoGetConvergedReason().

After exiting the TaoSolve() function, the solution and the gradient can be recovered with the following routines.

Note that the Vec returned by TaoGetSolution() will be the same vector passed to TaoSetSolution(). This information can be obtained during user-defined routines such as a function evaluation and customized monitoring routine or after the solver has terminated.

Certain special classes of problems solved with TAO utilize specialized code interfaces that are described below per problem type.

TAO solves PDE-constrained optimization problems of the form

where the state variable \(u\) is the solution to the discretized partial differential equation defined by \(g\) and parametrized by the design variable \(v\), and \(f\) is an objective function. The Lagrange multipliers on the constraint are denoted by \(y\). This method is set by using the linearly constrained augmented Lagrangian TAO solver tao_lcl.

We make two main assumptions when solving these problems: the objective function and PDE constraints have been discretized so that we can treat the optimization problem as finite dimensional and \(\nabla_u g(u,v)\) is invertible for all \(u\) and \(v\).

Unlike other TAO solvers where the solution vector contains only the optimization variables, PDE-constrained problems solved with tao_lcl combine the design and state variables together in a monolithic solution vector \(x^T = [u^T, v^T]\). Consequently, the user must provide index sets to separate the two,

where the first IS is a PETSc IndexSet containing the indices of the state variables and the second IS the design variables.

PDE constraints have the general form \(g(x) = 0\), where \(c: \mathbb R^n \to \mathbb R^m\). These constraints should be specified in a routine, written by the user, that evaluates \(g(x)\). The routine that evaluates the constraint equations should have the form

The first argument of this routine is a TAO solver object. The second argument is the variable vector at which the constraint function should be evaluated. The third argument is the vector of function values \(g(x)\), and the fourth argument is a pointer to a user-defined context. This routine and the user-defined context should be set in the TAO solver with the

command. In this function, the first argument is the TAO solver object, the second argument a vector in which to store the constraints, the third argument is a function point to the routine for evaluating the constraints, and the fourth argument is a pointer to a user-defined context.

The Jacobian of \(g(x)\) is the matrix in \(\mathbb R^{m \times n}\) such that each column contains the partial derivatives of \(g(x)\) with respect to one variable. The evaluation of the Jacobian of \(g\) should be performed by calling the

routines. In these functions, The first argument is the TAO solver object. The second argument is the variable vector at which to evaluate the Jacobian matrix, the third argument is the Jacobian matrix, and the last argument is a pointer to a user-defined context. The fourth and fifth arguments of the Jacobian evaluation with respect to the state variables are for providing PETSc matrix objects for the preconditioner and for applying the inverse of the state Jacobian, respectively. This inverse matrix may be PETSC_NULL, in which case TAO will use a PETSc Krylov subspace solver to solve the state system. These evaluation routines should be registered with TAO by using the

routines. The first argument is the TAO solver object, and the second argument is the matrix in which the Jacobian information can be stored. For the state Jacobian, the third argument is the matrix that will be used for preconditioning, and the fourth argument is an optional matrix for the inverse of the state Jacobian. One can use PETSC_NULL for this inverse argument and let PETSc apply the inverse using a KSP method, but faster results may be obtained by manipulating the structure of the Jacobian and providing an inverse. The fifth argument is the function pointer, and the sixth argument is an optional user-defined context. Since no solve is performed with the design Jacobian, there is no need to provide preconditioner or inverse matrices.

For nonlinear least squares applications, we are solving the optimization problem

For these problems, the objective function value should be computed as a vector of residuals, \(r(x)\), computed with a function of the form

routine. If required by the algorithm, the Jacobian of the residual, \(J = \partial r(x) / \partial x\), should be computed with a function of the form

Complementarity applications have equality constraints in the form of nonlinear equations \(C(X) = 0\), where \(C: \mathbb R^n \to \mathbb R^m\). These constraints should be specified in a routine written by the user with the form

that evaluates \(C(X)\). The first argument of this routine is a TAO Solver object. The second argument is the variable vector \(X\) at which the constraint function should be evaluated. The third argument is the output vector of function values \(C(X)\), and the fourth argument is a pointer to a user-defined context.

This routine and the user-defined context must be registered with TAO by using the

command. In this command, the first argument is TAO Solver object, the second argument is vector in which to store the function values, the third argument is the user-defined routine that evaluates \(C(X)\), and the fourth argument is a pointer to a user-defined context that will be passed back to the user.

The Jacobian of the function is the matrix in \(\mathbb R^{m \times n}\) such that each column contains the partial derivatives of \(f\) with respect to one variable. The evaluation of the Jacobian of \(C\) should be performed in a routine of the form

In this function, the first argument is the TAO Solver object and the second argument is the variable vector at which to evaluate the Jacobian matrix. The third argument is the Jacobian matrix, and the sixth argument is a pointer to a user-defined context. Since the Jacobian matrix may be used in solving a system of linear equations, a preconditioner for the matrix may be needed. The fourth argument is the matrix that will be used for preconditioning the linear system; in most cases, this matrix will be the same as the Hessian matrix. The fifth argument is the flag used to set the Jacobian matrix and linear solver in the routine KSPSetOperators().

This routine should be specified to TAO by using the

command. The first argument is the TAO Solver object; the second and third arguments are the Mat objects in which the Jacobian will be stored and the Mat object that will be used for the preconditioning (they may be the same), respectively. The fourth argument is the function pointer; and the fifth argument is an optional user-defined context. The Jacobian matrix should be created in a way such that the product of it and the variable vector can be stored in the constraint vector.

TAO includes a variety of optimization algorithms for several classes of problems (unconstrained, bound-constrained, and PDE-constrained minimization, nonlinear least-squares, and complementarity). The TAO algorithms for solving these problems are detailed in this section, a particular algorithm can chosen by using the TaoSetType() function or using the command line arguments -tao_type <name>. For those interested in extending these algorithms or using new ones, please see Adding a Solver for more information.

Unconstrained minimization is used to minimize a function of many variables without any constraints on the variables, such as bounds. The methods available in TAO for solving these problems can be classified according to the amount of derivative information required:

Function evaluation only – Nelder-Mead method (tao_nm)

Function and gradient evaluations – limited-memory, variable-metric method (tao_lmvm) and nonlinear conjugate gradient method (tao_cg)

Function, gradient, and Hessian evaluations – Newton Krylov methods: Newton line search (tao_nls), Newton trust-region (tao_ntr), and Newton trust-region line-search (tao_ntl)

The best method to use depends on the particular problem being solved and the accuracy required in the solution. If a Hessian evaluation routine is available, then the Newton line search and Newton trust-region methods will likely perform best. When a Hessian evaluation routine is not available, then the limited-memory, variable-metric method is likely to perform best. The Nelder-Mead method should be used only as a last resort when no gradient information is available.

Each solver has a set of options associated with it that can be set with command line arguments. These algorithms and the associated options are briefly discussed in this section.

TAO features three Newton-Krylov algorithms, separated by their globalization methods for unconstrained optimization: line search (NLS), trust region (NTR), and trust region with a line search (NTL). They are available via the TAO solvers TAONLS, TAONTR and TAONTL, respectively, or the -tao_type nls/ntr/ntl flag.

The Newton line search method solves the symmetric system of equations

to obtain a step \(d_k\), where \(H_k\) is the Hessian of the objective function at \(x_k\) and \(g_k\) is the gradient of the objective function at \(x_k\). For problems where the Hessian matrix is indefinite, the perturbed system of equations

is solved to obtain the direction, where \(\rho_k\) is a positive constant. If the direction computed is not a descent direction, the (scaled) steepest descent direction is used instead. Having obtained the direction, a Moré-Thuente line search is applied to obtain a step length, \(\tau_k\), that approximately solves the one-dimensional optimization problem

The Newton line search method can be selected by using the TAO solver tao_nls. The options available for this solver are listed in Table 18. For the best efficiency, function and gradient evaluations should be performed simultaneously when using this algorithm.

KSPType for linear system

PCType for linear system

Initial perturbation value

Minimum initial perturbation value

Maximum initial perturbation value

Gradient norm factor when initializing perturbation

Maximum perturbation when increasing value

Perturbation growth when increasing value

Gradient norm factor when increasing perturbation

Minimum non-zero perturbation when decreasing value

Perturbation shrink factor when decreasing value

Gradient norm factor when decreasing perturbation

\(\nu_1\) in step update

\(\nu_2\) in step update

\(\nu_3\) in step update

\(\nu_4\) in step update

\(\omega_1\) in step update

\(\omega_2\) in step update

\(\omega_3\) in step update

\(\omega_4\) in step update

\(\omega_5\) in step update

\(\eta_1\) in reduction update

\(\eta_2\) in reduction update

\(\eta_3\) in reduction update

\(\eta_4\) in reduction update

\(\alpha_1\) in reduction update

\(\alpha_2\) in reduction update

\(\alpha_3\) in reduction update

\(\alpha_4\) in reduction update

\(\alpha_5\) in reduction update

\(\mu_1\) in interpolation update

\(\mu_2\) in interpolation update

\(\gamma_1\) in interpolation update

\(\gamma_2\) in interpolation update

\(\gamma_3\) in interpolation update

\(\gamma_4\) in interpolation update

\(\theta\) in interpolation update

The system of equations is approximately solved by applying the conjugate gradient method, Nash conjugate gradient method, Steihaug-Toint conjugate gradient method, generalized Lanczos method, or an alternative Krylov subspace method supplied by PETSc. The method used to solve the systems of equations is specified with the command line argument -tao_nls_ksp_type (cg|nash|stcg|gltr|gmres) where stcg is the default. See the PETSc manual for further information on changing the behavior of the linear system solvers.

A good preconditioner reduces the number of iterations required to solve the linear system of equations. For the conjugate gradient methods and generalized Lanczos method, this preconditioner must be symmetric and positive definite. The available options are to use no preconditioner, the absolute value of the diagonal of the Hessian matrix, a limited-memory BFGS approximation to the Hessian matrix, or one of the other preconditioners provided by the PETSc package. These preconditioners are specified by the command line arguments -tao_nls_pc_type (none|jacobi|icc|ilu|lmvm), respectively. The default is the lmvm preconditioner, which uses a BFGS approximation of the inverse Hessian. See the PETSc manual for further information on changing the behavior of the preconditioners.

The perturbation \(\rho_k\) is added when the direction returned by the Krylov subspace method is not a descent direction, the Krylov method diverged due to an indefinite preconditioner or matrix, or a direction of negative curvature was found. In the last two cases, if the step returned is a descent direction, it is used during the line search. Otherwise, a steepest descent direction is used during the line search. The perturbation is decreased as long as the Krylov subspace method reports success and increased if further problems are encountered. There are three cases: initializing, increasing, and decreasing the perturbation. These cases are described below.

If \(\rho_k\) is zero and a problem was detected with either the direction or the Krylov subspace method, the perturbation is initialized to

where \(g(x_k)\) is the gradient of the objective function and imin is set with the command line argument -tao_nls_imin imin with a default value of \(10^{-4}\), imfac by -tao_nls_imfac with a default value of 0.1, and imax by -tao_nls_imax with a default value of 100. When using the gltr method to solve the system of equations, an estimate of the minimum eigenvalue \(\lambda_1\) of the Hessian matrix is available. This value is used to initialize the perturbation to \(\rho_{k+1} = \max\left\{\rho_{k+1}, -\lambda_1\right\}\) in this case.

If \(\rho_k\) is nonzero and a problem was detected with either the direction or Krylov subspace method, the perturbation is increased to

where \(g(x_k)\) is the gradient of the objective function and pgfac is set with the command line argument -tao_nls_pgfac with a default value of 10, pmgfac by -tao_nls_pmgfac with a default value of 0.1, and pmax by -tao_nls_pmax with a default value of 100.

If \(\rho_k\) is nonzero and no problems were detected with either the direction or Krylov subspace method, the perturbation is decreased to

where \(g(x_k)\) is the gradient of the objective function, psfac is set with the command line argument -tao_nls_psfac with a default value of 0.4, and pmsfac is set by -tao_nls_pmsfac with a default value of 0.1. Moreover, if \(\rho_{k+1} < \text{pmin}\), then \(\rho_{k+1} = 0\), where pmin is set with the command line argument -tao_nls_pmin and has a default value of \(10^{-12}\).

Near a local minimizer to the unconstrained optimization problem, the Hessian matrix will be positive-semidefinite; the perturbation will shrink toward zero, and one would eventually observe a superlinear convergence rate.

When using nash, stcg, or gltr to solve the linear systems of equation, a trust-region radius needs to be initialized and updated. This trust-region radius simultaneously limits the size of the step computed and reduces the number of iterations of the conjugate gradient method. The method for initializing the trust-region radius is set with the command line argument -tao_nls_init_type (constant|direction|interpolation); interpolation, which chooses an initial value based on the interpolation scheme found in [CGT00], is the default. This scheme performs a number of function and gradient evaluations to determine a radius such that the reduction predicted by the quadratic model along the gradient direction coincides with the actual reduction in the nonlinear function. The iterate obtaining the best objective function value is used as the starting point for the main line search algorithm. The constant method initializes the trust-region radius by using the value specified with the -tao_trust0 radius command line argument, where the default value is 100. The direction technique solves the first quadratic optimization problem by using a standard conjugate gradient method and initializes the trust region to \(\|s_0\|\).

The method for updating the trust-region radius is set with the command line argument -tao_nls_update_type (step|reduction|interpolation); step is the default. The step method updates the trust-region radius based on the value of \(\tau_k\). In particular,

where \(0 < \omega_1 < \omega_2 < \omega_3 = 1 < \omega_4 < \omega_5\) and \(0 < \nu_1 < \nu_2 < \nu_3 < \nu_4\) are constants. The reduction method computes the ratio of the actual reduction in the objective function to the reduction predicted by the quadratic model for the full step, \(\kappa_k = \frac{f(x_k) - f(x_k + d_k)}{q(x_k) - q(x_k + d_k)}\), where \(q_k\) is the quadratic model. The radius is then updated as

where \(0 < \alpha_1 < \alpha_2 < \alpha_3 = 1 < \alpha_4 < \alpha_5\) and \(0 < \eta_1 < \eta_2 < \eta_3 < \eta_4\) are constants. The interpolation method uses the same interpolation mechanism as in the initialization to compute a new value for the trust-region radius.

This algorithm will be deprecated in the next version and replaced by the Bounded Newton Line Search (BNLS) algorithm that can solve both bound constrained and unconstrained problems.

The Newton trust-region method solves the constrained quadratic programming problem

to obtain a direction \(d_k\), where \(H_k\) is the Hessian of the objective function at \(x_k\), \(g_k\) is the gradient of the objective function at \(x_k\), and \(\Delta_k\) is the trust-region radius. If \(x_k + d_k\) sufficiently reduces the nonlinear objective function, then the step is accepted, and the trust-region radius is updated. However, if \(x_k + d_k\) does not sufficiently reduce the nonlinear objective function, then the step is rejected, the trust-region radius is reduced, and the quadratic program is re-solved by using the updated trust-region radius. The Newton trust-region method can be set by using the TAO solver tao_ntr. The options available for this solver are listed in Table 19. For the best efficiency, function and gradient evaluations should be performed separately when using this algorithm.

KSPType for linear system

PCType for linear system

constant, direction, interpolation

Radius initialization method

\(\mu_1\) in interpolation init

\(\mu_2\) in interpolation init

\(\gamma_1\) in interpolation init

\(\gamma_2\) in interpolation init

\(\gamma_3\) in interpolation init

\(\gamma_4\) in interpolation init

\(\theta\) in interpolation init

step, reduction, interpolation

\(\mu_1\) in interpolation init

\(\mu_2\) in interpolation init

\(\gamma_1\) in interpolation init

\(\gamma_2\) in interpolation init

\(\gamma_3\) in interpolation init

\(\gamma_4\) in interpolation init

\(\theta\) in interpolation init

\(\eta_1\) in reduction update

\(\eta_2\) in reduction update

\(\eta_3\) in reduction update

\(\eta_4\) in reduction update

\(\alpha_1\) in reduction update

\(\alpha_2\) in reduction update

\(\alpha_3\) in reduction update

\(\alpha_4\) in reduction update

\(\alpha_5\) in reduction update

\(\mu_1\) in interpolation update

\(\mu_2\) in interpolation update

\(\gamma_1\) in interpolation update

\(\gamma_2\) in interpolation update

\(\gamma_3\) in interpolation update

\(\gamma_4\) in interpolation update

\(\theta\) in interpolation update

The quadratic optimization problem is approximately solved by applying the Nash or Steihaug-Toint conjugate gradient methods or the generalized Lanczos method to the symmetric system of equations \(H_k d = -g_k\). The method used to solve the system of equations is specified with the command line argument -tao_ntr_ksp_type (nash|stcg|gltr) where stcg is the default. See the PETSc manual for further information on changing the behavior of these linear system solvers.

A good preconditioner reduces the number of iterations required to compute the direction. For the Nash and Steihaug-Toint conjugate gradient methods and generalized Lanczos method, this preconditioner must be symmetric and positive definite. The available options are to use no preconditioner, the absolute value of the diagonal of the Hessian matrix, a limited-memory BFGS approximation to the Hessian matrix, or one of the other preconditioners provided by the PETSc package. These preconditioners are specified by the command line argument -tao_ntr_pc_type (none|jacobi|icc|ilu|lmvm), respectively. The default is the lmvm preconditioner. See the PETSc manual for further information on changing the behavior of the preconditioners.

The method for computing an initial trust-region radius is set with the command line arguments -tao_ntr_init_type (constant|direction|interpolation); interpolation, which chooses an initial value based on the interpolation scheme found in [CGT00], is the default. This scheme performs a number of function and gradient evaluations to determine a radius such that the reduction predicted by the quadratic model along the gradient direction coincides with the actual reduction in the nonlinear function. The iterate obtaining the best objective function value is used as the starting point for the main trust-region algorithm. The constant method initializes the trust-region radius by using the value specified with the -tao_trust0 radius command line argument, where the default value is 100. The direction technique solves the first quadratic optimization problem by using a standard conjugate gradient method and initializes the trust region to \(\|s_0\|\).

The method for updating the trust-region radius is set with the command line arguments -tao_ntr_update_type (reduction|interpolation); reduction is the default. The reduction method computes the ratio of the actual reduction in the objective function to the reduction predicted by the quadratic model for the full step, \(\kappa_k = \frac{f(x_k) - f(x_k + d_k)}{q(x_k) - q(x_k + d_k)}\), where \(q_k\) is the quadratic model. The radius is then updated as

where \(0 < \alpha_1 < \alpha_2 < \alpha_3 = 1 < \alpha_4 < \alpha_5\) and \(0 < \eta_1 < \eta_2 < \eta_3 < \eta_4\) are constants. The interpolation method uses the same interpolation mechanism as in the initialization to compute a new value for the trust-region radius.

This algorithm will be deprecated in the next version and replaced by the Bounded Newton Trust Region (BNTR) algorithm that can solve both bound constrained and unconstrained problems.

NTL safeguards the trust-region globalization such that a line search is used in the event that the step is initially rejected by the predicted versus actual decrease comparison. If the line search fails to find a viable step length for the Newton step, it falls back onto a scaled gradient or a gradient descent step. The trust radius is then modified based on the line search step length.

This algorithm will be deprecated in the next version and replaced by the Bounded Newton Trust Region with Line Search (BNTL) algorithm that can solve both bound constrained and unconstrained problems.

The limited-memory, variable-metric method (LMVM) computes a positive definite approximation to the Hessian matrix from a limited number of previous iterates and gradient evaluations. A direction is then obtained by solving the system of equations

where \(H_k\) is the Hessian approximation obtained by using the BFGS update formula. The inverse of \(H_k\) can readily be applied to obtain the direction \(d_k\). Having obtained the direction, a Moré-Thuente line search is applied to compute a step length, \(\tau_k\), that approximately solves the one-dimensional optimization problem

The current iterate and Hessian approximation are updated, and the process is repeated until the method converges. This algorithm is the default unconstrained minimization solver and can be selected by using the TAO solver tao_lmvm. For best efficiency, function and gradient evaluations should be performed simultaneously when using this algorithm.

The primary factors determining the behavior of this algorithm are the type of Hessian approximation used, the number of vectors stored for the approximation and the initialization/scaling of the approximation. These options can be configured using the -tao_lmvm_mat_lmvm prefix. For further detail, we refer the reader to the MATLMVM matrix type definitions in the PETSc Manual.

The LMVM algorithm also allows the user to define a custom initial Hessian matrix \(H_{0,k}\) through the interface function TaoLMVMSetH0(). This user-provided initialization overrides any other scalar or diagonal initialization inherent to the LMVM approximation. The provided \(H_{0,k}\) must be a PETSc Mat type object that represents a positive-definite matrix. The approximation prefers MatSolve() if the provided matrix has MATOP_SOLVE implemented. Otherwise, MatMult() is used in a KSP solve to perform the inversion of the user-provided initial Hessian.

In applications where TaoSolve() on the LMVM algorithm is repeatedly called to solve similar or related problems, -tao_lmvm_recycle flag can be used to prevent resetting the LMVM approximation between subsequent solutions. This recycling also avoids one extra function and gradient evaluation, instead re-using the values already computed at the end of the previous solution.

This algorithm will be deprecated in the next version and replaced by the Bounded Quasi-Newton Line Search (BQNLS) algorithm that can solve both bound constrained and unconstrained problems.

The nonlinear conjugate gradient method can be viewed as an extension of the conjugate gradient method for solving symmetric, positive-definite linear systems of equations. This algorithm requires only function and gradient evaluations as well as a line search. The TAO implementation uses a Moré-Thuente line search to obtain the step length. The nonlinear conjugate gradient method can be selected by using the TAO solver tao_cg. For the best efficiency, function and gradient evaluations should be performed simultaneously when using this algorithm.

Five variations are currently supported by the TAO implementation: the Fletcher-Reeves method, the Polak-Ribiére method, the Polak-Ribiére-Plus method [NW06], the Hestenes-Stiefel method, and the Dai-Yuan method. These conjugate gradient methods can be specified by using the command line argument -tao_cg_type (fr|pr|prp|hs|dy), respectively. The default value is prp.

The conjugate gradient method incorporates automatic restarts when successive gradients are not sufficiently orthogonal. TAO measures the orthogonality by dividing the inner product of the gradient at the current point and the gradient at the previous point by the square of the Euclidean norm of the gradient at the current point. When the absolute value of this ratio is greater than \(\eta\), the algorithm restarts using the gradient direction. The parameter \(\eta\) can be set by using the command line argument -tao_cg_eta eta; where 0.1 is the default value.

This algorithm will be deprecated in the next version and replaced by the Bounded Nonlinear Conjugate Gradient (BNCG) algorithm that can solve both bound constrained and unconstrained problems.

The Nelder-Mead algorithm [NM65] is a direct search method for finding a local minimum of a function \(f(x)\). This algorithm does not require any gradient or Hessian information of \(f\) and therefore has some expected advantages and disadvantages compared to the other TAO solvers. The obvious advantage is that it is easier to write an application when no derivatives need to be calculated. The downside is that this algorithm can be slow to converge or can even stagnate, and it performs poorly for large numbers of variables.

This solver keeps a set of \(N+1\) sorted vectors \({x_1,x_2,\ldots,x_{N+1}}\) and their corresponding objective function values \(f_1 \leq f_2 \leq \ldots \leq f_{N+1}\). At each iteration, \(x_{N+1}\) is removed from the set and replaced with

where \(\mu\) can be one of \({\mu_0,2\mu_0,\frac{1}{2}\mu_0,-\frac{1}{2}\mu_0}\) depending on the values of each possible \(f(x(\mu))\).

The algorithm terminates when the residual \(f_{N+1} - f_1\) becomes sufficiently small. Because of the way new vectors can be added to the sorted set, the minimum function value and/or the residual may not be impacted at each iteration.

Two options can be set specifically for the Nelder-Mead algorithm:

sets the initial set of vectors (\(x_0\) plus value in each coordinate direction); the default value is \(1\).

sets the value of \(\mu_0\); the default is \(\mu_0=1\).

Bound-constrained optimization algorithms solve optimization problems of the form

These solvers use the bounds on the variables as well as objective function, gradient, and possibly Hessian information.

For any unbounded variables, the bound value for the associated index can be set to PETSC_INFINITY for the upper bound and PETSC_NINFINITY for the lower bound. If all bounds are set to infinity, then the bounded algorithms are equivalent to their unconstrained counterparts.

Before introducing specific methods, we will first define two projection operations used by all bound constrained algorithms.

TAO features three bounded Newton-Krylov (BNK) class of algorithms, separated by their globalization methods: projected line search (BNLS), trust region (BNTR), and trust region with a projected line search fall-back (BNTL). They are available via the TAO solvers TAOBNLS, TAOBNTR and TAOBNTL, respectively, or the -tao_type bnls/bntr/bntl flag.

The BNK class of methods use an active-set approach to solve the symmetric system of equations,

only for inactive variables in the interior of the bounds. The active-set estimation is based on Bertsekas [Ber82] with the following variable index categories:

At each iteration, the bound tolerance is estimated as \(\epsilon_{k+1} = \text{min}(\epsilon_k, ||w_k||_2)\) with \(w_k = x_k - \mathfrak{B}(x_k - \beta D_k g_k)\), where the diagonal matrix \(D_k\) is an approximation of the Hessian inverse \(H_k^{-1}\). The initial bound tolerance \(\epsilon_0\) and the step length \(\beta\) have default values of \(0.001\) and can be adjusted using -tao_bnk_as_tol and -tao_bnk_as_step flags, respectively. The active-set estimation can be disabled using the option -tao_bnk_as_type none, in which case the algorithm simply uses the current iterate with no bound tolerances to determine which variables are actively bounded and which are free.

BNK algorithms invert the reduced Hessian using a Krylov iterative method. Trust-region conjugate gradient methods (KSPNASH, KSPSTCG, and KSPGLTR) are required for the BNTR and BNTL algorithms, and recommended for the BNLS algorithm. The preconditioner type can be changed using the -tao_bnk_pc_type none/ilu/icc/jacobi/lmvm. The lmvm option, which is also the default, preconditions the Krylov solution with a MATLMVM matrix. The remaining supported preconditioner types are default PETSc types. If Jacobi is selected, the diagonal values are safeguarded to be positive. icc and ilu options produce good results for problems with dense Hessians. The LMVM and Jacobi preconditioners are also used as the approximate inverse-Hessian in the active-set estimation. If neither are available, or if the Hessian matrix does not have MATOP_GET_DIAGONAL defined, then the active-set estimation falls back onto using an identity matrix in place of \(D_k\) (this is equivalent to estimating the active-set using a gradient descent step).

A special option is available to accelerate the convergence of the BNK algorithms by taking a finite number of BNCG iterations at each Newton iteration. By default, the number of BNCG iterations is set to zero and the algorithms do not take any BNCG steps. This can be changed using the option flag -tao_bnk_max_cg_its its. While this reduces the number of Newton iterations, in practice it simply trades off the Hessian evaluations in the BNK solver for more function and gradient evaluations in the BNCG solver. However, it may be useful for certain types of problems where the Hessian evaluation is disproportionately more expensive than the objective function or its gradient.

BNLS safeguards the Newton step by falling back onto a BFGS, scaled gradient, or gradient steps based on descent direction verifications. For problems with indefinite Hessian matrices, the step direction is calculated using a perturbed system of equations,

where \(\rho_k\) is a dynamically adjusted positive constant. The step is globalized using a projected Moré-Thuente line search. If a trust-region conjugate gradient method is used for the Hessian inversion, the trust radius is modified based on the line search step length.

BNTR globalizes the Newton step using a trust region method based on the predicted versus actual reduction in the cost function. The trust radius is increased only if the accepted step is at the trust region boundary. The reduction check features a safeguard for numerical values below machine epsilon, scaled by the latest function value, where the full Newton step is accepted without modification.

BNTL safeguards the trust-region globalization such that a line search is used in the event that the step is initially rejected by the predicted versus actual decrease comparison. If the line search fails to find a viable step length for the Newton step, it falls back onto a scaled gradient or a gradient descent step. The trust radius is then modified based on the line search step length.

The BQNLS algorithm uses the BNLS infrastructure, but replaces the step calculation with a direct inverse application of the approximate Hessian based on quasi-Newton update formulas. No Krylov solver is used in the solution, and therefore the quasi-Newton method chosen must guarantee a positive-definite Hessian approximation. This algorithm is available via tao_type bqnls.

BQNK algorithms use the BNK infrastructure, but replace the exact Hessian with a quasi-Newton approximation. The matrix-free forward product operation based on quasi-Newton update formulas are used in conjunction with Krylov solvers to compute step directions. The quasi-Newton inverse application is used to precondition the Krylov solution, and typically helps converge to a step direction in \(\mathcal{O}(10)\) iterations. This approach is most useful with quasi-Newton update types such as Symmetric Rank-1 that cannot strictly guarantee positive-definiteness. The BNLS framework with Hessian shifting, or the BNTR framework with trust region safeguards, can successfully compensate for the Hessian approximation becoming indefinite.

Similar to the full Newton-Krylov counterpart, BQNK algorithms come in three forms separated by the globalization technique: line search (BQNKLS), trust region (BQNKTR) and trust region w/ line search fall-back (BQNKTL). These algorithms are available via tao_type (bqnkls|bqnktr|bqnktl).

BNCG extends the unconstrained nonlinear conjugate gradient algorithm to bound constraints via gradient projections and a bounded Moré-Thuente line search.

Like its unconstrained counterpart, BNCG offers gradient descent and a variety of CG updates: Fletcher-Reeves, Polak-Ribiére, Polak-Ribiére-Plus, Hestenes-Stiefel, Dai-Yuan, Hager-Zhang, Dai-Kou, Kou-Dai, and the Self-Scaling Memoryless (SSML) BFGS, DFP, and Broyden methods. These methods can be specified by using the command line argument -tao_bncg_type (gd|fr|pr|prp|hs|dy|hz|dk|kd|ssml_bfgs|ssml_dfp|ssml_brdn), respectively. The default value is ssml_bfgs. We have scalar preconditioning for these methods, and it is controlled by the flag tao_bncg_alpha. To disable rescaling, use \(\alpha = -1.0\), otherwise \(\alpha \in [0, 1]\). BNCG is available via the TAO solver TAOBNCG or the -tao_type bncg flag.

Some individual methods also contain their own parameters. The Hager-Zhang and Dou-Kai methods have a parameter that determines the minimum amount of contribution the previous search direction gives to the next search direction. The flags are -tao_bncg_hz_eta and -tao_bncg_dk_eta, and by default are set to \(0.4\) and \(0.5\) respectively. The Kou-Dai method has multiple parameters. -tao_bncg_zeta serves the same purpose as the previous two; set to \(0.1\) by default. There is also a parameter to scale the contribution of \(y_k \equiv \nabla f(x_k) - \nabla f(x_{k-1})\) in the search direction update. It is controlled by -tao_bncg_xi, and is equal to \(1.0\) by default. There are also times where we want to maximize the descent as measured by \(\nabla f(x_k)^T d_k\), and that may be done by using a negative value of \(\xi\); this achieves better performance when not using the diagonal preconditioner described next. This is enabled by default, and is controlled by -tao_bncg_neg_xi. Finally, the Broyden method has its convex combination parameter, set with -tao_bncg_theta. We have this as 1.0 by default, i.e. it is by default the BFGS method. One can also individually tweak the BFGS and DFP contributions using the multiplicative constants -tao_bncg_scale; both are set to \(1\) by default.

All methods can be scaled using the parameter -tao_bncg_alpha, which continuously varies in \([0, 1]\). The default value is set depending on the method from initial testing.

BNCG also offers a special type of method scaling. It employs Broyden diagonal scaling as an option for its CG methods, turned on with the flag -tao_bncg_diag_scaling. Formulations for both the forward (regular) and inverse Broyden methods are developed, controlled by the flag -tao_bncg_mat_lmvm_forward. It is set to True by default. Whether one uses the forward or inverse formulations depends on the method being used. For example, in our preliminary computations, the forward formulation works better for the SSML_BFGS method, but the inverse formulation works better for the Hestenes-Stiefel method. The convex combination parameter for the Broyden scaling is controlled by -tao_bncg_mat_lmvm_theta, and is 0 by default. We also employ rescaling of the Broyden diagonal, which aids the linesearch immensely. The rescaling parameter is controlled by -tao_bncg_mat_lmvm_alpha, and should be \(\in [0, 1]\). One can disable rescaling of the Broyden diagonal entirely by setting -tao_bncg_mat_lmvm_sigma_hist 0.

One can also supply their own preconditioner, serving as a Hessian initialization to the above diagonal scaling. The appropriate user function in the code is TaoBNCGSetH0(tao, H0) where H0 is the user-defined Mat object that serves as a preconditioner. For an example of similar usage, see tao/tutorials/ex3.c.

The active set estimation uses the Bertsekas-based method described in Bounded Newton-Krylov Methods, which can be deactivated using -tao_bncg_as_type none, in which case the algorithm will use the current iterate to determine the bounded variables with no tolerances and no look-ahead step. As in the BNK algorithm, the initial bound tolerance and estimator step length used in the Bertsekas method can be set via -tao_bncg_as_tol and -tao_bncg_as_step, respectively.

In addition to automatic scaled gradient descent restarts under certain local curvature conditions, we also employ restarts based on a check on descent direction such that \(\nabla f(x_k)^T d_k \in [-10^{11}, -10^{-9}]\). Furthermore, we allow for a variety of alternative restart strategies, all disabled by default. The -tao_bncg_unscaled_restart flag allows one to disable rescaling of the gradient for gradient descent steps. The -tao_bncg_spaced_restart flag tells the solver to restart every \(Mn\) iterations, where \(n\) is the problem dimension and \(M\) is a constant determined by -tao_bncg_min_restart_num and is 6 by default. We also have dynamic restart strategies based on checking if a function is locally quadratic; if so, go do a gradient descent step. The flag is -tao_bncg_dynamic_restart, disabled by default since the CG solver usually does better in those cases anyway. The minimum number of quadratic-like steps before a restart is set using -tao_bncg_min_quad and is 6 by default.

Constrained solvers solve optimization problems that incorporate either or both equality and inequality constraints, and may optionally include bounds on solution variables.

The TAOADMM algorithm is intended to blend the decomposability of dual ascent with the superior convergence properties of the method of multipliers. [BPC+11] The algorithm solves problems in the form

where \(x \in \mathbb R^n\), \(z \in \mathbb R^m\), \(A \in \mathbb R^{p \times n}\), \(B \in \mathbb R^{p \times m}\), and \(c \in \mathbb R^p\). Essentially, ADMM is a wrapper over two TAO solver, one for \(f(x)\), and one for \(g(z)\). With method of multipliers, one can form the augmented Lagrangian

Then, ADMM consists of the iterations

In certain formulation of ADMM, solution of \(z^{k+1}\) may have closed-form solution. Currently ADMM provides one default implementation for \(z^{k+1}\), which is soft-threshold. It can be used with either TaoADMMSetRegularizerType_ADMM() or -tao_admm_regularizer_type regularizer_soft_thresh. User can also pass spectral penalty value, \(\rho\), with either TaoADMMSetSpectralPenalty() or -tao_admm_spectral_penalty. Currently, user can use

TaoADMMSetMisfitObjectiveAndGradientRoutine()

TaoADMMSetRegularizerObjectiveAndGradientRoutine()

TaoADMMSetMisfitHessianRoutine()

TaoADMMSetRegularizerHessianRoutine()

Any other combination of routines is currently not supported. Hessian matrices can either be constant or non-constant, of which fact can be set via TaoADMMSetMisfitHessianChangeStatus(), and TaoADMMSetRegularizerHessianChangeStatus(). Also, it may appear in certain cases where augmented Lagrangian’s Hessian may become nearly singular depending on the \(\rho\), which may change in the case of -tao_admm_dual_update (update_basic|update_adaptive|update_adaptive_relaxed). This issue can be prevented by TaoADMMSetMinimumSpectralPenalty().

The TAOALMM method solves generally constrained problems of the form

where \(g(x)\) are equality constraints, \(h(x)\) are inequality constraints and \(l\) and \(u\) are lower and upper bounds on the optimization variables, respectively.

TAOALMM converts the above general constrained problem into a sequence of bound constrained problems at each outer iteration \(k = 1,2,\dots\)

where \(L(x, \lambda_k)\) is the augmented Lagrangian merit function and \(\lambda_k\) is the Lagrange multiplier estimates at outer iteration \(k\).

TAOALMM offers two versions of the augmented Lagrangian formulation: the canonical Hestenes-Powell augmented Lagrangian [Hes69] [Pow69] with inequality constrained converted to equality constraints via slack variables, and the slack-less Powell-Hestenes-Rockafellar formulation [Roc74] that utilizes a pointwise max() on the inequality constraints. For most applications, the canonical Hestenes-Powell formulation is likely to perform better. However, the PHR formulation may be desirable for problems featuring very large numbers of inequality constraints as it avoids inflating the dimension of the subproblem with slack variables.

The inner subproblem is solved using a nested bound-constrained first-order TAO solver. By default, TAOALM uses a quasi-Newton-Krylov trust-region method (TAOBQNKTR). Other first-order methods such as TAOBNCG and TAOBQNLS are also appropriate, but a trust-region globalization is strongly recommended for most applications.

The TAOPDIPM method (-tao_type pdipm) implements a primal-dual interior point method for solving general nonlinear programming problems of the form

Here, \(f(x)\) is the nonlinear objective function, \(g(x)\), \(h(x)\) are the equality and inequality constraints, and \(x^-\) and \(x^+\) are the lower and upper bounds on decision variables \(x\).

PDIPM converts the inequality constraints to equalities using slack variables \(z\) and a log-barrier term, which transforms (6) to

Here, \(ce(x)\) is set of equality constraints that include \(g(x)\) and fixed decision variables, i.e., \(x^- = x = x^+\). Similarly, \(ci(x)\) are inequality constraints including \(h(x)\) and lower/upper/box-constraints on \(x\). \(\mu\) is a parameter that is driven to zero as the optimization progresses.

The Lagrangian for (7)) is

where, \(\lambda_{ce}\) and \(\lambda_{ci}\) are the Lagrangian multipliers for the equality and inequality constraints, respectively.

The first order KKT conditions for optimality are as follows

(9) is solved iteratively using Newton’s method using PETSc’s SNES object. After each Newton iteration, a line-search is performed to update \(x\) and enforce \(z,\lambda_{ci} \geq 0\). The barrier parameter \(\mu\) is also updated after each Newton iteration. The Newton update is obtained by solving the second-order KKT system \(Hd = -\nabla L_{\mu}\). Here,\(H\) is the Hessian matrix of the KKT system. For interior-point methods such as PDIPM, the Hessian matrix tends to be ill-conditioned, thus necessitating the use of a direct solver. We recommend using LU preconditioner -pc_type lu and using direct linear solver packages such SuperLU_Dist or MUMPS.

TAO solves PDE-constrained optimization problems of the form

where the state variable \(u\) is the solution to the discretized partial differential equation defined by \(g\) and parametrized by the design variable \(v\), and \(f\) is an objective function. The Lagrange multipliers on the constraint are denoted by \(y\). This method is set by using the linearly constrained augmented Lagrangian TAO solver tao_lcl.

We make two main assumptions when solving these problems: the objective function and PDE constraints have been discretized so that we can treat the optimization problem as finite dimensional and \(\nabla_u g(u,v)\) is invertible for all \(u\) and \(v\).

Given the current iterate \((u_k, v_k, y_k)\), the linearly constrained augmented Lagrangian method approximately solves the optimization problem

where \(A_k = \nabla_u g(u_k,v_k)\), \(B_k = \nabla_v g(u_k,v_k)\), and \(g_k = g(u_k, v_k)\) and

is the augmented Lagrangian function. This optimization problem is solved in two stages. The first computes the Newton direction and finds a feasible point for the linear constraints. The second computes a reduced-space direction that maintains feasibility with respect to the linearized constraints and improves the augmented Lagrangian merit function.

The Newton direction is obtained by fixing the design variables at their current value and solving the linearized constraint for the state variables. In particular, we solve the system of equations

to obtain a direction \(du\). We need a direction that provides sufficient descent for the merit function

That is, we require \(g_k^T A_k du < 0\).

If the Newton direction is a descent direction, then we choose a penalty parameter \(\rho_k\) so that \(du\) is also a sufficient descent direction for the augmented Lagrangian merit function. We then find \(\alpha\) to approximately minimize the augmented Lagrangian merit function along the Newton direction.

We can enforce either the sufficient decrease condition or the Wolfe conditions during the search procedure. The new point,

satisfies the linear constraint

If the Newton direction computed does not provide descent for the merit function, then we can use the steepest descent direction \(du = -A_k^T g_k\) during the search procedure. However, the implication that the intermediate point approximately satisfies the linear constraint is no longer true.

We are now ready to compute a reduced-space step for the modified optimization problem:

We begin with the change of variables

and make the substitution

Hence, the unconstrained optimization problem we need to solve is

which is equivalent to

We apply one step of a limited-memory quasi-Newton method to this problem. The direction is obtain by solving the quadratic problem

where \(\tilde{H}_k\) is the limited-memory quasi-Newton approximation to the reduced Hessian matrix, a positive-definite matrix, and \(\tilde{g}_{k+\frac{1}{2}}\) is the reduced gradient.

The reduced gradient is obtained from one linearized adjoint solve

and some linear algebra

Because the Hessian approximation is positive definite and we know its inverse, we obtain the direction

and recover the full-space direction from one linearized forward solve,

Having the full-space direction, which satisfies the linear constraint, we now approximately minimize the augmented Lagrangian merit function along the direction.

We enforce the Wolfe conditions during the search procedure. The new point is

The reduced gradient at the new point is computed from

where \(c_{k+1} = \nabla_u \tilde{f}_k (u_{k+1},v_{k+1})\) and \(d_{k+1} = \nabla_v \tilde{f}_k (u_{k+1},v_{k+1})\). The multipliers \(y_{k+1}\) become the multipliers used in the next iteration of the code. The quantities \(v_{k+\frac{1}{2}}\), \(v_{k+1}\), \(\tilde{g}_{k+\frac{1}{2}}\), and \(\tilde{g}_{k+1}\) are used to update \(H_k\) to obtain the limited-memory quasi-Newton approximation to the reduced Hessian matrix used in the next iteration of the code. The update is skipped if it cannot be performed.

Given a function \(F: \mathbb R^n \to \mathbb R^m\), the nonlinear least-squares problem minimizes

The nonlinear equations \(F\) should be specified with the function TaoSetResidual().

The TAOBRGN algorithms is a Gauss-Newton method is used to iteratively solve nonlinear least squares problem with the iterations

where \(r(x)\) is the least-squares residual vector, \(J_k = \partial r(x_k)/\partial x\) is the Jacobian of the residual, and \(\alpha_k\) is the step length parameter. In other words, the Gauss-Newton method approximates the Hessian of the objective as \(H_k \approx (J_k^T J_k)\) and the gradient of the objective as \(g_k \approx -J_k r(x_k)\). The least-squares Jacobian, \(J\), should be provided to Tao using TaoSetJacobianResidual() routine.

The BRGN (-tao_type brgn) implementation adds a regularization term \(\beta(x)\) such that

where \(\lambda\) is the scalar weight of the regularizer. BRGN provides two default implementations for \(\beta(x)\):

L2-norm - \(\beta(x) = \frac{1}{2}||x_k||_2^2\)

L2-norm Proximal Point - \(\beta(x) = \frac{1}{2}||x_k - x_{k-1}||_2^2\)

L1-norm with Dictionary - \(\beta(x) = ||Dx||_1 \approx \sum_{i} \sqrt{y_i^2 + \epsilon^2}-\epsilon\) where \(y = Dx\) and \(\epsilon\) is the smooth approximation parameter.

The regularizer weight can be controlled with either TaoBRGNSetRegularizerWeight() or -tao_brgn_regularizer_weight command line option, while the smooth approximation parameter can be set with either TaoBRGNSetL1SmoothEpsilon() or -tao_brgn_l1_smooth_epsilon. For the L1-norm term, the user can supply a dictionary matrix with TaoBRGNSetDictionaryMatrix(). If no dictionary is provided, the dictionary is assumed to be an identity matrix and the regularizer reduces to a sparse solution term.

The regularization selection can be made using the command line option -tao_brgn_regularization_type (l2pure|l2prox|l1dict|user) where the user option allows the user to define a custom \(\mathcal{C}2\)-continuous regularization term. This custom term can be defined by using the interface functions:

TaoBRGNSetRegularizerObjectiveAndGradientRoutine() - Provide user-call back for evaluating the function value and gradient evaluation for the regularization term.

TaoBRGNSetRegularizerHessianRoutine() - Provide user call-back for evaluating the Hessian of the regularization term.

One algorithm for solving the least squares problem ((10)) when the Jacobian of the residual vector \(F\) is unavailable is the model-based POUNDERS (Practical Optimization Using No Derivatives for sums of Squares) algorithm (tao_pounders). POUNDERS employs a derivative-free trust-region framework as described in [CSV09] in order to converge to local minimizers. An example of this version of POUNDERS applied to a practical least-squares problem can be found in [KortelainenLesinskiMore+10].

In each iteration \(k\), the algorithm maintains a model \(m_k(x)\), described below, of the nonlinear least squares function \(f\) centered about the current iterate \(x_k\).

If one assumes that the maximum number of function evaluations has not been reached and that \(\|\nabla m_k(x_k)\|_2>\)gtol, the next point \(x_+\) to be evaluated is obtained by solving the trust-region subproblem

where \(\Delta_k\) is the current trust-region radius. By default we use a trust-region norm with \(p=\infty\) and solve ((11)) with the BLMVM method described in Bound-constrained Limited-Memory Variable-Metric Method (BLMVM). While the subproblem is a bound-constrained quadratic program, it may not be convex and the BQPIP and GPCG methods may not solve the subproblem. Therefore, a bounded Newton-Krylov Method should be used; the default is the BNTR algorithm. Note: BNTR uses its own internal trust region that may interfere with the infinity-norm trust region used in the model problem ((11)).

The residual vector is then evaluated to obtain \(F(x_+)\) and hence \(f(x_+)\). The ratio of actual decrease to predicted decrease,

as well as an indicator, valid, on the model’s quality of approximation on the trust region is then used to update the iterate,

and trust-region radius,

where \(0 < \eta_1 < 1\), \(0 < \gamma_0 < 1 < \gamma_1\), \(0<\omega_1<1\), and \(\Delta_{\max}\) are constants.

If \(\rho_k\leq 0\) and valid is false, the iterate and trust-region radius remain unchanged after the above updates, and the algorithm tests whether the direction \(x_+-x_k\) improves the model. If not, the algorithm performs an additional evaluation to obtain \(F(x_k+d_k)\), where \(d_k\) is a model-improving direction.

The iteration counter is then updated, and the next model \(m_{k}\) is obtained as described next.

In each iteration, POUNDERS uses a subset of the available evaluated residual vectors \(\{ F(y_1), F(y_2), \cdots \}\) to form an interpolatory quadratic model of each residual component. The \(m\) quadratic models

thus satisfy the interpolation conditions

on a common interpolation set \(\{y_1, \cdots , y_{l_k}\}\) of size \(l_k\in[n+1,\)npmax\(]\).

The gradients and Hessians of the models in (12) are then used to construct the main model,

The process of forming these models also computes the indicator valid of the model’s local quality.

POUNDERS supports the following parameters that can be set from the command line or PETSc options file:

The initial trust-region radius (\(>0\), real). This is used to determine the size of the initial neighborhood within which the algorithm should look.

The maximum number of interpolation points used (\(n+2\leq\) npmax \(\leq 0.5(n+1)(n+2)\)). This input is made available to advanced users. We recommend the default value (npmax\(=2n+1\)) be used by others.

Use the gqt algorithm to solve the subproblem ((11)) (uses \(p=2\)) instead of BQPIP.

If the default BQPIP algorithm is used to solve the subproblem ((11)), the parameters of the subproblem solver can be accessed using the command line options prefix -pounders_subsolver_. For example,

sets the gradient tolerance of the subproblem solver to \(10^{-5}\).

Additionally, the user provides an initial solution vector, a vector for storing the separable objective function, and a routine for evaluating the residual vector \(F\). These are described in detail in Objective Function and Gradient Routines and Nonlinear Least Squares. Here we remark that because gradient information is not available for scaling purposes, it can be useful to ensure that the problem is reasonably well scaled. A simple way to do so is to rescale the decision variables \(x\) so that their typical values are expected to lie within the unit hypercube \([0,1]^n\).

Because the gradient function is not provided to POUNDERS, the norm of the gradient of the objective function is not available. Therefore, for convergence criteria, this norm is approximated by the norm of the model gradient and used only when the model gradient is deemed to be a reasonable approximation of the gradient of the objective. In practice, the typical grounds for termination for expensive derivative-free problems is the maximum number of function evaluations allowed.

Mixed complementarity problems, or box-constrained variational inequalities, are related to nonlinear systems of equations. They are defined by a continuously differentiable function, \(F:\mathbb R^n \to \mathbb R^n\), and bounds, \(\ell \in \{\mathbb R\cup \{-\infty\}\}^n\) and \(u \in \{\mathbb R\cup \{\infty\}\}^n\), on the variables such that \(\ell \leq u\). Given this information, \(\mathbf{x}^* \in [\ell,u]\) is a solution to MCP(\(F\), \(\ell\), \(u\)) if for each \(i \in \{1, \ldots, n\}\) we have at least one of the following:

Note that when \(\ell = \{-\infty\}^n\) and \(u = \{\infty\}^n\), we have a nonlinear system of equations, and \(\ell = \{0\}^n\) and \(u = \{\infty\}^n\) correspond to the nonlinear complementarity problem [Cot64].

Simple complementarity conditions arise from the first-order optimality conditions from optimization [Kar39] [KT51]. In the simple bound-constrained optimization case, these conditions correspond to MCP(\(\nabla f\), \(\ell\), \(u\)), where \(f: \mathbb R^n \to \mathbb R\) is the objective function. In a one-dimensional setting these conditions are intuitive. If the solution is at the lower bound, then the function must be increasing and \(\nabla f \geq 0\). If the solution is at the upper bound, then the function must be decreasing and \(\nabla f \leq 0\). If the solution is strictly between the bounds, we must be at a stationary point and \(\nabla f = 0\). Other complementarity problems arise in economics and engineering [FP97], game theory [Nas50], and finance [HP98].

Evaluation routines for \(F\) and its Jacobian must be supplied prior to solving the application. The bounds, \([\ell,u]\), on the variables must also be provided. If no starting point is supplied, a default starting point of all zeros is used.

TAO has two implementations of semismooth algorithms [MFF+01] [DeLucaFK96] [FFK97] for solving mixed complementarity problems. Both are based on a reformulation of the mixed complementarity problem as a nonsmooth system of equations using the Fischer-Burmeister function [Fis92]. A nonsmooth Newton method is applied to the reformulated system to calculate a solution. The theoretical properties of such methods are detailed in the aforementioned references.

The Fischer-Burmeister function, \(\phi:\mathbb R^2 \to \mathbb R\), is defined as

This function has the following key property,

used when reformulating the mixed complementarity problem as the system of equations \(\Phi(x) = 0\), where \(\Phi:\mathbb R^n \to \mathbb R^n\). The reformulation is defined componentwise as

We note that \(\Phi\) is not differentiable everywhere but satisfies a semismoothness property [Mif77] [Qi93] [QS93]. Furthermore, the natural merit function, \(\Psi(x) := \frac{1}{2} \| \Phi(x) \|_2^2\), is continuously differentiable.

The two semismooth TAO solvers both solve the system \(\Phi(x) = 0\) by applying a nonsmooth Newton method with a line search. We calculate a direction, \(d^k\), by solving the system \(H^kd^k = -\Phi(x^k)\), where \(H^k\) is an element of the \(B\)-subdifferential [QS93] of \(\Phi\) at \(x^k\). If the direction calculated does not satisfy a suitable descent condition, then we use the negative gradient of the merit function, \(-\nabla \Psi(x^k)\), as the search direction. A standard Armijo search [Arm66] is used to find the new iteration. Nonmonotone searches [GLL86] are also available by setting appropriate runtime options. See Line Searches for further details.

The first semismooth algorithm available in TAO is not guaranteed to remain feasible with respect to the bounds, \([\ell, u]\), and is termed an infeasible semismooth method. This method can be specified by using the tao_ssils solver. In this case, the descent test used is that

Both \(\delta > 0\) and \(\rho > 2\) can be modified by using the runtime options -tao_ssils_delta delta and -tao_ssils_rho rho, respectively. By default, \(\delta = 10^{-10}\) and \(\rho = 2.1\).

An alternative is to remain feasible with respect to the bounds by using a projected Armijo line search. This method can be specified by using the tao_ssfls solver. The descent test used is the same as above where the direction in this case corresponds to the first part of the piecewise linear arc searched by the projected line search. Both \(\delta > 0\) and \(\rho > 2\) can be modified by using the runtime options -tao_ssfls_delta delta and -tao_ssfls_rho rho respectively. By default, \(\delta = 10^{-10}\) and \(\rho = 2.1\).

The recommended algorithm is the infeasible semismooth method, tao_ssils, because of its strong global and local convergence properties. However, if it is known that \(F\) is not defined outside of the box, \([\ell,u]\), perhaps because of the presence of \(\log\) functions, the feasibility-enforcing version of the algorithm, tao_ssfls, is a reasonable alternative.

TAO also contained two active-set semismooth methods for solving complementarity problems. These methods solve a reduced system constructed by block elimination of active constraints. The subdifferential in these cases enables this block elimination.

The first active-set semismooth algorithm available in TAO is not guaranteed to remain feasible with respect to the bounds, \([\ell, u]\), and is termed an infeasible active-set semismooth method. This method can be specified by using the tao_asils solver.

An alternative is to remain feasible with respect to the bounds by using a projected Armijo line search. This method can be specified by using the tao_asfls solver.

Quadratic solvers solve optimization problems of the form

where the gradient and the Hessian of the objective are both constant.

The GPCG [MoreT91] algorithm is much like the TRON algorithm, discussed in Section Trust-Region Newton Method (TRON), except that it assumes that the objective function is quadratic and convex. Therefore, it evaluates the function, gradient, and Hessian only once. Since the objective function is quadratic, the algorithm does not use a trust region. All the options that apply to TRON except for trust-region options also apply to GPCG. It can be set by using the TAO solver tao_gpcg or via the optio flag -tao_type gpcg.

The BQPIP algorithm is an interior-point method for bound constrained quadratic optimization. It can be set by using the TAO solver of tao_bqpip or via the option flag -tao_type bgpip. Since it assumes the objective function is quadratic, it evaluates the function, gradient, and Hessian only once. This method also requires the solution of systems of linear equations, whose solver can be accessed and modified with the command TaoGetKSP().

BMRM is a numerical approach to optimizing an unconstrained objective in the form of \(f(x) + 0.5 * \lambda \| x \|^2\). Here \(f\) is a convex function that is finite on the whole space. \(\lambda\) is a positive weight parameter, and \(\| x \|\) is the Euclidean norm of \(x\). The algorithm only requires a routine which, given an \(x\), returns the value of \(f(x)\) and the gradient of \(f\) at \(x\).

OWLQN [AG07] is a numerical approach to optimizing an unconstrained objective in the form of \(f(x) + \lambda \|x\|_1\). Here f is a convex and differentiable function, \(\lambda\) is a positive weight parameter, and \(\| x \|_1\) is the \(\ell_1\) norm of \(x\): \(\sum_i |x_i|\). The algorithm only requires evaluating the value of \(f\) and its gradient.

The TRON [LMore99] algorithm is an active-set method that uses a combination of gradient projections and a preconditioned conjugate gradient method to minimize an objective function. Each iteration of the TRON algorithm requires function, gradient, and Hessian evaluations. In each iteration, the algorithm first applies several conjugate gradient iterations. After these iterates, the TRON solver momentarily ignores the variables that equal one of its bounds and applies a preconditioned conjugate gradient method to a quadratic model of the remaining set of free variables.

The TRON algorithm solves a reduced linear system defined by the rows and columns corresponding to the variables that lie between the upper and lower bounds. The TRON algorithm applies a trust region to the conjugate gradients to ensure convergence. The initial trust-region radius can be set by using the command TaoSetInitialTrustRegionRadius(), and the current trust region size can be found by using the command TaoGetCurrentTrustRegionRadius(). The initial trust region can significantly alter the rate of convergence for the algorithm and should be tuned and adjusted for optimal performance.

This algorithm will be deprecated in the next version in favor of the Bounded Newton Trust Region (BNTR) algorithm.

BLMVM is a limited-memory, variable-metric method and is the bound-constrained variant of the LMVM method for unconstrained optimization. It uses projected gradients to approximate the Hessian, eliminating the need for Hessian evaluations. The method can be set by using the TAO solver tao_blmvm. For more details, please see the LMVM section in the unconstrained algorithms as well as the LMVM matrix documentation in the PETSc manual.

This algorithm will be deprecated in the next version in favor of the Bounded Quasi-Newton Line Search (BQNLS) algorithm.

This section discusses options and routines that apply to most TAO solvers and problem classes. In particular, we focus on linear solvers, convergence tests, and line searches.

One of the most computationally intensive phases of many optimization algorithms involves the solution of linear systems of equations. The performance of the linear solver may be critical to an efficient computation of the solution. Since linear equation solvers often have a wide variety of options associated with them, TAO allows the user to access the linear solver with the

command. With access to the KSP object, users can customize it for their application to achieve improved performance. Additional details on the KSP options in PETSc can be found in the User-Guide.

By default the TAO solvers run silently without displaying information about the iterations. The user can initiate monitoring with the command

The routine mon indicates a user-defined monitoring routine, and void* denotes an optional user-defined context for private data for the monitor routine.

The routine set by TaoMonitorSet() is called once during each iteration of the optimization solver. Hence, the user can employ this routine for any application-specific computations that should be done after the solution update.

Convergence of a solver can be defined in many ways. The methods TAO uses by default are mentioned in Convergence. These methods include absolute and relative convergence tolerances as well as a maximum number of iterations of function evaluations. If these choices are not sufficient, the user can specify a customized test

Users can set their own customized convergence tests of the form

The second argument is a pointer to a structure defined by the user. Within this routine, the solver can be queried for the solution vector, gradient vector, or other statistic at the current iteration through routines such as TaoGetSolutionStatus() and TaoGetTolerances().

To use this convergence test within a TAO solver, one uses the command

The second argument of this command is the convergence routine, and the final argument of the convergence test routine denotes an optional user-defined context for private data. The convergence routine receives the TAO solver and this private data structure. The termination flag can be set by using the routine

By using the command line option -tao_ls_type. Available line searches include Moré-Thuente [MoreT92], Armijo, gpcg, and unit.

The line search routines involve several parameters, which are set to defaults that are reasonable for many applications. The user can override the defaults by using the following options

-tao_ls_max_funcs max

One should run a TAO program with the option -help for details. Users may write their own customized line search codes by modeling them after one of the defaults provided.

Some TAO algorithms can re-use information accumulated in the previous TaoSolve() call to hot-start the new solution. This can be enabled using the -tao_recycle_history flag, or in code via the TaoSetRecycleHistory() interface.

For the nonlinear conjugate gradient solver (TAOBNCG), this option re-uses the latest search direction from the previous TaoSolve() call to compute the initial search direction of a new TaoSolve(). By default, the feature is disabled and the algorithm sets the initial direction as the negative gradient.

For the quasi-Newton family of methods (TAOBQNLS, TAOBQNKLS, TAOBQNKTR, TAOBQNKTL), this option re-uses the accumulated quasi-Newton Hessian approximation from the previous TaoSolve() call. By default, the feature is disabled and the algorithm will reset the quasi-Newton approximation to the identity matrix at the beginning of every new TaoSolve().

The option flag has no effect on other TAO solvers.

One of the strengths of both TAO and PETSc is the ability to allow users to extend the built-in solvers with new user-defined algorithms. It is certainly possible to develop new optimization algorithms outside of TAO framework, but Using TAO to implement a solver has many advantages,

TAO includes other optimization solvers with an identical interface, so application problems may conveniently switch solvers to compare their effectiveness.

TAO provides support for function evaluations and derivative information. It allows for the direct evaluation of this information by the application developer, contains limited support for finite difference approximations, and allows the uses of matrix-free methods. The solvers can obtain this function and derivative information through a simple interface while the details of its computation are handled within the toolkit.

TAO provides line searches, convergence tests, monitoring routines, and other tools that are helpful in an optimization algorithm. The availability of these tools means that the developers of the optimization solver do not have to write these utilities.

PETSc offers vectors, matrices, index sets, and linear solvers that can be used by the solver. These objects are standard mathematical constructions that have many different implementations. The objects may be distributed over multiple processors, restricted to a single processor, have a dense representation, use a sparse data structure, or vary in many other ways. TAO solvers do not need to know how these objects are represented or how the operations defined on them have been implemented. Instead, the solvers apply these operations through an abstract interface that leaves the details to PETSc and external libraries. This abstraction allows solvers to work seamlessly with a variety of data structures while allowing application developers to select data structures tailored for their purposes.

PETSc provides the user a convenient method for setting options at runtime, performance profiling, and debugging.

TAO solver implementation files must include the TAO implementation file taoimpl.h:

This file contains data elements that are generally kept hidden from application programmers, but may be necessary for solver implementations to access.

TAO solvers must be written in C or C++ and include several routines with a particular calling sequence. Two of these routines are mandatory: one that initializes the TAO structure with the appropriate information and one that applies the algorithm to a problem instance. Additional routines may be written to set options within the solver, view the solver, setup appropriate data structures, and destroy these data structures. In order to implement the conjugate gradient algorithm, for example, the following structure is useful.

This structure contains two parameters, two counters, and two work vectors. Vectors for the solution and gradient are not needed here because the TAO structure has pointers to them.

All TAO solvers have a routine that accepts a TAO structure and computes a solution. TAO will call this routine when the application program uses the routine TaoSolve() and will pass to the solver information about the objective function and constraints, pointers to the variable vector and gradient vector, and support for line searches, linear solvers, and convergence monitoring. As an example, consider the following code that solves an unconstrained minimization problem using the conjugate gradient method.

The first line of this routine casts the second argument to a pointer to a TAO_CG data structure. This structure contains pointers to three vectors and a scalar that will be needed in the algorithm.

After declaring an initializing several variables, the solver lets TAO evaluate the function and gradient at the current point in the using the routine TaoComputeObjectiveAndGradient(). Other routines may be used to evaluate the Hessian matrix or evaluate constraints. TAO may obtain this information using direct evaluation or other means, but these details do not affect our implementation of the algorithm.

The norm of the gradient is a standard measure used by unconstrained minimization solvers to define convergence. This quantity is always nonnegative and equals zero at the solution. The solver will pass this quantity, the current function value, the current iteration number, and a measure of infeasibility to TAO with the routine

Most optimization algorithms are iterative, and solvers should include this command somewhere in each iteration. This routine records this information, and applies any monitoring routines and convergence tests set by default or the user. In this routine, the second argument is the current iteration number, and the third argument is the current function value. The fourth argument is a nonnegative error measure associated with the distance between the current solution and the optimal solution. Examples of this measure are the norm of the gradient or the square root of a duality gap. The fifth argument is a nonnegative error that usually represents a measure of the infeasibility such as the norm of the constraints or violation of bounds. This number should be zero for unconstrained solvers. The sixth argument is a nonnegative steplength, or the multiple of the step direction added to the previous iterate. The results of the convergence test are returned in the last argument. If the termination reason is TAO_CONTINUE_ITERATING, the algorithm should continue.

After this monitoring routine, the solver computes a step direction using the conjugate gradient algorithm and computations using Vec objects. These methods include adding vectors together and computing an inner product. A full list of these methods can be found in the manual pages.

Nonlinear conjugate gradient algorithms also require a line search. TAO provides several line searches and support for using them. The routine

passes the current solution, gradient, and objective value to the line search and returns a new solution, gradient, and objective value. More details on line searches can be found in Line Searches. The details of the line search applied are specified elsewhere, when the line search is created.

TAO also includes support for linear solvers using PETSc KSP objects. Although this algorithm does not require one, linear solvers are an important part of many algorithms. Details on the use of these solvers can be found in the PETSc users manual.

The TAO solver is initialized for a particular algorithm in a separate routine. This routine sets default convergence tolerances, creates a line search or linear solver if needed, and creates structures needed by this solver. For example, the routine that creates the nonlinear conjugate gradient algorithm shown above can be implemented as follows.

This routine declares some variables and then allocates memory for the TAO_CG data structure. Notice that the Tao object now has a pointer to this data structure (tao->data) so it can be accessed by the other functions written for this solver implementation.

This routine also sets some default parameters particular to the conjugate gradient algorithm, sets default convergence tolerances, and creates a particular line search. These defaults could be specified in the routine that solves the problem, but specifying them here gives the user the opportunity to modify these parameters either by using direct calls setting parameters or by using options.

Finally, this solver passes to TAO the names of all the other routines used by the solver.

Note that the lines EXTERN_C_BEGIN and EXTERN_C_END surround this routine. These macros are required to preserve the name of this function without any name-mangling from the C++ compiler (if used).

Another routine needed by most solvers destroys the data structures created by earlier routines. For the nonlinear conjugate gradient method discussed earlier, the following routine destroys the two work vectors and the TAO_CG structure.

This routine is called from within the TaoDestroy() routine. Only algorithm-specific data objects are destroyed in this routine; any objects indexed by TAO (tao->linesearch, tao->ksp, tao->gradient, etc.) will be destroyed by TAO immediately after the algorithm-specific destroy routine completes.

If the SetUp routine has been set by the initialization routine, TAO will call it during the execution of TaoSolve(). While this routine is optional, it is often provided to allocate the gradient vector, work vectors, and other data structures required by the solver. It should have the following form.

The SetFromOptions routine should be used to check for any algorithm-specific options set by the user and will be called when the application makes a call to TaoSetFromOptions(). It should have the following form.

The View routine should be used to output any algorithm-specific information or statistics at the end of a solve. This routine will be called when the application makes a call to TaoView() or when the command line option -tao_view is used. It should have the following form.

Once a new solver is implemented, TAO needs to know the name of the solver and what function to use to create the solver. To this end, one can use the routine

where name is the name of the solver (i.e., tao_blmvm), path is the path to the library containing the solver, cname is the name of the routine that creates the solver (in our case, TaoCreate_CG), and create is a pointer to that creation routine. If one is using dynamic loading, then the fourth argument will be ignored.

Once the solver has been registered, the new solver can be selected either by using the TaoSetType() function or by using the -tao_type command line option.

Galen Andrew and Jianfeng Gao. Scalable training of l1-regularized log-linear models. In Proceedings of the 24th international conference on Machine learning (ICML), 33–40. 2007.

L. Armijo. Minimization of functions having Lipschitz-continuous first partial derivatives. Pacific Journal of Mathematics, 16:1–3, 1966.

Dimitri P. Bertsekas. Projected Newton methods for optimization problems with simple constraints. SIAM Journal on Control and Optimization, 20:221–246, 1982.

Stephen Boyd, Neal Parikh, Eric Chu, Borja Peleato, Jonathan Eckstein, and others. Distributed optimization and statistical learning via the alternating direction method of multipliers. Foundations and Trends® in Machine learning, 3(1):1–122, 2011.

A. R. Conn, N. I. M. Gould, and Ph. L. Toint. Trust-Region Methods. SIAM, Philadelphia, Pennsylvania, 2000.

Andrew R. Conn, Katya Scheinberg, and Luís N. Vicente. Introduction to Derivative-Free Optimization. MPS/SIAM Series on Optimization. Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 2009. ISBN 0-89871-460-5.

R. W. Cottle. Nonlinear programs with positively bounded Jacobians. PhD thesis, Department of Mathematics, University of California, Berkeley, California, 1964.

Francisco Facchinei, Andreas Fischer, and Christian Kanzow. A semismooth Newton method for variational inequalities: The case of box constraints. Complementarity and Variational Problems: State of the Art, 92:76, 1997.

M. C. Ferris and J. S. Pang. Engineering and economic applications of complementarity problems. SIAM Review, 39:669–713, 1997. URL: http: //www.siam.org/journals/sirev/39-4/28596.html.

A. Fischer. A special Newton–type optimization method. Optimization, 24:269–284, 1992.

L. Grippo, F. Lampariello, and S. Lucidi. A nonmonotone line search technique for Newton's method. SIAM Journal on Numerical Analysis, 23:707–716, 1986.

Magnus R Hestenes. Multiplier and gradient methods. Journal of optimization theory and applications, 4(5):303–320, 1969.

J. Huang and J. S. Pang. Option pricing and linear complementarity. Journal of Computational Finance, 2:31–60, 1998.

W. Karush. Minima of functions of several variables with inequalities as side conditions. Master's thesis, Department of Mathematics, University of Chicago, 1939.

H. W. Kuhn and A. W. Tucker. Nonlinear programming. In J. Neyman, editor, Proceedings of the Second Berkeley Symposium on Mathematical Statistics and Probability, pages 481–492. University of California Press, Berkeley and Los Angeles, 1951.

C.-J. Lin and J. J. Moré. Newton's method for large bound-constrained optimization problems. SIOPT, 9(4):1100–1127, 1999. URL: http://www.mcs.anl.gov/home/more/papers/nb.ps.gz.

R. Mifflin. Semismooth and semiconvex functions in constrained optimization. SIAM Journal on Control and Optimization, 15:957–972, 1977.

Jorge J. Moré and G. Toraldo. On the solution of large quadratic programming problems with bound constraints. SIOPT, 1:93–113, 1991.

Jorge J. Moré and David Thuente. Line search algorithms with guaranteed sufficient decrease. Technical Report MCS-P330-1092, Mathematics and Computer Science Division, Argonne National Laboratory, 1992.

T. S. Munson, F. Facchinei, M. C. Ferris, A. Fischer, and C. Kanzow. The semismooth algorithm for large scale complementarity problems. INFORMS Journal on Computing, 2001.

J. F. Nash. Equilibrium points in N–person games. Proceedings of the National Academy of Sciences, 36:48–49, 1950.

J. A. Nelder and R. Mead. A simplex method for function minimization. Computer Journal, 7:308–313, 1965.

Jorge Nocedal and Stephen Wright. Numerical optimization. Springer Science & Business Media, 2006.

Michael JD Powell. A method for nonlinear constraints in minimization problems. Optimization, pages 283–298, 1969.

L. Qi. Convergence analysis of some algorithms for solving nonsmooth equations. Mathematics of Operations Research, 18:227–244, 1993.

L. Qi and J. Sun. A nonsmooth version of Newton's method. Mathematical Programming, 58:353–368, 1993.

R Tyrrell Rockafellar. Augmented lagrange multiplier functions and duality in nonconvex programming. SIAM Journal on Control, 12(2):268–285, 1974.

T. De Luca, F. Facchinei, and C. Kanzow. A semismooth equation approach to the solution of nonlinear complementarity problems. Mathematical Programming, 75:407–439, 1996.

M. Kortelainen, T. Lesinski, J. Moré, W. Nazarewicz, J. Sarich, N. Schunck, M. V. Stoitsov, and S. M. Wild. Nuclear energy density optimization. Physical Review C, 82(2):024313, 2010. doi:10.1103/PhysRevC.82.024313.

For more on MPI and PETSc, see Running PETSc Programs.

TS: Scalable ODE and DAE Solvers

PetscRegressor: Regression Solvers

**Examples:**

Example 1 (unknown):
```unknown
FormFunctionGradient
```

Example 2 (unknown):
```unknown
FormHessian
```

Example 3 (unknown):
```unknown
src/tao/unconstrained/tutorials/rosenbrock1.c
```

Example 4 (cpp):
```cpp
#include <petsctao.h>
typedef struct {
  MPI_Comm  comm;
  PetscInt  n;         /* dimension */
  PetscReal alpha;     /* condition parameter */
  PetscBool chained;   /* chained vs. unchained Rosenbrock function */
  PetscBool test;      /* run tests in AppCtxFinalize() */
  PetscBool jacobi_pc; /* Create Jacobi Hpre */
  PetscBool use_fd;    /* Use finite difference for grad and hess */
} AppCtx;

static PetscErrorCode AppCtxInitialize(MPI_Comm, AppCtx *); /* process options */
static PetscErrorCode AppCtxFinalize(AppCtx *, Tao);        /* clean up and optionally run tests */
static PetscErrorCode AppCtxCreateSolution(AppCtx *, Vec *);
static PetscErrorCode AppCtxCreateHessianMatrices(AppCtx *, Mat *, Mat *);
```

---

## VecFischer#

**URL:** https://petsc.org/release/manualpages/Tao/VecFischer/

**Contents:**
- VecFischer#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Evaluates the Fischer-Burmeister function for complementarity problems.

F - function evaluated at x

FB - The Fischer-Burmeister function vector

The Fischer-Burmeister function is defined as

and is used reformulate a complementarity problem as a semismooth system of equations.

The result of this function is done by cases:

l[i] == - infinity, u[i] == infinity – fb[i] = -f[i]

l[i] == - infinity, u[i] finite – fb[i] = phi(u[i]-x[i], -f[i])

l[i] finite, u[i] == infinity - - fb[i] = phi(x[i]-l[i], f[i])

l[i] finite < u[i] finite - - fb[i] = phi(x[i]-l[i], phi(u[i]-x[i], -f[u]))

otherwise l[i] == u[i] - - fb[i] = l[i] - x[i]

Vec, VecSFischer(), MatDFischer(), MatDSFischer()

src/tao/util/tao_util.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode VecFischer(Vec X, Vec F, Vec L, Vec U, Vec FB)
```

Example 2 (unknown):
```unknown
VecSFischer()
```

Example 3 (unknown):
```unknown
MatDFischer()
```

Example 4 (unknown):
```unknown
MatDSFischer()
```

---

## VecNestGetTaoTermSumParameters#

**URL:** https://petsc.org/release/manualpages/TaoTerm/VecNestGetTaoTermSumParameters/

**Contents:**
- VecNestGetTaoTermSumParameters#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Note#
- See Also#
- Level#
- Location#
- Examples#

A wrapper around VecNestGetSubVec() for TAOTERMSUM.

params - a VECNEST that has one nested vector for each term of a TAOTERMSUM

index - the index of a term

subparams - the parameters of the internal terms of TAOTERMSUM. (may be NULL)

VecNestGetSubVec() cannot return NULL for the subvec. If params was created by TaoTermSumParametersPack(), then any NULL subvecs that were passed to that function will be returned NULL by this function.

TaoTerm: composable objective function terms, TaoTerm, TAOTERMSUM, TaoTermSumParametersPack(), TaoTermSumParametersUnpack(), VECNEST, VecNestGetSubVec()

src/tao/term/impls/sum/taotermsum.c

src/tao/unconstrained/tutorials/elastic_net_regularization.c

Index of all TaoTerm routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
VecNestGetSubVec()
```

Example 2 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode VecNestGetTaoTermSumParameters(Vec params, PetscInt index, Vec *subparams)
```

Example 3 (unknown):
```unknown
VecNestGetSubVec()
```

Example 4 (unknown):
```unknown
TaoTermSumParametersPack()
```

---

## VecSFischer#

**URL:** https://petsc.org/release/manualpages/Tao/VecSFischer/

**Contents:**
- VecSFischer#
- Synopsis#
- Input Parameters#
- Output Parameter#
- Notes#
- See Also#
- Level#
- Location#

Evaluates the Smoothed Fischer-Burmeister function for complementarity problems.

F - function evaluated at x

mu - smoothing parameter

FB - The Smoothed Fischer-Burmeister function vector

The Smoothed Fischer-Burmeister function is defined as

and is used reformulate a complementarity problem as a semismooth system of equations.

The result of this function is done by cases:

l[i] == - infinity, u[i] == infinity – fb[i] = -f[i] - 2mux[i]

l[i] == - infinity, u[i] finite – fb[i] = phi(u[i]-x[i], -f[i], mu)

l[i] finite, u[i] == infinity - - fb[i] = phi(x[i]-l[i], f[i], mu)

l[i] finite < u[i] finite - - fb[i] = phi(x[i]-l[i], phi(u[i]-x[i], -f[u], mu), mu)

otherwise l[i] == u[i] - - fb[i] = l[i] - x[i]

Vec, VecFischer(), MatDFischer(), MatDSFischer()

src/tao/util/tao_util.c

Index of all Tao routines Table of Contents for all manual pages Index of all manual pages

**Examples:**

Example 1 (unknown):
```unknown
#include "petsctao.h" 
PetscErrorCode VecSFischer(Vec X, Vec F, Vec L, Vec U, PetscReal mu, Vec FB)
```

Example 2 (go):
```go
phi(a,b) := sqrt(a*a + b*b + 2*mu*mu) - a - b
```

Example 3 (unknown):
```unknown
VecFischer()
```

Example 4 (unknown):
```unknown
MatDFischer()
```

---
